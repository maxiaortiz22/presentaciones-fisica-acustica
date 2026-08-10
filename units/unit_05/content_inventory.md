# Unidad 5 — Inventario de contenido

## Criterio de clasificación

- **Imprescindible:** exigido por el programa o necesario para interpretar correctamente un tema obligatorio.
- **Importante:** ampliación del libro con alto valor didáctico o profesional.
- **Complementario:** profundización útil si el tiempo, los recursos y el grupo lo permiten.
- **Respaldo:** detalle formal, normativo, soluciones o variantes para consulta y preguntas.
- **Fuera de alcance:** contenido que pertenece a procesamiento avanzado, psicoacústica, Audiología clínica o metrología especializada.

La etiqueta `out_of_scope` de `content_coverage_matrix.csv` se interpreta como “fuera del listado literal del programa”, no como orden de eliminación. Algunas ampliaciones son soportes necesarios para leer espectros reales sin errores.

## Conceptos principales

| Concepto | Clasificación | Función pedagógica | Advertencia |
|---|---|---|---|
| Dominio temporal | Imprescindible | Punto de partida: duración, transitorios, repetición y amplitud. | No presentarlo como una representación inferior al espectro. |
| Dominio frecuencial | Imprescindible | Organiza contribuciones según frecuencia. | El eje vertical debe declarar magnitud, unidad, referencia y normalización. |
| Espectro de magnitud y espectro de fase | Imprescindible/Importante | Muestran cuánto y con qué relación temporal contribuyen las componentes. | La magnitud sola no determina la forma temporal. |
| Señal periódica, aperiódica y transitoria | Importante | Delimita cuándo resulta natural usar serie o transformada y cómo tratar registros reales. | Las categorías pueden coexistir aproximadamente en distintos tramos. |
| Serie de Fourier | Imprescindible | Representa señales periódicas mediante componentes armónicas. | Es una representación, no un mecanismo físico. |
| Transformada de Fourier | Imprescindible | Extiende la representación frecuencial a señales no necesariamente periódicas. | Su magnitud no es automáticamente intensidad. |
| DFT y FFT | Importante | Conecta la teoría con registros finitos y herramientas reales. | FFT es un algoritmo para calcular la DFT. |
| Espectrograma | Importante | Representa evolución temporal del contenido frecuencial. | Color, ventana y resolución deben declararse. |
| Espectro de señal | Imprescindible | Describe un registro particular. | Depende de señal, captura y método. |
| Respuesta en frecuencia | Imprescindible | Describe cómo un sistema modifica entrada según frecuencia. | No se obtiene de la salida aislada. |
| Frecuencia fundamental | Imprescindible | Relaciona periodicidad con `f_0 = 1/T_0`. | No es necesariamente la línea mayor ni debe estar presente. |
| Armónico, parcial y sobretono | Imprescindible | Ordena componentes espectrales sin usar términos como sinónimos. | Todo armónico es parcial; el primer sobretono no es el primer armónico. |
| Formante | Importante | Conecta periodicidad de fuente con resonancias del tracto vocal. | No es un armónico ni un diagnóstico. |
| Infrasonido, rango audible y ultrasonido | Imprescindible | Clasifica regiones convencionales de frecuencia. | `20 Hz` y `20 kHz` son fronteras aproximadas, no límites universales. |
| Rango dinámico | Imprescindible | Compara niveles superior e inferior bajo condiciones comunes. | Vocal, instrumental y auditivo requieren tarea y procedimiento definidos. |
| Banda de octava y tercio de octava | Imprescindible | Resume espectros con resolución relativa. | Una octava es una razón `2:1`, no una diferencia fija en hertz. |
| Filtro | Imprescindible | Modifica componentes de una señal según frecuencia. | Distinguir ideal/real, tipo, corte, transición y pendiente. |
| Frecuencia límite, central y ancho de banda | Imprescindible | Parametriza bandas y filtros. | Una banda posee límites inferior y superior; el criterio de corte debe declararse. |
| Ponderación A | Imprescindible | Introduce una respuesta normalizada de medición. | No representa una audición individual ni convierte SPL en HL. |
| Sonómetro | Imprescindible | Integra transducción, ponderación, detector, tiempo e informe. | La lectura depende de configuración, calibración, intervalo y entorno. |

## Conceptos secundarios y ampliaciones

| Concepto | Clasificación | Decisión preliminar |
|---|---|---|
| Término medio `a_0/2` y coeficientes `a_n`, `b_n` | Complementario | Mostrar significado; cálculo integral como respaldo. |
| Fenómeno de Gibbs | Complementario | Usarlo para explicar oscilaciones de la suma parcial, sin formalizar convergencia. |
| Unidad imaginaria `j` y forma polar compleja | Complementario | Introducción mínima si se muestra la transformada; operación compleja detallada a respaldo. |
| Frecuencia de muestreo y período de muestreo | Importante | Necesarios para interpretar DFT y frecuencia máxima representable; la profundidad queda abierta. |
| Duración observada `T_obs` | Importante | Base de la separación nominal entre bins. |
| Separación entre bins `Δf` | Importante | Cálculo útil; diferenciar de precisión y de ancho de banda. |
| Ventanas y fuga espectral | Importante | Explican por qué un tono real no aparece siempre en una sola línea. |
| Resolución temporal–frecuencial | Importante | Central si se usa espectrograma de voz; modular según tiempo. |
| Nivel por bin y nivel por banda | Complementario | Útil para U10 y para evitar promedios de dB; no cargar la apertura. |
| Ganancia de amplitud `G(f)` | Importante | Cálculo simple a una frecuencia y lectura de signo. |
| Fase de respuesta y retardo puro | Complementario | Evidencia de que magnitud constante no implica sistema neutro. |
| Fundamental ausente | Importante | Corrige la identificación de `f_0` por máximo; el pitch se reserva para U7. |
| Parcial inarmónico | Importante | Evita clasificar toda componente como armónica. |
| Ponderaciones C y Z | Importante | Contextualizan A y evitan tratarla como único descriptor. |
| Nivel equivalente `L_Xeq,T` | Importante | Conecta promedios energéticos con sonometría y U10. |
| Ponderaciones temporales F/S | Complementario | Introducción conceptual; ensayo normativo a respaldo. |
| Nivel máximo y nivel pico | Importante | Distinción metrológica necesaria. |
| Verificación de campo, evaluación de modelo y ensayo periódico | Complementario | Nombrar diferencias; no enseñar certificación de instrumentos. |
| Ruido de fondo para audiometría | Importante | Aplicación profesional con advertencia: no usar un único límite en dB(A). |

## Definiciones que deben conservar precisión

| Término | Definición de trabajo | Límite o error a evitar |
|---|---|---|
| señal | Representación de una magnitud variable que porta información sobre un fenómeno. | No confundir señal compleja con número complejo. |
| espectro | Representación de cómo se distribuye una señal según frecuencia. | Es propiedad de la señal observada y del método de análisis. |
| respuesta en frecuencia | Relación entre salida y entrada de un sistema en función de la frecuencia. | No es el espectro de la salida. |
| serie de Fourier | Representación de una señal periódica como suma de componentes sinusoidales. | Declarar condiciones y alcance. |
| transformada de Fourier | Operación que representa una señal mediante componentes de frecuencia. | La DFT es la versión discreta para una secuencia finita. |
| FFT | Algoritmo eficiente para calcular una DFT. | No es una nueva magnitud ni un mecanismo físico. |
| bin | Ubicación o intervalo frecuencial discreto asociado con una DFT. | Depende de `f_s`, `N`, duración y convención. |
| ventana | Función temporal aplicada a un segmento antes del análisis. | Controla un compromiso; no elimina todos los errores. |
| fuga espectral | Distribución de la contribución de una componente entre varios bins debido al registro finito y su ventana. | No identificarla automáticamente con ruido. |
| frecuencia fundamental | Inversa del período fundamental de una señal periódica. | Puede no ser el máximo ni una línea presente. |
| armónico | Componente cuya frecuencia es `n f_0`, con `n` entero positivo. | El primer armónico es la fundamental si está presente. |
| parcial | Componente sinusoidal identificable de una señal compleja. | Puede ser armónico o inarmónico. |
| sobretono | Parcial por encima de la fundamental. | El primer sobretono suele ser el segundo parcial. |
| formante | Región de resonancia asociada al tracto vocal u otro sistema resonante. | No es sinónimo de armónico. |
| octava | Intervalo entre frecuencias cuya razón es `2:1`. | No equivale a una cantidad fija de hertz. |
| filtro | Sistema que modifica componentes según frecuencia. | Especificar tipo, cortes, pendiente y condiciones. |
| frecuencia de corte | Frecuencia definida por un criterio de atenuación que delimita una banda. | `−3 dB` no es universal para cualquier filtro o instrumento. |
| ponderación A | Respuesta frecuencial normalizada aplicada a una medición. | No cuantifica sonoridad individual ni dB HL. |
| sonómetro | Instrumento que mide niveles sonoros conforme a configuraciones y requisitos definidos. | Preferir “sonómetro”; evitar “decibelímetro”. |
| nivel equivalente | Nivel constante con la misma media cuadrática que la señal durante el intervalo. | No es promedio aritmético de dB. |

## Magnitudes y notación

| Entidad | Símbolo preferido | Unidad | Convención o riesgo |
|---|---:|---:|---|
| señal temporal genérica | `x(t)` | según variable | Para presión usar `p(t)`. |
| presión acústica instantánea | `p(t)` | Pa | Recuperada de U4. |
| tiempo | `t` | s | Eje temporal. |
| período fundamental | `T_0` | s | Menor período positivo. |
| frecuencia fundamental | `f_0` | Hz | No usar `F0` en ecuaciones. |
| transformada | `X(f)` | depende de convención | Declarar convención si se calculan amplitudes absolutas. |
| espectro de magnitud | `\lvert X(f)\rvert` | depende de convención | No llamarlo intensidad sin derivación física. |
| fase espectral | `φ_X(f)` | rad | No queda codificada en la altura de `\lvert X\rvert`. |
| coeficientes de serie | `a_0`, `a_n`, `b_n` | unidad de `x(t)` | Formalismo complementario. |
| índice armónico | `n` | 1 | Entero positivo. |
| unidad imaginaria | `j` | 1 | `j² = −1`; introducción mínima. |
| frecuencia de muestreo | `f_s` | Hz | `f_s = 1/T_s`. |
| período de muestreo | `T_s` | s | No confundir con `T_0`. |
| número de muestras | `N` | 1 | Entero; puede colisionar con sonoridad en U7. |
| duración observada | `T_obs` | s | Determina `Δf` nominal. |
| separación entre bins | `Δf` | Hz | No confundir con ancho de banda `B`. |
| respuesta en frecuencia | `H(f)` | razón o unidad definida | `H = Y/X` cuando procede. |
| entrada/salida espectral | `X(f)`, `Y(f)` | según convención | Usar rótulos además de símbolos. |
| ganancia | `G(f)` | dB | Para razón de amplitudes comparables: `20 log10 \lvert H\rvert`. |
| retardo | `τ` | s | Si coincide con transmisión en U9, calificar. |
| fase de respuesta | `φ_H(f)` | rad | Puede cambiar aunque `\lvert H\rvert = 1`. |
| límite inferior/superior | `f_L`, `f_H` | Hz | Declarar criterio. |
| frecuencia central | `f_c` | Hz | Para banda geométrica: `√(f_L f_H)`. |
| ancho de banda | `B` o `Δf_B` | Hz | Preferir `B` si no hay otra colisión. |
| denominador de fracción de octava | `b` | 1 | `b = 1` para octava, `b = 3` para tercio. |
| rango dinámico | `R_D` | dB | Diferencia entre niveles compatibles. |
| corrección A | `A(f)` | dB | Se aplica por frecuencia; no es nivel. |
| niveles ponderados | `L_A(f)`, `L_Z(f)` | dB(A), dB(Z) o descriptor completo | Preferir símbolos completos a `dBA` aislado. |
| presión ponderada | `p_X(t)` | Pa | `X` identifica A, C o Z. |
| presión de referencia | `p_ref` | Pa | En aire: `20 µPa` para SPL. |
| nivel equivalente | `L_Xeq,T` | dB con ponderación declarada | Para A: `L_Aeq,T`. |
| máximo A/Fast | `L_AFmax` | dB(A) | No equivale a pico. |
| nivel pico C | `L_Cpeak` | dB(C) | Detector de pico y configuración declarados. |

## Fórmulas y relaciones

| Relación | Significado | Prioridad | Tratamiento |
|---|---|---|---|
| `x(t + T) = x(t)` | Condición de periodicidad. | Central | Lectura conceptual y ejemplos. |
| `f_0 = 1/T_0` | Relación período–frecuencia fundamental. | Central | Cálculo breve con unidad. |
| `x(t) = a_0/2 + Σ[a_n cos(2πnf_0t) + b_n sin(2πnf_0t)]` | Serie trigonométrica de Fourier. | Central como mapa; complemento para operar | Identificar términos, no derivar en apertura. |
| `a_n = (2/T_0)∫x(t)cos(2πnf_0t)dt`, `b_n = ...` | Coeficientes de serie. | Respaldo/complemento | Interpretar proyección; cálculo integral no obligatorio. |
| `X(f) = ∫x(t)e^(−j2πft)dt` | Transformada de Fourier continua. | Central como formalización | Definir `j`, unidad y convención; no exigir cálculo. |
| `X(f) = \lvert X(f)\rvert e^(jφ_X(f))` | Separación magnitud–fase. | Importante | Vincular con tres gráficos de la misma señal. |
| `T_obs = N/f_s` | Duración del registro. | Importante | Cálculo guiado. |
| `Δf = f_s/N = 1/T_obs` | Separación nominal entre bins. | Importante | Diferenciar de precisión. |
| `q_B = Σ q_k` | Integración de contribuciones cuadráticas en banda. | Complementario | Declarar compatibilidad y no correlación. |
| `L_B = 10 log10(Σ10^(L_k/10))` | Suma de niveles compatibles por banda. | Complementario | Recuperar suma energética de U4. |
| `H(f) = Y(f)/X(f)` | Respuesta de sistema. | Central | Condición `X(f) ≠ 0` y entrada/salida comparables. |
| `G(f) = 20 log10 \lvert H(f)\rvert` | Ganancia de amplitud. | Central/Importante | Cálculo a una frecuencia e interpretación del signo. |
| `φ_H(f) = −2πfτ` | Fase de un retardo puro. | Complementario | Mostrar que magnitud y fase son independientes. |
| `R_D = L_sup − L_inf` | Rango dinámico. | Central | Extremos bajo misma magnitud, referencia y condición. |
| `f_c = √(f_L f_H)` | Centro geométrico. | Central | Comparar con promedio aritmético. |
| `f_H/f_L = 2^(1/b)` | Razón de una banda fraccional. | Central | `b = 1` y `b = 3`. |
| `f_L = f_c 2^(−1/2b)`, `f_H = f_c 2^(1/2b)` | Límites de banda. | Central | Ejemplo de tercio de octava. |
| `B = f_H − f_L` | Ancho absoluto de banda. | Central | Distinguir ancho relativo y `Δf`. |
| `L_A(f) = L_Z(f) + A(f)` | Corrección A para un tono. | Central con cautela | No generalizar a banda ancha. |
| `L_Xeq,T = 10 log10[(1/T)∫p_X²(t)/p_ref² dt]` | Nivel equivalente ponderado. | Importante/complementario | Primero promedio energético discreto; integral como formalización. |

## Representaciones y recursos existentes

| Recurso | Tipo | Contenido | Uso potencial | Limitación |
|---|---|---|---|---|
| `tiempo-magnitud-fase.pdf` | Gráfico propio | `p(t)`, amplitud por componente y fase. | Puente principal entre dominios. | Diseñado para página vertical; adaptar etiquetas. |
| `serie-fourier-progresiva.pdf` | Gráfico propio | Aproximación de onda rectangular. | Síntesis progresiva y Gibbs. | Conviene animación/revelado, no captura estática. |
| `compromiso-tiempo-frecuencia.pdf` | Gráfico propio | Dos espectrogramas con ventanas distintas. | Resolución temporal/frecuencial. | El color requiere leyenda grande y explicación previa. |
| `espectro-respuesta-sistema.tex` | Diagrama/gráfico propio | Entrada × respuesta = salida. | Nudo señal/sistema. | Reconstruir con objetos editables y ejes legibles. |
| `componentes-espectrales.tex` | Gráfico propio | Armónicos, inarmónicos y fundamental ausente. | Terminología y errores frecuentes. | Dividir o revelar por casos. |
| `bandas-octava-tercio.tex` | Diagrama cuantitativo propio | Una octava y tres tercios. | Razón, centro, límites y ancho. | Requiere escala final de aula. |
| `filtros-ideales-reales.pdf` | Gráfico propio | Cuatro tipos de filtro. | Clasificación e ideal/real. | Cuatro paneles pueden requerir dos slides. |
| `cadena-sonometro.tex` | Diagrama estructural propio | Micrófono → procesamiento → resultado. | Integración sonométrica. | Reconstruir mediante `diagram-generation` en la etapa correspondiente. |
| `generate_unit5_figures.py` | Script reproducible | Genera cuatro gráficos cuantitativos. | Base para adaptación de estilo. | Revisar parámetros y exportación al tamaño real de slide. |

## Ejemplos resueltos del capítulo

| Ejemplo | Conceptos | Uso preliminar |
|---|---|---|
| Presión con componentes de `100 Hz` y `200 Hz` | Periodicidad, `T_0`, fundamental, segundo armónico y fase. | Central; puente desde U3/U4. |
| Registro `f_s = 8000 Hz`, `N = 2000` | `T_obs` y `Δf`; comparación con registro más largo. | Central si se conserva bloque digital. |
| Sistema con `p_in = 0,020 Pa`, `p_out = 0,010 Pa` | `\lvert H\rvert = 0,50`, `G ≈ −6,02 dB`. | Central; señal frente a sistema. |
| Tercio de octava centrado en `1000 Hz` | `f_L`, `f_H`, `B`; redondeo. | Central; cálculo de bandas. |
| Tono de `63 Hz`, `L_Z = 80 dB(Z)` | Corrección A `−26,2 dB`, resultado `53,8 dB(A)`. | Central o complementario; requiere conservar fuente normativa. |
| `70 dB` y `80 dB` durante tiempos iguales | Promedio energético `≈77,4 dB`. | Importante; recupera suma/logaritmos. |

## Aplicaciones incluidas o sugeridas

| Aplicación | Concepto iluminado | Límite |
|---|---|---|
| Espectro/espectrograma de vocal | Periodicidad, líneas armónicas, envolvente y evolución temporal. | No diagnostica por sí solo. |
| Fuente glótica–tracto vocal | Señal frente a sistema; armónicos frente a formantes. | Modelo introductorio y dependiente del método. |
| Respuesta de audífono o dispositivo | Relación entrada–salida. | No es el espectro de la señal que lo atraviesa. |
| Ruido de banda en audiómetro | Filtrado audiométrico. | No confundir con ponderación A ni convertir SPL a HL. |
| Verificación de ambiente audiométrico | Bandas, instrumento y criterios. | No usar lectura global de teléfono ni límite universal en dB(A). |
| Medición ambiental | A/C/Z, `L_eq`, máximo, pico e intervalo. | Requiere configuración, calibración y procedimiento. |
| Preparación de cóclea y psicoacústica | Respuesta, bandas y selectividad. | No decir que el oído realiza una FFT. |

## Banco de ejercicios disponible

El capítulo contiene soluciones completas para todas las categorías:

| Categoría | Cantidad | Cobertura |
|---|---:|---|
| Preguntas conceptuales | 6 | Periodicidad, Fourier, componentes, resolución, señal/sistema, filtros/ponderación. |
| Lectura e interpretación de gráficos | 5 | Tiempo–magnitud–fase, síntesis, espectrograma, componentes y filtros. |
| Numéricos guiados | 5 | `f_0/T_0`, `T_obs/Δf`, tercio de octava, respuesta/ganancia y corrección A. |
| Numéricos autónomos | 5 | Resolución, octava, suma por banda, `L_Aeq` y fase/ganancia. |
| Aplicaciones en Fonoaudiología | 5 | Voz/formantes, ruido de ambiente, dispositivo, informe incompleto y rango vocal. |
| Pregunta integradora | 1 | Vocal + análisis digital + dispositivo + condiciones reproducibles. |
| Distractores y errores frecuentes | 4 | Fundamental, `Δf`, promedio energético y lectura `dB(A)`. |

La secuencia futura debería elegir, como máximo, un diagnóstico, un ejemplo, una comprobación y una transferencia por bloque. El resto corresponde a complemento o respaldo.

## Contenido que puede pasar casi directamente a slides

“Casi directamente” significa conservar idea, precisión y fuente, no copiar la página.

| Contenido | Fuente | Motivo |
|---|---|---|
| Contraste tiempo/frecuencia/fase | TEX 5.3 y figura 5.1 | Ejes y advertencias están definidos con claridad. |
| Periódica, aperiódica y transitoria | TEX 5.3.1 | Ejemplos acústicos y categorías no excluyentes. |
| Fourier no crea componentes | TEX 5.4 | Mensaje central y error frecuente. |
| Síntesis progresiva | Figura 5.2 | Visual potente para intuición antes del formalismo. |
| FFT como algoritmo de DFT | TEX 5.4.4 | Distinción breve y precisa. |
| Espectro de señal frente a respuesta de sistema | TEX 5.5 y figura 5.4 | Nudo curricular explícito. |
| Definiciones de componentes | TEX 5.6 y figura 5.5 | Terminología correcta con contraejemplos. |
| Cautelas sobre rangos | TEX 5.7 | Evita fronteras y umbrales universales. |
| Concepto de rango dinámico | TEX 5.7.2 | Definición con condiciones comunes. |
| Banda, centro, límites y ancho | TEX 5.8 y figura 5.6 | Ecuaciones y ejemplo resuelto consistentes. |
| Tipos de filtro | TEX 5.9 y figura 5.7 | Clasificación canónica e ideal/real. |
| Filtrado, ponderación y audiometría | TEX 5.9.1 | Comparación profesional directa. |
| Cadena funcional del sonómetro | TEX 5.11 y figura 5.8 | Integra la unidad sin depender de un modelo comercial. |
| Errores frecuentes | TEX 5.13 | Material para diagnóstico y recapitulación. |

## Necesidades de nuevos recursos

### Más explicación

- por qué el análisis frecuencial reorganiza la misma información;
- qué significa fase espectral sin exigir números complejos;
- diferencia y relación entre serie, transformada, DFT y FFT;
- por qué duración, ventana y normalización afectan un espectro;
- diferencia entre resolución, precisión e incertidumbre;
- diferencia entre bin, banda y densidad espectral;
- por qué `H(f)` necesita entrada y salida;
- relación entre fundamental, armónicos, formantes y pitch;
- por qué las fronteras auditivas y el umbral de dolor dependen de condiciones;
- cómo actúa una ponderación en una señal de banda ancha;
- diferencia entre promedio energético, máximo y pico.

### Más ejemplos

- dos señales con igual magnitud espectral y fase diferente;
- mismo tono con número entero y no entero de períodos en la ventana;
- mismo registro con dos duraciones para comparar `Δf`;
- misma salida producida por entradas/sistemas diferentes;
- serie con segundo armónico mayor y caso de fundamental ausente;
- octavas centradas en frecuencias distintas para comparar `B` en hertz;
- filtro ideal y respuesta real de un dispositivo documentado;
- misma medición con A y Z;
- informe incompleto de “72 dB” para reconstruir los metadatos faltantes.

### Gráficos cuantitativos

- reutilizar/adaptar las cuatro figuras generadas por script;
- curva nominal A/C/Z calculada y documentada;
- ejemplo de mismo espectro de magnitud con dos fases;
- señal vocal sintética o registro autorizado con envolvente/armónicos;
- comparación de respuesta de filtro y espectro de salida;
- rango dinámico con datos y condiciones de una fuente verificable;
- nivel equivalente frente a promedio aritmético.

### Diagramas estructurales

- mapa “señal temporal → método → representación”;
- tabla/flujo serie–transformada–DFT–FFT;
- entrada `X(f)` → sistema `H(f)` → salida `Y(f)`;
- fuente glótica → tracto vocal → radiación/registro, con límites del modelo;
- filtrado de señal vs ponderación de medición vs filtrado audiométrico;
- cadena del sonómetro con corredores y conectores editables.

Los diagramas deberán derivarse a `diagram-generation` en una etapa posterior y cumplir el ciclo de renderizado y corrección del repositorio.

### Imágenes técnicas

- fotografía de un sonómetro y calibrador con fuente/licencia;
- fotografía o captura técnica de un sistema de medición de voz, solo si explica el montaje;
- interfaz de software espectral únicamente si permite enseñar parámetros y no funciona como decoración;
- transductor o audífono con respuesta publicada, si se necesita un caso real.

### Animaciones

- suma progresiva de componentes de Fourier;
- modificación de fase con magnitud constante;
- desplazamiento del contenido entre bins al cambiar duración/ventana;
- construcción de espectrograma por ventanas sucesivas;
- barrido de frecuencia atravesando filtros;
- revelado secuencial de la cadena del sonómetro.

Ninguna animación debe ser indispensable para comprender la versión estática.

### Demostraciones

- generar y escuchar componentes aisladas y su suma a nivel seguro;
- analizar una vocal sostenida en vivo y discutir qué no permite concluir;
- variar duración y ventana en un software de análisis;
- aplicar filtros audibles a habla o ruido;
- comparar A/Z con sonómetro disponible;
- calcular `L_eq` de dos intervalos y contrastarlo con promedio de dB.

### Actividades

- clasificar gráficos como señal, sistema o medición;
- completar ejes, unidades y metadatos faltantes;
- reconstruir `f_0` a partir de separación entre líneas;
- detectar un formante confundido con armónico;
- ordenar serie, transformada, DFT y FFT por objeto y operación;
- elegir ventana larga/corta según pregunta;
- calcular una banda y justificar centro geométrico;
- identificar filtro y región de transición;
- decidir si una corrección A de tono puede generalizarse;
- auditar un informe sonométrico incompleto.

## Conceptos que deben recordarse durante la unidad

- `f = 1/T` y la unidad `Hz`;
- senoide, fase y superposición;
- presión acústica `p(t)` en `Pa`;
- diferencia entre pico y RMS;
- nivel como razón logarítmica con referencia;
- suma energética de contribuciones no correlacionadas;
- frecuencia física frente a pitch;
- nivel físico frente a sonoridad;
- toda gráfica requiere ejes, unidades, escala y condiciones;
- un mismo aspecto visual no garantiza que dos gráficos representen el mismo objeto.

## Preparación de unidades futuras

| Concepto de U5 | Unidad futura | Uso posterior |
|---|---|---|
| respuesta en frecuencia | U6 | Transferencia del oído externo/medio y selectividad coclear. |
| espectro y bandas | U6–U7 | Tonotopía, timbre y filtros auditivos. |
| fundamental/armónicos/formantes | U7 | Pitch y timbre. |
| resolución y espectrograma | U7–U8 | Voz, habla y lectura crítica de análisis. |
| filtros | U7–U8–U10 | Enmascaramiento, estímulos, dispositivos y ruidos de banda. |
| ponderaciones y sonómetro | U8–U10 | Ambiente de prueba, exposición y medición de ruido. |
| `L_eq`, máximo y pico | U10 | Caracterización temporal y exposición. |
| separación señal/sistema | U6–U8 | Oído, audífonos, implantes y pruebas. |

## Contenido fuera de alcance actual

- demostraciones matemáticas de convergencia y condiciones de Dirichlet;
- transformadas generalizadas y distribuciones;
- diseño algorítmico de FFT;
- teorema de muestreo y aliasing en profundidad, salvo puente mínimo si se incorpora;
- estimación espectral avanzada, PSD, promediado Welch y análisis cepstral;
- diseño de filtros FIR/IIR, polos y ceros;
- análisis clínico de formantes, jitter, shimmer u otros parámetros de voz;
- modelos perceptuales de pitch, sonoridad y timbre, reservados para U7;
- calibración audiométrica detallada y RETSPL, reservadas para U8;
- certificación, evaluación de modelo o ensayo periódico de sonómetros;
- límites legales de exposición o requisitos jurisdiccionales, reservados para U10 y fuentes aplicables.

## Términos para el glosario de la unidad

- señal;
- señal compleja o compuesta;
- dominio temporal;
- espectro;
- espectro de magnitud;
- espectro de fase;
- serie de Fourier;
- transformada de Fourier;
- DFT;
- FFT;
- bin;
- ventana;
- fuga espectral;
- resolución frecuencial;
- espectrograma;
- respuesta en frecuencia;
- frecuencia fundamental;
- armónico;
- parcial;
- sobretono;
- formante;
- infrasonido;
- ultrasonido;
- rango dinámico;
- octava;
- tercio de octava;
- filtro;
- frecuencia de corte;
- frecuencia central;
- ancho de banda;
- ponderación A;
- sonómetro;
- nivel equivalente;
- nivel máximo;
- nivel pico.
