# Unidad 6 — Análisis de fuentes

## Jerarquía aplicada

1. `context/programa/Programa de Física Acústica.pdf` — alcance obligatorio; programa 2025, p. 4.
2. `context/libro_latex/chapters/06-percepcion-auditiva.tex` — fuente editable y estructural principal.
3. `context/libro_pdf/Física Acústica para Fonoaudiología.pdf` — versión maquetada; capítulo 6, pp. 151–175.
4. `course_map.md`, `course_dependency_map.md` y `content_coverage_matrix.csv` — arquitectura, dependencias y estado de cobertura.
5. `style/presentation_style_guide.md`, `style/notation_guide.md` y `style/glossary.md` — criterios de comunicación, notación y terminología.
6. `context/libro_latex/bibliography/references.bib` — trazabilidad de las fuentes técnicas ya citadas por el capítulo.

No se incorporaron fuentes externas nuevas en esta etapa. Los vacíos obligatorios se registran para una búsqueda posterior y no se completan con conocimiento general sin cita.

## Disponibilidad y método de revisión

| Fuente | Estado | Revisión realizada | Limitación |
|---|---|---|---|
| Programa oficial | Disponible, 6 páginas | Extracción textual completa del bloque de U6 y verificación de la p. 4 | El programa enumera temas; no define profundidad ni secuencia pedagógica. |
| Capítulo LaTeX U6 | Disponible, 1259 líneas | Lectura completa, incluidas secciones, ejercicios, soluciones, glosario, ecuaciones, figuras y citas | Dos puntos programáticos no están desarrollados de forma explícita. |
| Libro PDF | Disponible, 296 páginas | Identificación de pp. 151–175, extracción de estructura y renderizado visual de las 25 páginas | Es material de lectura vertical; no debe copiarse como slides. |
| Mapas curriculares | Disponibles | Lectura completa de `course_map.md` y `course_dependency_map.md`; revisión de todas las filas U06 de la matriz | Varias referencias `book_section` de U06 corresponden a una numeración anterior. |
| Guías de estilo/notación/glosario | Disponibles | Lectura completa de los tres documentos solicitados | Existen decisiones terminológicas y de notación aún pendientes. |
| Figuras propias U6 | Siete fuentes TikZ | Inventario de archivos y verificación en el PDF | Requieren reconstrucción para 16:9, tamaño aula y editabilidad. |
| Guía de ejercicios independiente | No localizada | El capítulo sí incluye banco completo y soluciones | No hay evidencia de parciales, recuperatorios o criterios docentes específicos para seleccionar ejercicios. |
| Deck previo de U6 | No localizado | `units/unit_06/` solo contenía `.gitkeep` | No existe una secuencia previa que preservar. |

## Alcance obligatorio extraído del programa

El programa formula U6 como una cadena amplia de contenidos anatómicos y funcionales. Para revisar la cobertura se agrupa sin alterar su obligatoriedad:

| Grupo programático | Elementos obligatorios |
|---|---|
| Cadena general | Oído como transductor acústico–mecánico–eléctrico; oído externo, medio e interno. |
| Oído externo | Pabellón, canal auditivo, membrana timpánica y cambio de frente de onda esférica a cilíndrica. |
| Oído medio | Caja timpánica, trompa de Eustaquio, martillo, yunque, estribo, ventana oval, conversión de fuerza/desplazamiento, transformador mecánico y comportamiento de la cadena. |
| Protección e igualación | Señales intensas, reflejo estapedial, tiempos de reacción, igualación de presiones e impedancias y trompa de Eustaquio. |
| Vía ósea | Audición por vía ósea o transmisión paratimpánica. |
| Arquitectura coclear | Cóclea, rampas vestibular/coclear/timpánica, perilinfa, endolinfa, membranas de Reissner, basilar y tectorial, ventanas oval/redonda. |
| Mecánica coclear | Movimiento de líquidos y membranas, micromecánica, desplazamiento relativo órgano de Corti–membrana tectoria, comportamiento ondulatorio y tonal de la membrana basilar. |
| Transducción celular | Transformación mecánica–bioeléctrica, potencial de reposo, órgano y túnel de Corti, CCI y CCE. |
| Dependencia con el nivel | Características de respuesta ante señales débiles e intensas. |

## Comparación programa–LaTeX–PDF

| Tema | Programa | LaTeX | PDF | Evaluación |
|---|---|---|---|---|
| Oído como transductor | Exigido | Cadena explícita de siete etapas y dominios | Figura 6.1, p. 152 | Cubierto y pedagógicamente fortalecido. |
| Pabellón | Exigido | Función direccional y filtrado espectral | 6.4.1, p. 153 | Cubierto con ampliación útil. |
| CAE | Exigido | Geometría real, reflexiones, posición y transferencia | 6.4.2–6.4.4, pp. 153–154 | Cubierto. |
| Frente esférico → cilíndrico | Formulación literal | El capítulo no afirma una conversión universal; usa conducto real y modelo de cuarto de onda | La misma cautela aparece en pp. 153–154 | Cobertura parcial deliberada; requiere decisión docente. |
| Membrana timpánica | Exigida | `Δp → F`, deformación y límites del pistón rígido | 6.4.5, pp. 154–155 | Cubierta con modelo cuantitativo. |
| Caja, trompa y huesecillos | Exigidos | Anatomía funcional integrada | 6.5.1, p. 155; figura 6.2 | Cubiertos. |
| Igualación de presión e impedancias | Exigida | Separa presión estática/trompa de adaptación mecánica de impedancias | 6.5, pp. 155–158 | Cubierta con mayor precisión conceptual. |
| Transformador mecánico | Exigido | Áreas, palanca, razón de presiones y dB de razón | 6.5.2–6.5.3, pp. 155–158 | Cubierto y cuantificado. |
| Reflejo y tiempos | Exigidos | Dependencia de frecuencia/nivel/estímulo/persona; sin umbral o latencia universal | 6.5.4, p. 158 | Cubierto con cautela apropiada; no hay valores fijos. |
| Conducción ósea/paratimpánica | Exigida | Cinco contribuciones simultáneas; rechaza ruta única | 6.6, pp. 158–159 | Cubierta; terminología del programa se corrige y contextualiza. |
| Cóclea, rampas y fluidos | Exigidos | Vista longitudinal y transversal, perilinfa/endolinfa, helicotrema | 6.7.1, pp. 159–160 | Cubiertos. |
| Membranas y ventanas | Exigidas | Reissner, basilar, tectoria, oval y redonda con función | 6.7.1, pp. 159–160 | Cubiertas. |
| Movimiento de líquidos | Exigido | Movimiento oscilatorio; rechaza flujo continuo oval→redonda | 6.7.1, p. 160 | Cubierto y corregido conceptualmente. |
| Onda viajera/tonotopía | Exigida como comportamiento tonal | Lugar característico, extensión y dependencia de frecuencia/nivel | 6.7.2–6.7.3, pp. 160–162 | Cubierta con ampliación esencial. |
| Señales débiles/intensas | Exigidas | Proceso activo, sensibilidad, selectividad, compresión y ensanchamiento | 6.7.3, pp. 161–162 | Cubiertas. |
| Órgano de Corti | Exigido | Micromecánica y relación con membranas | 6.8.1, p. 161 | Cubierto. |
| Túnel de Corti | Exigido | No aparece como término ni estructura delimitada | No aparece en pp. 151–175 | Ausente; ampliación externa obligatoria. |
| CCI/CCE | Exigidas | Funciones diferenciadas, aferencia y electromotilidad | 6.8.2, pp. 161–163 | Cubiertas con buena precisión. |
| Potencial de reposo | Exigido | Se describen potencial eléctrico endolinfático y potencial receptor; no hay definición explícita del reposo celular | La misma ausencia se observa en pp. 163–164 | Parcial; requiere ampliación y visual específico. |
| Transducción mecanoeléctrica | Exigida | *Tip links*, canales, K⁺, potencial receptor, Ca²⁺, glutamato y aferencia | 6.8.3, pp. 163–164 | Cubierta y ampliada. |
| Codificación periférica | No listada literalmente | Lugar/tiempo para frecuencia y tasa/reclutamiento/extensión para nivel | 6.9, pp. 163–164 | Ampliación importante que prepara U7. |
| Aplicación y límites clínicos | Implícitos en objetivos generales | CAE, oído medio, vía ósea, OEA y potenciales; pruebas cruzadas | 6.10, pp. 164–165 | Ampliación disciplinar valiosa. |

## Correspondencia LaTeX–PDF

### Verificación estructural

| Sección LaTeX | PDF | Resultado |
|---|---:|---|
| 6.1 Propósito y resultados | 151–152 | Presente. |
| 6.2 Conocimientos previos | 152 | Presente. |
| 6.3 Del campo acústico a la señal neural | 152–153 | Presente; figura 6.1 en p. 152. |
| 6.4 Oído externo y membrana timpánica | 153–155 | Presente; ecuaciones y ejemplo legibles. |
| 6.5 Oído medio | 155–158 | Presente; figuras 6.2 y 6.3 en pp. 155 y 157. |
| 6.6 Conducción ósea | 158–159 | Presente; figura 6.4 en p. 159. |
| 6.7 Arquitectura y mecánica coclear | 159–161 | Presente; figuras 6.5 y 6.6 en pp. 160 y 162. |
| 6.8 Órgano de Corti y células ciliadas | 161–163 | Presente; figura 6.7 en p. 164 por flujo de maquetación. |
| 6.9 Codificación periférica | 163–164 | Presente. |
| 6.10 Relación con Fonoaudiología | 164–165 | Presente. |
| 6.11 Errores frecuentes | 165–166 | Presente. |
| 6.12 Síntesis | 166 | Presente. |
| 6.13 Ejercicios | 166–170 | Presente. |
| 6.14 Soluciones | 170–175 | Presente. |
| 6.15 Glosario | 175 | Presente. |

No se detectaron diferencias sustantivas entre el contenido del LaTeX revisado y las páginas correspondientes del PDF. El PDF funciona como verificación de maquetación y de presencia de figuras, no como fuente textual superior al LaTeX.

### Verificación visual

Se renderizaron e inspeccionaron las 25 páginas del capítulo, 151–175. La versión PDF:

- conserva el título largo “El mecanismo periférico de la percepción auditiva”;
- muestra las siete figuras propias sin cortes visibles;
- mantiene ecuaciones, unidades, captions y numeración;
- presenta las soluciones y el glosario completos;
- no exhibe páginas faltantes, imágenes rotas ni errores visuales que cambien el contenido.

La maquetación es correcta para libro, pero confirma que las figuras y los párrafos son demasiado densos para trasladarlos directamente a formato 16:9. En particular, las figuras de cadena, conducción ósea, arquitectura coclear y CCI/CCE necesitan mayor tamaño, menos texto simultáneo o revelado por etapas.

## Fórmulas, magnitudes y ejemplos localizados

| Elemento | LaTeX | PDF | Evaluación |
|---|---|---|---|
| `f_res ≈ c/(4ℓ)` | 6.4.3 | p. 154 | Correcta dimensionalmente; modelo ideal explícito. |
| Ejemplo `ℓ=27 mm`, `c=343 m/s` | 6.4.4 | p. 154 | Resultado `≈3,18 kHz`; no universal. |
| `F ≈ Δp·A` | 6.4.5 | p. 154 | Correcta; no determina desplazamiento. |
| `R_A=A_TM/A_E` | 6.5.2 | p. 156 | Razón adimensional; notación de área a armonizar. |
| `R_p≈R_A R_L` | 6.5.2 | p. 156 | Modelo ideal; colisión de `R_p` con U4. |
| `G_p=20 log10(R_p)` | 6.5.3 | p. 156 | Razón en dB, no dB SPL. |
| Ejemplo `R_A=20`, `R_L=1,2` | 6.5.3 | pp. 156–157 | `R_p=24`, `G_p≈27,60 dB`; valores didácticos. |
| Curvas `s/L` | figura 6.6 | p. 162 | Normalizadas y conceptuales; no son datos anatómicos. |

## Ampliaciones del libro respecto del programa

- objetivos observables y delimitación con U7/U8;
- cadena explícita de dominios físicos;
- pistas espectrales y dependencia individual del pabellón;
- función de transferencia y dependencia espacial en el CAE;
- modelo y ejemplo de cuarto de onda;
- conversión presión–fuerza con análisis dimensional;
- razones de área, palanca, presión y expresión logarítmica;
- carácter no universal de umbral y latencia del reflejo;
- conducción ósea descrita mediante cinco mecanismos;
- helicotrema y dos vistas de arquitectura coclear;
- lugar característico, tonotopía, solapamiento y dependencia con el nivel;
- cóclea activa, compresión y selectividad;
- prestina, *tip links*, K⁺, Ca²⁺, glutamato y sinapsis aferente;
- distinción potencial receptor/potencial de acción;
- codificación inicial de frecuencia y nivel;
- aplicaciones a medición en CAE, OEA y potenciales;
- banco graduado de ejercicios, distractores y soluciones.

Estas ampliaciones son pertinentes, pero no todas deben tener igual peso visible. El detalle molecular, la codificación temporal y las variantes numéricas son candidatos a material complementario o respaldo.

## Diferencias, tensiones y vacíos documentales

### 1. Título oficial frente a título de trabajo

- Programa: “El mecanismo de la percepción auditiva”.
- LaTeX/PDF y pedido actual: “El mecanismo periférico de la percepción auditiva”.
- Evaluación: “periférico” delimita mejor el contenido y evita invadir U7, pero debe conservarse la trazabilidad con el título oficial.

### 2. Frente de onda en el CAE

- Programa: “cambio de frente de onda esférica a cilíndrica”.
- Libro: CAE curvo, variable y finito con onda incidente/reflejada, impedancias y función de transferencia; usa un tubo de cuarto de onda solo como aproximación.
- Evaluación: no corresponde enseñar una conversión geométrica literal y universal. Debe explicarse la intención programática mediante modelos y límites.

### 3. Igualación de presiones e impedancias

- El programa las enumera próximas.
- El libro separa correctamente presión estática/trompa de Eustaquio de adaptación de impedancias para una señal acústica.
- Evaluación: la distinción debe ser central para evitar atribuir a la trompa una igualación acústica ciclo a ciclo.

### 4. Vía ósea o “transmisión paratimpánica”

- El programa sugiere una denominación alternativa singular.
- El libro adopta conducción ósea multimecanismo e incluye contribuciones del CAE y huesecillos.
- Evaluación: usar “conducción ósea” como término preferido y explicar la formulación del programa como histórica o simplificada.

### 5. Potencial de reposo

- Obligatorio en el programa.
- El capítulo menciona el potencial eléctrico de la endolinfa y el potencial receptor, pero no define el potencial de reposo de una célula ni su referencia.
- Evaluación: cobertura parcial. Requiere una fuente fisiológica primaria o manual académico validado y una comparación explícita de potenciales.

### 6. Túnel de Corti

- Obligatorio en el programa.
- Ausente en LaTeX, PDF y glosario del capítulo; el glosario transversal también lo mantiene pendiente.
- Evaluación: ausencia clara. Debe incorporarse con fuente anatómica y representación validada antes del storyboard.

### 7. Terminología de rampas

- Programa: rampa vestibular, coclear y timpánica.
- Libro: rampa vestibular, conducto coclear o rampa media y rampa timpánica.
- Guías: pendiente decidir entre español y nomenclatura latina `scala vestibuli/media/tympani`.
- Evaluación: mantener ambos términos en primera aparición y adoptar uno como visible principal.

### 8. Notación de área

- Capítulo: `A`, `A_TM`, `A_E`.
- Guía transversal: `S` para área, para evitar colisión con amplitud `A`.
- Evaluación: se necesita una decisión explícita antes de redactar ecuaciones.

### 9. Colisión de `R_p`

- U4 y la guía: `R_p` es coeficiente de reflexión de presión.
- U6: `R_p` es razón ideal de presiones del transformador mecánico.
- Evaluación: colisión crítica entre unidades consecutivas; debe resolverse antes del storyboard.

### 10. Referencias de sección en la matriz

Varias filas U06 de `content_coverage_matrix.csv` apuntan a una numeración anterior. Por ejemplo, pabellón/CAE figuran en 6.2 cuando el capítulo actual los ubica en 6.4; oído medio figura en 6.3–6.4 cuando actualmente es 6.5. Los estados de cobertura son útiles, pero la trazabilidad de sección necesita una actualización futura con `course-architecture`.

## Qué puede pasar casi directamente a diapositivas

- cadena de transformación y distinción de dominios;
- lista de conocimientos previos en forma de diagnóstico;
- CAE real frente a modelo ideal de cuarto de onda;
- ecuación y ejemplo `f_res` con limitaciones;
- presión → fuerza y por qué no basta para desplazamiento;
- separación presión estática/acústica;
- áreas + palanca + intercambio energético;
- cautela del reflejo estapedial;
- conducción ósea multimecanismo;
- doble vista coclear;
- onda viajera y tonotopía;
- débil frente a intensa;
- CCI frente a CCE;
- secuencia de transducción;
- aplicaciones y errores frecuentes;
- integrador de 2 kHz a 40/70 dB SPL.

La redacción debe fragmentarse y las figuras deben reconstruirse. No deben copiarse páginas completas ni trasladarse párrafos largos.

## Qué necesita más explicación o transformación

| Contenido | Necesidad | Motivo |
|---|---|---|
| Frente de onda del CAE | Explicación, gráfico y decisión docente | Tensión entre formulación del programa y precisión del libro. |
| Anatomía general | Imagen técnica + diagrama funcional | El esquema propio es útil, pero no suficiente como única referencia anatómica. |
| Oído medio | Diagrama por etapas + ejemplo | La combinación de áreas, palanca, impedancia, energía y dB produce carga muy alta. |
| Reflejo | Línea temporal conceptual o comparación de estímulos | “Protección” y latencia se malinterpretan con facilidad. |
| Conducción ósea | Diagrama convergente y actividad | Cinco mecanismos no deben convertirse en una lista memorizada. |
| Cóclea | Dos vistas coordinadas, imagen y revelado | La orientación tridimensional es difícil para primer año. |
| Túnel de Corti | Nueva fuente y visual | Tema obligatorio ausente. |
| Potenciales | Comparación explícita y fuente | Tema obligatorio solo parcial y terminología próxima. |
| Onda viajera | Gráficos grandes y, si aporta, animación | El visual del libro es pequeño y normalizado. |
| CCI/CCE/transducción | Varias etapas/slides | Una sola figura no puede contener función, mecánica, iones, sinapsis y aferencia con letra de aula. |
| Codificación periférica | Ejemplos y límite con U7 | Puede invadir psicoacústica o neurociencia central. |
| Aplicación clínica | Casos “permite/no permite” | Evita diagnóstico a partir de un dato aislado. |

## Implicancias de las guías de estilo, notación y glosario

- La unidad necesita una idea dominante por slide y bloques cortos con recapitulaciones.
- Las figuras de libro no pueden copiarse a media slide: deben rediseñarse para texto de 22–24 pt y ecuaciones centrales de 30 pt o más.
- Los diagramas estructurales deben ser editables y pasar por `diagram-generation` en una etapa posterior.
- Teal debe representar señal, magnitud o proceso físico; ocre puede marcar respuesta clínica/perceptual, sin convertir color en única codificación.
- Ecuaciones con símbolos definidos, unidades, hipótesis y significado; no usar capturas.
- Debe mantenerse la distinción entre `p(t)`, `Δp`, `F`, desplazamiento, `L_p`, potencial receptor y actividad neural.
- `dB SPL` y una razón de presión en dB no son intercambiables.
- Las siglas CAE, CCI y CCE deben desarrollarse en primera aparición.
- “Conducción ósea”, “sonómetro”, “pitch/altura tonal” y “sonoridad” deben conservar el uso del glosario.
- La terminología anatómica y las colisiones `A/S` y `R_p` deben resolverse antes de la escritura de slides.

## Coherencia con la arquitectura del curso

`course_map.md` y `course_dependency_map.md` coinciden en que U6 tiene carga muy alta y recibe simultáneamente:

- mecánica de U2;
- ondas de U3;
- presión, impedancia y niveles de U4;
- respuesta en frecuencia de U5.

La estrategia global recomendada —externo, medio, ósea, cóclea, órgano de Corti y codificación— se conserva, pero se subdivide en ocho bloques preliminares para separar arquitectura coclear de onda viajera y transducción de codificación. Cada bloque debe cerrar con:

```text
entrada → transformación → salida → qué no permite concluir
```

La unidad prepara U7 y U8, pero no debe adelantar sus desarrollos. Los puentes se limitan a:

- frecuencia/pitch y nivel/sonoridad no equivalentes;
- OEA vinculada con CCE pero dependiente de toda la cadena de entrada/salida;
- potenciales como respuestas eléctricas evocadas;
- vía aérea/ósea como bases funcionales de evaluación y dispositivos.

## Fuentes técnicas citadas por el capítulo

| Clave | Fuente | Uso principal en U6 |
|---|---|---|
| `carlini2024` | Carlini, Bordeau y Ambard, *Frontiers in Psychology* (2024) | Pabellón, claves espectrales y localización. |
| `ugarteburu2022` | Ugarteburu et al., *Frontiers in Bioengineering and Biotechnology* (2022) | CAE, tímpano y mecánica del oído medio. |
| `schilder2015` | Schilder et al., *Clinical Otolaryngology* (2015) | Trompa de Eustaquio y funciones. |
| `ashaHearingAdults` | ASHA Practice Portal | Reflejo acústico y cautelas de interpretación. |
| `stenfeltGoode2005` | Stenfelt y Goode, *Otology & Neurotology* (2005) | Conducción ósea multimecanismo. |
| `fettiplace2017` | Fettiplace, *Comprehensive Physiology* (2017) | Arquitectura coclear, células ciliadas, transducción y sinapsis. |
| `capraraPeng2022` | Caprara y Peng, *Molecular and Cellular Neuroscience* (2022) | Mecanotransducción y función celular. |

Estas referencias bastan para rastrear el contenido existente, pero el futuro tratamiento de túnel de Corti y potencial de reposo deberá registrar una fuente específica y, de ser posible, una referencia anatómica/fisiológica primaria o manual académico autorizado.
