# Unidad 3 — Revisión integral y corrección del deck v02

**Archivo revisado:** `output/unidad_03_mecanica_ondulatoria_v02.pptx`  
**Archivo de origen:** `output/unidad_03_mecanica_ondulatoria_v01.pptx`  
**Fecha:** 30 de julio de 2026  
**Alcance visual:** 96/96 diapositivas examinadas en PowerPoint, PDF y render PNG a 1600 × 900 px.  
**Resultado:** 0 problemas `critical` y 0 problemas `major` abiertos.

## Dictamen

La versión v02 cubre el programa oficial de la Unidad 3, mantiene correspondencia con el capítulo del libro y presenta una progresión adecuada para estudiantes de primer año. Las fórmulas, unidades, definiciones y ejemplos numéricos revisados son correctos.

La revisión detectó cuatro grupos de problemas mayores en v01: reducción sistémica de la tipografía de los SVG, gráficos de superposición demasiado densos y poco alineados con sus títulos, códigos de producción visibles para el público y una regresión de orden de capas durante la primera reconstrucción. Todos fueron corregidos y verificados en el render final.

La unidad puede pasar a revisión docente con dos limitaciones menores de producción documentadas: los visuales siguen siendo SVG vectoriales —no grupos de formas nativas de PowerPoint— y no se incorporó multimedia porque los recursos del manifiesto no estaban aprobados.

## Fuentes comprobadas

- Programa oficial: `context/programa/Programa de Física Acústica.pdf`, p. 3.
- Libro editable: `context/libro_latex/chapters/03-mecanica-ondulatoria.tex`.
- Libro de referencia: capítulo de Unidad 3, pp. 61–88 del PDF.
- Documentos de producción: `brief.md`, `storyboard.md`, `slide_text.md`, `speaker_notes.md`, manifiestos, planes y reportes de gráficos y diagramas.

## Cobertura del programa

| Contenido obligatorio | Evidencia principal en el deck | Estado |
|---|---|---|
| Movimiento oscilatorio | 8–10, 13–16 | completo |
| Movimiento ondulatorio | 9–16, 48–59 | completo |
| Movimiento armónico simple | 17–38 | completo |
| Tono puro: definición | 39–41 | completo |
| Tono puro representado en un parlante | 42–47 | completo |
| Tono puro: expresión matemática | 29, 40, 45, 55 | completo |
| Frecuencia, `f` | 23–25, 27, 29–30, 40 | completo |
| Período, `T` | 22–25, 27, 53, 56, 59 | completo |
| Amplitud, `A` | 21, 27, 29–30, 40, 45 | completo |
| Fase, `φ` | 26–29, 64–68, 72–75 | completo |
| Longitud de onda, `λ` | 51–59, 63, 66 | completo |

No se identificaron omisiones del alcance oficial. Las ampliaciones —velocidad de partícula frente a propagación, superposición, cancelación activa, frecuencia angular y número de onda— corresponden al desarrollo del libro o están presentadas como material de apoyo.

## Correspondencia con el libro

| Sección del capítulo | Bloque del deck | Evaluación |
|---|---|---|
| Conocimientos previos | 2–6 | recupera sistema, variable, equilibrio, elasticidad y lectura de gráficos |
| De la oscilación local a la onda | 7–16 | conserva la distinción entre movimiento local, perturbación y transporte de energía |
| Movimiento armónico simple | 17–35 | desarrolla fuerza restauradora, parámetros y relaciones entre posición, velocidad y aceleración |
| Qué representa una sinusoide | 28–38 | explicita variable, ejes, unidades, escala y calibración |
| Tono puro: del parlante al medio | 39–47 | conecta señal, cono, aire, presión y contexto audiométrico |
| Onda viajera en espacio y tiempo | 48–63 | distingue cortes temporal y espacial y deriva `c = λf` |
| Fase, superposición e interferencia | 64–78 | avanza desde diferencia de fase hacia suma, cancelación y límites |
| Relación con Fonoaudiología, errores y síntesis | 76–83 | integra oído, voz, producción, propagación, recepción y recapitulación |
| Autoevaluación, soluciones y glosario | 84–96 | ofrece respaldo trigonométrico, fórmulas, soluciones y notación |

No se encontraron contradicciones entre el deck y el capítulo.

## Exactitud científica

- La relación `T = 1/f` y el ejemplo `T = 2 ms → f = 500 Hz` son correctos.
- El MAS se presenta con `m·a = −k_s·x`; el signo se interpreta como dirección hacia el equilibrio y se incluye control dimensional.
- `x(t) = A cos(2πft + φ₀)` define variable, amplitud, frecuencia y fase inicial.
- La onda viajera combina dependencia espacial y temporal y distingue el signo asociado a la convención de propagación.
- `c = λ/T = λf` es dimensionalmente consistente. El ejemplo `f = 1000 Hz`, `λ = 0,34 m` produce `c = 340 m/s`.
- Se diferencia velocidad local `u` de rapidez de propagación `c`.
- En superposición se suman desplazamientos instantáneos con signo; los casos `Δφ = 0`, `π/2` y `π` producen `2A`, `√2 A` y `0` para amplitudes iguales.
- El material de respaldo usa de manera coherente `ω = 2πf`, `ω = √(k_s/m)`, `k_onda = 2π/λ` y `c = ω/k_onda = λf`.
- Se evita la ambigüedad entre la constante elástica `k_s` y el número de onda `k_onda`.
- Los términos oscilación, perturbación, tono puro, amplitud, período, frecuencia, fase, longitud de onda, presión y calibración se emplean de forma consistente.

## Evaluación pedagógica

La secuencia sigue una progresión clara:

`fenómeno local → onda → MAS → lectura de sinusoides → tono puro y parlante → onda viajera → fase → superposición → aplicación`.

Fortalezas:

- recupera prerrequisitos antes del formalismo;
- introduce una distinción conceptual por vez;
- define símbolos y unidades cerca de las fórmulas;
- combina diagramas, gráficos, ejemplos numéricos y preguntas;
- incluye recapitulaciones en 16, 38, 47, 69, 78 y 81–83;
- vuelve sobre errores frecuentes mediante las cuatro afirmaciones iniciales y sus soluciones;
- conecta teoría con parlante, aire, presión, audiometría, oído y voz;
- reserva el formalismo adicional y las soluciones detalladas para 84–96.

La carga cognitiva es alta pero controlada mediante divisores de bloque y recapitulaciones. Las repeticiones de mapas de ruta y pares de gráficos cumplen una función de comparación o avance; no son duplicaciones decorativas.

## Evaluación visual y de diagramas

Se revisaron las 96 diapositivas renderizadas y, con mayor detalle, todos los bloques con gráficos, ecuaciones o conectores.

Resultado final:

- no hay flechas que tapen texto o fórmulas;
- no hay conectores que atraviesen cajas o contenido;
- no hay etiquetas montadas sobre líneas;
- no hay texto que salga de sus cajas;
- no hay objetos fuera del área de la diapositiva;
- no hay auto-shrink activo;
- no hay ecuaciones centrales ilegibles;
- no hay clipping visible;
- la jerarquía entre título, nodo, contenido, caption y fuente es consistente;
- los gráficos 72–75 se leen correctamente dentro de la slide final, no solo como assets aislados.

La corrección de unidades tipográficas deja los diagramas con un mínimo de 20 pt para etiquetas auxiliares y 22 pt para texto principal. Los gráficos usan 18 pt como mínimo para ticks y 20–22 pt para etiquetas sustantivas.

## Diseño y naturalidad

- La estética es académica y consistente con la identidad de la Unidad 1.
- No se detectaron portadas exageradas, frases grandilocuentes, iconos irrelevantes ni imágenes puramente decorativas.
- Los títulos son informativos y naturales.
- Las cajas se emplean como estructura conceptual, no como tarjetas genéricas.
- La alternancia entre divisores, diagramas, ecuaciones, gráficos, ejercicios y recapitulaciones evita una secuencia de slides idénticas.
- Se eliminaron códigos internos y lenguaje de producción que habían quedado visibles en v01.

## Auditoría de producción

| Control | Resultado |
|---|---|
| Apertura y guardado en Microsoft PowerPoint | correcto |
| Formato | 16:9 |
| Slides | 96 |
| Masters / layouts | 2 / 27 |
| Notas del orador | 96/96 |
| Bloques `[Sources]` en notas | 96/96 |
| Visuales con alt text o título | 80/80 |
| Objetos fuera de página | 0 |
| Auto-shrink | 0 |
| Códigos internos visibles | 0 |
| Caracteres corruptos | 0 |
| Enlaces externos | 0; no había recursos aprobados para enlazar |
| Audio / video | 0; se conservaron alternativas estáticas |
| Fuentes | Calibri, Calibri Light y Cambria Math |
| Render final | 96 PNG a 1600 × 900 px |
| PDF de revisión | 96 páginas |
| Peso del PPTX | 10.109.523 bytes, aceptable para 96 slides vectoriales |

## Registro de problemas

| review_id | slide_id | category | severity | finding | evidence | recommended_fix | status | owner |
|---|---|---|---|---|---|---|---|---|
| U03-RV-001 | 2–12, 18–80, 84–95; 80 visuales | diseño / diagramas | major | Los tamaños declarados en puntos se escribían como píxeles CSS en el SVG; PowerPoint mostraba el texto un 25 % más pequeño. | Un texto previsto en 22 pt se renderizaba a 16,5 pt; afectaba nodos, etiquetas y ecuaciones. | Normalizar `px = pt × 96/72`, regenerar todos los SVG y reemplazar los 80 visuales. | corregido en v02 | producción |
| U03-RV-002 | 72–74 | contenido / pedagogía / gráficos | major | Las tres slides reutilizaban un gráfico de cinco casos que no correspondía con el foco específico de cada título. | El render mostraba información de refuerzo, cancelación y desfase parcial simultáneamente en las tres slides. | Usar un gráfico de un solo caso por slide y destacar la resultante correspondiente. | corregido en v02 | contenido y gráficos |
| U03-RV-003 | 75 | pedagogía / carga cognitiva | major | El ejercicio de predicción era demasiado denso y reducía la legibilidad. | Cuatro o cinco casos apilados con ticks, leyendas y anotaciones pequeñas. | Reducir a tres casos canónicos y ocultar la resultante hasta la discusión. | corregido en v02 | contenido y gráficos |
| U03-RV-004 | 3, 13, 61, 82, 88 | naturalidad / producción | major | Quedaban códigos internos y expresiones dirigidas a producción, no al alumnado. | `U03-087`, `U03-MEDIA001`, `U03-MEDIA003`, `U03-003` y `U03-CH003` eran visibles. | Reescribir las consignas y captions en lenguaje académico natural. | corregido en v02 | redacción |
| U03-RV-005 | 2–95 con SVG; primera compilación v02 | diseño / producción | major | En la primera reconstrucción, algunos SVG nuevos quedaron delante de captions y otros textos nativos. | El primer render v02 ocultó parcialmente captions. | Enviar cada visual reemplazado al fondo, reconstruir y revisar las 96 slides. | corregido antes del cierre | producción |
| U03-RV-006 | 13, 25, 87, 96 | diseño | minor | Algunos textos secundarios usan 15–17,25 pt. | Son estado alternativo, énfasis de ejemplo o claves de tabla; el contenido principal permanece en tamaños mayores y es legible en el render. | Elevarlos en una futura revisión si cambia el layout o se proyecta en un aula muy grande. | abierto, no bloqueante | diseño |
| U03-RV-007 | 80 visuales | producción / editabilidad | minor | Los diagramas y gráficos son SVG vectoriales, no grupos de formas nativas de PowerPoint. | Se pueden escalar sin pérdida, pero sus componentes no se editan individualmente dentro del deck. | Conservar SVG, scripts y fuentes reproducibles; convertir solo los diagramas que deban editarse en clase. | abierto, mitigado | producción |
| U03-RV-008 | revisión automatizada | producción / entorno | minor | `slides_test.py` no inicia por falta de `pdf2image`; el runtime de `artifact-tool` tampoco estaba disponible. | La validación estándar no pudo ejecutarse en este entorno. | Mantener la auditoría equivalente: PowerPoint, OOXML, PDF, 96 PNG, hojas de contacto y revisión visual. | mitigado | entorno |
| U03-RV-009 | 9–10, 31–34, 42/47, mapas de ruta | naturalidad | suggestion | Algunos layouts o visuales se repiten en secuencias cercanas. | La repetición introduce una comparación, una pregunta o un cambio de foco. | Conservar mientras mantenga su función pedagógica; evitar agregar nuevas repeticiones sin cambio cognitivo. | aceptado | pedagogía |

## Problemas abiertos

- `critical`: 0.
- `major`: 0.
- `minor`: 2 abiertos y 1 mitigado.
- `suggestion`: 1 aceptada.

Ningún problema abierto afecta la exactitud científica, la cobertura del programa, la legibilidad de diagramas ni la continuidad de la clase.

## Verificación final

- PowerPoint v02 abierto y guardado correctamente.
- PDF v02 exportado con 96 páginas.
- 96 PNG regenerados después de las correcciones.
- Ocho hojas de contacto revisadas de principio a fin.
- Slides 13, 19, 61, 72, 73, 74, 75, 82 y 88 inspeccionadas nuevamente a resolución completa.
- Gráficos 72–75 verificados sin superposición de etiquetas, conectores o captions.
- Texto visible inspeccionado sin códigos internos ni caracteres dañados.

**Conclusión:** la versión v02 queda sin problemas críticos ni mayores abiertos y está lista para revisión docente.
