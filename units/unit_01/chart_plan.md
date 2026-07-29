# Unidad 1 — Plan de gráficos y diagramas propios

## Especificación común

- Tamaño de diseño: 13,333… × 7,5 in (16:9), con márgenes seguros del template.
- Salida principal implementada: SVG 16:9; los diagramas que convenga reconstruir como formas nativas conservan el SVG como referencia editable.
- Salida de revisión implementada: PNG 2400 × 1350 px.
- Tipografía: Calibri para rótulos; Cambria Math para ecuaciones.
- Ejes: carbón; rejilla gris tenue; curva principal teal o bordó según función.
- Todo gráfico cuantitativo incluirá ejes, unidades, escala y anotación de lectura.
- Los modelos conceptuales indicarán “esquema conceptual” o “no a escala”.
- No se generarán datos experimentales ficticios.

## Plan detallado

| chart_id | slides | pregunta que responde | variables y unidades | escala | datos o modelo | anotaciones clave | salida | script necesario | validaciones |
|---|---|---|---|---|---|---|---|---|---|
| U01-CH001 | U01-001, U01-007–U01-009, U01-012, U01-014, U01-079 | ¿Qué origina, transmite y recibe la perturbación? | Roles cualitativos; sin unidades. | No aplica. | Modelo fuente–medio–receptor del libro. | “origina”, “permite propagación”, “responde”; receptor no siempre humano. | Formas PPT + SVG. | No; formas nativas. | Flechas con un solo sentido funcional; 3–5 nodos; no insinuar diagnóstico. |
| U01-CH002 | U01-010 | ¿La materia viaja junto con la perturbación? | Posición x (m, escala arbitraria) y desplazamiento local ξ (escala arbitraria). | Lineal conceptual. | Cadena de osciladores con pulso de compresión; partícula marcada. | Frente de perturbación; posición de equilibrio; “movimiento local”. | SVG de 3 estados + PNG. | `u01_anim_001_propagacion_particulas.py`. | Centro de masa sin deriva; la marca vuelve cerca del equilibrio; declarar no a escala. |
| U01-CH003 | U01-017 | ¿Qué función cumple cada parte de d = 2 m? | d, valor 2, unidad m. | No aplica. | Anotación tipográfica exacta. | magnitud; símbolo; valor; unidad. | Formas PPT + SVG. | No. | d en cursiva; m en redonda; espacio entre valor y unidad. |
| U01-CH004 | U01-019 | ¿Cómo se construyen magnitudes derivadas desde magnitudes base? | t (s), l/d (m), m (kg); unidades derivadas. | No aplica. | Estructura SI simplificada a la unidad. | “fundamental no significa más importante”; “derivada = definida mediante otras”. | SVG + formas PPT. | No. | Contrastar con BIPM 2026 y NIST SP 1247; no incluir unidades fuera de alcance. |
| U01-CH005 | U01-021 | ¿Qué operaciones producen m/s, N y Pa? | m, s, kg, N, Pa. | No aplica. | Relaciones exactas m/s; kg·m/s²; N/m². | División, multiplicación, potencia de unidad. | Formas PPT animables + SVG final. | No. | `1 N = 1 kg·m/s²`; `1 Pa = 1 N/m²`; tipografía SI. |
| U01-CH006 | U01-022 | ¿Qué magnitudes, símbolos y unidades usaremos? | d,t,v,a,F,F_g,p,ρ,f,S,V y sus unidades. | Tabla, no aplica. | Inventario del capítulo. | Familias: movimiento, mecánica, repetición. | Tabla nativa + SVG de respaldo. | No. | Símbolos coherentes con guía; máximo 8 filas visibles; dividir si es necesario. |
| U01-CH007 | U01-025–U01-027 | ¿Cómo se distinguen rapidez, velocidad y propagación? | d (m), Δt (s), v_med (m/s), c (m/s). | Lineal conceptual. | Trayecto unidimensional y frente móvil. | Intervalo, vector, frente, partícula local. | SVG + formas PPT. | No. | La flecha de c sigue al frente; la partícula no recorre d; rapidez sin dirección. |
| U01-CH008 | U01-028–U01-029 | ¿Cómo se obtiene y verifica un tiempo de propagación? | d = 100 m; c = 343 m/s; t ≈ 0,29 s. | Trayecto lineal; cálculo exacto mostrado. | Modelo de velocidad constante del libro. | Hipótesis: aire cercano a 20 °C; cancelación de m. | SVG + ecuación nativa. | `u01_plot_006_tiempo_propagacion.py` opcional; puede resolverse con formas. | 100/343 = 0,291545… s; redondeo 0,29 s; unidad final s; no universalizar c. |
| U01-CH009 | U01-030–U01-031 | ¿Qué cambia entre masa y peso? | m (kg), F_g (N), g (m/s²). | Comparación conceptual. | F_g = mg, masa constante y dos valores hipotéticos de g sin cálculo obligatorio. | inercia; fuerza gravitatoria; “kg ≠ N”. | SVG + formas PPT. | No. | No definir masa como cantidad de materia; F_g en N; g claramente dato local. |
| U01-CH010 | U01-032–U01-034 | ¿Qué relación física expresa cada cociente o producto? | F (N), m (kg), a (m/s²), F⊥ (N), S (m²), p (Pa), ρ (kg/m³), V (m³). | Comparaciones cualitativas con valores simples opcionales. | F = ma; p = F⊥/S; ρ = m/V. | fuerza neta; fuerza perpendicular; igual F con distinta S; igual V con distinta m. | Tres SVG + composición maestra. | No. | Consistencia dimensional; usar S; no equiparar presión e intensidad. |
| U01-CH011 | U01-024, U01-035 | ¿Cómo se conectan las magnitudes de la unidad? | Dimensiones y unidades de d,t,v,m,a,F,S,p,V,ρ. | Red cualitativa. | Dependencias exactas del capítulo. | Flechas rotuladas “÷ tiempo”, “× masa”, “÷ área”, “÷ volumen”. | SVG + formas PPT. | No. | No más de 7 nodos visibles por etapa; versión vacía y completa coherentes. |
| U01-CH012 | U01-036–U01-038 | ¿Cómo representan el mismo valor el decimal, la potencia y el prefijo? | p = 0,000020 Pa = 2,0×10^-5 Pa = 20 µPa. | Base 10; zoom decimal conceptual. | Ejemplo exacto del libro. | coeficiente; exponente; prefijo micro. | SVG + formas PPT. | `u01_plot_007_notacion_cientifica.py` opcional. | Igualdad numérica; coma decimal; espacio valor–unidad; µ correcto. |
| U01-CH013 | U01-039–U01-040 | ¿Qué factor introduce cada prefijo? | k = 10³; m = 10^-3; µ = 10^-6. | Logarítmica conceptual por potencias de 10. | Prefijos SI oficiales. | Mayúsculas/minúsculas; magnitud no cambia al convertir. | Tabla nativa + SVG. | No. | Contrastar con BIPM 2026; no mezclar m unidad, m masa y mili sin tipografía. |
| U01-CH014 | U01-041–U01-043, U01-087 | ¿Qué expresiones tienen dimensiones compatibles? | [M], [L], [T]; dimensiones de v,a,F,p,ρ. | Red dimensional. | Álgebra dimensional exacta. | “necesaria, no suficiente”; d/c, dc, c/d. | SVG corto + SVG extendido. | `u01_plot_008_mapa_dimensional.py` opcional. | `[d/c]=T`; `[dc]=L²T^-1`; `[c/d]=T^-1`; derivación de Pa correcta. |
| U01-CH015 | U01-046–U01-047 | ¿Cómo cuentan tabla, ecuación y gráfico la misma relación? | t (s), d (m), c = 4,0 m/s en ejemplo. | Ejes lineales; t 0–5 s; d 0–20 m. | d(t) = ct con c constante. | Puntos (0,0), (1,4), (3,12), (5,20); condición t ≥ 0. | SVG + PNG + CSV. | `u01_plot_001_funcion_distancia.py`. | Ejes y unidades; pendiente 4,0 m/s; no extender a t < 0; sin suavizado. |
| U01-CH016 | U01-044–U01-051 | ¿Cómo recupera la inversa la entrada? | t (s), d (m), c (m/s); pares entrada–salida. | Diagramas de correspondencia. | d(t)=ct y t(d)=d/c; contraejemplo no unívoco. | directa; inversa; dominio; salida única. | Formas PPT + SVG. | No. | Cada flecha llega a una salida; inversa solo en dominio indicado; unidades intercambiadas correctamente. |
| U01-CH017 | U01-052 | ¿Por qué f⁻¹ no es 1/f? | x e y adimensionales en f(x)=2x. | No aplica. | Álgebra exacta y composición. | `f(f⁻¹(x))=x`; “recupera entrada” versus “invierte valor”. | Ecuaciones nativas + SVG de apoyo. | No. | f⁻¹(x)=x/2; 1/f(x)=1/(2x); excluir x=0 del recíproco. |
| U01-CH018 | U01-053–U01-057, U01-090 | ¿Qué lados compara cada razón trigonométrica? | Longitudes en cm; θ en grados o rad. | Geométrica exacta. | Triángulo rectángulo genérico y 3–4–5. | opuesto, adyacente, hipotenusa; razones adimensionales. | SVG + formas PPT. | `u01_plot_009_triangulo_razones.py` opcional. | Hipotenusa opuesta al ángulo recto; etiquetas relativas a θ; 3/5,4/5,3/4 correctos. |
| U01-CH019 | U01-053, U01-058–U01-061, U01-090 | ¿Cómo conectan grados, radianes y proyecciones? | θ (° y rad); x=cosθ; y=sinθ, adimensionales. | Círculo unitario; ejes -1 a 1. | Geometría exacta del círculo unitario. | arco; 2π rad; cos y sin; 225°/585° orientación final. | SVG + PNG + estados animables. | `u01_plot_010_circulo_unitario.py`. | Radio 1; 360°=2π rad; proyecciones y signos correctos; ejes sin unidades. |
| U01-CH020 | U01-062–U01-067 | ¿Cómo se relacionan exponencial y logaritmo? | x,y adimensionales; y=10^x; y=log10(x). | x exp: -3 a 3; x log: 10^-3 a 10^3 con representación adecuada. | Funciones matemáticas exactas. | puntos correspondientes; y=x; dominio x>0 para log. | SVG + PNG + CSV. | `u01_plot_002_exponencial_log.py`. | Pares (0,1), (1,10), (2,100); simetría inversa; no graficar log para x≤0. |
| U01-CH021 | U01-069 | ¿Qué cambia al ubicar razones en una escala logarítmica? | Razón Q/Q0 adimensional: 1,10,100,1000. | Panel lineal 0–1000 y panel log base 10 de 10^0 a 10^3. | Valores exactos. | Igual separación multiplicativa en panel log. | SVG + PNG + CSV. | `u01_plot_003_escalas_lineal_log.py`. | Misma anchura útil; ticks explícitos; no confundir eje log con datos perceptuales. |
| U01-CH022 | U01-070–U01-071 | ¿Cómo se transforma una razón de potencia en dB? | r=Q/Q0 adimensional; L_Q (dB). | r logarítmica 1–1000; L lineal 0–30 dB. | L_Q=10log10(r). | referencia Q0; 1→0, 10→10, 100→20, 1000→30. | SVG + PNG + CSV. | `u01_plot_004_razon_db.py`. | Coeficiente 10, no 20; argumento adimensional; no rotular SPL/HL/SL. |
| U01-CH023 | U01-072–U01-080 | ¿Qué tipo de dato representa cada elemento? | Categorías cualitativas; Hz, dB HL, amplitud digital cuando corresponda. | Matriz, no aplica. | Casos del capítulo y ejercicios F1–F3. | medición; nivel referido; atributo; respuesta; límite clínico. | Formas PPT + SVG. | No. | No usar flechas deterministas; teal/ocre más rótulos; dB HL no convertible sin calibración. |
| U01-CH024 | U01-081–U01-083 | ¿Qué permite resolver el caso y qué queda fuera? | d=6,8 m; c=340 m/s; Δt=0,50 s; N=100; Q/Q0=100; amplitud digital. | Escena espacial conceptual y cálculos exactos. | Ejercicio integrador I1 del libro. | fuente/medio/receptor; t=0,020 s; f=200 Hz; L_Q=20 dB; límites. | SVG + formas PPT + PNG final. | `u01_plot_011_caso_integrador.py` opcional. | 6,8/340=0,020 s; 100/0,50=200 Hz; 10log10(100)=20 dB; no inferir pitch ni clínica. |
| U01-CH025 | U01-084 | ¿Qué conceptos de U1 necesita cada unidad futura? | Unidades curriculares; sin unidades físicas. | Mapa de dependencias. | course_map.md y dependency_map.md. | U2 mecánica; U3 funciones/trigonometría; U4 presión/log/dB. | Formas PPT + SVG. | No. | Solo dependencias documentadas; máximo cuatro nodos. |
| U01-CH026 | U01-076 | ¿Por qué un espectro físico no equivale a timbre? | Frecuencia (Hz) y amplitud relativa (adimensional). | Frecuencia lineal 0–4000 Hz; amplitud normalizada 0–1. | Dos espectros sintéticos: componentes discretos controlados, no mediciones. | “datos sintéticos”; “mismo descriptor no determina experiencia”. | SVG + PNG + CSV. | `u01_plot_005_espectros_conceptuales.py`. | Ejes y unidades; normalización declarada; máximo 6 componentes; no atribuir instrumentos o voces reales. |

## Arquitectura de scripts implementada

| script | función | entradas | salidas | dependencias | estado |
|---|---|---|---|---|---|
| `units/unit_01/scripts/u01_chartlib.py` | Biblioteca común con metadatos, sistema visual y generadores U01-CH001–U01-CH026. | `chart_id` y parámetros internos documentados. | SVG, PNG, CSV, README, caption, alt text, fuente y, para U01-CH002, GIF. | NumPy, Matplotlib, Pillow. | Ejecutado y verificado. |
| `units/unit_01/scripts/u01_generate_all_charts.py` | Regeneración integral y hojas de contacto. | Sin parámetros obligatorios. | 26 paquetes de recursos, informe JSON y dos hojas de contacto. | `u01_chartlib.py`. | Ejecutado y verificado. |
| `assets/generated/u01_ch*/script.py` | Wrapper portátil de reproducción individual. | ID fijo del recurso. | Regenera únicamente su paquete. | Biblioteca común mediante ruta relativa. | 26/26 ejecutados sin error. |

Cada paquete contiene `script.py`, `data.csv`, SVG, PNG, `README.md`, `caption.txt`, `alt_text.txt` y `source.txt`. U01-CH002 agrega el GIF propio y conserva la figura estática de tres estados como respaldo sin conexión.

## Estado de implementación

| chart_id | carpeta de salida | escala/modelo declarado | control específico | estado |
|---|---|---|---|---|
| U01-CH001 | `assets/generated/u01_ch001_fuente_medio_receptor/` | Cualitativo. | Tres roles y sentido funcional de flechas. | Aprobado. |
| U01-CH002 | `assets/generated/u01_ch002_propagacion_particulas/` | Conceptual, no a escala. | Partícula marcada oscila sin transporte neto; GIF + alternativa estática. | Aprobado. |
| U01-CH003 | `assets/generated/u01_ch003_magnitud_valor_unidad/` | Tipográfico. | Símbolo, igualdad, valor y unidad diferenciados. | Aprobado. |
| U01-CH004 | `assets/generated/u01_ch004_si_base_derivadas/` | Árbol conceptual SI. | Dependencias base/derivadas verificadas. | Aprobado. |
| U01-CH005 | `assets/generated/u01_ch005_construccion_unidades/` | Algebraico. | N y Pa construidos con unidades SI correctas. | Aprobado. |
| U01-CH006 | `assets/generated/u01_ch006_mapa_magnitudes/` | Tabla. | Símbolos, relaciones y unidades revisados. | Aprobado. |
| U01-CH007 | `assets/generated/u01_ch007_cinematica_propagacion/` | Conceptual, no a escala. | Rapidez, velocidad y frente no se equiparan. | Aprobado. |
| U01-CH008 | `assets/generated/u01_ch008_tiempo_propagacion/` | Trayecto conceptual; cálculo exacto. | 100/343 = 0,291545… s; redondeo 0,29 s. | Aprobado. |
| U01-CH009 | `assets/generated/u01_ch009_masa_peso/` | Comparación conceptual. | Masa en kg; peso en N. | Aprobado. |
| U01-CH010 | `assets/generated/u01_ch010_fuerza_presion_densidad/` | Tres comparaciones conceptuales, no a escala. | F = ma; p = F⊥/S; ρ = m/V. | Aprobado. |
| U01-CH011 | `assets/generated/u01_ch011_red_magnitudes/` | Red conceptual. | Relaciones y unidades entre diez magnitudes. | Aprobado. |
| U01-CH012 | `assets/generated/u01_ch012_notacion_20uPa/` | Base 10. | Tres escrituras de 20 µPa numéricamente equivalentes. | Aprobado. |
| U01-CH013 | `assets/generated/u01_ch013_prefijos/` | Potencias de 10. | k, unidad, m y µ correctamente ordenados. | Aprobado. |
| U01-CH014 | `assets/generated/u01_ch014_dependencias_dimensionales/` | Red dimensional. | [d/c]=T; [dc]=L²T⁻¹; [c/d]=T⁻¹. | Aprobado. |
| U01-CH015 | `assets/generated/u01_ch015_funcion_distancia/` | Ejes lineales; t en s y d en m. | Pendiente 4,0 m/s; d(5 s)=20 m. | Aprobado. |
| U01-CH016 | `assets/generated/u01_ch016_funcion_inversa/` | Correspondencias. | Inversa recupera la entrada; contraejemplo no unívoco. | Aprobado. |
| U01-CH017 | `assets/generated/u01_ch017_inversa_reciproco/` | Algebraico. | f⁻¹(x)=x/2 y 1/f(x)=1/(2x), x≠0. | Aprobado. |
| U01-CH018 | `assets/generated/u01_ch018_triangulo_razones/` | Geometría exacta 3–4–5. | Pitágoras y razones 3/5, 4/5 y 3/4. | Aprobado. |
| U01-CH019 | `assets/generated/u01_ch019_circulo_unitario/` | Ejes lineales adimensionales. | Radio 1; cos²θ+sin²θ=1; 360°=2π rad. | Aprobado. |
| U01-CH020 | `assets/generated/u01_ch020_exponencial_log/` | Ejes lineales en ventana didáctica. | Puntos inversos y dominio x>0 del logaritmo. | Aprobado. |
| U01-CH021 | `assets/generated/u01_ch021_escalas_lineal_log/` | Panel lineal y panel log base 10. | Ticks 1, 10, 100, 1000 explícitos. | Aprobado. |
| U01-CH022 | `assets/generated/u01_ch022_razon_db/` | Razón en eje log; nivel en eje lineal. | 1→0, 10→10, 100→20, 1000→30 dB. | Aprobado. |
| U01-CH023 | `assets/generated/u01_ch023_matriz_clasificacion/` | Matriz cualitativa. | Sin equivalencias deterministas entre físico, referido, perceptual y clínico. | Aprobado. |
| U01-CH024 | `assets/generated/u01_ch024_caso_integrador/` | Escena conceptual y cálculos exactos. | 0,020 s; 200 Hz; 20 dB; límites de inferencia explícitos. | Aprobado. |
| U01-CH025 | `assets/generated/u01_ch025_dependencias_curso/` | Mapa curricular. | Solo U1–U4 y dependencias documentadas. | Aprobado. |
| U01-CH026 | `assets/generated/u01_ch026_espectros_conceptuales/` | Frecuencia lineal; amplitud normalizada. | Datos sintéticos declarados; no se atribuyen fuentes reales. | Aprobado. |

## Validación transversal

1. Revisar cada fórmula contra el capítulo LaTeX.
2. Comprobar consistencia dimensional con cálculo independiente.
3. Verificar que no haya ejes sin nombre o unidad.
4. Declarar datos sintéticos y modelos conceptuales.
5. Comparar las exportaciones SVG y PNG para detectar textos cortados.
6. Probar legibilidad al 25 % de zoom y en proyección 16:9.
7. Mantener archivos fuente, datos y README junto a cada gráfico generado.
