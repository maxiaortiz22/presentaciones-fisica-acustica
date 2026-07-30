# Registro de cambios — Unidad 02

## Criterio de versionado

Se conservaron todas las versiones previas. La versión `final` es una promoción controlada de `v02`, sin reconstrucción ni cambios binarios, para preservar masters, layouts, notas, texto alternativo, enlaces y editabilidad.

## Historial

| Fecha | Versión | Archivo | Cambios principales | Estado |
|---|---|---|---|---|
| 2026-07-29 | v01 | `output/unidad_02_mecanica_termodinamica_v01.pptx` | primera producción completa de 110 slides, notas, recursos y PDF de revisión inicial | conservada |
| 2026-07-29 | v02 | `output/unidad_02_mecanica_termodinamica_v02.pptx` | corrección de todos los problemas `major`, alt text, ajustes de diagramas, gráficos, fórmulas y referencias | aprobada |
| 2026-07-29 | final | `output/unidad_02_mecanica_termodinamica_final.pptx` | promoción binaria de v02; sin cambios de contenido | publicada |

## Cambios de v01 a v02

### Gráficos y diseño

- Se reubicaron rótulos y anotaciones en U02-018 y U02-036.
- Se aumentaron márgenes y separaciones de ejes en U02-038, U02-040, U02-080, U02-081 y U02-103.
- Se regeneraron las figuras cuantitativas afectadas.
- Se corrigieron líneas de fuente recortadas o duplicadas en U02-019, U02-036, U02-044, U02-080 y U02-096.

### Diagramas

- Se separó la etiqueta `F_el + F_amort` del conector en U02-019, U02-044 y U02-096.
- Se verificaron nuevamente flechas, puntas, conectores, etiquetas, cajas y tamaños dentro de la slide final.

### Fórmulas y contenido

- Se recompuso en una línea el resultado del ejemplo de presión de U02-030.
- Se explicitó la unidad del coeficiente térmico en U02-103.
- Se reemplazaron instrucciones internas por referencias bibliográficas completas en U02-100 y U02-109.

### Accesibilidad y producción

- Se incorporaron 78 descripciones alternativas.
- Se conservaron 110 notas y 110 bloques `[Sources]`.
- Se volvió a renderizar el deck completo.
- Se ejecutaron pruebas de desborde y revisión visual de las 110 slides.

## Revisión de consistencia

La comparación con la guía de estilo, el mapa del curso, el glosario, la guía de notación, el template y la Unidad 1 produjo:

- `units/unit_02/consistency_report.md`;
- promoción de `style/glossary.md` como referencia canónica;
- promoción de `style/notation_guide.md` como referencia canónica;
- actualización de `style/decision_log.md` con D-052 y D-053;
- actualización de `style/presentation_style_guide.md`;
- conservación de los archivos `_draft.md` como enlaces de compatibilidad.

Las diferencias de extensión, densidad de ecuaciones, cantidad de diagramas y frecuencia de recapitulaciones se mantuvieron porque tienen una razón pedagógica.

## Cierre final

Se crearon, sin sobrescribir archivos anteriores:

- `output/unidad_02_mecanica_termodinamica_final.pptx`;
- `output/unidad_02_mecanica_termodinamica_final_review.pdf`;
- `output/unidad_02_mecanica_termodinamica_final_audit.json`;
- `scripts/u02_final_audit.py`;
- `final_report.md`;
- `change_log.md`.

El PDF final se generó a partir de los 110 PNG del render v02 aprobado. Se reabrió y verificó con 110 páginas de 960 × 540 pt, sin cifrado.

La auditoría final confirmó:

- 110 slides;
- 110 notas no vacías;
- 110 bloques `[Sources]`;
- 2 masters;
- 27 layouts;
- numeración correcta en 110/110 slides;
- 78 descripciones alternativas;
- 146 archivos multimedia internos;
- 2 enlaces externos;
- 102 filas de manifiesto sin IDs duplicados;
- 94 registros activos sin rutas faltantes;
- 110 renders de 1600 × 900 px.

La versión final y v02 son binariamente idénticas:

`SHA-256 31FC4F9BDC0A454FC47B752EA342A0D60AA0534AF499B15FD8CC2E710331A61F`

## Problemas abiertos

| ID | Severidad | Estado | Tratamiento |
|---|---|---|---|
| DR-009 / CG-A01 | `minor` | abierto | normalizar subíndices tipográficos en una futura pasada transversal |
| DR-010 / CG-A05 | `minor` / requiere decisión | abierto | convertir selectivamente a formas nativas cuando la edición directa lo justifique |
| DR-011 | `suggestion` | abierto | dictar por rutas y no proyectar las 110 slides de forma lineal |
| CG-A02–CG-A04 | requiere decisión | documentado | actualizar mapa, definir umbral OMML y normalizar vocabulario de metadata en tareas transversales |

No quedan problemas `critical` ni `major`.
