# Briefing semanal

Origen: tarea programada de claude.ai (trig_01F9PYGKmwmppXMRDnoJzF6k). Cron: `CRON_TZ=America/Montevideo 40 5 * * 1`. Notificaciones: correo. Conectores: Notion, Gmail, Calendar, Drive, Sheets, Todoist.

## Prompt original

Briefing semanal para la Weekly Review de Juan Manuel (zona horaria America/Montevideo). Corre sin supervisión: no hagas preguntas. Responde en español, breve, sin usar el separador de tres guiones. Tu respuesta final se le envía por correo. Las decisiones son suyas: preparas evidencia y sugieres. Lo único que escribes es: las tareas recurrentes de la semana con sus eventos de calendario, las porciones de lo comido en la planilla de comidas (ver COMIDAS), el bloque del briefing en Notion y el template si la página está vacía (ver SALIDA). No modifiques ninguna otra tarea, base ni evento.

Si la skill "briefing-semanal" está disponible, úsala: tiene el detalle de las tareas recurrentes, las reglas de capacidad y los pasos. Respeta igualmente las reglas de este mensaje (en particular: no crear "Plan de Comidas" ni "Super", y la sección COMIDAS). Si no está disponible, sigue lo de abajo.

REFERENCIAS
- Semanas ISO de lunes a domingo. Hoy es lunes: la semana que termina es la semana ISO anterior y la semana a planificar es la semana en curso.
- Weeks: collection://f914dcf1-83a8-418a-86b6-6a3637a43994, páginas "Semana NN - AA". Template de semana: página [Week], id 84e98a4b1777434c99187ab1cfbc9e64.
- Weekly Goals: collection://3a78da52-9e8e-80ec-9194-000b92d60eca. Task DB: collection://020b9241-244e-42d2-9ce7-db5671397421 (Urgencia: Esta semana, Normal, Sin apuro; vacío = Normal). Projects: collection://9c4c5809-fcf0-4783-9e5a-71e03f4eb42b.
- Quarters: páginas "AA - QN" con metas e indicadores semanales.
- Google Calendar: principal (juanm.trelles@gmail.com), "Rutina" (Trabajo, lunes a viernes 9:00 a 18:00; no listar) y "Morcillas".

TAREAS RECURRENTES (semana en curso; no duplicar si ya existen con mismo nombre y fecha)
- Lunes: "Weekly Review" (30 min) + evento de 30 min en el primer hueco libre entre 9:00 y 12:00.
- No crear "Plan de Comidas" ni "Super": la planificación de comidas, las compras y las tareas de verdulería las crea la skill planificar-comidas cada dos semanas.
- Martes y viernes: "GYM" (1 h) + evento "GYM" de 1 h en el primer hueco libre entre 7:00 y 9:00, si no entre 18:00 y 20:00. Si no hay hueco, crear la tarea sin evento y avisarlo.
- Las tareas llevan solo la fecha en Do Date. Los eventos van al calendario principal.

CAPACIDAD (semana en curso)
- Lunes a viernes 4 h base; fines de semana 0. Restar la parte antes de las 20:00 de cada evento del calendario principal y Morcillas (no Trabajo, no eventos de día completo; los que empiezan a las 20:00 o más tarde no cuentan). Práctica Fútbol cuenta de 18:30 a 20:00. Mínimo 0. Planificable = libres × 0.7. Carga agendada = suma de Tiempo (Medio día = 4 h) sin contar GYM ni Weekly Review.

COMIDAS (plan contra lo comido)
- Planilla Google Sheets "Plan y registro de comidas Juanma", id 1mfIChB1alVFoRp2GkjKzOCv-Q1tEYxMVxdDSMwUVGgM (locale es_UY). Cada semana de comidas tiene una pestaña "Semana DD/MM" (DD/MM = primer día) con columnas por día: "Planificado" y "Lo que comí". Filas 5 a 13: Desayuno, Colación, Almuerzo, Colación, Merienda, Colación, Cena, Otros, Comentarios. Filas 16 a 20: porciones de Carbohidratos, Proteínas, Grasas, Fruta y Vegetales; columna P = meta del día (6, 10, 3, 1, 2; total 22).
- Revisa los últimos 7 días hasta ayer (domingo); pueden estar repartidos en dos pestañas "Semana".
- Para cada día con algo cargado en "Lo que comí", calcula las porciones con la pestaña Equivalencias (cantidades en crudo; 180 g de carne cruda = 3 prote; legumbres 0,5 carbo + 0,5 prote) y escríbelas en la columna "Lo que comí" de ese día, filas 16 a 20. No toques las columnas "Planificado" ni otras filas.
- En el briefing: días que cumplieron las 22 porciones, faltantes o excesos por grupo, platos planificados que no se cocinaron y platos con Estado "Probar" en la pestaña "Banco de comidas" que se comieron (pregunta qué le parecieron para marcarlos Le gusta o Descartado). Si no cargó nada, dilo en una línea.

PASOS
1. Crear las tareas recurrentes.
2. Semana que termina: tareas hechas por proyecto; Weekly Goals con Señal; eventos; entrenamientos vs mínimo de 3; lo que quedó sin hacer, destacando las que tenían Urgencia = Esta semana.
3. Alineación con las metas del Quarter y proyectos activos sin próxima acción.
4. Capacidad por día (tabla) y total planificable.
5. Candidatas: Urgencia = Esta semana, Next Up, próxima acción de proyectos del Quarter, Due Date próximos 14 días y vencidas, lo que piden los indicadores del Q; con Tiempo y total vs capacidad. No incluir tareas Sin apuro sin Due Date.
6. Pipelines: Waiting y "Por decidir".
7. Comidas (ver COMIDAS).
8. Candidatos a Weekly Goal: 2 o 3 con una línea de por qué.

SALIDA
- Busca la página de la semana que termina. Si no existe, no la crees: avísalo en la primera línea y solo manda el correo (las tareas recurrentes se crean igual).
- Si la página existe pero está vacía, primero aplica el template [Week] (update_page con command apply_template y template_id 84e98a4b1777434c99187ab1cfbc9e64), vuelve a leerla hasta ver el contenido y después sigue.
- Lee notion://docs/enhanced-markdown-spec e inserta al INICIO de la página un bloque desplegable (toggle) titulado "🤖 Briefing semanal" con todo el contenido. No toques nada más de la página.
- Primera línea del briefing: lo recurrente creado, lo que ya existía y lo que no se pudo agendar.
- Tu respuesta final es el mismo briefing, escaneable, omitiendo secciones vacías. Si algún conector falla, dilo en una línea y sigue.
