# Unidad 4 — Informe de validación de diagramas

## Resultado

Las 22 familias de diagramas fueron aprobadas con cero problemas críticos y cero problemas mayores abiertos. Cada recurso fue renderizado de forma individual a 2560×1440 y también dentro del canvas real 16:9 de 1280×720 mediante una slide técnica editable.

## Gates de aceptación

| gate | resultado |
|---|---|
| Texto dentro de cada caja | aprobado |
| Texto principal ≥22 pt | aprobado; rango 22–40 pt |
| Etiquetas de conector ≥20 pt | aprobado; 21 pt |
| Ecuaciones centrales ≥28 pt | aprobado; 30–40 pt |
| Padding interno ≥0,18 in equivalente | aprobado; 18 px mínimos en canvas de 96 ppp |
| Cero conectores sobre texto | aprobado |
| Cero etiquetas apoyadas sobre líneas | aprobado |
| Puntas fuera de palabras, símbolos y ecuaciones | aprobado |
| Flechas hacia el destino correcto | aprobado |
| Cero nodos fuera del canvas | aprobado |
| Fuente editable conservada | aprobado; PowerPoint nativo por recurso |
| SVG y PNG de respaldo | aprobado |
| Render en slide real | aprobado |
| Prueba de overflow del PPTX agregado | aprobada: “No overflow detected” |

## Iteraciones registradas

1. **Composición inicial:** la estimación de texto detectó desbordes en DG-001, DG-002, DG-004, DG-005, DG-006, DG-008–010, DG-013–014, DG-017, DG-020 y DG-022. Se ampliaron cajas, se redistribuyeron líneas y se resumieron rótulos sin bajar la fuente.
2. **Primer render completo:** la inspección visual detectó etiquetas verticales atravesadas por conectores, líderes de ecuación terminando en el borde general y la palabra “interfaz” apilada de forma deficiente. Se desplazaron etiquetas, se añadieron anclas invisibles próximas a símbolos y se movió el rótulo de interfaz fuera de la barra.
3. **Control de dirección:** el exportador interpretó `head` como extremo inicial y mostró las puntas invertidas. Se cambió globalmente al extremo `tail` y se volvió a renderizar toda la biblioteca.
4. **Render final:** se inspeccionó el montaje de las 22 familias y a tamaño original DG-005, DG-006, DG-008, DG-014 y DG-019. No quedaron problemas críticos ni mayores.

## Trazabilidad

Cada carpeta contiene `validation.json`, `*.layout.json`, README, SVG, PNG y PPTX editable. El resumen automático está en `assets/generated/diagrams/validation_summary.json`; el control conjunto está en `visual_validation_summary.json`.
