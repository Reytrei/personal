---
name: "end-of-day"
description: "Cierre del día de Juan Manuel desde el board personal (botón End day): deja en Notion el estado de las sesiones del día que no lo dejaron, pasa a Notion lo que se tildó en daily/AAAA-MM-DD.md (Done). Corre sin preguntas: no planifica ni mueve fechas. Usar cuando corra /end-of-day o pida cerrar el día."
argument-hint: "[AAAA-MM-DD]"
---

# End of day (board personal)

Devuelve a Notion lo que pasó en el board durante el día. Notion es la fuente de las tareas: después de esta corrida, Task DB refleja el día sin tocarla a mano.

**Corre de punta a punta sin preguntar nada.** Es el botón que Juanma aprieta antes de irse: solo registra lo que pasó. No planifica, no propone y no mueve fechas; lo que quedó pendiente lo decide `/daily` a la mañana siguiente.

`DIA` = `~/personal/daily/<fecha>.md` (fecha = el argumento, o hoy en America/Montevideo). Si no existe, decirlo y terminar.
`SCRIPTS` = `~/personal/.claude/skills/end-of-day/scripts`. `TMP` = el scratchpad de esta sesión (si no, `$TMPDIR`).

## Paso 1: estado de las sesiones del día
Que ninguna sesión que trabajó una tarea quede sin su estado en Notion (mañana se sigue desde ahí, no desde la conversación).

1. Listar: `python3 -I $SCRIPTS/sesiones.py <fecha>`. Por sesión da sus tareas de Notion y su `Estado:` (`none`, `current` o `stale`).
2. Saltear las sesiones con `Estado: current`, las que no nombran ninguna tarea de Notion y las que fueron solo una pregunta corta ya respondida.
3. Para cada sesión que queda (`none` o `stale`):
   - Condensar: `python3 -I $SCRIPTS/condensar_sesion.py <ID completo> <TMP>/eod-<id8>.txt`.
   - Lanzar un subagente por sesión, todos en un mismo mensaje (Agent, `subagent_type: general-purpose`, `model: sonnet`), con este pedido:
     > Escribís el estado de una sesión de Claude Code en su tarea de Notion. No ves la sesión, solo su transcript condensado en `<TMP>/eod-<id8>.txt` (leelo entero, por partes si hace falta). Sesión "<nombre>" (<ID completo>), tarea de Notion <url>.
     > 1. Leé `~/personal/.claude/skills/handoff/SKILL.md` y seguí su paso 3 al pie de la letra, con "sesión \"<nombre>\" · escrito por /end-of-day" en la primera línea de `## Estado`. Excepción: no marques Done aunque la tarea parezca terminada; ponelo como "Falta 1: confirmar que está terminada y tildarla".
     > 2. Solo hechos: lo que el transcript muestra que se hizo. Lo que Claude propuso y Juanma no confirmó va como pregunta, no como hecho. Si la sesión terminó con una pregunta a Juanma, va textual en "Preguntas para Juanma" y "Falta 1" es "Respuesta de Juanma a la pregunta 1, después …".
     > 3. No escribas nada más: ni otras páginas, ni propiedades, ni archivos, ni correos.
     > 4. Respondé solo: la tarea, el estado (en curso / esperando a Juanma / lista para revisar / terminada) y Falta 1.
4. Volver a correr `sesiones.py`: cada sesión procesada tiene que dar `Estado: current`. Si no, reintentarla una vez y, si sigue fallando, anotarla en la respuesta.

## Paso 2: leer el día
De `DIA`, cada línea `- [ ]` / `- [x]` con su `Card: [..](<url de Notion>)` (el id de la página son los 32 caracteres hex del final de la URL), y sus notas `  - HH:MM: …` (avances a medias). `## Done (unplanned)` se ignora: lo hecho fuera del plan Juanma lo carga directo en Notion.

## Paso 3: aplicar en Notion
Sin pedir OK:

| En el board | En Notion |
|---|---|
| Tildada `- [x]` con Card | Done = true |
| Sin tildar, con notas `HH:MM: …` y sin sesión | Las notas van a `## Historial` de su página como `- DD/MM HH:MM: …` (así el avance no se pierde) |
| Cualquier otra sin tildar | Nada |

Nunca cambiar Do Date, Due Date, Urgencia ni proyecto. Si una escritura falla, seguir con el resto y anotarla para la respuesta.

## Paso 4: cerrar el archivo
Agregar al final de `DIA`:

```
_Cerrado <HH:MM>: <N> estados de sesión en Notion, <N> hechas en Notion, <N> pendientes._
```

Esa línea es la que `/daily` busca para saber que el día quedó cerrado.

## Respuesta
La misma línea de cierre y, si algo falló, qué fue. Nada más: ni preguntas, ni sugerencias, ni próximos pasos.
