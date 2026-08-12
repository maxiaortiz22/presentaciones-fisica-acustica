# Registro de cambios — Unidad 09

## Versiones conservadas

| Versión | Archivo | Estado |
|---|---|---|
| v01 | `output/unidad_09_propagacion_sonido_v01.pptx` | Primer deck producido y renderizado; se conserva como antecedente. |
| v02 | `output/unidad_09_propagacion_sonido_v02.pptx` | Revisión integral con problemas críticos y mayores corregidos; se conserva sin sobrescritura. |
| final | `output/unidad_09_propagacion_sonido_final.pptx` | Versión de cierre, derivada de v02 mediante correcciones localizadas. |

## Cambios de v01 a v02

- Se corrigieron recortes de títulos, pies superpuestos y desbordes.
- Se reconstruyeron diagramas, ejercicios y comparaciones de las slides señaladas en `review.md`.
- Se completaron definiciones, unidades, fórmulas y soluciones.
- Se reemplazaron pantallas editoriales o bloqueadas por contenidos cualitativos seguros.
- Se completaron tabla de símbolos, ejercicios, recapitulaciones, casos y bibliografía.
- Se incorporaron notas y descripciones accesibles en las 96 slides.

## Cambios de v02 a final

1. **Notación energética:** se normalizaron `Rₑ`, `α` y `τₑ` en las slides 37, 58, 59, 86 y 90; `R` queda reservado para el índice de reducción sonora en dB.
2. **Ecuación logarítmica:** se reemplazó `log10` por `log₁₀` y se explicitó `τₑ` en las slides 58–59.
3. **Captions:** se retiraron 51 códigos internos `U09-DG/CH-… · UCASAL` del área visible; la trazabilidad permanece en notas y manifiesto.
4. **Notas:** se eliminaron 84 campos “Demostración o revelado: No corresponde” y se sustituyeron tres preguntas genéricas recurrentes por consignas funcionales.
5. **Numeración:** se ensayó el uso exclusivo del campo dinámico del layout. Como no se visualizó en el render, se conservaron los 96 números locales, editables y sin duplicación visual.
6. **Accesibilidad:** se incorporó texto alternativo OOXML a las cuatro imágenes de gráficos.
7. **Producción:** se generaron un PowerPoint final nuevo, un render de 96 PNG y un PDF de revisión de 96 páginas.
8. **Consistencia:** se actualizaron `consistency_report.md`, `style/glossary.md`, `style/notation_guide.md` y `style/decision_log.md` sin homogeneizar las diferencias pedagógicas intencionales.
9. **Script de regeneración:** `u09_build_presentation.mjs` quedó alineado con los captions, la notación, la numeración efectiva y la nota de multimedia de la versión final.

## Verificaciones de cierre

- `slides_test.py`: aprobado.
- `u09_validate_final_deck.py`: aprobado; 96 slides, 96 notas, 2 masters, 27 layouts, 96 renders, 0 critical, 0 major.
- Auditoría OOXML: 96 bloques `[Sources]`, 96 números visibles, 0 códigos internos visibles, 4/4 imágenes con alt text, 0 relaciones externas y 0 archivos de audio/video embebidos.
- Revisión visual de las 96 slides y ampliación final de las slides 37, 58, 59, 86 y 90.

## Artefactos finales

- `../../output/unidad_09_propagacion_sonido_final.pptx` — copia final publicada.
- `output/unidad_09_propagacion_sonido_final.pptx` — copia de producción de la unidad.
- `output/unidad_09_propagacion_sonido_final_review.pdf`
- `output/unidad_09_propagacion_sonido_final/`
- `final_report.md`
- `review.md`
- `consistency_report.md`

SHA-256 del PowerPoint final: `0071FA5B817A01284F8891B1D70D9152C37CF7CCA5EEBA69197099683F64A8FA`.

## Problemas abiertos

- **Minor:** `U09-MEDIA-001` no tiene archivo de audio aprobado. La slide 55 conserva alternativa estática autosuficiente.
- **Suggestion:** falta una adopción normativa institucional completa para publicar máximos de ruido en cabinas.
- **Suggestion:** cualquier ampliación cuantitativa de absorción atmosférica o conversión modal deberá incorporar una fuente primaria y condiciones completas.

No quedan problemas críticos ni mayores.
