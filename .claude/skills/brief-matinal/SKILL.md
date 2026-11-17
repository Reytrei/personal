---
name: "brief-matinal"
description: "Arma el morning brief de Juan Manuel: calendario, tareas de hoy vs horas libres, vencidas, seguimientos, Weekly Goals, correos importantes e importados de Todoist. Usar cuando pida su brief o planificar el día."
---

# Brief matinal

Objetivo: que Juan Manuel sepa en 1 minuto qué tiene hoy, si entra todo en sus horas libres y qué merece atención. Lo único que escribe este proceso es la base Capacidad (paso 1); todo lo demás es solo lectura.

## Reglas de entrega (obligatorias)
- El resultado de esta skill es el brief escrito como texto en la respuesta final. En una tarea programada, ese último mensaje es lo único que se envía por push y correo: si no existe, Juan Manuel no recibe nada.
- Si esta skill se usa después de "todoist-a-notion", la importación NO termina la tarea: siempre hay que completar todos los pasos de abajo y escribir el brief.
- No usar la skill "morning", no publicar artifacts ni crear archivos o documentos: el brief va solo como texto.
- Si un paso o un conector falla, anotarlo en una línea dentro del brief y seguir con el resto. Nunca cortar por un error parcial.
- Antes de terminar, verificar que el último mensaje contenga el brief completo (omitiendo solo secciones vacías).

## Si corre sin supervisión (tarea programada)
La rutina tiene tres pasos obligatorios; terminar uno no termina la tarea, aunque no haya habido nada que importar. No hacer preguntas ni esperar confirmaciones.
1. Correr la skill `todoist-a-notion` en modo sin supervisión (Inbox y Lista de compras) y guardar lo importado para el paso 9.
2. Armar el brief con los pasos de abajo.
3. Enviarlo por correo con send_message de Gmail a juanm.trelles@gmail.com. Asunto: "☀️ Morning brief DD/MM" (fecha de hoy). Cuerpo: el brief en texto plano, tal cual. Un solo correo por ejecución; no responder ni reenviar otros correos. Si el envío falla, reintentar una vez; si vuelve a fallar, indicarlo en la primera línea del mensaje final.

Después del envío, el brief completo es el último mensaje.

## Referencias
- Zona horaria: America/Montevideo.
- Google Calendar: leer los calendarios principal (juanm.trelles@gmail.com), "Rutina" (bloques de Trabajo; el horario cambia según el mes, leerlo del calendario y no asumirlo) y "Morcillas" (compartido, viajes y planes). Listar calendarios si los IDs cambian.
- Task DB: collection://020b9241-244e-42d2-9ce7-db5671397421 (Done checkbox, Do Date, Due Date, Status, Tiempo, Minutos, Projects, Priority).
- Capacidad: collection://31eb5037-cb83-4e8a-ba74-bd519ec05a71 (Día, Fecha, Presupuesto (min), Restado (min), Libres (min), Planificable (min), Detalle). Una fila por fecha.
- Weeks: collection://f914dcf1-83a8-418a-86b6-6a3637a43994 (página "Semana NN - AA" de la semana actual).
- Weekly Goals: collection://3a78da52-9e8e-80ec-9194-000b92d60eca (relación con Weeks; Done, Señal).
- Win Today (señales diarias): collection://6d18da52-9e8e-828f-a39c-8793ee33189d (filas "Señal DD/MM").
- Correo: Gmail. El Outlook de Juan Manuel es personal y no tiene conector disponible.

## Reglas de capacidad
- Presupuesto: 360 min de lunes a viernes dentro de la franja de 8:00 a 20:00 (incluye los huecos dentro del trabajo); 0 sábado y domingo. Si hoy es día hábil y no hay bloque de Trabajo en "Rutina" (viaje, feriado, vacaciones), avisarlo en lugar de asumir la capacidad.
- Restar la parte antes de las 20:00 de cada evento del calendario principal y de "Morcillas". Los que empiezan a las 20:00 o después no cuentan (son sociales). No restar los bloques de Trabajo ni los eventos de día completo.
- Práctica Fútbol: 90 min (desde las 18:30 por el traslado, hasta las 20:00).
- GYM de martes y viernes: se resta por su evento; si no tiene evento, restar 60 min igual.
- Libres = Presupuesto - Restado (mínimo 0). Planificable = Libres × 0.7, redondeado.
- Detalle: lista corta de lo que restó (ej. "Práctica Fútbol 90, Traumatólogo 45").

## Pasos
1. **Capacidad (hoy y los próximos 6 días)**: calcularla con las reglas y actualizar la base Capacidad. Para cada fecha: si ya hay una fila con esa Fecha, actualizarla; si no, crearla con Día = "Lun 26/10" (abreviatura del día y DD/MM). No borrar filas viejas.
2. **Calendario de hoy**: eventos con hora. Señalar viajes o eventos de todo el día.
3. **Tareas de hoy**: Task DB con Do Date = hoy y Done = false. Sumar Tiempo (5 min, 15 min, 30 min, 1 h, 2 h, Medio día = 4 h), sin contar GYM ni Weekly Review si tienen evento en el calendario. Comparar con el Planificable de hoy. Si la suma lo supera, decirlo claro y sugerir qué mover (primero las que no tienen Urgencia = Esta semana ni Due Date cercana). Listar aparte las que no tienen Tiempo.
4. **Vencidas**: Do Date < hoy y Done = false. Agrupar si son muchas.
5. **Seguimientos**: Status = Waiting con Do Date <= hoy (toca reclamar).
6. **Fechas límite próximas**: Due Date en los próximos 3 días.
7. **Weekly Goals**: los de la semana actual, con su estado.
8. **Correo**: hilos de las últimas 24 h en la bandeja principal de Gmail que pidan acción o respuesta (personas reales, trámites, bancos, facturas, plazos). Ignorar promociones, newsletters, notificaciones automáticas y los correos "Morning brief" de días anteriores. Máximo 5, una línea cada uno con qué pide.
9. **Importado de Todoist**: si en esta corrida se importaron tareas, señales o compras, listarlas con lo que se asignó. Para compras, una línea con la cantidad agregada a Pendientes y los productos.
10. **Señal pendiente**: si en Win Today no existe la fila "Señal DD/MM" del día hábil anterior (los lunes, la del viernes), terminar con: "¿Cuál fue la señal de [día]? Anotala en Todoist como 'señal: ...' y mañana la cargo."
11. **Cierre**: una pregunta corta para elegir 1 a 3 wins del día, sugiriendo candidatos alineados con los Weekly Goals.

## Formato
- Español, breve, escaneable desde el celular.
- Orden: resumen de una línea (carga del día vs planificable) → calendario → tareas → alertas (vencidas, seguimientos, plazos) → correo → importados → señal pendiente → wins.
- Omitir secciones vacías.
- No usar el separador '---'.
- El brief completo debe ser el último mensaje.