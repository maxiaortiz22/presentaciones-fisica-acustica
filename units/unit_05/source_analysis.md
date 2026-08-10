# Unidad 5 — Análisis de fuentes

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
| `AGENTS.md` | Disponible | Flujo, jerarquía, profundidad, revisión y restricciones de la etapa. |
| Programa oficial | Disponible | Alcance obligatorio; U5 comienza en p. 3 y concluye en p. 4. |
| `course_map.md` | Disponible | Función, objetivos, continuidad, carga y bloques recomendados. |
| `course_dependency_map.md` | Disponible | Dependencias simultáneas, nudos, errores críticos y evidencia mínima. |
| `content_coverage_matrix.csv` | Disponible | Cobertura tema por tema; referencias de sección U05 desactualizadas respecto del capítulo actual. |
| Capítulo LaTeX de U5 | Disponible | Fuente estructural principal; 1.650 líneas. |
| Libro PDF | Disponible | Capítulo U5 en pp. 119–149; 31 páginas con contenido. |
| `presentation_style_guide.md` | Disponible | Función dominante por slide, densidad, editabilidad y criterios visuales. |
| `style/notation_guide.md` | Disponible | Convenciones de `x(t)`, `X(f)`, `H(f)`, `f_s`, `N`, `Δf`, bandas y descriptores. |
| `style/glossary.md` | Disponible | Definiciones y advertencias para señal, espectro, respuesta, componentes y medición. |
| Presentación previa de U5 | No localizada | `units/unit_05/` contenía solo `.gitkeep`; no hay deck de esta unidad para auditar. |
| Guía de ejercicios independiente | No localizada | El capítulo contiene banco completo de autoevaluación y soluciones. |
| Datos reales de voz o medición | No localizados para esta unidad | Las figuras actuales usan modelos o datos sintéticos; deberán incorporarse con trazabilidad si se requieren. |

## Alcance obligatorio extraído del programa

Texto del programa oficial 2025, pp. 3–4:

> Forma de representación de señales complejas: series de Fourier y transformada de Fourier. Gráficos de respuesta en frecuencia y espectro. Rangos de frecuencia del sonido: infrasonido, sonido audible y ultrasonido. Rango dinámico vocal e instrumental. Rango dinámico del oído: umbral de dolor. Fundamentales, armónicos, parciales y sobretonos. Armónicos y octavas. División del espectro en bandas. Filtros. Frecuencia límite y central. Ancho de banda. Curvas de ponderación: dBA. Medidor de nivel de presión sonora.

Descomposición exhaustiva:

| ID | Tema obligatorio | Acción mínima esperada |
|---|---|---|
| P-U05-01 | Representación de señales complejas | Contrastar tiempo y frecuencia con ejes y unidades. |
| P-U05-02 | Serie de Fourier | Explicar representación de una señal periódica por componentes armónicas. |
| P-U05-03 | Transformada de Fourier | Explicar extensión a señales no necesariamente periódicas. |
| P-U05-04 | Gráfico de espectro | Identificar señal, eje frecuencial y magnitud representada. |
| P-U05-05 | Gráfico de respuesta en frecuencia | Interpretar relación entrada–salida y diferenciarla del espectro. |
| P-U05-06 | Infrasonido, sonido audible y ultrasonido | Clasificar regiones con fronteras aproximadas y condiciones. |
| P-U05-07 | Rango dinámico vocal | Definir extremos y condiciones de emisión/medición. |
| P-U05-08 | Rango dinámico instrumental | Definir extremos y condiciones del instrumento/registro. |
| P-U05-09 | Rango dinámico del oído y umbral de dolor | Comparar límite inferior/superior sin fijar valor universal. |
| P-U05-10 | Fundamental | Relacionar `f_0` con periodicidad, no con amplitud máxima. |
| P-U05-11 | Armónicos | Identificar múltiplos enteros de `f_0`. |
| P-U05-12 | Parciales | Usar el término general para componentes sinusoidales. |
| P-U05-13 | Sobretonos | Diferenciar orden de parcial y número de armónico. |
| P-U05-14 | Armónicos y octavas | Distinguir serie armónica de relación `2:1` y explorar su vínculo. |
| P-U05-15 | División del espectro en bandas | Explicar agrupación por límites definidos. |
| P-U05-16 | Filtros | Reconocer función y tipos básicos. |
| P-U05-17 | Frecuencia límite y central | Definir `f_L`, `f_H`, `f_c` y criterio de corte. |
| P-U05-18 | Ancho de banda | Calcular `B = f_H − f_L` y distinguir ancho absoluto/relativo. |
| P-U05-19 | Curva de ponderación A / dBA | Interpretar respuesta normalizada y nomenclatura técnica. |
| P-U05-20 | Medidor de nivel de presión sonora | Describir cadena funcional, configuración y resultado informado. |

## Comparación programa–LaTeX–PDF

| Tema del programa | LaTeX actual | PDF | Cobertura | Observación pedagógica |
|---|---|---|---|---|
| Representación de señales complejas | 5.3–5.4 | 120–126 | Completa y ampliada | Añade tiempo, magnitud, fase y categorías temporalmente no excluyentes. |
| Serie de Fourier | 5.4.1–5.4.2 | 121–124 | Completa y ampliada | Incluye ecuación, coeficientes, síntesis progresiva, Gibbs y ejemplo. |
| Transformada de Fourier | 5.4.3 | 123–125 | Completa y ampliada | Incluye convención compleja, unidades, magnitud y fase. |
| Espectro | 5.3, 5.4, 5.5 | 120–129 | Completa | Aclara que la ordenada no es automáticamente intensidad. |
| Respuesta en frecuencia | 5.5–5.5.1 | 127–130 | Completa y ampliada | Define `H(f)`, ganancia, fase, retardo y ejemplo entrada–salida. |
| Infra/audible/ultra | 5.7.1 | 131 | Completa con cautelas | Las fronteras se presentan como aproximadas y dependientes de condiciones. |
| Rango dinámico vocal e instrumental | 5.7.2 | 131–132 | Conceptualmente completa, sin cifras | Falta seleccionar ejemplos numéricos trazables si se desean comparaciones concretas. |
| Rango auditivo/umbral de dolor | 5.7.2 | 131–132 | Completa con corrección conceptual | Sustituye un “umbral de dolor” universal por límites definidos por frecuencia, estímulo y oyente. |
| Fundamental, armónicos, parciales y sobretonos | 5.6 | 129–131 | Completa y ampliada | Añade parciales inarmónicos, fundamental ausente y formantes. |
| Armónicos y octavas | 5.6 y 5.8 | 129–133 | Temas cubiertos, relación distribuida | Conviene una comparación explícita: serie armónica no equivale a división en octavas. |
| División en bandas | 5.4.7 y 5.8 | 127, 132–133 | Completa y ampliada | Distingue bin/banda e incorpora octava y tercio. |
| Filtros | 5.9–5.9.1 | 133–135 | Completa y ampliada | Incluye cuatro tipos, ideal/real, transición y filtrado audiométrico. |
| Frecuencia límite/central y ancho | 5.8–5.9 | 132–134 | Completa | Aclara dos límites y centro geométrico; ejemplo de tercio. |
| Curva A/dBA | 5.10–5.10.1 | 135–136 | Completa y ampliada | Añade C/Z, corrección de tono y advertencia para banda ancha; falta figura propia A/C/Z. |
| Medidor de nivel de presión sonora | 5.11 | 136–138 | Completa y ampliada | Usa el término preferido “sonómetro” y añade `L_eq`, máximo, pico y verificación. |

No se detectó ningún tema obligatorio ausente. Se detectaron tres necesidades de refuerzo antes del storyboard: datos condicionados para rangos dinámicos, relación explícita armónicos–octavas y visual de ponderaciones A/C/Z.

## Correspondencia LaTeX–PDF

### Verificación estructural

El PDF es una representación compilada del capítulo LaTeX actual:

- el capítulo comienza en la p. 119;
- el glosario concluye en la p. 149;
- la p. 150 queda en blanco antes del comienzo de U6 en la p. 151;
- las secciones 5.1–5.17 aparecen en el mismo orden;
- las ocho figuras 5.1–5.8 están presentes;
- las ecuaciones principales conservan numeración 5.1–5.21;
- el banco de ejercicios incluye todas las categorías y soluciones;
- las citas y referencias cruzadas visibles aparecen resueltas.

No se observaron diferencias sustantivas entre el contenido del LaTeX y el PDF.

### Verificación visual

Se renderizaron y revisaron las páginas 119–149 del capítulo y las páginas 3–4 del programa:

- no se detectaron páginas de contenido faltantes;
- no se observaron figuras cortadas ni ecuaciones fuera de página;
- las páginas 119–138 concentran el desarrollo conceptual y cuantitativo;
- la síntesis y el banco de ejercicios comienzan en p. 139;
- las soluciones ocupan pp. 143–148 y el glosario pp. 148–149;
- la composición es adecuada para lectura cercana, pero no es transferible directamente al aula por densidad, orientación vertical y tamaño de gráficos;
- la p. 150 en blanco es una decisión de paginación, no una pérdida de contenido.

Las figuras se verificaron en:

- p. 122: tiempo, magnitud y fase;
- p. 124: serie de Fourier progresiva;
- p. 126: compromiso tiempo–frecuencia;
- p. 128: espectro, respuesta de sistema y salida;
- p. 130: componentes espectrales;
- p. 132: octava y tercios de octava;
- p. 134: filtros ideales y no ideales;
- p. 137: cadena funcional del sonómetro.

## Ampliaciones del libro respecto del programa

| Ampliación | Estado en matriz | Valor curricular | Decisión preliminar |
|---|---|---|---|
| Señales periódicas, aperiódicas y transitorias | Integrada | Prepara elección de representación y segmentación. | Parte central breve. |
| Magnitud y fase | Integrada | Evita pensar que el espectro de magnitud contiene toda la información. | Parte central. |
| Muestreo, DFT y FFT | `out_of_scope` literal | Conecta Fourier con software y registros reales. | Ruta mínima central o complemento según tiempo. |
| `T_obs` y `Δf` | `out_of_scope` literal | Permite interpretar resolución nominal. | Importante; incluir si se usa DFT/espectrograma. |
| Ventanas y fuga | `out_of_scope` literal | Explica espectros reales y límites del análisis. | Importante con visual; detalle complementario. |
| Espectrograma | `out_of_scope` literal | Muy relevante para voz y habla. | Recomendado en parte central ampliada. |
| Nivel por bin y por banda | `out_of_scope` literal | Evita comparar análisis incompatibles y promediar dB. | Complementario; prepara U10. |
| Fase de respuesta y retardo | Ampliación | Demuestra que magnitud plana no implica sistema transparente. | Complementario. |
| Formantes y modelo fuente–filtro | Ampliación | Aplicación directa a voz. | Parte central introductoria o complemento breve. |
| Parciales inarmónicos y fundamental ausente | Ampliación | Corrige identificación por máximo y prepara pitch. | Parte central. |
| Tercios de octava | Ampliación | Relevante para medición y U9/U10. | Parte central junto a octavas. |
| Ponderaciones C y Z | `out_of_scope` literal | Contextualizan A y evitan absolutizarla. | Introducción central breve; detalle complementario. |
| `L_eq`, máximo y pico | `out_of_scope` literal | Necesarios para interpretar resultados reales y preparar U10. | Importante; profundidad según tiempo. |
| Verificación de instrumento y ruido de fondo | Ampliación metrológica | Evita usar aplicaciones o límites globales como sustitutos. | Aplicación central breve; detalle a respaldo. |

## Diferencias, tensiones y vacíos documentales

1. **Referencias de sección desactualizadas en la matriz.** Las filas U05 usan numeración anterior: por ejemplo, rangos figuran como 5.8–5.10 y sonómetro como 5.17, mientras el capítulo actual los organiza en 5.7 y 5.11. Los estados de cobertura son válidos; debe corregirse `book_section` en una tarea posterior de arquitectura.
2. **`dBA` frente a `dB(A)`.** El programa usa `dBA`; la guía de notación y el libro prefieren `dB(A)` o descriptores como `L_Aeq,T`. Debe conservarse el término del programa al explicarlo y adoptar notación técnica coherente en el material.
3. **“Medidor de nivel de presión sonora” frente a “sonómetro”.** El libro y el glosario usan el término disciplinar preferido `sonómetro`. Conviene mencionar la formulación del programa y luego mantener `sonómetro`.
4. **Rangos dinámicos sin valores.** El libro define correctamente el concepto y evita cifras universales, pero el programa nombra rangos vocal, instrumental y auditivo. Para una comparación concreta se necesitan fuentes, condiciones y población; no deben inventarse valores.
5. **Umbral de dolor.** El programa lo presenta como límite del rango auditivo; el libro lo problematiza y propone nivel de incomodidad u otro límite definido. La tensión debe hacerse visible y validarse con el docente.
6. **Armónicos y octavas.** El libro cubre ambos temas en secciones separadas. La secuencia futura debe explicar que una octava es una razón `2:1`; algunos armónicos se relacionan por octavas, pero una serie armónica no es una escala de octavas.
7. **Profundidad digital.** DFT/FFT, muestreo, ventana, fuga y espectrograma no aparecen literalmente en el programa, pero el mapa global y el capítulo los consideran útiles. Es la decisión de alcance más importante antes del storyboard.
8. **Convención de transformada y ordenada.** `X(f)` depende de la convención y la normalización. Los gráficos futuros deberán declarar si muestran pico, RMS, magnitud, potencia, densidad o nivel.
9. **Notación `P(f)`/`X(f)`.** `course_map.md` menciona `P(f)` junto con `X(f)`, mientras la guía adopta `X(f)` para señal genérica y `p(t)` para presión. Debe definirse si la transformada de presión se escribirá `P(f)` o si se mantendrá `X(f)` en ejemplos genéricos.
10. **Figura A/C/Z pendiente.** El capítulo contiene un `TODO` explícito. Una curva nominal requiere reproducir expresiones normativas, citar edición y distinguir respuesta nominal de tolerancias del instrumento.
11. **Espectrograma de voz.** El capítulo ofrece un ejemplo sintético excelente para resolución, pero no un caso de voz. Incorporarlo exige un registro propio/autorizado, parámetros reproducibles y límites no diagnósticos.
12. **Filtro y ponderación.** La similitud visual de sus respuestas puede ocultar que tienen propósitos diferentes. La separación debe ser un eje pedagógico, no una nota lateral.
13. **Sonómetro y normas.** El libro cita IEC/ISO/ANSI y datos puntuales. No debe transformarse esta introducción en entrenamiento de conformidad o en una lista de valores legales sin jurisdicción y edición aplicables.
14. **Densidad de ejercicios.** El banco es amplio y completo; su transferencia íntegra al hilo principal produciría sobrecarga. Debe seleccionarse por objetivo y llevar soluciones a respaldo.

## Qué puede pasar casi directamente a diapositivas

“Casi directamente” significa conservar idea, precisión y fuente, no copiar la página.

| Contenido | Fuente | Motivo |
|---|---|---|
| Dos descripciones de una señal | TEX 5.3 | Contraste claro y advertencia sobre la ordenada. |
| Periodicidad y categorías temporales | TEX 5.3.1 | Definiciones precisas con ejemplo de vocal. |
| Fourier como representación | TEX 5.4 | Corrige el error conceptual principal. |
| Síntesis progresiva y Gibbs | Figura 5.2 | Intuición visual; debe revelarse por etapas. |
| FFT como algoritmo | TEX 5.4.4 | Frase breve, necesaria y precisa. |
| Espectro frente a respuesta | TEX 5.5 y figura 5.4 | Nudo curricular explícito con modelo entrada–salida. |
| Definiciones de fundamental, armónico, parcial y sobretono | TEX 5.6 | Terminología consistente con glosario. |
| Casos de componentes | Figura 5.5 | Corrige máximo=fundamental y todo parcial=armónico. |
| Cautelas sobre rangos | TEX 5.7 | Evita cifras universales. |
| Ecuaciones de bandas | TEX 5.8 | Símbolos y unidades coherentes; requiere graduación. |
| Filtros ideales/no ideales | TEX 5.9 y figura 5.7 | Clasificación completa y visual. |
| Filtrado/ponderación/audiometría | TEX 5.9.1 | Comparación de alta relevancia profesional. |
| Corrección A para un tono | TEX 5.10.1 | Ejemplo válido con fuente normativa y límite de generalización. |
| Cadena del sonómetro | TEX 5.11 y figura 5.8 | Integra transducción, procesamiento y descriptor. |
| Errores frecuentes | TEX 5.13 | Banco directo para preguntas y recapitulaciones. |

## Qué necesita más explicación o transformación

| Contenido | Problema si se transfiere linealmente | Transformación necesaria |
|---|---|---|
| Nueve resultados del capítulo | Demasiados para apertura y mezclan núcleo con ampliaciones. | Sintetizar en los ocho objetivos del brief. |
| Tres vistas de la señal | Puede convertirse en lectura pasiva de una figura. | Revelado sincronizado y preguntas sobre ejes/información ausente. |
| Serie completa y coeficientes | Formalismo abrupto para primer año. | Síntesis visual antes de ecuación; cálculo de coeficientes a complemento/respaldo. |
| Transformada compleja | `j`, integral y unidades aparecen juntos. | Capa conceptual, luego magnitud/fase, luego fórmula como referencia. |
| DFT/FFT | Fácil confundir método, resultado, algoritmo y magnitud vertical. | Tabla de objetos y parámetros; un ejemplo reproducible. |
| Ventanas/fuga | La figura final no muestra el recorte que produce el efecto. | Animación o secuencia temporal → ventana → espectro. |
| Espectrograma | Tres dimensiones visuales y compromiso doble. | Enseñar ejes/color por separado y comparar dos configuraciones. |
| Bin/banda | La fórmula de suma puede ocultar la diferencia conceptual. | Contenedores sobre el mismo eje con límites y dependencia de `T_obs`. |
| `H = Y/X` | Puede leerse como división de cualquier salida por cualquier entrada. | Modelo lineal, misma frecuencia, entrada no nula y condiciones comparables. |
| Fuente–filtro de voz | Riesgo de convertir formantes en armónicos o diagnóstico. | Diagrama fuente–sistema–salida y espectros diferenciados. |
| Rangos dinámicos | Falta de valores concretos puede volverlo abstracto; cifras sueltas serían engañosas. | Casos con condiciones y fuentes verificadas; registrar incertidumbre y población. |
| Octava/tercio | Cuatro fórmulas consecutivas pueden dominar la comprensión. | Eje logarítmico, razón primero, cálculo después. |
| Cuatro filtros en una figura | Demasiados paneles para una sola slide legible. | Dividir por familias o usar comparación progresiva. |
| Ponderaciones A/C/Z | El capítulo carece de figura propia. | Generar curvas nominales verificadas y separar respuesta de tolerancia. |
| `L_eq` integral | Puede percibirse como fórmula desconectada. | Promedio discreto/energético antes de integral y ejemplo con dos intervalos. |
| Sonómetro | La cadena es correcta, pero densa para un único diagrama. | Revelado por etapas y salida con descriptor completo. |
| Banco de ejercicios | Exceso de material para clase. | Selección por bloque; soluciones y variantes a respaldo. |

## Implicancias de las guías de estilo, notación y glosario

- Cada slide futura deberá cumplir una sola función dominante; la densidad del capítulo exige división, no reducción tipográfica.
- Las figuras del libro no deben insertarse como páginas o capturas. Se priorizan SVG, gráficos reproducibles y formas editables.
- Toda ordenada espectral debe declarar magnitud, unidad, escala, referencia y normalización cuando correspondan.
- Las ecuaciones deben definir símbolos, unidades, significado y condiciones antes de usarse en un cálculo.
- Se usarán `x(t)`/`X(f)` para señal genérica y `p(t)` para presión; la forma de la transformada de presión queda como decisión abierta.
- Se mantendrán `f_0`, `f_s`, `N`, `T_obs`, `Δf`, `H(f)`, `f_L`, `f_H`, `f_c`, `B` y `L_Aeq,T` según la guía.
- No se usará “intensidad” como rótulo genérico de un espectro.
- Se preferirá `dB(A)` o un descriptor completo frente a `dBA` aislado.
- Se mantendrán las distinciones frecuencia/pitch, nivel/sonoridad y dB SPL/dB HL.
- La futura unidad necesitará bloques cortos y mini recapitulaciones frecuentes por exigencia específica de `AGENTS.md` y de la arquitectura global.

## Coherencia con la arquitectura del curso

`course_map.md` y `course_dependency_map.md` coinciden en:

- carga conceptual muy alta;
- dependencia simultánea de señal temporal, fase, RMS, dB y lectura de gráficos;
- nudos señal/sistema, Fourier/mecanismo, bin/banda, fundamental/máximo y filtro/ponderación;
- bloques dominios, Fourier, registro digital, señal/sistema, componentes, bandas/filtros y ponderaciones/sonómetro;
- mini recapitulación “qué objeto se representa” al cerrar cada bloque;
- errores críticos: “FFT es intensidad”, “espectro = respuesta” y “A convierte SPL en audición”;
- evidencia mínima al cierre: decidir si un gráfico representa señal o sistema y explicar sus ejes.

No se propone modificar la arquitectura global en esta etapa. Sí se recomienda corregir en otra tarea las referencias de sección de U05 en `content_coverage_matrix.csv`.

## Fuentes técnicas citadas por el capítulo

El capítulo fundamenta afirmaciones mediante referencias ya registradas en `references.bib`, entre ellas:

- Oxenham (2018) e ISO 226:2023 para límites auditivos y cautelas perceptuales;
- Brockmann-Bauser y Drinnan (2011) para análisis acústico de voz y límites de inferencia clínica;
- IEC 61260-1:2014 para filtros de octava y fracciones de octava;
- IEC 61672-1:2013 para ponderaciones A/C/Z, especificaciones y datos nominales;
- IEC 61672-2:2013 e IEC 61672-3:2013 para evaluación y ensayos de sonómetros;
- ISO 8253-1:2010 y ANSI/ASA S3.1-1999 (R2023) para condiciones de ruido en audiometría.

Estas fuentes pertenecen al libro y no fueron reemplazadas ni ampliadas. En etapas posteriores deberá verificarse la edición normativa aplicable antes de mostrar curvas, tolerancias, procedimientos o límites numéricos.
