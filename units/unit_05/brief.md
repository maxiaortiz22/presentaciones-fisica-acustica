# Unidad 5 — Brief pedagógico

## Identificación

- **Unidad:** 5.
- **Título oficial:** Análisis frecuencial de señales acústicas.
- **Etapa:** cierre y versión final.
- **Estado:** aprobado; alineado con storyboard, deck, notas y revisiones finales.
- **Público:** estudiantes de primer año de la Licenciatura en Fonoaudiología.
- **Carga conceptual global:** muy alta.
- **Pregunta organizadora:** ¿qué objeto representa cada gráfico frecuencial y qué podemos inferir —o no— de sus ejes, su escala y sus condiciones de análisis?

Este documento conserva el alcance pedagógico de origen; la secuencia final y las rutas de uso se documentan en `storyboard.md`.

## Función de la unidad dentro del curso

La Unidad 5 transforma las señales complejas y los niveles estudiados en U4 en representaciones que permiten describir contenido frecuencial, comparar entrada y salida de sistemas, agrupar energía en bandas e interpretar mediciones sonométricas. Es una unidad bisagra entre acústica física, procesamiento introductorio de señales y aplicaciones en voz, audición y medición.

Debe permitir pasar de “esta señal cambia en el tiempo” a preguntas más precisas:

1. qué variable y qué registro se analizan;
2. si el gráfico representa una señal, un sistema o una medición procesada;
3. qué significan magnitud, fase, frecuencia, bin y banda;
4. cómo se relacionan periodicidad, fundamental, armónicos y parciales;
5. qué condiciones determinan resolución y fuga en un registro finito;
6. cómo un filtro o una ponderación modifica una señal o un resultado;
7. qué información mínima debe acompañar una medición de un sonómetro;
8. qué inferencias perceptuales o clínicas no están justificadas por el análisis aislado.

La unidad prepara la respuesta frecuencial y la tonotopía de U6, el timbre, el pitch, los filtros auditivos y el enmascaramiento de U7, la interpretación de estudios y dispositivos de U8, el análisis por bandas en U9 y la caracterización temporal y espectral del ruido en U10.

## Trabajo de comunicación

Al finalizar la unidad, el estudiantado debe poder observar una forma temporal, un espectro, un espectrograma, una respuesta en frecuencia o una lectura sonométrica y responder:

- qué entidad se representa;
- cuál es la variable de cada eje y su unidad;
- si la ordenada expresa amplitud, magnitud, potencia, densidad o nivel;
- qué condiciones de muestreo, duración, ventana, banda y normalización afectan la lectura;
- si la periodicidad permite definir una frecuencia fundamental;
- si una línea es fundamental, armónico, parcial o sobretono;
- si el gráfico pertenece a una señal o describe la relación entrada–salida de un sistema;
- qué tipo de filtro, ponderación o descriptor temporal se aplicó;
- qué afirmaciones sobre audición, voz o clínica requieren evidencia adicional.

## Alcance obligatorio del programa

El programa oficial 2025, pp. 3–4, exige:

> Forma de representación de señales complejas: series de Fourier y transformada de Fourier. Gráficos de respuesta en frecuencia y espectro. Rangos de frecuencia del sonido: infrasonido, sonido audible y ultrasonido. Rango dinámico vocal e instrumental. Rango dinámico del oído: umbral de dolor. Fundamentales, armónicos, parciales y sobretonos. Armónicos y octavas. División del espectro en bandas. Filtros. Frecuencia límite y central. Ancho de banda. Curvas de ponderación: dBA. Medidor de nivel de presión sonora.

El núcleo mínimo no puede omitir ninguno de esos temas. El inventario exhaustivo y su correspondencia con el libro se encuentran en `content_inventory.md` y `source_analysis.md`.

## Profundidad prevista

La profundidad adecuada es conceptual, gráfica y cuantitativa introductoria, con formalismo graduado:

- presentar primero una señal concreta y dos representaciones de la misma información;
- distinguir el objeto representado antes de interpretar una curva;
- introducir serie y transformada de Fourier como modelos matemáticos, sin exigir derivaciones integrales;
- mostrar por qué magnitud y fase son informaciones diferentes;
- resolver cálculos sencillos de período/fundamental, duración de registro, separación entre bins, respuesta, ganancia, límites de banda, ancho de banda, corrección de un tono y promedio energético;
- diferenciar análisis de una señal, respuesta de un sistema y procesamiento de una medición;
- interpretar límites y rangos como dependientes de condiciones, no como cifras universales;
- separar magnitudes físicas, descriptores metrológicos y atributos perceptuales o clínicos.

No se requiere cálculo complejo operativo, demostración de convergencia de Fourier, derivación de algoritmos FFT, diseño matemático de filtros, procesamiento digital avanzado, evaluación normativa completa de sonómetros ni análisis clínico de voz. Las integrales y exponenciales complejas del libro deben funcionar como formalización compacta y referencia, no como barrera de entrada.

## Objetivos de aprendizaje propuestos

Al finalizar la unidad, el estudiante podrá:

1. **Comparar e interpretar** representaciones temporal, frecuencial y tiempo–frecuencia de una señal, identificando variable, ejes, unidades, escala y condiciones de análisis.
2. **Explicar** la serie y la transformada de Fourier como representaciones matemáticas de una señal, y distinguir transformada, DFT y FFT sin atribuirles creación de componentes físicas.
3. **Relacionar y calcular** período fundamental, frecuencia fundamental, duración observada y separación nominal entre bins, diferenciando resolución frecuencial de precisión de estimación.
4. **Diferenciar** el espectro de una señal de la respuesta en frecuencia de un sistema y calcular una respuesta o ganancia simple a partir de entrada y salida comparables.
5. **Identificar y comparar** frecuencia fundamental, armónico, parcial, sobretono y formante, incluyendo casos de mayor armónico dominante y fundamental ausente sin convertirlos automáticamente en atributos perceptuales.
6. **Clasificar e interpretar** infrasonido, rango audible, ultrasonido y rangos dinámicos vocal, instrumental y auditivo, declarando condiciones y evitando umbrales universales.
7. **Calcular e interpretar** límites, centro y ancho de bandas de octava o tercio de octava, y reconocer respuestas de filtros pasa bajos, pasa altos, pasa banda y elimina banda.
8. **Interpretar** ponderaciones A, C y Z, la cadena funcional de un sonómetro y descriptores como nivel equivalente, máximo y pico, distinguiéndolos de dB HL, sonoridad y diagnóstico.

## Perfil de entrada y conocimientos previos

### Se espera recuperar

De la Unidad 1:

- magnitud, símbolo, valor y unidad;
- funciones, relaciones directas e inversas;
- potencias de diez y notación científica;
- logaritmo decimal y razones adimensionales;
- lectura de ejes lineales y logarítmicos;
- manejo algebraico elemental.

De la Unidad 3:

- senoide, frecuencia, período, amplitud y fase;
- `f = 1/T`;
- superposición;
- señal u onda armónica ideal;
- diferencia entre oscilación local y propagación.

De la Unidad 4:

- presión acústica `p(t)` en pascales;
- valores instantáneo, pico y RMS;
- señal compleja o compuesta;
- nivel de presión sonora y referencia;
- suma de contribuciones cuadráticas y niveles;
- diferencia entre magnitud física, nivel y percepción.

### No se debe asumir dominado

- diferencia entre dominio temporal y dominio frecuencial;
- lectura de un eje espectral y sus posibles unidades;
- interpretación de fase espectral;
- números complejos o exponenciales complejas;
- diferencia entre serie, transformada, DFT y FFT;
- significado de muestreo, ventana, bin, fuga y normalización;
- distinción entre resolución y precisión;
- diferencia entre espectro de señal y respuesta de sistema;
- diferencia entre fundamental, máximo espectral, armónico, parcial, sobretono y formante;
- uso de razones de frecuencia en octavas;
- diferencia entre corte, límite, centro y ancho de banda;
- diferencia entre filtro, ponderación y filtrado audiométrico;
- diferencia entre nivel equivalente, máximo y pico;
- diferencia entre dB(A), dB SPL, dB HL, pitch y sonoridad.

### Diagnóstico inicial recomendado

Antes del desarrollo formal conviene comprobar, sin calificación:

1. si el estudiante obtiene `f` a partir de `T` y reconoce la unidad de ambas magnitudes;
2. si distingue la amplitud de una señal del nivel expresado en decibeles;
3. si reconoce que dos senoides pueden sumarse con fases diferentes;
4. si identifica qué eje muestra tiempo y cuál frecuencia en dos gráficos simples;
5. si puede explicar por qué una señal compleja no es necesariamente ruido;
6. si recuerda que los niveles en dB no se promedian aritméticamente;
7. si puede comparar razones `2:1`, `3:1` y diferencias fijas en hertz;
8. si distingue una propiedad de una señal de una propiedad de un dispositivo.

## Conceptos difíciles y nudos pedagógicos

| Nudo | Por qué es difícil | Tratamiento recomendado |
|---|---|---|
| Tiempo, frecuencia y fase | El espectro suele presentarse como si reemplazara al tiempo y la fase queda oculta. | Usar una misma señal en tres vistas; preguntar qué se conserva y qué información no aparece en la magnitud. |
| Fourier como representación | El lenguaje de “descomponer” puede sugerir piezas físicas preexistentes o un mecanismo del oído. | Mostrar síntesis progresiva y declarar que se cambia de base matemática; separar modelo, medición y mecanismo. |
| Serie, transformada, DFT y FFT | Cuatro términos aparecen juntos y se confunden como sinónimos. | Tabla periódica/aperiódica/registro finito/algoritmo; formalismo en capas. |
| Muestreo, ventana, fuga y resolución | Varias decisiones del análisis modifican simultáneamente la apariencia del espectro. | Un solo registro controlado con cambios de `T_obs` y ventana; actividad de predicción antes del resultado. |
| Bin frente a banda | Ambos ocupan intervalos de frecuencia, pero uno depende del análisis y el otro de límites definidos. | Comparación con límites explícitos y suma energética; no usar “barra” como término técnico. |
| Espectro frente a respuesta | Ambos se dibujan contra frecuencia y pueden tener aspecto similar. | Cadena entrada–sistema–salida y pregunta constante “¿qué objeto se representa?”. |
| Fundamental frente a máximo | El máximo visual domina la lectura y compite con la definición por periodicidad. | Tres casos: segundo armónico mayor, parciales inarmónicos y fundamental ausente. |
| Armónico, parcial, sobretono y formante | Los términos provienen de tradiciones diferentes y se usan de manera laxa en voz y música. | Tabla inclusiva y ejemplo vocal: líneas armónicas frente a envolvente de resonancias. |
| Rangos de frecuencia y dinámicos | Las fronteras `20 Hz`/`20 kHz` y el “umbral de dolor” se memorizan como universales. | Presentar convenciones y variables de contexto; no usar cifras sin población, frecuencia, tarea y descriptor. |
| Octava y ancho de banda | Una octava parece una diferencia fija en hertz. | Eje logarítmico y bandas contiguas; contrastar mismo ancho relativo con distinto ancho absoluto. |
| Filtro ideal frente a real | Los dibujos rectangulares inducen a pensar en cortes abruptos. | Comparación ideal/real, transición y criterio de corte declarados. |
| Ponderación A | Se interpreta como corrección auditiva universal o conversión a dB HL. | Mostrarla como respuesta de medición; comparar propósito con filtro de señal y filtro audiométrico. |
| Nivel equivalente, máximo y pico | “Promedio” y “máximo” se usan sin descriptor temporal. | Misma señal con tres detectores conceptuales y configuración visible. |

## Ideas erróneas previsibles

- Fourier descubre o crea componentes que antes no estaban.
- El oído o la cóclea “hacen una FFT”.
- La representación temporal contiene menos información que el espectro.
- El eje vertical de cualquier FFT es intensidad.
- Un espectro de magnitud permite reconstruir por sí solo la forma temporal.
- Serie de Fourier, transformada de Fourier, DFT y FFT son la misma operación.
- Una FFT es un instrumento o una transformación física diferente.
- Aumentar `N` siempre mejora todo el análisis, sin considerar `f_s`, duración, ventana o estacionariedad.
- Menor `Δf` garantiza una frecuencia exacta.
- Ventanear elimina la fuga sin introducir ningún compromiso.
- Un bin y una banda de octava son equivalentes.
- Un espectro y una respuesta en frecuencia son sinónimos.
- La salida de un sistema permite conocer su respuesta sin conocer la entrada.
- La línea de mayor amplitud siempre es la fundamental.
- El primer sobretono es el primer armónico.
- Todo parcial es armónico.
- Un formante es un armónico intenso.
- La fundamental debe estar físicamente presente como una línea espectral.
- Frecuencia fundamental y pitch son idénticos por definición.
- Por debajo de `20 Hz` nada puede percibirse y por encima de `20 kHz` todo es clínicamente irrelevante.
- Existe un único rango dinámico vocal, instrumental o auditivo.
- El umbral de dolor es una cifra universal y puede usarse como límite superior sin condiciones.
- Una octava siempre contiene la misma cantidad de hertz.
- La frecuencia de corte marca una discontinuidad perfecta en cualquier filtro real.
- Ponderar A convierte dB SPL en audición, sonoridad o dB HL.
- Para una señal de banda ancha se puede sumar una única corrección A a un nivel total.
- El nivel equivalente es el promedio aritmético de lecturas en dB.
- El máximo con respuesta Fast es igual al nivel de pico.
- Una aplicación de teléfono reemplaza una medición sonométrica o la verificación de ruido de fondo para audiometría.

## Bloques pedagógicos preliminares y carga cognitiva

La tabla organiza núcleos para estimar carga. No constituye un storyboard.

| Bloque preliminar | Pregunta guía | Contenido dominante | Carga | Medida de alivio |
|---|---|---|---|---|
| 1. Una señal, varias representaciones | ¿Qué pregunta responde cada representación? | Tiempo, frecuencia, magnitud, fase; periódica, aperiódica y transitoria. | Alta | Una señal común, lectura guiada de ejes y mini tabla “objeto–ejes–unidad”. |
| 2. Herramientas de Fourier | ¿Qué significa representar una señal mediante sinusoides? | Serie, transformada, síntesis progresiva, magnitud y fase. | Muy alta | Intuición y visual antes de ecuaciones; formalismo en capas; recapitulación inmediata. |
| 3. Del registro al análisis digital | ¿Qué cambia cuando observamos una señal finita? | Muestreo, DFT/FFT, `T_obs`, `Δf`, ventana, fuga, espectrograma, bin/banda. | Muy alta | Datos sintéticos controlados, un parámetro por vez y decisión explícita sobre profundidad central. |
| 4. Señal frente a sistema | ¿El gráfico describe el contenido o la transformación? | `X(f)`, `H(f)`, `Y(f)`, magnitud, fase, ganancia, retardo, fuente–filtro en voz. | Muy alta | Diagrama entrada–sistema–salida, cálculo de una frecuencia y recapitulación “qué objeto”. |
| 5. Componentes y rangos | ¿Cómo nombramos componentes y límites sin convertirlos en universales? | Fundamental, armónico, parcial, sobretono, formante; infra/audible/ultra; rangos dinámicos. | Alta | Casos contrastantes, ejemplos de voz y tabla de condiciones de medición. |
| 6. Bandas y filtros | ¿Cómo agrupamos o modificamos regiones del espectro? | Octava, tercio, `f_L`, `f_H`, `f_c`, `B`; tipos de filtro; ideal/real. | Muy alta | Eje logarítmico, ejemplo numérico, audio/visual filtrado y recapitulación. |
| 7. Ponderaciones y sonometría | ¿Cómo se convierte una señal de micrófono en un resultado informado? | A/C/Z, filtrado/ponderación/audiometría, cadena del sonómetro, `L_eq`, máximo, pico, verificación. | Muy alta | Cadena funcional por etapas, misma señal con configuraciones distintas y límites de inferencia visibles. |
| 8. Integración profesional | ¿Qué análisis es adecuado para cada pregunta de voz, dispositivo o ambiente? | Casos de Fonoaudiología, selección de herramienta, errores frecuentes y cierre. | Media-alta | Casos breves de decisión, recuperación acumulativa y pregunta integradora. |

Los bloques 2, 3, 4, 6 y 7 no deberían dictarse de corrido. La arquitectura del curso exige bloques cortos y una mini recapitulación “señal/sistema/medición; ejes; unidad; condiciones” al cerrar cada núcleo. La unidad probablemente necesita más de un encuentro.

## Estrategia didáctica recomendada

- Seguir la progresión señal concreta → representación → formalización → lectura → aplicación → límite.
- Mantener visible el objeto representado: señal de entrada, sistema, señal de salida o resultado de medición.
- Introducir vocabulario y símbolos antes de operar con ellos.
- Usar ecuaciones como compactación de una relación ya comprendida, no como punto de partida.
- Separar el eje frecuencial de la magnitud representada en el eje vertical.
- Reutilizar una señal sintética simple para tiempo, espectro, fase, DFT, ventana y filtrado, pero no introducir todas las decisiones a la vez.
- Intercalar ejercicios de lectura y clasificación antes de cálculos.
- Terminar cada cálculo con una interpretación, una unidad y una condición de validez.
- Ubicar aplicaciones de voz, audífonos, audiometría y medición ambiental cerca del concepto que iluminan.
- Mantener los límites entre frecuencia/pitch, nivel/sonoridad y dB SPL/dB HL.
- Reservar derivaciones, normalizaciones de DFT, diseño de filtros y detalle normativo para complemento o respaldo.

## Recursos disponibles

### Figuras propias del capítulo

- `tiempo-magnitud-fase.pdf`: misma presión sintética en tiempo, magnitud y fase.
- `serie-fourier-progresiva.pdf`: onda rectangular aproximada con uno, tres y diez términos impares.
- `compromiso-tiempo-frecuencia.pdf`: espectrogramas con ventanas Hann de `25 ms` y `200 ms`.
- `espectro-respuesta-sistema.tex`: entrada, respuesta del sistema y salida.
- `componentes-espectrales.tex`: serie armónica, parciales inarmónicos y fundamental ausente.
- `bandas-octava-tercio.tex`: octava centrada en `1000 Hz` y tres tercios contiguos.
- `filtros-ideales-reales.pdf`: pasa bajos, pasa altos, pasa banda y elimina banda.
- `cadena-sonometro.tex`: recorrido conceptual desde presión acústica hasta nivel informado.

Las ocho figuras son correctas y pedagógicamente valiosas, pero deberán reconstruirse o adaptarse a formato 16:9, tamaño de aula, revelado por etapas y editabilidad. No corresponde copiar páginas del PDF.

Falta una figura propia de curvas A, C y Z: el LaTeX conserva un `TODO` explícito para generarla desde expresiones normativas y distinguir respuesta nominal de límites de aceptación.

### Recursos demostrativos posibles

- generador de tonos y suma de dos o más componentes;
- visualización sincronizada de forma temporal, espectro de magnitud y fase;
- síntesis progresiva de una onda rectangular;
- registro de una vocal sostenida con espectro y espectrograma, con advertencia no diagnóstica;
- control interactivo de duración y ventana para observar `Δf` y fuga;
- filtrado audible pasa bajos, pasa altos y pasa banda con nivel seguro;
- comparación de una misma señal con ponderaciones A y Z en un sonómetro disponible;
- demostración de nivel equivalente frente a promedio aritmético de dB;
- inspección física de micrófono, calibrador y sonómetro, sin convertir la demostración en certificación metrológica.

Toda demostración sonora requiere control de nivel, duración breve y alternativa visual.

## Aplicaciones profesionales prioritarias

1. **Voz y habla:** periodicidad, armónicos, envolvente, formantes y espectrograma como descriptores, no diagnósticos aislados.
2. **Audífonos y dispositivos:** respuesta en frecuencia como relación entrada–salida, distinta del espectro de la voz.
3. **Audiometría:** filtros de estímulos y ruido de banda, diferenciados de ponderaciones sonométricas y de dB HL.
4. **Medición ambiental y clínica:** configuración de sonómetro, bandas, ponderación e intervalo de medición.
5. **Oído y percepción:** espectro y respuesta como preparación de tonotopía, pitch, timbre, filtros auditivos y enmascaramiento.
6. **Ruido:** bandas, ponderaciones y nivel equivalente como base de U10.

## Extensión probable de la presentación

La extensión no debe fijarse por estética. Con una idea dominante por slide, formalismo graduado, ejemplos, actividades y recapitulaciones, se estima:

- **parte central para enseñanza:** aproximadamente 82–104 slides;
- **material complementario:** aproximadamente 18–30 slides;
- **respaldo con derivaciones, ejercicios, soluciones, normalizaciones y referencias:** aproximadamente 24–38 slides;
- **paquete total probable si se conserva todo:** aproximadamente 124–172 slides.

La parte central probablemente requiera tres o cuatro encuentros de 75–100 minutos, según la profundidad asignada al análisis digital y la sonometría. Las slides complementarias y de respaldo no deben incorporarse automáticamente. Si se dispone de menos tiempo, se debe definir una ruta de corte explícita; no se recomienda comprimir Fourier, señal/sistema, bandas/filtros y ponderación/sonómetro en una única exposición continua.

## Clasificación preliminar del contenido

### Parte central

- alcance literal del programa;
- puente U4: señal compleja, presión, RMS y nivel;
- tiempo, frecuencia, magnitud y fase;
- periodicidad, aperiodicidad y transitorios;
- serie y transformada de Fourier en nivel conceptual y gráfico;
- diferencia entre transformada, DFT y FFT, al menos en forma cualitativa;
- espectro de señal frente a respuesta en frecuencia de sistema;
- fundamental, armónico, parcial, sobretono y fundamental ausente;
- formante como resonancia/envolvente, con alcance introductorio;
- infrasonido, rango audible y ultrasonido con fronteras aproximadas;
- concepto de rango dinámico y condiciones para vocal, instrumento y audición;
- octavas, tercios, límites, centro y ancho de banda;
- filtros pasa bajos, pasa altos, pasa banda y elimina banda; ideal frente a real;
- diferencia entre filtrado, ponderación y filtrado audiométrico;
- ponderación A y nomenclatura `dB(A)`/descriptores `L_A...`;
- cadena funcional del sonómetro y requisitos mínimos de información;
- errores frecuentes, aplicaciones y recapitulaciones.

La inclusión central de `T_obs`, `Δf`, ventanas, fuga, espectrograma, C/Z y `L_eq` debe modularse con una ruta mínima y una ruta ampliada; son extensiones del libro muy útiles para interpretar análisis reales y evitar errores.

### Material complementario

- forma trigonométrica completa de la serie y cálculo de coeficientes;
- transformada compleja, unidades y espectro de fase con mayor formalidad;
- muestreo, DFT, normalización, ventana Hann y fuga con ejemplos adicionales;
- resolución temporal/frecuencial y espectrogramas comparativos;
- nivel por bin y suma de niveles por banda;
- fase de `H(f)` y retardo puro;
- respuesta fuente–filtro de voz y lectura introductoria de formantes;
- ponderaciones C y Z con comparación detallada;
- `L_eq`, ponderaciones temporales, máximo y pico;
- verificación de instrumento y ruido de fondo audiométrico en nivel conceptual;
- ejercicios autónomos seleccionados.

### Slides de respaldo

- derivación y convergencia de series de Fourier;
- coeficientes `a_n` y `b_n` e integrales completas;
- convención y unidades de transformada;
- detalles de DFT, FFT, simetría, escala unilateral y normalización;
- ejemplos adicionales de ventanas y fuga;
- diseño y orden de filtros;
- curvas nominales A/C/Z y referencias normativas, una vez verificadas;
- fórmulas completas de `L_Xeq,T`, máximo y pico;
- banco completo de ejercicios y soluciones;
- variantes numéricas y pregunta integradora;
- glosario de la unidad;
- referencias técnicas y normativas;
- respuestas a preguntas sobre fundamental ausente, formantes, pitch, dB HL y aplicaciones de teléfono.

## Relación con otras unidades

| Unidad | Relación |
|---|---|
| U1 | Recupera funciones, logaritmos, razones, unidades y lectura de gráficos. |
| U3 | Recibe senoides, período, frecuencia, fase y superposición. |
| U4 | Recibe `p(t)`, RMS, señales complejas, niveles y suma energética. |
| U6 | Entrega respuesta en frecuencia y separación señal/sistema para oído externo, medio y cóclea. |
| U7 | Entrega espectro, bandas y filtros para timbre, pitch, filtros auditivos y enmascaramiento. |
| U8 | Prepara interpretación de dispositivos, estímulos, mediciones y diferencias SPL/HL. |
| U9 | Entrega bandas y filtros para propagación, aislamiento, recintos y cabinas. |
| U10 | Entrega análisis temporal/frecuencial, ponderaciones y `L_eq` para caracterización de ruido. |

## Criterio de cierre de la unidad

La evidencia mínima será que el estudiante pueda:

1. decidir si un gráfico representa una señal, un sistema o una medición procesada;
2. identificar ejes, unidades, escala y condiciones relevantes de un espectro;
3. explicar Fourier como representación y distinguir serie, transformada, DFT y FFT;
4. obtener `f_0` desde la periodicidad y no desde el pico mayor;
5. diferenciar fundamental, armónico, parcial, sobretono y formante;
6. calcular e interpretar límites y ancho de una banda simple;
7. reconocer un tipo de filtro y distinguirlo de una ponderación;
8. interpretar una lectura sonométrica indicando qué información falta y rechazando conversiones automáticas a percepción o dB HL.

## Fuentes consultadas

- `AGENTS.md`.
- `skills/course-architecture/SKILL.md`.
- `skills/unit-storyboard/SKILL.md`, utilizada solo para las fases de brief e inventario.
- `context/programa/Programa de Física Acústica.pdf`, programa 2025, pp. 3–4.
- `course_map.md`.
- `course_dependency_map.md`.
- `content_coverage_matrix.csv`.
- `context/libro_latex/main.tex`.
- `context/libro_latex/chapters/05-analisis-frecuencial.tex`.
- `context/libro_latex/bibliography/references.bib`.
- `context/libro_pdf/Física Acústica para Fonoaudiología.pdf`, pp. 119–149.
- `style/presentation_style_guide.md`.
- `style/notation_guide.md`.
- `style/glossary.md`.

No se incorporaron fuentes externas nuevas en esta etapa.
