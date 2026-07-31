# Unidad 3 — Registro de producción del PowerPoint

**Fecha:** 30 de julio de 2026  
**Versión:** v01  
**Nombre corto:** `mecanica_ondulatoria`  
**Estado:** aprobado para revisión docente; sin problemas críticos ni mayores detectados.

## Entregables

- `output/unidad_03_mecanica_ondulatoria_v01.pptx`
- `output/unidad_03_mecanica_ondulatoria_preview.pdf`
- `output/contact_sheet.png`

## Base de producción

Se utilizó el template aprobado `output/fisica_acustica_template_v01.pptx` y se trabajó exclusivamente a partir de:

- `storyboard.md`;
- `slide_text.md`;
- `speaker_notes.md`;
- `asset_manifest.csv`;
- `chart_plan.md` y `charts_review.md`;
- `diagram_plan.md`, `diagram_validation_report.md` y `diagram_assets_review.md`;
- sistema visual y decisiones registradas en el repositorio.

La secuencia aprobada de 96 slides se conservó sin divisiones ni reordenamientos.

## Construcción

- Formato: 16:9, 13,333 × 7,5 pulgadas.
- Estructura del template conservada: 2 Slide Masters y 27 layouts.
- Cada slide se construyó duplicando el patrón correspondiente del template.
- Títulos, subtítulos, contenido, definiciones, preguntas, captions, numeración y ecuaciones de apoyo permanecen como texto o formas editables.
- Las ecuaciones centrales se mantuvieron como texto editable con Cambria Math cuando fue posible; las expresiones integradas en figuras validadas permanecen dentro del SVG.
- Se incorporaron notas del orador en las 96 slides, con bloque de fuentes en todas ellas.
- Se incorporó numeración del 1 al 96.
- No se aplanó ninguna diapositiva completa.

## Gráficos y diagramas insertados

| Tipo | Cantidad | Formato | Estado |
|---|---:|---|---|
| Diagramas | 57 | SVG con fallback interno de PowerPoint | Aprobados |
| Gráficos | 23 | SVG con fallback interno de PowerPoint | Aprobados |
| Total de visuales propios | 80 | SVG | Aprobados |

Todos los visuales insertados corresponden a la versión aprobada vigente. No se insertaron archivos preliminares. Los 80 visuales incluyen texto alternativo y permanecen dentro del área de la slide.

### Revisión de diagramas en contexto

Los 57 diagramas se revisaron individualmente en su render validado y nuevamente dentro del render final de PowerPoint a 1600 × 900 px. Se comprobó:

- texto legible y cajas con espacio suficiente;
- ausencia de texto desbordado o superpuesto;
- flechas y puntas fuera de las áreas tipográficas;
- etiquetas separadas de sus conectores;
- ausencia de elementos recortados;
- captions y créditos fuera del área principal del diagrama.

Resultado: sin problemas críticos ni mayores.

## Multimedia, imágenes y enlaces

- `U03-MEDIA001` quedó identificado en U03-013 junto con su alternativa estática; no se incrustó porque su estado no era aprobado.
- `U03-MEDIA003` quedó identificado; U03-061 utiliza como alternativa estática el diagrama aprobado `U03-DG020-S062`.
- No se incrustaron audios, videos ni imágenes externas con estado `proposed` o `shortlisted`.
- No se agregaron enlaces externos: el manifiesto no contenía un enlace multimedia aprobado para esta versión. Por lo tanto, no existen vínculos externos pendientes o rotos.

## Ajustes de producción respecto del texto aprobado

Para evitar clipping en el layout real, se condensaron únicamente los siguientes títulos. No cambió la idea central, el orden ni el contenido pedagógico:

| Slide | Título utilizado en el deck |
|---|---|
| U03-004 | Equilibrio, elasticidad y gráficos: lo que ya sabemos |
| U03-012 | Longitudinal y transversal: dos direcciones |
| U03-033 | Posición, velocidad y aceleración no coinciden |
| U03-036 | La sinusoide no es la trayectoria de una partícula |
| U03-042 | Señal eléctrica, cono, aire y presión: una cadena |
| U03-046 | Un tono audiométrico exige nivel y calibración |
| U03-053 | Período y longitud de onda: tiempo y espacio |
| U03-062 | u es movimiento local; c, propagación |
| U03-067 | El retraso se vuelve fase si conocemos f |
| U03-073 | La oposición de fase puede cancelar |
| U03-074 | El desfase intermedio produce suma parcial |
| U03-076 | La cancelación activa exige control |
| U03-079 | Producción, propagación y recepción |
| U03-081 | De la fuerza restauradora a la onda |
| U03-083 | Describimos la onda; ahora mediremos el sonido |
| U03-086 | Masa y elasticidad fijan la frecuencia ideal |

No fue necesario dividir slides; por ello no se modificaron el storyboard ni los documentos de redacción.

## Reemplazos respecto de una versión anterior

Esta es la primera producción del deck (`v01`), por lo que no existe una versión anterior del PowerPoint contra la cual registrar reemplazos. Cantidad de assets reemplazados: **0**.

## Verificación posterior

| Control | Resultado |
|---|---|
| Apertura del PPTX en Microsoft PowerPoint | Correcta |
| Slides | 96 |
| Formato | 16:9 |
| Masters / layouts | 2 / 27 |
| Slides con notas no vacías | 96 |
| Slides con bloque de fuentes | 96 |
| Títulos y numeración | 96 / 96 |
| Placeholders vacíos | 0 |
| Visuales con texto alternativo | 80 / 80 |
| Visuales fuera de los límites | 0 |
| Assets no aprobados insertados | 0 |
| Render de PowerPoint | 96 PNG, 1600 × 900 px |
| PDF de revisión | 96 páginas |
| Vista mosaico | Generada |
| Revisión visual de las 96 slides | Completada |

El control estándar `slides_test.py` no pudo iniciarse porque el entorno no dispone de `pdf2image`. Se ejecutó un control equivalente sobre el OOXML, el PDF y los renders, y se verificó además la apertura de solo lectura en Microsoft PowerPoint. Todos los controles equivalentes aprobaron.

## Desviaciones y problemas abiertos

- Desviación de producción: condensación de 16 títulos, registrada arriba.
- Multimedia no aprobada: identificada, no incrustada y sustituida por alternativas estáticas cuando correspondía.
- Problemas críticos: 0.
- Problemas mayores: 0.
- Problemas abiertos de contenido o diagramación: 0.

## Revisión correctiva v02 — 30 de julio de 2026

**Archivo:** `output/unidad_03_mecanica_ondulatoria_v02.pptx`  
**Estado:** sin problemas críticos ni mayores abiertos.

Cambios realizados:

- se corrigió la conversión de puntos a píxeles CSS en los generadores SVG;
- se regeneraron y reemplazaron los 80 visuales;
- se elevaron los diagramas a 20 pt como mínimo para etiquetas auxiliares y 22 pt para texto principal;
- se reemplazaron los gráficos densos de U03-072, U03-073 y U03-074 por un caso de superposición por slide;
- se redujo U03-075 a tres casos de predicción con la resultante oculta;
- se eliminaron códigos internos y lenguaje de producción visible en U03-003, U03-013, U03-061, U03-082 y U03-088;
- se corrigió el orden de capas de los SVG reemplazados;
- se volvió a exportar el PDF y el render completo de 96 PNG a 1600 × 900 px;
- se generó `output/contact_sheet_v02.png`;
- se revisaron ocho hojas de contacto y las slides afectadas a resolución completa.

Verificación de v02:

| Control | Resultado |
|---|---|
| Slides | 96 |
| Visuales reemplazados | 80 |
| Masters / layouts | 2 / 27 |
| Notas / bloques de fuentes | 96 / 96 |
| Alt text o título en visuales | 80 / 80 |
| Objetos fuera de página | 0 |
| Auto-shrink | 0 |
| Códigos internos visibles | 0 |
| Caracteres corruptos | 0 |
| Render visual completo | aprobado |
| Peso del PPTX | 10.109.523 bytes |

Pendientes no bloqueantes:

- los visuales son SVG vectoriales y reproducibles, pero no grupos de formas nativas de PowerPoint;
- los recursos multimedia siguen sin incrustarse porque no tienen estado aprobado;
- la herramienta estándar basada en `pdf2image` no está disponible en el entorno; se usó PowerPoint, OOXML, PDF y revisión de los 96 renders.
