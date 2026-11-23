---
name: "importar-finanzas"
description: "Importa los extractos de Itaú, Revolut y Santander que Juan Manuel deja en su Mac (~/Finanzas: Itau, Revolut, Santander; Drive Finanzas/Importar como respaldo) y su parte de los gastos de Splitwise (desde Gmail) a su hoja Finanzas 2026, sin duplicar, aplicando sus reglas y verificando saldos. Usar cuando pida importar o cargar movimientos."
---

# Importar movimientos a Finanzas 2026

Juanma (Juan Manuel) deja los extractos de sus bancos y de los de Mili en carpetas de su Mac, dentro de `~/Finanzas`: las cuentas Itaú de los dos las baja un script, y los PDF de Revolut y Santander los baja él a mano tal como salen del banco. Las carpetas de Google Drive (Finanzas/Importar) quedan como respaldo si la Mac no está disponible. Los gastos de Splitwise llegan por correo a Gmail. Esta habilidad los carga en la pestaña Movimientos de la hoja **Finanzas 2026**, sin duplicar, clasificándolos con la pestaña Reglas, y verifica que los saldos de la hoja coincidan con los del banco. La hoja la usan Juanma, Mili y los dos en conjunto. Respondé siempre en español rioplatense, breve.

## Datos fijos

- Hoja Finanzas 2026: `1FiCS-xYOUwxZn2sHkUtaiPEbfQHwi6h9sKdV_lDrC5k`
- Carpetas locales en la Mac de Juanma (fuente principal), cada una con su subcarpeta `Procesados`:
  - `~/Finanzas/Itau`: CSV del script `~/Finanzas/itau_descargar.py`, de Juanma (`itau_juanma_*.csv`) y de Mili (`itau_mili_*.csv`)
  - `~/Finanzas/Revolut/Personal` y `~/Finanzas/Revolut/Conjunta`: PDF de Revolut tal como los baja la app
  - `~/Finanzas/Santander`: PDF `umsatz` de Santander (cuentas de Mili) tal como lo baja la web
- Respaldo en Drive (cuando la Mac no está disponible). Carpeta Importar: `1HRQtVWwNC5nxmujLGUb1BWI88bB1Pxui`
  - Subcarpeta Revolut personal: `1tojr7sVTEHEFQpPgyNtLrymumSZQ5BGA`
  - Subcarpeta Revolut conjunta: `1a1Fz6lzAYNwR88OBHaOwEfZstzsJeM3H`
  - Subcarpeta Itau Mili: `1huoI_RLWVCyQV6bxxmPAGbeUQuvsBqqs`
  - Subcarpeta Santander Mili: `1LcaqZ17qc4dvXoFlVbbAj1vj_D_oxY0t`
  - Subcarpeta Itau Juanma: `1XB19VA7v5NspeoZ9WVbyAC8vlAuSr__r`
- Carpeta Procesados de Drive: `1A62hVTBUTnxPC-uTIawkHomFNaoF6aeD`
- Panel: https://claude.ai/artifact/7agtdXA8ZoAjPJGbhUaJQ8 · Bandeja de movimientos: https://claude.ai/artifact/YTViakx5LShNydN993nB1C

Formatos que se aceptan:
- **Revolut, PDF original (Mac: `~/Finanzas/Revolut/Personal` o `Conjunta`)**: el PDF tal como lo baja la app, con una sección por divisa. La app lo genera en dos variantes según el idioma ("Estado de cuenta en EUR" con `€1,048.48`, o "Extracto en EUR" con `1.048,48€`, que además cambia algunos textos, como "Tarifa del plan Metal" en vez de "Comisión del plan Metal"): el script lee las dos. Toma el signo de las columnas Dinero saliente / Dinero entrante, usa la **Fecha valor** y controla que cada saldo cierre con el anterior. Los movimientos del bloque "Pendientes" se cargan como pendientes (ver "Movimientos pendientes"), con la fecha de la transacción. La descripción es la línea principal (y su continuación si se corta, como "Transferencia a JUAN MANUEL TRELLES & MILAGROS CANAL"), sin el detalle en letra chica. El saldo del banco es el "Saldo final" del resumen más los pendientes que quedan cargados (el banco no los descuenta del saldo final, la hoja sí). Si el título dice "compartida" o "conjunta" y el PDF está en Personal (o al revés), no se importa y se avisa. Puede haber varios PDF por carpeta (por ejemplo, uno por mes): la deduplicación lo resuelve, y los que repiten un movimiento con otro texto salen como posibles duplicados.
- **Santander, CSV original (Mac: `~/Finanzas/Santander`; el formato preferido)**: el `umsatz.csv` que baja la web, una cuenta por archivo, en Latin-1 (el script lo detecta solo). Es la misma tabla que la Hoja de Drive (ver "Santander desde Drive"): cada movimiento trae la descripción entera en una celda, así que sale igual que lo ya cargado y no aparecen falsos duplicados. El número de cuenta viene con ceros adelante (001200417441) y el script los saca. La fila "Desde: … Hasta: …" da el período, que sirve para borrar pendientes anulados.
- **Santander, PDF original (Mac: `~/Finanzas/Santander`; alternativa al CSV)**: el `umsatz.pdf` que baja la web, una cuenta por archivo. La cuenta sale del número del encabezado sin ceros adelante (001200417441 → "Santander UYU", 5200549831 → "Santander USD"). La descripción junta las columnas Tipo Movimiento y Descripción (el PDF corta palabras al final de la línea, como "DLO*PE" + "DIDOSYA": el script las vuelve a pegar). Los "DEBITO A CONFIRMAR" se cargan como pendientes (ver "Movimientos pendientes"), con la descripción limpia ("COMPRA MONTEVIDEO/DLO*PEDIDOSYA PROPINA"). El saldo del banco es el del movimiento más nuevo, que ya incluye los pendientes. Como el PDF escribe las descripciones distinto que la Hoja de Drive, un movimiento con el mismo monto y cuenta que uno ya cargado (±3 días) pero con otra descripción sale como posible duplicado. Ojo: en los movimientos confirmados el PDF a veces pega palabras que no estaban cortadas ("RUDYB", "SALADEL", "DUTYFREE"; 23/11/2026), y entonces salen como posibles duplicados de lo ya cargado: si la referencia es la misma y el saldo cierra sin ellos, no se cargan. Por eso es mejor el CSV. El PDF trae solo el período elegido en la web (por ejemplo, el mes): si la última importación de Santander quedó antes del inicio de ese período, faltan movimientos y el saldo no va a cerrar; pedile a Juanma el extracto que cubra el hueco.
- **Revolut, extracto PDF desde Drive (respaldo)**: un solo PDF por subcarpeta ("Revolut personal" o "Revolut conjunta") con una sección por divisa (EUR, USD, GBP, MAD, AUD, CLP…). No lo bajes con `download_file_content` (el base64 se trunca): leelo con Google Drive `read_file_content` y guardá el `fileContent` tal cual como `.txt` (alcanza con las secciones que tienen transacciones, los "Resumen del saldo" y los pies de página "Estado de cuenta … en XXX Generado el"). El script toma la divisa del pie de cada página, usa la **Fecha valor** (la segunda fecha) como fecha del movimiento, salta el bloque "Pendientes" (desde Drive no se cargan pendientes) y saca el signo de la diferencia de saldo (el PDF no separa salientes de entrantes). El saldo del banco es el "Saldo final" del resumen. Las divisas sin cuenta en `REVOLUT_CUENTAS` (GBP, MAD, AUD, CLP) se avisan y no se importan.
- **Revolut, extracto por cuenta (.csv)**: formato anterior. El archivo no dice de qué cuenta es, por eso va en la subcarpeta "Revolut personal" o "Revolut conjunta". La moneda sale del archivo (personal EUR → "Revolut EUR", personal USD → "Revolut USD", conjunta EUR → "Revolut conjunta"). Solo se importan los movimientos COMPLETADOS; los PENDIENTES entran en una importación posterior.
- **Revolut, extracto consolidado (.xlsx)**: formato anterior, sigue funcionando desde cualquier carpeta.
- **Itaú desde Drive (respaldo; Hoja de Google en las subcarpetas "Itau Mili" o "Itau Juanma")**: Juanma sube el .xls desde drive.google.com con la conversión a formato de Google activada, así que llega como Hoja de cálculo de Google. No se puede bajar el .xls original: el connector lo devuelve en base64 y se trunca. La Hoja se exporta a CSV con `download_file_content` y `exportMimeType: "text/csv"` (liviano, sin el logo). Si en la carpeta aparece un .xls sin convertir, no intentes bajarlo: avisale a Juanma que lo vuelva a subir desde la web con la conversión activada (Configuración de Drive → General → "Convertir archivos subidos al formato del editor de Documentos de Google"). La cuenta sale del número dentro del archivo (3444197 → "Itaú UYU conjunta", 3444189 → "Itaú USD Mili"). Desde el 30/10/2026 la 3444197 es la cuenta conjunta de Juanma y Mili (titular Ambos): lo anterior quedó en "Itaú UYU Mili", que está cerrada (saldo 0; su saldo al 29/10 pasó a la conjunta como aporte de Mili). Nunca cargues movimientos nuevos en "Itaú UYU Mili". Lo mismo vale para la subcarpeta **"Itau Juanma"** (4226957 → "Itaú UYU", 4226940 → "Itaú USD"). Las dos son el respaldo cuando el script local no anda. Si aparece un número nuevo, preguntale a Juanma qué cuenta es, agregala a `ITAU_CUENTAS` en el script y a la pestaña Cuentas (con su titular). El script copia a Notas la referencia y el destino de todos los movimientos (salvo "Otro" y la marca automática de las compras con tarjeta, "DDMMAA NOMBRE"): Juanma necesita las referencias para reconocer cada movimiento. Las operaciones "DEB. CAMBIOS" no traen referencia en el extracto exportado: si Juanma la conoce, va a Notas a mano.
- **Santander desde Drive (respaldo; Hoja de Google en la subcarpeta "Santander Mili")**: Juanma sube el archivo `umsatz` convertido a Hoja de Google (uno por cuenta); se exporta a CSV igual que Itaú (`exportMimeType: "text/csv"`). Trae una cabecera (Cliente, Cuenta, Número, Moneda, Sucursal) y la tabla `Fecha,Referencia,Concepto,Descripción,Débito,Crédito,Saldos`, del más nuevo al más viejo, con punto decimal y el débito ya en negativo. La cuenta sale de `Número` (1200417441 → "Santander UYU", 5200549831 → "Santander USD"; un número nuevo se pregunta y se agrega a `SANTANDER_CUENTAS` y a Cuentas). Los "DEBITO A CONFIRMAR" se cargan como pendientes, igual que desde la Mac. La descripción queda sin el "TARJ: ####" y "COMPRA CON TARJETA DEBITO" se acorta a "COMPRA". El saldo del banco es el del movimiento más nuevo (incluye los pendientes). Si una cuenta viene sin movimientos, el archivo igual se mueve a Procesados. El saldo inicial de las cuentas Santander (Cuentas, columna F) lo pasa Juanma: no lo cargues sin su ok.
- **Itaú Juanma y Mili, CSV del script local (`itau_juanma_*.csv` e `itau_mili_*.csv` en `~/Finanzas/Itau`)**: lo genera `itau_descargar.py`, que Juanma corre a mano en la Terminal antes de importar (`python3 ~/Finanzas/itau_descargar.py juanma mili`; por defecto trae los últimos 7 días, con `--desde AAAA-MM-DD` trae desde esa fecha). Cada persona tiene su entrada en el Llavero (`itau-finanzas-juanma`, `itau-finanzas-mili`). Claude no puede correrlo: necesita el Llavero de macOS y a veces un token (el de Mili llega a su celular). La cuenta sale de la columna `nro_cuenta` (4226957 → "Itaú UYU", 4226940 → "Itaú USD", 3444197 → "Itaú UYU conjunta", 3444189 → "Itaú USD Mili"); un número nuevo se trata igual que en Itaú desde Drive. El script escribe algunas descripciones con minúsculas ("DLO*PedidosY") y la Hoja de Drive todo en mayúsculas: la deduplicación no distingue mayúsculas, así que no se duplican. `descripcion_adicional` ("referencia - destino") va a Notas en todos los movimientos, salvo "Otro". El saldo del banco es `saldo_actual_cuenta`. Los `*_crudo.json` son para diagnóstico: no se importan. Si Itaú pide el token de inicio seguro y lo rechaza con "Ha ocurrido un error inesperado", casi siempre es un código del iToken vencido: que lo vuelva a correr escribiendo un código recién generado; si sigue fallando, que lo corra con `--diagnostico` y te pase la salida. Si el script no anda, la alternativa es exportar los extractos desde la web y subirlos convertidos a Hoja de Google a la subcarpeta "Itau Juanma" o "Itau Mili" de Drive. Los `.xls` sueltos en `~/Finanzas/Itau` no se importan desde la Mac.

- **Splitwise, correos de Gmail** (todos los grupos por igual): ver la sección "Splitwise" más abajo. Se carga solo la parte de Juanma (en Splitwise es **DonPepe**) en "Splitwise UYU" o "Splitwise USD" según la moneda del gasto. El saldo de esas cuentas es lo que debe (negativo) o le deben (positivo).

El nombre del archivo no importa, y los archivos viejos se pueden borrar: la deduplicación es por movimiento (columna K, "ID de importación"), no por archivo. En Itaú y Santander el ID incluye el saldo, que cambia si el banco agrega después otro movimiento del mismo día; por eso el script también compara sin el saldo (banco, cuenta, fecha, descripción, monto) y solo carga los que excedan a los ya cargados.

## Movimientos pendientes

Los pendientes de Revolut (bloque "Pendientes") y de Santander ("DEBITO A CONFIRMAR") se cargan apenas aparecen, para que los gastos estén en la hoja aunque el banco tarde unos días en confirmarlos. Itaú no tiene: el script solo baja movimientos confirmados.
- **Al cargarlos:** el ID empieza con `pend|` (`pend|sant|<nro>|<fecha>|<referencia>|<monto>` o `pend|rev|<cuenta>|<fecha>|<descripción>|<monto>|<n>`) y Notas dice "A confirmar". Se clasifican con Reglas y entran sin revisar, como todo lo demás. Si siguen pendientes en el próximo extracto, no se tocan.
- **Cuando se confirman:** el script busca el pendiente de la misma cuenta y signo, confirmado entre 2 días antes y 10 días después: primero con el monto exacto; si no, con un monto parecido (±15%) y la misma descripción (Revolut) o alguna palabra en común (Santander). Si lo encuentra, no agrega una fila nueva: devuelve en `actualizar` la fila a corregir (fecha, descripción, monto, Notas e ID del movimiento confirmado). La clasificación y la revisión hechas en la Bandeja quedan como estaban. Si el monto cambió (pasa con compras en otra moneda), se actualiza igual y se avisa.
- **Cuando el banco los anula:** si un pendiente ya cargado no aparece en el extracto, ni pendiente ni confirmado, y ese extracto cubre su fecha (el período del PDF), el script lo devuelve en `borrar` y se borra la fila sin preguntar (Juanma lo decidió así); se informa en el resumen. Si ningún extracto de la importación cubre su fecha, queda como está.

## Pasos

1. **Listar archivos en la Mac (fuente principal).** Con las herramientas de la Mac (`device_list_dir`; si no está conectada `~/Finanzas`, pedila con `device_request_folder_access`), listá `~/Finanzas/Itau`, `~/Finanzas/Revolut/Personal`, `~/Finanzas/Revolut/Conjunta` y `~/Finanzas/Santander`, sin entrar a `Procesados` (ignorá `.DS_Store`).
   - Itaú: tomá los `itau_juanma_*.csv` e `itau_mili_*.csv` (no los `_crudo.json`). Si falta el de alguno de los dos, o el más nuevo es de antes de hoy, preguntale a Juanma si quiere correr el script antes de seguir. Si la última importación de una cuenta Itaú es de hace más de 7 días, recordale usar `--desde` con esa fecha para no dejar huecos.
   - Revolut: tomá los `.pdf`. Santander: tomá los `.csv` (preferidos) y los `.pdf`.
   - Si la Mac no responde o se rechaza el acceso a la carpeta, usá el respaldo de Drive (paso 1b) y avisalo al final (Juanma puede agregar la carpeta con "+" → "Agregar carpeta" en la app).
1b. **Respaldo en Drive.** Con Google Drive `search_files`, buscá `parentId = '<id>'` en la carpeta Importar, en las dos subcarpetas de Revolut y en las subcarpetas Itau Mili, Itau Juanma y Santander Mili (excluí carpetas con `mimeType != 'application/vnd.google-apps.folder'`). Revisalo siempre, aunque la Mac ande: si Juanma dejó algo ahí, se importa igual (si un movimiento viene de los dos lados, la deduplicación lo resuelve). Si no hay archivos en ningún lado, seguí igual: puede haber correos de Splitwise (paso 2b).
2. **Traer los archivos.** Los de la Mac traelos con `device_stage_files` y copialos a una carpeta nueva y vacía (por ejemplo `entrada/`), sin cambiarles la extensión. Los de Drive: para cada archivo, `download_file_content` (devuelve base64); para las Hojas de Google de Itau Mili, Itau Juanma y Santander Mili, con `exportMimeType: "text/csv"`; para los PDF de Revolut, `read_file_content` guardado como `.txt`. Decodificalo y guardalo en `entrada/`, conservando la extensión original (las Hojas como `.csv`; el texto de los PDF de Revolut como `.txt`). Armá `manifiesto.json`: `[{"path": "entrada/x.pdf", "carpeta": "...", "nombre": "<nombre del archivo o título en Drive>", "exportado": "AAAA-MM-DD"}]`. Si dos archivos tienen el mismo nombre, renombralos en `entrada/` (el nombre real va en `"nombre"`). Valores de `"carpeta"`:
   - Mac: `~/Finanzas/Itau` → `"Itau local"`; `Revolut/Personal` → `"Revolut personal"`; `Revolut/Conjunta` → `"Revolut conjunta"`; `Santander` → `"Santander Mili"`.
   - Drive: el nombre de la subcarpeta (`"Revolut personal"`, `"Revolut conjunta"`, `"Itau Mili"`, `"Itau Juanma"`, `"Santander Mili"`) o `"Importar"`.
   El script distingue solo si un archivo de Revolut o Santander es el PDF original (Mac) o el texto/CSV de Drive. `"exportado"` es la fecha en que se exportó el extracto: Itaú por script, la del sello del nombre (`itau_<alias>_AAAAMMDD-HHMM.csv`); Revolut, la fecha "Generado el" del PDF (o la fecha "hasta" del nombre en los CSV viejos); Santander desde la Mac, la fecha de modificación del archivo (`mtimeMs` de `device_list_dir`) en hora de Montevideo; lo de Drive, la fecha de creación del archivo en Drive, en hora de Montevideo.
2b. **Splitwise.** Seguí la sección "Splitwise": escribí `entrada/splitwise.json` y agregalo al manifiesto como `{"path": "entrada/splitwise.json", "carpeta": "Splitwise", "nombre": "splitwise.json"}`. Si no hay correos ni archivos, decíselo y terminá.
3. **Leer el contexto de la hoja** con Google Sheets `get_values` (la hoja usa formato es_UY: fechas `dd/mm/aaaa`, números `1.234,56`):
   - `Config!B5`: fecha de inicio del registro (`desde`).
   - `Movimientos!K2:K`: IDs ya cargados.
   - `Movimientos!A2:G`: fecha, cuenta, descripción, monto, tipo, categoría y De quién de lo ya cargado. Juntalo fila a fila con los IDs de `K2:K` y armá `existentes`: `[[fecha_iso, cuenta, monto, tipo, categoria, id, descripcion, de_quien, fila]]`, donde `fila` es el número de fila de la hoja (el primer valor es la fila 2). Sirve para detectar posibles duplicados, para vincular gastos que pagó Juanma en Splitwise y para encontrar los pendientes ya cargados. No leas `A2:K` entero: la respuesta es enorme.
   - `Reglas!A4:F200` (texto, cuenta, tipo, categoría, persona, De quién), `'Categorías'!A4:B60` (categoría → ámbito por defecto), `Cuentas!A4:E30` (cuenta → titular en la columna B, moneda en la D y tipo de cuenta en la E).
   Escribí `contexto.json` con: `desde`, `ids`, `existentes`, `reglas`, `ambitos`, `tipos_cuenta`, `monedas_cuenta`, `titulares`.
4. **Procesar.** Instalá lo necesario si falta (`pip install --break-system-packages xlrd openpyxl pdfplumber`), guardá el script de abajo como `importar_finanzas.py` en otra carpeta y corré `python3 -I importar_finanzas.py manifiesto.json contexto.json > resultado.json`.
5. **Revisar antes de escribir.** Mostrale a Juanma en pocas líneas:
   - cuántos movimientos nuevos hay por cuenta;
   - los pendientes: cuántos se cargan nuevos (filas con Notas "A confirmar"), cuántos se confirmaron (`actualizar`; los que tienen `monto_cambio` con el monto de antes y el de ahora) y cuáles se van a borrar porque el banco los anuló (`borrar`);
   - los `avisos` (cuentas o divisas sin configurar, archivos fuera de lugar);
   - los `posibles_duplicados`: movimientos nuevos de Revolut con el mismo monto y cuenta que uno ya cargado en ±3 días, y de Santander lo mismo pero con otra descripción. Preguntale cuáles cargar; no los cargues sin su ok.
   - los `splitwise_revisar`: gastos que pagó él y no se pudieron vincular (sin movimiento del banco, o con más de un candidato), y los correos de gastos editados o eliminados. Los que no tienen movimiento todavía se vuelven a intentar solos en la próxima importación; no hace falta guardar nada.
   Las `filas` normales, las de `actualizar` y las de `borrar` aplicalas sin preguntar.
6. **Escribir.** Todo lo que se carga entra **sin revisar** (columna S "Revisado" vacía): no cuenta en el presupuesto, los KPIs ni las deudas hasta que Juanma o Mili lo aprueban en la Bandeja, aunque una regla ya lo haya clasificado. Los saldos de Cuentas sí lo incluyen. Nunca escribas en la columna S al importar. Buscá la primera fila vacía con `get_values` de `Movimientos!A2:A` (fila = cantidad de valores + 2) y escribí las filas con `update_values` en `Movimientos!A{n}:K{m}`. Solo columnas A a K: de la L a la Q son fórmulas. La fecha va como número de serie, el monto como número y "De quién" (columna G) como texto (Juanma, Mili, Conjunto o vacío), tal como las devuelve el script.
   Después, para cada elemento de `actualizar`, escribí en su `fila` la columna A (fecha, número de serie), C:D (descripción y monto) y J:K (Notas e ID), en tres `update_values`. No toques E a I ni la S: ahí está la clasificación y la revisión.
   Al final, los de `borrar` (vienen ordenados de la fila más alta a la más baja; respetá ese orden para que los números no se corran): conseguí el `sheetId` de la pestaña Movimientos con Google Sheets `get_spreadsheet` y borrá cada fila con `update_spreadsheet` y una solicitud `deleteDimension` (`dimension: "ROWS"`, `startIndex: fila - 1`, `endIndex: fila`). Antes de borrar, leé la columna K de esa fila y confirmá que el ID es el pendiente esperado.
7. **Verificar saldos.** Las cuentas Splitwise, las Conjunta Itaú UYU/USD (fantasma) y la cerrada "Itaú UYU Mili" no tienen saldo de banco: no se controlan. "Itaú UYU conjunta" sí (es la 3444197). Leé `Cuentas!A4:J30` (la columna J es el saldo calculado) y comparalo con `saldos_archivo` (en Revolut ya incluye los pendientes cargados). Si una cuenta no coincide, avisá la diferencia: suele ser un movimiento borrado o editado a mano, o el saldo inicial de esa cuenta (columna F).
7b. **Fecha de exportación.** Para cada cuenta de `exportado`, escribí la fecha en la columna L ("Última exportación") de su fila en `Cuentas` (buscá la fila en `Cuentas!A4:A30`), como fecha `dd/mm/aaaa`, solo si es más nueva que la que ya tiene. Si revisaste los correos de Splitwise, poné la fecha de hoy en "Splitwise UYU" y "Splitwise USD". Wallbit no se toca: su fecha sale sola de la sincronización diaria. El panel usa esta columna para avisar qué cuentas llevan más de 7 días sin exportar.
8. **Mover los archivos procesados** (los correos de Splitwise no se tocan). Si un archivo dio error o quedó sin importar, dejalo donde estaba.
   - Mac: con `device_bash`, mové cada archivo importado a la subcarpeta `Procesados` de su propia carpeta (`~/Finanzas/Itau/Procesados`, `~/Finanzas/Revolut/Personal/Procesados`, `~/Finanzas/Revolut/Conjunta/Procesados`, `~/Finanzas/Santander/Procesados`), con `mkdir -p` y `mv -n`; nunca borrar. Los CSV de Itaú van junto con su `_crudo.json` del mismo sello si existe. Si en `Procesados` ya hay un archivo con el mismo nombre (pasa con `umsatz.pdf`), agregale la fecha de exportación al nombre (`umsatz_AAAA-MM-DD.pdf`) antes de moverlo.
   - Drive: a Procesados con Google Drive `update_file` (`parentId` de Procesados).
9. **Cerrar** con un resumen corto: movimientos cargados por cuenta, que quedan sin revisar en la Bandeja (link), cuántos de ellos no tienen clasificación (tipo vacío, o Gasto sin categoría o sin De quién), y el resultado del control de saldos.

## Splitwise

1. **Buscar correos.** Gmail `search_threads` con `from:splitwise.com after:<desde en AAAA/MM/DD>` (paginá hasta el final). Leé cada hilo con `get_thread` para ver el cuerpo completo.
2. **Qué correos cuentan.**
   - Gasto nuevo agregado en cualquier grupo o entre amigos: se importa.
   - Pagos o liquidaciones de deuda ("pagó", "liquidó", "settle up"): se ignoran.
   - Gasto editado, eliminado o restaurado: no se carga solo; se lista en la revisión del paso 5 para que Juanma decida.
   - Correos de cuenta (confirmaciones, cambios de correo, inicios de sesión, recordatorios, resúmenes): se ignoran.
3. **Datos de cada gasto.** Fecha del gasto (si el correo no la trae, la del correo en hora de Montevideo), descripción, grupo, total, moneda, quién pagó y la **parte de DonPepe** (lo que le corresponde consumir, no el saldo neto). En los correos "X añadió … Debes N", pagó X y N es la parte de DonPepe. Si el correo no deja claro quién pagó o la parte, no lo incluyas: listalo en la revisión.
4. **Dos casos:**
   - **Pagó otro** (`"caso": "pago_otro"`): el gasto no pasa por ningún banco de Juanma. Se carga su parte en negativo en la cuenta Splitwise.
   - **Pagó DonPepe solo** (`"caso": "pague_yo"`): el gasto completo ya está en el banco con el que pagó (por ejemplo Itaú −5.000) y se queda así. El script busca ese movimiento y carga en la cuenta Splitwise la parte de los demás en positivo (+4.000), con el mismo tipo, categoría y De quién del movimiento del banco. Así la categoría suma solo su parte y Splitwise muestra lo que le deben. Si pagaron entre varios, no lo incluyas: listalo en la revisión.
5. **Moneda.** UYU → "Splitwise UYU"; USD → "Splitwise USD". Otra moneda: no lo incluyas y avisá.
6. **Escribir `entrada/splitwise.json`:** `[{"caso": "pago_otro" | "pague_yo", "fecha": "AAAA-MM-DD", "cuenta": "Splitwise UYU", "moneda": "UYU", "desc": "<descripción>", "grupo": "<grupo>", "total": <total>, "parte": <parte de DonPepe>, "id": "sw|<id del mensaje de Gmail>"}]`. Montos en positivo; el script pone los signos.
7. **Vínculo con el banco (lo hace el script).** Siempre después de los extractos del banco, para ver también los movimientos nuevos de la misma importación. Busca un movimiento de −total en una cuenta de la misma moneda que no sea Splitwise, con ±3 días de diferencia, que no esté ya vinculado. Si hay exactamente uno, carga la fila y en Notas deja la referencia al movimiento del banco; el ID queda `sw|<id del correo>|ref=<ID del banco>`. Si no hay ninguno o hay más de uno, no carga nada y lo devuelve en `splitwise_revisar`. Como no queda cargado, se reintenta solo en la próxima importación.
8. **Clasificación.** La hace el script con la pestaña Reglas (caso "pago_otro") o copiando la del banco (caso "pague_yo"). Si no hay categoría, queda Tipo "Gasto" sin categoría y Juanma la completa desde la Bandeja. Nunca uses la categoría de Splitwise ni inventes categorías: solo las de la pestaña Categorías.
9. Los grupos bros (hermano) y amigos se cargaron a mano el 16/10/2026 desde CSV (IDs `sw|csv|...`), con el saldo previo al 01/10 como saldo inicial de Splitwise UYU. Si aparecen correos de esos grupos con fecha de gasto anterior o igual al 16/10/2026, mostralos como posible duplicado antes de cargarlos.
10. **Saldar deudas de Splitwise.** Las transferencias para pagar o cobrar deudas de Splitwise las marca Juanma con el tipo "Saldo deuda Splitwise": no cuentan como gasto y la fórmula de Cuentas las pasa, con signo cambiado, a la cuenta Splitwise de la misma moneda. Los correos de pagos o liquidaciones se ignoran.
11. **Gastos que paga Juanma y divide.** Splitwise no le manda mail por los gastos que carga él mismo, así que esos no llegan por Gmail: Juanma los marca en la Bandeja con "Dividido en Splitwise" y su parte. La Bandeja carga la fila en "Splitwise UYU/USD" con la parte de los otros en positivo, la misma clasificación y el ID `sw|bandeja|ref=<ID del movimiento del banco>`. El script ya trata ese movimiento del banco como vinculado (por el `|ref=`), así que nunca lo vuelve a vincular. Si igual aparece un correo "pague_yo" de un gasto ya dividido en la Bandeja, no lo cargues: mencionalo en la revisión como ya registrado.

## Reglas de clasificación

El script aplica la primera regla cuyo texto aparece en la descripción (y cuya cuenta coincide, si la regla tiene cuenta). Las reglas solo actúan al importar: nunca reclasifiques movimientos ya cargados.

**De quién (columna G de Movimientos).** Cada movimiento es de **Juanma**, de **Mili** o del **Conjunto**. El script lo toma de la regla (columna F de Reglas) y, si la regla no lo dice, de la categoría: ámbito Conjunta → Conjunto; ámbito Personal → el titular de la cuenta si es una persona (Juanma o Mili); con una cuenta de titular Ambos queda vacío para elegirlo en la Bandeja. Los movimientos que no son Gasto llevan el titular de la cuenta (Ambos → Conjunto).

**Deudas.** Entre Juanma, Mili y la conjunta no se marca Pendiente: Pendiente es solo para deudas con terceros. La pestaña Deudas lleva una cuenta corriente de cada uno con la conjunta de cada moneda (UYU y USD: Conjunta Itaú, cuentas fantasma; EUR: Revolut conjunta), calculada sola: si quien pagó (titular de la cuenta) no es De quién, la conjunta le debe el 100% a quien pagó; si el gasto es de una persona y no lo pagó ella, esa persona le debe el 100% a la conjunta. Un ingreso (o ingreso extra) de una persona que entra en la cuenta de la otra genera deuda directa entre ellos. Las transferencias entre ellos van con tipo "Pago Juanma–Mili" (cuenta solo la salida). Las transferencias de cada uno a "Itaú UYU conjunta" van con tipo "Aporte a conjunta" (hay reglas para los traspasos desde Itaú UYU, Itaú USD e Itaú USD Mili): cuentan a favor de quien aporta, por la salida de su cuenta. Desde el día 1 de cada mes, Deudas resta el aporte esperado del mes en UYU, así que un saldo negativo con la conjunta es lo que esa persona tiene que transferir. Nunca se reparte por porcentaje de sueldo. Solo cuentan los movimientos revisados.

**Ingresos extra.** Un "Ingreso extra" con categoría suma al presupuesto de esa categoría (de quien sea, según De quién) en lugar de ir al fondo Bonus; sin categoría va al Bonus.

## Script

```python
#!/usr/bin/env python3
"""Importador de extractos bancarios para la hoja "Finanzas 2026".

Uso:  python3 -I importar_finanzas.py manifiesto.json contexto.json > resultado.json

manifiesto.json: [{"path": "/ruta/archivo", "carpeta": "Revolut personal" | "Revolut conjunta" | "Itau Mili" | "Itau Juanma" | "Santander Mili" | "Itau local" | "Importar" | "Splitwise", "nombre": "archivo.pdf", "exportado": "AAAA-MM-DD"}, ...]
                 Revolut y Santander: PDF original (Mac) o texto/CSV exportado de Drive; se distingue por el contenido.
contexto.json:   {"desde": "2026-10-01",
                  "ids": [ids ya cargados en Movimientos!K],
                  "existentes": [[fecha_iso, cuenta, monto, tipo, categoria, id, descripcion, de_quien, fila], ...]  (duplicados, vínculo Splitwise y pendientes),
                  "monedas_cuenta": {cuenta: moneda},
                  "reglas": [[texto, cuenta, tipo, categoria, persona, de_quien], ...],
                  "ambitos": {categoria: "Personal"|"Conjunta"},
                  "tipos_cuenta": {cuenta: "Personal"|"Conjunta"|"Personal Mili"|"Inversión"},
                  "titulares": {cuenta: "Juanma"|"Mili"|"Ambos"}}

Salida (JSON): {"filas": [[serial, cuenta, desc, monto, tipo, cat, de_quien, persona, estado, notas, id], ...],
                "actualizar": [{"fila", "A", "C", "D", "J", "K", "antes", "monto_cambio"}],  (pendientes que se confirmaron)
                "borrar": [{"fila", "detalle"}],  (pendientes anulados, de la fila más alta a la más baja)
                "posibles_duplicados": [...], "splitwise_revisar": [...], "saldos_archivo": {cuenta: saldo},
                "exportado": {cuenta: "AAAA-MM-DD"}, "avisos": [...], "pendientes_en_extractos": n}
"""
import csv, datetime, io, json, re, sys, collections

ITAU_CUENTAS = {'3444197': 'Itaú UYU conjunta', '3444189': 'Itaú USD Mili', '4226957': 'Itaú UYU', '4226940': 'Itaú USD'}  # 3444197: conjunta desde el 30/10/2026 (antes 'Itaú UYU Mili')
REVOLUT_CUENTAS = {('personal', 'EUR'): 'Revolut EUR', ('personal', 'USD'): 'Revolut USD', ('conjunta', 'EUR'): 'Revolut conjunta'}
REV_CONSOLIDADO = {'Cuenta Personal (EUR)': 'Revolut EUR', 'Cuenta Personal (USD)': 'Revolut USD', 'Cuenta Compartida (EUR)': 'Revolut conjunta'}
SANTANDER_CUENTAS = {'1200417441': 'Santander UYU', '5200549831': 'Santander USD'}
REF_TARJETA = re.compile(r'^\d{6}\s')  # marca de compra con tarjeta: DDMMAA + nombre del titular
MES = {'ene': 1, 'feb': 2, 'mar': 3, 'abr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'ago': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dic': 12}


def serial(iso):
    return (datetime.date.fromisoformat(iso) - datetime.date(1899, 12, 30)).days


def num(s):
    s = str(s).strip()
    if s in ('', 'None'):
        return 0.0
    return float(s.replace(',', ''))


# ---------- Revolut: extracto por cuenta (CSV) ----------
def leer_revolut_csv(path, carpeta, avisos):
    raw = open(path, 'rb').read().decode('utf-8-sig')
    rows = list(csv.DictReader(io.StringIO(raw)))
    if not rows:
        return [], {}, 0
    k = rows[0].keys()
    col = (lambda es, en: es if es in k else en)
    c_prod, c_fin, c_desc, c_imp, c_com, c_div, c_est, c_sal = (
        col('Producto', 'Product'), col('Fecha de finalización', 'Completed Date'), col('Descripción', 'Description'),
        col('Importe', 'Amount'), col('Comisión', 'Fee'), col('Divisa', 'Currency'), col('Estado', 'State'), col('Saldo', 'Balance'))
    tipo_cta = 'conjunta' if 'conjunta' in carpeta.lower() else 'personal' if 'personal' in carpeta.lower() else None
    if not tipo_cta:
        avisos.append(f'{path}: extracto de Revolut fuera de las subcarpetas "Revolut personal" o "Revolut conjunta"; no se sabe de qué cuenta es. No se importó.')
        return [], {}, 0
    movs, saldos, pendientes = [], {}, 0
    for r in rows:
        estado = (r.get(c_est) or '').upper()
        if estado not in ('COMPLETADO', 'COMPLETED'):
            pendientes += 1
            continue
        prod = (r.get(c_prod) or '').lower()
        if prod not in ('actual', 'current'):
            avisos.append(f'Revolut: se omitió un movimiento del producto "{r.get(c_prod)}" ({r.get(c_desc)}).')
            continue
        cuenta = REVOLUT_CUENTAS.get((tipo_cta, r.get(c_div)))
        if not cuenta:
            avisos.append(f'Revolut {tipo_cta}: no hay cuenta configurada para la moneda {r.get(c_div)}. Se omitió "{r.get(c_desc)}".')
            continue
        fecha = (r.get(c_fin) or '')[:10]
        monto = round(num(r.get(c_imp)) - num(r.get(c_com)), 2)
        movs.append(dict(fecha=fecha, cuenta=cuenta, desc=(r.get(c_desc) or '').strip(), monto=monto))
        if r.get(c_sal):
            saldos[cuenta] = num(r.get(c_sal))
    return movs, saldos, pendientes


# ---------- Revolut: extracto consolidado (xlsx) ----------
def leer_revolut_consolidado(path, avisos, desde):
    import openpyxl
    rows = list(openpyxl.load_workbook(path, data_only=True).active.iter_rows(values_only=True))
    out, cuenta_rev, en_tabla, tx = [], None, False, False
    for r in rows:
        a = r[0]
        if a == 'Cuentas Corrientes Resúmenes de transacciones':
            tx = True; continue
        if not tx:
            continue
        if isinstance(a, str) and 'Resúmenes de transacciones' in a:
            break
        if isinstance(a, str) and a.startswith('Cuenta ') and '(' in a:
            cuenta_rev = a; en_tabla = False; continue
        if a == 'Fecha':
            en_tabla = True; continue
        if a in ('Total', '---------'):
            en_tabla = False
        if en_tabla and isinstance(a, str) and re.match(r'^\d{1,2} \w{3} \d{4}$', a):
            d, m, y = a.split()
            fecha = datetime.date(int(y), MES[m[:3].lower()], int(d)).isoformat()
            if fecha < desde:
                continue
            cuenta = REV_CONSOLIDADO.get(cuenta_rev)
            if not cuenta:
                avisos.append(f'Revolut consolidado: "{cuenta_rev}" no está configurada; se omitieron sus movimientos.'); continue
            s = str(r[3]); neg = s.strip().startswith('-')
            monto = (-1 if neg else 1) * float(re.sub(r'[^0-9.]', '', s.replace(',', '')))
            out.append(dict(fecha=fecha, cuenta=cuenta, desc=str(r[1]).strip(), monto=round(monto, 2)))
    return out


# ---------- Itaú (xls) ----------
def leer_itau(path, avisos):
    import xlrd
    s = xlrd.open_workbook(path).sheet_by_index(0)
    hdr = None; nro = None; info = {}; out = []; saldo_final = None
    for i in range(s.nrows):
        r = s.row_values(i)
        if 'Nro de cuenta' in r:
            v = s.row_values(i + 1)
            nro = str(v[r.index('Nro de cuenta')]).strip().split('.')[0]
            info = {'moneda': v[r.index('Moneda')], 'titular': v[r.index('Nombre')]}
        if 'Concepto' in r and 'Saldo' in r:
            hdr = {k: r.index(k) for k in ('Fecha', 'Concepto', 'Débito', 'Crédito', 'Saldo')}; continue
        if not hdr:
            continue
        f = str(r[hdr['Fecha']]).strip(); c = str(r[hdr['Concepto']]).strip()
        if c == 'SALDO FINAL' or f == 'SALDO FINAL':
            saldo_final = r[hdr['Saldo']] if r[hdr['Saldo']] != '' else next((x for x in r[::-1] if isinstance(x, float)), None)
            continue
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', f) or c == 'SALDO ANTERIOR':
            continue
        d, m, y = map(int, f.split('/'))
        monto = round(float(r[hdr['Crédito']] or 0) - float(r[hdr['Débito']] or 0), 2)
        saldo = r[hdr['Saldo']]
        desc = re.sub(r'\s{2,}', ' ', c)
        fecha = datetime.date(y, m, d).isoformat()
        out.append(dict(fecha=fecha, cuenta=None, desc=desc, monto=monto,
                        id=f'itau|{nro}|{fecha}|{desc}|{monto!r}|{saldo!r}'))
    cuenta = ITAU_CUENTAS.get(nro)
    if not cuenta:
        avisos.append(f'Itaú: la cuenta {nro} ({info.get("moneda")}, {info.get("titular")}) no está configurada. No se importó.')
        return [], {}
    for m in out:
        m['cuenta'] = cuenta
    return out, ({cuenta: float(saldo_final)} if saldo_final not in (None, '') else {})


# ---------- Itaú (Hoja de Google exportada a CSV) ----------
def num_uy(s):
    s = str(s).strip()
    return float(s.replace('.', '').replace(',', '.')) if s else 0.0


def leer_itau_csv(path, avisos):
    rows = list(csv.reader(io.StringIO(open(path, 'rb').read().decode('utf-8-sig'))))
    hdr = None; nro = None; info = {}; out = []; saldo_final = None
    for i, r in enumerate(rows):
        if 'Nro de cuenta' in r and i + 1 < len(rows):
            v = rows[i + 1]
            nro = str(v[r.index('Nro de cuenta')]).strip().split('.')[0]
            info = {'moneda': v[r.index('Moneda')], 'titular': v[r.index('Nombre')]}
            continue
        if 'Concepto' in r and 'Saldo' in r:
            hdr = {k: r.index(k) for k in ('Fecha', 'Concepto', 'Débito', 'Crédito', 'Saldo')}
            hdr.update({k: r.index(k) for k in ('Referencia', 'Destino') if k in r}); continue
        if not hdr:
            continue
        f = r[hdr['Fecha']].strip(); c = r[hdr['Concepto']].strip()
        if c == 'SALDO FINAL' or f == 'SALDO FINAL':
            saldo_final = num_uy(r[hdr['Saldo']]); continue
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', f) or c == 'SALDO ANTERIOR':
            continue
        d, m, y = map(int, f.split('/'))
        monto = round(num_uy(r[hdr['Crédito']]) - num_uy(r[hdr['Débito']]), 2)
        saldo = num_uy(r[hdr['Saldo']])
        desc = re.sub(r'\s{2,}', ' ', c)
        fecha = datetime.date(y, m, d).isoformat()
        # La referencia (y el destino si no es "Otro") va a Notas en todos los movimientos,
        # salvo la marca automática de las compras con tarjeta ("061026 NOMBRE DEL TITULAR")
        partes = [r[hdr[k]].strip() for k in ('Referencia', 'Destino') if k in hdr and hdr[k] < len(r)]
        partes = [x for x in partes if x and x.lower() != 'otro' and not REF_TARJETA.match(x)]
        notas = ' · '.join(partes)
        out.append(dict(fecha=fecha, cuenta=None, desc=desc, monto=monto, notas=notas,
                        id=f'itau|{nro}|{fecha}|{desc}|{monto!r}|{saldo!r}'))
    cuenta = ITAU_CUENTAS.get(nro)
    if not cuenta:
        avisos.append(f'Itaú: la cuenta {nro} ({info.get("moneda")}, {info.get("titular")}) no está configurada. No se importó.')
        return [], {}
    for m in out:
        m['cuenta'] = cuenta
    return out, ({cuenta: saldo_final} if saldo_final is not None else {})


# ---------- Itaú (CSV del script local itau_descargar.py) ----------
def leer_itau_local(path, avisos):
    rows = list(csv.DictReader(io.StringIO(open(path, 'rb').read().decode('utf-8-sig'))))
    out, saldos, sin_config = [], {}, {}
    for r in rows:
        nro = str(r.get('nro_cuenta') or '').strip()
        cuenta = ITAU_CUENTAS.get(nro)
        if not cuenta:
            sin_config[nro] = (r.get('moneda'), r.get('titular'))
            continue
        fecha = (r.get('fecha') or '')[:10]
        desc = re.sub(r'\s{2,}', ' ', (r.get('descripcion') or '').strip())
        monto = round(float(r['importe']), 2)
        saldo = float(r['saldo']) if (r.get('saldo') or '').strip() not in ('', 'None') else ''
        partes = [x.strip() for x in (r.get('descripcion_adicional') or '').split(' - ')]
        notas = ' · '.join(x for x in partes if x and x.lower() != 'otro' and not REF_TARJETA.match(x))
        out.append(dict(fecha=fecha, cuenta=cuenta, desc=desc, monto=monto, notas=notas,
                        id=f'itau|{nro}|{fecha}|{desc}|{monto!r}|{saldo!r}'))
        if (r.get('saldo_actual_cuenta') or '').strip() not in ('', 'None'):
            saldos[cuenta] = float(r['saldo_actual_cuenta'])
    for nro, (mon, tit) in sin_config.items():
        avisos.append(f'Itaú: la cuenta {nro} ({mon}, {tit}) no está configurada. No se importó.')
    return out, saldos


# ---------- Revolut: extracto PDF (texto de read_file_content guardado como .txt) ----------
AMT = r'(?:AU\$|€|\$|£)?-?[\d,]+(?:\.\d{2})?(?: [A-Z]{3})?'
TX_RE = re.compile(r'(\d{1,2} [a-z]{3,4}\.? \d{4}) (\d{1,2} [a-z]{3,4}\.? \d{4}) (.+?)\s+(' + AMT + r')\s+(' + AMT + r')(?=\s)', re.S)


def _amt(s):
    return float(re.sub(r'[^0-9.\-]', '', s.replace(',', '')))


def _fecha_es(s):
    d, m, y = s.replace('.', '').split()
    return datetime.date(int(y), MES[m[:3].lower()], int(d)).isoformat()


def leer_revolut_pdf(path, carpeta, avisos):
    """Texto del PDF de Revolut (una sección por divisa; cada página termina en 'Estado de cuenta [compartida] en XXX Generado el').
    El PDF no marca si cada importe sale o entra: el signo sale de la diferencia de saldo. La fecha es la 'Fecha valor'."""
    tipo_cta = 'conjunta' if 'conjunta' in carpeta.lower() else 'personal' if 'personal' in carpeta.lower() else None
    if not tipo_cta:
        avisos.append(f'{path}: extracto de Revolut fuera de las subcarpetas "Revolut personal" o "Revolut conjunta". No se importó.')
        return [], {}, 0
    texto = open(path, encoding='utf-8').read().replace('\\*', '*')
    paginas = re.split(r'Generado el', texto)
    movs, saldos, pendientes, prev = [], {}, 0, {}
    for pag in paginas[:-1]:
        mon = re.search(r'en ([A-Z]{3})\s*$', pag)
        if not mon:
            continue
        mon = mon.group(1)
        cuenta = REVOLUT_CUENTAS.get((tipo_cta, mon))
        res = re.search(r'Cuenta \(Cuenta Corriente\) (' + AMT + r') (' + AMT + r') (' + AMT + r') (' + AMT + r')', pag)
        if res:
            prev[mon] = _amt(res.group(1))
            if cuenta:
                saldos[cuenta] = _amt(res.group(4))
        if 'Pendientes desde' in pag:
            bloque = pag.split('Pendientes desde', 1)[1].split('Transacciones de la cuenta', 1)[0]
            pendientes += len(re.findall(r'\n\d{1,2} [a-z]{3,4}\.? \d{4} ', bloque))
            pag = pag.replace(bloque, '')
        cuerpo = pag.split('Transacciones de la cuenta', 1)[-1] if 'Transacciones de la cuenta' in pag else pag
        for m in TX_RE.finditer(cuerpo):
            desc = re.sub(r'\s+', ' ', m.group(3).split('IBAN')[0]).strip()
            importe, saldo = _amt(m.group(4)), _amt(m.group(5))
            base = prev.get(mon)
            signo = 1 if base is not None and round(saldo - base, 2) == round(importe, 2) else -1
            if base is not None and round(abs(saldo - base), 2) != round(importe, 2):
                avisos.append(f'Revolut {mon}: el saldo no cierra en "{desc}" {m.group(2)}; revisá el signo.')
            prev[mon] = saldo
            if not cuenta:
                avisos.append(f'Revolut {tipo_cta}: no hay cuenta configurada para {mon}. Se omitió "{desc}" ({m.group(4)}).')
                continue
            movs.append(dict(fecha=_fecha_es(m.group(2)), cuenta=cuenta, desc=desc, monto=round(signo * importe, 2)))
    return movs, saldos, pendientes


# ---------- PDFs originales (carpetas locales de la Mac) ----------
def es_pdf(path):
    with open(path, 'rb') as f:
        return f.read(5) == b'%PDF-'


def num_auto(s):
    """Importe con símbolo o código de moneda, en formato 1,048.48 o 1.048,48 (Revolut cambia según el idioma)."""
    s = re.sub(r'[^0-9.,\-]', '', s)
    neg = s.startswith('-')
    s = s.lstrip('-')
    if not s:
        return None
    p = max(s.rfind('.'), s.rfind(','))
    if p >= 0 and len(s) - p - 1 == 3 and s.count(s[p]) >= 1 and (s.count('.') + s.count(',')) == s.count(s[p]):
        s = s.replace(s[p], '')  # solo separadores de miles (ej. 1.000 CLP)
    elif p >= 0:
        s = s[:p].replace('.', '').replace(',', '') + '.' + s[p + 1:]
    v = float(s)
    return -v if neg else v


def lineas_pdf(path):
    """Palabras de cada página agrupadas en líneas (por altura), con posición y tamaño de letra."""
    import pdfplumber
    paginas = []
    with pdfplumber.open(path) as pdf:
        for pg in pdf.pages:
            ws = sorted(pg.extract_words(extra_attrs=['size']), key=lambda w: (round(w['top']), w['x0']))
            lineas = []
            for w in ws:
                if lineas and abs(lineas[-1][0]['top'] - w['top']) < 2.5:
                    lineas[-1].append(w)
                else:
                    lineas.append([w])
            paginas.append([sorted(l, key=lambda w: w['x0']) for l in lineas])
    return paginas


def montos_linea(linea, x_min):
    """Importes de una línea a la derecha de x_min; une '0.00' + 'MAD' en un solo importe."""
    out, i = [], 0
    ws = [w for w in linea if w['x0'] >= x_min]
    while i < len(ws):
        w = ws[i]
        if re.search(r'\d', w['text']):
            x1, txt = w['x1'], w['text']
            if i + 1 < len(ws) and re.fullmatch(r'[A-Z]{3}', ws[i + 1]['text']) and ws[i + 1]['x0'] - x1 < 6:
                x1 = ws[i + 1]['x1']; i += 1
            v = num_auto(txt)
            if v is not None:
                out.append(dict(x0=w['x0'], x1=x1, v=v))
        i += 1
    return out


FECHA_ES = re.compile(r'^(\d{1,2}) ([a-z]{3,4})\.? (\d{4})')


MES_LARGO = re.compile(r'(\d{1,2}) de ([a-záéíóú]+) de (\d{4})')


def _periodo_es(txt):
    """'... desde el 1 de octubre de 2026 al 31 de octubre de 2026' -> ('2026-10-01', '2026-10-31')."""
    fs = MES_LARGO.findall(txt)
    if len(fs) < 2:
        return None
    try:
        return tuple(datetime.date(int(y), MES[m[:3].lower()], int(d)).isoformat() for d, m, y in fs[:2])
    except (KeyError, ValueError):
        return None


def leer_revolut_pdf_original(path, carpeta, avisos):
    """PDF de Revolut tal como lo baja la app ("Estado de cuenta en XXX" o "Extracto en XXX", con 1,048.48€ o 1.048,48€).
    Usa las columnas Dinero saliente / Dinero entrante para el signo y la Fecha valor como fecha.
    Los movimientos del bloque "Pendientes" se devuelven con pend=True (fecha de la transacción).
    Devuelve (movimientos, saldos, cantidad de pendientes, periodos {cuenta: [(desde, hasta)]})."""
    tipo_cta = 'conjunta' if 'conjunta' in carpeta.lower() else 'personal' if 'personal' in carpeta.lower() else None
    if not tipo_cta:
        avisos.append(f'{path}: extracto de Revolut fuera de las carpetas Personal o Conjunta. No se importó.')
        return [], {}, 0, {}
    movs, saldos, pendientes, periodos = [], {}, 0, collections.defaultdict(list)
    mon, modo, cols, actual = None, None, None, None
    for lineas in lineas_pdf(path):
        for l in lineas:
            txt = ' '.join(w['text'] for w in l)
            size = max(w['size'] for w in l)
            if size > 15:  # título de la página: "Estado de cuenta [compartida] en EUR" / "Extracto [de cuenta conjunta] en EUR"
                m = re.search(r' en ([A-Z]{3})$', txt)
                if m:
                    if m.group(1) != mon:
                        mon, modo, cols = m.group(1), None, None
                    es_conj = bool(re.search(r'compartida|conjunta', txt, re.I))
                    if es_conj != (tipo_cta == 'conjunta'):
                        avisos.append(f'{path}: el PDF dice "{txt}" pero está en la carpeta {carpeta}. No se importó.')
                        return [], {}, 0, {}
                continue
            cuenta = REVOLUT_CUENTAS.get((tipo_cta, mon))
            if txt.startswith('Cuenta (Cuenta Corriente)'):
                ms = montos_linea(l, l[0]['x1'] + 60)
                if ms and cuenta:
                    saldos[cuenta] = ms[-1]['v']
                continue
            if size > 11:  # títulos de sección
                modo = 'tx' if txt.startswith('Transacciones de la cuenta') else 'pend' if txt.startswith('Pendientes') else None
                actual = None
                per = _periodo_es(txt) if modo else None
                if per and cuenta and per not in periodos[cuenta]:
                    periodos[cuenta].append(per)
                continue
            if 'Descripción' in txt and 'Dinero saliente' in txt:  # cabezal de la tabla (Pendientes no tiene columna Saldo)
                def x(palabra, despues=0):
                    return next((w for w in l if w['text'] == palabra and w['x0'] > despues), None)
                sal = x('saliente'); sdo = x('Saldo')
                cols = dict(desc=x('Descripción')['x0'], sal=x('Dinero')['x0'], ent=x('Dinero', sal['x1'])['x0'],
                            saldo=sdo['x1'] if sdo else 1e9)
                continue
            if modo is None or not cols:
                continue
            if size < 7:
                actual = None  # detalle en letra chica: termina la descripción
                continue
            fechas = FECHA_ES.match(txt)
            if fechas and l[0]['x0'] < cols['desc'] - 30:
                resto = txt[fechas.end():].strip()
                f2 = FECHA_ES.match(resto)
                fecha = _fecha_es(' '.join(f2.groups()) if (f2 and modo == 'tx') else ' '.join(fechas.groups()))
                desc = ' '.join(w['text'] for w in l if cols['desc'] - 3 <= w['x0'] < cols['sal'] - 5)
                ms = montos_linea(l, cols['sal'] - 10)
                importe = next((m['v'] for m in ms if m['x0'] < cols['ent'] - 10), None)
                signo = -1
                if importe is None:
                    importe = next((m['v'] for m in ms if m['x0'] < cols['saldo'] - 60), None); signo = 1
                saldo = next((m['v'] for m in ms if m['x1'] > cols['saldo'] - 5), None) if modo == 'tx' else None
                if modo == 'pend':
                    pendientes += 1
                if importe is None:
                    avisos.append(f'Revolut {mon}: no encontré el importe de "{desc}" ({fecha}).'); actual = None; continue
                if not cuenta:
                    avisos.append(f'Revolut {tipo_cta}: no hay cuenta configurada para {mon}. Se omitió "{desc}" ({importe:g}).'); actual = None; continue
                actual = dict(fecha=fecha, cuenta=cuenta, desc=desc, monto=round(signo * importe, 2), saldo=saldo, pend=(modo == 'pend'))
                movs.append(actual)
            elif actual is not None:
                # Continuación de la descripción: solo líneas en letra normal enteras dentro de la columna, antes del detalle en letra chica
                if l[0]['x0'] < cols['desc'] - 3 or l[-1]['x1'] > cols['sal'] - 5:
                    actual = None
                else:
                    actual['desc'] = f"{actual['desc']} {txt}"
    # Control: el saldo de cada movimiento tiene que cerrar con el anterior
    prev = {}
    for m in movs:
        s = m.pop('saldo', None)
        if s is not None and m['cuenta'] in prev and round(prev[m['cuenta']] + m['monto'], 2) != round(s, 2):
            avisos.append(f"Revolut {m['cuenta']}: el saldo no cierra en \"{m['desc']}\" {m['fecha']}; revisá el signo.")
        if s is not None:
            prev[m['cuenta']] = s
    return movs, saldos, pendientes, dict(periodos)


def _texto_columna(ws, x_ini, x_fin):
    """Texto de una columna de varias líneas. El PDF de Santander corta palabras al final de la línea
    ("MONTEVIDEO/DLO*PE" + "DIDOSYA"): si una línea ocupa todo el ancho y termina en letra o número, se pega sin espacio."""
    lineas = collections.OrderedDict()
    for w in sorted(ws, key=lambda w: (round(w['top']), w['x0'])):
        if x_ini <= w['x0'] < x_fin:
            lineas.setdefault(round(w['top']), []).append(w)
    out = ''
    for l in lineas.values():
        t = ' '.join(w['text'] for w in l)
        if out:
            out += '' if (pegar and re.search(r'[A-Za-z0-9]$', out)) else ' '
        out += t
        pegar = l[0]['x0'] <= x_ini + 8 and l[-1]['x1'] >= x_fin - 8
    return re.sub(r'\s+', ' ', out).strip()


def limpiar_pendiente_santander(conc):
    """'DEBITO A CONFIRMAR BANRED COMPRA 581264 - MONTEVIDEO/DLO*PEDIDOSYA PROPINAVIS3 -' -> 'COMPRA MONTEVIDEO/DLO*PEDIDOSYA PROPINA'."""
    s = re.sub(r'^DEBITO A CONFIRMAR\s*', '', conc, flags=re.I)
    s = re.sub(r'^BANRED\s+', '', s, flags=re.I)
    s = re.sub(r'\b\d{6}\s*-\s*', '', s)
    s = re.sub(r'\s*VIS\d*\s*-?\s*$', '', s)
    return re.sub(r'\s+', ' ', s).strip(' -') or conc


def leer_santander_pdf(path, avisos):
    """PDF 'umsatz' de Santander tal como lo baja la web (una cuenta por archivo, del más nuevo al más viejo).
    Los "DEBITO A CONFIRMAR" se devuelven con pend=True. Devuelve (movimientos, saldos, pendientes, periodos)."""
    nro = mon = None; out = []; saldo_banco = None; pend = 0; cols = None; filas = []; periodo = None
    for lineas in lineas_pdf(path):
        for i, l in enumerate(lineas):
            txt = ' '.join(w['text'] for w in l)
            if txt.startswith('Cuenta') and 'Moneda' in txt and i + 1 < len(lineas):
                sig = ' '.join(w['text'] for w in lineas[i + 1])
                m = re.search(r'(\d{6,})\s+([A-Z]{3})\b', sig)
                if m:
                    nro, mon = m.group(1).lstrip('0'), m.group(2)
                continue
            m = re.fullmatch(r'(\d{2})/(\d{2})/(\d{4}) - (\d{2})/(\d{2})/(\d{4})', txt)
            if m and not cols:
                g = m.groups()
                periodo = (f'{g[2]}-{g[1]}-{g[0]}', f'{g[5]}-{g[4]}-{g[3]}')
                continue
            if txt.startswith('Fecha') and 'Saldo' in txt:
                xs = {w['text']: w for w in l}
                cols = dict(ref=xs['Referencia']['x0'] - 5, tipo=xs['Tipo']['x0'] - 15, desc=xs['Descripción']['x0'] - 5,
                            deb=xs['Débito']['x0'] - 10, cred=xs['Crédito']['x0'] - 10, saldo=xs['Saldo']['x0'] - 15)
                continue
            if not cols:
                continue
            if re.match(r'^\d{2}/\d{2}/\d{4}$', l[0]['text']) and l[0]['x0'] < cols['ref']:
                filas.append(dict(fecha=l[0]['text'], ws=list(l[1:])))
            elif filas:
                filas[-1]['ws'] += l
    for f in filas:
        col = lambda a, b: _texto_columna(f['ws'], cols[a], cols[b] if b else 1e9)
        ref = col('ref', 'tipo')
        tipo = col('tipo', 'desc').strip(' -')
        descr = col('desc', 'deb').strip(' -')
        conc = f'{tipo} {descr}'.strip() if descr and descr not in tipo else tipo
        deb = num_auto(col('deb', 'cred') or '0') or 0.0
        cred = num_auto(col('cred', 'saldo') or '0') or 0.0
        saldo = num_auto(col('saldo', None) or '')
        d, m_, y = map(int, f['fecha'].split('/'))
        fecha = datetime.date(y, m_, d).isoformat()
        monto = round(cred - abs(deb), 2)
        if saldo_banco is None and saldo is not None:
            saldo_banco = saldo  # el más nuevo; incluye los pendientes, que también se cargan
        if conc.upper().startswith('DEBITO A CONFIRMAR'):
            pend += 1
            desc = limpiar_pendiente_santander(conc)
            out.append(dict(fecha=fecha, cuenta=None, desc=desc, monto=monto, notas='', pend=True,
                            id=f'pend|sant|{nro}|{fecha}|{ref}|{monto!r}'))
            continue
        desc = re.sub(r'\s*TARJ: #+\d+$', '', conc).replace('COMPRA CON TARJETA DEBITO ', 'COMPRA ')
        out.append(dict(fecha=fecha, cuenta=None, desc=desc, monto=monto, notas='',
                        id=f'sant|{nro}|{fecha}|{ref}|{desc}|{monto!r}|{saldo!r}'))
    cuenta = SANTANDER_CUENTAS.get(nro)
    if not cuenta:
        avisos.append(f'Santander: la cuenta {nro} ({mon}) no está configurada. No se importó.')
        return [], {}, 0, {}
    for m in out:
        m['cuenta'] = cuenta
    return out, ({cuenta: saldo_banco} if saldo_banco is not None else {}), pend, ({cuenta: [periodo]} if periodo else {})


# ---------- Santander CSV: el que baja la web (Mac, Latin-1) o la Hoja de Google exportada (Drive, UTF-8) ----------
def leer_santander_csv(path, avisos):
    raw = open(path, 'rb').read()
    try:
        texto = raw.decode('utf-8-sig')
    except UnicodeDecodeError:
        texto = raw.decode('latin-1')  # el CSV original de la web de Santander
    rows = list(csv.reader(io.StringIO(texto)))
    nro = mon = None; hdr = None; out = []; saldo_banco = None; pend = 0; periodo = None
    for r in rows:
        if not r:
            continue
        if r[0] == 'Número':
            nro = r[1].strip().lstrip('0')  # la web escribe 001200417441; la Hoja de Google, 1200417441
        elif r[0] == 'Moneda':
            mon = r[1].strip()
        elif r[0] == 'Desde:' and len(r) > 3:
            try:
                periodo = tuple(datetime.date(*map(int, x.strip().split('/')[::-1])).isoformat() for x in (r[1], r[3]))
            except ValueError:
                pass
        elif r[0] == 'Fecha' and 'Concepto' in r:
            hdr = {k: r.index(k) for k in ('Fecha', 'Referencia', 'Concepto', 'Débito', 'Crédito', 'Saldos')}
        elif hdr and re.match(r'^\d{2}/\d{2}/\d{4}$', r[0].strip()):
            conc = re.sub(r'\s+', ' ', r[hdr['Concepto']]).strip()
            d, m, y = map(int, r[0].split('/'))
            fecha = datetime.date(y, m, d).isoformat()
            monto = round(num(r[hdr['Crédito']]) + num(r[hdr['Débito']]), 2)  # el débito ya viene en negativo
            saldo = num(r[hdr['Saldos']])
            if saldo_banco is None:
                saldo_banco = saldo  # el extracto viene del más nuevo al más viejo; incluye los pendientes
            ref = r[hdr['Referencia']].strip()
            if conc.upper().startswith('DEBITO A CONFIRMAR'):
                pend += 1
                out.append(dict(fecha=fecha, cuenta=None, desc=limpiar_pendiente_santander(conc), monto=monto, notas='', pend=True,
                                id=f'pend|sant|{nro}|{fecha}|{ref}|{monto!r}'))
                continue
            desc = re.sub(r'\s*TARJ: #+\d+$', '', conc).replace('COMPRA CON TARJETA DEBITO ', 'COMPRA ')
            out.append(dict(fecha=fecha, cuenta=None, desc=desc, monto=monto, notas='',
                            id=f'sant|{nro}|{fecha}|{ref}|{desc}|{monto!r}|{saldo!r}'))
    cuenta = SANTANDER_CUENTAS.get(nro)
    if not cuenta:
        avisos.append(f'Santander: la cuenta {nro} ({mon}) no está configurada. No se importó.')
        return [], {}, 0, {}
    for m in out:
        m['cuenta'] = cuenta
    return out, ({cuenta: saldo_banco} if saldo_banco is not None else {}), pend, ({cuenta: [periodo]} if periodo else {})


# ---------- Clasificación ----------
QUIENES = ('Juanma', 'Mili', 'Conjunto')


def clasificar(desc, cuenta, reglas):
    """Devuelve (tipo, categoria, persona, de_quien de la regla o '')."""
    for r in reglas:
        r = (list(r) + [''] * 6)[:6]
        if r[0] and str(r[0]).lower() in desc.lower() and (not r[1] or r[1] == cuenta):
            q = str(r[5] or '').strip()
            return r[2] or '', r[3] or '', r[4] or '', q if q in QUIENES else ''
    return '', '', '', ''


def de_quien(tipo, cat, quien_regla, cuenta, ctx):
    """De quién es el movimiento: la regla manda; si no, la categoría y el titular de la cuenta."""
    if quien_regla:
        return quien_regla
    tit = ctx.get('titulares', {}).get(cuenta, '')
    if tipo != 'Gasto':
        return 'Conjunto' if tit == 'Ambos' else (tit if tit in QUIENES else '')
    amb = ctx.get('ambitos', {}).get(cat) if cat else None
    if amb == 'Conjunta':
        return 'Conjunto'
    if amb == 'Personal' and tit in ('Juanma', 'Mili'):
        return tit
    return ''


# ---------- Splitwise (JSON armado desde los correos) ----------
def leer_splitwise(path, avisos):
    out = []
    for m in json.load(open(path)):
        if m.get('caso') not in ('pago_otro', 'pague_yo') or not all(m.get(k) not in (None, '') for k in ('fecha', 'cuenta', 'desc', 'total', 'parte', 'id')):
            avisos.append(f'Splitwise: gasto incompleto, no se importó ({m}).'); continue
        total, parte = round(float(m['total']), 2), round(float(m['parte']), 2)
        base = dict(fecha=m['fecha'], cuenta=m['cuenta'], moneda=m.get('moneda', ''), desc=str(m['desc']).strip(),
                    grupo=m.get('grupo', ''), total=total, parte=parte, id=m['id'], caso=m['caso'], splitwise=True)
        base['monto'] = -parte if m['caso'] == 'pago_otro' else round(total - parte, 2)
        base['notas'] = f"Splitwise {base['grupo']} · total {total:g} {base['moneda']}".strip()
        out.append(base)
    return out


def vincular_splitwise(sw, candidatos, ya_vinculados, monedas):
    """Devuelve el movimiento del banco que pagó el gasto, o una lista vacía/varios si no es único."""
    f0 = datetime.date.fromisoformat(sw['fecha'])
    cands = [c for c in candidatos
             if c['id'].lower() not in ya_vinculados and not c['cuenta'].startswith('Splitwise')
             and monedas.get(c['cuenta']) == sw['moneda'] and round(c['monto'], 2) == -sw['total']
             and abs((datetime.date.fromisoformat(c['fecha']) - f0).days) <= 3]
    return cands


def _palabras(s):
    return {w for w in re.findall(r'[A-Za-z]{4,}', s.upper()) if w not in ('COMPRA', 'MONTEVIDEO', 'MDEO', 'DEBITO', 'TARJETA')}


def buscar_pendiente(m, pend_hoja, solo_exacto=False):
    """Fila pendiente de la hoja que corresponde al movimiento confirmado m, o None.
    Misma cuenta y signo, confirmado entre 2 días antes y 10 días después del pendiente. Primero monto exacto;
    si no, monto parecido (±15%) con la misma descripción (Revolut) o alguna palabra en común (Santander). Gana el más cercano en fecha."""
    f0 = datetime.date.fromisoformat(m['fecha'])
    mejores = []
    for p in pend_hoja:
        if p['cuenta'] != m['cuenta'] or (p['monto'] > 0) != (m['monto'] > 0):
            continue
        dias = (f0 - datetime.date.fromisoformat(p['fecha'])).days
        if not -2 <= dias <= 10:
            continue
        exacto = round(p['monto'], 2) == round(m['monto'], 2)
        parecido = abs(p['monto'] - m['monto']) <= 0.15 * abs(p['monto'])
        mismo_texto = p['desc'].strip().lower() == m['desc'].strip().lower() if m['id'].startswith('rev|') else bool(_palabras(p['desc']) & _palabras(m['desc']))
        if exacto or (parecido and mismo_texto and not solo_exacto):
            mejores.append((0 if exacto else 1, 0 if mismo_texto else 1, round(abs(p['monto'] - m['monto']), 2), abs(dias), p['fila'], p))
    return min(mejores, key=lambda t: t[:5])[5] if mejores else None


def main():
    manifiesto = json.load(open(sys.argv[1]))
    ctx = json.load(open(sys.argv[2]))
    desde = datetime.date.fromisoformat(ctx['desde'])
    ids = {i.lower() for i in ctx.get('ids', [])}  # sin distinguir mayúsculas: la web de Itaú y el script local escriben distinto (DLO*PEDIDOSY / DLO*PedidosY)
    ex_raw = [(list(e) + [''] * 9)[:9] for e in ctx.get('existentes', [])]
    existentes = [(datetime.date.fromisoformat(e[0]), e[1], round(float(e[2]), 2)) for e in ex_raw if not str(e[5]).startswith('pend|')]
    monedas = ctx.get('monedas_cuenta', {})
    avisos, movs, saldos, pendientes = [], [], {}, 0
    exportado, periodos = {}, collections.defaultdict(list)
    for f in manifiesto:
        p, carpeta, nombre = f['path'], f.get('carpeta', ''), f.get('nombre', f['path'])
        low = nombre.lower()
        inicio = len(movs)
        saldos_antes = set(saldos)
        try:
            if carpeta == 'Splitwise' and low.endswith('.json'):
                movs += leer_splitwise(p, avisos)
            elif carpeta == 'Itau local' and low.endswith('.csv'):
                m, s = leer_itau_local(p, avisos); movs += m; saldos.update(s)
            elif carpeta == 'Santander Mili':
                lector = leer_santander_pdf if es_pdf(p) else leer_santander_csv
                m, s, pend, per = lector(p, avisos); movs += m; saldos.update(s); pendientes += pend
                for c, ps in per.items(): periodos[c] += ps
            elif carpeta.startswith('Revolut') and low.endswith(('.pdf', '.txt')):
                if es_pdf(p):  # PDF original (Mac)
                    m, s, pend, per = leer_revolut_pdf_original(p, carpeta, avisos)
                    for c, ps in per.items(): periodos[c] += ps
                else:  # texto del PDF desde Drive (no trae los pendientes)
                    m, s, pend = leer_revolut_pdf(p, carpeta, avisos)
                movs += m; saldos.update(s); pendientes += pend
            elif carpeta in ('Itau Mili', 'Itau Juanma'):
                m, s = leer_itau_csv(p, avisos); movs += m; saldos.update(s)
            elif low.endswith('.csv'):
                m, s, pend = leer_revolut_csv(p, carpeta, avisos); movs += m; saldos.update(s); pendientes += pend
            elif low.endswith('.xlsx'):
                movs += leer_revolut_consolidado(p, avisos, ctx['desde'])
            elif low.endswith('.xls'):
                m, s = leer_itau(p, avisos); movs += m; saldos.update(s)
            else:
                avisos.append(f'{nombre}: formato no reconocido; no se importó.')
        except Exception as e:
            avisos.append(f'{nombre}: no se pudo leer ({e}).')
        # Fecha de exportación de cada cuenta que trajo este archivo (la más nueva si hay varios)
        if f.get('exportado') and carpeta != 'Splitwise':
            for c in {m['cuenta'] for m in movs[inicio:] if m.get('cuenta')} | (set(saldos) - saldos_antes):
                exportado[c] = max(exportado.get(c, ''), f['exportado'])
        # IDs de Revolut: cuenta|fecha|descripción|monto|n, con n contando repeticiones idénticas dentro del mismo archivo
        # (los pendientes llevan "pend|" adelante y se numeran aparte)
        cont = collections.Counter()
        for m in movs[inicio:]:
            if 'id' not in m:
                base = f"{'pend|' if m.get('pend') else ''}rev|{m['cuenta']}|{m['fecha']}|{m['desc']}|{m['monto']!r}"
                cont[base] += 1
                m['id'] = f'{base}|{cont[base]}'
    # Primero los bancos, después Splitwise: así el vínculo ve los movimientos nuevos de esta misma importación
    sw_movs = [m for m in movs if m.get('splitwise')]
    pend_archivo = [m for m in movs if m.get('pend')]
    movs = [m for m in movs if not m.get('splitwise') and not m.get('pend')]
    filas, dudosos, vistos, revisar, actualizar, borrar = [], [], set(), [], [], []
    # Pendientes ya cargados en la hoja (ID "pend|..."), con su número de fila
    ids_pend_archivo = {m['id'].lower() for m in pend_archivo}
    pend_hoja = [dict(fecha=e[0], cuenta=e[1], monto=round(float(e[2]), 2), id=e[5], desc=e[6], fila=e[8])
                 for e in ex_raw if str(e[5]).startswith('pend|') and str(e[5]).lower() not in ids_pend_archivo and e[8] not in ('', None)]
    # Itaú y Santander: el ID lleva el saldo, que cambia si el banco agrega después otro movimiento ese mismo día.
    # Por eso también se compara sin el saldo: de cada (banco, cuenta, fecha, descripción, monto) solo entran los que excedan a los ya cargados.
    def sin_saldo_k(i):
        p = i.split('|')
        if p[0] == 'itau': return '|'.join(p[:5])
        if p[0] == 'sant': return '|'.join(p[:3] + p[4:6])
        return None
    cargados = collections.Counter(k for k in (sin_saldo_k(i) for i in ids if not i.endswith('|septiembre')) if k)
    nuevos = sorted(movs, key=lambda x: (x['fecha'], x['cuenta']))
    for m in nuevos:  # primero descuenta los que coinciden exacto
        k = sin_saldo_k(m['id'].lower())
        if k and m['id'].lower() in ids:
            cargados[k] -= 1
    # Confirmaciones de pendientes: primero las de monto exacto, después las de monto parecido
    confirma = {}
    for m in nuevos:
        if m['id'].lower() not in ids and pend_hoja:
            p = buscar_pendiente(m, [x for x in pend_hoja if x['fila'] not in {y['fila'] for y in confirma.values()}], solo_exacto=True)
            if p:
                confirma[m['id']] = p
    for m in nuevos:
        if m['id'].lower() in ids or m['id'] in vistos or datetime.date.fromisoformat(m['fecha']) < desde:
            continue
        k = sin_saldo_k(m['id'].lower())
        if k and cargados[k] > 0:
            cargados[k] -= 1
            continue
        vistos.add(m['id'])
        # ¿Es la confirmación de un pendiente ya cargado? Se actualiza esa misma fila (queda su clasificación y revisión)
        p = confirma.get(m['id']) or buscar_pendiente(m, [x for x in pend_hoja if x['fila'] not in {y['fila'] for y in confirma.values()}])
        if p:
            pend_hoja.remove(p)
            actualizar.append(dict(fila=p['fila'], A=serial(m['fecha']), C=m['desc'], D=m['monto'], J=m.get('notas', ''), K=m['id'],
                                   antes=f"{p['fecha']} {p['desc']} {p['monto']:g}", monto_cambio=round(p['monto'], 2) != round(m['monto'], 2)))
            continue
        tipo, cat, per, q = clasificar(m['desc'], m['cuenta'], ctx.get('reglas', []))
        fila = [serial(m['fecha']), m['cuenta'], m['desc'], m['monto'], tipo, cat, de_quien(tipo, cat, q, m['cuenta'], ctx), per, '', m.get('notas', ''), m['id']]
        f0 = datetime.date.fromisoformat(m['fecha'])
        # Revolut: mismo monto y cuenta en ±3 días. Santander: lo mismo pero con otra descripción (el PDF y la Hoja de Drive la escriben distinto)
        if (m['id'].startswith('rev|') and any(c == m['cuenta'] and v == m['monto'] and abs((f - f0).days) <= 3 for f, c, v in existentes)) or \
           (m['id'].startswith('sant|') and any(e[1] == m['cuenta'] and round(float(e[2]), 2) == m['monto'] and str(e[5]).startswith('sant|')
                                                and abs((datetime.date.fromisoformat(e[0]) - f0).days) <= 3 and e[6].strip().lower() != m['desc'].lower()
                                                for e in ex_raw)):
            dudosos.append(fila)
        else:
            filas.append(fila)
    # Pendientes nuevos: se cargan con "A confirmar" en Notas
    for m in sorted(pend_archivo, key=lambda x: (x['fecha'], x['cuenta'])):
        if m['id'].lower() in ids or m['id'] in vistos or datetime.date.fromisoformat(m['fecha']) < desde:
            continue
        vistos.add(m['id'])
        tipo, cat, per, q = clasificar(m['desc'], m['cuenta'], ctx.get('reglas', []))
        filas.append([serial(m['fecha']), m['cuenta'], m['desc'], m['monto'], tipo, cat, de_quien(tipo, cat, q, m['cuenta'], ctx), per, '',
                      'A confirmar', m['id']])
    # Pendientes de la hoja que ya no están en el extracto y no se confirmaron: el banco los anuló. Solo si un extracto de esa cuenta cubre su fecha.
    for p in pend_hoja:
        if any(d <= p['fecha'] <= h for d, h in periodos.get(p['cuenta'], [])):
            borrar.append(dict(fila=p['fila'], detalle=f"{p['fecha']} {p['cuenta']} {p['desc']} {p['monto']:g}"))
    # Revolut: el "Saldo final" del PDF no incluye los pendientes y la hoja sí: para el control se le suman los que quedan cargados
    filas_borradas = {b['fila'] for b in borrar}
    quedan = {m['id'].lower(): (m['cuenta'], m['monto']) for m in pend_archivo}
    quedan.update({str(p['id']).lower(): (p['cuenta'], p['monto']) for p in pend_hoja if p['fila'] not in filas_borradas})
    for c in [c for c in saldos if c in REVOLUT_CUENTAS.values()]:
        saldos[c] = round(saldos[c] + sum(v for cc, v in quedan.values() if cc == c), 2)
    # Splitwise
    candidatos = [dict(fecha=e[0], cuenta=e[1], monto=float(e[2]), tipo=e[3], cat=e[4], id=e[5], desc=e[6], quien=e[7]) for e in ex_raw]
    candidatos += [dict(fecha=(datetime.date(1899, 12, 30) + datetime.timedelta(days=f[0])).isoformat(), cuenta=f[1], monto=f[3],
                        tipo=f[4], cat=f[5], id=f[10], desc=f[2], quien=f[6]) for f in filas]  # no los posibles duplicados: pueden no cargarse
    ya_vinculados = {i.split('|ref=', 1)[1] for i in ids if '|ref=' in i}
    sw_ids = {i.split('|ref=', 1)[0] for i in ids}
    for m in sorted(sw_movs, key=lambda x: x['fecha']):
        if m['id'].lower() in sw_ids or m['id'] in vistos or datetime.date.fromisoformat(m['fecha']) < desde:
            continue
        vistos.add(m['id'])
        if m['caso'] == 'pago_otro':
            tipo, cat, per, q = clasificar(m['desc'], m['cuenta'], ctx.get('reglas', []))
            tipo = tipo or 'Gasto'
            filas.append([serial(m['fecha']), m['cuenta'], m['desc'], m['monto'], tipo, cat, de_quien(tipo, cat, q, m['cuenta'], ctx), per,
                          '', m['notas'], m['id']])
            continue
        if m['monto'] <= 0:
            continue  # pagó todo y era todo suyo: el gasto ya está entero en el banco
        cands = vincular_splitwise(m, candidatos, ya_vinculados, monedas)
        if len(cands) != 1:
            revisar.append({'motivo': 'sin movimiento del banco' if not cands else 'más de un movimiento posible',
                            'gasto': f"{m['fecha']} {m['desc']} ({m['grupo']}) total {m['total']:g} {m['moneda']}, parte {m['parte']:g}",
                            'candidatos': [f"{c['fecha']} {c['cuenta']} {c['desc']} {c['monto']:g}" for c in cands]})
            continue
        b = cands[0]
        ya_vinculados.add(b['id'].lower())
        notas = f"{m['notas']} · parte de otros de: {b['cuenta']} {b['desc']} {b['fecha']}"
        filas.append([serial(m['fecha']), m['cuenta'], m['desc'], m['monto'], b['tipo'] or 'Gasto', b['cat'] or '', b.get('quien') or '', '', '', notas,
                      f"{m['id']}|ref={b['id']}"])
    print(json.dumps({'filas': filas, 'actualizar': actualizar, 'borrar': sorted(borrar, key=lambda b: -b['fila']),
                      'posibles_duplicados': dudosos, 'splitwise_revisar': revisar, 'saldos_archivo': saldos, 'exportado': exportado,
                      'avisos': list(dict.fromkeys(avisos)), 'pendientes_en_extractos': pendientes}, ensure_ascii=False))


if __name__ == '__main__':
    main()
```