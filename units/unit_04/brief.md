# Unidad 4 — Brief pedagógico

## Identificación

- **Unidad:** 4.
- **Título oficial:** Generalidades sobre el sonido, sus propiedades y magnitudes.
- **Etapa:** estudio de fuentes y brief pedagógico.
- **Estado:** listo para revisión docente antes de construir el storyboard.
- **Público:** estudiantes de primer año de la Licenciatura en Fonoaudiología.
- **Carga conceptual global:** muy alta.
- **Pregunta organizadora:** ¿qué magnitud medimos cuando describimos un sonido y qué podemos inferir —o no— a partir de ese dato?

Este documento no redacta slides, no fija títulos de slides y no establece todavía una secuencia slide por slide.

## Función de la unidad dentro del curso

La Unidad 4 es el núcleo de acústica física del curso. Recibe de las unidades 2 y 3 los modelos de fuerza, energía, elasticidad, oscilación, onda, fase y superposición, y los convierte en magnitudes observables de un campo acústico. Debe permitir pasar de “hay una onda” a preguntas más precisas:

1. qué variable física cambia;
2. cómo se expresa su valor instantáneo, medio, pico o eficaz;
3. cómo se relacionan presión, movimiento local y transferencia de energía;
4. qué significa un nivel en decibeles;
5. cómo cambian las mediciones al sumar señales o variar distancia y dirección;
6. qué condiciones limitan cada modelo.

La unidad prepara directamente el análisis frecuencial y la sonometría de U5, la adaptación de impedancias del oído medio en U6, la separación entre magnitudes físicas y atributos perceptuales en U7, las mediciones clínicas de U8, la propagación real en U9 y los descriptores de ruido en U10.

## Trabajo de comunicación

Al finalizar la unidad, el estudiantado debe poder mirar una ecuación, una gráfica, un esquema de medición o un valor en decibeles y responder:

- qué magnitud se informa;
- cuál es su símbolo y unidad;
- si el valor es instantáneo, pico, promedio, RMS o nivel;
- cuál es la referencia del nivel;
- qué hipótesis relacionan presión, velocidad de partícula e intensidad;
- si las señales se suman como presiones o mediante magnitudes cuadráticas;
- qué geometría y condiciones permiten aplicar una ley de distancia;
- qué afirmaciones perceptuales o clínicas no están justificadas por el dato físico aislado.

## Alcance obligatorio del programa

El programa oficial 2025, p. 3, exige:

> Naturaleza del sonido. Definición física y psicoacústica. Formas de generación del sonido. Elasticidad del medio de propagación. Propiedades de la onda acústica. Velocidad de propagación. Reflexión del sonido e impedancia acústica. Campo acústico. Ondas esféricas y cilíndricas. El tono puro como unidad más simple de sonido, Valor RMS y valor promedio. Tono puro y señales complejas. Presión sonora. El decibel y la presión sonora. Relación con los seres humanos (percepción). Fuentes coherentes y no coherentes. Suma energética. Valores de referencia de uso común (aire y agua) y nomenclatura. Nivel de presión sonora. Nivel de presión sonora en campo libre para fuentes omnidireccionales. Ley del cuadrado inverso. Factor Q, índice y factor de directividad. Cálculo de nivel de presión sonora en función de la distancia.

El núcleo mínimo no puede omitir ninguno de esos temas. El inventario exhaustivo y su correspondencia con el libro se encuentran en `content_inventory.md` y `source_analysis.md`.

## Profundidad prevista

La profundidad adecuada es conceptual, algebraica y cuantitativa básica, con lectura crítica de hipótesis:

- presentar intuición y representación antes de fórmulas;
- definir cada símbolo, unidad, tipo de promedio y referencia;
- resolver cálculos sencillos de RMS, niveles, suma, distancia y directividad;
- distinguir magnitudes lineales de niveles logarítmicos;
- comparar modelos ideales sin presentarlos como descripciones universales;
- interpretar resultados en lenguaje físico;
- separar estímulo, medición, percepción y decisión clínica.

No se requiere cálculo diferencial. Las integrales del libro deben enseñarse como definiciones de promedio temporal; para el cálculo en clase pueden acompañarse con versiones discretas o ejemplos sobre un período. No corresponde derivar la ecuación de onda, formalizar teoría completa de campos complejos, desarrollar psicoacústica, enseñar procedimientos clínicos ni anticipar en detalle normas de sonometría.

## Objetivos de aprendizaje propuestos

Al finalizar la unidad, el estudiante podrá:

1. **Diferenciar** el sonido como fenómeno físico de la sensación sonora y describir la cadena fuente–medio–campo–receptor sin hacer depender la existencia del campo de un oyente.
2. **Explicar** cómo elasticidad e inercia permiten la propagación, relacionar cualitativamente `c`, rigidez y densidad, y distinguir rapidez de propagación de velocidad de partícula.
3. **Distinguir y relacionar** presión acústica, velocidad de partícula, impedancia específica, intensidad, potencia y energía mediante significado, símbolo, unidad y condiciones de uso.
4. **Interpretar y calcular** valores instantáneo, pico, pico a pico, medio y RMS de señales simples, evitando extender la relación sinusoidal a señales complejas.
5. **Calcular e interpretar** niveles de presión sonora con magnitud y referencia explícitas, justificar los factores 10 y 20 y diferenciar dB SPL, dB HL y atributos perceptuales.
6. **Predecir y calcular** la suma de señales coherentes y no correlacionadas, considerando fase, referencia común y naturaleza de las magnitudes sumadas.
7. **Comparar y aplicar** los modelos plano, cilíndrico y esférico; usar la ley del cuadrado inverso y la ecuación de cambio de nivel con distancia dentro de sus condiciones de validez.
8. **Interpretar** el factor de directividad y el índice de directividad como descriptores de redistribución angular, vinculándolos con medición en campo sonoro sin suponer creación de potencia.

## Perfil de entrada y conocimientos previos

### Se espera recuperar

De la Unidad 1:

- magnitud, símbolo, valor y unidad;
- presión, densidad y área;
- razones, potencias de diez y notación científica;
- logaritmo decimal y argumento adimensional;
- proporcionalidad directa, inversa e inversa al cuadrado;
- lectura de ejes y análisis dimensional.

De la Unidad 2:

- fuerza, presión y energía;
- potencia como energía por unidad de tiempo;
- elasticidad, inercia y densidad;
- temperatura y rapidez del sonido en aire;
- conservación de energía.

De la Unidad 3:

- onda mecánica y onda viajera;
- longitudinalidad en fluidos;
- frecuencia, período, amplitud, fase y longitud de onda;
- `c = λf`;
- tono puro ideal y señal sinusoidal;
- superposición;
- diferencia entre velocidad de partícula y rapidez de propagación.

### No se debe asumir dominado

- uso seguro de logaritmos en razones físicas;
- diferencia entre presión estática y presión acústica;
- distinción entre `p(t)`, `p̂`, `p_pp`, `p̄`, `p_rms` y `p_ref`;
- significado de promedio cuadrático;
- relación entre presión y energía bajo impedancia constante;
- diferencia entre intensidad, potencia y sus niveles;
- suma de niveles en dB;
- coherencia frente a no correlación;
- geometría de frentes de onda;
- condiciones de campo libre y campo lejano;
- diferencia entre factor de directividad e índice de directividad;
- diferencia entre dB SPL, dB HL, sonoridad y “volumen”.

### Diagnóstico inicial recomendado

Antes del desarrollo formal conviene comprobar, sin calificación:

1. si el estudiante identifica la unidad de presión, potencia y energía;
2. si distingue `u` de `c` aunque ambas se expresen en `m·s⁻¹`;
3. si explica por qué una senoide centrada en cero puede tener amplitud no nula;
4. si interpreta una razón `10`, `100` o `1000` en escala logarítmica;
5. si recuerda qué se conserva y qué cambia cuando una onda pasa a otro medio;
6. si reconoce que la suma instantánea depende de fase;
7. si puede comparar áreas de esferas de radios `r` y `2r`.

## Conceptos difíciles y nudos pedagógicos

| Nudo | Por qué es difícil | Tratamiento recomendado |
|---|---|---|
| Fenómeno físico frente a percepción | El lenguaje cotidiano usa “sonido” para estímulo y experiencia. | Comparación explícita estímulo–medición–experiencia; limitar la formalización perceptual a U7. |
| Elasticidad, densidad y `c` | La fórmula puede leerse como causalidad simple entre propiedades que cambian conjuntamente. | Modelo de regiones vecinas y lectura de tendencias, con advertencia sobre comparación de materiales. |
| `p`, `u`, `I`, `W_ac` y `E_ac` | Comparten el mismo fenómeno, pero describen variables locales, flujos y totales. | Tabla y diagrama con significado, unidad, localización y operación; ejemplo dimensional. |
| Impedancia y reflexión | `Z = p/u` parece una división universal y `R_p` puede confundirse con reflexión energética. | Introducir onda plana ideal, interfaz y condiciones antes de fórmulas; separar amplitud y energía. |
| Pico, medio y RMS | “Promedio” se usa informalmente para magnitudes diferentes. | Construcción visual cuadrar → promediar → raíz y contraste con media cero. |
| Decibel, 10 y 20 | Se memoriza una receta sin identificar magnitud o referencia. | Empezar por razón adimensional; conectar factor 20 con proporcionalidad cuadrática bajo impedancia comparable. |
| Referencias en aire y agua | El mismo número en dB parece comparable entre medios. | Tabla de medio–magnitud–referencia–nomenclatura y ejercicios de interpretación, no conversión automática. |
| Coherencia y suma energética | La regla “dos fuentes suman 3 dB” compite con el caso coherente de 6 dB. | Mismos dos tonos en casos de fase fija y no correlación; mostrar primero qué cantidades se suman. |
| Geometrías plana/cilíndrica/esférica | La forma del recinto o conducto se confunde con la forma del frente de onda. | Frentes de igual fase, área disponible y ley de decaimiento, con contraejemplo del tubo. |
| Ley del cuadrado inverso | La regla de `−6 dB` se aplica a cualquier entorno y distancia. | Lista visible de condiciones, ejemplo y contraejemplo en sala/campo próximo. |
| Directividad | `Q > 1` se interpreta como creación de energía o ganancia total. | Comparación a igual potencia y distancia; patrón polar y balance angular. |

## Ideas erróneas previsibles

- El sonido requiere un oyente para existir.
- Todo sonido en cualquier medio es exclusivamente longitudinal.
- Una fuente, un medio y un receptor son tres requisitos equivalentes para que exista el campo.
- Mayor densidad implica siempre mayor rapidez del sonido.
- La frecuencia cambia cuando la onda atraviesa una interfaz estacionaria.
- La presión acústica negativa es una presión total negativa.
- La velocidad de partícula `u` es la rapidez del sonido `c`.
- `p/u = ρc` vale en cualquier campo acústico.
- Intensidad, potencia y energía son nombres intercambiables.
- El valor medio de una senoide igual a cero implica ausencia de señal o energía.
- `p_rms = p̂/√2` vale para cualquier señal.
- El decibel mide intensidad o “volumen”.
- Un valor en dB está completo sin magnitud ni referencia.
- `80 dB SPL` equivale a `80 dB HL` o determina una sonoridad única.
- Valores en dB referidos a aire y agua pueden compararse directamente.
- Los niveles en dB se suman aritméticamente.
- Dos fuentes iguales siempre agregan `3 dB`.
- Una onda en un tubo circular es una onda cilíndrica.
- Una cabina absorbente es necesariamente campo libre.
- Duplicar distancia siempre resta exactamente `6 dB`.
- La intensidad “cae 6 dB” en lugar de dividirse por cuatro.
- `Q_dir = 4` significa cuatro veces más potencia total.

## Bloques pedagógicos preliminares y carga cognitiva

La tabla organiza núcleos para estimar carga. No constituye un storyboard.

| Bloque preliminar | Pregunta guía | Contenido dominante | Carga | Medida de alivio |
|---|---|---|---|---|
| 1. Fenómeno, fuente y medio | ¿Qué existe físicamente antes de medir o escuchar? | Naturaleza física/perceptual; generación; fuente–medio–campo–receptor; elasticidad, inercia y `c`. | Alta | Puente breve desde U3, ejemplos concretos de fuentes y demostración/animación de compresión. |
| 2. Magnitudes del campo | ¿Qué magnitud describe cada aspecto del fenómeno? | `p`, `u`, `Z`, reflexión, `I`, `W_ac`, `E_ac`; unidades y condiciones. | Muy alta | Introducir una magnitud por vez, diagrama de relaciones, ejemplo dimensional y recapitulación obligatoria. |
| 3. Valores de señal | ¿Qué número resume una señal variable? | Instantáneo, pico, pico a pico, medio, RMS; tono puro y señales complejas. | Alta | Construcción gráfica del RMS, ejemplo numérico y actividad de clasificación. |
| 4. Niveles y referencias | ¿Qué significa realmente un valor en decibeles? | Razones, `L_p`, `L_I`, `L_W`, factores 10/20, aire/agua, SPL/HL/percepción. | Muy alta | Separar magnitud–referencia–descriptor, mapa de conversiones permitidas y recapitulación obligatoria. |
| 5. Superposición y suma | ¿Qué cambia según la relación temporal entre señales? | Presión instantánea, coherencia, fase, no correlación, suma de niveles y correlación parcial. | Muy alta | Comparación con los mismos datos en dos casos; ejercicio inmediato y correlación parcial como extensión. |
| 6. Geometría, distancia y dirección | ¿Cómo se distribuye la energía en el espacio? | Onda plana, cilíndrica y esférica; campo libre/reverberante/difuso; `1/r`, `1/r²`, distancia, `Q_dir`, `DI`. | Muy alta | Visuales por etapas, condiciones de validez, ejemplo de distancia y recapitulación integradora. |
| 7. Aplicaciones y transferencia | ¿Qué permite interpretar una medición en Fonoaudiología? | Micrófono calibrado, campo sonoro, audiometría, transductores, límites de inferencia. | Media-alta | Casos breves integrados cerca del concepto; cierre con decisión justificada. |

Los bloques 2, 4, 5 y 6 no deberían dictarse de corrido. Se requieren recapitulaciones después de magnitudes, niveles y propagación, tal como indica la arquitectura global. La unidad probablemente necesita más de un encuentro.

## Estrategia didáctica recomendada

- Seguir la progresión fenómeno → magnitud → representación → ecuación → aplicación → límite.
- Mantener separados estímulo físico, sistema de medición, descriptor y experiencia perceptual.
- Introducir símbolos antes de operar y repetir su significado cuando reaparezcan después de un bloque.
- Usar una misma situación de medición para conectar presión, RMS, nivel, suma y distancia, pero no presentar todas las operaciones simultáneamente.
- Hacer visible cuándo cambia la hipótesis: onda plana, campo lejano, campo libre, misma referencia, misma dirección o señales no correlacionadas.
- Intercalar preguntas de predicción y lectura de gráficos antes de cálculos.
- Terminar cada ejercicio numérico con una interpretación y una condición de validez.
- Mantener las aplicaciones de Fonoaudiología cerca del concepto que iluminan.
- Reservar derivaciones extensas, soluciones completas y correlación parcial para material complementario o respaldo si el tiempo de clase es limitado.

## Recursos disponibles

### Figuras propias del capítulo

- `impedancia-reflexion-interfaz.tex`: incidencia, reflexión y transmisión en una interfaz.
- `presion-velocidad-intensidad.tex`: tres curvas normalizadas de una onda plana progresiva.
- `rms-sinusoide.tex`: construcción gráfica del valor eficaz.
- `escala-presion-db-spl.tex`: correspondencia matemática entre presión eficaz y dB SPL en aire.
- `suma-coherente-no-correlacionada.tex`: comparación `+6,02 dB` frente a `+3,01 dB`.
- `propagacion-esferica.tex`: potencia constante sobre esferas de radios `r` y `2r`.
- `directividad-q.tex`: comparación polar entre fuente omnidireccional y direccional.

Las siete figuras son conceptualmente valiosas, pero deberán reconstruirse o adaptarse para tamaño de aula, revelado por etapas y editabilidad. No corresponde copiar páginas del PDF ni usar los diagramas a la escala del libro.

### Recursos demostrativos posibles

- parlante con cono visible o membrana vibrante;
- resorte o modelo de compresiones con marcadores materiales;
- visualización de una señal sinusoidal y cálculo de media/RMS;
- simulador de fase para suma coherente;
- dos fuentes independientes para discutir suma no correlacionada;
- sonómetro o micrófono calibrado para una demostración de distancia, aclarando las limitaciones del recinto;
- patrón polar de un transductor técnico con frecuencia declarada;
- animación comparativa de frentes planos, cilíndricos y esféricos.

Toda demostración sonora requiere control de nivel, duración breve y alternativa visual.

## Aplicaciones profesionales prioritarias

1. **Micrófonos y medición:** qué variable local detecta un micrófono y por qué la calibración importa.
2. **Audiometría en campo sonoro:** efecto de distancia, dirección, campo y referencia sin convertir automáticamente SPL a HL.
3. **Oído medio:** impedancia y reflexión como preparación de la adaptación de impedancias en U6.
4. **Transductores y voz:** directividad dependiente de geometría y frecuencia.
5. **Sonometría:** RMS y niveles como base de los descriptores que se formalizarán en U5 y U10.
6. **Percepción:** separación entre frecuencia/pitch y nivel/sonoridad como preparación de U7.

## Extensión probable de la presentación

La extensión no debe fijarse por estética. Con una idea dominante por slide, ejemplos, actividades y recapitulaciones, se estima:

- **parte central para enseñanza:** aproximadamente 82–100 slides;
- **material complementario:** aproximadamente 14–22 slides;
- **respaldo con derivaciones, ejercicios adicionales, soluciones y glosario:** aproximadamente 20–32 slides;
- **paquete total probable si se conserva todo:** aproximadamente 116–154 slides.

La ruta central validada requiere cuatro encuentros de aproximadamente 75–100 minutos: B00–B03, B04–B06, B07–B08 y B09–B11. Las slides complementarias y de respaldo no deben incorporarse automáticamente; se usan según dudas, tiempo y objetivos del grupo. Si se dispone de menos encuentros, habrá que definir una ruta de corte explícita; no se recomienda acelerar fórmulas, eliminar ejemplos críticos ni omitir condiciones de validez.

## Clasificación preliminar del contenido

### Parte central

- alcance literal del programa;
- fenómeno físico frente a sensación sonora;
- fuentes, medio, campo y receptor;
- elasticidad, inercia y velocidad de propagación;
- presión acústica y velocidad de partícula;
- impedancia y reflexión en nivel conceptual, con fórmula graduada;
- intensidad, potencia y energía como distinciones necesarias;
- valores instantáneo, pico, pico a pico, medio y RMS;
- tono puro frente a señal compleja;
- decibel, `L_p`, referencia y diferencia 10/20;
- referencias de presión en aire y agua;
- límites entre SPL, HL y sonoridad;
- fuentes coherentes/no correlacionadas y suma de niveles;
- ondas plana, cilíndrica y esférica;
- campo libre y condiciones de validez;
- ley del cuadrado inverso y nivel con distancia;
- `Q_dir` y `DI`;
- errores frecuentes, aplicaciones y recapitulaciones.

### Material complementario

- deducción detallada de `c = √(K_s/ρ)`;
- coeficientes de reflexión de presión e intensidad con más casos;
- intensidad instantánea con signo y promedio integral;
- niveles de intensidad y potencia con ejercicios propios;
- correlación parcial mediante `γ`;
- campo reverberante y campo difuso con mayor profundidad;
- derivación algebraica completa de las leyes de distancia;
- ejemplos técnicos de directividad dependiente de frecuencia;
- ejercicios autónomos seleccionados.

### Slides de respaldo

- demostraciones algebraicas e integrales completas;
- análisis dimensional detallado;
- banco completo de ejercicios y soluciones;
- variantes numéricas;
- tabla extensa de referencias y nomenclaturas;
- glosario de la unidad;
- referencias normativas y bibliográficas;
- respuestas a preguntas sobre campos próximos, estacionarios, reverberantes y coeficientes de transmisión;
- comparación ampliada entre dB SPL, dB HL, dB SL y ponderaciones.

## Relación con otras unidades

| Unidad | Relación |
|---|---|
| U1 | Recupera presión, densidad, unidades, razones, potencias, logaritmos y proporcionalidad. |
| U2 | Recupera fuerza, energía, potencia, elasticidad, inercia y temperatura. |
| U3 | Recibe onda, frecuencia, fase, superposición, `u`, `c` y `c = λf`. |
| U5 | Entrega `p(t)`, `p_rms`, señales complejas y niveles para Fourier, bandas, ponderaciones y sonometría. |
| U6 | Entrega presión, fuerza, impedancia y transferencia de energía para oído externo y medio. |
| U7 | Entrega nivel físico y campo libre para separar estímulo de sonoridad, pitch y umbral. |
| U8 | Prepara dB SPL/dB HL, calibración y condiciones de campo en estudios auditivos. |
| U9 | Entrega reflexión, geometría, campo y ley de distancia para propagación real, recintos y cabinas. |
| U10 | Entrega promedios, RMS, niveles y suma energética para caracterización y exposición a ruido. |

## Criterio de cierre de la unidad

La evidencia mínima será que el estudiante pueda:

1. clasificar `p`, `u`, `I`, `W_ac` y `E_ac` por significado y unidad;
2. explicar cuándo `p/u = ρc` es una relación válida y cuándo no;
3. calcular media y RMS de un caso simple y justificar su diferencia;
4. interpretar un valor en dB indicando magnitud y referencia;
5. decidir si corresponde una suma coherente o no correlacionada;
6. aplicar una ley de distancia y enumerar sus condiciones;
7. diferenciar `Q_dir` de `DI` y explicar por qué no crean potencia;
8. rechazar una inferencia automática desde dB SPL hacia sonoridad o dB HL.

## Fuentes consultadas

- `AGENTS.md`.
- `context/programa/Programa de Física Acústica.pdf`, programa 2025, p. 3.
- `course_map.md`.
- `course_dependency_map.md`.
- `content_coverage_matrix.csv`.
- `context/libro_latex/main.tex`.
- `context/libro_latex/chapters/04-sonido-propiedades-magnitudes.tex`.
- capítulos 2, 3, 5, 6, 7, 9 y 10 mediante las dependencias explícitas del libro y del mapa del curso.
- `context/libro_pdf/Física Acústica para Fonoaudiología.pdf`, pp. 89–117.
- `style/presentation_style_guide.md`.
- `style/notation_guide.md`.
- `style/glossary.md`.

No se incorporaron fuentes externas nuevas en esta etapa.
