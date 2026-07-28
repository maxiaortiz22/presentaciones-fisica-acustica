# Mapa global del curso de Física Acústica

Estado: arquitectura curricular inicial.  
Fecha: 28 de julio de 2026.

## Fuentes y criterio

Este mapa aplica la jerarquía de `AGENTS.md`:

1. `context/programa/Programa de Física Acústica.pdf` — alcance obligatorio, programa 2025, pp. 3–5.
2. `context/libro_latex/main.tex` y `context/libro_latex/chapters/*.tex` — fuente estructural y editable.
3. `context/libro_pdf/Física Acústica para Fonoaudiología.pdf` — edición 2026, 296 páginas, verificada visualmente en su totalidad.
4. `context/libro_latex/bibliography/references.bib` — bibliografía técnica, científica y normativa.
5. Ejercicios, respuestas, glosarios, figuras TikZ y gráficos reproducibles integrados en el libro.

No se localizaron guías de ejercicios, parciales, recuperatorios ni cuestionarios independientes. El libro sí contiene, en todas las unidades, preguntas conceptuales, interpretación de gráficos, ejercicios numéricos guiados y autónomos, aplicaciones fonoaudiológicas, una pregunta integradora, distractores y soluciones u orientaciones.

## Propósito general

Construir una base física y matemática que permita describir la producción, propagación, medición y percepción del sonido; interpretar señales, instrumentos y sistemas auditivos; y relacionar esos modelos con problemas de Fonoaudiología sin confundir magnitudes físicas, experiencias perceptuales y conclusiones clínicas.

El curso debe permitir que el estudiante:

- identifique qué fenómeno o sistema se analiza;
- seleccione magnitudes, unidades y representaciones adecuadas;
- interprete ecuaciones y gráficos con sus hipótesis;
- conecte mecanismos físicos con audición, voz, ambientes y dispositivos;
- reconozca cuándo una conclusión exige medición, norma, protocolo o evaluación profesional adicional.

## Perfil del estudiante

Estudiantes de primer año de Fonoaudiología, con conocimientos potencialmente heterogéneos de álgebra, trigonometría, gráficos, física, procesamiento de señales y anatomía auditiva. No se presupone cálculo diferencial. Las razones de cambio, integrales y promedios deben introducirse mediante significado físico antes de su formalización.

## Vista global

| Unidad | Función en el curso | Profundidad esperada | Carga | Aplicaciones principales | Alerta central |
|---|---|---|---|---|---|
| 1 | Lenguaje físico y matemático común | Operativa e introductoria | Alta | Audiometría, voz, medición, dispositivos | No confundir magnitud, unidad y percepción. |
| 2 | Base mecánica y energética | Modelos unidimensionales y balances | Alta | Tímpano, cadena osicular, vibrador óseo, tejidos | Mecánica y termodinámica compiten por tiempo. |
| 3 | Paso de oscilación a onda | Formalización algebraico-trigonométrica | Alta | Tonos, registros temporales, parlante | Distinguir tiempo, espacio y propagación. |
| 4 | Magnitudes y niveles acústicos | Cuantitativa, con condiciones de validez | Muy alta | Micrófonos, dB SPL, campo sonoro, distancia | Unidad bisagra y de máxima densidad. |
| 5 | Descripción frecuencial y medición | Conceptual y computacional introductoria | Muy alta | Voz, filtros, audífonos, sonometría | Separar señal, sistema, banda y medición. |
| 6 | Mecanismo auditivo periférico | Físico-funcional, no diagnóstico | Muy alta | Oído externo, medio, cóclea, OEA, PEAT | Anatomía, mecánica y electrofisiología simultáneas. |
| 7 | Psicoacústica | Psicofísica introductoria con modelos acotados | Muy alta | Umbrales, inteligibilidad, localización, enmascaramiento | No convertir relaciones perceptuales en equivalencias universales. |
| 8 | Alteraciones, estudios y rehabilitación | Comparativa e introductoria | Muy alta | Evaluación auditiva, audífonos, implantes | Evitar diagnóstico a partir de un dato aislado. |
| 9 | Propagación real, recintos y cabinas | Aplicación de modelos previos | Alta | Campo sonoro, cabinas, aislamiento | Normas y valores no son universales. |
| 10 | Caracterización y control del ruido | Integración temporal, frecuencial y contextual | Alta | Ruido de prueba, SNR, exposición, control | El enmascaramiento clínico solo se introduce. |

## Temas que atraviesan varias unidades

| Tema | Introducción | Formalización | Reutilización intencional |
|---|---|---|---|
| Magnitudes, unidades y referencias | U1 | U4 | U5, U8, U9, U10 |
| Funciones y logaritmos | U1 | U4–U5 | U7–U10 |
| Fuerza, energía, elasticidad y amortiguamiento | U2 | U3–U4 | U6, U9 |
| Frecuencia, período, fase y longitud de onda | U3 | U3 | U4–U7, U9–U10 |
| Velocidad de partícula y propagación | U3 | U4 | U6, U9 |
| Decibel y niveles | U1, como anticipo | U4 | U5, U7–U10 |
| Espectro y respuesta en frecuencia | U5 | U5 | U6–U8, U10 |
| Impedancia | U4 | U4 | U6 |
| Magnitud física y atributo perceptual | U1 | U7 | U3–U8, U10 |
| Ruido y relación señal–ruido | U7 | U10 | U8–U10 |
| Enmascaramiento | U7 | U7 | U10, aplicación audiométrica introductoria |
| Reflexión y reverberación | U4 | U9 | U7, U10 |
| Calibración y escalas dB SPL/HL/SL | U1, anticipo | U4 y U8 | U5–U10 |

## Unidad 1 — Nociones básicas e introducción a la acústica

### Alcance obligatorio del programa

Acústica y aplicaciones en Audiología; Sistema Internacional; velocidad, distancia, masa, peso, tiempo, presión, densidad y fuerza; función y función inversa; seno, coseno y tangente; exponencial y logaritmo.

### Objetivos y profundidad

El objetivo explícito es establecer el lenguaje que se utilizará en el curso. Implícitamente, debe reducir la ansiedad matemática y enseñar a leer una ecuación como una relación entre magnitudes. La profundidad esperada es operativa: conversiones, sustitución, interpretación de gráficos sencillos y coherencia dimensional, sin cálculo diferencial.

El libro cubre todo el programa y añade aceleración, notación científica, análisis dimensional, un anticipo del decibel y la distinción entre magnitud física y atributo perceptual.

### Resultados de aprendizaje

Al finalizar, el estudiante podrá:

1. definir acústica y representar un fenómeno mediante fuente, medio y receptor;
2. reconocer magnitudes fundamentales y derivadas y expresar resultados con unidades SI;
3. diferenciar masa de peso y relacionar distancia, tiempo, velocidad, aceleración, fuerza, presión y densidad;
4. interpretar funciones directas e inversas sin confundir inversa con recíproco;
5. aplicar razones trigonométricas, exponenciales y logaritmos en ejemplos sencillos;
6. comprobar la consistencia dimensional y distinguir una medida física de un atributo perceptual.

### Continuidad

| Aspecto | Decisión |
|---|---|
| Conocimientos previos | Aritmética, fracciones, potencias y ecuaciones de un paso. |
| Conexión anterior | Inicio del curso. Partir de voz–aire–micrófono–oyente. |
| Prepara | Fuerza y energía en U2; senoides y fase en U3; decibeles en U4. |
| Notación | \(d,t,m,F,p,\rho,f\); SI; coma decimal; espacio entre valor y unidad. |
| Visual reutilizable | Fuente–medio–receptor; mapa de dependencias dimensionales; escala lineal/logarítmica. |
| Aplicación | Audiometría, registro de voz, entrada/salida de dispositivos y condiciones de medición. |

## Unidad 2 — Leyes de la mecánica clásica y de la termodinámica

### Alcance obligatorio del programa

Leyes de Newton; calor; entropía; conservación de la energía.

### Objetivos y profundidad

Debe permitir analizar fuerzas y balances energéticos en sistemas sencillos. El libro amplía el programa con presión sobre superficies, masa–resorte–amortiguador, trabajo, energía cinética y elástica, energía interna, primera ley y dependencia de la velocidad del sonido con la temperatura.

La profundidad apropiada es de modelos unidimensionales y balances cualitativos o algebraicos. No corresponde desarrollar termodinámica formal completa.

### Resultados de aprendizaje

1. interpretar las tres leyes de Newton identificando sistema y fuerza neta;
2. calcular aceleración, fuerza o masa en modelos unidimensionales;
3. explicar el papel de masa, rigidez y amortiguamiento;
4. comparar energía cinética, potencial, transferencia y disipación;
5. diferenciar temperatura, calor, energía interna y entropía;
6. aplicar balances mecánicos y energéticos a sistemas acústicos y auditivos simples.

### Continuidad

| Aspecto | Decisión |
|---|---|
| Conocimientos previos | U1: masa, aceleración, fuerza, presión, unidades y análisis dimensional. |
| Conexión anterior | Pasar de “qué se mide” a “qué cambia el movimiento y la energía”. |
| Prepara | Osciladores en U3; elasticidad e intensidad en U4; oído medio en U6. |
| Notación | \(\sum F, m, a, k, x, E_k, E_p, U, Q_\mathrm{calor}, W_\mathrm{trabajo}, S\). |
| Visual reutilizable | Diagrama de cuerpo libre; masa–resorte–amortiguador; balance de energía. |
| Aplicación | Tímpano, cadena osicular, vibrador óseo, viscoelasticidad y propagación en aire. |

## Unidad 3 — Fundamentos de la mecánica ondulatoria

### Alcance obligatorio del programa

Movimiento oscilatorio y ondulatorio; movimiento armónico simple; tono puro en un parlante, definición y expresión matemática; frecuencia, período, amplitud, fase y longitud de onda.

### Objetivos y profundidad

Debe separar oscilación local, representación sinusoidal y propagación. El libro cubre todo el programa y añade posición, velocidad y aceleración, frecuencia angular, número de onda, lectura temporal y espacial, velocidad de partícula, superposición e interferencia.

La profundidad esperada es algebraico-trigonométrica: leer y calcular parámetros, no derivar ecuaciones de onda.

### Resultados de aprendizaje

1. diferenciar movimiento oscilatorio de movimiento ondulatorio;
2. representar un MAS y relacionar posición, velocidad y aceleración;
3. calcular \(T\), \(f\), \(\omega\), \(\lambda\), \(k\) y \(c\) con unidades;
4. interpretar amplitud, fase inicial y diferencia de fase;
5. comparar una gráfica temporal con una representación espacial;
6. aplicar superposición a interferencia constructiva, parcial y destructiva.

### Continuidad

| Aspecto | Decisión |
|---|---|
| Conocimientos previos | U1: seno, coseno, radianes y funciones; U2: equilibrio, inercia y fuerza restauradora. |
| Conexión anterior | El sistema masa–resorte pasa de balance mecánico a oscilación. |
| Prepara | Magnitudes acústicas de U4 y análisis de Fourier de U5. |
| Notación | \(x(t),A,f,T,\omega,\varphi_0,\Delta\varphi,\lambda,k,c,u\). |
| Visual reutilizable | MAS en tres curvas; onda en tiempo/espacio; parlante–medio; superposición. |
| Aplicación | Tonos audiométricos, registros temporales y generación sonora. |

## Unidad 4 — Generalidades sobre el sonido, sus propiedades y magnitudes

### Alcance obligatorio del programa

Naturaleza y definiciones física/psicoacústica; generación; elasticidad; propiedades y velocidad de la onda; reflexión e impedancia; campo acústico; ondas esféricas y cilíndricas; tono puro, RMS, promedio y señales complejas; presión sonora; decibel, percepción, fuentes coherentes/no coherentes y suma energética; referencias en aire y agua; nivel de presión sonora; campo libre omnidireccional; ley del cuadrado inverso; \(Q\), factor e índice de directividad; nivel en función de distancia.

### Objetivos y profundidad

Es la unidad física central del curso. El libro cubre el alcance completo y lo amplía con velocidad de partícula, intensidad, potencia, energía, valores de pico/pico a pico, niveles de intensidad y potencia, correlación parcial, onda plana, campo reverberante y condiciones de validez.

La profundidad debe incluir cálculos sencillos y análisis de hipótesis. No conviene impartirla como un bloque único.

### Resultados de aprendizaje

1. diferenciar presión, velocidad de partícula, intensidad, potencia y energía;
2. explicar impedancia y reflexión en una interfaz;
3. calcular valores pico, medio y RMS de señales simples;
4. calcular e interpretar niveles de presión sonora con referencia explícita;
5. sumar señales coherentes y niveles no correlacionados;
6. aplicar ley del cuadrado inverso, \(Q\) y \(DI\) declarando condiciones de validez.

### Continuidad

| Aspecto | Decisión |
|---|---|
| Conocimientos previos | U2: fuerza, energía, elasticidad; U3: onda, fase, superposición y \(c=\lambda f\). |
| Conexión anterior | La onda deja de ser solo geometría y pasa a describirse con magnitudes medibles. |
| Prepara | Espectros y sonometría en U5; oído medio en U6; psicoacústica en U7; propagación en U9. |
| Notación | \(p,u,Z,I,W,E_\mathrm{ac},p_\mathrm{rms},L_p,L_I,L_W,p_\mathrm{ref},Q,DI,r\). |
| Visual reutilizable | Presión–velocidad–intensidad; RMS; escala presión/dB; suma; propagación esférica; directividad. |
| Aplicación | Micrófonos, dB SPL, campo sonoro, calibración, distancia y transductores. |

### Estrategia de carga

Dividir en: fenómeno/medio; magnitudes; valores de señal; niveles; suma; geometría/distancia/directividad. Insertar recapitulaciones después de magnitudes, niveles y propagación.

## Unidad 5 — Análisis frecuencial de señales acústicas

### Alcance obligatorio del programa

Series y transformada de Fourier; respuesta en frecuencia y espectro; infrasonido, audible y ultrasonido; rangos dinámicos vocal, instrumental y auditivo; umbral de dolor; fundamental, armónico, parcial y sobretono; octavas y bandas; filtros, frecuencias límite/central y ancho de banda; ponderación A/dBA; medidor de nivel de presión sonora.

### Objetivos y profundidad

El libro cubre todo el alcance y amplía con fase espectral, DFT/FFT, muestreo, ventanas, espectrograma, fuga, resolución, respuesta entrada–salida, formantes, tercios de octava, ponderaciones A/C/Z, nivel equivalente, máximo/pico y verificación instrumental.

Los rangos dinámicos y el umbral de dolor se presentan correctamente como dependientes de condiciones, no como cifras universales.

### Resultados de aprendizaje

1. comparar representaciones temporal, espectral y tiempo–frecuencia;
2. explicar serie, transformada, DFT y FFT sin atribuirles creación de componentes;
3. diferenciar espectro de señal y respuesta en frecuencia de sistema;
4. distinguir fundamental, armónico, parcial, sobretono y formante;
5. calcular resolución, límites, centro y ancho de bandas;
6. interpretar filtros, ponderaciones y descriptores básicos de un sonómetro.

### Continuidad

| Aspecto | Decisión |
|---|---|
| Conocimientos previos | U3: senoides, período, fase y superposición; U4: presión, RMS y niveles. |
| Conexión anterior | Una señal compleja medida en U4 se descompone y se compara con sistemas. |
| Prepara | Respuesta del oído en U6, timbre y filtros auditivos en U7, estudios/dispositivos en U8 y ruido en U10. |
| Notación | \(p(t),P(f),X(f),H(f),f_s,N,\Delta f,T_\mathrm{obs},f_0,f_c,f_L,f_H,B,L_{A\mathrm{eq},T}\). |
| Visual reutilizable | Tiempo–magnitud–fase; Fourier progresivo; espectrograma; señal vs respuesta; bandas; filtros; sonómetro. |
| Aplicación | Voz, formantes, audífonos, estímulos audiométricos, medición ambiental. |

### Estrategia de carga

Separar: dominios; Fourier; digitalización; señal vs sistema; componentes/rangos; bandas/filtros; ponderaciones/sonómetro. Usar datos sintéticos controlados y ejercicios de lectura antes de fórmulas.

## Unidad 6 — El mecanismo de la percepción auditiva

### Alcance obligatorio del programa

Oído como transductor acústico–mecánico–eléctrico; oído externo, medio e interno; pabellón, CAE y tímpano; frente de onda; caja timpánica, trompa, huesecillos y ventana oval; fuerza/desplazamiento y transformador mecánico; cadena osicular, reflejo estapedial y latencia; igualación de presión e impedancias; conducción ósea; cóclea, fluidos, rampas y membranas; ventanas; órgano y túnel de Corti; CCI/CCE; señales débiles/intensas; transducción y tonotopía.

### Objetivos y profundidad

El libro reorganiza el listado anatómico como una cadena funcional. Cubre casi todo con mayor precisión: rechaza una conversión geométrica literal esférica–cilíndrica en el CAE, presenta conducción ósea como multimecanismo y evita umbrales o latencias universales del reflejo.

Quedan dos puntos a explicitar: el término anatómico “túnel de Corti” no aparece y el “potencial de reposo” se aborda indirectamente mediante potencial eléctrico endolinfático y potencial de membrana.

### Resultados de aprendizaje

1. ordenar las etapas acústica, mecánica, hidromecánica, celular y neural;
2. explicar las funciones del oído externo y la dependencia espacial de la presión en el CAE;
3. relacionar áreas, fuerzas, presiones y desplazamientos en el oído medio;
4. describir la cóclea, las ventanas, rampas, fluidos y membranas;
5. explicar onda viajera, tonotopía y dependencia con el nivel;
6. diferenciar CCI, CCE y secuencia de transducción mecanoeléctrica.

### Continuidad

| Aspecto | Decisión |
|---|---|
| Conocimientos previos | U2: mecánica; U3: ondas; U4: presión e impedancia; U5: respuesta en frecuencia. |
| Conexión anterior | La señal y el sistema físico se aplican a una cadena biológica real. |
| Prepara | Atributos perceptuales en U7 y estudios/dispositivos en U8. |
| Notación | \(p,F,A,R_A,R_L,R_p,f_\mathrm{res},\lambda,c\); CCI, CCE, CAE. |
| Visual reutilizable | Cadena de transducción; oído periférico; adaptación; cóclea; onda viajera; CCI/CCE. |
| Aplicación | Medición en CAE, vía aérea/ósea, OEA y potenciales evocados. |

### Estrategia de carga

Trabajar cinco cadenas breves: externo; medio; conducción ósea; cóclea; órgano de Corti/transducción. Cada cadena debe cerrar con “entrada–transformación–salida–qué no permite concluir”.

## Unidad 7 — Características subjetivas y psicoacústica

### Alcance obligatorio del programa

Curvas isofónicas normalizadas; umbral absoluto/audibilidad y máxima sensibilidad; resonancia del CAE y diferencia campo–tímpano; pitch, duración, timbre y sonoridad; nivel de sonoridad, SPL, fones y sones; enmascaramiento; ruido, reverberación y tiempo de reverberación; voz e inteligibilidad; pérdida de articulación; efecto Haas; sonido reflejado; efecto cocktail party; localización, audición binaural, ITD e ILD.

### Objetivos y profundidad

El libro cubre el alcance y añade filtros auditivos, ERB, enmascaramiento temporal, energético/informacional, SNR, pistas espectrales y movimiento de cabeza. Corrige “Hass” a “Haas” y diferencia el resultado histórico de la familia de fenómenos de precedencia.

Las curvas isofónicas numéricas normalizadas requieren datos de la edición aplicable de ISO 226; la figura actual es conceptual. El tiempo de reverberación se usa aquí como descriptor y se formaliza en U9.

### Resultados de aprendizaje

1. diferenciar pares físico–perceptuales: frecuencia/pitch, nivel/sonoridad, espectro/timbre y duración física/percibida;
2. interpretar umbrales y curvas isofónicas bajo condiciones declaradas;
3. comparar fones, sones y dB SPL sin tratarlos como equivalentes;
4. explicar enmascaramiento simultáneo, temporal, energético e informacional;
5. relacionar SNR y reverberación con inteligibilidad sin usar una fórmula universal;
6. integrar ITD, ILD, pistas espectrales y atención en escenas espaciales y concurrentes.

### Continuidad

| Aspecto | Decisión |
|---|---|
| Conocimientos previos | U4: campo y niveles; U5: espectro; U6: transferencia y codificación periférica. |
| Conexión anterior | De la representación neural inicial a la experiencia y la tarea de escucha. |
| Prepara | Estudios y rehabilitación en U8; recintos en U9; ruido y enmascaramiento aplicado en U10. |
| Notación | \(L_p,L_N,N,\mathrm{ERB},\mathrm{SNR},\mathrm{ALCons},\mathrm{ITD},\mathrm{ILD},\Delta t\). |
| Visual reutilizable | Campo audible; isofónicas; fones/sones; enmascaramiento; precedencia; ITD/ILD; fuentes concurrentes. |
| Aplicación | Audiometría, logoaudiometría, inteligibilidad, dispositivos y orientación espacial. |

### Estrategia de carga

Usar ciclos repetidos: estímulo físico → tarea → respuesta → límite del modelo. Separar umbral/sonoridad, enmascaramiento/inteligibilidad y espacio/escenas concurrentes.

## Unidad 8 — Enfermedades, estudios y rehabilitación

### Alcance obligatorio del programa

Curvas de recuperación después de exposición; TTS; pérdida auditiva inducida por ruido; tinnitus; presbiacusia; riesgo porcentual por ruido ocupacional y edad; audiometría, logoaudiometría, timpanometría, acufenometría, PEAT, OEA y electrococleografía; audífonos e implantes cocleares.

### Objetivos y profundidad

El libro cubre las alteraciones, pruebas y dispositivos mediante un marco comparativo y añade trauma acústico, ototoxicidad, conducción ósea y estimulación electroacústica. Evita convertir patrones en diagnósticos.

Son parciales las curvas de recuperación pos-exposición y el riesgo porcentual por edad: se explican dependencias y límites, pero no se presentan curvas epidemiológicas ni porcentajes. Requieren fuente primaria, contexto poblacional y decisión docente.

### Resultados de aprendizaje

1. diferenciar exposición, alteración, síntoma y resultado;
2. explicar TTS, PAIR, tinnitus, presbiacusia, trauma y ototoxicidad con alcance introductorio;
3. comparar estudios según estímulo, magnitud, sistema, respuesta y limitaciones;
4. interpretar audiogramas, curvas logoaudiométricas y timpanogramas conceptuales;
5. comparar audífono, implante coclear y conducción ósea por su transformación física;
6. reconocer por qué una batería de pruebas y un protocolo son necesarios para una conclusión clínica.

### Continuidad

| Aspecto | Decisión |
|---|---|
| Conocimientos previos | U4: escalas; U5: señal/sistema; U6: vías y transducción; U7: umbral y percepción. |
| Conexión anterior | Los mecanismos y atributos se convierten en preguntas de evaluación e intervención. |
| Prepara | Exposición, ruido y enmascaramiento de U10. |
| Notación | dB SPL, dB HL, dB SL, TTS, PAIR/NIHL, OEA, PEAT, \(L_{A\mathrm{eq},T}\). |
| Visual reutilizable | Cadena de prueba; audiograma; logoaudiometría; timpanogramas; OEA/PEAT; dispositivos. |
| Aplicación | Núcleo profesional de Audiología y rehabilitación. |

## Unidad 9 — Factores que afectan la propagación

### Alcance obligatorio del programa

Distancia; direccionalidad; temperatura, viento y presión atmosférica; superficies, reflexión, absorción, refracción en sólidos y atmósfera; difracción y longitud de onda; aislamiento e insonorización; cabinas, ley de masas y ruido máximo permitido para audiometrías.

### Objetivos y profundidad

El libro cubre todo el alcance, incluida refracción en interfaces fluido–sólido, y amplía con absorción atmosférica, transmisión, reverberación, Sabine, acondicionamiento y rutas laterales. La profundidad es de estimación y reconocimiento de mecanismos, no diseño profesional.

Los valores de ruido permitido deben obtenerse de normas vigentes según vía, transductor, bandas, menor nivel de prueba y jurisdicción.

### Resultados de aprendizaje

1. aplicar el cambio de nivel con distancia y directividad;
2. explicar efectos de gradientes térmicos y de viento;
3. diferenciar reflexión, absorción, transmisión, refracción y difracción;
4. calcular estimaciones sencillas de reverberación y ley de masas;
5. comparar acondicionamiento, aislamiento e insonorización;
6. justificar una verificación por bandas de una cabina audiométrica.

### Continuidad

| Aspecto | Decisión |
|---|---|
| Conocimientos previos | U2: temperatura; U3: \(\lambda\); U4: campo/distancia/directividad; U5: bandas; U7: sonoridad. |
| Conexión anterior | Los estímulos y pruebas de U8 dependen del ambiente físico. |
| Prepara | Control de ruido de U10. |
| Notación | \(r,Q,DI,c,\lambda,\alpha,A,T_{60},\tau,TL\). |
| Visual reutilizable | Gradientes; balance en superficie; reverberación; barrera; ley de masas; cabina. |
| Aplicación | Campo sonoro, cabinas, ambientes de voz y medición ambiental. |

## Unidad 10 — Ruidos

### Alcance obligatorio del programa

Tipos y clasificación; diferencia ruido/sonido; ruido aleatorio; blanco, rosa, vocal y NBN; revisión del enmascaramiento.

### Objetivos y profundidad

El libro cubre y amplía fuertemente el programa con estacionariedad, clasificaciones temporales, estadística, densidad espectral, métricas de exposición, SNR, ruido de fondo y control fuente–trayecto–receptor.

“Ruido vocal” se precisa como ruido con forma espectral vocal. La técnica clínica de enmascaramiento solo se presenta de manera funcional; criterios de plateau, niveles iniciales y procedimientos quedan fuera y requieren protocolo específico.

### Resultados de aprendizaje

1. diferenciar sonido físico, señal medida y valoración contextual como ruido;
2. clasificar señales aleatorias por evolución temporal y estacionariedad;
3. calcular e interpretar media, RMS, varianza y nivel equivalente;
4. comparar ruido blanco, rosa, con forma vocal y NBN;
5. diferenciar ruido de fondo, enmascarante y protección auditiva;
6. organizar medidas de control en fuente, trayecto y receptor.

### Continuidad

| Aspecto | Decisión |
|---|---|
| Conocimientos previos | U4: RMS/niveles; U5: bandas/ponderaciones; U7: enmascaramiento/SNR; U8: exposición; U9: control. |
| Conexión anterior | Integra propagación, medición, percepción y salud en señales variables. |
| Prepara | Cierre del curso y aplicación transversal. |
| Notación | \(p(t),\bar p,p_\mathrm{rms},\sigma_p^2,S_{pp}(f),L_{\mathrm{eq},T},L_\mathrm{max},L_\mathrm{peak},L_N\). |
| Visual reutilizable | Realizaciones temporales; histogramas; blanco/rosa por banda; SNR; enmascaramiento; jerarquía de control. |
| Aplicación | Evaluación auditiva, comunicación en ruido, exposición y diseño de espacios. |

## Comparación general programa–libro

| Categoría | Resultado |
|---|---|
| Cobertura completa | La gran mayoría del alcance de U1–U5, U7, U9 y la caracterización física de U10. |
| Cobertura parcial | U6: frente de onda, potencial de reposo y túnel de Corti; U7: curvas isofónicas numéricas y formalización de \(T_{60}\); U8: recuperación pos-exposición y riesgo porcentual por edad; U10: técnica clínica de enmascaramiento. |
| Ausencia clara | El término y descripción del túnel de Corti no aparecen en el capítulo U6. |
| Exceso útil del libro | Análisis dimensional, amortiguamiento, DFT/FFT, ventanas, C/Z, cóclea activa, ERB, dispositivos de conducción ósea, Sabine, estadística y control de ruido. |
| Diferencias de orden | Decibel se anticipa en U1 y formaliza en U4; reverberación se usa perceptualmente en U7 y físicamente en U9; enmascaramiento se explica en U7 y se aplica en U10. |
| Diferencias terminológicas | “Hass” → Haas/precedencia; “ruido vocal” → ruido con forma espectral vocal; “rampa coclear” → conducto coclear/rampa media; “transmisión paratimpánica” → conducción ósea multimecanismo. |

## Recursos especiales esperados

- señales audibles de tono, ruido, suma y filtrado, con alternativa visual;
- gráficos reproducibles de ondas, niveles, Fourier, espectros, filtros y ruido;
- diagramas anatómicos técnicamente validados para U6 y U8;
- datos normalizados verificados para isofónicas y requisitos de cabinas;
- ejemplos de voz con método, ejes, unidades y alcance declarados;
- ejercicios diagnósticos de errores conceptuales al inicio de cada bloque;
- revisiones pedagógicas independientes para U4, U5, U6 y U7.

