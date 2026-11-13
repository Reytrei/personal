---
name: "planificar-semana"
description: "Organiza la semana de Juan Manuel en su Weekly Review: después de que fija los Weekly Goals, propone qué tarea hacer cada día según capacidad, metas y vencimientos, y carga las Do Date."
---

# Planificar semana

Se usa durante la Weekly Review, después de que Juan Manuel fijó sus Weekly Goals. Es una conversación: se propone, él ajusta y recién con su OK se carga. Nunca asumir: ante una duda que cambie el plan, preguntar.

## Referencias
- Zona horaria: America/Montevideo. Semana ISO de lunes a domingo.
- Weeks: collection://f914dcf1-83a8-418a-86b6-6a3637a43994 (página "Semana NN - AA"). El "🤖 Briefing semanal" está arriba de la página de la semana que terminó.
- Weekly Goals: collection://3a78da52-9e8e-80ec-9194-000b92d60eca (relación con Weeks).
- Task DB: collection://020b9241-244e-42d2-9ce7-db5671397421 (Task, Done, Do Date, Due Date, Status, Urgencia, Tiempo, Projects).
- Capacidad: collection://31eb5037-cb83-4e8a-ba74-bd519ec05a71 (Planificable (min) por día; la actualiza el morning brief).
- Quarter vigente: página "AA - QN" con metas e indicadores semanales.
- Google Calendar: principal (juanm.trelles@gmail.com), "Rutina" (bloques de Trabajo; el horario cambia según el mes, leerlo del calendario y no asumirlo) y "Morcillas" (compartido con Mili; algunos eventos están cargados en hora de Madrid, verificar la hora si algo no cierra).

## Reglas de fechas (no confundir)
- **Do Date** = el día en que planifica hacerla. Es lo único que este proceso asigna.
- **Due Date** = vencimiento real. Nunca inventarlo ni cambiarlo; si una tarea necesita uno, preguntar.
- Una tarea puede tener Do Date anterior a su Due Date por una razón concreta (ej. la factura se hace el viernes 30 porque recién ese día sabe las horas trabajadas, aunque vence el 31).

## Urgencia
- Propiedad Urgencia: Esta semana, Normal, Sin apuro. Vacío = Normal.
- La urgencia real sale sobre todo de la Due Date y de los Weekly Goals; Urgencia solo marca lo que se sale de lo normal (algo que tiene que salir ya sin tener vencimiento, o algo que puede esperar).
- Si una tarea marcada "Esta semana" no se hizo la semana anterior, preguntar si sigue siendo urgente.

## Capacidad
- Usar el Planificable (min) de la base Capacidad. Recalcularlo si cambió algo: 360 min de lunes a viernes dentro de la franja de 8:00 a 20:00, 0 fines de semana (si un día hábil no tiene bloque de Trabajo por viaje, feriado o vacaciones, preguntar su capacidad); restar eventos antes de las 20:00 (los que empiezan a las 20:00 o después son sociales y no cuentan); Práctica Fútbol cuenta desde las 18:30; ×0.7.
- Si Juan Manuel cancela entrenamientos o eventos (lesión, cambio de planes), ese tiempo vuelve a estar disponible.
- Entrenamientos o turnos sin día confirmado (ej. un GYM extra, fisioterapia): reservar su tiempo en el total de la semana y dejar margen en los días, sin asignarlos a uno.
- Si él dice que un día tiene la noche libre y quiere avanzar, se puede cargar más ese día.
- Tareas con su propio evento en el calendario (GYM, Weekly Review) no suman a la carga.

## Pasos
1. **Leer contexto**: Weekly Goals recién fijados; briefing semanal; metas e indicadores del Q; capacidad de la semana; calendario de la semana.
2. **Revisar TODAS las tareas abiertas** de Task DB (Done = false), no solo las agendadas. Clasificarlas:
   - Sirven a un Weekly Goal (prioridad máxima, aunque no tengan fecha).
   - Due Date en los próximos 7 días o vencidas.
   - Urgencia = Esta semana.
   - Piden los indicadores del Q (editoriales, posts, etc.).
   - Creadas en los últimos días sin fecha (para que no se pierdan).
   - Waiting: no se planifican; solo se mencionan si toca seguimiento.
   - Urgencia = Sin apuro sin Due Date: no se agendan (ej. mandados que hace cuando pasa cerca).
   - Resto: queda fuera de la semana.
3. **Preguntar lo que falte** (máximo 3 o 4 preguntas): disponibilidad de otras personas (ej. Mili para tareas conjuntas), compromisos que no están en el calendario, si algo grande tiene que salir esta semana, entrenamientos cancelados, si lo marcado "Esta semana" que quedó pendiente sigue siendo urgente.
4. **Proponer** una tabla por día (tareas y minutos vs planificable), con este orden de prioridad: Weekly Goals, vencimientos, Urgencia = Esta semana, indicadores del Q, resto. Marcar los días que se pasan. Listar aparte lo que queda afuera y por qué. Si hay tareas grandes del Weekly Goal, ponerlas temprano en la semana.
5. **Ajustar** con lo que diga Juan Manuel. Si menciona tareas nuevas (ej. reservar un lugar, escribir una carta), crearlas con Tiempo estimado.
6. **Cargar** con su OK: Do Date de cada tarea; Urgencia = Esta semana para las del Weekly Goal y las que él marque como urgentes; Status = Waiting para lo que son recordatorios a la espera de respuesta de otra persona; eventos de calendario solo si los pide. Si algo se cancela (ej. entrenamientos), borrar las tareas y eventos solo con su confirmación.
7. **Cerrar** con un resumen corto: la semana día por día y lo que quedó pendiente de decidir.

## Estilo
- Español, breve. Tablas para la semana. No usar el separador '---'.
- No cambiar Due Dates, no agendar tareas Sin apuro, no mover tareas que él ya fijó sin preguntárselo.