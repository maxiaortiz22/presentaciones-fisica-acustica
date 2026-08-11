# Unidad 6 — Registro de cambios

## Convención

Este archivo registra cambios entre artefactos publicados. Las versiones previas se preservan; no se reemplazaron `unidad_06_mecanismo_periferico_v01.pptx` ni `unidad_06_mecanismo_periferico_v02.pptx`.

## v01 → v02

- Cierre de hallazgos críticos y mayores de la primera revisión integral.
- Corrección de conectores, textos, fórmulas, fuentes y estados bloqueados.
- Consolidación de 117 slides, 117 notas, 2 masters y 27 layouts.
- Producción de PDF, render completo, mosaico y validación v02.

## v02 → final

### Arquitectura pedagógica

- Organización visible en cuatro encuentros.
- Señalización de ruta central, ampliaciones y respaldo.
- Conservación de 82 slides centrales, 23 complementarias y 12 de respaldo.
- Sincronización de storyboard, texto, notas, decisiones y mapa de fuentes.

### Contenido y exactitud

- Diferenciación explícita entre conducto auditivo ideal y real.
- Explicación visual de la palanca y del intercambio fuerza–desplazamiento sin creación de energía.
- Corrección de CCE: conversión de energía electroquímica en trabajo mecánico.
- Separación causal CCI → sinapsis/fibra y CCE → realimentación mecánica.
- Sustitución de lenguaje ambiguo de “reclutamiento” por extensión de la región de excitación y población más amplia.
- Desarrollo de “potencial evocado” sin imponer una sigla institucional.
- G3 convertido en ejemplo numérico resuelto con datos, resultado y límite.
- Potencial endococlear presentado con referencia de medida explícita, sin subíndice Unicode ambiguo.

### Pedagogía

- Nuevos apoyos intuitivos antes de formalismos del oído medio.
- Secuencia anatómica acumulativa de base/ápex, rampas, membranas, órgano de Corti y túnel de Corti.
- Estados visibles de movimiento relativo y deflexión del haz.
- Mapa de dominios antes de la taxonomía de potenciales.
- Actividad de clasificación CCI/CCE sin mostrar la respuesta por adelantado.
- Notas menos formularias, con variación de preguntas, errores y transiciones.

### Diseño y diagramas

- Nuevos visuales nativos editables en U06-013, 033, 051–057, 073–075, 083–084, 101 y 111.
- Regeneración de U06-DG-044, 047, 059, 060 y 063.
- Corrección de cajas insuficientes, rótulos sobre líneas, helicotrema angosto y ventanas próximas al subtítulo.
- Ajuste de títulos largos y cajas tipográficas para evitar overflow ascendente.
- CCI/CCE llevadas a 20 pt dentro del esquema coclear.
- Encabezado académico uniforme por encuentro/ruta y eliminación de códigos internos visibles.
- Captions visibles restringidos a claves de lectura de gráficos.

### Producción

- Nuevo archivo `output/unidad_06_mecanismo_periferico_final.pptx`.
- Numeración dinámica nativa en 117 slides.
- Alt text aplicado a 64 objetos visuales; 117 notas con alt text y fuentes.
- PDF final de revisión, 117 renders y contact sheet final.
- Validación OOXML aprobada y `slides_test.py` sin overflow.
- 64 usos reales de assets aprobados y 17 composiciones nativas finales; las notas ya no atribuyen los ocho assets reemplazados.
- Hash final PPTX: `8F300D7B0B1C47168C6C52AB6EC0195D05E6B416E3C3E5157E68B8D5CCB739BE`.

## Archivos creados

- `output/unidad_06_mecanismo_periferico_final.pptx`.
- `output/unidad_06_mecanismo_periferico_final_review.pdf`.
- `output/render_final/`.
- `output/contact_sheet_final.png`.
- `output/validation_final.json`.
- `final_report.md`.
- `change_log.md`.
- `scripts/u06_finalize_native.ps1`.
- `tmp/final_build/template-frame-map.json`, `template-audit.txt` y `deviation-log.txt`.

## Archivos actualizados para el cierre

- `brief.md`.
- `storyboard.md`.
- `slide_text.md`.
- `speaker_notes.md`.
- `open_decisions.md`.
- `source_map.md`.
- `review.md`.
- `consistency_report.md`.
- `production_log.md`.
- `scripts/u06_build_presentation.mjs`.
- `scripts/u06_generate_diagrams.mjs`.
- `scripts/u06_generate_charts.py`.
- Assets regenerados U06-DG-044, 047, 059, 060, 063 y U06-CH-006.

## Problemas abiertos

No quedan problemas críticos ni mayores. Permanecen únicamente sugerencias de uso: administrar el tiempo mediante la ruta central, producir multimedia solo si aporta una demostración concreta y agregar hipervínculos externos solo si se desea navegación desde PowerPoint.
