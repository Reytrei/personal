---
name: "planificar-comidas"
description: "Planifica las comidas de Juan Manuel cada dos semanas (miércoles a martes): calendario de platos de 4 porciones, lista de compras, pedido de carnicería y súper y tareas de verdulería en Notion."
---

# Planificar comidas

Se corre cada dos semanas, el lunes. Arma el calendario de comidas del ciclo de miércoles a martes que sigue, la lista de compras y los pedidos, para que todo llegue antes del miércoles. Responder en español, breve, sin usar el separador '---'. Ante dudas, preguntar antes de ejecutar. Nunca finalizar compras ni pagar.

## Referencias

- Contexto completo (reglas, hábitos, historial de ciclos): doc del proyecto `claude/nutricion-contexto.md`. Leerlo siempre primero; sus reglas mandan sobre esta skill si hay diferencias.
- Planilla "Plan y registro de comidas Juanma", id `1mfIChB1alVFoRp2GkjKzOCv-Q1tEYxMVxdDSMwUVGgM` (locale es_UY: fórmulas en español con punto y coma):
  - Metas (porciones por comida), Equivalencias (porciones en crudo), Crudo y cocido.
  - Banco de comidas (A:K): Comida, Momento, Qué lleva, Porciones, Se cocina el doble, Notas, Última vez planificada, Proteína, Método, Base de carbohidrato, Estado.
  - Plantilla semana (sheetId 0) y, por semana, las pestañas "Resumen DD/MM" y "Semana DD/MM" (DD/MM = primer día de la semana). Copiar el formato de las últimas creadas.
- Planilla "Compras", id `1BFvM-VzSs784I43GmrqDg4T4b6Ltpiy7VSO2lhKRuwU`: Pendientes (A:G), Referencia, Carnicería, Historial.
- Notion Task DB: collection://020b9241-244e-42d2-9ce7-db5671397421. Proyecto Nutricionista: página 19d8da52-9e8e-806e-a5bd-f819f436c9ad (propiedad Projects).

## Reglas de planificación

- Porciones del día: 22 (desayuno 1 carbo, 2 prote, 1 grasa; almuerzo y cena 2 carbo, 3 prote, 1 grasa, 1 veg; merienda 1 carbo, 2 prote, 1 fruta). Todo en crudo. Carne: 180 g crudos por porción (unos 300 g si tiene hueso).
- Cada plato que se cocina rinde **4 porciones**. El calendario muestra dónde va cada sobra, pero él las corre según quién coma en casa.
- Fijos: miércoles a la noche asado con amigos; viernes al mediodía milanesa con su padre (de Flor de Pocitos); sábado al mediodía pasta de la fábrica de enfrente (no va a la lista). El resto del fin de semana es libre: no se planifica.
- Mili: come todos los días (se lleva comida a la oficina), salvo el jueves al mediodía. Confirmarlo cada ciclo.
- Desayuno con Mili en casa: tostada con palta y 1 huevo, y café con 200 ml de leche a media mañana. Sin Mili: pan integral con jamón, queso y palta o frutos secos. Merienda: yogur descremado sin azúcar con whey, granola y 1 fruta.
- Sin pasta entre semana. No poner pollo en dos comidas seguidas (ojo con la milanesa de pollo del viernes). Mientras haga frío, ensalada solo como acompañante. Arroz blanco. Costilla con puré. Recortes de suprema en wok o marinados en yogur al horno; pollo al horno con pata y muslo. Preferir el secreto congelado.
- Fruta: por ahora solo banana y mandarina.
- Dieta base (Estado "Base" en el Banco de comidas): secreto al horno, carne al horno (picaña, colita, etc.), milanesa, entraña a la plancha, costilla de cerdo al horno con puré, pata y muslo al horno con papas y boniato, y wok de pollo con verduras. **Cada una va al menos 1 vez en el ciclo de dos semanas** (la milanesa ya está por el fijo del viernes) y alguna puede ir 2 veces.
- Diversidad: el resto de los platos completa el ciclo. Los "Rota" no se repiten de un ciclo al siguiente (mirar Última vez planificada). Incluir 1 plato "Probar" por ciclo: proponer 2 o 3 opciones con una línea cada una y que él elija. Variar método y base de carbohidrato entre platos seguidos. Nunca usar "Descartado" ni "Pausado".

## Pasos

1. **Contexto**: leer el doc del proyecto, el Banco de comidas, las dos últimas pestañas "Semana" (para saber qué se cocinó y qué sobró) y Pendientes.
2. **Preguntar** (en una sola tanda, con AskUserQuestion si está disponible): viajes de Mili, visitas o eventos fuera de los fijos, qué hay en stock (sobre todo carne congelada) y cuál de los 2 o 3 platos "Probar" quiere.
3. **Calendario**: proponer los platos del ciclo (cuántos según quién come: con Mili, unos 4 por semana; solo, 2 o 3) y el calendario día por día (almuerzo y cena, con COCINAR en los días que se cocina y "X que sobró" en los demás). Mostrarlo como tabla por semana y ajustar hasta que confirme.
4. **Planilla**: para cada semana, duplicar la Plantilla semana como "Semana DD/MM" y una "Resumen" anterior como "Resumen DD/MM", y completar:
   - Resumen: calendario (Desayuno, Almuerzo, Merienda, Cena con nombres cortos que incluyan las verduras, y "Para tener en cuenta": qué cocinar, qué sacar del freezer, qué comprar en la fábrica). Debajo, "Platos para cocinar" con qué lleva cada plato para 4 porciones.
   - Semana: fila Mili, Planificado de cada comida con la composición de la porción, y porciones planificadas (filas 16 a 20) en los días hábiles.
   - Banco de comidas: actualizar Última vez planificada y agregar los platos nuevos con Estado "Probar".
5. **Lista de compras**: preguntar el stock de lo que no es carne (desayuno, merienda, almacén) y cargar en Pendientes, con ID `menu|AAAA-MM-DD|producto` (fecha del miércoles de inicio):
   - Carne de las dos semanas → Flor de Pocitos.
   - Súper → Tata (salvo lo puntual de La Molienda o lo que sea de Natal).
   - Verdulería y fruta de las dos semanas: no van a Pendientes, van a las tareas de Notion (paso 7).
6. **Pedidos**: correr la skill pedido-carniceria con la carne del ciclo y después armar-compra para el súper. Recordarle que él finaliza y paga.
7. **Notion** (Task DB, proyecto Nutricionista, solo Do Date con fecha):
   - "Comprar verdulería" para el miércoles de cada semana del ciclo, 30 min, con la lista de esa semana (producto y cantidad aproximada) como contenido.
   - "Planificar comidas" para el lunes anterior al próximo ciclo (12 días después del lunes de hoy), 1 h, con una línea de contenido que indique el ciclo siguiente.
   - Antes de crear, buscar si ya existe una tarea con el mismo nombre y fecha.
8. **Cierre**: actualizar en el doc del proyecto la sección Semanas con el ciclo (platos, pedido de carne) y cualquier preferencia nueva que haya aparecido. Responder con una línea por cosa hecha: planilla, Pendientes, carrito de la carnicería, súper y tareas de Notion.