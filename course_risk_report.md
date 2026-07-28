# Informe de riesgos del curso

**Estado:** borrador de arquitectura curricular  
**Fecha de análisis:** 28 de julio de 2026  
**Alcance:** programa oficial 2025, libro completo 2026 en PDF y LaTeX, ejercicios incluidos en el libro y materiales complementarios disponibles en el repositorio.

## Resumen ejecutivo

El curso posee una base documental sólida: el libro desarrolla las diez unidades del programa, conserva una progresión reconocible y ofrece ejercicios, preguntas conceptuales, aplicaciones fonoaudiológicas y orientaciones de respuesta. No se detectaron contradicciones físicas graves entre el programa y el libro. Las principales brechas están concentradas en contenidos normativos o clínicos que dependen de fuentes externas vigentes, en algunos términos anatómicos puntuales de la Unidad 6 y en la ausencia de materiales de evaluación independientes.

El mayor riesgo pedagógico no es la falta general de contenido, sino la densidad. Las unidades 4 a 7 encadenan magnitudes acústicas, análisis frecuencial, fisiología auditiva y psicofísica. Si se presentan como inventarios de fórmulas, estructuras o términos, pueden producir aprendizaje fragmentario. Requieren bloques breves, recuperación deliberada de prerrequisitos, ejemplos resueltos y recapitulaciones frecuentes.

## Fuentes revisadas y limitaciones

- El programa oficial disponible corresponde a 2025.
- El libro disponible corresponde a 2026 y contiene 296 páginas.
- El PDF completo y los once archivos de capítulos LaTeX fueron contrastados.
- El `main.tex` está disponible y referencia introducción, diez unidades y bibliografía.
- Cada unidad del libro contiene actividades y orientaciones de resolución.
- No se localizaron guías de ejercicios independientes, parciales, cuestionarios, rúbricas, bancos de ítems ni devoluciones de cohortes anteriores.
- No se localizaron cronograma, carga horaria efectiva por unidad, modalidad de cursado ni calendario de evaluaciones.

Estas ausencias no impiden definir la arquitectura, pero sí limitan la calibración exacta de profundidad, ritmo y cantidad de práctica.

## Registro priorizado de riesgos

| ID | Severidad | Unidad | Riesgo o vacío | Evidencia | Consecuencia posible | Tratamiento recomendado |
|---|---|---:|---|---|---|---|
| R01 | alta | transversal | No se confirmó que el programa 2025 sea la versión vigente para el dictado 2026. | El libro es 2026 y el programa identificado es 2025. | Desarrollar un alcance desactualizado u omitir cambios curriculares recientes. | Validar versión y resolución del programa antes de cerrar briefs. |
| R02 | alta | 4–7 | Sobrecarga cognitiva acumulativa. | Las cuatro unidades concentran niveles logarítmicos, Fourier, anatomofisiología y psicofísica. | Memorización sin integración; confusión entre variables físicas, respuestas del sistema y perceptos. | Dividir en bloques cortos, incorporar recuperaciones y realizar revisión pedagógica independiente por unidad. |
| R03 | alta | 6 | “Túnel de Corti” no aparece explícitamente en los capítulos disponibles. | Búsqueda textual en LaTeX y revisión del capítulo/PDF. | Incumplimiento literal de un tema obligatorio del programa. | Incorporar una definición anatómica breve con fuente académica primaria o manual de referencia. |
| R04 | alta | 7 | Las curvas isofónicas normalizadas no cuentan aún con datos normativos trazables en el material. | El libro explica el concepto, pero la figura exacta queda condicionada a datos ISO 226. | Dibujar una curva ilustrativa como si fuera normativa o usar valores desactualizados. | Obtener la edición vigente de ISO 226 o una fuente primaria autorizada y registrar versión/licencia. |
| R05 | alta | 8 | Faltan curvas cuantitativas de recuperación tras exposición. | El texto describe TTS y su evolución temporal, pero no aporta curvas. | Quedar por debajo del alcance literal del programa o inventar una trayectoria típica. | Definir con el docente si bastará un esquema conceptual o si se incorporará evidencia experimental primaria. |
| R06 | alta | 8 | “Porcentaje de riesgo” por edad y ruido ocupacional no puede expresarse universalmente. | El libro advierte dependencia de población, exposición, definición de caso y modelo. | Presentar cifras engañosas o trasladar resultados entre poblaciones. | Elegir norma/modelo o estudio epidemiológico, población y desenlace antes de cuantificar. |
| R07 | alta | 9 | Faltan niveles máximos permisibles numéricos para ruido ambiente en audiometría. | El libro cubre el criterio, pero no fija una tabla normativa. | Usar límites incompatibles con transductor, vía, banda o jurisdicción. | Confirmar norma vigente, configuración audiométrica y jurisdicción institucional. |
| R08 | alta | 10 | La técnica clínica de enmascaramiento está cubierta solo en nivel introductorio. | No se desarrolla de forma completa nivel inicial, oclusión, sobreenmascaramiento y meseta. | Que el alumnado interprete la introducción como protocolo clínico suficiente. | Delimitar resultado esperado o ampliar con protocolo y bibliografía clínica adoptados por la cátedra. |
| R09 | media | 6 | El enunciado “transformación esférica a cilíndrica” simplifica en exceso el CAE. | El libro describe un conducto curvo, de sección variable, finito y dependiente de frecuencia/posición. | Reificar una geometría ideal como descripción anatómica literal. | Conservar el tema del programa, pero enseñar la idealización y sus límites explícitos. |
| R10 | media | 6 | “Potencial de reposo” no está definido de manera explícita y delimitada. | El capítulo explica potencial endococlear y potencial receptor. | Confusión entre potencial intracelular de reposo, potencial endococlear y respuesta receptora. | Añadir comparación terminológica y valores solo con fuente fisiológica fiable. |
| R11 | media | 6 | “Transmisión paratimpánica” puede sugerir una vía única de conducción ósea. | El libro presenta múltiples mecanismos. | Modelo fisiológico desactualizado o excesivamente simple. | Explicar la terminología histórica y priorizar el modelo multimecanismo. |
| R12 | media | 7 | El programa escribe “Hass”; la denominación aceptada es Haas. | Diferencia terminológica entre programa y libro. | Propagación de un error ortográfico y confusión entre Haas y precedencia. | Usar “efecto de precedencia (incluye el efecto de Haas)” y registrar la corrección. |
| R13 | media | 7/9 | El tiempo de reverberación aparece primero como factor perceptual y después como magnitud física. | Orden del programa y del libro. | Introducir una fórmula antes de que exista una necesidad perceptual, o repetir sin propósito. | En U7 definir y escuchar/interpretar; en U9 formalizar decaimiento, absorción y cálculo. |
| R14 | media | 2 | Mecánica clásica y termodinámica comparten una sola unidad. | El alcance oficial reúne dos marcos conceptuales extensos. | Cambios abruptos de modelo y terminología. | Organizar dos bloques con un puente común: energía, medio material y disipación. |
| R15 | media | 5 | El libro amplía a muestreo, FFT, ventanas, fuga y espectrogramas. | Es contenido adicional al programa literal. | Consumir tiempo destinado a Fourier, filtros y medición; elevar la carga matemática. | Definir núcleo obligatorio y extensión según carga horaria; priorizar interpretación sobre algoritmo. |
| R16 | media | 8 | Riesgo de exceder el nivel de Física Acústica con procedimientos clínicos. | La unidad integra patologías, estudios y rehabilitación. | Confundir principios físicos con competencia diagnóstica o indicación clínica. | Delimitar qué explica la física y qué requiere asignaturas/protocolos clínicos específicos. |
| R17 | media | transversal | No hay evaluaciones auténticas ni resultados de cohortes para estimar dificultades. | Solo existen actividades internas del libro. | Resultados de aprendizaje y práctica desalineados con la evaluación real. | Solicitar parciales previos anonimizados, rúbrica o tabla de especificaciones. |
| R18 | media | transversal | Colisiones de símbolos entre capítulos. | `Q` puede ser calor o directividad; `k` rigidez o número de onda; `A` amplitud o área. | Errores de lectura al reutilizar fórmulas. | Adoptar la guía de notación transversal y calificar símbolos cuando compartan contexto. |
| R19 | media | 4 | Se concentran muchas magnitudes y niveles relacionados. | Presión, velocidad de partícula, intensidad, potencia, energía, RMS, referencias y suma de niveles. | Mezclar magnitud lineal con nivel logarítmico o sumar dB aritméticamente. | Usar un mapa estable magnitud → símbolo → unidad → nivel y problemas de contraste. |
| R20 | media | 5/7 | Frecuencia fundamental, pitch y timbre pueden confundirse. | Se introducen en unidades consecutivas desde dominios distintos. | Identificar pitch con f0 en todos los casos o timbre solo con armónicos. | Repetir ejemplos de fundamental ausente, misma f0 con espectros/envolventes distintos y señales aperiódicas. |
| R21 | media | 4/7 | Nivel de presión sonora y sonoridad pueden tratarse como sinónimos. | El curso transita de magnitud física a percepto. | Interpretación perceptual directa de cualquier cambio en dB. | Mantener lenguaje diferenciado y comparar igual SPL con distinta frecuencia/duración. |
| R22 | media | 9 | “Insonorización” es una etiqueta ambigua. | Puede reunir aislamiento y acondicionamiento. | Elegir soluciones físicas incorrectas para el problema. | Separar transmisión entre recintos, absorción interna y control de reverberación. |
| R23 | baja | 5 | La figura comparativa A/C/Z figura como pendiente o susceptible de mejora. | Revisión del capítulo y sus marcadores de figura. | Explicación excesivamente verbal de ponderaciones. | Generar figura propia a partir de una fuente normativa trazable. |
| R24 | baja | transversal | No se conoce disponibilidad de demostraciones, sonómetro, parlantes, auriculares o cabina. | No hay inventario de equipamiento docente. | Diseñar actividades imposibles de ejecutar o no comparables entre comisiones. | Registrar equipamiento, software, condiciones de aula y alternativas sin instrumental. |

## Contradicciones y diferencias que deben conservarse visibles

No se detectaron fórmulas centrales incompatibles entre las fuentes. Sí existen enunciados del programa que el libro matiza o actualiza:

- **CAE y frente de onda:** el programa sugiere una conversión esférica–cilíndrica; el libro la presenta como una idealización insuficiente.
- **Transmisión paratimpánica:** el libro evita atribuir la conducción ósea a una sola vía.
- **Reflejo acústico:** la latencia no se reduce a un valor único.
- **Curvas isofónicas:** una curva normativa debe identificarse por edición de norma, no por una ilustración genérica.
- **Umbral de dolor:** no se presenta como constante universal.
- **Efecto “Hass”:** se corrige a **Haas** y se ubica dentro del efecto de precedencia.
- **Ruido vocal:** se prefiere **ruido con espectro de habla**.
- **Insonorización:** se descompone en aislamiento y acondicionamiento.

Estas diferencias no deberían ocultarse: son oportunidades para enseñar el alcance de los modelos y la importancia de la terminología técnica.

## Problemas de secuencia

1. La Unidad 1 debe dejar realmente operativos razones, logaritmos, lectura de gráficos y unidades; de lo contrario, la dificultad reaparece como “problema de acústica” en U4 y U5.
2. La conservación de energía de U2 debe conectarse explícitamente con amortiguamiento, absorción y transmisión, no quedar aislada como termodinámica general.
3. U3 debe fijar la diferencia entre oscilación de partículas y propagación de la perturbación antes de hablar de velocidad del sonido.
4. U4 debe estabilizar magnitudes lineales y niveles antes de Fourier o medición.
5. U5 debe distinguir señal, sistema y representación antes de U6/U7.
6. U6 debe cerrar con un mapa causal de transducción antes de introducir perceptos en U7.
7. U7 introduce reverberación por su efecto en audición e inteligibilidad; U9 debe anunciarse como formalización posterior.
8. U8 depende de U6 y U7, pero también reutiliza dB HL, dB SL y dB SPL; esas escalas deben compararse explícitamente.
9. U10 vuelve sobre enmascaramiento después de U7 y audiometría después de U8; la repetición debe presentarse como aplicación clínica, no como reinicio.

## Conceptos que necesitan ejemplos adicionales

- Conversión entre período y frecuencia y lectura de prefijos.
- Diferencia masa/peso y presión/fuerza.
- Velocidad de partícula frente a velocidad de propagación.
- Promedio, valor pico y RMS en una senoide.
- Referencia de nivel y por qué dos cantidades en dB no son comparables sin contexto.
- Suma de fuentes coherentes, no coherentes y parcialmente correlacionadas.
- Ley de distancia con condiciones de campo libre y fuente ideal.
- Espectro de una señal frente a respuesta en frecuencia de un sistema.
- Fuga espectral y resolución mediante la misma señal observada con ventanas distintas, si se conserva la ampliación.
- Adaptación de impedancias del oído medio sin una “ganancia” universal.
- Potencial endococlear, potencial de reposo y potencial receptor.
- Frecuencia fundamental frente a pitch; espectro frente a timbre.
- Igual SPL con distinta sonoridad; igual sonoridad con distinto SPL.
- TTS frente a cambio permanente, evitando inferencias diagnósticas.
- Absorción frente a aislamiento.
- Ruido blanco por Hz frente a ruido rosa por octava.
- Enmascaramiento central, periférico y clínico; técnica de meseta si se incorpora.

## Fuentes externas necesarias

| Prioridad | Tema | Tipo de fuente requerida | Uso previsto |
|---|---|---|---|
| alta | Curvas isofónicas | norma ISO 226 vigente o datos primarios autorizados | figura normativa y ejemplos de nivel de sonoridad |
| alta | Ruido máximo permisible en audiometría | norma audiométrica vigente aplicable y documentación de transductores/vía | tabla por bandas y condiciones |
| alta | Riesgo por edad y exposición ocupacional | norma/modelo de predicción o estudio epidemiológico primario | cuantificación condicionada y trazable |
| alta | Recuperación tras exposición | estudios fisiológicos/audiológicos primarios o revisión académica | curvas no universales con condiciones |
| alta | Técnica clínica de enmascaramiento | protocolo o manual clínico adoptado por la cátedra | procedimiento, límites y ejercicios |
| media | Túnel de Corti y potenciales cocleares | tratado de anatomía/fisiología auditiva o artículo de revisión | completar U6 y evitar confusiones |
| media | Ponderaciones A/C/Z | norma de sonómetros o documentación técnica normativa | gráfico reproducible y terminología |
| media | ALCons e inteligibilidad | fuente original y bibliografía crítica | alcance, supuestos y límites |
| media | Exposición ocupacional y criterios preventivos | normativa nacional/institucional vigente | conectar Física Acústica con prevención sin universalizar límites |

Toda incorporación externa debe registrarse con autor u organización, título, edición/fecha, URL o identificador, fecha de acceso y función pedagógica.

## Decisiones pendientes del docente

1. Confirmar el programa vigente y si existe una versión posterior a 2025.
2. Informar carga horaria total, duración de cada encuentro y semanas asignadas a cada unidad.
3. Definir cuáles ampliaciones del libro son obligatorias, opcionales o solo material de consulta.
4. Precisar la profundidad matemática esperada para Fourier, muestreo, FFT y estadística del ruido.
5. Resolver si “transformación del frente de onda” se evaluará como enunciado idealizado o como análisis crítico del CAE real.
6. Elegir la bibliografía anatómica para completar túnel de Corti y potencial de reposo.
7. Autorizar/adquirir la fuente normativa para curvas isofónicas.
8. Elegir el modelo o estudio para riesgo combinado de edad y ruido, o decidir que se enseñará solo cualitativamente.
9. Identificar la norma audiométrica y jurisdicción aplicables a la cabina y al ruido ambiente.
10. Definir el protocolo clínico de enmascaramiento que se espera que el alumnado pueda aplicar.
11. Proporcionar evaluaciones anteriores, rúbricas o una tabla de especificaciones.
12. Confirmar equipamiento y software disponibles para demostraciones y prácticas.
13. Acordar terminología institucional para términos con variantes: acúfeno/tinnitus, sonoridad/loudness, PEAT/PEATC y conducto coclear/scala media.

## Criterio de avance

La arquitectura global puede considerarse suficientemente fundada para iniciar briefs cuando se validen el programa vigente, la carga horaria y el alcance de las ampliaciones. Las unidades 6 a 10 no deberían cerrarse como contenido definitivo hasta resolver las fuentes externas de prioridad alta. Ninguna de estas decisiones exige modificar el programa o el libro en esta etapa.
