# Unidad 3 — Plan de gráficos cuantitativos

## Estado

**Implementado y validado el 2026-07-30.** Las trece familias se clasificaron antes de generarse como **gráfico cuantitativo**. Se produjeron 23 variantes con scripts reproducibles, CSV, SVG, PNG, textos de accesibilidad, fuentes, metadatos y render de prueba 16:9.

Salida: `units/unit_03/assets/generated/charts/`.

## Especificación común

- Diseñar en el tamaño físico del layout 16:9 indicado en el storyboard.
- Salida principal: SVG; respaldo de revisión: PNG de 2400 × 1350 px o recorte equivalente.
- Cada paquete incluirá `script.py`, `data.csv`, SVG, PNG, `README.md`, caption, texto alternativo, fuente y parámetros.
- Tipografía compatible con la plantilla; ejes ≥20 pt, ticks ≥18 pt, anotaciones ≥22 pt.
- No duplicar el título de PowerPoint dentro del gráfico.
- Fondo blanco o transparente, grilla tenue solo si ayuda.
- Color principal teal y comparación bordó/naranja, con rótulos o patrones redundantes.
- Datos sintéticos identificados como **modelo**, nunca como mediciones.
- Usar punto decimal en CSV y coma decimal en el render visible.

## Plan detallado

| chart_id | slides | pregunta que responde | variables y unidades | escala | datos o modelo | anotaciones | formato de salida | script necesario | validaciones | estado en la planificación original |
|---|---|---|---|---|---|---|---|---|---|---|
| U03-CH001 | U03-004; U03-022–023 | ¿Cómo se leen `T` y `f` y por qué son recíprocos? | x: `t` (s o ms); y: amplitud normalizada; series `f=1 Hz` y `f=2 Hz` para comparación | Lineal; ventana 0–2 s para comparación y variante 0–4 ms para el puente acústico | `y=cos(2πft)`; muestreo ≥200 puntos por ciclo | Marcar estados equivalentes, un intervalo correcto `T`, uno incorrecto de medio ciclo y conteo de ciclos | SVG + PNG + CSV; tres variantes desde un script | `units/unit_03/scripts/u03_plot_001_periodo_frecuencia.py` | `T=1/f`; mismas escalas entre series; ejes y unidades; intervalos unen estados equivalentes; amplitud rotulada normalizada | planned |
| U03-CH002 | U03-030 | ¿Qué aspecto tiene el desplazamiento de un cono de 500 Hz y 10 µm? | x: `t` (ms); y: `x` (µm) | Lineal; 0–4 ms; -12–12 µm | `x=10 µm cos(2π·500 t)`; parámetros del ejemplo del libro | `A_x=10 µm`, `T=2 ms`; banda “modelo hipotético, no presión ni audibilidad” | SVG + PNG + CSV | `units/unit_03/scripts/u03_plot_002_desplazamiento_cono.py` | Conversión `0,010 mm=10 µm`; exactamente dos ciclos; máximos ±10 µm; no inferir presión o sonoridad | planned |
| U03-CH003 | U03-033–034; apoyo U03-088 | ¿Cómo se coordinan posición, velocidad y aceleración durante un ciclo? | x: `t/T` adimensional; y: `x/A_x`, `v/(ωA_x)`, `a/(ω²A_x)` adimensionales | Lineal; 0–1,25 ciclos; y -1,15–1,15 en los tres paneles | `cos(2πt/T)`, `-sin(2πt/T)`, `-cos(2πt/T)` | Líneas verticales en 0, 1/4, 1/2, 3/4 y 1 ciclo; variante de pregunta con un instante | SVG + PNG + CSV | `units/unit_03/scripts/u03_plot_003_mas_cinematica.py` | Misma frecuencia; signos correctos; normalización explícita; escalas verticales iguales; no ocultar que las unidades físicas difieren | planned |
| U03-CH004 | U03-035–036 | ¿Por qué una misma forma no implica la misma magnitud? | x: `t` (ms); y: `x` (µm), `ξ` (µm), `p_ac` (Pa), `V` (V) | Lineal; 0–4 ms; cuatro escalas verticales propias claramente rotuladas | Sinusoides de 500 Hz con amplitudes didácticas independientes: 10 µm, 2 µm, 0,20 Pa y 0,50 V | Rótulo directo de variable y unidad; aviso “formas comparables, amplitudes no equivalentes” | SVG + PNG + CSV | `units/unit_03/scripts/u03_plot_004_variables_sinusoidales.py` | No alinear valores como si existiera conversión calibrada; misma `f`; ejes separados; datos rotulados como modelo | planned |
| U03-CH005 | U03-041; apoyo U03-MEDIA005 | ¿En qué difiere una realización tonal finita de una sinusoide ideal? | x: `t` (s); y: amplitud normalizada | Lineal; 0–1,0 s; y -1,1–1,1 | Tono 500 Hz con envolvente cosenoidal de 50 ms de ataque y caída, tramo estable de 0,90 s | Regiones “ataque”, “tramo estable”, “caída”; no mostrar espectro | SVG + PNG + CSV + WAV opcional | `units/unit_03/scripts/u03_plot_005_tono_transitorio.py` | Cero en extremos; continuidad de envolvente; `f` estable en tramo; audio sin clipping; no introducir Fourier | planned |
| U03-CH006 | U03-045 | ¿Qué registra un micrófono en una posición fija? | x: `t` (ms); y: presión acústica instantánea `p_ac` (Pa) | Lineal; 0–4 ms; -0,22–0,22 Pa | `p_ac=0,20 Pa cos(2π·500 t)`; valor pico hipotético, no RMS | Línea `p_ac=0` como presión ambiente de referencia; `A_p=0,20 Pa`; punto fijo `x=x₀` | SVG + PNG + CSV | `units/unit_03/scripts/u03_plot_006_presion_temporal.py` | Pa visibles; cero definido como variación respecto de presión ambiente; no usar dB ni RMS; declarar modelo no calibrado | planned |
| U03-CH007 | U03-050–054; U03-059 | ¿Cómo se relacionan el mapa `ξ(x,t)` y sus cortes temporal y espacial? | mapa: x `x` (m), y `t` (ms), color `ξ/A_ξ`; cortes: `ξ/A_ξ` frente a `t` o `x` | `x=0–1,36 m`; `t=0–4 ms`; color -1 a 1; cortes con y -1,1 a 1,1 | `ξ/A_ξ=cos(2π·500t-2πx/0,68)`; `f=500 Hz`, `T=2 ms`, `λ=0,68 m`, `c=340 m/s` | Marcar `x₀=0,34 m`, `t₀=1 ms`, crestas, un `T`, un `λ` e intervalos candidatos | SVG + PNG + CSV/NPZ; mapa y cinco variantes | `units/unit_03/scripts/u03_plot_007_onda_espacio_tiempo.py` | Un único dataset; cortes coinciden numéricamente con el mapa; dirección coherente con el signo; paleta divergente accesible; normalización visible | planned |
| U03-CH008 | U03-058; U03-080; U03-094–095 | ¿Puede el estudiante leer `T` y `λ` y calcular `c`? | x temporal: `t` (ms); y espacial: `x` (m); amplitud normalizada | tiempo 0–12 ms; espacio 0–4,08 m; amplitud -1,1–1,1 | Modelo distinto de U03-CH007: `f=250 Hz`, `T=4 ms`, `λ=1,36 m`, `c=340 m/s`, fase inicial `π/4` | Versión ejercicio sin valores; versión solución con intervalos equivalentes y cálculo | SVG + PNG + CSV; variantes ejercicio/solución | `units/unit_03/scripts/u03_plot_008_ejercicio_tiempo_espacio.py` | `λf=340 m/s`; fase no altera `T` o `λ`; mismos datos entre ejercicio y solución; unidades completas | planned |
| U03-CH009 | U03-063 | ¿Qué cambia cuando aumenta `f` y el medio mantiene `c`? | x: `x` (m); y: amplitud normalizada; series `f₁=250 Hz`, `f₂=500 Hz` | Lineal; 0–2,72 m; y -1,1–1,1 | `λ₁=1,36 m`, `λ₂=0,68 m`, `c=340 m/s`; mismo instante y fase inicial | Corchetes de `λ₁` y `λ₂`; rótulo directo `c` común | SVG + PNG + CSV | `units/unit_03/scripts/u03_plot_009_frecuencia_longitud.py` | Misma escala espacial; `λ₂=λ₁/2`; `c` idéntica; no usar “más rápida” para la segunda curva | planned |
| U03-CH010 | U03-064; U03-068 | ¿Cómo se reconoce una diferencia de fase? | x: `t/T`; y: amplitud normalizada; pares con `Δφ=0`, `π/2`, `π` | Lineal; 0–1,5 ciclos; y -1,1–1,1 | Pares `cos(2πt/T)` y `cos(2πt/T+Δφ)` | Puntos equivalentes, flecha de desplazamiento horizontal y variante de pregunta sin rótulo | SVG + PNG + CSV | `units/unit_03/scripts/u03_plot_010_pares_fase.py` | Misma amplitud y frecuencia; convención de adelanto declarada; escala común; color acompañado de estilo de línea | planned |
| U03-CH011 | U03-066 | ¿Qué separación espacial corresponde a una diferencia de fase? | x: `x/λ`; y: amplitud normalizada | Lineal; 0–1,25 `λ`; y -1,1–1,1 | `cos(2πx/λ)` en un instante fijo | Puntos a `0`, `λ/4`, `λ/2`, `λ`; rótulos `0`, `π/2`, `π`, `2π` | SVG + PNG + CSV | `units/unit_03/scripts/u03_plot_011_fase_espacial.py` | Comparación al mismo instante; puntos correctos; `λ` no tratado como tiempo; no introducir `k_onda` en la ruta central | planned |
| U03-CH012 | U03-072–075 | ¿Cómo cambia la resultante con `Δφ`? | x: `t/T`; y: amplitud normalizada; `y₁`, `y₂`, `y_R` | Lineal; 0–1,5 ciclos; y -2,2–2,2 para todos los casos | Dos señales de amplitud 1 y desfases `0`, `π/3`, `π/2`, `2π/3`, `π` | Instantes de suma, rótulos directos y variantes de pregunta sin resultante | SVG + PNG + CSV | `units/unit_03/scripts/u03_plot_012_superposicion.py` | Misma escala vertical; suma punto a punto exacta; cancelación total solo en `π`; no autoajustar paneles | planned |
| U03-CH013 | U03-093 | ¿Cómo varía la amplitud resultante con la fase para amplitudes iguales? | x: `Δφ` (rad); y: `A_R/A` adimensional | x 0–`2π`; y 0–2,1 | `A_R/A=sqrt(2+2cosΔφ)`; dominio completo | Puntos `0→2`, `π/2→√2`, `π→0`, `3π/2→√2`, `2π→2` | SVG + PNG + CSV | `units/unit_03/scripts/u03_plot_013_amplitud_fase.py` | Radicando no negativo dentro de tolerancia; puntos exactos; simetría; ticks en múltiplos de `π`; no presentar como percepción | planned |

## Arquitectura prevista de scripts

| archivo | función | salidas |
|---|---|---|
| `units/unit_03/scripts/u03_chart_style.py` | Tokens visuales, tamaños físicos, validación de canvas y helpers de exportación. | Estilo común y metadatos. |
| `units/unit_03/scripts/u03_plot_001_...py` a `u03_plot_013_...py` | Generar cada familia y sus variantes desde parámetros declarados. | CSV, SVG, PNG, README, caption, alt text y metadata JSON. |
| `units/unit_03/scripts/u03_generate_all_charts.py` | Regenerar las trece familias y ejecutar controles numéricos. | Reporte JSON y hoja de contacto. |

## Validación obligatoria

1. Ejecutar cada script desde la raíz sin edición manual.
2. Comprobar ecuaciones con cálculo independiente y consistencia dimensional.
3. Verificar que los gráficos coordinados provengan del mismo dataset.
4. Confirmar unidades, escalas, normalizaciones y condiciones del modelo.
5. Insertar o simular la inserción en el layout real y renderizar a 16:9.
6. Revisar clipping, solapamientos, leyendas, anotaciones y márgenes.
7. Comprobar legibilidad en vista completa y a 25 % de zoom.
8. Asegurar que color no sea la única codificación.
9. Repetir generación y render hasta cero problemas críticos o mayores.

## Estado final de implementación

| chart_id | clasificación obligatoria | variantes | estado final |
|---|---|---:|---|
| U03-CH001 | gráfico cuantitativo | 3 | approved |
| U03-CH002 | gráfico cuantitativo | 1 | approved |
| U03-CH003 | gráfico cuantitativo | 2 | approved |
| U03-CH004 | gráfico cuantitativo | 1 | approved |
| U03-CH005 | gráfico cuantitativo | 1 | approved |
| U03-CH006 | gráfico cuantitativo | 1 | approved |
| U03-CH007 | gráfico cuantitativo | 5 | approved |
| U03-CH008 | gráfico cuantitativo | 2 | approved |
| U03-CH009 | gráfico cuantitativo | 1 | approved |
| U03-CH010 | gráfico cuantitativo | 2 | approved |
| U03-CH011 | gráfico cuantitativo | 1 | approved |
| U03-CH012 | gráfico cuantitativo | 2 | approved |
| U03-CH013 | gráfico cuantitativo | 1 | approved |

El resultado consolidado se registra en `assets/generated/_review/u03_charts_generation_report.json` y `u03_final_assets_audit.json`.
