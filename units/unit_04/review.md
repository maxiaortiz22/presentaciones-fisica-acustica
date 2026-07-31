# Revisión integral — Unidad 4

## Alcance y método

- Deck de entrada: `output/unidad_04_sonido_magnitudes_v01.pptx`.
- Deck corregido: `output/unidad_04_sonido_magnitudes_v02.pptx`.
- Se inspeccionaron el PowerPoint, las 125 diapositivas renderizadas, los renders ampliados de las slides afectadas, el PDF final de 125 páginas, los layouts, las notas, los assets, `slide_text.md`, `storyboard.md`, el programa oficial y el capítulo 4 del libro en LaTeX/PDF.
- Dimensiones: contenido, pedagogía, diseño, diagramas/esquemas, producción y naturalidad.
- Resultado de la auditoría completa: 0 `critical`, 14 `major`, 6 `minor` y 4 `suggestion`.
- Estado posterior a la corrección: 0 `critical` y 0 `major` abiertos.

## Cobertura y exactitud

Los 22 temas obligatorios desagregados del programa están presentes. La secuencia cubre naturaleza física y perceptual del sonido, generación, elasticidad e inercia, rapidez, campo y magnitudes, impedancia y reflexión, descriptores temporales, RMS, niveles y referencias, coherencia, suma energética, geometrías, ley de distancia y directividad.

La correspondencia conceptual con el capítulo 4 es sustantivamente completa. Se verificaron las referencias `20 µPa` para aire, `1 µPa` para agua, `10⁻¹² W·m⁻²` para intensidad y `10⁻¹² W` para potencia; la relación `20 log₁₀(p/p_ref)`; los casos de suma coherente/no correlacionada; y las leyes ideales de decaimiento plano, cilíndrico y esférico. No se detectaron errores científicos críticos.

## Evaluación pedagógica

- La progresión parte de fenómenos y mediciones concretas antes de formalizar magnitudes y niveles.
- Los prerrequisitos se recuperan de manera explícita y las condiciones de validez acompañan las fórmulas.
- Hay divisores, recapitulaciones parciales, preguntas, errores frecuentes, aplicaciones a medición/audiología y soluciones de respaldo.
- La carga cognitiva es alta por extensión, pero está segmentada en once bloques y un apéndice; conviene planificar más de un encuentro o separar la ruta central del respaldo.
- En v02 se retiraron visuales reutilizados que no respondían a la consigna y se dejaron explicaciones editables autocontenidas.

## Hallazgos y resolución

| review_id | slide_id | category | severity | finding | correction/evidence | status | owner |
|---|---|---|---|---|---|---|---|
| U04-R-001 | U04-025, 044, 047, 057, 109 | diseño/gráficos | major | Leyendas metodológicas internas invadían ejes o pies. | Se eliminaron del asset; las condiciones permanecen en captions/notas. Render v02 sin colisiones. | resuelto | Codex |
| U04-R-002 | U04-084, 086 | diseño/gráficos | major | Rótulo inferior y etiqueta vertical demasiado extensa reducían la lectura. | Se retiró el texto interno redundante y se acortó el eje a `I/I₀ · escala log`. Render ampliado aprobado. | resuelto | Codex |
| U04-R-003 | U04-095, 097 | diseño/gráficos | major | La etiqueta de 8 m quedaba cortada y el pie competía con el eje X. | Se reancló la anotación extrema hacia el interior y se retiró el pie interno. `−18,06 dB` se ve completo. | resuelto | Codex |
| U04-R-004 | U04-121 | diseño/gráficos | major | El rótulo interno se montaba sobre el eje X y el eje Y era demasiado largo. | Se retiró el rótulo, se acortó a `Incremento total (dB)` y se ajustaron márgenes. | resuelto | Codex |
| U04-R-005 | U04-122 | diseño/gráficos | major | La leyenda tapaba la ecuación de amplitud resultante. | Ecuación y leyenda se distribuyeron en bandas superiores separadas. | resuelto | Codex |
| U04-R-006 | U04-011, 058 | contenido/diseño | major | El asset combinado mostraba paneles ajenos a la consigna. | Se sustituyó por contenido editable específico para cada slide. | resuelto | Codex |
| U04-R-007 | U04-065 | contenido | major | Faltaban las referencias explícitas de aire y agua. | Se incorporaron `20 µPa` y `1 µPa`, con la advertencia de no comparar niveles sin declarar medio y referencia. | resuelto | Codex |
| U04-R-008 | U04-066 | contenido/pedagogía | major | Faltaba la derivación que explica el factor 20. | Se incorporó `10 log₁₀[(p/p_ref)²] = 20 log₁₀(p/p_ref)` y su condición física. | resuelto | Codex |
| U04-R-009 | U04-102 | contenido/pedagogía | major | Se pedía interpretar un patrón polar no aprobado y ausente. | La slide quedó como advertencia conceptual autocontenida sobre frecuencia y condiciones; ya no exige leer un gráfico inexistente. | resuelto | Codex |
| U04-R-010 | U04-105, 124 | contenido/pedagogía | major | La cadena de medición reutilizada no representaba el caso integrador. | Se reemplazó por consignas y criterios de decisión editables coherentes con el caso y su solución. | resuelto | Codex |
| U04-R-011 | U04-114 | contenido | major | No aparecían las referencias de `L_I` y `L_W`. | Se añadieron `I_ref = 10⁻¹² W·m⁻²` y `W_ref = 10⁻¹² W` con notación legible. | resuelto | Codex |
| U04-R-012 | U04-120 | contenido/diagramas | major | Se mostraba un ejemplo de impedancia ajeno al ejercicio RMS, con conectores superpuestos. | Se retiró el asset y se incorporaron las expresiones sinusoidal y discreta como ecuaciones editables. | resuelto | Codex |
| U04-R-013 | U04-125 y títulos con notación | contenido/producción | major | Quedaban comandos LaTeX y backticks visibles. | Se corrigió el parser y el texto fuente; el render final no muestra marcas de LaTeX/Markdown. | resuelto | Codex |
| U04-R-014 | deck completo | naturalidad | minor | Hay secuencias largas de slides similares por revelado progresivo. | Se conservan porque cumplen una función docente; revisar si se crea una versión para lectura autónoma. | abierto | Docente |
| U04-R-015 | deck completo | producción/editabilidad | minor | Los diagramas son SVG dentro del PPTX y no nodos nativos de PowerPoint. | Se conservan los fuentes editables y scripts reproducibles. Migrar sólo los diagramas que requieran edición frecuente. | abierto | Producción |
| U04-R-016 | U04-013, 072–076, 079, 095, 097 | producción | minor | La multimedia planificada no está incrustada. | Se mantiene alternativa estática declarada hasta aprobar fuente/licencia y realizar prueba de reproducción. | abierto | Docente |
| U04-R-017 | captions y créditos | diseño | minor | Captions/créditos usan 11–12 pt y no son lectura expositiva desde el fondo. | Se aceptan como metadato; ampliar sólo si una condición pasa a ser contenido principal. | abierto | Producción |
| U04-R-018 | U04-001–125 | producción | minor | El deck depende de Calibri, Calibri Light y Cambria Math. | Son las únicas fuentes directas; verificar sustitución en el equipo del aula o incrustar si la licencia lo permite. | abierto | Docente |
| U04-R-019 | U04-102 | recursos | suggestion | Falta un patrón polar real aprobado con frecuencia y condiciones declaradas. | U04-CH-012 sigue `pending_approval`; puede recuperarse el ejercicio gráfico en una versión posterior. | abierto | Docente |
| U04-R-020 | deck completo | naturalidad | suggestion | 125 slides pueden ser excesivas para una única sesión. | Separar ruta central y respaldo o distribuir la unidad en más de un encuentro. | abierto | Docente |
| U04-R-021 | U04-113 | diseño | suggestion | La anotación `η=1` tiene contraste bajo. | Es aceptable como respaldo; reforzar si pasa a la ruta central. | abierto | Producción |
| U04-R-022 | 99 imágenes | producción/accesibilidad | major | El exportador no había escrito la propiedad de texto alternativo, aunque la descripción estaba en notas. | Se asignó en PowerPoint el texto alternativo específico a las 99 imágenes; verificación XML `99/99`. | resuelto | Codex |
| U04-R-023 | U04-044, 067, 070, 084–086, 095, 099 | producción | minor | Quedaban ocho placeholders mínimos fuera del lienzo. | Se eliminaron; verificación XML: 0 placeholders locales. | resuelto | Codex |
| U04-R-024 | deck completo | producción | suggestion | El verificador heurístico de fidelidad marca reemplazos de contenido demostrativo como overlays y detecta un generador auxiliar ajeno al deck final. | Revisión manual y del paquete: el autor final importa el starter, conserva 2 masters/27 layouts, elimina contenido local de muestra y no deja placeholders. Se documenta el falso positivo. | abierto_documentado | Producción |

## Verificación final de v02

- Render final completo: 125/125 slides a 1600 × 900 px.
- Revisión ampliada: U04-025, 044, 057, 084, 086, 095, 097, 109, 114, 120, 121, 122, 124 y 125.
- Diagramas: sin texto fuera de cajas, flechas sobre texto, conectores atravesando contenido, etiquetas montadas sobre líneas ni auto-shrink crítico en el render final.
- Control automático de canvas: `Test passed. No overflow detected.`
- PDF final: 125 páginas, 16:9, renderizado y revisado en las páginas afectadas.
- Paquete PPTX: 125 slides, 125 notes slides, 2 masters, 27 layouts, 99 imágenes con texto alternativo, 0 placeholders locales y 3 enlaces externos.
- Notas: 125/125 no vacías, con bloque `[Sources]` y descripción alternativa.
- Fuentes directas: Calibri, Calibri Light y Cambria Math.
- Peso final: aproximadamente 2,50 MiB; el guardado en PowerPoint consolidó medios duplicados sin aplanar las slides.

## Problemas abiertos

No quedan problemas `critical` ni `major`. Permanecen abiertos cinco `minor` —revelados extensos, SVG no nativos, multimedia pendiente, captions pequeños y dependencia tipográfica— y cuatro `suggestion`, todos documentados en la tabla. Ninguno impide la proyección en clase ni afecta exactitud, legibilidad o integridad del archivo.

## Cierre final posterior a la revisión pedagógica independiente

La revisión pedagógica independiente se realizó después de v02 y reabrió doce hallazgos `major`. El cierre final no conserva la afirmación anterior como autoridad: cada hallazgo se volvió a contrastar con el PPTX y el render.

| Hallazgo independiente | Estado final | Resolución o aceptación explícita |
|---|---|---|
| U04-IPR-001 · duración | resuelto | La ruta central se recalculó en 347 min y se distribuyó en cuatro encuentros de 98, 84, 76 y 89 min. |
| U04-IPR-002 · prerrequisitos/RMS | resuelto | U04-004 ya no anticipa el visual de RMS; U04-038 declara el uso como anticipo controlado y define operacionalmente el valor eficaz antes de la relación energética. |
| U04-IPR-003 · revelado progresivo | resuelto | Se retiraron visuales familiares completos en las slides donde mostraban fórmulas futuras; las relaciones centrales pasan a texto y ecuaciones editables específicas. |
| U04-IPR-004 · suma 073/078/079 | resuelto | U04-073 y 078 muestran las expresiones prometidas; U04-079 incluye sustitución y resultado de 70 + 70 dB. |
| U04-IPR-005 · coherencia | resuelto | El árbol binario se retiró del recorrido central; la secuencia separa coherencia de fase cero y conserva resultados intermedios. |
| U04-IPR-006 · caso integrador | resuelto | U04-105 contiene datos, distancias, referencia y condiciones; U04-124 resuelve cada contribución y la suma final `74,95 dB SPL`. |
| U04-IPR-007 · solución RMS | resuelto | U04-120 calcula media y RMS con cuatro muestras y explica por qué el atajo sinusoidal no es universal. |
| U04-IPR-008 · directividad | resuelto | U04-102 usa datos didácticos normalizados a dos frecuencias y tres ángulos; no pide leer un patrón inexistente. El dataset real queda como ampliación futura. |
| U04-IPR-009 · notas estandarizadas | aceptado con condición | Se reescribieron las preguntas y guías de las slides de mayor riesgo conceptual. Las preguntas genéricas restantes se aceptan como andamiaje opcional, no como guion obligatorio del docente. |
| U04-IPR-010 · glifos | resuelto | U04-085, 092 y 108 ya no dependen de los glifos corruptos; el render final no contiene relaciones matemáticas ilegibles. |
| U04-IPR-011 · densidad B03–B04 | aceptado con condición | El contenido se conserva por cobertura del programa, pero se dicta al final del primer encuentro y al inicio del segundo, con recap U04-033 y sin desarrollar formalismo complejo. |
| U04-IPR-012 · recapitulaciones | aceptado con condición | Se conservan siete recaps por la densidad de U4; U04-080 y U04-108 pasan a recuperación activa. En las demás, las notas indican ocultar o pedir respuestas antes de revelar. |

Resultado final: **0 problemas críticos y 0 problemas mayores no resueltos o no aceptados**. Las aceptaciones anteriores tienen una condición pedagógica explícita y se registran también en `final_report.md`.

### Auditoría final del paquete

- 125 slides y 125 notes slides;
- 125 bloques `[Sources]`;
- 2 masters y 27 layouts;
- 75 imágenes/figuras insertadas con 75 descripciones accesibles;
- 0 placeholders locales;
- numeración continua 1–125;
- 3 enlaces externos preservados;
- 0 comandos LaTeX, backticks, badges de producción o etiquetas de multimedia pendiente visibles;
- PDF de revisión de 125 páginas y render final de 125 PNG;
- 0 problemas críticos o mayores observados en las slides afectadas a tamaño original.

## Estado de aprobación

`unidad_04_sonido_magnitudes_final.pptx` queda aprobada para uso docente y la Unidad 4 cumple la definición de terminado. No existen problemas `critical` ni `major` sin resolver o aceptar explícitamente. La multimedia no aprobada, el patrón polar real pendiente y la editabilidad externa de algunos SVG permanecen como limitaciones conocidas, pero no bloquean el cierre porque el recorrido visible es autocontenido y conserva alternativas estáticas.
