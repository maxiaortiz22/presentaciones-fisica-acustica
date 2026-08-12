# Unidad 7 — Brief pedagógico

## Identificación

- **Unidad:** 7.
- **Título oficial del programa:** Características subjetivas de la percepción auditiva (psicoacústica).
- **Título de trabajo:** Características subjetivas de la percepción auditiva (Psicoacústica).
- **Etapa:** estudio de fuentes y brief pedagógico previo al storyboard.
- **Estado:** borrador de arquitectura de unidad; requiere resolución de decisiones abiertas antes de secuenciar diapositivas.
- **Público:** estudiantes de primer año de la Licenciatura en Fonoaudiología.
- **Carga conceptual global:** muy alta.
- **Pregunta organizadora:** ¿cómo se relacionan un estímulo físico, una tarea de escucha y una respuesta perceptual sin confundir medición, experiencia e inferencia clínica?

Esta etapa aplica `course-architecture` y las fases de brief e inventario de `unit-storyboard`. No crea `storyboard.md`, texto de slides, notas del orador ni PowerPoint.

## Función de la unidad dentro del curso

La Unidad 7 es el pasaje explícito desde la cadena auditiva periférica estudiada en U6 hacia la experiencia y el desempeño del oyente. Recibe de U4 los niveles y el campo acústico, de U5 el espectro y los filtros, y de U6 la transferencia del oído periférico. Su aporte propio es el marco psicofísico:

```text
estímulo físico → tarea → respuesta → condiciones de interpretación
```

La unidad debe permitir que el estudiante deje de tratar como sinónimos pares que están relacionados, pero no son equivalentes:

- frecuencia ↔ altura tonal o *pitch*;
- nivel de presión sonora ↔ sonoridad;
- espectro ↔ timbre;
- duración física ↔ duración percibida;
- SNR ↔ inteligibilidad;
- retardo físico ↔ percepción de una reflexión;
- ITD/ILD ↔ localización completa.

La evidencia mínima al cierre, según `course_dependency_map.md`, es que el estudiante pueda separar **estímulo, tarea y respuesta** al interpretar un resultado psicofísico.

## Alcance obligatorio del programa

El programa oficial 2025, p. 4, exige cubrir:

- características subjetivas de la percepción auditiva y psicoacústica;
- curvas isofónicas normalizadas;
- umbral absoluto de audición y umbral de audibilidad;
- máxima sensibilidad del oído;
- resonancia del canal auditivo;
- diferencia entre nivel de presión sonora en el tímpano y en campo libre;
- altura o *pitch*;
- duración subjetiva;
- timbre;
- sonoridad;
- nivel de sonoridad y nivel de presión sonora;
- fones y sones;
- enmascaramiento;
- concepto de ruido y tiempo de reverberación;
- voz humana, sonoridad e inteligibilidad;
- pérdida de articulación de consonantes;
- efecto “Hass”, que se tratará con la grafía correcta **Haas** y dentro del efecto de precedencia;
- percepción del sonido reflejado;
- efecto *cocktail party*;
- mecanismo auditivo de localización;
- audición binaural;
- diferencia interaural de tiempo;
- diferencia interaural de intensidad, que se expresará con mayor precisión como **diferencia interaural de nivel (ILD)**.

El núcleo no puede omitir estos puntos. Las isofónicas numéricas, el concepto de ruido y el tiempo de reverberación presentan decisiones de alcance que se documentan en `source_analysis.md` y `open_decisions.md`.

## Profundidad prevista y límites

La profundidad adecuada es psicofísica introductoria, cuantitativa acotada y aplicada:

- describir toda observación mediante estímulo, tarea, respuesta y condiciones;
- interpretar curvas de umbral e isofónicas sin convertirlas en propiedades individuales universales;
- definir magnitudes físicas, atributos perceptuales y escalas sin intercambiarlos;
- aplicar relaciones cuantitativas sencillas solo dentro de sus hipótesis;
- explicar el enmascaramiento mediante elevación del umbral, relación espectro–tiempo y filtros auditivos;
- usar SNR, reverberación y ALCons para formular preguntas, no para predecir automáticamente inteligibilidad;
- separar el cálculo de un retardo de la percepción de fusión, coloración o eco;
- integrar ITD, ILD, pistas espectrales, movimiento y atención en la audición espacial;
- relacionar los conceptos con Audiología, voz, audífonos e implantes sin adelantar protocolos ni diagnóstico.

No corresponde desarrollar en profundidad:

- métodos psicofísicos adaptativos y teoría de detección de señales;
- modelos avanzados de sonoridad, pitch o escena auditiva;
- cálculo normativo de ISO 226, STI, SII o acústica de salas;
- diseño profesional de recintos;
- estadística completa del ruido;
- técnica clínica de enmascaramiento audiométrico;
- neuroanatomía auditiva central extensa;
- diagnóstico o rehabilitación, que pertenecen a U8.

## Objetivos de aprendizaje propuestos

Al finalizar la unidad, el estudiante podrá:

1. **Distinguir y relacionar** frecuencia/pitch, nivel de presión sonora/sonoridad, espectro/timbre y duración física/duración percibida, indicando cuál es magnitud física y cuál atributo perceptual.
2. **Interpretar** umbrales y curvas de igual sonoridad como resultados psicofísicos dependientes del estímulo, la tarea, el procedimiento, la población y el campo de presentación.
3. **Comparar y calcular** nivel de presión sonora, nivel de sonoridad y sonoridad mediante dB SPL, fones y sones, respetando el dominio y las limitaciones del modelo utilizado.
4. **Explicar y cuantificar** la elevación del umbral por enmascaramiento, diferenciando formas simultáneas y temporales, y componentes energéticos e informacionales.
5. **Relacionar** SNR, ruido, reverberación y pérdida de articulación de consonantes con la inteligibilidad del habla, sin asumir una fórmula universal ni una causa única.
6. **Explicar** la percepción de reflexiones mediante diferencia de recorrido, retardo, nivel, espectro y contexto, diferenciando el efecto de precedencia del resultado histórico denominado efecto Haas.
7. **Integrar** ITD, ILD, pistas espectrales, movimientos de la cabeza y atención para analizar localización y escucha con fuentes concurrentes.
8. **Delimitar** qué puede inferirse —y qué no— de un resultado perceptual o una medición acústica en aplicaciones fonoaudiológicas.

## Perfil de entrada y conocimientos previos

### Se espera recuperar

De U1:

- magnitud, valor, unidad y variable;
- proporcionalidad, función, potencia y logaritmo;
- lectura de ejes lineales y logarítmicos;
- diferencia entre magnitud física y atributo perceptual.

De U3:

- frecuencia, período, amplitud, fase y duración;
- tono puro, señal compleja y superposición;
- diferencia entre oscilación local y propagación.

De U4:

- presión acústica y presión eficaz;
- nivel de presión sonora `L_p`, referencia y dB SPL;
- diferencia entre nivel absoluto y diferencia de niveles;
- campo libre, reflexión, distancia y posición de medición.

De U5:

- espectro, fundamental, armónicos y fundamental ausente;
- respuesta en frecuencia de un sistema;
- bandas y filtros;
- SNR como comparación física bajo condiciones compatibles.

De U6:

- transferencia del pabellón y del CAE;
- dependencia frecuencial y espacial de la presión próxima al tímpano;
- tonotopía y codificación periférica inicial;
- separación entre mecanismo periférico y percepto.

### No se debe asumir dominado

- definición operacional de umbral;
- variabilidad psicofísica y papel del criterio de respuesta;
- lectura de curvas isofónicas;
- diferencia entre fon, son y dB SPL;
- fundamental ausente como ejemplo de pitch no reducible a una componente;
- duración percibida, resolución e integración temporal;
- elevación del umbral y patrón de enmascaramiento;
- filtros auditivos, banda crítica y ERB;
- enmascaramiento temporal, energético e informacional;
- relación entre SNR, reverberación, material lingüístico e inteligibilidad;
- ALCons como porcentaje observado y no diagnóstico;
- precedencia frente a efecto Haas;
- ITD, ILD, cono de confusión y pistas espectrales;
- segregación auditiva, atención y liberación espacial del enmascaramiento.

### Diagnóstico inicial recomendado

Antes del desarrollo formal conviene comprobar, sin calificación:

1. si el estudiante distingue `Hz`, `Pa`, dB SPL, fon y son;
2. si reconoce que dos tonos con igual `L_p` pueden no resultar igualmente sonoros;
3. si diferencia el espectro de una señal de su timbre percibido;
4. si puede explicar por qué una respuesta en campo libre no describe automáticamente la presión en el tímpano;
5. si distingue una diferencia física de nivel de una conclusión perceptual;
6. si identifica qué información falta al enunciado “la persona no oyó el tono”.

## Conceptos difíciles y nudos pedagógicos

| Nudo | Por qué es difícil | Tratamiento recomendado |
|---|---|---|
| Estímulo–tarea–respuesta | Se tiende a leer una respuesta como propiedad fija del oído. | Repetir la estructura en cada bloque y exigir condiciones antes de interpretar una cifra. |
| Umbral probabilístico | El lenguaje cotidiano sugiere una frontera exacta entre oír y no oír. | Usar una curva de respuestas o una actividad de detección conceptual; evitar un “punto mágico”. |
| Campo libre–tímpano | Ambos valores se expresan en dB SPL y parecen intercambiables. | Comparar posiciones y definir una diferencia de transferencia dependiente de frecuencia. |
| Isofónicas | Una curva normativa invita a leer equivalencias universales. | Separar procedimiento de construcción, datos normativos y límites de población/campo. |
| Pares físico–perceptuales | Las variables covarían, lo que favorece el uso como sinónimos. | Tabla estable físico ↔ perceptual con contraejemplos y unidades. |
| Fones y sones | Se mezclan nivel físico, nivel perceptual y escala de razón. | Introducir en tres etapas: comparación a 1 kHz, definición de fon y escala de sones. |
| Enmascaramiento | Se confunden nivel del enmascarador, umbral enmascarado y cantidad de enmascaramiento. | Gráfico con tres cantidades y un ejemplo numérico antes de filtros auditivos. |
| ERB y banda crítica | El modelo puede convertirse en una banda anatómica fija. | Presentar ERB como ancho equivalente de un filtro modelado, con frecuencia y condiciones. |
| Temporalidad | Simultáneo, hacia adelante y hacia atrás se invierten con facilidad. | Líneas temporales centradas en la señal objetivo; nombres definidos por el orden relativo. |
| SNR e inteligibilidad | Un único número parece prometer una predicción directa. | Conservar una matriz de condiciones: espectro, tiempo, sala, material, tarea y oyente. |
| Ruido y reverberación | U7 necesita sus efectos perceptuales, pero U9/U10 son propietarios de la física detallada. | Introducción funcional y puente explícito; no adelantar estadística ni Sabine. |
| ALCons | El porcentaje puede confundirse con una fórmula de sala o un diagnóstico. | Calcular solo un porcentaje observado y discutir causas alternativas. |
| Precedencia/Haas | Persiste la “regla de 20 ms”. | Separar retardo geométrico de respuesta perceptual y mostrar una zona gradual dependiente de condiciones. |
| Audición espacial | ITD e ILD parecen suficientes para toda dirección. | Añadir cono de confusión, pistas espectrales y movimiento de cabeza. |
| *Cocktail party* | Puede imaginarse como un filtro físico único. | Separar mezcla acústica, segregación, atención y enmascaramiento informacional. |

## Ideas erróneas previsibles

- `0 dB SPL` es el umbral universal de audición.
- El umbral es una frontera instantánea idéntica para todas las personas.
- La región de máxima sensibilidad implica que cualquier sonido allí es siempre más sonoro.
- El nivel en campo libre es el mismo que llega al tímpano.
- La resonancia del CAE agrega energía o produce una ganancia fija de sonoridad.
- Dos tonos con igual dB SPL tienen igual sonoridad.
- Frecuencia y pitch son sinónimos.
- La altura tonal solo existe si está presente la componente fundamental.
- El timbre es solamente la cantidad de armónicos.
- Duración percibida, resolución temporal e integración temporal son la misma propiedad.
- Un fon es un dB SPL.
- Un son es un nivel en dB.
- Ocho sones significan ocho veces más intensidad acústica.
- El nivel del enmascarador es el nuevo umbral.
- La ERB es una banda anatómica universal y constante.
- El enmascaramiento requiere siempre superposición temporal completa.
- Una SNR fija determina un porcentaje fijo de inteligibilidad.
- Reducir el ruido garantiza inteligibilidad alta aunque la reverberación permanezca.
- ALCons identifica la causa de los errores.
- Toda reflexión temprana mejora la inteligibilidad.
- Haas y precedencia son nombres de una regla universal de 20 ms.
- ITD localiza graves e ILD localiza agudos sin excepciones.
- ITD e ILD resuelven por sí solas elevación y adelante–atrás.
- El efecto *cocktail party* es un filtro físico localizado en el oído.
- Una diferencia perceptual constituye por sí sola evidencia diagnóstica.

## Relación con unidades anteriores y futuras

| Relación | Decisión pedagógica |
|---|---|
| U4 → U7 | Recuperar `L_p`, dB SPL, diferencia de niveles, campo libre y reflexiones. No reenseñar toda la teoría de niveles. |
| U5 → U7 | Recuperar espectro, fundamental ausente, filtros y bandas para pitch, timbre y enmascaramiento. |
| U6 → U7 | Partir de transferencia del CAE y codificación periférica; avanzar hacia tarea y respuesta sin repetir anatomía completa. |
| U7 → U8 | Preparar umbral, habla, localización y límites de inferencia para interpretar estudios y dispositivos sin anticipar diagnóstico. |
| U7 → U9 | Introducir el efecto perceptual de reflexiones y reverberación; dejar `T_60`, decaimiento y modelos de recinto para U9. |
| U7 → U10 | Formalizar enmascaramiento y SNR; dejar clasificación, estadística y señales de ruido para U10. |

## Aplicaciones profesionales prioritarias

1. **Umbral y audiometría:** diferenciar resultado psicofísico, escala de nivel, frecuencia, procedimiento y criterio.
2. **Medición en CAE y campo sonoro:** entender que la posición y la transferencia condicionan el estímulo disponible.
3. **Logoaudiometría y habla en ruido:** interpretar SNR, material lingüístico y porcentaje de respuestas sin convertirlos en diagnóstico aislado.
4. **Audífonos e implantes:** distinguir respuesta física del dispositivo, percepción del timbre/sonoridad y evaluación del desempeño.
5. **Micrófonos direccionales y sistemas remotos:** separar mejora física de SNR de beneficio perceptual individual.
6. **Escucha binaural:** analizar preservación o alteración de ITD, ILD y pistas espectrales en tareas de localización y segregación.
7. **Ambientes de voz:** relacionar ruido y reverberación con inteligibilidad, dejando el cálculo de recintos para U9.
8. **Enmascaramiento audiométrico:** aportar el mecanismo perceptual y la terminología, reservando la técnica clínica para U10 y protocolos específicos.

## Bloques pedagógicos preliminares y carga cognitiva

La tabla estima núcleos y dificultad. **No es un storyboard ni fija diapositivas individuales.**

| Bloque preliminar | Pregunta guía | Contenido dominante | Carga | Medida de alivio |
|---|---|---|---|---|
| 1. Puente psicofísico | ¿Qué se presentó, qué hizo el oyente y qué se registró? | Alcance, estímulo–tarea–respuesta, variabilidad y pares físico–perceptuales. | Alta | Un marco recurrente y diagnóstico breve. |
| 2. Umbral y sensibilidad | ¿Qué significa detectar y por qué depende de la frecuencia y del punto de medición? | Umbral, campo audible, máxima sensibilidad, CAE y campo–tímpano. | Muy alta | Curvas cualitativas, dos posiciones de medición, ejemplo y recapitulación. |
| 3. Isofónicas y atributos | ¿Cómo pueden variar pitch, sonoridad, timbre y duración con el estímulo? | Curvas de igual sonoridad, pitch, fundamental ausente, timbre, duración. | Muy alta | Un atributo por vez; audio/visual accesible y tabla de pares. |
| 4. Fones y sones | ¿Qué miden las dos escalas y cuándo puede usarse la conversión? | `L_N`, fon, sonoridad, son y modelo introductorio. | Alta | Tres escalas separadas, gráfico y un cálculo con límites visibles. |
| 5. Enmascaramiento | ¿Cómo cambia la detectabilidad por espectro y tiempo? | Elevación del umbral, simultáneo, filtros, ERB, temporal, energético/informacional. | Muy alta | Dividir fenómeno → gráfico → modelo → aplicación; dos recapitulaciones. |
| 6. Voz, ruido y recinto | ¿Por qué una SNR no alcanza para predecir inteligibilidad? | SNR, ruido, reverberación, material lingüístico, ALCons, STI/SII como referencia. | Muy alta | Caso de aula, matriz de condiciones, porcentaje observado y frontera con U9/U10. |
| 7. Reflexiones y precedencia | ¿Qué puede calcularse y qué debe observarse perceptualmente? | Diferencia de recorrido, retardo, fusión, coloración, eco, precedencia/Haas. | Alta | Separar cálculo y percepción; demostración opcional y error de 20 ms. |
| 8. Espacio y fuentes concurrentes | ¿Cómo se localiza y selecciona una voz entre varias? | Audición binaural, ITD, ILD, pistas espectrales, cono, movimiento, *cocktail party*. | Muy alta | Construcción progresiva de pistas; escena integradora y recapitulación. |
| 9. Aplicación e integración | ¿Qué permite afirmar cada dato y qué queda para U8–U10? | Aplicaciones, errores, ejercicios, síntesis y puente. | Alta | Matriz “medida/percepto/inferencia” y pregunta integradora. |

Los bloques 2, 3, 5, 6 y 8 no deberían dictarse sin pausas. `AGENTS.md` exige para U7 bloques cortos, recapitulaciones frecuentes y revisión pedagógica independiente.

## Estrategia didáctica recomendada

- Mantener la progresión **fenómeno → medición/tarea → representación → modelo → aplicación → límite**.
- Usar `estímulo → tarea → respuesta → condiciones` como recapitulación común.
- Definir el objeto de cada eje antes de interpretar una curva.
- Introducir primero un contraste perceptual concreto y después la escala o ecuación.
- Presentar cada atributo perceptual en una unidad breve con un contraejemplo a la equivalencia física.
- No introducir tres conceptos nuevos en una misma slide futura.
- Alternar gráficos, comparaciones, audio controlado, mini ejercicios y recapitulaciones.
- Diseñar toda demostración auditiva con nivel seguro, alternativa visual, instrucciones y propósito.
- Mantener las aplicaciones cerca del concepto que iluminan, sin adelantar protocolos de U8.
- Conservar visibles las condiciones de validez en isofónicas, fones/sones, ERB, SNR, ALCons, precedencia e ITD.
- Cerrar cada bloque con una pregunta de inferencia: “¿qué falta para sostener esta conclusión?”.

## Evaluación de transferencia a diapositivas

### Puede pasar casi directamente como idea o estructura

- el marco estímulo–tarea–respuesta;
- las cuatro distinciones físico–perceptuales;
- la definición operacional de umbral y la advertencia de variabilidad;
- el contraste campo libre–tímpano y su ejemplo de diferencia de nivel;
- el procedimiento de construcción conceptual de una isofónica;
- definiciones breves de pitch, sonoridad, timbre y duración percibida;
- distinción fon/son y el ejemplo de conversión acotada;
- elevación del umbral por enmascaramiento;
- líneas temporales de enmascaramiento;
- distinción energético/informacional;
- SNR como diferencia de niveles comparables;
- ALCons como porcentaje observado;
- retardo geométrico frente a resultado perceptual;
- integración de ITD, ILD, pistas espectrales y movimiento;
- escena de fuentes concurrentes;
- errores frecuentes y pregunta integradora.

“Casi directamente” significa conservar el razonamiento y la terminología, no copiar párrafos, páginas o figuras a escala de libro.

### Necesita transformación sustantiva

- los listados largos de objetivos y errores;
- las figuras TikZ con rótulos pequeños para aula;
- las explicaciones de atributos, que deben separarse en varios momentos;
- filtros auditivos y ERB, que requieren preparación visual y límite del modelo;
- SNR, reverberación, ALCons, STI y SII, que compiten por carga conceptual;
- precedencia, Haas, coloración, fusión y eco, que no caben en una regla temporal única;
- audición espacial, que necesita construcción acumulativa;
- soluciones completas del banco de ejercicios, que deben reservarse en gran parte para respaldo.

## Recursos disponibles

- capítulo LaTeX completo con secciones, ecuaciones, ejemplos, ejercicios, soluciones y glosario;
- capítulo PDF, pp. 177–205, verificado visualmente;
- nueve figuras TikZ propias sobre umbral, campo–tímpano, isofónicas, fones/sones, enmascaramiento, precedencia, audición espacial y fuentes concurrentes;
- figura raster `context/libro_latex/figures/FletcherMunson.png`, cuya pertinencia, licencia y actualización normativa deben verificarse antes de cualquier uso;
- figura raster `context/libro_latex/figures/enmascaramiento.png`, que también requiere evaluación y trazabilidad;
- bibliografía ya registrada para ISO 226, definiciones ASA, filtros auditivos, precedencia, audición espacial, habla y fuentes concurrentes;
- guías transversales de estilo, notación y glosario.

No se localizó un deck previo de U7 ni una guía independiente de ejercicios/evaluaciones. La ausencia se registra como limitación, no como autorización para inventar criterios docentes.

## Estimación de extensión probable

La densidad del capítulo, la cantidad de conceptos nuevos y la exigencia de ejemplos, actividades y recapitulaciones justifican una presentación larga. Como estimación inicial —no como máximo—:

| Componente | Rango probable | Criterio |
|---|---:|---|
| Ruta central | 76–94 slides | Nueve bloques, una idea dominante por slide, ejemplos seleccionados, comprobaciones y recapitulaciones. |
| Material complementario | 12–20 slides | ERB ampliada, integración temporal, STI/SII, variantes y demostraciones. |
| Respaldo | 14–24 slides | Soluciones, glosario, fuentes, condiciones normativas y variantes numéricas. |
| **Total probable** | **102–138 slides** | Dependerá de cantidad y duración de encuentros, audios y nivel de desarrollo de enmascaramiento/espacio. |

Una planificación razonable podría requerir tres o cuatro encuentros. Comprimir todo en una clase única obligaría a retirar ejemplos o a violar la legibilidad y la progresión requerida.

## Priorización preliminar

### Parte central

- alcance psicofísico y marco estímulo–tarea–respuesta;
- umbral, sensibilidad, campo audible y campo–tímpano;
- curvas isofónicas y pares físico–perceptuales;
- pitch, sonoridad, timbre y duración;
- nivel de sonoridad, fon, sonoridad y son;
- elevación del umbral y enmascaramiento simultáneo/temporal;
- distinción energético/informacional;
- SNR, reverberación e inteligibilidad;
- ALCons como concepto y porcentaje observado;
- precedencia frente a Haas;
- ITD, ILD, pistas espectrales, movimiento y fuentes concurrentes;
- aplicaciones, errores y síntesis.

### Material complementario

- fundamental ausente con mayor desarrollo o demostración;
- integración y resolución temporal ampliadas;
- banco de filtros auditivos, banda crítica y ERB con cálculo;
- patrones de enmascaramiento asimétricos;
- STI y SII como marcos diferenciados, sin cálculo normativo;
- liberación espacial del enmascaramiento;
- variantes de modelos geométricos de ITD;
- análisis de dispositivos que modifican SNR o pistas binaurales.

### Slides de respaldo

- datos normativos y condiciones de ISO 226, una vez verificados;
- soluciones completas de ejercicios;
- conversiones adicionales entre fones y sones;
- cálculos alternativos de ERB, retardo, SNR, ALCons e ITD;
- bibliografía técnica y definiciones normativas;
- glosario extendido;
- límites de modelos y distractores razonables;
- material de consulta sobre STI/SII y acústica de recintos.

## Criterio de cierre de esta etapa

Esta etapa queda completa cuando existen y son coherentes:

- `brief.md`;
- `content_inventory.md`;
- `source_analysis.md`;
- `open_decisions.md`.

El siguiente paso autorizado en el flujo será resolver las decisiones de prioridad alta y recién después crear el storyboard completo. No se redactan slides en este documento.
