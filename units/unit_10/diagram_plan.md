# Unidad 10 — Plan de diagramas editables y ecuaciones anotadas

Versión de planificación · 2026-08-12

## Contrato de implementación

Todos los recursos U10-DG se clasifican como `diagram` o como capa `diagram` de un visual `mixed`; los que explican fórmulas se presentan como `equation_only` en la slide. Se construirán por defecto con formas, textos, tablas, ecuaciones y conectores nativos de PowerPoint. El SVG/PNG será respaldo, no sustituto de la versión editable.

Cada recurso se diseñará dentro del rectángulo real del layout 16:9. Contrato mínimo: título de nodo 24–28 pt, cuerpo 22–24 pt, conector 20–22 pt, ecuación 28–40 pt, margen interno ≥0,18 in, aire interno 10–20 % y distancia línea–texto no relacionado ≥0,10 in. No se autoriza auto-shrink.

## Perfiles de validación

- **V0 · base:** medir textos; cero overflow/clipping; cero objetos fuera de canvas; contraste y orden de lectura; render en slide real y revisión completa.
- **V1 · conectores:** V0 + conectores anclados a bordes; corredores reservados; etiquetas en cajas independientes; cero líneas o puntas sobre texto; destino correcto.
- **V2 · ecuación:** V0 + bounding box matemático medido; máximo cuatro callouts; líderes a 0,05–0,10 in del símbolo; unidades y símbolos verificados; OMML o texto matemático editable.
- **V3 · alta densidad:** V0/V1 según corresponda + prueba a vista completa; dividir slide si una caja supera tres líneas, una etiqueta baja de 20 pt o aparecen cruces.
- **V4 · familia coordinada:** V0 + geometría, IDs y colores idénticos entre estados; solo cambia la capa pedagógicamente relevante.
- **V5 · condicionado:** no producir hasta resolver la fuente; luego aplicar V0–V3 y revisión disciplinar independiente.

## Especificación por diagrama

| diagram_id | slide / clase | propósito y tipo | nodos o cajas | conectores y etiquetas | ecuaciones | texto estimado | layout y restricciones geométricas | editable / respaldo | validación y estado |
|---|---|---|---|---|---|---|---|---|---|
| U10-DG-001 | U10-001 · `diagram` | Portada conceptual: anticipar cuatro ejes de caracterización. | Onda central; tiempo; frecuencia; nivel; efecto. | Cuatro ramales sin rótulo largo. | Ninguna. | 1–3 palabras/nodo. | FA_00; ocupar tercio inferior, sin competir con título. | Sí; SVG/PNG. | V0/V1; aprobado tras render 2026-08-12 |
| U10-DG-002 | U10-002 · `diagram` | Escena técnica del caso disparador. | Avenida, fachada, consultorio, conversación, climatización, portazo, receptor. | Rutas “entra”, “interfiere”, “se evalúa”; numeradas. | Ninguna. | 1–5 palabras/nodo. | FA_13; plano 60 % + preguntas 40 %; evitar más de 6 rutas simultáneas. | Sí; SVG/PNG. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-003 | U10-003 · `diagram` | Ruta de objetivos. | Distinguir, describir, calcular, interpretar, proponer. | Flecha de progresión; sin etiquetas. | Ninguna. | 1 verbo + complemento breve. | FA_02; dos filas, máximo 3 nodos/fila. | Sí; SVG/PNG. | V0/V1; aprobado tras render 2026-08-12 |
| U10-DG-004 | U10-004 · `diagram` | Red de prerrequisitos. | Presión/RMS; dB; espectro; SNR; percepción; propagación. | “sostiene” hacia U10, agrupados por unidad previa. | `L_p`, `p_rms` solo como símbolos. | 2–5 palabras/nodo. | FA_11; 3+3 nodos, centro libre para U10. | Sí; SVG/PNG. | V1; aprobado tras render 2026-08-12 |
| U10-DG-005 | U10-005 · `diagram` | Mapa completo de clase. | Nueve bloques y tres pausas. | Trayecto principal; ramal punteado a respaldo. | Ninguna. | 2–4 palabras/nodo. | FA_03; dos filas; numeración constante; no usar nueve tarjetas pequeñas. | Sí; SVG/PNG. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-006 | U10-007 · `diagram` | Cadena fenómeno–representación. | Fuente; presión `p(t)`; micrófono; señal; medición; receptor/efecto. | “genera”, “transduce”, “resume”, “interpreta”. | `p(t)`; unidad Pa. | 1–4 palabras/nodo. | FA_12; horizontal; corredor superior para etiquetas. | Sí; SVG/PNG. | V1; aprobado tras render 2026-08-12 |
| U10-DG-007 | U10-008 · `diagram` | Misma señal, tres funciones. | Forma de onda común; escuchar; medir; enmascarar. | Ramales “tarea”. | Ninguna. | 2–6 palabras/escena. | FA_11; señal a la izquierda, tres escenas apiladas. | Sí; SVG/PNG. | V1; aprobado tras render 2026-08-12 |
| U10-DG-008 | U10-009 · `diagram` | Mapa semántico del término ruido. | Contextual; físico/de señales; operativo. | Desde nodo “ruido”; etiqueta “uso”. | Ninguna. | Definición ≤10 palabras + ejemplo ≤4. | FA_08; tres columnas; cajas ≥2,2 in. | Sí; SVG/PNG. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-009 | U10-010 · `diagram` | Actividad de clasificación contextual. | Cuatro casos; tarea; función elegida. | Conectores revelables, sin cruce. | Ninguna. | 8–12 palabras/caso. | FA_14; 2×2; respuestas en capa oculta. | Sí; PNG de consigna/solución. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-010 | U10-013 · `diagram` | Recap señal–contexto–receptor. | Tres vértices + pregunta central. | Flechas bidireccionales sin etiqueta o con verbos de 1 palabra. | Ninguna. | 1–4 palabras/nodo. | FA_16; triángulo amplio, no iconografía decorativa. | Sí; SVG/PNG. | V1; aprobado tras render 2026-08-12 |
| U10-DG-011 | U10-018 · `diagram` | Clasificación temporal no excluyente. | Predictibilidad; continuidad; impulsividad; ejemplos. | Árbol con retorno “puede coexistir”. | Ninguna. | 1–5 palabras/nodo. | FA_14; dos ejes paralelos, no árbol de exclusión única. | Sí; SVG/PNG. | V1/V3 + revisión taxonómica; aprobado tras render 2026-08-12 |
| U10-DG-012 | U10-019 · `diagram` | Crear necesidad de estadísticos. | Muestra; ventana; registro; descriptores. | “amplía contexto”, “resume”. | Ninguna. | 1–5 palabras/nodo. | FA_12; embudo horizontal sin sugerir pérdida cero. | Sí; SVG/PNG. | V1; aprobado tras render 2026-08-12 |
| U10-DG-013 | U10-020 · `equation_only` | Ecuación de media anotada. | Ecuación central; callouts `N`, `p_i`, `p̄`; unidad. | Líderes cortos sin flecha. | `p̄=(1/N)Σp_i`. | Callout 3–7 palabras. | FA_09; fórmula centro-izquierda, interpretación derecha. | OMML + formas; SVG/PNG. | V2; aprobado tras render 2026-08-12 |
| U10-DG-014 | U10-021 · `equation_only` | Proceso conceptual de RMS. | Cuadrar; promediar; raíz; unidad recuperada. | Flechas “evita cancelación”, “promedia”, “devuelve Pa”. | `p_rms=√[(1/N)Σp_i²]`. | 1–5 palabras/etapa. | FA_09; fórmula arriba, tres etapas abajo. | OMML + formas; SVG/PNG. | V1/V2; aprobado tras render 2026-08-12 |
| U10-DG-015 | U10-022 · `equation_only` | Varianza frente a RMS. | Media; desviaciones; cuadrado; promedio; caja contraste. | Secuencia con etiqueta breve. | `σ_p²=(1/N)Σ(p_i−p̄)²`. | 2–6 palabras/nodo. | FA_09; no más de 4 callouts; unidad Pa² visible. | OMML + formas; SVG/PNG. | V1/V2; aprobado tras render 2026-08-12 |
| U10-DG-016 | U10-023 · `mixed` | Ejemplo media cero/RMS no cero. | Datos; media; cuadrados; RMS; varianza; interpretación. | Flechas de cálculo. | Sustituciones numéricas editables. | ≤1 línea por paso. | FA_10; dos filas, resultado destacado; no comprimir cinco columnas. | Sí; SVG/PNG. | V1/V2/V3; aprobado tras render 2026-08-12 |
| U10-DG-017 | U10-025 · `diagram` | Matriz de descriptores. | Filas media/RMS/varianza/distribución; columnas pregunta/unidad/límite. | Sin flechas; relación por alineación. | Símbolos, no derivaciones. | 2–7 palabras/celda. | FA_16/FA_18; ≤4 filas, columnas ≥1,6 in. | Tabla nativa editable; PNG. | V0/V3; aprobado tras render 2026-08-12 |
| U10-DG-018 | U10-028 · `diagram` | Densidad × ancho de banda. | Rectángulo espectral; altura `S_pp`; base `Δf`; área. | Callouts externos. | `p_rms²≈S_pp·Δf`. | 2–5 palabras/callout. | FA_08; 60 % gráfico conceptual, 40 % explicación. | Formas/OMML; SVG/PNG. | V1/V2; aprobado tras render 2026-08-12 |
| U10-DG-019 | U10-029 · `equation_only` | Ecuación de potencia de banda. | Integral; `f_L`, `f_H`, `S_pp`, resultado/unidad. | Máximo cuatro líderes. | `p_rms²=∫_{f_L}^{f_H}S_pp(f)df`. | 3–7 palabras/callout. | FA_09; reserva lateral para unidades Pa²/Hz·Hz=Pa². | OMML + formas; SVG/PNG. | V2; aprobado tras render 2026-08-12 |
| U10-DG-020 | U10-030 · `mixed` | Cálculo de potencia en una banda. | Datos; `Δf`; producto; `p_rms²`; interpretación. | Flechas “calcular”, “integrar”. | Caso numérico a verificar. | 1 línea/etapa. | FA_10; cuatro etapas grandes. | Sí; SVG/PNG. | V1/V2; aprobado tras render 2026-08-12 |
| U10-DG-021 | U10-036 · `diagram` | Recap color–pendiente–banda. | Blanco; rosa; PSD; octava; experiencia. | Relaciones “constante por Hz”, “constante por octava”. | `S_0`, `K/f` pequeños. | 2–6 palabras/nodo. | FA_16; dos filas coordinadas con CH-010. | Sí; SVG/PNG. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-022 | U10-038 · `diagram` | Ruido conformado al habla. | Ruido base; filtro; envolvente objetivo; salida. | “filtra según”; “conserva contorno, no habla”. | `H(f)` opcional. | 2–7 palabras/nodo. | FA_08; proceso horizontal; envolvente no normativa. | Sí; SVG/PNG. | V1; aprobado tras render 2026-08-12 |
| U10-DG-023 | U10-039 · `diagram` | Banco de filtros. | Entrada banda ancha; pasa-bajos; pasa-altos; pasabanda; salidas. | Flechas ancladas; etiquetas de banda. | `H_LP`, `H_HP`, `H_BP` solo si se definen. | 1–4 palabras/nodo. | FA_11; entrada izquierda, tres ramas; corredores separados. | Sí; SVG/PNG. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-024 | U10-040 · `diagram` | Definición visual de NBN. | Espectro amplio; filtro centrado; banda de salida; `f_L/f_c/f_H`. | “selecciona”. | `Δf=f_H−f_L`. | 1–5 palabras/nodo. | FA_08; mitad proceso, mitad respuesta idealizada. | Sí; SVG/PNG. | V1/V2; aprobado tras render 2026-08-12 |
| U10-DG-025 | U10-041 · `equation_only` | Parámetros de NBN. | Eje de frecuencia; límites; centro; ancho; pendientes. | Callouts sin cruces. | `Δf=f_H−f_L`; definición de `f_c` según fuente. | 2–6 palabras/callout. | FA_09/10; no mezclar centro aritmético y geométrico sin declarar. | OMML + formas; SVG/PNG. | V2 + verificación de definición; aprobado tras render 2026-08-12 |
| U10-DG-026 | U10-043 · `diagram` | Árbol para elegir señal de prueba. | Objetivo; región espectral; ancho; tipo; parámetros faltantes. | Preguntas en conectores de 1–3 palabras. | Ninguna. | 2–7 palabras/nodo. | FA_14; máximo tres niveles; solución en capa oculta. | Sí; SVG/PNG. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-027 | U10-044 · `diagram` | Tabla visual de familias. | Blanco, rosa, habla, NBN; forma/uso/cautela. | Sin conectores. | Mini fórmulas opcionales. | 2–7 palabras/celda. | FA_16/18; 4×4; mini espectros como formas, no charts falsos. | Tabla/formas editables; PNG. | V0/V3; aprobado tras render 2026-08-12 |
| U10-DG-028 | U10-046 · `diagram` | Cadena de medición. | Fuente; micrófono; ponderación; detector; integración; indicador; metadatos. | “transduce”, “pondera”, “integra”, “reporta”. | `L_Aeq,T` como salida. | 1–4 palabras/nodo. | FA_12; seis nodos en dos niveles; metadatos debajo. | Sí; SVG/PNG. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-029 | U10-048 · `diagram` | Máximo frente a pico. | Evento común; detector temporal; detector de pico; dos salidas. | “aplica ponderación/constante”, “busca extremo”. | `L_max`, `L_peak`. | 2–6 palabras/nodo. | FA_11; ramas paralelas simétricas. | Sí; SVG/PNG. | V1 + coordinación CH-011; aprobado tras render 2026-08-12 |
| U10-DG-030 | U10-049 · `equation_only` | Significado de nivel equivalente. | Evento variable; energía acumulada; nivel constante equivalente; intervalo `T`. | “misma energía en T”. | `L_eq,T` genérico y/o forma integral verificada. | 2–7 palabras/nodo. | FA_09; no saturar con integral y analogía simultáneas. | OMML + formas; SVG/PNG. | V1/V2; aprobado tras render 2026-08-12 |
| U10-DG-031 | U10-050 · `mixed` | Ejemplo de `L_eq` por intervalos iguales. | Tres intervalos; niveles; conversión lineal; suma; log; resultado. | Flechas de cálculo. | Fórmula de promedio energético. | 1 línea/etapa. | FA_10; línea temporal arriba, cálculo abajo. | Sí; SVG/PNG. | V1/V2/V3; aprobado tras render 2026-08-12 |
| U10-DG-032 | U10-052 · `diagram` | Fondo, señal objetivo y enmascarador. | Receptor central; tres capas acústicas; tarea. | “se desea”, “interfiere”, “se agrega deliberadamente”. | Ninguna. | 2–7 palabras/capa. | FA_11; no usar volumen/color como nivel cuantitativo. | Sí; SVG/PNG. | V1; aprobado tras render 2026-08-12 |
| U10-DG-033 | U10-053 · `equation_only` | Ecuación de SNR. | `L_señal`, `L_ruido`, diferencia y regla de signo. | Callouts exteriores. | `SNR=L_señal−L_ruido`. | 3–7 palabras/callout. | FA_09; positivo/0/negativo en franja inferior. | OMML + formas; SVG/PNG. | V2; aprobado tras render 2026-08-12 |
| U10-DG-034 | U10-055 · `diagram` | Palancas de SNR en comunicación. | Fuente vocal; distancia; ruido; oyente; tratamiento/control. | “aumenta señal”, “reduce ruido”, “modifica tarea”. | SNR solo como rótulo. | 2–6 palabras/nodo. | FA_13; escena + tres palancas, sin promesa de inteligibilidad. | Sí; SVG/PNG. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-035 | U10-056 · `diagram` | Selector de descriptor. | Preguntas sobre instante/extremo/energía/distribución/contraste; salidas. | Pregunta → indicador. | `L(t)`, `L_max`, `L_peak`, `L_eq,T`, `L_N,T`, SNR. | 2–5 palabras/nodo. | FA_16; árbol ≤2 niveles o matriz; no seis tarjetas diminutas. | Sí; SVG/PNG. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-036 | U10-058 · `diagram` | Puente físico-perceptual al masking. | Ruido externo; representación interna; señal; detectabilidad. | “eleva competencia”, “reduce detectabilidad”. | Ninguna. | 2–7 palabras/nodo. | FA_12; cadena simple, sin anatomía detallada. | Sí; SVG/PNG. | V1; aprobado tras render 2026-08-12 |
| U10-DG-037 | U10-059 · `diagram` | Cuatro elementos del enmascaramiento. | Señal; enmascarador; receptor/oído; criterio de respuesta. | Relaciones numeradas. | Ninguna. | 2–6 palabras/nodo. | FA_08; cuatro cuadrantes con centro libre. | Sí; SVG/PNG. | V1; aprobado tras render 2026-08-12 |
| U10-DG-038 | U10-060/061 · `diagram` | Arquitectura audiométrica conceptual. | Oído evaluado; oído no evaluado; transductor; ruta cruzada; enmascarante; respuesta. | “señal de prueba”, “posible cruce”, “controla”. | Sin niveles ni fórmula de masking. | 1–5 palabras/nodo. | FA_22/14; dos estados idénticos, izquierda/derecha inequívocas; sin protocolo. | Sí; SVG/PNG. | V1/V3/V4 + revisión audiológica; aprobado tras render 2026-08-12 |
| U10-DG-039 | U10-062 · `diagram` | Enmascaramiento vs protección. | Propósito perceptual; propósito de exposición; acción; resultado medido. | Bifurcación “¿qué se intenta cambiar?”. | Ninguna. | 2–7 palabras/nodo. | FA_11; dos columnas, sin conectores cruzados. | Sí; SVG/PNG. | V1; aprobado tras render 2026-08-12 |
| U10-DG-040 | U10-063 · `diagram` | Encuadre prudente de ruido y tinnitus. | Percepción; apoyo sonoro; evaluación; evidencia/plan individual. | “puede integrar”, “no sustituye”. | Ninguna. | 3–8 palabras/nodo. | FA_13; máximo cuatro nodos; incluir límite visible. | Sí; SVG/PNG. | V1 + revisión clínica; aprobado tras render 2026-08-12 |
| U10-DG-041 | U10-064 · `diagram` | Recap de función y frontera. | Señal; ruta; control; respuesta; caja “protocolo requerido”. | Cadena y ramal de límite. | Ninguna. | 2–6 palabras/nodo. | FA_16; no repetir DG-038 completo. | Sí; SVG/PNG. | V1; aprobado tras render 2026-08-12 |
| U10-DG-042 | U10-066 · `diagram` | Tres planos de análisis. | Exposición; resultado funcional; salud/diagnóstico; evidencia requerida. | “informa”, no “determina”. | Magnitudes como ejemplos. | 3–8 palabras/celda. | FA_11; matriz 3 columnas; conectores mínimos. | Sí; SVG/PNG. | V0/V3; aprobado tras render 2026-08-12 |
| U10-DG-043 | U10-067 · `diagram` | Límite causal individual. | Medición; historia de exposición; función; evaluación clínica; variables mediadoras. | “contribuye a”, “requiere”. | Ninguna. | 2–7 palabras/nodo. | FA_04; zigzag evitado; secuencia horizontal + mediadores abajo. | Sí; SVG/PNG. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-044 | U10-069 · `diagram` | Ruido de fondo en cabina. | Cabina; fuente residual; transductor; oído; banda; prueba; criterio. | Rutas “entra”, “se presenta”, “puede limitar”. | `L_A` global tachado como suficiente, sin valor. | 1–5 palabras/nodo. | FA_13; corte simplificado; no certificar ni mostrar umbral normativo. | Sí; SVG/PNG. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-045 | U10-070 · `diagram` | Jerarquía fuente–trayecto–receptor. | Fuente; mantenimiento/sustitución; barrera/encapsulado; receptor/organización/EPP; verificación. | “controlar primero”, “comprobar después”. | Ninguna. | 2–6 palabras/nodo. | FA_12; tres zonas + franja de verificación; corredores claros. | Sí; SVG/PNG. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-046 | U10-071 · `diagram` | Diferenciar reducción, absorción, aislamiento, cancelación y protección. | Cinco términos; mecanismo; dato de verificación. | Sin flechas o una relación por fila. | No usar `R` genérico. | 2–7 palabras/celda. | FA_11/18; cinco filas, tres columnas; dividir si baja 22 pt. | Tabla editable; PNG. | V0/V3 + revisión terminológica; aprobado tras render 2026-08-12 |
| U10-DG-047 | U10-072 · `diagram` | Actividad: dónde intervenir. | Caso; fuente; trayecto; receptor; opciones; métrica antes/después. | Tarjetas conectables; solución oculta. | Ninguna. | 3–9 palabras/tarjeta. | FA_14; 3 zonas horizontales; conexiones en capa de respuesta. | Sí; PNG consigna/solución. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-048 | U10-073 · `diagram` | Red de aplicaciones fonoaudiológicas. | Evaluación auditiva; voz/habla; ambiente clínico; prevención; pregunta física central. | Desde nodo “caracterizar”. | Ninguna. | 2–7 palabras/nodo. | FA_13; cuatro cuadrantes, sin iconos genéricos. | Sí; SVG/PNG. | V1; aprobado tras render 2026-08-12 |
| U10-DG-049 | U10-075 · `diagram` | Cadena medir–interpretar–controlar–verificar. | Propósito; configuración; dato; inferencia; acción; comprobación. | Verbos en flechas. | Ninguna. | 1–5 palabras/nodo. | FA_16; seis nodos en dos filas, retorno de verificación. | Sí; SVG/PNG. | V1/V3; aprobado tras render 2026-08-12 |
| U10-DG-050 | U10-077 · `diagram` | Base del caso integrador. | Avenida; HVAC; puerta; consultorio; conversación; prueba; tres receptores. | Rutas numeradas y leyenda estable. | Ninguna. | 1–4 palabras/nodo. | FA_13; plano base 65 %; espacio lateral para consigna. | Sí; SVG/PNG. | V1/V3/V4; aprobado tras render 2026-08-12 |
| U10-DG-051 | U10-078 · `mixed` | Capa temporal del caso. | DG-050 + ventanas y trazas CH-014. | Líderes desde fuente a minigráfico. | Símbolos de descriptor, no ecuaciones. | 1–4 palabras/callout. | FA_12; conservar posiciones DG-050; máximo tres trazas. | Sí; SVG/PNG. | V1/V3/V4; producir después de CH-014; aprobado tras render 2026-08-12 |
| U10-DG-052 | U10-079 · `diagram` | Capa espectro/nivel/SNR. | DG-050 + bandas, indicador por fuente y conversación objetivo. | Líderes “medir por bandas”, “comparar”. | `L_Aeq,T`, pico, SNR como rótulos. | 1–5 palabras/callout. | FA_12; mismas posiciones; no mostrar valores inventados. | Sí; SVG/PNG. | V1/V3/V4; aprobado tras render 2026-08-12 |
| U10-DG-053 | U10-080 · `diagram` | Capa señal deliberada/control/autoridad. | DG-050 + enmascarador; controles; cajas norma/protocolo. | “requiere fuente”, “actuar aquí”. | Ninguna. | 2–7 palabras/nodo. | FA_12; decisiones externas en margen derecho; no simular aprobación. | Sí; SVG/PNG. | V1/V3/V4; aprobado tras render 2026-08-12 |
| U10-DG-054 | U10-081 · `diagram` | Matriz de respuesta integradora. | Evidencia; descriptor; configuración; interpretación; acción; límite. | Sin flechas; alineación por fila. | Símbolos breves. | 2–8 palabras/celda. | FA_14; seis columnas solo si ≥22 pt; preferir 3×2. | Tabla editable; PNG. | V0/V3/V4; aprobado tras render 2026-08-12 |
| U10-DG-055 | U10-083 · `diagram` | Mapa final de síntesis. | Señal/contexto; tiempo; estadística; frecuencia; nivel; función; receptor; control; límite. | Relaciones selectivas, no red completa. | Ninguna. | 1–4 palabras/nodo. | FA_17; reutilizar DG-005 y mostrar enriquecimiento; máximo 10 flechas. | Sí; SVG/PNG. | V1/V3/V4; aprobado tras render 2026-08-12 |
| U10-DG-056 | U10-086 · `equation_only` | Identidad RMS–varianza–media. | Ecuación; tres términos; condición media cero; unidades. | Tres callouts. | `p_rms²=σ_p²+p̄²`. | 3–7 palabras/callout. | FA_23; fórmula central 36 pt; derivación mínima abajo. | OMML + formas; SVG/PNG. | V2; aprobado tras render 2026-08-12 |
| U10-DG-057 | U10-087 · `equation_only` | Integral del rosa por octava. | Intervalo `f` a `2f`; integral; resultado `K ln 2`; dos bandas. | Líderes cortos. | `∫_f^{2f}K/ν dν=K ln2`. | 2–6 palabras/callout. | FA_23; dos etapas, no más de 4 callouts. | OMML + formas; SVG/PNG. | V2 + verificación simbólica; aprobado tras render 2026-08-12 |
| U10-DG-058 | U10-088 · `equation_only` | Combinación de intervalos desiguales. | Intervalos `T_i`; niveles `L_i`; conversión lineal; promedio ponderado; resultado. | Flechas de cálculo. | Fórmula general verificada antes de producir. | 1 línea/etapa. | FA_23; puede dividirse en fórmula y ejemplo. | OMML + formas; SVG/PNG. | V2/V3; bloqueado hasta verificar ejemplo. |
| U10-DG-059 | U10-089 · `mixed` | Soluciones comentadas. | Selección de ejercicios; dato; operación; unidad; interpretación. | Flujo por ejercicio, sin conexiones entre problemas. | Varias; una por bloque. | ≤1 línea/paso. | FA_23; máximo dos ejercicios por slide; probablemente serie 089a–c. | Sí; SVG/PNG. | V2/V3; prototipar después de slide-writing. |
| U10-DG-060 | U10-091 · `diagram` | Arquitectura de protocolo clínico completo. | Indicación; oído de prueba/no prueba; nivel inicial; incrementos; meseta; sobreenmascaramiento; detención. | Flujo clínico con decisiones sí/no. | Solo fórmulas avaladas por protocolo. | A definir por fuente. | FA_23; no diseñar ni reservar geometría final antes de validar el protocolo. | Sí, obligatoria; respaldo. | V5; bloqueado por fuente institucional. |

## Familias coordinadas

1. DG-001, DG-005 y DG-055 comparten vocabulario y jerarquía para que la unidad abra, oriente y cierre con el mismo mapa enriquecido.
2. DG-013–017 comparten código visual de estadística: azul para dato, naranja para transformación y bordó para interpretación.
3. DG-018–027 comparten código espectral y límites `f_L`, `f_c`, `f_H`.
4. DG-028–035 comparten cadena de medición y notación de detectores.
5. DG-036–041 usan la misma orientación oído evaluado/no evaluado y requieren revisión audiológica.
6. DG-042–049 reutilizan fuente–trayecto–receptor de U9 sin copiar su desarrollo.
7. DG-050–055 forman una sola escena base con capas; no deben redibujarse de manera independiente.

## Gate de producción

La producción empezará por DG-002, 005, 011, 017, 023, 038, 045 y 050–055. Tras cada generación se realizará render a tamaño real, inspección visual y registro de iteración. Después de cinco intentos con un problema crítico o mayor, el recurso se dividirá o quedará bloqueado.

No se generaron diagramas ni ecuaciones en esta fase.


## Clasificación obligatoria y resultado de producción

Registro cerrado el 2026-08-12. La clasificación se fijó antes de ejecutar cada generador.

| ID | Clasificación obligatoria | Resultado | Carpeta |
|---|---|---|---|
| U10-DG-001 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-001/` |
| U10-DG-002 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-002/` |
| U10-DG-003 | diagrama de proceso | aprobado | `assets/generated/diagrams/U10-DG-003/` |
| U10-DG-004 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-004/` |
| U10-DG-005 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-005/` |
| U10-DG-006 | diagrama de proceso | aprobado | `assets/generated/diagrams/U10-DG-006/` |
| U10-DG-007 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-007/` |
| U10-DG-008 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-008/` |
| U10-DG-009 | diagrama de proceso | aprobado | `assets/generated/diagrams/U10-DG-009/` |
| U10-DG-010 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-010/` |
| U10-DG-011 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-011/` |
| U10-DG-012 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-012/` |
| U10-DG-013 | ecuación anotada | aprobado | `assets/generated/diagrams/U10-DG-013/` |
| U10-DG-014 | ecuación anotada | aprobado | `assets/generated/diagrams/U10-DG-014/` |
| U10-DG-015 | ecuación anotada | aprobado | `assets/generated/diagrams/U10-DG-015/` |
| U10-DG-016 | esquema mixto | aprobado | `assets/generated/diagrams/U10-DG-016/` |
| U10-DG-017 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-017/` |
| U10-DG-018 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-018/` |
| U10-DG-019 | ecuación anotada | aprobado | `assets/generated/diagrams/U10-DG-019/` |
| U10-DG-020 | esquema mixto | aprobado | `assets/generated/diagrams/U10-DG-020/` |
| U10-DG-021 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-021/` |
| U10-DG-022 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-022/` |
| U10-DG-023 | diagrama de proceso | aprobado | `assets/generated/diagrams/U10-DG-023/` |
| U10-DG-024 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-024/` |
| U10-DG-025 | ecuación anotada | aprobado | `assets/generated/diagrams/U10-DG-025/` |
| U10-DG-026 | diagrama de proceso | aprobado | `assets/generated/diagrams/U10-DG-026/` |
| U10-DG-027 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-027/` |
| U10-DG-028 | diagrama de proceso | aprobado | `assets/generated/diagrams/U10-DG-028/` |
| U10-DG-029 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-029/` |
| U10-DG-030 | ecuación anotada | aprobado | `assets/generated/diagrams/U10-DG-030/` |
| U10-DG-031 | esquema mixto | aprobado | `assets/generated/diagrams/U10-DG-031/` |
| U10-DG-032 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-032/` |
| U10-DG-033 | ecuación anotada | aprobado | `assets/generated/diagrams/U10-DG-033/` |
| U10-DG-034 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-034/` |
| U10-DG-035 | diagrama de proceso | aprobado | `assets/generated/diagrams/U10-DG-035/` |
| U10-DG-036 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-036/` |
| U10-DG-037 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-037/` |
| U10-DG-038 | diagrama de proceso | aprobado | `assets/generated/diagrams/U10-DG-038/` |
| U10-DG-039 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-039/` |
| U10-DG-040 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-040/` |
| U10-DG-041 | diagrama de proceso | aprobado | `assets/generated/diagrams/U10-DG-041/` |
| U10-DG-042 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-042/` |
| U10-DG-043 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-043/` |
| U10-DG-044 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-044/` |
| U10-DG-045 | diagrama de proceso | aprobado | `assets/generated/diagrams/U10-DG-045/` |
| U10-DG-046 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-046/` |
| U10-DG-047 | diagrama de proceso | aprobado | `assets/generated/diagrams/U10-DG-047/` |
| U10-DG-048 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-048/` |
| U10-DG-049 | diagrama de proceso | aprobado | `assets/generated/diagrams/U10-DG-049/` |
| U10-DG-050 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-050/` |
| U10-DG-051 | esquema mixto | aprobado | `assets/generated/diagrams/U10-DG-051/` |
| U10-DG-052 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-052/` |
| U10-DG-053 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-053/` |
| U10-DG-054 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-054/` |
| U10-DG-055 | diagrama conceptual | aprobado | `assets/generated/diagrams/U10-DG-055/` |
| U10-DG-056 | ecuación anotada | aprobado | `assets/generated/diagrams/U10-DG-056/` |
| U10-DG-057 | ecuación anotada | aprobado | `assets/generated/diagrams/U10-DG-057/` |
| U10-DG-058 | ecuación anotada | bloqueado hasta verificar ejemplo | no generado |
| U10-DG-059 | esquema mixto | bloqueado hasta slide-writing | no generado |
| U10-DG-060 | diagrama de proceso | bloqueado por protocolo institucional | no generado |
