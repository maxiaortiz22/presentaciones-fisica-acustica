# Unidad 4 — Revisión de redacción

**Resultado:** redacción completa para las 125 slides aprobadas, con texto visible, notas y trazabilidad. No quedan problemas críticos ni mayores. No se produjo ni modificó ningún PowerPoint.

## Cobertura

- Secuencia verificada: `U04-001` a `U04-125`, sin faltantes ni duplicados.
- Slides con gráfico cuantitativo: 11.
- Slides con diagrama, esquema mixto o ecuación anotada: 92.
- Tipos de slide: aplicación=3, cierre=1, comparación=9, definición=11, derivación=1, divisor=11, ecuación=20, ejemplo=8, error frecuente=8, explicación=9, gráfico=6, mapa=1, objetivos=1, portada=1, pregunta=6, proceso=5, profundización=4, puente=1, recapitulación=9, recapitulación final=1, recordatorio=2, referencia=1, solución=6.
- Cada ficha de `slide_text.md` incluye título, subtítulo, contenido visible, ecuaciones, definiciones, ejemplo, caption, visual, layout, fuente, transición y texto alternativo.
- Cada ficha de `speaker_notes.md` incluye duración, propósito, explicación, guía visual, pregunta, respuesta, énfasis/error, multimedia, transición y fuente.

## Revisión por criterios

| criterio | estado | evidencia / decisión |
|---|---|---|
| Fidelidad al storyboard | aprobado | Se conservaron IDs, títulos, bloque, función, mensaje, alcance, layout, fuente y transición. |
| Nivel de primer año | aprobado | La secuencia conserva intuición → definición → ecuación → ejemplo → interpretación. |
| Símbolos y unidades | aprobado | Se aplicó `notation_guide.md`; toda ecuación redactada identifica magnitudes y las notas exigen control de unidades. |
| Ejemplos con pasos | aprobado | Los ejemplos numéricos usan únicamente valores ya presentes en storyboard/libro; U04-105 no recibe datos nuevos. |
| Interpretación física | aprobado | Las notas piden distinguir magnitud, referencia, ventana y dominio de validez. |
| Fonoaudiología | aprobado | Voz, micrófono, sonómetro, SPL/HL y campo sonoro aparecen con límites explícitos. |
| Diagramas | aprobado para escritura | El copy exterior resume la idea central y evita duplicar nodos; las explicaciones extensas quedan en notas. |
| Accesibilidad | aprobado | Todas las slides incluyen texto alternativo; los captions distinguen gráficos, esquemas conceptuales y recursos externos. |
| Tono | aprobado | Español académico claro, sin tono publicitario ni fórmulas retóricas genéricas. |
| PowerPoint | no iniciado | Fuera del alcance solicitado. |

## Hallazgos y pendientes no bloqueantes

| elemento | severidad | tratamiento | estado |
|---|---|---|---|
| U04-105: el storyboard no fija un conjunto numérico para el caso integrador | menor | Se redactó como diagnóstico de datos, decisiones y limitaciones; no se inventaron valores. | resuelto para escritura; validar antes del montaje si se desea cálculo numérico |
| U04-102: patrón polar con datos abiertos | menor | El copy funciona con dos o tres frecuencias, pero no afirma valores. | pendiente de aprobación de `U04-CH-012` |
| Recursos audiovisuales propuestos o preseleccionados | menor | Las notas indican usar alternativa estática mientras no estén aprobados. | pendiente de curaduría/producción |
| Notación visible `W_ac` y `Q_dir` | menor | Se aplicó la guía transversal y se documentó la equivalencia con `W` y `Q` del libro. | pendiente de validación docente global |

## Controles automáticos ejecutados

- Conteo y continuidad de IDs.
- Presencia de todos los campos obligatorios por slide.
- Correspondencia de fuentes con cada fila del storyboard.
- Detección de recursos con estado `proposed`, `shortlisted` o `pending_approval`.
- Confirmación de que los archivos de salida son Markdown y no se generó `.pptx`.

## Recursos visuales todavía no aprobados

- U04-013: `U04-MED-001` — `shortlisted`.
- U04-072: `U04-MED-002` — `proposed`.
- U04-072: `U04-MED-003` — `proposed`.
- U04-073: `U04-MED-002` — `proposed`.
- U04-074: `U04-MED-003` — `proposed`.
- U04-075: `U04-MED-002` — `proposed`.
- U04-075: `U04-MED-003` — `proposed`.
- U04-076: `U04-MED-004` — `proposed`.
- U04-079: `U04-MED-004` — `proposed`.
- U04-095: `U04-MED-005` — `proposed`.
- U04-097: `U04-MED-005` — `proposed`.
- U04-102: `U04-CH-012` — `pending_approval`.
- U04-102: `U04-DATA-001` — `proposed`.
- U04-102: `U04-REF-001` — `proposed`.
