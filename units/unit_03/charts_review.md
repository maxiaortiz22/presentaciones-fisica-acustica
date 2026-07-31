# Unidad 3 — Revisión de gráficos propios

## Resultado

**Aprobado.** Se implementaron 13 familias y 23 variantes, todas clasificadas antes de generarse como **gráfico cuantitativo**. No quedan problemas críticos ni mayores.

## Entregables comprobados

Cada familia contiene:

- script reproducible;
- `data.csv`;
- SVG vectorial;
- PNG de alta resolución;
- `README.md`;
- caption sugerido;
- texto alternativo;
- `source.txt`;
- metadatos y validación;
- render `slide_context.png` a 2400 × 1350 px.

## Revisión por familia

| ID | modelo o fuente | escala y unidades | variantes | resultado |
|---|---|---|---:|---|
| U03-CH001 | `cos(2πft)` | lineal; s y ms | 3 | approved |
| U03-CH002 | ejemplo del libro: 10 µm, 500 Hz | lineal; ms y µm | 1 | approved |
| U03-CH003 | MAS exacto normalizado | lineal; `t/T` y variables normalizadas | 2 | approved |
| U03-CH004 | sinusoides didácticas independientes | lineal; µm, Pa y V en ejes separados | 1 | approved |
| U03-CH005 | tono sintético de 500 Hz con rampas cosenoidales | lineal; s y detalle en ms | 1 | approved |
| U03-CH006 | presión hipotética de 0,20 Pa pico | lineal; ms y Pa | 1 | approved |
| U03-CH007 | onda viajera exacta, `c=340 m/s` | lineal; m, ms y `ξ/Aξ` | 5 | approved |
| U03-CH008 | ejercicio exacto, `f=250 Hz`, `λ=1,36 m` | lineal; ms y m | 2 | approved |
| U03-CH009 | perfiles a 250 y 500 Hz con `c` fija | lineal; m | 1 | approved |
| U03-CH010 | pares sinusoidales con `Δφ=0,π/2,π` | lineal; `t/T` | 2 | approved |
| U03-CH011 | perfil espacial a instante fijo | lineal; `x/λ` | 1 | approved |
| U03-CH012 | suma punto a punto con cinco desfases | lineal; `t/T` y amplitud normalizada | 2 | approved |
| U03-CH013 | `A_R/A=√(2+2cosΔφ)` | lineal; rad y amplitud normalizada | 1 | approved |

## Controles numéricos independientes

- U03-CH002: máximos exactos `+10 µm` y `−10 µm`.
- U03-CH003: `a/(ω²Aₓ) = −x/Aₓ`, residuo máximo `0`.
- U03-CH008: `1,36 m × 250 Hz = 340 m/s`.
- U03-CH012: residuo máximo de la suma `y_R−y₁−y₂ = 1,11×10⁻¹⁶`.
- U03-CH013: residuo máximo frente a la fórmula exacta `0`.
- Todos los modelos sintéticos están identificados como modelos; no se presentan como mediciones.

## Correcciones realizadas tras el primer render

| problema | severidad | corrección | estado |
|---|---|---|---|
| Rótulos de variables recortados en pequeños múltiples | mayor | Se llevaron dentro del área útil sin bajar de 20 pt | cerrado |
| Tono de 500 Hz aparecía como banda sólida en una ventana de 1 s | mayor | Se conservó la envolvente completa y se agregó un detalle temporal de 8 ms | cerrado |
| Bloque de parámetros en U03-CH007 tenía colisión vertical | mayor | Se redistribuyó el panel informativo | cerrado |
| Algunas anotaciones competían con curvas o puntos notables | menor | Se desplazaron y se agregó fondo blanco local | cerrado |
| Variantes obsoletas podían quedar en una regeneración | mayor | El exportador elimina solo los archivos de figura de su paquete antes de escribir | cerrado |

## Verificación visual

- Se revisaron las cinco hojas de contacto.
- Se comprobó cada paquete en su render individual y en `slide_context.png`.
- Se verificaron ejes, unidades, normalizaciones, paleta redundante, márgenes y resolución.
- Resultado final: cero problemas críticos o mayores.

Registro máquina: `assets/generated/_review/u03_charts_generation_report.json` y `u03_final_assets_audit.json`.
