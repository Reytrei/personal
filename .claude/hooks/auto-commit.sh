#!/bin/bash
# Hook Stop: que ninguna sesión termine con cambios sin commitear o sin pushear.
# 1ª vez con cambios: bloquea el stop y le pide a Claude commits descriptivos y push.
# Si Claude ya tuvo su oportunidad (stop_hook_active) y quedan cambios: commit automático con la lista de archivos.
# Siempre termina pusheando lo que haya. Nunca reescribe historial ni fuerza.

input=$(cat)
active=$(printf '%s' "$input" | jq -r '.stop_hook_active // false' 2>/dev/null)

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" || exit 0
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

msg() { jq -n --arg m "$1" '{systemMessage: $m}'; }

changes=$(git status --porcelain)

if [ -n "$changes" ] && [ "$active" != "true" ]; then
  jq -n --arg files "$changes" '{
    decision: "block",
    reason: ("Hay cambios sin commitear en el repo personal:\n" + $files + "\nHacé commits chicos con mensaje descriptivo en español (uno por acción, como pide CLAUDE.md) y push a main. Si alguno de estos cambios no es tuyo o no debería subirse, decilo en vez de commitearlo.")
  }'
  exit 0
fi

if [ -n "$changes" ]; then
  files=$(git status --porcelain | awk '{print $NF}' | head -5 | paste -sd ', ' -)
  n=$(printf '%s\n' "$changes" | wc -l | tr -d ' ')
  [ "$n" -gt 5 ] && files="$files y $((n - 5)) más"
  git add -A && git commit -q -m "Cambios automáticos: $files" || { msg "auto-commit: no se pudo commitear"; exit 0; }
fi

# Pushear si hay commits locales sin subir.
git fetch -q 2>/dev/null
ahead=$(git rev-list --count @{u}..HEAD 2>/dev/null || echo 0)
[ "$ahead" -eq 0 ] && exit 0

if ! git push -q 2>/dev/null; then
  git pull -q --rebase 2>/dev/null && git push -q 2>/dev/null \
    || { git rebase --abort 2>/dev/null; msg "auto-commit: el push falló, hay $ahead commit(s) sin subir en ~/personal"; exit 0; }
fi
msg "auto-commit: $ahead commit(s) subidos a GitHub"
