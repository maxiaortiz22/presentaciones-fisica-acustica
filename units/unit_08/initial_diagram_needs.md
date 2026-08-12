# Necesidades iniciales de diagramas — Unidad 8

## Criterio

Todos los recursos siguientes son candidatos explícitos para `diagram-generation`. Deberán construirse con formas, textos y conectores editables de PowerPoint, en el tamaño real del layout previsto. Las ecuaciones anotadas también se tratan como diagramas porque requieren jerarquía, callouts y unidades alrededor de la expresión.

## B00–B01 · Apertura y clases de evidencia

| diagram_id | Slides | Tipo | Contenido estructural | Riesgo geométrico / decisión | Fuente | Prioridad | Estado |
|---|---|---|---|---|---|---|---|
| U08-DG-001 | U08-002 | caso ramificado | Queja inicial → tres observaciones → preguntas posibles | Medio: evitar flechas causales hacia diagnósticos | TEX 8.3; PDF pp. 208–209; BR | alta | propuesto |
| U08-DG-002 | U08-007 | mapa de clase | Once bloques agrupados en cuatro encuentros + respaldo | Alto: usar cuatro macroetapas, no once cajas iguales | BR; EP; TPL | alta | prototipo obligatorio |
| U08-DG-003 | U08-009, U08-016 | mapa conceptual acumulativo | Exposición, alteración, síntoma, resultado y limitación | Alto: las relaciones deben decir “puede relacionarse”, no sugerir cadena inevitable | TEX 8.1, 8.4.1; GLO | alta | propuesto |
| U08-DG-004 | U08-010 | matriz de preguntas | Seis preguntas del caso en dos filas | Alto: dividir revelado en dos etapas; máximo tres nodos visibles por aparición | TEX 8.3; PDF pp. 208–209 | alta | prototipo obligatorio |
| U08-DG-005 | U08-012 | esquema por regiones | Conductivo, sensorioneural y mixto | Medio: fronteras funcionales, no dibujo anatómico exhaustivo | TEX 8.4.1; REF `ashaHearingAdults` | media | complementario |
| U08-DG-006 | U08-013 | inferencia limitada | Patrón observado → hipótesis posibles → preguntas abiertas | Bajo: bloquear flecha directa patrón→causa | TEX 8.4.2, 8.8; SA | alta | propuesto |
| U08-DG-007 | U08-015 | batería convergente | Pregunta central + antecedentes + conductual + fisiológico | Medio: integrar sin nodo final “diagnóstico” | TEX 8.5.1, 8.7; REF `ashaHearingAdults` | alta | propuesto |

## B02–B03 · Exposición, TTS, alteraciones y riesgo

| diagram_id | Slides | Tipo | Contenido estructural | Riesgo geométrico / decisión | Fuente | Prioridad | Estado |
|---|---|---|---|---|---|---|---|
| U08-DG-008 | U08-018 | mapa de variables | Nivel, descriptor, ponderación, duración, espectro e impulsividad | Medio: agrupar en descripción de señal y descripción temporal | TEX 8.4.2; U5; NOT | alta | propuesto |
| U08-DG-009 | U08-020 | ecuación anotada | `ΔL_T(f,Δt)=L_U,1(f,Δt)-L_U,0(f)` + símbolos, unidad y signo | Medio: preservar 28 pt y separar definición de interpretación | TEX ec. 8.1; NOT | alta | propuesto |
| U08-DG-010 | U08-021 | ejemplo resuelto | Datos → compatibilidad → sustitución → 15 dB → límite | Bajo: no convertir la conclusión en diagnóstico | TEX NG1; PDF pp. 224, 229–230 | alta | propuesto |
| U08-DG-011 | U08-026 | ecuación y cálculo | Normalización de `L_Aeq,T` a 8 h, con cociente temporal adimensional | Medio: distinguir valor calculado de juicio normativo | TEX ec. 8.2; U5; NOT | media | complementario |
| U08-DG-012 | U08-029 | mapa de evidencia | Exposición repetida + resultado compatible + antecedentes + límites | Alto: ninguna rama debe funcionar como criterio diagnóstico suficiente | TEX 8.4.2; PDF pp. 210–211 | alta | propuesto |
| U08-DG-013 | U08-033 | modelo multifactorial | Edad + historia de exposición + comorbilidades + variabilidad → desempeño/mediciones | Medio: evitar suma determinista o causalidad única | PO; TEX 8.4.5; SA | alta | propuesto |
| U08-DG-014 | U08-034, U08-036 | checklist de porcentaje | Evento, población, período, exposición, comparador, incertidumbre | Alto: seis campos; usar construcción progresiva y no radar decorativo | PO; COV U08-06; OD-U08-05/06 | alta | prototipo obligatorio |

## B04 · Marco común de estudios

| diagram_id | Slides | Tipo | Contenido estructural | Riesgo geométrico / decisión | Fuente | Prioridad | Estado |
|---|---|---|---|---|---|---|---|
| U08-DG-015 | U08-037, U08-038 | cadena de medición | Estímulo → sistema auditivo → respuesta → sensor/tarea → registro → interpretación | Medio: mantener seis etapas legibles en ancho completo | TEX 8.5.1; PDF pp. 211–212 | alta | propuesto |
| U08-DG-016 | U08-039, U08-044 | matriz recurrente | Seis preguntas: estímulo, parte/función, magnitud, sensor/tarea, resultado, límite | Crítico: no usar seis tarjetas densas; construir en dos filas y reutilizar vacía | TEX tabla 8.1; BR | alta | prototipo obligatorio |
| U08-DG-017 | U08-041 | mapa anatómico-funcional | Oído externo/medio, cóclea, vía neural y respuesta integrada + estudios relacionados | Crítico: mostrar dependencias compartidas; dividir si las líneas se cruzan | TEX tabla 8.1; U6 | alta | prototipo obligatorio |
| U08-DG-018 | U08-042 | sistema de condiciones | Ambiente + equipo + transductor/sensor + protocolo + persona → registro | Medio: flechas hacia “registro interpretable”, no hacia “verdad” | TEX 8.5.1–8.5.4; normas por validar | alta | propuesto |
| U08-DG-019 | U08-043 | batería por discrepancia | Pregunta → pruebas complementarias → concordancia/discrepancia → nueva pregunta | Medio: bucle visible sin parecer algoritmo clínico | TEX 8.5.1, 8.7; BR | alta | propuesto |

## B05 · Audiometría tonal

| diagram_id | Slides | Tipo | Contenido estructural | Riesgo geométrico / decisión | Fuente | Prioridad | Estado |
|---|---|---|---|---|---|---|---|
| U08-DG-020 | U08-046 | rutas físicas | Generador → auricular → vía aérea / vibrador → vía ósea → tarea | Alto: evitar anatomía incorrecta y cruce de rutas | TEX 8.5.2; PDF pp. 212–213; U6 | alta | propuesto |
| U08-DG-021 | U08-047 | comparación de referencias | dB SPL, dB HL y dB SL: referencia, uso y operación permitida | Alto: tres escalas con suficiente espacio; preferir tabla-diagrama | NOT; GLO; TEX cap. 8 | alta | prototipo obligatorio |
| U08-DG-022 | U08-051 | ecuación anotada | `G_AO(f)=L_VA(f)-L_VO(f)` + variables, compatibilidad y límite | Bajo | TEX ec. 8.3; NOT | alta | propuesto |
| U08-DG-023 | U08-052 | ejemplo resuelto | `40-15=25 dB` + lectura restringida | Bajo: resultado no debe rotularse como enfermedad | TEX C8/respuesta; PDF pp. 224, 229 | alta | propuesto |
| U08-DG-024 | U08-053 | condiciones de audiometría | Audiograma rodeado por ambiente, calibración, transductor, colocación, consigna y enmascaramiento | Alto: seis callouts; usar dos coronas o dos etapas | TEX 8.5.2; REF `ashaPureTone2005`, `iso8253_1_2010` | media | complementario |

## B06 · Habla y tinnitus referido

| diagram_id | Slides | Tipo | Contenido estructural | Riesgo geométrico / decisión | Fuente | Prioridad | Estado |
|---|---|---|---|---|---|---|---|
| U08-DG-025 | U08-055 | tres tareas | Detección, reconocimiento e identificación: estímulo, respuesta y variable | Medio: compararlas sin crear una taxonomía clínica exhaustiva | TEX 8.5.3; PDF pp. 214–215 | alta | propuesto |
| U08-DG-026 | U08-056 | cadena logoaudiométrica | Material verbal → nivel → presentación → respuesta → porcentaje | Bajo | TEX fig. 8.4; PDF pp. 214–215 | alta | propuesto |
| U08-DG-027 | U08-061 | bucle de correspondencia | Percepto referido ↔ tono/ruido ajustable ↔ decisión de semejanza | Medio: dejar claro que el ajuste depende de la persona y la sesión | TEX 8.5.5; PDF pp. 216–217 | alta | propuesto |
| U08-DG-028 | U08-062 | comparación físico-perceptual | Señal externa medible vs percepto referido vs resultado de correspondencia | Medio: tres planos, sin iconos ambiguos | TEX 8.4.4, 8.5.5; U7 | alta | propuesto |
| U08-DG-029 | U08-063 | escala/ecuación anotada | Umbral individual + nivel de correspondencia → diferencia en dB SL | Medio: nombrar el umbral de referencia y no sugerir intensidad interna | TEX 8.5.5; NOT; OD-U08-21/32 | media | complementario |

## B07 · Timpanometría

| diagram_id | Slides | Tipo | Contenido estructural | Riesgo geométrico / decisión | Fuente | Prioridad | Estado |
|---|---|---|---|---|---|---|---|
| U08-DG-030 | U08-066 | cadena instrumental | Tono sonda + presión controlada → oído medio → micrófono → inmitancia → curva | Alto: reservar corredor para presión y retorno acústico | TEX 8.5.4; PDF pp. 215–216 | alta | propuesto |
| U08-DG-031 | U08-068 | proceso animable | Presión 1 → medición 1 → punto; repetición → curva | Medio: diseñar cuatro estados reutilizables para GIF y estático | TEX 8.5.4; EP | alta | propuesto |
| U08-DG-032 | U08-071 | condiciones para curva plana | Sellado/obstrucción/protocolo/sistema → curva observada → preguntas abiertas | Alto: no asociar una sola causa; dos niveles máximo | TEX 8.5.4; SA | alta | propuesto |

## B08 · Estudios fisiológicos

| diagram_id | Slides | Tipo | Contenido estructural | Riesgo geométrico / decisión | Fuente | Prioridad | Estado |
|---|---|---|---|---|---|---|---|
| U08-DG-033 | U08-074–075 | cadena de ida y retorno | Estímulo acústico → cóclea → emisión → sonda/micrófono → registro | Alto: diferenciar direcciones con color y corredores separados | TEX 8.5.6; PDF p. 217 | alta | propuesto |
| U08-DG-034 | U08-076 | integración de OEA | Registro OEA + antecedentes + otras pruebas → interpretación limitada | Bajo: sin nodo “audición normal” | TEX 8.5.6; SA | alta | propuesto |
| U08-DG-035 | U08-077 | cadena PEAT | Estímulo → vía auditiva → electrodos → amplificación/promedio → forma de onda | Medio: separar fenómeno biológico de procesamiento instrumental | TEX 8.5.7; PDF pp. 217–218 | alta | propuesto |
| U08-DG-036 | U08-080 | cadena ECoG | Estímulo → generadores cocleares/nerviosos → electrodo cercano → registro | Medio: no sobredetallar montaje invasivo | TEX 8.5.8; PDF p. 218 | alta | propuesto |
| U08-DG-037 | U08-081 | componentes ECoG | CM, SP y AP: sigla, generador general y relación con la traza | Alto: tres componentes + definiciones; mantener como complemento | TEX 8.5.8; REF `simpson2020` | media | complementario |
| U08-DG-038 | U08-082–083 | comparación de pruebas | OEA vs PEAT vs ECoG por estímulo, generador, sensor, magnitud y límite | Crítico: matriz central; dividir en dos etapas si no mantiene 22 pt | TEX 8.5.6–8.5.8; BR | alta | prototipo obligatorio |

## B09 · Rehabilitación

| diagram_id | Slides | Tipo | Contenido estructural | Riesgo geométrico / decisión | Fuente | Prioridad | Estado |
|---|---|---|---|---|---|---|---|
| U08-DG-039 | U08-085 | cadena común de dispositivo | Entrada → transducción → procesamiento → salida → sistema auditivo remanente | Medio: salida debe quedar abierta a acústica/eléctrica/mecánica | TEX 8.6; PDF pp. 219–221 | alta | propuesto |
| U08-DG-040 | U08-086 | cadena de audífono | Micrófono → A/D/procesamiento → receptor → presión sonora en oído | Medio: evitar diagrama de marca o promesa funcional | TEX 8.6.1; PDF p. 219 | alta | propuesto |
| U08-DG-041 | U08-087 | ecuación anotada | `G(f)=L_salida(f)-L_entrada(f)` + compatibilidad, unidad y límite | Bajo | TEX ec. 8.4; NOT | alta | propuesto |
| U08-DG-042 | U08-088 | ejemplo resuelto | Entrada 60 dB SPL → salida 82 dB SPL → ganancia 22 dB | Bajo: separar ganancia de beneficio | TEX NG3/respuesta; PDF pp. 225, 230 | alta | propuesto |
| U08-DG-043 | U08-090–091 | cadena de implante | Micrófono → procesador → enlace transcutáneo → receptor/estimulador → electrodos | Alto: distinguir partes externas e internas sin detalle quirúrgico | TEX 8.6.2; PDF pp. 219–220 | alta | propuesto |
| U08-DG-044 | U08-091 | mapa de codificación | Bandas → canales → electrodos → patrones eléctricos → perceptos | Crítico: no equiparar bandas, electrodos y perceptos; construcción progresiva | TEX 8.6.2; SA | alta | prototipo obligatorio |
| U08-DG-045 | U08-092 | comparación física | Audífono vs implante: entrada común, transformación, salida y sistema utilizado | Alto: evitar eje “menos/más severo” o ranking terapéutico | TEX 8.6.1–8.6.2; tabla 8.2 | alta | propuesto |
| U08-DG-046 | U08-093 | comparación ampliada | Conducción ósea: salida mecánica; EAS: salida acústica + eléctrica | Alto: dos sistemas distintos; no fijar indicaciones ni corte frecuencial | TEX 8.6.3–8.6.4; PDF pp. 220–221 | media | complementario |
| U08-DG-047 | U08-094 | síntesis de dispositivos | Audífono, implante, conducción ósea y EAS por cadena física y límite | Crítico: usar cuatro mini-cadenas; dividir si el texto baja de 22 pt | TEX tabla 8.2; BR | alta | prototipo obligatorio |

## B10 · Integración y cierre

| diagram_id | Slides | Tipo | Contenido estructural | Riesgo geométrico / decisión | Fuente | Prioridad | Estado |
|---|---|---|---|---|---|---|---|
| U08-DG-048 | U08-096 | matriz de caso | Datos del caso × clase de evidencia × pregunta que habilitan | Crítico: tabla editable con revelado; máximo seis datos por vista | TEX 8.3, 8.7; EP | alta | prototipo obligatorio |
| U08-DG-049 | U08-098 | integración razonada | Dato → interpretación permitida → límite → próximo dato necesario | Medio: cuatro pasos reiterados en tres ejemplos | TEX 8.7–8.8; BR | alta | propuesto |
| U08-DG-050 | U08-100 | proceso profesional | Pregunta → antecedentes → selección de pruebas → control técnico → integración → decisión profesional | Alto: no cerrar con prescripción; distinguir alcance de la asignatura | TEX 8.7; PDF pp. 221–222 | alta | propuesto |
| U08-DG-051 | U08-101 | síntesis acumulativa | Seis preguntas comunes aplicadas a exposición, pruebas y dispositivos | Crítico: síntesis central; construir en tres estados, no “todo en uno” | TEX cap. 8; BR; EP | alta | prototipo obligatorio |
| U08-DG-052 | U08-102 | puente de curso | Unidad 8 → Unidad 10: exposición, descriptor, efecto, control y comunicación | Bajo: puente, no desarrollo adelantado | CM; CDM; COV | media | propuesto |

## Reglas de diseño y aceptación

- Texto principal: 24 pt preferido y 22 pt mínimo; etiquetas breves de conectores: 20 pt mínimo; ecuaciones centrales: 28 pt o más.
- Mantener al menos 0,18 pulgadas de margen interior y 10–20 % de aire dentro de cada caja.
- Anclar conectores a bordes y reservar corredores; ninguna línea, punta o etiqueta debe cruzar, tocar o terminar dentro de texto.
- Mantener al menos 0,10 pulgadas entre líneas y texto no relacionado; colocar etiquetas fuera de la línea.
- No usar “shrink text to fit”. Ampliar, sintetizar, redistribuir o dividir antes de bajar los mínimos.
- Distinguir visualmente señal acústica, respuesta bioeléctrica, dato conductual y salida mecánica sin depender solo del color.
- En ecuaciones, definir símbolo, unidad, referencia, condiciones de compatibilidad y significado físico; el resultado debe quedar separado del límite interpretativo.
- Prototipar primero U08-DG-002, 004, 014, 016, 017, 021, 038, 044, 047, 048 y 051 porque concentran el mayor riesgo de densidad.
- Renderizar cada diagrama a 16:9 en el layout asignado; revisar clipping, colisiones, conectores, jerarquía y lectura desde aula; corregir y volver a renderizar hasta no registrar problemas críticos o mayores.
