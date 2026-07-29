# Informe de reparación de diagramas — Unidad 1

Fecha: 2026-07-29  
Archivo final: `output/unidad_01_nociones_basicas_v02_diagram_fix.pptx`

## Resultado

Se repararon y reemplazaron 72 visuales generados. Los diagramas estructurales se reconstruyeron con cajas, textos, líneas y conectores editables de PowerPoint. Los gráficos cuantitativos se regeneraron mediante Python en SVG y PNG al tamaño real de uso; la animación se regeneró como GIF y conserva una alternativa estática. No se modificaron las 22 diapositivas fuera del alcance.

No quedan problemas críticos ni mayores en la revisión renderizada.

## Gates aplicados

- Tipografía estructural: cuerpo y nodos desde 22 pt; encabezados de nodos 24–28 pt; ecuaciones centrales 28 pt o más.
- Tipografía cuantitativa: títulos/ejes 22 pt, leyendas 20 pt, ticks y anotaciones auxiliares 18–26 pt.
- Padding interior de cajas: mínimo equivalente a 0,18 in; se redujo texto o redistribuyó el visual antes de bajar el tamaño.
- Conectores anclados, con lado de salida/entrada definido y etiquetas fuera de la línea.
- Callouts fuera del bounding box de la ecuación, sin tocar símbolos.
- Validación por asset dentro de la slide completa y validación final de las 94 slides.

## Revisión por slide

La columna “Validación” usa la abreviatura **R/M/Q**: render individual, revisión en mosaico y reapertura/inspección del PPTX.

| Slide | Asset anterior | Problema | Corrección | Fuente final | Validación | Estado |
|---:|---|---|---|---|---|---|
| 1 | U01-CH001 raster | Motivo pequeño | Motivo nativo redimensionado | Sin cuerpo / rótulo existente | R/M/Q | Aprobado |
| 7 | U01-CH001 raster | Motivo pequeño | Motivo nativo con geometría más simple | Sin cuerpo / rótulo existente | R/M/Q | Aprobado |
| 8 | U01-CH001 raster | Etiquetas y flechas imprecisas | Tres cajas y conectores nativos con rótulos separados | 24–28 pt | R/M/Q | Aprobado |
| 9 | U01-CH001 raster | Roles poco legibles | Tres cajas nativas compactas | 22–24 pt | R/M/Q | Aprobado |
| 10 | U01-CH002 GIF | Partículas/rótulos pequeños | GIF y alternativa estática regenerados | 22 pt | R/M/Q + medio GIF | Aprobado |
| 12 | U01-CH001 raster | Esquema pequeño | Versión nativa compacta | 22–24 pt | R/M/Q | Aprobado |
| 14 | U01-CH001 raster | Competía con la comparación | Cajas nativas dentro de la región original | 22–24 pt | R/M/Q | Aprobado |
| 17 | U01-CH003 raster | Callouts próximos a ecuación | Ecuación central y cuatro líderes separados | 24–34 pt | R/M/Q | Aprobado |
| 19 | U01-CH004 raster | Mucho vacío y texto pequeño | Bases y derivadas redistribuidas | 22–28 pt | R/M/Q | Aprobado |
| 21 | U01-CH005 raster | Flechas/rótulos pequeños | Tres relaciones con flecha y etiqueta fuera del corredor | 22–32 pt | R/M/Q | Aprobado |
| 22 | U01-CH006 raster | Tabla pequeña | Tabla nativa editable | 22 pt | R/M/Q | Aprobado |
| 24 | U01-CH011 raster | Red ilegible | Motivo nativo de sección | Sin cuerpo / rótulo existente | R/M/Q | Aprobado |
| 25 | U01-CH007 raster | Exceso de elementos | Tres relaciones apiladas | 22 pt | R/M/Q | Aprobado |
| 26 | U01-CH007 raster | Operaciones pequeñas | Tres relaciones apiladas con ecuación central 28 pt | 22–28 pt | R/M/Q | Aprobado |
| 27 | U01-CH007 raster | Columnas pequeñas | Tres columnas nativas | 22–24 pt | R/M/Q | Aprobado |
| 28 | U01-CH008 raster | Cálculo/recorrido pequeños | Recorrido, unidades y ecuación nativos | 22–28 pt | R/M/Q | Aprobado |
| 29 | U01-CH008 auxiliar | Objeto oculto de 1×1 px | Conservado deliberadamente | No aplica | Estructura | Aprobado |
| 30 | U01-CH009 raster | Texto pequeño en cajas amplias | Comparación nativa de masa/peso | 22–24 pt | R/M/Q | Aprobado |
| 31 | U01-CH009 raster | Cálculo y contraste pequeños | Cálculo lateral y dos cajas nativas | 22–24 pt | R/M/Q | Aprobado |
| 32 | U01-CH010 raster | Ecuaciones pequeñas | Ecuación central y tres tarjetas | 22–30 pt | R/M/Q | Aprobado |
| 33 | U01-CH010 raster | Ecuaciones pequeñas | Ecuación central y tres tarjetas | 22–30 pt | R/M/Q | Aprobado |
| 34 | U01-CH010 raster | Ecuaciones pequeñas | Ecuación central y tres tarjetas | 22–30 pt | R/M/Q | Aprobado |
| 35 | U01-CH011 raster | Red densa | Tres relaciones nativas apiladas | 22–24 pt | R/M/Q | Aprobado |
| 36 | U01-CH012 raster | Equivalencias pequeñas | Filas nativas de notación | 22–24 pt | R/M/Q | Aprobado |
| 37 | U01-CH012 raster | Equivalencias pequeñas | Filas nativas de notación | 22–24 pt | R/M/Q | Aprobado |
| 38 | U01-CH012 raster | Equivalencias pequeñas | Filas nativas de notación | 22–24 pt | R/M/Q | Aprobado |
| 39 | U01-CH013 raster | Prefijos/factores pequeños | Eje y rótulos nativos | 20–24 pt | R/M/Q | Aprobado |
| 40 | U01-CH013 raster | Prefijos/factores pequeños | Eje y rótulos nativos | 20–24 pt | R/M/Q | Aprobado |
| 41 | U01-CH014 raster | Red dimensional densa | Matriz dimensional nativa | 22–24 pt | R/M/Q | Aprobado |
| 42 | U01-CH014 raster | Red dimensional densa | Matriz dimensional nativa a ancho completo | 22–24 pt | R/M/Q | Aprobado |
| 43 | U01-CH014 raster | Red lateral pequeña | Matriz compacta nativa | 22 pt | R/M/Q | Aprobado |
| 44 | U01-CH016 raster | Motivo pequeño | Motivo nativo de sección | Sin cuerpo / rótulo existente | R/M/Q | Aprobado |
| 45 | U01-CH016 raster | Flujo pequeño | Flujo nativo compacto | 22–24 pt | R/M/Q | Aprobado |
| 46 | U01-CH015 raster | Ejes/anotación pequeños | Gráfico SVG/PNG regenerado | 18–22 pt | R/M/Q | Aprobado |
| 47 | U01-CH015 raster | Ejes/anotación pequeños | Gráfico SVG/PNG regenerado | 18–22 pt | R/M/Q | Aprobado |
| 48 | U01-CH016 raster | Flujo pequeño | Flujo nativo dentro de región original | 22–24 pt | R/M/Q | Aprobado |
| 49 | U01-CH016 raster | Retorno inverso poco claro | Flechas directa e inversa explícitas | 22–24 pt | R/M/Q | Aprobado |
| 50 | U01-CH016 raster | Texto pequeño | Flujo nativo y retorno explícito | 22–28 pt | R/M/Q | Aprobado |
| 51 | U01-CH016 raster | Texto pequeño | Flujo nativo y retorno explícito | 22–24 pt | R/M/Q | Aprobado |
| 52 | U01-CH017 raster | Mucho vacío y texto pequeño | Dos cajas comparativas nativas | 22–24 pt | R/M/Q | Aprobado |
| 53 | U01-CH018 raster | Motivo pequeño | Triángulo nativo de sección | Sin cuerpo / rótulo existente | R/M/Q | Aprobado |
| 54 | U01-CH018 raster | Etiquetas próximas a lados | Triángulo y razones nativos | 22–28 pt | R/M/Q | Aprobado |
| 55 | U01-CH018 raster | Etiquetas pequeñas | Triángulo y razones nativos | 22–28 pt | R/M/Q | Aprobado |
| 56 | U01-CH018 raster | Etiquetas pequeñas | Triángulo y razones nativos | 22–28 pt | R/M/Q | Aprobado |
| 57 | U01-CH018 raster | Etiquetas pequeñas | Triángulo y razones nativos | 22–28 pt | R/M/Q | Aprobado |
| 58 | U01-CH019 raster | Ejes/callouts pequeños | Círculo unitario regenerado | 18–26 pt | R/M/Q | Aprobado |
| 59 | U01-CH019 raster | Ejes/callouts pequeños | Círculo unitario regenerado | 18–26 pt | R/M/Q | Aprobado |
| 60 | U01-CH019 raster | Ejes/callouts pequeños | Círculo unitario regenerado | 18–26 pt | R/M/Q | Aprobado |
| 61 | U01-CH019 raster | Ejes/callouts pequeños | Círculo unitario regenerado | 18–26 pt | R/M/Q | Aprobado |
| 62 | U01-CH020 raster | Motivo pequeño | Motivo nativo de sección | Sin cuerpo / rótulo existente | R/M/Q | Aprobado |
| 63 | U01-CH020 raster | Ejes/leyenda pequeños | Gráfico regenerado | 18–22 pt | R/M/Q | Aprobado |
| 64 | U01-CH020 raster | Ejes/leyenda pequeños | Gráfico regenerado | 18–22 pt | R/M/Q | Aprobado |
| 65 | U01-CH020 raster | Ejes/leyenda pequeños | Gráfico regenerado | 18–22 pt | R/M/Q | Aprobado |
| 66 | U01-CH020 raster | Ejes/leyenda pequeños | Gráfico regenerado | 18–22 pt | R/M/Q | Aprobado |
| 67 | U01-CH020 raster | Ejes/leyenda pequeños | Gráfico regenerado | 18–22 pt | R/M/Q | Aprobado |
| 69 | U01-CH021 raster | Ticks pequeños | Escalas regeneradas | 18–22 pt | R/M/Q | Aprobado |
| 70 | U01-CH022 raster | Equivalencias pequeñas | Razón–dB regenerado | 18–22 pt | R/M/Q | Aprobado |
| 71 | U01-CH022 raster | Equivalencias pequeñas | Razón–dB regenerado | 18–22 pt | R/M/Q | Aprobado |
| 72 | U01-CH023 raster | Motivo pequeño | Matriz nativa compacta | Sin cuerpo / rótulo existente | R/M/Q | Aprobado |
| 73 | U01-CH023 raster | Cuerpo pequeño | Matriz nativa completa | 22–24 pt | R/M/Q | Aprobado |
| 74 | U01-CH023 raster | Matriz lateral pequeña | Matriz nativa 2×2 | 22 pt | R/M/Q | Aprobado |
| 75 | U01-CH023 raster | Cuerpo pequeño | Matriz nativa completa | 22–24 pt | R/M/Q | Aprobado |
| 76 | U01-CH026 raster | Ejes/armónicos pequeños | Espectros regenerados | 18–22 pt | R/M/Q | Aprobado |
| 77 | U01-CH023 raster | Matriz lateral pequeña | Matriz nativa 2×2 | 22 pt | R/M/Q | Aprobado |
| 78 | U01-CH023 raster | Matriz lateral pequeña | Matriz nativa 2×2 | 22 pt | R/M/Q | Aprobado |
| 79 | U01-CH001 raster | Modelo pequeño | Tres cajas y conectores nativos | 22–24 pt | R/M/Q | Aprobado |
| 80 | U01-CH023 raster | Matriz lateral pequeña | Matriz nativa 2×2 | 22 pt | R/M/Q | Aprobado |
| 81 | U01-CH024 raster | Nodos/resultados pequeños | Caso integrador nativo | 22–24 pt | R/M/Q | Aprobado |
| 82 | U01-CH024 raster | Nodos/resultados pequeños | Caso integrador nativo | 22–24 pt | R/M/Q | Aprobado |
| 83 | U01-CH024 raster | Nodos/resultados pequeños | Caso integrador nativo | 22–24 pt | R/M/Q | Aprobado |
| 84 | U01-CH025 raster | Dirección y rótulos pequeños | U1 con flechas salientes hacia U2/U3/U4 | 22–24 pt | R/M/Q | Aprobado |
| 87 | U01-CH014 raster | Respaldo dimensional pequeño | Matriz nativa | 22 pt | R/M/Q | Aprobado |
| 90 | U01-CH018 raster | Solución gráfica pequeña | Triángulo y razones nativos | 22–28 pt | R/M/Q | Aprobado |

## Verificaciones finales

- Reapertura y render completo: 94/94 slides.
- `slides_test.py`: ejecución sin errores.
- Estructura preservada: 94 slides, 94 notas, 2 masters y 27 layouts antes y después.
- Enlaces externos preservados: 2 antes y 2 después.
- Animación preservada: 1 archivo GIF antes y después.
- Slides fuera del alcance: 22/22 renders idénticos por SHA-256.
- Slides reparadas: 72/72 renders cambiaron respecto del respaldo.
- Revisión visual en mosaico y a tamaño completo: sin overflow, clipping, conectores sobre texto ni etiquetas apoyadas sobre líneas.
- No se detectaron cambios accidentales de layout, pérdida de notas o deformación de imágenes.

## Limitación documentada

La API de edición usada permite nombrar cada forma con el prefijo estable del asset, pero no expone agrupación nativa de formas. Por eso los diagramas editables están compuestos por objetos individuales claramente nombrados, no por un único grupo. Se conservaron las notas de accesibilidad existentes; los reemplazos raster mantienen texto alternativo. Esta limitación no afecta la lectura, la edición ni la geometría del deck.
