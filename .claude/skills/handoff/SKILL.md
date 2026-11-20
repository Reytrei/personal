---
name: "handoff"
description: "Deja el estado de una sesión en su tarea de Notion (sección \"## Estado\" de la página en Task DB): qué se hizo, qué falta, preguntas para Juanma, archivos y links, para que otra sesión o Juanma sigan sin leer la conversación. Usar cuando Juanma pida un handoff, diga que corta o cambia de sesión, o invoque /handoff. Usarla también sin que lo pida al terminar cada paso de trabajo sobre una tarea de Notion, y cuando la sesión queda esperando una respuesta o una acción de Juanma."
argument-hint: "[url o id de la tarea de Notion]"
---

# Handoff (personal)

Escribe el estado de la sesión **en la página de la tarea de Notion**, no en un archivo. El lector no tiene acceso a esta conversación: es otra sesión de Claude o Juanma dentro de unos días. No usar etiquetas internas ("opción B", "paso 2") sin explicarlas.

Escribe en Notion: la sección `## Estado` (y `## Historial`) de esa página y, si la tarea quedó terminada, Done = true. De `daily/` solo toca una cosa: si marcó Done, tilda la línea de esa tarea en el plan de hoy (paso 4), para que el board no la siga mostrando pendiente. Notion es la fuente.

## Paso 1: la tarea
La página de Task DB que esta sesión trabaja: el argumento, la línea `Notion task: <url>` del primer mensaje (sesiones abiertas desde el board), o la línea del plan de hoy (`~/personal/daily/<hoy>.md`, solo para leer). Si no está claro, preguntar; nunca adivinar. Si el trabajo no tiene tarea en Notion, preguntar si crear una en Task DB (Task, Tiempo y nada más) o no dejar estado.

## Paso 2: juntar hechos, no recordarlos
- Archivos creados o editados: ruta completa y si quedaron commiteados (`git status -sb` en el repo).
- Links: borradores en Gmail, planillas, páginas, publicaciones, con su estado (enviado o no, publicado o no).
- Lo que se decidió y quién lo decidió (Juanma, o propuesta de Claude sin confirmar).

## Paso 3: escribir en Notion
Leer la página. Si ya tiene `## Estado`, pasarlo a una línea al final de `## Historial` (crearla si no existe) con el formato `- DD/MM: <estado anterior en una línea>`, y reemplazar `## Estado` por el nuevo. Si no tiene, agregar `## Estado` al final del contenido. No tocar el resto de la página ni sus propiedades (salvo Done, abajo).

```markdown
## Estado
DD/MM HH:MM · sesión "<nombre de la sesión>" · <en curso | esperando a Juanma | lista para revisar | terminada>

**Hecho:** <qué se hizo, en 1 a 4 líneas>
**Falta:**
1. <próximo paso concreto, que una sesión nueva pueda arrancar sin esta conversación>
2. …
**Preguntas para Juanma:**
1. <pregunta con las opciones explicadas>
**Archivos y links:** <ruta o link: qué es y su estado>
```

Omitir los renglones vacíos (sin preguntas no va "Preguntas para Juanma"). Si la tarea quedó terminada, "Falta" no va, el estado es `terminada` y se marca Done = true en la página (única propiedad que se toca).

## Paso 4: tildar en el plan de hoy (solo si marcó Done)
En `~/personal/daily/<hoy>.md` (fecha de America/Montevideo), buscar la línea `- [ ]` cuyo `Card:` termina con el id de la página (los 32 caracteres hex) y cambiarla a `- [x]`. Nada más: no tocar otras líneas, notas ni secciones. Si el archivo no existe o la tarea no está en el plan, no hacer nada. No commitear.

## Respuesta
Una línea: qué quedó en Notion (estado y Falta 1), con el link a la página, y si se tildó en el plan de hoy.
