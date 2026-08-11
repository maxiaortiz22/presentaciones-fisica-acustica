# Unidad 6 — Informe de validación de diagramas

Fecha de validación: 2026-08-10  
Estado global: **aprobado**  
Alcance: 53 diagramas y variantes aprobados en `diagram_plan.md`, renderizados individualmente y verificados en composición 16:9.

## Clasificación final

| Clasificación obligatoria | Cantidad |
|---|---:|
| Diagrama conceptual | 21 |
| Diagrama de proceso | 19 |
| Ecuación anotada | 5 |
| Esquema mixto | 8 |
| **Total** | **53** |

## Ciclo de aceptación aplicado

1. Se generó una fuente editable de una diapositiva por recurso.
2. Se ejecutó preflight geométrico y tipográfico.
3. Se exportaron PNG y SVG individuales.
4. Se inspeccionaron los diagramas a tamaño final y en montajes comparativos.
5. Se corrigieron ajuste de texto, separación de cajas, ruteo y orientación de puntas.
6. Se volvió a generar y renderizar el conjunto completo.
7. El validador consolidado comprobó estructura, dimensiones, archivos y manifiesto.

## Criterios verificados

| Control | Resultado |
|---|---|
| Texto fuera de cajas o recortado | 0 incidencias |
| Conectores sobre texto | 0 incidencias |
| Puntas de flecha sobre palabras, símbolos o ecuaciones | 0 incidencias |
| Etiquetas apoyadas sobre conectores | 0 incidencias |
| Objetos fuera del canvas | 0 incidencias |
| Padding interno | 0,208 in; supera el mínimo de 0,18 in |
| Texto principal | 22,5 pt |
| Títulos de nodos | 24 pt |
| Etiquetas de conectores | 20,25 pt |
| Ecuaciones centrales | 34,5 pt |
| Render individual | realizado en 53/53 recursos |
| Verificación a tamaño de slide | realizada en 53/53 recursos |

Los diagramas son esquemáticos y declaran `not_to_scale: true`; no expresan proporciones anatómicas ni magnitudes cuantitativas salvo las ecuaciones explícitamente rotuladas.

## Correcciones derivadas de la revisión

- Se amplió el ajuste manual de texto para evitar saltos de línea imprevistos en la exportación.
- Se redistribuyeron nodos y corredores en bifurcaciones, bucles y comparaciones de dos rutas.
- Se corrigió la orientación efectiva de las puntas de flecha del exportador y se regeneró todo el conjunto.
- Se simplificaron rótulos extensos sin bajar el cuerpo por debajo del mínimo legible.
- Se revisaron de forma reforzada U06-DG-012, 017, 025, 044, 046, 054, 058B y 060 por su densidad o ruteo.

## Resultado y pendientes

Problemas críticos: **0**  
Problemas mayores: **0**  
Diagramas aprobados: **53 de 53 implementados**

No se generaron familias que siguen pendientes por anatomía, notación, terminología, fotografía propia, validación docente o fuente. Las variantes U06-DG-053B y U06-DG-054B conservan `detail_pending`; se aprobaron únicamente sus maestros U06-DG-053 y U06-DG-054.

Cada carpeta contiene su `validation.json`; el control consolidado está en `assets/generated/asset_validation_summary.json`.
