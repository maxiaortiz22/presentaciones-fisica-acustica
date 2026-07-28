# Estado inicial del proyecto

Fecha de auditoría: 28 de julio de 2026.

## Estado general

**Estado: fuentes académicas sustancialmente disponibles, infraestructura pedagógica y de producción aún sin iniciar.**

El repositorio ya tiene la estructura base completa, las ocho skills locales, el programa, el libro PDF, los capítulos LaTeX de las diez unidades y dos presentaciones de referencia. Las carpetas `style/`, `scripts/`, `output/` y `units/unit_01/` a `units/unit_10/` están vacías. Por lo tanto, el proyecto está preparado para comenzar la fase de arquitectura, pero todavía no cumple ningún entregable de unidad.

No se creó el mapa del curso, el template, la guía de estilo ni ninguna presentación.

## Fuentes disponibles

| Fuente | Estado | Valor para el proyecto |
|---|---|---|
| Programa oficial 2025 | Disponible | Define objetivos, evaluación, bibliografía y alcance de las diez unidades. |
| Libro completo 2026 | Disponible | PDF de 296 páginas que sigue las diez unidades e incluye explicaciones, ejercicios, respuestas y glosarios. |
| Fuente LaTeX completa | Disponible, pendiente de compilación de control | `main.tex`, introducción, diez capítulos editables, bibliografía, figuras y scripts. |
| Bibliografía | Disponible | 56 entradas BibTeX; no se detectaron claves citadas faltantes. |
| Figuras TikZ | Disponibles | 56 figuras editables, todas referenciadas y presentes. |
| Figuras generadas | Disponibles | Ocho PDF reproducibles para U5 y U10, con dos scripts Python. |
| PowerPoint original de U1 | Disponible | Referencia visual primaria, 20 slides 16:9, mayormente editable. |
| Deck de Gemini | Disponible con limitaciones | Referencia visual secundaria de 15 slides, completamente aplanada como imágenes. |
| Ejercicios y respuestas | Disponibles dentro del libro | Todas las unidades tienen ejercicios y soluciones o respuestas orientativas. |
| Skills del proyecto | Disponibles | Arquitectura, estilo, storyboard, assets, gráficos, redacción, revisión y consistencia. |

## Fuentes faltantes

1. **Programa vigente confirmado.** Solo hay un programa 2025, mientras el libro está fechado 2026.
2. **Guía de ejercicios independiente.** El programa anuncia una guía, pero no está en el repositorio; los ejercicios del libro no necesariamente la sustituyen.
3. **Evaluaciones y criterios operativos.** No hay parciales, recuperatorios, rúbricas, banco de preguntas ni ejemplos de evaluación.
4. **Material adicional de la plataforma.** No hay videos, audios, documentos complementarios ni demostraciones de clase.
5. **Fuentes institucionales.** No se localizaron identidad visual UCASAL, logotipos autorizados, manual de marca ni plantilla institucional independiente.
6. **Procedencia y licencia de imágenes heredadas.** Las 28 imágenes raster no usadas carecen de manifiesto.
7. **Feedback docente previo.** No hay comentarios, registro de decisiones ni revisión de la Unidad 1 original.
8. **Condiciones de cursado.** No están documentados duración de las clases, cantidad de encuentros por unidad, modalidad, equipamiento de aula ni disponibilidad sin conexión.
9. **Requisitos de accesibilidad y distribución.** No hay decisión sobre subtitulado, texto alternativo, exportación a PDF, compatibilidad de PowerPoint o publicación en plataforma.

## Hallazgos técnicos

- Todas las carpetas requeridas existen; no se creó ninguna.
- El repositorio contenía 122 archivos antes de estos dos informes.
- No se detectaron duplicados binarios exactos.
- `main.tex` está disponible e incorpora la introducción, las diez unidades y la bibliografía en el orden esperado.
- Todas las 64 figuras actualmente referenciadas por los capítulos —56 TikZ y 8 PDF— existen.
- Hay 28 imágenes raster no referenciadas por el LaTeX actual.
- Las 56 claves bibliográficas citadas están presentes y no se detectaron etiquetas LaTeX duplicadas.
- No quedan bloques `\verify{...}` activos en los capítulos.
- Persiste un `TODO` en U5 para una figura original de curvas A, C y Z.
- U7 mantiene un comentario de nueve figuras pendientes de diseño y aprobación, aunque las nueve figuras temáticas ya existen y están insertadas.
- El `main.log` obsoleto fue eliminado por el usuario; no hay residuos de compilación en la raíz LaTeX.
- El PowerPoint original de U1 tiene 20 slides, 1 master, 11 layouts, 22 medios y ningún slide de notas.
- El deck secundario tiene una imagen a pantalla completa por slide; no permite reutilizar texto, formas ni layouts como elementos editables.

## Riesgos

| Riesgo | Severidad | Impacto probable | Mitigación recomendada |
|---|---|---|---|
| Compilación LaTeX aún no verificada | Media | Todavía no está confirmado que una compilación limpia de `main.tex` reproduzca el PDF canónico de 296 páginas. | Ejecutar una compilación de control y revisar errores, referencias, bibliografía y paginación antes de editar el libro. |
| Programa 2025 frente a libro 2026 | Alta | Puede generarse cobertura contra un alcance desactualizado. | Confirmar por escrito el programa vigente antes de crear el mapa curricular. |
| Ausencia de guía y evaluaciones | Alta | Los storyboards pueden no preparar adecuadamente la práctica y la evaluación real. | Incorporar guía, parciales o al menos una matriz de competencias evaluadas. |
| Raster sin procedencia | Alta | Riesgo de licencia, atribución, baja calidad o error técnico. | Mantenerlos como no aprobados hasta documentar origen y licencia. |
| Figuras U7 con estado contradictorio | Alta | Una visualización conceptual puede presentarse como validada sin estarlo. | Resolver explícitamente estado, fuente de datos y aprobación antes de usarlas en slides. |
| Curvas A/C/Z pendientes | Alta | U5 puede quedar incompleta o apoyarse en una imagen no trazable. | Crear o validar una figura normativa con fuente y condiciones declaradas. |
| Deck Gemini aplanado | Media | No sirve como plantilla editable ni conserva jerarquía de masters/layouts. | Usarlo solo como referencia de composición secundaria. |
| U1 sin notas ni fuentes | Media | No documenta el desarrollo oral ni la procedencia de sus imágenes. | Tratarla como referencia visual, no como unidad terminada según `AGENTS.md`. |
| Carpetas de unidad vacías | Media | No hay briefs, storyboards, manifests ni historial de decisiones. | Iniciar cada unidad solo después de arquitectura y estilo. |
| Falta de parámetros de cursado | Media | Puede sobredimensionarse o subdimensionarse cada deck. | Registrar duración, modalidad, recursos de aula y tiempo disponible. |
| Títulos ampliados en U6 y U8 | Baja | Posible diferencia de alcance o terminología entre programa y libro. | Documentar la equivalencia o diferencia en la futura matriz de cobertura. |
| Nombres raster genéricos | Baja | Dificultan trazabilidad y asignación a slides. | Renombrar solo después de aprobar y registrar cada recurso; no hacerlo durante esta auditoría. |

## Decisiones pendientes

1. Confirmar si el programa 2025 sigue siendo el programa oficial vigente.
2. Confirmar mediante una compilación limpia que `main.tex` produce correctamente el libro y decidir cuál es el PDF canónico.
3. Aclarar si el PDF de 296 páginas es la versión definitiva que debe usarse para paginación y citas.
4. Confirmar si existe una guía de ejercicios externa y si sus problemas deben aparecer en los decks.
5. Incorporar parciales, recuperatorios o una descripción más precisa de las competencias evaluadas.
6. Definir duración y cantidad de clases destinadas a cada unidad.
7. Confirmar disponibilidad de audios, videos, instrumentos, parlantes, sonómetro, material anatómico y conexión a internet.
8. Decidir el estado de las nueve figuras de U7.
9. Resolver la visualización de curvas A, C y Z de U5 con una fuente normativa verificable.
10. Identificar origen, licencia y estado de las 28 imágenes raster heredadas.
11. Confirmar si existe manual de marca o plantilla institucional UCASAL.
12. Definir si la Unidad 1 original debe conservarse intacta como baseline o si luego se hará una versión revisada.
13. Definir requisitos de accesibilidad, distribución y compatibilidad de PowerPoint.

## Información necesaria para desarrollar correctamente las diez unidades

Antes de producir storyboards o decks conviene contar, como mínimo, con:

- programa vigente confirmado;
- libro fuente compilable y versión PDF canónica;
- duración y modalidad de cada clase;
- calendario o distribución tentativa de unidades;
- guía de ejercicios y evaluaciones existentes;
- feedback docente sobre la Unidad 1 original;
- recursos técnicos disponibles en aula;
- identidad institucional autorizada;
- política de uso de imágenes, videos y audio;
- requisitos de accesibilidad y formatos de entrega;
- criterio de aprobación de figuras conceptuales y normativas;
- responsable de validar contenido clínico, normativo y pedagógico.

## Próximos pasos recomendados

1. **Cerrar los faltantes críticos:** programa vigente, guía de ejercicios, evaluaciones y parámetros de cursado.
2. **Verificar la fuente LaTeX:** compilar `main.tex`, revisar el resultado y declarar qué PDF del libro es canónico.
3. **Curar los recursos existentes:** clasificar las 28 imágenes raster como aprobadas, reemplazadas o rechazadas y documentar procedencia/licencia.
4. **Resolver pendientes técnicos:** figuras U7 y curvas A/C/Z de U5.
5. **Ejecutar `course-architecture`:** solo después de confirmar programa y versión del libro, para producir mapa, dependencias y matriz de cobertura.
6. **Ejecutar `style-system`:** auditar en detalle el PowerPoint original de U1, la identidad institucional disponible y el deck secundario.
7. **Iniciar U1 con `unit-storyboard`:** crear brief y storyboard antes de redactar o producir slides.
8. **Continuar el flujo obligatorio por unidad:** assets/gráficos, redacción, PowerPoint, render, revisión y consistencia.

## Cambios realizados durante esta auditoría

- Creado `project_inventory.md`.
- Creado `project_status.md`.
- Incorporado al inventario el `main.tex` copiado por el usuario.
- Registrada la eliminación, realizada por el usuario, del `main.log` obsoleto.
- No se crearon carpetas porque todas las requeridas ya existían.
- El agente no movió, renombró, editó ni eliminó archivos fuente preexistentes.
- No se creó mapa de curso, template, guía de estilo ni presentación.
