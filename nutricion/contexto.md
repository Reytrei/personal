# Nutrición: contexto del sistema

Plan de alimentación de Juanma con la Lic. Camila de Horta (programa Nutre Tu Hábito) y cómo se integra con las compras.

## Piezas

- **Carpeta de Drive "Nutrición Juanma Trelles"** (id `1pDrlmx3jgxSyNi7dnAMzXIu9_-pMXoE8`):
  - Equivalencias 2026 (PDF): el archivo más importante. Porciones por grupo, en crudo, separadas en desayuno/merienda y almuerzo/cena.
  - Menú mes 1 (PDF): la tabla de porciones por comida es lo fundamental; el menú de 7 días es orientativo.
  - Lista de compras de la nutri (PDF): tipos de productos a elegir, sin marcas.
  - Registro alimentario (Google Sheets, de la nutri): 12 semanas de jueves a miércoles. No se usa por ahora.
- **Planilla "Plan y registro de comidas Juanma"** (id `1mfIChB1alVFoRp2GkjKzOCv-Q1tEYxMVxdDSMwUVGgM`, locale es_UY, fórmulas en español con punto y coma):
  - Una pestaña por semana ("Semana 10/11", etc.), copia de "Plantilla semana" (sheetId 0): martes a lunes, cada día con columnas Planificado y "Lo que comí". Filas: Mili, Desayuno, Colación, Almuerzo, Colación, Merienda, Colación, Cena, Otros, Comentarios. Bloque Porciones (filas 16–21) que completa Claude; columna P es la meta del día. En rojo lo comido que no coincide con la meta.
  - Cada semana tiene además una pestaña "Resumen dd/mm" al principio: calendario con un día por fila (Desayuno, Almuerzo, Merienda, Cena con nombres cortos; lo que se cocina ese día empieza con "COCINAR" y se resalta) y una columna "Para tener en cuenta". Debajo, la tabla "Platos para cocinar" con qué lleva cada plato para 4 porciones.
  - Juanma escribe en "Lo que comí" lo que comió (texto), Claude calcula las porciones y después se ven las diferencias.
  - Banco de comidas (sheetId 4), columnas A:K: Comida, Momento, Qué lleva, Porciones, Se cocina el doble, Notas, Última vez planificada, Proteína, Método, Base de carbohidrato, Estado (Base = dieta base, se puede repetir; Rota; Probar; Fijo; Pausado; Descartado).
  - Metas, Equivalencias (tabla con filtro), Crudo y cocido.
- **Notion**: proyecto "Nutricionista" (Command Center / Projects). Ahí van todas las tareas de este tema, en Task DB.

## Porciones diarias (22)

| Comida | Carbo | Prote | Grasa | Fruta | Vegetales |
|---|---|---|---|---|---|
| Desayuno | 1 | 2 | 1 | | |
| Almuerzo | 2 | 3 | 1 | | 1 |
| Merienda | 1 | 2 | | 1 | |
| Cena | 2 | 3 | 1 | | 1 |
| Total | 6 | 10 | 3 | 1 | 2 |

Lo importante es cumplir las porciones totales del día. Todas las medidas se usan **en crudo** (las diferencias crudo/cocido de los archivos no importan). Los alimentos se cambian dentro de su grupo. Legumbres: 0,5 carbo + 0,5 prote. Infusiones libres; colaciones no obligatorias. Cortes grasos (secreto, costilla, picaña, asado): la grasa del día viene en la carne, sin aceite agregado.

## Hábitos y criterios de planificación

- Viernes al mediodía: milanesa con su padre. Miércoles a la noche: asado con amigos.
- Cuando vienen invitados (su madre, su abuela, su padre): un corte grande de carne, como picaña o colita de cuadril, con arroz y ensalada.
- Desayuno con Mili en casa: 1 tostada con palta y 1 huevo; la otra proteína a media mañana (café con leche, yogur, queso o jamón). Sin Mili: algo sin cocinar, como pan con jamón y queso.
- Merienda: yogur con whey y granola (más 1 fruta).
- No repetir pollo en comidas seguidas.
- Recortes de suprema: en wok, o al horno marinados en yogur y especias (solos al horno no quedan bien). Pollo al horno: pata y muslo. También se pueden comprar supremas enteras y sacar filetes.
- Mientras no haga calor: ensalada solo como acompañante, no como plato principal.
- Pasta: nada entre semana. Sábado al mediodía, pasta de la fábrica de enfrente (no va a la lista). Los fideos con atún no le parecen una comida.
- **Cada vez que se cocina, 4 porciones**, así alcanza para Mili, sus padres o cualquier visita. Juanma reparte las sobras; el calendario las muestra pero se corren según quién coma en casa.
- Porción de carne: **180 g crudos** (criterio de Juanma; la tabla de la nutri dice 50 g por porción de proteína, o sea 150 g por comida). Con hueso (costilla, pata y muslo), unos 300 g por porción.
- Fin de semana libre: no se planifica (sábado al mediodía es la pasta).
- Mili come en casa todos los días (lleva comida a la oficina), salvo el jueves al mediodía, que va a la oficina sin comida.
- Incluir los cortes que le gustan (secreto, costilla de cerdo, muslos) e intercalarlos con los magros.
- Cocinar siempre para que sobre; las sobras se comen otro día. Mili come un poco menos; a veces vienen sus padres. No hilar fino con cantidades: la carne se compra cada 2 semanas como hasta ahora.
- Ir armando el banco de comidas y rotarlas.
- Arroz: por ahora blanco, no integral.
- Milanesa: se compra hecha en Flor de Pocitos (180 g = 3 prote + 1 carbo). Hay oferta web de milanesa de pollo empanada (2 kg a $800).
- Secreto: preferir el congelado (más barato y con menos grasa que el fresco).
- No poner pollo en dos comidas seguidas: la milanesa del viernes puede ser de pollo, así que el viernes a la noche no va pollo.
- Costilla de cerdo: con puré de acompañante.
- Cuando está solo, nada que no convenga cocinar para uno (como tortilla de papa).
- En el resumen semanal, cada comida nombra también sus verduras o acompañamientos.
- Ñoquis y pastas frescas: los compra en la fábrica de pasta de enfrente; no van a la lista.

## Proceso semanal

Se planifica **cada 2 semanas, el lunes**, con la skill **planificar-comidas**. El ciclo va de **miércoles a martes** (a partir del 25/11/2026; el martes 24 se cubre como día cero). El lunes se piden la carne (Flor de Pocitos) y el súper (Tata) para que llegue todo antes del miércoles.

1. Preguntar qué cambia (viajes, visitas, eventos) y qué hay en stock.
2. Armar el calendario de dos semanas con platos de 4 porciones, usando el Banco de comidas. **Dieta base** (cada una al menos 1 vez por ciclo, alguna 2): secreto al horno, carne al horno (picaña, colita, etc.), milanesa (fijo del viernes), entraña a la plancha, costilla de cerdo al horno con puré, pata y muslo al horno con papas y boniato, wok de pollo con verduras. El resto rota, con 1 plato "Probar" por ciclo (proponer 2 o 3 y que él elija).
3. Con el menú confirmado: lista de compras en Pendientes (carne de las dos semanas, súper), pedido-carniceria y armar-compra.
4. Crear en Notion (Task DB, proyecto Nutricionista) dos tareas "Comprar verdulería", una por semana, con la lista adentro, y la tarea "Planificar comidas" del lunes dentro de dos semanas.
5. El briefing semanal (lunes) calcula las porciones de lo comido, compara contra lo planificado y pregunta por los platos "Probar".

Compras: el súper se pide casi siempre a Tata (carrito en la web). La Molienda solo para cosas puntuales. Natal está enfrente: se le pasa la lista y cruza. Fruta: por ahora solo banana y mandarina (agregar otras cuando haga calor).

## Semanas

- 10/11 al 16/11: primera semana planificada (tercera versión, iterando). Mili de viaje desde el martes después del almuerzo. Miércoles al mediodía vienen su madre y su abuela. Stock al planificar: wok de pollo con verduras para unas 2 comidas. Lista cargada en Pendientes de Compras el 09/11 (IDs `menu|2026-11-10|...`): jamón, queso magro y fideos integrales en Tata, y la carne en Flor de Pocitos. Mili vuelve el lunes 16 a la mañana.
- 17/11 al 23/11: segunda semana del primer ciclo de dos semanas, con Mili en casa. Pestañas "Resumen 17/11" y "Semana 17/11".
- Ciclo 10/11 al 23/11 (rehecho el 10/11 con 4 porciones por plato): semana 1 cocina picaña (mié), secreto (jue), pata y muslo (lun); semana 2 cocina bife de vacío encebollado y wok de recortes (mar), costilla (jue), colita (vie), pata y muslo (lun). Carrito de Flor de Pocitos armado el 10/11 (picaña 1,2 kg, colita Las Piedras 1,1 kg, bife de vacío Agroluna 0,7 kg, secreto congelado 1 kg, costilla 1 kg, muslos 3 kg, milanesa de pollo 2 kg; unos $4.320). Los recortes de suprema del wok ya estaban congelados. Próximo ciclo: martes 24/11.

## Automatizaciones

- Briefing mensual (día 1, 5:28): crea las tareas mensuales (alquiler, Antel, BPS y Fonasa, cierre financiero, Monthly Review).
- Briefing semanal (lunes, 5:40): desde el 10/11 ya no crea "Plan de Comidas" ni "Super"; agrega la sección de comidas (porciones de lo comido contra lo planificado).
- Tarea "Planificar comidas" del lunes 23/11 creada en Notion; cada corrida de la skill crea la siguiente.
