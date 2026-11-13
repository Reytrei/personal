---
name: "briefing-semanal"
description: "Prepara el briefing para la Weekly Review de Juan Manuel: qué pasó la semana anterior, alineación con metas del Q y candidatos a Weekly Goal. Usar cuando pida su briefing semanal o preparar la weekly."
---

# Briefing semanal

Objetivo: que Juan Manuel llegue a su Weekly Review recordando qué hizo, con las tareas recurrentes ya creadas, sabiendo cuánto entra en la semana y con las candidatas armadas. Las decisiones son suyas: este proceso prepara evidencia y sugiere. Lo único que crea por su cuenta son las tareas recurrentes y sus bloques de calendario.

## Referencias
- Zona horaria: America/Montevideo. Semanas ISO de lunes a domingo.
- Semana que termina: la semana ISO anterior si hoy es lunes; si no, la semana en curso.
- Semana a planificar: la semana ISO en curso si hoy es lunes; si no, la próxima.
- Weeks: collection://f914dcf1-83a8-418a-86b6-6a3637a43994. Páginas "Semana NN - AA" (NN = semana ISO, AA = año en dos dígitos). La Weekly Review se hace en la página de la semana que termina.
- Weekly Goals: collection://3a78da52-9e8e-80ec-9194-000b92d60eca (relación con Weeks; Done; Señal).
- Task DB: collection://020b9241-244e-42d2-9ce7-db5671397421 (Task, Done, Do Date, Due Date, Status, Projects, Urgencia, Tiempo). Urgencia: Esta semana, Normal, Sin apuro; vacío = Normal.
- Projects: collection://9c4c5809-fcf0-4783-9e5a-71e03f4eb42b (activos: Status In Progress, Planning, Not started).
- Quarters: páginas "AA - QN" (ej. "26 - Q4"); las metas del trimestre y sus indicadores semanales están en la página. Buscarla con la búsqueda de Notion.
- Google Calendar: principal (juanm.trelles@gmail.com), "Rutina" (bloques de Trabajo; el horario cambia según el mes, leerlo del calendario y no asumirlo; ignorar en el resumen de eventos) y "Morcillas" (compartido).

## Tareas recurrentes de la semana a planificar
Antes de crear algo, comprobar que no exista ya: en Task DB, una tarea con el mismo nombre y Do Date ese día; en el calendario principal, un evento con el mismo título ese día. Si existe, no duplicar.

| Tarea | Do Date | Tiempo | Calendario |
|---|---|---|---|
| Weekly Review | lunes | 30 min | Evento "Weekly Review" de 30 min en el primer hueco libre del lunes entre 9:00 y 12:00 |
| Importar finanzas | lunes | 15 min | No |
| Revisar finanzas | lunes | 30 min | No |
| GYM | martes | 1 h | Evento "GYM" de 1 h en el primer hueco libre entre 7:00 y 9:00; si no hay, entre 18:00 y 20:00 |
| GYM | viernes | 1 h | Igual que el martes |

- No crear "Plan de Comidas" ni "Super": la planificación de comidas, las compras y las tareas de verdulería las crea la skill planificar-comidas cada dos semanas.
- Hueco libre = sin eventos en el calendario principal ni en "Morcillas" (los bloques de Trabajo no cuentan como ocupado para la Weekly Review).
- Los eventos se crean en el calendario principal. La tarea de Task DB lleva solo la fecha (sin hora).
- Si no hay hueco para un GYM, crear la tarea igual, sin evento, y avisarlo en el briefing.
- Si un día de GYM coincide con otro entrenamiento del calendario, crearlo igual y avisarlo para que él decida.

## Reglas de capacidad
Capacidad = horas por día disponibles para tareas propias. El día tiene las mismas horas aunque empiece antes: entrenamientos y eventos restan del presupuesto del día sin importar a qué hora sean.
- Presupuesto base de lunes a viernes: 6 h dentro de la franja de 8:00 a 20:00 (incluye los huecos dentro del trabajo, por ejemplo mientras espera a Claude). El día no debería terminar más tarde de las 20:00.
- Si un día hábil no tiene bloque de Trabajo en "Rutina" (viaje, feriado, vacaciones), marcarlo en la tabla y preguntar cuánta capacidad tiene; no asumirla.
- Sábado y domingo: sin capacidad.
- Restar la parte de cada evento del calendario principal y de "Morcillas" que cae antes de las 20:00. Los eventos que empiezan a las 20:00 o después no se cuentan (son sociales). No restar los bloques de Trabajo ni los eventos de día completo.
- Práctica Fútbol: contar desde las 18:30 (traslado) hasta las 20:00, es decir 1.5 h.
- GYM de martes y viernes: se resta por su evento del calendario. Si no se pudo agendar, restar 1 h igual.
- Entrenamientos o turnos que él va a hacer pero sin día confirmado (ej. un GYM extra, fisioterapia): restarlos como una fila "Reserva" al final de la tabla (horas × 0.7 del total), no de un día puntual. Preguntar si los hay.
- Mínimo 0 h por día.
- Capacidad planificable = horas libres × 0.7 (el 30% es colchón).
- Carga ya agendada = suma de Tiempo de tareas abiertas con Do Date ese día (Medio día = 4 h). No sumar las tareas que ya tienen su propio evento en el calendario (GYM y Weekly Review), porque ya se restaron.

## Pasos
1. Identificar la semana que termina y su página en Weeks, y la semana a planificar.
2. **Crear las tareas recurrentes** de la semana a planificar según la tabla.
3. **Semana que termina**:
   - Tareas hechas: Done = true y Do Date dentro de la semana, agrupadas por proyecto y "sin proyecto".
   - Weekly Goals de esa semana: cumplidos o no, con su Señal si la tiene.
   - Eventos del calendario de esa semana (no los bloques de Trabajo), para recordar lo que no pasó por Task DB.
   - Entrenamientos: contar solo los eventos del calendario que sean entrenamiento (GYM, Práctica Fútbol, Cross Training, Fisioterapia u otros con nombre de entrenamiento). No usar Daily Tracking. Indicar si llegó al mínimo de 3. Si hay tareas "GYM" hechas sin evento ese día, avisarlo para que él lo confirme.
   - Lo que quedó sin hacer: Do Date dentro de la semana y Done = false. Destacar las que tenían Urgencia = Esta semana.
4. **Alineación**:
   - Metas del Quarter vigente con su indicador semanal (si la página no existe o no tiene metas, decirlo).
   - Qué parte de lo hecho empujó proyectos activos o metas, y qué parte fue mantenimiento o urgencias.
   - Proyectos activos sin ninguna tarea abierta (sin próxima acción).
5. **Capacidad de la semana a planificar**: tabla por día con presupuesto, lo que se resta, horas libres, planificables (×0.7), carga ya agendada y margen. Cerrar con el total planificable y avisar los días sobrecargados.
6. **Candidatas para la semana** (el pool del que elige):
   - Tareas con Urgencia = Esta semana.
   - Tareas con Status = Next Up.
   - La próxima acción de cada proyecto vinculado al Quarter vigente (tarea abierta más cercana; si no hay, marcar "sin próxima acción").
   - Tareas con Due Date en los próximos 14 días y vencidas.
   - Lo que piden los indicadores del Q esa semana (ej. envíos a editoriales, posts de LinkedIn), indicando si ya hay tarea o falta crearla.
   - No incluir tareas con Urgencia = Sin apuro y sin Due Date.
   - Para cada candidata, Tiempo (o "sin estimar") y por qué está. Sumar el Tiempo del pool y compararlo con la capacidad planificable.
7. **Pipelines**: Status = Waiting (con fecha de seguimiento). Cuántas tareas hay en "Por decidir" (sin Do Date, sin proyecto, sin Status) y cuáles llevan más de 30 días abiertas.
8. **Comidas (plan contra lo comido)**: planilla "Plan y registro de comidas Juanma" (id `1mfIChB1alVFoRp2GkjKzOCv-Q1tEYxMVxdDSMwUVGgM`, locale es_UY). Revisar los últimos 7 días hasta ayer en las pestañas "Semana DD/MM" (pueden ser dos). Para cada día con algo en "Lo que comí", calcular las porciones con la pestaña Equivalencias (en crudo; 180 g de carne = 3 prote; legumbres 0,5 carbo + 0,5 prote) y escribirlas en la columna "Lo que comí" de ese día, filas 16 a 20 (carbo, prote, grasa, fruta, vegetales; meta en la columna P). En el briefing: días que cumplieron las 22 porciones, faltantes o excesos por grupo, platos planificados que no se cocinaron y platos con Estado "Probar" del Banco de comidas que se comieron, preguntando qué le parecieron. Si no cargó nada, decirlo en una línea.
9. **Candidatos a Weekly Goal**: 2 o 3, cada uno con una línea de por qué, alineados a las metas del Quarter si existen; si no, a proyectos activos y fechas límite. Son sugerencias: él elige.

## Salida
- Insertar al INICIO de la página de la semana que termina un bloque desplegable (toggle) titulado "🤖 Briefing semanal" con todo el contenido dentro. Leer antes notion://docs/enhanced-markdown-spec para la sintaxis. Además de eso, de las tareas recurrentes con sus eventos y de las porciones de lo comido en la planilla de comidas, no modificar nada más.
- Al inicio del briefing, una línea con lo recurrente creado (y lo que ya existía o no se pudo agendar).
- Si la página de la semana que termina no existe, no crearla: avisarlo en la primera línea de la respuesta.
- Responder con el mismo contenido (para el correo).
- Español, breve, escaneable. Omitir secciones vacías. No usar el separador '---'.