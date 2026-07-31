# Unidad 3 — Plan de diagramas editables

## Estado

**Implementado y validado el 2026-07-30.** Se generaron las 25 familias y 62 variantes para las slides candidatas. Cada variante incluye SVG editable, PNG, `source.json`, script reproducible, textos de accesibilidad, fuente y validaciones individual y en contexto 16:9. No se insertó ningún recurso en el deck ni se construyó la presentación.

## Contrato común de geometría

- Implementación predeterminada: formas, cuadros de texto, ecuaciones y conectores nativos de PowerPoint.
- SVG y PNG solo como respaldo, preview o excepción documentada.
- Diseñar dentro del área real del layout 16:9.
- Título de nodo 24–28 pt; cuerpo 22–24 pt; etiqueta de conector 20–22 pt; ecuación central 28–40 pt.
- Margen interior mínimo 0,18 in; 10–20 % de aire dentro de cajas.
- Máximo tres líneas de cuerpo por nodo.
- Conectores anclados a bordes; corredores vacíos y etiquetas separadas de las líneas.
- Separación mínima 0,10 in entre líneas y texto no relacionado.
- Callouts fuera del bounding box de la ecuación y líderes terminados a 0,05–0,10 in del símbolo.
- Si una familia no entra sin violar los mínimos, se divide la slide; no se usa shrink-to-fit.

## Plan detallado

| diagram_id | slides | visual_class | propósito pedagógico | tipo | nodos o cajas | conectores y etiquetas | ecuaciones o fórmulas | texto estimado por caja | layout previsto | restricciones geométricas | validaciones obligatorias | editable en PowerPoint |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| U03-DG001 | U03-002; U03-015; U03-079 | diagram | Distinguir fuente, medio, receptor, movimiento local y propagación. | Cadena funcional con dos niveles de flechas | 3–5 nodos: fuente, transductor opcional, medio, receptor y sistema de interpretación | Conectores horizontales “perturba”, “se propaga”, “recibe”; flechas locales cortas dentro o fuera de fuente/receptor | Ninguna | 2–6 palabras por nodo; callouts ≤8 palabras | FA_22_VISUAL_COMPLETO; FA_13_APLICACION_CLINICA | Dos códigos redundantes de flecha; no colocar etiquetas sobre la cadena; U03-002 oculta la respuesta inicial | Cero cruces; destino correcto; lectura izquierda–derecha; flechas locales no parecen transporte | Sí, obligatorio |
| U03-DG002 | U03-006; U03-016; U03-047; U03-059; U03-069; U03-078; U03-081 | diagram/mixed | Orientar y recuperar la progresión sin reescribir cada bloque. | Mapa progresivo y variantes de recap | 9 nodos breves; variantes reducidas de 2–4 nodos | 8 conectores principales sin etiqueta o con verbo de una palabra; rutas secundarias solo en mapa final | `c=λf` solo como nodo en U03-059; no ecuaciones en U03-006 | 1–4 palabras por nodo | FA_03_MAPA_CLASE; FA_16_RECAP_PARCIAL; FA_17_RECAP_FINAL | Dos filas de 5+4 nodos; corredores centrales; no reducir mapa final para “entrar” | Orden inequívoco; etapa activa visible sin depender solo del color; cero conectores cruzados | Sí, obligatorio |
| U03-DG003 | U03-008; U03-020; U03-021 | diagram | Construir equilibrio, elongación, ciclo y amplitud sobre una geometría estable. | Secuencia de estados sobre eje | 3 estados para U03-008/U03-021; 5 estados para ciclo | Flechas de movimiento y retorno; sin conectores entre cajas | `A_x` y signos de `x`; sin ecuación temporal | Etiquetas de 1–4 palabras; callouts ≤6 palabras | FA_08_DEFINICION; FA_12_PROCESO | Misma escala de eje y misma posición de equilibrio; espacio inferior para signos | Extremos simétricos; flechas de velocidad/aceleración correctas; corchete de amplitud no mide extremo–extremo | Sí, obligatorio |
| U03-DG004 | U03-009; U03-010; U03-014 | diagram | Mostrar retraso espacial y separar materia, frente y energía. | Secuencia temporal de partículas y comparación | 4–5 miniestados; una partícula marcada; frente marcado | Flecha larga “avance del frente”; flechas locales cortas; etiquetas independientes | Ninguna | Rótulos de 1–5 palabras; consignas fuera del visual | FA_12_PROCESO; FA_11_COMPARACION; FA_14_PREGUNTA_EJERCICIO | Reservar dos corredores verticales; no apoyar la flecha larga sobre partículas o texto | La marca vuelve cerca de su equilibrio; el frente avanza; códigos accesibles; cero solapamientos | Sí, obligatorio |
| U03-DG005 | U03-011–012 | diagram | Definir medio/interacción y comparar orientación longitudinal/transversal. | Conceptual + comparación de dos paneles | U03-011: 5 regiones y frontera; U03-012: 2 paneles con medio y flechas | Conectores vecinales; flecha de propagación; flechas locales paralelas o perpendiculares | Ninguna | 2–6 palabras por callout | FA_08_DEFINICION; FA_11_COMPARACION | Paneles idénticos en ancho; onda longitudinal sin curva transversal superpuesta | Direcciones correctas; aire solo en longitudinal; no sugerir partículas que viajan con la onda | Sí, obligatorio |
| U03-DG006 | U03-004; U03-018–019 | mixed/equation_only | Recuperar fuerza restauradora y definir el modelo del MAS. | Ilustración técnica y ecuación anotada | Masa, resorte, equilibrio, eje y banda de hipótesis | Flecha `x`; flecha `F_rest`; 4 líderes a símbolos | `ma=-k_sx` | Hipótesis 2–5 palabras; callouts ≤6 palabras | FA_11_COMPARACION; FA_08_DEFINICION; FA_09_ECUACION_INTERPRETACION | Ecuación centrada; callouts fuera; no más de cuatro simultáneos; usar `k_s` | Signos y unidades; líder no toca subíndices; texto ≥22 pt; ecuación ≥28 pt | Sí, obligatorio |
| U03-DG007 | U03-026; U03-065; U03-084 | diagram/mixed | Mantener una correspondencia coherente entre fase, ciclo y sinusoide. | Círculo–sinusoide y línea angular | Círculo con 4 puntos; sinusoide con 4 puntos; línea de fracciones opcional | 4–5 líderes entre puntos equivalentes; flecha angular | `Δφ=φ₂-φ₁` en U03-065 | Etiquetas de 1–4 palabras | FA_05_TEXTO_VISUAL_60_40; FA_09_ECUACION_INTERPRETACION; FA_23_APENDICE | Misma orientación angular en todas las variantes; evitar cruces en el centro del círculo | Puntos equivalentes correctos; grados/radianes/ciclo coherentes; conectores no cubren curva | Sí, obligatorio |
| U03-DG008 | U03-027 | diagram | Convertir cuatro definiciones en preguntas operativas. | Matriz 2×2 | 4 celdas: amplitud, período, frecuencia y fase; señal central opcional | Sin conectores o líderes breves desde la señal | `f=1/T` solo como recordatorio pequeño | 8–12 palabras por celda, máximo 2 líneas | FA_16_RECAP_PARCIAL | Celdas iguales; no forzar una señal central si reduce el texto | Símbolo y unidad correctos; lectura a distancia; sin redundancia literal | Sí, preferido; tabla nativa aceptable |
| U03-DG009 | U03-029 | equation_only | Vincular cada término de `x(t)` con una característica física. | Ecuación anotada | Ecuación central, mini señal y 4–5 callouts | Líderes cortos a `x(t)`, `A_x`, `f`, `φ₀`; uno a `t` solo si cabe | `x(t)=A_x cos(2πft+φ₀)` | 3–6 palabras por callout | FA_09_ECUACION_INTERPRETACION | Si cinco callouts colisionan, agrupar `t` con variable independiente; señal debajo de ecuación | Líderes no tocan caracteres; unidades y símbolos conformes; cero cruces | Sí, ecuación y callouts editables |
| U03-DG010 | U03-031–032 | diagram | Razonar signos de velocidad y aceleración en estados del ciclo. | Cuatro estados coordinados | 4 estados por slide; masa/cono, eje y banda de signos | Flechas locales `v` o `a`; sin flechas entre estados | Ninguna en ruta; ecuaciones solo en U03-088 | 1–3 símbolos y 1 frase de síntesis por estado | FA_12_PROCESO | Una variable dinámica por versión; misma geometría y escala | Direcciones correctas; `v=0` en extremos; `a=0` en equilibrio; sin confundir variables | Sí, obligatorio |
| U03-DG011 | U03-036 | mixed | Distinguir trayectoria física y representación gráfica. | Comparación de dos paneles | Objeto con recorrido rectilíneo; gráfico sinusoidal con ejes | Dos conectores “movimiento real” y “registro”; sin cruce central | Ninguna | 4–8 palabras por panel | FA_15_ERROR_FRECUENTE | Mantener paneles separados por espacio central; ejes visibles | El recorrido real no adopta forma sinusoidal; variables y unidades visibles | Sí, obligatorio |
| U03-DG012 | U03-037–038 | mixed/diagram | Organizar niveles de evidencia y crear un protocolo de lectura. | Escalera de tres niveles + checklist | U03-037: 3 nodos; U03-038: gráfico genérico y 4 callouts | Conectores “agrega escala” y “agrega calibración”; líderes del checklist | Ninguna | 6–10 palabras por nodo; callouts ≤5 palabras | FA_15_ERROR_FRECUENTE; FA_16_RECAP_PARCIAL | Corredores verticales; no apoyar etiquetas sobre flechas; gráfico sin datos ficticios | Conclusiones permitidas distintas en cada nivel; 4 preguntas legibles | Sí, obligatorio |
| U03-DG013 | U03-040 | equation_only | Definir tono puro ideal y sus condiciones. | Ecuación anotada con banda de hipótesis | Ecuación, mini sinusoide, 3 callouts y banda inferior | Líderes a `A_s`, `f`, `φ₀`; sin conectores de proceso | `s(t)=A_s cos(2πft+φ₀)` | Callouts 3–5 palabras; hipótesis 3 ítems breves | FA_08_DEFINICION | Declarar `s`; no usar una unidad genérica falsa; banda no invade ecuación | Variables definidas; frecuencia única; condición ideal visible; ecuación ≥28 pt | Sí, obligatorio |
| U03-DG014 | U03-042; U03-045; U03-047 | diagram/mixed | Separar variables y conversiones en la cadena del parlante. | Proceso de cuatro nodos | `V(t)`, cono `x(t)`, aire `ξ(t)`, presión `p(t)` | 3 conectores anclados con etiquetas “excita”, “desplaza”, “modifica presión” | Símbolos y unidades; no fórmula de conversión | 2–6 palabras por nodo; unidad en segunda línea | FA_12_PROCESO; FA_07_GRAFICO_EXPLICACION; FA_16_RECAP_PARCIAL | Slide completa en U03-042; etiquetas arriba/abajo de flechas; no afirmar amplitudes iguales | Orden y unidades correctos; conectores llegan al borde; no se infiere calibración | Sí, obligatorio |
| U03-DG015 | U03-043–044 | diagram | Explicar cómo el cono perturba el aire vecino. | Corte técnico simplificado y dos estados | U03-043: parlante y 3 posiciones; U03-044: 2 estados, partículas y regiones | Flecha de cono, flechas locales, flecha de propagación; rótulos compresión/rarefacción | `A_x` opcional; ninguna fórmula | 1–6 palabras por callout | FA_05_TEXTO_VISUAL_60_40; FA_22_VISUAL_COMPLETO | Callouts fuera del corte; partículas no sirven como texto; slide completa en U03-044 | Cono no se traslada; partículas no recorren la sala; compresión/rarefacción coherentes | Sí, obligatorio |
| U03-DG016 | U03-046 | mixed | Mostrar la función de calibración sin enseñar procedimiento clínico. | Cadena técnica | 4 nodos: generador, transductor, acoplador/oído, control | 3 conectores “señal”, “entrega”, “verifica”; callout “calibración” | `f`, nivel y condiciones como etiquetas, no fórmula | 2–6 palabras por nodo | FA_13_APLICACION_CLINICA | Espacio opcional 35 % para foto propia; si no hay foto, ampliar diagrama | No confundir acoplador con oído; no incluir resultado clínico; etiquetas ≥20 pt | Sí, obligatorio |
| U03-DG017 | U03-049 | diagram | Introducir `ξ(x,t)` como pregunta de posición e instante. | Cuadrícula conceptual | Matriz 3×3; fila `t=t₀` y columna `x=x₀` destacadas | Dos corchetes o líderes “tiempo fijo” y “posición fija” | `ξ(x,t)` | 1 símbolo por celda; callouts ≤6 palabras | FA_08_DEFINICION | No usar números densos; filas y columnas suficientemente grandes | Coordenadas coherentes; fila/columna no invertidas; contraste accesible | Sí, tabla y callouts editables |
| U03-DG018 | U03-053 | mixed | Comparar `T` y `λ` usando gráficos verdaderamente coordinados. | Comparación 2×2 | Dos gráficos U03-CH007, tabla de dos filas y 2 pares de puntos | Líderes entre estados equivalentes; sin redibujar curvas | `T` y `λ` con unidades | Tabla: 4–8 palabras por celda | FA_11_COMPARACION | Reservar 60 % para gráficos; conectores en margen central; dividir si texto <22 pt | Mismo dataset y fase; eje fijo declarado; conectores no cubren gráficos | Sí para tabla, conectores y rótulos; gráficos como SVG |
| U03-DG019 | U03-055–057; U03-059 | equation_only/mixed | Construir la onda viajera y la relación `c=λf`. | Ecuaciones anotadas + snapshots | U03-055: ecuación y 3 bandas; U03-056: 2 snapshots; U03-057: regla de 34 cm | Líderes a grupos temporal/espacial/inicial; flecha de avance entre snapshots | `ξ=A_ξ cos(2πft-2πx/λ+φ₀)`; `c=λ/T=λf` | Callouts 3–6 palabras | FA_09_ECUACION_INTERPRETACION; FA_10_EJEMPLO_RESUELTO; FA_16_RECAP_PARCIAL | Máximo cuatro callouts; ecuación ≥28 pt; no combinar ambos desarrollos en una sola geometría | Signo y dirección coherentes; unidades `m/s`; snapshots separados exactamente por `T` | Sí, obligatorio; SVG de ecuación solo si la nativa falla |
| U03-DG020 | U03-062; U03-069 | diagram | Diferenciar `u`, `c`, `φ₀` y `Δφ` mediante referentes. | Comparación de dos paneles + matriz | Partícula, frente y matriz 2×2 | Flechas locales `u`; flecha de fase `c`; sin conectarlas entre sí | Símbolos, sin ecuaciones | 4–8 palabras por celda | FA_11_COMPARACION; FA_16_RECAP_PARCIAL | Color más forma de punta y rótulo; flechas no comparten carril | Referente correcto; unidad común no sugiere identidad; matriz legible | Sí, obligatorio |
| U03-DG021 | U03-071 | equation_only | Mostrar suma punto a punto y separar valor instantáneo de amplitud. | Ecuación anotada + tres columnas temporales | Ecuación y 3 columnas con `y₁`, `y₂`, `y_R` | 6 flechas cortas de contribución a resultante; sin cruces | `y_R=y₁+y₂` | 1 valor o signo por mini nodo; callouts ≤5 palabras | FA_09_ECUACION_INTERPRETACION | Columnas iguales; flechas dentro de cada columna; no sumar amplitudes en rótulos | Sumas exactas; signos visibles; ecuación ≥28 pt; cero flechas sobre texto | Sí, obligatorio |
| U03-DG022 | U03-076 | diagram | Explicar cancelación activa como proceso espacialmente limitado. | Flujo técnico con zona | 5 nodos: ruido, sensor, control, fuente secundaria, zona | 5 conectores: “mide”, “calcula”, “emite”, “coinciden”; etiqueta de fase en corredor | Ninguna fórmula central | 2–6 palabras por nodo; límites fuera del flujo | FA_13_APLICACION_CLINICA | Zona de reducción sin texto interno; usar conectores en codo si hace falta | Orden causal; no prometer cancelación global; todas las flechas llegan al nodo correcto | Sí, obligatorio |
| U03-DG023 | U03-077 | diagram | Aplicar superposición a oído y voz sin adelantar otras unidades. | Dos mini cadenas paralelas | Máximo 3 nodos por cadena | 2 conectores por cadena, sin etiquetas largas | Ninguna | 2–5 palabras por nodo; límite en caption | FA_13_APLICACION_CLINICA | Paneles de igual ancho; no mezclar anatomía detallada | Una función por nodo; ningún conector cruza el separador | Sí, obligatorio |
| U03-DG024 | U03-080–081; U03-095 | mixed | Integrar mecanismo, gráficos, cálculo y límites. | Caso integrador + mapa conceptual + flujo de solución | U03-080: 4 nodos y 2 gráficos; U03-081: 9 nodos; U03-095: 5 pasos | Conectores numerados; enlaces desde nodos a gráficos; flechas del flujo | `f=1/T`, `c=λf` y resultados solo donde corresponda | 2–6 palabras por nodo; pasos ≤10 palabras | FA_14_PREGUNTA_EJERCICIO; FA_17_RECAP_FINAL; FA_23_APENDICE | Muy alta complejidad; separar consigna y solución si el área útil cae bajo 65 % | Cero cruces; gráficos legibles; texto ≥22 pt; secuencia verificable a vista completa | Sí; gráficos SVG incrustados, resto nativo |
| U03-DG025 | U03-024; U03-067; U03-085–092 | equation_only | Mantener consistencia de símbolos, unidades y equivalencias en ecuaciones. | Familia de ecuaciones anotadas | Una ecuación central, 2–4 callouts y hasta 2 casos laterales | Líderes cortos; ramas de proporcionalidad o equivalencia | `f=1/T`; `Δφ=2πfΔt`; `ω=2πf`; `ω=sqrt(k_s/m)`; `k_onda=2π/λ`; forma compacta; `c=ω/k_onda`; `A_R` | 3–7 palabras por callout | FA_09_ECUACION_INTERPRETACION; FA_23_APENDICE | Una relación principal por variante; no más de cuatro callouts; evitar líderes sobre radicales/subíndices | Control dimensional; glifos y subíndices conformes a guía; ecuaciones ≥28 pt; cero líderes sobre caracteres | Sí, obligatorio |

## Orden de producción recomendado

1. **Fundacionales:** U03-DG001–DG007 y DG014–DG020.
2. **Integración de gráficos:** U03-DG018, DG019 y DG024 después de generar U03-CH007/U03-CH008.
3. **Superposición:** U03-DG021–DG023 después de U03-CH012.
4. **Respaldos:** U03-DG025.

## Ciclo de aceptación

Para cada variante:

1. construir en el layout final;
2. medir texto y ecuaciones;
3. renderizar la slide completa;
4. comprobar clipping, solapamientos, conectores, etiquetas, puntas, márgenes y tamaños;
5. registrar hallazgos;
6. corregir y volver a renderizar;
7. aprobar solo con cero problemas críticos o mayores.

Si una variante conserva un problema crítico después de cinco iteraciones, debe dividirse o cambiar de tipo de visual.

## Clasificación obligatoria y estado final

| diagram_id | clasificación aplicada a sus variantes | variantes | estado final |
|---|---|---:|---|
| U03-DG001 | diagrama conceptual | 3 | approved |
| U03-DG002 | diagrama conceptual | 7 | approved |
| U03-DG003 | diagrama conceptual | 3 | approved |
| U03-DG004 | diagrama de proceso | 3 | approved |
| U03-DG005 | diagrama conceptual | 2 | approved |
| U03-DG006 | diagrama conceptual / ecuación anotada | 3 | approved |
| U03-DG007 | diagrama conceptual | 3 | approved |
| U03-DG008 | diagrama conceptual | 1 | approved |
| U03-DG009 | ecuación anotada | 1 | approved |
| U03-DG010 | diagrama de proceso | 2 | approved |
| U03-DG011 | esquema mixto | 1 | approved |
| U03-DG012 | esquema mixto | 2 | approved |
| U03-DG013 | ecuación anotada | 1 | approved |
| U03-DG014 | diagrama de proceso | 3 | approved |
| U03-DG015 | diagrama conceptual | 2 | approved |
| U03-DG016 | diagrama de proceso | 1 | approved |
| U03-DG017 | diagrama conceptual | 1 | approved |
| U03-DG018 | esquema mixto | 1 | approved |
| U03-DG019 | esquema mixto | 4 | approved |
| U03-DG020 | diagrama conceptual | 2 | approved |
| U03-DG021 | ecuación anotada | 1 | approved |
| U03-DG022 | diagrama de proceso | 1 | approved |
| U03-DG023 | diagrama de proceso | 1 | approved |
| U03-DG024 | esquema mixto | 3 | approved |
| U03-DG025 | ecuación anotada | 10 | approved |

### Editabilidad en esta fase

La fuente editable aprobada es SVG más `source.json`, con IDs, geometría, tamaños y relaciones. La conversión a formas nativas de PowerPoint queda diferida a la fase de montaje porque la consigna actual indica no construir todavía la presentación. Esta excepción está registrada en cada `README.md` e índice de familia.
