# Unidad 7 — Informe de validación de diagramas

Fecha de cierre: 2026-08-11. Estado: **aprobado como assets v01**.

## Cobertura y clasificación obligatoria

Se validaron **55 diagramas**: 11 diagramas conceptuales, 20 diagramas de proceso, 13 ecuaciones anotadas y 11 esquemas mixtos. No se clasificó ningún diagrama como gráfico cuantitativo.

## Gates aplicados

1. Render individual y segundo render dentro del canvas real 16:9, 2560×1440.
2. Cero desbordes, clipping, objetos fuera del canvas y texto fuera de caja.
3. Cero líneas, conectores, líderes o puntas sobre texto; etiquetas separadas de los conectores.
4. Texto principal 22,5 pt; títulos de nodo 24 pt; etiquetas 20,25 pt; ecuaciones 34,5 pt.
5. Padding interno 0,208 in, superior al mínimo de 0,18 in.
6. SVG parseable, PNG no vacío, PPTX editable y ZIP/Open XML válido, layout JSON e inspección NDJSON presentes.
7. Caption, texto alternativo, fuente conceptual y declaración “no está a escala” conservados en cada README.

## Iteraciones y correcciones

La revisión consolidada detectó y corrigió reflujos de texto en U07-DG-003, 004, 017B, 022A, 022B, 028B y 033B; también se ajustaron el tamaño del bloque de ecuación, la dirección de conectores espaciales y los corredores de flechas. Los prototipos críticos U07-DG-032, 037, 039, 041 y 042 se revisaron a tamaño completo.

Resultado final: **0 problemas críticos y 0 problemas mayores** en los 55 recursos.

## Recursos no aprobados en esta tanda

- U07-DG-010: requiere la fotografía REM seleccionada y su overlay definitivo.
- U07-DG-020C: continúa pendiente de decisión sobre la fórmula ERB de Glasberg–Moore.
- U07-DG-022: es un alias de familia; las variantes efectivas aprobadas son 022A, 022B y 022C.
