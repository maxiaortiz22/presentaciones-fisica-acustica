# Unidad 1 — Revisión de gráficos, diagramas y figuras propias

## Resultado

**Estado general: aprobado para la fase de redacción y montaje.**

Se implementaron los 26 recursos U01-CH001–U01-CH026 previstos en `chart_plan.md`. Cada recurso cuenta con un paquete reproducible y no se construyó ni modificó ningún PowerPoint.

## Entorno de generación

- Fecha de ejecución y revisión: 2026-07-28.
- Python: 3.12.7, distribución Anaconda.
- NumPy: 1.26.4.
- Matplotlib: 3.9.2.
- Pillow: 10.4.0.
- SciPy y pandas no fueron necesarios: los modelos usan relaciones algebraicas exactas, arreglos pequeños y datos conceptuales declarados.
- Sistema visual aplicado: paleta bordó, teal, ocre, carbón, grises y marfil de `style/presentation_style_guide.md`.

## Inventario producido

- 26 SVG en lienzo 16:9.
- 26 PNG de alta resolución, todos de 2400 × 1350 px.
- 26 scripts individuales portátiles.
- 26 archivos `data.csv`.
- 26 archivos `README.md`.
- 26 captions sugeridos.
- 26 textos alternativos.
- 26 declaraciones de fuente o modelo.
- 1 GIF propio para U01-CH002, 47 cuadros, 2400 × 1350 px.
- 1 alternativa estática de tres estados para la animación.
- 2 hojas de contacto para revisión visual.
- 1 informe JSON de generación.

Los archivos se encuentran bajo `units/unit_01/assets/generated/`. La estructura de cada paquete es:

```text
u01_chNNN_descripcion/
├── script.py
├── data.csv
├── u01_fig_NNN_descripcion.svg
├── u01_fig_NNN_descripcion.png
├── README.md
├── caption.txt
├── alt_text.txt
└── source.txt
```

## Revisión técnica

| control | resultado |
|---|---|
| Cantidad de carpetas U01-CH | 26/26. |
| Script individual ejecutable | 26/26 sin error. |
| SVG válido y parseable | 26/26. |
| PNG presente | 26/26. |
| Resolución PNG | 26/26 a 2400 × 1350 px. |
| CSV con encabezado y datos/modelo | 26/26. |
| README, caption, alt text y fuente | 26/26. |
| Escalas de ejes declaradas | Conforme en todos los gráficos cuantitativos. |
| Ejes y unidades | Presentes donde corresponden; variables matemáticas puras rotuladas como adimensionales. |
| Modelos conceptuales | Identificados como conceptuales o no a escala. |
| Datos sintéticos | Declarados explícitamente en U01-CH026; no se presentan como mediciones. |
| Animación con alternativa estática | Conforme en U01-CH002. |
| Gráficos 3D decorativos | Ninguno. |

## Validaciones numéricas independientes

| recurso | comprobación | resultado |
|---|---|---|
| U01-CH008 | 100 m / 343 m·s⁻¹ = 0,291545… s | Correcto; se muestra 0,29 s. |
| U01-CH015 | d(5 s) = (4,0 m/s)(5 s) | 20 m. |
| U01-CH018 | 3² + 4² = 5² | Correcto. |
| U01-CH018 | sen θ = 3/5; cos θ = 4/5; tan θ = 3/4 | Correcto. |
| U01-CH019 | cos²θ + sen²θ = 1 | Correcto dentro de tolerancia numérica. |
| U01-CH020 | log₁₀(100) = 2 | Correcto. |
| U01-CH022 | 10 log₁₀(100) | 20 dB. |
| U01-CH024 | 6,8 m / 340 m·s⁻¹ | 0,020 s. |
| U01-CH024 | 100 / 0,50 s | 200 Hz. |
| U01-CH024 | 10 log₁₀(100) | 20 dB. |

## Revisión visual

Se revisaron las dos hojas de contacto y, a tamaño original, las figuras con mayor riesgo de densidad o recorte: U01-CH014, U01-CH020 y U01-CH025. También se verificó el GIF U01-MEDIA002.

Resultados:

- no se observan textos cortados, solapamientos críticos ni deformaciones;
- la jerarquía cromática distingue contenido físico, clínico y advertencias sin depender exclusivamente del color;
- los rótulos de ejes y unidades son legibles;
- las ecuaciones mantienen contraste y separación;
- los modelos cualitativos no imitan datos experimentales;
- U01-CH020 diferencia exponencial, logaritmo y recta `y = x`;
- U01-CH021 y U01-CH022 declaran explícitamente la escala logarítmica;
- U01-CH026 identifica sus datos como sintéticos y normalizados.

Hojas de revisión:

- `assets/generated/_review/u01_charts_contact_sheet_01.png`
- `assets/generated/_review/u01_charts_contact_sheet_02.png`

## Incidencias detectadas y corregidas

| id | severidad | problema | corrección | estado |
|---|---|---|---|---|
| CR-001 | Menor | Un símbolo perpendicular Unicode no estaba disponible en Calibri durante la exportación. | Se reemplazó por notación matemática `F_{\perp}` renderizada por MathText. | Cerrado. |
| CR-002 | Mayor | El texto central de U01-CH025 excedía su contenedor. | Se amplió el nodo, se dividió el texto en líneas y se reajustaron flechas. | Cerrado. |
| CR-003 | Mayor | El recorte automático producía algunas imágenes menores que 1920 px de ancho. | Se eliminó el recorte del lienzo y se normalizó toda salida a 2400 × 1350 px. | Cerrado. |
| CR-004 | Menor | Los wrappers individuales registraban una ruta absoluta al repositorio. | Se reemplazó por resolución relativa desde `__file__`; se ejecutaron los 26 wrappers. | Cerrado. |

## Observaciones para la fase de PowerPoint

- SVG es la salida principal para conservar calidad vectorial. En las slides que requieran revelado progresivo, conviene reconstruir nodos y flechas como formas nativas usando el SVG como referencia.
- Las ecuaciones deben permanecer editables cuando se monte el deck, aunque la figura de respaldo incluya su representación vectorial.
- U01-CH006 se conserva como respaldo visual; si el layout lo permite, la tabla debería recrearse como tabla nativa.
- U01-CH011, U01-CH016, U01-CH024 y U01-CH025 admiten animación por etapas, pero ya poseen una versión estática completa.
- U01-MEDIA002 es un GIF sin audio; la alternativa sin reproducción es U01-CH002.

## Problemas abiertos

No quedan problemas críticos ni mayores en los recursos generados. La decisión sobre qué diagramas se reconstruyen como formas nativas corresponde a la fase de montaje del PowerPoint y no impide usar los SVG/PNG aprobados.

