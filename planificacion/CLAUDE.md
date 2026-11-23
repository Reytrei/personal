# Planificación: tareas y rutinas

Sistema personal de productividad: captura en Todoist, tareas en Notion (por ahora), rutinas diaria, semanal y mensual.

- Skills: `todoist-a-notion`, `brief-matinal`, `briefing-semanal`, `weekly-review` (guía la weekly paso a paso y usa las otras dos), `planificar-semana`, `briefing-mensual`, `daily` y `end-of-day` (las del board).
- Board personal: http://localhost:4748 (código en `~/Code/task-board`, perfil personal). Start day corre `/daily`, que escribe `daily/AAAA-MM-DD.md` desde Notion; End day corre `/end-of-day`, que devuelve a Notion lo hecho. Notion sigue siendo la fuente de las tareas.
- Tareas programadas: hoy siguen corriendo en claude.ai con sus prompts originales (en el historial de git, commit cf2ce77; mandan el resultado por correo). En `tareas-programadas/` está su cron y el prompt de una línea para cuando se migren: la lógica vive en las skills y el resultado se lee en Claude Code. Se migran cuando exista el área de trabajo propia (un botón tipo "Start Day", como el del Task Board) o a Morcillo.
- Notion: Task DB `collection://020b9241-244e-42d2-9ce7-db5671397421`, Projects `collection://9c4c5809-fcf0-4783-9e5a-71e03f4eb42b`, Weeks `collection://f914dcf1-83a8-418a-86b6-6a3637a43994`, Weekly Goals `collection://3a78da52-9e8e-80ec-9194-000b92d60eca`, Capacidad `collection://31eb5037-cb83-4e8a-ba74-bd519ec05a71`, Win Today `collection://6d18da52-9e8e-828f-a39c-8793ee33189d`, Months `collection://d7aaa3c2-0e22-4427-94ac-acdc06417105`.
- Pilares (Pillars `collection://157630fd-483d-4178-82f7-92d964a03a3f`): las áreas de su vida que se mantienen siempre, sin final. Activos: Salud, Morcillas (casa, pareja con Mili, viajes, finanzas del día a día y trámites), Familia, Amigos, Life OS (sus sistemas de gestión personal), Escritura y arte, Carrera, Aprendizaje. Cada página de pilar empieza con su **Estándar** (cómo se ve bien cuidado).
  - Proyecto → uno o más pilares (relación Pillars en Projects). Todo proyecto activo lleva al menos uno.
  - Tarea → el pilar se hereda del proyecto (Pillar Rollup, no consultable por SQL: resolverlo con la relación Pillars de Projects). Solo las tareas sin proyecto llevan Pillars directo.
  - Las metas son otro eje: un proyecto puede servir a un pilar sin servir a una meta del Q.
  - Un pilar que se fusiona o termina se archiva (Status = Archived), no se borra.
  - En los reportes, un proyecto con varios pilares cuenta en todos: se muestra presencia por pilar, no un reparto exacto del tiempo.
  - Armar un sistema (por ejemplo el de finanzas) va en Life OS más el pilar del tema; operar el tema va solo en su pilar.
- Do Date = cuándo planifica hacerla. Due Date = vencimiento real. Nunca inventar ni cambiar fechas.
- Capacidad: las reglas están en la skill `brief-matinal` (360 min lunes a viernes, 0 fines de semana; Planificable = Libres × 0.7).
