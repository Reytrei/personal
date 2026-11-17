"""Sesiones de Claude Code en ~/personal de un día, y si dejaron su estado en Notion.

Uso: python3 -I sesiones.py [AAAA-MM-DD] [--exclude <prefijo de session id>]
Fecha por defecto: hoy (hora local).

Por sesión: nombre (título de /rename, si no el automático), ID, inicio y fin, cómo empezó, cantidad de prompts,
las tareas de Notion que nombró (URL o id de página en sus prompts) y la línea "Estado":
- "none": nunca actualizó el "## Estado" de una página de Notion (skill handoff).
- "current": lo actualizó y no hubo prompts después.
- "stale": lo actualizó, pero la sesión siguió después.
Al final, cómo terminó (su último mensaje). Saltea las sesiones que empiezan con /daily o /end-of-day. Solo lectura.
"""
import datetime as dt
import glob
import json
import os
import re
import sys

ROOT = os.path.expanduser("~/.claude-personal/projects")
SKIP_FIRST = ("/daily", "/end-of-day")
NOTION_ID = re.compile(r"(?:notion\.(?:so|com)/(?:p/)?(?:[^\s)\"'`]*-)?)([0-9a-f]{32})")


def text_of(content):
    if isinstance(content, str):
        return content
    return " ".join(b.get("text", "") for b in content if b.get("type") == "text")


def norm(pid):
    return pid.replace("-", "").lower()


def digest(path):
    first = last = start = last_prompt = None
    custom = auto = None
    prompts = 0
    last_text = ""
    tasks = []  # Notion page ids named in prompts, in order
    estado = {}  # page id -> last "## Estado" update timestamp
    for line in open(path):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        if d.get("type") == "custom-title" and d.get("customTitle"):
            custom = d["customTitle"]
        if d.get("type") == "ai-title" and d.get("aiTitle"):
            auto = d["aiTitle"]
        if d.get("isSidechain"):
            continue
        ts = d.get("timestamp")
        if ts:
            start = start or ts
            last = ts
        if d.get("type") == "user" and not d.get("isMeta"):
            t = text_of(d["message"]["content"]).strip()
            if not t or t.startswith("<local-command") or "[Request interrupted" in t:
                continue
            m = re.search(r"<command-name>(.*?)</command-name>.*?(?:<command-args>(.*?)</command-args>)?", t, re.S)
            if m:
                t = f"{m.group(1)} {m.group(2) or ''}".strip()
            elif t.startswith("<"):
                continue
            prompts += 1
            last_prompt = ts or last_prompt
            first = first or t
            for pid in NOTION_ID.findall(t):
                if pid not in tasks:
                    tasks.append(pid)
        if d.get("type") == "assistant":
            for b in d["message"].get("content", []):
                if b.get("type") != "tool_use" or "notion-update-page" not in b.get("name", ""):
                    continue
                inp = b.get("input") or {}
                if "## Estado" in json.dumps(inp, ensure_ascii=False):
                    pid = norm(str(inp.get("page_id", "")))[-32:]
                    estado[pid] = ts
            t = text_of(d["message"].get("content", [])).strip()
            if t:
                last_text = t
    return start, last, first, prompts, last_text[-1200:], custom or auto or "(sin título)", last_prompt, tasks, estado


def estado_line(last_prompt, estado):
    if not estado:
        return "Estado: none"
    pid, when = max(estado.items(), key=lambda kv: kv[1] or "")
    state = "stale (siguió después)" if last_prompt and when and last_prompt[:19] > when[:19] else "current"
    return f"Estado: {state} · página {pid} · escrito {str(when)[:16]} UTC"


def main():
    args = sys.argv[1:]
    exclude = None
    if "--exclude" in args:
        i = args.index("--exclude")
        exclude = args[i + 1]
        del args[i : i + 2]
    day = dt.date.fromisoformat(args[0]) if args else dt.date.today()
    lo = dt.datetime.combine(day, dt.time()).timestamp()
    hi = lo + 86400
    files = [
        f
        for f in glob.glob(os.path.join(ROOT, "-Users-*-personal", "*.jsonl"))
        if lo <= os.path.getmtime(f) and not (exclude and os.path.basename(f).startswith(exclude))
    ]
    shown = 0
    out = []
    for f in sorted(files, key=os.path.getmtime):
        start, end, first, prompts, ending, title, last_prompt, tasks, estado = digest(f)
        if not prompts or first.startswith(SKIP_FIRST):
            continue
        if start and dt.datetime.fromisoformat(start.replace("Z", "+00:00")).timestamp() >= hi:
            continue  # empezó otro día, después del pedido
        shown += 1
        full_id = os.path.basename(f)[:-6]
        out.append(f'## "{title}" · {full_id[:8]} · {start[:16]} → {end[:16]} UTC · {prompts} prompts')
        out.append(f"ID: {full_id}")
        out.append("Tareas de Notion: " + (", ".join(tasks) if tasks else "ninguna nombrada"))
        out.append(estado_line(last_prompt, estado))
        out.append(f"Empezó con: {first[:300]}")
        out.append("Terminó con:")
        out.append(ending)
        out.append("")
    print(f"# Sesiones del {day} ({shown})\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
