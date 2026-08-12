# Registro de producción — Unidad 08

## Resultado

- Presentación: `output/unidad_08_salud_auditiva_v01.pptx`.
- Revisión PDF: `output/unidad_08_salud_auditiva_preview.pdf` (114 páginas).
- Mosaico: `output/contact_sheet.png` (114 diapositivas rotuladas).
- Versión: `v01`, producida el 2026-08-12.
- Nombre corto: `salud_auditiva`.
- No se construyó una versión previa de la Unidad 08 contra la cual comparar objetos; por lo tanto, no hubo reemplazos dentro de un deck anterior.

## Base y estructura

- Se utilizó el template aprobado `output/fisica_acustica_template_v01.pptx` mediante un starter de 114 diapositivas preparado desde sus layouts.
- Formato confirmado: 12.192.000 × 6.858.000 EMU, relación 1,777778 (16:9).
- Estructura OOXML final: 114 slides, 114 notes slides, 2 Slide Masters y 27 layouts.
- Se conservaron identidad UCASAL, riel superior, pie institucional, numeración y jerarquía tipográfica del sistema visual.
- El orden, la cantidad de slides y la ruta pedagógica del storyboard se conservaron. No fue necesario dividir slides ni renumerar el storyboard.
- Texto, paneles, tablas conceptuales, conectores, procesos, ecuaciones y numeración se construyeron como objetos editables; no hay slides aplanadas como imagen.
- Las 114 slides contienen notas del orador. Las notas incorporan fuentes y texto alternativo del contenido proyectado.

## Recursos incorporados

### Gráficos cuantitativos

Se insertaron como SVG los seis gráficos aprobados y aplicables:

- `U08-CH-001` — slide 22.
- `U08-CH-005A` — slide 48.
- `U08-CH-010` — slide 75.
- `U08-CH-008` — slide 78.
- `U08-CH-009` — slide 89.
- `U08-CH-011` — slide 110.

Los seis objetos tienen texto alternativo no vacío, caption/crédito visible y mantienen sus ejes, unidades y aclaraciones de carácter conceptual. No se insertaron los gráficos bloqueados `U08-CH-002`, `003`, `004`, `005`, `006` y `007`; sus slides conservan explicaciones o actividades sin inventar datos.

### Diagramas y ecuaciones

Los recursos de `diagram_validation_report.md` fueron revisados nuevamente en el tamaño real del área útil de las slides. Las exportaciones individuales ocupan un canvas completo 16:9 e incluyen título y pie propios. La inserción recortada en el template produjo problemas mayores en contexto: clipping de nodos, rótulos sobre conectores, duplicación de títulos y pérdida de padding.

Por ese motivo, la versión final no inserta esas exportaciones raster/SVG recortadas. Se reemplazaron durante producción por composiciones nativas editables basadas en el mismo objetivo pedagógico: cajas, paneles, conectores, comparaciones, procesos y ecuaciones. En particular se corrigieron y redistribuyeron las slides 31, 43, 66, 77, 82 y 101. La slide 82 se resolvió como tres paneles OEA–PEAT–ECoG; la slide 66 como proceso de cuatro etapas; la slide 101 como seis preguntas transferibles.

Las ecuaciones anotadas se expresaron como texto matemático editable y paneles de interpretación cuando fue posible. `U08-DG-011` y `U08-DG-029` permanecen bloqueados según el informe aprobado. `U08-DG-042` no se utilizó porque su cálculo 82 − 60 = 22 dB contradice el ejemplo redactado para la slide 88 (70 − 52 = 18 dB); se preservó el ejemplo del storyboard/slide text.

Este reemplazo es una desviación de implementación respecto de las referencias de asset del storyboard, no una modificación del contenido, del orden ni de la idea central de las slides. Ninguna versión preliminar de los diagramas quedó dentro del PPTX final.

### Imágenes y multimedia

- No se incorporaron fotografías externas: las entradas correspondientes del manifiesto permanecen `shortlisted` o pendientes de recorte/aprobación.
- No se embebieron videos o GIF: las slides multimedia incluyen alternativa estática y la indicación de reproducción en las notas, sin descargar ni incorporar recursos no aprobados.
- No se añadieron enlaces externos nuevos fuera de los ya registrados en fuentes/notas.

## Revisión de diagramas en contexto

Se renderizó cada slide y se revisó el mosaico completo. En las composiciones editables finales:

- las flechas terminan en los bordes de las cajas y no cubren texto;
- no hay etiquetas apoyadas sobre conectores;
- el texto entra en las cajas sin `shrink-to-fit`;
- se mantuvieron fuentes de aula legibles y padding interno;
- no se observan clipping, superposición o recorte de elementos;
- no quedan problemas críticos ni mayores.

Los diagramas 16:9 recortados que fallaron esta verificación fueron eliminados explícitamente del deck antes de producir los entregables finales.

## Controles posteriores

- Render completo: 114/114 PNG generados.
- Vista mosaico: regenerada desde el PPTX final y revisada visualmente.
- PDF: 114/114 páginas verificadas.
- `slides_test.py`: aprobado; `No overflow detected`.
- Inspección de objetos: 114 notas, 6 imágenes SVG, 0 placeholders locales vacíos y 0 textos internos de producción visibles.
- Texto alternativo: 6/6 gráficos con `alt` no vacío; el contenido editable cuenta además con descripción en las notas.
- Formato: 16:9 confirmado por lectura de `presentation.xml`.
- No se detectaron slides completas aplanadas como imagen.

## Desviaciones y pendientes abiertos

- Las referencias a diagramas aprobados se implementaron como composiciones editables del deck debido a la falla de sus exportaciones completas al insertarse dentro del layout. Esto favorece legibilidad, editabilidad y cumplimiento de la validación en contexto.
- Los contenidos que dependen de fuentes cuantitativas o decisiones docentes pendientes permanecen explicativos, sin completar curvas ni cifras por inferencia. Afectan especialmente a las ampliaciones relacionadas con `U08-CH-002`/U08-023 y U08-111, y `U08-CH-004`/U08-035 y U08-112.
- Continúan pendientes las decisiones documentadas sobre descriptor de exposición, simbología audiométrica, referencia dB SL y profundidad/unidad timpanométrica.
- Los recursos multimedia siguen identificados pero no embebidos hasta contar con selección, recorte y aprobación final.

## Trazabilidad técnica

- Script de armado: `scripts/u08_build_presentation.mjs`.
- Plan de duplicación de layouts: `scripts/u08_generate_template_plan.mjs`.
- Preparación de recortes evaluados y descartados: `scripts/u08_prepare_diagram_crops.py`.
- Generación del PDF de revisión: `scripts/u08_create_preview_pdf.py`.
- SHA-256 PPTX: `7B0B7053937CD97D98B6BC89AC72447B639394AE6661F61F6834CDE0BDD39580`.
- SHA-256 PDF: `6F21923C7ACDBB4C448CAA10185D08A8BED650EA5CC9B01ADD054383DA2747C6`.
- SHA-256 mosaico: `CDE1769F7D9DDFBC2CDEE5F1A0AD57C53E7E435C938AD5059ADB151195AA9EA7`.

---

## Revisión integral y corrección — v02

- Presentación: `output/unidad_08_salud_auditiva_v02.pptx`.
- Render: `output/unidad_08_salud_auditiva_v02/` (114 PNG).
- Hoja de contacto: `output/unidad_08_salud_auditiva_v02_contact_sheet.png`.
- Informe: `review.md`.
- Fecha: 2026-08-12.

### Cambios principales

- Se corrigieron dos fallas críticas: contenido de fones/sones ajeno a la Unidad 8 en U08-051 y correcciones genéricas sobre 0 dB SPL en seis slides de error frecuente.
- Se reconstruyeron procesos y diagramas editables, especialmente U08-038, U08-046 y U08-085, con conectores anclados detrás de los nodos y sin cruces sobre texto.
- Se materializaron mapas, recapitulaciones, tablas y gráficos que en v01 estaban vacíos, incompletos o mostraban scaffolding.
- Se completaron los ejercicios U08-107–110 con datos y ecuaciones del capítulo; U08-110 usa 10, 15 y 21 dB a 500, 1000 y 2000 Hz.
- Se cubrió el requisito de riesgo porcentual ocupacional en U08-035 y U08-112 mediante el modelo NIOSH 1997, con definición de exceso de riesgo, edad, exposición e IC 95 %.
- Se actualizaron `slide_text.md`, `speaker_notes.md`, `source_map.md` y `asset_manifest.csv` para reflejar las correcciones y eliminar bloqueos obsoletos.
- `U08-CH-011` quedó marcado como superado por una composición nativa porque sus datos de v01 no coincidían con el ejemplo del libro.
- Se serializó texto alternativo en las 5 imágenes de contenido; las 114 notas conservan además una descripción `[Alt text]`.

### Controles finales v02

- PowerPoint: 114 slides, 114 notas, 2 masters, 27 layouts y 16:9.
- Archivo: 659.403 bytes, sin macros y sin fuentes embebidas no estándar.
- Render: 114/114 slides generado desde el PPTX final.
- Revisión visual: hoja de contacto completa y slides afectadas a tamaño completo.
- `slides_test.py`: `Test passed. No overflow detected.`
- Texto alternativo: 5/5 imágenes de contenido con descripción OOXML no vacía.
- Hallazgos abiertos: 0 `critical`, 0 `major`; quedan decisiones editoriales y multimedia no bloqueantes registradas en `review.md`.

### Trazabilidad v02

- Script de armado: `scripts/u08_build_presentation.mjs`.
- SHA-256 PPTX: `2A4A8903B1CD491A86D6EE702D374D43EA3AB79F5D3361CC1CF3BBBE86B5699A`.
- SHA-256 hoja de contacto: `7A0A2A621F1E4F9528D1CF8001E029A69F3297A791AFC51084CAEE1D21DEBED8`.
