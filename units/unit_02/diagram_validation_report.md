# Unidad 2 — Informe de validación de diagramas

## Resultado

**Estado general: 73/73 variantes aprobadas.**

Se validaron las 15 familias U02-DG001–U02-DG015 y todas sus variantes por slide. La salida final no contiene problemas críticos ni mayores.

## Clasificación previa

| clasificación | cantidad |
|---|---:|
| diagrama conceptual | 24 |
| diagrama de proceso | 13 |
| ecuación anotada | 17 |
| esquema mixto | 19 |
| **Total** | **73** |

## Ciclo de aceptación

| iteración global | aprobadas | retenidas | corrección principal |
|---:|---:|---:|---|
| 1 | 21 | 52 | Detectar padding insuficiente y conectores que atravesaban nodos. |
| 2 | 40 | 33 | Preservar saltos de línea, redistribuir procesos de cinco o seis pasos y corregir sistemas anidados. |
| 3 | 50 | 23 | Acortar rótulos y aumentar el wrap sin reducir tipografía. |
| 4 | 71 | 2 | Usar el canvas físico completo y recuperar 0,18 in de padding real. |
| 5 | 73 | 0 | Corregir los dos rótulos largos restantes. |
| 6 | 73 | 0 | Revisión visual final: corregir U02-066 y reemplazar esquemas demasiado genéricos. |

## Gates automáticos finales

| gate | resultado |
|---|---|
| SVG parseable | 73/73. |
| PNG individual | 73/73 a 2400 × 1100 px. |
| Render en slide real | 73/73 a 2400 × 1350 px. |
| Texto principal | 22 pt o más en 73/73. |
| Etiqueta de conector | 20 pt o más en 73/73. |
| Ecuación central | 36 pt en las 17 ecuaciones anotadas. |
| Padding interno | 0,18 in o más en todos los nodos textuales. |
| Desbordes o clipping | 0. |
| Conectores sobre texto o nodos no relacionados | 0. |
| Etiquetas apoyadas sobre líneas | 0. |
| Flechas a destino incorrecto | 0. |
| Objetos fuera del canvas | 0. |
| Wrappers individuales | 73/73 ejecutados sin error. |

Los resultados por recurso están en cada `validation.json`; el consolidado está en `assets/generated/_review/u02_diagrams_generation_report.json`.

## Revisión a tamaño de slide

Se generó `slide_context.png` para cada recurso con el sistema visual 16:9 y el título real del storyboard. Se revisaron las siete hojas de contacto:

- `u02_diagrams_contact_sheet_01.png`;
- `u02_diagrams_contact_sheet_02.png`;
- `u02_diagrams_contact_sheet_03.png`;
- `u02_diagrams_contact_sheet_04.png`;
- `u02_diagrams_contact_sheet_05.png`;
- `u02_diagrams_contact_sheet_06.png`;
- `u02_diagrams_contact_sheet_07.png`.

Hallazgos corregidos durante la revisión:

| id | severidad | hallazgo | corrección | estado |
|---|---|---|---|---|
| DV-001 | Mayor | Los procesos de cinco o seis nodos comprimían texto y corredores. | Se convirtieron en recorridos de dos filas con orden numerado. | Cerrado. |
| DV-002 | Mayor | U02-008 superponía el texto de la frontera con los elementos internos. | La frontera pasó a ser un contorno sin texto central y recibió rótulo externo. | Cerrado. |
| DV-003 | Mayor | U02-019/U02-044/U02-096 usaban un bloque textual como sustituto del DCL. | Se dibujaron cuerpo, eje y fuerzas en corredores separados. | Cerrado. |
| DV-004 | Mayor | U02-066 superponía las cifras de `Q` y `W_sobre` con rótulos de transferencia. | Se creó un modo de cálculo sin rótulos redundantes y se regeneró. | Cerrado. |
| DV-005 | Mayor | U02-039, U02-045, U02-046, U02-057 y U02-092 eran demasiado genéricos. | Se reemplazaron por comparaciones, rutas o recapitulaciones específicas. | Cerrado. |
| DV-006 | Menor | Algunos títulos heredaban backticks del storyboard. | El render de contexto elimina marcas Markdown. | Cerrado. |

## Editabilidad

Cada paquete conserva:

- SVG con texto y formas vectoriales;
- `source.json` con canvas, bounding boxes, IDs, texto, tamaños y conectores;
- script reproducible;
- lista estable de objetos con patrón `U02_DGxxx_Sxxx_*`.

No se generó un PowerPoint, conforme a la instrucción de no construir todavía la presentación. Las formas nativas y los conectores anclados de PowerPoint se ensamblarán en la fase de montaje usando SVG y JSON como especificación.

## Problemas abiertos

No quedan problemas críticos ni mayores en los assets. Queda fuera de esta tarea comprobar animaciones o la editabilidad nativa dentro de PowerPoint.

