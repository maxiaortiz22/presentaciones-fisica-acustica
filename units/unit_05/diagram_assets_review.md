# Unidad 5 — Revisión de assets de diagramas

Fecha: 2026-07-31
Estado general: **14 familias aprobadas; 1 pendiente de norma**.

## Paquete entregado por familia

Cada carpeta aprobada en `assets/generated/diagrams/U05-DG-*` contiene:

- `u05_dg_*_master.pptx`: versión editable 16:9;
- `u05_dg_*.svg`: respaldo vectorial;
- `u05_dg_*.png`: render 2560×1440;
- `diagram_source.json`: fuente semántica editable, IDs, conectores y clasificación;
- `u05_dg_*.layout.json`: inventario geométrico del render;
- `README.md`: caption sugerido, texto alternativo, fuente conceptual y notas de uso;
- `validation.json`: resultado de los gates por familia.

## Revisión pedagógica y visual

| ID | Función | Observación de uso | Estado |
|---|---|---|---|
| DG-001 | mapa narrativo | master acumulativo; no es una miniatura del deck | aprobado |
| DG-002 | rutina de lectura | orden objeto→ejes→unidades→condiciones→pregunta | aprobado |
| DG-003 | ecuación anotada | cuatro callouts; ecuación central dominante | aprobado |
| DG-004 | cadena digital | seis etapas en recorrido de dos filas | aprobado |
| DG-005 | recorte y agrupación | distingue operaciones sin mezclar bin y banda | aprobado |
| DG-006 | señal–sistema | cadena X–H–Y y condición `X≠0` | aprobado |
| DG-007 | componentes y voz | separa armónico, parcial, sobretono y formante | aprobado |
| DG-008 | rangos condicionados | límites aproximados; no a escala perceptual | aprobado |
| DG-009 | octavas y tercios | relaciones algebraicas sin tabla normativa | aprobado |
| DG-010 | tipos de filtro | cuatro ramas con regiones de paso/rechazo | aprobado |
| DG-012 | cadena del sonómetro | distingue medición, procesamiento e informe | aprobado |
| DG-013 | decisión integradora | rutas por pregunta, evidencia y límite | aprobado |
| DG-014 | recapitulación | grilla estable reutilizable | aprobado |
| DG-015 | solución y glosario | secuencia de cuatro pasos; navegación a implementar en deck | aprobado |

## Consistencia del sistema visual

- Fondo blanco, bordo `#4D1434`, acento `#903163`, teal `#2F7E83` y texto carbón `#3D3D3D`.
- Calibri y jerarquías compatibles con la referencia académica de la Unidad 1.
- Formas planas, conectores anclados, esquinas discretas y ausencia de 3D o degradados decorativos.
- Las figuras conceptuales que no representan una escala física o perceptual lo declaran en el README y/o en la propia figura.

## Pendiente abierto

DG-011 no fue generado: la cadena A/C/Z debe esperar la validación autorizada de IEC 61672-1 y el cierre de CH-017. La omisión es deliberada y está registrada en `diagram_plan.md` y `asset_manifest.csv`.

## Cierre

Los assets aprobados están listos para una fase posterior de escritura e integración en PowerPoint. En esta tarea no se creó, editó ni ensambló el deck de la Unidad 5.
