# Unidad 2 — Necesidades iniciales de assets

## Alcance de este documento

Este inventario identifica recursos visuales y multimedia que deberán producirse o curarse después del storyboard. No es todavía un manifiesto de assets: no se descargaron archivos, no se eligieron URLs definitivas y no se asignaron licencias.

Se distinguen tres familias:

1. recursos internos del libro que conviene reconstruir;
2. imágenes técnicas externas que requieren curación y trazabilidad;
3. demostraciones o animaciones que conviene producir como recursos propios.

Los gráficos cuantitativos se registran en `initial_chart_needs.md` y los diagramas editables en `initial_diagram_needs.md`.

## Recursos internos disponibles

| asset_id | slides previstas | recurso de origen | uso pedagógico | tratamiento requerido | prioridad | estado |
|---|---|---|---|---|---|---|
| U02-INT-001 | U02-027–032 | Figura 2.1: diferencia de presión y fuerza sobre una superficie | Mostrar cómo una diferencia de presión produce una fuerza neta | Reconstruir como formas y flechas editables; adaptar área `A` del libro a `S` para continuidad con U1; preparar etapas de revelado | alta | identificado |
| U02-INT-002 | U02-035–046 | Figura 2.2: masa–resorte–amortiguador | Construir el modelo mecánico por capas | Redibujar en tamaño final; separar masa, resorte y amortiguador antes de mostrar el sistema completo | alta | identificado |
| U02-INT-003 | U02-079–082 | Figura 2.3: velocidad del sonido frente a temperatura | Leer tendencia, pendiente y límites de una aproximación | Regenerar como gráfico reproducible; no reutilizar la figura rasterizada | alta | identificado |
| U02-INT-004 | U02-054–057 y U02-086–089 | Figura 2.4: ruta cualitativa de energía | Distinguir transferencia, almacenamiento y disipación | Reconstruir como diagrama editable sin sugerir proporciones cuantitativas | alta | identificado |

## Imágenes técnicas externas por curar

| asset_id | slides previstas | tipo | necesidad visual | función pedagógica | perfil de fuente preferido | requisitos de selección | alternativa sin asset | prioridad | estado |
|---|---|---|---|---|---|---|---|---|---|
| U02-AST-001 | U02-085 | ilustración anatómica técnica | Membrana timpánica y estructuras vecinas en una vista simple | Vincular el modelo de superficie flexible con una estructura real y declarar sus límites | atlas universitario, publicación científica o material institucional de salud | anatomía clara, rótulos verificables, licencia registrable, sin detalle clínico innecesario | esquema propio simplificado y rotulado como modelo | alta | pendiente de `asset-curation` |
| U02-AST-002 | U02-086 | ilustración técnica | Oído medio con membrana, cadena osicular y entrada/salida energética | Explicar que un sistema pasivo transforma variables sin crear energía | universidad, publicación científica o fabricante de equipamiento docente | permitir lectura en aula, evitar atribuir porcentajes no documentados, créditos y alt text | diagrama conceptual propio sin anatomía detallada | alta | pendiente de `asset-curation` |
| U02-AST-003 | U02-087 | fotografía técnica | Vibrador óseo y zona de contacto | Dar un referente concreto para tercera ley y fuerza de contacto | fabricante técnico, universidad o publicación clínica con uso permitido | dispositivo identificable, punto de contacto visible, sin uso publicitario, licencia registrable | dibujo técnico propio del contacto entre dos cuerpos | media | pendiente de `asset-curation` |
| U02-AST-004 | U02-085 | micrografía o ilustración técnica opcional | Tejido o material viscoelástico | Mostrar por qué un modelo lineal concentrado no es una anatomía literal | publicación científica o universidad | debe aportar información material, no ser decorativa; pie que declare escala y alcance | omitir y usar comparación esquemática | baja | pendiente de decisión |

## Recursos multimedia y demostraciones propias

| media_id | slides previstas | formato preferido | contenido | propósito | versión estática obligatoria | condiciones de uso | prioridad | estado |
|---|---|---|---|---|---|---|---|---|
| U02-MED-001 | antes o durante U02-002 | demostración en vivo o clip propio breve | Superficie flexible con presiones comparables a ambos lados y perturbación cualitativa | Abrir la unidad con un fenómeno que requiera fuerza neta, respuesta y energía | secuencia de tres estados: equilibrio, diferencia de presión, respuesta | no cuantificar si el montaje no está calibrado; declarar carácter cualitativo | alta | guion pendiente |
| U02-MED-002 | U02-034 | clip propio o GIF | Masa–resorte con menor y mayor amortiguamiento | Motivar los tres mecanismos antes de introducir la ecuación | dos secuencias de posiciones en paralelo | mismo encuadre y escala temporal; evitar que el cambio de masa sea una variable oculta | alta | guion pendiente |
| U02-MED-003 | U02-069 | GIF o animación simple | Oscilación amortiguada con ruta de energía asociada | Conectar disminución de amplitud con conversión de energía mecánica en interna | tres fotogramas con barras cualitativas no proporcionales | sin ejes ni cifras si no se genera un modelo cuantitativo; rotular “esquema” | media | concepto pendiente |
| U02-MED-004 | U02-077 | animación propia | Compresiones y rarefacciones locales con una partícula marcada y la perturbación avanzando | Preparar U3 y separar movimiento local de propagación | diagrama estático con dos instantes | no desarrollar todavía parámetros ondulatorios ni resonancia | alta | concepto pendiente |

No se propone video externo como requisito. Si la producción propia no es viable, la búsqueda posterior deberá priorizar material universitario o científico y conservar una alternativa estática equivalente.

## Requisitos de producción y curación

- Registrar en el manifiesto posterior: identificador, autor u organización, URL, licencia conocida, fecha de acceso, propósito, slide prevista y estado.
- Evitar imágenes de stock, ilustraciones médicas sin procedencia y fotografías meramente decorativas.
- No usar imágenes generadas por IA para sustituir anatomía o dispositivos técnicos verificables.
- Preparar texto alternativo para cada imagen o recurso multimedia.
- Mantener el recorte sin deformación y comprobar legibilidad en el tamaño real de la slide.
- No repetir la misma imagen externa en slides diferentes; si un concepto reaparece, usar un detalle, un diagrama propio o una vista distinta.
- Toda animación debe tener un estado final estático que conserve el significado si no se reproduce.
- No atribuir valores anatómicos, clínicos o de rendimiento a imágenes que solo funcionen como referencia visual.

## Carga inicial de assets

| familia | cantidad prevista | observación |
|---|---:|---|
| Recursos internos a reconstruir | 4 | Dos se convierten en diagramas, uno en gráfico y uno en ruta conceptual. |
| Imágenes externas prioritarias | 3 | Membrana, oído medio y vibrador óseo. |
| Imagen externa opcional | 1 | Tejido o material viscoelástico. |
| Multimedia o demostraciones propias | 4 | Dos pueden resolverse como demostración en vivo más versión estática. |

La cantidad puede reducirse si las aplicaciones se resuelven con diagramas propios suficientemente informativos. No debe aumentarse para “decorar” la presentación.
