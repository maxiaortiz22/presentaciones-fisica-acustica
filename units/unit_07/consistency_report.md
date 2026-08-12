# Informe de consistencia — Unidad 7

**Unidad:** 7 · Características subjetivas de la percepción auditiva y psicoacústica  
**Fecha:** 2026-08-11  
**Deck comparado:** `output/unidad_07_psicoacustica_final.pptx`  
**Baseline:** guía de estilo, mapa del curso, glosario, guía de notación, template v01 y unidades 1–6 finalizadas  
**Criterio:** una diferencia se conserva cuando responde a una función pedagógica real; no se usa la mayoría de los decks como sustituto de una decisión global documentada.

## Dictamen final

La versión final mantiene las diferencias pedagógicas justificadas de la Unidad 7 y ya no presenta inconsistencias bloqueantes respecto del curso. Se resolvieron la ruta de ampliaciones, la notación visible, fon/son, la terminología de enmascaramiento, los ejemplos de cálculo, la semántica de cinco diagramas, los bloques duplicados de fuentes, los pies de producción y las instrucciones a multimedia inexistente.

Persisten dos decisiones globales que no corresponde resolver solo en U7: OMML frente a texto editable en Cambria Math y el color canónico de títulos. Además, se aceptan tres deudas menores: diagramas heredados insertados como raster aunque conservan maestros editables; una cadencia repetitiva en algunas notas; y seis medios opcionales no producidos, con alternativa visual completa.

### Estado de las diferencias que eran inconsistentes en v02

| IDs | Clasificación final | Resolución o decisión |
|---|---|---|
| CG07-01, CG07-10 | **aceptable** | Slide 30 incorpora un trazado cualitativo legible y una consigna resoluble; no reproduce datos normativos de ISO 226 y lo declara. |
| CG07-07, CG07-08 | **aceptable** | Se estandarizaron señal enmascarante/enmascarador, fon y son en texto visible y fuentes editables. |
| CG07-11, CG07-12, CG07-13 | **aceptable** | El parser dejó de convertir subíndices en paréntesis y se eliminó `abs(...)`; la notación compleja usa texto editable y subíndices Unicode. |
| CG07-17 | **aceptable** | 24, 51, 58, 81, 91 y 105 muestran datos, sustitución, resultado e interpretación. |
| CG07-21, CG07-22 | **aceptable** | 74, 85, 103, 107 y 117 son nativas y causalmente corregidas. Los diagramas heredados conservan fuentes `.pptx`/SVG/scripts y quedan como deuda menor aceptada. |
| CG07-24 | **aceptable** | Se conserva la frecuencia alta de recapitulaciones por densidad; algunas tarjetas repetidas quedan como recurso de recuperación estable, no como default global. |
| CG07-25 | **intencional** | La transferencia profesional se concentra donde hay suficientes magnitudes para evitar adelantar protocolos de U8; 25, 77–87 y 115–118 sostienen aplicaciones próximas al concepto. |
| CG07-26 | **aceptable** | El PowerPoint contiene 134 notas y exactamente 134 bloques `[Sources]`. |
| CG07-27 | **aceptable** | Las notas se rotulan como versión final sincronizada; la repetición residual se registra como deuda estilística menor. |
| CG07-29 | **aceptable** | Las 18 complementarias muestran `AMPLIACIÓN`; las 13 de respaldo, `A DEMANDA`. |
| CG07-30, CG07-31 | **aceptable** | Se retiraron pies y códigos internos de diagramas; la trazabilidad queda en notas y manifiesto. |
| CG07-32B | **aceptable** | Los componentes repetidos se conservan solo cuando cumplen comparación, proceso o recuperación; los cinco diagramas críticos ya no usan grillas ambiguas. |
| CG07-36 | **aceptable** | Dos medios esenciales fueron producidos y aprobados; para los seis opcionales las notas ya no indican reproducir archivos ausentes. |

## Dictamen diagnóstico de v02 — histórico

La Unidad 7 pertenece visual y estructuralmente al mismo curso: conserva 16:9, dos masters, 27 layouts, numeración dinámica, tipografías, pie institucional y la paleta bordó–teal–ocre del sistema. Su mayor profundidad, sus cuatro encuentros y sus recapitulaciones más frecuentes son diferencias **intencionales** y apropiadas para una unidad de carga muy alta.

En la v02, el deck todavía contenía inconsistencias que no debían pasar a U8–U10:

- la notación correcta del archivo fuente se degrada en el PPTX visible a formas como `L(N)`, `N(son)`, `T(60)`, `G(CT)` y `abs(Δt(LR))`;
- alterna las unidades españolas fon/son con *phon/sone*;
- usa “máscara”, “enmascarador” y “señal objetivo” sin una preferencia terminológica estable;
- repite 39 captions de producción y 39 créditos internos visibles, en contra de D-056 y D-066;
- las notas contienen dos bloques de fuentes por slide y siguen rotuladas como v01;
- las 18 slides complementarias aparecen proyectadas como `RUTA CENTRAL`;
- varios ejemplos y recapitulaciones se apartan del contrato pedagógico del template;
- la secuencia 27–30 no satisface todavía la lectura de una curva isofónica normalizada exigida por el programa y el mapa.

Esa revisión diagnóstica no modificó el deck. La fase de cierre posterior corrigió o aceptó explícitamente los puntos anteriores; la matriz que sigue se conserva como trazabilidad histórica.

## Fuentes de comparación

- `AGENTS.md`;
- `style/presentation_style_guide.md`;
- `course_map.md` y `course_dependency_map.md`;
- `style/glossary.md`;
- `style/notation_guide.md`;
- `style/decision_log.md`;
- `style/layout_catalog.md`, `style/component_catalog.md` y `style/slide_master_spec.md`;
- `output/fisica_acustica_template_v01.pptx` y `style/template_mosaic.png`;
- decks finales y renders de U1–U6;
- `units/unit_07/output/unidad_07_psicoacustica_v02.pptx` y sus 134 renders;
- `units/unit_07/storyboard.md`, `slide_text.md`, `speaker_notes.md`, `review.md` e `independent_pedagogical_review.md`.

## Cómo se interpretó el baseline

Las unidades anteriores contienen legados que no deben propagarse:

- U3 conserva numerosos avisos “no a escala”, aunque D-056 ya ordena retirarlos;
- U5 mantiene una paleta azul–verde–violeta más marcada; D-062 establece que no constituye una variante global;
- U6 mostró problemas de numeración/rutas y créditos internos que dieron lugar a D-065 y D-066;
- todos los decks finales U1–U7 usan texto editable en Cambria Math y registran cero ecuaciones OMML en el paquete, aunque la guía prefiere OMML para ecuaciones estructuradas; esta diferencia sigue siendo una decisión técnica global pendiente.

Por eso, U7 se compara primero con las reglas canónicas y después con las soluciones efectivamente consolidadas en U1–U6.

## Matriz diagnóstica de diferencias en v02

| ID | Dimensión | Baseline | Unidad 7 | Clasificación | Impacto y recomendación |
|---|---|---|---|---|---|
| CG07-01 | Cobertura / mapa | El programa y el mapa exigen interpretar curvas isofónicas normalizadas; un esquema conceptual no sustituye datos normativos. | 27–29 explican el procedimiento, pero 30 pide leer una curva que no aparece. | **inconsistente** | Incorporar una curva con norma/edición/condiciones o cambiar la consigna. Reabre la cobertura que el review anterior daba por cerrada. |
| CG07-02 | Profundidad | U4–U7 son unidades densas; el mapa permite varios encuentros, bloques cortos y recapitulaciones. | 134 slides, cuatro encuentros, 103 centrales, 18 complementarias y 13 de respaldo. | **intencional** | La extensión es comparable con U4 (125), U5 (150) y U6 (117). No reducir por uniformidad; hacer operativa la selección. |
| CG07-03 | Continuidad curricular | U7 recibe niveles, espectro y oído periférico de U4–U6 y prepara U8–U10. | Los puentes iniciales y finales explicitan esas dependencias y evitan adelantar protocolos clínicos. | **aceptable** | Conservar. El uso perceptual de reverberación en U7 y su formalización en U9 coincide con el mapa. |
| CG07-04 | Terminología | El programa escribe “Hass”; libro, glosario y decisiones corrigen a Haas y lo distinguen de precedencia. | Usa efecto de Haas y rechaza la regla universal de 20 ms. | **intencional** | Conservar; es una corrección de fuente documentada, no una desviación. |
| CG07-05 | Terminología | El programa habla de diferencia interaural de intensidad; la guía adopta ILD como diferencia de nivel. | Usa “diferencia interaural de nivel” e `ILD`. | **intencional** | Conservar y desarrollar la sigla en la primera aparición. |
| CG07-06 | Terminología | El glosario prefiere “altura tonal (pitch)”: español primero y término inglés después. | Define “altura tonal o pitch”, pero varios títulos posteriores usan solo “pitch”. | **aceptable** | La alternancia es comprensible después de definirla. Preferir “altura tonal” en recapitulaciones y dejar *pitch* como equivalencia bibliográfica. |
| CG07-07 | Terminología | El capítulo usa señal enmascarante/enmascarador; la consistencia requiere una forma estable. | Alterna “máscara” (9 usos) y “enmascarador” (7 usos); no usa “señal enmascarante”. | **inconsistente** | Adoptar “señal enmascarante” o “enmascarador”; evitar “máscara” aislada. La regla quedó agregada al glosario. |
| CG07-08 | Terminología / unidades | El material visible en español usa fon y son; *phon/sone* se reservan para citas. | Predominan fon/sones, pero aparecen 7 usos de *phon* y uno de *sone*. | **inconsistente** | Uniformar texto visible a fon/son sin alterar las referencias bibliográficas. |
| CG07-09 | Definiciones | El glosario separa magnitud física, tarea, respuesta y condiciones. | El marco estímulo → tarea → respuesta se introduce temprano y reaparece de forma consistente. | **aceptable** | Conservar; es la principal continuidad conceptual con U1 y U6. |
| CG07-10 | Definiciones | Una curva isofónica puede ser conceptual o normativa; el carácter debe ser inequívoco. | Los textos mencionan ISO 226, pero la actividad visible no ofrece datos ni una curva y las notas hablan de seguir ejes ausentes. | **inconsistente** | Aplicar D-069: separar visualmente esquema de construcción y curva normativa. |
| CG07-11 | Símbolos | La guía adopta `L_p`, `L_N`, `N_son`, `T_60`, subíndices tipográficos y valor absoluto matemático. | `slide_text.md` usa la notación correcta; el PPTX muestra `L(N)`, `N(son)`, `T(60)` y `abs(Δt(LR))`. | **inconsistente** | Corregir el parser/autor del deck y volver a renderizar. No aceptar paréntesis como sustituto de subíndice. |
| CG07-12 | Símbolos | Campo–tímpano: `G_CT(f)=L_{p,T}-L_{p,campo}`; enmascaramiento: `M(f_obj)` y umbrales con subíndices. | El PPTX muestra `G(CT)(f)`, `M(f(obj))` y `L(umbral),e/q`. | **inconsistente** | Aplicar D-068 y la guía de notación actualizada. Las fórmulas fuente pueden conservarse; el error está en la composición visible. |
| CG07-13 | Símbolos | ITD puede desarrollarse como `Δt_LR`; ILD mantiene el orden izquierda menos derecha. | La definición y el signo de ILD son coherentes, pero la cota de ITD pierde subíndices y usa `abs`. | **inconsistente** | Mostrar `\lvertΔt_{LR}\rvert≈d/c`; conservar la explicación de que es una cota didáctica. |
| CG07-14 | Unidades | Coma decimal, espacio valor–unidad, prefijos SI y referencias explícitas. | Usa `0,180 m`, `343 m·s⁻¹`, `525 µs`, dB SPL, fon, son y porcentajes de manera dimensionalmente coherente. | **aceptable** | Conservar. Unificar el glifo micro en todo el deck durante la corrección tipográfica. |
| CG07-15 | Fórmulas — tratamiento | Toda fórmula debe tener contexto, símbolos, unidades, significado y límite. | Las relaciones centrales incluyen interpretación y condiciones; la secuencia concepto → fórmula → ejemplo coincide con U2–U6. | **aceptable** | Mantener la estructura conceptual. La inconsistencia está en la composición y en el ejemplo, no en la selección de fórmulas. |
| CG07-16 | Fórmulas — implementación | La guía prefiere OMML para ecuaciones estructuradas; D-048 admite texto Cambria Math en ejemplos y el decision log mantiene pendiente el umbral técnico. | U7 usa texto editable Cambria Math y no contiene OMML, igual que U1–U6. | **requiere decisión** | No corregir solo U7. Definir una política global por tipo de ecuación y retrocorregir solo cuando exista una herramienta estable. |
| CG07-17 | Ejemplos | `FA_10_EJEMPLO_RESUELTO` exige datos → relación → sustitución → resultado → chequeo. U2, U4 y U5 modelan esos pasos en sus mejores ejemplos. | 24, 51, 58, 81, 91 y 105 muestran resultado y límite, pero repiten “Aplique la relación…” en el panel de significado. | **inconsistente** | Rehacer los ejemplos centrales con pasos visibles; no alterar la cantidad de ejemplos por homogeneidad. |
| CG07-18 | Gráficos | Fondo blanco, ejes y unidades, rejilla gris, curva bordó/teal, anotación de lectura y fuente. | 14, 15, 26, 36, 50, 60–61, 64 y 84 siguen la paleta y el tratamiento de U4/U6. | **aceptable** | Conservar el estilo. Mejorar la lectura específica de cada gráfico, especialmente isofónicas y `T_60`. |
| CG07-19 | Gráficos | U5 puede ser más gráfico y usar ritmos distintos, pero su antigua paleta no es baseline global. | U7 no copia el azul–verde–violeta dominante de U5 y vuelve a bordó, teal, ocre y gris. | **intencional** | Conservar. Es coherencia con la guía, no falta de continuidad con U5. |
| CG07-20 | Diagramas — semántica | El color debe conservar significado y una diferencia temática puede justificarse. | En el marco psicofísico usa teal para estímulo físico, tinte bordó para tarea/procesamiento, ocre para respuesta y gris para condiciones. | **intencional** | Conservar como excepción funcional D-071; no extenderla a slides sin ese marco. |
| CG07-21 | Diagramas — editabilidad | Diagramas simples deben ser formas/conectores nativos; SVG es admisible para ciencia compleja. | Parte importante de los diagramas aprobados sigue insertada como raster, aunque posee script y alt text. | **inconsistente** | Al corregir 74, 85, 103, 107 y 117, migrar esos diagramas a formas nativas; no convertir por sistema los que no cambien. |
| CG07-22 | Diagramas — causalidad | Los conectores deben expresar orden causal/temporal estable, como en las correcciones finales de U1, U3 y U5. | 74 y 85 colocan la respuesta arriba y las causas como ramas; 103 no muestra la diferencia de recorridos; 107 no representa el cono. | **inconsistente** | Corregir semántica, no solo alineación. Coincide con IP07-05 de la revisión independiente. |
| CG07-23 | Recapitulaciones — frecuencia | U4–U7 requieren pausas más frecuentes que U1–U3. | Incluye recapitulaciones aproximadamente cada 8–12 slides. | **intencional** | Conservar la frecuencia; no igualarla a unidades más cortas. |
| CG07-24 | Recapitulaciones — componente | `FA_C10_MINI_RECAP` pide tres líneas/columnas sin tarjetas separadas y una pregunta de control. | Varias recaps usan tres tarjetas casi idénticas; 45 y 53 repiten la misma organización. | **inconsistente** | Mantener el ritmo, pero convertir algunas recaps en recuperación activa y reducir la estética de tarjetas. |
| CG07-25 | Aplicaciones | La guía y U1–U6 integran conexiones profesionales cerca del concepto que iluminan. | Las aplicaciones fonoaudiológicas fuertes se concentran en 115–118. | **inconsistente** | Distribuir microaplicaciones en umbral, sonoridad, enmascaramiento, inteligibilidad e ITD/ILD. No adelantar protocolos de U8. |
| CG07-26 | Notas — alcance | Las notas amplían, incluyen preguntas, errores, transición y un bloque `[Sources]` por slide. | Hay 134 notes slides, pero cada una contiene dos bloques de fuentes: uno heredado de `speaker_notes.md` y otro añadido al empaquetar; total 268. | **inconsistente** | Conservar un único bloque `[Sources]` y el alt text separado. |
| CG07-27 | Notas — versión y naturalidad | Las unidades finalizadas recientes rotulan las notas como finales/sincronizadas y evitan guías formularias repetidas. | `speaker_notes.md` sigue como “v01”; 50 notas repiten “Señalar el foco principal…” y las 134 repiten “Idea que debe quedar al cerrar”. | **inconsistente** | Sincronizar con v02 y reescribir solo las intervenciones que agreguen valor específico. |
| CG07-28 | Pies y numeración | Pie institucional, wordmark, número dinámico inferior y ausencia de total manual. | El PPTX conserva dos masters, 27 layouts y placeholders `sldNum` en los 27 layouts; los números 1–134 son estables. | **aceptable** | Conservar. No añadir una segunda numeración manual en encabezados. |
| CG07-29 | Navegación | Los rótulos de ruta se usan solo si reflejan una clasificación operativa. | Las 18 complementarias intercaladas mantienen `RUTA CENTRAL`; solo el respaldo está diferenciado. | **inconsistente** | Aplicar D-070: rotular `AMPLIACIÓN`, crear secciones o esconderlas por defecto. |
| CG07-30 | Captions | D-056 exige un caption funcional y prohíbe repetir avisos de producción como “no está a escala”. | El deck visible repite 39 avisos “no está a escala” y 37–39 rótulos “Figura conceptual”. | **inconsistente** | Retirar el texto repetido; conservar solo el límite que cambie la interpretación del visual. |
| CG07-31 | Créditos | D-066 reserva códigos internos para notas/manifiesto y pide créditos legibles por personas solo cuando sean necesarios. | 39 slides muestran fórmulas como “Libro del curso (TEX/PDF)… brief, storyboard y planes U07; elaboración propia UCASAL”. | **inconsistente** | Mover trazabilidad interna a notas/manifiesto. En pantalla, dejar autor/organización/licencia cuando exista un asset externo o dato normativo. |
| CG07-32A | Layouts — estructura | El template exige jerarquía real de masters y layouts. | La jerarquía está preservada: 2 masters y 27 layouts. | **aceptable** | Conservar la estructura y editar en el nivel adecuado. |
| CG07-32B | Layouts — uso | El layout se elige por función y no debe convertirse en una grilla de tarjetas por defecto. | Muchas slides construyen grillas de tarjetas dentro de layouts genéricos. | **inconsistente** | Corregir únicamente recaps, comparaciones y procesos cuyo componente contradice el catálogo. |
| CG07-33 | Paleta | Bordó institucional, teal físico, ocre perceptual/clínico, gris neutral, fondos blanco/marfil. | Los colores dominantes del XML son precisamente `#4D1434`, `#903163`, `#2F7E83`, `#9F541A`, `#969FA7` y carbón. | **aceptable** | Conservar. No intentar parecerse a la paleta excepcional de U5. |
| CG07-34 | Tipografía | Calibri Light para títulos, Calibri para texto y Cambria Math para fórmulas; tamaños de aula. | Usa solo esas familias principales y mantiene títulos/cuerpo legibles en los 134 renders. | **aceptable** | Conservar familias y escala. La notación matemática debe corregirse sin cambiar la fuente. |
| CG07-35 | Color de títulos | La guía escrita dice carbón; varias unidades consolidadas usan bordó. El decision log mantiene la decisión abierta. | U7 usa títulos bordó de forma sistemática. | **requiere decisión** | No corregir solo U7. Elegir una convención global y aplicarla en una revisión transversal posterior. |
| CG07-36 | Multimedia / notas | El componente de media puede ser opcional, pero las instrucciones deben apuntar a archivos existentes y probados. | Ocho medios figuran como `proposed`, sin ruta local; las notas indican reproducir varios. | **inconsistente** | Producirlos o retirar la instrucción. La alternativa estática puede conservarse como respaldo. |

## Síntesis por clasificación

### Intencionales

- profundidad y extensión de cuatro encuentros;
- mayor frecuencia de recapitulaciones;
- corrección Haas/Hass;
- uso de ILD como diferencia de nivel;
- retorno a la paleta canónica frente a la excepción visual de U5;
- marco estímulo → tarea → respuesta → condiciones y su color semántico acotado.

Estas diferencias no deben homogeneizarse.

### Aceptables

- continuidad curricular con U4–U6 y puente a U8–U10;
- uso posterior de *pitch* después de definir altura tonal;
- unidades y consistencia dimensional;
- tratamiento conceptual de fórmulas;
- estilo general de gráficos;
- masters, layouts, pies, numeración, paleta y tipografía.

### Inconsistentes

- ausencia de la curva isofónica que exige la actividad;
- terminología enmascarador/máscara y fon/phon;
- subíndices convertidos en paréntesis y `abs(...)` visible;
- ejemplos sin procedimiento completo;
- diagramas raster o con causalidad ambigua;
- recaps en tarjetas repetidas y aplicaciones tardías;
- duplicación y versión obsoleta de notas;
- complementarias rotuladas como ruta central;
- captions y créditos de producción repetidos;
- instrucciones a multimedia inexistente.

### Requieren decisión

1. **OMML frente a texto Cambria Math.** La inconsistencia es global: U1–U7 usan texto editable y cero objetos OMML pese a la preferencia escrita. No corresponde corregir una sola unidad.
2. **Color de títulos.** Carbón en la guía, bordó en la práctica consolidada. Mantener U7 hasta una decisión transversal.

## Actualizaciones realizadas a las referencias globales

### `style/glossary.md`

- Se aclaró la diferencia entre curva isofónica conceptual y normativa.
- Se añadieron psicoacústica, fon, señal enmascarante/enmascarador, filtro auditivo, ERB, enmascaramiento temporal, energético e informacional, inteligibilidad, ALCons, audición binaural y efecto cocktail party.
- Se ampliaron SNR, precedencia, ITD e ILD con condiciones y límites coherentes con el capítulo.
- Se fijó fon/son en español y se desaconsejó “máscara” aislada.

### `style/notation_guide.md`

- Se prohibió convertir subíndices en paréntesis o valor absoluto en `abs(...)`.
- Se añadió `G_CT(f)` para campo–tímpano.
- Se añadieron umbrales en quietud/enmascarado y `M(f_obj)`.
- Se fijó `N_son`, la forma equivalente de SNR por diferencia de niveles, ALCons con conteos, `Δt_LR`, ILD y `ERB_N(f_c)`.

### `style/decision_log.md`

- D-068: notación y unidades psicoacústicas.
- D-069: distinción curva isofónica conceptual/normativa.
- D-070: uso operativo de rótulos de ruta y ampliación.
- D-071: marco y color semántico de U7 como excepción pedagógica justificada.

## Problemas abiertos para U7

1. Corregir CG07-01, 07–13, 17, 21–22, 24–27, 29–31 y 36 en una siguiente versión del deck.
2. Volver a renderizar todas las slides con notación, captions, créditos o navegación modificados.
3. Revisar individualmente 23–24, 29–30, 45–53, 57–58, 74, 84–86, 103–107, 117 y 122–131.
4. Mantener abiertas las decisiones globales de OMML y color de títulos; no bloquear solo U7 por ellas.
5. Actualizar el renglón de notación de U7 en `course_map.md` de `N` a `N_son` en una futura pasada de `course-architecture`; no se modificó el mapa desde esta revisión para no mezclar mantenimiento curricular con consistencia de la unidad.

## Verificación

- Se inspeccionaron el template y los contact sheets finales de U1–U7.
- Se compararon los siete PPTX mediante lectura del paquete OOXML.
- U7 conserva 134 slides, 134 notes slides, 2 masters, 27 layouts, 27 placeholders de numeración y las tres familias tipográficas canónicas.
- Se contrastaron términos, símbolos, unidades, captions, créditos, rutas y notas contra los archivos fuente y el render.
- Se verificaron las tablas Markdown y las nuevas decisiones globales después de editar la documentación.
