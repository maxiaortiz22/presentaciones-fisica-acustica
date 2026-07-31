# Unidad 3 — Registro de cambios

**Nombre corto:** `mecanica_ondulatoria`  
**Fecha de cierre:** 2026-07-30

## Resumen de versiones

| Versión | Archivo | Estado | Descripción |
|---|---|---|---|
| v01 | `output/unidad_03_mecanica_ondulatoria_v01.pptx` | preservada | Primera producción completa de 96 slides. |
| v02 | `output/unidad_03_mecanica_ondulatoria_v02.pptx` | aprobada | Revisión correctiva integral; 0 críticos y 0 mayores abiertos. |
| final | `output/unidad_03_mecanica_ondulatoria_final.pptx` | vigente | Copia binariamente idéntica de v02 después de la auditoría de cierre. |

## Desarrollo previo a v01

- Se analizaron el programa oficial, el capítulo LaTeX y el libro en PDF.
- Se produjeron `brief.md`, inventario de contenido, mapa de fuentes y storyboard de 96 slides.
- Se redactaron texto visible y notas del orador para la secuencia completa.
- Se crearon 13 familias de gráficos y 25 familias de diagramas propios.
- Se organizó un manifiesto de 49 recursos con estado, fuente, licencia y path.
- Se generaron 23 gráficos y 57 diagramas utilizados en el deck.

## v01 — Primera producción

- Se construyeron 96 slides en formato 16:9.
- Se preservaron 2 masters y 27 layouts del template.
- Se incorporaron notas del orador y bloques `[Sources]` en todas las slides.
- Se insertaron 80 visuales propios con título o texto alternativo.
- Se incorporó numeración completa.
- Se generaron PDF, 96 PNG y hoja de contacto.
- Se conservaron alternativas estáticas para toda multimedia no aprobada.

## v02 — Revisión correctiva

- Se corrigió la conversión de puntos a píxeles CSS en los generadores SVG.
- Se regeneraron y reemplazaron los 80 visuales.
- Se elevó el texto de diagramas a 22 pt para contenido principal y 20 pt para etiquetas auxiliares.
- Se reemplazaron los gráficos densos de U03-072, U03-073 y U03-074 por un caso de superposición por slide.
- Se redujo U03-075 a tres casos canónicos con la resultante oculta.
- Se eliminaron códigos internos y lenguaje de producción en U03-003, U03-013, U03-061, U03-082 y U03-088.
- Se corrigió el orden de capas de los SVG reemplazados.
- Se reexportaron el PDF y los 96 PNG.
- Se revisaron todas las slides y nuevamente las afectadas a resolución completa.
- Resultado: 0 problemas críticos y 0 problemas mayores abiertos.

## Revisión de consistencia

- Se comparó U3 con template, sistema visual, mapa del curso, glosario, notación y U1–U2.
- Se conservaron como intencionales la segmentación, las recapitulaciones, la variable genérica `ξ(x,t)` y el formalismo avanzado en respaldo.
- Se actualizó el criterio transversal para rapidez de propagación `c`.
- Se añadieron al glosario perturbación mecánica y diferencia de fase o desfase.
- Se registraron D-054, D-055 y D-056 en `style/decision_log.md`.
- Se documentaron cuatro inconsistencias editoriales locales y tres decisiones técnicas globales para futuras versiones.

## Cierre y versión final

- Se verificó la existencia y estado de todos los entregables exigidos por `AGENTS.md`.
- Se comprobaron 96 slides, 96 notas, 96 bloques `[Sources]`, 2 masters, 27 layouts, 80 visuales con texto alternativo, 0 placeholders vacíos y 0 auto-shrink.
- Se verificaron 49 IDs únicos en el manifiesto y 39 recursos aprobados sin paths faltantes.
- Se comprobaron un PDF de 96 páginas y 96 PNG de 1600 × 900 px.
- Se verificó la integridad ZIP/OOXML del PowerPoint.
- Se creó `output/unidad_03_mecanica_ondulatoria_final.pptx` sin sobrescribir v01 o v02.
- La versión final conserva exactamente el contenido de v02:
  - tamaño: 10.109.523 bytes;
  - SHA-256: `b5b45bec4e14c9403602ec18cc15cdfd84f750dbe9a78e7ee2ef5d2062897217`.
- Se crearon `final_report.md` y este `change_log.md`.

## Pendientes no bloqueantes

- Elevar textos secundarios de U03-013, U03-025, U03-087 y U03-096 si cambia el contexto de proyección.
- Corregir coma decimal, subíndices visibles y captions duplicados en una futura revisión editorial.
- Decidir el criterio global para OMML y para diagramas nativos frente a SVG.
- Definir un vocabulario controlado del manifiesto.
- Incorporar multimedia solo después de aprobación, verificación de licencia y prueba técnica.
- Considerar enlaces internos hacia el respaldo si se requiere navegación no lineal.

