# Unidad 9 — Revisión de assets diagramáticos

Fecha de cierre: 2026-08-12

## Inventario entregado

Cada uno de los 67 recursos aprobados incluye:

```text
U09-DG-NNN/
├── editable.pptx
├── diagram_source.json
├── figure.svg
├── figure.png
├── figure.layout.json
├── editable.pptx.inspect.ndjson
├── README.md
├── caption.txt
├── alt_text.txt
└── validation.json
```

Los archivos se encuentran en `units/unit_09/assets/generated/diagrams/`. Las seis hojas de contacto, el resumen estructural y el resumen de aprobación están en `units/unit_09/assets/generated/_review/`.

## Revisión de uso

| dimensión | decisión | estado |
|---|---|---|
| sistema visual | bordó institucional, teal físico, ocre aplicado y grises del style system | aprobado |
| legibilidad | nodos 22,5 pt o más; fórmulas 30 pt o más; títulos de nodo equivalentes a 24 pt | aprobado |
| conectores | nativos, anclados, detrás de nodos y sin rótulos sobre la línea | aprobado |
| recursos conceptuales | declaración “no está a escala” cuando corresponde | aprobado |
| accesibilidad | caption y texto alternativo separados por recurso | aprobado |
| trazabilidad | fuente conceptual, IDs de objetos y geometría conservados | aprobado |
| presentación final | no creada; sólo se produjeron fuentes editables individuales de assets | conforme al encargo |

## Decisiones de implementación

- Las familias científicas con múltiples resultados —balance de superficie, interfaz, árbol de mecanismos y rutas de cabina— usan ramas independientes para no expresar causalidades inexistentes.
- Las comparaciones sin relación causal se presentan como paneles alineados, no como flujos.
- Los recursos de actividad conservan una secuencia editable y no incorporan datos cuantitativos inventados.
- Las ecuaciones se conservan como texto matemático editable dentro del asset PPTX. La conversión a OMML queda para la fase de construcción del deck, cuando se disponga del contexto definitivo de slide; no se aplanaron como captura.
- Los PNG funcionan como previews de revisión, mientras SVG, PPTX y JSON conservan editabilidad y reproducibilidad.

## Estado por grupo

- **Aprobados:** U09-DG-001–031, U09-DG-033–047, U09-DG-049–066 y U09-DG-068–070.
- **Bloqueados:** U09-DG-032, U09-DG-048 y U09-DG-067.
- **Problemas críticos abiertos:** 0.
- **Problemas mayores abiertos:** 0.
