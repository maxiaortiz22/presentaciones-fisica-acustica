# Unidad 5 — Informe final

Fecha de cierre: 2026-08-03
Estado: **cerrada con observaciones menores documentadas; 0 problemas críticos y 0 problemas mayores abiertos**.

## Entregables finales

- PowerPoint de entrega: `output/unidad_05_analisis_frecuencial_final.pptx`.
- Copia de trabajo trazable: `units/unit_05/output/unidad_05_analisis_frecuencial_final.pptx`.
- PDF de revisión: `units/unit_05/output/unidad_05_analisis_frecuencial_final_review.pdf`.
- Render: `units/unit_05/output/unidad_05_analisis_frecuencial_final/`, 150 PNG.
- SHA-256 del PowerPoint final: `2D00BF0391C3B7F133BE28F965AE69F9FDFC76B6492905FE65A27962F4AF3AF7`.

Las versiones `v01` y `v02` se conservaron sin sobrescritura.

## Resumen cuantitativo

| indicador | resultado |
|---|---:|
| Slides totales | 150 |
| Ruta central | 77 |
| Ampliación | 55 |
| Respaldo | 18 |
| Bloques | 14: B00–B13 |
| Duración central estimada | 384 min, más pausas y actividades |
| Distribución recomendada | 6 encuentros de 55–70 min |
| Banco completo | 768 min; no proyectar linealmente |
| Notas del orador | 150/150, todas con bloque de fuentes |
| Masters / layouts | 2 / 27 |
| Formas editables / imágenes | 1658 / 27 |
| Enlaces externos | 3, verificados con respuesta HTTP 200 |
| Tamaño del PPTX | 2.90 MB |

## Bloques

1. B00 — Apertura y orientación.
2. B01 — Representaciones de señal.
3. B02 — Herramientas de Fourier.
4. B03 — Registro digital.
5. B04 — Ventanas y tiempo–frecuencia.
6. B05 — Señal y sistema.
7. B06 — Componentes y terminología espectral.
8. B07 — Rangos y límites.
9. B08 — Octavas y bandas.
10. B09 — Filtros.
11. B10 — Ponderaciones.
12. B11 — Sonómetro y descriptores.
13. B12 — Integración y cierre.
14. B13 — Respaldo formal y técnico.

## Cobertura del programa

La cobertura es completa. La presentación incluye:

- series y transformada de Fourier, con DFT/FFT diferenciadas;
- espectro, respuesta en frecuencia y representación tiempo–frecuencia;
- muestreo, duración de registro, bins, resolución y ventanas;
- infrasonido, rango audible y ultrasonido;
- rangos dinámicos vocal, instrumental y auditivo bajo condiciones declaradas;
- frecuencia fundamental, armónicos, parciales, sobretonos y formantes;
- armónicos frente a octavas;
- división del espectro en bandas, centro geométrico, límites y ancho;
- filtros pasa bajos, pasa altos, pasa banda y elimina banda;
- ponderaciones A, C y Z y límite del ejemplo tonal;
- sonómetro, cadena de medición, nivel equivalente, máximo y pico;
- aplicaciones a voz, audífono, medición y ambiente audiométrico;
- errores frecuentes, recapitulaciones, preguntas y caso integrador.

## Recursos multimedia

No se incrustaron audios ni videos. La decisión evita dependencias de reproducción y deja alternativas estáticas completas. La slide U05-132 contiene tres enlaces oficiales verificados:

- IEC 61672-1;
- IEC 61260-1;
- NIOSH Sound Level Meter App.

## Gráficos propios

Se conservan 13 familias aprobadas de gráficos reproducibles, utilizadas en 34 slides: CH-001, CH-002, CH-003, CH-005, CH-006, CH-007, CH-008, CH-011, CH-013, CH-015, CH-016, CH-018 y CH-019. Cada familia dispone de script, datos o descripción reproducible, exportación y validación en `assets/generated/charts/`.

## Diagramas propios

Se conservan 14 familias aprobadas de diagramas editables o adaptados a la slide final, utilizadas en 77 slides: DG-001–010 y DG-012–015. La revisión renderizada no encontró flechas sobre texto, etiquetas montadas en conectores, cruces de contenido, desbordes ni puntas dentro de áreas tipográficas.

## Slides complementarias

- 55 slides llevan la etiqueta visible `AMPLIACIÓN`.
- 18 slides llevan la etiqueta `RESPALDO`.
- 77 slides llevan la etiqueta `CENTRAL`.

El banco completo se conserva para selección docente. El formalismo integral, la forma compleja, la DFT formal y otros detalles técnicos no forman parte de la proyección automática.

## Fuentes principales

- programa oficial de Física Acústica 2025;
- libro del curso, capítulo 5, LaTeX y PDF, pp. 119–149;
- IEC 61260-1 e IEC 61672-1/2/3 en los alcances citados;
- glosario, guía de notación, mapa del curso y decisiones de estilo del repositorio;
- bibliografía académica citada en el capítulo, incluida la referencia de voz usada en el bloque correspondiente;
- recursos externos registrados en `asset_manifest.csv`.

El manifiesto contiene 46 registros. Todos los assets aprobados con ruta local existen y están organizados; la figura interna `U05-BOOK-001` registra el espectrograma de U05-048.

## Decisiones pedagógicas

- Se hizo visible una ruta central de 77 slides para evitar usar 150 slides como secuencia única.
- La intuición precede al formalismo: U05-120 explica el nivel equivalente antes del ejemplo U05-121 y la integral queda en U05-146.
- U05-032 y U05-048 son centrales porque sostienen muestreo y lectura tiempo–frecuencia.
- U05-048 usa un espectrograma sintético documentado y prohíbe explícitamente inferencia clínica.
- U05-023, U05-042, U05-092, U05-110/111 y U05-121 corrigen notación o interpretación.
- U05-126/127/149 forman un caso autosuficiente con datos, unidades, resultados y separación entre señal y sistema.
- La ruta central usa cuerpo mínimo de 20 pt en las formas heredadas que estaban a 18,75 pt.
- Las diferencias justificadas respecto de unidades anteriores —más gráficos, más recapitulaciones y mayor extensión— se conservaron.

## Limitaciones conocidas

1. El exportador conserva texto alternativo en el modelo de trabajo, pero no serializa el atributo OOXML `descr`: la auditoría final encuentra 0/27 imágenes con alt text persistido. Es una observación menor de accesibilidad y debe corregirse si se exige cumplimiento formal.
2. Algunas slides de ampliación o respaldo conservan cuerpos de 18,75 pt para no forzar auto-shrink ni desborde. No deben proyectarse por defecto; la ruta central cumple el mínimo de 20 pt.
3. Las ecuaciones son editables como texto matemático, no como OMML nativo.
4. El PDF de revisión es raster y sirve para control visual; el PPTX es el original editable.
5. No hay audio o video incrustado; las demostraciones auditivas sugeridas quedan como opción docente.

## Recomendaciones para dictar la clase

- Usar la ruta CENTRAL en seis encuentros y seleccionar ampliaciones según diagnóstico del grupo.
- No proyectar B13 de forma lineal; usarlo como consulta, devolución o material de campus.
- Pedir siempre la rutina: objeto, ejes, unidades, condiciones y conclusión permitida.
- Antes de cada cálculo, solicitar una predicción cualitativa y una verificación dimensional.
- En U05-048, limitar la consigna a lectura descriptiva del ejemplo sintético.
- En U05-110/111, repetir que la corrección A depende de la frecuencia y que el caso tonal no se extiende a banda ancha.
- Dar 6–8 minutos de trabajo en U05-126 antes de revelar U05-127; reservar U05-149 para la devolución.
- Usar las recapitulaciones para recuperación activa, no para releer tarjetas.
- Si se dispone de audio confiable, añadir demostraciones breves sin reemplazar las alternativas estáticas.

## Verificación de la definición de terminado

| requisito | estado | evidencia |
|---|---|---|
| `brief.md` | completo | objetivos, alcance y prerrequisitos |
| `storyboard.md` | completo | 150 filas, bloques, ruta y fuentes |
| `slide_text.md` | completo | versión final sincronizada |
| `speaker_notes.md` | completo | versión final; 150 notas en PPTX |
| `asset_manifest.csv` | completo | 46 registros; aprobados presentes |
| scripts | completo | 6 scripts de unidad |
| gráficos | completo | 13 familias aprobadas; 79 archivos |
| diagramas | completo | 14 familias aprobadas; 113 archivos |
| PowerPoint | completo | 150 slides, 16:9, editable, 2 masters y 27 layouts |
| PDF de revisión | completo | 150 páginas |
| render | completo | 150 PNG; revisión total y ampliada de slides modificadas |
| `review.md` | completo | 0 críticos y 0 mayores abiertos |
| revisión de consistencia | completa | aprobada con diferencias intencionales documentadas |
| enlaces | completo | 3/3 verificados |
| numeración | completo | ID y ruta visibles en 150/150 slides |
| pruebas | completo | `slides_test.py`: sin desbordes |

## Dictamen final

La Unidad 5 cumple la definición de terminado. No quedan problemas críticos ni mayores abiertos. Las observaciones menores no afectan la corrección conceptual, la legibilidad de la ruta central, la editabilidad ni el dictado de la clase.
