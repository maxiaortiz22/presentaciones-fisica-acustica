# Unidad 2 — Plan de diagramas editables

## Estado de implementación

**Implementado y validado el 2026-07-29.** Se generaron las 73 variantes previstas en las 15 familias, incluida U02-061. Cada variante posee SVG editable, `source.json` con geometría e IDs estables, PNG individual de 2400 × 1100 px, render `slide_context.png` de 2400 × 1350 px, script, README, caption, texto alternativo, fuente e informe JSON de validación.

Clasificación previa a la generación:

| clasificación obligatoria | cantidad |
|---|---:|
| diagrama conceptual | 24 |
| diagrama de proceso | 13 |
| ecuación anotada | 17 |
| esquema mixto | 19 |
| **Total** | **73** |

Salida: `units/unit_02/assets/generated/diagrams/`.

El ciclo global necesitó seis iteraciones: `21 → 40 → 50 → 71 → 73 → 73` variantes aprobadas. La última iteración incorporó también correcciones de revisión visual. El resultado final tiene cero problemas críticos o mayores.

Por instrucción expresa de no construir todavía la presentación, no se creó un `.pptx`. En esta fase la fuente editable es SVG + JSON de objetos; la reconstrucción con formas nativas y conectores de PowerPoint queda reservada al montaje del deck.

## Decisión de implementación

Los diagramas se producirán por familias para mantener una gramática estable sin repetir composiciones idénticas. El plan comprende las 72 candidatas registradas en el storyboard y agrega U02-061, cuya comparación de dos sistemas se beneficiará de un diagrama editable.

Por defecto se usarán:

- formas nativas de PowerPoint;
- textos editables;
- conectores anclados;
- ecuaciones nativas o SVG cuando OMML no sea viable;
- grupos con IDs estables;
- SVG y PNG de respaldo, nunca como sustitución del archivo editable.

Durante esta fase autónoma de assets, el SVG funciona como fuente vectorial editable/importable y `source.json` conserva posiciones, textos, conectores, IDs y tamaños. La decisión de formas nativas se mantiene para la futura fase de PowerPoint.

## Especificación común

- Canvas real: 13,333 × 7,5 in o área exacta del placeholder del layout.
- Márgenes seguros de la presentación: 0,67 in laterales, 0,45 in superior y 0,52 in inferior.
- Texto de nodo: 24 pt preferido, 22 pt mínimo.
- Etiquetas de conector: 20 pt mínimo.
- Ecuación central: 30–40 pt; 28 pt mínimo.
- Margen interno por caja: 0,18 in.
- Espacio libre dentro de cada caja: 10–20 %.
- Máximo ordinario: 3 líneas de cuerpo por nodo.
- Separación línea–texto no relacionado: 0,10 in.
- Conectores detrás de los nodos y anclados a sus bordes.
- Etiquetas en cajas separadas, nunca apoyadas sobre líneas.
- Sin auto-shrink.

## Plan detallado por familia

| diagram_id | slides | propósito pedagógico | tipo | nodos o cajas | conectores y etiquetas | ecuaciones | texto estimado por caja | layouts previstos | restricciones geométricas específicas | editable y exportación | validaciones específicas |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U02-DG001 | U02-002;U02-006 | Convertir la membrana inicial en pregunta y luego en mapa de la unidad. | Dos estados + mapa de proceso | U02-002: 2 regiones de aire y 1 membrana; U02-006: 5 etapas | Flechas normales sin rótulos largos; mapa con 4 conectores “permite explicar” | Ninguna en apertura | 2–5 palabras por región; 3–6 por etapa | FA_22_VISUAL_COMPLETO; FA_03_MAPA_CLASE | La membrana ocupa al menos 45 % del ancho en U02-002; mapa en una sola fila; sin cruces | Sí, formas PPT; SVG/PNG final | Presiones simétricas en equilibrio; diferencia visible sin deformación exagerada; orden de etapas correcto |
| U02-DG002 | U02-008–U02-013 | Elegir sistema, ubicar interacciones y construir fuerza neta antes de la primera ley. | Frontera, diagrama de cuerpo libre y ecuación anotada | 1 cuerpo principal; 1 frontera; 1–3 agentes; eje independiente | Flechas ancladas al cuerpo; rótulos `F_1`, `F_2`, `F_neta`; eje con `+x` | `F_neta = ΣF`; `F_neta = 0`; primera ley en forma verbal | 2–6 palabras por rótulo; máximo 2 líneas en frontera | FA_08_DEFINICION; FA_05/06; FA_12_PROCESO; FA_14; FA_09 | El eje no puede confundirse con una fuerza; mínimo 0,18 in entre flechas paralelas; resultante separada de fuerzas individuales | Sí, formas y ecuaciones PPT; SVG/PNG | Todas las fuerzas pertenecen al sistema elegido; signos coherentes con eje; equilibrio no implica ausencia de fuerzas |
| U02-DG003 | U02-016;U02-017;U02-019;U02-020 | Interpretar la segunda ley y la proporcionalidad con la masa. | Cadena causal, ecuación anotada, ejemplo y comparación | 3 nodos causales; 1 cuerpo libre; 2 masas en comparación | `F_neta` → `a` → `Δv`; flechas de fuerza iguales en comparación | `F_neta = ma`; `a = F_neta/m`; suma algebraica del ejemplo | 3–7 palabras por nodo; callouts de 1–3 palabras | FA_12_PROCESO; FA_09; FA_10; FA_14B | En U02-019 reservar 55 % del ancho al cálculo y 45 % al diagrama; masas alineadas por base | Sí; formas y OMML; SVG/PNG | Resultante calculada antes de dividir; flechas iguales realmente iguales; unidades N, kg y m/s² correctas |
| U02-DG004 | U02-021;U02-022;U02-093 | Separar pares de tercera ley de fuerzas equilibradas. | Dos cuerpos + dos diagramas coordinados | 2 cuerpos A/B; 1 interacción; 2 diagramas de cuerpo libre; hasta 3 casos en respaldo | Par `F_A→B` y `F_B→A`; conectores nunca entran al cuadro del otro cuerpo | `F_A→B = -F_B→A` | 2–5 palabras por cuerpo; 1 línea por fuerza | FA_09; FA_11; FA_23_APENDICE | Los cuerpos ocupan regiones no superpuestas; mínimo 0,35 in entre diagramas; cada fuerza aparece una sola vez en cada DCL | Sí, formas PPT; SVG/PNG | Igual módulo, dirección opuesta y cuerpos distintos; ningún par se cancela dentro del mismo DCL |
| U02-DG005 | U02-025;U02-027–U02-032 | Pasar de presiones a diferencia de presión, fuerza y aceleración. | Esquema técnico, ecuaciones anotadas y cadena causal | 2 regiones; 1 superficie; 2 fuerzas; 4 nodos de recap | Flechas normales desde cada región; resultante separada; cadena sin retorno | `Δp = p_izq-p_der`; `F_pres = Δp·S`; cancelación Pa·m²=N | 2–6 palabras por región/nodo; hasta 4 callouts | FA_22; FA_09; FA_10; FA_13; FA_16 | La superficie no debe quedar oculta por flechas; rótulos de presión fuera del área de la membrana; usar `S` visible | Sí; formas y OMML; SVG/PNG | Signo de `Δp` coincide con eje; fuerzas opuestas; unidades y ejemplo 0,50 Pa × 2,0×10⁻⁴ m² verificados |
| U02-DG006 | U02-035–U02-046 | Construir y aplicar el modelo masa–resorte–amortiguador por capas. | Modelo mecánico, comparación, matriz de signos y ecuación anotada | Masa, pared, resorte, amortiguador, fuerza externa; variantes con 1–4 mecanismos | Corredores separados para `F_ext`, `F_el`, `F_amort`; rótulos `se opone a x` y `se opone a v` | `F_el=-k_sx`; `F_amort=-bv`; `F_ext-k_sx-bv=ma` | 1–5 palabras por etiqueta; máximo 4 callouts por ecuación | FA_03; FA_05/06; FA_09; FA_11; FA_22; FA_14B; FA_10; FA_16 | Diseñar el modelo completo primero; masa ≥1,1×0,8 in; corredor superior para fuerza externa e inferior para desplazamiento/velocidad; U02-043 puede dividirse | Sí, formas PPT obligatorias; SVG/PNG de referencia | Fuerzas apuntan según `x` y `v`; conectores no cruzan resorte/amortiguador ni rótulos; parámetros no se presentan como anatómicos |
| U02-DG007 | U02-048–U02-057 | Distinguir transferencia, almacenamiento, salida y disipación sin destruir energía. | Fuerza–desplazamiento, depósitos y rutas de energía | 1 sistema; 1–4 depósitos/rutas; 2 estados de resorte; 1 frontera | Flechas de grosor uniforme; etiquetas “entra”, “se almacena”, “sale”, “se disipa” | `W_trab=Fd`; `E_c=½mv²`; `E_el=½k_sx²`; balance de energía | 3–7 palabras por nodo; ecuaciones con máximo 3 callouts | FA_06; FA_09; FA_12; FA_08; FA_10; FA_16 | No usar anchos proporcionales; distinguir cruce de frontera de cambio interno; máximo 4 rutas simultáneas | Sí, formas y OMML; SVG/PNG | El balance cierra; `ΔE_mec` no se dibuja como depósito; mJ coherentes; disipación termina en energía interna |
| U02-DG008 | U02-059;U02-061–U02-066 | Separar magnitudes de estado de transferencias y aplicar la primera ley. | Frontera termodinámica, comparación y casos de signos | 1 sistema; 2 magnitudes internas; 2 transferencias; 4 mini casos | Flechas entrantes positivas y salientes negativas; etiquetas fuera de la línea | `ΔU = Q_calor + W_sobre`; casos `Q` y `W` con signos | 2–6 palabras por tarjeta; máximo 2 líneas | FA_14; FA_08; FA_11; FA_09; FA_12; FA_10 | Mantener idéntica orientación de frontera en todo B06; cuatro casos en grilla 2×2; texto no puede invadir flechas | Sí, formas y OMML; SVG/PNG | `T_temp` y `U` dentro; calor y trabajo sobre la frontera; convención estable; U02-061 no introduce datos inventados |
| U02-DG009 | U02-071;U02-073;U02-105 | Explicar irreversibilidad y producción de entropía sin metáfora de desorden. | Desigualdad ramificada y cadena causal | Desigualdad central; 2 ramas; cadena de 4 nodos | Rama `=0` reversible ideal y `>0` irreversible; conectores horizontales | `ΔS_total ≥ 0`; `ΔS_total=0`; `ΔS_total>0` | 3–7 palabras por nodo; 1 línea por rama | FA_09; FA_12; FA_23_APENDICE | Callouts fuera del bounding box de la desigualdad; no más de 2 ramas; “energía total conservada” separado del flujo | Sí, formas y OMML; SVG/PNG | Alcance “sistema total aislado”; unidad J·K⁻¹; no asociar entropía con eco o desorden cotidiano |
| U02-DG010 | U02-078;U02-079;U02-082;U02-101–U02-103 | Separar movimiento local, propagación, temperatura, frecuencia y percepción. | Esquema longitudinal, ecuaciones anotadas, árbol de variables y trayectos | Cadena de partículas; 1 partícula marcada; 3 nodos medio/fuente/percepción; 2 trayectos | Flecha del frente distinta de flecha local; conectores “depende del medio” y “no determina por sí sola” | Aproximación `c(ϑ)`; `c=λf` como puente; `c=√(γRT/M)`; `t=d/c` | 2–6 palabras por nodo; máximo 4 callouts en ecuación general | FA_11; FA_09; FA_15; FA_23 | Separar área de gráfico y área de trayectos en U02-103; partícula marcada no deriva; no más de 4 parámetros alrededor de la raíz | Sí, formas y OMML; SVG/PNG | Frente avanza y partícula vuelve; unidades de ecuación general; no inferir pitch; hipótesis de aire seco/gas ideal visibles |
| U02-DG011 | U02-084;U02-086;U02-087 | Aplicar los mismos modelos a membrana, oído medio y vibrador con límites. | Mapa de aplicaciones, ruta pasiva y diagrama de contacto | Hasta 5 aplicaciones; 4 conceptos; ruta oído externo–medio–interno; 2 cuerpos en contacto | Conectores cortos y rotulados; par de fuerzas en vibrador/cabeza | Ninguna ecuación central; balance cualitativo y tercera ley opcionales | 2–6 palabras por nodo; máximo 2 líneas | FA_03; FA_13_APLICACION_CLINICA | En U02-086 reservar 50–55 % a anatomía y 45–50 % a ruta; no cubrir rótulos de U02-IMG002; U02-087 deja foto sin flechas sobre el rostro | Sí, formas PPT sobre/adyacentes a imagen; SVG/PNG del diagrama solo | Ruta no sugiere ganancia energética; vibrador y cabeza son cuerpos distintos; límites clínicos visibles |
| U02-DG012 | U02-088;U02-089 | Elegir el modelo apropiado y cerrar la unidad con una cadena causal. | Árbol de decisión y mapa final | Caso común + 3 ramas; mapa de 6 nodos | Preguntas en conectores breves: “¿fuerza?”, “¿energía?”, “¿propagación?” | Relaciones solo como rótulos breves; no cálculo completo | 3–7 palabras por nodo | FA_14_PREGUNTA_EJERCICIO; FA_17_RECAP_FINAL | Máximo 3 ramas desde el caso; cierre en dos filas si seis nodos no caben; sin cruces | Sí, formas PPT; SVG/PNG | Cada rama conduce a una relación correcta; mapa final agrega límites y no duplica el mapa inicial |
| U02-DG013 | U02-091;U02-092 | Dar respaldo a sistema, eje, signos y diagnóstico. | Checklist con mini DCL | 2 mini sistemas; hasta 4 mini respuestas | Flechas pequeñas pero ≥1,5 pt; etiquetas externas | `F_neta=ΣF` cuando corresponda | 2–5 palabras por mini caja | FA_23_APENDICE | Si cuatro respuestas no cumplen 22 pt, usar dos columnas o dividir; no compactar | Sí; formas PPT; SVG/PNG | Signos y sistemas consistentes con ruta central; respuestas no visibles antes de su uso |
| U02-DG014 | U02-095;U02-096 | Reunir parámetros y solución completa del modelo mecánico. | Tabla + mini modelo + cálculo | 1 mini modelo; tabla de 7 variables; secuencia de 4 cálculos | Flechas de fuerza con rótulos cortos | Modelo completo y balance instantáneo | Tabla 18–20 pt; etiquetas 20–22 pt | FA_23_APENDICE | Tabla y modelo no comparten el mismo corredor; U02-096 se divide si ecuación baja de 28 pt | Sí, tabla/formas/OMML; SVG/PNG | Unidades de `m`, `k_s`, `b`, `x`, `v`, `a`; resultado del libro verificado |
| U02-DG015 | U02-104;U02-106–U02-108 | Conservar casos de signos y solución integradora sin saturar la ruta principal. | Grilla de fronteras, plan ramificado, modelo y ruta energética | 4 fronteras; 3 ramas; modelo de superficie; 3 destinos energéticos | Entradas/salidas consistentes; conectores en codo en el plan | Primera ley; balance de fuerzas; balance de energía; `c(ϑ)` | 2–6 palabras por nodo; pasos de cálculo fuera de cajas | FA_23_APENDICE | Máximo 4 mini paneles; dividir U02-108 si aparecen más de 2 ecuaciones principales | Sí, formas y OMML; SVG/PNG | Convención de signos estable; parámetros del caso no anatómicos; límites físicos/perceptuales/ clínicos explícitos |

## Registro de variantes

| familia | variantes requeridas |
|---|---|
| U02-DG001 | membrana equilibrio/desequilibrio; mapa de cinco etapas |
| U02-DG002 | dos fronteras; interacción; eje; suma; equilibrio; primera ley |
| U02-DG003 | cadena causal; ecuación; ejemplo con tres fuerzas; comparación de masas |
| U02-DG004 | par de interacción; dos DCL; tres contraejemplos |
| U02-DG005 | dos presiones; `Δp`; `F_pres`; unidades; ejemplo; membrana distribuida; recap |
| U02-DG006 | mapa triple; masa; resorte; amortiguador; dos mini gráficos coordinados; modelo completo; ecuación; signos; ejemplo; tabla; recap |
| U02-DG007 | trabajo; energía cinética; energía elástica; intercambio; sistema aislado; rutas; balance; ejemplo; recap |
| U02-DG008 | clasificación; dos sistemas; calor; estado/transferencia; primera ley; signos; ejemplo |
| U02-DG009 | desigualdad; puente mecánico-térmico; comparación de límites |
| U02-DG010 | partícula/frente; ecuación lineal; medio/fuente/percepción; ecuación general; dimensiones; trayectos |
| U02-DG011 | mapa de aplicaciones; ruta del oído medio; vibrador–cabeza |
| U02-DG012 | árbol del caso; mapa final |
| U02-DG013 | referencia de signos; devolución diagnóstica |
| U02-DG014 | tabla de parámetros; solución mecánica |
| U02-DG015 | casos térmicos; plan integrador; solución de fuerzas; energía/temperatura/límites |

## Nombres de objetos previstos

Los objetos se nombrarán con el patrón:

```text
U02_DG006_S041_NODE_MASS
U02_DG006_S041_EDGE_FEL
U02_DG006_S041_LABEL_X
U02_DG006_S042_EQ_MAIN
```

Cada grupo tendrá:

- `NODE_*` para cuerpos, cajas o estados;
- `EDGE_*` para conectores;
- `LABEL_*` para etiquetas independientes;
- `EQ_*` para ecuaciones;
- `CALLOUT_*` para líderes y rótulos;
- `BG_*` solo para planos no informativos.

## Animación interna

La animación se limita a aparición y énfasis:

| animation_id | slides | secuencia | duración total | estado estático |
|---|---|---|---:|---|
| U02-ANI001 | U02-002 | presiones → fuerzas → pregunta | 6–8 s | ambos estados completos |
| U02-ANI002 | U02-006 | cinco etapas del mapa | 8–10 s | mapa completo |
| U02-ANI003 | U02-011 | fuerzas individuales → suma → resultante | 8–12 s | todas las flechas visibles |
| U02-ANI004 | U02-025–028 | fuerzas de cada lado → `Δp` → `F_pres` | 10–15 s distribuida | cada slide independiente |
| U02-ANI005 | U02-035–042 | masa → resorte → amortiguador → balance | 20–30 s distribuida | modelo completo U02-041/U02-042 |
| U02-ANI006 | U02-052–055 | intercambio → frontera → rutas → ecuación | 12–18 s | balance completo |
| U02-ANI007 | U02-063–065 | estado → transferencias → signos | 10–15 s | cuatro casos visibles |
| U02-ANI008 | U02-089 | seis nodos explicados en orden | 10–15 s | mapa final completo |

No se usarán trayectorias de movimiento, giros, rebotes ni animaciones decorativas.

## Validación automática y visual

Para cada variante:

1. medir textos y ecuaciones en el tamaño final;
2. comprobar cajas, márgenes internos y líneas aisladas;
3. detectar intersecciones nodo–nodo, conector–texto y etiqueta–línea;
4. verificar que cada conector esté anclado al borde correcto;
5. comprobar que ninguna punta cubra un borde o carácter;
6. confirmar que los objetos estén dentro del canvas;
7. renderizar dentro del layout real;
8. revisar a vista completa y 25 % de zoom;
9. registrar hallazgos y corregir;
10. repetir hasta cero problemas críticos o mayores.

## Gates de aceptación

- cero desbordes o clipping;
- cero conectores sobre texto;
- cero etiquetas apoyadas sobre líneas;
- cero flechas que lleguen al cuerpo equivocado;
- texto principal ≥22 pt;
- etiquetas de conectores ≥20 pt;
- ecuaciones centrales ≥28 pt;
- orden de lectura inequívoco;
- distinción no dependiente solo del color;
- fuente SVG/JSON editable aprobada en esta fase; versión PowerPoint nativa diferida al montaje;
- SVG/PNG de respaldo y preview disponibles;
- caption, alt text y lista de objetos completados.

Si una variante no cumple después de cinco iteraciones, se dividirá la slide. No se aprobará reduciendo tipografía.

## Resultado de aceptación

- 73/73 SVG parseables.
- 73/73 PNG individuales a 2400 × 1100 px.
- 73/73 renders a tamaño real de slide a 2400 × 1350 px.
- 73/73 textos principales a 22 pt o más.
- 73/73 etiquetas de conectores a 20 pt o más.
- 17/17 ecuaciones anotadas a 36 pt.
- cero desbordes, clipping, conectores sobre texto, etiquetas sobre líneas o puntas sobre caracteres en la validación final.
- 73/73 wrappers individuales ejecutados sin error.
- siete hojas de contacto revisadas.
