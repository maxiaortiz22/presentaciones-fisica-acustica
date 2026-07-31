# Unidad 3 — Análisis de fuentes

## Jerarquía aplicada

1. Programa oficial 2025.
2. Libro del curso en LaTeX.
3. Libro del curso en PDF, edición 2026.
4. Arquitectura curricular y matriz de cobertura.
5. Guías locales de estilo, notación y glosario.
6. Bibliografía citada por el capítulo.

No se incorporaron fuentes externas nuevas en esta etapa.

## Disponibilidad y limitaciones

| Fuente solicitada | Estado | Uso |
|---|---|---|
| `AGENTS.md` | Disponible | Flujo, jerarquía de fuentes y criterios pedagógicos. |
| Programa oficial | Disponible | Alcance obligatorio; Unidad 3 en p. 3. |
| `course_map.md` | Disponible | Función, objetivos, carga, continuidad y alertas. |
| `course_dependency_map.md` | Disponible | Prerrequisitos y reutilización futura. |
| `content_coverage_matrix.csv` | Disponible | Cobertura tema por tema y ampliaciones fuera del listado literal. |
| Capítulo LaTeX de U3 | Disponible | Fuente estructural principal; 1.596 líneas. |
| Libro PDF | Disponible | Capítulo U3 en pp. 61–88; 28 páginas. |
| `presentation_style_guide.md` | Disponible | Densidad, legibilidad, función de slide y criterios visuales. |
| `style/notation_guide.md` | Disponible | Referencia transversal definitiva para símbolos, unidades y colisiones. |
| `style/glossary.md` | Disponible | Referencia terminológica transversal; algunas entradas conservan pendientes explícitos. |
| Presentación previa de U3 | No localizada | No hay deck docente de esta unidad para auditar. |
| Guía de ejercicios independiente | No localizada | El capítulo contiene un banco amplio de autoevaluación y soluciones. |

Las versiones definitivas de notación y glosario se incorporaron al actualizar el repositorio con `origin/main`. Sustituyen a los borradores consultados en la primera revisión.

## Alcance obligatorio extraído del programa

Texto del programa oficial 2025, p. 3:

> Movimiento oscilatorio y ondulatorio. Movimiento armónico simple. El tono puro: representación en un parlante, definición y expresión matemática. Concepto de frecuencia (f), periodo (T), amplitud (A), fase (ϕ) y longitud de onda (λ).

Descomposición exhaustiva:

| ID | Tema obligatorio | Acción mínima esperada |
|---|---|---|
| P-U03-01 | Movimiento oscilatorio | Definir, reconocer y diferenciar de propagación. |
| P-U03-02 | Movimiento ondulatorio | Explicar perturbación, medio y avance. |
| P-U03-03 | Movimiento armónico simple | Interpretar el modelo y su expresión. |
| P-U03-04 | Tono puro | Definirlo como modelo sinusoidal ideal. |
| P-U03-05 | Representación en un parlante | Relacionar señal, cono y perturbación del medio. |
| P-U03-06 | Expresión matemática del tono | Identificar variable, amplitud, frecuencia y fase. |
| P-U03-07 | Frecuencia `f` | Definir, medir, leer y calcular. |
| P-U03-08 | Período `T` | Definir, medir, leer y calcular. |
| P-U03-09 | Amplitud `A` | Interpretar como amplitud de una variable definida. |
| P-U03-10 | Fase `ϕ` | Interpretar estado del ciclo y comparación. |
| P-U03-11 | Longitud de onda `λ` | Definir, leer en espacio y calcular. |

## Comparación programa–LaTeX–PDF

| Tema del programa | LaTeX | PDF | Cobertura | Observación |
|---|---|---|---|---|
| Movimiento oscilatorio | 3.3.1 | 62–63 | Completa | Define equilibrio, desplazamiento y límites del concepto. |
| Movimiento ondulatorio | 3.3.2 | 62–64 | Completa | Separa movimiento local, propagación, energía y materia. |
| MAS | 3.4 | 64–68 | Completa y ampliada | Incluye dinámica, parámetros y cinemática. |
| Tono puro | 3.6 | 69–70 | Completa | Distingue modelo ideal de señal real con transitorios. |
| Parlante | 3.4.4 y 3.6 | 68–70 | Completa y ampliada | Incluye ejemplo de cono y cadena de variables. |
| Expresión matemática | 3.4.2, 3.6 y 3.7.1 | 65–71 | Completa y ampliada | Presenta MAS y onda viajera; exige graduar formalismo. |
| Frecuencia | 3.4.2 | 65–66 | Completa | Incluye `f`, `T` y `ω`. |
| Período | 3.4.2 y 3.7.2 | 65–66, 71 | Completa | Se lee temporalmente y se calcula. |
| Amplitud | 3.4.2 y 3.5 | 65–69 | Completa y mejorada | Obliga a nombrar la variable y la unidad. |
| Fase | 3.4.2 y 3.8.1 | 65–66, 73–74 | Completa y ampliada | Distingue fase inicial y diferencia de fase. |
| Longitud de onda | 3.7.2–3.7.4 | 71–73 | Completa | Integra lectura espacial, `k` y `c = λf`. |

No se detectó ningún tema obligatorio ausente.

## Correspondencia LaTeX–PDF

### Verificación estructural

El PDF es una representación compilada del capítulo LaTeX actual:

- el capítulo comienza en la p. 61;
- el glosario concluye en la p. 88;
- la Unidad 4 comienza en la p. 89;
- las secciones 3.1–3.14 aparecen en el mismo orden;
- las seis figuras y la tabla de variables sinusoidales están presentes;
- el banco de ejercicios y sus soluciones conserva todas las categorías;
- las ecuaciones principales mantienen numeración y contenido.

No se observaron diferencias sustantivas de contenido entre LaTeX y PDF.

### Verificación visual

Se renderizaron y revisaron las 28 páginas del capítulo:

- no se detectaron páginas faltantes;
- no se observaron figuras cortadas ni referencias sin resolver;
- las páginas 63–75 concentran los seis visuales conceptuales;
- las páginas 78–87 son densas por el banco de ejercicios y soluciones;
- la composición del libro es adecuada para lectura cercana, pero su escala, densidad y formato vertical no son transferibles directamente al aula.

Se inspeccionaron con detalle:

- p. 71: pareja temporal/espacial, adecuada como concepto pero demasiado pequeña para una slide;
- p. 75: superposición en tres casos, conceptualmente completa pero requiere mayor contraste y revelado por etapas.

## Ampliaciones del libro respecto del programa

| Ampliación | Estado en matriz | Valor curricular | Decisión preliminar |
|---|---|---|---|
| Posición, velocidad y aceleración | Incluida en sección MAS | Profundiza significado mecánico. | Conservar interpretación; graduar ecuaciones. |
| Frecuencia angular `ω` | `out_of_scope` | Compacta la fase temporal. | Introducir como extensión formal, no como objetivo dominante. |
| Número de onda `k` | `out_of_scope` | Hace simétrica la lectura espacial. | Complementario; usar `k_onda` por notación. |
| Lectura temporal y espacial | Ampliación del libro | Esencial para no confundir `T` y `λ`. | Parte central. |
| Velocidad de propagación | Ampliación instrumental | Necesaria para operar con `λ`. | Parte central mediante `c = λf`. |
| Velocidad de partícula | Ampliación preparatoria | Evita un error crítico y prepara U4. | Distinción conceptual central; ecuación complementaria. |
| Ondas longitudinales/transversales | Ampliación explicativa | Da sentido físico a sonido en fluidos. | Parte central breve. |
| Superposición e interferencia | `out_of_scope` | Prepara suma en U4 y Fourier en U5. | Cualitativo central; fórmula complementaria. |
| Cancelación activa | `out_of_scope` | Aplicación atractiva con límites. | Material complementario. |
| Transitorios de un tono real | Ampliación explicativa | Evita presentar el tono ideal como objeto físico ilimitado. | Parte central breve o complementaria. |

La matriz usa `out_of_scope` para marcar lo que no aparece en el listado literal del programa. Esto no obliga a eliminarlo: debe presentarse como ampliación identificada y subordinada al núcleo obligatorio.

## Diferencias, tensiones y resoluciones documentales

1. **Alcance literal frente a arquitectura global.** La matriz marca `ω`, `k` y superposición como fuera del alcance literal, mientras `course_map.md` incorpora esos contenidos en los resultados de aprendizaje de U3. La propuesta es mantenerlos con profundidad graduada.
2. **Símbolo `k`.** El capítulo usa `k` para rigidez y número de onda. La guía transversal resuelve la colisión mediante `k_s` y `k_onda`.
3. **Símbolo `A`.** El programa y el capítulo usan `A` para amplitud; la guía transversal prefiere `A_x` o acento circunflejo cuando puede existir colisión con área.
4. **Valor de `c`.** El capítulo usa `340`, `343` y `344 m/s` como datos en distintos ejercicios. Debe evitarse que parezcan valores universales incompatibles.
5. **Terminología perceptual.** El capítulo usa “altura tonal o pitch” y “sonoridad” correctamente como atributos, pero no corresponde desarrollarlos en U3.
6. **Archivos de estilo solicitados.** La actualización desde `origin/main` incorporó `style/notation_guide.md` y `style/glossary.md`; el faltante quedó resuelto.
7. **Programa: “periodo”.** En la redacción del material se recomienda “período”, de acuerdo con el uso general del repositorio.

## Qué puede pasar casi directamente a diapositivas

“Casi directamente” significa conservar la idea y precisión, no copiar párrafos o páginas.

| Contenido | Fuente | Motivo |
|---|---|---|
| Definición de oscilación | TEX 3.3.1 | Es breve, concreta y distingue equilibrio. |
| Dos escalas de movimiento | TEX 3.3.2 | La oposición movimiento local/propagación es clara. |
| Definiciones de longitudinal y transversal | TEX 3.3.3 | Admiten comparación visual directa. |
| Definiciones de `A`, `f`, `T`, `ω`, `φ₀` | TEX 3.4.2 | Precisas, aunque deben repartirse. |
| Relaciones `T = 1/f` y `ω = 2πf` | TEX 3.4.2 | Correctas y dimensionalmente claras. |
| Lectura de extremos y equilibrio en MAS | TEX 3.4.3 | Tres observaciones de alto valor pedagógico. |
| Tabla “qué representa una sinusoide” | TEX 3.5 | Excelente comparación; requiere dividirse o rediseñarse. |
| Definición de tono puro ideal | TEX 3.6 | Precisa y con límite explícito. |
| Cadena conceptual del parlante | TEX 3.6 | Secuencia de cuatro pasos reutilizable como diagrama. |
| Definiciones temporal/espacial | TEX 3.7.2 | Son el núcleo de la lectura de `T` y `λ`. |
| Relación `c = λf` | TEX 3.7.3 | Fundamental para la unidad y las siguientes. |
| Distinción `u`/`c` | TEX 3.7.5 | Correcta y necesaria. |
| Condiciones de superposición | TEX 3.8.2 | Evitan sumas de variables incompatibles. |
| Lista de errores frecuentes | TEX 3.10 | Puede alimentar preguntas y recapitulaciones. |

## Qué necesita más explicación o transformación

| Contenido | Problema si se transfiere linealmente | Transformación necesaria |
|---|---|---|
| Propósito y 10 resultados del capítulo | Demasiados para una apertura de clase. | Sintetizar en 6–8 objetivos observables y un mapa visual. |
| Onda mecánica y transporte de energía | Puede quedar abstracto. | Fenómeno con marca material, secuencia temporal y pregunta guiada. |
| Límite de la analogía del resorte | Puede confundirse con aire o con movimiento transversal. | Callout explícito sobre qué representa y qué no. |
| `ma = -kx` | Puede convertirse en álgebra sin intuición. | Diagrama de fuerzas y análisis de signo antes de la ecuación. |
| `ω = √(k/m)` | Introduce formalismo adicional. | Mantener como aplicación opcional del modelo masa–resorte. |
| Ecuaciones de `v(t)` y `a(t)` | Exigen derivación o memorización si aparecen de golpe. | Gráfico de cuatro instantes; ecuaciones como apoyo o respaldo. |
| Ejemplo completo del cono | Tiene demasiadas operaciones para una sola slide. | Separar datos, predicción y límite; elegir uno o dos resultados. |
| Tabla de variables sinusoidales | Cinco filas y cuatro columnas son densas para aula. | Convertir en secuencia de comparaciones o varias slides. |
| Tono ideal frente a real | El texto menciona transitorios sin mostrarlos. | Gráfico de senoide ilimitada frente a ráfaga con envolvente. |
| `ξ(x,t)` | Función de dos variables de alta carga. | Construir por etapas: `x` fijo, `t` fijo y recién luego ecuación completa. |
| `k = 2π/λ` y `c = ω/k` | Pueden ocultar la relación básica. | Priorizar `c = λf`; dejar las formas angulares como extensión. |
| Superposición y fórmula de `A_R` | La fórmula puede desplazar las condiciones físicas. | Mostrar primero suma visual y compatibilidad de unidades. |
| Cancelación activa | Ejemplo atractivo propenso a sobregeneralización. | Caso limitado, geometría/posición y mensaje “reducción local, no silencio universal”. |
| Aplicación audiométrica | Riesgo de derivar hacia diagnóstico. | Separar estímulo físico, calibración, procedimiento, respuesta e inferencia. |
| Banco completo de ejercicios | No cabe en el hilo principal. | Seleccionar ejercicios diagnósticos y llevar soluciones a respaldo. |

## Necesidades de recursos

### Más explicación

- por qué una onda puede transportar energía sin transporte neto equivalente de materia;
- por qué una curva no es necesariamente una trayectoria;
- qué significa “fijar `x`” o “fijar `t`”;
- por qué `u` y `c` comparten unidad sin ser la misma magnitud;
- de qué depende la velocidad de propagación;
- qué condiciones hacen válido el MAS;
- qué condiciones hacen válida la cancelación total.

### Más ejemplos

- oscilación amortiguada frente a MAS ideal;
- mismo `f` con distinta fase;
- misma forma sinusoidal para metros, pascales y volts;
- misma onda vista en tiempo y espacio;
- dos frecuencias en el mismo medio y sus longitudes de onda;
- dos señales desfasadas con amplitudes iguales y desiguales;
- tono audiométrico como estímulo calibrado, sin inferencia diagnóstica.

### Gráficos

- MAS en cuatro instantes;
- `x`, `v`, `a` normalizados;
- temporal frente a espacial con ejes y unidades;
- tono ideal frente a ráfaga;
- `λ` para dos frecuencias a `c` fija;
- superposición por fase;
- comparación de órdenes de magnitud de `u` y `c`.

### Diagramas

- movimiento local/propagación;
- longitudinal/transversal;
- cadena señal–parlante–medio;
- mapa de magnitudes temporales y espaciales;
- condiciones de cancelación total.

Los diagramas futuros deberán cumplir la skill `diagram-generation` y el ciclo de aceptación de `AGENTS.md`.

### Imágenes

- fotografía técnica de parlante;
- fotografía propia del resorte marcado;
- captura de medición temporal calibrada.

Las imágenes no son imprescindibles si los gráficos y diagramas propios resuelven mejor la explicación.

### Animaciones

- compresión que avanza con una partícula marcada;
- corte temporal y espacial de una onda;
- construcción de fase;
- suma de sinusoides;
- ráfaga de tono y transitorios.

### Demostraciones

- resorte largo;
- masa–resorte;
- visualizador temporal;
- generador de tonos con nivel controlado.

### Actividades

- predecir qué se mueve en un resorte;
- clasificar ejes;
- estimar `T` y `λ` antes de calcular;
- completar una tabla “magnitud–símbolo–unidad–dominio”;
- corregir distractores del capítulo;
- explicar en pares por qué `u ≠ c`.

## Coherencia con la arquitectura del curso

`course_map.md` y `course_dependency_map.md` coinciden en:

- carga conceptual alta;
- profundidad algebraico-trigonométrica;
- necesidad de distinguir tiempo, espacio y propagación;
- recuperación de seno/coseno, radianes, equilibrio, inercia y resorte;
- preparación de U4 y U5;
- alerta sobre partícula que viaja, `u = c` y “frecuencia alta → mayor `c`”;
- visuales coordinados de MAS, tiempo/espacio, parlante y superposición;
- evidencia mínima: leer `T` y `λ` en gráficos diferentes y calcular `c`.

No se propone modificar los mapas globales en esta etapa.

## Fuentes técnicas citadas por el capítulo

El capítulo cita, entre otras:

- Oxenham para la relación entre frecuencia y pitch;
- Xiang y Blauert para el alcance del tono real;
- Moser para cancelación activa;
- ASHA e ISO 8253-1 para el uso introductorio de tonos audiométricos.

Estas referencias pertenecen al libro y no fueron reemplazadas ni ampliadas. Al redactar slides, deberá conservarse la trazabilidad de cualquier afirmación técnica que dependa de ellas.
