# Unidad 5 — Storyboard pedagógico completo

Versión final · 2026-08-03
Fuente de verdad visible: `slide_text.md`. Las notas de implementación y tiempos se encuentran en `speaker_notes.md`.

## Trabajo de comunicación

Al finalizar, estudiantes de primer año deben poder decidir qué representa un gráfico frecuencial, explicar cómo se obtuvo y usarlo para interpretar una señal, un sistema o una medición sin confundir magnitudes físicas, descriptores metrológicos y atributos perceptuales.

## Arco pedagógico

Señal concreta → representaciones → intuición de Fourier → registro finito → ventanas y tiempo–frecuencia → señal/sistema → componentes → rangos → bandas → filtros → medición → decisión profesional. La intuición precede al formalismo; integrales, forma compleja y desarrollos técnicos quedan en ampliación o respaldo.

## Fuentes y abreviaturas

- `PO`: programa oficial 2025, U5.
- `TEX`: libro del curso, capítulo 5 en LaTeX.
- `PDF`: libro del curso, pp. 119–149.
- `NOT`: `style/notation_guide.md`.
- `GLO`: `style/glossary.md`.
- `CM`: mapa del curso y dependencias.
- `EP`: elaboración pedagógica propia.

## Bloques y preguntas guía

| bloque | título | pregunta guía | slides |
|---|---|---|---|
| B00 | Apertura y orientación | ¿Qué objeto, representación y límite estamos leyendo? | U05-001–007 |
| B01 | Representaciones de señal | ¿Qué cambia entre tiempo, frecuencia y fase? | U05-008–017 |
| B02 | Herramientas de Fourier | ¿Cómo representan sinusoides una señal compleja? | U05-018–029 |
| B03 | Registro digital | ¿Cómo condicionan muestreo, duración y bins el resultado? | U05-030–040 |
| B04 | Ventanas y tiempo–frecuencia | ¿Qué información se gana y se pierde al recortar? | U05-041–051 |
| B05 | Señal y sistema | ¿La curva describe contenido o transformación? | U05-052–062 |
| B06 | Componentes y terminología espectral | ¿Cómo se distinguen fundamental, armónico, parcial y formante? | U05-063–073 |
| B07 | Rangos y límites | ¿De qué condiciones dependen los límites frecuenciales? | U05-074–083 |
| B08 | Octavas y bandas | ¿Cómo se agrupan frecuencias conservando razones? | U05-084–094 |
| B09 | Filtros | ¿Qué región conserva o atenúa un filtro y bajo qué criterio? | U05-095–105 |
| B10 | Ponderaciones | ¿Qué significa aplicar A, C o Z a una medición? | U05-106–116 |
| B11 | Sonómetro y descriptores | ¿Cómo se obtiene e informa un nivel reproducible? | U05-117–124 |
| B12 | Integración y cierre | ¿Qué representación responde una pregunta profesional? | U05-125–132 |
| B13 | Respaldo | ¿Qué formalismo o detalle técnico hace falta consultar? | U05-133–150 |

## Storyboard slide por slide

| slide | bloque | función | título | intención visible | visual | layout | fuente | ruta |
|---|---|---|---|---|---|---|---|---|
| U05-001 | B00 · Apertura y orientación | explicación | Unidad 5 · Análisis frecuencial de señales acústicas | De la señal registrada a una interpretación con límites. | transición mínima entre forma temporal y espectro; sin fórmulas. | FA_00_PORTADA. | PO; BR; CM. | central |
| U05-002 | B00 · Apertura y orientación | pregunta/actividad | Dos señales tienen igual RMS: ¿son iguales? | Un mismo descriptor global puede ocultar estructuras diferentes. | `U05-CH-001`. | FA_22_VISUAL_COMPLETO. | PREV U04-109; BR; TEX 5.1. | central |
| U05-003 | B00 · Apertura y orientación | pregunta/actividad | ¿Qué representa cada gráfico? | Primero describimos; después interpretamos. | `U05-DG-002`, versión sin respuestas. | FA_14B_MINI_EJERCICIO. | BR; CDM; EP. | central |
| U05-004 | B00 · Apertura y orientación | explicación | Lo que recuperamos de U3 y U4 | Dos caminos convergen en la señal compleja. | `U05-DG-002`, variante puente U3/U4. | FA_02B_CONOCIMIENTOS_PREVIOS. | TEX 5.2; BR; NOT. | central |
| U05-005 | B00 · Apertura y orientación | explicación | Qué podremos interpretar, calcular y explicar | Ocho resultados observables. | composición tipográfica en cuatro pares. | FA_02_OBJETIVOS. | BR objetivos; CM. | ampliación |
| U05-006 | B00 · Apertura y orientación | explicación | Mapa de la unidad: de la señal a la decisión | Cuatro tramos, una rutina de lectura. | `U05-DG-001`. | FA_03_MAPA_CLASE. | BR; CM; CDM. | central |
| U05-007 | B00 · Apertura y orientación | explicación | Cinco preguntas para leer cualquier gráfico | Una lectura válida empieza antes de mirar la curva. | `U05-DG-002`. | FA_12_PROCESO. | BR; NOT; GLO. | central |
| U05-008 | B01 · Representaciones de señal | divisor | Una señal, varias representaciones | ¿Qué pregunta responde cada vista? | motivo técnico de una señal temporal discreta. | FA_01_DIVISOR. | TEX 5.3; PDF p. 120. | central |
| U05-009 | B01 · Representaciones de señal | explicación | El dominio temporal muestra cuándo cambia la señal | Leemos evolución, duración y transitorios. | panel temporal de `U05-CH-002`. | FA_08_DEFINICION. | TEX 5.3; NOT. | central |
| U05-010 | B01 · Representaciones de señal | explicación | El dominio frecuencial organiza contribuciones por frecuencia | El eje vertical debe nombrarse: no es automáticamente intensidad. | `U05-DG-003`, variante espectro anotado. | FA_08_DEFINICION. | TEX 5.3; NOT; GLO. | central |
| U05-011 | B01 · Representaciones de señal | explicación | Una presión, tres lecturas | Tiempo, magnitud y fase describen la misma señal. | `U05-CH-002`. | FA_22_VISUAL_COMPLETO. | TEX fig. 5.1; PDF p. 122. | ampliación |
| U05-012 | B01 · Representaciones de señal | pregunta/actividad | Leamos el gráfico antes de interpretarlo | Describir no es todavía explicar una causa. | `U05-CH-002` con llamadas numeradas. | FA_14_PREGUNTA_EJERCICIO. | TEX ejercicios L1. | ampliación |
| U05-013 | B01 · Representaciones de señal | explicación | La fase cambia la forma sin cambiar las magnitudes | “Cuánto” y “cuándo dentro del ciclo” son informaciones distintas. | `U05-CH-003`. | FA_07_GRAFICO_EXPLICACION. | TEX 5.4.3; BR. | ampliación |
| U05-014 | B01 · Representaciones de señal | explicación | Igual magnitud espectral no significa igual señal temporal | Para reconstruir la forma se necesitan magnitud y fase. | `U05-CH-003`, versión comparativa. | FA_11_COMPARACION. | TEX 5.4.3; EP. | ampliación |
| U05-015 | B01 · Representaciones de señal | formalización/ejemplo | Una señal periódica repite un patrón | El menor período define la frecuencia fundamental. | `U05-DG-003`, variante periodicidad. | FA_09_ECUACION_INTERPRETACION. | TEX 5.3.1, ecs. 5.1–5.2. | central |
| U05-016 | B01 · Representaciones de señal | explicación | Periódica, aperiódica y transitoria no son etiquetas excluyentes | Una vocal puede ser casi periódica en un tramo y transitoria en sus bordes. | alternativa conceptual; `U05-CH-004` queda pendiente de U05-MED-003. | FA_11_COMPARACION. | TEX 5.3.1; GLO. | ampliación |
| U05-017 | B01 · Representaciones de señal | recapitulación | Hasta acá: tiempo, frecuencia y fase | Elegimos la vista según la pregunta. | `U05-DG-014`, recap 1. | FA_16_RECAP_PARCIAL. | TEX 5.3; U05-007–016. | central |
| U05-018 | B02 · Herramientas de Fourier | divisor | Fourier: representar una señal con sinusoides | Cambiamos la forma de describir; no modificamos la señal. | `U05-DG-003`, variante suma progresiva. | FA_01_DIVISOR. | TEX 5.4; BR. | central |
| U05-019 | B02 · Herramientas de Fourier | pregunta/actividad | ¿Podemos construir una forma compleja sumando tonos? | Prediga antes de observar el resultado. | `U05-CH-005`, estado de tres términos. | FA_14_PREGUNTA_EJERCICIO. | U3; TEX 5.4; EP. | central |
| U05-020 | B02 · Herramientas de Fourier | explicación | Escuchar componentes y suma | La escucha ilustra la suma; no demuestra una teoría perceptual. | alternativa estática `U05-CH-005`; audio pendiente. | FA_19_MEDIA_AUDIO_VIDEO. | TEX 5.4; EP. | central |
| U05-021 | B02 · Herramientas de Fourier | explicación | Agregar componentes aproxima una forma no sinusoidal | La escala permanece fija para comparar la aproximación. | `U05-CH-005`. | FA_22_VISUAL_COMPLETO. | TEX fig. 5.2; PDF p. 124. | central |
| U05-022 | B02 · Herramientas de Fourier | formalización/ejemplo | La serie ubica componentes en múltiplos de `f_0` | La ecuación compacta una idea ya observada. | `U05-DG-003`, ecuación anotada. | FA_09_ECUACION_INTERPRETACION. | TEX 5.4.1, ec. 5.3. | ampliación |
| U05-023 | B02 · Herramientas de Fourier | explicación | Los coeficientes indican cuánto aporta cada componente | Se obtienen comparando la señal con seno y coseno durante un período. | `U05-DG-003`, variante dos ecuaciones. | FA_23_APENDICE. | TEX 5.4.1, ecs. 5.4–5.5. | ampliación |
| U05-024 | B02 · Herramientas de Fourier | formalización/ejemplo | Dos componentes, un período fundamental | Buscamos la repetición común, no el pico más alto. | `U05-DG-003`, variante ejemplo. | FA_10_EJEMPLO_RESUELTO. | TEX 5.4.2. | central |
| U05-025 | B02 · Herramientas de Fourier | pregunta/actividad | ¿Qué mejora al sumar más términos? | Observe tramos suaves y vecindades de discontinuidades. | `U05-CH-005` con tres regiones señaladas. | FA_14_PREGUNTA_EJERCICIO. | TEX ejercicio L2. | ampliación |
| U05-026 | B02 · Herramientas de Fourier | explicación | La transformada no exige repetición exacta | Serie y transformada responden a objetos ideales diferentes. | `U05-DG-003`, comparación serie/transformada. | FA_11_COMPARACION. | TEX 5.4.3. | ampliación |
| U05-027 | B02 · Herramientas de Fourier | formalización/ejemplo | La transformada compara la señal con cada frecuencia | La fórmula es referencia, no procedimiento de cálculo en esta unidad. | `U05-DG-003`, ecuación anotada. | FA_09_ECUACION_INTERPRETACION. | TEX 5.4.3, ec. 5.6; NOT. | ampliación |
| U05-028 | B02 · Herramientas de Fourier | formalización/ejemplo | Una transformada tiene magnitud y fase | Dos informaciones diferentes conservadas en una expresión. | `U05-DG-003`, variante polar. | FA_09_ECUACION_INTERPRETACION. | TEX 5.4.3, ec. 5.7. | ampliación |
| U05-029 | B02 · Herramientas de Fourier | recapitulación | Fourier cambia la representación, no la señal | Elegimos herramienta según el objeto. | `U05-DG-014`, recap 2. | FA_16_RECAP_PARCIAL. | TEX 5.4; BR. | central |
| U05-030 | B03 · Registro digital | divisor | De la señal continua a un registro digital | Entre el fenómeno y el gráfico hay decisiones de adquisición. | `U05-DG-004`, apertura. | FA_01_DIVISOR. | TEX 5.4.4; CM. | central |
| U05-031 | B03 · Registro digital | explicación | El micrófono no entrega una FFT | Transducción, muestreo y cálculo son operaciones distintas. | `U05-DG-004`, variante de cuatro etapas. | FA_12_PROCESO. | TEX 5.4.4 y 5.11; GLO. | central |
| U05-032 | B03 · Registro digital | explicación | Muestrear es observar la señal en instantes separados | La frecuencia de muestreo indica cuántas observaciones se realizan por segundo. | `U05-CH-006`, caso seguro. | FA_08_DEFINICION. | TEX 5.4.4; NOT; EP. | central |
| U05-033 | B03 · Registro digital | formalización/ejemplo | `N` muestras a `f_s` determinan la duración observada | Más muestras alargan el registro solo si `f_s` permanece fija. | `U05-DG-004`, ecuación y dos tiras temporales. | FA_09_ECUACION_INTERPRETACION. | TEX 5.4.4, ec. 5.8. | central |
| U05-034 | B03 · Registro digital | explicación | DFT y FFT no son sinónimos de “espectro” | Definición, algoritmo y gráfico ocupan niveles diferentes. | `U05-DG-004`, matriz conceptual. | FA_11_COMPARACION. | TEX 5.4.4; GLO. | ampliación |
| U05-035 | B03 · Registro digital | explicación | La DFT evalúa frecuencias discretas llamadas bins | Su separación depende del registro. | `U05-CH-007`. | FA_07_GRAFICO_EXPLICACION. | TEX 5.4.4 y 5.4.7; NOT. | ampliación |
| U05-036 | B03 · Registro digital | formalización/ejemplo | Observar más tiempo acerca los bins | La separación nominal mejora; la exactitud no está garantizada. | `U05-CH-007` con ecuación anotada por `U05-DG-004`. | FA_09_ECUACION_INTERPRETACION. | TEX 5.4.4, ec. 5.9. | central |
| U05-037 | B03 · Registro digital | formalización/ejemplo | De `f_s` y `N` a `T_obs` y `Δf` | Ejemplo resuelto con unidades. | `U05-DG-004`, ejemplo resuelto. | FA_10_EJEMPLO_RESUELTO. | TEX 5.4.6. | ampliación |
| U05-038 | B03 · Registro digital | pregunta/actividad | Si duplicamos `N`, ¿qué cambia realmente? | Mantenga `f_s` constante. | ecuaciones como pista, sin respuesta visible. | FA_14B_MINI_EJERCICIO. | TEX ejercicio D2. | ampliación |
| U05-039 | B03 · Registro digital | error frecuente | Más resolución no significa frecuencia exacta | La estimación también depende de señal, ruido y método. | `U05-DG-004`, variante error y condiciones. | FA_15_ERROR_FRECUENTE. | TEX 5.4.4 y 5.13. | ampliación |
| U05-040 | B03 · Registro digital | recapitulación | Hasta acá: registro, DFT, FFT y bins | Parámetros mínimos para interpretar un gráfico digital. | `U05-DG-014`, recap 3. | FA_16_RECAP_PARCIAL. | TEX 5.4.4; U05-031–039. | central |
| U05-041 | B04 · Ventanas y tiempo–frecuencia | divisor | El espectro depende del recorte temporal | Analizar un segmento implica seleccionar una parte del registro. | señal larga y segmento de `U05-CH-008`. | FA_01_DIVISOR. | TEX 5.4.5. | central |
| U05-042 | B04 · Ventanas y tiempo–frecuencia | explicación | Recortar una señal equivale a multiplicarla por una ventana | La ventana pondera qué parte del registro entra al análisis. | `U05-DG-005`, proceso de tres etapas. | FA_12_PROCESO. | TEX 5.4.5; EP. | central |
| U05-043 | B04 · Ventanas y tiempo–frecuencia | explicación | El mismo tono puede repartirse entre varios bins | La compatibilidad entre frecuencia, duración y ventana modifica el resultado. | `U05-CH-008`. | FA_07_GRAFICO_EXPLICACION. | TEX 5.4.5; EP. | ampliación |
| U05-044 | B04 · Ventanas y tiempo–frecuencia | explicación | Fuga espectral: distribución causada por el registro finito | No es una falla única del software. | detalle de `U05-CH-008` con callouts. | FA_08_DEFINICION. | TEX 5.4.5 y 5.13. | central |
| U05-045 | B04 · Ventanas y tiempo–frecuencia | explicación | Una ventana reduce lóbulos laterales y ensancha picos | Toda elección introduce un compromiso. | recurso CH-009 pendiente de cerrar fuente y normalización; usar esquema conceptual provisional. | FA_11_COMPARACION. | TEX 5.4.5; SciPy pendiente de verificación. | ampliación |
| U05-046 | B04 · Ventanas y tiempo–frecuencia | explicación | Ventanas cortas y largas responden preguntas diferentes | Resolución temporal y frecuencial compiten. | alternativa conceptual basada en TEX fig. 5.3; CH-010 vocal pendiente. | FA_22_VISUAL_COMPLETO. | TEX fig. 5.3; PDF p. 126. | ampliación |
| U05-047 | B04 · Ventanas y tiempo–frecuencia | explicación | Un espectrograma repite el análisis sobre segmentos sucesivos | Cada columna resume un espectro local. | `U05-DG-005`, variante proceso tiempo–frecuencia. | FA_12_PROCESO. | TEX 5.4.5; GLO. | central |
| U05-048 | B04 · Ventanas y tiempo–frecuencia | aplicación | Un espectrograma muestra cambios; no basta para diagnosticar | Una descripción acústica aislada no determina una condición clínica. | `context/libro_latex/figures/espectrograma.png`, figura del libro. | FA_13_APLICACION_CLINICA. | TEX 5.12; Brockmann2011. | central |
| U05-049 | B04 · Ventanas y tiempo–frecuencia | explicación | Un bin depende del registro; una banda depende de límites | Ambos ocupan frecuencia, pero no son el mismo objeto. | `U05-DG-005`. | FA_11_COMPARACION. | TEX 5.4.7; GLO. | ampliación |
| U05-050 | B04 · Ventanas y tiempo–frecuencia | formalización/ejemplo | Los niveles por banda no se promedian en dB | Primero se suman contribuciones compatibles en escala lineal. | `U05-DG-005`, variante lineal→nivel. | FA_09_ECUACION_INTERPRETACION. | TEX 5.4.7; PREV U4. | ampliación |
| U05-051 | B04 · Ventanas y tiempo–frecuencia | recapitulación | Hasta acá: duración, ventana, resolución y escala | Un espectro es inseparable de sus condiciones de análisis. | `U05-DG-014`, recap 4. | FA_16_RECAP_PARCIAL. | TEX 5.4.4–5.4.7; NOT. | central |
| U05-052 | B05 · Señal y sistema | divisor | Señal y sistema pueden compartir eje, pero no significado | ¿La curva describe contenido o transformación? | `U05-DG-006`. | FA_01_DIVISOR. | PO; TEX 5.5; CDM. | central |
| U05-053 | B05 · Señal y sistema | explicación | El espectro pertenece a un registro particular | Fuente, ambiente, sensor, segmento y método dejan huella. | `U05-DG-006`, variante señal y condiciones. | FA_08_DEFINICION. | TEX 5.5; GLO. | central |
| U05-054 | B05 · Señal y sistema | explicación | La respuesta en frecuencia pertenece a un sistema | Compara cómo cambia la salida respecto de la entrada. | `U05-DG-006`, variante sistema. | FA_08_DEFINICION. | PO; TEX 5.5; GLO. | ampliación |
| U05-055 | B05 · Señal y sistema | explicación | Espectro y respuesta se leen con preguntas diferentes | Curvas parecidas pueden responder preguntas incompatibles. | `U05-DG-006`, comparación simétrica. | FA_11_COMPARACION. | TEX 5.5; CDM. | central |
| U05-056 | B05 · Señal y sistema | explicación | Entrada, respuesta y salida forman una cadena | La salida combina contenido de entrada y transformación del sistema. | `U05-DG-006`. | FA_22_VISUAL_COMPLETO. | TEX fig. 5.4. | ampliación |
| U05-057 | B05 · Señal y sistema | formalización/ejemplo | `H(f)` compara salida y entrada cuando hay señal de prueba | La división requiere entrada no nula y condiciones compatibles. | `U05-DG-006`, ecuación anotada. | FA_09_ECUACION_INTERPRETACION. | TEX 5.5, ec. 5.12; NOT. | central |
| U05-058 | B05 · Señal y sistema | formalización/ejemplo | Una reducción de amplitud se expresa como ganancia negativa | Ejemplo en 1000 Hz. | `U05-DG-006`, ejemplo. | FA_10_EJEMPLO_RESUELTO. | TEX 5.5.1; NOT. | ampliación |
| U05-059 | B05 · Señal y sistema | formalización/ejemplo | Un retraso cambia fase sin cambiar magnitud | Magnitud plana no implica sistema transparente. | `U05-DG-006`, variante retardo. | FA_09_ECUACION_INTERPRETACION. | TEX 5.5, ec. 5.14. | ampliación |
| U05-060 | B05 · Señal y sistema | aplicación | En voz, armónicos de fuente y resonancias del tracto no son lo mismo | Modelo fuente–filtro introductorio. | `U05-DG-007`. | FA_13_APLICACION_CLINICA. | TEX 5.5 y 5.12; Brockmann2011. | ampliación |
| U05-061 | B05 · Señal y sistema | aplicación | La respuesta de un audífono no es el espectro de la voz | Dispositivo y señal son objetos diferentes. | `U05-DG-006`, aplicación a dispositivo. | FA_13_APLICACION_CLINICA. | TEX aplicación F3. | central |
| U05-062 | B05 · Señal y sistema | pregunta/actividad | Hasta acá: ¿señal, sistema o salida? | Clasifique el objeto antes de leer la curva. | `U05-DG-014`, recap 5. | FA_16_RECAP_PARCIAL. | TEX 5.5; CDM. | central |
| U05-063 | B06 · Componentes y terminología espectral | divisor | Nombrar componentes sin confundir periodicidad y amplitud | El pico más alto puede no ser la fundamental. | `U05-CH-011`, caso con segundo armónico dominante. | FA_01_DIVISOR. | PO; TEX 5.6. | central |
| U05-064 | B06 · Componentes y terminología espectral | explicación | La fundamental se obtiene de la periodicidad | Su línea puede ser pequeña o estar ausente. | `U05-DG-007`, relación tiempo–espectro. | FA_08_DEFINICION. | TEX 5.6; GLO. | central |
| U05-065 | B06 · Componentes y terminología espectral | explicación | Armónico, parcial y sobretono responden criterios distintos | Una componente puede recibir más de una etiqueta válida. | tabla nativa de cuatro filas. | FA_18_TABLA_DATOS. | TEX 5.6; GLO. | central |
| U05-066 | B06 · Componentes y terminología espectral | explicación | El segundo armónico puede ser el componente mayor | Altura de línea y orden armónico son propiedades diferentes. | panel de `U05-CH-011`. | FA_07_GRAFICO_EXPLICACION. | TEX fig. 5.5a. | central |
| U05-067 | B06 · Componentes y terminología espectral | explicación | La periodicidad puede persistir sin línea en `f_0` | El espaciado conserva información de la repetición. | panel de `U05-CH-011`. | FA_07_GRAFICO_EXPLICACION. | TEX 5.6; fig. 5.5c. | ampliación |
| U05-068 | B06 · Componentes y terminología espectral | explicación | No todo parcial cae en un múltiplo entero | Parcial es una categoría más amplia que armónico. | panel de `U05-CH-011`. | FA_07_GRAFICO_EXPLICACION. | TEX fig. 5.5b. | ampliación |
| U05-069 | B06 · Componentes y terminología espectral | error frecuente | El pico más alto no decide la fundamental | Use periodicidad y espaciado; no solo altura. | `U05-DG-007`, tres mini espectros. | FA_15_ERROR_FRECUENTE. | TEX 5.13; ejercicio D1. | ampliación |
| U05-070 | B06 · Componentes y terminología espectral | explicación | Un formante es una región de resonancia, no un armónico | Las líneas de fuente muestrean una envolvente del sistema vocal. | `U05-DG-007`. | FA_08_DEFINICION. | TEX 5.5; Brockmann2011. | ampliación |
| U05-071 | B06 · Componentes y terminología espectral | aplicación | En una vocal, líneas y envolvente cuentan historias diferentes | Periodicidad de fuente y resonancias del tracto se leen por separado. | alternativa conceptual; CH-012 pendiente de U05-MED-003. | FA_13_APLICACION_CLINICA. | TEX aplicación F1; Brockmann2011. | central |
| U05-072 | B06 · Componentes y terminología espectral | pregunta/actividad | ¿Fundamental, armónico, parcial, sobretono o formante? | Clasifique y justifique el criterio. | combinación simplificada de `U05-CH-011` y esquema vocal. | FA_14B_MINI_EJERCICIO. | TEX ejercicios C3, L4 y F1. | ampliación |
| U05-073 | B06 · Componentes y terminología espectral | recapitulación | Hasta acá: periodicidad, componentes y resonancias | Fuente y sistema aportan informaciones distintas. | `U05-DG-014`, recap 6. | FA_16_RECAP_PARCIAL. | TEX 5.5–5.6. | central |
| U05-074 | B07 · Rangos y límites | divisor | Los límites son convenciones bajo condiciones | Frecuencia y nivel participan en la detectabilidad. | `U05-CH-013`. | FA_01_DIVISOR. | PO; TEX 5.7. | central |
| U05-075 | B07 · Rangos y límites | explicación | `20 Hz` y `20 kHz` son fronteras aproximadas | Dependen de oyente, nivel, estímulo y condiciones. | `U05-CH-013`. | FA_07_GRAFICO_EXPLICACION. | TEX 5.7.1; Oxenham2018; ISO 226:2023. | central |
| U05-076 | B07 · Rangos y límites | explicación | Infrasonido no significa siempre imperceptible | La experiencia depende de más que la frecuencia. | esquema frecuencia–nivel conceptual. | FA_05_TEXTO_VISUAL_60_40. | TEX 5.7.1; Oxenham2018. | ampliación |
| U05-077 | B07 · Rangos y límites | explicación | El rango audible cambia con frecuencia, nivel y oyente | “Audible” describe una relación. | `U05-DG-008`. | FA_05_TEXTO_VISUAL_60_40. | TEX 5.7.1; CM U7. | central |
| U05-078 | B07 · Rangos y límites | aplicación | Ultrasonido nombra frecuencia, no una técnica única | La aplicación debe identificarse por procedimiento y propósito. | esquema propio; imagen externa solo después de curaduría. | FA_13_APLICACION_CLINICA. | TEX 5.7.1. | ampliación |
| U05-079 | B07 · Rangos y límites | formalización/ejemplo | Un rango dinámico compara dos niveles compatibles | Los extremos deben compartir magnitud, referencia y condición. | `U05-DG-008`, escala vertical. | FA_09_ECUACION_INTERPRETACION. | TEX 5.7.2, ec. 5.15; NOT. | ampliación |
| U05-080 | B07 · Rangos y límites | aplicación | El rango vocal depende de tarea y montaje | Ejemplo hipotético, no valor universal. | `U05-DG-008`, aplicación vocal. | FA_13_APLICACION_CLINICA. | TEX aplicación F5. | central |
| U05-081 | B07 · Rangos y límites | aplicación | Un instrumento tampoco tiene un único rango dinámico | Técnica, nota, sala y posición modifican los extremos. | esquema propio; recurso externo pendiente de curaduría. | FA_13_APLICACION_CLINICA. | PO; TEX 5.7.2; OD. | ampliación |
| U05-082 | B07 · Rangos y límites | error frecuente | El “umbral de dolor” no es un techo universal | El criterio superior debe definirse explícitamente. | `U05-DG-008`, límites condicionados. | FA_15_ERROR_FRECUENTE. | PO; TEX 5.7.2; OD-U05-07. | ampliación |
| U05-083 | B07 · Rangos y límites | recapitulación | Hasta acá: frecuencia, nivel y condición | Dos tipos de rango, dos preguntas distintas. | `U05-DG-014`, recap 7. | FA_16_RECAP_PARCIAL. | TEX 5.7. | central |
| U05-084 | B08 · Octavas y bandas | divisor | Dividir el espectro por razones, no por diferencias fijas | Una octava conserva la relación 2:1. | esquema conceptual de `U05-DG-009`; CH-014 normativo pendiente. | FA_01_DIVISOR. | PO; TEX 5.8. | central |
| U05-085 | B08 · Octavas y bandas | explicación | Agrupar frecuencias resume el espectro | Se conserva energía por intervalo y se pierde detalle fino. | `U05-CH-015`. | FA_07_GRAFICO_EXPLICACION. | TEX 5.4.7 y 5.8. | central |
| U05-086 | B08 · Octavas y bandas | formalización/ejemplo | Una octava cumple `f_H/f_L=2` | Las fracciones de octava conservan una razón general. | `U05-DG-009`. | FA_09_ECUACION_INTERPRETACION. | TEX 5.8, ec. 5.17. | ampliación |
| U05-087 | B08 · Octavas y bandas | explicación | Una serie armónica no avanza por octavas | Múltiplos enteros y razones 2:1 no son la misma regla. | `U05-DG-009`, comparación de rectas. | FA_11_COMPARACION. | PO; TEX 5.6 y 5.8; EP. | central |
| U05-088 | B08 · Octavas y bandas | formalización/ejemplo | El centro geométrico conserva simetría de razones | En bandas logarítmicas no usamos la media aritmética. | `U05-DG-009`, eje anotado. | FA_09_ECUACION_INTERPRETACION. | TEX 5.8, ec. 5.16. | ampliación |
| U05-089 | B08 · Octavas y bandas | formalización/ejemplo | Los límites se ubican simétricamente en escala logarítmica | El factor depende de cuántas bandas caben en una octava. | `U05-DG-009`, ecuaciones anotadas. | FA_09_ECUACION_INTERPRETACION. | TEX 5.8, ec. 5.18. | central |
| U05-090 | B08 · Octavas y bandas | formalización/ejemplo | El ancho en hertz es `B=f_H−f_L` | Igual ancho relativo produce mayor ancho absoluto a frecuencias altas. | `U05-DG-009`, comparación lineal. | FA_09_ECUACION_INTERPRETACION. | PO; TEX 5.8, ec. 5.19. | ampliación |
| U05-091 | B08 · Octavas y bandas | explicación | Tres tercios completan una octava | Igual longitud logarítmica; distinto ancho en hertz. | `U05-DG-009`; CH-014 queda pendiente de verificación IEC 61260-1. | FA_22_VISUAL_COMPLETO. | TEX fig. 5.6; IEC 61260-1 pendiente. | ampliación |
| U05-092 | B08 · Octavas y bandas | formalización/ejemplo | Tercio de octava centrado en `1000 Hz` | Cálculo exacto antes del redondeo nominal. | `U05-DG-009`, ejemplo resuelto. | FA_10_EJEMPLO_RESUELTO. | TEX 5.8.1; corrección documentada en storyboard. | central |
| U05-093 | B08 · Octavas y bandas | pregunta/actividad | ¿Qué banda tiene mayor ancho en hertz? | Compare octavas centradas en 500 y 2000 Hz. | `U05-DG-009`, dos bandas sin respuesta. | FA_14B_MINI_EJERCICIO. | TEX ejercicios G3/A2 adaptados. | ampliación |
| U05-094 | B08 · Octavas y bandas | recapitulación | Hasta acá: bin, banda, octava y tercio | Cuatro entidades que no deben confundirse. | `U05-DG-014`, recap 8. | FA_16_RECAP_PARCIAL. | TEX 5.4.7 y 5.8. | central |
| U05-095 | B09 · Filtros | divisor | Un filtro modifica componentes según frecuencia | Su respuesta define qué regiones conserva o atenúa. | `U05-CH-016`. | FA_01_DIVISOR. | PO; TEX 5.9. | central |
| U05-096 | B09 · Filtros | explicación | Un filtro se describe por respuesta, cortes y transición | Tipo y frecuencia de corte no alcanzan por sí solos. | `U05-DG-010`. | FA_08_DEFINICION. | TEX 5.9; GLO. | central |
| U05-097 | B09 · Filtros | explicación | Pasa bajos y pasa altos conservan regiones opuestas | Las dos respuestas comparten una frecuencia de corte declarada. | paneles superiores de `U05-CH-016`. | FA_11_COMPARACION. | TEX fig. 5.7a–b. | central |
| U05-098 | B09 · Filtros | explicación | Pasa banda y elimina banda usan dos límites | Entre `f_L` y `f_H`, una respuesta conserva y la otra atenúa. | paneles inferiores de `U05-CH-016`. | FA_11_COMPARACION. | TEX fig. 5.7c–d. | central |
| U05-099 | B09 · Filtros | explicación | Un filtro real no cambia de forma instantánea | El rectángulo ideal no es una especificación universal. | `U05-CH-016`. | FA_22_VISUAL_COMPLETO. | TEX fig. 5.7; script U5. | ampliación |
| U05-100 | B09 · Filtros | error frecuente | La frecuencia de corte requiere un criterio | `−3 dB` es frecuente, pero no universal. | `U05-DG-010`, curva anotada. | FA_15_ERROR_FRECUENTE. | TEX 5.9; GLO; OD-U05-23. | ampliación |
| U05-101 | B09 · Filtros | formalización/ejemplo | Un pasa banda se describe con límites, centro y ancho | Los mismos símbolos pueden describir una banda de análisis o un sistema. | `U05-DG-010`, ejemplo. | FA_10_EJEMPLO_RESUELTO. | TEX 5.9. | ampliación |
| U05-102 | B09 · Filtros | explicación | Escuchar qué conserva cada filtro | La escucha es demostración, no medición. | alternativa estática con `U05-CH-016`; audio pendiente. | FA_19_MEDIA_AUDIO_VIDEO. | TEX 5.9; EP. | ampliación |
| U05-103 | B09 · Filtros | pregunta/actividad | ¿Qué filtro representa cada curva? | Identifique paso, rechazo y transición. | `U05-CH-016`, versión ejercicio. | FA_14_PREGUNTA_EJERCICIO. | TEX ejercicio L5. | ampliación |
| U05-104 | B09 · Filtros | explicación | Filtrar, ponderar y filtrar un estímulo persiguen propósitos distintos | Operaciones semejantes; objetos y salidas diferentes. | `U05-DG-010`, tres procesos paralelos. | FA_06B_DOS_COLUMNAS. | TEX 5.9.1; GLO. | ampliación |
| U05-105 | B09 · Filtros | recapitulación | Hasta acá: tipo, límites, transición y propósito | Leer un filtro es leer un sistema. | `U05-DG-014`, recap 9. | FA_16_RECAP_PARCIAL. | TEX 5.9. | central |
| U05-106 | B10 · Ponderaciones | divisor | Ponderar es modificar la respuesta de medición | A, C y Z se aplican antes de informar un descriptor. | DG-011 pendiente de verificación normativa; usar cadena conceptual sin curvas. | FA_01_DIVISOR. | PO; TEX 5.10. | central |
| U05-107 | B10 · Ponderaciones | explicación | La misma señal produce resultados distintos según la ponderación | Cada respuesta corrige frecuencias de manera diferente. | DG-011 pendiente; alternativa conceptual de tres ramas. | FA_12_PROCESO. | TEX 5.10; EP. | central |
| U05-108 | B10 · Ponderaciones | explicación | A, C y Z no responden igual a todas las frecuencias | Curvas nominales; no bandas de tolerancia. | CH-017 pendiente; usar esquema no cuantitativo. | FA_22_VISUAL_COMPLETO. | TEX 5.10; IEC 61672-1 pendiente. | ampliación |
| U05-109 | B10 · Ponderaciones | explicación | La ponderación A es una respuesta normalizada de medición | `dB(A)` informa respuesta frecuencial, no toda la configuración. | cadena conceptual de DG-011, pendiente. | FA_08_DEFINICION. | PO; TEX 5.10; NOT; GLO. | central |
| U05-110 | B10 · Ponderaciones | formalización/ejemplo | Para un tono, la corrección se aplica en su frecuencia | Esta suma en dB representa una corrección de respuesta, no suma de fuentes. | ecuación conceptual; punto normativo pendiente. | FA_09_ECUACION_INTERPRETACION. | TEX 5.10, ec. 5.20; IEC 61672-1 pendiente. | central |
| U05-111 | B10 · Ponderaciones | formalización/ejemplo | Un tono de `63 Hz` cambia mucho entre Z y A | La corrección es puntual y depende de la frecuencia. | cálculo textual con condición de tono explícita. | FA_10_EJEMPLO_RESUELTO. | TEX 5.10.1; IEC 61672-1:2013. | central |
| U05-112 | B10 · Ponderaciones | error frecuente | Una corrección única no alcanza para un sonido de banda ancha | Ponderar exige corregir por frecuencia e integrar energéticamente. | DG-011 conceptual, pendiente de curvas. | FA_15_ERROR_FRECUENTE. | TEX 5.10; ejercicio G5. | ampliación |
| U05-113 | B10 · Ponderaciones | explicación | `dB(A)`, dB SPL, dB HL y sonoridad no son intercambiables | Magnitud, referencia y percepción responden a procedimientos distintos. | tabla nativa de cuatro filas. | FA_18_TABLA_DATOS. | TEX 5.9.1 y 5.12; NOT; GLO. | ampliación |
| U05-114 | B10 · Ponderaciones | pregunta/actividad | “72 dB(A)”: ¿qué sabemos y qué falta? | Auditar una lectura incompleta. | ficha conceptual de DG-011. | FA_14_PREGUNTA_EJERCICIO. | TEX ejercicios D4/F4. | ampliación |
| U05-115 | B10 · Ponderaciones | explicación | Curva nominal y tolerancia de instrumento no son lo mismo | Una respuesta objetivo no demuestra conformidad. | esquema no cuantitativo. | FA_23_APENDICE. | IEC 61672-1 pendiente; OD-U05-21. | ampliación |
| U05-116 | B10 · Ponderaciones | recapitulación | Hasta acá: filtro de medición, descriptor y límite | A/C/Z no completan por sí solas una lectura. | `U05-DG-014`, recap 10. | FA_16_RECAP_PARCIAL. | TEX 5.10. | central |
| U05-117 | B11 · Sonómetro y descriptores | divisor | Del micrófono al resultado informado | Un sonómetro procesa presión local bajo una configuración declarada. | `U05-DG-012`. | FA_01_DIVISOR. | PO; TEX 5.11; PREV. | central |
| U05-118 | B11 · Sonómetro y descriptores | explicación | Sonómetro, micrófono y calibrador cumplen funciones distintas | Reconocer componentes no demuestra clase ni conformidad. | imagen técnica pendiente de curaduría o esquema propio. | FA_06_VISUAL_TEXTO_40_60. | TEX 5.11.3. | central |
| U05-119 | B11 · Sonómetro y descriptores | explicación | La presión existe antes de que aparezca un número en pantalla | La cadena cambia representación, no el fenómeno ya ocurrido. | `U05-DG-012`. | FA_22_VISUAL_COMPLETO. | TEX fig. 5.8. | central |
| U05-120 | B11 · Sonómetro y descriptores | explicación | El nivel equivalente conserva la media cuadrática del intervalo | Un nivel constante equivalente representa la misma contribución energética media. | `U05-DG-012`, variante equivalente. | FA_08_DEFINICION. | TEX 5.11.1; GLO. | central |
| U05-121 | B11 · Sonómetro y descriptores | formalización/ejemplo | `70 dB` y `80 dB` no promedian `75 dB` | Para tiempos iguales, domina el tramo de mayor energía. | `U05-CH-018` con cálculo de `U05-DG-012`. | FA_10_EJEMPLO_RESUELTO. | TEX 5.11.4. | central |
| U05-122 | B11 · Sonómetro y descriptores | explicación | Equivalente, máximo y pico responden preguntas distintas | La misma señal alimenta descriptores diferentes. | `U05-DG-012`, tres ramas. | FA_11_COMPARACION. | TEX 5.11.1–5.11.2; NOT. | ampliación |
| U05-123 | B11 · Sonómetro y descriptores | aplicación | El ruido de fondo audiométrico no se verifica con un único dB(A) | El criterio depende de banda, transductor y propósito. | `U05-CH-019`. | FA_13_APLICACION_CLINICA. | TEX aplicación F2; ISO 8253-1/ANSI citadas solo como contexto. | central |
| U05-124 | B11 · Sonómetro y descriptores | recapitulación | Hasta acá: instrumento, configuración y resultado | Seis campos para que una lectura sea interpretable. | `U05-DG-014`, recap 11. | FA_16_RECAP_PARCIAL. | TEX 5.11–5.13. | central |
| U05-125 | B12 · Integración y cierre | aplicación | Una pregunta profesional determina la representación adecuada | Elegir la herramienta comienza por identificar el objeto. | `U05-DG-013`. | FA_13_APLICACION_CLINICA. | BR; TEX 5.12; EP. | central |
| U05-126 | B12 · Integración y cierre | pregunta/actividad | Caso integrador: vocal, espectro y dispositivo | Separe datos de señal, registro y sistema antes de calcular. | `U05-DG-013`, dos zonas señal/sistema. | FA_14_PREGUNTA_EJERCICIO. | TEX pregunta I1. | central |
| U05-127 | B12 · Integración y cierre | formalización/ejemplo | Resolver exige separar señal, sistema y condiciones | Una ruta de solución, no una repetición de todas las fórmulas. | `U05-DG-013`, solución por rutas. | FA_10_EJEMPLO_RESUELTO. | TEX solución I1. | central |
| U05-128 | B12 · Integración y cierre | error frecuente | Ocho atajos que cambian el significado | Corrija cada afirmación con una evidencia. | dos columnas editables; sin símbolos decorativos. | FA_15_ERROR_FRECUENTE. | TEX 5.13; BR. | central |
| U05-129 | B12 · Integración y cierre | recapitulación | De una señal registrada a una medición interpretable | Objeto, representación, método, parámetros y límites forman una cadena. | `U05-DG-001`, estado final. | FA_17_RECAP_FINAL. | PO; TEX 5.1–5.14; CM; CDM. | central |
| U05-130 | B12 · Integración y cierre | pregunta/actividad | ¿Qué podés explicar ahora que al inicio no podías? | Recuperación sin calificación punitiva. | tipografía y campos breves. | FA_14_PREGUNTA_EJERCICIO. | BR objetivos; U05-002–007. | central |
| U05-131 | B12 · Integración y cierre | explicación | El oído también responde de manera diferente según frecuencia | Puente a Unidad 6: un sistema biológico, no una FFT. | cadena conceptual de tres etapas. | FA_21_CIERRE_PUENTE. | CM U5→U6; CDM; TEX 6.1–6.2. | ampliación |
| U05-132 | B12 · Integración y cierre | explicación | Fuentes y recursos para continuar | Jerarquía y trazabilidad antes de ampliar. | tabla de referencias. | FA_20_BIBLIO_RECURSOS. | PO; `references.bib`; `source_analysis.md`. | central |
| U05-133 | B13 · Respaldo | explicación | Números complejos: una herramienta para magnitud y fase | Apoyo matemático a demanda. | plano complejo mínimo, editable. | FA_23_APENDICE. | TEX 5.4.3; NOT. | respaldo |
| U05-134 | B13 · Respaldo | explicación | Cómo se calculan `a_n` y `b_n` | Integrar la coincidencia con seno y coseno sobre un período. | ecuaciones anotadas y período resaltado. | FA_23_APENDICE. | TEX 5.4.1. | respaldo |
| U05-135 | B13 · Respaldo | explicación | Convención y unidades de la transformada | Las amplitudes absolutas dependen de definición y normalización. | par de ecuaciones y tabla de unidades. | FA_23_APENDICE. | TEX 5.4.3; NOT. | respaldo |
| U05-136 | B13 · Respaldo | explicación | DFT: índices, frecuencias y normalización | Referencia técnica reproducible. | ecuación anotada y eje de índices. | FA_23_APENDICE. | TEX 5.4.4; NOT; EP. | respaldo |
| U05-137 | B13 · Respaldo | explicación | Muestreo y aliasing: límite conceptual | Frecuencias continuas diferentes pueden compartir las mismas muestras. | `U05-CH-006`. | FA_23_APENDICE. | OD-U05-22; NOT; EP. | respaldo |
| U05-138 | B13 · Respaldo | explicación | Ventanas: ninguna gana en todos los criterios | Seleccionar según separación, rango dinámico y amplitud. | esquema conceptual hasta aprobar CH-009. | FA_23_APENDICE. | TEX 5.4.5; fuente SciPy pendiente. | respaldo |
| U05-139 | B13 · Respaldo | explicación | Sumar bins compatibles dentro de una banda | Dos contribuciones de 50 dB no producen 100 dB. | diagrama lineal→suma→nivel. | FA_23_APENDICE. | TEX ejercicio A3. | respaldo |
| U05-140 | B13 · Respaldo | explicación | Ganancia y fase de un dispositivo con retardo | Magnitud y fase describen aspectos diferentes. | ejemplo por pasos y señales desplazadas. | FA_23_APENDICE. | TEX ejercicio A5. | respaldo |
| U05-141 | B13 · Respaldo | explicación | Modelo fuente–filtro de voz: alcance y límites | La envolvente depende también de radiación, sensor y método. | `U05-DG-007`, versión ampliada dividida en dos filas. | FA_23_APENDICE. | TEX 5.5 y 5.12; Brockmann2011. | respaldo |
| U05-142 | B13 · Respaldo | explicación | Rangos dinámicos: qué debe declarar una fuente | Contrato de trazabilidad antes de incorporar cifras. | tabla nativa. | FA_23_APENDICE. | PO; TEX 5.7.2; OD-U05-06/07. | respaldo |
| U05-143 | B13 · Respaldo | explicación | Frecuencias centrales nominales requieren norma y edición | Cálculo exacto y serie nominal no son sinónimos. | tabla conceptual sin valores normativos definitivos. | FA_23_APENDICE. | TEX 5.8; IEC 61260-1 pendiente. | respaldo |
| U05-144 | B13 · Respaldo | explicación | Orden y pendiente de filtro cambian la transición | Dos filtros del mismo tipo pueden responder diferente. | detalle de `U05-CH-016` o variante reproducible. | FA_23_APENDICE. | TEX fig. 5.7; script U5; EP. | respaldo |
| U05-145 | B13 · Respaldo | explicación | Expresiones nominales de A, C y Z | Respaldo bloqueado hasta verificar IEC 61672-1. | placeholder textual, sin curva ni ecuación normativa. | FA_23_APENDICE. | IEC 61672-1 pendiente; OD-U05-12/21. | respaldo |
| U05-146 | B13 · Respaldo | explicación | Definición integral de `L_Xeq,T` | Formalización del promedio cuadrático durante un intervalo. | ecuación anotada y cadena de operaciones. | FA_23_APENDICE. | TEX 5.11.1, ec. 5.21; NOT. | respaldo |
| U05-147 | B13 · Respaldo | explicación | Fast, Slow, máximo y pico: referencias de diseño | Constantes orientativas no demuestran conformidad. | tabla nativa con advertencia. | FA_23_APENDICE. | TEX 5.11.2; IEC 61672-1/2. | respaldo |
| U05-148 | B13 · Respaldo | explicación | Evaluación de modelo, ensayo periódico y comprobación de campo | Tres procedimientos, tres alcances documentales. | tres procesos paralelos. | FA_23_APENDICE. | TEX 5.11.3; IEC 61672-2/3. | respaldo |
| U05-149 | B13 · Respaldo | explicación | Solución completa del caso integrador | Cada cálculo se asigna primero a señal o sistema. | `U05-DG-015`, solución por pasos. | FA_23_APENDICE. | TEX solución I1. | respaldo |
| U05-150 | B13 · Respaldo | explicación | Glosario de señales, espectro y medición | Consulta alfabética; no usar como cierre proyectado. | índice alfabético en dos columnas; dividir si no conserva 22 pt. | FA_23_APENDICE. | TEX 5.17; GLO. | respaldo |

## Cantidad y distribución

- **Total:** 150 slides.
- **Ruta central:** 77 slides; 384 min de exposición guiada estimada, sin contar pausas.
- **Ampliación:** 55 slides seleccionables según tiempo, equipamiento y nivel matemático.
- **Respaldo:** 18 slides de consulta o devolución.
- **Banco completo:** aproximadamente 768 min si se utilizara todo; no se recomienda proyectarlo de forma lineal.

| bloque | slides | cantidad | centrales | ampliación | respaldo | central estimada | banco completo |
|---|---|---:|---:|---:|---:|---:|---:|
| B00 | U05-001–007 | 7 | 6 | 1 | 0 | 24 min | 27 min |
| B01 | U05-008–017 | 10 | 5 | 5 | 0 | 20 min | 44 min |
| B02 | U05-018–029 | 12 | 6 | 6 | 0 | 28 min | 59 min |
| B03 | U05-030–040 | 11 | 6 | 5 | 0 | 29 min | 54 min |
| B04 | U05-041–051 | 11 | 6 | 5 | 0 | 28 min | 56 min |
| B05 | U05-052–062 | 11 | 6 | 5 | 0 | 30 min | 58 min |
| B06 | U05-063–073 | 11 | 6 | 5 | 0 | 29 min | 57 min |
| B07 | U05-074–083 | 10 | 5 | 5 | 0 | 23 min | 48 min |
| B08 | U05-084–094 | 11 | 6 | 5 | 0 | 33 min | 61 min |
| B09 | U05-095–105 | 11 | 5 | 6 | 0 | 22 min | 56 min |
| B10 | U05-106–116 | 11 | 6 | 5 | 0 | 28 min | 55 min |
| B11 | U05-117–124 | 8 | 7 | 1 | 0 | 40 min | 46 min |
| B12 | U05-125–132 | 8 | 7 | 1 | 0 | 50 min | 53 min |
| B13 | U05-133–150 | 18 | 0 | 0 | 18 | 0 min | 94 min a demanda |
| **Total** | **U05-001–150** | **150** | **77** | **55** | **18** | **384 min** | **768 min** |

### Distribución sugerida de la ruta central

1. **Encuentro 1 — B00–B02:** orientación, representaciones y Fourier intuitivo; 55–65 min.
2. **Encuentro 2 — B03–B04:** registro digital, muestreo, ventanas y espectrograma; 55–65 min.
3. **Encuentro 3 — B05–B06:** señal/sistema y terminología espectral; 55–65 min.
4. **Encuentro 4 — B07–B08:** rangos, bandas, octavas y tercios; 55–65 min.
5. **Encuentro 5 — B09–B10:** filtros, ponderaciones y descriptores; 55–65 min.
6. **Encuentro 6 — B11–B12:** sonómetro, nivel equivalente, aplicaciones y caso integrador; 60–70 min.

## Decisiones pedagógicas de cierre

- La etiqueta de ruta es visible en las 150 slides: CENTRAL, AMPLIACIÓN o RESPALDO.
- U05-032 y U05-048 son centrales porque sostienen muestreo y lectura tiempo–frecuencia.
- U05-120 es central y precede al ejemplo U05-121; la integral se conserva en U05-146 como respaldo.
- U05-023, forma compleja y DFT formal no son requisito de la ruta central.
- El caso U05-126/127 contiene datos y resultados verificables; U05-149 conserva la devolución completa.
- Las recapitulaciones recuperan relaciones, no copian listas de títulos.

## Riesgos y controles

| severidad | riesgo | control |
|---|---|---|
| alta | Fatiga por un banco de 150 slides | Ruta central explícita de 77 slides en seis encuentros; ampliación y respaldo no se proyectan por defecto. |
| alta | Serie, transformada, DFT y FFT como sinónimos | Comparaciones y recapitulaciones distinguen objeto, operación y resultado. |
| alta | Espectro confundido con respuesta de sistema | B05 y caso integrador separan señal, sistema y salida. |
| alta | Pico mayor confundido con `f_0` | Contraejemplos y caso final separan periodicidad y envolvente. |
| alta | Ponderación A confundida con audición | Se presenta como filtro de medición y se limita el ejemplo tonal. |
| alta | `L_eq` calculado como promedio aritmético de dB | Intuición cuadrática en U05-120, ejemplo energético en U05-121 e integral en respaldo. |
| media | Formalismo sin intuición | Integrales y forma compleja quedan fuera de la ruta central. |
| media | Inferencia clínica a partir de un espectrograma aislado | U05-048 usa señal sintética y una consigna descriptiva explícita. |

## Estado

Storyboard alineado con la versión final del deck. Toda slide tiene bloque, función, visual/layout, fuente y ruta asignados.
