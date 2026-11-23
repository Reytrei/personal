---
name: "todoist-a-notion"
description: "Procesa el Inbox de Todoist de Juan Manuel (tareas a Task DB y señales a Win Today en Notion) y la Lista de compras (a la planilla Compras). Usar cuando pida 'procesa mi inbox' o importar tareas de Todoist."
---

# Importar Inbox de Todoist a Notion

Todoist es la única bandeja de captura. Notion es el sistema. Este proceso mueve todo lo capturado a Notion y deja Todoist vacío.

## Referencias
- Zona horaria: America/Montevideo.
- Task DB (data source): collection://020b9241-244e-42d2-9ce7-db5671397421
- Projects (data source): collection://9c4c5809-fcf0-4783-9e5a-71e03f4eb42b (usar solo proyectos con Status In Progress, Planning o Not started; consultarlos en cada corrida)
- Pillars (data source): collection://157630fd-483d-4178-82f7-92d964a03a3f (usar solo los de Status Active; reglas en `planificacion/CLAUDE.md`)
- Win Today (señales diarias): collection://6d18da52-9e8e-828f-a39c-8793ee33189d (Daily Goal = título, Señal = texto, 🎢 Weeks = relación)
- Weeks: collection://f914dcf1-83a8-418a-86b6-6a3637a43994 (páginas "Semana NN - AA", semana ISO)
- Todoist "Lista de compras": projectId 6hr9fqPq7rQRwQrp.
- Planilla Google Sheets "Compras": id 1BFvM-VzSs784I43GmrqDg4T4b6Ltpiy7VSO2lhKRuwU (pestañas Pendientes, Referencia, Historial).
- Propiedades de Task DB: Task (título), Do Date (fecha), Due Date (fecha), Projects (relación), Urgencia (select: Esta semana, Normal, Sin apuro; vacío = Normal), Status (select; Waiting = depende de otro), Tiempo (select: 5 min, 15 min, 30 min, 1 h, 2 h, Medio día), Done (checkbox).

## Pasos
1. Leer todas las tareas abiertas del Inbox de Todoist (projectId "inbox").
2. Si no hay nada, decirlo en una línea y seguir con Compras (paso 7).
3. **Señales**: si el texto empieza con "señal:" o "senal:" (sin importar mayúsculas), NO es una tarea. Crear una fila en Win Today con:
   - **Daily Goal** = "Señal DD/MM" (día al que corresponde).
   - **Señal** = el texto sin el prefijo.
   - **🎢 Weeks** = la página "Semana NN - AA" de ese día.
   - Día al que corresponde: el de captura en Todoist (addedAt, hora de Montevideo); si se capturó antes de las 12:00, corresponde al día anterior.
4. **Tareas**: para cada una, crear una página en Task DB con:
   - **Task**: el texto de la tarea, limpio (sin la fecha ni la palabra "urgente" si estaban escritas en el texto).
   - **Tiempo**: siempre estimarlo.
   - **Projects**: solo si la relación con un proyecto activo es obvia. Ante la duda, sin proyecto.
   - **Pillars**: solo si la tarea queda sin proyecto (con proyecto, el pilar se hereda). Asignar el pilar activo que corresponda; puede ser más de uno. Ante la duda, sin pilar y anotarlo como duda.
   - **Urgencia**:
     - Esta semana: si en Todoist tiene prioridad p1 (en la API, priority = 4) o el texto dice "urgente".
     - Sin apuro: si es una compra o un recado sin plazo, o el texto dice "sin apuro" o "cuando pueda".
     - En cualquier otro caso, dejarla vacía (cuenta como Normal).
   - **Do Date**: SOLO si la tarea trae fecha desde Todoist. Nunca inventar fechas.
   - **Due Date**: solo si el texto o la descripción mencionan un plazo explícito. No confundir con Do Date: Do Date es cuándo planifica hacerla, Due Date es el vencimiento.
   - **Descripción** (contenido de la página, siempre): qué hay que hacer y cuándo está lista, en 1 a 3 líneas, a partir del texto y la descripción de Todoist (esta última va también, tal cual, debajo). Si no se puede saber qué es o cuándo está lista, es una **duda**: en corrida manual se pregunta (ver abajo); sin supervisión, crear la página con `Descripción pendiente: <qué falta saber>` como primera línea.
5. Completar en Todoist cada ítem (tarea o señal) que se creó bien en Notion. Si una creación falló, no completarlo en Todoist.
6. Lo que queda sin fecha ni proyecto aparece solo en la vista "Por decidir" de Task DB; no hace falta hacer nada más.
7. **Compras** (Lista de compras → planilla Compras; no crea nada en Notion):
   - Leer todas las tareas abiertas del proyecto "Lista de compras". Si no hay, terminar.
   - Leer la columna G de la pestaña Pendientes y saltear las tareas cuyo ID ya esté cargado.
   - Por cada tarea nueva, agregar una fila al final de Pendientes (columnas A:G): **Fecha alta** = fecha de captura en Todoist (addedAt, hora de Montevideo) como DD/MM/AAAA; **Producto** = texto limpio sin la cantidad; **Cantidad** = la cantidad si viene en el texto o la descripción (ej. "x2", "1 kg"), si no vacía; **Dónde comprar** = el valor de la columna E de la pestaña Referencia si el producto coincide claramente con una fila de la columna A, si no "A definir"; **Estado** = "Pendiente"; **Notas** = la descripción de Todoist, si la hay; **ID Todoist** = el id de la tarea.
   - No tocar las pestañas Referencia ni Historial.
   - Después de escribir, volver a leer Pendientes y completar en Todoist SOLO las tareas cuyo ID quedó cargado.

## Si Juan Manuel está presente (corrida manual)
Antes de crear, mostrar una tabla con la propuesta (Tarea, Descripción, Do Date, Due Date, Proyecto, Pilar, Urgencia, Tiempo), las señales detectadas con el día asignado y las compras con su comercio. Debajo, las dudas numeradas, una por tarea, con opciones cuando se pueda (ej. "¿'Llamar a Pedro' es por el presupuesto del baño o por el cumpleaños?"). Esperar su OK, correcciones y respuestas; con eso, crear.

## Si corre sin supervisión (rutina matinal)
Aplicar las reglas de arriba sin preguntar y devolver la lista de lo importado (tareas, señales y compras) con lo que se asignó, marcando las que quedaron con `Descripción pendiente`, para que lo revise en el brief. Si un paso falla, anotarlo y seguir con el resto.

## Reglas
- Nunca borrar en Todoist; solo completar.
- No modificar tareas existentes de Notion en este proceso.
- Responder en español, breve, sin usar el separador '---'.