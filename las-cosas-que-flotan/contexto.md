# Contexto · Las cosas que flotan

## Objetivo actual
Meta Q4 (Notion): enviar el libro a editoriales antes del 15/12, entre 1 y 3 envíos por semana. Para cada editorial se adapta el dosier (relato de muestra) y el correo.

## Dónde está cada cosa
- **OneDrive**: `Personal Admin/Cuentos/LCFP/`
  - `Borradores/`: manuscrito (*Las cosas que flotan.docx*), versión Ribera del Duero, carpeta Premio Onetti.
  - `Proyecto Editoriales/`: carpeta de trabajo.
    - `Plantilla dosier/`: solo la plantilla genérica (ver LEEME.md): base.json, banco de relatos (`relatos/`), diseño, generador, fotos y fuentes.
    - `Dossiers/<Editorial>/`: registro de cada envío: JSON de la editorial, dosier PDF y manuscrito si se envió. `generar.py` deja el PDF junto al JSON.
    - `Dossiers/Rediseño/`: dosier base nuevo (*Dossier_LasCosasQueFlotan_borrador.pdf*) y foto de portada original.
    - `Dossiers/La Caja/`: lo que se envió a La Caja (versión vieja) y `la-caja.json`.
    - `Dossiers/Minúscula/`: dosier, manuscrito en PDF y `minuscula.json`.
    - `Dossiers/Barrett/`: propuesta de 2 páginas en PDF (sinopsis + autor).
    - `Dossiers/Reservoir Books/`: manuscrito en PDF (copia del de Minúscula).
    - `Dossiers/Galaxia Gutenberg/`: dosier con "Lo de Fabio" y `galaxia-gutenberg.json`.
    - `Dossiers/Fulgencio Pimentel/`: dosier con "La pecera" y `fulgencio-pimentel.json`.
- **Notion**: proyecto "Contactar Editoriales Españolas" con sus tareas y la base "Seguimiento Editoriales" (26 editoriales). Es el único registro de seguimiento; el Excel se eliminó.
- **Próximos proyectos** (cuando se termine de enviar a las españolas): editoriales de Uruguay, y después uno para buscar premios y postular. Ribera del Duero no es prioridad: se lo dan a autores conocidos (lo admitió un editor); se puede mandar porque no se pierde nada.
- **Gmail**: correo enviado a La Caja el 7/8/2026 (asunto "Manuscrito - Las cosas que flotan"). Sirve de plantilla de correo.

## Skill `contactar-editorial`
Creada el 28/10/2026. Recibe nombre y web de la editorial y frena antes de cada paso: chequeo previo (duplicados y bases de envío; si no aceptan, pregunta si seguir), investigación, conexiones con el catálogo (título ancla), relato de muestra, dosier, borrador en Gmail, Notion y cierre. Tiene un modo "marcar enviado".
Decisiones:
- Relatos: se extraen del manuscrito .docx de Borradores.
- Firma del correo: solo email.
- Adjunto: el dosier (ya trae el relato). Si las bases piden el manuscrito, también el manuscrito. Se adjuntan a mano en el borrador.
- Notion: queda "No enviado" con próxima acción hasta confirmar el envío.
- 26/11: "Enviado" en Seguimiento Editoriales es solo para el envío del libro (dosier o manuscrito). Una consulta previa ("¿aceptan envíos?") deja la ficha en "No enviado", con la consulta en notas y la próxima acción en esperar respuesta.
- Correo base corregido: "uruguayo" en minúscula, bio con puntuación y mención a Selecta.
- 15/11: el PDF se genera en la Mac, corriendo `generar.py` desde `Plantilla dosier/` (jinja2 y Playwright instalados); queda en `Dossiers/<Editorial>/`.
- Nada de una editorial se guarda en la plantilla.
- El seguimiento se ajusta al plazo de respuesta de cada editorial (por defecto, 3 meses).
- Si la editorial pide un formato propio (como Barrett, 2 páginas), se salta el dosier y el correo es corto: no repite lo que va en el adjunto, saluda a los editores por nombre, felicita y menciona algo concreto de la editorial.
- Envíos por formulario de grupos grandes (como PRH): sin ancla ni dosier si el formulario no lo pide; va el manuscrito completo y la sinopsis son los dos párrafos de "El libro".
- Si el .docx original no cambió, se reutiliza el PDF del manuscrito ya preparado.
- 10/11: es preferible un ancla que Juan Manuel haya leído (más genuino) antes que una novedad que no conoce.
- 12/11: antes de preparar, comprobar si la editorial publica solo autoras u otra restricción de autoría (las sugerencias de Notion no siempre lo recogen).

## Dosier (decisiones tomadas)
- A4 horizontal, pensado para leer en pantalla. Fondo blanco, sobrio, acento azul (#1f4e79).
- Tipografías: Newsreader (texto) e Inter (etiquetas).
- Portada: foto de Naja Bertolt Jensen (Unsplash, licencia libre), bolsa bajo el agua. Sin el texto "Dossier de presentación".
- Páginas: portada, El libro + ficha técnica, Índice (marca el relato de muestra), El autor + contacto, portadilla del relato, relato a dos columnas sin justificar.
- Párrafos de "El libro" con el mismo tamaño y peso. Sin guiones largos.
- Bio: "Juan Manuel Trelles (Montevideo, 1994) vivió en Irlanda y en Chile antes de instalarse en Valencia, donde reside actualmente. Es científico de datos por la Universidad de Londres y magíster en Investigación Matemática por la Universitat Politècnica de València." Luego el párrafo literario (Reflujo, taller Finis Terrae con Simonetti, escuela Selecta).
- Se mantiene que vive en España.
- Contacto: solo email.
- Premio Onetti: postulado. No mencionarlo en la bio.
- La plantilla admite, además de párrafos (`t`, `brk`), secciones numeradas (`sec`) y estrofas en cursiva (`estrofa`).
- 5/11: arreglos en la plantilla: `| safe` en los párrafos de "El libro" (se veía `<em>` literal) y texto de "El libro" a 12 pt (la sinopsis larga empujaba la ficha sobre el pie).
- Índice corregido el 28/10: "Abrigo" = "Entre llamadas, el hospital y un disco por terminar, un nieto descubre que el abrigo que le dejó su abuelo guarda el calor pero no lo genera."; "El último dios griego" = "El día que murió el Diego.". 5/11: "Lo de Fabio" = "Un pibe va a comprar faso por primera vez y ve a su padre en lo del dealer." 10/11: "La pecera" y "Oscura era la noche" coinciden con sus relatos.

## Manuscrito para envíos
- Si las bases piden el manuscrito, se manda una copia (el original no se toca): en .docx si lo piden así, si no en PDF.
- Doble espacio si lo piden, páginas numeradas, cada relato en página nueva y carátula con la foto del dosier, título, nombre y email.
- PDF vigente (interlineado 1,5, 125 páginas): `Dossiers/Minúscula/Las cosas que flotan - Juan Manuel Trelles.pdf`. Sirve mientras el .docx original no cambie (última modificación: 14/12/2025).

## Correo (estructura del enviado a La Caja)
Preferencias (5/11): sin dos puntos, sin abrir el porqué con "Pienso en"; el porqué no puede ser solo el título ancla, tiene que sumar algo de la línea de la editorial. En Galaxia Gutenberg se sacó la sinopsis del correo (queda una línea de qué es el libro); en Fulgencio Pimentel también.
1. Presentación: nombre, primer libro, 11 cuentos, unas 40.000 palabras.
2. Línea de presentación del libro (desde Galaxia Gutenberg reemplaza al párrafo del libro). 16/11: se arma para cada envío según lo que se manda, con 2 o 3 versiones para elegir; no se copia de correos anteriores. No usar "hombres que no saben decir lo que sienten" ni paráfrasis: en la sinopsis funciona por la ironía del "(para variar)", pero en el correo es la única descripción del libro y suena a cliché.
3. Por qué esa editorial: un título de su catálogo con el que dialoga el libro (en La Caja: *De ningún lugar a ninguna parte*, de Bekim Sejranović; en Minúscula: *Sabrina y Corina*, de Kali Fajardo-Anstine; en Barrett: *Una música futura*, de María José Navia; en Galaxia Gutenberg: *Alimento para puma*, de Matías Gotelli; en Fulgencio Pimentel: *La comemadre*, de Roque Larraquy). Es lo que se personaliza.
4. Bio breve.
5. Cierre: adjunta el dosier con el relato y ofrece el manuscrito completo (si va adjunto, solo se menciona).
