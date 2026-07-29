# Unidad 1 — Análisis de fuentes

## Jerarquía aplicada

1. Programa oficial 2025.
2. Capítulo LaTeX de la Unidad 1.
3. PDF del libro, edición generada el 27 de julio de 2026.
4. Mapas curriculares y matriz de cobertura.
5. Guías de estilo, notación y glosario.
6. Presentación previa del docente, como antecedente visual y de contenido.

No se incorporaron fuentes externas nuevas en esta etapa.

## Disponibilidad y limitaciones

| Fuente solicitada | Estado | Observación |
|---|---|---|
| Programa oficial | Disponible | `context/programa/Programa de Física Acústica.pdf`, 6 páginas. |
| `course_map.md` | Disponible | Arquitectura curricular inicial del 28/07/2026. |
| `course_dependency_map.md` | Disponible | Dependencias y puntos de control. |
| `content_coverage_matrix.csv` | Disponible | Los 11 temas programáticos de U1 figuran como `covered`. |
| Libro LaTeX | Disponible | Capítulo de 973 líneas, figuras TikZ y bibliografía. |
| Libro PDF | Disponible | 296 páginas; U1 ocupa pp. 13–35 y la p. 36 es separador en blanco. |
| `presentation_style_guide.md` | Disponible | Guía visual vigente. |
| `notation_guide.md` | No existe | Se consultó `style/notation_guide_draft.md`. |
| `glossary.md` | No existe | Se consultó `style/glossary_draft.md`. |
| Presentación anterior | Disponible | Deck docente de 20 slides, sin notas del orador. |

La ausencia de versiones no marcadas como borrador de notación y glosario debe resolverse antes de redactar las slides definitivas.

## Alcance obligatorio: programa frente al libro

| Tema del programa | Cobertura LaTeX | Páginas PDF | Estado | Observación |
|---|---|---:|---|---|
| Qué es la acústica | 1.3–1.4 | 14–15 | Completa | El libro añade fuente–medio–receptor y límites de la inferencia clínica. |
| Aplicaciones en Audiología | 1.4 y 1.11 | 15, 25–26 | Completa | Se amplía a voz, dispositivos, ambientes y medición. |
| Sistema de unidades | 1.6–1.7 | 16–20 | Completa | Incluye SI, fundamentales/derivadas, notación y dimensiones. |
| Velocidad | 1.6.2 y 1.6.4 | 17–18 | Completa | Precisa rapidez, velocidad vectorial y propagación. |
| Distancia | 1.6.2, 1.6.5 y 1.8.1 | 17–20 | Completa | Se usa en propagación y funciones. |
| Masa | 1.6.2–1.6.3 | 17–18 | Completa | Se define mediante inercia. |
| Peso | 1.6.3 | 18 | Completa | Se diferencia explícitamente de masa. |
| Tiempo | 1.6.2 y ejemplos | 17–20 | Completa | Incluye `t` y `Δt`. |
| Presión | 1.6.2, 1.7.2 y 1.10.2 | 17, 19, 25 | Completa | Presión mecánica media; presión acústica se reserva para U4. |
| Densidad | 1.6.2 | 17 | Completa | Incluye relación y unidad. |
| Fuerza | 1.6.2–1.6.3 | 17–18 | Completa | `F=ma` se presenta con condiciones. |
| Función | 1.8.1 | 19–20 | Completa | Incluye variable, dominio y modelo `d(t)=ct`. |
| Función inversa | 1.8.2 | 20–21 | Completa | Incluye diferencia con recíproco. |
| Seno, coseno y tangente | 1.8.3 | 21–22 | Completa | Añade grados, radianes y círculo unitario. |
| Función exponencial | 1.8.4 | 22 | Completa | Incluye crecimiento/decrecimiento y potencias de diez. |
| Logaritmo | 1.8.5 | 22–23 | Completa | Incluye relación inversa y argumento adimensional. |

## Ampliaciones del libro

| Ampliación | Justificación pedagógica | Ubicación sugerida |
|---|---|---|
| Fuente–medio–receptor | Organiza fenómenos y se reutiliza en U9/U10. | Parte central. |
| Sonido como perturbación mecánica | Da sentido al curso antes de formalizar ondas. | Parte central, con alcance acotado. |
| Aceleración y frecuencia | Permiten relacionar magnitudes y preparar U2/U3. | Parte central. |
| Siete unidades fundamentales | Da contexto al SI. | Selección central; tabla completa complementaria. |
| Notación científica y prefijos | Necesarios para magnitudes acústicas. | Parte central. |
| Análisis dimensional | Reduce errores en todas las unidades. | Parte central. |
| Grados, radianes y círculo unitario | Prerrequisito para fase y senoides. | Parte central. |
| Anticipo del decibel | Da propósito al logaritmo. | Parte central, sin formalizar SPL. |
| Físico frente a perceptual | Evita confusiones en U4/U7. | Parte central. |
| Calibración y niveles audiométricos | Conecta con práctica profesional. | Aplicación central breve; detalle en respaldo. |

La matriz de cobertura marca notación científica/análisis dimensional y distinción físico–perceptual como `out_of_scope`. En términos curriculares son ampliaciones respecto del listado literal, pero resultan necesarias como andamiaje. Conviene describirlas como **ampliaciones instrumentales centrales**, no como contenidos prescindibles.

## Correspondencia LaTeX–PDF

### Verificación estructural

- El archivo LaTeX de la Unidad 1 fue modificado el 27/07/2026 a las 18:21.
- El PDF fue generado el mismo día a las 18:41, después de la fuente.
- El índice del PDF reproduce las secciones 1.1 a 1.16 del capítulo.
- La Unidad 1 comienza en la p. 13 y concluye en la p. 35.
- La p. 36 queda en blanco por el inicio del capítulo siguiente en página impar.
- La Unidad 2 comienza en la p. 37.

No se detectaron diferencias de contenido entre la fuente y el PDF actual.

### Verificación visual

Se renderizaron las pp. 13–37. El PDF muestra correctamente:

- ecuaciones y símbolos;
- tablas de magnitudes;
- las cinco figuras TikZ;
- referencias bibliográficas;
- ejercicios y soluciones;
- glosario y cierre.

La composición es correcta para libro, pero no debe transferirse de manera directa a slides:

- las pp. 16–17 concentran tablas y definiciones;
- las pp. 19–24 combinan varias herramientas matemáticas con alta densidad;
- las pp. 27–35 reúnen ejercicios y soluciones en formato de lectura individual;
- el tamaño y la estructura de tablas no son adecuados para aula;
- las figuras son conceptualmente útiles, pero requieren jerarquía, color semántico y revelado progresivo.

## Figuras y tablas del capítulo

| Recurso | PDF | Evaluación para slides |
|---|---:|---|
| Figura 1.1: fuente–medio–receptor | 14 | Puede pasar casi directamente en contenido; reconstruir visualmente. |
| Tabla 1.1: magnitudes fundamentales | 16 | Dividir; no mostrar las siete filas con igual jerarquía en la parte central. |
| Tabla 1.2: magnitudes derivadas | 17 | Convertir en secuencia de relaciones, no en tabla única. |
| Figura 1.2: dependencias dimensionales | 20 | Muy valiosa; necesita construcción progresiva. |
| Figura 1.3: función directa/inversa | 21 | Puede adaptarse directamente con una animación de ida/vuelta. |
| Figura 1.4: círculo trigonométrico | 22 | Reutilizable como SVG o formas editables. |
| Figura 1.5: escala lineal/logarítmica | 24 | Reutilizable; conviene revelar `1, 10, 100, 1000`. |
| Tabla 1.3: físico/perceptual | 24 | Transformar en varias comparaciones; evitar tabla densa. |

## Contenido que puede pasar casi directamente

Con adaptación de redacción y diseño, pueden trasladarse:

- situación inicial de vocalización;
- definición de fuente, medio y receptor;
- definición de acústica;
- definición de magnitud, valor y unidad;
- diferencia masa/peso;
- diferencia entre rapidez y velocidad de propagación;
- ejemplo de tiempo de propagación;
- definición de función e inversa;
- contraejemplo de inversa y recíproco;
- razones trigonométricas;
- equivalencia entre grados y radianes;
- definición de exponencial y logaritmo;
- ejemplo `Q/Q₀=100`;
- pares físico/perceptual;
- ejemplos resueltos;
- errores frecuentes;
- preguntas y ejercicios seleccionados.

“Pasar directamente” significa conservar la idea y los datos, no copiar párrafos o páginas como imagen.

## Contenido que necesita mayor explicación

| Contenido | Problema si se copia | Recurso necesario |
|---|---|---|
| Sonido mecánico | Puede adelantar U3/U4 o reforzar que la materia viaja. | Animación de partículas y pulso. |
| SI | Una lista de unidades favorece memorización sin sentido. | Objetos medibles y clasificación. |
| Fundamental/derivada | La tabla oculta las operaciones. | Diagrama de construcción. |
| Rapidez/velocidad/propagación | Comparten unidades y se confunden. | Comparación con flechas y contexto. |
| Presión | Puede confundirse con presión acústica e intensidad. | Modelo fuerza–superficie y advertencia. |
| Análisis dimensional | Puede parecer un truco algebraico. | Opciones correctas/incorrectas y unidades visibles. |
| Función | Una definición verbal no asegura comprensión. | Tabla–gráfico–ecuación coordinados. |
| Función inversa | Alta confusión con recíproco. | Ida/vuelta y prueba por composición. |
| Radianes | La conversión aislada es memorística. | Círculo y arco. |
| Exponencial/logaritmo | Requiere potencias previas y lectura gráfica. | Pares entrada–salida y reflejo `y=x`. |
| dB | Puede invadir U4 o instalar reglas incompletas. | Escala y un solo caso de tipo potencia. |
| Físico/perceptual | Una tabla puede sugerir correspondencias uno a uno. | Casos y preguntas sobre condiciones. |
| dB HL/SPL | La mención puede parecer una conversión directa. | Cadena de calibración conceptual. |

## Necesidades de recursos

### Más ejemplos

- una medición con unidad correcta e incorrecta;
- dos objetos con igual masa en valores de `g` distintos;
- rapidez escalar frente a velocidad con dirección;
- presión con igual fuerza y áreas distintas;
- densidad con igual masa y volúmenes distintos;
- funciones invertibles y no invertibles en dominios simples;
- ángulos equivalentes;
- factores multiplicativos y logaritmos;
- amplitud digital calibrada frente a no calibrada.

### Gráficos

- magnitud–valor–unidad;
- red de magnitudes;
- función directa e inversa;
- exponencial/logaritmo;
- escala lineal/logarítmica;
- clasificación físico/perceptual.

### Imágenes

- cadena real de voz o parlante, aire y micrófono;
- resorte con espira marcada;
- equipo de medición o estímulo audiométrico, con uso preciso.

### Animaciones o demostraciones

- propagación sin transporte neto de materia;
- construcción de magnitudes derivadas;
- ida/vuelta de funciones;
- barrido del círculo unitario;
- compresión de una escala multiplicativa.

### Actividades

- diagnóstico inicial;
- clasificación fundamental/derivada;
- análisis dimensional por opciones;
- mini cálculo en parejas;
- error frecuente y corrección;
- pregunta integradora final.

## Análisis de la presentación docente previa

### Fortalezas

- conserva identidad UCASAL y tono académico directo;
- cubre el listado básico del programa;
- utiliza ecuaciones editables;
- incluye visuales para función, exponencial/logaritmo y trigonometría;
- presenta magnitudes con ejemplos.

### Limitaciones de alcance

- 20 slides son insuficientes para una clase detallada de 4 horas;
- no declara objetivos ni conocimientos previos;
- no incluye actividades, recapitulaciones o cierre pedagógico;
- no desarrolla notación científica, análisis dimensional ni decibel;
- no trabaja explícitamente físico/perceptual;
- no incluye ejercicios resueltos paso a paso;
- termina con “Muchas gracias” sin síntesis ni puente.

### Formulaciones que deben revisarse

- “masa = cantidad de materia” es menos precisa que la definición por inercia adoptada en el libro;
- la tabla usa grados Celsius como magnitud fundamental, cuando la magnitud es temperatura termodinámica y la unidad SI es kelvin;
- “implantes cocleares: uso de ondas eléctricas” debe reemplazarse por estimulación eléctrica;
- “evaluación auditiva para determinar el estado de la cóclea” es una inferencia demasiado amplia;
- las afirmaciones sobre corrección de pronunciación, timbre, tono y tartamudeo necesitan reformulación y fuentes;
- “diagnóstico” no debe atribuirse a una medición acústica aislada;
- la relación trigonométrica visible en la slide 18 debe revisarse y presentarse con condiciones;
- los gráficos raster y la tabla de prefijos carecen de trazabilidad registrada;
- el meme de la slide 16 no se reutilizará por defecto.

## Coherencia con mapas curriculares

El brief mantiene las decisiones de `course_map.md` y `course_dependency_map.md`:

- carga global alta;
- profundidad operativa;
- prioridad de análisis dimensional;
- diagnóstico de masa/peso, inversa/recíproco y frecuencia/pitch;
- decibel solo como anticipo;
- continuidad hacia U2, U3 y U4;
- punto de control final centrado en magnitud, símbolo, valor, unidad y relación directa/inversa.

## Inconsistencias documentales detectadas

1. `content_coverage_matrix.csv` usa números de sección que no corresponden a la versión actual del capítulo. La cobertura temática es correcta, pero la trazabilidad debe actualizarse.
2. La matriz menciona “cifras significativas” dentro de U01-X1; el capítulo las usa en ejercicios, pero no ofrece un desarrollo conceptual suficiente.
3. La matriz clasifica dos ampliaciones centrales como `out_of_scope`; conviene aclarar que son ampliaciones instrumentales, no material descartable.
4. El capítulo usa área `A`, mientras la guía de notación prefiere `S`.
5. El capítulo y los ejemplos alternan `343 m/s` y `340 m/s` como velocidad didáctica del sonido. Ambos son válidos con hipótesis diferentes, pero la presentación debe elegir una convención y explicar los redondeos.
6. Solo existen versiones `draft` de la guía de notación y del glosario.

## Fuentes técnicas citadas por el capítulo

- BIPM, SI Brochure, 9.ª edición, actualización 2026.
- NIST SP 811, guía de uso del SI.
- Cramer (1993), velocidad del sonido en aire.
- Oxenham (2018), percepción y codificación del sonido.
- ISO 389-1:2017, cero de referencia audiométrico.
- ISO 8253-1:2010, métodos audiométricos.

Estas referencias ya están registradas en `references.bib`. No se requiere buscar nuevas fuentes en esta etapa, salvo que se decida ampliar una aplicación o incorporar datos normativos visibles.

