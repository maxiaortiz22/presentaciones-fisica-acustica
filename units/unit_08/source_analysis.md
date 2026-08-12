# Unidad 8 — Análisis de fuentes

## Jerarquía aplicada

Se aplicó la jerarquía definida en `AGENTS.md`:

1. programa oficial 2025;
2. capítulo 8 del libro en LaTeX;
3. capítulo 8 del libro publicado en PDF;
4. arquitectura curricular (`course_map.md`, `course_dependency_map.md` y `content_coverage_matrix.csv`);
5. guías transversales de estilo, notación y glosario;
6. bibliografía académica, profesional, normativa y sanitaria ya citada en el capítulo.

No se incorporaron fuentes externas nuevas ni datos no presentes en el repositorio. Las brechas detectadas se registran como decisiones pendientes.

## Disponibilidad y método de revisión

| Fuente | Ubicación | Revisión realizada |
|---|---|---|
| Programa oficial | `context/programa/Programa de Física Acústica.pdf` | Texto completo de 6 páginas; alcance U8 en p. 4 y objetivos generales/específicos en pp. 1–2. |
| Libro LaTeX | `context/libro_latex/chapters/08-enfermedades-diagnostico-rehabilitacion.tex` | Lectura completa de 1477 líneas: contenido, ecuaciones, tablas, figuras, ejercicios, respuestas, glosario y fuentes. |
| Libro PDF | `context/libro_pdf/Física Acústica para Fonoaudiología.pdf` | Capítulo completo localizado en pp. 207–233; extracción textual de todas las páginas y revisión visual representativa de pp. 207, 213, 216, 219 y 221. |
| Mapa del curso | `course_map.md` | Función, alcance, resultados, carga, continuidad y alertas de U8. |
| Dependencias | `course_dependency_map.md` | Dependencias U4–U7 → U8, puente U8 → U10 y evidencia mínima. |
| Matriz de cobertura | `content_coverage_matrix.csv` | Revisión de U08-01 a U08-15 y U08-X1. |
| Sistema visual | `style/presentation_style_guide.md` | Principios, densidad, gráficos, ecuaciones, tablas, animaciones, accesibilidad y editabilidad. |
| Notación | `style/notation_guide.md` | Reglas generales; escalas SPL/HL/SL; TTS, HIR/NIHL, OEA y PEAT/PEATC; pendientes de validación. |
| Glosario | `style/glossary.md` | TTS, hipoacusia inducida por ruido, tinnitus, dB HL, dB SL, OEA, conducción ósea y términos previos. |

El directorio `units/unit_08/` contenía únicamente `.gitkeep`; no existía brief, storyboard ni deck previo que conservar o comparar.

## Alcance obligatorio extraído del programa

La formulación original del programa, p. 4, es:

> Enfermedades y estudios auditivos, técnicas de rehabilitación. Curvas de corrección después de una exposición. Desplazamiento temporal de audición (TTS). Pérdida de la audición inducida por el ruido. Tinnitus o acúfenos. Presbiacúsia. Riesgo porcentual de pérdida auditiva por ruido ocupacional en función de la edad. Estudios auditivos y técnicas de rehabilitación. Audiometrías. Logoaudiometrías. Timpanometría. Acufenometría. Potenciales auditivos evocados (PEAT). Otoemisiones acústicas (OEA). Electrococleografía. Audífonos e implantes cocleares.

Para el brief se normalizan solo aspectos editoriales:

- “desplazamiento temporal de audición” se desarrolla como **desplazamiento temporal del umbral**;
- “presbiacúsia” se escribe **presbiacusia**;
- audiometría y logoaudiometría se usan en singular como nombres de procedimientos;
- la expresión “curvas de corrección” se conserva como cita del programa y se marca para aclaración; no se corrige silenciosamente a “recuperación”.

Los objetivos específicos generales del programa también exigen caracterizar enfermedades auditivas y conocer métodos de diagnóstico, dentro de una formación que integra teoría y ejercicios. El capítulo limita correctamente este mandato: presenta fundamentos y alcance de estudios, pero no sustituye protocolos ni diagnóstico profesional.

## Comparación programa–LaTeX–PDF

| Tema | Programa | LaTeX | PDF | Estado y decisión |
|---|---|---|---|---|
| Curvas pos-exposición | “Curvas de corrección después de una exposición” | Explica dependencia temporal del TTS y rechaza tiempos universales; no incluye curva cuantitativa. | Concordante, pp. 209–210. | **Brecha obligatoria.** Aclarar término y seleccionar fuente primaria antes del storyboard. |
| TTS | Obligatorio | Definición, ecuación, variables, límites y ejercicios. | Concordante, pp. 209–210 y 224–232. | Cubierto con buena profundidad introductoria. |
| Pérdida inducida por ruido | Obligatoria | PAIR/NIHL, historia, patrón y cautela causal. | Concordante, p. 210. | Cubierto; resolver sigla visible. |
| Tinnitus/acúfeno | Obligatorio | Definición, variabilidad, diferencia con TTS y puente a acufenometría. | Concordante, p. 211. | Cubierto. |
| Presbiacusia | Obligatoria | Multifactorialidad y ausencia de patrón único. | Concordante, p. 211. | Cubierto. |
| Riesgo porcentual por ruido y edad | Obligatorio | Explica por qué no existe un porcentaje universal, pero no aporta tabla/curva. | Concordante; no hay representación cuantitativa. | **Brecha obligatoria.** Requiere fuente, población, definición de caso y modelo. |
| Audiometría | Obligatoria | Estímulo, magnitud, vías, respuesta, resultado, límites, ecuación y figura. | Concordante, pp. 212–213. | Cubierta. |
| Logoaudiometría | Obligatoria | Material, escala, porcentaje, control cruzado, límites y figura conceptual. | Concordante, pp. 213–215. | Cubierta. |
| Timpanometría | Obligatoria | Estímulo, inmitancia/admitancia, presión, morfologías y límites. | Concordante, pp. 215–216. | Cubierta. |
| Acufenometría | Obligatoria | Correspondencias de frecuencia/nivel, enmascaramiento e inhibición residual con límites. | Concordante, pp. 216–217. | Cubierta; profundidad del enmascaramiento debe acotarse. |
| PEAT | Obligatorio | Estímulo, potencial, latencia, electrodos, generadores y limitaciones. | Concordante, pp. 217–219. | Cubierto; validar PEAT/PEATC. |
| OEA | Obligatoria | Estímulo, presión, SPL, SNR, CCE, transmisión externa/media y pesquisa. | Concordante, pp. 216–219. | Cubierta. |
| Electrococleografía | Obligatoria | Potenciales cocleares/nervio distal, electrodos y dependencia de protocolo. | Concordante, p. 218. | Cubierta. |
| Audífonos | Obligatorios | Cadena, ganancia, procesamiento y límites. | Concordante, p. 219. | Cubiertos. |
| Implantes cocleares | Obligatorios | Cadena, código eléctrico, electrodos/canales y límites. | Concordante, pp. 219–220. | Cubiertos. |
| Trauma acústico | No explícito | Desarrollo introductorio con cautela sanitaria. | Concordante, pp. 210–211. | Ampliación importante. |
| Ototoxicidad | No explícita | Diferencia causa química de exposición acústica. | Concordante, p. 211. | Ampliación importante. |
| Conducción ósea | No explícita como dispositivo | Dispositivo y salida mecánica; ambas cócleas. | Concordante, pp. 220–221. | Complementario. |
| Estimulación electroacústica | No explícita | Combina salida acústica y eléctrica. | Concordante, pp. 220–221. | Complementario. |

La matriz de cobertura coincide con esta lectura: U08-02 a U08-15 figuran `covered`; U08-01 y U08-06 figuran `external_expansion`; U08-X1 agrupa ampliaciones fuera del alcance obligatorio.

## Correspondencia LaTeX–PDF

### Verificación estructural

El PDF reproduce la estructura sustantiva del LaTeX:

| Contenido | LaTeX | PDF |
|---|---|---|
| Propósito y objetivos | `sec:u8-proposito` | pp. 207–208 |
| Conocimientos previos y situación | `sec:u8-previos`, `sec:u8-situacion` | pp. 208–209 |
| Alteraciones y patologías | `sec:u8-alteraciones` | pp. 209–211 |
| Estudios auditivos | `sec:u8-estudios` | pp. 211–219 |
| Rehabilitación | `sec:u8-rehabilitacion` | pp. 219–221 |
| Relación profesional y errores | `sec:u8-relacion-fonoaudiologia`, `sec:u8-errores` | pp. 221–223 |
| Síntesis y ejercicios | `sec:u8-sintesis`, `sec:u8-ejercicios` | pp. 223–228 |
| Respuestas | `sec:u8-respuestas` | pp. 228–232 |
| Glosario y alcance documental | `sec:u8-glosario`, `sec:u8-fuentes` | pp. 232–233 |

No se detectaron omisiones, ecuaciones divergentes ni figuras diferentes entre las dos versiones. El PDF parece una compilación coherente del LaTeX disponible.

### Verificación visual

La revisión de páginas representativas confirmó:

- **p. 207:** apertura, propósito y resultados completos, con una densidad propia del libro que no debe trasladarse como slide;
- **p. 213:** audiograma conceptual legible en página impresa, con ejes, vías y cálculo; requiere ampliación y revelado por etapas en aula;
- **p. 216:** tres timpanogramas claros, pero acompañados por contenido de acufenometría/OEA en la misma página; deben separarse en el deck;
- **p. 219:** cadena OEA–PEAT y comienzo de dispositivos; el diagrama es correcto pero contiene muchos rótulos pequeños para media slide;
- **p. 221:** tabla y diagrama de dispositivos comparten página; ambos necesitan slides independientes o secuencia acumulativa.

La maquetación del libro es adecuada para lectura cercana. No es una referencia directa de tamaño tipográfico, cantidad de texto ni composición de diapositivas.

## Fórmulas, magnitudes y ejemplos localizados

| Relación | Ubicación LaTeX/PDF | Magnitudes | Ejemplo disponible | Observación |
|---|---|---|---|---|
| `ΔL_T = L_{U,1} - L_{U,0}` | Ecuación 8.1; pp. 209–210 | `f`, `Δt`, umbrales dB HL, diferencia dB | 12 → 27 dB HL = 15 dB | Central; separar cálculo de diagnóstico. |
| Normalización de `L_Aeq,T` | Ecuación 8.2; p. 210 | nivel ponderado A, tiempos, razón adimensional | 95 dB(A), 1 h → 86,0 dB(A), 8 h | Importante; no convertir en norma. |
| `G_AO = L_VA - L_VO` | Ecuación 8.3; p. 213 | umbrales VA/VO en dB HL | 40 − 15 = 25 dB | Central o actividad; validar símbolo/nombre. |
| `G = L_sal - L_ent` | Ecuación 8.4; p. 219 | niveles de entrada/salida en dB SPL | 70 − 52 = 18 dB | Central o complemento; no equivale a beneficio. |

Magnitudes adicionales: frecuencia en Hz; presión acústica en Pa; presión de conducto en daPa; admitancia/inmitancia con unidad del equipo; potencial en µV; latencia en ms; SNR en dB; porcentaje de respuestas; corriente en A; desplazamiento en m.

## Ampliaciones del libro respecto del programa

El libro añade contenido pedagógicamente útil:

1. distinción explícita entre exposición, alteración, síntoma y resultado;
2. situación introductoria que convierte una queja en preguntas distintas;
3. clasificación conductiva/sensorioneural/mixta con advertencia de batería;
4. trauma acústico y ototoxicidad;
5. cadena común para comparar pruebas;
6. diferencia entre prueba conductual y fisiológica;
7. descripción sistemática de estímulo, magnitud, sistema, respuesta, resultado y límites;
8. diferencia cuantitativa entre vías audiométricas;
9. comparación OEA–PEAT por generador y sensor;
10. dispositivos de conducción ósea y estimulación electroacústica;
11. ganancia electroacústica;
12. banco extenso de ejercicios, aplicaciones y distractores;
13. glosario específico y revisión bibliográfica de afirmaciones clínicas/normativas.

Estas ampliaciones mejoran la comprensión, pero no todas deben ocupar la ruta central. Trauma/ototoxicidad son importantes para evitar causalidad acústica simplista; conducción ósea y estimulación electroacústica pueden quedar como complemento según tiempo.

## Diferencias, tensiones y vacíos documentales

### 1. “Curvas de corrección” frente a curvas de recuperación

El programa usa literalmente “curvas de corrección después de una exposición”; `course_map.md` y la matriz interpretan “recuperación”. El capítulo explica el curso temporal del TTS, pero no usa una curva cuantitativa. Debe confirmarse si “corrección” es la denominación docente deseada, un error editorial o una referencia a recuperación del umbral.

### 2. Falta de curva cuantitativa pos-exposición

No existe en el repositorio una curva con datos, población, nivel/espectro/duración de exposición, frecuencia de prueba y tiempos de medición. No se debe fabricar una forma universal. Una figura conceptual puede enseñar variables, pero el programa parece exigir además una curva de contenido sustantivo.

### 3. Riesgo porcentual por edad y ruido ocupacional

El capítulo evita correctamente un porcentaje universal. Sin embargo, el programa exige riesgo porcentual en función de la edad. La cobertura no queda completa solo con advertir que el riesgo depende del contexto. Hace falta una fuente primaria o normativa con:

- población y rango etario;
- definición de exposición;
- definición de pérdida/caso;
- duración o historia laboral;
- tratamiento de sexo/género u otros factores si la fuente los usa;
- modelo estadístico o normativo;
- interpretación de grupo frente a individuo.

### 4. Título de la unidad

El programa usa “Enfermedades y estudios auditivos, técnicas de rehabilitación”. El pedido y el capítulo agregan “Alteraciones”. El título de trabajo es pedagógicamente más preciso y menos reduccionista; debe conservarse la trazabilidad con el título oficial.

### 5. PAIR, HIR y NIHL

El capítulo usa PAIR/NIHL; la guía de notación propone HIR o NIHL y pide elegir una sigla institucional. `course_map.md` registra PAIR/NIHL. La decisión debe resolverse antes de escribir títulos, ejes y actividades.

### 6. PEAT, PEATC y ABR

Programa y capítulo usan PEAT; la guía deja pendiente la forma institucional PEAT/PEATC. ABR solo debería aparecer como equivalencia bibliográfica después de desarrollar el término en español.

### 7. Tinnitus o acúfeno

Programa y capítulo presentan ambos términos; el glosario pide elegir el par preferido por la cátedra. Puede usarse “tinnitus o acúfeno” al introducir y luego mantener una forma dominante.

### 8. “Estudios diagnósticos” y alcance real

El título del bloque LaTeX es “Estudios diagnósticos”, pero el propio texto insiste en que ningún resultado equivale a diagnóstico. En diapositivas conviene usar “estudios auditivos” o “estudios para la evaluación auditiva” como rótulo principal y explicar el alcance diagnóstico integrado.

### 9. dB SPL, dB HL y dB SL

El capítulo es consistente al no tratarlos como intercambiables. El deck deberá reforzar esta distinción antes de cálculos y porcentajes. La guía exige desarrollar referencia y condición.

### 10. Inmitancia y admitancia

El capítulo usa inmitancia como categoría y admitancia como magnitud habitual. No fija una unidad universal porque depende del equipo/protocolo. En el gráfico conceptual normaliza `Y/Y_max`. La futura slide no debe presentar esa normalización como formato clínico normativo.

### 11. Normalización de exposición y normativa

La ecuación didáctica de `L_Aeq,T` supone contribución despreciable fuera del intervalo activo. No incorpora intercambio de dosis, picos, impulsividad, protección ni criterios legales. La normativa citada debe validarse por edición y jurisdicción antes de cualquier afirmación aplicada.

### 12. Patrones conceptuales y etiquetas clínicas

Audiograma, curva logoaudiométrica y timpanogramas son deliberadamente sintéticos. Deben conservar rótulos como “datos ficticios”, “esquema conceptual” y “sin valor diagnóstico/normativo”. No deben reutilizarse como ejemplos de enfermedades.

### 13. Densidad de las descripciones de pruebas

El capítulo repite seis campos para cada estudio, lo cual es excelente como referencia, pero una transcripción produciría slides clonadas y mucha carga verbal. El storyboard deberá alternar cadena, mapa, gráfico, comparación, actividad y recapitulación.

### 14. Bibliografía histórica y vigencia

El capítulo cita una fuente de 1977 para electrofisiología junto con referencias actuales. Puede servir para principios generales, pero cualquier protocolo, criterio o valor operativo debe verificarse con fuentes vigentes antes de convertirse en contenido visible.

### 15. Frontera con U10

U8 debe explicar exposición, TTS y pérdida inducida por ruido, y puede anticipar SNR/enmascaramiento como condición de pruebas. U10 conserva la caracterización física de tipos de ruido y la revisión de la técnica de enmascaramiento. La superposición debe ser intencional y no duplicar el desarrollo.

## Qué puede pasar casi directamente a diapositivas

- la pregunta introductoria y la separación de datos;
- la definición del TTS y el cálculo de diferencia;
- la frase “una escotadura puede ser compatible, pero no demuestra etiología”;
- la matriz de seis preguntas para estudios;
- la oposición conductual/fisiológica con sus límites;
- el audiograma conceptual, remaquetado;
- la curva desempeño–nivel como estructura de lectura;
- las tres morfologías timpanométricas, separadas de diagnósticos;
- la comparación OEA–PEAT por sensor y magnitud;
- la diferencia audífono/implante por tipo de salida;
- los ejercicios de clasificación, operación compatible y límite de inferencia;
- el caso integrador como cierre.

Las ideas son transferibles; la densidad textual y la composición de página no lo son.

## Qué necesita más explicación o recursos

| Contenido | Necesidad | Motivo |
|---|---|---|
| Categorías de evidencia | Diagrama y caso recurrente | Es la base de todas las inferencias posteriores. |
| Curva pos-exposición | Fuente primaria + gráfico | Falta contenido cuantitativo obligatorio. |
| Riesgo porcentual | Fuente + metadatos + actividad crítica | Falta contenido obligatorio y existe alto riesgo de interpretación personal. |
| SPL/HL/SL | Tabla/diagrama y operaciones | Comparten dB pero no referencia. |
| Batería de pruebas | Mapa funcional y actividad | Evita memorizar nombres y diagnosticar por dato único. |
| Audiograma | Gráfico grande y revelado | Convención vertical y vías requieren guía. |
| Logoaudiometría | Caso con metadatos | Un porcentaje aislado es engañoso. |
| Timpanometría | Animación del barrido + curvas | La forma final oculta el proceso de medición. |
| OEA/PEAT/electrococleografía | Diagramas paralelos | Generador, sensor y magnitud compiten conceptualmente. |
| Dispositivos | Cadenas editables y, quizá, imágenes técnicas | Debe verse dónde cambia el dominio físico. |
| Procesamiento de audífonos | Gráfico entrada–salida/respuesta | “Amplificar” es insuficiente y puede sugerir linealidad fija. |

## Implicancias de estilo, notación y glosario

- Una idea dominante por slide; no colocar los seis campos completos de una prueba en un único panel pequeño.
- Cuerpo visible de 22–24 pt, nunca menos de 20 pt; ecuaciones principales con espacio propio.
- Teal puede identificar estímulo, señal o medición física; ocre puede identificar respuesta perceptual/clínica. No depender solo del color.
- Usar gráficos propios o reconstrucciones editables antes que capturas del PDF.
- Todo gráfico debe tener magnitud, símbolo, unidad y condición; las curvas conceptuales deben rotularse explícitamente.
- Audiograma, timpanograma y curvas de riesgo/recuperación necesitan captions con alcance.
- Desarrollar TTS, PAIR/HIR/NIHL, OEA y PEAT/PEATC en su primera aparición.
- Mantener `L_Aeq,T`, `ΔL_T`, `G_AO` y `G(f)` con subíndices matemáticos editables.
- No restar ni alinear visualmente niveles con referencias incompatibles como si fueran equivalentes.
- Reconstruir diagramas a tamaño real mediante `diagram-generation`; las figuras de libro no cumplen por sí solas los mínimos de tipografía para aula.
- Cualquier audio debe ser seguro, breve, no diagnóstico y contar con alternativa visual/textual.
- Animaciones solo para revelar pasos, barridos o trayectos; la versión estática debe seguir siendo comprensible.

## Coherencia con la arquitectura del curso

La arquitectura clasifica U8 como **muy alta carga**, con profundidad comparativa e introductoria y una alerta central: evitar diagnóstico a partir de un dato aislado.

Dependencias explícitas:

- U4 aporta escalas y niveles;
- U5 aporta señal/sistema, exposición, espectro, medición y respuesta en frecuencia;
- U6 aporta vías, transferencia y transducción;
- U7 aporta umbral, percepción, habla y condiciones de tarea;
- U8 prepara exposición, ruido y enmascaramiento aplicado de U10.

La evidencia mínima de `course_dependency_map.md` —comparar dos pruebas sin convertir resultados en diagnósticos— se adopta como criterio de cierre. La intervención recomendada —matriz común de seis preguntas— se adopta como estructura organizadora, no como plantilla visual repetida.

## Fuentes técnicas ya citadas por el capítulo

El capítulo contiene referencias trazables para principios generales:

| Clave local | Fuente/organización | Uso principal en U8 |
|---|---|---|
| `ashaHearingAdults` | ASHA Practice Portal | Evaluación auditiva, batería de pruebas y límites. |
| `ashaPureTone2005` | ASHA | Audiometría tonal y procedimientos. |
| `iso8253_1_2010` | ISO 8253-1 | Audiometría tonal liminar. |
| `ryan2016` | Ryan et al. | TTS y cambios permanentes inducidos por ruido. |
| `kurabi2017` | Kurabi et al. | Mecanismos celulares de daño por ruido. |
| `nioshOtotoxic2018` | NIOSH | Ototoxicidad ocupacional. |
| `ashaTinnitus` | ASHA Practice Portal | Tinnitus y acufenometría. |
| `gatesMills2005` | Gates y Mills | Presbiacusia. |
| `skinnerGlattke1977` | Skinner y Glattke | Electrofisiología auditiva general. |
| `simpson2020` | Simpson et al. | Electrococleografía. |
| `whoHearing2021` | OMS | Rehabilitación y dispositivos. |
| `nidcdCI2024` | NIDCD | Implantes cocleares. |
| `stenfeltGoode2005` | Stenfelt y Goode | Conducción ósea. |
| `argentinaResolucion85` | SRT, Argentina | Medición de ruido laboral. |
| `nioshNoise1998` | NIOSH | Exposición ocupacional a ruido. |

Estas referencias no resuelven automáticamente las dos brechas programáticas. Antes de usar curvas o porcentajes se debe comprobar que la fuente concreta aporte datos reproducibles y condiciones compatibles con el propósito docente.

## Conclusión del análisis

Programa, LaTeX y PDF son coherentes en el núcleo de alteraciones, estudios y dispositivos. El capítulo ofrece una base excepcionalmente completa para una secuencia comparativa y cauta, con fórmulas, figuras, ejercicios y límites explícitos. La principal dificultad no es la falta de contenido general, sino la coexistencia de muchos dominios y el riesgo de inferencia clínica indebida.

La unidad no está lista para storyboard hasta resolver o encuadrar de forma explícita:

1. qué significa “curvas de corrección” en el programa;
2. qué fuente sostendrá una curva pos-exposición;
3. qué fuente/modelo sostendrá el riesgo porcentual por edad y ruido;
4. qué siglas y términos adoptará la cátedra;
5. cuántos encuentros y qué profundidad se asignarán a ampliaciones y dispositivos.
