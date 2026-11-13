---
name: "pedido-carniceria"
description: "Arma el pedido quincenal de Juan Manuel a la Carnicería Flor de Pocitos: revisa precios y ofertas de la web, sugiere unos 2 kg por tipo de carne según sus gustos rotando cortes de vaca, y arma el carrito en la web. Usar cuando pida el pedido de la carnicería o de carne."
---

# Pedido de la carnicería

Pedido grande cada unas 2 semanas a la Carnicería Flor de Pocitos (flordepocitos.com, Obligado 1253). Responder en español, breve, sin usar el separador '---'. Ante dudas, preguntar antes de ejecutar. Se puede armar el carrito, pero nunca finalizar la compra, ingresar datos de pago ni enviar el pedido: eso lo hace él.

## Referencias

Planilla Google Sheets "Compras" (Drive: Personal Admin/Compras), id `1BFvM-VzSs784I43GmrqDg4T4b6Ltpiy7VSO2lhKRuwU`:
- **Carnicería** (A:H): Producto (nombre exacto en la web), Tipo (Vaca, Cerdo, Pollo, Otro), Envase, Estado (Le gusta, Probar, Candidato, Descartado), Precio/kg, Fecha precio, Uso (horno, sartén, preparaciones), Notas.
- **Historial** (A:F): filas con Comercio = "Flor de Pocitos" son los pedidos anteriores.

Envío: vive en Pocitos (Zona I), envío gratis desde $800. Delivery de lunes a sábado de 8 a 19 h; lo pedido después de las 19:30 se entrega el día hábil siguiente.

## Precios y cantidades

Leer la lista completa con el navegador integrado: abrir flordepocitos.com y, desde la página, pedir `/wp-json/wc/store/v1/products?per_page=100&page=N` (páginas 1, 2, ... hasta que venga vacía). Cada producto trae `id`, nombre, `prices.price` y `prices.regular_price` (dividir por 10^`currency_minor_unit`), categorías, stock y `add_to_cart` con `minimum` y `multiple_of`. Un precio menor al regular, o la categoría "Ofertas Exclusivas Web", es una oferta. Los precios son por kg salvo que el nombre diga otra cosa.

La cantidad (en kg) solo puede ser un múltiplo de `multiple_of` y no menor que `minimum`. Muchos cortes no se pueden pedir de a 1 kg (por ejemplo, bife de vacío de a 0,7 kg, entraña de a 0,4 kg; los muslos en oferta tienen mínimo de 3 kg). Proponer siempre cantidades válidas, eligiendo la combinación que deje cada tipo de carne más cerca de su objetivo, y decir cuándo se ajustó una cantidad.

## Criterios

- **Cantidad**: unos 2 kg por tipo de carne (vaca, cerdo, pollo). No es estricto: se puede pasar si hay una oferta de algo que se congela bien o de vacuno al vacío (dura unos 90 días).
- **Sin parrilla**: solo cortes que queden bien al horno o a la sartén. No sugerir asado de tira, costillares con hueso ni otros cortes pensados para parrilla. También sirven picada, milanesas o cortes para churrascos y preparaciones: no todo tiene que ser un corte grande.
- **Envase**: vacuno siempre al vacío, salvo picada y similares. Cerdo: el secreto al vacío; las costillas no. Pollo: en general sin vacío.
- **Base que funciona** (repetir salvo que él pida otra cosa): cerdo = secreto + costilla; pollo = muslos + recortes de suprema. Si está la oferta de muslos en paquete de 3 kg, sugerirla.
- **Rotación**: rotar sobre todo la vaca, sin innovar mucho. Elegir entre los cortes "Le gusta", evitar repetir los del pedido anterior y sumar como máximo un "Probar" o "Candidato" por pedido. Para cerdo y pollo, una rotación solo como sugerencia opcional.
- **Descartados**: nunca sugerirlos.
- **Marcas**: si un corte existe en varias marcas, comparar precios y decir la diferencia; si es chica, preferir la que ya le gustó.
- **Stock en casa**: antes de sugerir picada u otros congelables, preguntar si ya tiene (por ejemplo, picada congelada).

## Pasos

1. Leer Carnicería e Historial (Flor de Pocitos). Ver qué se pidió la última vez y si hay cortes en "Probar" que ya compró.
2. Si hay "Probar" ya comprados, preguntar primero qué le parecieron y actualizar su Estado (Le gusta o Descartado).
3. Leer la lista de precios, cantidades válidas y ofertas de la web.
4. Proponer el pedido en una tabla: producto (nombre exacto de la web), envase, cantidad, precio/kg y total, con el total estimado y si llega al envío gratis. Aclarar que el total es estimado porque se cobra por el peso real.
5. Debajo: agregados opcionales (ofertas que convienen, picada para preparaciones) y 2 o 3 cortes para la próxima rotación.
6. Ajustar hasta que confirme. Si pide comparar marcas o cortes, hacerlo con los precios del día.
7. Al confirmar: actualizar en Carnicería los precios consultados y agregar los cortes nuevos (Estado "Probar").
8. **Armar el carrito** (si lo pide o acepta):
   - En el navegador integrado, desde flordepocitos.com, revisar el carrito actual con `/wp-json/wc/store/v1/cart`. Si ya tiene productos, preguntar si vaciarlo o sumar al existente antes de tocarlo.
   - Agregar cada producto pidiendo `/?add-to-cart=<id>&quantity=<kg>` con las cantidades confirmadas.
   - Volver a leer el carrito y comparar producto por producto contra lo confirmado (nombres, cantidades y total). Si algo no coincide, corregirlo o avisar.
   - Abrir `/carrito/` en el navegador. Si el panel del navegador está oculto, pedirle que lo muestre (Cmd+Shift+B en Mac o Ctrl+Shift+B en Windows, o el ícono del globo) y que finalice la compra él. Aclarar que el carrito queda en el navegador de la app, no en su Chrome ni en el celular.
9. **Registro**: cuando avise que hizo el pedido, buscar en Gmail el mail de confirmación de info@flordepocitos.com ("Hemos recibido tu pedido") y cargar cada producto en Historial con fecha, cantidad, Comercio = "Flor de Pocitos" y total, con el número de pedido en Notas (y "Para probar" en los cortes en prueba). Si no hay mail, usar lo confirmado y avisarlo.