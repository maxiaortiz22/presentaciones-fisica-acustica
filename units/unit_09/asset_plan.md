# Unidad 9 — Plan integral de recursos visuales y multimedia

Versión de planificación · 2026-08-12

## Decisión general

El storyboard aprobado es la autoridad slide por slide. Cada recurso se clasifica antes de producirse como `chart`, `diagram`, `mixed`, `external_image`, `video_or_gif` o `equation_only`. `none` se conserva únicamente como decisión negativa explícita cuando la slide funciona con tabla, tipografía o espacio de trabajo y no necesita imagen.

Prioridad aplicada:

1. gráficos propios reproducibles;
2. diagramas, tablas y ecuaciones editables;
3. fotografías técnicas reales con licencia;
4. animaciones/audio propios con alternativa estática;
5. recursos externos solo si superan al visual propio;
6. ninguna imagen generada con IA: no existe una ventaja pedagógica que compense el riesgo de errores geométricos o constructivos en U9.

## Enrutamiento por skill

| clase | responsable | producto |
|---|---|---|
| `chart` | `chart-generation` | script, datos/modelo, SVG y PNG |
| `diagram` | `diagram-generation` | formas/conectores/tabla/ecuación editables; SVG/PNG de respaldo |
| `equation_only` | `diagram-generation` | OMML y callouts editables |
| `mixed` | coordinación de skills | capas separadas; nunca slide aplanada |
| `external_image` | `asset-curation` | original, recorte derivado, crédito, alt text y callouts |
| `video_or_gif` | `asset-curation` + producción propia | MP4/GIF/audio local, captura estática y parámetros |
| `none` | composición nativa | decisión explícita de no agregar imagen |

## Decisión por modalidad solicitada

| modalidad | decisión para U9 |
|---|---|
| Fotografía real | Solo opcional en U09-020, U09-066 y U09-076 para mostrar montaje, envolvente o cabina real; nunca como prueba de desempeño. |
| Ilustración técnica | Sí, pero reconstruida como esquema científico editable en los bloques de atmósfera, interfaces, barreras, recintos y cabina. |
| Imagen anatómica | No corresponde al alcance de U9. |
| Gráfico propio | Sí: 11 recursos U09-CH-001–011; dos permanecen bloqueados por fuente. |
| Diagrama editable | Sí: 70 recursos U09-DG-001–070; es la modalidad dominante. |
| Tabla | Sí, como tabla nativa para matrices, checklist, notación y eventual información normativa; nunca como captura. |
| Animación | Cuatro propuestas propias y opcionales; la información completa existe también en estado estático. |
| GIF | Solo fallback silencioso de animaciones breves si conserva texto ≥20 pt; MP4 es preferido. |
| Video | No se selecciona video externo; las animaciones propias pueden exportarse como MP4. |
| Audio | Solo U09-MEDIA-001, habla seca/reverberada propia y no calibrada. |
| Captura de instrumento | No se usa una captura real; U09-075 tendrá una interfaz ficticia para no validar aplicaciones telefónicas. |
| Ecuación anotada | Sí, mediante OMML y callouts editables; ninguna ecuación queda como captura. |
| Ninguna imagen | U09-086, U09-093, U09-094 y U09-096 se resuelven con tabla, tipografía o actividad y no reciben decoración. |

## Decisión slide por slide

| slide_id | título de trabajo | visual_class | modalidad elegida | recurso/alternativa | skill | layout | decisión |
|---|---|---|---|---|---|---|---|
| U09-001 | Factores que afectan la propagación del sonido | diagram | diagrama editable | Ilustración técnica sintética de fuente, trayecto urbano y clínica; U09-DG-001, candidata para `diagram-generation`. | `diagram-generation` | FA_00_PORTADA | Primera prioridad; producir como recurso propio editable. |
| U09-002 | La clínica junto a la avenida | diagram | diagrama editable | Mapa del caso con rutas numeradas; U09-DG-002, candidata para `diagram-generation`. | `diagram-generation` | FA_13_APLICACION_CLINICA | Primera prioridad; producir como recurso propio editable. |
| U09-003 | Qué podremos explicar y estimar | diagram | diagrama editable | Ruta de objetivos en dos niveles; sin iconos decorativos. | `diagram-generation` | FA_02_OBJETIVOS | Primera prioridad; producir como recurso propio editable. |
| U09-004 | Qué necesitamos recuperar | diagram | diagrama editable | Tarjetas de prerrequisitos y pregunta breve. | `diagram-generation` | FA_02B_CONOCIMIENTOS_PREVIOS | Primera prioridad; producir como recurso propio editable. |
| U09-005 | De la emisión a la verificación | diagram | diagrama editable | Mapa horizontal con hitos y pausas; U09-DG-003, candidata para `diagram-generation`. | `diagram-generation` | FA_03_MAPA_CLASE | Primera prioridad; producir como recurso propio editable. |
| U09-006 | ¿De quién es el nivel recibido? | diagram | diagrama editable | Fondo de divisor con esquema mínimo de tres etapas. | `diagram-generation` | FA_01_DIVISOR | Primera prioridad; producir como recurso propio editable. |
| U09-007 | Fuente–trayecto–receptor | diagram | diagrama editable | Diagrama principal con zonas y ejemplos; U09-DG-004, candidata para `diagram-generation`. | `diagram-generation` | FA_12_PROCESO | Primera prioridad; producir como recurso propio editable. |
| U09-008 | Emitir no es recibir | mixed | diagrama editable + apoyo cuantitativo | Tabla comparativa y mini cadena; U09-DG-005, candidata para `diagram-generation`. | `diagram-generation` | FA_11_COMPARACION | Primera prioridad; producir como recurso propio editable. |
| U09-009 | Ocho mecanismos, cuatro preguntas | diagram | tabla nativa o matriz editable | Matriz mecanismo–magnitud–dependencia–modelo; U09-DG-006, candidata para `diagram-generation`. | `diagram-generation` | FA_18_TABLA_DATOS | Primera prioridad; producir como recurso propio editable. |
| U09-010 | ¿Fuente, trayecto o medición? | diagram | diagrama editable | Tarjetas arrastrables o revelado; U09-DG-007, candidata para `diagram-generation`. | `diagram-generation` | FA_14_PREGUNTA_EJERCICIO | Primera prioridad; producir como recurso propio editable. |
| U09-011 | Antes de una fórmula: cuatro preguntas | diagram | diagrama editable | Cuatro bloques conectados; U09-DG-008, candidata para `diagram-generation`. | `diagram-generation` | FA_16_RECAP_PARCIAL | Primera prioridad; producir como recurso propio editable. |
| U09-012 | ¿Qué explica el modelo ideal? | diagram | diagrama editable | Dos trayectos desde una misma fuente. | `diagram-generation` | FA_01_DIVISOR | Primera prioridad; producir como recurso propio editable. |
| U09-013 | La misma potencia ocupa más superficie | diagram | diagrama editable | Reconstrucción de figura U4; U09-DG-009, candidata para `diagram-generation`. | `diagram-generation` | FA_22_VISUAL_COMPLETO | Primera prioridad; producir como recurso propio editable. |
| U09-014 | Cambiar la distancia cambia `L_p` | mixed | gráfico propio + ecuación/diagrama anotado | Ecuación central U09-DG-010 y mini curva U09-CH-001; candidata para `diagram-generation`. | `chart-generation` + `diagram-generation` | FA_09_ECUACION_INTERPRETACION | Primera prioridad; producir como recurso propio editable. |
| U09-015 | De 0,50 m a 1,00 m | mixed | ecuación anotada + diagrama editable | Secuencia de cálculo; U09-DG-011, candidata para `diagram-generation`. | `diagram-generation` | FA_10_EJEMPLO_RESUELTO | Primera prioridad; producir como recurso propio editable. |
| U09-016 | “Duplicar distancia siempre resta 6 dB” | diagram | diagrama editable | Comparación ideal/real. | `diagram-generation` | FA_15_ERROR_FRECUENTE | Primera prioridad; producir como recurso propio editable. |
| U09-017 | Una fuente no emite igual en todas las direcciones | diagram | diagrama editable | Reconstrucción de figura U4; U09-DG-012, candidata para `diagram-generation`. | `diagram-generation` | FA_11_COMPARACION | Primera prioridad; producir como recurso propio editable. |
| U09-018 | El patrón cambia con la frecuencia | chart | gráfico propio | U09-CH-002 patrón polar por frecuencia. | `chart-generation` | FA_07_GRAFICO_EXPLICACION | Segunda prioridad; puede ocultarse sin romper la secuencia. |
| U09-019 | Del factor `Q_dir` al índice `DI` | mixed | ecuación anotada + diagrama editable | Ecuación con comparador omnidireccional; U09-DG-013, candidata para `diagram-generation`. | `diagram-generation` | FA_09_ECUACION_INTERPRETACION | Primera prioridad; producir como recurso propio editable. |
| U09-020 | Campo sonoro: geometría y orientación importan | mixed | fotografía real + callouts/diagrama editable | Foto técnica U09-IMG-001 con sobreimpresión geométrica o diagrama alternativo U09-DG-014. | `asset-curation` + `diagram-generation` | FA_13_APLICACION_CLINICA | Primera prioridad; producir como recurso propio editable. |
| U09-021 | ¿Distancia, dirección o ambos? | diagram | diagrama editable | Tarjetas de decisión; U09-DG-015, candidata para `diagram-generation`. | `diagram-generation` | FA_16_RECAP_PARCIAL | Primera prioridad; producir como recurso propio editable. |
| U09-022 | ¿Aire uniforme o aire con gradiente? | diagram | diagrama editable | Perfil uniforme frente a perfil vertical. | `diagram-generation` | FA_01_DIVISOR | Primera prioridad; producir como recurso propio editable. |
| U09-023 | La rapidez aumenta con la temperatura | mixed | gráfico propio + ecuación/diagrama anotado | U09-CH-003 rapidez frente a temperatura; ecuación anotada U09-DG-016. | `chart-generation` + `diagram-generation` | FA_07_GRAFICO_EXPLICACION | Primera prioridad; producir como recurso propio editable. |
| U09-024 | Temperatura, `c` y `λ`: no confundir | mixed | ecuación anotada + diagrama editable | Dos estados y ecuación `λ=c/f`; U09-DG-017, candidata para `diagram-generation`. | `diagram-generation` | FA_10_EJEMPLO_RESUELTO | Primera prioridad; producir como recurso propio editable. |
| U09-025 | Gradientes térmicos: la trayectoria puede curvarse | diagram | diagrama editable | U09-DG-018, candidata para `diagram-generation`, reconstrucción de figura 9.1. | `diagram-generation` | FA_22_VISUAL_COMPLETO | Primera prioridad; producir como recurso propio editable. |
| U09-026 | Viento uniforme: cambia la rapidez efectiva | mixed | ecuación anotada + diagrama editable | Ecuación con brújula angular; U09-DG-019, candidata para `diagram-generation`. | `diagram-generation` | FA_09_ECUACION_INTERPRETACION | Primera prioridad; producir como recurso propio editable. |
| U09-027 | Gradiente de viento: aparece curvatura | diagram | diagrama editable | U09-DG-020, candidata para `diagram-generation`, reconstrucción de figura 9.2. | `diagram-generation` | FA_11_COMPARACION | Primera prioridad; producir como recurso propio editable. |
| U09-028 | Presión y densidad cambian juntas | mixed | ecuación anotada + diagrama editable | Balanza conceptual de variables; U09-DG-021, candidata para `diagram-generation`. | `diagram-generation` | FA_09_ECUACION_INTERPRETACION | Primera prioridad; producir como recurso propio editable. |
| U09-029 | Altitud y humedad: no hay una resta universal | diagram | diagrama editable | U09-DG-022, candidata para `diagram-generation`. | `diagram-generation` | FA_05_TEXTO_VISUAL_60_40 | Segunda prioridad; puede ocultarse sin romper la secuencia. |
| U09-030 | Absorción atmosférica no es divergencia | mixed | ecuación anotada + diagrama editable | Ecuación estructural y comparación; U09-DG-023, candidata para `diagram-generation`. | `diagram-generation` | FA_11_COMPARACION | Primera prioridad; producir como recurso propio editable. |
| U09-031 | Turbulencia: variabilidad, no corrección fija | diagram | diagrama editable | U09-DG-024, candidata para `diagram-generation`. | `diagram-generation` | FA_06_VISUAL_TEXTO_40_60 | Segunda prioridad; puede ocultarse sin romper la secuencia. |
| U09-032 | Qué registrar antes de comparar mediciones exteriores | diagram | diagrama editable | Ficha de campo editable; U09-DG-025, candidata para `diagram-generation`. | `diagram-generation` | FA_13_APLICACION_CLINICA | Primera prioridad; producir como recurso propio editable. |
| U09-033 | Cuatro efectos, cuatro respuestas | diagram | diagrama editable | U09-DG-026, candidata para `diagram-generation`. | `diagram-generation` | FA_16_RECAP_PARCIAL | Primera prioridad; producir como recurso propio editable. |
| U09-034 | ¿Adónde va la energía incidente? | diagram | diagrama editable | Haz incidente que llega a una interfaz. | `diagram-generation` | FA_01_DIVISOR | Primera prioridad; producir como recurso propio editable. |
| U09-035 | Tres destinos simultáneos | diagram | diagrama editable | U09-DG-027, candidata para `diagram-generation`, reconstrucción de figura 9.3. | `diagram-generation` | FA_22_VISUAL_COMPLETO | Primera prioridad; producir como recurso propio editable. |
| U09-036 | El balance debe cerrar | mixed | ecuación anotada + diagrama editable | U09-DG-028, candidata para `diagram-generation`. | `diagram-generation` | FA_09_ECUACION_INTERPRETACION | Primera prioridad; producir como recurso propio editable. |
| U09-037 | ¿Qué fracción falta? | mixed | ecuación anotada + diagrama editable | Tarjeta de cálculo y diagrama reducido. | `diagram-generation` | FA_14B_MINI_EJERCICIO | Primera prioridad; producir como recurso propio editable. |
| U09-038 | Reflexión: cambia la dirección, no la identidad del mecanismo | diagram | diagrama editable | U09-DG-029, candidata para `diagram-generation`. | `diagram-generation` | FA_08_DEFINICION | Primera prioridad; producir como recurso propio editable. |
| U09-039 | Reflexión, eco y reverberación no son sinónimos | mixed | gráfico propio + ecuación/diagrama anotado | U09-CH-004 respuesta temporal conceptual, con anotaciones U09-DG-030. | `chart-generation` + `diagram-generation` | FA_11_COMPARACION | Primera prioridad; producir como recurso propio editable. |
| U09-040 | Refracción en una interfaz aire–sólido | diagram | diagrama editable | U09-DG-031, candidata para `diagram-generation`. | `diagram-generation` | FA_22_VISUAL_COMPLETO | Primera prioridad; producir como recurso propio editable. |
| U09-041 | Snell acústica: relación entre ángulos y rapidez | mixed | ecuación anotada + diagrama editable | Ecuación anotada U09-DG-032, candidata para `diagram-generation`. | `diagram-generation` | FA_09_ECUACION_INTERPRETACION | Segunda prioridad; puede ocultarse sin romper la secuencia. |
| U09-042 | Difracción: la onda alcanza la “sombra” | diagram | diagrama editable | U09-DG-033, candidata para `diagram-generation`. | `diagram-generation` | FA_08_DEFINICION | Primera prioridad; producir como recurso propio editable. |
| U09-043 | La escala de `λ` cambia con la frecuencia | chart | gráfico propio | U09-CH-005 longitud de onda frente a frecuencia. | `chart-generation` | FA_07_GRAFICO_EXPLICACION | Primera prioridad; producir como recurso propio editable. |
| U09-044 | La misma barrera, tres frecuencias | diagram | diagrama editable | U09-DG-034, candidata para `diagram-generation`. | `diagram-generation` | FA_11_COMPARACION | Primera prioridad; producir como recurso propio editable. |
| U09-045 | ¿Difracción o transmisión? | diagram | diagrama editable | U09-DG-035, candidata para `diagram-generation`. | `diagram-generation` | FA_15_ERROR_FRECUENTE | Primera prioridad; producir como recurso propio editable. |
| U09-046 | ¿Qué ocurrió en la interfaz? | diagram | diagrama editable | U09-DG-036, candidata para `diagram-generation`. | `diagram-generation` | FA_16_RECAP_PARCIAL | Primera prioridad; producir como recurso propio editable. |
| U09-047 | ¿Cómo persiste el sonido en una sala? | diagram | diagrama editable | Sala con ruta directa y primeras reflexiones. | `diagram-generation` | FA_01_DIVISOR | Primera prioridad; producir como recurso propio editable. |
| U09-048 | De la llegada directa a la cola reverberante | diagram | diagrama editable | U09-DG-037, candidata para `diagram-generation`. | `diagram-generation` | FA_12_PROCESO | Primera prioridad; producir como recurso propio editable. |
| U09-049 | `T_60`: describir un decaimiento | chart | gráfico propio | U09-CH-006 decaimiento sonoro anotado. | `chart-generation` | FA_07_GRAFICO_EXPLICACION | Primera prioridad; producir como recurso propio editable. |
| U09-050 | Área equivalente de absorción | mixed | diagrama editable + apoyo cuantitativo | U09-DG-038, candidata para `diagram-generation`. | `diagram-generation` | FA_08_DEFINICION | Primera prioridad; producir como recurso propio editable. |
| U09-051 | Sabine: volumen frente a absorción | mixed | ecuación anotada + diagrama editable | U09-DG-039, candidata para `diagram-generation`. | `diagram-generation` | FA_09_ECUACION_INTERPRETACION | Primera prioridad; producir como recurso propio editable. |
| U09-052 | Un aula de 8 × 6 × 3 m | mixed | ecuación anotada + diagrama editable | Secuencia de cálculo U09-DG-040, candidata para `diagram-generation`. | `diagram-generation` | FA_10_EJEMPLO_RESUELTO | Primera prioridad; producir como recurso propio editable. |
| U09-053 | Igual `A_eq`, distinto campo local | diagram | diagrama editable | U09-DG-041, candidata para `diagram-generation`. | `diagram-generation` | FA_11_COMPARACION | Segunda prioridad; puede ocultarse sin romper la secuencia. |
| U09-054 | “Un `T_60` corto significa buen aislamiento” | diagram | diagrama editable | U09-DG-042, candidata para `diagram-generation`. | `diagram-generation` | FA_15_ERROR_FRECUENTE | Primera prioridad; producir como recurso propio editable. |
| U09-055 | Seco y reverberado: escuchar y ver | video_or_gif | audio + animación/gráfico | U09-MEDIA-001 y U09-CH-006. | `asset-curation` + producción propia | FA_19_MEDIA_AUDIO_VIDEO | Opcional, local y con captura estática autosuficiente. |
| U09-056 | Recinto: llegada, decaimiento y límite | diagram | diagrama editable | U09-DG-043, candidata para `diagram-generation`. | `diagram-generation` | FA_16_RECAP_PARCIAL | Primera prioridad; producir como recurso propio editable. |
| U09-057 | ¿Qué limita el paso entre espacios? | diagram | diagrama editable | Corte simple de dos recintos. | `diagram-generation` | FA_01_DIVISOR | Primera prioridad; producir como recurso propio editable. |
| U09-058 | De `τ_E` al índice `R` | mixed | ecuación anotada + diagrama editable | U09-DG-044, candidata para `diagram-generation`. | `diagram-generation` | FA_09_ECUACION_INTERPRETACION | Primera prioridad; producir como recurso propio editable. |
| U09-059 | Una escala lineal se vuelve logarítmica | chart | gráfico propio | U09-CH-007 transmisión frente a índice. | `chart-generation` | FA_07_GRAFICO_EXPLICACION | Primera prioridad; producir como recurso propio editable. |
| U09-060 | El sonido encuentra más de un camino | diagram | diagrama editable | U09-DG-045, candidata para `diagram-generation`. | `diagram-generation` | FA_22_VISUAL_COMPLETO | Primera prioridad; producir como recurso propio editable. |
| U09-061 | Acondicionar, aislar e insonorizar | diagram | diagrama editable | U09-DG-046, candidata para `diagram-generation`. | `diagram-generation` | FA_11_COMPARACION | Primera prioridad; producir como recurso propio editable. |
| U09-062 | Masa superficial: masa por unidad de área | mixed | diagrama editable + apoyo cuantitativo | U09-DG-047, candidata para `diagram-generation`. | `diagram-generation` | FA_08_DEFINICION | Primera prioridad; producir como recurso propio editable. |
| U09-063 | Ley de masas: una tendencia ideal | mixed | ecuación anotada + diagrama editable | U09-DG-048, candidata para `diagram-generation`. | `diagram-generation` | FA_09_ECUACION_INTERPRETACION | Primera prioridad; producir como recurso propio editable. |
| U09-064 | ¿Qué cambia al duplicar masa o frecuencia? | mixed | ecuación anotada + diagrama editable | Secuencia de cálculo U09-DG-049, candidata para `diagram-generation`. | `diagram-generation` | FA_14B_MINI_EJERCICIO | Primera prioridad; producir como recurso propio editable. |
| U09-065 | Fuera de la recta ideal | chart | gráfico propio | U09-CH-008 ley de masas con regiones cualitativas. | `chart-generation` | FA_07_GRAFICO_EXPLICACION | Segunda prioridad; puede ocultarse sin romper la secuencia. |
| U09-066 | Una pared robusta con una puerta débil | mixed | fotografía real + callouts/diagrama editable | Imagen técnica U09-IMG-002 o diagrama U09-DG-050, candidata para `diagram-generation`. | `asset-curation` + `diagram-generation` | FA_13_APLICACION_CLINICA | Segunda prioridad; puede ocultarse sin romper la secuencia. |
| U09-067 | ¿Elemento, conjunto o ruta débil? | diagram | diagrama editable | U09-DG-051, candidata para `diagram-generation`. | `diagram-generation` | FA_16_RECAP_PARCIAL | Primera prioridad; producir como recurso propio editable. |
| U09-068 | ¿Qué debe cumplir una cabina para una prueba concreta? | diagram | diagrama editable | Silueta de cabina con tres capas. | `diagram-generation` | FA_01_DIVISOR | Primera prioridad; producir como recurso propio editable. |
| U09-069 | “Si tiene espuma, está insonorizada” | diagram | diagrama editable | U09-DG-052, candidata para `diagram-generation`. | `diagram-generation` | FA_15_ERROR_FRECUENTE | Primera prioridad; producir como recurso propio editable. |
| U09-070 | La cabina como conjunto | diagram | diagrama editable | U09-DG-053, candidata para `diagram-generation`, primera mitad de figura 9.6. | `diagram-generation` | FA_22_VISUAL_COMPLETO | Primera prioridad; producir como recurso propio editable. |
| U09-071 | Por dónde puede ingresar el ruido | diagram | diagrama editable | U09-DG-054, candidata para `diagram-generation`, segunda mitad de figura 9.6. | `diagram-generation` | FA_22_VISUAL_COMPLETO | Primera prioridad; producir como recurso propio editable. |
| U09-072 | Verificar una cabina es verificar un sistema | diagram | diagrama editable | U09-DG-055, candidata para `diagram-generation`. | `diagram-generation` | FA_12_PROCESO | Primera prioridad; producir como recurso propio editable. |
| U09-073 | dB(A) global frente a niveles por bandas | chart | gráfico propio | U09-CH-009 comparación conceptual global/bandas. | `chart-generation` | FA_11_COMPARACION | Primera prioridad; producir como recurso propio editable. |
| U09-074 | Un “máximo permitido” necesita contexto | diagram | diagrama editable | U09-DG-056, candidata para `diagram-generation`. | `diagram-generation` | FA_18_TABLA_DATOS | Primera prioridad; producir como recurso propio editable. |
| U09-075 | “La cabina tiene 28 dB(A)” | mixed | diagrama editable + apoyo cuantitativo | Captura ficticia no instrumental y matriz de faltantes; U09-DG-057, candidata para `diagram-generation`. | `diagram-generation` | FA_13_APLICACION_CLINICA | Primera prioridad; producir como recurso propio editable. |
| U09-076 | Inspección guiada de una cabina real | external_image | fotografía real con callouts | U09-IMG-003 y U09-IMG-004 con callouts; candidatos para `diagram-generation` por anotaciones. | `asset-curation` + `diagram-generation` | FA_06_VISUAL_TEXTO_40_60 | Usar solo si se aprueba licencia/encuadre; fallback propio obligatorio. |
| U09-077 | ¿Qué ruta limita la prueba? | diagram | diagrama editable | U09-DG-058, candidata para `diagram-generation`. | `diagram-generation` | FA_16_RECAP_PARCIAL | Primera prioridad; producir como recurso propio editable. |
| U09-078 | ¿Qué podemos estimar y qué debemos medir? | diagram | diagrama editable | Tres puertas de decisión. | `diagram-generation` | FA_01_DIVISOR | Primera prioridad; producir como recurso propio editable. |
| U09-079 | Caso final I: fuente y emisión | diagram | diagrama editable | Mapa del caso, capa fuente; U09-DG-059, candidata para `diagram-generation`. | `diagram-generation` | FA_13_APLICACION_CLINICA | Primera prioridad; producir como recurso propio editable. |
| U09-080 | Caso final II: rutas exteriores e interiores | diagram | diagrama editable | U09-DG-060, candidata para `diagram-generation`. | `diagram-generation` | FA_22_VISUAL_COMPLETO | Primera prioridad; producir como recurso propio editable. |
| U09-081 | Caso final III: receptor, cabina y medición | diagram | diagrama editable | U09-DG-061, candidata para `diagram-generation`. | `diagram-generation` | FA_13_APLICACION_CLINICA | Primera prioridad; producir como recurso propio editable. |
| U09-082 | Estimar, medir o consultar | diagram | tabla nativa o matriz editable | Matriz de trabajo U09-DG-062, candidata para `diagram-generation`. | `diagram-generation` | FA_14_PREGUNTA_EJERCICIO | Primera prioridad; producir como recurso propio editable. |
| U09-083 | Del fenómeno a la decisión responsable | diagram | diagrama editable | U09-DG-063, candidata para `diagram-generation`. | `diagram-generation` | FA_17_RECAP_FINAL | Primera prioridad; producir como recurso propio editable. |
| U09-084 | Del trayecto al control del ruido | diagram | diagrama editable | Diagrama de puente U09-DG-064, candidata para `diagram-generation`. | `diagram-generation` | FA_21_CIERRE_PUENTE | Primera prioridad; producir como recurso propio editable. |
| U09-085 | De potencia a −6 dB por duplicar distancia | mixed | diagrama editable + apoyo cuantitativo | U09-DG-065, candidata para `diagram-generation`. | `diagram-generation` | FA_23_APENDICE | Producir después de la ruta central y solo si resuelve una consulta real. |
| U09-086 | Símbolos que no deben confundirse | none | tabla nativa o texto estructurado | Tabla nativa. | composición nativa | FA_23_APENDICE | Decisión negativa: sin imagen decorativa. |
| U09-087 | Ejercicios de distancia y directividad | mixed | diagrama editable + apoyo cuantitativo | U09-DG-066, candidata para `diagram-generation`. | `diagram-generation` | FA_23_APENDICE | Producir después de la ruta central y solo si resuelve una consulta real. |
| U09-088 | Absorción atmosférica por bandas | chart | gráfico propio | U09-CH-010 pendiente de fuente primaria. | `chart-generation` | FA_23_APENDICE | Producir después de la ruta central y solo si resuelve una consulta real. |
| U09-089 | Refracción y conversión modal | diagram | diagrama editable | U09-DG-067, candidata para `diagram-generation`. | `diagram-generation` | FA_23_APENDICE | Producir después de la ruta central y solo si resuelve una consulta real. |
| U09-090 | Balance, `A_eq` y Sabine | mixed | diagrama editable + apoyo cuantitativo | U09-DG-068, candidata para `diagram-generation`. | `diagram-generation` | FA_23_APENDICE | Producir después de la ruta central y solo si resuelve una consulta real. |
| U09-091 | Límites de Sabine y modelos alternativos | diagram | tabla nativa o matriz editable | Tabla nativa; posible U09-DG-069, candidata para `diagram-generation`. | `diagram-generation` | FA_23_APENDICE | Producir después de la ruta central y solo si resuelve una consulta real. |
| U09-092 | Ruido máximo admisible para audiometría | chart | gráfico propio | U09-CH-011 bloqueado. | `chart-generation` | FA_23_APENDICE | No producir cifras; conservar estructura bloqueada. |
| U09-093 | Campo libre, sala y cabina | none | tabla nativa o texto estructurado | Tabla nativa. | composición nativa | FA_23_APENDICE | Decisión negativa: sin imagen decorativa. |
| U09-094 | Doce afirmaciones para discutir | none | ninguna imagen | Tarjetas de verdadero/falso justificado. | composición nativa | FA_23_APENDICE | Decisión negativa: sin imagen decorativa. |
| U09-095 | Clínica junto a la avenida: resolución orientativa | diagram | diagrama editable | U09-DG-070, candidata para `diagram-generation`. | `diagram-generation` | FA_23_APENDICE | Producir después de la ruta central y solo si resuelve una consulta real. |
| U09-096 | Fuentes para continuar | none | tabla nativa o texto estructurado | Lista bibliográfica y matriz de trazabilidad. | composición nativa | FA_20_BIBLIO_RECURSOS | Decisión negativa: sin imagen decorativa. |

## Shortlist externo y decisiones de curaduría

| asset_id | slide | título/autor/organización | URL | licencia conocida | propósito | evaluación | alternativa | estado |
|---|---|---|---|---|---|---|---|---|
| U09-IMG-001 | U09-020 | *Hearing acuity test in anechoic chamber 1949*; autor desconocido; anuncio AT&T recuperado por Wikimedia Commons | https://commons.wikimedia.org/wiki/File:Hearing_acuity_test_in_anechoic_chamber_1949.jpg | Dominio público en EE. UU. por publicación sin aviso; revisar aplicabilidad territorial | Mostrar un montaje real de altavoz, receptor y control de posición. | Exacta como evidencia histórica, pero no representa práctica clínica actual; 1020×820. | U09-DG-014 moderno y neutro. | proposed; no descargar salvo decisión docente |
| U09-IMG-002 | U09-066 | *Hearing Test Booth (39818427705)*; Ross Dunn; Wikimedia Commons/Flickr | https://commons.wikimedia.org/wiki/File:Hearing_Test_Booth_(39818427705).jpg | CC BY-SA 2.0 | Recorte opcional de puerta/envolvente para discutir ruta débil. | 3024×4032 y licencia clara; el encuadre debe verificarse antes de asegurar que muestra la junta requerida. | U09-DG-050. | shortlisted; descarga falló por HTTP 429 |
| U09-IMG-003 | U09-076 | *Hearing Test Booth (39818427705)*; Ross Dunn; Wikimedia Commons/Flickr | https://commons.wikimedia.org/wiki/File:Hearing_Test_Booth_(39818427705).jpg | CC BY-SA 2.0 | Inspección exterior de cabina; localizar puerta y envolvente sin inferir desempeño. | Alta resolución, recortable y reutilizable con atribución/ShareAlike. | U09-DG-053. | shortlisted; descarga falló por HTTP 429 |
| U09-IMG-004 | U09-076 | *Audiometro.jpg*; HMatos (FOB); Wikimedia Commons | https://commons.wikimedia.org/wiki/File:Audiometro.jpg | CC BY-SA 4.0 | Mostrar cabina con audiometro como contexto técnico real. | Relevante y licencia clara, pero resolución 486×538 insuficiente para visual dominante; solo inset pequeño. | U09-DG-053/054. | shortlisted, no descargado |
| U09-IMG-005 | U09-044, opcional | *Noise Barriers* / *Highway Traffic Noise Barriers at a Glance*; Federal Highway Administration | https://www.fhwa.dot.gov/environment/noise/noise_barriers/ | Obra de organismo federal; licencia específica de la fotografía debe verificarse | Dar escala real a una barrera sin usar la foto para inferir atenuación. | Fuente técnica confiable; imagen secundaria, no mejora el diagrama de tres frecuencias. | U09-DG-034. | proposed; no descargar hasta verificar imagen concreta |
| U09-IMG-006 | U09-032, opcional | No se selecciona recurso externo | — | — | Contextualizar un montaje de medición exterior. | La ficha propia comunica mejor variables y posiciones; una foto genérica distraería. | U09-DG-025. | replaced por diagrama propio |
| U09-REF-001 | U09-088 | ISO 9613-1:1993; International Organization for Standardization | https://www.iso.org/standard/17426.html | Copyright ISO; resumen público, texto completo restringido | Fuente de control para absorción atmosférica. | Confirma variables y rango general, no habilita reconstruir curvas. | Mantener U09-CH-010 bloqueado. | reference-only |
| U09-REF-002 | U09-092 | ISO 8253-1:2010; ISO | https://www.iso.org/standard/43601.html | Copyright ISO | Fuente candidata para requisitos de audiometría tonal por vía aérea/ósea. | Página oficial indica edición 2 y confirmación vigente; no contiene tabla reproducible. | Checklist U09-DG-056 sin cifras. | reference-only |
| U09-REF-003 | U09-020, U09-092 | ISO 8253-2:2009; ISO | https://www.iso.org/standard/51997.html | Copyright ISO | Requisitos de campo sonoro y procedimientos con altavoces. | Fuente oficial y vigente; texto completo no disponible en el repositorio. | Diagrama U09-DG-014 sin valores normativos. | reference-only |
| U09-REF-004 | U09-092 | ASA/ANSI S3.1-1999 (R2023); Acoustical Society of America / ANSI | https://webstore.ansi.org/standards/asa/asaansis31999r2023 | Copyright ASA/ANSI | Norma candidata para MPANL de salas audiométricas. | Resumen oficial confirma bandas y escenarios; no autoriza transcribir cifras. | U09-DG-056 y U09-074 conceptuales. | reference-only |

Fecha de acceso de todos los recursos externos: **2026-08-12**.

## Modalidades descartadas

- **Imagen anatómica:** no corresponde; U9 trata propagación, recintos y medición, no anatomía.
- **Captura de instrumento:** solo sería útil en U09-075, pero una captura real puede parecer validación de una app; se usará interfaz ficticia y claramente no instrumental.
- **Fotografía de material absorbente:** riesgo alto de reforzar “espuma = aislamiento”.
- **IA generativa:** no necesaria; los fenómenos requieren geometría y notación verificables.
- **Streaming:** no; todo recurso temporal tendrá archivo local o alternativa estática.
- **Tablas normativas como captura:** prohibidas; si se aprueba una norma, se reconstruirá una tabla nativa con trazabilidad celda por celda.

## Descargas

Se intentó descargar U09-IMG-003 desde el archivo original de Wikimedia Commons por ser claramente reutilizable. El servidor respondió HTTP 429 y no se creó archivo parcial. No se eludió el límite ni se descargaron alternativas de procedencia dudosa. La carpeta `assets/external/original/` quedó preparada, pero sin archivos.

## Criterios de aprobación de assets externos

1. licencia y autor verificables;
2. resolución ≥1200 px para media slide o ≥2000 px para visual dominante;
3. propósito que no pueda resolverse mejor con un visual propio;
4. recorte posible sin deformación ni pérdida de contexto;
5. ausencia de marca de agua, datos personales o publicidad dominante;
6. crédito visible de 9–10 pt y referencia completa en notas;
7. alt text y alternativa propia disponibles.
