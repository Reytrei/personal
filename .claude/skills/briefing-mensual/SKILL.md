---
name: "briefing-mensual"
description: "Prepara el briefing para la Monthly Review de Juan Manuel: semáforo de metas del Quarter, Weekly Goals, señales y proyectos del mes; crea las tareas recurrentes del mes y la página del mes siguiente. Usar cuando pida su briefing mensual o preparar la monthly."
---

# Briefing mensual

La Monthly es un control de rumbo sobre las metas del trimestre: este proceso prepara evidencia y sugiere; las decisiones son suyas. Lo único que escribe es: las tareas recurrentes del mes, la página del mes siguiente (y la del mes en curso si falta o está vacía), el template en la página del mes que terminó si está vacía y el bloque del briefing en esa página. No modificar ninguna otra tarea ni base.

## Referencias
- Zona horaria: America/Montevideo.
- Mes que terminó: el mes anterior al de hoy (la tarea programada corre el día 1). Mes en curso: el que empieza.
- Months: collection://d7aaa3c2-0e22-4427-94ac-acdc06417105, páginas "<Mes> - AA" en español con mayúscula inicial (ej. "Octubre - 26"). La review se hace en la página del mes que terminó. Template [Month]: id 9e844afbee8142459fdd80f21990a9c5.
- Quarters: páginas "AA - QN" (ej. "26 - Q4"); las metas están escritas en la página. Usar el Quarter al que pertenece el mes que terminó.
- Weeks: collection://f914dcf1-83a8-418a-86b6-6a3637a43994 ("Semana NN - AA", propiedades Focus y Effectiveness).
- Weekly Goals: collection://3a78da52-9e8e-80ec-9194-000b92d60eca (Done, Señal, relación con Weeks).
- Win Today (señales diarias): collection://6d18da52-9e8e-828f-a39c-8793ee33189d (filas "Señal DD/MM", texto en Señal).
- Task DB: collection://020b9241-244e-42d2-9ce7-db5671397421 (Urgencia: Esta semana, Normal, Sin apuro; vacío = Normal).
- Projects: collection://9c4c5809-fcf0-4783-9e5a-71e03f4eb42b.
- Pillars: collection://157630fd-483d-4178-82f7-92d964a03a3f (activos: Status Active; cada página empieza con su **Estándar**). El pilar de una tarea sale de su proyecto o, si no tiene, de su relación Pillars. Reglas en `planificacion/CLAUDE.md`.
- Google Calendar: principal (juanm.trelles@gmail.com), "Rutina" (ignorar los bloques de Trabajo) y "Morcillas".

## Tareas recurrentes del mes en curso
- Crearlas en Task DB con Task, Do Date (solo fecha) y Tiempo, nada más: sin proyecto, sin Urgencia, sin Due Date, sin evento de calendario.
- No duplicar: antes de crear, buscar en Task DB una tarea con el mismo nombre y Do Date dentro del mes en curso; si existe, no crearla.

| Tarea | Do Date | Tiempo |
|---|---|---|
| Pagar alquiler casa | primer lunes del mes | 5 min |
| Pagar Antel | primer lunes del mes | 5 min |
| Pagar BPS y Fonasa | primer lunes del mes | 5 min |
| Cerrar mes financiero | primer lunes del mes | 1 h |
| Monthly Review | ver abajo | 30 min |

- "Cerrar mes financiero" lleva además como contenido de la página: "Importar los movimientos del mes anterior, aprobarlos en la Bandeja y correr la skill cierre-financiero (manda el reporte por correo)."
- "Monthly Review": el primer día hábil (lunes a viernes) entre el día 1 y el 7 con Planificable de al menos 30 min. Calcular la capacidad de cada día con las reglas de la skill `brief-matinal`, y al Planificable restarle la suma de Tiempo de las tareas que ya tienen esa Do Date y Done = false (Medio día = 240 min). Si ningún día llega a 30 min, usar el primer día hábil del mes y avisarlo.

## Mes siguiente
- Crear en Months la página del mes que sigue al mes en curso (si corre el 1/12, "Enero - 27") con Name = "<Mes> - AA" y sin otras propiedades. Si ya existe, no crearla.
- Después de crearla, aplicarle el template [Month] (update_page con command apply_template, template_id 9e844afbee8142459fdd80f21990a9c5).
- Si la página del mes en curso existe pero está vacía, aplicarle también el template. Si no existe, crearla igual con el template.

## Contenido
0. Primera línea: tareas recurrentes creadas (con su fecha), las que ya existían, páginas de mes creadas y lo que no se pudo crear.
1. **Semáforo sugerido por meta del Quarter**: 🟢 / 🟡 / 🔴 con la evidencia del mes que lo justifica (tareas, proyectos, Weekly Goals). Si no hay evidencia, decirlo; él decide el color final.
2. **Weekly Goals del mes**: cumplidos y no cumplidos, y cuáles se repitieron sin cumplirse.
3. **Señales del mes**: resumen y 1 o 2 patrones candidatos que se repiten.
4. **Tareas cerradas** por proyecto y "sin proyecto"; proyectos que avanzaron y proyectos activos sin movimiento.
4b. **Recorrido por pilares**: tabla con cada pilar activo, su Estándar, la actividad del mes (tareas hechas y minutos; un proyecto con varios pilares cuenta en todos), los proyectos que lo movieron y un 🟢 / 🟡 / 🔴 sugerido contra el estándar, con la evidencia. Él decide el color. Destacar los pilares sin actividad en el mes y si eso parece decisión (mantenimiento) o abandono.
5. **Hitos del calendario** del mes (viajes, eventos importantes).
6. **Focus y Effectiveness** de cada semana del mes, y semanas sin registro.
7. **Entrenamientos**: promedio por semana vs mínimo de 3, contando los eventos de entrenamiento del calendario con el mismo criterio que la skill `briefing-semanal`.
8. **Tareas Sin apuro**: las tareas abiertas con Urgencia = Sin apuro, con su antigüedad, para que decida si suben de urgencia, siguen igual o se borran.
9. **Preguntas para decidir**: sobre las metas en 🟡 o 🔴 (ajustar, bloque fijo, pausar o soltar) y sobre los pilares en 🔴 (crear un proyecto o una tarea, o aceptarlo por ahora).

## Salida
- Buscar la página del mes que terminó. Si no existe, no crearla: avisarlo en la primera línea y no insertar nada (las tareas recurrentes y las páginas de "Mes siguiente" se crean igual).
- Si está vacía, primero aplicarle el template [Month], volver a leerla hasta ver el contenido y después seguir.
- Leer notion://docs/enhanced-markdown-spec e insertar al INICIO de la página un bloque desplegable (toggle) titulado "🤖 Briefing mensual" con todo el contenido. No tocar nada más.
- Responder con el mismo briefing, escaneable, omitiendo secciones vacías. Español, breve, sin el separador '---'. Si algún conector falla, decirlo en una línea y seguir.

## Si corre sin supervisión (tarea programada, día 1)
- No hacer preguntas.
- El briefing completo es el último mensaje. No enviar correos.
