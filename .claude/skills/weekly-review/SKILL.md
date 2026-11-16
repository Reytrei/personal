---
name: "weekly-review"
description: "Guía la Weekly Review de Juan Manuel paso a paso sobre la plantilla de la página de la semana en Notion: reflexión, indicadores del Q, clean execution, projects scan, Weekly Goals, plan, pipelines y cierre. Usar cuando pida hacer la weekly, la weekly review o planificar la semana desde cero."
---

# Weekly Review

Conversación guiada, **un paso por mensaje**: se presenta el paso, se espera su respuesta, se ejecuta lo que decida y recién ahí se pasa al siguiente. Nunca adelantarse a planificar la semana sin haber hecho Clean execution y Projects scan: ahí se crean las tareas que faltan. Las decisiones son suyas; este proceso prepara evidencia, sugiere y ejecuta con su OK.

## Referencias
- Las de `briefing-semanal` (Weeks, Weekly Goals, Task DB, Projects, Quarters, Seguimiento Editoriales, calendarios). Zona horaria America/Montevideo.
- Semana que termina = la ISO anterior si hoy es lunes; si no, la en curso. La review se hace en su página "Semana NN - AA". La semana a planificar es la siguiente.
- Skills que usa: `briefing-semanal` (paso 0), `planificar-semana` (paso 6), `contactar-editorial` (si hay que preparar envíos).

## Pasos

0. **Briefing.** Buscar el toggle "🤖 Briefing semanal" al inicio de la página de la semana que termina. Si no existe, correr `briefing-semanal`. Si existe, no duplicarlo: revisar qué cambió desde que se generó (tareas marcadas Done después, eventos nuevos, envíos registrados en Seguimiento Editoriales) y decirlo en 2 o 3 líneas.

1. **Reflexión e indicadores del Q.** Mostrar la tabla de indicadores de la página prellenada con lo que sale de los datos (envíos desde Seguimiento Editoriales por Fecha de envío; entrenamientos del calendario; posts; hitos) y pedir lo que solo sabe él: reflexión de la semana, horas de Brick, puntaje de nutrición y correcciones. Con su respuesta: escribir la reflexión y completar la tabla en la página; guardar Brick en la propiedad ScreenTime de la semana que termina (horas decimales, ej. 3 h 12 min = 3.2); marcar Done los Weekly Goals que diga que cumplió.

2. **Clean execution.** Partir del "Clean execution propuesto" del briefing (actualizado con lo que cambió): marcar hechas, duplicados, Do Dates que ya no son reales, arrastradas con Urgencia = Esta semana, vencidas y "Por decidir". Una línea por tarea con la acción sugerida. Ejecutar lo que apruebe. No cambiar Due Dates sin que lo diga.

3. **Projects scan.** Tabla de proyectos activos (In Progress, Planning, Not started) con su próxima acción y una propuesta de tareas a crear (➕), sobre todo para los proyectos de metas del Q cuyos indicadores piden algo esta semana. Para editoriales, armar las tareas desde Seguimiento Editoriales (Próxima acción de las "No enviado"). Proponer cerrar proyectos terminados o pasar a Someday los que no se mueven. Con su OK: crear las tareas con Tiempo y Status = Next Up, cambiar Status de proyectos y tildar en la página del Quarter las metas que dé por cumplidas.

4. **Weekly Goals.** Proponer 2 o 3 candidatos (los del briefing, ajustados con lo que salió en los pasos 1 a 3). Él elige. Crearlos en Weekly Goals con Name, Priority (1st, 2nd, 3rd), Señal medible, Projects y relación con la página de la semana a planificar.

5. **Entrenamientos.** Proponer los entrenamientos de la semana a planificar: mínimo 3 (hábito del Q), contando los que ya están en el calendario (Práctica Fútbol, Cross Training, etc.). Por defecto, GYM martes y viernes, 1 h, en el primer hueco libre entre 7:00 y 9:00 o, si no hay, entre 18:00 y 20:00. Si hay una lesión o un plan de fisio en curso, preguntar qué manda el plan y qué entrenamientos se suspenden. Avisar superposiciones. Con su OK: crear en Task DB una tarea por entrenamiento (nombre del entrenamiento, Tiempo, Do Date sin hora) y su evento en el calendario principal; borrar los que cancele. Antes de crear, comprobar que no existan (misma tarea y Do Date, mismo evento ese día).

6. **Plan de la semana.** Recién ahora correr `planificar-semana` con los goals y los entrenamientos fijados.

7. **Pipelines.** Waiting sin seguimiento o con más de 30 días: proponer fecha de seguimiento, dejar o borrar.

8. **Cierre.** Recordar lo manual (limpiar descargas y fotos). Confirmar que existe la página de la semana a planificar (si no, ofrecer crearla). Marcar Done la tarea "Weekly Review" del día. Cerrar con un resumen corto de la semana día por día.

## Estilo
- Español rioplatense, breve. Tablas para indicadores, proyectos y plan. No usar el separador '---'.
- Al empezar, decir en una línea los pasos que vienen, para que sepa dónde está.
