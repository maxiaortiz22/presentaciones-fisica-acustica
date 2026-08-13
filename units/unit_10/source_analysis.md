# Unidad 10 — Análisis de fuentes

## Fuentes consultadas

1. `AGENTS.md`.
2. `context/programa/Programa de Física Acústica.pdf`, especialmente p. 5 de 6.
3. `course_map.md`, sección Unidad 10 y comparación programa–libro.
4. `course_dependency_map.md`, matriz de prerrequisitos, recuperaciones y dependencia crítica U10.
5. `content_coverage_matrix.csv`, filas U10-01 a U10-X1.
6. `context/libro_latex/main.tex` y `context/libro_latex/chapters/10-ruido-caracterizacion.tex` completo.
7. `context/libro_latex/figures/scripts/unidad-10/generate_unit10_figures.py`.
8. Los tres TikZ y los cuatro PDF generados de `figures/.../unidad-10/`.
9. `context/libro_pdf/Física Acústica para Fonoaudiología.pdf`, páginas físicas 261–290.
10. `style/presentation_style_guide.md`, `style/notation_guide.md` y `style/glossary.md`.

No se consultaron fuentes externas nuevas. Las referencias bibliográficas del capítulo se inventariaron como respaldo documental, sin asumir que su sola cita autoriza reproducir valores o procedimientos.

## Alcance obligatorio extraído del programa

La formulación del programa es: “Tipos de ruido y su clasificación. Diferencia entre ruido y sonido. Ruido aleatorio. Ruido blanco, rosa, vocal y de banda estrecha (NBN). Revisión de la técnica de enmascaramiento”.

Interpretación curricular:

- la clasificación no puede limitarse a colores; debe incluir al menos el criterio temporal y el espectral;
- la diferencia ruido/sonido debe explicitar el papel de tarea y contexto;
- “ruido aleatorio” requiere alguna descripción estadística, aunque el programa no indique profundidad;
- blanco/rosa requieren bandas y densidad para evitar definiciones erróneas;
- “ruido vocal” debe vincularse con el término técnico preferido del repositorio;
- “revisión de la técnica” exige recuperar el propósito audiométrico, pero no autoriza inventar un protocolo.

## Estructura del capítulo LaTeX

El capítulo contiene 20 secciones numeradas en el PDF:

- propósito, prerrequisitos y situación introductoria;
- sonido/ruido y determinístico/aleatorio;
- estacionariedad y clasificación temporal;
- estadística y descripción frecuencial;
- blanco, rosa, espectro de habla y NBN;
- descriptores y exposición;
- SNR y ruido de fondo;
- enmascaramiento aplicado;
- salud, normativa y control;
- Fonoaudiología, errores, síntesis, ejercicios, soluciones, glosario y fuentes.

Incluye 11 ecuaciones numeradas, 7 figuras, 2 tablas conceptuales, 32 grupos sustantivos de actividades, 5 distractores adicionales y soluciones. La organización es más amplia que el programa, pero mantiene advertencias de alcance y evita presentar límites universales.

## Verificación del PDF

Se extrajo el texto y se renderizaron las 30 páginas del capítulo. La correspondencia es:

| PDF | Contenido principal |
|---|---|
| 261–264 | Propósito, conocimientos previos, situación, ruido/sonido, aleatoriedad y estacionariedad. |
| 264–267 | Clasificación temporal, media/RMS/varianza y distribución. |
| 268–271 | PSD, blanco, rosa, espectro de habla, NBN y conformación espectral. |
| 272–274 | Descriptores, nivel equivalente, percentiles, SNR y gráfico de mezclas. |
| 275 | Enmascaramiento audiométrico introductorio. |
| 276–280 | Exposición, documentos, control, Fonoaudiología, errores y síntesis. |
| 281–284 | Ejercicios y autoevaluación. |
| 285–289 | Soluciones y orientaciones. |
| 290 | Glosario y alcance documental. |

No se observaron páginas, ecuaciones o figuras faltantes, clipping ni fallas sustantivas de compilación. LaTeX y PDF pueden considerarse concordantes para el análisis. Las figuras son legibles en página, pero su tipografía y densidad no son apropiadas para reutilización directa en aula.

## Comparación programa–LaTeX–PDF

| Tema del programa | LaTeX/PDF | Evaluación | Decisión pedagógica |
|---|---|---|---|
| Tipos y clasificación | Temporal, estadística, espectral y funcional. | Cubierto y ampliado. | Mantener temporal + espectral en el núcleo; no copiar todas las taxonomías como lista. |
| Diferencia ruido/sonido | Tres usos del término y caso contextual. | Cubierto con buena profundidad. | Puede transferirse con transformación visual moderada. |
| Ruido aleatorio | Determinístico, realización, pseudoaleatorio, estacionariedad y estadísticas. | Cubierto y ampliado. | Conservar intuición y descriptores; limitar formalismo estocástico. |
| Ruido blanco | PSD constante por Hz y banda finita. | Cubierto rigurosamente. | Central; exigir contraste con energía por octava. |
| Ruido rosa | PSD `K/f` e integral por octava. | Cubierto rigurosamente. | Central conceptualmente; derivación como complemento. |
| Ruido vocal | Ruido con forma espectral vocal y dependencia de especificación. | Cubierto, con corrección terminológica. | Presentar equivalencia con el término del programa. |
| NBN | Límites, centro, ancho, pendientes y uso audiométrico. | Cubierto. | Central; no igualar a tercio de octava. |
| Revisión de enmascaramiento | Fenómeno recuperado de U7, ruta cruzada, función y límites. | Parcial respecto de una técnica clínica completa. | Cubrir función y arquitectura; protocolo solo con decisión y fuente clínica. |

## Aportes del capítulo fuera del programa

El capítulo amplía con estacionariedad, distribución, PSD, descriptores temporales, percentiles, nivel equivalente, exposición, SNR, salud, lectura de documentos y control. La ampliación es coherente con el cierre integrador y con `course_map.md`, pero no todo debe ocupar el mismo nivel de prioridad.

Se consideran ampliaciones especialmente útiles: estacionariedad, PSD mínima para blanco/rosa, máximo/pico/equivalente, SNR y control. Se consideran complementarios o de respaldo: derivación rosa, percentiles en profundidad, dosis, normativa cuantitativa, selección de protectores y acufenometría.

## Fortalezas de las fuentes

- El capítulo distingue fenómeno, señal, tarea, percepción y salud.
- Las fórmulas incluyen símbolos, unidades, ejemplos y condiciones.
- Los modelos blanco y rosa se limitan a bandas finitas.
- Las figuras cuantitativas son reproducibles y declaran datos sintéticos.
- Los diagramas de enmascaramiento y control incluyen advertencias de alcance.
- Las actividades cubren concepto, gráfico, cálculo, aplicación y distractores.
- Las fuentes normativas y clínicas se citan cerca de la afirmación correspondiente.
- El texto evita certificar cabinas, recomendar terapia o fijar límites universales.

## Vacíos, tensiones y desbalances

### Brecha curricular principal

La matriz ya marca “revisión de técnica de enmascaramiento” como `external_expansion`. Faltan indicaciones, niveles iniciales, atenuación interaural, efecto de oclusión, sobreenmascaramiento, incrementos y método de meseta. No deben añadirse de memoria.

### Sobrecarga potencial

La secuencia media/RMS/varianza → distribución → PSD → integral → blanco/rosa puede exceder la base matemática de primer año. Requiere ejemplos y representaciones previas. El capítulo es correcto como texto, pero no puede convertirse linealmente en slides.

### Ausencias de recurso

- No hay audios inventariados para comparar tipos de ruido.
- No hay datos reales de aula, consultorio o exposición; las figuras son sintéticas.
- No hay una curva universal de “ruido vocal”, decisión correcta pero que exige un ejemplo documentado si se desea mostrar una.
- No hay tabla normativa reproducible para exposición o cabinas.
- No hay protocolo clínico completo de enmascaramiento.

### Localizadores desactualizados

`content_coverage_matrix.csv` conserva numeración anterior. En el PDF actual:

- clasificación temporal es 10.6 y descripción frecuencial 10.8;
- enmascaramiento aplicado es 10.11, no 10.8;
- métricas, exposición y control se extienden aproximadamente entre 10.7 y 10.13, no solo 10.2–10.7.

Los estados de cobertura siguen siendo razonables; los `book_section` requieren actualización posterior mediante `course-architecture`.

## Consistencia terminológica y de notación

| Punto | Fuente | Guía transversal | Decisión recomendada |
|---|---|---|---|
| “Ruido vocal” | Programa. | Preferir ruido con espectro de habla. | Mostrar equivalencia una vez y usar el término preferido. |
| Presión de referencia | Un ejemplo del capítulo usa `p_0=20 µPa`. | Reservar `p_0` para estática y usar `p_ref`. | Corregir en slides a `p_ref=20 µPa`. |
| Nivel equivalente A | El capítulo alterna formas tipográficas. | Usar `L_Aeq,T`. | Normalizar subíndices y declarar `T`. |
| Pico y máximo | El capítulo usa símbolos genéricos. | Preferir descriptores completos como `L_AFmax` y `L_Cpeak` cuando se especifique configuración. | Empezar genérico y pasar al descriptor completo en medición. |
| Reducción `R` | Ejemplo del capítulo define `R=L_i-L_f`. | `R` queda reservado al índice de reducción sonora en U9. | Usar `ΔL` o escribir “reducción” sin nuevo símbolo. |
| PSD | Capítulo usa `S_pp(f)`. | Guía usa `S_x(f)` y admite caso de presión. | Conservar `S_pp(f)` y definir Pa²/Hz. |

## Qué puede pasar casi directamente a una presentación

- la situación del consultorio junto a una avenida;
- los tres usos de “ruido”;
- el contraste determinístico/aleatorio;
- las cuatro definiciones temporales;
- el ejemplo de media cero con RMS no nulo;
- el contraste igual RMS/diferente distribución;
- el mensaje blanco por Hz/rosa por octava;
- los parámetros que especifican un NBN;
- la distinción fondo/enmascarante/protección;
- los tres planos exposición–función–salud;
- el mapa fuente–trayecto–receptor;
- la lista de errores frecuentes y la pregunta integradora.

“Casi directamente” significa conservar el razonamiento, no copiar párrafos. Las tablas y figuras deben remaquetarse con la guía visual.

## Qué requiere más elaboración

- **Explicación:** estacionariedad, PSD, unidades por Hz, promedio energético y detectores.
- **Ejemplos:** ventanas temporales, igual `L_eq` con picos distintos, NBN especificado y SNR contextual.
- **Gráficos:** densidad × ancho; máximo/pico/equivalente; curva documentada de espectro de habla si se adopta.
- **Diagramas:** reconstrucción editable de los tres TikZ; mapa fenómeno–señal–tarea.
- **Imágenes:** solo mediciones o montajes técnicos con función pedagógica.
- **Animaciones:** clasificación temporal, integración por octavas, ruta cruzada y control por eslabón.
- **Demostraciones:** audios seguros y nivelados; medición exploratoria no normativa.
- **Actividades:** clasificación, selección de descriptor, detección de información faltante y caso integrador.

## Referencias internas citadas por el capítulo

El capítulo registra, entre otras, ISO 389-4:1994, IEC 60645-1:2017, ISO 8253-1:2010, ANSI/ASA S3.1-1999 (R2023), ISO 4869-2:2018, NIOSH 98-126, guías ASHA, OMS 2018 y normativa argentina. En una etapa posterior deberá comprobarse edición, vigencia, jurisdicción, acceso al texto completo y permiso de reproducción antes de extraer cifras, tablas o procedimientos.

## Conclusión

Programa, LaTeX y PDF coinciden en el núcleo de clasificación, ruido aleatorio, tipos espectrales y revisión funcional del enmascaramiento. El capítulo ofrece material suficiente y pedagógicamente responsable, pero su amplitud exige una frontera clara entre núcleo, complemento y respaldo. La unidad no debe pasar a storyboard hasta resolver el alcance clínico del enmascaramiento, el tiempo disponible, la profundidad matemática, la notación y las fuentes normativas.
