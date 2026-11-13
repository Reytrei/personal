# Compras de la casa: contexto del sistema

Cómo funcionan las compras de la casa de Juanma: dónde se anotan, cómo se importan y cómo se decide dónde comprar.

## Piezas

- **Todoist, proyecto "Lista de compras"** (id `6hr9fqPq7rQRwQrp`): Juanma anota ahí lo que falta, con la cantidad en el texto si la sabe. No está compartido con Mili.
- **Planilla "Compras"** (Google Sheets, Drive: Personal Admin/Compras, id `1BFvM-VzSs784I43GmrqDg4T4b6Ltpiy7VSO2lhKRuwU`):
  - Referencia: dónde conviene cada producto, con precio, fecha del precio, alternativa y si la marca es fija. Incluye todo lo de los primeros pedidos; lo que no vuelve a comprarse simplemente se ignora.
  - Pendientes: lo importado de Todoist (o agregado desde el panel, con ID `panel|...`) que falta comprar.
  - Historial: lo comprado (supermercado, carnicería y Mercado Libre), para sacar cantidades y frecuencias reales con el tiempo.
  - Comercios: modalidad, costo de envío, mínimo para envío gratis, medio de pago y dónde ver ofertas.
  - Parámetros: ahorro mínimo para sumar un comercio ($500 o 20% del total), tope de relleno para envío gratis (30%, caso a caso), recurrente desde 3 compras, precio vigente 30 días.
  - Carnicería: cortes de Flor de Pocitos con estado (Le gusta, Probar, Candidato, Descartado), envase, precio y uso.
- **Panel "Compras de la casa"** (https://claude.ai/artifact/4x1en6xixiAHH8HqR5RCuY): lee y escribe la planilla por el conector de Google Sheets. Muestra lo pendiente agrupado por comercio, permite agregar productos, cambiar cantidad o comercio y marcar comprado (pasa a Historial con precio opcional y borra la fila de Pendientes). También muestra compras recientes, gasto por comercio en 90 días, próximo pedido de carne (último + 14 días) y cortes en prueba.
- **Tarea programada "Morning brief"** (días hábiles 5:47): además del Inbox, importa "Lista de compras" a Pendientes (sin duplicar por ID de Todoist) y completa esas tareas en Todoist.
- **Skill "armar-compra"** (manual, lunes o martes): asistente de compras para Tata, La Molienda, Natal y verdulería. Compara precios con envío incluido, reparte por comercio solo si el ahorro neto lo justifica, sugiere ofertas de recurrentes y relleno para llegar al envío gratis, arma la lista definitiva y al confirmar pasa lo comprado a Historial.
- **Skill "pedido-carniceria"** (manual, cada unas 2 semanas): arma el pedido a Flor de Pocitos con la lista de precios de la web, arma el carrito en el navegador integrado (Juanma finaliza y paga) y registra el pedido en Historial desde el mail de confirmación.

## Comercios

- Tata: supermercado con delivery. Envío gratis desde $5.000 en Montevideo; por debajo, envío desde $220. Juanma no tiene OCA. Las búsquedas de la web tardan mucho en cargar en el navegador integrado; para precios y links sirve la API pública `https://tatauy.vtexcommercestable.com.br/api/catalog_system/pub/products/search/<texto>?sc=4` (abierta en esa misma pestaña) y la página de producto `https://www.tata.com.uy/<linkText>-<itemId>/p`, donde el botón Agregar arma el carrito.
- La Molienda: granos, legumbres, harinas, especias, frutos secos, semillas, suplementos. Delivery por PedidosYa ($199). Paga con Itaú Platinum (25%). Envío gratis si el total después del descuento supera $3.500.
- Verdulería de la esquina: va una vez por semana caminando y compra lo que le tienta; si falta algo baja en el momento. Si hay verduras en la lista, solo se asignan a la verdulería, sin más análisis. También huevos (medio maple $170 al 27/10/2026).
- Natal: limpieza, higiene y papel. Va caminando. No tiene precios online.
- Carnicería Flor de Pocitos: proceso propio (skill "pedido-carniceria"). Zona I, envío gratis desde $800. La lista de precios completa se lee con la API pública de la tienda (`/wp-json/wc/store/v1/products`); cada corte tiene una cantidad mínima y un múltiplo (por ejemplo, bife de vacío de a 0,7 kg, entraña de a 0,4 kg).
- Mercado Libre: para lo que no es comida (ferretería, hogar, suplementos). La primera vez pide captcha (lo resuelve Juanma). El envío gratis es por vendedor (la mayoría desde $1.000); el costo real por vendedor se ve en el carrito (`/gz/cart`). Al leer resultados, tomar el precio actual (`.poly-price__current`), no el tachado. Juanma finaliza y paga.
- Otros supers (no cargados como comercios todavía): Tienda Inglesa, envío gratis desde $6.000, si no $260 en Montevideo, retiro Click & Go gratis. Devoto: mínimo sin confirmar.
- Farmacias con descuento Itaú: San Roque (15%, 20% con Platinum martes y jueves; la web muestra los precios con descuento) y El Túnel (15%, 20% con Platinum lunes y miércoles).
- Farmashop: los resultados de búsqueda cargan por JavaScript; esperar unos 8 segundos antes de leer. Envío gratis desde $1.200.
- Wikimúsculos: suplementos, con precio "Descuento Itaú" (15%). Ojo con las promos atadas a comprar proteína.

## Carnicería: criterios

- Pedidos grandes cada unas 2 semanas, con unos 2 kg por tipo de carne (vaca, cerdo, pollo). Flexible si hay ofertas de algo congelable o vacuno al vacío (dura unos 90 días).
- No tiene parrilla: cortes para horno o sartén. También picada, churrascos o milanesas, no todo corte grande.
- Envase: vacuno al vacío salvo picada; secreto al vacío, costillas no; pollo sin vacío.
- Base que funciona: secreto y costilla de cerdo, muslos y recortes de suprema. Rotar sobre todo la vaca, sin innovar mucho.
- Le gustan: colita de cuadril Las Piedras, picaña Las Lilas, entraña, secreto, costilla Camposur, muslos, recortes de suprema. No le gustó la arañita.
- Tiene carne picada congelada (al 27/10/2026).

## Pedidos

- Carne #5647 (08/10/2026): muslos 3 kg, arañita, colita de cuadril Las Piedras, picaña Las Lilas, recortes de suprema, costilla y secreto. $4.062, retiro en local.
- Carne #5676 (27/10/2026): bife de vacío Agroluna 0,7 kg, entraña Agroluna 1,2 kg, secreto congelado 1 kg, costilla 1 kg, muslos 3 kg (oferta), recortes de suprema 1 kg. $3.047,80, envío gratis. En prueba: bife de vacío, entraña Agroluna y secreto congelado.
- Tata #1446455 (27/10/2026): 15 productos, $5.062, envío gratis, entrega 28/10 de 10 a 12, pago contra entrega.
- Mercado Libre #2000015733436555 (27/10/2026): creatina Cibeles 350 g ($1.725, Farmacity), 2 zapatillas Electraline 4 schuko 3 m ($922) y filtro de agua Kassel FA2 ($1.580), ambos de Universo Mágico. Total $4.227, envío gratis.

## Criterios generales

- No se hace compra mensual fija: se compra lo que falta, hasta tener claras las cantidades.
- Granos, legumbres secas, harinas, especias a granel, frutos secos y semillas suelen convenir en La Molienda; productos de marca, lácteos, pastas, enlatados, congelados, bebidas y limpieza en Tata. Lo que no es comida, comparar también en Mercado Libre.
- Marcas fijas: yerba Sara; granola tradicional Que Granola (Tata).
- En prueba: arroz Blue Patna (compra del 27/10/2026), porque el blanco Saman no lo convenció. Preguntar qué le pareció antes de repetirlo.
- No le gustaron: puré de papas Natura, arroz blanco Saman, el café que compraron (evalúa suscripción en otro lado; no sugerirlo).
- Pizza congelada (no refrigerada); la Sadia muzzarella está bien.
- Creatina: laboratorio Cibeles 350 g. Precios al 27/10/2026: Mercado Libre (Farmacity) $1.725 con envío gratis, Wikimúsculos $1.947 con Itaú, Farmashop $2.112, TuShop $2.450. No la tienen La Molienda ni San Roque.
- Agua: compró un filtro (Kassel FA2) para dejar de comprar bidones; no sugerir agua Salus salvo que la pida.
- La Molienda queda en espera hasta juntar más productos (barras de cereal y yogur Silente pendientes).
- Budinera en espera: para pan de molde, mín. 30 cm (la de Tata era chica). Puede comprarla en una tienda cerca de casa; opción ML: Tramontina 30 cm $459 + envío $185.
- Productos para probar: sin categorías preferidas ni excluidas.

## Pendientes

- Confirmar el mínimo de envío gratis de Devoto.
- Confirmar el tamaño del aceite De la Sierra de Tata.
- En el próximo pedido de carne, preguntar por el bife de vacío, la entraña Agroluna y el secreto congelado.
