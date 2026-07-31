# Unidad 4 — Análisis de fuentes

## Jerarquía aplicada

1. Programa oficial 2025.
2. Libro del curso en LaTeX.
3. Libro del curso en PDF, edición compilada 2026.
4. Arquitectura curricular y matriz de cobertura.
5. Guías locales de estilo, notación y glosario.
6. Bibliografía citada por el capítulo.

No se incorporaron fuentes externas nuevas en esta etapa.

## Disponibilidad y limitaciones

| Fuente solicitada | Estado | Uso |
|---|---|---|
| `AGENTS.md` | Disponible | Flujo, jerarquía, profundidad, sistema de revisión y restricciones de la etapa. |
| Programa oficial | Disponible | Alcance obligatorio; Unidad 4 en p. 3. |
| `course_map.md` | Disponible | Función central, objetivos, continuidad, carga y bloques recomendados. |
| `course_dependency_map.md` | Disponible | Dependencias simultáneas, nudos y errores críticos. |
| `content_coverage_matrix.csv` | Disponible | Cobertura tema por tema; varias referencias internas de sección están desactualizadas. |
| Capítulo LaTeX de U4 | Disponible | Fuente estructural principal; 1.690 líneas. |
| Libro PDF | Disponible | Capítulo U4 en pp. 89–117; 29 páginas con contenido. |
| `presentation_style_guide.md` | Disponible | Función dominante por slide, legibilidad, densidad, editabilidad y criterios de visualización. |
| `style/notation_guide.md` | Disponible | Convenciones transversales; plantea `W_ac` y `Q_dir`, mientras el libro usa `W` y `Q`. |
| `style/glossary.md` | Disponible | Definiciones y límites entre magnitud física, nivel y percepción. |
| Presentación previa de U4 | No localizada | No hay deck docente de esta unidad para auditar. |
| Guía de ejercicios independiente | No localizada | El capítulo contiene banco amplio de autoevaluación y soluciones. |

## Alcance obligatorio extraído del programa

Texto del programa oficial 2025, p. 3:

> Naturaleza del sonido. Definición física y psicoacústica. Formas de generación del sonido. Elasticidad del medio de propagación. Propiedades de la onda acústica. Velocidad de propagación. Reflexión del sonido e impedancia acústica. Campo acústico. Ondas esféricas y cilíndricas. El tono puro como unidad más simple de sonido, Valor RMS y valor promedio. Tono puro y señales complejas. Presión sonora. El decibel y la presión sonora. Relación con los seres humanos (percepción). Fuentes coherentes y no coherentes. Suma energética. Valores de referencia de uso común (aire y agua) y nomenclatura. Nivel de presión sonora. Nivel de presión sonora en campo libre para fuentes omnidireccionales. Ley del cuadrado inverso. Factor Q, índice y factor de directividad. Cálculo de nivel de presión sonora en función de la distancia.

Descomposición exhaustiva:

| ID | Tema obligatorio | Acción mínima esperada |
|---|---|---|
| P-U04-01 | Naturaleza del sonido | Explicar el fenómeno mecánico y el medio material. |
| P-U04-02 | Definición física y psicoacústica | Diferenciar estímulo físico y sensación sonora. |
| P-U04-03 | Formas de generación | Relacionar distintas fuentes con perturbación del medio. |
| P-U04-04 | Elasticidad del medio | Explicar acción restauradora e inercia distribuida. |
| P-U04-05 | Propiedades de la onda acústica | Recuperar longitudinalidad, propagación, frecuencia, fase, amplitud y energía. |
| P-U04-06 | Velocidad de propagación | Interpretar `c`, sus dependencias y su diferencia con `u`. |
| P-U04-07 | Reflexión e impedancia | Explicar interfaz, desajuste de impedancias y componentes reflejada/transmitida. |
| P-U04-08 | Campo acústico | Definir distribución espacial y temporal de magnitudes. |
| P-U04-09 | Ondas esféricas y cilíndricas | Comparar frentes, áreas y leyes de decaimiento. |
| P-U04-10 | Tono puro como unidad simple | Recuperar senoide ideal como patrón de referencia. |
| P-U04-11 | Valor RMS y valor promedio | Definir, calcular y diferenciar. |
| P-U04-12 | Tono puro y señales complejas | Distinguir una senoide de formas no sinusoidales. |
| P-U04-13 | Presión sonora | Definir presión acústica y sus descriptores. |
| P-U04-14 | Decibel y presión sonora | Definir `L_p` y referencia. |
| P-U04-15 | Relación con percepción humana | Delimitar qué inferencias físicas no determinan una experiencia única. |
| P-U04-16 | Fuentes coherentes/no coherentes | Diferenciar relaciones temporales y forma de suma. |
| P-U04-17 | Suma energética | Calcular contribuciones no correlacionadas y niveles compatibles. |
| P-U04-18 | Referencias aire/agua y nomenclatura | Declarar magnitud, medio, referencia y descriptor. |
| P-U04-19 | Campo libre y fuente omnidireccional | Construir el modelo ideal de distancia. |
| P-U04-20 | Ley del cuadrado inverso | Derivar conceptualmente y aplicar con hipótesis. |
| P-U04-21 | `Q`, índice/factor de directividad | Interpretar `Q` y `DI`; resolver la ambigüedad de redacción del programa. |
| P-U04-22 | Nivel en función de distancia | Calcular cambio de `L_p` entre dos distancias. |

## Comparación programa–LaTeX–PDF

| Tema del programa | LaTeX actual | PDF | Cobertura | Observación pedagógica |
|---|---|---|---|---|
| Naturaleza física/psicoacústica | 4.3 | 90–91 | Completa | La separación física/perceptual es precisa y prepara U7. |
| Formas de generación | 4.3.1 | 91 | Concepto cubierto, ejemplos limitados | El parlante domina; conviene ampliar con voz, membranas, cuerdas y flujo. |
| Elasticidad del medio | 4.4 | 91 | Completa y ampliada | Incluye inercia, densidad y `c = √(K_s/ρ)`. |
| Propiedades de onda acústica | 4.3–4.5, con recuperación de U3 | 90–95 | Distribuida, completa | Necesita una síntesis visible para que la cobertura no dependa de remisiones. |
| Velocidad de propagación | 4.4 | 91 | Completa | Incluye temperatura, cambio de medio y `λ = c/f`. |
| Reflexión e impedancia | 4.5.3–4.5.4 | 92–93 | Completa y ampliada | Agrega `Z_0`, `R_p` y `R_I` con hipótesis. |
| Campo acústico | 4.5 y 4.9 | 92, 101–102 | Completa | Separa magnitudes locales y geometría de campo. |
| Ondas esféricas/cilíndricas | 4.9 | 101–102 | Completa, pero breve | La cilíndrica no posee figura ni ejemplo resuelto propio. |
| Tono puro | 4.6.2, recuperado de U3 | 97 | Completa | Se usa correctamente como modelo ideal. |
| RMS y promedio | 4.6–4.6.1 | 95–97 | Completa y ampliada | Agrega instantáneo, pico y pico a pico. |
| Señales complejas | 4.6.2 | 97 | Completa como puente | Fourier se reserva para U5. |
| Presión sonora | 4.5.1, 4.6 y 4.7.1 | 92, 95–98 | Completa | Distingue `p(t)`, pico, RMS y referencia. |
| Decibel y presión | 4.7–4.7.4 | 97–99 | Completa y ampliada | Incluye `L_I`, `L_W` y justificación 10/20. |
| Percepción humana | 4.3, 4.7.5 y 4.12 | 90, 99, 106 | Completa y limitada correctamente | No invade la psicoacústica de U7. |
| Fuentes coherentes/no coherentes | 4.8–4.8.2 | 100–101 | Completa | Incluye fase y condiciones de no correlación. |
| Suma energética | 4.8.2 | 100–101 | Completa | Agrega niveles iguales y fórmula general para dos niveles. |
| Referencias aire/agua | 4.7.1–4.7.2 | 98–99 | Completa | Aire `20 µPa`, agua `1 µPa`; también referencias de intensidad/potencia aérea. |
| Campo libre/omnidireccional | 4.9.1–4.10 | 102–104 | Completa | Se incluyen campo lejano y condiciones de validez. |
| Ley del cuadrado inverso | 4.10 | 102–104 | Completa | Derivación geométrica, ecuación de nivel y ejemplo. |
| `Q` y directividad | 4.11 | 104–105 | Completa para `Q` y `DI` | El programa parece repetir “factor”; requiere interpretación docente. |
| Nivel con distancia | 4.10.2 | 104 | Completa | Ejemplo `1 m → 4 m` y advertencia sobre pérdidas/reflexiones. |

No se detectó ningún tema obligatorio ausente. Sí se detectaron dos coberturas que necesitan refuerzo didáctico: variedad de formas de generación y onda cilíndrica.

## Correspondencia LaTeX–PDF

### Verificación estructural

El PDF es una representación compilada del capítulo LaTeX actual:

- el capítulo comienza en la p. 89;
- el glosario concluye en la p. 117;
- la p. 118 queda en blanco antes del comienzo de U5 en la p. 119;
- las secciones 4.1–4.17 aparecen en el mismo orden;
- las siete figuras 4.1–4.7 están presentes;
- las ecuaciones principales conservan numeración 4.1–4.27;
- el banco de ejercicios y sus soluciones mantiene todas las categorías;
- las citas y referencias cruzadas visibles aparecen resueltas.

No se observaron diferencias sustantivas entre el contenido del LaTeX y el PDF.

### Verificación visual

Se renderizaron y revisaron las páginas 89–117 del capítulo:

- no se detectaron páginas de contenido faltantes;
- no se observaron figuras cortadas ni ecuaciones fuera de página;
- las páginas 92–105 concentran la teoría cuantitativa y las siete figuras;
- las páginas 108–116 son densas por ejercicios y soluciones;
- la composición es adecuada para lectura cercana en formato libro, pero no es transferible directamente al aula por escala, densidad y orientación vertical;
- la p. 118 en blanco es una decisión de paginación y no una pérdida de contenido.

Las figuras se verificaron en:

- p. 93: interfaz e impedancias;
- p. 95: presión, velocidad e intensidad;
- p. 97: construcción del RMS;
- p. 98: escala presión–dB SPL;
- p. 101: suma coherente/no correlacionada;
- p. 103: propagación esférica;
- p. 105: directividad.

## Ampliaciones del libro respecto del programa

| Ampliación | Estado en matriz | Valor curricular | Decisión preliminar |
|---|---|---|---|
| Velocidad de partícula | Integrada en campo acústico | Esencial para impedancia e intensidad. | Parte central. |
| Intensidad, potencia y energía | `out_of_scope` literal | Evita reducir todo a presión y justifica niveles. | Parte central en distinción; profundidad de cálculo graduable. |
| Valor pico y pico a pico | Ampliación | Aclara descriptores de señal. | Parte central breve. |
| Onda plana y `p/u = ρc` | `out_of_scope` literal | Idealización necesaria para relaciones cuantitativas. | Parte central con límites; derivación complementaria. |
| Coeficientes `R_p` y `R_I` | Ampliación | Separa amplitud y energía reflejada. | Concepto central; cálculo complementario. |
| Niveles de intensidad/potencia | `out_of_scope` literal | Justifican 10/20 y nomenclatura. | Introducción central; ejercicios complementarios. |
| Correlación parcial `γ` | Ampliación | Une casos coherente/no correlacionado. | Material complementario. |
| Campo reverberante y difuso | Ampliación | Prepara U7/U9 y limita “campo libre”. | Definición breve central o complementaria. |
| Condiciones de validez | Ampliación necesaria | Evita aplicar reglas ideales de forma universal. | Parte central. |

La etiqueta `out_of_scope` de la matriz significa “fuera del listado literal del programa”, no “debe eliminarse”. En esta unidad, intensidad, potencia, energía y onda plana son soportes explicativos necesarios para los temas obligatorios.

## Diferencias, tensiones y vacíos documentales

1. **Referencias de sección desactualizadas en la matriz.** Varias filas U04 apuntan a secciones 4.11–4.19, pero el capítulo actual organiza esos contenidos principalmente en 4.5–4.11. Los estados de cobertura siguen siendo válidos; la trazabilidad de secciones debe corregirse en una tarea de arquitectura.
2. **`Q`, índice y factor de directividad.** El programa parece nombrar tres elementos, mientras el libro define dos: factor `Q` e índice `DI`. No se inventará una tercera magnitud; debe validarse la interpretación docente.
3. **Notación `W`/`Q`.** El libro usa `W` para potencia acústica y `Q` para directividad. La guía transversal recomienda `W_ac` y `Q_dir` para evitar colisiones con watt, trabajo y calor. Debe acordarse la notación visible antes del storyboard.
4. **“Formas de generación”.** El libro explica la fuente de manera general y usa sobre todo el parlante. La formulación plural del programa justifica una expansión con varios mecanismos concretos.
5. **“Propiedades de la onda acústica”.** La cobertura está distribuida entre U3 y U4. Conviene una recuperación explícita, no una repetición extensa.
6. **Onda cilíndrica.** Está definida y se indica `I ∝ 1/r`, pero carece de figura, ejemplo resuelto y actividad propia. Al ser obligatoria, requiere un apoyo visual nuevo.
7. **“Presión sonora” frente a “presión acústica”.** El glosario prefiere `presión acústica` para la magnitud lineal y `nivel de presión sonora` para `L_p`. Mantener esa distinción en el material.
8. **Percepción.** El programa pide relación con seres humanos, pero U7 contiene la formalización. U4 debe presentar límites de inferencia y no desarrollar curvas isofónicas o sonoridad.
9. **Campo libre y audiometría.** El libro advierte correctamente que una sala o cabina real requiere condiciones y calibración. No presentar la ley de distancia como procedimiento clínico suficiente.
10. **Densidad de ejercicios.** El banco es valioso, pero su transferencia completa al hilo principal produciría sobrecarga. Debe seleccionarse por objetivo y llevar soluciones a respaldo.
11. **“No coherentes” frente a “no correlacionadas”.** El programa usa “fuentes no coherentes”; el capítulo formula la suma mediante presiones no correlacionadas durante un intervalo. En el material conviene conservar la expresión del programa al presentar el tema y usar “no correlacionadas” al declarar la condición matemática, sin tratarlas como etiquetas automáticas de una fuente por su nombre.

## Qué puede pasar casi directamente a diapositivas

“Casi directamente” significa conservar idea, precisión y fuente, no copiar la página.

| Contenido | Fuente | Motivo |
|---|---|---|
| Definición física/perceptual | TEX 4.3 | Contraste claro y disciplinarmente correcto. |
| Fuente–medio–receptor | TEX 4.3.1 | Secuencia breve; debe incorporar “campo” y no hacer del receptor un requisito. |
| Elasticidad + inercia | TEX 4.4 | Explicación intuitiva anterior a la ecuación. |
| Definiciones de `p` y `u` | TEX 4.5.1–4.5.2 | Breves, con unidad y error frecuente. |
| Definición de `Z` y límite de `p/u = ρc` | TEX 4.5.3 | Precisa y necesaria. |
| Distinción `I`, `W_ac`, `E_ac` | TEX 4.5.5 | Organiza local, flujo y total. |
| Lista de descriptores de señal | TEX 4.6 | Completa; debe dividirse en varias representaciones. |
| Definición de RMS | TEX 4.6 | Correcta y acompañada por explicación de cuadrado/raíz. |
| Tono puro/señal compleja | TEX 4.6.2 | Delimita correctamente lo que se reserva para U5. |
| Requisitos para interpretar dB | TEX 4.7 | Magnitud, referencia y condición adicional. |
| `L_p` y referencias aire/agua | TEX 4.7.1 | Cobertura obligatoria con advertencia metrológica. |
| Explicación 10/20 | TEX 4.7.3 | Evita regla memorística; requiere construcción por etapas. |
| Comparación coherente/no correlacionada | TEX 4.8.1–4.8.2 | Casos canónicos y números pedagógicos. |
| Modelos plano/cilíndrico/esférico | TEX 4.9 | Comparación conceptual central. |
| Condiciones de validez | TEX 4.10.1 | Deben quedar visibles junto a la ley de distancia. |
| Definiciones de `Q` y `DI` | TEX 4.11 | Precisas; falta acordar notación final. |
| Errores frecuentes | TEX 4.13 | Material directo para diagnóstico y recapitulación. |

## Qué necesita más explicación o transformación

| Contenido | Problema si se transfiere linealmente | Transformación necesaria |
|---|---|---|
| Diez resultados del capítulo | Demasiados para una apertura y no coinciden uno a uno con el programa. | Sintetizar en los ocho objetivos del brief. |
| Definición de sonido | Puede quedar verbal y abstracta. | Fenómeno concreto, medio visible y contraste con percepción. |
| Generación | Un único parlante no representa la pluralidad del programa. | Mosaico técnico o secuencia de mecanismos con variable que perturba el medio. |
| `c = √(K_s/ρ)` | Riesgo de concluir “más denso = siempre más lento”. | Tendencias separadas y comparación con advertencia. |
| Mapa de magnitudes | El capítulo introduce muchas variables consecutivas. | Diagrama y tabla progresiva; una magnitud nueva por paso. |
| Impedancia/reflexión | Fórmulas y coeficientes pueden ocultar el mecanismo. | Interfaz visual, hipótesis y casos límite antes del cálculo. |
| Integrales de intensidad/media/RMS | Pueden intimidar a primer año. | Interpretación como promedio y versión discreta/visual antes de notación integral. |
| RMS | Una sola figura no garantiza comprensión de la raíz cuadrática. | Revelado en cuatro etapas y actividad con muestras simples. |
| 10 frente a 20 | Alta propensión a memorización. | Derivación corta desde proporcionalidad cuadrática y árbol de decisión. |
| Aire/agua | Tabla textual no muestra la imposibilidad de comparación directa. | Casos con el mismo número y referencias distintas; nomenclatura completa. |
| Coherencia/no correlación | Dos fórmulas juntas producen regla superficial. | Simulación o gráficos con fase y promedio temporal. |
| Correlación parcial | Formalismo adicional sin demanda literal. | Complementario, después de dominar extremos. |
| Onda cilíndrica | Cobertura textual sin evidencia visual. | Diagrama propio y ejemplo de duplicación de distancia (`−3,01 dB` ideal). |
| Campo libre/reverberante/difuso | Definiciones se confunden con tipos de sala. | Escenarios y contraejemplos; preparar U9. |
| Ley del cuadrado inverso | La derivación y condiciones están separadas en páginas. | Mantener fórmula, geometría, condiciones y contraejemplo próximos. |
| Directividad | Patrón conceptual no muestra dependencia de frecuencia. | Patrón por etapas y, más adelante, datos técnicos verificados. |
| Banco de ejercicios | Demasiado extenso para la secuencia principal. | Selección por objetivo; soluciones y variantes a respaldo. |

## Implicancias de las guías de estilo, notación y glosario

- Cada slide futura deberá cumplir una sola función dominante; la densidad del capítulo exige división, no reducción tipográfica.
- Las figuras del libro no deben insertarse como capturas. Se priorizan formas editables, SVG y gráficos con ejes/unidades legibles.
- Las ecuaciones deben definir símbolos, unidades, significado y condiciones; no se aprobarán fórmulas aisladas.
- El color físico/perceptual puede apoyar la comparación, pero no debe ser el único código.
- Se debe usar `presión acústica` para `p(t)` y `nivel de presión sonora` para `L_p`.
- La notación transversal resuelve colisiones con `W_ac`, `Q_dir`, `p_ref`, `T_obs` y `S` para área; la forma visible requiere validación docente en dos casos.
- Un valor en dB debe incluir descriptor, referencia y ponderación cuando corresponda.
- La futura unidad necesitará bloques cortos y recapitulaciones frecuentes por exigencia específica de `AGENTS.md` y del mapa del curso.

## Coherencia con la arquitectura del curso

`course_map.md` y `course_dependency_map.md` coinciden en:

- carga conceptual muy alta;
- papel central de U4 para las unidades 5–10;
- dependencias simultáneas de mecánica, ondas, promedios, logaritmos y geometría;
- nudos `p/u/I/W`, pico/RMS, 10/20, coherencia, cuadrado inverso y directividad;
- bloques fenómeno/medio, magnitudes, valores de señal, niveles, suma y geometría/directividad;
- recapitulaciones después de magnitudes, niveles y propagación;
- errores críticos: “dB mide intensidad”, “dos fuentes suman siempre 3 dB” y “duplicar distancia siempre resta 6 dB”.

No se propone modificar la arquitectura pedagógica global en esta etapa. Sí se recomienda corregir en otra tarea las referencias de sección de U4 en `content_coverage_matrix.csv`.

## Fuentes técnicas citadas por el capítulo

El capítulo fundamenta sus afirmaciones mediante referencias ya registradas en `references.bib`, entre ellas:

- Xiang y Blauert para acústica física, propagación, campos e impedancia;
- NIST SP 811 e ISO 1683 para unidades, niveles y referencias;
- ISO 389-1 para referencias audiométricas;
- IEC 61672-1 para ponderaciones y sonometría;
- ISO 8253-1 e ISO 8253-2 para audiometría y campo sonoro.

Estas fuentes pertenecen al libro y no fueron reemplazadas ni ampliadas. En etapas posteriores deberá conservarse la trazabilidad de las afirmaciones técnicas y verificarse la edición normativa antes de mostrar tablas o requisitos específicos.
