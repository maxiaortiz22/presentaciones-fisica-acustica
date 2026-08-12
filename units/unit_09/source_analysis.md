# Unidad 9 — Análisis de fuentes

## Jerarquía aplicada

Se aplicó la jerarquía definida en `AGENTS.md`:

1. programa oficial 2025;
2. capítulo 9 del libro en LaTeX;
3. capítulo 9 del libro publicado en PDF;
4. arquitectura curricular (`course_map.md`, `course_dependency_map.md` y `content_coverage_matrix.csv`);
5. guías transversales de estilo, notación y glosario;
6. bibliografía académica y normativa ya citada en el capítulo.

No se incorporaron fuentes externas nuevas ni datos no presentes en el repositorio. Las necesidades normativas y cuantitativas detectadas se registran como decisiones pendientes.

## Disponibilidad y método de revisión

| Fuente | Ubicación | Revisión realizada |
|---|---|---|
| Programa oficial | `context/programa/Programa de Física Acústica.pdf` | Extracción textual completa de 6 páginas de contenido; alcance U9 en p. 5 y objetivos/metodología en pp. 1–2. Revisión visual de la p. 5. |
| Libro LaTeX | `context/libro_latex/chapters/09-propagacion-sonido.tex` | Lectura completa: contenido, 10 relaciones/modelos cuantitativos, 6 figuras U9, ejercicios, respuestas, glosario y fuentes. |
| Figuras LaTeX | `context/libro_latex/figures/tikz/unidad-9/` y dos figuras de U4 | Lectura de los seis archivos U9 y de propagación esférica/directividad de U4, incluidos propósito y notas de accesibilidad. |
| Bibliografía LaTeX | `context/libro_latex/bibliography/references.bib` | Revisión de las claves citadas por U9 y de sus metadatos locales. |
| Libro PDF | `context/libro_pdf/Física Acústica para Fonoaudiología.pdf` | Capítulo completo localizado en pp. 235–259; extracción textual y revisión visual de todas las páginas 235–259. La p. 260 está en blanco y U10 comienza en p. 261. |
| Mapa del curso | `course_map.md` | Función, alcance, resultados, carga, continuidad y alerta normativa de U9. |
| Dependencias | `course_dependency_map.md` | Dependencias U2–U5/U7 → U9, puente U9 → U10, errores previsibles y evidencia mínima. |
| Matriz de cobertura | `content_coverage_matrix.csv` | Revisión de U09-01 a U09-12 y U09-X1; comparación de localizadores con el capítulo actual. |
| Sistema visual | `style/presentation_style_guide.md` | Principios, densidad, gráficos, ecuaciones, tablas, diagramas, animaciones, accesibilidad y editabilidad. |
| Notación | `style/notation_guide.md` | Reglas generales y secciones de propagación/recintos; detección de colisiones de símbolos. |
| Glosario | `style/glossary.md` | Definiciones de reflexión, absorción, transmisión, refracción, difracción, reverberación, acondicionamiento, aislamiento e insonorización. |

El directorio `units/unit_09/` contenía únicamente `.gitkeep`; no existía brief, storyboard ni deck previo que conservar o comparar.

## Alcance obligatorio extraído del programa

La formulación original del programa, p. 5, es:

> Factores que afectan a la propagación del sonido. Distancia a la fuente. Fuentes direccionales. Temperatura ambiente. Velocidad y dirección del viento. Presión atmosférica. Efectos de las superficies sobre el ruido. Reflexión. Absorción. Refracción del sonido en sólidos y en la atmósfera. Difracción y longitud de onda. Aislamiento. Insonorización. Cabinas sonoamortiguadas: ley de masas, ruido máximo permitido para audiometrías.

Para el brief se normalizan solo aspectos editoriales o terminológicos:

- el título de trabajo conserva la forma del libro, sin la preposición “a”, pero el título oficial queda registrado;
- “fuentes direccionales” se desarrolla mediante directividad, factor e índice;
- “efectos de las superficies sobre el ruido” se interpreta físicamente como reflexión, absorción, transmisión y efectos sobre el campo;
- “refracción en sólidos” se encuadra como refracción en interfaces fluido–sólido y posible conversión modal, sin diseño especializado;
- “insonorización” se conserva como término del programa, pero se trata como objetivo general ambiguo y no como magnitud;
- “cabinas sonoamortiguadas” se mantiene en la trazabilidad y se presenta como sistema, no como una caja revestida;
- “ruido máximo permitido” no se convierte en un valor único: exige norma, edición, vía, transductor, bandas, menor nivel de prueba y jurisdicción.

Los objetivos generales del programa también exigen comprender la propagación, operar con magnitudes, interpretar gráficos y combinar teoría con ejercicios. El capítulo responde bien a ese mandato al incluir modelos, aplicaciones, interpretación visual y problemas.

## Comparación programa–LaTeX–PDF

| Tema | Programa | LaTeX | PDF | Estado y decisión |
|---|---|---|---|---|
| Distancia a la fuente | Obligatoria | Ecuación de cambio de `L_p`, condiciones y ejemplo. | Concordante, p. 237. | Cubierta; recuperar U4 sin repetir derivación completa. |
| Fuentes direccionales | Obligatorio | `Q`, `DI`, comparación a igual potencia/distancia y ejemplo. | Concordante, pp. 237–238. | Cubierto; normalizar a `Q_dir` y evitar doble conteo. |
| Temperatura ambiente | Obligatoria | Aproximación de `c(θ)`, `λ = c/f`, estado uniforme y gradiente. | Concordante, pp. 238–239. | Cubierta con buena profundidad introductoria. |
| Velocidad y dirección del viento | Obligatorio | Viento uniforme, `c_ef`, gradiente, propagación a favor/en contra y turbulencia. | Concordante, pp. 239–240. | Cubierto; resolver símbolo de viento y separar tiempo/trayectoria/nivel. |
| Presión atmosférica | Obligatoria | Relación con densidad y `c`; altitud y ausencia de corrección universal. | Concordante, pp. 240–241. | Cubierta conceptualmente; conviene una visualización adicional. |
| Efectos de superficies | Obligatorio | Balance energético, reverberación, transmisión, aislamiento y rutas. | Concordante, pp. 241–247. | Cubierto y ampliado. |
| Reflexión | Obligatoria | Destino energético, llegada individual y relación con reverberación. | Concordante, pp. 241–243. | Cubierta; diferenciar coeficiente de presión, intensidad y energía. |
| Absorción | Obligatoria | Absorción atmosférica y material, coeficiente y área equivalente. | Concordante, pp. 241–243. | Cubierta; separar claramente los dos contextos. |
| Refracción atmosférica | Obligatoria | Gradientes térmicos/viento y definición general. | Concordante, pp. 239–243. | Cubierta cualitativamente y con dos figuras. |
| Refracción en sólidos | Obligatoria | Un párrafo sobre interfaz, Snell, tipos de onda y conversión modal. | Concordante, p. 243. | **Cobertura mínima.** Requiere más explicación y un diagrama, sin profundizar en elasticidad sólida. |
| Difracción y longitud de onda | Obligatoria | Relación `λ/obstáculo`, ejemplo 250/4000 Hz y figura comparativa. | Concordante, pp. 243–244. | Cubierta; no asignar atenuación sin geometría. |
| Aislamiento | Obligatorio | Transmisión, índice de reducción, rutas laterales y sistema constructivo. | Concordante, pp. 244–247. | Cubierto; mantenerlo separado de absorción. |
| Insonorización | Obligatoria | Término general contrastado con acondicionamiento y aislamiento. | Concordante, p. 246. | Cubierta con precisión terminológica. |
| Cabinas sonoamortiguadas | Obligatorio | Sistema completo, tratamiento interior, envolvente y rutas de ingreso. | Concordante, pp. 247–248. | Cubierta y bien aplicada a Fonoaudiología. |
| Ley de masas | Obligatoria | Fórmula didáctica, tendencia, límites, figura y ejemplo relativo. | Concordante, pp. 245–246. | Cubierta; validar convención y término constante antes de usar valores absolutos. |
| Ruido máximo permitido para audiometrías | Obligatorio | Explica dependencias y documentación necesaria; no incluye tabla. | Concordante, pp. 247–248 y 259. | **Cobertura conceptual / expansión externa pendiente.** Requiere norma completa y aplicable para valores. |
| Absorción atmosférica | No explícita | Coeficiente dependiente de frecuencia/atmósfera y ecuación combinada. | Concordante, p. 241. | Ampliación importante, sin ejemplo numérico local. |
| Reverberación y Sabine | No explícitos en U9; reverberación se menciona en U7 | Definición, `T_60`, `A_eq`, fórmula, ejemplo y límites. | Concordante, pp. 242–243. | Ampliación importante que formaliza U7. |
| Acondicionamiento acústico | No explícito como término | Diferencia objetivo interior de aislamiento. | Concordante, p. 246. | Ampliación importante para precisar “insonorización”. |
| Pérdida por transmisión y rutas laterales | No explícitas | Relación `τ ↔ R`, medición y rutas débiles. | Concordante, pp. 244–247. | Ampliación necesaria para comprender aislamiento real. |

La matriz de cobertura coincide en el estado general: U09-01 a U09-11 aparecen `covered`, U09-12 `external_expansion` y U09-X1 `out_of_scope`. Sin embargo, sus localizadores de sección no coinciden con la numeración actual del capítulo y deben actualizarse en una tarea futura de arquitectura.

## Correspondencia LaTeX–PDF

### Verificación estructural

El PDF reproduce la estructura sustantiva del LaTeX:

| Contenido | LaTeX | PDF |
|---|---|---|
| Propósito y objetivos | `sec:u9-proposito` | pp. 235–236 |
| Conocimientos previos y situación | `sec:u9-previos`, `sec:u9-situacion` | p. 236 |
| Distancia, directividad y emisión/recepción | `sec:u9-distancia-directividad` | pp. 237–238 |
| Condiciones atmosféricas | `sec:u9-atmosfera` | pp. 238–241 |
| Superficies, reverberación, refracción y difracción | `sec:u9-superficies` | pp. 241–244 |
| Aislamiento, ley de masas y objetivos | `sec:u9-aislamiento` | pp. 244–246 |
| Cabinas y ruido ambiente | `sec:u9-cabinas` | pp. 247–248 |
| Relación profesional, errores y síntesis | `sec:u9-fonoaudiologia`, `sec:u9-errores`, `sec:u9-sintesis` | pp. 248–250 |
| Ejercicios y autoevaluación | `sec:u9-ejercicios` | pp. 250–253 |
| Soluciones y orientaciones | `sec:u9-soluciones` | pp. 254–258 |
| Glosario y fuentes | `sec:u9-glosario`, `sec:u9-fuentes` | pp. 258–259 |

No se detectaron omisiones, ecuaciones divergentes, figuras faltantes ni diferencias sustantivas entre las dos versiones. El PDF parece una compilación coherente del LaTeX disponible.

### Verificación visual

La revisión de todas las páginas 235–259 confirmó:

- **pp. 235–236:** apertura, objetivos, prerrequisitos y caso organizador completos; la densidad es apropiada para libro, no para slides;
- **pp. 237–238:** ecuaciones de distancia y directividad legibles, pero con varios párrafos que deberán dividirse;
- **pp. 239–240:** diagramas térmicos y de viento conceptualmente claros; sus rótulos son demasiado pequeños para proyectarlos sin reconstrucción;
- **pp. 241–242:** absorción atmosférica y balance de superficie bien separados; el balance es una base visual fuerte;
- **pp. 242–243:** Sabine, ejemplo, refracción y difracción comparten pocas páginas y requerirán secuencias separadas;
- **p. 244:** la figura de difracción y el inicio de aislamiento ocupan la misma página; deben independizarse;
- **pp. 245–246:** ley de masas, límites y tres objetivos están bien organizados, pero la figura necesita mayor jerarquía y tamaño;
- **pp. 247–248:** la cabina como sistema es pedagógicamente sólida, aunque contiene demasiados elementos y rótulos para media slide;
- **pp. 249–250:** errores, síntesis y ejercicios son reutilizables como preguntas/recapitulación, no como texto continuo;
- **pp. 250–258:** banco de actividades y soluciones amplio; conviene seleccionar, distribuir y reservar respuestas completas;
- **p. 259:** las fuentes documentan correctamente por qué no hay tabla normativa reproducida;
- **p. 260:** página en blanco de separación; no pertenece al contenido sustantivo de U9.

La maquetación del libro es adecuada para lectura cercana. No constituye una referencia directa de tamaño tipográfico, cantidad de texto o composición de diapositivas.

## Fórmulas, magnitudes y ejemplos localizados

| Relación/modelo | Ubicación LaTeX/PDF | Magnitudes | Ejemplo disponible | Observación |
|---|---|---|---|---|
| Cambio de `L_p` con distancia | Ecuación 9.1; p. 237 | `L_p`, `r` | 90 dB SPL; 0,50 → 1,00 m | Central; regla condicionada. |
| `DI = 10 log10 Q` | Ecuación 9.2; pp. 237–238 | `Q`, `DI`, ángulos | `Q = 4` → 6,02 dB | Central; no sumar dos veces. |
| `L_W = 10 log10(W/W_0)` | Texto 9.4.3; p. 238 | potencia y nivel de potencia | Sin ejemplo independiente | Recordatorio para diferenciar emisión y recepción. |
| `c(θ)` lineal | Ecuación 9.3; pp. 238–239 | `c`, temperatura | 5 °C y 25 °C | Central como aproximación acotada. |
| `λ = c/f` | Texto y ejercicios; pp. 239, 244, 252, 256 | `λ`, `c`, `f` | 250/4000 Hz; 125/500/4000 Hz | Central para atmósfera y difracción. |
| `c_ef = c + u cos ψ` | Ecuación 9.4; pp. 239–240 | rapidez, viento, ángulo | Sin ejemplo numérico | Conceptual; resolver colisión de `u`. |
| `c = √(γp_a/ρ_a)` | Ecuación 9.5; p. 240 | presión, densidad, `γ` | Sin ejemplo numérico | Importante para negar corrección aislada. |
| Distancia + absorción atmosférica | Ecuación 9.6; p. 241 | `L_p`, `r`, `a_atm` | Sin coeficiente local | Complemento/central breve; no inventar datos. |
| Balance `R + α + τ = 1` | Ecuación 9.7; pp. 241–242 | fracciones energéticas | 0,55 + 0,30 → 0,15 | Central; normalizar símbolos. |
| Sabine y área equivalente | Ecuación 9.8; pp. 242–243 | `V`, `S_i`, `α_i`, `A`, `RT_60` | aula 8 × 6 × 3 m → 0,52 s | Importante; normalizar `A_eq`, `T_60`. |
| `R = 10 log10(1/τ)` | Ecuación 9.9; pp. 244–245 | transmisión e índice | `τ = 0,01` → 20 dB; `0,001` → 30 dB | Central; distinguir medición real. |
| Ley de masas | Ecuación 9.10; pp. 245–246 | masa superficial, frecuencia, reducción | duplicación → +6,02 dB | Central como tendencia; cautela con término constante. |

## Ampliaciones del libro respecto del programa

El libro añade contenido pedagógicamente útil:

1. la situación fuente–trayecto–receptor como organizador;
2. diferencia entre nivel de potencia emitido y presión recibida;
3. condiciones explícitas de distancia y directividad;
4. distinción entre estados atmosféricos uniformes y gradientes;
5. absorción atmosférica dependiente de frecuencia, humedad, presión y temperatura;
6. tratamiento conjunto de presión, densidad y altitud;
7. transmisión energética y balance ideal en superficies;
8. reverberación, área equivalente y fórmula de Sabine;
9. diferencia entre eco, reflexión y reverberación;
10. pérdida por transmisión e índice de reducción sonora;
11. rutas laterales, fugas y debilidades del conjunto;
12. acondicionamiento acústico como término necesario para precisar insonorización;
13. cabina como sistema funcional y no como revestimiento;
14. banco extenso de ejercicios, aplicaciones y distractores;
15. glosario y revisión bibliográfica de afirmaciones atmosféricas, constructivas y normativas.

Estas ampliaciones sostienen la comprensión y previenen errores. Sabine y la absorción atmosférica pueden ocupar una ruta central acotada o un complemento cercano según tiempo; el diseño constructivo detallado permanece fuera de alcance.

## Diferencias, tensiones y vacíos documentales

### 1. Localizadores desactualizados en `content_coverage_matrix.csv`

La matriz asigna distancia a 9.2, directividad a 9.3, atmósfera a 9.4 y cabinas a 9.15. En el capítulo actual esas secciones son, respectivamente, 9.4, 9.4, 9.5 y 9.8. La cobertura y los estados son válidos, pero los localizadores no lo son. Deben corregirse más adelante mediante `course-architecture` para mantener trazabilidad global.

### 2. Ruido máximo permitido sin tabla normativa local

El programa exige el tema y el libro explica correctamente las dependencias, pero no reproduce valores. La bibliografía local cita ISO 8253-1:2010, ISO 8253-2:2009 y ANSI/ASA S3.1-1999 (R2023), aunque el repositorio no contiene las normas completas ni una decisión de adopción/jurisdicción. No puede redactarse una tabla hasta resolver esa fuente.

### 3. Refracción en sólidos con cobertura mínima

El programa la exige explícitamente. El capítulo menciona Snell acústica, tipos de onda y conversión modal, pero no incluye ecuación, ejemplo ni figura. La ruta central necesita al menos un diagrama de interfaz y una explicación cualitativa; el desarrollo matemático completo puede quedar en respaldo.

### 4. Notación del capítulo frente a la guía transversal

El LaTeX usa `Q`, `u` para viento, `R` caligráfica como fracción reflejada, `τ`, `A` y `RT_60`. La guía prefiere `Q_dir`, reserva `u(t)` para velocidad de partícula, propone `R_E`, `τ_E`, `A_eq` y `T_60`. El futuro deck debe seguir la guía y registrar la equivalencia con el libro.

### 5. Masa superficial

El capítulo usa `m`, que también representa masa básica. La unidad puede definirla con claridad o usar `m_s` en la presentación. La decisión debe coordinarse con la notación global antes de redacción.

### 6. Ley de masas absoluta

La forma `20 log10(mf) − 47 dB` se presenta como aproximación didáctica bajo incidencia difusa media y con unidades normalizadas. El propio capítulo advierte que término constante, campo de incidencia y límites deben verificarse. Es seguro enseñar la tendencia relativa; usar valores absolutos requiere confirmar la convención elegida.

### 7. Sabine frente al alcance del programa

La matriz marca Sabine como `out_of_scope` porque el programa no la nombra en U9. Sin embargo, la arquitectura indica que U9 formaliza la reverberación introducida en U7 y el capítulo incluye un desarrollo útil. Debe decidirse si será central breve, complemento o respaldo; no conviene eliminarla sin dejar un puente físico de reverberación.

### 8. Absorción atmosférica sin datos numéricos

El capítulo incluye la estructura de una estimación, pero no valores de `a_atm`. Para primer año puede bastar la dependencia cualitativa y la separación de mecanismos. Un gráfico cuantitativo exige datos trazables de una norma o fuente académica.

### 9. “Insonorización” como término programático ambiguo

Programa y capítulo usan la palabra, pero el glosario recomienda reservarla como objetivo general y preferir acondicionamiento o aislamiento según el mecanismo. El deck debe mostrar el término oficial sin reforzar una falsa magnitud combinada.

### 10. Campo libre y modelos ideales

El capítulo recupera U4 y añade correctamente límites. La futura presentación no debe repetir una derivación larga ni presentar el entorno real como suma automática de “correcciones” independientes. La integración final debe ser conceptual y metrológica.

### 11. Frontera con U10

U9 explica propagación, recintos, aislamiento y condiciones de cabina. U10 conserva caracterización estadística/espectral del ruido, exposición y control. El caso de la avenida puede anticipar control fuente–trayecto–receptor sin desarrollar todavía tipos de ruido o enmascaramiento.

### 12. Terminología de rapidez y velocidad

El programa y el libro usan “velocidad de propagación”; la guía admite esa forma convencional, pero prefiere “rapidez” cuando puede confundirse con magnitudes vectoriales. En una misma explicación debe distinguirse `c`, velocidad de partícula y vector/componente de viento.

## Qué puede pasar casi directamente a diapositivas

- la pregunta organizadora y el caso fuente–trayecto–receptor;
- la ecuación de distancia, su ejemplo y su lista de condiciones;
- la definición comparativa de directividad y el ejemplo `Q = 4`;
- el contraste temperatura uniforme/gradiente;
- los dos diagramas atmosféricos como estructura visual;
- la frase “la fuente fija la frecuencia; cambia `c` y, por lo tanto, `λ`”;
- el balance energético de una partición;
- la distinción reflexión–reverberación–eco;
- la comparación de difracción para longitudes de onda diferentes;
- el ejemplo de Sabine, dividido en pasos;
- la relación entre transmisión e índice de reducción;
- la tendencia de la ley de masas y sus límites;
- la comparación de tres objetivos acústicos;
- el diagrama de cabina como sistema;
- las condiciones mínimas de una futura tabla normativa;
- los errores frecuentes, ejercicios visuales y aplicaciones.

Las ideas, relaciones y preguntas son transferibles. La densidad textual, la notación no normalizada y la composición de página no lo son.

## Qué necesita más explicación o recursos

| Contenido | Necesidad | Motivo |
|---|---|---|
| Emisión frente a recepción | Diagrama y ejemplo comparativo | Evita atribuir todo cambio a la fuente. |
| Distancia y directividad | Visual combinado y actividad | Se aplican juntas, pero no son el mismo mecanismo. |
| Estado uniforme y gradiente | Diagramas por etapas | Rapidez, tiempo, trayectoria y nivel compiten conceptualmente. |
| Presión/densidad/altitud | Comparación de variables y supuestos | La ecuación invita a una regla aislada incorrecta. |
| Absorción atmosférica | Gráfico con fuente o explicación cualitativa | No hay coeficientes locales trazables. |
| Coeficientes de reflexión | Tabla de magnitudes | Presión, intensidad y energía usan símbolos/relaciones diferentes. |
| Refracción en sólidos | Diagrama de interfaz | La cobertura del libro es demasiado breve para el programa. |
| Eco y reverberación | Línea temporal o respuesta al impulso | El texto solo no muestra la multiplicidad de llegadas. |
| Difracción | Comparación geométrica y cálculo de `λ` | Debe evitarse la idea de transmisión por el material. |
| Sabine | Secuencia cálculo–interpretación–límites | Fórmula simple, hipótesis fuertes. |
| `τ_E` e índice `R` | Conversión lineal/logarítmica | Evita tratar `R` como diferencia arbitraria de niveles. |
| Ley de masas | Gráfico grande y zonas fuera del modelo | La recta ideal parece universal. |
| Cabina | Diagrama editable y fotografía técnica | El sistema contiene demasiadas rutas para una lista. |
| Ruido máximo | Fuente normativa y tabla por bandas | Brecha obligatoria; un dB(A) único es insuficiente. |

## Implicancias de estilo, notación y glosario

- Una idea dominante por slide y cuerpo visible de 22–24 pt; no comprimir los diagramas del libro.
- Usar teal para magnitudes/medio y ocre solo cuando la dimensión perceptual o clínica sea central; no depender solo del color.
- Reconstruir figuras como formas y conectores editables, con rótulos de 22–24 pt y corredores libres para flechas.
- Rotular todos los esquemas atmosféricos, de difracción y ley de masas como cualitativos/no a escala.
- Mantener fórmula, significado, unidades, hipótesis y un ejemplo cercanos.
- Usar `Q_dir`, `R_E`, `τ_E`, `A_eq`, `T_60` y `W_ac` según `notation_guide.md`, declarando equivalencias con el capítulo cuando sea útil.
- Resolver el símbolo de velocidad del viento para evitar colisión con `u(t)` de velocidad de partícula.
- Reservar `R` sin subíndice para índice de reducción sonora claramente rotulado.
- No presentar `dB`, dB SPL, dB(A) o dB HL como intercambiables.
- Toda curva cuantitativa debe incluir ejes, unidades, banda/frecuencia, condiciones y fuente.
- Toda tabla normativa debe indicar norma, edición, jurisdicción/adopción, vía, transductor y condiciones.
- Animaciones solo para cambios de estado, trayectos o revelado de rutas; la versión estática debe ser autosuficiente.

## Coherencia con la arquitectura del curso

La arquitectura clasifica U9 como **alta carga**, con profundidad de aplicación de modelos previos y una alerta central: normas y valores no son universales.

Dependencias explícitas:

- U2 aporta temperatura y propiedades del medio;
- U3 aporta `λ` y `c = λf`;
- U4 aporta niveles, campo libre, distancia, potencia y directividad;
- U5 aporta bandas, espectro y medición;
- U7 aporta la diferencia entre nivel físico y sonoridad y el anticipo de reverberación;
- U9 prepara el control de ruido de U10.

La evidencia mínima de `course_dependency_map.md` —identificar el mecanismo dominante de cada trayecto— se adopta como criterio de cierre. La intervención recomendada —diagramas de trayectos y balances por mecanismo— se adopta como principio organizador, no como storyboard ya resuelto.

La única incoherencia documental global detectada es la numeración desactualizada de las secciones U9 en `content_coverage_matrix.csv`; no afecta la cobertura, pero sí la trazabilidad.

## Fuentes técnicas ya citadas por el capítulo

El capítulo contiene referencias trazables para principios generales:

| Clave local | Fuente/organización | Uso principal en U9 |
|---|---|---|
| `xiangBlauert2021` | Xiang y Blauert, *Acoustics for Engineers*, 3.ª ed. | Propagación, directividad, atmósfera, superficies, refracción y difracción. |
| `iso9613_1_1993` | ISO 9613-1:1993 | Absorción atmosférica y condiciones de propagación exterior. |
| `moser2009` | Möser, *Engineering Acoustics*, 2.ª ed. | Recintos, acondicionamiento, aislamiento y cabinas como sistemas. |
| `iso3382_2_2008` | ISO 3382-2:2008 | Medición de tiempo de reverberación en recintos ordinarios. |
| `fahyGardonio2007` | Fahy y Gardonio, *Sound and Structural Vibration*, 2.ª ed. | Transmisión, ley de masas y límites constructivos. |
| `iso10140_2_2021` | ISO 10140-2:2021 | Medición de aislamiento de elementos en laboratorio. |
| `iso8253_1_2010` | ISO 8253-1:2010 | Audiometría tonal por vía aérea y ósea; requisitos vinculados al ambiente. |
| `iso8253_2_2009` | ISO 8253-2:2009 | Audiometría de campo sonoro. |
| `ansiS31_2023` | ANSI/ASA S3.1-1999 (R2023) | Niveles máximos permisibles de ruido ambiente para salas audiométricas. |
| `iso1996_2_2017` | ISO 1996-2:2017 | Medición y evaluación de ruido ambiental. |

Estas referencias respaldan el análisis conceptual, pero no autorizan a reproducir tablas o valores si el repositorio no contiene la fuente completa y si no se ha decidido qué edición/adopción rige el material docente.

## Conclusión del análisis

Programa, LaTeX y PDF son coherentes en el núcleo obligatorio de propagación, superficies, aislamiento y cabinas. El capítulo ofrece una base particularmente sólida: modelos acotados, seis figuras propias, ejemplos, ejercicios y advertencias contra reglas universales. La mayor dificultad no es la ausencia de contenido general, sino **mantener separados muchos mecanismos y niveles de inferencia**.

La unidad no está lista para storyboard hasta resolver o encuadrar explícitamente:

1. cantidad y duración de encuentros;
2. profundidad central de Sabine y absorción atmosférica;
3. ampliación pedagógica de refracción en sólidos;
4. normalización de símbolos respecto de la guía transversal;
5. convención elegida para la ley de masas y su masa superficial;
6. norma, edición y adopción para ruido ambiente máximo;
7. estrategia de reconstrucción de diagramas y selección de ejercicios;
8. corrección futura de los localizadores U9 en la matriz de cobertura.
