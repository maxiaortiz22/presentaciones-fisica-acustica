# Unidad 7 — Análisis de fuentes

## Jerarquía aplicada

1. `context/programa/Programa de Física Acústica.pdf` — alcance obligatorio; programa 2025, p. 4.
2. `context/libro_latex/chapters/07-psicoacustica.tex` — fuente editable y estructural principal.
3. `context/libro_pdf/Física Acústica para Fonoaudiología.pdf` — versión maquetada; capítulo 7, pp. 177–205.
4. `course_map.md`, `course_dependency_map.md` y `content_coverage_matrix.csv` — arquitectura, dependencias y estado de cobertura.
5. `style/presentation_style_guide.md`, `style/notation_guide.md` y `style/glossary.md` — criterios visuales, de notación y terminología.
6. `context/libro_latex/bibliography/references.bib` — trazabilidad de las fuentes técnicas ya citadas por el capítulo.

No se incorporaron fuentes externas nuevas en esta etapa. Cuando el programa exige contenido normativo o una definición que el capítulo solo trata parcialmente, se registra la necesidad de verificación posterior en lugar de completarla silenciosamente.

## Disponibilidad y método de revisión

| Fuente | Estado | Revisión realizada | Limitación |
|---|---|---|---|
| Programa oficial | Disponible, 6 páginas | Extracción textual completa y verificación visual de la p. 4 | Enumera temas, pero no define profundidad ni secuencia. Usa “Hass” e “intensidad” en formulaciones que requieren precisión terminológica. |
| Capítulo LaTeX U7 | Disponible, 1506 líneas | Lectura completa: propósito, desarrollo, ecuaciones, figuras, ejercicios, soluciones y glosario | Las isofónicas numéricas se dejan pendientes de datos normativos; ruido y `T_60` se remiten parcialmente a U10/U9. |
| Libro PDF | Disponible, 296 páginas | Identificación y renderizado visual completo de pp. 177–205 | Es material vertical de lectura; texto y figuras no pueden copiarse directamente a 16:9. |
| Arquitectura curricular | Disponible | Lectura de U7 y dependencias globales; revisión de todas las filas U07 de la matriz | La matriz marca ERB fuera de alcance y `T_60` parcial; requiere decidir su peso en la unidad. |
| Guías de estilo/notación/glosario | Disponibles | Lectura completa de los tres documentos solicitados | Hay tensiones entre términos/símbolos del LaTeX y las convenciones transversales. |
| Figuras propias U7 | Nueve fuentes TikZ | Inventario en LaTeX y verificación en PDF | Correctas como esquemas de libro, pero pequeñas y densas para aula. |
| Imágenes raster previas | `FletcherMunson.png`, `enmascaramiento.png` | Localizadas en `context/libro_latex/figures/` | Origen, licencia, vigencia normativa y función pedagógica no están verificados. |
| Guía de ejercicios independiente | No localizada | El capítulo contiene banco completo y soluciones | No hay evidencia local de parciales, recuperatorios ni criterios docentes de selección. |
| Deck previo de U7 | No localizado | `units/unit_07/` solo contenía `.gitkeep` | No existe una secuencia previa específica que preservar. |

## Alcance obligatorio extraído del programa

La formulación original de la Unidad 7 se agrupa para análisis sin eliminar ningún tema:

| Grupo programático | Elementos obligatorios |
|---|---|
| Marco general | Características subjetivas de la percepción auditiva y psicoacústica. |
| Umbral y sensibilidad | Curvas isofónicas normalizadas; umbral absoluto; umbral de audibilidad; máxima sensibilidad. |
| Oído externo y campo | Resonancia del canal auditivo; diferencia entre nivel de presión sonora en tímpano y campo libre. |
| Atributos | Altura/pitch, duración subjetiva, timbre y sonoridad. |
| Escalas de sonoridad | Nivel de sonoridad, nivel de presión sonora, fones y sones. |
| Enmascaramiento y ambiente | Enmascaramiento; concepto de ruido y tiempo de reverberación. |
| Voz | Voz humana, sonoridad e inteligibilidad; pérdida de articulación de consonantes. |
| Reflexiones | Efecto “Hass”; percepción del sonido reflejado. |
| Escena y espacio | Efecto cocktail; mecanismo de localización; audición binaural; diferencia interaural de tiempo e intensidad. |

## Comparación programa–LaTeX–PDF

| Tema | Programa | LaTeX | PDF | Evaluación |
|---|---|---|---|---|
| Psicoacústica | Exigida | Marco estímulo–tarea–respuesta y condiciones | 7.1–7.3, pp. 177–179 | Cubierta y pedagógicamente fortalecida. |
| Curvas isofónicas normalizadas | Exigidas | Define procedimiento y límites; figura conceptual, no datos normativos | 7.5, p. 182 | Cobertura conceptual; curva numérica requiere ISO 226:2023 verificada. Estado de ampliación externa. |
| Umbral absoluto/audibilidad | Exigidos | Definición operacional, criterio y variabilidad | 7.4.1, pp. 179–180 | Cubiertos con mayor precisión. |
| Máxima sensibilidad | Exigida | Región de menor umbral en frecuencias medias, sin valor universal | 7.4.1, pp. 179–180 | Cubierta. |
| Resonancia del canal auditivo | Exigida | Recupera U6 y la integra en transferencia campo–tímpano | 7.4.2, pp. 180–181 | Cubierta; no repite el modelo anatómico completo. |
| Campo libre vs tímpano | Exigido | Define `G_CT(f)` y ejemplo de dos posiciones | 7.4.2–7.4.3, pp. 180–181 | Cubierto y cuantificado. |
| Pitch | Exigido | Atributo, periodicidad, espectro, nivel, contexto y fundamental ausente | 7.6.1, p. 183 | Cubierto y ampliado. |
| Duración subjetiva | Exigida | Duración percibida, resolución e integración temporal | 7.6.4, pp. 183–184 | Cubierta y ampliada. |
| Timbre | Exigido | Espectro, envolvente, ataque, decaimiento, ruido y tiempo | 7.6.3, p. 183 | Cubierto con enfoque multidimensional. |
| Sonoridad | Exigida | Atributo dependiente de múltiples variables | 7.6.2, p. 183 | Cubierta. |
| Nivel de sonoridad vs `L_p` | Exigido | Diferencia explícita entre `L_p`, `L_N` y sonoridad | 7.7, pp. 184–185 | Cubierto. |
| Fones y sones | Exigidos | Definiciones, modelo y ejemplo | 7.7–7.7.1, pp. 184–185 | Cubiertos; terminología y símbolo necesitan armonización con las guías. |
| Enmascaramiento | Exigido | Elevación de umbral, simultáneo, temporal, filtros, energético/informacional | 7.8, pp. 185–188 | Cubierto y ampliamente expandido. |
| Concepto de ruido | Exigido junto a reverberación | El ruido aparece como enmascarador/interferencia y en SNR, pero no recibe una definición general autónoma | 7.8–7.12, pp. 185–194 | Cobertura funcional parcial; la definición y clasificación son propiedad de U10. |
| Tiempo de reverberación | Exigido | Se define el efecto de reflexiones sucesivas y se remite la física a U9; no se formaliza `T_60` | 7.9.2, p. 189 | Parcial deliberada; conviene introducir el descriptor sin cálculo y conservar formalización para U9. |
| Voz humana | Exigida | Habla como señal objetivo, material lingüístico y fuentes concurrentes | 7.9 y 7.12, pp. 189–194 | Cubierta funcionalmente; no desarrolla producción vocal, que no es el foco. |
| Sonoridad e inteligibilidad | Exigidas | Sonoridad se desarrolla antes; inteligibilidad se vincula con SNR, reverberación, tarea y oyente | 7.6–7.9 | Cubiertas sin equivalencia causal simple. |
| Pérdida de articulación | Exigida | Define ALCons, ecuación, ejemplo y límites | 7.9.3–7.9.4, pp. 189–190 | Cubierta y cuantificada como porcentaje observado. |
| Efecto “Hass” | Exigido | Corrige a Haas y lo diferencia de precedencia | 7.10, pp. 190–191 | Cubierto con corrección terminológica necesaria. |
| Sonido reflejado | Exigido | Retardo geométrico y respuestas perceptuales dependientes de condiciones | 7.10, pp. 190–191 | Cubierto y ampliado. |
| Efecto cocktail | Exigido | Escena con segregación, atención y enmascaramiento | 7.12, pp. 193–194 | Cubierto y corregido como fenómeno multicomponente. |
| Localización | Exigida | ITD, ILD, pistas espectrales, cono y movimiento | 7.11, pp. 191–193 | Cubierta y ampliada. |
| Audición binaural | Exigida | Comparación de señales disponibles en ambos oídos | 7.11.1, pp. 191–192 | Cubierta. |
| Diferencia interaural de tiempo | Exigida | ITD y modelo geométrico | 7.11.1–7.11.2, pp. 191–192 | Cubierta y cuantificada. |
| Diferencia interaural de intensidad | Exigida | Se usa ILD, diferencia interaural de nivel | 7.11.1, p. 192 | Cubierta con terminología físicamente más precisa. |

## Correspondencia LaTeX–PDF

### Verificación estructural

| Sección LaTeX | PDF | Resultado |
|---|---:|---|
| 7.1 Propósito y resultados | 177–178 | Presente. |
| 7.2 Conocimientos previos | 178 | Presente. |
| 7.3 Estímulo a respuesta | 178–179 | Presente. |
| 7.4 Umbral, audibilidad y sensibilidad | 179–181 | Presente; figuras 7.1 y 7.2. |
| 7.5 Curvas de igual sonoridad | 182 | Presente; figura 7.3 conceptual. |
| 7.6 Atributos perceptuales | 183–184 | Presente. |
| 7.7 Fones y sones | 184–185 | Presente; figura 7.4 y ejemplo. |
| 7.8 Enmascaramiento y filtros | 185–188 | Presente; figuras 7.5 y 7.6. |
| 7.9 Voz, reverberación e inteligibilidad | 189–190 | Presente; ecuaciones SNR y ALCons. |
| 7.10 Reflexiones y precedencia | 190–191 | Presente; figura 7.7 y ejemplo. |
| 7.11 Audición espacial | 191–193 | Presente; figura 7.8 y modelo ITD. |
| 7.12 Fuentes concurrentes | 193–194 | Presente; figura 7.9. |
| 7.13 Relación con Fonoaudiología | 195 | Presente. |
| 7.14 Errores frecuentes | 195–196 | Presente. |
| 7.15 Síntesis | 196 | Presente. |
| 7.16 Ejercicios | 196–200 | Presente. |
| 7.17 Soluciones | 200–204 | Presente. |
| 7.18 Glosario | 204–205 | Presente. |

No se detectaron diferencias sustantivas entre el LaTeX revisado y las páginas correspondientes del PDF. El PDF confirma contenido, flujo de figuras y legibilidad editorial; el LaTeX sigue siendo la fuente textual y estructural principal.

### Verificación visual

Se renderizaron e inspeccionaron las 29 páginas del capítulo, 177–205. La versión PDF:

- contiene las nueve figuras propias sin cortes visibles;
- conserva ecuaciones, unidades, captions, ejercicios, soluciones y glosario;
- no presenta imágenes rotas ni páginas faltantes;
- rotula las figuras conceptuales como no normativas cuando corresponde;
- muestra una maquetación correcta para libro.

La revisión también confirma que la maquetación no es transferible directamente a PowerPoint:

- las figuras 7.5, 7.7, 7.8 y 7.9 reúnen demasiadas relaciones y rótulos pequeños para media slide;
- los bloques de atributos, errores y ejercicios son demasiado densos para una única slide;
- las curvas cualitativas necesitan ejes y condiciones más visibles en aula;
- los diagramas deben reconstruirse como objetos editables y, en varios casos, dividirse por etapas.

## Fórmulas, magnitudes y ejemplos localizados

| Elemento | LaTeX | PDF | Evaluación |
|---|---|---|---|
| `G_CT(f)=L_p,T−L_p,campo` | 7.4.2 | p. 180 | Correcta como diferencia de niveles; no es dB SPL ni sonoridad. |
| Ejemplo 50/58 dB SPL | 7.4.3 | p. 181 | `8 dB`; central para posición de medición. |
| `N=2^[(L_N−40 phon)/(10 phon)] sone` | 7.7 | p. 184 | Modelo acotado; notación/terminología a armonizar. |
| Ejemplo `70 phon → 8 sone` | 7.7.1 | p. 184 | Útil si se diferencia de `70 dB SPL`. |
| `M=L_umbral,e−L_umbral,q` | 7.8.1 | p. 186 | Correcta como elevación; `f_s` colisiona con muestreo de U5. |
| `ERB_N(f_c)` | 7.8.3 | p. 186 | Modelo de Glasberg–Moore; ampliación fuera del programa. |
| Ejemplo ERB a 1000 Hz | 7.8.4 | pp. 186–187 | `≈133 Hz`; no ancho clínico universal. |
| `SNR=L_p,s−L_p,n` | 7.9.1 | p. 189 | Requiere condiciones compatibles; no predice sola inteligibilidad. |
| `ALCons=100(1−n_c/n_p)%` | 7.9.3 | p. 189 | Porcentaje observado, no modelo causal. |
| Ejemplo ALCons 68/80 | 7.9.4 | p. 190 | `15 %`; central para límites de inferencia. |
| `Δt=Δr/c` | 7.10 | p. 190 | Correcta dimensionalmente; percepción depende de otras variables. |
| Ejemplo `3,43 m → 10,0 ms` | 7.10.1 | p. 191 | Central para separar cálculo y efecto perceptual. |
| `ILD=L_p,L−L_p,R` | 7.11.1 | p. 192 | Diferencia de nivel; orden de resta a declarar. |
| `abs(Δt_LR)≈d/c` | 7.11.2 | p. 192 | Modelo rectilíneo de orden de magnitud. |
| Ejemplo `d=0,180 m` | 7.11.2 | p. 192 | `0,525 ms`; no constante anatómica. |

## Ampliaciones del libro respecto del programa

- marco estímulo–tarea–respuesta y criterios de interpretación;
- carácter probabilístico del umbral;
- cautela de seguridad sobre niveles elevados;
- definición cuantitativa de transferencia campo–tímpano;
- procedimiento de construcción de una isofónica;
- fundamental ausente;
- resolución e integración temporal;
- modelo explícito fon–son;
- elevación del umbral;
- patrones de enmascaramiento y filtros auditivos;
- banda crítica y ERB;
- enmascaramiento simultáneo, hacia adelante y hacia atrás;
- distinción energético/informacional;
- SNR con condiciones de comparabilidad;
- STI y SII como métodos diferentes;
- ALCons como porcentaje observado;
- precedencia como familia y Haas como resultado histórico acotado;
- modelo geométrico de retardo e ITD;
- pistas espectrales, cono de confusión y movimiento;
- segregación, atención y liberación espacial del enmascaramiento;
- banco graduado de ejercicios, aplicaciones, distractores y soluciones.

Estas ampliaciones son pertinentes, pero ERB, STI/SII, integración temporal avanzada y liberación espacial no necesitan el mismo peso visible que el alcance obligatorio.

## Diferencias, tensiones y vacíos documentales

### 1. Isofónicas “normalizadas” frente a figura conceptual

- Programa: exige curvas isofónicas normalizadas.
- LaTeX/PDF: explican el concepto y muestran una figura de construcción sin datos normativos.
- Referencia local: `ISO 226:2023`, tercera edición.
- Evaluación: no se puede presentar una curva numérica normativa a partir del esquema actual. Antes del storyboard debe definirse si se incorporarán datos autorizados de ISO 226:2023, con condiciones y trazabilidad, o si la ruta central conservará una curva conceptual y la normativa quedará como respaldo.

### 2. “Umbral absoluto” y “umbral de audibilidad”

- Programa: los enumera por separado.
- Libro: usa umbral absoluto y campo audible; no los convierte en dos cantidades universales diferentes.
- Evaluación: conviene explicar la relación terminológica y evitar una duplicación artificial de contenido.

### 3. “Máxima sensibilidad del oído”

- Programa: formulación general.
- Libro: región de menor nivel umbral bajo condiciones definidas.
- Evaluación: usar “región de máxima sensibilidad” y declarar frecuencia, campo, población y procedimiento; no presentar una frecuencia única universal.

### 4. Resonancia del “canal” frente a transferencia del CAE

- Programa: efecto de resonancia del canal auditivo.
- Libro: integra resonancia con pabellón, concha, geometría, dirección y posición de medición.
- Evaluación: la resonancia debe tratarse como parte de una transferencia dependiente de frecuencia, no como una ganancia fija.

### 5. Fon/son y `phon`/`sone`

- Programa y glosario transversal: fones y sones; unidad visible “fon” y “son”.
- LaTeX/PDF: texto en español, pero símbolos/unidades `phon` y `sone` en ecuación y figura.
- Evaluación: debe fijarse una convención visible antes del storyboard y conservar equivalencias inglesas solo para bibliografía.

### 6. Símbolo de sonoridad `N`

- LaTeX: `N`.
- Guía transversal: `N_son` si puede colisionar con número de muestras `N` de U5.
- Evaluación: adoptar `N_son` en U7 mejora continuidad y evita reusar el símbolo recién aprendido.

### 7. Frecuencia de objetivo `f_s`

- LaTeX: `f_s` para frecuencia de la señal objetivo en enmascaramiento.
- Guía/U5: `f_s` es frecuencia de muestreo.
- Evaluación: colisión transversal importante. Se recomienda `f_obj` para el objetivo.

### 8. ERB y banda crítica

- Programa: no las exige.
- Libro: proporciona modelo y ecuación.
- Matriz: U07-X1 figura `out_of_scope` como ampliación.
- Evaluación: el modelo de filtros es útil para explicar enmascaramiento, pero el cálculo de ERB puede ser complementario. Debe decidirse antes de estimar la ruta central.

### 9. Concepto de ruido

- Programa: “Concepto de ruido y tiempo de reverberación”.
- Libro U7: usa ruido como enmascarador o interferencia, pero posterga tipos y caracterización física a U10.
- Glosario: la definición formal de ruido se ubica en U10.
- Evaluación: U7 necesita una definición funcional breve vinculada con la tarea, sin adelantar la taxonomía ni la estadística.

### 10. Tiempo de reverberación

- Programa: exige el concepto.
- Libro U7: describe reverberación y sus efectos, pero no define ni calcula `T_60`; remite U9.
- Matriz: estado `partial`.
- Evaluación: incluir como mínimo una definición conceptual de `T_60`, su unidad y su carácter de descriptor, sin fórmula de Sabine ni cálculo normativo. La formalización queda en U9.

### 11. Sonoridad e inteligibilidad de la voz

- Programa: las menciona juntas.
- Libro: desarrolla sonoridad como atributo y luego inteligibilidad como desempeño de identificación.
- Evaluación: no deben fundirse en una sola relación causal. Una voz más sonora no es automáticamente más inteligible.

### 12. ALCons observado frente a predicción acústica

- Programa: exige el concepto.
- Libro: define el porcentaje observado y advierte contra modelos no verificados.
- Evaluación: mantener el cálculo observado como núcleo; cualquier fórmula predictiva de sala requiere fuente y dominio explícitos y no es necesaria aquí.

### 13. “Hass” frente a Haas/precedencia

- Programa: grafía “Hass”.
- Libro, glosario y bibliografía: Haas y efecto de precedencia.
- Evaluación: corregir la grafía en contenido visible y conservar la formulación original solo en trazabilidad. Rechazar una regla universal de 20 ms.

### 14. “Diferencia interaural de intensidad” frente a ILD

- Programa: intensidad.
- Libro/guía: diferencia de niveles medidos en ambos oídos, ILD.
- Evaluación: enseñar **diferencia interaural de nivel**; explicar que una diferencia en dB no es una resta de intensidades lineales.

### 15. Título y capitalización

- Programa: “Características subjetivas de la percepción auditiva (psicoacústica)”.
- LaTeX/PDF: misma formulación con “Psicoacústica” capitalizada.
- Evaluación: diferencia editorial menor; conviene adoptar el título oficial con capitalización consistente en portada y metadatos.

## Qué puede pasar casi directamente a diapositivas

- propósito y marco estímulo–tarea–respuesta;
- cuatro pares físico–perceptuales;
- definición de umbral y advertencia de condiciones;
- campo–tímpano, ecuación y ejemplo;
- construcción conceptual de isofónicas;
- definiciones de atributos, fragmentadas;
- fon/son, ecuación y ejemplo con límites;
- elevación del umbral y clasificación temporal;
- energético frente a informacional;
- SNR y ALCons con interpretación;
- cálculo de retardo frente a resultados perceptuales;
- ITD/ILD y pistas adicionales;
- escena de fuentes concurrentes;
- aplicaciones, errores, síntesis y pregunta integradora.

Las ideas son transferibles; la redacción extensa y las figuras de libro no lo son.

## Qué necesita más explicación o recursos

| Contenido | Necesidad | Motivo |
|---|---|---|
| Umbral | Gráfico/actividad probabilística | La definición verbal no basta para desmontar una frontera rígida. |
| Isofónicas | Datos normativos o decisión explícita de esquema | El programa exige normalización; el visual actual no contiene datos. |
| Pitch/timbre/duración | Audio + visual equivalente | Son atributos que se comprenden mejor por contraste controlado. |
| Fones/sones | Gráfico grande y tabla de tres escalas | Alto riesgo de confundir `L_p`, `L_N` y sonoridad. |
| Enmascaramiento | Varios gráficos y líneas temporales | Elevación, patrón, filtro, ERB y orden temporal no caben juntos. |
| Ruido/reverberación | Caso de aula + frontera U9/U10 | Evitar adelantar física de recintos y ruido. |
| ALCons | Ejemplo y discusión causal | El porcentaje puede parecer diagnóstico o fórmula predictiva. |
| Precedencia/Haas | Audio controlado + diagrama por etapas | Una regla temporal fija sería incorrecta. |
| Audición espacial | Construcción acumulativa y posiblemente animación | ITD, ILD, espectro, movimiento y ambigüedad compiten simultáneamente. |
| Fuentes concurrentes | Escena integrada y actividad | Debe separarse mezcla física de selección perceptual. |

## Implicancias de estilo, notación y glosario

- U7 requiere una idea dominante por slide, bloques cortos y recapitulaciones frecuentes.
- Teal puede representar estímulo/medición física y ocre respuesta perceptual cuando la comparación sea central; no depender solo del color.
- Las futuras curvas deben distinguir “normativa con fuente” de “esquema conceptual; no usar para lectura normativa”.
- Los gráficos necesitan ejes con magnitud, símbolo, unidad y escala explícita.
- Las ecuaciones deben conservar símbolo, unidad, significado, ejemplo y dominio de validez.
- Se recomienda `N_son`, `f_obj`, fon y son para armonizar con las guías.
- `L_p`, `L_N`, `N_son`, `M`, SNR, ALCons, ITD e ILD no son intercambiables.
- No usar “volumen” como término técnico de sonoridad.
- Desarrollar siglas en primera aparición por unidad.
- Los diagramas estructurales deberán reconstruirse de forma editable y pasar por validación renderizada en una etapa posterior.
- Toda experiencia auditiva necesita alternativa visual y no puede depender de niveles extremos ni de una reproducción no controlada.

## Coherencia con la arquitectura del curso

`course_map.md` y `course_dependency_map.md` clasifican U7 como carga muy alta por la combinación de:

- niveles y campo de U4;
- espectro y filtros de U5;
- transferencia y codificación periférica de U6;
- psicofísica, habla y escucha espacial propias de U7.

La estrategia global recomendada —umbral/sensibilidad; atributos/sonoridad; enmascaramiento; voz/recinto; reflexiones; espacio/escenas— se conserva y se amplía a nueve bloques preliminares para separar fones/sones, precedencia e integración. La recapitulación común será:

```text
estímulo → tarea → respuesta → condiciones → límite de inferencia
```

U7 prepara U8, U9 y U10, pero debe respetar fronteras:

- U8: pruebas, diagnóstico y rehabilitación;
- U9: física de recintos y `T_60`;
- U10: caracterización del ruido y técnica de enmascaramiento aplicada.

## Fuentes técnicas ya citadas por el capítulo

| Clave | Fuente | Uso principal en U7 |
|---|---|---|
| `iso226_2023` | ISO 226:2023, 3.ª edición | Umbral e isofónicas normalizadas. |
| `oxenham2018` | Oxenham, *Annual Review of Psychology* (2018) | Percepción/codificación, atributos, umbral y fundamental ausente. |
| `carlini2024` | Carlini, Bordeau y Ambard, *Frontiers in Psychology* (2024) | Transferencia externa, ITD/ILD, pistas espectrales y localización. |
| `asaPhon` | ASA Standards Terminology Database | Definición de phon/fon. |
| `asaSone` | ASA Standards Terminology Database | Definición de sone/son y escala de razón. |
| `glasbergMoore1990` | Glasberg y Moore, *Hearing Research* (1990) | Forma de filtros auditivos y ERB. |
| `moore2008` | Moore, *Philosophical Transactions B* (2008) | Procesos auditivos, enmascaramiento e inteligibilidad. |
| `litovsky1999` | Litovsky et al., JASA (1999) | Efecto de precedencia. |
| `bronkhorst2000` | Bronkhorst, *Acta Acustica* (2000) | *Cocktail party*, habla con múltiples fuentes y enmascaramiento informacional. |
| `iec60268_16_2020` | IEC 60268-16:2020, con corrección 2025 | STI y límites de métodos normativos de inteligibilidad. |
| `moser2009` | Möser, *Engineering Acoustics* (2009) | Reverberación e inteligibilidad/acústica aplicada. |

Estas referencias permiten rastrear el contenido existente. La incorporación de datos normativos, audios o imágenes deberá registrarse más adelante mediante las skills correspondientes.
