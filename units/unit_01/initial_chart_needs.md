# Unidad 1 — Necesidades iniciales de gráficos y diagramas

## Criterio general

Todos los gráficos y diagramas deben ser propios o reconstruidos a partir de las ideas del libro, preferentemente como SVG o formas editables de PowerPoint. Los gráficos con ejes se generarán de forma reproducible con Python/Matplotlib cuando corresponda.

Convenciones comunes:

- ejes, magnitudes y unidades siempre explícitos;
- variables en cursiva y unidades en redonda;
- coma decimal en texto en español;
- `S` para área en la presentación, salvo decisión posterior documentada;
- `F_g` para peso y `F_\perp` para componente perpendicular;
- el color teal identifica descripción física y el ocre puede apoyar comparación perceptual;
- no usar flechas que sugieran causalidad determinista entre magnitud física y atributo perceptual.

| chart_id | slides | tipo | contenido y especificación | propósito | datos/modelo | formato | prioridad | estado |
|---|---|---|---|---|---|---|---|---|
| U01-CH001 | U01-001, U01-008, U01-014 | diagrama de proceso | Fuente → medio → receptor, con ejemplos intercambiables y respuesta del receptor. | Crear el modelo visual troncal de la unidad. | TEX fig:fuente-medio-receptor. | Formas PPT/SVG. | Crítica | Por reconstruir |
| U01-CH002 | U01-010 | animación/diagrama | Cadena de partículas con una partícula marcada; frente de compresión avanza y la marca oscila alrededor del equilibrio. | Separar propagación de transporte de materia. | Modelo conceptual, no datos medidos. | SVG por fotogramas + GIF/MP4. | Crítica | Por producir |
| U01-CH003 | U01-017 | diagrama anotado | Anatomía de `d = 2 m`: magnitud, símbolo, valor, unidad y tipografía. | Fijar la gramática de una medición. | TEX sec:u1-magnitud-unidad; NOT. | Formas PPT. | Crítica | Por producir |
| U01-CH004 | U01-019, U01-021 | árbol conceptual | Magnitudes fundamentales → operaciones → magnitudes derivadas. | Evitar que “derivada” se entienda como menos importante. | SI y relaciones del capítulo. | SVG/PPT. | Alta | Por producir |
| U01-CH005 | U01-021 | cadena de unidades | m/s; kg·m/s² = N; N/m² = Pa, con revelado por etapas. | Mostrar que las unidades conservan la relación física. | TEX tab:u1-magnitudes-derivadas. | Formas PPT animables. | Crítica | Por producir |
| U01-CH006 | U01-022 | tabla visual | Magnitud, símbolo, relación y unidad para d, t, v, a, F, F_g, p, ρ y f. | Dar orientación antes de construir fórmulas una por una. | TEX tabla derivadas; INV magnitudes. | Tabla PPT editable. | Alta | Por producir |
| U01-CH007 | U01-025–U01-028 | esquema cinemático | Trayecto d, intervalo Δt, rapidez media y frente de propagación c; distinguir movimiento local. | Coordinar situación, símbolos y ecuación. | Modelo de propagación constante. | SVG/PPT. | Crítica | Por producir |
| U01-CH008 | U01-028 | resolución dimensional | `m ÷ (m/s) = s` alineado con los pasos del cálculo de 100 m. | Hacer visible la comprobación de unidades. | d = 100 m; c = 343 m/s. | Formas PPT. | Alta | Por producir |
| U01-CH009 | U01-030 | comparación mecánica | Masa/inercia frente a peso/fuerza gravitatoria; qué cambia si cambia g. | Corregir la confusión masa–peso. | TEX sec:u1-masa-peso. | SVG/PPT. | Crítica | Por producir |
| U01-CH010 | U01-032–U01-034 | serie de tres diagramas | Fuerza neta y aceleración; igual fuerza en áreas diferentes; igual volumen con masas distintas. | Presentar F, p y ρ sin una tabla abstracta. | Modelos introductorios del capítulo. | SVG/PPT con estilo común. | Crítica | Por producir |
| U01-CH011 | U01-035 | red de magnitudes | d, t, v; m, a, F; F, S, p; m, V, ρ, con unidades. | Integrar el bloque y preparar análisis dimensional. | TEX fig:magnitudes-fundamentales-derivadas. | SVG/PPT. | Crítica | Por reconstruir |
| U01-CH012 | U01-037–U01-039 | recta/zoom decimal | Desplazamiento decimal y equivalencia 0,000020 Pa; 2,0 × 10^-5 Pa; 20 µPa. | Conectar notación científica y prefijos. | Ejemplo del capítulo. | Formas PPT. | Alta | Por producir |
| U01-CH013 | U01-039–U01-040 | escalera de prefijos | k, unidad, m, µ con factor, dirección de conversión y un ejemplo. | Evitar reglas de mover coma sin significado. | SI/BIPM citado en TEX. | Formas PPT. | Alta | Por producir |
| U01-CH014 | U01-041–U01-043, U01-087 | mapa dimensional | [M], [L], [T] y cadenas hacia v, a, F, p y ρ; versión corta y extendida. | Dar un control visual de coherencia. | TEX fig:magnitudes-fundamentales-derivadas. | SVG/PPT. | Crítica | Por reconstruir |
| U01-CH015 | U01-046–U01-047 | gráfico coordinado | Tabla t–d, ecuación d(t) = ct y gráfico lineal con ejes t (s), d (m). | Coordinar representaciones de una función. | Datos didácticos con c constante. | SVG + script reproducible. | Crítica | Por producir |
| U01-CH016 | U01-048–U01-050 | diagrama de correspondencias | Directa e inversa con entrada/salida y contraejemplo no unívoco. | Diferenciar inversión de simple manipulación simbólica. | TEX fig:funcion-directa-inversa. | SVG/PPT. | Crítica | Por reconstruir |
| U01-CH017 | U01-052 | comparación algebraica | Para f(x) = 2x: f^-1(x) = x/2 frente a 1/f(x) = 1/(2x), con prueba por composición. | Corregir inversa/recíproco. | TEX ejercicio D4. | Formas PPT. | Alta | Por producir |
| U01-CH018 | U01-054–U01-057 | triángulo parametrizado | Triángulo rectángulo con θ; lados opuesto, adyacente e hipotenusa; variante 3–4–5. | Mantener consistencia entre definiciones y ejemplo. | Geometría del capítulo. | SVG/PPT. | Crítica | Por producir |
| U01-CH019 | U01-058–U01-061 | círculo unitario | Orientación, arco, grados/radianes y proyecciones cos θ/sin θ; no sobrecargar con identidades. | Preparar periodicidad y fase. | TEX fig:circulo-trigonometrico; PDF p.22. | SVG/PPT animable. | Crítica | Por reconstruir |
| U01-CH020 | U01-064–U01-067 | gráficos exponencial/log | Tabla y = 10^x; curva exponencial; log10 x; recta y = x y puntos correspondientes. | Mostrar cambio multiplicativo e inversión. | Datos matemáticos exactos. | SVG + script reproducible. | Crítica | Por producir |
| U01-CH021 | U01-069 | comparación de escalas | Ejes lineal y logarítmico con 1, 10, 100 y 1000; misma anchura útil. | Hacer visible diferencia versus razón. | TEX fig:escala-lineal-logaritmica; PDF p.24. | SVG + script reproducible. | Crítica | Por reconstruir |
| U01-CH022 | U01-070–U01-071 | escalera razón–dB | Q/Q0 = 1, 10, 100, 1000 frente a 0, 10, 20, 30 dB para magnitud tipo potencia. | Dar sentido al anticipo de dB y a la referencia. | L_Q = 10 log10(Q/Q0). | SVG/PPT. | Crítica | Por producir |
| U01-CH023 | U01-073–U01-080 | matriz de clasificación | Medición física, nivel referido, atributo perceptual, control/respuesta y conclusión clínica. | Evitar equivalencias y ordenar casos de voz/Audiología. | TEX tab:u1-fisico-perceptual y ejercicios F1–F3. | Formas PPT. | Crítica | Por producir |
| U01-CH024 | U01-081–U01-083 | mapa integrador | Escena voz–aire–micrófono con d, c, N, Δt, amplitud digital y Q/Q0; salida hacia cálculos y límites. | Reutilizar todo el lenguaje de la unidad en un único sistema. | TEX ejercicio I1. | SVG/PPT animable. | Crítica | Por producir |
| U01-CH025 | U01-084 | mapa de dependencias | U1 alimenta U2 con mecánica, U3 con funciones/trigonometría y U4 con presión/log/dB. | Hacer explícita la continuidad curricular. | MAP y DEP. | Formas PPT. | Media | Por producir |

## Scripts reproducibles previstos

| script_id | gráficos | función |
|---|---|---|
| `u01_plot_001_funcion_distancia.py` | U01-CH015 | Generar tabla/gráfico d(t) con parámetros configurables y exportar SVG. |
| `u01_plot_002_exponencial_log.py` | U01-CH020 | Generar exponencial, logaritmo, y = x y puntos correspondientes. |
| `u01_plot_003_escalas_lineal_log.py` | U01-CH021 | Comparar posiciones de 1, 10, 100 y 1000 en escalas lineal y log. |
| `u01_plot_004_razon_db.py` | U01-CH022 | Generar correspondencia Q/Q0 y L_Q para magnitudes tipo potencia. |

## Controles antes de generar

1. Confirmar dimensiones y tipografía del template 16:9.
2. Mantener todos los textos editables y con tamaño apto para aula.
3. Verificar consistencia dimensional y valores numéricos en cada gráfico.
4. Etiquetar como “datos ilustrativos” cualquier curva no proveniente de medición.
5. Exportar SVG y PNG de revisión, conservando el script fuente.
6. Probar las animaciones también como secuencia estática para PDF o impresión.

