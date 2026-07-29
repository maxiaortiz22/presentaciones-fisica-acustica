# Registro de cambios — Unidad 1

## Versiones

| versión | estado | cambios principales |
|---|---|---|
| `v01` | archivada | primera producción completa del storyboard; 94 slides, assets, notas y PDF inicial de revisión |
| `v02` | revisada | corrección integral de contenido, pedagogía, diseño, producción y accesibilidad |
| `final_pre_diagram_fix` | archivada | primera versión declarada final; preservada íntegramente antes de la reparación |
| `v02_diagram_fix` | revisada | reparación de diagramas y regeneración de gráficos al tamaño final |
| `final` | entregable | integra reparación, accesibilidad 16/16, PDF final y controles de cierre |

Las versiones anteriores se conservan en `units/unit_01/output/` y no fueron sobrescritas.

## Cambios de v01 a v02

- Se incorporó la definición visible de acústica.
- Se reconstruyó la referencia de las siete magnitudes fundamentales del SI.
- Se completaron recapitulaciones y slides de respaldo que estaban vacías o incompletas.
- Se corrigieron solapamientos de fórmulas, textos y figuras.
- Se corrigió la inconsistencia entre el ejercicio de 68 m y una figura de 100 m.
- Se reorganizaron slides con imágenes que ocultaban contenido.
- Se eliminó duplicación en los casos integradores.
- Se completó el respaldo 85–94 y se agregó el banco de transferencia.
- Se agregó numeración editable en slides 2–94.
- Se serializó texto alternativo en 73/73 imágenes.
- Se incorporó el GIF propio y su alternativa estática.
- Se completó la bibliografía y se agregaron dos hipervínculos externos.
- Se eliminaron cajas vacías, rótulos residuales y repeticiones visuales sin función.
- Se ajustaron contraste de portada y separación entre ecuaciones y definiciones.

El detalle de cada corrección se conserva en `review.md`.

## Cambios de v02 a final

- Se creó `unidad_01_nociones_basicas_final.pptx` sin sobrescribir v01 ni v02.
- Se preservó el contenido visible de las 94 slides. La comparación de renders produjo 94 coincidencias exactas.
- Se agregó a las notas de cada slide un bloque `[Sources]` derivado de `source_map.md`.
- Se conservaron las notas pedagógicas previas; el paquete final contiene 94 notes slides.
- Se restauró y verificó el texto alternativo de 73/73 imágenes después de la exportación.
- Se verificaron 2 masters, 27 layouts, 1 GIF, 2 enlaces externos y numeración en slides 2–94.
- Se ejecutó el control automático de desbordes y el control de fidelidad al template; ambos fueron aprobados.
- Se renderizaron nuevamente las 94 slides y se inspeccionaron visualmente por lotes.
- Se creó `output/contact_sheet_final.png`.
- Se verificó el PDF v02 de 94 páginas, incluida inspección visual de las páginas 1 y 94.
- Se creó `course_consistency_report.md` como línea de base para las unidades siguientes.
- Se creó `final_report.md` con el cierre académico, pedagógico y técnico.

## Estado final

- Problemas críticos abiertos: 0.
- Problemas mayores abiertos: 0.
- Problemas menores abiertos: 0.
- Sugerencias operativas abiertas: 3.

Las sugerencias abiertas no requieren cambios obligatorios en el deck: ensayo del ritmo, prueba del GIF en el aula y decisión sobre una posible demostración sonora en vivo.

## Cierre posterior a la reparación de diagramas — 2026-07-29

### Preservación de versiones

- La versión final anterior se conservó como `output/unidad_01_nociones_basicas_final_pre_diagram_fix.pptx`.
- Se conservaron `v01`, `v02`, `v02_diagram_fix` y el respaldo exacto `final_backup_before_diagram_fix`.
- El nuevo entregable ocupa el nombre estable `output/unidad_01_nociones_basicas_final.pptx`.

### Cambios incorporados

- Se integró la reparación de 72 usos de diagramas documentada en `diagram_repair_report.md`.
- Los diagramas estructurales se reconstruyeron con formas, textos, tablas y conectores editables.
- Los gráficos cuantitativos se regeneraron al tamaño final; los SVG y scripts permanecen en `assets/generated/diagram_fix/`.
- Se restauró el texto alternativo de los 16 objetos de imagen a partir de `slide_text.md`.
- Se actualizó `asset_manifest.csv` con las fuentes de producción de la reparación.

### Entregables de cierre

- `output/unidad_01_nociones_basicas_final.pptx`.
- `output/unidad_01_nociones_basicas_final.pdf`.
- `output/final_render/` con 94 PNG.
- `output/pdf_review_render/` con 94 PNG.
- `output/contact_sheet_final.png`.
- `output/contact_sheet_final_pdf.png`.

### Validaciones

- 94 slides, 94 notas, 94 bloques `[Sources]`, 2 masters y 27 layouts.
- 16/16 objetos de imagen con texto alternativo.
- 1.639 formas editables, 49 conectores y una tabla nativa.
- Numeración visible en slides 2–94.
- 1 GIF y 2 enlaces externos preservados.
- `slides_test.py`: aprobado, sin overflow.
- Render accesible frente al candidato reparado: 94/94 slides idénticas.
- PDF: 94 páginas, 16:9, render completo inspeccionado.
- Consistencia curricular, terminológica, notacional, pedagógica y visual: aprobada.
