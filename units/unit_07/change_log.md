# Registro de cambios — Unidad 7

## Final — 2026-08-11

**Archivo nuevo:** `output/unidad_07_psicoacustica_final.pptx`  
**Base preservada:** `output/unidad_07_psicoacustica_v02.pptx`

### Pedagogía y contenido

- Se convirtió la actividad isofónica de la slide 30 en una lectura cualitativa autosuficiente, con ejes, unidades, dos puntos y límite normativo explícito.
- Se etiquetaron las 18 slides complementarias como `AMPLIACIÓN` y se mantuvieron 13 slides `A DEMANDA`.
- Se transformaron 24, 51, 58, 81, 91 y 105 en ejemplos resueltos visibles: datos → sustitución → resultado → interpretación.
- Se redibujaron 74, 85, 103, 107 y 117 para corregir dirección causal, diferencia de recorridos, ambigüedad espacial y nodo integrador de la escena.
- Se normalizó la terminología a fon/son y señal enmascarante/enmascarador.
- Se eliminó la notación visible de programación (`abs(...)`) y la conversión errónea de subíndices en paréntesis.

### Multimedia y assets

- Se añadió `scripts/u07_generate_media.py`.
- Se generó `U07-MEDIA-001`, tonos de 250 Hz y 1 kHz con igual RMS digital nominal.
- Se generó `U07-MEDIA-006`, directo más copia a −6 dB con retardos de 5, 20 y 50 ms.
- Se actualizaron rutas, estado, licencia, fecha y notas en `asset_manifest.csv`.
- Se retiraron de las notas órdenes de reproducir U07-MEDIA-002, 003 y 007 inexistentes; los medios 004, 005 y 008 permanecen opcionales y condicionados.

### Diseño y producción

- Los cinco diagramas corregidos se construyeron con formas y conectores nativos.
- Se corrigieron solapamientos detectados en el primer render final de las slides 85, 103 y 117.
- Se retiraron pies repetitivos y códigos de producción de los diagramas proyectados; la trazabilidad se conserva en notas/manifiesto.
- Se dejó un solo bloque `[Sources]` por slide en el PowerPoint.
- Se preservaron masters, layouts, paleta, tipografías, numeración y versiones v01/v02.

### QA final

- Render completo repetido después de las correcciones: 134/134 PNG.
- PDF de revisión: 134 páginas.
- Inspección ampliada: 24, 30, 51, 58, 74, 81, 85, 91, 103, 105, 107 y 117.
- `slides_test.py`: aprobado, sin overflow.
- 44/44 imágenes con texto alternativo.
- 134/134 notas y 134 bloques `[Sources]`.
- 18 rótulos `AMPLIACIÓN`; 13 rótulos `A DEMANDA`.
- 0 relaciones externas; no hay enlaces rotos.
- 0 problemas críticos abiertos; 0 problemas mayores bloqueantes.

## v02 — 2026-08-11

- Corrección de errores críticos de texto editorial proyectado y temporalidad del enmascaramiento.
- Corrección de asignación de assets, clipping, reflexión, ecuaciones, alt text, divisores y preguntas de cierre.
- Primera aprobación visual completa; posteriormente reabierta por la revisión pedagógica independiente y el control de consistencia.

## v01 — 2026-08-11

- Primera producción completa de 134 slides a partir de brief, storyboard, texto, notas y manifiesto.
- Base inicial de gráficos, diagramas, layouts y render para revisión integral.
