# Unidad 3 — Brief pedagógico

## Identificación

- **Unidad:** 3.
- **Título oficial:** Fundamentos de la mecánica ondulatoria.
- **Etapa:** estudio de fuentes y brief pedagógico.
- **Estado:** listo para revisión docente antes de construir el storyboard.
- **Público:** estudiantes de primer año de la Licenciatura en Fonoaudiología.
- **Carga conceptual global:** alta.
- **Pregunta organizadora:** ¿cómo puede una región del medio oscilar localmente mientras una perturbación se propaga hasta otro lugar?

Este documento no redacta slides ni fija todavía una secuencia slide por slide.

## Función de la unidad dentro del curso

La Unidad 3 transforma la base matemática de la Unidad 1 y el modelo mecánico de la Unidad 2 en el lenguaje que utilizarán las unidades acústicas posteriores. Su función principal es separar tres niveles que suelen confundirse:

1. el movimiento local de un cuerpo o de una partícula;
2. la representación sinusoidal de una magnitud;
3. la propagación espacial de una perturbación.

La unidad debe dejar operativas las relaciones entre frecuencia, período, amplitud, fase, longitud de onda y velocidad de propagación, sin convertir el curso en una derivación formal de la ecuación de onda. Es la puerta de entrada a las magnitudes acústicas de la Unidad 4 y al análisis de señales de la Unidad 5.

## Trabajo de comunicación

Al finalizar la unidad, el estudiantado debe poder mirar un fenómeno, una ecuación o una gráfica y responder:

- qué sistema o variable oscila;
- qué magnitud representa cada eje y en qué unidad;
- si la representación describe tiempo, espacio o ambos;
- qué parámetro se puede leer o calcular;
- qué se propaga y qué permanece cerca del equilibrio;
- qué conclusión es física y cuál requeriría información perceptual, instrumental o clínica adicional.

## Alcance obligatorio del programa

El programa oficial 2025, p. 3, establece:

> Movimiento oscilatorio y ondulatorio. Movimiento armónico simple. El tono puro: representación en un parlante, definición y expresión matemática. Concepto de frecuencia (f), periodo (T), amplitud (A), fase (ϕ) y longitud de onda (λ).

Por lo tanto, el núcleo mínimo no puede omitir:

1. movimiento oscilatorio;
2. movimiento ondulatorio;
3. movimiento armónico simple;
4. tono puro como modelo ideal;
5. relación entre señal, parlante y perturbación del medio;
6. expresión matemática de una sinusoide;
7. frecuencia;
8. período;
9. amplitud;
10. fase;
11. longitud de onda.

## Profundidad prevista

La profundidad adecuada es algebraico-trigonométrica y de lectura de representaciones:

- interpretar antes de calcular;
- usar seno y coseno sin exigir demostraciones con cálculo diferencial;
- definir cada símbolo y conservar las unidades durante los cálculos;
- leer período en una gráfica temporal y longitud de onda en una representación espacial;
- resolver relaciones directas e inversas sencillas;
- justificar físicamente el signo y los máximos de posición, velocidad y aceleración;
- reconocer las hipótesis de un modelo ideal;
- distinguir magnitudes físicas de atributos perceptuales.

No corresponde exigir:

- derivación de la ecuación diferencial del oscilador o de la ecuación de onda;
- tratamiento vectorial o tridimensional completo;
- impedancia, intensidad, potencia, RMS o niveles en decibeles, que pertenecen a la Unidad 4;
- transformadas o series de Fourier, que pertenecen a la Unidad 5;
- interpretación diagnóstica de respuestas a tonos.

## Objetivos de aprendizaje propuestos

Al finalizar la unidad, el estudiante podrá:

1. **Distinguir** movimiento oscilatorio, movimiento local de partícula y propagación de una perturbación.
2. **Reconocer y representar** un movimiento armónico simple, identificando equilibrio, elongación, amplitud, ciclo y condiciones del modelo ideal.
3. **Relacionar y calcular** frecuencia, período y, cuando corresponda, frecuencia angular, con símbolos y unidades correctos.
4. **Interpretar** amplitud, fase inicial y diferencia de fase en ecuaciones y gráficas sin confundirlas con intensidad, sonoridad o altura tonal.
5. **Comparar** una gráfica temporal y una representación espacial de la misma onda, identificando qué variable permanece fija en cada caso.
6. **Calcular e interpretar** longitud de onda y velocidad de propagación mediante `c = λf`, declarando las condiciones del medio.
7. **Explicar** la cadena conceptual señal eléctrica → movimiento del parlante → movimiento local del medio → propagación, sin equiparar las amplitudes de variables diferentes.
8. **Aplicar** cualitativamente la superposición y la diferencia de fase a casos constructivos, parciales y destructivos, indicando las condiciones necesarias para una cancelación total.

Los objetivos 1–7 cubren y hacen enseñable el alcance obligatorio. El objetivo 8 es una ampliación preparatoria del libro y de la arquitectura global del curso.

## Perfil de entrada y conocimientos previos

### Se espera recuperar

De la Unidad 1:

- magnitud, símbolo, valor y unidad;
- Sistema Internacional y conversiones;
- notación científica y prefijos `m` y `µ`;
- función seno y coseno;
- radianes y ciclo completo;
- lectura básica de ejes;
- proporcionalidad e inversa;
- análisis dimensional.

De la Unidad 2:

- posición de equilibrio;
- inercia;
- fuerza neta;
- fuerza restauradora;
- modelo masa–resorte;
- elasticidad;
- amortiguamiento como pérdida de energía;
- velocidad de propagación dependiente del medio.

### No se debe asumir dominado

- lectura fluida de una sinusoide;
- diferencia entre trayectoria y gráfica;
- uso de fase en radianes;
- distinción entre variable temporal y coordenada espacial;
- interpretación de una función de dos variables `ξ(x,t)`;
- despeje seguro de `T = 1/f` y `λ = c/f`;
- diferencia entre velocidad de partícula y velocidad de propagación;
- diferencia entre frecuencia física y altura tonal;
- condiciones de linealidad y superposición.

### Diagnóstico inicial recomendado

Antes del desarrollo formal conviene comprobar, sin calificación:

1. si el estudiante identifica el equilibrio y el signo del desplazamiento en un sistema masa–resorte;
2. si puede reconocer un ciclo en una gráfica;
3. si convierte `1 ms` a segundos;
4. si interpreta `1 Hz = 1 s⁻¹`;
5. si distingue una curva matemática de la trayectoria del objeto;
6. si anticipa qué sucede con `T` cuando aumenta `f`.

## Conceptos difíciles y nudos pedagógicos

| Nudo | Por qué es difícil | Tratamiento recomendado |
|---|---|---|
| Oscilación frente a propagación | La imagen de una onda suele sugerir que la materia avanza con la curva. | Coordinación entre una marca material y una compresión que se desplaza; demostración con resorte. |
| Curva frente a trayectoria | Una sinusoide se interpreta espontáneamente como la forma geométrica del movimiento. | Nombrar siempre ejes, variable fija y unidad; contrastar trayectoria, registro temporal y fotografía espacial. |
| Tiempo frente a espacio | Dos curvas idénticas pueden tener segundos o metros en el eje horizontal. | Pareja de gráficos con el mismo estado de fase y preguntas de lectura antes de fórmulas. |
| MAS como modelo | “Movimiento repetitivo” se toma como sinónimo de MAS. | Mostrar un contraejemplo amortiguado o no sinusoidal y explicitar las hipótesis. |
| Fase | Es un parámetro abstracto y se confunde con tiempo, demora o amplitud. | Vincular posición dentro del ciclo con el círculo trigonométrico y comparar dos señales. |
| Posición, velocidad y aceleración | Comparten frecuencia, pero sus máximos no coinciden. | Gráfico coordinado y análisis de cuatro instantes del ciclo. |
| `u` frente a `c` | Tienen la misma unidad y ambas se llaman velocidad. | Diagrama con dos flechas semánticamente distintas y un ejemplo de órdenes de magnitud. |
| `c = λf` | Puede leerse erróneamente como causalidad universal entre frecuencia y velocidad. | Fijar el medio y preguntar qué variable se ajusta al cambiar `f`. |
| Tono puro ideal frente a señal real | El modelo omite inicio, fin, transitorios y respuesta del sistema. | Comparar sinusoide ideal ilimitada con una ráfaga de tono con envolvente. |
| Amplitud física frente a percepción | “Más amplitud” se traduce automáticamente como “más volumen”. | Exigir nombre y unidad de la variable; reservar sonoridad y pitch para U7. |

## Ideas erróneas previsibles

- La partícula del medio viaja desde la fuente hasta el receptor.
- La curva sinusoidal es la trayectoria del objeto.
- Toda oscilación es periódica y todo movimiento periódico es MAS.
- Frecuencia y período tienen el mismo valor numérico.
- La frecuencia angular `ω` y la frecuencia `f` son la misma magnitud.
- La amplitud no necesita especificar variable ni unidad.
- La amplitud equivale a intensidad, “volumen” o sonoridad.
- La frecuencia equivale a altura tonal o pitch.
- La separación entre máximos siempre es longitud de onda, aunque el eje sea temporal.
- La velocidad de partícula `u` es la velocidad del sonido `c`.
- Si aumenta la frecuencia, el sonido se propaga más rápido en el mismo medio.
- Un desfase de `π rad` siempre produce cancelación total.
- Dos señales pueden sumarse solo porque sus gráficas tienen la misma forma, aunque representen magnitudes distintas.
- El movimiento del cono en metros se convierte directamente en presión en pascales.
- Una respuesta aislada a un tono permite concluir audición normal o hipoacusia.

## Ampliaciones del libro que conviene conservar

### Ampliaciones instrumentales centrales

Aunque exceden la formulación literal del programa, son necesarias para enseñar sus temas sin ambigüedad:

- posición de equilibrio, elongación y ciclo;
- ondas longitudinales y transversales;
- lectura temporal frente a lectura espacial;
- velocidad de propagación y relación `c = λf`;
- diferencia entre velocidad local de partícula y velocidad de propagación;
- modelo ideal frente a señal producida o medida;
- distinción entre magnitud física y atributo perceptual;
- superposición cualitativa como preparación de U4 y U5.

### Ampliaciones de profundidad graduable

- frecuencia angular `ω`;
- número de onda `k_onda`;
- relación `ω = √(k_s/m)`;
- ecuaciones completas de velocidad y aceleración;
- ecuación viajera `ξ(x,t)`;
- fórmula de amplitud resultante para dos sinusoides;
- alcance de la cancelación activa.

Estas ampliaciones no deben desplazar la lectura conceptual ni transformarse en una lista de fórmulas obligatorias.

## Bloques pedagógicos preliminares y carga cognitiva

La tabla define bloques conceptuales para estimar carga; no constituye un storyboard.

| Bloque preliminar | Pregunta guía | Contenido dominante | Carga | Medida de alivio |
|---|---|---|---|---|
| 1. Puente mecánico | ¿Qué hace volver al sistema al equilibrio? | Masa–resorte, equilibrio, fuerza restauradora, oscilación. | Media | Recuperación breve de U2 y demostración concreta. |
| 2. Movimiento local y propagación | ¿Qué se mueve y qué avanza? | Oscilación, onda, energía, materia, longitudinal/transversal. | Alta | Resorte marcado, dos instantes y recapitulación verbal. |
| 3. MAS y parámetros temporales | ¿Cómo describimos un ciclo ideal? | `A`, `f`, `T`, `φ₀`, `ω`, ecuación sinusoidal. | Alta | Introducir un símbolo por vez; ejemplo numérico corto. |
| 4. Cinemática y significado de la curva | ¿Qué informa cada punto de la sinusoide? | `x`, `v`, `a`; extremos y equilibrio; variable y unidad. | Alta | Gráfico coordinado y actividad de cuatro instantes. |
| 5. Tono puro y parlante | ¿Qué relación existe entre señal, cono y aire? | Modelo ideal, cadena de transducción, variables no intercambiables. | Media | Diagrama de etapas y audio opcional con advertencia de nivel. |
| 6. Onda en tiempo y espacio | ¿Cómo puede la misma onda verse de dos maneras? | `ξ(x,t)`, gráfica temporal, fotografía espacial, `T`, `λ`, `c`. | Muy alta | Dos gráficos alineados, animación por etapas y ejercicio de lectura antes del cálculo. |
| 7. Dos velocidades y fase | ¿Qué velocidad describe cada movimiento y cómo se comparan ciclos? | `u`, `c`, fase inicial y diferencia de fase. | Alta | Flechas diferenciadas, unidades explícitas y mini recapitulación. |
| 8. Superposición, aplicaciones y cierre | ¿Qué ocurre cuando coinciden perturbaciones? | Suma, interferencia, condiciones de cancelación, Fonoaudiología, errores frecuentes. | Alta | Casos 0, `π/2`, `π`; pregunta de transferencia y recapitulación final. |

Los bloques 3, 4, 6 y 7 no deberían impartirse sin pausas de comprobación. El bloque 6 es el punto de máxima carga y merece una recapitulación propia.

## Estrategia didáctica recomendada

- Seguir la progresión fenómeno → representación → formalización → aplicación.
- Introducir cada ecuación después de establecer qué variable describe y qué queda fijo.
- Usar una misma señal de ejemplo para conectar `T`, `f`, `ω`, `λ`, `k_onda` y `c`, pero no presentar todas las relaciones simultáneamente.
- Mantener la convención visual movimiento local/propagación en todos los diagramas.
- Hacer que cada ejercicio numérico termine con una interpretación física.
- Intercalar preguntas de lectura de gráficos antes de problemas algebraicos.
- Explicitar el límite de las analogías con resorte y cuerda.
- Incorporar una mini recapitulación después de MAS y otra después de tiempo/espacio.
- Mantener cerca de cada concepto su aplicación a parlante, registro temporal o tono audiométrico.

## Recursos disponibles

### Figuras propias del capítulo

- `oscilacion-propagacion.tex`: movimiento local frente a avance de una compresión.
- `longitudinal-transversal.tex`: clasificación por dirección.
- `mas-cinematica.tex`: posición, velocidad y aceleración normalizadas.
- `parlante-medio.tex`: señal eléctrica, cono, desplazamiento local y presión.
- `onda-tiempo-espacio.tex`: lectura temporal y fotografía espacial de una misma onda.
- `superposicion-desfase.tex`: suma para diferencias de fase `0`, `π/2` y `π`.

Estas figuras son conceptualmente valiosas, pero deberán rediseñarse para tamaño de aula y editabilidad. No corresponde copiar la página del libro como imagen.

### Recursos demostrativos posibles

- resorte largo con una espira marcada;
- masa–resorte o péndulo de pequeña amplitud;
- video en cámara lenta del cono de un parlante, si existe una fuente técnica verificable;
- animación coordinada de partícula y frente de perturbación;
- reproducción breve de tonos con control de nivel y alternativa visual;
- osciloscopio o visualizador temporal con ejes conocidos.

## Aplicaciones profesionales prioritarias

1. **Generación sonora:** diferenciar señal eléctrica, movimiento del transductor y perturbación del aire.
2. **Registros temporales:** medir período y frecuencia solo cuando los ejes y la calibración están definidos.
3. **Tonos audiométricos:** distinguir frecuencia física, nivel calibrado, procedimiento y respuesta del paciente.
4. **Magnitud frente a percepción:** no equiparar frecuencia con pitch ni amplitud con sonoridad.
5. **Base para dispositivos:** reconocer que fase, superposición y transferencia se reutilizarán en audífonos, mediciones y control activo.

## Extensión probable de la presentación

La extensión no debe fijarse por estética. Con el alcance y los apoyos necesarios se estima:

- **parte central para enseñanza:** aproximadamente 58–70 slides;
- **material complementario:** aproximadamente 8–14 slides;
- **respaldo con derivaciones, ejercicios adicionales y soluciones:** aproximadamente 10–16 slides;
- **paquete total probable si se conserva todo:** aproximadamente 76–100 slides.

La parte central probablemente requiera dos encuentros de 80–100 minutos o tres encuentros más breves, según el tiempo destinado a demostraciones y resolución. Si la unidad debe dictarse en un solo encuentro, será necesario acordar qué ampliaciones pasan a material complementario; no se recomienda comprimir el cuerpo tipográfico ni omitir ejemplos.

## Clasificación preliminar del contenido

### Parte central

- alcance literal del programa;
- puente equilibrio → oscilación;
- movimiento local frente a propagación;
- ondas longitudinales y transversales como apoyo;
- MAS como modelo ideal;
- `A`, `f`, `T`, `φ₀` y relación `T = 1/f`;
- expresión matemática de una sinusoide;
- significado de ejes y unidades;
- tono puro ideal y cadena parlante–medio;
- lectura temporal frente a espacial;
- longitud de onda y `c = λf`;
- distinción conceptual `u` frente a `c`;
- diferencia de fase;
- superposición e interferencia en nivel cualitativo;
- ejemplos breves, errores frecuentes y aplicaciones.

### Material complementario

- frecuencia angular `ω` y número de onda `k_onda` con ejercicios;
- relación `ω = √(k_s/m)`;
- comparación completa de posición, velocidad y aceleración;
- ecuación viajera `ξ(x,t)`;
- cálculo de velocidad máxima de partícula;
- fórmula de amplitud resultante;
- actividad de cancelación activa con límites;
- ejercicios autónomos seleccionados.

### Slides de respaldo

- derivaciones no necesarias para el hilo principal;
- análisis dimensional detallado de las ecuaciones;
- solución completa de ejercicios guiados y autónomos;
- variantes numéricas;
- glosario de la unidad;
- citas técnicas y condiciones de uso de tonos audiométricos;
- comparación más detallada entre modelo ideal, ráfaga de tono y señal medida;
- material para responder preguntas sobre dispersión, ondas en sólidos y cancelación activa.

## Relación con otras unidades

| Unidad | Relación |
|---|---|
| U1 | Recupera seno, coseno, radianes, funciones, unidades y relaciones inversas. |
| U2 | Parte de equilibrio, inercia, fuerza restauradora, elasticidad y masa–resorte. |
| U4 | Entrega onda, fase, superposición, velocidad de partícula y `c = λf` para definir presión, intensidad, impedancia, RMS y niveles. |
| U5 | Entrega sinusoide, frecuencia, fase y superposición para Fourier, espectro y filtros. |
| U6 | Prepara movimiento local, propagación y ondas para oído medio y onda viajera coclear. |
| U7 | Prepara la separación frecuencia/pitch y amplitud/sonoridad. |
| U9 | Entrega longitud de onda para difracción y propagación dependiente del medio. |

## Criterio de cierre de la unidad

La evidencia mínima será que el estudiante pueda:

1. explicar con palabras y un esquema por qué una partícula no viaja con la onda;
2. identificar `A`, `T`, `f` y fase en una sinusoide rotulada;
3. leer `T` y `λ` en dos gráficos diferentes de la misma onda;
4. calcular `f`, `λ` o `c` conservando unidades;
5. diferenciar `u` y `c`;
6. explicar por qué una amplitud de desplazamiento no determina presión ni sonoridad;
7. indicar las condiciones para cancelación total.

## Fuentes consultadas

- `AGENTS.md`.
- `context/programa/Programa de Física Acústica.pdf`, programa 2025, p. 3.
- `course_map.md`.
- `course_dependency_map.md`.
- `content_coverage_matrix.csv`.
- `context/libro_latex/main.tex`.
- `context/libro_latex/chapters/02-mecanica-clasica-termodinamica.tex`.
- `context/libro_latex/chapters/03-mecanica-ondulatoria.tex`.
- `context/libro_latex/chapters/04-sonido-propiedades-magnitudes.tex`.
- capítulos posteriores citados en el mapa de dependencias.
- `context/libro_pdf/Física Acústica para Fonoaudiología.pdf`, pp. 61–88.
- `style/presentation_style_guide.md`.
- `style/notation_guide.md`.
- `style/glossary.md`.
