# Unidad 4 — Revisión del storyboard

## Dictamen

**Aprobado para avanzar a curaduría de assets, especificación de gráficos y producción de diagramas.** No está aprobado todavía para redactar el contenido completo de slides ni para construir el PowerPoint: antes deben resolverse las decisiones abiertas de notación y validarse con el docente la extensión/ruta de dictado.

La propuesta cubre el alcance obligatorio, sostiene una progresión gradual y separa con claridad ruta central, material complementario y respaldo.

## Evidencia revisada

- Programa oficial, Unidad 4, p. 3.
- Capítulo LaTeX `04-sonido-propiedades-magnitudes.tex`.
- Capítulo PDF, pp. 89–117, incluidas las figuras 4.1–4.7.
- `course_map.md`, `course_dependency_map.md` y `content_coverage_matrix.csv`.
- `brief.md`, `content_inventory.md`, `source_analysis.md` y `open_decisions.md` de U4.
- Guías de presentación, notación y glosario.
- Template v01: mosaico de sus 27 layouts y auditoría existente.
- Presentación final de U3: revisión visual de sus 96 renders para continuidad de progresión, recaps y densidad.

## Validación estructural

| control | resultado | estado |
|---|---|---|
| IDs | U04-001 a U04-125, correlativos y únicos | conforme |
| Filas | 125 | conforme |
| Campos por fila | 15 en las 125 filas | conforme |
| Estados | 91 `central`, 18 `complementary`, 16 `backup` | conforme |
| Clases visuales | 43 diagram, 30 equation_only, 19 mixed, 19 none, 11 chart, 2 external_image, 1 video_or_gif | conforme |
| Candidatas `diagram-generation` | 81 slides, incluidas ecuaciones anotadas | conforme |
| Candidatas `chart-generation` | 17 slides | conforme |
| Layouts | Solo nombres existentes en el template/catalogo, incluidos `FA_02B`, `FA_06B` y `FA_14B` | conforme |
| Apertura y cierre | Portada, diagnóstico, objetivos, mapa, recap final, autoevaluación y puente U5 | conforme |

## Cobertura del programa

| contenido obligatorio | slides principales | juicio |
|---|---|---|
| Sonido como fenómeno físico y sensación sonora | U04-007–010, 068 | cubierto y delimitado |
| Generación del sonido | U04-010–014 | cubierto con cinco mecanismos |
| Elasticidad e inercia del medio | U04-015–021 | cubierto con progresión causal |
| Velocidad de propagación | U04-020–022 | cubierto; fórmula graduada |
| Campo acústico | U04-023–024 | cubierto |
| Presión acústica | U04-025–026 | cubierto |
| Velocidad de partícula | U04-027–028 | cubierto y contrastado con `c` |
| Impedancia acústica específica | U04-029–030 | cubierto con condiciones |
| Reflexión por discontinuidad | U04-031–033; 113 | concepto central, cálculo complementario/respaldo |
| Intensidad acústica | U04-034–039 | cubierto |
| Potencia y energía acústicas | U04-040–042 | cubierto y diferenciado de intensidad |
| Valores instantáneo, pico, pico a pico y medio | U04-043–050 | cubierto |
| Valor eficaz/RMS | U04-051–058 | cubierto con límite sinusoidal |
| Tono puro y señal compleja | U04-057–058, 109 | cubierto y conectado con U5 |
| Decibel y niveles | U04-059–068 | cubierto |
| Referencias en aire y agua | U04-062–065 | cubierto |
| Suma coherente y fase | U04-069–075 | cubierto |
| Suma no correlacionada y suma de niveles | U04-076–080 | cubierto |
| Ondas planas, cilíndricas y esféricas | U04-081–087; 117 | cubierto; cilíndrica tiene tratamiento propio |
| Campo libre, reverberante y difuso | U04-088–089; 116 | cubierto con límites |
| Ley del cuadrado inverso y distancia | U04-090–097; 118 | cubierto con hipótesis y ejemplo |
| Omnidireccionalidad, factor `Q` e índice `DI` | U04-098–102; 123 | cubierto; ambigüedad del programa resuelta sin inventar magnitud |

No se detecta ningún contenido obligatorio sin slide asignada.

## Trazabilidad de objetivos

| objetivo del brief | evidencia principal | comprobación |
|---|---|---|
| OA1 · fenómeno/sensación y cadena | U04-008–014 | recap U04-014 y error U04-106 |
| OA2 · elasticidad, inercia, `c` y `u` | U04-016–022, 027–028 | recap U04-022 y comparación U04-028 |
| OA3 · `p`, `u`, `Z`, `I`, `W_ac`, `E_ac` | U04-023–042 | ejemplo U04-039 y aplicación U04-042 |
| OA4 · descriptores y RMS | U04-043–058 | actividad U04-049 y recap U04-058 |
| OA5 · niveles, referencia y 10/20 | U04-059–068 | ejemplo U04-063 y recap/aplicación U04-068 |
| OA6 · suma coherente/no correlacionada | U04-069–080 | ejemplos U04-074/079 y árbol U04-080 |
| OA7 · geometrías y distancia | U04-081–097 | gráfico U04-086 y ejemplo U04-097 |
| OA8 · `Q` y `DI` | U04-098–102 | ejemplo U04-101 y aplicación U04-102 |

## Progresión y carga cognitiva

| bloque | carga | fundamento | control previsto |
|---|---|---|---|
| B00 | baja–media | activa lenguaje y prerrequisitos | diagnóstico sin sanción y mapa |
| B01 | media | varias entidades con vocabulario cotidiano ambiguo | cadena funcional y recap |
| B02 | media–alta | causalidad distribuida y relación multivariable | intuición antes de ecuación |
| B03 | alta | introduce `p`, `u`, `Z` y reflexión | una magnitud por etapa; cálculo de reflexión graduado |
| B04 | alta | distingue flujo local, potencia y energía | gráfico coordinado, ejemplo y aplicación instrumental |
| B05 | media | múltiples descriptores cercanos | misma señal y matriz comparativa |
| B06 | media–alta | operación cuadrática y ventana | proceso visual antes de integral |
| B07 | alta | logaritmos, referencias y tres tipos de nivel | rutina fija y ejemplo ancla |
| B08 | muy alta | superposición, fase, RMS y logaritmos | bifurcación coherente/no correlacionada y recap frecuente |
| B09 | media–alta | tres geometrías y tres regímenes de campo | comparación geométrica y árbol de selección |
| B10 | alta | distancia, dominio de validez y angularidad | intuición→ecuación→ejemplo→error |
| B11 | media | integración de decisiones | caso, lista de errores y mapa final |
| B12 | variable | formalismo y soluciones | uso a demanda fuera de la ruta central |

La densidad máxima se concentra deliberadamente en B03–B04, B07–B08 y B10. Cada tramo tiene divisor, ejemplo o actividad y recapitulación antes de avanzar.

## Repetición y redundancia

- La distinción físico/perceptual reaparece al tratar niveles porque cambia su función: de definición ontológica a límite interpretativo.
- La cadena fuente–medio–campo–receptor reaparece como cadena de medición; se añaden sensor, procesamiento y reporte.
- RMS reaparece en nivel y suma, pero solo como entrada operativa; el algoritmo no se vuelve a enseñar.
- Las condiciones de onda plana/campo libre se repiten junto a cada fórmula porque forman parte de su significado, no como nota ornamental.
- Los mapas de U04-006, 014 y 107 cambian de orientación a progreso y síntesis.

No se detectaron dos slides consecutivas con el mismo propósito, mensaje y tratamiento visual. Durante `slide-writing` deberá evitarse copiar definiciones completas en recaps.

## Viabilidad visual y continuidad

- Los layouts propuestos existen en el template y cubren portada, divisores, ecuaciones, ejemplos, aplicaciones, preguntas, recaps, media y apéndice.
- La alternancia visual evita una secuencia de ecuaciones idénticas: después de bloques formales aparecen gráfico, caso, comparación o recap.
- La continuidad con U3 se conserva mediante `FA_02B_CONOCIMIENTOS_PREVIOS`, mapas de clase, divisores, ejemplos resueltos y recaps parciales.
- Las siete figuras del capítulo se reconstruyen o reinterpretan; no se propone pegarlas como capturas pequeñas.
- Dos assets externos centrales/útiles y un recurso multimedia tienen alternativa propia o estática.
- Las 81 candidatas a diagrama no implican 81 artes únicos: se agrupan en 20 familias reutilizables con evolución pedagógica.

## Decisiones adoptadas

1. 125 slides totales: 91 centrales, 18 complementarias y 16 de respaldo.
2. Tres encuentros de aproximadamente 87, 97 y 108 minutos para la ruta central.
3. `W_ac` se usa provisionalmente para potencia acústica; el libro usa `W`.
4. `Q` y `DI` se presentan como factor e índice de directividad.
5. “No coherente” se operacionaliza como “no correlacionada durante la ventana”.
6. La onda cilíndrica recibe tratamiento central y solución de respaldo.
7. Integrales y derivaciones largas no bloquean el hilo central.

## Riesgos y controles pendientes

| severidad | riesgo | control antes de producción | estado |
|---|---|---|---|
| alta | Exceso de duración para el calendario real | Validar tres encuentros y ruta de corte con el docente. | abierto |
| alta | Saturación de ecuaciones anotadas en B07–B10 | Prototipar una slide de ecuación y una derivación a tamaño real. | abierto |
| alta | Ambigüedad final de `Q` frente a `Q_dir` | Resolver en `notation_guide.md` antes de redactar copy. | abierto |
| media | Referencias de agua y niveles de potencia/intensidad | Verificar valores exactos en LaTeX/PDF al redactar. | abierto |
| media | Patrón polar externo sin licencia o condiciones | Curar U04-AS-007 o usar datos sintéticos declarados. | abierto |
| media | Demostración de cancelación que no funcione en aula | Mantener gráficos y audio propio como evidencia principal. | controlado |
| media | Ponderaciones, campo próximo y psicoacústica invaden unidades futuras | Mantenerlos como límites, no como desarrollo. | controlado |
| baja | Helper de inspección no procesa rutas con espacios | Se usaron los renders completos existentes de U3 y el mosaico auditado del template; no afecta el contenido. | cerrado |

## Condiciones para avanzar

- Aprobación docente de la ruta de tres encuentros y del volumen central.
- Cierre de notación `W_ac`, `Q/Q_dir` y referencias de nivel.
- Priorización de los gráficos U04-CH-002, 003, 005, 007, 008, 010 y 011.
- Prototipo renderizado de las familias de diagramas U04-DG-005, 013, 014, 015 y 017.
- Curaduría o reemplazo sintético del patrón polar U04-AS-007.

Hasta cumplir esas condiciones, el storyboard queda en estado **planificado y revisado**, sin autorización para escribir slides completas ni generar el deck.
