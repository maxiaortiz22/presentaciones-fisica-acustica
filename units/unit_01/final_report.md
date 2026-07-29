# Informe final — Unidad 1

## Estado de cierre

**Unidad terminada.** La versión final cumple la definición de terminado de `AGENTS.md`. La revisión integral no registra problemas críticos ni mayores abiertos. La limitación menor de agrupación de formas está aceptada y permanecen tres sugerencias operativas que dependen del ensayo docente y del equipamiento del aula.

Archivo final:

- `output/unidad_01_nociones_basicas_final.pptx`
- `output/unidad_01_nociones_basicas_final.pdf`

SHA-256 del PowerPoint final: `1C8EA2C8D41E5EEC7907A3CA6F09A7E8E8B1DBD71C2B6089A5C29BF6DDEC7FD4`.

Las versiones `v01`, `v02`, `v02_diagram_fix` y la versión final previa a la reparación se conservaron sin sobrescritura.

## Definición de terminado

| componente | verificación | estado |
|---|---|---|
| `brief.md` | alcance, objetivos, carga cognitiva y decisiones de centralidad documentados | cumplido |
| `storyboard.md` | 94 slides trazadas, con bloques, fuentes, transiciones y estados | cumplido |
| `slide_text.md` | contenido visible, ecuaciones, captions, layouts y texto alternativo para 94 slides | cumplido |
| `speaker_notes.md` | notas pedagógicas para 94 slides | cumplido |
| `asset_manifest.csv` | 42 registros, identificadores únicos y créditos completos; los assets no utilizados conservan su estado de curación | cumplido |
| scripts | cuatro utilidades principales y 26 paquetes de figuras reproducibles con script y metadatos | cumplido |
| gráficos | 26 familias propias; SVG/PNG conservados y diagramas estructurales reconstruidos como formas nativas | cumplido |
| PowerPoint | versión final 16:9, editable, accesible y basada en el template | cumplido |
| PDF de revisión | `output/unidad_01_nociones_basicas_final.pdf`, 94 páginas 16:9, render completo inspeccionado | cumplido |
| render | 94 slides en `output/final_render/`, 94 páginas PDF renderizadas y mosaicos finales | cumplido |
| `review.md` | 0 problemas críticos y 0 mayores abiertos; una limitación menor aceptada | cumplido |
| consistencia | contraste con programa, mapas, glosario, notación y sistema visual | cumplido |

## Síntesis de la presentación

- **Cantidad total:** 94 slides.
- **Ruta central:** 72 slides.
- **Slides complementarias seleccionables:** 12.
- **Slides de respaldo:** 10.
- **Bloques pedagógicos principales:** 10, de B00 a B09.
- **Bloques de respaldo:** RB01 y RB02.
- **Duración estimada de exposición:** 225 minutos de contenido, más una pausa de 15 minutos; total previsto de 4 horas.

### Distribución por bloque

| bloque | foco | slides | duración estimada |
|---|---|---:|---:|
| B00 | apertura, diagnóstico, objetivos y mapa | 6 | 15 min |
| B01 | campo de la acústica y sistema fuente–medio–receptor | 8 | 20 min |
| B02 | medición, magnitudes, unidades y SI | 9 | 30 min |
| B03 | movimiento, masa, fuerza, presión y densidad | 12 | 35 min |
| B04 | notación científica, prefijos y análisis dimensional | 8 | 20 min |
| pausa | descanso previsto | — | 15 min |
| B05 | variables, funciones e inversas | 9 | 25 min |
| B06 | trigonometría, grados, radianes y ciclo | 9 | 25 min |
| B07 | exponenciales, logaritmos y anticipo del decibel | 10 | 25 min |
| B08 | medición física, percepción y conclusión clínica | 9 | 20 min |
| B09 | caso integrador, recapitulación y puente futuro | 4 | 10 min |
| RB01 | referencias y soluciones de mecánica y notación | 5 | a demanda |
| RB02 | profundización matemática, escalas dB y transferencia | 5 | a demanda |

## Temas cubiertos

- definición, alcance y aplicaciones de la acústica;
- fuente, medio, receptor, perturbación y propagación;
- medición, magnitud, símbolo, valor, unidad y referencia;
- Sistema Internacional, magnitudes fundamentales y derivadas;
- distancia, tiempo, rapidez media y velocidad de propagación;
- masa, peso, aceleración y fuerza;
- presión, área, volumen y densidad;
- notación científica, prefijos SI y órdenes de magnitud;
- consistencia dimensional y detección de resultados imposibles;
- variables, funciones, dominio e inversa;
- seno, coseno, tangente, grados, radianes y vuelta completa;
- crecimiento exponencial, logaritmos y escalas lineales y logarítmicas;
- relación logarítmica expresada en decibeles y necesidad de una referencia;
- distinción entre medición física, nivel referido, atributo perceptual y conclusión;
- aplicaciones a voz, micrófonos, registro, audiometría y razonamiento fonoaudiológico;
- integración de cálculos, unidades e interpretación con un caso de vocalización.

La matriz de cobertura y `review.md` confirman que el alcance obligatorio del programa está representado y que no existen omisiones críticas.

## Recursos multimedia

- **1 GIF propio** de propagación longitudinal, incorporado sin audio.
- **Alternativa estática** disponible para el GIF y para su uso sin conexión.
- **Demostración sugerida con resorte** acompañada por instrucciones de predicción, observación y comparación.
- No se incorporaron videos ni audios externos. Una demostración sonora en vivo queda como opción docente, no como requisito del deck.

## Gráficos y figuras propias

Se produjeron **26 familias de recursos gráficos propios**. Cada familia conserva, según corresponda:

- script reproducible;
- datos o modelo declarado;
- SVG;
- PNG de alta resolución;
- README;
- caption sugerido;
- texto alternativo;
- fuente o criterio de elaboración.

Los recursos cubren sistemas acústicos, mapas de magnitudes, movimiento y propagación, masa y peso, fuerza–presión–densidad, notación científica, prefijos, análisis dimensional, funciones e inversas, trigonometría, exponenciales, logaritmos, escalas, decibeles y distinciones entre medición e interpretación.

En el archivo final, los diagramas estructurales se implementan como objetos editables. Los gráficos cuantitativos y el GIF ocupan 16 objetos de imagen con texto alternativo; sus SVG y scripts fuente se conservan en `assets/generated/`.

## Slides complementarias y de respaldo

Las 12 slides complementarias permiten ajustar el ritmo sin romper la progresión central. Incluyen práctica adicional, ampliaciones matemáticas, conversiones y anticipos conceptuales.

Las 10 slides de respaldo reúnen:

- referencia completa del SI;
- tabla ampliada de prefijos;
- dependencias dimensionales;
- soluciones de diagnósticos y ejercicios;
- propiedades adicionales de logaritmos;
- distinción entre dB SPL, dB HL y dB SL;
- bibliografía técnica;
- banco de transferencia.

## Fuentes principales

1. Programa oficial de Física Acústica, alcance de Unidad 1.
2. Libro del curso, capítulo 1 en LaTeX.
3. Libro del curso en PDF, capítulo correspondiente.
4. `course_map.md` y `course_dependency_map.md`.
5. `content_coverage_matrix.csv`.
6. BIPM, *The International System of Units (SI Brochure)*.
7. NIST, recursos técnicos sobre el Sistema Internacional.
8. Guías locales de presentación, notación y glosario.

Las fuentes slide por slide están registradas en `source_map.md`; el deck final incorpora un bloque de fuente en las notas de las 94 slides.

## Decisiones pedagógicas

- Se priorizó intuición antes del formalismo y una idea principal por slide.
- Se construyó un puente explícito desde fenómenos cotidianos hacia lenguaje físico y matemático.
- Las magnitudes se presentan como una red de relaciones, no como definiciones aisladas.
- Los cálculos incluyen unidades, comprobación dimensional e interpretación física.
- Se distinguen deliberadamente dato físico, referencia, percepción y conclusión clínica.
- Se usan preguntas diagnósticas, mini ejercicios, errores frecuentes y recapitulaciones.
- La repetición de fuente–medio–receptor y de las cuatro categorías de descripción es pedagógica: cambia el contexto y aumenta la transferencia.
- Las ampliaciones matemáticas y técnicas se separan de la ruta central para permitir adaptación al grupo.
- La Unidad 1 establece la base terminológica, notacional, pedagógica y visual para las unidades siguientes.

## Verificaciones de producción

- 94 slides y 94 notas del orador.
- 94/94 notas con bloque `[Sources]`.
- 2 Slide Masters y 27 layouts en el paquete final.
- Numeración visible y editable en slides 2–94; portada sin número.
- 16/16 objetos de imagen con texto alternativo; los diagramas restantes son formas nativas.
- 1.639 formas editables, 49 conectores y una tabla nativa.
- 1 GIF incorporado y alternativa estática disponible.
- 2 enlaces externos funcionales registrados en la bibliografía y verificados el 2026-07-29.
- Textos, formas, flechas y numeración editables.
- Ecuaciones conservadas como texto editable con Cambria Math cuando fue posible.
- Gráficos incorporados en formato vectorial o raster de alta resolución, con scripts fuente reproducibles.
- Fuentes utilizadas: Calibri, Calibri Light y Cambria Math.
- Control automático de desbordes: aprobado.
- Fidelidad al template: aprobada; se conservaron 2 masters y 27 layouts.
- Comparación visual entre el candidato reparado y la versión accesible final: 94/94 slides idénticas.
- PDF final: 94 páginas, 960 × 540 pt, PDF 1.7 etiquetado.
- Mosaico final inspeccionado por lotes, sin solapamientos, recortes ni deformaciones.

## Limitaciones conocidas

- La extensión completa ocupa una clase de cuatro horas; las slides complementarias deben seleccionarse según el ritmo real del grupo.
- El GIF debe probarse en el equipo y en el modo de presentación del aula. Existe respaldo estático.
- Las ecuaciones son editables como texto, pero no todas están serializadas como objetos OMML.
- El PDF de revisión es una representación estática y rasterizada; no reproduce animaciones.
- Los diagramas nativos se editan como objetos individualmente nombrados; la API utilizada no permite agruparlos en un único objeto.
- Los gráficos cuantitativos se embeben como PNG por compatibilidad, pero conservan SVG y script reproducible.
- No se incorporó una demostración sonora. Puede añadirse en vivo si el docente dispone de calibración y condiciones controladas.
- Al ser la primera unidad terminada, su sistema funciona como línea de base para la consistencia de las unidades 2–10.

## Recomendaciones para dictar la clase

1. Usar las preguntas iniciales para estimar conocimientos previos antes de decidir cuántas slides complementarias exponer.
2. Mantener la ruta central y realizar la pausa prevista después de B04.
3. Hacer la demostración del resorte antes de formalizar fuente, medio y receptor.
4. Pedir siempre que los resultados incluyan unidad e interpretación, no solo un número.
5. Contrastar 343 m/s como valor condicionado con 340 m/s como redondeo didáctico del ejercicio.
6. Reforzar que un nivel en dB requiere indicar magnitud, referencia y procedimiento.
7. No intercambiar dB SPL, dB HL y dB SL; usar la slide de respaldo cuando aparezca esa duda.
8. Utilizar las soluciones de respaldo después de recoger los razonamientos del grupo.
9. Cerrar con el caso integrador y explicitar qué herramientas se reutilizarán en mecánica, ondas, sonido y audiología.

## Problemas abiertos

No quedan problemas críticos ni mayores. La limitación menor de agrupación está aceptada. Las sugerencias abiertas son:

- ensayar el ritmo real de exposición;
- probar el GIF en el equipo del aula;
- decidir si se realiza una demostración sonora en vivo.

Estas sugerencias no impiden el uso de la versión final.
