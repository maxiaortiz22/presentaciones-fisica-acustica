# Registro de producción — Unidad 06

Fecha de producción: 10 de agosto de 2026  
Estado: **apto para revisión docente**, con cinco bloqueos de fuente identificados antes de la proyección.

## Entregables

- `output/unidad_06_mecanismo_periferico_v01.pptx`
- `output/unidad_06_mecanismo_periferico_preview.pdf`
- `output/contact_sheet.png`

## Fuentes de producción

Se construyó el deck a partir de:

- `output/fisica_acustica_template_v01.pptx`;
- `storyboard.md`;
- `slide_text.md`;
- `speaker_notes.md`;
- `source_map.md`;
- `asset_manifest.csv`;
- `chart_plan.md` y `charts_review.md`;
- `diagram_plan.md`, `diagram_validation_report.md` y `diagram_assets_review.md`;
- la guía de estilo y los assets aprobados de `assets/generated/`.

No se usaron recursos externos con estado `proposed`, `shortlisted` o solamente `downloaded`. Las alternativas estáticas aprobadas reemplazan a los recursos multimedia todavía propuestos.

## Resultado de construcción

- 117 diapositivas, formato panorámico 16:9 (13,333 × 7,5 pulgadas).
- 2 Slide Masters y 27 layouts del template conservados.
- Textos, cajas, conectores y diagramas propios mantenidos como elementos editables.
- Gráficos cuantitativos insertados desde SVG aprobado.
- 72 inserciones de assets aprobados: 63 instancias de diagramas y 9 instancias de gráficos.
- 57 assets únicos utilizados: 51 diagramas y 6 gráficos.
- 117 diapositivas con notas del orador, bloque de fuentes y texto alternativo en notas.
- 72 objetos visuales con texto alternativo en el archivo PPTX.
- Numeración, captions y créditos integrados según el material aprobado.
- No se aplanó ninguna diapositiva como imagen.
- No se incrustaron videos ni GIF: los cuatro recursos propios de `media_plan.md` siguen en estado `proposed`; se conservaron sus alternativas estáticas aprobadas.

## Desviaciones respecto del storyboard

No fue necesario dividir diapositivas ni cambiar su orden. Se mantuvieron los 117 identificadores `U06-001` a `U06-117`.

Las siguientes diapositivas se produjeron como placas visibles de **material no habilitado para proyección**, porque dependen de fuentes o datos todavía no aprobados:

- `U06-057`;
- `U06-085`;
- `U06-096`;
- `U06-115`;
- `U06-116`.

Esta decisión preserva la trazabilidad y evita fabricar datos, valores o afirmaciones anatómicas. Deben revisarse y sustituirse por contenido validado antes de una versión de clase.

## Reemplazos y correcciones durante la producción

No existía una versión anterior del PowerPoint de la unidad; por lo tanto, no hubo reemplazos respecto de otro deck publicado. Durante la iteración interna se sustituyeron explícitamente las versiones preliminares por las versiones corregidas en el archivo final:

- conectores de diagramas: se corrigieron anclajes, lados de salida y llegada, puntas y orden de capas;
- captions: se redujeron a una línea para no invadir el pie;
- títulos extensos: se ajustó jerarquía y se eliminó el subtítulo redundante cuando correspondía;
- `U06-052`: se usó un layout textual en lugar de improvisar un diagrama no aprobado;
- texto alternativo: se incorporó mediante posprocesamiento nativo de PowerPoint y se volvió a exportar el PDF y los renders.

## Revisión de diagramas en contexto de slide

Se renderizaron las 117 diapositivas con PowerPoint y se revisaron el mosaico completo y muestras a tamaño final. La inspección específica verificó:

- texto contenido dentro de las cajas;
- fuentes legibles sin reducción extrema;
- conectores detrás de las cajas y con corredores libres;
- puntas de flecha fuera del área tipográfica;
- etiquetas separadas de las líneas;
- ausencia de clipping, recortes o elementos fuera del lienzo;
- captions y pies sin superposición.

Tras las correcciones no se detectaron problemas visuales críticos ni mayores en los diagramas insertados.

## Controles automáticos y renderizados

- Validación Open XML: **aprobada**.
- Diapositivas: 117.
- Diapositivas con notas: 117.
- Relación de aspecto: 1,777778.
- Objetos fuera del lienzo: 0.
- Placeholders locales residuales: 0.
- PDF de revisión: 117 páginas, una por diapositiva.
- Render del PPTX: 117 PNG individuales.
- Render independiente del PDF: 117 PNG individuales.
- Vista mosaico final: `output/contact_sheet.png`.

El comprobador auxiliar `slides_test.py` no pudo ejecutarse por una ruta interna ausente de su dependencia empaquetada. Se cubrió ese control mediante render nativo de PowerPoint, inspección estructural Open XML, comprobación de límites de objetos, render independiente del PDF y revisión visual del mosaico y de diapositivas seleccionadas a tamaño completo.

## Integridad de los archivos finales

- PPTX: SHA-256 `700122a5c1ef59c629e396932e5cef8ae4ebc182b85ce6f671f0610b83ff2e82`.
- PDF: SHA-256 `f577777dbde4e3c6feccaceb7f5d5f1d4bb5a19cb3d6d260454f99906fb2defc`.
- Mosaico: SHA-256 `f0c68b5b67f6ff9269d933222b8242d7d9f694ab0e54728df1f3fcefccbfc3d9`.

## Pendientes antes de la versión de clase

1. Resolver las cinco diapositivas bloqueadas con fuentes aprobadas.
2. Decidir si se producen los recursos multimedia propios propuestos; mientras tanto, conservar las alternativas estáticas actuales.
3. Realizar la revisión docente de contenido y anatomía antes de publicar una versión final.

---

## Revisión integral y producción v02 — 10 de agosto de 2026

Estado: **sin problemas críticos ni mayores abiertos; apto para revisión docente final**.

### Entregables v02

- `output/unidad_06_mecanismo_periferico_v02.pptx`;
- `output/unidad_06_mecanismo_periferico_v02_preview.pdf`;
- `output/render_v02/` con 117 PNG;
- `output/contact_sheet_v02.png`;
- `output/validation_v02.json`;
- `review.md`.

### Cambios respecto de v01

- se corrigió la cadena de portada a aire → tímpano → cóclea → nervio y se separó el diagrama del título;
- se corrigió el sentido causal de `U06-DG-002`, `U06-DG-012` y `U06-DG-025`;
- se eliminaron conectores causales impropios entre estados en `U06-DG-043`;
- se resolvieron las diapositivas U06-057, U06-085, U06-096, U06-115 y U06-116 con contenido trazable y diagramas editables;
- se amplió a ancho completo la presentación de gráficos para recuperar legibilidad de ejes, rótulos y anotaciones;
- se cerró la convención de notación `S`, `M_p` y `G_p`, y se retiraron marcas visibles de provisionalidad;
- se corrigieron duplicaciones, markdown visible, títulos extensos y preguntas repetidas en divisores;
- se conservaron 117 notas con fuentes y texto alternativo; no se incorporaron videos ni enlaces externos.

### Controles finales

- validación Open XML: aprobada;
- 117 diapositivas y 117 páginas renderizadas;
- 2 masters y 27 layouts conservados;
- relación 16:9;
- 72 objetos con texto alternativo;
- 0 placeholders locales, 0 enlaces externos y 0 objetos fuera del lienzo;
- `slides_test.py`: aprobado, sin overflow;
- revisión visual completa de la v01 y control completo/muestras a tamaño final de la v02;
- búsqueda en el artefacto final: sin `PROVISIONAL`, `BLOQUEADA`, `EXT-PEND` ni placas de “no proyectar”.

### Integridad v02

- PPTX: 708.362 bytes; SHA-256 `E63A34C4EA6D69C9238BCA309B87B92CB71DC3C8CEBAA61443E9EDEFE573667C`.
- PDF: 1.067.109 bytes; SHA-256 `AE6110556E3DDA624939C7D52BA4F56AE2CF2408EDC440A42316DCEE313DE553`.
- Mosaico: 2.390.321 bytes; SHA-256 `098A6317DCD1CE21F51A4309D238EC0A1D13197DA0D0E18F82A58E380D98F869`.

### Pendientes no críticos

1. Revisión docente independiente de anatomía y fisiología, requerida por el proyecto para U6.
2. Confirmación de duración real de encuentros y eventual recorte de slides complementarias.
3. Producción opcional de multimedia; las alternativas estáticas actuales son completas.

## Versión final — 2026-08-10

- Archivo: `output/unidad_06_mecanismo_periferico_final.pptx`.
- Fuente preservada: `output/unidad_06_mecanismo_periferico_v02.pptx`; v01 y v02 no fueron sobrescritas.
- 117 slides; 2 masters; 27 layouts; 16:9.
- 64 usos reales de assets aprobados y 17 composiciones nativas finales; 64 objetos con alt text y 117 notas con alt text/fuentes.
- Numeración dinámica aplicada mediante campos de PowerPoint en las 117 slides.
- PDF: `output/unidad_06_mecanismo_periferico_final_review.pdf`, 117 páginas.
- Render: `output/render_final/`, 117 PNG a 1600 × 900.
- Mosaico: `output/contact_sheet_final.png`.
- Validación U06: `output/validation_final.json`, estado `pass`.
- `slides_test.py`: aprobado, sin objetos fuera del lienzo.
- PPTX: 745.584 bytes; SHA-256 `8F300D7B0B1C47168C6C52AB6EC0195D05E6B416E3C3E5157E68B8D5CCB739BE`.
- PDF: 1.113.602 bytes; SHA-256 `9D3D831F2356B40FA44B0AC43EE6A8A22857EF1EC7ADC6549CB9A5657A26164A`.
