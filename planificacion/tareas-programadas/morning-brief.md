# Morning brief

Origen: tarea programada de claude.ai (trig_01XofNu7NuLt9sDPMbH7CUT6). Cron: `CRON_TZ=America/Montevideo 47 5 * * 1-5`. Notificaciones: push y correo. Conectores: Notion, Gmail, Calendar, Drive, Sheets, Todoist.

## Prompt original

Rutina matinal de Juan Manuel (zona horaria America/Montevideo). Corre sin supervisión: no hagas preguntas ni esperes confirmaciones. Responde en español, breve, sin usar el separador de tres guiones.

REGLAS DE EJECUCIÓN (obligatorias)
- La tarea tiene TRES pasos y los tres son obligatorios: 1) importar Todoist (Inbox y Lista de compras), 2) armar el brief, 3) enviarlo por correo. Terminar un paso NO termina la tarea: sigue siempre con el siguiente, aunque no haya habido nada que importar.
- No uses la skill "morning", no publiques artifacts, no crees archivos ni documentos.
- Si un paso o un conector falla, anótalo en una línea dentro del brief y sigue con el resto. Nunca cortes la ejecución por un error parcial.
- Tu último mensaje debe ser también el brief completo, en texto plano.

Si las skills "todoist-a-notion" y "brief-matinal" están disponibles, úsalas en ese orden para los pasos 1 y 2, pero respeta igualmente estas reglas, las de SEÑALES y las de COMPRAS de este mensaje. Si no hay skills, sigue estos pasos.

PASO 1 — Importar Inbox de Todoist a Notion
- Lee todas las tareas abiertas del Inbox de Todoist (projectId "inbox"). Si no hay, sigue con COMPRAS.
- SEÑALES: si el texto empieza con "señal:" o "senal:" (sin importar mayúsculas), NO es una tarea. Crea una fila en Win Today (data source collection://6d18da52-9e8e-828f-a39c-8793ee33189d) con: Daily Goal = "Señal DD/MM" (fecha del día al que corresponde), Señal = el texto sin el prefijo, 🎢 Weeks = la página "Semana NN - AA" (semana ISO) de ese día en Weeks (collection://f914dcf1-83a8-418a-86b6-6a3637a43994). El día al que corresponde: el de captura en Todoist (addedAt, hora de Montevideo); si se capturó antes de las 12:00, corresponde al día anterior. Luego complétala en Todoist.
- Por cada tarea normal, crea una página en Task DB (data source collection://020b9241-244e-42d2-9ce7-db5671397421) con: Task = texto limpio; Tiempo = estimación (5 min, 15 min, 30 min, 1 h, 2 h, Medio día), siempre; Projects = solo si la relación con un proyecto activo es obvia (Projects: collection://9c4c5809-fcf0-4783-9e5a-71e03f4eb42b, Status In Progress, Planning o Not started), si hay duda sin proyecto; Urgencia = "Esta semana" si en Todoist tiene prioridad p1 (en la API priority = 4) o el texto dice "urgente", "Sin apuro" si es una compra o recado sin plazo o el texto dice "sin apuro" o "cuando pueda", y vacía en cualquier otro caso; Do Date SOLO si la tarea trae fecha en Todoist, nunca inventar fechas; Due Date solo si hay un plazo explícito en el texto (Do Date = cuándo planifica hacerla, Due Date = vencimiento, no confundir); la descripción de Todoist va como contenido.
- Completa en Todoist solo lo que se creó bien en Notion. Nunca borres en Todoist. No modifiques tareas existentes de Notion.
- COMPRAS (Lista de compras → planilla Compras): lee todas las tareas abiertas del proyecto de Todoist "Lista de compras" (projectId 6hr9fqPq7rQRwQrp). Si no hay, pasa al Paso 2. Planilla Google Sheets "Compras", id 1BFvM-VzSs784I43GmrqDg4T4b6Ltpiy7VSO2lhKRuwU. Antes de escribir, lee la columna G de la pestaña Pendientes y saltea las tareas cuyo ID ya esté cargado. Por cada tarea nueva agrega una fila al final de Pendientes (columnas A:G) con: Fecha alta = fecha de captura en Todoist (addedAt, hora de Montevideo) como DD/MM/AAAA; Producto = texto limpio sin la cantidad; Cantidad = la cantidad si viene en el texto o la descripción (ej. "x2", "1 kg"), si no vacía; Dónde comprar = el valor de la columna E de la pestaña Referencia si el producto coincide claramente con una fila de la columna A, si no "A definir"; Estado = "Pendiente"; Notas = la descripción de Todoist, si la hay; ID Todoist = el id de la tarea. No toques las pestañas Referencia ni Historial. Después de escribir, vuelve a leer Pendientes y completa en Todoist SOLO las tareas cuyo ID quedó cargado. No las borres. Esto no crea nada en Notion.
- Guarda la lista de lo importado (tareas, señales y compras, con lo asignado) para el punto 9 del brief. Al terminar, pasa de inmediato al Paso 2.

PASO 2 — Brief matinal (solo lectura, salvo la base Capacidad)
CAPACIDAD: presupuesto 240 min de lunes a viernes (2 h de huecos en el trabajo + 18:00 a 20:00), 0 sábado y domingo. Resta la parte antes de las 20:00 de cada evento del calendario principal (juanm.trelles@gmail.com) y "Morcillas"; los eventos que empiezan a las 20:00 o después no cuentan; no restes los bloques de Trabajo del calendario "Rutina" ni eventos de día completo. Práctica Fútbol = 90 min (desde 18:30). GYM de martes y viernes se resta por su evento; si no tiene evento, resta 60 min igual. Libres = Presupuesto - Restado (mínimo 0). Planificable = Libres × 0.7, redondeado.
1. Capacidad: calcúlala para hoy y los próximos 6 días y actualiza la base Capacidad (collection://31eb5037-cb83-4e8a-ba74-bd519ec05a71): para cada fecha, si existe una fila con esa Fecha actualízala, si no créala con Día = abreviatura y DD/MM (ej. "Lun 26/10"), Fecha, Presupuesto (min), Restado (min), Libres (min), Planificable (min) y Detalle (qué restó). No borres filas.
2. Calendario de hoy: eventos con hora; señala viajes o eventos de todo el día.
3. Tareas de hoy: Task DB con Do Date = hoy y Done = false. Suma Tiempo (Medio día = 4 h), sin contar GYM ni Weekly Review si tienen evento. Compárala con el Planificable de hoy; si lo supera, dilo claro y sugiere qué mover (primero las que no tienen Urgencia = Esta semana ni Due Date cercana). Lista aparte las que no tienen Tiempo.
4. Vencidas: Do Date anterior a hoy y Done = false.
5. Seguimientos: Status = Waiting con Do Date hoy o antes.
6. Fechas límite: Due Date en los próximos 3 días.
7. Weekly Goals de la semana actual (data source collection://3a78da52-9e8e-80ec-9194-000b92d60eca, relacionados con la página "Semana NN - AA" de Weeks), con su estado.
8. Correo: hilos de las últimas 24 h en la bandeja principal de Gmail que pidan acción o respuesta: personas reales, trámites, bancos, facturas, plazos. Ignora promociones, newsletters, notificaciones automáticas y los correos "Morning brief" de días anteriores. Máximo 5, una línea cada uno.
9. Lo importado de Todoist en el paso 1 (tareas, señales y compras), con lo que se asignó. Para compras, una línea con la cantidad agregada a Pendientes y los productos.
10. SEÑAL PENDIENTE: revisa en Win Today si existe una fila "Señal DD/MM" del día hábil anterior (los lunes, la del viernes). Si no existe, agrega al final una pregunta corta: "¿Cuál fue la señal de [día]? Anotala en Todoist como 'señal: ...' y mañana la cargo."
11. Cierre: una pregunta corta para elegir 1 a 3 wins del día, con candidatos alineados a los Weekly Goals.

Formato: una línea de resumen arriba (carga del día vs planificable), luego calendario, tareas, alertas, correo, importados, señal pendiente y wins. Escaneable desde el celular. Omite secciones vacías. Si algún conector falla, dilo en una línea y sigue con el resto.

PASO 3 — Enviar el brief por correo (obligatorio)
- Envía el brief completo con la herramienta send_message de Gmail a juanm.trelles@gmail.com. Asunto: "☀️ Morning brief DD/MM" (fecha de hoy). Cuerpo: el brief en texto plano, tal cual.
- Envía un solo correo por ejecución. No respondas ni reenvíes otros correos.
- Si el envío falla, reintenta una vez; si vuelve a fallar, indícalo en la primera línea de tu mensaje final.
- Después del envío, escribe el brief completo como tu último mensaje.
