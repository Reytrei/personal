# Briefing mensual

Origen: tarea programada de claude.ai (trig_01GhYiAY1B6G3hXkJP2F2YNc). Cron: `CRON_TZ=America/Montevideo 28 5 1 * *`. Notificaciones: correo. Conectores: Notion, Gmail, Calendar, Drive, Sheets, Todoist.

## Prompt original

Briefing mensual para la Monthly Review de Juan Manuel (zona horaria America/Montevideo). Corre sin supervisión: no hagas preguntas. Responde en español, breve, sin usar el separador de tres guiones. Tu respuesta final se le envía por correo. La Monthly es un control de rumbo sobre las metas del trimestre: preparas evidencia y sugieres; las decisiones son suyas. Lo único que escribes es: las tareas recurrentes del mes (ver TAREAS RECURRENTES), la página del mes siguiente (ver MES SIGUIENTE), el bloque del briefing en Notion y el template si la página está vacía. No modifiques ninguna otra tarea ni base.

REFERENCIAS
- Months: collection://d7aaa3c2-0e22-4427-94ac-acdc06417105, páginas "<Mes> - AA" en español (ej. "Octubre - 26"). La review se hace en la página del mes que terminó (hoy es día 1: el mes anterior). Template [Month]: id 9e844afbee8142459fdd80f21990a9c5.
- Quarters: páginas "AA - QN"; las metas están escritas en la página. Usa el Quarter al que pertenece el mes que terminó.
- Weeks: collection://f914dcf1-83a8-418a-86b6-6a3637a43994 ("Semana NN - AA", propiedades Focus y Effectiveness).
- Weekly Goals: collection://3a78da52-9e8e-80ec-9194-000b92d60eca (Done, Señal, relación con Weeks).
- Win Today (señales diarias): collection://6d18da52-9e8e-828f-a39c-8793ee33189d (filas "Señal DD/MM", texto en Señal).
- Task DB: collection://020b9241-244e-42d2-9ce7-db5671397421 (Urgencia: Esta semana, Normal, Sin apuro; vacío = Normal). Projects: collection://9c4c5809-fcf0-4783-9e5a-71e03f4eb42b.
- Google Calendar: principal (juanm.trelles@gmail.com), "Rutina" (ignorar bloques de Trabajo) y "Morcillas".

TAREAS RECURRENTES DEL MES (mes en curso, el que empieza hoy)
- Créalas en Task DB con Task, Do Date (solo fecha), Tiempo y nada más: sin proyecto, sin Urgencia, sin Due Date, sin evento de calendario. En "Cerrar mes financiero" agrega además como contenido de la página: "Importar los movimientos del mes anterior, aprobarlos en la Bandeja y correr la skill cierre-financiero (manda el reporte por correo)."
- No dupliques: antes de crear, busca en Task DB una tarea con el mismo nombre y Do Date dentro del mes en curso; si existe, no la crees.
- "Pagar alquiler casa", 5 min, Do Date = primer lunes del mes.
- "Pagar Antel", 5 min, Do Date = primer lunes del mes.
- "Pagar BPS y Fonasa", 5 min, Do Date = primer lunes del mes.
- "Cerrar mes financiero", 1 h, Do Date = primer lunes del mes.
- "Monthly Review", 30 min, Do Date = el primer día hábil (lunes a viernes) entre el día 1 y el día 7 del mes con Planificable de al menos 30 min. Capacidad del día: 240 min de lunes a viernes; resta la parte antes de las 20:00 de cada evento del calendario principal y Morcillas (no los bloques de Trabajo de Rutina ni los eventos de día completo; los que empiezan a las 20:00 o más tarde no cuentan; Práctica Fútbol = 90 min; GYM de martes y viernes = 60 min si no tiene evento); Libres = 240 − restado (mínimo 0); Planificable = Libres × 0.7, menos la suma de Tiempo de las tareas que ya tienen esa Do Date y Done = false (Medio día = 240 min). Si ningún día llega a 30 min, usa el primer día hábil del mes y avísalo.

MES SIGUIENTE
- Crea en Months la página del mes que sigue al que empieza hoy (si corre el 1/12, crea "Enero - 27"), con Name = "<Mes> - AA" (mes en español con mayúscula inicial, año de dos dígitos) y sin otras propiedades.
- Si ya existe una página con ese nombre, no la crees.
- Después de crearla, aplica el template [Month] (update_page con apply_template, template_id 9e844afbee8142459fdd80f21990a9c5).
- Si la página del mes que empieza hoy existe pero está vacía, aplícale también el template [Month]. Si no existe, créala igual con el template.

CONTENIDO
0. Primera línea: tareas recurrentes creadas (con su fecha), las que ya existían, páginas de mes creadas y lo que no se pudo crear.
1. Semáforo sugerido por meta del Quarter: 🟢 / 🟡 / 🔴 con la evidencia del mes que lo justifica (tareas, proyectos, Weekly Goals). Si no hay evidencia, dilo; él decide el color final.
2. Weekly Goals del mes: cumplidos y no cumplidos, y cuáles se repitieron sin cumplirse.
3. Señales del mes: resumen y 1 o 2 patrones candidatos que se repiten.
4. Tareas cerradas por proyecto y "sin proyecto"; proyectos que avanzaron y proyectos activos sin movimiento.
5. Hitos del calendario del mes (viajes, eventos importantes).
6. Focus y Effectiveness de cada semana del mes, y semanas sin registro.
7. Entrenamientos: promedio por semana (tareas GYM hechas + fútbol) vs mínimo de 3.
8. Tareas Sin apuro: lista de las tareas abiertas con Urgencia = Sin apuro, con su antigüedad, para que decida si suben de urgencia, siguen igual o se borran.
9. Preguntas para decidir: sobre las metas en 🟡 o 🔴 (ajustar, bloque fijo, pausar o soltar).

SALIDA
- Busca la página del mes que terminó. Si no existe, no la crees: avísalo en la primera línea y solo manda el correo (las tareas recurrentes y las páginas de MES SIGUIENTE se crean igual).
- Si está vacía, primero aplica el template [Month] (update_page con apply_template, template_id 9e844afbee8142459fdd80f21990a9c5), vuelve a leerla hasta ver el contenido, y después sigue.
- Lee notion://docs/enhanced-markdown-spec e inserta al INICIO de la página un bloque desplegable (toggle) titulado "🤖 Briefing mensual" con todo el contenido. No toques nada más.
- Respuesta final: el mismo briefing, escaneable, omitiendo secciones vacías. Si algún conector falla, dilo en una línea y sigue.
