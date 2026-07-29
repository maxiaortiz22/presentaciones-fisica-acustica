# Change log — reparación de diagramas de Unidad 1

## 2026-07-29 — v02 diagram fix

### Presentación

- Se tomó como fuente vigente `output/unidad_01_nociones_basicas_final.pptx`.
- Se creó el respaldo exacto `output/unidad_01_nociones_basicas_final_backup_before_diagram_fix.pptx`.
- Se generó `output/unidad_01_nociones_basicas_v02_diagram_fix.pptx` sin sobrescribir el original.

### Diagramas estructurales

- Se reemplazaron 65 usos rasterizados por formas, textos, tablas, líneas y conectores editables.
- Se corrigieron sentidos de flechas, corredores, etiquetas, padding, tamaño de cajas y jerarquía tipográfica.
- Se nombraron los objetos con prefijos `U01-CHxxx` para facilitar su trazabilidad.
- El objeto auxiliar oculto de U01-CH008 en la slide 29 se preservó.

### Gráficos y animación

- Se regeneraron U01-CH015, U01-CH019, U01-CH020, U01-CH021, U01-CH022 y U01-CH026 en SVG y PNG al tamaño final.
- Se regeneró U01-CH002 como GIF y alternativa estática.
- Se agregó `scripts/u01_regenerate_quantitative_diagrams.py`.
- Se agregó `scripts/u01_repair_diagrams_native.mjs`.
- Los nuevos archivos fuente quedaron en `assets/generated/diagram_fix/`.

### Revisión

- Se renderizaron las 94 slides antes y después.
- Se guardaron previews y mosaicos en `output/diagram_repair_review/`.
- Se verificó que las 22 slides fuera del alcance fueran idénticas a nivel de render.
- Se preservaron 94 notas, 2 masters, 27 layouts, 2 relaciones externas y 1 GIF.
- Resultado final: sin problemas críticos ni mayores.
