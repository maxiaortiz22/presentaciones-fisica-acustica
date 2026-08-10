# Revisión pedagógica independiente — Unidad 5

**Unidad:** Análisis frecuencial de señales acústicas
**Deck revisado:** `output/unidad_05_analisis_frecuencial_v02.pptx`
**Fecha de revisión:** 2026-08-03
**Tipo de revisión:** segunda lectura docente, independiente de las decisiones de diseño y secuenciación previas
**Estado de esta pasada:** solo diagnóstico; no se modificó el PowerPoint

## 1. Fuentes y método

Se contrastaron:

- el programa oficial, Unidad 5;
- el capítulo 5 del libro en LaTeX y su versión PDF, pp. 119–149;
- `brief.md`;
- `storyboard.md`;
- `speaker_notes.md`;
- las 150 slides del deck v02 y el render completo;
- `review.md`, incluida su declaración de problemas cerrados.

La evaluación se realizó como si el material fuera recibido por un segundo docente que no participó en su producción. No se consideró correcta por defecto la estructura actual ni se usó la revisión anterior como criterio de aprobación.

## 2. Dictamen general

La unidad tiene buena cobertura del programa, una base conceptual cuidadosa y notas del orador que anticipan varios errores frecuentes. Como **banco de recursos**, es valiosa. Como **secuencia de clase por defecto**, todavía no está pedagógicamente resuelta.

El problema principal no es la ausencia de contenido, sino su exceso, su jerarquía poco visible y la cantidad de cambios de nivel de abstracción. El storyboard propone 150 slides, de las cuales 104 son centrales, con una duración estimada de 438 minutos. La distribución en cinco encuentros incluye un tercer encuentro estimado en 116 minutos y el propio storyboard reconoce que podría requerir una sexta clase. Esto confirma que el recorrido central no es una ruta realista para un grupo de primer año sin recortes sustanciales.

El tramo más exigente —serie y transformada de Fourier, muestreo, DFT/FFT, bins, resolución, ventanas, fuga y espectrograma— aparece antes de que la aplicación vocal y profesional tenga suficiente peso motivador. El resultado es una larga secuencia de formalización y metrología digital que puede hacer que los estudiantes aprendan nombres y fórmulas sin consolidar para qué problema sirve cada herramienta.

**Conclusión pedagógica:** no aprobaría la v02 como ruta de proyección completa. Sí la aprobaría como repositorio de material a partir del cual construir una ruta central más corta, explícita y dividida en seis encuentros o en dos submódulos.

## 3. Fortalezas que conviene preservar

1. **La pregunta organizadora es pertinente.** La unidad insiste en identificar objeto, ejes, unidades, condiciones y límite de la inferencia antes de interpretar un gráfico.
2. **La cobertura del programa es completa.** Se incluyen Fourier, espectro y respuesta, rangos, componentes, octavas y bandas, filtros, ponderación A y sonometría.
3. **Las cautelas conceptuales son buenas.** Se evita equiparar dB(A), dB SPL, dB HL, sonoridad y pitch; también se evita presentar umbrales o rangos dinámicos como universales.
4. **Las notas proponen recuperación activa.** Las recapitulaciones U05-017, 029, 040, 051, 062, 073, 083, 094, 105, 116, 124 y 130 contienen preguntas de clasificación, decisión o justificación, no solo repetición.
5. **El libro contiene ejemplos y figuras adecuados.** En particular, la figura 5.3 permite enseñar el compromiso tiempo–frecuencia con dos espectrogramas comparables, y los ejercicios del capítulo ofrecen tareas interpretativas de mejor calidad que varias slides actuales.
6. **La separación señal/sistema/medición está bien orientada.** Es una distinción difícil y relevante para Fonoaudiología; debe mantenerse, pero con una entrada más concreta.

## 4. Problemas pedagógicos abiertos

Todos los problemas de esta tabla quedan **open**, porque esta primera pasada no modifica el deck.

| ID | Severidad | Prioridad | Evidencia | Diagnóstico pedagógico | Cambio propuesto | Estado |
|---|---|---|---|---|---|---|
| IPR-01 | major | imprescindible | 150 slides; 104 centrales; 438 min; B06–B08 suma 116 min | La ruta central supera una carga razonable para cinco clases y exige demasiados cambios conceptuales por encuentro. El estudiante puede completar actividades locales sin construir un mapa estable de la unidad. | Definir una ruta central de aproximadamente 65–80 slides y seis encuentros, o dividir la unidad en 5A y 5B. Mantener el resto como ampliación y respaldo. | open |
| IPR-02 | major | imprescindible | Slides complementarias intercaladas; la distinción vive sobre todo en storyboard y notas | Un docente que recibe solo el deck no sabe qué proyectar. Las marcas de profundización son pequeñas e inconsistentes y no equivalen a una ruta operativa. | Marcar de forma visible `Central`, `Ampliación` y `Respaldo`; crear índice por encuentro y, preferentemente, una versión de aula con la ruta central ya seleccionada. | open |
| IPR-03 | major | imprescindible | U05-018–051 ocupa 34 slides antes del bloque señal/sistema y de la aplicación vocal sostenida | La formalización de Fourier y del análisis digital domina el primer tramo. Para primer año, la motivación profesional llega tarde y la secuencia corre el riesgo de sentirse como matemática sin problema concreto. | Adelantar un caso de voz o dispositivo después de U05-017 y usarlo como hilo conductor. Introducir cada herramienta porque resuelve una pregunta del caso. | open |
| IPR-04 | major | imprescindible | U05-022, 023, 027, 028; U05-133–136 | La serie completa, las integrales de coeficientes, la forma compleja y la DFT formal exceden lo necesario para la primera comprensión. Aunque algunas slides se declaran complementarias en las notas, el deck no lo hace evidente. | Conservar en la ruta central la idea “promedio + componentes en múltiplos de `f₀`” y una síntesis gráfica. Trasladar integrales, convención compleja y suma DFT al respaldo. Si se enseñan, separar estructura, símbolos e interpretación en slides distintas. | open |
| IPR-05 | major | imprescindible | U05-023 | La ecuación integra de `0` a `T₀`, pero el panel define `t₀` como “inicio elegido”. El símbolo definido no aparece en la expresión. Esto convierte una slide ya difícil en una inconsistencia conceptual. | Usar límites `t₀` a `t₀+T₀` y definir `t₀`, o conservar `0` a `T₀` y eliminar `t₀`. | open |
| IPR-06 | major | imprescindible | U05-032 figura como complementaria; U05-033–040 dependen de `fₛ`, `N`, `Tobs`, bins y `Δf` | El prerrequisito visual de muestreo puede omitirse mientras sus fórmulas quedan en la ruta central. La clasificación central/complementaria es internamente incoherente. | Hacer central una única explicación visual de muestreo y aliasing antes de usar `N/fₛ`; luego introducir duración y separación entre bins. | open |
| IPR-07 | major | imprescindible | U05-042, 047 y 048; capítulo PDF, figura 5.3 | Se explica la ventana con tres cajas nominales, no mostrando `x(t)`, `w(t)` y su producto. La notación renderizada `xw(t)` puede leerse como producto o como nombre de señal. U05-047 describe un espectrograma sin mostrarlo y U05-048 habla de voz sin un registro visible. | Usar gráficos alineados de señal, ventana y señal ventaneada; escribir `x_w(t)`. Incorporar la figura 5.3 del capítulo o una reproducción propia equivalente y después un espectrograma vocal anotado. Si no hay registro aprobado, dejar la aplicación vocal fuera de la ruta central. | open |
| IPR-08 | major | imprescindible | Nota U05-048: “usar alternativa conceptual hasta aprobar registro”; render U05-048 con texto desbordado | Las notas reconocen que la aplicación no está terminada. Proyectarla como si fuera una aplicación resuelta produce una promesa pedagógica incumplida y dificulta leer la conclusión. | Reemplazarla por un registro aprobado con parámetros y consignas descriptivas, o marcarla explícitamente como pendiente y no proyectable. | open |
| IPR-09 | major | recomendado | U05-052–061 | `X(f)`, `H(f)`, `Y(f)`, magnitud, ganancia y fase aparecen antes de que el estudiante vea un dispositivo con datos concretos. La aplicación al audífono llega después del formalismo. | Comenzar con una entrada, una salida y una curva de un dispositivo concreto; preguntar qué cambió. Nombrar `H(f)` después. Llevar fase y retardo al tramo complementario si el grupo no lo necesita. | open |
| IPR-10 | major | recomendado | U05-063–073 | El bloque de componentes es relevante, pero llega después de más de 60 slides y repite la misma familia de espectros para distinguir fundamental, armónicos, parciales, sobretonos, fundamental ausente y formantes. | Adelantar la voz como motivación y condensar el bloque en una comparación principal, una actividad y una aplicación vocal. Mantener la fundamental ausente como ampliación demostrada, no solo afirmada. | open |
| IPR-11 | major | imprescindible | U05-085–093; U05-092 | Se encadenan suma por banda, razón de octava, armónicos versus octavas, centro geométrico, límites, ancho, tercios y un cálculo. U05-092 anuncia un tercio de octava en 1000 Hz, pero muestra “fórmulas de U05-089” y una corrección textual sin el cálculo numérico. La revisión anterior declaró este ejemplo resuelto, lo que no coincide con el render. | Enseñar primero la razón 2:1 con un ejemplo concreto; luego centro y límites; por último un único cálculo completo. Completar U05-092 con `f_L`, `f_H` y `B`, o eliminarla. Pasar valores nominales y normalización a respaldo. | open |
| IPR-12 | minor | recomendado | U05-095–105 | Los cuatro tipos de filtro se explican varias veces mediante curvas muy similares. La aplicación a habla, voz o audífono no muestra una comparación antes/después. | Reducir repeticiones y usar un solo problema aplicado: espectro de entrada, respuesta del filtro y espectro de salida, con pregunta de interpretación. | open |
| IPR-13 | major | recomendado | U05-106–116 | El bloque de ponderaciones ocupa 11 slides. Las cautelas son valiosas, pero la cantidad relativa es alta respecto del programa y repite distinciones ya formuladas en texto. | Condensar en seis o siete slides: propósito, A/C/Z cualitativas, ejemplo tonal, caso de banda ancha, descriptores no intercambiables y recapitulación. Mantener tolerancias y expresiones nominales en respaldo. | open |
| IPR-14 | major | imprescindible | U05-120 antes de U05-121 | La definición integral de nivel equivalente aparece antes del ejemplo que da intuición energética. Las notas dicen “presentar nivel constante equivalente antes de integral”, pero la slide visible comienza por la integral. | Invertir el orden: predicción con 70 y 80 dB, resolución energética, definición verbal y recién después formalización integral opcional. | open |
| IPR-15 | major | imprescindible | U05-126, 127 y 149 | El “caso integrador” no contiene valores numéricos ni un registro/gráfico que pueda analizarse. U05-127 remite a slides anteriores; U05-149, llamada “solución completa”, vuelve a mostrar un procedimiento sin resultados. El caso no es autosuficiente ni resoluble por quien recibe el material. | Construir una consigna completa con tabla o gráficos, datos suficientes y datos deliberadamente faltantes. Dar una solución paso a paso con cálculos, unidades, interpretación y límite de inferencia. | open |
| IPR-16 | major | imprescindible | `speaker_notes.md` se identifica como v01; deck v02; U05-048 y U05-149 | Las notas son pedagógicamente útiles, pero no están sincronizadas con el estado real del deck. En algunos casos describen una pieza aún no aprobada o una solución que la slide no contiene. | Actualizar las notas a v02 y validar, slide por slide, que consigna, respuesta esperada, visual y transición sean compatibles. | open |
| IPR-17 | minor | recomendado | Recapitulaciones U05-017, 029, 040, 051, 062, 073, 083, 094, 105, 116 y 124 | Las notas proponen buenas preguntas de recuperación, pero las slides visibles se parecen a inventarios o listas. Sin las notas, la actividad no siempre es evidente. | Mostrar en cada recapitulación una consigna, tiempo, modo de respuesta y evidencia esperada. Reutilizar un mismo caso con datos nuevos para favorecer integración, no solo recuerdo. | open |
| IPR-18 | major | recomendado | Vocabulario distribuido; glosario U05-150 | “ordenada”, “normalización”, “convención”, “estimador”, “bin”, “lóbulo lateral”, “respuesta nominal”, “descriptor”, “integración energética” y otros términos se acumulan antes del glosario final. | Introducir primero una expresión cotidiana y luego el término técnico; mantener un glosario progresivo por bloque. No depender de U05-150, que está en respaldo y es demasiado tardía. | open |
| IPR-19 | minor | recomendado | U05-048, 061, 071, 080, 118 y 123 | Las aplicaciones son prudentes, pero varias son conceptuales, hipotéticas o ilustrativas. Falta al menos una experiencia auténtica completa con voz, audífono o medición. | Incluir un registro vocal autorizado o sintético claramente declarado, una curva real de dispositivo con fuente, o una medición didáctica documentada. Pedir primero una decisión profesional limitada y después el cálculo. | open |
| IPR-20 | minor | recomendado | Gran cantidad de layouts “ecuación + qué significa + cómo se usa” y tarjetas de recapitulación | La consistencia ayuda, pero la repetición visual reduce la señal de jerarquía: una definición, un ejemplo, un error frecuente y una conclusión se perciben como igualmente importantes. | Reservar el layout de fórmula para relaciones centrales; usar más secuencias de antes/después, comparación de gráficos, predicción y resolución. | open |
| IPR-21 | minor | recomendado | U05-032, 037, 048, 092, 121 y 149 en el render | Hay rótulos cortados, fórmulas mal distribuidas, texto fuera de su panel o contenido que parece placeholder. Aunque sean problemas visuales, interrumpen la explicación y elevan la carga extrínseca. | Corregir estos renders antes de usar las actividades en clase y revalidarlos a tamaño de proyección. | open |

## 5. Exactitud conceptual y correspondencia con las fuentes

### Cobertura del programa

No se detectaron omisiones sustantivas del programa oficial. El deck incluso amplía el alcance con DFT, FFT, bins, resolución, ventanas, fuga y espectrograma. Estas ampliaciones están respaldadas por el capítulo, pero no todas deben ocupar la ruta central.

### Correspondencia con el capítulo

La estructura del deck sigue de cerca el capítulo. Sin embargo, en varios lugares convierte material de consulta o profundización en contenido proyectado sin conservar el soporte visual del libro. El caso más claro es el compromiso tiempo–frecuencia: el capítulo lo muestra mediante dos espectrogramas comparables, mientras que el deck lo sustituye por un diagrama de proceso y texto.

También se desaprovechan ejercicios de lectura del capítulo que ya están bien formulados. Las tareas C2–C6 y L1–L5 del libro podrían reemplazar varias slides declarativas y reducir la necesidad de crear recapitulaciones nuevas.

### Errores o ambigüedades conceptuales

- **U05-023:** límites de integración y definición de `t₀` incompatibles.
- **U05-042:** `xw(t)` no distingue con claridad el nombre de la señal ventaneada del producto; conviene `x_w(t)`.
- **U05-033:** `Tobs=N/fₛ` coincide con la convención del libro para la longitud del registro. Conviene nombrarla “duración del registro de análisis” y no el intervalo entre la primera y la última marca temporal, para evitar una discusión innecesaria sobre `(N-1)/fₛ`.
- **U05-067–071:** la fundamental ausente y el pitch están tratados con cautela, pero son conceptualmente avanzados. Deben demostrarse con señal temporal o audio y mantener explícito el límite hacia psicoacústica.
- **U05-092 y U05-149:** no contienen el cálculo o la solución que anuncian. El problema es de completitud pedagógica, no de validez de una fórmula concreta.

No se identificaron otros errores físicos graves en las fórmulas centrales revisadas. El mayor riesgo actual es que la densidad y el orden hagan que una formulación correcta se aprenda sin interpretación.

## 6. Propuesta de secuencia revisada

La propuesta no elimina el material existente: cambia su jerarquía y el orden de acceso.

### Encuentro 1 — Qué representa cada gráfico

- problema inicial de igual RMS y señales distintas;
- dominio temporal, espectro de magnitud y fase;
- rutina de lectura;
- Fourier como cambio de descripción, sin integrales;
- mini aplicación vocal que dé sentido a la pregunta.

### Encuentro 2 — Periodicidad y componentes de la voz

- período y `f₀`;
- construcción con senoides;
- fundamental, armónicos, parciales y sobretonos;
- fuente, tracto vocal, envolvente y formantes;
- actividad de clasificación y recapitulación.

### Encuentro 3 — Del registro a un espectro calculado

- transducción y muestreo;
- `fₛ`, `N`, duración y bins;
- resolución como capacidad de separar componentes;
- ventana y fuga mediante gráficos;
- espectrograma real como aplicación. DFT formal, FFT, normalización y detalles de ventana quedan como ampliación.

### Encuentro 4 — Señal, sistema y filtros

- caso concreto de entrada/salida de un dispositivo;
- espectro versus respuesta en frecuencia;
- magnitud, ganancia y, si resulta necesario, fase;
- filtros, límites, centro y ancho;
- comparación antes/después.

### Encuentro 5 — Rangos, octavas y bandas

- límites convencionales y condiciones;
- rango dinámico vocal, instrumental y auditivo;
- octava como razón 2:1;
- bandas, centro geométrico y un único ejemplo numérico completo;
- lectura de niveles por banda.

### Encuentro 6 — Ponderación, sonometría y decisión

- A, C y Z según propósito;
- ejemplo tonal y límite para banda ancha;
- cadena del sonómetro;
- intuición energética antes de `L_eq`;
- caso integrador autosuficiente;
- recapitulación final y puente hacia percepción auditiva.

## 7. Propuesta priorizada de cambios

### Imprescindibles

1. Definir y hacer visible una ruta central más corta; no usar las 150 slides como secuencia por defecto.
2. Reorganizar la unidad en seis encuentros o dos submódulos y adelantar una aplicación vocal concreta.
3. Relegar integrales de Fourier, convención compleja, DFT formal y detalles de ventanas al material complementario o de respaldo.
4. Hacer central la intuición de muestreo antes de `N`, `fₛ`, `Tobs` y `Δf`.
5. Corregir la inconsistencia de U05-023 y la notación de U05-042.
6. Incorporar un espectrograma real o sintético bien documentado; no dejar U05-047/048 como explicación sin objeto visible.
7. Completar U05-092 con un cálculo verificable.
8. Invertir U05-120/121 para presentar intuición y ejemplo antes de la integral de nivel equivalente.
9. Rehacer U05-126/127/149 como un caso integrador autosuficiente y resoluble.
10. Sincronizar `speaker_notes.md` con la v02 y retirar instrucciones o alternativas todavía pendientes.
11. Corregir los renders que impiden leer consignas, fórmulas o conclusiones antes de proyectar el material.

### Recomendados

1. Adelantar y condensar el bloque de voz y componentes.
2. Reducir la extensión relativa de bandas, filtros y ponderaciones sin perder los errores frecuentes esenciales.
3. Convertir las recapitulaciones visibles en tareas explícitas de recuperación y decisión.
4. Usar un glosario progresivo y lenguaje cotidiano antes del término técnico.
5. Reemplazar repeticiones de tarjetas por comparaciones, predicciones y visuales antes/después.
6. Incorporar una aplicación auténtica con datos y condiciones declaradas.
7. Reutilizar ejercicios de interpretación ya presentes en el capítulo, en especial los de lectura de gráficos.
8. Mantener el caso profesional como hilo conductor en varios encuentros, en vez de reservar la integración para el final.

### Opcionales

1. Añadir demostraciones breves de audio: suma de armónicos, fundamental ausente y filtrado.
2. Animar de forma progresiva la síntesis de Fourier y la formación de un espectrograma.
3. Preparar una hoja de trabajo con la rutina “objeto–ejes–unidades–condiciones–conclusión”.
4. Crear una versión docente con notas de tiempo, cortes sugeridos y rutas alternativas según duración de clase.
5. Convertir las ecuaciones de respaldo a objetos matemáticos nativos de Office para mejorar lectura y edición.

## 8. Criterio para una segunda revisión

La unidad debería volver a revisarse pedagógicamente cuando exista una ruta central visible y se hayan resuelto U05-023, 042, 047/048, 092, 120/121 y 126/127/149. La segunda pasada debe comprobar, con el render final y las notas actualizadas, que:

- cada encuentro tenga un propósito dominante;
- ninguna fórmula aparezca antes de la intuición o del problema que resuelve;
- las aplicaciones incluyan datos, visuales y condiciones suficientes;
- las recapitulaciones exijan recuperación o decisión;
- un docente nuevo pueda impartir la ruta sin consultar el storyboard para saber qué omitir.

---

## 9. Segunda revisión independiente sobre la versión final

La segunda pasada se realizó después de aplicar la propuesta priorizada y revisar el render final.

### Imprescindibles

| cambio | estado | evidencia |
|---|---|---|
| Ruta central más corta y visible | resuelto | 77 CENTRAL, 55 AMPLIACIÓN, 18 RESPALDO; seis encuentros. |
| Formalismo secundario fuera de la secuencia obligatoria | resuelto | U05-023 y formalismos de B13 no son centrales. |
| Muestreo antes de fórmulas dependientes | resuelto | U05-032 es central antes de U05-033/036. |
| U05-023 y U05-042 | resuelto | Intervalo coherente y señal ventaneada sin símbolo ambiguo. |
| Espectrograma visible y documentado | resuelto | U05-048 usa la figura sintética del libro y consigna descriptiva. |
| U05-092 completo | resuelto | Límites y ancho numéricos visibles. |
| Intuición de `L_eq` antes de integral | resuelto | U05-120/121 centrales; U05-146 respaldo. |
| Caso integrador autosuficiente | resuelto | U05-126/127/149 con datos, unidades y resultados. |
| Notas sincronizadas | resuelto | `speaker_notes.md` final y 150/150 notas con fuentes. |
| Renders ilegibles o desbordados | resuelto | Render total, revisión ampliada y prueba sin desbordes. |

### Recomendados

| cambio | estado | decisión |
|---|---|---|
| Adelantar una aplicación concreta | resuelto | U05-048 entra en la ruta central; el caso profesional completo permanece al cierre. |
| Reducir filtros y ponderaciones | resuelto | La ruta central selecciona el núcleo y deja repeticiones en ampliación. |
| Recapitulaciones activas | aceptado | Las notas contienen preguntas; puede profundizarse con actividades de aula. |
| Glosario progresivo | aceptado | Vocabulario introducido por bloques y glosario final de respaldo. |
| Aplicación auténtica con datos | resuelto | Caso integrador reproducible con señal y dispositivo. |
| Caso como hilo conductor | parcial aceptado | Se anticipan voz, audífono y espectrograma; el caso completo se reserva para integrar. |

### Opcionales

- Audio, animación progresiva, hoja de trabajo y OMML quedan como mejoras futuras.
- No son condiciones para declarar terminada la unidad porque existen alternativas estáticas completas.

### Dictamen pedagógico final

Un segundo docente puede distinguir qué proyectar sin consultar documentos externos: la ruta está rotulada en cada slide. La secuencia central introduce intuición antes del formalismo, contiene aplicaciones intermedias, recapitulaciones y un caso resoluble. No quedan problemas pedagógicos críticos ni mayores abiertos.
