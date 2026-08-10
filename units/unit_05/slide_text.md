# Unidad 5 — Texto visible de las slides

Versión: final · 2026-08-03
Base exclusiva: `storyboard.md` aprobado. Los recursos pendientes se señalan como tales; este documento no autoriza todavía el armado del PowerPoint.

## B00 · Apertura y orientación

### U05-001 — Unidad 5 · Análisis frecuencial de señales acústicas

- **Subtítulo:** De la señal registrada a una interpretación con límites.
- **Contenido visible:** Señal · Sistema · Medición.
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** Una misma escala de frecuencia puede describir objetos diferentes.
- **Visual:** transición mínima entre forma temporal y espectro; sin fórmulas.
- **Layout:** `FA_00_PORTADA`.
- **Fuente:** PO; BR; CM.
- **Texto alternativo:** Forma temporal que se transforma en un espectro y conduce a las palabras señal, sistema y medición.

### U05-002 — Dos señales tienen igual RMS: ¿son iguales?

- **Subtítulo:** Un mismo descriptor global puede ocultar estructuras diferentes.
- **Contenido visible:** Observe ambas señales. ¿Tienen la misma forma? ¿Repiten el mismo patrón? ¿Qué información falta para diferenciarlas?
- **Ecuaciones:** `x_RMS,A = x_RMS,B`.
- **Definición:** RMS resume tamaño eficaz; no describe distribución frecuencial.
- **Ejemplo:** dos señales normalizadas al mismo RMS.
- **Caption:** Igual RMS, distinta evolución temporal.
- **Visual:** `U05-CH-001`.
- **Layout:** `FA_22_VISUAL_COMPLETO`.
- **Fuente:** PREV U04-109; BR; TEX 5.1.
- **Texto alternativo:** Dos gráficos temporales con igual RMS y formas diferentes.

### U05-003 — ¿Qué representa cada gráfico?

- **Subtítulo:** Primero describimos; después interpretamos.
- **Contenido visible:** Para cada visual indique: objeto; ejes; unidades; condiciones. Opciones: forma temporal, espectro, respuesta o espectrograma.
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** La apariencia no identifica por sí sola el objeto representado.
- **Visual:** `U05-DG-002`, versión sin respuestas.
- **Layout:** `FA_14B_MINI_EJERCICIO`.
- **Fuente:** BR; CDM; EP.
- **Texto alternativo:** Cuatro mini gráficos para clasificar mediante una lista de lectura común.

### U05-004 — Lo que recuperamos de U3 y U4

- **Subtítulo:** Dos caminos convergen en la señal compleja.
- **Contenido visible:** U3: frecuencia `f`, período `T`, fase y superposición. U4: presión `p(t)`, RMS, nivel en dB y referencia.
- **Ecuación:** `f=1/T`.
- **Definición:** Superposición: suma de contribuciones compatibles.
- **Ejemplo:** varias senoides pueden formar una única presión compleja.
- **Caption:** Conocimientos previos necesarios para analizar frecuencia.
- **Visual:** `U05-DG-002`, variante puente U3/U4.
- **Layout:** `FA_02B_CONOCIMIENTOS_PREVIOS`.
- **Fuente:** TEX 5.2; BR; NOT.
- **Texto alternativo:** Dos columnas de conceptos previos que convergen en señal compleja.

### U05-005 — Qué podremos interpretar, calcular y explicar

- **Subtítulo:** Ocho resultados observables.
- **Contenido visible:** Interpretar tiempo, frecuencia y fase. Distinguir serie, transformada, DFT y FFT. Calcular `f_0`, `T_obs` y `Δf`. Separar señal y sistema. Nombrar componentes. Interpretar rangos. Calcular bandas y reconocer filtros. Leer ponderaciones y sonometría.
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** Las metas se comprobarán nuevamente al cierre.
- **Visual:** composición tipográfica en cuatro pares.
- **Layout:** `FA_02_OBJETIVOS`.
- **Fuente:** BR objetivos; CM.
- **Texto alternativo:** Ocho objetivos agrupados en cuatro pares temáticos.

### U05-006 — Mapa de la unidad: de la señal a la decisión

- **Subtítulo:** Cuatro tramos, una rutina de lectura.
- **Contenido visible:** 1. Representar. 2. Analizar. 3. Organizar y modificar. 4. Medir y decidir.
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** Cada tramo responde una pregunta distinta sobre señal, sistema o medición.
- **Visual:** `U05-DG-001`.
- **Layout:** `FA_03_MAPA_CLASE`.
- **Fuente:** BR; CM; CDM.
- **Texto alternativo:** Mapa narrativo con cuatro etapas desde representación hasta decisión profesional.

### U05-007 — Cinco preguntas para leer cualquier gráfico

- **Subtítulo:** Una lectura válida empieza antes de mirar la curva.
- **Contenido visible:** ¿Qué objeto? ¿Qué muestran los ejes? ¿Qué unidad y escala? ¿Bajo qué condiciones? ¿Qué permite concluir?
- **Ecuaciones / ejemplo:** —
- **Definición:** Condiciones: decisiones de registro, análisis y medición que limitan la lectura.
- **Caption:** Rutina transversal de lectura.
- **Visual:** `U05-DG-002`.
- **Layout:** `FA_12_PROCESO`.
- **Fuente:** BR; NOT; GLO.
- **Texto alternativo:** Secuencia de cinco preguntas conectadas de izquierda a derecha.

## B01 · Una señal, varias representaciones

### U05-008 — Una señal, varias representaciones

- **Subtítulo:** ¿Qué pregunta responde cada vista?
- **Contenido visible:** Tiempo · Frecuencia · Fase.
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** Las representaciones son complementarias.
- **Visual:** motivo técnico de una señal temporal discreta.
- **Layout:** `FA_01_DIVISOR`.
- **Fuente:** TEX 5.3; PDF p. 120.
- **Texto alternativo:** Señal temporal acompañada por las palabras tiempo, frecuencia y fase.

### U05-009 — El dominio temporal muestra cuándo cambia la señal

- **Subtítulo:** Leemos evolución, duración y transitorios.
- **Contenido visible:** Eje horizontal: tiempo `t` en segundos. Eje vertical: presión `p(t)` en pascales. Preguntas: ¿cuánto dura?, ¿se repite?, ¿dónde cambia rápidamente?
- **Ecuaciones:** —
- **Definición:** Dominio temporal: representación de una magnitud en función del tiempo.
- **Ejemplo:** presión acústica registrada por un micrófono.
- **Caption:** La forma temporal no muestra directamente cómo se distribuyen las frecuencias.
- **Visual:** panel temporal de `U05-CH-002`.
- **Layout:** `FA_08_DEFINICION`.
- **Fuente:** TEX 5.3; NOT.
- **Texto alternativo:** Presión en pascales frente a tiempo en segundos con duración y transitorios señalados.

### U05-010 — El dominio frecuencial organiza contribuciones por frecuencia

- **Subtítulo:** El eje vertical debe nombrarse: no es automáticamente intensidad.
- **Contenido visible:** Eje horizontal: frecuencia `f` en hertz. Ordenadas posibles: amplitud, magnitud, potencia, densidad o nivel. Siempre informar unidad, escala y normalización.
- **Ecuaciones:** —
- **Definición:** Espectro: representación de una señal según frecuencia bajo una convención declarada.
- **Ejemplo:** líneas en 100 y 200 Hz.
- **Caption:** La frecuencia ubica componentes; la ordenada dice cuánto representa cada una.
- **Visual:** `U05-DG-003`, variante espectro anotado.
- **Layout:** `FA_08_DEFINICION`.
- **Fuente:** TEX 5.3; NOT; GLO.
- **Texto alternativo:** Espectro de líneas con eje de frecuencia y distintas etiquetas posibles para la ordenada.

### U05-011 — Una presión, tres lecturas

- **Subtítulo:** Tiempo, magnitud y fase describen la misma señal.
- **Contenido visible:** Temporal: cuándo cambia. Magnitud: cuánto aporta cada frecuencia. Fase: relación temporal dentro del ciclo.
- **Ecuaciones:** `p(t)=p_1(t)+p_2(t)`.
- **Definición:** Fase espectral: ángulo asociado con cada componente, expresado en radianes.
- **Ejemplo:** componentes de 100 y 200 Hz con amplitudes y fases conocidas.
- **Caption:** Misma señal, tres preguntas complementarias.
- **Visual:** `U05-CH-002`.
- **Layout:** `FA_22_VISUAL_COMPLETO`.
- **Fuente:** TEX fig. 5.1; PDF p. 122.
- **Texto alternativo:** Tres paneles coordinados muestran forma temporal, magnitud y fase de una misma presión.

### U05-012 — Leamos el gráfico antes de interpretarlo

- **Subtítulo:** Describir no es todavía explicar una causa.
- **Contenido visible:** Identifique variable, unidades, frecuencias y amplitudes. ¿Qué fase tiene cada componente? ¿Qué conclusión no puede obtenerse solo con estos paneles?
- **Ecuaciones / definiciones:** —
- **Ejemplo:** lectura guiada de `U05-CH-002`.
- **Caption:** Primero ejes y datos; después interpretación.
- **Visual:** `U05-CH-002` con llamadas numeradas.
- **Layout:** `FA_14_PREGUNTA_EJERCICIO`.
- **Fuente:** TEX ejercicios L1.
- **Texto alternativo:** Figura de tres paneles con cinco números que señalan ejes y componentes.

### U05-013 — La fase cambia la forma sin cambiar las magnitudes

- **Subtítulo:** “Cuánto” y “cuándo dentro del ciclo” son informaciones distintas.
- **Contenido visible:** Misma frecuencia y magnitud. Fases diferentes. Formas temporales diferentes.
- **Ecuaciones:** `|X_A(f)|=|X_B(f)|`, pero `φ_A(f)≠φ_B(f)`.
- **Definición:** `|X(f)|` es magnitud; `φ_X(f)` es fase en radianes.
- **Ejemplo:** dos sumas de las mismas componentes con fases modificadas.
- **Caption:** Igual magnitud espectral no implica igual forma temporal.
- **Visual:** `U05-CH-003`.
- **Layout:** `FA_07_GRAFICO_EXPLICACION`.
- **Fuente:** TEX 5.4.3; BR.
- **Texto alternativo:** Dos señales temporales diferentes comparten magnitudes espectrales y muestran fases distintas.

### U05-014 — Igual magnitud espectral no significa igual señal temporal

- **Subtítulo:** Para reconstruir la forma se necesitan magnitud y fase.
- **Contenido visible:** Compare: forma temporal; magnitud común; fase A; fase B. La conclusión solo vale bajo la misma convención de representación.
- **Ecuaciones:** `X(f)=|X(f)|e^{jφ_X(f)}`.
- **Definición / ejemplo:** reconstrucción de las dos señales de U05-013.
- **Caption:** La fase conserva información que la magnitud no muestra.
- **Visual:** `U05-CH-003`, versión comparativa.
- **Layout:** `FA_11_COMPARACION`.
- **Fuente:** TEX 5.4.3; EP.
- **Texto alternativo:** Cuatro paneles comparan dos formas temporales, una magnitud común y dos fases.

### U05-015 — Una señal periódica repite un patrón

- **Subtítulo:** El menor período define la frecuencia fundamental.
- **Contenido visible:** Si existe un menor `T_0>0` que reproduce la señal, la señal es periódica.
- **Ecuaciones:** `x(t+T_0)=x(t)`; `f_0=1/T_0`.
- **Definición:** `T_0`: período fundamental en segundos; `f_0`: frecuencia fundamental en hertz.
- **Ejemplo:** `T_0=0,010 s` → `f_0=100 Hz`.
- **Caption:** Un período completo contiene el patrón que vuelve a repetirse.
- **Visual:** `U05-DG-003`, variante periodicidad.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.3.1, ecs. 5.1–5.2.
- **Texto alternativo:** Señal temporal con un período resaltado y ecuaciones anotadas.

### U05-016 — Periódica, aperiódica y transitoria no son etiquetas excluyentes

- **Subtítulo:** Una vocal puede ser casi periódica en un tramo y transitoria en sus bordes.
- **Contenido visible:** Periódica: repite un patrón. Aperiódica: no presenta repetición exacta. Transitoria: cambia durante un intervalo breve.
- **Ecuaciones:** —
- **Definición / ejemplo:** ataque, tramo estable y final de una vocal sostenida.
- **Caption:** La clasificación depende del tramo y de la escala temporal observada.
- **Visual:** alternativa conceptual; `U05-CH-004` queda pendiente de U05-MED-003.
- **Layout:** `FA_11_COMPARACION`.
- **Fuente:** TEX 5.3.1; GLO.
- **Texto alternativo:** Envolvente conceptual de una vocal dividida en ataque, tramo estable y final.

### U05-017 — Hasta acá: tiempo, frecuencia y fase

- **Subtítulo:** Elegimos la vista según la pregunta.
- **Contenido visible:** Tiempo: ubica cambios. Magnitud: distribuye contribuciones. Fase: organiza relaciones temporales. Pregunta: ¿qué vista elegiría para localizar un transitorio?
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** Tres vistas, un mismo objeto: la señal.
- **Visual:** `U05-DG-014`, recap 1.
- **Layout:** `FA_16_RECAP_PARCIAL`.
- **Fuente:** TEX 5.3; U05-007–016.
- **Texto alternativo:** Mapa de recapitulación con tres representaciones conectadas a una señal común.

## B02 · Herramientas de Fourier

### U05-018 — Fourier: representar una señal con sinusoides

- **Subtítulo:** Cambiamos la forma de describir; no modificamos la señal.
- **Contenido visible:** ¿Cómo puede una suma de componentes simples representar una forma compleja?
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** Fourier es una herramienta matemática de representación.
- **Visual:** `U05-DG-003`, variante suma progresiva.
- **Layout:** `FA_01_DIVISOR`.
- **Fuente:** TEX 5.4; BR.
- **Texto alternativo:** Varias senoides convergen visualmente en una forma compleja.

### U05-019 — ¿Podemos construir una forma compleja sumando tonos?

- **Subtítulo:** Prediga antes de observar el resultado.
- **Contenido visible:** Compare frecuencia, amplitud y fase de tres tonos. Dibuje o describa la suma esperada. ¿Qué parámetro cambiaría más la forma?
- **Ecuación:** `x(t)=x_1(t)+x_2(t)+x_3(t)`.
- **Definición:** Superposición: suma algebraica de señales compatibles.
- **Ejemplo:** tres componentes sintéticas.
- **Caption:** Las componentes se suman en cada instante.
- **Visual:** `U05-CH-005`, estado de tres términos.
- **Layout:** `FA_14_PREGUNTA_EJERCICIO`.
- **Fuente:** U3; TEX 5.4; EP.
- **Texto alternativo:** Tres senoides coordinadas y un espacio reservado para predecir la suma.

### U05-020 — Escuchar componentes y suma

- **Subtítulo:** La escucha ilustra la suma; no demuestra una teoría perceptual.
- **Contenido visible:** Secuencia: tono 1 → tono 2 → tono 3 → suma. Mantener nivel seguro y duración breve. Alternativa: observar las cuatro formas temporales.
- **Ecuaciones / definiciones:** —
- **Ejemplo:** audio propio pendiente de producción.
- **Caption:** Una señal resultante puede representarse mediante varias componentes.
- **Visual:** alternativa estática `U05-CH-005`; audio pendiente.
- **Layout:** `FA_19_MEDIA_AUDIO_VIDEO`.
- **Fuente:** TEX 5.4; EP.
- **Texto alternativo:** Cuatro paneles estáticos muestran tres componentes y su suma.

### U05-021 — Agregar componentes aproxima una forma no sinusoidal

- **Subtítulo:** La escala permanece fija para comparar la aproximación.
- **Contenido visible:** 1 término: estructura básica. 3 términos: bordes más definidos. 5 términos: mayor aproximación y oscilaciones cerca de discontinuidades.
- **Ecuación:** suma parcial de armónicos impares.
- **Definición:** Suma parcial: aproximación obtenida con un número finito de términos.
- **Ejemplo:** onda rectangular.
- **Caption:** Más términos mejoran la aproximación, pero no eliminan las oscilaciones de borde.
- **Visual:** `U05-CH-005`.
- **Layout:** `FA_22_VISUAL_COMPLETO`.
- **Fuente:** TEX fig. 5.2; PDF p. 124.
- **Texto alternativo:** Cuatro paneles muestran una onda rectangular aproximada con cantidades crecientes de armónicos impares.

### U05-022 — La serie ubica componentes en múltiplos de `f_0`

- **Subtítulo:** La ecuación compacta una idea ya observada.
- **Contenido visible:** Término medio + componentes seno y coseno en `n f_0`.
- **Ecuación:** `x(t)=a_0/2+Σ_{n=1}^{∞}[a_n cos(2πnf_0t)+b_n sin(2πnf_0t)]`.
- **Definiciones:** `n`: índice entero; `a_n,b_n`: coeficientes con la unidad de `x`; `f_0` en Hz; `t` en s.
- **Ejemplo:** `n=2` corresponde a `2f_0`.
- **Caption:** La serie organiza una señal periódica en componentes armónicas.
- **Visual:** `U05-DG-003`, ecuación anotada.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.4.1, ec. 5.3.
- **Texto alternativo:** Ecuación central con callouts para media, índice, frecuencia y coeficientes.

### U05-023 — Los coeficientes indican cuánto aporta cada componente

- **Subtítulo:** Se obtienen comparando la señal con seno y coseno durante un período.
- **Contenido visible:** `a_n`: contribución coseno. `b_n`: contribución seno. El intervalo de cálculo es un período fundamental.
- **Ecuaciones:** `a_n=(2/T_0)∫x(t)cos(2πnf_0t)dt`; `b_n=(2/T_0)∫x(t)sin(2πnf_0t)dt`, en `t∈[t_0,t_0+T_0]`.
- **Definiciones:** `t_0`: inicio elegido; `T_0`: duración del período; `dt` en s.
- **Ejemplo:** una simetría puede anular una familia de coeficientes.
- **Caption:** Profundización no evaluable mediante integración.
- **Visual:** `U05-DG-003`, variante dos ecuaciones.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX 5.4.1, ecs. 5.4–5.5.
- **Texto alternativo:** Dos integrales anotadas comparten un período resaltado.

### U05-024 — Dos componentes, un período fundamental

- **Subtítulo:** Buscamos la repetición común, no el pico más alto.
- **Contenido visible:** Datos: `f_1=100 Hz`, `f_2=200 Hz`. Paso 1: períodos `0,010 s` y `0,005 s`. Paso 2: patrón común `T_0=0,010 s`. Paso 3: `f_0=100 Hz`; 200 Hz es el segundo armónico.
- **Ecuaciones:** `T=1/f`; `f_0=1/T_0`.
- **Definición / ejemplo:** ejemplo resuelto del capítulo.
- **Caption:** La fundamental se obtiene de la periodicidad común.
- **Visual:** `U05-DG-003`, variante ejemplo.
- **Layout:** `FA_10_EJEMPLO_RESUELTO`.
- **Fuente:** TEX 5.4.2.
- **Texto alternativo:** Tres pasos de cálculo junto a un espectro con líneas en 100 y 200 Hz.

### U05-025 — ¿Qué mejora al sumar más términos?

- **Subtítulo:** Observe tramos suaves y vecindades de discontinuidades.
- **Contenido visible:** ¿Dónde disminuye el error? ¿Dónde persisten oscilaciones? ¿Cambió la escala? ¿Sería correcto llamarlas ruido?
- **Ecuaciones / definiciones:** —
- **Ejemplo:** comparación de estados de `U05-CH-005`.
- **Caption:** Las oscilaciones de Gibbs pertenecen a la aproximación matemática.
- **Visual:** `U05-CH-005` con tres regiones señaladas.
- **Layout:** `FA_14_PREGUNTA_EJERCICIO`.
- **Fuente:** TEX ejercicio L2.
- **Texto alternativo:** Aproximaciones de Fourier con llamadas en segmentos centrales y bordes.

### U05-026 — La transformada no exige repetición exacta

- **Subtítulo:** Serie y transformada responden a objetos ideales diferentes.
- **Contenido visible:** Señal periódica ideal → serie → líneas en múltiplos de `f_0`. Señal general → transformada → función continua ideal de frecuencia.
- **Ecuaciones:** —
- **Definición:** Transformada de Fourier: representación frecuencial de una señal bajo una convención matemática.
- **Ejemplo:** pulso aislado frente a señal periódica.
- **Caption:** Un registro real requiere distinguir señal ideal, observación finita y cálculo digital.
- **Visual:** `U05-DG-003`, comparación serie/transformada.
- **Layout:** `FA_11_COMPARACION`.
- **Fuente:** TEX 5.4.3.
- **Texto alternativo:** Dos columnas comparan señal periódica con espectro de líneas y señal general con espectro continuo ideal.

### U05-027 — La transformada compara la señal con cada frecuencia

- **Subtítulo:** La fórmula es referencia, no procedimiento de cálculo en esta unidad.
- **Contenido visible:** `X(f)` reúne magnitud y fase para cada frecuencia según una convención.
- **Ecuación:** `X(f)=∫_{−∞}^{∞}x(t)e^{−j2πft}dt`.
- **Definiciones:** `x(t)`: señal; `f` en Hz; `j²=−1`; con esta convención, si `x` tiene unidad `U`, `X` tiene `U·s`.
- **Ejemplo:** presión genérica: usar `x(t)` para no fijar aún `P(f)`.
- **Caption:** La exponencial compleja compacta comparación con seno y coseno.
- **Visual:** `U05-DG-003`, ecuación anotada.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.4.3, ec. 5.6; NOT.
- **Texto alternativo:** Integral de Fourier con cuatro callouts para señal, frecuencia, unidad y número imaginario.

### U05-028 — Una transformada tiene magnitud y fase

- **Subtítulo:** Dos informaciones diferentes conservadas en una expresión.
- **Contenido visible:** Magnitud `|X(f)|`: tamaño de la contribución. Fase `φ_X(f)`: relación angular, en radianes.
- **Ecuación:** `X(f)=|X(f)|e^{jφ_X(f)}`.
- **Definición:** Forma polar de la transformada.
- **Ejemplo:** volver a las componentes de 100 y 200 Hz de U05-011.
- **Caption:** Magnitud y fase deben compartir convención y eje frecuencial.
- **Visual:** `U05-DG-003`, variante polar.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.4.3, ec. 5.7.
- **Texto alternativo:** Ecuación polar conectada a mini gráficos de magnitud y fase.

### U05-029 — Fourier cambia la representación, no la señal

- **Subtítulo:** Elegimos herramienta según el objeto.
- **Contenido visible:** Serie: periodicidad ideal. Transformada: señal general. DFT: registro finito y discreto. FFT: algoritmo que calcula la DFT. Error a evitar: “Fourier crea componentes”.
- **Ecuaciones / ejemplo:** —
- **Definición:** Representar no equivale a producir un mecanismo físico.
- **Caption:** Objeto, herramienta y salida deben nombrarse por separado.
- **Visual:** `U05-DG-014`, recap 2.
- **Layout:** `FA_16_RECAP_PARCIAL`.
- **Fuente:** TEX 5.4; BR.
- **Texto alternativo:** Mapa de cuatro herramientas con su objeto y un error frecuente asociado.

## B03 · Del registro a la DFT

### U05-030 — De la señal continua a un registro digital

- **Subtítulo:** Entre el fenómeno y el gráfico hay decisiones de adquisición.
- **Contenido visible:** Presión acústica → transducción → muestras → análisis.
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** Un registro finito no es la señal física completa.
- **Visual:** `U05-DG-004`, apertura.
- **Layout:** `FA_01_DIVISOR`.
- **Fuente:** TEX 5.4.4; CM.
- **Texto alternativo:** Cadena de cuatro etapas desde presión continua hasta análisis digital.

### U05-031 — El micrófono no entrega una FFT

- **Subtítulo:** Transducción, muestreo y cálculo son operaciones distintas.
- **Contenido visible:** `p(t)` en Pa → señal eléctrica → muestras `x[n]` → DFT y visualización.
- **Ecuaciones:** —
- **Definiciones:** Transducción: conversión entre formas de energía. Muestra: valor registrado en un instante.
- **Ejemplo:** cadena de adquisición de una vocal.
- **Caption:** El software calcula una representación a partir de datos adquiridos.
- **Visual:** `U05-DG-004`, variante de cuatro etapas.
- **Layout:** `FA_12_PROCESO`.
- **Fuente:** TEX 5.4.4 y 5.11; GLO.
- **Texto alternativo:** Cuatro nodos distinguen presión, señal eléctrica, muestras y cálculo digital.

### U05-032 — Muestrear es observar la señal en instantes separados

- **Subtítulo:** La frecuencia de muestreo indica cuántas observaciones se realizan por segundo.
- **Contenido visible:** `f_s`: frecuencia de muestreo en Hz o muestras/s. `T_s`: intervalo entre muestras en s.
- **Ecuación:** `T_s=1/f_s`.
- **Definición:** Muestreo: registro de valores en instantes discretos.
- **Ejemplo:** `f_s=8000 Hz` → `T_s=0,000125 s=125 µs`.
- **Caption:** Los puntos son muestras; la curva continua representa el modelo subyacente.
- **Visual:** `U05-CH-006`, caso seguro.
- **Layout:** `FA_08_DEFINICION`.
- **Fuente:** TEX 5.4.4; NOT; EP.
- **Texto alternativo:** Senoide continua con puntos de muestreo igualmente espaciados.

### U05-033 — `N` muestras a `f_s` determinan la duración observada

- **Subtítulo:** Más muestras alargan el registro solo si `f_s` permanece fija.
- **Contenido visible:** Datos necesarios: cantidad `N` y frecuencia de muestreo `f_s`.
- **Ecuación:** `T_obs=N/f_s`.
- **Definiciones:** `N`: número de muestras, sin unidad. `T_obs`: duración observada, en s.
- **Ejemplo:** `N=2000`, `f_s=8000 Hz` → `T_obs=0,250 s`.
- **Caption:** El cociente entre muestras y muestras por segundo da segundos.
- **Visual:** `U05-DG-004`, ecuación y dos tiras temporales.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.4.4, ec. 5.8.
- **Texto alternativo:** Ecuación anotada junto a registros de distinta cantidad de muestras.

### U05-034 — DFT y FFT no son sinónimos de “espectro”

- **Subtítulo:** Definición, algoritmo y gráfico ocupan niveles diferentes.
- **Contenido visible:** Transformada: modelo continuo. DFT: valores discretos. FFT: algoritmo eficiente. Gráfico: visualización de resultados con una ordenada declarada.
- **Ecuaciones / ejemplo:** —
- **Definición:** FFT no es un instrumento ni una nueva magnitud física.
- **Caption:** Nombrar el proceso evita confundir cálculo y resultado.
- **Visual:** `U05-DG-004`, matriz conceptual.
- **Layout:** `FA_11_COMPARACION`.
- **Fuente:** TEX 5.4.4; GLO.
- **Texto alternativo:** Matriz que separa transformada, DFT, FFT y gráfico por función.

### U05-035 — La DFT evalúa frecuencias discretas llamadas bins

- **Subtítulo:** Su separación depende del registro.
- **Contenido visible:** Bin `k`: posición frecuencial `f_k=kΔf`. Los bins no son bandas normalizadas ni tienen ancho físico universal.
- **Ecuación:** `f_k=kΔf`.
- **Definiciones:** `k`: índice entero; `Δf`: separación entre bins en Hz.
- **Ejemplo:** bins cada 4 Hz.
- **Caption:** Una componente puede coincidir con un bin o distribuirse entre varios.
- **Visual:** `U05-CH-007`.
- **Layout:** `FA_07_GRAFICO_EXPLICACION`.
- **Fuente:** TEX 5.4.4 y 5.4.7; NOT.
- **Texto alternativo:** Rejilla de frecuencias discretas con bins y dos componentes señaladas.

### U05-036 — Observar más tiempo acerca los bins

- **Subtítulo:** La separación nominal mejora; la exactitud no está garantizada.
- **Contenido visible:** Con `f_s` fija, aumentar `N` aumenta `T_obs` y reduce `Δf`.
- **Ecuación:** `Δf=f_s/N=1/T_obs`.
- **Definiciones:** `Δf` en Hz; no equivale por sí sola a precisión.
- **Ejemplo:** `T_obs=0,25 s` → `Δf=4 Hz`; `0,50 s` → `2 Hz`.
- **Caption:** Más duración produce una rejilla frecuencial más densa.
- **Visual:** `U05-CH-007` con ecuación anotada por `U05-DG-004`.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.4.4, ec. 5.9.
- **Texto alternativo:** Dos rejillas de bins comparan registros de diferente duración.

### U05-037 — De `f_s` y `N` a `T_obs` y `Δf`

- **Subtítulo:** Ejemplo resuelto con unidades.
- **Contenido visible:** Datos: `f_s=8000 Hz`, `N=2000`. 1. `T_obs=2000/8000=0,250 s`. 2. `Δf=8000/2000=4 Hz`. 3. Los bins quedan separados nominalmente 4 Hz.
- **Ecuaciones:** `T_obs=N/f_s`; `Δf=f_s/N`.
- **Definición / ejemplo:** procedimiento reproducible.
- **Caption:** Cálculo e interpretación deben conservarse juntos.
- **Visual:** `U05-DG-004`, ejemplo resuelto.
- **Layout:** `FA_10_EJEMPLO_RESUELTO`.
- **Fuente:** TEX 5.4.6.
- **Texto alternativo:** Dos pasos de cálculo terminan en un eje con bins cada 4 Hz.

### U05-038 — Si duplicamos `N`, ¿qué cambia realmente?

- **Subtítulo:** Mantenga `f_s` constante.
- **Contenido visible:** Elija y justifique: A. se duplica `f_s`; B. se duplica `T_obs`; C. `Δf` se reduce a la mitad; D. la frecuencia estimada se vuelve exacta.
- **Ecuaciones:** `T_obs=N/f_s`; `Δf=f_s/N`.
- **Definiciones / ejemplo:** —
- **Caption:** Más datos no mejoran automáticamente todos los aspectos del análisis.
- **Visual:** ecuaciones como pista, sin respuesta visible.
- **Layout:** `FA_14B_MINI_EJERCICIO`.
- **Fuente:** TEX ejercicio D2.
- **Texto alternativo:** Pregunta de opción múltiple con dos ecuaciones de apoyo.

### U05-039 — Más resolución no significa frecuencia exacta

- **Subtítulo:** La estimación también depende de señal, ruido y método.
- **Contenido visible:** Error: “menor `Δf` garantiza exactitud”. Corrección: influyen estabilidad, relación señal/ruido, ventana y estimador.
- **Ecuación:** `Δf=1/T_obs` describe separación nominal.
- **Definición:** Precisión y resolución no son sinónimos.
- **Ejemplo:** dos picos borrosos aun con bins cercanos.
- **Caption:** La rejilla limita la lectura, pero no resume toda la incertidumbre.
- **Visual:** `U05-DG-004`, variante error y condiciones.
- **Layout:** `FA_15_ERROR_FRECUENTE`.
- **Fuente:** TEX 5.4.4 y 5.13.
- **Texto alternativo:** Ecuación de separación rodeada por cuatro factores que afectan la estimación.

### U05-040 — Hasta acá: registro, DFT, FFT y bins

- **Subtítulo:** Parámetros mínimos para interpretar un gráfico digital.
- **Contenido visible:** `f_s` y `N` definen duración y bins. La FFT calcula la DFT. La ordenada necesita unidad y normalización. Pregunta: ¿qué dato falta si solo dice “FFT”?
- **Ecuaciones:** `T_obs=N/f_s`; `Δf=f_s/N`.
- **Definición / ejemplo:** —
- **Caption:** El resultado depende de cómo se registró y representó la señal.
- **Visual:** `U05-DG-014`, recap 3.
- **Layout:** `FA_16_RECAP_PARCIAL`.
- **Fuente:** TEX 5.4.4; U05-031–039.
- **Texto alternativo:** Cadena digital recapitulada con metadatos de muestreo, duración y ordenada.

## B04 · Ventanas y tiempo–frecuencia

### U05-041 — El espectro depende del recorte temporal

- **Subtítulo:** Analizar un segmento implica seleccionar una parte del registro.
- **Contenido visible:** ¿Qué cambia si el recorte contiene un número entero o no entero de ciclos?
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** La observación finita forma parte del análisis.
- **Visual:** señal larga y segmento de `U05-CH-008`.
- **Layout:** `FA_01_DIVISOR`.
- **Fuente:** TEX 5.4.5.
- **Texto alternativo:** Señal extensa con una región temporal seleccionada.

### U05-042 — Recortar una señal equivale a multiplicarla por una ventana

- **Subtítulo:** La ventana pondera qué parte del registro entra al análisis.
- **Contenido visible:** Señal × ventana = segmento analizado.
- **Ecuación:** `señal ventaneada=x(t)·w(t)`.
- **Definiciones:** `w(t)`: ventana adimensional; la señal ventaneada conserva la unidad de `x(t)`.
- **Ejemplo:** ventana rectangular: 1 dentro del intervalo y 0 fuera.
- **Caption:** Toda selección temporal tiene una forma de ventana, explícita o implícita.
- **Visual:** `U05-DG-005`, proceso de tres etapas.
- **Layout:** `FA_12_PROCESO`.
- **Fuente:** TEX 5.4.5; EP.
- **Texto alternativo:** Tres mini gráficos muestran señal, ventana y producto resultante.

### U05-043 — El mismo tono puede repartirse entre varios bins

- **Subtítulo:** La compatibilidad entre frecuencia, duración y ventana modifica el resultado.
- **Contenido visible:** Caso A: número entero de períodos. Caso B: número no entero. Misma frecuencia; distinta distribución espectral.
- **Ecuaciones:** —
- **Definición:** Fuga espectral: distribución de una contribución entre bins por observación finita.
- **Ejemplo:** tono sintético con ventana rectangular.
- **Caption:** La fuga no representa nuevas componentes físicas ni ruido agregado.
- **Visual:** `U05-CH-008`.
- **Layout:** `FA_07_GRAFICO_EXPLICACION`.
- **Fuente:** TEX 5.4.5; EP.
- **Texto alternativo:** Dos registros temporales y sus espectros comparan ciclos enteros y no enteros.

### U05-044 — Fuga espectral: distribución causada por el registro finito

- **Subtítulo:** No es una falla única del software.
- **Contenido visible:** Causa: recorte y discontinuidad de borde. Efecto: una contribución se distribuye. Depende de frecuencia, duración y ventana.
- **Ecuaciones:** —
- **Definición / ejemplo:** mini caso derivado de U05-043.
- **Caption:** Un tono no ocupa necesariamente una sola línea de la DFT.
- **Visual:** detalle de `U05-CH-008` con callouts.
- **Layout:** `FA_08_DEFINICION`.
- **Fuente:** TEX 5.4.5 y 5.13.
- **Texto alternativo:** Pico central con contribuciones laterales y llamadas a borde y duración.

### U05-045 — Una ventana reduce lóbulos laterales y ensancha picos

- **Subtítulo:** Toda elección introduce un compromiso.
- **Contenido visible:** Rectangular: lóbulo principal estrecho, laterales altos. Hann: lóbulo principal más ancho, laterales menores. Elegir según la pregunta.
- **Ecuaciones / ejemplo:** —
- **Definición:** Lóbulo principal y lóbulos laterales describen la respuesta de la ventana.
- **Caption:** Ninguna ventana mejora simultáneamente todos los criterios.
- **Visual:** recurso CH-009 pendiente de cerrar fuente y normalización; usar esquema conceptual provisional.
- **Layout:** `FA_11_COMPARACION`.
- **Fuente:** TEX 5.4.5; SciPy pendiente de verificación.
- **Texto alternativo:** Comparación conceptual de ventanas rectangular y Hann y sus respuestas normalizadas.

### U05-046 — Ventanas cortas y largas responden preguntas diferentes

- **Subtítulo:** Resolución temporal y frecuencial compiten.
- **Contenido visible:** Ventana corta: localiza cambios. Ventana larga: separa frecuencias próximas. Leer siempre tiempo, frecuencia, color y parámetros.
- **Ecuaciones / definiciones:** —
- **Ejemplo:** `25 ms` frente a `200 ms`.
- **Caption:** El espectrograma depende de la duración de ventana elegida.
- **Visual:** alternativa conceptual basada en TEX fig. 5.3; CH-010 vocal pendiente.
- **Layout:** `FA_22_VISUAL_COMPLETO`.
- **Fuente:** TEX fig. 5.3; PDF p. 126.
- **Texto alternativo:** Dos espectrogramas de la misma señal muestran mejor localización temporal o mejor separación frecuencial.

### U05-047 — Un espectrograma repite el análisis sobre segmentos sucesivos

- **Subtítulo:** Cada columna resume un espectro local.
- **Contenido visible:** Segmentar → aplicar ventana → calcular espectro → codificar magnitud con color → avanzar en el tiempo.
- **Ecuaciones:** —
- **Definición:** Espectrograma: representación tiempo–frecuencia cuya escala de color debe declararse.
- **Ejemplo:** seguimiento de un cambio tonal.
- **Caption:** Tiempo, frecuencia y color codifican tres dimensiones.
- **Visual:** `U05-DG-005`, variante proceso tiempo–frecuencia.
- **Layout:** `FA_12_PROCESO`.
- **Fuente:** TEX 5.4.5; GLO.
- **Texto alternativo:** Cinco etapas convierten una señal segmentada en columnas de un espectrograma.

### U05-048 — Un espectrograma muestra cambios; no basta para diagnosticar

- **Subtítulo:** Una descripción acústica aislada no determina una condición clínica.
- **Contenido visible:** Ejemplo sintético de 3 s: tiempo en el eje horizontal, frecuencia en el vertical e intensidad espectral en la escala de color. Debe informar `f_s`, ventana, solapamiento y escala.
- **Ecuaciones:** —
- **Definición / ejemplo:** describir cuándo aparecen componentes de 500, 1500 y 3000 Hz; no inferir una condición clínica.
- **Caption:** Lectura cualitativa de un ejemplo sintético del libro; no es un registro vocal ni autoriza inferencia clínica.
- **Visual:** `context/libro_latex/figures/espectrograma.png`, figura del libro.
- **Layout:** `FA_13_APLICACION_CLINICA`.
- **Fuente:** TEX 5.12; Brockmann2011.
- **Texto alternativo:** Espectrograma sintético de tres segundos con componentes en 500, 1500 y 3000 Hz y barra de intensidad espectral.

### U05-049 — Un bin depende del registro; una banda depende de límites

- **Subtítulo:** Ambos ocupan frecuencia, pero no son el mismo objeto.
- **Contenido visible:** Bin: posición de la DFT; cambia con `T_obs`. Banda: intervalo `[f_L,f_H]`; integra contribuciones entre límites definidos.
- **Ecuaciones:** `f_k=kΔf`.
- **Definiciones:** `f_L` y `f_H`: límites inferior y superior en Hz.
- **Ejemplo:** varios bins dentro de una banda.
- **Caption:** Cambiar la duración mueve la rejilla de bins, no los límites definidos de la banda.
- **Visual:** `U05-DG-005`.
- **Layout:** `FA_11_COMPARACION`.
- **Fuente:** TEX 5.4.7; GLO.
- **Texto alternativo:** Dos ejes alineados muestran bins discretos y una banda delimitada.

### U05-050 — Los niveles por banda no se promedian en dB

- **Subtítulo:** Primero se suman contribuciones compatibles en escala lineal.
- **Contenido visible:** 1. Convertir o conservar magnitud energética lineal. 2. Sumar dentro de la banda. 3. Expresar el resultado como nivel.
- **Ecuaciones:** `q_B=Σq_k`; `L_B=10log10(Σ10^{L_k/10})`.
- **Definiciones:** `q_k`: contribución compatible; `L_k`: nivel con referencia común.
- **Ejemplo:** dos niveles de 50 dB producen 53,01 dB.
- **Caption:** Sumar niveles exige coherencia de magnitud, referencia y tratamiento.
- **Visual:** `U05-DG-005`, variante lineal→nivel.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.4.7; PREV U4.
- **Texto alternativo:** Dos ecuaciones conectan contribuciones lineales con nivel total de banda.

### U05-051 — Hasta acá: duración, ventana, resolución y escala

- **Subtítulo:** Un espectro es inseparable de sus condiciones de análisis.
- **Contenido visible:** Informar: `f_s`; `N` o `T_obs`; ventana; solapamiento si corresponde; ordenada y unidad; escala y normalización. Pregunta: ¿ventana corta o larga para localizar un ataque?
- **Ecuaciones:** `Δf=1/T_obs`.
- **Definición / ejemplo:** —
- **Caption:** Los metadatos hacen reproducible la lectura.
- **Visual:** `U05-DG-014`, recap 4.
- **Layout:** `FA_16_RECAP_PARCIAL`.
- **Fuente:** TEX 5.4.4–5.4.7; NOT.
- **Texto alternativo:** Rutina de lectura ampliada con parámetros de registro y ventana.

## B05 · Señal frente a sistema

### U05-052 — Señal y sistema pueden compartir eje, pero no significado

- **Subtítulo:** ¿La curva describe contenido o transformación?
- **Contenido visible:** Espectro de señal ≠ respuesta en frecuencia de sistema.
- **Ecuación conceptual:** entrada × respuesta = salida.
- **Definiciones / ejemplo:** —
- **Caption:** El objeto representado es la primera pregunta.
- **Visual:** `U05-DG-006`.
- **Layout:** `FA_01_DIVISOR`.
- **Fuente:** PO; TEX 5.5; CDM.
- **Texto alternativo:** Cadena de entrada, sistema y salida acompañada por dos curvas semejantes con significado distinto.

### U05-053 — El espectro pertenece a un registro particular

- **Subtítulo:** Fuente, ambiente, sensor, segmento y método dejan huella.
- **Contenido visible:** El espectro de una vocal depende de: emisión; sala; micrófono; tramo elegido; análisis.
- **Ecuaciones:** —
- **Definición:** Espectro de señal: descripción frecuencial de un registro concreto.
- **Ejemplo:** una vocal sostenida bajo condiciones declaradas.
- **Caption:** No existe “el espectro de la voz” sin contexto.
- **Visual:** `U05-DG-006`, variante señal y condiciones.
- **Layout:** `FA_08_DEFINICION`.
- **Fuente:** TEX 5.5; GLO.
- **Texto alternativo:** Señal central rodeada por cinco condiciones de registro y análisis.

### U05-054 — La respuesta en frecuencia pertenece a un sistema

- **Subtítulo:** Compara cómo cambia la salida respecto de la entrada.
- **Contenido visible:** Ejemplos de sistema: filtro, audífono, tracto vocal. Una salida aislada no permite separar entrada y sistema.
- **Ecuaciones:** —
- **Definición:** Respuesta en frecuencia: relación entrada–salida en función de la frecuencia bajo un modelo y procedimiento.
- **Ejemplo:** ganancia de un audífono bajo prueba.
- **Caption:** La respuesta caracteriza transformación, no contenido de una fuente particular.
- **Visual:** `U05-DG-006`, variante sistema.
- **Layout:** `FA_08_DEFINICION`.
- **Fuente:** PO; TEX 5.5; GLO.
- **Texto alternativo:** Sistema entre entrada y salida con ejemplos de filtro, audífono y tracto vocal.

### U05-055 — Espectro y respuesta se leen con preguntas diferentes

- **Subtítulo:** Curvas parecidas pueden responder preguntas incompatibles.
- **Contenido visible:** Señal: ¿qué contiene este registro? Sistema: ¿cómo transforma una entrada? Datos: registro único frente a pares entrada–salida comparables.
- **Ecuaciones:** —
- **Definición / ejemplo:** espectro vocal frente a respuesta de un dispositivo.
- **Caption:** Preguntar de quién es la curva antes de interpretarla.
- **Visual:** `U05-DG-006`, comparación simétrica.
- **Layout:** `FA_11_COMPARACION`.
- **Fuente:** TEX 5.5; CDM.
- **Texto alternativo:** Dos columnas comparan objeto, datos y conclusiones de espectro y respuesta.

### U05-056 — Entrada, respuesta y salida forman una cadena

- **Subtítulo:** La salida combina contenido de entrada y transformación del sistema.
- **Contenido visible:** `X(f)` entrada · `H(f)` sistema · `Y(f)` salida.
- **Ecuación:** `Y(f)=H(f)X(f)`.
- **Definiciones:** magnitudes complejas bajo la misma convención y frecuencia.
- **Ejemplo:** tres frecuencias con cambios diferentes de amplitud.
- **Caption:** Conocer la salida no determina por separado entrada y sistema.
- **Visual:** `U05-DG-006`.
- **Layout:** `FA_22_VISUAL_COMPLETO`.
- **Fuente:** TEX fig. 5.4.
- **Texto alternativo:** Cadena X–H–Y con tres frecuencias que cambian de manera diferente.

### U05-057 — `H(f)` compara salida y entrada cuando hay señal de prueba

- **Subtítulo:** La división requiere entrada no nula y condiciones compatibles.
- **Contenido visible:** Magnitud de `H`: cambio de tamaño. Fase de `H`: cambio angular o temporal.
- **Ecuación:** `H(f)=Y(f)/X(f)`, con `X(f)≠0`.
- **Definiciones:** `H(f)` puede ser adimensional si entrada y salida tienen la misma unidad.
- **Ejemplo:** relación de presiones en una frecuencia.
- **Caption:** No se divide cualquier salida por cualquier entrada.
- **Visual:** `U05-DG-006`, ecuación anotada.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.5, ec. 5.12; NOT.
- **Texto alternativo:** Ecuación de respuesta conectada a entrada, sistema y salida, con condición X distinta de cero.

### U05-058 — Una reducción de amplitud se expresa como ganancia negativa

- **Subtítulo:** Ejemplo en 1000 Hz.
- **Contenido visible:** Datos: `p_in=1,00 Pa`, `p_out=0,50 Pa`. 1. `|H|=0,50`. 2. `G=20log10(0,50)=−6,02 dB`. 3. La salida tiene la mitad de amplitud en esa frecuencia.
- **Ecuación:** `G(f)=20log10|H(f)|`.
- **Definición:** Ganancia: nivel de una razón de amplitudes compatible.
- **Caption:** Ganancia negativa indica reducción, no “nivel negativo”.
- **Visual:** `U05-DG-006`, ejemplo.
- **Layout:** `FA_10_EJEMPLO_RESUELTO`.
- **Fuente:** TEX 5.5.1; NOT.
- **Texto alternativo:** Dos valores de presión conducen a una razón 0,5 y una ganancia de menos 6,02 dB.

### U05-059 — Un retraso cambia fase sin cambiar magnitud

- **Subtítulo:** Magnitud plana no implica sistema transparente.
- **Contenido visible:** Para un retardo puro, `|H(f)|=1` y la fase cambia linealmente con frecuencia.
- **Ecuación:** `φ_H(f)=−2πfτ`.
- **Definiciones:** `τ`: retardo en s; `φ_H`: fase en rad.
- **Ejemplo:** dos señales iguales desplazadas en el tiempo.
- **Caption:** Un sistema puede conservar amplitud y modificar relaciones temporales.
- **Visual:** `U05-DG-006`, variante retardo.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.5, ec. 5.14.
- **Texto alternativo:** Dos señales desplazadas y una recta de fase decreciente con frecuencia.

### U05-060 — En voz, armónicos de fuente y resonancias del tracto no son lo mismo

- **Subtítulo:** Modelo fuente–filtro introductorio.
- **Contenido visible:** Fuente glótica: periodicidad y líneas. Tracto vocal: respuesta y envolvente. Radiación y registro: salida observada. No es diagnóstico.
- **Ecuación conceptual:** `Salida = Fuente × Filtro`.
- **Definiciones:** Armónicos: componentes periódicas. Formantes: regiones de resonancia.
- **Ejemplo:** vocal sostenida.
- **Caption:** El modelo separa objetos para interpretar un espectro de voz.
- **Visual:** `U05-DG-007`.
- **Layout:** `FA_13_APLICACION_CLINICA`.
- **Fuente:** TEX 5.5 y 5.12; Brockmann2011.
- **Texto alternativo:** Cadena fuente glótica, tracto vocal y registro con mini espectros diferenciados.

### U05-061 — La respuesta de un audífono no es el espectro de la voz

- **Subtítulo:** Dispositivo y señal son objetos diferentes.
- **Contenido visible:** Ganancias del dispositivo: 500 Hz, 1000 Hz y 2000 Hz. Pregunta: ¿qué gráfico caracteriza al audífono y cuál a la voz de entrada?
- **Ecuación:** `G(f)=20log10|H(f)|`.
- **Definición:** Respuesta del dispositivo: relación medida bajo una señal de prueba.
- **Ejemplo:** tres ganancias hipotéticas, sin uso prescriptivo.
- **Caption:** La respuesta del audífono modifica una entrada; no reemplaza su espectro.
- **Visual:** `U05-DG-006`, aplicación a dispositivo.
- **Layout:** `FA_13_APLICACION_CLINICA`.
- **Fuente:** TEX aplicación F3.
- **Texto alternativo:** Audífono entre voz de entrada y salida con tres valores de ganancia por frecuencia.

### U05-062 — Hasta acá: ¿señal, sistema o salida?

- **Subtítulo:** Clasifique el objeto antes de leer la curva.
- **Contenido visible:** Caso A: espectro de una vocal. Caso B: ganancia de un dispositivo. Caso C: espectro a la salida. Para cada uno: datos necesarios y conclusión posible.
- **Ecuación:** `Y=HX`.
- **Definición / ejemplo:** —
- **Caption:** Una misma frecuencia puede aparecer en objetos distintos.
- **Visual:** `U05-DG-014`, recap 5.
- **Layout:** `FA_16_RECAP_PARCIAL`.
- **Fuente:** TEX 5.5; CDM.
- **Texto alternativo:** Cadena entrada–sistema–salida convertida en tres preguntas de clasificación.

## B06 · Componentes espectrales y voz

### U05-063 — Nombrar componentes sin confundir periodicidad y amplitud

- **Subtítulo:** El pico más alto puede no ser la fundamental.
- **Contenido visible:** Fundamental · Armónico · Parcial · Sobretono · Formante.
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** Cada término responde un criterio diferente.
- **Visual:** `U05-CH-011`, caso con segundo armónico dominante.
- **Layout:** `FA_01_DIVISOR`.
- **Fuente:** PO; TEX 5.6.
- **Texto alternativo:** Espectro de líneas donde la componente más alta no coincide con la frecuencia fundamental.

### U05-064 — La fundamental se obtiene de la periodicidad

- **Subtítulo:** Su línea puede ser pequeña o estar ausente.
- **Contenido visible:** El menor período `T_0` organiza la repetición; `f_0` organiza el espaciado armónico.
- **Ecuación:** `f_0=1/T_0`.
- **Definiciones:** `T_0` en s; `f_0` en Hz. No equivale por definición a pitch.
- **Ejemplo:** separación de 100 Hz entre líneas.
- **Caption:** La amplitud no forma parte de la definición de `f_0`.
- **Visual:** `U05-DG-007`, relación tiempo–espectro.
- **Layout:** `FA_08_DEFINICION`.
- **Fuente:** TEX 5.6; GLO.
- **Texto alternativo:** Un período temporal se conecta con el espaciado entre líneas espectrales.

### U05-065 — Armónico, parcial y sobretono responden criterios distintos

- **Subtítulo:** Una componente puede recibir más de una etiqueta válida.
- **Contenido visible:** Armónico: múltiplo entero de `f_0`. Parcial: componente sinusoidal del espectro. Sobretono: parcial por encima de la fundamental; el primero suele coincidir con el segundo armónico en una serie armónica.
- **Ecuación:** `f_n=nf_0`, `n=1,2,3…`.
- **Definición / ejemplo:** 200 Hz con `f_0=100 Hz`: segundo armónico, parcial y primer sobretono.
- **Caption:** Todo armónico es parcial; no todo parcial es armónico.
- **Visual:** tabla nativa de cuatro filas.
- **Layout:** `FA_18_TABLA_DATOS`.
- **Fuente:** TEX 5.6; GLO.
- **Texto alternativo:** Tabla compara término, criterio, ejemplo y advertencia.

### U05-066 — El segundo armónico puede ser el componente mayor

- **Subtítulo:** Altura de línea y orden armónico son propiedades diferentes.
- **Contenido visible:** `f_0=100 Hz`. Línea mayor: 200 Hz. Conclusión: 200 Hz es el segundo armónico, no la fundamental.
- **Ecuación:** `f_2=2f_0`.
- **Definición / ejemplo:** serie armónica sintética.
- **Caption:** La periodicidad decide `f_0`; la amplitud decide cuál línea es mayor.
- **Visual:** panel de `U05-CH-011`.
- **Layout:** `FA_07_GRAFICO_EXPLICACION`.
- **Fuente:** TEX fig. 5.5a.
- **Texto alternativo:** Espectro armónico con líneas cada 100 Hz y máximo en 200 Hz.

### U05-067 — La periodicidad puede persistir sin línea en `f_0`

- **Subtítulo:** El espaciado conserva información de la repetición.
- **Contenido visible:** Líneas: 200, 300 y 400 Hz. Separación común: 100 Hz. `f_0` inferida: 100 Hz, aunque no aparece como línea.
- **Ecuación:** `Δf_componentes=100 Hz=f_0`.
- **Definición:** Fundamental ausente: serie compatible con una periodicidad cuya primera línea no está presente.
- **Ejemplo:** caso sintético, sin inferencia perceptual.
- **Caption:** Una línea visible no es requisito para definir periodicidad.
- **Visual:** panel de `U05-CH-011`.
- **Layout:** `FA_07_GRAFICO_EXPLICACION`.
- **Fuente:** TEX 5.6; fig. 5.5c.
- **Texto alternativo:** Espectro con líneas en 200, 300 y 400 Hz y flechas de separación de 100 Hz.

### U05-068 — No todo parcial cae en un múltiplo entero

- **Subtítulo:** Parcial es una categoría más amplia que armónico.
- **Contenido visible:** Frecuencias: 100, 235, 370 y 520 Hz. Prueba: dividir cada frecuencia por 100 Hz. Las razones no enteras identifican parciales inarmónicos.
- **Ecuaciones:** `f_i/f_0`.
- **Definición:** Parcial inarmónico: componente que no coincide con `nf_0` entero.
- **Ejemplo:** espectro sintético del capítulo.
- **Caption:** La presencia de parciales no garantiza una serie armónica.
- **Visual:** panel de `U05-CH-011`.
- **Layout:** `FA_07_GRAFICO_EXPLICACION`.
- **Fuente:** TEX fig. 5.5b.
- **Texto alternativo:** Espectro con cuatro componentes y razones no enteras respecto de 100 Hz.

### U05-069 — El pico más alto no decide la fundamental

- **Subtítulo:** Use periodicidad y espaciado; no solo altura.
- **Contenido visible:** Caso 1: armónico dominante. Caso 2: fundamental ausente. Caso 3: parciales inarmónicos. Pregunta: ¿en cuál puede justificarse `f_0`?
- **Ecuaciones:** `f_0=1/T_0`; `f_n=nf_0`.
- **Definición / ejemplo:** —
- **Caption:** La evidencia de periodicidad debe explicitarse.
- **Visual:** `U05-DG-007`, tres mini espectros.
- **Layout:** `FA_15_ERROR_FRECUENTE`.
- **Fuente:** TEX 5.13; ejercicio D1.
- **Texto alternativo:** Tres espectros contrastan máximo dominante, fundamental ausente e inarmonicidad.

### U05-070 — Un formante es una región de resonancia, no un armónico

- **Subtítulo:** Las líneas de fuente muestrean una envolvente del sistema vocal.
- **Contenido visible:** Armónicos: líneas relacionadas con periodicidad. Formantes: regiones amplias asociadas con resonancias. Dependencias: vocal, hablante, registro y método.
- **Ecuaciones:** —
- **Definición:** Formante: máximo o región de la envolvente espectral asociada con una resonancia del tracto vocal, según el método usado.
- **Ejemplo:** `F_1` y `F_2` en una vocal, sin diagnóstico.
- **Caption:** Formante y armónico describen objetos diferentes.
- **Visual:** `U05-DG-007`.
- **Layout:** `FA_08_DEFINICION`.
- **Fuente:** TEX 5.5; Brockmann2011.
- **Texto alternativo:** Líneas armónicas aparecen debajo de una envolvente con dos regiones formánticas.

### U05-071 — En una vocal, líneas y envolvente cuentan historias diferentes

- **Subtítulo:** Periodicidad de fuente y resonancias del tracto se leen por separado.
- **Contenido visible:** Líneas cada 100 Hz → periodicidad aproximada. Máximos amplios cerca de 700 y 1100 Hz → regiones de envolvente. Describir no equivale a diagnosticar.
- **Ecuaciones:** `f_0≈100 Hz` por espaciado.
- **Definición / ejemplo:** caso sintético; registro vocal real pendiente.
- **Caption:** Aplicación introductoria del modelo fuente–filtro.
- **Visual:** alternativa conceptual; CH-012 pendiente de U05-MED-003.
- **Layout:** `FA_13_APLICACION_CLINICA`.
- **Fuente:** TEX aplicación F1; Brockmann2011.
- **Texto alternativo:** Espectro sintético de vocal con líneas cada 100 Hz y envolvente con dos máximos amplios.

### U05-072 — ¿Fundamental, armónico, parcial, sobretono o formante?

- **Subtítulo:** Clasifique y justifique el criterio.
- **Contenido visible:** Cinco llamadas sobre dos espectros. Una componente puede admitir varias etiquetas; indique por qué. No use “pico mayor” como única evidencia.
- **Ecuaciones:** `f_n=nf_0`.
- **Definiciones / ejemplo:** actividad de clasificación.
- **Caption:** La etiqueta depende de periodicidad, múltiplo y objeto.
- **Visual:** combinación simplificada de `U05-CH-011` y esquema vocal.
- **Layout:** `FA_14B_MINI_EJERCICIO`.
- **Fuente:** TEX ejercicios C3, L4 y F1.
- **Texto alternativo:** Dos espectros con cinco componentes numeradas para clasificar.

### U05-073 — Hasta acá: periodicidad, componentes y resonancias

- **Subtítulo:** Fuente y sistema aportan informaciones distintas.
- **Contenido visible:** `f_0`: periodicidad. Armónicos y parciales: líneas. Sobretonos: conteo sobre la fundamental. Formantes: resonancias de la envolvente. Puente: pitch se estudiará en U7.
- **Ecuaciones:** `f_n=nf_0`.
- **Definición / ejemplo:** —
- **Caption:** El modelo fuente–filtro ordena el vocabulario.
- **Visual:** `U05-DG-014`, recap 6.
- **Layout:** `FA_16_RECAP_PARCIAL`.
- **Fuente:** TEX 5.5–5.6.
- **Texto alternativo:** Mapa conecta fuente periódica con líneas y tracto vocal con envolvente.

## B07 · Rangos de frecuencia y dinámicos

### U05-074 — Los límites son convenciones bajo condiciones

- **Subtítulo:** Frecuencia y nivel participan en la detectabilidad.
- **Contenido visible:** Infrasonido · rango audible convencional · ultrasonido.
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** Una frontera organiza lenguaje; no describe a todas las personas.
- **Visual:** `U05-CH-013`.
- **Layout:** `FA_01_DIVISOR`.
- **Fuente:** PO; TEX 5.7.
- **Texto alternativo:** Eje logarítmico de frecuencia con tres regiones y transiciones aproximadas.

### U05-075 — `20 Hz` y `20 kHz` son fronteras aproximadas

- **Subtítulo:** Dependen de oyente, nivel, estímulo y condiciones.
- **Contenido visible:** Infrasonido: por debajo de la región convencional. Audible: región convencional variable. Ultrasonido: por encima. No representan igual sensibilidad dentro del rango.
- **Ecuaciones:** —
- **Definición:** Frontera aproximada: referencia organizativa, no umbral universal.
- **Ejemplo:** una misma frecuencia puede detectarse o no al cambiar el nivel.
- **Caption:** Clasificación conceptual, no normativa ni perceptualmente uniforme.
- **Visual:** `U05-CH-013`.
- **Layout:** `FA_07_GRAFICO_EXPLICACION`.
- **Fuente:** TEX 5.7.1; Oxenham2018; ISO 226:2023.
- **Texto alternativo:** Escala logarítmica marca 20 Hz y 20 kHz con bandas de transición y advertencia de aproximación.

### U05-076 — Infrasonido no significa siempre imperceptible

- **Subtítulo:** La experiencia depende de más que la frecuencia.
- **Contenido visible:** Considerar nivel, duración, distorsión del sistema y vibración. No inferir efecto clínico a partir de la etiqueta.
- **Ecuaciones:** —
- **Definición:** Infrasonido: frecuencia por debajo de la frontera audible convencional.
- **Ejemplo:** estímulo de baja frecuencia bajo condiciones controladas, sin cifra de umbral.
- **Caption:** Frecuencia y detectabilidad no son sinónimos.
- **Visual:** esquema frecuencia–nivel conceptual.
- **Layout:** `FA_05_TEXTO_VISUAL_60_40`.
- **Fuente:** TEX 5.7.1; Oxenham2018.
- **Texto alternativo:** Diagrama conceptual combina baja frecuencia con nivel, duración, distorsión y vibración.

### U05-077 — El rango audible cambia con frecuencia, nivel y oyente

- **Subtítulo:** “Audible” describe una relación.
- **Contenido visible:** Estímulo: frecuencia, nivel y duración. Condiciones: ambiente y procedimiento. Oyente: características individuales. Resultado: detectabilidad.
- **Ecuaciones:** —
- **Definición:** Detectabilidad no equivale a sonoridad ni comodidad.
- **Ejemplo:** anticipo de umbrales de U7.
- **Caption:** No existe una caja audible idéntica para todas las personas.
- **Visual:** `U05-DG-008`.
- **Layout:** `FA_05_TEXTO_VISUAL_60_40`.
- **Fuente:** TEX 5.7.1; CM U7.
- **Texto alternativo:** Estímulo, condiciones y oyente convergen en la palabra detectabilidad.

### U05-078 — Ultrasonido nombra frecuencia, no una técnica única

- **Subtítulo:** La aplicación debe identificarse por procedimiento y propósito.
- **Contenido visible:** Ultrasonido: frecuencia superior al rango audible convencional. Ejemplo general: imagenología médica. Contraejemplo: una OEA no es automáticamente “ultrasonido”.
- **Ecuaciones:** —
- **Definición / ejemplo:** aplicación general, sin física de imagenología.
- **Caption:** La etiqueta frecuencial no reemplaza la descripción de la técnica.
- **Visual:** esquema propio; imagen externa solo después de curaduría.
- **Layout:** `FA_13_APLICACION_CLINICA`.
- **Fuente:** TEX 5.7.1.
- **Texto alternativo:** Esquema técnico separa región ultrasónica, imagenología y contraejemplo de OEA.

### U05-079 — Un rango dinámico compara dos niveles compatibles

- **Subtítulo:** Los extremos deben compartir magnitud, referencia y condición.
- **Contenido visible:** Límite inferior `L_inf`. Límite superior `L_sup`. Mismo descriptor y procedimiento.
- **Ecuación:** `R_D=L_sup−L_inf`.
- **Definiciones:** `R_D` en dB; no es un intervalo de frecuencias.
- **Ejemplo:** 62–86 dB SPL → `R_D=24 dB` bajo condiciones declaradas.
- **Caption:** Un rango dinámico es una diferencia de niveles.
- **Visual:** `U05-DG-008`, escala vertical.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.7.2, ec. 5.15; NOT.
- **Texto alternativo:** Escala de niveles con límites inferior y superior y ecuación de diferencia.

### U05-080 — El rango vocal depende de tarea y montaje

- **Subtítulo:** Ejemplo hipotético, no valor universal.
- **Contenido visible:** Condiciones constantes: tarea vocal, distancia, dirección, ponderación y descriptor. Caso: 62–86 dB SPL.
- **Ecuación:** `R_D=86−62=24 dB`.
- **Definición:** Rango vocal medido: intervalo de niveles para una tarea y montaje definidos.
- **Ejemplo:** caso didáctico hipotético.
- **Caption:** No confundir rango dinámico con rango de pitch o sonoridad.
- **Visual:** `U05-DG-008`, aplicación vocal.
- **Layout:** `FA_13_APLICACION_CLINICA`.
- **Fuente:** TEX aplicación F5.
- **Texto alternativo:** Escala de 62 a 86 dB SPL rodeada por cinco condiciones de medición.

### U05-081 — Un instrumento tampoco tiene un único rango dinámico

- **Subtítulo:** Técnica, nota, sala y posición modifican los extremos.
- **Contenido visible:** Antes de comparar valores, declarar: instrumento; ejecución; distancia y orientación; sala; descriptor. No usar una tabla genérica sin fuente.
- **Ecuaciones:** —
- **Definición:** Rango instrumental: diferencia entre niveles extremos bajo un protocolo definido.
- **Ejemplo:** plantilla de medición, sin cifras.
- **Caption:** Los datos concretos requieren fuente y montaje reproducible.
- **Visual:** esquema propio; recurso externo pendiente de curaduría.
- **Layout:** `FA_13_APLICACION_CLINICA`.
- **Fuente:** PO; TEX 5.7.2; OD.
- **Texto alternativo:** Instrumento esquemático acompañado por cinco variables de control.

### U05-082 — El “umbral de dolor” no es un techo universal

- **Subtítulo:** El criterio superior debe definirse explícitamente.
- **Contenido visible:** El programa exige tratar “umbral de dolor”. La interpretación correcta declara frecuencia, estímulo, procedimiento y población; puede emplear incomodidad u otro criterio definido.
- **Ecuaciones:** —
- **Definición:** Límite superior auditivo: criterio de respuesta definido, no una cifra universal.
- **Ejemplo:** comparación conceptual entre detección e incomodidad.
- **Caption:** El término obligatorio se conserva con sus límites de validez.
- **Visual:** `U05-DG-008`, límites condicionados.
- **Layout:** `FA_15_ERROR_FRECUENTE`.
- **Fuente:** PO; TEX 5.7.2; OD-U05-07.
- **Texto alternativo:** Dos límites auditivos conceptuales acompañados por condiciones y un rótulo de criterio definido.

### U05-083 — Hasta acá: frecuencia, nivel y condición

- **Subtítulo:** Dos tipos de rango, dos preguntas distintas.
- **Contenido visible:** Rango frecuencial: clasifica frecuencias. Rango dinámico: compara niveles. Pregunta común: ¿bajo qué estímulo, procedimiento y población?
- **Ecuación:** `R_D=L_sup−L_inf`.
- **Definición / ejemplo:** —
- **Caption:** Ningún límite es interpretable sin condiciones.
- **Visual:** `U05-DG-014`, recap 7.
- **Layout:** `FA_16_RECAP_PARCIAL`.
- **Fuente:** TEX 5.7.
- **Texto alternativo:** Ejes de frecuencia y nivel se cruzan junto a una lista de condiciones.

## B08 · Octavas y bandas

### U05-084 — Dividir el espectro por razones, no por diferencias fijas

- **Subtítulo:** Una octava conserva la relación 2:1.
- **Contenido visible:** ¿Cómo resumimos un espectro sin conservar cada bin?
- **Ecuación:** `f_H/f_L=2` para una octava.
- **Definición / ejemplo:** bandas contiguas en eje logarítmico.
- **Caption:** Igual ancho relativo no significa igual cantidad de hertz.
- **Visual:** esquema conceptual de `U05-DG-009`; CH-014 normativo pendiente.
- **Layout:** `FA_01_DIVISOR`.
- **Fuente:** PO; TEX 5.8.
- **Texto alternativo:** Bandas contiguas ocupan igual longitud en un eje logarítmico.

### U05-085 — Agrupar frecuencias resume el espectro

- **Subtítulo:** Se conserva energía por intervalo y se pierde detalle fino.
- **Contenido visible:** Espectro fino: localiza componentes. Niveles por banda: integran entre límites. Elegir según la pregunta.
- **Ecuaciones:** `q_B=Σq_k`.
- **Definición:** Banda: intervalo de frecuencia definido por `f_L` y `f_H`.
- **Ejemplo:** varios bins reunidos en una barra de banda.
- **Caption:** Una banda no es un bin ensanchado.
- **Visual:** `U05-CH-015`.
- **Layout:** `FA_07_GRAFICO_EXPLICACION`.
- **Fuente:** TEX 5.4.7 y 5.8.
- **Texto alternativo:** Espectro de líneas se compara con barras que integran grupos de frecuencias.

### U05-086 — Una octava cumple `f_H/f_L=2`

- **Subtítulo:** Las fracciones de octava conservan una razón general.
- **Contenido visible:** Para `b` bandas por octava, la razón entre límites es `2^(1/b)`. Casos: `b=1` octava; `b=3` tercio.
- **Ecuación:** `f_H/f_L=2^{1/b}`.
- **Definiciones:** `b`: fracción de octava, adimensional; frecuencias en Hz.
- **Ejemplo:** tercio: razón aproximada `2^(1/3)`.
- **Caption:** En escala logarítmica, razones iguales ocupan distancias iguales.
- **Visual:** `U05-DG-009`.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.8, ec. 5.17.
- **Texto alternativo:** Ecuación de razón y segmentos iguales en eje logarítmico.

### U05-087 — Una serie armónica no avanza por octavas

- **Subtítulo:** Múltiplos enteros y razones 2:1 no son la misma regla.
- **Contenido visible:** Armónicos: `f_0,2f_0,3f_0,4f_0`. Octavas: pares con razón 2:1. Son octavas `f_0→2f_0` y `2f_0→4f_0`; no `2f_0→3f_0`.
- **Ecuaciones:** `f_n=nf_0`; `f_2/f_1=2` para una octava.
- **Definición / ejemplo:** —
- **Caption:** Una serie armónica contiene algunas relaciones de octava, pero no es una escala de octavas.
- **Visual:** `U05-DG-009`, comparación de rectas.
- **Layout:** `FA_11_COMPARACION`.
- **Fuente:** PO; TEX 5.6 y 5.8; EP.
- **Texto alternativo:** Dos rectas numéricas contrastan múltiplos armónicos con saltos de razón dos.

### U05-088 — El centro geométrico conserva simetría de razones

- **Subtítulo:** En bandas logarítmicas no usamos la media aritmética.
- **Contenido visible:** El centro queda a la misma razón del límite inferior y superior.
- **Ecuación:** `f_c=√(f_Lf_H)`.
- **Definiciones:** `f_c`, `f_L`, `f_H` en Hz.
- **Ejemplo:** `f_L=500 Hz`, `f_H=2000 Hz` → `f_c=1000 Hz`.
- **Caption:** `f_c/f_L=f_H/f_c`.
- **Visual:** `U05-DG-009`, eje anotado.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.8, ec. 5.16.
- **Texto alternativo:** Centro geométrico ubicado entre dos límites con razones iguales.

### U05-089 — Los límites se ubican simétricamente en escala logarítmica

- **Subtítulo:** El factor depende de cuántas bandas caben en una octava.
- **Contenido visible:** Partimos de `f_c` y de `b`.
- **Ecuaciones:** `f_L=f_c·2^{−1/(2b)}`; `f_H=f_c·2^{1/(2b)}`.
- **Definiciones:** `b=1` para octava; `b=3` para tercio.
- **Ejemplo:** límites de una banda centrada en 1000 Hz.
- **Caption:** Los límites son recíprocos respecto del centro.
- **Visual:** `U05-DG-009`, ecuaciones anotadas.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.8, ec. 5.18.
- **Texto alternativo:** Dos ecuaciones apuntan a los límites inferior y superior de un eje de banda.

### U05-090 — El ancho en hertz es `B=f_H−f_L`

- **Subtítulo:** Igual ancho relativo produce mayor ancho absoluto a frecuencias altas.
- **Contenido visible:** `B` se expresa en Hz. No confundir con `Δf` entre bins.
- **Ecuación:** `B=f_H−f_L`.
- **Definiciones:** ancho absoluto `B`; separación de bins `Δf`.
- **Ejemplo:** dos octavas con centros diferentes.
- **Caption:** Una razón constante no implica diferencia constante.
- **Visual:** `U05-DG-009`, comparación lineal.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** PO; TEX 5.8, ec. 5.19.
- **Texto alternativo:** Dos bandas con igual razón muestran anchos distintos medidos en hertz.

### U05-091 — Tres tercios completan una octava

- **Subtítulo:** Igual longitud logarítmica; distinto ancho en hertz.
- **Contenido visible:** Octava centrada en 1000 Hz. Tres tercios contiguos. Leer primero razones y luego valores.
- **Ecuaciones:** `f_H/f_L=2`; por tercio, `2^{1/3}`.
- **Definición / ejemplo:** estructura conceptual sin tabla normativa de centros nominales.
- **Caption:** Tres razones iguales componen una razón total 2:1.
- **Visual:** `U05-DG-009`; CH-014 queda pendiente de verificación IEC 61260-1.
- **Layout:** `FA_22_VISUAL_COMPLETO`.
- **Fuente:** TEX fig. 5.6; IEC 61260-1 pendiente.
- **Texto alternativo:** Una octava se divide en tres segmentos iguales sobre un eje logarítmico.

### U05-092 — Tercio de octava centrado en `1000 Hz`

- **Subtítulo:** Cálculo exacto antes del redondeo nominal.
- **Contenido visible:** Dato: `f_c=1000 Hz`, `b=3`. 1. `f_L≈890,9 Hz`. 2. `f_H≈1122,5 Hz`. 3. `B≈231,6 Hz`.
- **Ecuaciones:** `f_L=1000/2^(1/6)=890,9 Hz`; `f_H=1000·2^(1/6)=1122,5 Hz`; `B=231,6 Hz`.
- **Definición:** Valores exactos calculados no equivalen automáticamente a centros nominales normalizados.
- **Ejemplo:** corrige el ancho 176 Hz citado erróneamente en el capítulo.
- **Caption:** El resultado conserva unidad y criterio de cálculo.
- **Visual:** `U05-DG-009`, ejemplo resuelto.
- **Layout:** `FA_10_EJEMPLO_RESUELTO`.
- **Fuente:** TEX 5.8.1; corrección documentada en storyboard.
- **Texto alternativo:** Banda centrada en 1000 Hz con límites 890,9 y 1122,5 Hz y ancho 231,6 Hz.

### U05-093 — ¿Qué banda tiene mayor ancho en hertz?

- **Subtítulo:** Compare octavas centradas en 500 y 2000 Hz.
- **Contenido visible:** Prediga antes de calcular. Ambas mantienen razón 2:1. ¿Cuál tiene mayor `B`? Justifique con una relación multiplicativa.
- **Ecuaciones:** `f_H/f_L=2`; `B=f_H−f_L`.
- **Definiciones / ejemplo:** actividad de comparación.
- **Caption:** A mayor frecuencia central, mayor ancho absoluto para la misma fracción.
- **Visual:** `U05-DG-009`, dos bandas sin respuesta.
- **Layout:** `FA_14B_MINI_EJERCICIO`.
- **Fuente:** TEX ejercicios G3/A2 adaptados.
- **Texto alternativo:** Dos bandas de octava con centros en 500 y 2000 Hz y campos vacíos para límites y ancho.

### U05-094 — Hasta acá: bin, banda, octava y tercio

- **Subtítulo:** Cuatro entidades que no deben confundirse.
- **Contenido visible:** Bin: depende del registro. Banda: intervalo definido. Octava: razón 2:1. Tercio: tres intervalos logarítmicos por octava. Pregunta: ¿cuál cambia al modificar `T_obs`?
- **Ecuaciones:** `Δf=1/T_obs`; `f_H/f_L=2^{1/b}`.
- **Definición / ejemplo:** —
- **Caption:** La elección depende del objeto y de la resolución necesaria.
- **Visual:** `U05-DG-014`, recap 8.
- **Layout:** `FA_16_RECAP_PARCIAL`.
- **Fuente:** TEX 5.4.7 y 5.8.
- **Texto alternativo:** Comparación compacta entre bin, banda, octava y tercio.

## B09 · Filtros

### U05-095 — Un filtro modifica componentes según frecuencia

- **Subtítulo:** Su respuesta define qué regiones conserva o atenúa.
- **Contenido visible:** Pasa bajos · Pasa altos · Pasa banda · Elimina banda.
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** Un filtro es un sistema, no una etiqueta para el espectro de entrada.
- **Visual:** `U05-CH-016`.
- **Layout:** `FA_01_DIVISOR`.
- **Fuente:** PO; TEX 5.9.
- **Texto alternativo:** Cuatro respuestas de filtro esquemáticas con una escala frecuencial común.

### U05-096 — Un filtro se describe por respuesta, cortes y transición

- **Subtítulo:** Tipo y frecuencia de corte no alcanzan por sí solos.
- **Contenido visible:** Informar: objeto; región de paso; región de rechazo; transición; criterio de corte; fase si importa.
- **Ecuaciones:** `B=f_H−f_L` para filtros de dos límites.
- **Definiciones:** `f_c`: frecuencia definida por un criterio; `f_L,f_H`: límites; `B`: ancho en Hz.
- **Ejemplo:** respuesta real pasa bajos.
- **Caption:** El modelo ideal es una referencia; la respuesta real cambia gradualmente.
- **Visual:** `U05-DG-010`.
- **Layout:** `FA_08_DEFINICION`.
- **Fuente:** TEX 5.9; GLO.
- **Texto alternativo:** Respuesta de filtro real anotada con paso, transición, rechazo y corte.

### U05-097 — Pasa bajos y pasa altos conservan regiones opuestas

- **Subtítulo:** Las dos respuestas comparten una frecuencia de corte declarada.
- **Contenido visible:** Pasa bajos: conserva bajas frecuencias. Pasa altos: conserva altas. Ambos presentan transición en un modelo real.
- **Ecuaciones:** —
- **Definición / ejemplo:** modelos Butterworth de orden 4, no dispositivos específicos.
- **Caption:** Leer primero ejes y regiones; después asociar consecuencias sonoras.
- **Visual:** paneles superiores de `U05-CH-016`.
- **Layout:** `FA_11_COMPARACION`.
- **Fuente:** TEX fig. 5.7a–b.
- **Texto alternativo:** Respuestas pasa bajos y pasa altos comparten escala logarítmica y cortes señalados.

### U05-098 — Pasa banda y elimina banda usan dos límites

- **Subtítulo:** Entre `f_L` y `f_H`, una respuesta conserva y la otra atenúa.
- **Contenido visible:** Pasa banda: región central de paso. Elimina banda: región central de rechazo. Notch: rechazo relativamente estrecho.
- **Ecuaciones:** `f_c=√(f_Lf_H)`; `B=f_H−f_L`.
- **Definición / ejemplo:** modelos ilustrativos.
- **Caption:** Centro y ancho describen una región del sistema.
- **Visual:** paneles inferiores de `U05-CH-016`.
- **Layout:** `FA_11_COMPARACION`.
- **Fuente:** TEX fig. 5.7c–d.
- **Texto alternativo:** Respuestas pasa banda y elimina banda con límites inferior y superior.

### U05-099 — Un filtro real no cambia de forma instantánea

- **Subtítulo:** El rectángulo ideal no es una especificación universal.
- **Contenido visible:** Ideal: transición vertical conceptual. Real: pendiente finita, rechazo limitado y fase posible. Los cortes se definen mediante un criterio.
- **Ecuaciones:** —
- **Definición:** Región de transición: intervalo donde cambia la ganancia entre paso y rechazo.
- **Ejemplo:** Butterworth de orden 4 frente a ideal esquemático.
- **Caption:** Tipo de filtro y orden del modelo son informaciones diferentes.
- **Visual:** `U05-CH-016`.
- **Layout:** `FA_22_VISUAL_COMPLETO`.
- **Fuente:** TEX fig. 5.7; script U5.
- **Texto alternativo:** Cuatro paneles comparan respuestas ideales discontinuas con curvas Butterworth suaves.

### U05-100 — La frecuencia de corte requiere un criterio

- **Subtítulo:** `−3 dB` es frecuente, pero no universal.
- **Contenido visible:** Error: “el corte es una pared”. Corrección: indicar curva, criterio y condiciones del modelo o instrumento.
- **Ecuaciones:** `G(f_c)=−3 dB` solo cuando ese criterio fue adoptado.
- **Definición:** Frecuencia de corte: frecuencia identificada mediante un criterio especificado.
- **Ejemplo:** punto de media potencia en un Butterworth compatible.
- **Caption:** Una línea vertical no reemplaza el criterio.
- **Visual:** `U05-DG-010`, curva anotada.
- **Layout:** `FA_15_ERROR_FRECUENTE`.
- **Fuente:** TEX 5.9; GLO; OD-U05-23.
- **Texto alternativo:** Curva real con punto de menos 3 dB y una región de transición sombreada.

### U05-101 — Un pasa banda se describe con límites, centro y ancho

- **Subtítulo:** Los mismos símbolos pueden describir una banda de análisis o un sistema.
- **Contenido visible:** Datos: `f_L=500 Hz`, `f_H=2000 Hz`. `f_c=√(500·2000)=1000 Hz`. `B=2000−500=1500 Hz`.
- **Ecuaciones:** `f_c=√(f_Lf_H)`; `B=f_H−f_L`.
- **Definición:** Aquí los límites pertenecen a la respuesta del filtro.
- **Ejemplo:** cálculo conceptual; criterio de límites debe declararse.
- **Caption:** El objeto “sistema” evita confundir este ancho con una banda de medición.
- **Visual:** `U05-DG-010`, ejemplo.
- **Layout:** `FA_10_EJEMPLO_RESUELTO`.
- **Fuente:** TEX 5.9.
- **Texto alternativo:** Curva pasa banda con límites 500 y 2000 Hz, centro 1000 Hz y ancho 1500 Hz.

### U05-102 — Escuchar qué conserva cada filtro

- **Subtítulo:** La escucha es demostración, no medición.
- **Contenido visible:** Secuencia pendiente: original → pasa bajos → pasa altos → pasa banda. Mantener nivel seguro y el mismo procedimiento. Alternativa: comparar espectros estáticos.
- **Ecuaciones / definiciones:** —
- **Ejemplo:** audio propio pendiente.
- **Caption:** El efecto audible depende de la señal, nivel y respuesta aplicada.
- **Visual:** alternativa estática con `U05-CH-016`; audio pendiente.
- **Layout:** `FA_19_MEDIA_AUDIO_VIDEO`.
- **Fuente:** TEX 5.9; EP.
- **Texto alternativo:** Cuatro espectros muestran señal original y tres versiones filtradas.

### U05-103 — ¿Qué filtro representa cada curva?

- **Subtítulo:** Identifique paso, rechazo y transición.
- **Contenido visible:** Para cada curva: tipo de filtro; región conservada; región atenuada; criterio visible o faltante.
- **Ecuaciones / definiciones:** —
- **Ejemplo:** cuatro curvas derivadas de `U05-CH-016`, sin rótulos.
- **Caption:** El tipo se decide por la respuesta, no por la forma de la caja.
- **Visual:** `U05-CH-016`, versión ejercicio.
- **Layout:** `FA_14_PREGUNTA_EJERCICIO`.
- **Fuente:** TEX ejercicio L5.
- **Texto alternativo:** Cuatro respuestas sin nombre para clasificar como filtros básicos.

### U05-104 — Filtrar, ponderar y filtrar un estímulo persiguen propósitos distintos

- **Subtítulo:** Operaciones semejantes; objetos y salidas diferentes.
- **Contenido visible:** Señal: modificar contenido. Medición: aplicar A/C/Z antes del descriptor. Audiometría: conformar un estímulo bajo referencias específicas. No convertir automáticamente dB SPL en dB HL.
- **Ecuaciones:** —
- **Definiciones:** filtro de señal; ponderación; filtro de estímulo.
- **Ejemplo:** habla filtrada, sonómetro y audiómetro.
- **Caption:** El propósito define qué significa la respuesta.
- **Visual:** `U05-DG-010`, tres procesos paralelos.
- **Layout:** `FA_06B_DOS_COLUMNAS`.
- **Fuente:** TEX 5.9.1; GLO.
- **Texto alternativo:** Tres cadenas paralelas comparan objeto, propósito y resultado de filtrado, ponderación y estímulo audiométrico.

### U05-105 — Hasta acá: tipo, límites, transición y propósito

- **Subtítulo:** Leer un filtro es leer un sistema.
- **Contenido visible:** Tipo: qué región pasa. Límites: dónde se evalúa. Transición: cómo cambia. Propósito: qué objeto modifica. Pregunta: ¿se modifica señal o medición?
- **Ecuaciones:** `Y=HX`.
- **Definición / ejemplo:** —
- **Caption:** La respuesta sola no informa el propósito de uso.
- **Visual:** `U05-DG-014`, recap 9.
- **Layout:** `FA_16_RECAP_PARCIAL`.
- **Fuente:** TEX 5.9.
- **Texto alternativo:** Rutina de lectura aplicada a cuatro propiedades de un filtro.

## B10 · Ponderaciones

### U05-106 — Ponderar es modificar la respuesta de medición

- **Subtítulo:** A, C y Z se aplican antes de informar un descriptor.
- **Contenido visible:** Micrófono → ponderación frecuencial → integración temporal → resultado.
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** Una ponderación pertenece a la cadena de medición.
- **Visual:** DG-011 pendiente de verificación normativa; usar cadena conceptual sin curvas.
- **Layout:** `FA_01_DIVISOR`.
- **Fuente:** PO; TEX 5.10.
- **Texto alternativo:** Cadena conceptual ubica la ponderación entre micrófono e integración.

### U05-107 — La misma señal produce resultados distintos según la ponderación

- **Subtítulo:** Cada respuesta corrige frecuencias de manera diferente.
- **Contenido visible:** Señal de banda ancha → rutas A, C y Z → integración → descriptores distintos. No calcular sin espectro completo.
- **Ecuaciones:** —
- **Definición:** Ponderación frecuencial: filtro normalizado del sistema de medición.
- **Ejemplo:** comparación conceptual sin valores.
- **Caption:** La corrección ocurre frecuencia por frecuencia.
- **Visual:** DG-011 pendiente; alternativa conceptual de tres ramas.
- **Layout:** `FA_12_PROCESO`.
- **Fuente:** TEX 5.10; EP.
- **Texto alternativo:** Una señal se divide en tres rutas A, C y Z que convergen en resultados distintos.

### U05-108 — A, C y Z no responden igual a todas las frecuencias

- **Subtítulo:** Curvas nominales; no bandas de tolerancia.
- **Contenido visible:** A atenúa más las bajas frecuencias. C es más plana. Z es nominalmente plana dentro de límites definidos. Eje: frecuencia logarítmica; corrección en dB.
- **Ecuaciones:** —
- **Definición:** Respuesta nominal no demuestra conformidad de un instrumento.
- **Ejemplo:** anclas cualitativas; no mostrar valores hasta verificar IEC 61672-1.
- **Caption:** Recurso cuantitativo pendiente de fuente normativa autorizada.
- **Visual:** CH-017 pendiente; usar esquema no cuantitativo.
- **Layout:** `FA_22_VISUAL_COMPLETO`.
- **Fuente:** TEX 5.10; IEC 61672-1 pendiente.
- **Texto alternativo:** Esquema cualitativo compara A, C y Z sin valores normativos.

### U05-109 — La ponderación A es una respuesta normalizada de medición

- **Subtítulo:** `dB(A)` informa respuesta frecuencial, no toda la configuración.
- **Contenido visible:** Escritura del programa: dBA. Escritura adoptada: `dB(A)` o descriptor completo. Ejemplos: `L_Aeq,T`, `L_AFmax`.
- **Ecuaciones:** —
- **Definiciones:** `A`: ponderación frecuencial; `F`: respuesta temporal Fast; `eq`: equivalente; `T`: intervalo.
- **Ejemplo:** una lectura debe completar el descriptor.
- **Caption:** Ponderación no equivale a audición individual ni a dB HL.
- **Visual:** cadena conceptual de DG-011, pendiente.
- **Layout:** `FA_08_DEFINICION`.
- **Fuente:** PO; TEX 5.10; NOT; GLO.
- **Texto alternativo:** Definición de ponderación A junto a ejemplos de descriptores completos.

### U05-110 — Para un tono, la corrección se aplica en su frecuencia

- **Subtítulo:** Esta suma en dB representa una corrección de respuesta, no suma de fuentes.
- **Contenido visible:** Condición: tono de una frecuencia conocida y valor de corrección verificado.
- **Ecuación:** `nivel A(f)=nivel Z(f)+corrección A(f)`.
- **Definiciones:** `L_Z`: nivel con ponderación Z; `A(f)`: corrección A en dB; `L_A`: resultado A.
- **Ejemplo:** tono de 63 Hz, con corrección de −26,2 dB según la referencia citada en el capítulo.
- **Caption:** La relación no se aplica como constante a señales de banda ancha.
- **Visual:** ecuación conceptual; punto normativo pendiente.
- **Layout:** `FA_09_ECUACION_INTERPRETACION`.
- **Fuente:** TEX 5.10, ec. 5.20; IEC 61672-1 pendiente.
- **Texto alternativo:** Ecuación de corrección para un tono conectada a una frecuencia puntual.

### U05-111 — Un tono de `63 Hz` cambia mucho entre Z y A

- **Subtítulo:** La corrección es puntual y depende de la frecuencia.
- **Contenido visible:** Dato del capítulo: `L_Z=80,0 dB(Z)`; `A(63 Hz)=−26,2 dB`. Cálculo: `L_A=80,0−26,2=53,8 dB(A)`.
- **Ecuación:** `L_A=L_Z+A(f)`.
- **Definición:** Corrección puntual válida para ese tono y esa edición de tabla.
- **Ejemplo:** no generalizar a banda ancha ni a percepción.
- **Caption:** Resultado verificado para el valor de corrección citado; no se generaliza a banda ancha.
- **Visual:** cálculo textual con condición de tono explícita.
- **Layout:** `FA_10_EJEMPLO_RESUELTO`.
- **Fuente:** TEX 5.10.1; IEC 61672-1:2013.
- **Texto alternativo:** Cálculo para un tono de 63 Hz: 80,0 dB(Z) − 26,2 dB = 53,8 dB(A).

### U05-112 — Una corrección única no alcanza para un sonido de banda ancha

- **Subtítulo:** Ponderar exige corregir por frecuencia e integrar energéticamente.
- **Contenido visible:** Error: sumar una constante al nivel total. Corrección: espectro → corrección A por frecuencia → suma energética → descriptor.
- **Ecuaciones:** `L_A(f)=L_Z(f)+A(f)` por componente compatible.
- **Definición / ejemplo:** señal con varias bandas.
- **Caption:** El ejemplo tonal no se traslada directamente a banda ancha.
- **Visual:** DG-011 conceptual, pendiente de curvas.
- **Layout:** `FA_15_ERROR_FRECUENTE`.
- **Fuente:** TEX 5.10; ejercicio G5.
- **Texto alternativo:** Proceso de tres etapas corrige componentes diferentes antes de integrarlas.

### U05-113 — `dB(A)`, dB SPL, dB HL y sonoridad no son intercambiables

- **Subtítulo:** Magnitud, referencia y percepción responden a procedimientos distintos.
- **Contenido visible:** dB SPL: nivel físico referido a presión. dB(A): medición con ponderación A. dB HL: referencia audiométrica. Sonoridad: atributo perceptual.
- **Ecuaciones:** —
- **Definiciones:** cada término incluye una referencia o procedimiento propio.
- **Ejemplo:** 72 dB(A) no se convierte automáticamente en dB HL.
- **Caption:** Un número en decibeles no identifica por sí solo qué se midió.
- **Visual:** tabla nativa de cuatro filas.
- **Layout:** `FA_18_TABLA_DATOS`.
- **Fuente:** TEX 5.9.1 y 5.12; NOT; GLO.
- **Texto alternativo:** Tabla compara dB SPL, dB(A), dB HL y sonoridad por referencia y alcance.

### U05-114 — “72 dB(A)”: ¿qué sabemos y qué falta?

- **Subtítulo:** Auditar una lectura incompleta.
- **Contenido visible:** Sabemos: ponderación A. Falta: descriptor temporal; intervalo; respuesta temporal; posición y condiciones; instrumento/procedimiento. ¿Permite inferir dB HL? No.
- **Ecuaciones:** —
- **Definición / ejemplo:** ficha de medición incompleta.
- **Caption:** La unidad escrita no reemplaza el descriptor completo.
- **Visual:** ficha conceptual de DG-011.
- **Layout:** `FA_14_PREGUNTA_EJERCICIO`.
- **Fuente:** TEX ejercicios D4/F4.
- **Texto alternativo:** Lectura 72 dB(A) rodeada por cinco campos faltantes.

### U05-115 — Curva nominal y tolerancia de instrumento no son lo mismo

- **Subtítulo:** Una respuesta objetivo no demuestra conformidad.
- **Contenido visible:** Curva nominal: objetivo de ponderación. Tolerancia: banda de aceptación según clase, frecuencia y ensayo. Conformidad: requiere procedimiento y evidencia.
- **Ecuaciones:** —
- **Definición / ejemplo:** esquema conceptual; no reproducir tolerancias.
- **Caption:** Detalle normativo reservado hasta disponer de fuente completa.
- **Visual:** esquema no cuantitativo.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** IEC 61672-1 pendiente; OD-U05-21.
- **Texto alternativo:** Curva objetivo central se diferencia de una banda de aceptación conceptual.

### U05-116 — Hasta acá: filtro de medición, descriptor y límite

- **Subtítulo:** A/C/Z no completan por sí solas una lectura.
- **Contenido visible:** Ponderación: modifica respuesta frecuencial. Descriptor: resume tiempo o extremo. Intervalo y condiciones: delimitan la interpretación. Caso: tono ≠ banda ancha.
- **Ecuaciones:** —
- **Definición / ejemplo:** —
- **Caption:** El nombre completo del resultado conserva las decisiones de medición.
- **Visual:** `U05-DG-014`, recap 10.
- **Layout:** `FA_16_RECAP_PARCIAL`.
- **Fuente:** TEX 5.10.
- **Texto alternativo:** Cadena de medición recapitulada con ponderación, descriptor, intervalo y condiciones.

## B11 · Sonómetro y descriptores

### U05-117 — Del micrófono al resultado informado

- **Subtítulo:** Un sonómetro procesa presión local bajo una configuración declarada.
- **Contenido visible:** Transducción · Procesamiento · Integración · Informe.
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** El número de pantalla es el final de una cadena.
- **Visual:** `U05-DG-012`.
- **Layout:** `FA_01_DIVISOR`.
- **Fuente:** PO; TEX 5.11; PREV.
- **Texto alternativo:** Cadena funcional agrupa seis etapas en transducción, procesamiento e informe.

### U05-118 — Sonómetro, micrófono y calibrador cumplen funciones distintas

- **Subtítulo:** Reconocer componentes no demuestra clase ni conformidad.
- **Contenido visible:** Micrófono: transduce presión. Cuerpo: acondiciona, procesa e informa. Calibrador acústico: aporta una señal de referencia para una comprobación definida.
- **Ecuaciones:** —
- **Definiciones:** comprobación no equivale automáticamente a calibración completa.
- **Ejemplo:** inspección física si el equipo está disponible.
- **Caption:** Fotografía o equipo real sujeto a fuente, licencia y disponibilidad.
- **Visual:** imagen técnica pendiente de curaduría o esquema propio.
- **Layout:** `FA_06_VISUAL_TEXTO_40_60`.
- **Fuente:** TEX 5.11.3.
- **Texto alternativo:** Esquema de sonómetro identifica micrófono, cuerpo y calibrador con sus funciones.

### U05-119 — La presión existe antes de que aparezca un número en pantalla

- **Subtítulo:** La cadena cambia representación, no el fenómeno ya ocurrido.
- **Contenido visible:** `p(t)` → micrófono → preamplificación/conversión → ponderación → detector/integración → indicador e informe.
- **Ecuaciones:** —
- **Definición:** Sonómetro: instrumento que mide niveles acústicos según configuración y especificaciones declaradas.
- **Ejemplo:** arquitectura conceptual, no modelo comercial.
- **Caption:** Cada etapa debe conservar su función y configuración.
- **Visual:** `U05-DG-012`.
- **Layout:** `FA_22_VISUAL_COMPLETO`.
- **Fuente:** TEX fig. 5.8.
- **Texto alternativo:** Seis cajas en dos filas siguen el recorrido desde presión acústica hasta informe.

### U05-120 — El nivel equivalente conserva la media cuadrática del intervalo

- **Subtítulo:** Un nivel constante equivalente representa la misma contribución energética media.
- **Contenido visible:** Señal variable durante `T` → promedio de `p_X²` → nivel constante equivalente `L_Xeq,T`. No promediar lecturas en dB.
- **Ecuaciones:** forma integral en respaldo U05-146.
- **Definiciones:** `X`: ponderación frecuencial; `eq`: equivalente; `T`: intervalo.
- **Ejemplo:** dos tramos de igual duración.
- **Caption:** La intuición proviene del RMS estudiado en U4.
- **Visual:** `U05-DG-012`, variante equivalente.
- **Layout:** `FA_08_DEFINICION`.
- **Fuente:** TEX 5.11.1; GLO.
- **Texto alternativo:** Señal variable entra a un bloque de promedio cuadrático y produce un nivel constante equivalente.

### U05-121 — `70 dB` y `80 dB` no promedian `75 dB`

- **Subtítulo:** Para tiempos iguales, domina el tramo de mayor energía.
- **Contenido visible:** 1. Escala lineal: `10^(70/10)` y `10^(80/10)`. 2. Promedio de ambas contribuciones. 3. Logaritmo: `L_eq≈77,4 dB`.
- **Ecuación:** Escala lineal: `(10^7+10^8)/2`; al volver a dB se obtiene `77,4 dB`.
- **Definiciones:** intervalo total dividido en dos tramos iguales.
- **Ejemplo:** resultado 77,4 dB, no 75 dB.
- **Caption:** Los decibeles se convierten antes de promediar.
- **Visual:** `U05-CH-018` con cálculo de `U05-DG-012`.
- **Layout:** `FA_10_EJEMPLO_RESUELTO`.
- **Fuente:** TEX 5.11.4.
- **Texto alternativo:** Dos tramos de 70 y 80 dB conducen mediante promedio energético a 77,4 dB.

### U05-122 — Equivalente, máximo y pico responden preguntas distintas

- **Subtítulo:** La misma señal alimenta descriptores diferentes.
- **Contenido visible:** `L_Xeq,T`: integra durante `T`. `L_XYmax`: máximo de una respuesta temporal `Y`. `L_Cpeak`: máximo instantáneo de detector de pico con ponderación C.
- **Ecuaciones:** —
- **Definiciones:** `F` y `S` son respuestas temporales; pico no equivale a máximo Fast.
- **Ejemplo:** señal con un impulso breve y un tramo sostenido.
- **Caption:** Informar el descriptor evita llamar “máximo” a resultados distintos.
- **Visual:** `U05-DG-012`, tres ramas.
- **Layout:** `FA_11_COMPARACION`.
- **Fuente:** TEX 5.11.1–5.11.2; NOT.
- **Texto alternativo:** Una señal se divide hacia detectores equivalente, máximo temporal y pico.

### U05-123 — El ruido de fondo audiométrico no se verifica con un único dB(A)

- **Subtítulo:** El criterio depende de banda, transductor y propósito.
- **Contenido visible:** Caso didáctico no normativo: compare nivel y límite hipotético en seis bandas. Identifique cuáles superan el límite. No usar una app de teléfono como sustituto del procedimiento.
- **Ecuaciones:** —
- **Definición:** Nivel por banda: resultado integrado entre límites definidos.
- **Ejemplo:** datos explícitamente hipotéticos.
- **Caption:** Ejercicio de lectura; no evalúa conformidad clínica o laboral.
- **Visual:** `U05-CH-019`.
- **Layout:** `FA_13_APLICACION_CLINICA`.
- **Fuente:** TEX aplicación F2; ISO 8253-1/ANSI citadas solo como contexto.
- **Texto alternativo:** Barras por banda se comparan con límites hipotéticos; bandas que exceden llevan tramado.

### U05-124 — Hasta acá: instrumento, configuración y resultado

- **Subtítulo:** Seis campos para que una lectura sea interpretable.
- **Contenido visible:** Magnitud/descriptor; ponderación frecuencial; respuesta temporal; intervalo; posición y ambiente; instrumento y verificación. Pregunta: complete “72 dB”.
- **Ecuaciones:** —
- **Definición / ejemplo:** ficha de medición.
- **Caption:** Una cifra aislada no conserva la cadena que la produjo.
- **Visual:** `U05-DG-014`, recap 11.
- **Layout:** `FA_16_RECAP_PARCIAL`.
- **Fuente:** TEX 5.11–5.13.
- **Texto alternativo:** Lista de seis campos completa una lectura inicialmente expresada solo como 72 dB.

## B12 · Integración y cierre

### U05-125 — Una pregunta profesional determina la representación adecuada

- **Subtítulo:** Elegir la herramienta comienza por identificar el objeto.
- **Contenido visible:** ¿Cuándo cambia? → forma temporal. ¿Qué frecuencias contiene? → espectro. ¿Cómo evoluciona? → espectrograma. ¿Cómo transforma un dispositivo? → respuesta. ¿Qué ocurre por bandas? → medición por bandas.
- **Ecuaciones:** —
- **Definición / ejemplo:** cinco preguntas profesionales breves.
- **Caption:** Representaciones distintas no son intercambiables.
- **Visual:** `U05-DG-013`.
- **Layout:** `FA_13_APLICACION_CLINICA`.
- **Fuente:** BR; TEX 5.12; EP.
- **Texto alternativo:** Árbol de decisión relaciona cinco preguntas con representaciones adecuadas.

### U05-126 — Caso integrador: vocal, espectro y dispositivo

- **Subtítulo:** Separe datos de señal, registro y sistema antes de calcular.
- **Contenido visible:** Datos: `f_s=8000 Hz`, `N=4000`, espaciado armónico `200 Hz`, máximo de envolvente `1000 Hz`; a `1000 Hz`, `p_in=0,020 Pa`, `p_out=0,010 Pa`, retardo `0,50 ms`. Calcular `T_obs`, `Δf`, `f_0`, ganancia y fase; indicar condiciones faltantes.
- **Ecuaciones:** disponibles en los bloques anteriores.
- **Definición / ejemplo:** caso I1 del capítulo.
- **Caption:** No resolver hasta clasificar cada dato por objeto.
- **Visual:** `U05-DG-013`, dos zonas señal/sistema.
- **Layout:** `FA_14_PREGUNTA_EJERCICIO`.
- **Fuente:** TEX pregunta I1.
- **Texto alternativo:** Caso se divide en datos de una vocal y datos de un dispositivo con cinco consignas.

### U05-127 — Resolver exige separar señal, sistema y condiciones

- **Subtítulo:** Una ruta de solución, no una repetición de todas las fórmulas.
- **Contenido visible:** Registro: `T_obs=0,50 s`, `Δf=2 Hz`. Señal: `f_0=200 Hz`; el máximo de envolvente en 1000 Hz no es `f_0`. Sistema: `|H|=0,50`, `G=−6,02 dB`, fase `−180°` a 1000 Hz. Cierre: condiciones para reproducir cada resultado.
- **Ecuaciones:** `T_obs=N/f_s`; `Δf=f_s/N`; `G=20log10|H|`; `φ=−2πfτ`.
- **Definición / ejemplo:** solución resumida; detalle en U05-149.
- **Caption:** Cada resultado pertenece primero a un objeto.
- **Visual:** `U05-DG-013`, solución por rutas.
- **Layout:** `FA_10_EJEMPLO_RESUELTO`.
- **Fuente:** TEX solución I1.
- **Texto alternativo:** Dos columnas de señal y sistema convergen en una lista de condiciones.

### U05-128 — Ocho atajos que cambian el significado

- **Subtítulo:** Corrija cada afirmación con una evidencia.
- **Contenido visible:** FFT=intensidad; espectro=respuesta; máximo=`f_0`; bin=banda; ventana corrige todo; octava=Hz fijo; A=audición; `L_eq`=promedio de dB.
- **Ecuaciones:** —
- **Definición / ejemplo:** cada error se acompaña por una corrección de una línea.
- **Caption:** La precisión terminológica protege la interpretación física.
- **Visual:** dos columnas editables; sin símbolos decorativos.
- **Layout:** `FA_15_ERROR_FRECUENTE`.
- **Fuente:** TEX 5.13; BR.
- **Texto alternativo:** Ocho errores frecuentes se enfrentan a ocho correcciones breves.

### U05-129 — De una señal registrada a una medición interpretable

- **Subtítulo:** Objeto, representación, método, parámetros y límites forman una cadena.
- **Contenido visible:** Señal física → registro → representación → análisis → sistema/banda/filtro → ponderación → descriptor → conclusión limitada.
- **Ecuaciones:** solo relaciones ancla: `T_obs=N/f_s`, `Y=HX`, `R_D=L_sup−L_inf`.
- **Definición / ejemplo:** mapa final.
- **Caption:** Interpretar es conservar la trazabilidad de cada transformación.
- **Visual:** `U05-DG-001`, estado final.
- **Layout:** `FA_17_RECAP_FINAL`.
- **Fuente:** PO; TEX 5.1–5.14; CM; CDM.
- **Texto alternativo:** Mapa de ocho nodos recorre desde señal física hasta conclusión con límites.

### U05-130 — ¿Qué podés explicar ahora que al inicio no podías?

- **Subtítulo:** Recuperación sin calificación punitiva.
- **Contenido visible:** Vuelva a U05-002 y U05-003. Elija cuatro acciones: identificar objeto; leer ejes; justificar `f_0`; distinguir señal/sistema; calcular banda; reconocer filtro; completar descriptor; limitar inferencia.
- **Ecuaciones:** —
- **Definición / ejemplo:** autoevaluación con escala de seguridad.
- **Caption:** Comprender incluye reconocer qué información falta.
- **Visual:** tipografía y campos breves.
- **Layout:** `FA_14_PREGUNTA_EJERCICIO`.
- **Fuente:** BR objetivos; U05-002–007.
- **Texto alternativo:** Ocho preguntas de autoevaluación junto a una escala personal de seguridad.

### U05-131 — El oído también responde de manera diferente según frecuencia

- **Subtítulo:** Puente a Unidad 6: un sistema biológico, no una FFT.
- **Contenido visible:** Señal acústica → oído externo y medio → cóclea. Pregunta: ¿cómo se transforma físicamente la señal?
- **Ecuaciones:** —
- **Definición:** Respuesta frecuencial no implica que el sistema ejecute un algoritmo FFT.
- **Ejemplo:** preparación para transferencia y organización frecuencial.
- **Caption:** La próxima unidad estudia mecanismos físicos y biológicos.
- **Visual:** cadena conceptual de tres etapas.
- **Layout:** `FA_21_CIERRE_PUENTE`.
- **Fuente:** CM U5→U6; CDM; TEX 6.1–6.2.
- **Texto alternativo:** Señal acústica atraviesa oído externo y medio antes de llegar a la cóclea.

### U05-132 — Fuentes y recursos para continuar

- **Subtítulo:** Jerarquía y trazabilidad antes de ampliar.
- **Contenido visible:** Programa oficial. Libro del curso. IEC 61260/61672. ISO 226/8253. Brockmann-Bauser y Drinnan. Recursos del aula verificados.
- **Ecuaciones / definiciones / ejemplo:** —
- **Caption:** Los enlaces y QR se incorporarán solo después de verificar edición y acceso.
- **Visual:** tabla de referencias.
- **Layout:** `FA_20_BIBLIO_RECURSOS`.
- **Fuente:** PO; `references.bib`; `source_analysis.md`.
- **Texto alternativo:** Lista de fuentes principales organizada por programa, libro, normas y bibliografía de voz.

## B13 · Respaldo

### U05-133 — Números complejos: una herramienta para magnitud y fase

- **Subtítulo:** Apoyo matemático a demanda.
- **Contenido visible:** Eje real: componente coseno. Eje imaginario: componente seno. Módulo y ángulo forman una representación polar.
- **Ecuaciones:** `j²=−1`; `X=|X|e^{jφ}`.
- **Definiciones:** `|X|`: módulo; `φ`: fase en rad.
- **Ejemplo:** vector complejo con magnitud fija.
- **Caption:** La forma compleja compacta dos componentes matemáticas.
- **Visual:** plano complejo mínimo, editable.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX 5.4.3; NOT.
- **Texto alternativo:** Vector en plano complejo con módulo y ángulo señalados.

### U05-134 — Cómo se calculan `a_n` y `b_n`

- **Subtítulo:** Integrar la coincidencia con seno y coseno sobre un período.
- **Contenido visible:** Misma ventana de un período; dos comparaciones ortogonales; coeficientes con la unidad de `x`.
- **Ecuaciones:** fórmulas completas de `a_n` y `b_n` de U05-023.
- **Definición:** Proyección: medida de semejanza bajo el producto e integración definidos.
- **Ejemplo:** simetría par favorece términos coseno.
- **Caption:** Formalismo de consulta; no requiere resolver integrales en el núcleo.
- **Visual:** ecuaciones anotadas y período resaltado.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX 5.4.1.
- **Texto alternativo:** Dos integrales comparan una señal con coseno y seno en un período.

### U05-135 — Convención y unidades de la transformada

- **Subtítulo:** Las amplitudes absolutas dependen de definición y normalización.
- **Contenido visible:** Convención directa del libro; transformada inversa adoptada; unidades; espectro unilateral o bilateral debe declararse.
- **Ecuaciones:** `X(f)=∫x(t)e^{−j2πft}dt`; `x(t)=∫X(f)e^{j2πft}df`.
- **Definiciones:** si `x` tiene unidad `U`, `X` tiene `U·s` con esta convención.
- **Ejemplo:** presión en Pa → transformada en Pa·s.
- **Caption:** No comparar amplitudes de espectros con normalizaciones distintas.
- **Visual:** par de ecuaciones y tabla de unidades.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX 5.4.3; NOT.
- **Texto alternativo:** Transformada directa e inversa se acompañan por una tabla de unidades.

### U05-136 — DFT: índices, frecuencias y normalización

- **Subtítulo:** Referencia técnica reproducible.
- **Contenido visible:** Índice temporal `n`; índice frecuencial `k`; cantidad `N`; frecuencia `f_k=kf_s/N`. Declarar escala, lados del espectro y normalización.
- **Ecuación:** `X[k]=Σ_{n=0}^{N−1}x[n]e^{−j2πkn/N}`.
- **Definiciones:** `n,k` adimensionales; `f_k` en Hz.
- **Ejemplo:** bins asociados con `k=0,1,2…`.
- **Caption:** La fórmula no determina por sí sola la ordenada graficada.
- **Visual:** ecuación anotada y eje de índices.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX 5.4.4; NOT; EP.
- **Texto alternativo:** Sumatoria DFT con callouts para índices, cantidad de muestras y frecuencia asociada.

### U05-137 — Muestreo y aliasing: límite conceptual

- **Subtítulo:** Frecuencias continuas diferentes pueden compartir las mismas muestras.
- **Contenido visible:** Misma `f_s`, dos senoides candidatas, puntos coincidentes. El límite de Nyquist requiere condiciones y no se evalúa en la ruta central.
- **Ecuaciones:** relación conceptual de frecuencias aliadas.
- **Definición:** Aliasing: ambigüedad producida por muestreo insuficiente para el contenido presente.
- **Ejemplo:** caso de `U05-CH-006`.
- **Caption:** Las muestras no conservan información ilimitada.
- **Visual:** `U05-CH-006`.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** OD-U05-22; NOT; EP.
- **Texto alternativo:** Dos senoides continuas atraviesan los mismos puntos de muestreo.

### U05-138 — Ventanas: ninguna gana en todos los criterios

- **Subtítulo:** Seleccionar según separación, rango dinámico y amplitud.
- **Contenido visible:** Rectangular y Hann: comparar lóbulo principal, laterales y corrección de amplitud. Tercera ventana solo con fuente documentada.
- **Ecuaciones:** —
- **Definición:** Normalización común necesaria para comparar respuestas.
- **Ejemplo:** recurso cuantitativo pendiente CH-009.
- **Caption:** No existe una ventana universalmente superior.
- **Visual:** esquema conceptual hasta aprobar CH-009.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX 5.4.5; fuente SciPy pendiente.
- **Texto alternativo:** Tabla cualitativa compara ventanas rectangular y Hann en tres criterios.

### U05-139 — Sumar bins compatibles dentro de una banda

- **Subtítulo:** Dos contribuciones de 50 dB no producen 100 dB.
- **Contenido visible:** `50 dB` → escala lineal. Sumar dos contribuciones iguales. Volver a dB: `53,01 dB`.
- **Ecuación:** `L_B=10log10(10^{50/10}+10^{50/10})`.
- **Definiciones:** referencia común y contribuciones compatibles.
- **Ejemplo:** resultado 53,01 dB.
- **Caption:** La suma se realiza antes del logaritmo.
- **Visual:** diagrama lineal→suma→nivel.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX ejercicio A3.
- **Texto alternativo:** Dos niveles de 50 dB convergen en una suma energética de 53,01 dB.

### U05-140 — Ganancia y fase de un dispositivo con retardo

- **Subtítulo:** Magnitud y fase describen aspectos diferentes.
- **Contenido visible:** A 500 Hz: `|H|=2` → `G=6,02 dB`. Retardo elegido para `φ_H=−90°`. Interpretar aumento y desplazamiento por separado.
- **Ecuaciones:** `G=20log10|H|`; `φ_H=−2πfτ`.
- **Definiciones:** ganancia en dB; fase en grados o radianes, convención declarada.
- **Ejemplo:** ejercicio A5.
- **Caption:** Igual ganancia no implica igual fase.
- **Visual:** ejemplo por pasos y señales desplazadas.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX ejercicio A5.
- **Texto alternativo:** Cálculos de ganancia y fase se vinculan con dos señales desplazadas.

### U05-141 — Modelo fuente–filtro de voz: alcance y límites

- **Subtítulo:** La envolvente depende también de radiación, sensor y método.
- **Contenido visible:** Fuente → tracto → radiación → ambiente → sensor → análisis. Registrar vocal, `f_s`, ventana, método de envolvente y tramo.
- **Ecuaciones:** `Salida=Fuente×Filtro` como modelo introductorio.
- **Definición:** El modelo organiza causas posibles; no diagnostica por sí solo.
- **Ejemplo:** preguntas reproducibles sobre una vocal.
- **Caption:** Respaldo para profundizar formantes sin introducir jitter o shimmer.
- **Visual:** `U05-DG-007`, versión ampliada dividida en dos filas.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX 5.5 y 5.12; Brockmann2011.
- **Texto alternativo:** Seis etapas muestran desde fuente vocal hasta método de análisis.

### U05-142 — Rangos dinámicos: qué debe declarar una fuente

- **Subtítulo:** Contrato de trazabilidad antes de incorporar cifras.
- **Contenido visible:** Población o fuente; tarea; distancia y orientación; ponderación; descriptor; incertidumbre o dispersión. Aplicar a voz, instrumentos y audición.
- **Ecuaciones:** `R_D=L_sup−L_inf`.
- **Definición / ejemplo:** plantilla sin valores.
- **Caption:** No se aprueba ninguna cifra aislada.
- **Visual:** tabla nativa.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** PO; TEX 5.7.2; OD-U05-06/07.
- **Texto alternativo:** Plantilla de seis campos para evaluar una cifra de rango dinámico.

### U05-143 — Frecuencias centrales nominales requieren norma y edición

- **Subtítulo:** Cálculo exacto y serie nominal no son sinónimos.
- **Contenido visible:** Centro exacto: ecuaciones de banda. Centro nominal: valor tabulado para instrumentos normalizados. Tolerancias: solo desde norma autorizada.
- **Ecuaciones:** `f_c=√(f_Lf_H)`.
- **Definición:** Serie nominal: conjunto de valores redondeados definido por una norma y edición.
- **Ejemplo:** máximo ocho filas solo después de verificar IEC 61260-1.
- **Caption:** Tabla numérica pendiente de verificación normativa.
- **Visual:** tabla conceptual sin valores normativos definitivos.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX 5.8; IEC 61260-1 pendiente.
- **Texto alternativo:** Comparación conceptual entre centro exacto calculado y centro nominal tabulado.

### U05-144 — Orden y pendiente de filtro cambian la transición

- **Subtítulo:** Dos filtros del mismo tipo pueden responder diferente.
- **Contenido visible:** Mismo corte conceptual; distinto orden. Mayor orden: transición más abrupta en este modelo. Tipo no determina por sí solo fase ni rechazo.
- **Ecuaciones:** —
- **Definición:** Orden: parámetro del modelo que influye en la pendiente.
- **Ejemplo:** Butterworth documentado, sin polos ni ceros.
- **Caption:** Comparación teórica con escala común.
- **Visual:** detalle de `U05-CH-016` o variante reproducible.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX fig. 5.7; script U5; EP.
- **Texto alternativo:** Dos curvas Butterworth de distinto orden comparten corte y muestran transiciones diferentes.

### U05-145 — Expresiones nominales de A, C y Z

- **Subtítulo:** Respaldo bloqueado hasta verificar IEC 61672-1.
- **Contenido visible:** Incluir solo después de confirmar expresiones, constantes, normalización y frecuencias de control. Diferenciar respuesta nominal de tolerancias.
- **Ecuaciones / definiciones / ejemplo:** pendientes; no insertar fórmulas provisionales.
- **Caption:** No aprobado para producción en v01.
- **Visual:** placeholder textual, sin curva ni ecuación normativa.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** IEC 61672-1 pendiente; OD-U05-12/21.
- **Texto alternativo:** Marcador de contenido normativo pendiente de verificación autorizada.

### U05-146 — Definición integral de `L_Xeq,T`

- **Subtítulo:** Formalización del promedio cuadrático durante un intervalo.
- **Contenido visible:** Ponderar presión → elevar al cuadrado → promediar durante `T` → dividir por referencia cuadrática → aplicar logaritmo.
- **Ecuación:** `L_Xeq,T=10log10[(1/T)∫_{t_1}^{t_2}p_X²(t)/p_ref² dt]`.
- **Definiciones:** `T=t_2−t_1`; `p_X` en Pa; `p_ref=20 µPa` en aire; resultado en dB.
- **Ejemplo:** vínculo con U05-121.
- **Caption:** La integral expresa la misma idea física que el promedio discreto.
- **Visual:** ecuación anotada y cadena de operaciones.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX 5.11.1, ec. 5.21; NOT.
- **Texto alternativo:** Ecuación integral con callouts para intervalo, presión ponderada y referencia.

### U05-147 — Fast, Slow, máximo y pico: referencias de diseño

- **Subtítulo:** Constantes orientativas no demuestran conformidad.
- **Contenido visible:** Fast: `0,125 s`. Slow: `1 s`. `L_XYmax`: máximo con respuesta temporal `Y`. Pico: detector diferente. Edición normativa obligatoria.
- **Ecuaciones:** —
- **Definiciones:** `F` y `S` son respuestas temporales normalizadas.
- **Ejemplo:** interpretar `L_AFmax` y `L_Cpeak` como descriptores distintos.
- **Caption:** Detalle técnico de respaldo; no es protocolo de ensayo.
- **Visual:** tabla nativa con advertencia.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX 5.11.2; IEC 61672-1/2.
- **Texto alternativo:** Tabla compara Fast, Slow, máximo y pico por función y notación.

### U05-148 — Evaluación de modelo, ensayo periódico y comprobación de campo

- **Subtítulo:** Tres procedimientos, tres alcances documentales.
- **Contenido visible:** Evaluación de modelo: diseño. Ensayo periódico: desempeño del instrumento. Comprobación de campo: condición antes/después del uso. No llamarlos a todos “calibración”.
- **Ecuaciones:** —
- **Definiciones:** propósito, actor, momento y evidencia.
- **Ejemplo:** comparación conceptual, no protocolo operativo.
- **Caption:** El nombre del procedimiento delimita qué puede concluirse.
- **Visual:** tres procesos paralelos.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX 5.11.3; IEC 61672-2/3.
- **Texto alternativo:** Tres columnas comparan evaluación de modelo, ensayo periódico y comprobación de campo.

### U05-149 — Solución completa del caso integrador

- **Subtítulo:** Cada cálculo se asigna primero a señal o sistema.
- **Contenido visible:** Registro: `0,50 s` y `2 Hz`. Señal: `f_0=200 Hz`; máximo de envolvente en `1000 Hz`. Sistema a `1000 Hz`: `|H|=0,50`, `G=−6,02 dB`, fase `−180°`. Cierre: metadatos y límites de inferencia.
- **Ecuaciones:** `T_obs=4000/8000=0,50 s`; `Δf=8000/4000=2 Hz`; `G=20log10(0,50)=−6,02 dB`; `φ=−2π·1000·0,00050=−π rad=−180°`.
- **Definición / ejemplo:** solución completa del capítulo; dividir en dos slides si la fuente baja de 22 pt.
- **Caption:** Respaldo para devolución trazable.
- **Visual:** `U05-DG-015`, solución por pasos.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX solución I1.
- **Texto alternativo:** Solución en dos zonas distingue cálculos de señal y sistema y termina en condiciones.

### U05-150 — Glosario de señales, espectro y medición

- **Subtítulo:** Consulta alfabética; no usar como cierre proyectado.
- **Contenido visible:** Armónico; banda; bin; DFT; espectro; FFT; filtro; formante; frecuencia fundamental; nivel equivalente; parcial; ponderación; respuesta en frecuencia; sobretono; sonómetro; transformada; ventana.
- **Ecuaciones:** —
- **Definiciones:** remitir a `style/glossary.md`; máximo dos líneas por término.
- **Ejemplo:** referencias de retorno a las slides principales.
- **Caption:** La precisión terminológica sostiene la interpretación.
- **Visual:** índice alfabético en dos columnas; dividir si no conserva 22 pt.
- **Layout:** `FA_23_APENDICE`.
- **Fuente:** TEX 5.17; GLO.
- **Texto alternativo:** Glosario alfabético de diecisiete términos con referencias a slides de la unidad.
