# Unidad 3 — Revisión del storyboard

## Dictamen

**Aprobado para pasar a la planificación detallada de recursos visuales, sin avanzar todavía a `slide-writing` ni a PowerPoint.**

El storyboard cubre el alcance obligatorio del programa, sostiene una progresión gradual para primer año y separa una ruta central de materiales complementarios y de respaldo. Las decisiones logísticas sobre duración y disponibilidad de demostraciones siguen abiertas, pero cuentan con alternativas que no rompen la secuencia.

## Evidencia revisada

- `AGENTS.md`.
- Programa oficial 2025, Unidad 3, p. 3.
- `context/libro_latex/chapters/03-mecanica-ondulatoria.tex`.
- Libro del curso en PDF, pp. 61–88.
- `course_map.md`.
- `course_dependency_map.md`.
- `content_coverage_matrix.csv`.
- `units/unit_03/brief.md`.
- `units/unit_03/content_inventory.md`.
- `units/unit_03/source_analysis.md`.
- `units/unit_03/open_decisions.md`.
- `style/presentation_style_guide.md`.
- `style/notation_guide.md`.
- `style/glossary.md`.
- `style/layout_catalog.md`, `style/component_catalog.md` y `style/template_mosaic.png`.
- `output/fisica_acustica_template_v01.pptx`, contrastado mediante el mosaico y los catálogos ya renderizados.
- Unidad 2 final y su contact sheet de 110 slides, usados como referencia de continuidad, ritmo, densidad y puente conceptual.

La inspección estructural directa del `.pptx` con la herramienta de presentaciones no fue posible porque el runtime local no expuso correctamente su paquete de análisis. La revisión visual no quedó bloqueada: el repositorio contiene renders completos, mosaicos, catálogos y auditorías del template y de la Unidad 2.

## Auditoría estructural

| control | resultado | estado |
|---|---|---|
| IDs | U03-001 a U03-096, consecutivos y sin duplicados | conforme |
| Columnas obligatorias | 15 campos en las 96 filas | conforme |
| Campos vacíos estructurales | no hay filas truncadas ni estados desplazados | conforme |
| Estados | 69 `central`, 14 `complementary`, 13 `backup` | conforme |
| Clases visuales | 19 `chart`, 31 `diagram`, 15 `mixed`, 15 `equation_only`, 14 `none`, 2 `video_or_gif` | conforme |
| Valores permitidos | solo se usan las siete clases admitidas; `external_image` no se fuerza porque las fotos son opcionales | conforme |
| Layouts | todos pertenecen al catálogo real `FA_00`–`FA_23` | conforme |
| Diagramas candidatos | 55 slides marcadas explícitamente para `diagram-generation` | conforme |
| Gráficos candidatos | 23 slides marcadas explícitamente para `chart-generation`; se agrupan en 13 familias reproducibles | conforme |
| Redacción completa | no se produjo copy final ni notas completas | conforme |
| PowerPoint | no se creó ni modificó un `.pptx` | conforme |

## Cobertura del programa

| alcance obligatorio | desarrollo central | complemento o respaldo | evaluación |
|---|---|---|---|
| Movimiento oscilatorio | U03-007–010 | U03-013–014 | Cubierto mediante equilibrio, movimiento local y demostración. |
| Movimiento ondulatorio | U03-009–016 y U03-048–063 | U03-012–013 | Cubierto como propagación en un medio con distinción materia–perturbación. |
| Movimiento armónico simple | U03-017–025 y U03-029 | U03-026, U03-030–033, U03-085–088 | Cubierto con modelo, fuerza restauradora, parámetros y expresión temporal; formalismo extendido fuera de la ruta central. |
| Tono puro: definición y expresión | U03-039–040 | U03-041 | Cubierto como modelo sinusoidal ideal y limitado frente a una realización real. |
| Representación en un parlante | U03-042–047 | U03-030 y assets opcionales | Cubierta la cadena señal–cono–aire–presión y la necesidad de calibración. |
| Frecuencia `f` | U03-023–025 | U03-030, U03-057–058 | Definida, interpretada, calculada y aplicada. |
| Período `T` | U03-022, U03-024–025 | U03-051, U03-058 | Definido, leído en un registro temporal y relacionado con `f`. |
| Amplitud | U03-021, U03-027, U03-029 | U03-030 y U03-035 | Definida con referente y unidad; diferenciada de valor instantáneo y atributo perceptual. |
| Fase | U03-064–066 y U03-068–069 | U03-026 y U03-067 | Cubierta primero como estado del ciclo y luego como comparación. |
| Longitud de onda `λ` | U03-052–058 | U03-055 y U03-089–091 | Definida, leída espacialmente y usada en `c=λf`. |

No se omite ningún contenido obligatorio. `c=λf`, velocidad de partícula y superposición se conservan como ampliaciones justificadas por el capítulo, el mapa de dependencias y los errores conceptuales que deben prevenirse.

## Mapeo de objetivos

| objetivo del brief | evidencia principal | comprobación |
|---|---|---|
| Distinguir oscilación local y propagación | U03-008–016 | U03-014 y recap U03-016 |
| Explicar el MAS y sus hipótesis | U03-017–020 | recap U03-027 y caso U03-080 |
| Interpretar amplitud, frecuencia, período y fase | U03-021–029 y U03-064–068 | U03-034, U03-068 y diagnóstico final |
| Leer una sinusoide de manera físicamente responsable | U03-028–038 | checklist U03-038 y caso U03-080 |
| Relacionar tono puro, parlante y medio | U03-039–047 | recap U03-047 y aplicación U03-046 |
| Diferenciar cortes temporal y espacial | U03-048–054 | ejercicio U03-058 |
| Calcular e interpretar `c=λf` | U03-056–058 | U03-058 y solución U03-094 |
| Aplicar el modelo con límites a voz, audición y medición | U03-046, U03-076–080 | caso integrador U03-080 |

## Progresión y carga cognitiva

| bloque | carga | decisión de secuencia | alivio o recapitulación |
|---|---|---|---|
| B00 · Apertura | media | fenómeno, diagnóstico, prerrequisitos, objetivos y mapa | U03-006 orienta sin formalizar |
| B01 · Oscilación y onda | media–alta | movimiento local antes de onda; materia antes de tipos | U03-016; demostración opcional |
| B02 · MAS | alta | modelo antes de parámetros; una magnitud nueva por slide | U03-027 |
| B03 · Sinusoides | muy alta | ecuación antes de lectura crítica; `x`, `v`, `a` complementarias | U03-038 |
| B04 · Tono y parlante | alta | definición antes de transducción; cada dominio con variable propia | U03-047 |
| B05 · Onda viajera | muy alta | función de dos variables, mapa y dos cortes separados; fórmula después | U03-059; ejercicio U03-058 |
| B06 · Velocidades y fase | alta | `u`–`c` antes de retomar fase; fase cualitativa antes de `Δφ` | U03-069 |
| B07 · Superposición | alta | suma instantánea, casos extremos y caso parcial; fórmula general en respaldo | U03-078 |
| B08 · Integración | media–alta | aplicación, caso, recap, diagnóstico y puente | U03-081–083 |
| B09 · Respaldo | variable | consulta no lineal | no forma parte de la exposición regular |

La carga máxima se concentra en B05 y B06. No deben dictarse sin una pausa, una recapitulación o un cambio de actividad entre ambos.

## Revisión de repetición y redundancia

- Movimiento local frente a propagación aparece en B01, B04 y B06, pero cambia de fenómeno básico a transducción y luego a comparación de velocidades.
- Fase se introduce cualitativamente en U03-026 y se recupera como relación en B06; la segunda aparición es más exigente.
- La cadena del parlante reaparece en U03-047 como control de variables y unidades, no como repetición del mecanismo.
- El diagnóstico U03-003 se repite en U03-082 exactamente para comparar razones iniciales y finales.
- Los recaps U03-016, 027, 038, 047, 059, 069, 078 y 081 agregan una regla de decisión o integran representaciones; ninguno copia el bloque precedente.

No se detectó redundancia sin propósito. En la fase de `slide-writing` deberá evitarse que la redacción visible vuelva equivalentes los títulos de explicación y recapitulación.

## Viabilidad visual

- Los layouts sugeridos existen en el template y cubren todos los tipos requeridos.
- Los 55 candidatos a `diagram-generation` están agrupados en 25 paquetes para reutilizar geometría sin clonar slides.
- Los 23 candidatos a `chart-generation` se reducen a 13 datasets o familias, lo que mejora consistencia.
- U03-044, U03-050, U03-053, U03-059, U03-080, U03-081 y U03-095 requieren slide completa o división si el texto no conserva los mínimos tipográficos.
- No se depende de imágenes externas para ningún contenido obligatorio.
- Toda animación o audio tiene alternativa estática.

## Continuidad con otras unidades

- **Desde U1:** ejes, unidades, seno/coseno, funciones y lectura de gráficos.
- **Desde U2:** sistema, equilibrio, fuerza restauradora, inercia, elasticidad, amortiguamiento y condiciones del medio.
- **Hacia U4:** presión acústica, magnitudes, calibración y límites de la curva normalizada.
- **Hacia U5:** forma temporal, tono ideal, superposición y necesidad de separar componentes.
- **Hacia U6–U7:** cadena de recepción y distinción física–perceptual.
- **Hacia U9:** dependencia de `c` respecto de las condiciones del medio.

El cierre U03-083 explicita los puentes a U4 y U5 sin enseñar anticipadamente RMS, nivel, Fourier, pitch o sonoridad.

## Decisiones de trabajo adoptadas

1. `ω`, `k_onda`, cinemática completa y fórmula general de interferencia quedan en respaldo.
2. Posición, velocidad y aceleración se trabajan cualitativamente como complemento, no como requisito de la ruta central.
3. `ξ(x,t)` se introduce antes de los cortes solo como pregunta “dónde y cuándo”; la ecuación completa aparece después de leer tiempo y espacio.
4. Superposición cualitativa se mantiene central por su valor preparatorio; cancelación activa es complementaria.
5. El ejemplo de longitud de onda usa `c≈340 m/s` como dato del problema, no como constante universal.
6. La planificación preferida es de tres encuentros de 75–80 minutos; el storyboard también permite dos encuentros extendidos mediante recortes complementarios.
7. Ninguna demostración física o multimedia es requisito para cubrir el programa.

## Riesgos y controles para la fase siguiente

| riesgo | severidad | control |
|---|---|---|
| Saturar B05 con función de dos variables | alta | Mantener U03-049 conceptual, reutilizar un único dataset y separar cortes. |
| Dibujar flechas sobre partículas o texto | alta | Enviar los paquetes críticos a `diagram-generation` y validar a tamaño final. |
| Usar escalas distintas en comparaciones | alta | Fijar escalas comunes en U03-CH03, U03-CH10 y U03-CH12. |
| Confundir `k_s` con `k_onda` | alta | Aplicar subíndices en toda ecuación y revisar contra `notation_guide.md`. |
| Introducir presión sin unidad o calibración | media–alta | Resolver la escala de U03-CH06 antes de redactar U03-045. |
| Depender de audio o video en aula | media | Conservar alternativa estática y consignas equivalentes. |
| Exceso de duración | media | Priorizar las 69 centrales y distribuirlas por encuentros; no comprimir B05–B06. |

## Condición de avance

El siguiente paso permitido es curar assets, producir gráficos o diseñar diagramas a partir de los inventarios iniciales. Antes de `slide-writing` conviene confirmar:

- tiempo real disponible y cantidad de encuentros;
- disponibilidad de resorte, parlante y reproducción segura;
- escala física o normalizada para U03-045;
- si la institución desea conservar la aplicación de cancelación activa.

No corresponde todavía redactar el texto completo de las slides ni producir el PowerPoint.
