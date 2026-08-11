# Informe de consistencia — Unidad 06

**Fecha:** 2026-08-10  
**Deck revisado:** `output/unidad_06_mecanismo_periferico_v02.pptx`  
**Render revisado:** `output/render_v02/` (117 diapositivas)  
**Alcance:** comparación con la guía de estilo, el mapa y las dependencias del curso, el glosario, la guía de notación, el template y las versiones finales de las Unidades 1 a 5.

## Dictamen

La Unidad 6 pertenece visual y estructuralmente al mismo curso: conserva el formato 16:9, los dos masters, la familia de 27 layouts, la paleta académica, Calibri/Calibri Light/Cambria Math, la jerarquía general, las notas con fuentes y la amplitud pedagógica esperada para una unidad densa.

La consistencia es, sin embargo, **parcial**. No por su mayor profundidad —que está justificada— sino por varias desviaciones locales: numeración manual en encabezados, captions y créditos repetidos, códigos internos visibles, abreviaturas antes de desarrollarlas, punto decimal en gráficos, una frase incompatible con conservación de la energía, notación eléctrica no canónica, recapitulaciones demasiado parecidas y notas excesivamente formularias.

No se modificó el deck en esta revisión. Las diferencias pedagógicas justificadas se preservan y se distinguen de los problemas que sí requieren corrección.

## Base de comparación

- `AGENTS.md`.
- `course_map.md`, `course_dependency_map.md` y `course_consistency_report.md`.
- `style/presentation_style_guide.md`, `slide_master_spec.md`, `layout_catalog.md`, `component_catalog.md` y `template_review.md`.
- `style/glossary.md`, `style/notation_guide.md` y `style/decision_log.md`.
- Template renderizado y mosaico general.
- Decks finales, renders e informes de consistencia/revisión de U1, U2, U3, U4 y U5.
- Storyboard, texto visible, notas, manifiesto, revisión integral, revisión pedagógica independiente y decisiones abiertas de U6.
- Inspección OOXML del PowerPoint y revisión del render completo, no solo del texto extraído.

## Comparación estructural

| Unidad | Slides | Masters | Layouts disponibles | Rasgo relevante |
|---|---:|---:|---:|---|
| U1 | 94 | 2 | 27 | Base docente y numeración automática inferior. |
| U2 | 110 | 2 | 27 | Consolidación de notación y ejemplos resueltos. |
| U3 | 96 | 2 | 27 | Mayor carga de diagramas y ecuaciones. |
| U4 | 125 | 2 | 27 | Unidad densa organizada en cuatro sesiones. |
| U5 | 150 | 2 | 27 | Banco con rutas; identificador superior como excepción funcional. |
| U6 | 117 | 2 | 27 | 25 layouts usados; 82 slides centrales, 23 complementarias y 12 de respaldo. |

La cantidad de slides de U6 no constituye por sí misma una anomalía. Está dentro del rango ya aceptado para U4–U5 y responde a la densidad de las Unidades 4–7 indicada en `AGENTS.md`.

## Matriz de diferencias

### Terminología, definiciones y alcance conceptual

| ID | Diferencia | Clasificación | Evidencia y criterio | Acción |
|---|---|---|---|---|
| CG6-01 | El deck emplea CAE, CCI y CCE antes de desarrollar las siglas de manera estable. | **inconsistente** | CAE aparece en la apertura y CCI/CCE en objetivos; la guía exige desarrollar las siglas por unidad. | Desarrollar cada sigla en su primera aparición visible y conservar luego la forma breve. |
| CG6-02 | “Conducto coclear o rampa media” reemplaza la alternancia libre con *scala media*. | **aceptable** | Es más natural para primer año y mantiene la equivalencia bibliográfica. | Convención incorporada al glosario y al registro de decisiones. |
| CG6-03 | U6 define órgano y túnel de Corti con más detalle que U1–U5. | **intencional** | Es contenido propio del mecanismo periférico y está respaldado en las fuentes de U6. | Conservar; validar la anatomía de los visuales, no reducir la definición. |
| CG6-04 | `pitch` aparece antes o sin la forma preferida “altura tonal (pitch)”. | **inconsistente** | El glosario reserva la forma bilingüe para distinguir el percepto de la frecuencia. | Usar “altura tonal (pitch)” en la primera aparición; luego elegir una forma estable. |
| CG6-05 | “Reclutar una región” puede confundirse con reclutamiento auditivo clínico. | **inconsistente** | U7–U8 reutilizarán “reclutamiento” con un significado clínico específico. | Reemplazar por “extender la región de excitación” o “activar una población más amplia”. |
| CG6-06 | Las OEA se anticipan en U6 aunque el mapa las vinculaba principalmente con U8. | **intencional** | En U6 funcionan como evidencia del mecanismo activo de las CCE; no se desarrolla aún la interpretación diagnóstica. | Conservar el anticipo y reservar la lectura clínica completa para U8. El glosario ahora registra primera aparición en U6. |
| CG6-07 | Se usa PEACT mientras la documentación global conserva PEAT/PEATC/ABR como forma pendiente. | **requiere decisión** | No hay una sigla institucional validada. | La cátedra debe elegir una forma; hasta entonces, desarrollar el término completo y evitar fijar una sigla local. |
| CG6-08 | La formulación “las CCE generan energía mecánica” sugiere creación de energía. | **inconsistente** | Contradice la conservación de la energía trabajada en U2. | Escribir que las CCE convierten energía electroquímica en trabajo mecánico y modifican la respuesta coclear. |
| CG6-09 | La unidad distingue mecanismo físico, correlato neural y percepto. | **aceptable** | Respeta la frontera con U7 y evita identificar frecuencia con pitch o nivel con sonoridad. | Conservar esta separación. |
| CG6-10 | Conducción ósea se presenta como fenómeno multimecanismo. | **aceptable** | Coincide con el glosario y evita reducirla a una única vía. | Conservar. |

### Símbolos, fórmulas, unidades y gráficos

| ID | Diferencia | Clasificación | Evidencia y criterio | Acción |
|---|---|---|---|---|
| CG6-11 | U6 usa `S_TM`, `S_E`, `R_S`, `R_L`, `M_p` y `G_p`, mientras el mapa antiguo enumera `A`, `R_A` y `R_p`. | **inconsistente** | La notación del deck evita la colisión de `R_p` con reflexión de presión y es físicamente más explícita, pero el mapa quedó desactualizado. | Mantener la convención de U6, ya registrada en la guía; actualizar el mapa mediante `course-architecture` en una tarea global. |
| CG6-12 | `G_p=20 log₁₀(M_p)` se presenta como expresión en dB de una razón de presiones, no como dB SPL. | **aceptable** | Distingue razón adimensional, nivel y energía; conserva el factor 20 para amplitudes compatibles. | Conservar y nombrar siempre las presiones comparadas. |
| CG6-13 | El modelo `f_res≈c/(4ℓ)` incluye magnitudes, unidades y límites del cuarto de onda. | **aceptable** | Sigue el tratamiento de fórmulas de U2–U5: contexto, símbolos, unidades, cálculo e interpretación. | Conservar. |
| CG6-14 | La fuerza `F≈Δp·S` se relaciona con el puente mecánico de U2. | **aceptable** | La aproximación y el área efectiva están declaradas. | Conservar; precisar el orden de `Δp`. |
| CG6-15 | Algunos gráficos conceptuales usan `0.25`, `0.50`, `0.75`. | **inconsistente** | La guía de notación exige coma decimal en español: `0,25`, `0,50`, `0,75`. | Regenerar o editar los ejes de las slides afectadas. |
| CG6-16 | En electrofisiología aparece `V(ref)`. | **inconsistente** | La referencia no queda expresada con una convención reutilizable. | Usar `ΔV` entre dos puntos o `V_ref` con la referencia nombrada, según la magnitud. |
| CG6-17 | Los gráficos normalizados declaran su carácter conceptual y no simulan datos clínicos. | **aceptable** | La cautela es coherente con el curso y evita falsa precisión. | Conservar el carácter conceptual; reducir captions redundantes. |
| CG6-18 | Una misma familia de curvas se repite con cambios mínimos en varias slides. | **inconsistente** | La repetición deja de aportar una nueva lectura y reduce la variedad visual respecto de U4–U5. | Unificar en una secuencia progresiva o reemplazar repeticiones por anotaciones/detalles distintos. |

### Profundidad, ejemplos, recapitulaciones y aplicaciones

| ID | Diferencia | Clasificación | Evidencia y criterio | Acción |
|---|---|---|---|---|
| CG6-19 | U6 es más profunda que U1–U3 y contiene más recapitulaciones. | **intencional** | U6 es una de las unidades densas señaladas por `AGENTS.md`; integra mecánica, fluidos, electroquímica y codificación periférica. | No recortar para igualar cantidad o ritmo con U1–U3. |
| CG6-20 | Parte de la electroquímica y de la medición periférica supera el mínimo literal del programa. | **requiere decisión** | El contenido prepara U7–U8, pero no todo necesita pertenecer a la ruta central. | Decidir qué queda central y qué pasa a complemento/respaldo; no eliminar por defecto. |
| CG6-21 | La ruta central no está dividida en sesiones visibles como U4 ni usa rutas explícitas como U5. | **requiere decisión** | 82 slides centrales y unas 394 min estimadas exceden una clase única razonable. | Definir sesiones o bloques de dictado y hacer visible la navegación si el deck se usará completo. |
| CG6-22 | Los ejemplos cuantitativos recuperan prerrequisitos antes del formalismo. | **aceptable** | Resonancia, fuerza por presión y razón de presiones siguen la gramática didáctica del curso. | Conservar. |
| CG6-23 | G3 se rotula como ejercicio resuelto pero ofrece consigna y pista, sin resolución visible o en notas. | **inconsistente** | No cumple el contrato de “ejemplo/ejercicio resuelto” usado en unidades anteriores. | Añadir resolución paso a paso o renombrarlo como mini ejercicio y dejar la solución esperada en notas. |
| CG6-24 | Hay recapitulaciones frecuentes al cerrar bloques. | **intencional** | Reduce carga cognitiva y responde a la exigencia especial para U4–U7. | Conservar la frecuencia. |
| CG6-25 | Varias recapitulaciones repiten una cadena de cajas ya mostrada. | **inconsistente** | El patrón global pide síntesis de tres ideas y una comprobación activa, no mera duplicación del diagrama. | Variar: tres afirmaciones, contraste, pregunta de transferencia o mini caso. |
| CG6-26 | Las aplicaciones mantienen prudencia y no convierten pruebas en diagnósticos automáticos. | **intencional** | Protege la frontera con U8 y es conceptualmente correcta. | Conservar el límite clínico. |
| CG6-27 | Algunas slides de aplicación son genéricas y no muestran medición, instrumento o salida real. | **inconsistente** | U1–U5 suelen anclar la aplicación en un objeto, curva, procedimiento o dato observable. | Incorporar al menos dos casos concretos: una OEA y una medición/reflejo con interpretación limitada. |

### Notas, pies, créditos y trazabilidad

| ID | Diferencia | Clasificación | Evidencia y criterio | Acción |
|---|---|---|---|---|
| CG6-28 | Las 117 slides tienen notas y bloque de fuentes. | **aceptable** | La cobertura supera o iguala el estándar de las unidades finalizadas. | Conservar. |
| CG6-29 | Las notas reiteran fórmulas como “Desarrollar la idea con esta conclusión” y una misma pregunta de control. | **inconsistente** | La repetición vuelve las notas menos naturales y menos útiles para un segundo docente. | Reescribir las notas más repetidas con transición, error frecuente, demostración o pregunta específica. |
| CG6-30 | Se usa “slide” de manera formularia en notas. | **inconsistente** | El registro general es español académico natural. | Preferir “diapositiva” o redactar sin nombrar el soporte. |
| CG6-31 | Existen 106 captions; 92 repiten “no a escala” y 72 créditos repiten “Producción propia UCASAL”. | **inconsistente** | Viola D-056: un recurso propio necesita caption funcional y trazabilidad en notas/manifiesto, no dos rótulos editoriales repetidos. | Conservar solo captions que orienten la lectura; mover producción, validación y fuente a notas/manifiesto. |
| CG6-32 | Treinta y dos créditos visibles contienen códigos internos de fuente. | **inconsistente** | El público no puede interpretar códigos como `PO`, `TEX` o similares; las notas ya contienen la referencia completa. | Mostrar autor/organización legible cuando haga falta y reservar códigos para documentación interna. |
| CG6-33 | El manifiesto registra 78 recursos con autor/organización, licencia y estado. | **aceptable** | La trazabilidad es comparable o superior a la de unidades anteriores. | Conservar y sincronizar si cambian recursos. |
| CG6-34 | No hay hipervínculos externos en el PPTX. | **aceptable** | Los enlaces no son obligatorios y las fuentes están documentadas en notas. | Añadir enlaces solo si cumplen una función de clase. |
| CG6-35 | Las imágenes poseen texto alternativo y las notas documentan la función visual. | **aceptable** | Nueve imágenes tienen descripción OOXML; la validación registra 72 objetos con alt text. | Conservar; revisar que los alt no describan adornos como contenido esencial. |

### Layouts, numeración, paleta, tipografía y lenguaje visual

| ID | Diferencia | Clasificación | Evidencia y criterio | Acción |
|---|---|---|---|---|
| CG6-36 | U6 usa 2 masters, 27 layouts disponibles y 25 layouts distintos. | **aceptable** | Coincide con el template y muestra variedad estructural real. | Conservar la infraestructura. |
| CG6-37 | Formato 16:9 y familias Calibri Light, Calibri y Cambria Math. | **aceptable** | Coincide con template y unidades previas. | Conservar. |
| CG6-38 | Paleta carbón, bordó, teal y ocre. | **aceptable** | Recupera la identidad de U1–U4 y la versión corregida de U5. | Conservar. |
| CG6-39 | Los títulos visibles son mayoritariamente bordó, mientras la guía escrita prescribe carbón. | **requiere decisión** | El uso bordó está consolidado en renders de varias unidades; corregir solo U6 crearía otra divergencia. | Resolver globalmente la regla y luego actualizar guía o decks de manera coordinada. |
| CG6-40 | Ciento dieciséis slides llevan un número manual en el encabezado. | **inconsistente** | El template reserva el encabezado para unidad/sección y usa número automático inferior. La excepción de rutas de U5 no aplica a U6. | Recuperar numeración automática inferior y retirar el contador manual del encabezado. |
| CG6-41 | Pie institucional, curso y marca UCASAL son coherentes. | **aceptable** | Coinciden con el template y las unidades finalizadas. | Conservar. |
| CG6-42 | El deck recurre con mucha frecuencia a tarjetas y cajas similares. | **inconsistente** | Aunque usa muchos layouts, el render final se percibe menos variado que U1–U5 y varias anatomías quedan resueltas como texto en cajas. | Sustituir selectivamente tarjetas por cortes anatómicos, diagramas de movimiento y comparaciones espaciales; no rediseñar todo el deck. |
| CG6-43 | Las formas y conectores se mantienen editables. | **aceptable** | Coincide con el estándar de producción y no hay slides aplanadas como imagen completa. | Conservar. |
| CG6-44 | Algunos diagramas CCI/CCE mezclan estructura, energía y salida neural en una causalidad visual ambigua. | **inconsistente** | La gramática de proceso de U2–U5 exige entradas, transformación y salidas distinguibles. | Redibujar con carriles o capas separadas y reservar corredores para conectores. |

## Diferencias que no deben homogeneizarse

Estas diferencias tienen una razón pedagógica y deben conservarse:

1. Más profundidad y más recapitulaciones que U1–U3.
2. Mayor proporción de anatomía funcional y mecanismos frente a ecuaciones formales.
3. Curvas conceptuales normalizadas cuando no hay datos experimentales que deban enseñarse como tales.
4. Introducción de OEA como evidencia del mecanismo coclear activo, dejando el uso diagnóstico para U8.
5. Aplicaciones clínicas prudentes, sin equivalencias automáticas entre resultado de prueba, sitio de lesión y diagnóstico.
6. Contenido puente hacia U7 y U8, siempre que su ubicación central, complementaria o de respaldo se decida explícitamente.

## Correcciones locales prioritarias para una futura revisión del deck

### Imprescindibles para consistencia

1. Corregir la frase sobre CCE y energía.
2. Desarrollar CAE, CCI, CCE y el término completo asociado con PEAT/PEATC antes de cualquier sigla.
3. Sustituir puntos por comas decimales en gráficos.
4. Reemplazar `V(ref)` por `ΔV` o `V_ref` con referencia explícita.
5. Retirar numeración manual superior y recuperar la numeración automática inferior.
6. Eliminar la repetición de “no a escala”, “Producción propia UCASAL” y códigos internos visibles.
7. Resolver el diagrama causal de CCI/CCE y el ejercicio G3.

### Recomendadas

1. Hacer visibles sesiones o bloques de dictado.
2. Variar recapitulaciones y notas del orador.
3. Reemplazar tarjetas repetidas por visuales anatómicos o de movimiento en los bloques más espaciales.
4. Incorporar dos aplicaciones con evidencia observable y límites interpretativos claros.
5. Sustituir el uso ambiguo de “reclutamiento”.

## Decisiones globales pendientes

1. Forma institucional preferida: PEAT, PEATC o ABR.
2. Color canónico de títulos de contenido: carbón según guía escrita o bordó según uso consolidado.
3. División concreta de U6 en sesiones y ubicación de la electroquímica/medición avanzada en ruta central o complementaria.
4. Actualización del mapa del curso con la notación del oído medio, tarea que corresponde a `course-architecture`.

## Documentación global actualizada

- `style/glossary.md`: corrección de “mecanoeléctrica”; incorporación de reflejo acústico, conducto coclear/rampa media, órgano y túnel de Corti, onda viajera y lugar característico; OEA pasa a primera aparición en U6 y se evita el lenguaje de creación de energía.
- `style/notation_guide.md`: nueva convención para áreas y razones del oído medio, `G_p`, resonancia de cuarto de onda y referencia de potenciales eléctricos.
- `style/decision_log.md`: actualización de D-056 y nuevas decisiones D-063 a D-067; se registran como pendientes la sigla de potenciales evocados y el color canónico de títulos.

## Estado final

**Consistencia global:** parcial, con infraestructura aprobada y correcciones locales pendientes.  
**Problemas críticos de identidad global:** ninguno.  
**Deck modificado durante esta revisión:** no.  
**Próximo paso recomendado:** aplicar las correcciones imprescindibles en una versión posterior del deck y volver a revisar las slides afectadas contra el render, sin reducir la profundidad ni las recapitulaciones que tienen justificación pedagógica.

## Actualización de cierre final

La versión `output/unidad_06_mecanismo_periferico_final.pptx` incorpora las correcciones que este informe había dejado pendientes. Esta sección reemplaza el estado “parcial” anterior.

| Diferencia | Clasificación final | Resolución |
|---|---|---|
| Profundidad y cantidad de slides | intencional | Se conserva por densidad de U6, pero se explicitan cuatro encuentros, ruta central, ampliaciones y respaldo. |
| Encabezados y numeración | consistente | Encabezado académico por encuentro/ruta y numeración dinámica nativa en 117 slides. |
| Captions, créditos y códigos internos | consistente | Los códigos quedan en notas/manifiesto; en pantalla solo permanecen captions funcionales de gráficos. |
| CCI, CCE, OEA y potencial evocado | consistente | Primeras apariciones desarrolladas; se evita una sigla institucional no acordada para potenciales evocados. |
| Oído medio y energía | consistente | Se usan `S_TM`, `S_E`, `R_S`, `R_L`, `M_p` y `G_p`; la palanca y las CCE no se describen como creadoras de energía. |
| Potenciales eléctricos | consistente | La referencia de medida se declara verbalmente; se eliminó el subíndice Unicode ambiguo en U06-084. |
| Gráficos | aceptable | Paleta, coma decimal, ejes y captions coinciden con el curso; las repeticiones restantes cambian la tarea pedagógica. |
| Diagramas | consistente | Formas y conectores editables, corredores libres y mínimos tipográficos verificados en el render final. |
| Recapitulaciones y ejemplos | intencional | Mayor frecuencia que en unidades livianas, justificada por U6; G3 queda resuelto y no como consigna vacía. |
| Notas y fuentes | consistente | 117/117 notas con fuentes y alt text; redacción menos formularia y matriz de fuentes sincronizada. |

**Consistencia global final:** aprobada.  
**Diferencias que requieren decisión para cerrar U6:** ninguna.  
**Diferencias pedagógicas preservadas:** profundidad, recapitulaciones frecuentes y banco complementario.  
**Problemas critical/major de consistencia:** ninguno.
