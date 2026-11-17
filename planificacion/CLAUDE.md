# Planificación: tareas y rutinas

Sistema personal de productividad: captura en Todoist, tareas en Notion (por ahora), rutinas diaria, semanal y mensual.

- Skills: `todoist-a-notion`, `brief-matinal`, `briefing-semanal`, `weekly-review` (guía la weekly paso a paso y usa las otras dos), `planificar-semana`, `briefing-mensual`, `daily` y `end-of-day` (las del board).
- Board personal: http://localhost:4748 (código en `~/Code/task-board`, perfil personal). Start day corre `/daily`, que escribe `daily/AAAA-MM-DD.md` desde Notion; End day corre `/end-of-day`, que devuelve a Notion lo hecho. Notion sigue siendo la fuente de las tareas.
- Tareas programadas: hoy siguen corriendo en claude.ai con sus prompts originales (en el historial de git, commit cf2ce77; mandan el resultado por correo). En `tareas-programadas/` está su cron y el prompt de una línea para cuando se migren: la lógica vive en las skills y el resultado se lee en Claude Code. Se migran cuando exista el área de trabajo propia (un botón tipo "Start Day", como el del Task Board) o a Morcillo.
- Notion: Task DB `collection://020b9241-244e-42d2-9ce7-db5671397421`, Projects `collection://9c4c5809-fcf0-4783-9e5a-71e03f4eb42b`, Weeks `collection://f914dcf1-83a8-418a-86b6-6a3637a43994`, Weekly Goals `collection://3a78da52-9e8e-80ec-9194-000b92d60eca`, Capacidad `collection://31eb5037-cb83-4e8a-ba74-bd519ec05a71`, Win Today `collection://6d18da52-9e8e-828f-a39c-8793ee33189d`, Months `collection://d7aaa3c2-0e22-4427-94ac-acdc06417105`.
- Do Date = cuándo planifica hacerla. Due Date = vencimiento real. Nunca inventar ni cambiar fechas.
- Capacidad: las reglas están en la skill `brief-matinal` (360 min lunes a viernes, 0 fines de semana; Planificable = Libres × 0.7).
