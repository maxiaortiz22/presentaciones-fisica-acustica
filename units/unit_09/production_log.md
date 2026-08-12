# Registro de producción — Unidad 09

## Corrección integral v02 — 2026-08-12

- Presentación corregida: `output/unidad_09_propagacion_sonido_v02.pptx`.
- Render final: `output/unidad_09_propagacion_sonido_v02/` (96 PNG).
- Se conservaron la v01, 96 slides, 2 masters, 27 layouts, 16:9 y 96 notas.
- Se corrigieron desbordes, títulos recortados, superposición del pie sobre el logo, notación matemática, captions incompletos y material editorial visible.
- Se desarrollaron el ejemplo de Sabine, ejercicios y soluciones de respaldo, tabla de notación, comparación de campos, banco de errores, resolución integradora y fuentes.
- Las slides 41, 88, 89 y 92 dejaron de ser pantallas bloqueadas: ahora ofrecen contenido cualitativo útil sin inventar ecuaciones, curvas o límites normativos.
- Validación final: `slides_test.py` sin overflow; `u09_validate_final_deck.py` con `status: pass`, 0 critical y 0 major.
- Archivo: 537.155 bytes; SHA-256 `4CBBBE5B68A7229DA8D22AACB333E71F3988A04C3E67BA6962382803F83F374B`.

La producción original de v01 se conserva a continuación como historial.

## Resultado

- Presentación: `output/unidad_09_propagacion_sonido_v01.pptx`.
- PDF de revisión: `output/unidad_09_propagacion_sonido_preview.pdf`.
- Vista mosaico: `output/contact_sheet.png`.
- Render individual: `output/unidad_09_propagacion_sonido_v01/` (96 PNG).
- Total: 96 diapositivas, en el mismo orden e identificación que el storyboard aprobado.
- Estado técnico: aprobado para revisión docente; 0 problemas críticos y 0 problemas mayores de producción abiertos.

## Base y construcción

- Template aprobado: `output/fisica_acustica_template_v01.pptx`.
- Formato: 16:9, 13,333 × 7,5 pulgadas.
- Jerarquía preservada: 2 Slide Masters y 27 layouts del template.
- Cada diapositiva se vinculó a un layout del template según `template-frame-map.json`; la validación de fidelidad del plan y del deck final terminó sin incidencias.
- Los títulos, subtítulos, cuerpos, captions, números y créditos son texto editable.
- Los diagramas insertados se reconstruyeron como formas y conectores editables cuando la fuente aprobada lo permitía.
- Los gráficos se insertaron como SVG validado; no se aplanó ninguna diapositiva completa.
- Se incorporaron notas del orador en las 96 diapositivas. Todas incluyen bloques de fuente y texto alternativo; la diapositiva U09-055 incluye además identificación de multimedia.
- No se agregaron hipervínculos externos porque el material aprobado no contenía URLs verificadas. La inspección OOXML encontró 0 relaciones externas pendientes o rotas.

## Recursos visuales insertados

- Diagramas: 63 instancias, construidas a partir de las versiones validadas más recientes de `diagram_source.json`.
- Gráficos: 7 instancias SVG correspondientes a 6 recursos únicos: U09-CH-002, U09-CH-003, U09-CH-005, U09-CH-006, U09-CH-007 y U09-CH-009. U09-CH-006 se reutilizó como alternativa estática en U09-055.
- U09-CH-001 y U09-CH-004 no se insertaron por separado porque las respectivas diapositivas emplean los diagramas editables validados U09-DG-010 y U09-DG-030, que cubren la misma función pedagógica sin duplicación visual.
- U09-DG-001 no se usó en portada para mantener el layout de portada aprobado.
- No se insertó ningún recurso marcado como bloqueado: U09-DG-032, U09-DG-048, U09-DG-067, U09-CH-008, U09-CH-010 y U09-CH-011.

## Desviaciones y decisiones trazables

No fue necesario dividir, eliminar ni reordenar diapositivas. Se conservaron los IDs U09-001 a U09-096 y la ruta central/complementaria/anexo indicada en el storyboard.

Las siguientes diapositivas mantienen una exclusión explícita para evitar introducir datos, constantes o referencias no aprobadas:

- U09-041: no se incorporó una formulación de Snell no validada; se muestra un estado de fuente pendiente.
- U09-063: se conservó únicamente la relación relativa de la ley de masa, sin constante absoluta.
- U09-088: no se incorporó una curva cuantitativa de absorción atmosférica sin datos aprobados.
- U09-089: se mantuvo una explicación cualitativa de modos, sin ecuaciones modales no validadas.
- U09-092: no se reprodujeron valores normativos sin la edición y tabla primaria verificadas.

Otros recursos previstos:

- U09-055: U09-MEDIA-001 está identificado en notas, pero no se incrustó porque no existe archivo local aprobado. Se utilizó U09-CH-006 como alternativa estática.
- U09-076: no se incorporó una fotografía externa porque no existe imagen aprobada en el manifiesto. Se mantuvo una composición textual editable y funcional.

## Reemplazos respecto de versiones anteriores

- No existía una versión anterior del PowerPoint de la Unidad 09; por lo tanto, no hubo reemplazos dentro de un deck previo.
- Durante esta producción se usaron explícitamente las fuentes finales aprobadas del manifiesto y se excluyeron las versiones bloqueadas o preliminares.
- No se modificaron crop, alineación o z-order por reemplazo posterior: la versión entregada fue renderizada después de la última inserción de cada recurso.

## Verificaciones realizadas

- Plan de template: 96/96 diapositivas mapeadas; 0 incidencias.
- Fidelidad al template: 2 masters y 27 layouts conservados; 0 incidencias.
- Render: 96/96 diapositivas generadas correctamente.
- PDF: 96 páginas verificadas.
- Control de desbordes: `slides_test.py` aprobado; sin overflow detectado.
- Control OOXML propio: tamaño 16:9, 96 notas, 0 placeholders vacíos, 0 imágenes sin texto alternativo y 0 imágenes a página completa.
- Revisión contextual de diagramas: 63/63 diapositivas con diagrama revisadas después de la inserción; sin clipping, desborde, solapamiento de texto ni interferencias mayores de flechas o etiquetas.
- Revisión visual: se inspeccionó la vista mosaico completa y una muestra ampliada de 20 diapositivas representativas, incluidas las cinco exclusiones de fuente.
- Resultado: 0 hallazgos críticos y 0 mayores abiertos de producción.

## Integridad de entregables

- PPTX — 552.912 bytes — SHA-256 `0BB4F55D40F54DE1E23EEB4AE117BBD972CF067AA8AAD5BC76FDB29AF4F79EF2`.
- PDF — 5.512.738 bytes — SHA-256 `270501BC2454B928670F80A84352D3EE17368D0EDCF16F0E59A3D5FF443EAD3A`.
- Contact sheet — 2.012.693 bytes — SHA-256 `CED406B10F6E3BDB9C71FA1BBFEBF2AC540B8CC1155A9241F8783925140A453D`.

## Scripts reproducibles

- `scripts/u09_inspect_template_full.mjs`: inspección completa del template.
- `scripts/u09_generate_template_plan.mjs`: mapeo storyboard–layout y auditoría previa.
- `scripts/u09_build_presentation.mjs`: construcción del PowerPoint y parche de texto alternativo.
- `scripts/u09_validate_final_deck.py`: validación estructural y de render.
- `scripts/u09_create_preview_pdf.py`: generación y comprobación del PDF de revisión.

## Pendientes editoriales

Las restricciones de U09-041, U09-063, U09-088, U09-089 y U09-092, junto con la fotografía de U09-076 y el archivo U09-MEDIA-001, requieren una fuente o archivo aprobado antes de incorporarse. No constituyen fallas técnicas del deck: están marcadas de forma explícita para impedir que se fabrique o atribuya contenido.

## Cierre final — 12 de agosto de 2026

La revisión v02 sustituyó los mensajes editoriales visibles de U09-041, U09-088, U09-089 y U09-092 por desarrollos cualitativos seguros. U09-063 conserva la relación relativa documentada. La fotografía de U09-076 fue reemplazada por un checklist editable y `U09-MEDIA-001` continúa como recurso opcional con alternativa estática.

Se generó `output/unidad_09_propagacion_sonido_final.pptx` dentro de la unidad y se publicó una copia idéntica en `../../output/unidad_09_propagacion_sonido_final.pptx`, sin sobrescribir v01 ni v02. La versión final normaliza `Rₑ`/`τₑ`, elimina códigos internos de captions, limpia notas de plantilla, conserva numeración visible verificada y añade alt text OOXML a los cuatro gráficos insertados.

Resultados finales:

- PowerPoint: 528.448 bytes; SHA-256 `0071FA5B817A01284F8891B1D70D9152C37CF7CCA5EEBA69197099683F64A8FA`.
- PDF de revisión: 96 páginas; SHA-256 `FF14043386076400A6372CACBAEC58497C7DBFC703962F4123BCFEC8DE65FEBD`.
- Render: 96/96 PNG.
- `slides_test.py`: aprobado, sin overflow.
- `u09_validate_final_deck.py`: aprobado, 0 critical y 0 major.
- Revisión visual: 96 slides en mosaico y slides 37, 58, 59, 86 y 90 a resolución completa tras la corrección localizada.
