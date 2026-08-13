# Unidad 10 — Inventario de contenidos

## Criterio de clasificación

- **Imprescindible:** requisito explícito del programa o prerrequisito inmediato para explicarlo correctamente.
- **Importante:** ampliación del libro que permite medir, aplicar o evitar un error central.
- **Complementario:** profundiza, contextualiza o aporta práctica sin ser necesario para la evidencia mínima.
- **Respaldo:** útil para consulta, soluciones o decisiones normativas; no debe interrumpir la ruta principal.

## Conceptos principales

| Concepto | Prioridad | Función pedagógica | Fuente principal |
|---|---|---|---|
| Sonido, señal y ruido contextual | Imprescindible | Evitar una diferencia física absoluta. | Programa; LaTeX 10.3–10.4; PDF 262–263. |
| Señal determinística y proceso aleatorio | Imprescindible | Definir qué se predice y qué se describe estadísticamente. | LaTeX 10.5; PDF 263–264. |
| Estacionariedad | Importante | Conectar estadística con ventana de observación. | LaTeX 10.5.1; PDF 263–264. |
| Clasificación temporal | Imprescindible | Distinguir continuo, fluctuante, intermitente e impulsivo. | LaTeX 10.6; PDF 264–265. |
| Media, RMS, varianza y distribución | Importante | Caracterizar realizaciones sin reducirlas a un solo número. | LaTeX 10.7; PDF 264–267. |
| Densidad espectral y contenido de banda | Imprescindible como soporte | Explicar blanco, rosa y ruido filtrado. | LaTeX 10.8; PDF 268–271. |
| Ruido blanco | Imprescindible | Densidad constante por Hz en una banda declarada. | Programa; LaTeX 10.8.1. |
| Ruido rosa | Imprescindible | Contenido aproximadamente constante por octava. | Programa; LaTeX 10.8.2. |
| Ruido con espectro de habla | Imprescindible | Precisar “ruido vocal” y su dependencia de una especificación. | Programa; LaTeX 10.8.3. |
| Ruido de banda estrecha (NBN) | Imprescindible | Definir límites, centro, ancho, pendientes y uso. | Programa; LaTeX 10.8.4. |
| Descriptores temporales y de exposición | Importante | Elegir una métrica coherente con la pregunta. | LaTeX 10.9; PDF 272–273. |
| SNR y ruido de fondo | Importante | Conectar medición con comunicación y prueba sin sobreinferir. | LaTeX 10.10; PDF 273–274. |
| Enmascaramiento aplicado | Imprescindible | Revisar función, señales, oídos y límites de protocolo. | Programa; LaTeX 10.11; PDF 275. |
| Exposición, salud y comunicación | Complementario cercano | Separar exposición, función y salud. | LaTeX 10.12; PDF 276–277. |
| Control fuente–trayecto–receptor | Importante | Integrar U9 y elegir el eslabón de intervención. | LaTeX 10.13; PDF 277–278. |

## Conceptos secundarios y distinciones

- realización de un proceso aleatorio;
- señal pseudoaleatoria y semilla;
- continuo estable frente a continuo fluctuante;
- histograma y distribución gaussiana como modelo, no como consecuencia de “ruido”;
- densidad unilateral y banda finita;
- igual ancho en Hz frente a igual ancho en octavas;
- respuesta objetivo `|H_v(f)|` y pasabanda `|H_B(f)|`;
- nivel instantáneo, `L_max`, `L_peak`, `L_eq,T` y `L_n,T`;
- ponderación frecuencial, respuesta temporal, detector e intervalo;
- ruido de fondo, ambiente residual y enmascarante deliberado;
- exposición, resultado funcional/perceptual y resultado de salud;
- norma de medición, guía sanitaria y criterio legal/ocupacional;
- reducción como resultado; absorción, aislamiento, cancelación activa y protección como mecanismos o intervenciones;
- medición exploratoria frente a medición calibrada y trazable.

## Magnitudes y fórmulas

| Magnitud/relación | Expresión de fuente | Unidad/condición | Prioridad | Tratamiento futuro |
|---|---|---|---|---|
| Media de presión | `p̄ = (1/N) Σ p_i` | Pa; ventana y muestras declaradas. | Central | Ejemplo con 4–5 muestras. |
| RMS | `p_rms = √[(1/N) Σ p_i²]` | Pa; no llamarlo “promedio”. | Central | Relacionar con U4 y nivel. |
| Varianza | `σ_p² = (1/N) Σ(p_i-p̄)²` | Pa²; intervalo declarado. | Central | Comparar con RMS, no memorizar aislada. |
| Identidad estadística | `p_rms² = σ_p² + p̄²` | Pa². | Complementario cercano | Visualizar caso media cero y caso constante. |
| Contenido de banda | `p_B,rms² = ∫[f_L,f_H] S_pp(f) df` | `S_pp`: Pa²/Hz; resultado: Pa². | Central conceptual | Introducir antes como área; integral sin cálculo avanzado. |
| Ruido blanco ideal | `S_pp(f)=S_0` | Banda finita declarada. | Central | Comparar bandas de igual ancho en Hz. |
| Ruido rosa ideal | `S_pp(f)=K/f` | `K` en Pa² para esta convención. | Central conceptual | Fórmula secundaria; el criterio por octava es el mensaje principal. |
| Contenido rosa por octava | `∫[f_1,2f_1] K/f df = K ln 2` | Pa²; modelo ideal. | Complementario | Puede quedar como demostración o respaldo. |
| Ancho NBN | `B=f_H-f_L` | Hz; declarar criterio de corte y pendientes. | Central | Cálculo breve. |
| Nivel equivalente de intervalos iguales | `L_eq=10 log10[(1/M)Σ10^(L_j/10)]` | Mismos descriptor, referencia, ponderación y duración. | Importante | Ejemplo energético; no extrapolar a duraciones desiguales. |
| SNR | `SNR=L_señal-L_ruido` | dB; misma banda, posición, referencia e intervalo. | Central | Interpretar signo y límites. |
| Cambio/reducción | `L_f-L_i=10 log10(I_f/I_i)` | Intensidades compatibles y mismo punto/condiciones. | Complementario | Evitar llamar `R` al resultado para no colisionar con U9. |

### Magnitudes y símbolos que deben conservarse

`p(t)`, `p̄`, `p_rms`, `σ_p²`, `S_pp(f)`, `f_L`, `f_c`, `f_H`, `B`, `L_eq,T`, `L_Aeq,T`, `L_AFmax`, `L_Cpeak`, `L_n,T` y `SNR`.

En las slides se deberá usar `p_ref` para la referencia de nivel, no `p_0`; y normalizar la escritura de `L_Aeq,T` según `style/notation_guide.md`.

## Ejemplos disponibles en el capítulo

| Ejemplo | Uso | Prioridad |
|---|---|---|
| Consultorio junto a avenida | Hilo conductor: tarea, fuente, trayecto, receptor y contexto. | Central. |
| Cinco muestras `−2,−1,0,1,2 mPa` | Media cero con RMS y varianza no nulos. | Central. |
| Densidad constante en 100 Hz | Conversión de Pa²/Hz a Pa², Pa y dB SPL. | Complementario cercano. |
| Cuatro intervalos de 15 min | Promedio energético de `L_Aeq`. | Importante. |
| Señal a 65 dB SPL y ruido a 58 dB SPL | SNR de +7 dB sin inferencia perceptual. | Central. |
| Intensidad final `0,1 I_i` | Reducción de 10 dB bajo comparación definida. | Complementario. |

## Ejercicios y actividades disponibles

El capítulo ofrece 32 grupos sustantivos de consignas, 5 distractores adicionales y sus soluciones/orientaciones:

- 10 preguntas conceptuales;
- 7 actividades de lectura de gráficos;
- 5 ejercicios numéricos guiados;
- 4 ejercicios numéricos autónomos;
- 5 aplicaciones a Fonoaudiología;
- 1 pregunta integradora;
- 5 distractores para justificar.

Selección preliminar para la ruta central, sin convertirla todavía en storyboard:

1. clasificar registros temporales y justificar categorías simultáneas;
2. calcular media/RMS/varianza en un conjunto pequeño;
3. explicar igual RMS con histogramas distintos;
4. relacionar blanco/rosa con integración por bandas;
5. calcular ancho de un NBN y enumerar datos faltantes;
6. comparar promedio aritmético y energético de niveles;
7. calcular SNR e interpretar el signo;
8. identificar señales y oídos en el diagrama de enmascaramiento;
9. clasificar controles por fuente, trayecto y receptor;
10. resolver el caso integrador del consultorio.

El resto puede distribuirse entre complemento, guía o respaldo.

## Recursos visuales existentes

| Recurso | Tipo | Estado conceptual | Adaptación necesaria para slides |
|---|---|---|---|
| `realizaciones-temporales-ruido.pdf` | Gráfico reproducible | Cuatro categorías con mismos ejes. | Regenerar con estilo del deck, tipografía 16–20 pt y posible revelado por etapas. |
| `estadistica-mismo-rms.pdf` | Gráfico reproducible | Tiempo + histogramas, igual media/RMS/varianza. | Probable división en dos slides para legibilidad. |
| `blanco-rosa-energia-bandas.pdf` | Gráfico reproducible | PSD y contenido por octavas. | Separar densidad e integración por bandas o usar dos etapas. |
| `relaciones-senal-ruido.pdf` | Gráfico reproducible | Misma señal/ruido escalado para tres SNR. | Puede acompañarse con audio sintético normalizado. |
| `conformacion-espectral.tex` | Diagrama estructural | Banda ancha → filtro → habla/NBN. | Reconstruir editable con `diagram-generation`; texto actual es de página. |
| `enmascaramiento-audiometrico-conceptual.tex` | Diagrama estructural | Señal de prueba, ruta cruzada y enmascarante. | Reconstruir editable; preservar advertencia “no es protocolo”. |
| `control-fuente-trayecto-receptor.tex` | Diagrama estructural | Ubica acciones y resultado comparado. | Reconstruir editable; puede requerir dos etapas. |

El script `context/libro_latex/figures/scripts/unidad-10/generate_unit10_figures.py` usa señales sintéticas, semillas fijas y modelos analíticos; no contiene datos clínicos ni límites normativos. Es una base reproducible adecuada, pero su estilo tipográfico corresponde al libro, no al aula.

## Necesidades de transformación didáctica

| Parte | Pasa casi directamente | Necesita transformación |
|---|---|---|
| Sonido/ruido/contexto | Definiciones y caso inicial. | Convertir tres usos en comparación visual y actividad. |
| Determinístico/aleatorio | Contraste conceptual. | Añadir predicción vs estadística y realización; evitar exceso de texto. |
| Clasificación temporal | Definiciones y figura. | Revelado o animación breve; ejemplos auditivos opcionales. |
| Estadística | Ejemplo numérico y figura. | Escalonar intuición → cálculo → distribución; no mostrar cuatro fórmulas juntas. |
| PSD | Unidades e integral. | Preparar con área de rectángulo y banda antes del símbolo integral. |
| Blanco/rosa | Explicación y gráfico propios. | Añadir escucha segura/normalizada y advertir banda finita. |
| Espectro de habla/NBN | Diagrama y parámetros. | Ejemplo espectral o señal de equipo con fuente; no inventar curva universal. |
| Métricas | Tabla del libro. | Dividir por preguntas; `L_max` vs `L_peak` merece contraste propio. |
| SNR | Fórmula, ejemplo y figura. | Conectar con una tarea, pero no con resultado universal. |
| Enmascaramiento | Texto y diagrama funcional. | Reponer brevemente U7 y definir el límite entre concepto y protocolo. |
| Exposición/normas | Separación de planos y tipos de documento. | Ejemplos contextualizados; cifras solo con fuente vigente y aplicable. |
| Control | Mapa y terminología. | Caso antes/después; distinguir resultado de mecanismo. |

## Recursos adicionales propuestos, sin producirlos aún

- **Más explicación:** PSD, promedio energético, detectores máximo/pico y ruta cruzada.
- **Más ejemplos:** estacionariedad a dos escalas; mismo `L_eq,T` con picos distintos; NBN con banda declarada; SNR en habla.
- **Gráficos:** ventana corta/larga; densidad × ancho; máximo/pico/equivalente sobre una misma señal; espectro de habla solo con fuente verificada.
- **Diagramas:** mapa “fenómeno–señal–tarea–efecto”; cadena de medición con ponderaciones; reconstrucción de los tres TikZ.
- **Imágenes:** foto técnica de medición o cabina solo si enseña posición, equipo o contexto; no usar stock decorativo.
- **Animaciones:** expansión de banda, integración por octavas, ruta cruzada y controles por eslabón; siempre con estado estático completo.
- **Demostraciones:** escucha comparada de blanco/rosa/NBN/espectro de habla a nivel seguro y normalizado; comparación exploratoria con sonómetro, aclarando que no certifica.
- **Actividades:** clasificación de registros, selección de descriptor, detección de datos faltantes y plan de caracterización.

## Glosario necesario

Ruido; aleatorio; realización; estacionariedad; continuo; fluctuante; intermitente; impulsivo; media; RMS; varianza; distribución; densidad espectral de potencia; ruido blanco; ruido rosa; ruido con espectro de habla; NBN; nivel equivalente; nivel máximo; nivel de pico; percentil de excedencia; SNR; ruido de fondo; enmascarante; enmascaramiento; exposición; absorción; aislamiento; cancelación activa; protección auditiva.

## Frontera central, complementaria y de respaldo

| Núcleo | Central | Complementario | Respaldo |
|---|---|---|---|
| Clasificación | Contexto, aleatorio, temporal, blanco/rosa/habla/NBN. | Pseudoaleatoriedad y más ejemplos. | Taxonomías normativas específicas. |
| Estadística | Media, RMS, varianza, distribución intuitiva. | Identidad y cálculos adicionales. | Probabilidad formal, autocorrelación. |
| Frecuencia | PSD como densidad y banda; comparación blanco/rosa. | Integral rosa y normalizaciones. | Derivaciones estocásticas. |
| Medición | Máximo, pico, equivalente y SNR. | Percentiles y promedios múltiples. | Dosis y tablas normativas. |
| Audiología | Función del enmascarante y ruta cruzada. | Acufenometría y elección general de señal. | Protocolo completo de masking. |
| Control/salud | Tres planos de inferencia y fuente–trayecto–receptor. | Tipos de documento, cancelación activa y protección. | Límites legales, selección de protector y certificación. |
