# Unidad 4 — Necesidades iniciales de gráficos cuantitativos

## Criterio

Los siguientes recursos son candidatos para `chart-generation`. Deberán producirse con scripts reproducibles, ejes y unidades explícitos, datos/equaciones documentados y exportación SVG cuando la editabilidad importe. Las curvas normalizadas deberán indicarlo en el propio gráfico.

| chart_id | slides | pregunta visual | variables o construcción | fuente de datos/modelo | salida prevista | prioridad | estado |
|---|---|---|---|---|---|---|---|
| U04-CH-001 | U04-025–026 | ¿Cómo oscila la presión acústica alrededor de la estática? | `p_total(t)`, `p_0`, `p(t)`; eje temporal y presión. | TEX 4.5.1; PDF p. 92. | SVG 16:9 y variante de detalle. | alta | especificar |
| U04-CH-002 | U04-036 | ¿Cómo se relacionan `p(t)`, `u(t)` e `i(t)`? | Tres curvas coordinadas y normalizadas; producto instantáneo. | TEX 4.5.5; PDF figura 4.2, pp. 94–95. | SVG multipanel. | alta | reconstruir |
| U04-CH-003 | U04-044–050 | ¿Qué señala cada descriptor temporal? | Señal asimétrica común; instante, extremos, pico a pico y media. | TEX 4.6; PDF pp. 95–97; construcción propia declarada. | Familia SVG con revelado progresivo. | alta | diseñar |
| U04-CH-004 | U04-048 | ¿Por qué media cero no equivale a señal nula? | Seno completo y línea cero con igual media. | TEX 4.6.4; PDF p. 96. | SVG comparativo. | media | diseñar |
| U04-CH-005 | U04-053–056 | ¿Cómo se construye el RMS? | Señal, cuadrado, media cuadrática y raíz; ventana común. | TEX 4.6.5; PDF figura 4.3, p. 97. | SVG de cuatro paneles y pasos individuales. | alta | reconstruir |
| U04-CH-006 | U04-057, U04-109 | ¿Pueden dos señales distintas tener igual RMS? | Sinusoide y señal compleja escaladas a igual RMS. | TEX 4.7; PDF p. 97; señales sintéticas. | SVG temporal; espectro solo como anticipo en U04-109. | alta | diseñar |
| U04-CH-007 | U04-064 | ¿Cómo se alinean presión y nivel? | Eje logarítmico de `p_rms` y eje lineal de `L_p`; anclas verificadas. | TEX 4.8.1; PDF figura 4.4, p. 98. | SVG vertical/horizontal según layout. | alta | reconstruir |
| U04-CH-008 | U04-070, U04-072–075 | ¿Cómo modifica la fase una suma coherente? | Pares sinusoidales y suma para `φ=0`, `π/2`, `π`. | TEX 4.9.1; PDF figura 4.5, pp. 100–101. | Familia SVG multipanel y cuadros individuales. | alta | diseñar |
| U04-CH-009 | U04-076–080 | ¿Cómo se distingue visualmente una suma no correlacionada? | Señales sintéticas, RMS y comparación `+3,01/+6,02 dB`. | TEX 4.9; PDF pp. 100–102. | SVG comparativo; semillas reproducibles. | alta | diseñar |
| U04-CH-010 | U04-084, U04-086, U04-117 | ¿Cómo cambia la intensidad con `r` según la geometría? | Curvas normalizadas `r^0`, `1/r`, `1/r²`; puntos en `r`, `2r`, `4r`. | TEX 4.10; PDF pp. 102–104. | SVG con escalas explícitas y variante cilíndrica. | alta | diseñar |
| U04-CH-011 | U04-095–097 | ¿Cómo cambia `L_p` con la distancia esférica? | `ΔL_p=20log10(r_0/r)`; anclas `1,2,4,8`. | TEX 4.11; PDF pp. 104–105. | SVG con eje `r/r_0`; sin truncado engañoso. | alta | diseñar |
| U04-CH-012 | U04-102 | ¿Cómo cambia un patrón polar con frecuencia? | Datos polares reales o sintéticos declarados, normalizados. | Asset U04-AS-007 o ecuación propia documentada. | SVG reproducible si hay datos; imagen externa si solo existe ficha. | alta | depende de curaduría |
| U04-CH-013 | U04-113 | ¿Cómo varía reflexión con el desajuste? | `R_p` y `R_I` frente a razón de impedancias. | TEX 4.5.4; PDF p. 93. | SVG de respaldo. | baja | opcional |
| U04-CH-014 | U04-121 | ¿Cuánto aumenta el total según la diferencia entre dos niveles? | Incremento de nivel frente a `ΔL` para fuentes no correlacionadas. | TEX 4.9.2; PDF pp. 101–102. | SVG de respaldo. | media | diseñar |
| U04-CH-015 | U04-122 | ¿Qué aspecto tiene la suma en cuadratura? | Dos senos a `π/2` y resultante. | TEX 4.9.1; PDF pp. 100–101. | SVG de respaldo. | baja | derivar de CH-008 |

## Reglas de producción

- Mantener una paleta coherente para `p`, `u`, intensidad, referencia y resultado en toda la unidad.
- No mezclar datos empíricos con curvas ideales sin diferenciarlos visualmente.
- Incluir ecuación o procedencia de los datos en el script y en metadatos/caption.
- Construir variantes por revelado sin cambiar escalas entre slides comparables.
- Para señales aleatorias, fijar semilla y documentar ventana y normalización.
- Comprobar legibilidad al tamaño real de la slide y reconstruir si ejes o leyendas quedan por debajo de los mínimos del sistema.
