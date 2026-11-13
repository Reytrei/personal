---
name: "armar-compra"
description: "Asistente de compras de la casa de Juan Manuel: compara precios con envío incluido, reparte por comercio, sugiere ofertas y relleno para envío gratis y arma la lista definitiva. Usar cuando pida armar la compra o ver qué comprar."
---

# Asistente de compras

No es un armador de listas: es un asistente que busca el menor costo total real (productos más envío) y aprovecha ofertas. Responder en español, breve, sin usar el separador '---'. Ante dudas, preguntar antes de ejecutar. Nunca hacer pedidos ni pagos.

## Referencias

Planilla Google Sheets "Compras" (Drive: Personal Admin/Compras), id `1BFvM-VzSs784I43GmrqDg4T4b6Ltpiy7VSO2lhKRuwU`:
- **Pendientes** (A:G): Fecha alta, Producto, Cantidad, Dónde comprar, Estado, Notas, ID Todoist. La importación desde Todoist ("Lista de compras") la hace la tarea programada "Morning brief"; esta skill no importa.
- **Referencia** (A:J): Producto, Categoría, Marca fija, Presentación, Dónde comprar, Precio ($), Fecha precio, Alternativa, Precio alternativa ($), Notas. Respetar lo que diga Notas (por ejemplo, "no sugerir").
- **Historial** (A:F): Fecha compra, Producto, Cantidad, Comercio, Precio total ($), Notas. Ignorar las filas de "Flor de Pocitos" (son de la carnicería).
- **Comercios**: modalidad (delivery o caminando), costo de envío, mínimo para envío gratis y sobre qué se mide, medio de pago y dónde ver ofertas. Leerla siempre; no usar montos de memoria.
- **Parámetros**: ahorro mínimo para sumar un comercio ($ y %), tope de relleno (%), compras para considerar algo recurrente y antigüedad máxima de un precio.

Comercios incluidos: Tata, La Molienda, Natal y la verdulería.

Criterio de reparto (preferencia de Juan Manuel): el súper se pide casi siempre a **Tata** por delivery. **La Molienda** solo para cosas puntuales que no hay en Tata o que él pida ahí. **Natal** está enfrente de su casa: lo que convenga ahí se le pasa como lista para que cruce. Las verduras y la fruta del plan de comidas van en las tareas de verdulería de Notion que crea la skill planificar-comidas, no en esta compra. La carnicería (Flor de Pocitos) queda fuera: tiene su propia skill ("pedido-carniceria"). Si en Pendientes aparece carne, dejarla aparte y avisar.

## Cómo consultar precios

- **Tata** (tata.com.uy): solo con el navegador. Buscar en `/s?q=<producto>`; si pide localidad, elegir "Montevideo a Costa de Oro". Los productos pueden tardar 10 a 20 segundos en cargar: esperar y volver a leer antes de dar por vacía una búsqueda. Ignorar los precios "OCA Price" (no tiene OCA). Tomar el precio de oferta si lo hay.
- **La Molienda** (lamolienda.uy): `/catalogo?q=<producto>`. Usar siempre el precio con Itaú 25% (paga con Itaú Platinum).
- **Natal**: no tiene precios online. Usar los precios de Referencia o Historial si existen; si no, dejar el producto asignado sin precio y aclararlo.
- Comparar siempre por la misma unidad (kg, litro, unidad) y aclarar cuando los productos no son equivalentes (por ejemplo, legumbres secas contra enlatadas). Si Marca fija = Sí, comparar solo esa marca.

## Pasos

1. **Leer** Pendientes (Estado = Pendiente), Referencia, Historial, Comercios y Parámetros. Si no hay pendientes, decirlo y preguntar si igual quiere ver ofertas de recurrentes.
2. **Verdulería**: frutas, verduras y huevos van directo a la verdulería, sin buscar precios ni comparar. Va una vez por semana caminando y compra lo que le tienta.
3. **Precios**: para el resto de los pendientes, usar el precio de Referencia si tiene menos días que la antigüedad máxima; si no, o si es un producto nuevo o "A definir", consultar el precio actual en los comercios que lo venden.
4. **Reparto inicial**: asignar cada producto al comercio más barato. Lo de limpieza, higiene y papel puede ir a Natal (caminando) si hay precio conocido más barato; si no, a Tata.
5. **Ajuste por envío** (para los comercios con delivery):
   - Calcular el subtotal de cada comercio con el medio de pago aplicado y compararlo con su mínimo de envío gratis, medido como indica Comercios (en La Molienda, el total después del descuento Itaú).
   - El objetivo es el menor costo total: suma de productos más envíos.
   - Sumar un comercio con delivery solo si el ahorro neto (después de su envío) llega al ahorro mínimo de Parámetros (en $ o en % del total de la compra). Si no llega, mover esos productos al comercio principal y decirlo.
   - Si un comercio no llega al envío gratis, evaluar: pagar el envío, mover productos a otro comercio o rellenar (paso 7). Mostrar el costo de cada opción.
   - Si el costo de envío de un comercio está vacío en Comercios, avisar que falta el dato, estimar con el envío gratis como referencia y pedir que lo confirme al llegar al carrito. Cuando lo confirme, ofrecer cargarlo en Comercios.
6. **Ofertas**: revisar las ofertas de cada comercio (columna "Dónde ver ofertas" de Comercios) y cruzarlas con:
   - productos recurrentes: los que aparecen en Historial al menos tantas veces como dice Parámetros. Si alguno está en oferta y es de vencimiento largo (almacén, legumbres, conservas, limpieza, papel, congelados), sugerir sumarlo aunque no esté en Pendientes, con el ahorro por unidad;
   - productos de Pendientes: si la oferta está en otro comercio, considerarla en el reparto.
   - Mientras Historial tenga pocos datos, se pueden usar como candidatos los productos de Referencia de vencimiento largo, marcándolos como "conocido, todavía no recurrente".
7. **Relleno para envío gratis**: si a un comercio le falta para el envío gratis un monto menor o igual al tope de relleno de Parámetros (% del pedido de ese comercio), sugerir cómo completarlo, en este orden: recurrentes de vencimiento largo, productos de Referencia de vencimiento largo y productos nuevos en oferta para probar (sin restricción de categoría). Comparar el relleno contra pagar el envío: rellenar conviene si lo que se suma se iba a comprar igual o si el producto nuevo vale la pena probar. Es una sugerencia caso a caso: él decide.
8. **Propuesta** (texto escaneable desde el celular):
   - Una línea de resumen: total estimado, envíos y ahorro contra comprar todo en Tata con envío.
   - Por comercio: productos con cantidad y precio estimado, subtotal, envío y total. Marcar lo que cambió de comercio respecto de Referencia y por qué.
   - Verdulería: solo la lista de lo que hay que comprar ahí.
   - Ofertas sugeridas y relleno sugerido, cada uno con el ahorro o el motivo.
   - Lo que quedó sin precio (Natal o no encontrado).
9. **Ajustes**: preguntar qué cambiar y aplicar los cambios hasta que confirme. Al confirmar, la propuesta queda como **lista definitiva** por comercio, lista para usar en la tienda o en el carrito.
9b. **Carrito de Tata** (si lo pide o acepta): en el navegador integrado, abrir tata.com.uy. Para encontrar cada producto usar la API pública `https://tatauy.vtexcommercestable.com.br/api/catalog_system/pub/products/search/<texto>?sc=4` (abierta en esa misma pestaña) y tomar `linkText` e `itemId`. Abrir la página `https://www.tata.com.uy/<linkText>-<itemId>/p` y usar el botón Agregar con la cantidad confirmada. Al terminar, abrir el carrito, comparar producto por producto contra la lista definitiva (nombres, cantidades, total y si llega al envío gratis) y corregir o avisar lo que no coincida. Él finaliza y paga: si el panel del navegador está oculto, pedirle que lo muestre (Cmd+Shift+B en Mac o Ctrl+Shift+B en Windows, o el ícono del globo) y aclarar que el carrito queda en el navegador de la app.
9c. **Natal**: pasarle la lista de lo que hay que comprar ahí, corta y escaneable.
10. **Referencia**: ofrecer agregar los productos nuevos y actualizar los precios consultados. No escribir en Referencia sin confirmación.
11. **Registro** (cuando confirme lo que compró y, si lo tiene, lo que pagó):
    - Agregar una fila en Historial por producto con fecha, cantidad, comercio y precio total (vacío si no lo sabe).
    - Borrar esas filas de Pendientes. Lo que no compró queda como Pendiente.
    - Si el precio real difiere del de Referencia, ofrecer actualizarlo.
    - Si se confirmó un costo de envío nuevo, ofrecer cargarlo en Comercios.
12. **Cierre**: una línea con productos comprados, pendientes que quedan, total gastado y ahorro estimado.