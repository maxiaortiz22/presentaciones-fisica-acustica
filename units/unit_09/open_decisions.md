# Unidad 9 — Decisiones abiertas

## Propósito

Este registro reúne decisiones que afectan alcance, terminología, fuentes, secuencia, recursos, seguridad o tiempo. No constituye un storyboard. Las decisiones de prioridad alta deben resolverse antes de aprobar una secuencia slide por slide.

## Decisiones adoptadas para esta etapa

| ID | Decisión | Justificación |
|---|---|---|
| DA-U09-01 | No crear storyboard ni PowerPoint. | Solicitud explícita y flujo obligatorio del repositorio. |
| DA-U09-02 | No redactar texto visible ni notas del orador. | Esta etapa termina en brief, inventario, análisis y decisiones. |
| DA-U09-03 | Tratar U9 como carga conceptual alta. | Coincidencia entre arquitectura, cantidad de mecanismos y componente normativo. |
| DA-U09-04 | Usar fuente–trayecto–receptor como pregunta organizadora. | Es el hilo conductor del capítulo y permite localizar cada mecanismo sin atribuirlo todo a la fuente. |
| DA-U09-05 | Mantener separados divergencia, absorción atmosférica, reflexión, absorción material, transmisión, refracción y difracción. | Es la puerta de entrada de la arquitectura y previene el error conceptual dominante. |
| DA-U09-06 | Mantener separados nivel de potencia emitido y nivel de presión recibido. | Son magnitudes diferentes y organizan correctamente distancia/directividad. |
| DA-U09-07 | Interpretar “insonorización” como objetivo general, no como magnitud física. | Coincidencia entre capítulo y glosario transversal. |
| DA-U09-08 | Considerar LaTeX y PDF sustantivamente concordantes. | Se leyó el capítulo completo y se verificaron visualmente todas las pp. 235–259. |
| DA-U09-09 | Tratar las figuras del libro como fuentes conceptuales, no como assets finales. | Están diseñadas para página impresa y requieren reconstrucción, editabilidad y tipografía de aula. |
| DA-U09-10 | No incorporar fuentes externas nuevas ni valores normativos en esta etapa. | Las fuentes locales bastan para analizar; la brecha se registra sin inventar datos. |
| DA-U09-11 | No modificar `course_map.md`, `course_dependency_map.md` ni `content_coverage_matrix.csv`. | El pedido limita las salidas a cuatro archivos de U9; la discrepancia de localizadores queda registrada. |
| DA-U09-12 | Adoptar provisionalmente la notación de `style/notation_guide.md` para el futuro deck. | Evita colisiones entre reflexión, reducción sonora, transmisión, área y reverberación. |
| DA-U09-13 | Considerar central la comprensión cualitativa de refracción en sólidos, aunque el capítulo la trate brevemente. | Es un requisito explícito del programa. |
| DA-U09-14 | No tratar una lectura global en dB(A) como criterio de aptitud audiométrica. | Programa, capítulo, arquitectura y guía de notación exigen condiciones y bandas. |

## Decisiones pendientes

| ID | Prioridad | Decisión | Evidencia/tensión | Recomendación preliminar | Impacto si queda abierta | Estado |
|---|---|---|---|---|---|---|
| OD-U09-01 | Alta | Confirmar cantidad y duración de encuentros. | Ruta central estimada en 52–70 slides y cuatro bloques de carga muy alta. | Planificar tres encuentros; dos solo si Sabine/atmósfera cuantitativa se reducen y hay poca práctica. | Define central/complementario, ritmo y cantidad de recapitulaciones. | Pendiente de planificación docente. |
| OD-U09-02 | Alta | Definir profundidad de repaso de U4. | Distancia y directividad ya se derivaron en U4. | Recuperar significado, ecuación y condiciones en 3–5 slides; no repetir derivaciones completas. | Riesgo de redundancia o de comenzar sin prerrequisitos activos. | Pendiente para storyboard. |
| OD-U09-03 | Alta | Elegir notación visible para directividad. | Capítulo usa `Q`; guía transversal usa `Q_dir`. | Usar `Q_dir` en material visible y explicar que corresponde al `Q` del libro. | Inconsistencia con U4/guía o colisión con calor. | Pendiente de consistencia global. |
| OD-U09-04 | Alta | Elegir símbolo para velocidad/componente del viento. | Capítulo usa `u`, reservado en la guía para velocidad de partícula. | Usar `v_viento` o símbolo institucional explícito; conservar `u` solo en cita del libro. | Confusión entre viento y oscilación de partículas. | Pendiente de notación. |
| OD-U09-05 | Alta | Normalizar símbolos del balance energético. | Capítulo usa `𝓡`, `α`, `τ`; guía propone `R_E`, `α`, `τ_E`. | Adoptar `R_E + α + τ_E = 1` y distinguir de `R_p`, `R_I` y `R`. | Colisiones graves entre reflexión y aislamiento. | Recomendación lista; falta validar con unidades previas. |
| OD-U09-06 | Alta | Normalizar `A`, `RT_60` y masa superficial. | Guía usa `A_eq`, `T_60`; capítulo usa `A`, `RT_60`, `m`. | Usar `A_eq`, `T_60` y evaluar `m_s` para masa superficial. | Inconsistencia visual y ambigüedad de símbolos. | Pendiente de notación. |
| OD-U09-07 | Alta | Definir peso de la absorción atmosférica. | Es ampliación del libro, relevante para separar mecanismos, pero no hay coeficientes locales. | Mantener concepto y ecuación de estructura en ruta central; gráfico/ejemplo numérico solo con fuente trazable. | Puede omitirse un mecanismo real o inventarse una corrección. | Recomendación preliminar. |
| OD-U09-08 | Media | Definir profundidad de humedad y turbulencia. | Influyen en propagación, pero el programa no las nombra y el capítulo las trata brevemente. | Introducir como variables que limitan reglas universales; desarrollo cuantitativo en complemento. | Sobrecarga atmosférica o explicación incompleta. | Pendiente según tiempo. |
| OD-U09-09 | Alta | Diseñar el contraste uniforme/gradiente. | Es el nudo principal de temperatura y viento. | Dos pares coordinados: “qué cambia” y “qué no cambia”, con diagramas y una recapitulación. | El estudiante aplicará correcciones universales de nivel. | Pendiente para storyboard/diagramas. |
| OD-U09-10 | Alta | Ampliar refracción en sólidos. | Programa explícito; capítulo ofrece solo un párrafo cualitativo. | Incluir interfaz aire–sólido con reflexión, transmisión, cambio de dirección y conversión modal cualitativa; Snell en respaldo o central breve. | Cobertura programática formal pero pedagógicamente insuficiente. | Pendiente de diseño y posible fuente adicional. |
| OD-U09-11 | Media | Definir si mostrar la ley de Snell acústica. | Ayuda a formalizar refracción en interfaz, pero suma ángulos, modos y supuestos. | Mostrar relación cualitativa en núcleo; ecuación solo si los ángulos y modos pueden explicarse sin sobrecarga. | Exceso de formalismo o tratamiento superficial. | Pendiente según tiempo. |
| OD-U09-12 | Alta | Diferenciar coeficientes de reflexión. | U4 usa coeficientes de presión/intensidad; U9 introduce fracción energética genérica. | Incorporar una comparación breve y declarar qué magnitud usa cada símbolo. | Se mezclarán amplitud, intensidad y energía en el balance. | Pendiente para storyboard. |
| OD-U09-13 | Alta | Decidir profundidad de reverberación y Sabine. | Programa U9 no nombra Sabine; U7 introdujo reverberación; libro la formaliza y matriz la marca `out_of_scope`. | Mantener definición, `A_eq`, un ejemplo de Sabine y límites en el núcleo o complemento cercano. | Se pierde continuidad con U7 o se desplaza el foco del programa. | Pendiente docente. |
| OD-U09-14 | Media | Evaluar si introducir modelos alternativos a Sabine. | Sabine pierde precisión en recintos pequeños/muy absorbentes. | Nombrar el límite sin desarrollar Eyring u otros; dejarlos en respaldo si se requieren. | Sobrecarga o falsa universalidad. | Recomendación preliminar. |
| OD-U09-15 | Alta | Definir estrategia visual de reflexión–eco–reverberación. | Mezcla mecanismo físico, señal temporal y percepción. | Usar respuesta al impulso sintética o línea temporal, con vínculo a U7. | Persistirá la equivalencia “una reflexión = reverberación”. | Pendiente de gráfico/animación. |
| OD-U09-16 | Alta | Definir tratamiento de difracción cuantitativa. | El programa exige `λ`; el capítulo rechaza atenuación sin geometría. | Calcular `λ` y comparar escalas; no calcular atenuación de barrera en ruta central. | Inventar una regla universal o dejar difracción demasiado vaga. | Recomendación lista; falta validar. |
| OD-U09-17 | Alta | Validar la forma didáctica de la ley de masas. | El término constante y el campo de incidencia dependen de convención/fuente. | Enseñar primero la pendiente relativa; usar valor absoluto solo tras verificar convención bibliográfica. | Resultado numérico presentado como universal o constructivo. | Pendiente técnico. |
| OD-U09-18 | Alta | Elegir término dominante para `R`: pérdida por transmisión o índice de reducción sonora. | El capítulo usa ambos según contexto; la guía reserva `R` para índice de reducción. | Usar “índice de reducción sonora `R`” cuando corresponda y explicar `TL` como equivalencia contextual, no alternarlos sin definición. | Confusión entre descriptor, diferencia de niveles y aislamiento. | Pendiente terminológica. |
| OD-U09-19 | Media | Definir profundidad de resonancia, rigidez y coincidencia. | Necesarios para limitar ley de masas, pero pertenecen a acústica constructiva más avanzada. | Mostrar zonas y nombrar mecanismos; detalles y frecuencia crítica en complemento/respaldo. | Ley de masas parece universal o bloque se vuelve demasiado técnico. | Recomendación preliminar. |
| OD-U09-20 | Alta | Fijar tratamiento de acondicionamiento, aislamiento e insonorización. | Programa exige aislamiento/insonorización; glosario añade acondicionamiento. | Comparación central por objetivo, mecanismo, magnitud y verificación; insonorización como término paraguas. | Confusión profesional muy probable. | Recomendación lista; falta validar. |
| OD-U09-21 | Alta | Definir alcance constructivo de cabinas. | Interés aplicado puede derivar a selección de materiales o diseño. | Enseñar sistema, rutas y verificación; no dimensionar ni especificar soluciones. | Recomendaciones constructivas simplistas o fuera de competencia. | Recomendación lista; falta validar. |
| OD-U09-22 | Alta | Seleccionar norma para ruido ambiente máximo. | Programa obligatorio; bibliografía cita ISO 8253-1, ISO 8253-2 y ANSI/ASA S3.1. | Determinar qué norma/edición y adopción local usará la cátedra antes de construir tablas. | Cobertura normativa incompleta o valores inaplicables. | Pendiente de fuente y decisión docente. |
| OD-U09-23 | Alta | Conseguir la fuente completa y versionada para la tabla normativa. | El repositorio solo contiene metadatos/citas, no el texto completo reproducible. | Incorporar fuente autorizada o tabla docente con trazabilidad explícita y permiso de uso. | No puede verificarse ni reproducirse la tabla. | Pendiente documental. |
| OD-U09-24 | Alta | Definir escenario audiométrico de la tabla. | Los límites dependen de vía, transductor, atenuación, bandas y menor nivel de prueba. | Elegir uno o más casos claramente rotulados; no fusionarlos en un “límite de cabina”. | Tabla pedagógicamente engañosa. | Pendiente junto con OD-U09-22. |
| OD-U09-25 | Alta | Definir adopción/jurisdicción aplicable. | ISO/ANSI no equivalen automáticamente a requisito local argentino/UCASAL. | Verificar criterio institucional y normativa local antes de afirmar obligatoriedad. | Afirmación normativa incorrecta. | Pendiente de cátedra/institución. |
| OD-U09-26 | Alta | Decidir cómo mostrar dB(A) frente a bandas. | Error central: “valor bajo en dB(A) certifica”. | Contrastar un descriptor global con una tabla por bandas y condiciones, sin inventar datos. | Se perpetúa la idea errónea del programa aplicado. | Pendiente de norma y gráfico. |
| OD-U09-27 | Alta | Seleccionar ejercicios para la ruta central. | El capítulo contiene 36 grupos/consignas y soluciones extensas. | Una comprobación por bloque, 3–4 cálculos seleccionados y un caso integrador; resto a respaldo/guía. | Deck sobredimensionado o sin práctica distribuida. | Pendiente para storyboard. |
| OD-U09-28 | Alta | Reconstruir los seis diagramas U9 y dos recordatorios U4. | Son correctos, pero contienen texto pequeño y notación no normalizada. | Reconstruir editables con `diagram-generation`, a tamaño real y con validación renderizada. | Ilegibilidad, colisiones y pérdida de editabilidad. | Pendiente de producción. |
| OD-U09-29 | Media | Definir si dividir el diagrama de cabina. | Presenta envolvente, tratamiento, seis componentes y tres rutas. | Reservar slide completa y revelar por etapas o dividir “elementos” y “rutas”. | Fuente pequeña y flechas sobre texto. | Pendiente de storyboard. |
| OD-U09-30 | Media | Definir gráficos cuantitativos propios. | Varias relaciones se beneficiarían de curvas, pero no todas requieren datos externos. | Generar distancia, `c(θ)`, `λ(f)`, `τ_E↔R` y ley de masas con ecuaciones; atmósfera/materiales solo con datos verificados. | Exceso de gráficos o datos sin fuente. | Pendiente de `chart-generation`. |
| OD-U09-31 | Alta | Seleccionar imágenes técnicas y licencias. | No hay fotos inventariadas; cabinas y montajes reales aportarían contexto. | Priorizar organismos, universidades, fabricantes técnicos y documentación; registrar licencia y propósito. | Stock decorativo, publicidad o falsa equivalencia espuma–aislamiento. | Pendiente de `asset-curation`. |
| OD-U09-32 | Media | Definir animaciones. | Gradientes, balance y rutas se benefician del revelado. | Usarlas solo para comparar estados o mostrar trayectos; conservar versión estática completa. | Dependencia del efecto o sobrecarga visual. | Pendiente para storyboard. |
| OD-U09-33 | Alta | Definir seguridad y alcance de demostraciones sonoras. | Reverberación y medición invitan a audios o pruebas en aula. | Usar niveles seguros, material pregrabado o sintético, alternativa visual y ninguna pretensión de calibración/certificación. | Exposición innecesaria o interpretación metrológica falsa. | Pendiente antes de assets. |
| OD-U09-34 | Media | Programar revisión pedagógica específica. | U9 no está entre U4–U7, pero tiene alta carga y riesgo normativo. | Revisar storyboard con foco en separación de mecanismos, hipótesis y límites antes de redactar. | Un deck correcto visualmente puede enseñar reglas universales incorrectas. | Pendiente de responsable/etapa. |
| OD-U09-35 | Media | Corregir localizadores U9 en la arquitectura global. | `content_coverage_matrix.csv` refiere a numeración anterior del capítulo. | Actualizar `book_section` con `course-architecture` en una tarea posterior, sin cambiar estados. | Trazabilidad defectuosa entre matriz y fuente. | Fuera de esta tarea. |
| OD-U09-36 | Media | Verificar si el título visible llevará “a la propagación”. | Programa incluye “a”; libro y nombre solicitado no. | Usar el título solicitado/del libro y conservar la forma oficial en metadatos o notas. | Diferencia editorial menor pero visible. | Recomendación preliminar. |

## Decisiones de frontera curricular recomendadas

| Tema | Núcleo U9 | Puente permitido | Desarrollo reservado |
|---|---|---|---|
| Termodinámica del aire | Relación `c`, temperatura, presión y densidad; estado frente a gradiente. | Humedad y altitud como variables relacionadas. | Termodinámica formal y meteorología completa. |
| Ondas | `λ = c/f`, escala geométrica, reflexión/refracción/difracción. | Conversión modal cualitativa. | Ecuaciones de ondas elásticas en sólidos. |
| Niveles y campo | Distancia, directividad, emisión y recepción. | Combinación conceptual de términos. | Derivaciones completas de U4 y modelos numéricos profesionales. |
| Recintos | Reflexión, reverberación, `A_eq`, `T_60`, acondicionamiento. | Sabine con un ejemplo y límites. | Diseño arquitectónico, STI/SII y modelos avanzados. |
| Aislamiento | Transmisión, índice `R`, ley de masas, fugas y rutas laterales. | Resonancia/rigidez/coincidencia como límites. | Diseño multicapa, cálculos constructivos y especificación de materiales. |
| Cabinas | Sistema, rutas, tratamiento interior y verificación. | Lectura de tabla normativa seleccionada. | Diseño, compra, certificación e inspección profesional. |
| Ruido | Ruido ambiente como condición y variable por bandas. | Puente a control fuente–trayecto–receptor. | Tipos, estadística, exposición y enmascaramiento en U10. |
| Audiometría | Condiciones ambientales, vía, transductor y menor nivel de prueba. | Necesidad de norma/procedimiento. | Técnica clínica completa, calibración y diagnóstico. |

## Condiciones de entrada al storyboard

Antes de crear `storyboard.md` deberían quedar resueltas, como mínimo:

1. cantidad y duración de encuentros;
2. profundidad del repaso de U4;
3. notación de `Q_dir`, viento, `R_E`, `τ_E`, `A_eq`, `T_60` y masa superficial;
4. profundidad y representación de absorción atmosférica;
5. ampliación de refracción en sólidos;
6. peso central o complementario de Sabine;
7. convención y alcance de la ley de masas;
8. norma, edición, fuente completa, adopción y escenario para ruido máximo;
9. selección de ejercicios centrales;
10. estrategia de reconstrucción de ocho visuales heredados;
11. necesidad de imágenes técnicas y animaciones;
12. criterios de seguridad y alcance para demostraciones;
13. responsable de la revisión pedagógica/normativa.

Si la fuente normativa aún no está disponible, puede planificarse la estructura general del storyboard, pero las slides con valores máximos deben permanecer bloqueadas y no redactarse con cifras reconstruidas de memoria o fuentes secundarias.
