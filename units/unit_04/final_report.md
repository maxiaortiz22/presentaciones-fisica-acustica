# Informe final — Unidad 4

**Unidad:** Generalidades sobre el sonido, sus propiedades y magnitudes  
**Versión final:** `output/unidad_04_sonido_magnitudes_final.pptx`  
**PDF de revisión:** `output/unidad_04_sonido_magnitudes_final_review.pdf`  
**Render:** `output/render_final/`  
**Fecha de cierre:** 2026-07-31

## Estado de cierre

La Unidad 4 cumple la definición de terminado de `AGENTS.md`. Existen todos los artefactos obligatorios, la presentación final fue renderizada por completo y no quedan problemas críticos ni problemas mayores sin resolver o aceptar explícitamente.

| Requisito | Estado | Evidencia |
|---|---|---|
| `brief.md` | completo | Alcance, objetivos, prerrequisitos, riesgos y ruta docente. |
| `storyboard.md` | completo y actualizado | 125 slides, 13 bloques, rutas central/complementaria/respaldo y duración real. |
| `slide_text.md` | completo y actualizado | Copy visible, ecuaciones, ejemplos, captions, fuentes y alt text de 125 slides. |
| `speaker_notes.md` | completo y actualizado | 125 notas con propósito, explicación, pregunta, respuesta, transición y fuente. |
| `asset_manifest.csv` | completo | 48 IDs únicos; 38 assets aprobados con archivo local existente. |
| scripts | organizado | 22 scripts principales y subcarpetas de producción reproducible. |
| gráficos | aprobado | 14 familias propias aprobadas; una familia polar permanece pendiente como ampliación. |
| diagramas | aprobado | 22 familias propias: 19 diagramas y 3 familias de ecuación anotada, con fuentes editables. |
| PowerPoint | final | 125 slides, 2 masters, 27 layouts, notas y accesibilidad. |
| PDF | final | 125 páginas. |
| render | final | 125 PNG y hoja de contacto. |
| `review.md` | actualizado | 0 críticos y 0 mayores no resueltos/no aceptados. |
| revisión pedagógica independiente | completa | Hallazgos reabiertos y tratados en el cierre final. |
| revisión de consistencia | actualizada | Convenciones locales resueltas; diferencias pedagógicas justificadas preservadas. |

## Métricas de la presentación

- **Cantidad total:** 125 slides.
- **Bloques:** 13, desde B00 Apertura hasta B12 Respaldo.
- **Ruta central:** 91 slides, 347 minutos estimados.
- **Slides complementarias:** 18, 78 minutos estimados.
- **Slides de respaldo:** 16, hasta 76 minutos a demanda.
- **Duración expandida máxima:** aproximadamente 501 minutos.
- **Distribución recomendada:** cuatro encuentros centrales de aproximadamente 98, 84, 76 y 89 minutos.

## Temas cubiertos

La presentación cubre el alcance completo del programa y del capítulo 4:

1. sentido físico y perceptual del sonido;
2. generación sonora en voz, parlantes, cuerdas, columnas de aire y turbulencia;
3. papel de elasticidad, inercia, densidad y rapidez de propagación;
4. campo acústico, presión acústica y velocidad de partícula;
5. impedancia característica, interfaz y reflexión;
6. intensidad instantánea y media;
7. potencia y energía acústicas;
8. valores instantáneo, pico, pico a pico, media y RMS;
9. decibel, referencias y niveles de presión, intensidad y potencia;
10. suma coherente, fase, cancelación y suma no correlacionada;
11. frentes y modelos plano, cilíndrico y esférico;
12. campo libre, reverberante y difuso;
13. ley de distancia, directividad, `Q_dir` e índice `DI`;
14. medición con micrófono/sonómetro, errores frecuentes y caso integrador.

Los 22 temas obligatorios desagregados en `source_map.md` están presentes.

## Recursos visuales y multimedia

### Gráficos propios

- 14 familias cuantitativas aprobadas, con SVG/PNG reproducibles.
- Incluyen presión y velocidad, descriptores temporales, RMS, niveles, suma de señales, geometrías, distancia y reflexión.
- `U04-CH-012` —patrones polares reales— queda pendiente porque el dataset abierto requiere una descarga masiva y validación adicional. La slide 102 usa datos didácticos explícitamente declarados y no depende de ese recurso.

### Diagramas propios

- 19 familias de diagramas y 3 familias de ecuaciones anotadas.
- Fuentes editables en PowerPoint más respaldos SVG/PNG.
- Validación geométrica previa: cero problemas críticos o mayores en cajas, conectores, flechas, etiquetas o desbordes.

### Multimedia

- No se incrustó audio ni video sin aprobación de fuente/licencia y prueba de reproducción.
- El manifiesto conserva cinco candidatos activos: un GIF preseleccionado, dos audios, un video/GIF de suma y un video de distancia.
- Todas las slides involucradas funcionan mediante alternativa estática; las etiquetas internas de producción fueron retiradas del material visible.

### Recursos externos

- Dos imágenes externas aprobadas se integran con crédito y enlace.
- Un tercer recurso externo descargado queda registrado sin incorporarse como asset aprobado.
- El paquete final conserva tres relaciones externas verificables.

## Fuentes principales

1. programa oficial de Física Acústica;
2. capítulo 4 del libro del curso en LaTeX;
3. capítulo 4 del libro en PDF, páginas 89–117;
4. Unidades 1–3 finalizadas para prerrequisitos, estilo y notación;
5. `course_map.md` y `course_dependency_map.md`;
6. glosario, guía de notación, guía visual, template y registro de decisiones;
7. fuentes externas registradas individualmente en `asset_manifest.csv` y en los bloques `[Sources]`.

## Decisiones pedagógicas finales

- La profundidad no se redujo para igualar la extensión de unidades anteriores: U4 formaliza las magnitudes acústicas que sostienen U5–U10.
- La ruta central se divide en cuatro encuentros; las complementarias y el respaldo no se proyectan automáticamente.
- RMS se anticipa operacionalmente cuando lo exige una relación energética y se construye formalmente en su bloque específico.
- Las ecuaciones centrales muestran significado, unidades y condiciones; los visuales familiares que revelaban contenido futuro fueron retirados de las slides afectadas.
- Coherencia no se identifica con fase cero: el resultado coherente depende de la fase relativa.
- El caso integrador combina distancia y suma no correlacionada con datos completos y solución numérica.
- Las siete recapitulaciones se mantienen por la densidad de la unidad; se usan como recuperación activa, no como lectura de mapas completos.
- Se adoptan `W_ac`, `K_s`, `i(t)`, `I`, `Z_0`, `Q_dir`, `R_p` y `R_I` según D-057–D-059.

## Verificación técnica final

- cobertura completa y sin contradicciones científicas detectadas;
- fórmulas, referencias y unidades verificadas;
- 125 notes slides y 125 bloques `[Sources]`;
- 75 imágenes/figuras con 75 descripciones accesibles;
- 0 placeholders locales y 0 contenido fuera de lienzo detectado en el paquete final;
- numeración continua 1–125;
- 2 masters y 27 layouts del template;
- 3 enlaces externos preservados;
- tipografías directas del sistema: Calibri, Calibri Light y Cambria Math;
- 0 comandos LaTeX, backticks, badges de producción o avisos de multimedia pendiente visibles;
- PDF y render final con 125 páginas/slides.

El verificador automatizado `slides_test.py` no pudo ejecutarse por una ruta rota del runtime local de `artifact-tool`. Esta limitación de herramienta se compensó con render completo desde PowerPoint/PDF, inspección visual de la hoja de contacto, revisión a tamaño original de las slides afectadas y auditoría directa del paquete PPTX.

## Problemas mayores: estado

Los doce problemas `major` de la revisión pedagógica independiente quedaron:

- nueve resueltos mediante cambios visibles, secuenciales o de notas;
- tres aceptados con condición explícita: extensión de la secuencia formal, notas genéricas residuales y uso docente activo de algunas recapitulaciones.

No queda ningún problema `critical` ni `major` sin tratamiento.

## Limitaciones conocidas

1. La ruta central requiere cuatro encuentros; no es una presentación para una única clase.
2. Parte de los diagramas se inserta como SVG. Los textos generales, ecuaciones nuevas, ejemplos y notas siguen editables; las fuentes editables de los diagramas se conservan en `assets/generated/diagrams/`.
3. La multimedia no está incrustada y debe aprobarse y probarse antes de usarla.
4. El patrón polar real sigue pendiente; la comparación angular final usa datos didácticos declarados.
5. El equipo del aula debe disponer de Calibri, Calibri Light y Cambria Math o comprobar sustitución/incrustación.
6. Algunas preguntas genéricas permanecen en notas de bajo riesgo; el docente debe priorizar las preguntas específicas del fenómeno.
7. La actualización de `W`/`Q` en el mapa global del curso queda para una futura ejecución de `course-architecture`; el deck visible ya usa `W_ac` y `Q_dir`.

## Recomendaciones para dictar la clase

### Encuentro 1 — B00–B03 · 98 min

- Abrir con el dato incompleto “80 dB”.
- Recuperar `c=λf`, presión, energía, fase y superposición.
- Cerrar con U04-033 antes de introducir el bloque energético.
- Tratar impedancia de manera operacional; no desarrollar números complejos.

### Encuentro 2 — B04–B06 · 84 min

- Diferenciar `i(t)`, `I`, `W_ac` y `E_ac` mediante unidades y escala espacial/temporal.
- Usar U04-038 como anticipo de RMS y volver sobre ella después de construir el descriptor.
- Hacer que el grupo calcule o estime antes de revelar ejemplos.

### Encuentro 3 — B07–B08 · 76 min

- Exigir magnitud, referencia y condición cada vez que aparezca un valor en dB.
- Comparar explícitamente coherentes en fase, coherentes con otra fase y no correlacionadas.
- Resolver U04-079 en pizarra y usar U04-080 como recuperación activa.

### Encuentro 4 — B09–B11 · 89 min

- Construir las leyes geométricas desde el crecimiento del área.
- Verificar hipótesis antes de aplicar `−6 dB` por duplicación.
- Usar U04-102 para discutir frecuencia y ángulo sin atribuir los datos a un dispositivo real.
- Dejar U04-105 como actividad y usar U04-124 para devolución posterior.

Las slides 110–125 se consultan a demanda o se distribuyen como material posterior; no deben añadirse automáticamente al cuarto encuentro.

## Integridad de los entregables

- SHA-256 PPTX: `66EFAC5FFFD2E7108E47A03E5E99D689F8A6D476A46E7800EEE6D8445EAECE99`
- SHA-256 PDF: `1E7246B01A4E992EE7E79834C45CA4CDC45C2D6205400E73D708D9B653AE3677`

Estos hashes corresponden a la versión final auditada antes de redactar este informe.

