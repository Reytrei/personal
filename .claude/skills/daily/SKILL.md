---
name: "daily"
description: "Arranque del día de Juan Manuel desde el board personal (botón Start day): cierra el día anterior si quedó abierto, importa Todoist, calcula la capacidad y escribe el plan del día en daily/AAAA-MM-DD.md con cada tarea enlazada a su página de Task DB. Usar cuando corra /daily, pida arrancar o planificar el día, o ver qué tiene hoy."
argument-hint: "[AAAA-MM-DD]"
---

# Daily (board personal)

Una corrida a la mañana, desde el botón **Start day** del board personal (http://localhost:4748). Hace lo mismo que el morning brief, pero en vez de un mensaje deja el plan del día en un archivo que el board muestra y en el que se van tildando las tareas.

**Notion es la fuente de las tareas.** El archivo del día es una foto de trabajo: se arma desde Notion cada mañana y `/end-of-day` devuelve a Notion lo que se hizo. Nunca inventar tareas ni fechas.

**Nunca cambiar la Do Date (ni la Due Date) de una tarea sin el OK explícito de Juanma.** Organizar el día es sugerir: si algo no entra o conviene moverlo, se propone en la pregunta del paso 1 o en `## Tips`, y solo se escribe en Notion lo que Juanma aprobó tarea por tarea. Sin respuesta, no se mueve nada.

Rutas:
- `DAILY` = `~/personal/daily`, `HOY` = `DAILY/<fecha>.md` (fecha = el argumento, o hoy en America/Montevideo).
- `PREV` = el archivo más nuevo de `DAILY` anterior a la fecha.

## Paso 0: cerrar el día anterior
Si `PREV` existe y no termina con una línea `_Cerrado …_`, quedó sin cerrar: correr la skill `end-of-day` sobre `PREV` (fecha de `PREV`) antes de seguir, así lo tildado ayer queda Done en Notion y no reaparece hoy.

Después, juntar los **pendientes de ayer**: las líneas de `### Must do` de `PREV` sin tildar cuya tarea sigue con Done = false en Notion. `/end-of-day` no las mueve; se deciden acá, en la pregunta del paso 1.

## Paso 1: importar Todoist
Juanma está presente (tocó Start day): correr la skill `todoist-a-notion` en **corrida manual** (Inbox y Lista de compras), con la tabla de propuesta y las dudas sobre qué es cada tarea, y esperar su respuesta antes de crear. Si no hay nada que importar, seguir sin preguntar. Guardar lo importado para `## Tips`.

En la misma pregunta, sumar las tareas abiertas de Task DB cuyo contenido empieza con `Descripción pendiente:` o está vacío y que se crearon desde `PREV` (por ejemplo, las que importó el Morning brief de claude.ai): proponer su descripción y preguntar lo que falte. Con las respuestas, completar el contenido de esas páginas.

En la misma pregunta, los pendientes de ayer (paso 0): una tabla con Task, Tiempo, Due Date, la Falta 1 de su `## Estado` y una sugerencia (hoy, el próximo día hábil con Planificable libre según la base Capacidad, o sin fecha). Juanma elige para cada una; con la respuesta, cambiar su Do Date en Notion (nunca la Due Date). Si no hay pendientes, no preguntar por esto.

## Paso 2: datos del brief
Seguir los pasos 1 a 10 de la skill `brief-matinal` (capacidad de hoy y 6 días con actualización de la base Capacidad, calendario, tareas de hoy, vencidas, seguimientos, fechas límite, Weekly Goals, correo, señal pendiente) con sus reglas de capacidad. No escribir el brief como mensaje: los datos van al archivo del paso 3.

Además:
- **Esta semana sin fecha**: tareas abiertas con Urgencia = Esta semana y sin Do Date.
- Para cada tarea, guardar su URL de Notion (`https://app.notion.com/p/<id sin guiones>`), Tiempo, Urgencia, Due Date y proyecto.

## Paso 3: escribir `HOY`
Si `HOY` ya existe (segunda corrida del día), no pisarlo: conservar los tildes, las notas `HH:MM:` y `## Done (unplanned)`, y solo agregar tareas nuevas de Notion y actualizar Meetings, Waiting, Heads-up y Tips.

Formato (los títulos de sección van en inglés porque el board los usa como claves; el contenido en español; nunca usar el separador `---`):

```markdown
# <Día de la semana> <AAAA-MM-DD>

## Meetings
- <HH:MM>–<HH:MM> <evento>            (calendario principal y Morcillas; no Trabajo; viajes y día completo con "(todo el día)")
- Focus today: ~<Planificable en horas, 1 decimal> h (libres <Libres> min × 0.7; restó <Detalle>)

## Plan
<Una línea: carga de Must do vs planificable · Weekly Goals: N de M hechos · N vencidas> · [Semana NN - AA](<url de la página de Weeks>)
### Must do
- [ ] **<Task>** · <Tiempo> · <extras> · Card: [<Task>](<url de Notion>)
### If time
- [ ] **<Task>** · <Tiempo> · vencida (Do Date DD/MM) · Card: [<Task>](<url>)
### Later
- [ ] **<Task>** · <Tiempo> · Esta semana · Card: [<Task>](<url>)

## Waiting on others
- <Quién o qué>: <qué se espera> (seguimiento DD/MM) · Card: [<Task>](<url>)

## Email to answer
- <Remitente>: <qué pide, una línea> (<cuándo>)

## Heads-up
### <Día DD/MM>
- [ ] **Vence: <Task>** · Card: [<Task>](<url>)

## Tips
- Importado de Todoist: …
- Conectores o pasos que fallaron, si hubo (una línea cada uno).
- Si la carga supera lo planificable: qué mover (primero lo que no tiene Urgencia = Esta semana ni Due Date cercana). Solo sugerir, no mover.
- Señal pendiente: ¿cuál fue la señal de <día>? Anotala en Todoist como "señal: …".
- Wins de hoy: elegí 1 a 3. Candidatos: …

## Done (unplanned)
```

Reglas de las líneas:
- **Must do**: Do Date = hoy y Done = false. **If time**: vencidas (Do Date < hoy), marcadas `vencida (Do Date DD/MM)`. **Later**: Esta semana sin Do Date. Ninguna tarea en dos secciones. Las Status = Waiting van solo a `## Waiting on others`.
- **Tiempo**: tal cual (`5 min`, `15 min`, `30 min`, `1 h`, `2 h`); `Medio día` se escribe `4 h`; sin Tiempo, `sin estimar`. GYM o Weekly Review con evento en el calendario: `0 min (en el calendario HH:MM)`, porque su tiempo ya se restó de la capacidad.
- **extras** (solo si aplica, en este orden): `Esta semana` o `Sin apuro` (Urgencia), `due DD/MM` (Due Date), `Proyecto: <nombre>`, `Weekly Goal: <nombre>`.
- El título va igual que en Notion (sin el emoji). Si dos tareas se llaman igual, agregar ` (DD/MM)` a la segunda.
- **Heads-up**: Due Date en los próximos 3 días (sin hoy), un `###` por día en orden de fecha.
- **Email to answer**: solo los correos de personas reales o trámites que piden una respuesta de Juanma (suelen ser pocos o ninguno). No listar avisos, facturas que no piden nada ni newsletters.
- No hay sección de logins: si un conector o un paso falla, anotarlo en `## Tips` y seguir.
- Omitir las secciones vacías, salvo `## Plan` y `## Done (unplanned)`.

## Respuesta
Una línea con la carga contra lo planificable y lo que no se pudo hacer (conectores caídos, importación fallida). El plan se ve en el board; no repetirlo en el chat.
