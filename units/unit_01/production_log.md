# Unidad 1 — Registro de producción del PowerPoint v01

Fecha de producción: 2026-07-28  
Rama: `codex/unidad-01-presentacion`

## Entregables

- `output/unidad_01_nociones_basicas_v01.pptx`
- `output/unidad_01_nociones_basicas_preview.pdf`
- `output/contact_sheet.png`

## Base de producción

- Template aprobado: `output/fisica_acustica_template_v01.pptx`.
- Storyboard aprobado: 94 diapositivas.
- Texto visible y notas: `slide_text.md` y `speaker_notes.md`.
- Recursos: `asset_manifest.csv`, figuras reproducibles y alternativas estáticas.
- Sistema visual: `presentation_style_guide.md`, catálogo de layouts y especificación de Slide Master.

## Estructura resultante

- Formato: 16:9.
- Diapositivas: 94.
- Slide Masters conservados: 2.
- Layouts disponibles conservados: 27.
- Layouts usados por el storyboard: 25.
- Notas del orador: 94 de 94 slides.
- Slides con figuras aprobadas: 73.
- Figuras propias diferentes utilizadas: 26 de 26 (`U01-CH001` a `U01-CH026`).
- Textos, formas y ecuaciones introductorias: editables.
- Hipervínculos externos: BIPM y NIST en U01-093.
- Texto alternativo: incorporado en cada figura insertada y documentado en las notas.

## Decisiones de montaje

- Se duplicó una slide fuente del template por cada slide de salida y se preservó la relación master–layout–slide.
- La selección de layout sigue la columna `suggested_layout` del storyboard.
- Las figuras científicas se insertaron como PNG de alta resolución generado desde los SVG reproducibles. Los SVG y scripts permanecen disponibles en `assets/generated/`.
- Las ecuaciones se conservaron como texto editable en Cambria Math. No se convirtieron a objetos OMML por limitaciones de edición confiable del importador.
- La animación de propagación está identificada en notas y manifiesto; el deck y el PDF incluyen su alternativa estática para uso sin conexión.
- Las ampliaciones y respuestas de ejercicios se mantuvieron principalmente en notas o slides de respaldo.

## Desviaciones respecto del storyboard

- No fue necesario dividir ni agregar slides: se mantuvieron las 94 previstas.
- No hubo cambios de orden ni de bloque.
- Los layouts `FA_04_TITULO_CONTENIDO` y `FA_06_VISUAL_TEXTO_40_60` no se usan porque el storyboard aprobado no los solicita.
- Los gráficos no se reconstruyeron como charts nativos de PowerPoint: se priorizó fidelidad científica, legibilidad y trazabilidad mediante SVG/PNG más scripts reproducibles.
- El PDF representa el estado estático de las animaciones y multimedia.

## Controles ejecutados

1. Auditoría de las 27 slides fuente del template y mapeo completo en `template-frame-map.json`.
2. Validación del plan de reutilización antes de duplicar las slides.
3. Render de las 94 slides desde el deck editable.
4. Revisión visual en cuatro mosaicos de 24 slides y revisión puntual a tamaño completo.
5. Corrección de placeholders, títulos, asignación de texto por tamaño de contenedor y selección específica de U01-CH026.
6. Control automático con `slides_test.py`: **aprobado, sin desbordes detectados**.
7. Exportación del PDF mediante Microsoft PowerPoint.
8. Verificación del PDF: 94 páginas.
9. Render de las 94 páginas del PDF con Poppler y generación del mosaico final.
10. Verificación estructural del PPTX: 94 slides, 94 notes slides, 2 masters, 27 layouts.

## Resultado

El archivo v01 queda listo para revisión docente de contenido y ritmo de exposición. No se registran problemas críticos de producción ni desbordes automáticos.

---

# Unidad 1 — Registro de revisión y corrección v02

Fecha: 2026-07-28  
Rama: `codex/unidad-01-presentacion`

## Entregables v02

- `output/unidad_01_nociones_basicas_v02.pptx`
- `output/unidad_01_nociones_basicas_v02_preview.pdf`
- `output/contact_sheet_v02.png`
- `review.md`

## Alcance de la corrección

- Revisión comparada con programa oficial, capítulo LaTeX, PDF del libro, storyboard, textos, notas y manifiesto de recursos.
- Inspección visual de las 94 slides de v01.
- Corrección de cobertura visible, fórmulas, recapitulaciones, ejercicios, slides de respaldo y referencias.
- Segunda revisión visual de las 94 slides de v02 y control individual de las slides afectadas.
- Preservación de la versión v01 y de la estructura master–layout–slide.

## Cambios principales

- Se completaron la definición de acústica, la tabla del SI, recapitulaciones y respaldo.
- Se separaron ecuaciones, símbolos, unidades e interpretación.
- Se corrigió la inconsistencia de 68 m frente a 100 m en el ejercicio de propagación.
- Se eliminaron cajas vacías, captions duplicados, títulos genéricos y solapamientos con imágenes.
- Se incorporó numeración editable en 2–94.
- Se incorporó el GIF de propagación y su alternativa estática.
- Se completó la bibliografía técnica con enlaces a BIPM y NIST.
- Se aplicó texto alternativo a las 73 imágenes mediante PowerPoint nativo.

## Estructura final

- Formato: 16:9.
- Diapositivas: 94.
- Notas: 94.
- Slide Masters: 2.
- Layouts: 27.
- Imágenes con texto alternativo: 73/73.
- GIF: 1.
- Enlaces externos: 2.
- Fuentes: Calibri, Calibri Light y Cambria Math.
- Peso del PPTX: 3.344.694 bytes.

## Verificaciones

1. Render final de las 94 slides.
2. Mosaico final actualizado.
3. Revisión visual de todas las slides y de cada slide corregida.
4. `slides_test.py`: aprobado, sin desbordes.
5. Control de fidelidad del template: aprobado, 0 incidencias.
6. Verificación estructural: 94 slides, 94 notes slides, 2 masters y 27 layouts.
7. Verificación de accesibilidad: 73/73 imágenes con descripción.
8. Verificación de multimedia y enlaces: 1 GIF y 2 enlaces externos.
9. PDF de revisión generado desde los renders validados: 94 páginas.

## Desviaciones y decisiones

- El PDF v02 es un documento de revisión rasterizado a partir de los renders finales; el PowerPoint conserva todos sus elementos editables.
- PowerPoint nativo se usó únicamente para serializar el texto alternativo, ya que el exportador de edición no lo persistía en el paquete.
- No se alteraron el orden, los bloques ni la cantidad de slides del storyboard aprobado.

## Resultado

No quedan problemas críticos, mayores ni menores abiertos. Las sugerencias restantes se refieren al ensayo de ritmo y a la comprobación del GIF en el equipo del aula.

## Cierre y versión final

- Se generó `output/unidad_01_nociones_basicas_final.pptx` sin sobrescribir v01 ni v02.
- Se agregaron bloques `[Sources]` a las notas de las 94 slides a partir de `source_map.md`.
- Se restauró y verificó texto alternativo en 73/73 imágenes.
- Se comprobó la estructura real del paquete: 94 slides, 94 notes slides, 2 masters, 27 layouts, 27 medios, 1 GIF y 2 vínculos externos.
- Se ejecutó `slides_test.py`: aprobado, sin desbordes.
- Se ejecutó el control de fidelidad del template: aprobado, 0 incidencias.
- Se compararon los renders de v02 y final: 94/94 coincidencias exactas.
- Se inspeccionaron visualmente las 94 slides finales por lotes.
- Se creó `output/contact_sheet_final.png`.
- Se verificó el PDF v02: 94 páginas, formato 16:9, primera y última página correctas.
- Se creó `final_report.md`, `change_log.md` y `course_consistency_report.md`.

La versión final conserva el contenido visible aprobado de v02 y mejora la trazabilidad documental en las notas.
