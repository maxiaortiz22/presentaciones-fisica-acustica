# Unidad 7 — Revisión de gráficos propios

Fecha de cierre: 2026-08-11. Estado: **aprobado como assets v01**.

## Alcance y clasificación

Se implementaron **9 gráficos cuantitativos**: U07-CH-001, U07-CH-002A, U07-CH-002B, U07-CH-003, U07-CH-005, U07-CH-006, U07-CH-007, U07-CH-008 y U07-CH-009. Cada carpeta conserva script reproducible, CSV, parámetros JSON, SVG, PNG 2560×1440, preview a tamaño de slide, README, caption, texto alternativo, fuente/modelo y validación.

U07-CH-004 continúa bloqueado porque requiere datos normativos ISO con licencia y trazabilidad resueltas; se produjo U07-DG-011 como alternativa conceptual. U07-CH-010 continúa bloqueado hasta aprobar una voz/corpus y el pipeline de audio.

## Verificación cuantitativa

- U07-CH-001: función monótona, `P(L50)=0.5` y rango 0–1.
- U07-CH-002A/B: curvas conceptuales acotadas y versión B con barras de error explícitas; no se presentan como datos humanos.
- U07-CH-003: ejemplo sintético con normalización y escala declaradas.
- U07-CH-005: armónicos separados 200 Hz; la ausencia física de f₀ se marca sin inferir datos perceptuales.
- U07-CH-006: relación introductoria 40/50/60/70/80 fon → 1/2/4/8/16 sones verificada.
- U07-CH-007: función de polaridad conceptual y variante de ejercicio conservadas.
- U07-CH-008: igualdad de área del rectángulo equivalente verificada dentro de la tolerancia numérica registrada.
- U07-CH-009: pendiente −60/T₆₀ y variante T₃₀ verificadas; el piso de ruido es conceptual.

## Revisión visual

Todos los PNG miden 2560×1440, los SVG son parseables, los ejes incluyen magnitud y unidad, y las escalas lineales/logarítmicas se declaran en cada README. Las figuras sintéticas se rotulan como modelos didácticos/no normativos. Se corrigieron en iteración visual la separación entre caption y eje en U07-CH-005 y el anclaje de la anotación de 80 fon en U07-CH-006.

Resultado final: **0 problemas críticos y 0 problemas mayores**.
