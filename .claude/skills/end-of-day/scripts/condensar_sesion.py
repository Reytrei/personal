"""Condense one Claude Code session transcript into a readable text file.

Usage: python3 -I condense_session.py <session-id or id prefix> <out.txt>

Keeps, in order: every user prompt (full), every assistant text message
(full), one line per tool call (tool name + its key input), and the first
lines of each tool result (errors marked). Drops subagent sidechains,
attachments, snapshots and other bookkeeping lines. If the result is still
large, keeps the start (the goal) and the end (the current state) and cuts
the middle, saying how much was cut. Read-only on the transcript.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.expanduser("~/.claude-personal/projects")
RESULT_CHARS = 400
HEAD_CHARS = 60_000
TAIL_CHARS = 240_000


def find(session):
    hits = glob.glob(os.path.join(ROOT, "-Users-*-personal", f"{session}*.jsonl"))
    if len(hits) != 1:
        sys.exit(f"expected one transcript for {session!r}, found {len(hits)}: {hits}")
    return hits[0]


def tool_line(b):
    name, inp = b.get("name", "?"), b.get("input", {}) or {}
    for key in ("command", "file_path", "url", "pattern", "query", "skill", "description", "prompt"):
        if key in inp:
            val = str(inp[key]).replace("\n", " ⏎ ")
            return f"[tool {name}] {key}: {val[:600]}"
    return f"[tool {name}] {json.dumps(inp, ensure_ascii=False)[:600]}"


def result_text(b):
    c = b.get("content")
    if isinstance(c, list):
        c = " ".join(x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text")
    c = re.sub(r"\s+", " ", str(c or "")).strip()
    tag = "[result ERROR]" if b.get("is_error") else "[result]"
    return f"{tag} {c[:RESULT_CHARS]}{' …' if len(c) > RESULT_CHARS else ''}"


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    path, out = find(sys.argv[1]), sys.argv[2]
    lines, title = [], None
    for raw in open(path):
        try:
            d = json.loads(raw)
        except ValueError:
            continue
        t = d.get("type")
        if t == "custom-title" and d.get("customTitle"):
            title = d["customTitle"]
        if t == "ai-title" and d.get("aiTitle") and not title:
            title = d["aiTitle"]
        if d.get("isSidechain") or t not in ("user", "assistant"):
            continue
        ts = (d.get("timestamp") or "")[:16].replace("T", " ")
        content = d["message"].get("content", [])
        if isinstance(content, str):
            content = [{"type": "text", "text": content}]
        for b in content:
            bt = b.get("type")
            if bt == "text" and b.get("text", "").strip():
                txt = b["text"].strip()
                if t == "user":
                    if d.get("isMeta") or txt.startswith("<local-command") or txt.startswith("<system-reminder"):
                        continue
                    m = re.search(r"<command-name>(.*?)</command-name>", txt)
                    if m:
                        args = re.search(r"<command-args>(.*?)</command-args>", txt, re.S)
                        txt = f"{m.group(1)} {args.group(1) if args else ''}".strip()
                    lines.append(f"\n===== USER {ts} UTC =====\n{txt}\n")
                else:
                    lines.append(f"\n----- CLAUDE {ts} UTC -----\n{txt}\n")
            elif bt == "tool_use":
                lines.append(tool_line(b))
            elif bt == "tool_result":
                lines.append(result_text(b))
    body = "\n".join(lines)
    if len(body) > HEAD_CHARS + TAIL_CHARS:
        cut = len(body) - HEAD_CHARS - TAIL_CHARS
        body = (
            body[:HEAD_CHARS]
            + f"\n\n[… {cut:,} characters from the middle of the session cut; the end below is the latest state …]\n\n"
            + body[-TAIL_CHARS:]
        )
    header = f"# Session \"{title or '(untitled)'}\" · {os.path.basename(path)[:-6]}\n# Transcript: {path}\n"
    with open(out, "w") as f:
        f.write(header + body)
    print(f"{out}: {len(body):,} chars from {os.path.getsize(path):,} bytes")


if __name__ == "__main__":
    main()
