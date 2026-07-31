# Registro de producción — Unidad 4

## Resultado

- Presentación: `output/unidad_04_sonido_magnitudes_v01.pptx`.
- PDF de revisión: `output/unidad_04_sonido_magnitudes_preview.pdf`.
- Vista mosaico: `output/contact_sheet.png`.
- Total: 125 diapositivas en formato 16:9.
- Base: template académico aprobado `fisica_acustica_template_v01.pptx`.
- Estructura conservada: 2 Slide Masters y 27 layouts del template.

## Fuentes de producción

Se construyó exclusivamente a partir del storyboard, `slide_text.md`, `speaker_notes.md`, `source_map.md`, `asset_manifest.csv`, la guía de estilo y los informes de validación de gráficos y diagramas de la Unidad 4.

## Editabilidad y accesibilidad

- Títulos, subtítulos, cuerpo, ecuaciones tipográficas, captions, créditos y numeración se mantienen como objetos editables.
- Los gráficos y diagramas se insertaron como SVG aprobados; las fotografías externas se insertaron sin deformación.
- Cada asset visual insertado tiene texto alternativo.
- Las 125 diapositivas contienen notas del orador, texto alternativo narrativo y bloque `[Sources]`.
- Los tres créditos externos visibles conservan enlace funcional a la fuente.
- No se aplanó ninguna diapositiva completa como imagen.

## Assets insertados

- 108 inserciones visuales: 84 de diagramas o ecuaciones anotadas, 21 de gráficos cuantitativos y 3 de imágenes externas.
- Se usaron al menos una vez los 38 assets visuales con estado `approved` en el manifiesto.
- `U04-CH-012` no se insertó porque continúa en estado `pending_approval`; U04-102 usa el diagrama aprobado `U04-DG-017`.
- Nueve slides con audio, video o GIF todavía no aprobados muestran una identificación de alternativa estática; no se incrustó multimedia pendiente.

## Diagramas en contexto de slide

Los diagramas se ubicaron en una franja de gran formato para conservar aproximadamente su escala tipográfica de diseño. Se revisaron las slides con diagramas en los renders finales y se verificó:

- texto legible y contenido dentro de cajas;
- conectores y puntas sin cubrir texto;
- etiquetas separadas de las líneas;
- ausencia de clipping de nodos y ecuaciones;
- captions fuera del área de conectores;
- declaración “figura no a escala” cuando corresponde.

Resultado: sin problemas críticos ni mayores en diagramas insertados.

## Gráficos en contexto de slide

- Se usó encuadre `contain` para conservar completos ejes, unidades, leyendas y notas internas del asset aprobado.
- Las escalas lineales o logarítmicas permanecen declaradas en el propio gráfico.
- No se usaron datos nuevos ni se modificaron las curvas aprobadas.

## Desviaciones y trazabilidad

- Los placeholders vacíos del template tienen geometría nula. Se conservaron master y layout, se retiró únicamente el contenido demostrativo local y se agregaron objetos editables dentro de la zona segura documentada.
- No fue necesario dividir slides ni modificar el storyboard o el texto aprobado.
- No existe una versión anterior de la presentación de Unidad 4; por lo tanto, no hubo reemplazos dentro de un PowerPoint previo.
- La producción insertó siempre el archivo final aprobado de cada asset y excluyó explícitamente los estados `pending_approval`, `shortlisted`, `proposed` y `rejected`.

## Verificación posterior

- Render de las 125 slides: completado a 1600 × 900 px.
- Vista mosaico en orden numérico: completada.
- PDF de revisión: 125 páginas.
- Control automático de desbordes: aprobado, sin contenido fuera del canvas.
- Inspección del PPTX: 125 slides, 125 notes slides, 2 masters y 27 layouts.
- Revisión manual de portada, divisores, slides textuales, gráficos, imágenes externas, diagramas y slides de respaldo: completada.

## Estado final

Producción aprobada para revisión docente. No se registran problemas críticos ni mayores abiertos.

## Actualización de revisión — v02

- Archivo: `output/unidad_04_sonido_magnitudes_v02.pptx`.
- Informe integral: `review.md`.
- Se corrigieron los 14 hallazgos `major` de la auditoría, incluidos gráficos con colisiones, visuales reutilizados que no correspondían a la consigna, notación matemática visible y ausencia de texto alternativo en el paquete.
- Se regeneraron los gráficos U04-CH-001, 006, 010, 011 y 014; se actualizaron el generador del deck y el texto visible de las slides afectadas.
- Se renderizaron y revisaron nuevamente las 125 diapositivas; las afectadas se comprobaron además a tamaño completo.
- Verificación final del paquete: 125 slides, 125 notes slides, 2 masters, 27 layouts, 99 imágenes con texto alternativo, 0 placeholders locales, 3 enlaces externos y fuentes directas Calibri, Calibri Light y Cambria Math.
- PDF de revisión: `output/unidad_04_sonido_magnitudes_v02_preview.pdf`, 125 páginas.
- Resultado: 0 problemas `critical` y 0 `major` abiertos; los asuntos menores y sugerencias pendientes están documentados en `review.md`.

## Versión final

- PowerPoint: `output/unidad_04_sonido_magnitudes_final.pptx`.
- PDF de revisión: `output/unidad_04_sonido_magnitudes_final_review.pdf`.
- Render: `output/render_final/`, 125 PNG.
- Hoja de contacto: `output/contact_sheet_final.png`.
- Se preservaron v01 y v02 sin sobrescribirlas.
- Se incorporaron las correcciones derivadas de la revisión pedagógica independiente y del informe de consistencia.
- Auditoría final: 125 slides, 125 notas, 2 masters, 27 layouts, 75 recursos visuales con texto accesible, 0 placeholders, 3 enlaces externos y numeración completa.
