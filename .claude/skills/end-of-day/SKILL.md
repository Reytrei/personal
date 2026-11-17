---
name: "end-of-day"
description: "Cierre del día de Juan Manuel desde el board personal (botón End day): deja en Notion el estado de las sesiones del día que no lo dejaron, pasa a Notion lo que se tildó en daily/AAAA-MM-DD.md (Done), crea en Task DB lo hecho sin planificar y propone qué hacer con lo pendiente. Usar cuando corra /end-of-day o pida cerrar el día."
argument-hint: "[AAAA-MM-DD]"
---

# End of day (board personal)

Devuelve a Notion lo que pasó en el board durante el día. Notion es la fuente de las tareas: después de esta corrida, Task DB refleja el día sin tocarla a mano.

`DIA` = `~/personal/daily/<fecha>.md` (fecha = el argumento, o hoy en America/Montevideo). Si no existe, decirlo y terminar.
`SCRIPTS` = `~/personal/.claude/skills/end-of-day/scripts`. `TMP` = el scratchpad de esta sesión (si no, `$TMPDIR`).

## Paso 1: estado de las sesiones del día
Que ninguna sesión que trabajó una tarea quede sin su estado en Notion (mañana se sigue desde ahí, no desde la conversación).

1. Listar: `python3 -I $SCRIPTS/sesiones.py <fecha>`. Por sesión da sus tareas de Notion y su `Estado:` (`none`, `current` o `stale`).
2. Preguntar una vez: "¿Hay alguna sesión todavía corriendo en otra pestaña? Terminala o frenala antes, si no su estado va a quedar incompleto." Seguir sin esperar si Juanma ya dijo que terminó el día.
3. Saltear las sesiones con `Estado: current`, las que no nombran ninguna tarea de Notion y las que fueron solo una pregunta corta ya respondida.
4. Para cada sesión que queda (`none` o `stale`):
   - Condensar: `python3 -I $SCRIPTS/condensar_sesion.py <ID completo> <TMP>/eod-<id8>.txt`.
   - Lanzar un subagente por sesión, todos en un mismo mensaje (Agent, `subagent_type: general-purpose`, `model: sonnet`), con este pedido:
     > Escribís el estado de una sesión de Claude Code que ya terminó, en su tarea de Notion. No ves la sesión, solo su transcript condensado en `<TMP>/eod-<id8>.txt` (leelo entero, por partes si hace falta). Sesión "<nombre>" (<ID completo>), tarea de Notion <url>.
     > 1. Leé `~/personal/.claude/skills/handoff/SKILL.md` y seguí su paso 3 al pie de la letra, con "sesión \"<nombre>\" · escrito por /end-of-day" en la primera línea de `## Estado`. Excepción: aunque la tarea parezca terminada, no marques Done; decilo en la respuesta y Juanma lo aprueba en la tabla del cierre.
     > 2. Solo hechos: lo que el transcript muestra que se hizo. Lo que Claude propuso y Juanma no confirmó va como pregunta, no como hecho. Si la sesión terminó con una pregunta a Juanma, va textual en "Preguntas para Juanma" y "Falta 1" es "Respuesta de Juanma a la pregunta 1, después …".
     > 3. No escribas nada más: ni otras páginas, ni propiedades, ni archivos, ni correos.
     > 4. Respondé solo: la tarea, el estado (en curso / esperando a Juanma / lista para revisar / terminada) y Falta 1.
5. Volver a correr `sesiones.py`: cada sesión procesada tiene que dar `Estado: current`. Si no, arreglarla.

## Paso 2: leer el día
De `DIA`, cada línea `- [ ]` / `- [x]` con su `Card: [..](<url de Notion>)` (el id de la página son los 32 caracteres hex del final de la URL), sus notas `  - HH:MM: …` (avances a medias) y las líneas de `## Done (unplanned)`.

## Paso 3: proponer
Mostrar una tabla y esperar el OK o las correcciones de Juanma:

| Tarea | En el board | Propuesta para Notion |
|---|---|---|
| Tildadas `- [x]` con Card | hecha (`done HH:MM: …`) | Done = true |
| `## Done (unplanned)` con Card | hecha | Done = true |
| `## Done (unplanned)` sin Card | hecha | Crear en Task DB con Task, Tiempo estimado, Do Date = hoy y Done = true (si es claramente una tarea ya existente en Notion, marcar esa en vez de crear) |
| Must do sin tildar | pendiente (con su `## Estado` de Notion y su última nota) | Nueva Do Date: el próximo día hábil con Planificable libre según la base Capacidad, o sin fecha si Juanma lo prefiere |
| If time / Later sin tildar | no se tocó | Nada |
| Sesión que el paso 1 dejó como `terminada` | sin tildar | Done = true |

Nunca cambiar Due Date, Urgencia ni proyecto. Las notas `HH:MM: …` de una tarea pendiente que no tuvo sesión van a `## Historial` de su página como `- DD/MM HH:MM: …` (así el avance no se pierde).

Si corre sin Juanma (lo llama `/daily` para cerrar un día que quedó abierto), hacer el paso 1 sin preguntar, aplicar solo los Done y no mover fechas.

## Paso 4: aplicar
Aplicar lo aprobado en Notion. Si una escritura falla, decirlo y seguir con el resto. Después, agregar al final de `DIA`:

```
_Cerrado <HH:MM>: <N> estados de sesión en Notion, <N> hechas en Notion, <N> creadas, <N> reprogramadas, <N> pendientes sin cambio._
```

Esa línea es la que `/daily` busca para saber que el día quedó cerrado.

## Respuesta
La misma línea de cierre y, si quedó algo sin aplicar, qué fue.
