# Finanzas personales: contexto del sistema

Resumen de cómo funciona el sistema de finanzas de Juanma (Juan Manuel) y Mili: dónde están los datos, cómo se importan, cómo se clasifican y qué muestra cada vista. Sirve como contexto para cualquier conversación sobre el tema.

## Piezas del sistema

- **Hoja "Finanzas 2026"** (Google Sheets, ID `1FiCS-xYOUwxZn2sHkUtaiPEbfQHwi6h9sKdV_lDrC5k`): es la base de datos. Juanma no la usa directamente; alimenta los paneles. Las fórmulas escritas por API van con sintaxis en español y punto y coma (locale es_UY): SI, INDICE, FILAS, ESNUMERO, REDONDEAR.
- **Panel Finanzas** (https://claude.ai/artifact/7agtdXA8ZoAjPJGbhUaJQ8): la vista principal. Lee la pestaña Panel de la hoja.
- **Bandeja de movimientos** (https://claude.ai/artifact/YTViakx5LShNydN993nB1C): donde se revisan, clasifican y aprueban los movimientos importados. Escribe directo en la hoja.
- **Skill "importar-finanzas"**: carga los extractos y los gastos de Splitwise en la hoja.
- **Script de Wallbit** (Apps Script dentro de la hoja, proyecto "Proyecto sin título", archivo Wallbit.gs): sincroniza Wallbit por API todos los días. A mano se corre desde el menú "Wallbit" de la hoja (no por API). Claude puede leerlo y editarlo desde el navegador integrado (script.google.com, con la sesión de Google de Juanma iniciada).
- **Script de Itaú** (`~/Finanzas/itau_descargar.py` en la Mac de Juanma): descarga las cuentas Itaú de Juanma.

Moneda base: USD. El registro empieza el 01/10/2026 (`Config!B5`).

## Personas y "De quién"

Cada movimiento es de **Juanma**, de **Mili** o del **Conjunto** (columna "De quién"). Esto define en qué presupuesto cuenta y quién le debe a quién. No importa de qué cuenta salió el dinero: un gasto conjunto pagado desde la cuenta de Mili sigue siendo conjunto.

Cada cuenta tiene un titular: Juanma, Mili o Ambos. La cuenta conjunta real es **Itaú UYU conjunta** (la 3444197, que hasta el 29/10/2026 era de Mili). Las cuentas "Conjunta Itaú UYU/USD" son fantasma: no existen en el banco; su saldo es lo que la conjunta les debe a los dos (`Deudas!B6` y `C6`).

## Ingresos y unipersonales

Juanma y Mili tienen cada uno una empresa unipersonal que exporta servicios de software (IRPF, servicios personales, equipo provisto por la empresa cliente).

- **Impuestos**: IVA 0 (exportación de servicios). IRPF exonerado (desarrollo de software aprovechado en el exterior); requiere declaración jurada anual ante DGI y facturación electrónica. Si usaran equipo propio pasarían a IRAE sin exoneración.
- **BPS + Fonasa** (valores enero 2026, 1.ª categoría, sin cónyuge a cargo, sin hijos): Juanma $7.689 (régimen gradual, unipersonal abierta en oct. 2026; sube en oct. 2027 y después por tramos de 12 meses); Mili $8.833.
- **Juanma**: cobra por hora a Superhuman. Factura dos veces por mes y el pago llega por Wallbit unos 5 días después de la factura. El pago de los primeros días del mes corresponde a la segunda quincena del mes anterior. Facturación electrónica: $513,9 por mes. No tiene contador (un amigo contador lo ayudó a abrir la unipersonal).
- **Mili**: sueldo fijo, factura USD 5.500 por mes a Howdy (`Config!B44`). Cobra por transferencia en USD a Itaú USD Mili, una vez por mes, por el mes anterior. A veces se atrasa en facturar y le pagan dos meses juntos. Tiene contador (monto todavía no cargado).

**Ingreso neto** (`Config!B6` y `B7`) = facturación − costo empresa. Todos los porcentajes (aporte a la conjunta 40%, ahorro 40%, gasto personal 20%) y la parte de Juanma en la conjunta se calculan sobre el ingreso neto.

**Ajuste trimestral (solo Juanma)**: la facturación de Juanma se revisa cada trimestre.
- Hasta dic. 2026 se usa el estimado de USD 7.200 (`Config!B47`).
- Desde 2027, cada trimestre usa el promedio de los meses con ingreso cargado del trimestre anterior (Mensual, por mes imputado): ene–mar 2027 usa oct–dic 2026, abr–jun usa ene–mar, etc. Si el trimestre anterior no tiene datos, vuelve a `B47`.
- `Config!B43` es la facturación del trimestre del mes que muestra Presupuesto. El aporte esperado de Mensual (columna D) usa la misma regla por mes, así que es igual los tres meses del trimestre.
- Las categorías variables de Juanma se escalan en la misma proporción: `Presupuesto!D28:D44` son montos base y el factor `Config!B48` las ajusta para que el personal sea el 20% del neto (los fijos personales no se escalan). El presupuesto de Mili sigue derivándose proporcionalmente del de Juanma.
- Ojo: si el 1 del mes del cambio de trimestre todavía no entró el pago de la segunda quincena del último mes, ese mes cuenta por la mitad hasta que llegue (alrededor del día 5).

## Pestañas de la hoja

- **Movimientos**: un movimiento por fila. A–K son datos (fecha, cuenta, descripción, monto, tipo, categoría, De quién, persona, estado, notas, ID de importación); L–Q son fórmulas (moneda, monto en USD, tipo de cuenta, ámbito, mes); R es el mes imputado opcional; S es "Revisado".
- **Reglas**: clasificación automática al importar (texto, cuenta, tipo, categoría, persona, De quién).
- **Categorías**: lista de categorías con su ámbito por defecto.
- **Presupuesto**: gastos fijos y presupuesto variable por categoría (Juanma y conjunto; el de Mili se deriva proporcionalmente, salvo Costo empresa).
- **Cuentas**: titular, moneda, saldo inicial, saldo calculado y "Última exportación" de cada cuenta.
- **Deudas**: cuenta corriente de cada uno con la conjunta y deuda directa Juanma–Mili.
- **Patrimonio**: activos con % de Juanma y de Mili; historial mensual en las columnas P:S.
- **Mensual**: resumen mes a mes (sueldo, gasto, ahorro, aportes). Aporte esperado sobre la facturación trimestral menos costo empresa; objetivo de ahorro sobre el ingreso real del mes menos costo empresa; si Mili no tiene ingreso cargado se usa su facturación de Config. Columnas V–X: tipo de cambio fijo del mes (cierre USD/UYU del último día del mes anterior, GOOGLEFINANCE, vacío para meses futuros) y aporte esperado del mes en UYU de Juanma (D × V) y de Mili (`Config!B7 × B8 × V`).
- **Bonus**: fondo de ingresos extra sin categoría.
- **Wallbit**: datos crudos de la API de Wallbit. M2: saldo que devuelve la API; O2: diferencia API − hoja (USD) del último control.
- **Config**: parámetros (fecha de inicio, ingreso neto, % de aporte a la conjunta, objetivo de ahorro, tipos de cambio en vivo en A15:B40). Sección "Unipersonal" en A42:C48: facturación de cada uno (B43 trimestral para Juanma), costo empresa (calculado desde Presupuesto), estimado hasta dic. 2026 (B47) y factor de escala del presupuesto variable (B48).
- **Panel**: bloques que lee el panel. Cada bloque empieza con una fila "#nombre" seguida de los nombres de columna (kpis, cuentas, mensual, hoy, porcat, pat_hist, movimientos). El panel lee `Panel!A1:AC3004`; los bloques no pueden pisarse entre sí.

## Cuentas y cómo se importa cada una

| Cuenta | Titular | Cómo llega |
|---|---|---|
| Itaú UYU (4226957), Itaú USD (4226940) | Juanma | Script local en la Mac → CSV en `~/Finanzas/Itau` → skill |
| Itaú UYU conjunta (3444197) | Ambos | Extracto .xls subido a Drive (Finanzas/Importar/Itau Mili) con conversión a Hoja de Google → skill |
| Itaú USD Mili (3444189) | Mili | Igual que la anterior |
| Itaú UYU Mili | Mili | Cerrada (histórico hasta el 29/10/2026, saldo 0). No recibe movimientos nuevos. |
| Revolut EUR, Revolut USD | Juanma | CSV por cuenta en Drive (subcarpeta "Revolut personal") → skill |
| Revolut conjunta (EUR) | Ambos | CSV en Drive (subcarpeta "Revolut conjunta") → skill. Era la cuenta conjunta de España; no se usa para aportar. |
| Wallbit, Wallbit inversión | Juanma | Apps Script por API, todos los días a las 6:52 |
| Splitwise UYU / USD | Juanma | Correos de Splitwise en Gmail → skill |
| Santander UYU / USD | Mili | Todavía sin importar |
| Interactive Brokers | Juanma | Valor manual |

Detalles por fuente:

- **Itaú Juanma**: Juanma corre `python3 ~/Finanzas/itau_descargar.py juanma` en la Terminal (trae 7 días; `--desde AAAA-MM-DD` para más). Usa el Llavero de macOS y a veces pide un token, por eso Claude no puede correrlo. Los CSV procesados se mueven a `~/Finanzas/Itau/Procesados`.
- **Itaú Mili**: el .xls se sube desde drive.google.com con "Convertir archivos subidos al formato del editor" activado. La referencia y el destino de cada movimiento van a Notas (salvo "Otro" y la marca automática de compras con tarjeta). Las operaciones "DEB. CAMBIOS" no traen referencia en el extracto exportado. Todavía falta una regla para el sueldo de Howdy (no se sabe cómo aparece en el extracto; armarla con la primera importación que lo traiga).
- **Revolut**: solo se importan movimientos completados; los pendientes entran en la importación siguiente.
- **Wallbit**: el script guarda los movimientos en la pestaña Wallbit y los pasa a Movimientos con ID `wallbit|uuid`. Depósitos → Ingreso (sueldo; aparecen como "SUPERHUMAN INC"); compras con tarjeta → Gasto con Reglas; cashback → se omite; retenciones pendientes → entran cuando Wallbit las confirma. Retiros (WITHDRAWAL_*) → dos filas: el monto que llega, sin clasificar, y la diferencia entre lo que sale y lo que llega como comisión (Gasto sin categoría, ID `wallbit|uuid|comision`), que se clasifica caso a caso (por ejemplo, Costo empresa si es por cobrar el sueldo). Otros tipos → entran sin clasificar si el signo se deduce del nombre del tipo; si no, quedan como "Revisar" en la pestaña y se reintentan en cada sincronización. Después de cada sincronización compara el saldo USD de la API con el de Cuentas y deja la diferencia en `Wallbit!O2`; la sincronización manual la muestra en el aviso. También guarda cada día la foto del patrimonio del mes.
- **Splitwise**: Juanma es "DonPepe". Si pagó otro, se carga su parte en negativo en la cuenta Splitwise. Si pagó él, el gasto completo queda en su banco y se carga en Splitwise la parte de los demás en positivo, con la misma categoría. Los gastos que carga él mismo en Splitwise no llegan por mail: se marcan en la Bandeja con "Dividido en Splitwise".

Reglas comunes de importación:

- No se duplica: cada movimiento tiene un ID de importación (columna K) y lo ya cargado se saltea.
- Todo entra **sin revisar**: no cuenta en presupuesto, KPIs ni deudas hasta que se aprueba en la Bandeja. Los saldos sí lo incluyen.
- Después de importar se controla que el saldo de la hoja coincida con el del banco.
- La skill actualiza "Última exportación" en Cuentas; el panel marca en ámbar las cuentas con más de 7 días sin exportar.

## Migración a la cuenta conjunta (30/10/2026)

- La cuenta Itaú 3444197 pasó a ser la conjunta. Todo lo cargado hasta el 29/10 quedó en "Itaú UYU Mili" (titular Mili), sin reescribir filas.
- Cierre en "Itaú UYU Mili" y apertura en "Itaú UYU conjunta", los dos del 29/10 y revisados: el saldo de Mili ($9.751,54) entró como "Aporte a conjunta" de Mili (IDs `migracion|3444197|2026-10-29|cierre` y `|apertura`).
- En Patrimonio las dos cuentas conjuntas (Itaú UYU conjunta y Revolut conjunta) son 50% Juanma y 50% Mili.
- Reglas: TRASPASO DE 3444189 en la conjunta y TRASPASO A 3444197 desde Itaú USD Mili → Aporte a conjunta de Mili. TRASPASO A 3444197 desde Itaú UYU o Itaú USD, y TRASPASO DE 4226957/4226940 en la conjunta → Aporte a conjunta de Juanma.
- En la skill de importación, `ITAU_CUENTAS` mapea 3444197 → "Itaú UYU conjunta".
- Cuentas tiene fórmulas que solo miran las filas 4 a 19 (Movimientos!O, total de Cuentas). Una cuenta nueva se inserta dentro de ese rango, no al final. El bloque #cuentas del Panel quedó lleno (17 cuentas); otra cuenta más lo hace chocar con #patrimonio.

## Imputación de ingresos al mes

La columna "Mes" (Q, fórmula en Q1) decide en qué mes cuenta cada movimiento:

1. Si "Mes imputado" (R) tiene valor, manda R.
2. Ingreso de Juanma en Wallbit que llega del 1 al 10 del mes → mes anterior (es la segunda quincena trabajada).
3. Cualquier Ingreso de Mili → mes anterior (Howdy paga el mes vencido). Otros ingresos de Mili deben cargarse como "Ingreso extra".
4. El resto → mes de la fecha.

Si a Mili le pagan dos meses juntos, se parte en dos filas en la Bandeja y se pone el mes imputado de cada una.

## Tipos de movimiento

- **Gasto**: cuenta en el presupuesto de su categoría y bloque. Los reintegros, devoluciones y ventas que compensan un gasto (por ejemplo, vender algo comprado) se cargan como Gasto con monto positivo en la misma categoría: restan del gasto.
- **Ingreso**: sueldo.
- **Ingreso extra**: con categoría suma al presupuesto de esa categoría; sin categoría va al fondo Bonus.
- **Aporte a conjunta**: transferencia de uno de los dos a la cuenta conjunta.
- **Pago Juanma–Mili**: transferencia entre ellos; para la deuda cuenta solo la salida.
- **Cambio de moneda**: solo cuando alguien pasa plata entre sus propias cuentas en distinta moneda. Una transferencia de Mili a Juanma no es cambio de moneda.
- **Transferencia entre cuentas**, **Ahorro**: movimientos internos que no son gasto.
- **Pago a cobrar / Cobro de deuda / Reintegro**: deudas con terceros.
- **Saldo deuda Splitwise**: pagos o cobros para saldar Splitwise; no son gasto.

Las comisiones de transferencias (Wallbit, Itaú) son Gasto y se clasifican caso a caso: Costo empresa si son por cobrar el sueldo, otra categoría si no (por ejemplo, mandar plata para vacaciones).

El estado "Pendiente" es solo para deudas con terceros, nunca entre Juanma, Mili y la conjunta.

## Clasificación automática (pestaña Reglas)

- Se aplica la primera regla cuyo texto aparece en la descripción (y cuya cuenta coincide, si la regla tiene cuenta).
- "De quién" sale de la regla; si la regla no lo dice, del ámbito de la categoría (Conjunta → Conjunto; Personal → titular de la cuenta). Los que no son Gasto llevan el titular.
- Las reglas solo actúan al importar; nunca reclasifican lo ya cargado.
- Criterio: una regla solo debe marcar algo como Cambio de moneda si está limitada a una cuenta y la transferencia es entre cuentas propias. Si un concepto puede ser varias cosas (como "DEB. CAMBIOS"), mejor que no tenga regla y llegue sin clasificar a la Bandeja.
- Las devoluciones de IVA (REDIVA) se emparejan solas con su compra en la Bandeja y heredan su clasificación.

## Categorías

- Ámbito conjunto por defecto: Alquiler y gastos comunes, Servicios, Super, Casa, Vacaciones juntos.
- Ámbito personal por defecto: Salud, Deporte, Libros y cultura, Salidas, Ropa, Transporte, Escapadas, Regalos, Cuidado personal, Universidad, Infraestructura, Otros, Costo empresa.

El ámbito es solo el valor por defecto: cualquier categoría puede tener gastos personales y conjuntos. Servicios incluye suscripciones, telefonía, luz, agua, internet y limpieza. Costo empresa incluye BPS, Fonasa, facturación electrónica, contador de las unipersonales y comisiones por cobrar el sueldo.

## Presupuesto

- Gastos fijos (en UYU, convertidos a USD) más presupuesto variable por categoría, separado en Juanma y conjunto. Los gastos fijos están en `Presupuesto!A14:F25`; la columna F (Titular) se usa solo para Costo empresa.
- **Costo empresa** (fila 45): cada gasto fijo cuenta solo para su titular (Juanma o Mili), no proporcional. Se resta del ingreso antes de aplicar los porcentajes, por eso no cuenta contra el 20% personal en el Resumen (`Presupuesto!C8 = F46 − F45`, `C10 = P46 − P45`).
- Presupuesto personal de Juanma desde oct. 2026: 1.399 (20% de 6.995). Variable base: Servicios 100, Salud 55, Deporte 55, Libros y cultura 100, Salidas 235, Ropa 100, Transporte 70, Escapadas 115, Regalos 70, Cuidado personal 45, Infraestructura 45, Otros 70. Desde 2027 se escala cada trimestre con el factor `Config!B48`.
- El panel muestra el presupuesto en bloques por De quién (Juanma, Mili, Conjunto). Cada categoría se mide contra el presupuesto de su propio bloque; en rojo, lo que se pasó o tiene gasto sin presupuesto.

## Deudas

- **Saldo con la conjunta** (`Deudas!B4:E5`, una columna por moneda más Total USD). Positivo: la conjunta le debe; negativo: tiene que aportar (sirve de recordatorio para hacer la transferencia).
  - Suma los gastos del Conjunto que pagó cada uno desde sus cuentas y sus movimientos "Aporte a conjunta" en cuentas de las que es titular (la salida de su cuenta, con el signo cambiado; no cuenta la entrada en la conjunta para no duplicar).
  - Resta sus gastos personales pagados desde una cuenta "Ambos".
  - Desde el día 1 de cada mes (desde oct. 2026) resta el aporte esperado del mes en UYU (Mensual W y X) en la columna UYU, y su equivalente en USD (W o X / V) en el Total.
  - Más los saldos iniciales de la tabla H:L (deudas anteriores al 01/10/2026).
- Si el gasto es de una persona y no lo pagó ella: esa persona le debe el 100% a la conjunta.
- Ingreso de una persona que entra en la cuenta de la otra: deuda directa entre ellos.
- Nunca se reparte por porcentaje de sueldo. Solo cuentan los movimientos revisados.

## Panel

- Vistas: Juanma, Mili, Conjunto. Períodos: mes, trimestre, año.
- Secciones: avance del período, indicadores (gasto, ahorro, patrimonio, deudas), presupuesto por bloques, cuentas con fecha de exportación, evolución mensual, gasto por categoría (una dona por bloque), mes a mes, patrimonio, patrimonio por mes y movimientos.
- Colores: personal en azul, conjunto en naranja, rojo para lo pasado.
- Movimientos: por defecto los 40 más recientes del período; al buscar, todos los del período.

## Pendientes conocidos

- Las cuentas Santander de Mili todavía no se importan.
- Revolut USD no se usa por ahora.
- El aporte de 540 EUR de Juanma a Revolut conjunta (02/10) se devolvió; entra con el próximo export de Revolut. Al clasificar la devolución como "Aporte a conjunta" se compensa en Deudas.
- Las referencias de las operaciones "DEB. CAMBIOS" de Itaú no vienen en el extracto exportado; hay que cargarlas a mano en Notas.
- La foto mensual del patrimonio toma lo que la hoja tiene cargado a las 6:52; si se importa más tarde, el cierre del mes se puede corregir a mano en Patrimonio!P:S.
- Regla de importación para el sueldo de Howdy (Mili) y para los pagos de BPS y facturación electrónica (Costo empresa).
- Cargar el contador de Mili en Costo empresa.
- Verificar que "Costo empresa" aparezca bien en el Panel y en la Bandeja.
- Cuando suba el BPS de Juanma (oct. 2027), actualizar `Presupuesto!D23`.
- Aporte realizado y ahorro conjunto en Mensual no cuentan los gastos conjuntos que cada uno paga desde su propia cuenta (Deudas sí los cuenta, junto con el aporte esperado).
- Panel: la tarjeta "Saldo con la conjunta" muestra cuánto transferir en UYU (`Panel!AD2`/`AE2` = −Deudas!B4/B5 si es negativo).
- Que el panel marque en ámbar la diferencia de saldo de Wallbit (`Wallbit!O2`).
- Mensual V–X tienen fórmulas hasta la fila 18 (dic. 2027); extenderlas si se agregan meses.
