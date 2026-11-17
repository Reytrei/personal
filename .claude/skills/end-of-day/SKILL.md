---
name: "end-of-day"
description: "Cierre del día de Juan Manuel desde el board personal (botón End day): pasa a Notion lo que se tildó en daily/AAAA-MM-DD.md (Done), crea en Task DB lo hecho sin planificar y propone qué hacer con lo pendiente. Usar cuando corra /end-of-day o pida cerrar el día."
argument-hint: "[AAAA-MM-DD]"
---

# End of day (board personal)

Devuelve a Notion lo que pasó en el board durante el día. Notion es la fuente de las tareas: después de esta corrida, Task DB refleja el día sin tocarla a mano.

`DIA` = `~/personal/daily/<fecha>.md` (fecha = el argumento, o hoy en America/Montevideo). Si no existe, decirlo y terminar.

## Paso 1: leer el día
De `DIA`, cada línea `- [ ]` / `- [x]` con su `Card: [..](<url de Notion>)` (el id de la página son los 32 caracteres hex del final de la URL), sus notas `  - HH:MM: …` (avances a medias) y las líneas de `## Done (unplanned)`.

## Paso 2: proponer
Mostrar una tabla y esperar el OK o las correcciones de Juanma:

| Tarea | En el board | Propuesta para Notion |
|---|---|---|
| Tildadas `- [x]` con Card | hecha (`done HH:MM: …`) | Done = true |
| `## Done (unplanned)` con Card | hecha | Done = true |
| `## Done (unplanned)` sin Card | hecha | Crear en Task DB con Task, Tiempo estimado, Do Date = hoy y Done = true (si es claramente una tarea ya existente en Notion, marcar esa en vez de crear) |
| Must do sin tildar | pendiente (con su última nota si la tiene) | Nueva Do Date: el próximo día hábil con Planificable libre según la base Capacidad, o sin fecha si Juanma lo prefiere |
| If time / Later sin tildar | no se tocó | Nada |

Nunca cambiar Due Date, Urgencia ni proyecto. Las notas `HH:MM: …` de una tarea pendiente se agregan al final del contenido de su página como `DD/MM HH:MM: …` (así el avance no se pierde).

Si corre sin Juanma (lo llama `/daily` para cerrar un día que quedó abierto), aplicar solo los Done y no mover fechas.

## Paso 3: aplicar
Aplicar lo aprobado en Notion. Si una escritura falla, decirlo y seguir con el resto. Después, agregar al final de `DIA`:

```
_Cerrado <HH:MM>: <N> hechas en Notion, <N> creadas, <N> reprogramadas, <N> pendientes sin cambio._
```

Esa línea es la que `/daily` busca para saber que el día quedó cerrado.

## Respuesta
La misma línea de cierre y, si quedó algo sin aplicar, qué fue.
