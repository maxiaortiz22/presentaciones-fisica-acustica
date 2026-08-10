# Unidad 5 — Informe de validación de diagramas

Fecha de validación: 2026-07-31
Alcance: 14 familias editables; DG-011 permanece pendiente. No se construyó la presentación de la unidad.

## Resultado global

- Diagramas aprobados: **14 de 15**.
- Problemas críticos: **0**.
- Problemas mayores: **0**.
- Formato real de validación: 16:9, 13,333×7,5 pulgadas, render 2560×1440.
- Tipografía: Calibri; cuerpo de nodos 22,5 pt o mayor; títulos 24 pt o mayor; ecuaciones centrales 33 pt.
- Padding interno: 0,208 pulgadas en los nodos principales.

## Clasificación obligatoria

| Clasificación | Familias aprobadas |
|---|---|
| diagrama conceptual | DG-001, DG-006, DG-010, DG-014 |
| diagrama de proceso | DG-002, DG-004, DG-012, DG-013, DG-015 |
| ecuación anotada | DG-003, DG-009 |
| esquema mixto | DG-005, DG-007, DG-008 |

DG-011 se clasifica como **diagrama de proceso**, pero no se generó porque su contenido depende de la verificación normativa de CH-017.

## Gates aplicados

| Gate | Método | Resultado |
|---|---|---|
| texto dentro de cajas | cálculo previo, layout JSON y render | aprobado |
| fuente mínima legible | inspección de propiedades y render | aprobado |
| padding interno ≥0,18 in | validación programática; usado 0,208 in | aprobado |
| flechas sin cubrir texto | intersección con bboxes y revisión visual | aprobado |
| puntas fuera de áreas tipográficas | conectores anclados a bordes | aprobado |
| etiquetas separadas del conector | relaciones trasladadas a nodos/metadata cuando era necesario | aprobado |
| objetos dentro del canvas | validación de límites 1280×720 | aprobado |
| editabilidad | apertura estructural del PPTX y fuentes JSON | aprobado |
| respaldo estático | SVG parseable y PNG 2560×1440 | aprobado |
| IDs de objetos | unicidad y presencia en `diagram_source.json` | aprobado |

## Ciclo de aceptación

1. La prevalidación geométrica detectó cajas con texto insuficientemente holgado.
2. El primer render mostró wrapping no deseado, sentido incorrecto de algunas puntas y etiquetas demasiado próximas a conectores.
3. Se redistribuyeron DG-002, DG-004, DG-012 y DG-014 en dos filas; se ampliaron nodos en DG-007, DG-008, DG-010, DG-013 y DG-015; se acortaron títulos en DG-005 y DG-009.
4. Se anclaron los conectores a los bordes y se retiraron rótulos superpuestos, conservando su semántica en los nodos y en `diagram_source.json`.
5. Se renderizó nuevamente cada familia y se repitieron controles geométricos y visuales hasta obtener cero problemas críticos o mayores.

## Inventario geométrico final

| ID | Objetos | Conectores | Estado |
|---|---:|---:|---|
| DG-001 | 4 | 3 | aprobado |
| DG-002 | 5 | 4 | aprobado |
| DG-003 | 8 | 4 | aprobado |
| DG-004 | 6 | 5 | aprobado |
| DG-005 | 5 | 4 | aprobado |
| DG-006 | 3 | 2 | aprobado |
| DG-007 | 7 | 5 | aprobado |
| DG-008 | 6 | 2 | aprobado |
| DG-009 | 4 | 2 | aprobado |
| DG-010 | 7 | 6 | aprobado |
| DG-012 | 6 | 5 | aprobado |
| DG-013 | 5 | 6 | aprobado |
| DG-014 | 5 | 0 | aprobado |
| DG-015 | 4 | 3 | aprobado |

La familia DG-011 queda `pending_standard_check`: no existe un sustituto visual aprobado hasta verificar IEC 61672-1 y generar CH-017.

## Conclusión

Los 14 diagramas renderizados cumplen los gates de legibilidad, padding, conectores, editabilidad y respaldo estático. El resumen machine-readable se conserva en `assets/generated/asset_validation_summary.json` y cada carpeta contiene su propia validación.
