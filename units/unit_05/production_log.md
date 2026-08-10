# Registro de producción — Unidad 5

Versión: `v01`
Fecha: 2026-08-03
Nombre corto: `analisis_frecuencial`

## Resultado

- Presentación 16:9 de 150 slides.
- Se conservaron los 2 Slide Masters y los 27 layouts de la plantilla aprobada.
- Cada slide se creó duplicando la slide demostrativa del layout correspondiente; luego se retiró el contenido de muestra y se incorporó contenido editable.
- Los textos, ecuaciones tipográficas, cajas, callouts y conectores son editables.
- Los diagramas se reconstruyeron en el canvas 1280×720 a partir de sus `diagram_source.json` validados.
- Los gráficos aprobados se insertaron como SVG cuando el exportador lo admitió, con respaldo PNG de alta resolución en el repositorio.
- Se conservaron captions, créditos, numeración del template, notas del orador, enlaces y texto alternativo.

## Fuentes de producción

- `output/fisica_acustica_template_v01.pptx`.
- `units/unit_05/storyboard.md`.
- `units/unit_05/slide_text.md`.
- `units/unit_05/speaker_notes.md`.
- `units/unit_05/source_map.md`.
- `units/unit_05/asset_manifest.csv`.
- `units/unit_05/charts_review.md`.
- `units/unit_05/diagram_validation_report.md`.
- `units/unit_05/diagram_assets_review.md`.
- `style/` y catálogo de layouts/componentes.

## Assets insertados

- 13 familias de gráficos cuantitativos aprobadas, usadas en 34 slides.
- 14 familias de diagramas aprobadas, usadas o adaptadas en 77 slides.
- Una fotografía externa aprobada: `U05-EXT-003`, sonómetro, en U05-118; se mantuvo proporción, se mostró el equipo completo y se agregó crédito visible.
- Tres enlaces externos funcionales en U05-132: IEC 61672-1, IEC 61260-1 y NIOSH.
- Los recursos de audio/video todavía propuestos no se incrustaron. U05-020, U05-048 y U05-102 conservan alternativas estáticas y la indicación de reproducción opcional en notas.
- No se insertaron `U05-CH-004`, `U05-CH-009`, `U05-CH-010`, `U05-CH-012`, `U05-CH-014`, `U05-CH-017` ni `U05-DG-011`, porque continúan bloqueados o `pending_standard_check`.

## Desviaciones respecto del storyboard

| Slide | Desviación | Motivo y trazabilidad |
|---|---|---|
| U05-078 | Se usó la alternativa diagramática aprobada `U05-DG-008`; no se insertó `U05-EXT-001`. | El recorte de la fotografía de ecografía no permitía minimizar de forma suficiente rostro y exposición corporal dentro del layout final. Se preservó el propósito pedagógico con un esquema editable. |
| U05-121 | El panel visible conserva el cálculo en tres pasos y el resultado `77,4 dB`; la fórmula larga no se repitió debajo del gráfico. | La versión preliminar excedía el ancho disponible. Se eliminó la duplicación visual, sin perder el procedimiento ni el resultado. |
| U05-132 | Se incorporaron enlaces oficiales verificados y se ajustó el caption. | Los URLs ya estaban registrados en `asset_manifest.csv`; el requisito de producción exige enlaces funcionales. |

No fue necesario dividir slides. Por lo tanto, `storyboard.md` y `slide_text.md` no requirieron renumeración ni cambios estructurales.

## Reemplazos respecto de una versión anterior

No se encontró un PowerPoint anterior de Unidad 5 en `units/unit_05/output/`; `v01` es la primera versión producida. Durante el ciclo interno de producción se reemplazaron explícitamente las iteraciones preliminares por la versión final para corregir:

- títulos duplicados en portada y divisores;
- una fórmula larga fuera de su panel en U05-121;
- el layout de enlaces de U05-132;
- el encuadre y crédito del sonómetro en U05-118;
- la alternativa visual de U05-078;
- la serialización del texto alternativo.

## Verificación automática y visual

- Render PowerPoint: 150 de 150 slides a 1600×900 px.
- Vista mosaico: 150 slides, revisadas después de la última modificación visible y después del ajuste de accesibilidad.
- `slides_test.py`: aprobado; cero desbordes detectados.
- PDF: 150 páginas, MediaBox 960×540 pt, proporción 16:9.
- Render PDF con Poppler: 150 de 150 páginas; mosaico final revisado.
- Open XML: 150 slides, 150 notes slides, 2 masters, 27 layouts.
- Notas: 150 de 150 contienen bloque `[Sources]`.
- Accesibilidad: 150 resúmenes alternativos de slide; 31 de 31 imágenes serializadas con descripción alternativa.
- Enlaces externos: 3 relaciones activas.

## Revisión de diagramas en contexto

- Se revisaron 77 slides que contienen diagramas aprobados o adaptaciones directas de sus familias.
- Se inspeccionaron individualmente muestras de ecuación anotada, bandas y árbol de decisión a tamaño 1600×900.
- Resultado: cero colisiones críticas o mayores; ninguna flecha tapa texto; las puntas terminan en bordes; las etiquetas no se apoyan sobre conectores; no hay clipping; cajas y padding permanecen legibles.
- Tipografía de diagramas: cuerpos de 22,5 pt o mayores, títulos de nodo de 24 pt o mayores y ecuaciones centrales de 28 pt o mayores.

## Archivos y huellas

| Archivo | SHA-256 |
|---|---|
| `unidad_05_analisis_frecuencial_v01.pptx` | `19564272BF73FE9DAAA21D4F8623F2B6BF734293BEE77344892D745F70AB5A01` |
| `unidad_05_analisis_frecuencial_preview.pdf` | `46F7DDF79FF0A9765FD573F2D10F326BFBBCF114937A8CA2C1491F77AA83DF3C` |
| `contact_sheet.png` | `5EE1A4C215F0C1728A7F4F930C2E6A43384A8194F9F0EB3EDC3A8A7C3B7369BB` |

## Estado

Aprobado para revisión docente. Problemas críticos abiertos: ninguno. Problemas mayores abiertos: ninguno.
