# Informe final — Unidad 09

## Estado de cierre

La Unidad 09, **Factores que afectan a la propagación del sonido**, cumple la definición de terminado del repositorio. La presentación final tiene 96 diapositivas, 96 notas del orador, render completo, PDF de revisión y controles estructurales aprobados. No quedan problemas críticos ni mayores.

Archivo final publicado: `../../output/unidad_09_propagacion_sonido_final.pptx`. Se conserva una copia de producción idéntica en `output/unidad_09_propagacion_sonido_final.pptx` dentro de la unidad.

## Entregables verificados

| Entregable | Estado | Evidencia |
|---|---|---|
| `brief.md` | Completo | Alcance, objetivos, prerrequisitos, dificultades, aplicaciones y límites. |
| `storyboard.md` | Completo | Secuencia de 96 slides, rutas y fuentes. |
| `slide_text.md` | Completo | Texto visible, fórmulas, visuales, captions y alt text. |
| `speaker_notes.md` | Completo | 96/96 slides con notas; se retiraron campos sin acción y preguntas genéricas. |
| `asset_manifest.csv` | Completo | 95 registros con tipo, estado, procedencia y propósito. |
| `scripts/` | Completo | 18 scripts de producción, gráficos, diagramas, PDF y validación. |
| Gráficos | Completo | Archivos reproducibles y versiones SVG/PNG; 4 gráficos cuantitativos usados en el deck final. |
| Diagramas | Completo | 47 diagramas de la biblioteca insertados y 31 composiciones nativas adicionales; 67 fuentes editables `.pptx` aprobadas en la biblioteca. |
| PowerPoint | Completo | Copia publicada en el `output/` raíz y copia de producción en la unidad, sin sobrescribir v01 ni v02. |
| PDF de revisión | Completo | `unidad_09_propagacion_sonido_final_review.pdf`, 96 páginas. |
| Render | Completo | 96 PNG en `output/unidad_09_propagacion_sonido_final/`. |
| `review.md` | Completo | 0 críticos, 0 mayores; una incidencia menor opcional. |
| Revisión de consistencia | Completa | `consistency_report.md` actualizado; tres inconsistencias resueltas y una diferencia técnica aceptada. |

## Magnitud y duración

- **Cantidad de slides:** 96.
- **Ruta central:** 75 slides, aproximadamente 260 minutos.
- **Complementarias:** 9 slides, aproximadamente 27 minutos más una ampliación cualitativa sin tiempo fijo.
- **Respaldo:** 11 slides, aproximadamente 36 minutos más dos ampliaciones cualitativas sin tiempo fijo.
- **Fuente bloqueada tratada de forma segura:** 1 slide sin tiempo fijo.
- **Duración completa tabulada:** 323 minutos, más las cuatro slides cualitativas a demanda. En clase conviene distribuir la ruta central en tres encuentros y un cierre integrador, no proyectar las 96 slides en una única sesión.

| Bloque | Slides | Tiempo tabulado |
|---|---:|---:|
| Encuentro 1 — fuente, distancia, directividad y atmósfera | 1–33 | 113 min |
| Encuentro 2 — interfaces, obstáculos y recintos | 34–56 | 77 min |
| Encuentro 3 — aislamiento, ley de masas y cabinas | 57–77 | 72 min |
| Integración y cierre | 78–84 | 29 min |
| Respaldo y ampliaciones | 85–96 | 32 min |

## Temas cubiertos

La cobertura del programa es completa y corresponde al capítulo 9 del libro:

1. distancia, divergencia geométrica y ley del inverso del cuadrado;
2. fuentes direccionales, factor de directividad e índice de directividad;
3. temperatura y rapidez del sonido;
4. viento uniforme, dirección y gradientes;
5. presión, densidad, humedad y absorción atmosférica;
6. reflexión, absorción y transmisión en interfaces;
7. refracción atmosférica e interfaz aire–sólido;
8. difracción, barreras y relación con la longitud de onda;
9. recintos, absorción equivalente, reverberación y Sabine;
10. acondicionamiento, aislamiento, insonorización y ley de masas;
11. cabinas sonoamortiguadas, vías de transmisión y verificación;
12. criterio de ruido máximo admisible para audiometría, tratado sin inventar una cifra normativa universal.

## Recursos visuales y multimedia

- **Gráficos propios usados:** 4, sobre patrón de directividad, rapidez y temperatura, longitud de onda y decaimiento `T₆₀`.
- **Diagramas propios:** 47 diagramas procedentes de la biblioteca de assets y 31 composiciones editables construidas directamente en PowerPoint.
- **Biblioteca organizada:** 75 SVG, 90 PNG, 67 archivos PowerPoint editables y 221 archivos JSON de trazabilidad o validación.
- **Multimedia:** no hay audio ni video embebido. `U09-MEDIA-001` es un audio comparativo opcional para la slide 55; la alternativa estática de habla seca/reverberada permite dictarla sin el recurso.
- **Slides complementarias:** 9 de ampliación y 11 de respaldo. La slide normativa mantiene un tratamiento conceptual seguro mientras no exista una fuente institucional completa.

## Fuentes principales

- Programa oficial de Física Acústica de UCASAL, 2025, Unidad 9.
- Libro del curso, capítulo 9, páginas 235–259.
- Fuente LaTeX `context/libro_latex/chapters/09-propagacion-sonido.tex` y figuras TikZ de la unidad.
- Guía de estilo, glosario, guía de notación y registro de decisiones del proyecto.
- Identificadores ISO 8253-1, ISO 8253-2 e ISO 1996-2 como referencias a verificar antes de incorporar valores normativos; no se atribuyen cifras sin edición y contexto completos.

Cada una de las 96 notas incluye un bloque `[Sources]`. Los códigos de producción se conservan en notas y manifiesto, no en captions visibles.

## Decisiones pedagógicas

- Organizar la unidad como secuencia **mecanismo → modelo → estimación → límite**.
- Separar fuente, trayecto, receptor y medición antes de introducir cálculos.
- Presentar intuición y condiciones de validez antes de cada fórmula.
- Diferenciar divergencia, absorción, reflexión, transmisión, refracción y difracción antes de integrarlas.
- Usar casos de clínica, recinto y cabina como puente hacia la Unidad 10.
- Conservar diferencias de ritmo y densidad de diagramas frente a U7–U8 porque responden al contenido físico, no a una inconsistencia de estilo.
- Reservar ampliaciones formales o normativas para cuando exista fuente primaria suficiente.

## Producción, editabilidad y consistencia

- Formato 16:9, 2 masters y 27 layouts conservados.
- Texto, ecuaciones, tablas, tarjetas, conectores y diagramas principales editables en PowerPoint.
- Los cuatro gráficos insertados se entregan como SVG y PNG, con scripts reproducibles; no son gráficos nativos de PowerPoint.
- Numeración visible 1–96 mediante objetos editables. Los campos dinámicos existen en los layouts, pero no se visualizan en el render de las slides importadas; se mantiene la solución local sin duplicación visual.
- Cuatro imágenes con texto alternativo OOXML; los diagramas construidos con formas tienen descripción funcional en las notas.
- No hay relaciones externas ni enlaces rotos. Tampoco hay video o audio embebido.
- Fuentes utilizadas en el deck: Calibri, Calibri Light y Cambria Math, disponibles en el entorno de producción.
- Tamaño final: 528.448 bytes.

## Verificaciones finales

- `slides_test.py`: aprobado, sin overflow.
- `u09_validate_final_deck.py`: aprobado, 0 critical y 0 major.
- 96/96 slides renderizadas y revisadas en mosaicos.
- Slides 37, 58, 59, 86 y 90 revisadas además a resolución completa después de normalizar `Rₑ` y `τₑ`.
- 96/96 notas, 96/96 marcadores `[Sources]`, 4/4 imágenes con alt text.
- 0 códigos internos visibles, 0 campos de notas “No corresponde” y 0 consignas genéricas detectadas.
- SHA-256 del PPTX final: `0071FA5B817A01284F8891B1D70D9152C37CF7CCA5EEBA69197099683F64A8FA`.

## Limitaciones conocidas

1. El audio opcional `U09-MEDIA-001` no está disponible ni embebido; no afecta la autosuficiencia de la slide 55.
2. No se publica un máximo universal de ruido para cabinas hasta adoptar norma, edición, jurisdicción, vía, transductor, bandas y escenario de prueba.
3. La absorción atmosférica cuantitativa por bandas requiere una fuente primaria y condiciones ambientales completas.
4. La conversión modal y la relación de Snell se mantienen cualitativas donde las fuentes locales no justifican un desarrollo matemático adicional.
5. La política global de OMML frente a texto matemático editable y el color canónico de títulos siguen siendo decisiones de sistema, no defectos locales de U9.

No hay limitaciones críticas ni mayores abiertas.

## Recomendaciones para dictar la clase

- Dividir la ruta central en tres encuentros y reservar las slides 78–84 para integración y transferencia.
- Abrir cada encuentro con el caso o la pregunta del divisor y recuperar hipótesis antes de revelar el modelo.
- No leer los diagramas completos: seguir una ruta, identificar el mecanismo y recién después señalar la ecuación o conclusión.
- En los ejercicios, pedir siempre magnitud, unidad, hipótesis y alcance de la respuesta.
- Usar la slide 55 con o sin audio; si se incorpora `U09-MEDIA-001`, anticipar la consigna antes de reproducirlo.
- Tratar las slides 85–96 como material a demanda, diagnóstico, discusión o cierre, no como continuación obligatoria de la exposición.
- En cabinas, insistir en que absorción interior, aislamiento y aptitud audiométrica son decisiones diferentes.

## Dictamen

**Unidad cerrada y apta para dictado.** Cobertura completa, 0 problemas críticos, 0 problemas mayores y una incidencia menor opcional documentada.
