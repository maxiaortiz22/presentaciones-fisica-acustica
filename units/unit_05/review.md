# Revisión integral — Unidad 05

## Identificación

- **Unidad:** 05 — Análisis frecuencial de señales acústicas.
- **Versión revisada:** `unidad_05_analisis_frecuencial_v01.pptx`.
- **Versión corregida:** `unidad_05_analisis_frecuencial_v02.pptx`.
- **Cantidad de slides:** 150.
- **Fecha de revisión:** 2026-08-03.
- **Fuentes principales contrastadas:** programa oficial; `context/libro_latex/chapters/05-analisis-frecuencial.tex`; PDF del libro del curso; `brief.md`; `storyboard.md`; `slide_text.md`; `speaker_notes.md`.
- **Método:** inspección del PowerPoint, render individual de las 150 slides, contact sheet, revisión ampliada de slides afectadas, prueba automática de desbordes y auditoría del paquete PPTX.

## Resultado ejecutivo

El v01 cubría el programa y seguía una secuencia pedagógica extensa, pero no era apto para entrega: reutilizaba diagramas que no correspondían al contenido, invertía numerosas cadenas causales, exponía notas de producción y fuentes pendientes, presentaba fórmulas como texto LaTeX sin componer y tenía títulos o gráficos recortados.

El v02 corrige todos los problemas **critical** y **major** detectados. La revisión final no encontró desbordes del canvas, flechas invertidas, conectores sobre texto, etiquetas sobre líneas, texto fuera de cajas ni placeholders visibles. Quedan dos asuntos menores de producción y dos sugerencias, documentados al final.

## Cobertura del programa y correspondencia con el libro

| Tema obligatorio | Slides principales | Verificación |
|---|---:|---|
| Serie y transformada de Fourier | 18–29; 133–136 | Cubierto; ecuaciones, símbolos y unidades contrastados con TEX 5.4.1–5.4.4. |
| Respuesta en frecuencia y espectro | 52–62; 140–141 | Cubierto; se distingue señal, sistema, entrada, respuesta y salida. |
| Infrasonido, audible y ultrasonido | 74–83 | Cubierto con límites condicionados y sin universalizar umbrales. |
| Rango dinámico vocal, instrumental y auditivo | 77–83; 142 | Cubierto; se exige declarar tarea, montaje, descriptor y condiciones. |
| Fundamental, armónicos, parciales y sobretonos | 63–73 | Cubierto; se separan periodicidad, amplitud, resonancia y terminología. |
| Armónicos y octavas | 84–94 | Cubierto; se diferencia múltiplo entero de razón 2:1. |
| Bandas, centro y ancho | 84–94; 143 | Cubierto; fórmulas y unidades verificadas contra TEX 5.8. |
| Filtros y frecuencias de corte | 95–105; 144 | Cubierto; se distingue modelo ideal, respuesta real, criterio de corte y transición. |
| Ponderaciones A, C y Z; dB(A) | 106–116; 145 | Cubierto; ejemplo de 63 Hz verificado contra TEX 5.10.1 y la referencia normativa citada por el libro. |
| Sonómetro, descriptores y nivel equivalente | 117–124; 146–148 | Cubierto; cadena de medición, Leq, Fast, Slow, máximo, pico y verificación instrumental. |

No se detectaron omisiones del programa. Las ampliaciones sobre DFT, FFT, bins, ventanas, fuga y espectrograma corresponden al capítulo del libro y preparan las aplicaciones posteriores.

## Hallazgos y correcciones

| ID | Severidad inicial | Dimensión | Problema | Corrección aplicada en v02 | Estado |
|---|---|---|---|---|---|
| CR-01 | critical | Diseño | Portada y varios títulos largos se superponían con subtítulos o quedaban recortados. | Escala tipográfica dependiente de longitud, mayor altura de título, nueva posición del subtítulo y rótulo de unidad separado de la barra superior. | closed |
| CR-02 | critical | Diagramas | Las flechas de procesos apuntaban al origen en vez del destino en adquisición, sistema X–H–Y, fuente–filtro, filtros, sonómetro y recapitulaciones. | Conectores editables reconstruidos con punta en el extremo de destino y orden de lectura izquierda→derecha. | closed |
| CR-03 | critical | Contenido / diagramas | Un mismo diagrama genérico se reutilizaba para periodicidad, transformada, DFT, espectrograma, bandas, filtros, ponderaciones y aplicaciones que no representaba. | Se retiró el mapeo automático inadecuado. Cada slide usa ahora ecuación, comparación o proceso derivado de su contenido; se conservaron solo gráficos cuantitativos pertinentes. | closed |
| CR-04 | critical | Producción / naturalidad | Slides 48, 71, 108, 110, 111, 115, 138, 143 y 145 mostraban “pendiente”, “provisional”, “bloqueado” o instrucciones internas. | Sustitución por contenido académico verificable, síntesis cualitativa o ejemplo resuelto del libro. Las advertencias de producción quedaron fuera de la superficie proyectada. | closed |
| CR-05 | critical | Fórmulas | Slides 22–27, 33, 37, 50, 57–59 y 133–146 mostraban guiones bajos, llaves y sintaxis LaTeX sin componer; algunas omitían la fórmula anunciada. | Ecuaciones centrales reescritas como texto matemático editable y legible, con subíndices Unicode, límites de integración, logaritmos, símbolos y unidades. | closed |
| CR-06 | critical | Contenido | El ejemplo de ponderación a 63 Hz se declaraba provisional aunque el libro aporta el valor nominal y la cita. | Se incorporó el cálculo `80,0 − 26,2 = 53,8 dB(A)` y se limitó explícitamente su uso a un tono de 63 Hz bajo iguales condiciones. | closed |
| MJ-01 | major | Pedagogía | Ejemplos numéricos y comparaciones (24, 37, 58, 80, 88, 90, 92, 101, 121) no mostraban el cálculo anunciado. | Se añadieron datos, relación usada, resultado y significado físico en layouts de ecuación o ejemplo. | closed |
| MJ-02 | major | Pedagogía | Slides de espectrograma, ventanas, rango dinámico, ponderación y medición incluían paneles vacíos o visuales no funcionales. | Se reemplazaron por definiciones operativas, condiciones de lectura, límites de inferencia y procesos editables. | closed |
| MJ-03 | major | Diagramas | En v01 algunas líneas atravesaban el orden lógico y los diagramas no conservaban una jerarquía clara entre título y cuerpo. | Nodos de 22–25 pt, ecuaciones de 32–40 pt, márgenes internos amplios y corredores de flechas sin texto. | closed |
| MJ-04 | major | Diseño | Gráficos reutilizados fuera de contexto, labels recortados y slides casi vacías generaban carga cognitiva o conclusiones equivocadas. | Se restringieron los charts a slides donde el gráfico responde a la pregunta; el resto usa visuales específicos o composición textual. | closed |
| MJ-05 | major | Naturalidad | Repetición de tarjetas “Primera lectura / Segunda lectura / Qué leer” y composiciones clonadas producía una estética genérica. | Se aumentó la variedad entre procesos, ecuaciones, comparaciones, ejercicios, recaps, tablas conceptuales, imágenes técnicas y gráficos. | closed |
| MJ-06 | major | Producción | Slides 20 y 102 prometían escucha sin audio ni enlace utilizable. | Se reformularon como comparación estática y se dejó la demostración sonora como actividad opcional controlada, sin prometer un recurso inexistente. | closed |
| MJ-07 | major | Producción | Recapitulaciones de seis bloques excedían el ancho del canvas. | Ancho y separación adaptativos para cinco y seis nodos. | closed |
| MN-01 | minor | Diseño | Algunos créditos normativos ocupan dos líneas. | Se mantuvieron por trazabilidad; no invaden el contenido ni el footer. | closed |
| MN-02 | minor | Producción | El exportador conserva `alt` en el modelo de artifact-tool, pero no escribe el atributo OOXML `descr` en las imágenes exportadas. | Se asignaron nombres estables a las 26 imágenes y se conservaron captions y texto alternativo en el modelo inspeccionable. Requiere remediación posterior del PPTX si se exige accesibilidad plena. | open |
| SG-01 | suggestion | Producción | Las ecuaciones avanzadas son texto matemático editable, no objetos de ecuación nativos de Office. | Mantener como está para máxima compatibilidad o convertir selectivamente a ecuaciones Office en una fase posterior. | open |
| SG-02 | suggestion | Multimedia | No se incrustaron audio ni video. | Las slides afectadas tienen alternativas estáticas completas; producir audio propio sería una ampliación, no un requisito para comprender la unidad. | open |

## Revisión por dimensión

### Contenido

- Cobertura completa del programa.
- Correspondencia comprobada con el capítulo 5 del libro.
- Fórmulas revisadas: serie y transformada de Fourier, duración observada, resolución, respuesta en frecuencia, ganancia, retardo, rango dinámico, centro geométrico, límites de bandas, suma energética y nivel equivalente.
- Símbolos y unidades visibles: s, Hz, Pa, Pa·s, dB, dB SPL, dB(A), rad.
- Se conserva la distinción entre registro, señal ideal, algoritmo, resultado, sistema, medición y percepción.
- El caso de 63 Hz y las constantes Fast/Slow se apoyan en las referencias citadas por el libro; no se inventaron tolerancias ni tablas normativas.

### Pedagogía

- La secuencia avanza desde lectura temporal hacia Fourier, digitalización, ventanas, señal/sistema, voz, rangos, bandas, filtros, ponderaciones y sonómetro.
- Se recuperan RMS, presión, período, frecuencia, fase y decibel de unidades anteriores.
- Hay ejemplos numéricos, preguntas de predicción, ejercicios, errores frecuentes y recapitulaciones al final de cada bloque.
- Las aplicaciones a voz, audífonos, audiometría y medición están acompañadas por límites de inferencia.
- El contenido denso se segmenta; no se detectaron slides con texto por debajo del umbral cómodo de aula en los diagramas corregidos.

### Diseño

- Contraste, márgenes, jerarquía y alineación consistentes con la plantilla institucional.
- Se eliminaron desbordes y títulos solapados.
- Los charts conservados tienen función pedagógica explícita.
- No hay imágenes deformadas ni fondos decorativos que compitan con el contenido.
- Se redujo la repetición de layouts sin introducir estética publicitaria.

### Diagramas y esquemas

- Cero flechas con sentido invertido en el v02.
- Cero puntas sobre texto o fórmulas.
- Cero conectores que atraviesen cajas.
- Cero etiquetas montadas sobre líneas.
- Cero textos fuera de sus cajas.
- Cero auto-shrink; los textos usan tamaños explícitos.
- Los procesos se revisaron dentro de la slide final, no como assets aislados.
- Formas, cajas, textos y conectores permanecen editables.

### Producción

- Formato 16:9.
- 150 slides; 150 notas del orador.
- 2 masters y 27 layouts conservados.
- 3 hipervínculos externos presentes.
- 26 imágenes con nombre estable; texto alternativo presente en la inspección de artifact-tool, con la limitación de exportación documentada en MN-02.
- Tamaño final: 1,89 MB.
- No hay audios, videos ni enlaces multimedia rotos.
- La versión v01 se preservó; el archivo corregido se guardó como v02.

### Naturalidad

- Se eliminaron frases de estado de producción y marcas típicas de borrador.
- Las portadas y divisores conservan tono académico, sin promesas grandilocuentes.
- No se usan iconos genéricos ni imágenes decorativas.
- Las tarjetas repetidas se limitaron a recaps o comparaciones donde cumplen una función clara.

## Verificación final

- Render completo de las 150 slides: **realizado**.
- Revisión ampliada de slides críticas y mayores: **realizada**.
- `slides_test.py`: **Test passed. No overflow detected.**
- Auditoría del paquete PPTX: 150 slides, 150 notes, 2 masters, 27 layouts, 3 hyperlinks, 1,89 MB.
- Problemas critical abiertos: **0**.
- Problemas major abiertos: **0**.
- Problemas minor abiertos: **1**.
- Sugerencias abiertas: **2**.

## Estado

**Aprobado con observaciones menores.** No existen problemas críticos ni mayores abiertos. La unidad no se declara plenamente accesible hasta resolver MN-02 si la entrega exige texto alternativo escrito en el atributo OOXML estándar.

---

## Actualización de cierre — versión final

Fecha: 2026-08-03
Archivo revisado: `unidad_05_analisis_frecuencial_final.pptx`
SHA-256: `2D00BF0391C3B7F133BE28F965AE69F9FDFC76B6492905FE65A27962F4AF3AF7`.

### Problemas resueltos después de v02

| id | severidad original | problema | corrección final | estado |
|---|---|---|---|---|
| FINAL-01 | major | Ruta de 104 slides y 438 min difícil de dictar | Ruta CENTRAL visible de 77 slides; 55 de ampliación y 18 de respaldo; seis encuentros | resuelto |
| FINAL-02 | major | Formalismo sin ruta de omisión clara | Integrales, forma compleja y DFT formal fuera de la ruta central | resuelto |
| FINAL-03 | major | U05-023 con límites y definiciones inconsistentes | Intervalo `t∈[t₀,t₀+T₀]`, símbolos y unidades explícitos | resuelto |
| FINAL-04 | major | U05-042 con `xw(t)` ambiguo | “señal ventaneada = x(t)·w(t)” y nodo final sin doble etiqueta | resuelto |
| FINAL-05 | major | U05-048 sin espectrograma utilizable | Figura sintética del libro, ejes, barra de color, consigna y límite clínico | resuelto |
| FINAL-06 | major | U05-092 remitía a otra slide sin cálculo completo | Límites y ancho calculados y redondeados al final | resuelto |
| FINAL-07 | major | U05-110/111 con notación ambigua y estado provisional | Relación verbal y ejemplo de 63 Hz verificado | resuelto |
| FINAL-08 | major | U05-120/121 priorizaban formalismo | Intuición cuadrática central, ejemplo a continuación e integral en respaldo | resuelto |
| FINAL-09 | major | Caso U05-126/127/149 no autosuficiente | Datos, unidades, resultados, ganancia y fase completos | resuelto |
| FINAL-10 | major | Paleta y jerarquía fuera del sistema del curso | Paleta institucional aplicada y cuerpo central mínimo de 20 pt | resuelto |
| FINAL-11 | major | Solapamiento de portada detectado en render | Corredor vertical y separación título/subtítulo corregidos | resuelto |

### Revisión de diagramas en render final

- No se observan flechas sobre texto o fórmulas.
- No hay etiquetas apoyadas en conectores.
- No hay conectores atravesando cajas o contenidos.
- No hay texto fuera de cajas ni clipping.
- No se usó auto-shrink como solución.
- Las ecuaciones centrales son legibles; los cuerpos de la ruta central cumplen 20 pt o más.
- U05-042 y U05-149 se inspeccionaron a tamaño completo dentro de la slide final.

### Auditoría final

- 150 slides y 150 notas; 150/150 notas con fuentes.
- 2 masters, 27 layouts, 16:9.
- 1658 formas editables y 27 imágenes.
- 3 enlaces externos verificados.
- 150 PNG renderizados y 150 páginas de PDF.
- `slides_test.py`: sin desbordes.
- Problemas `critical` abiertos: **0**.
- Problemas `major` abiertos: **0**.

### Observaciones abiertas

| id | severidad | observación | decisión |
|---|---|---|---|
| MN-FINAL-01 | minor | El alt text no persiste en OOXML `descr` (0/27 imágenes). | Documentar y reinyectar si la entrega exige accesibilidad formal. |
| MN-FINAL-02 | minor | Algunas slides de ampliación/respaldo conservan 18,75 pt. | Aceptado porque no se proyectan por defecto; la ruta central cumple 20 pt. |
| SG-FINAL-01 | suggestion | Ecuaciones editables como texto, no OMML. | Migrar selectivamente en una futura revisión técnica. |
| SG-FINAL-02 | suggestion | No hay audio/video incrustado. | Añadir solo si existe un recurso estable y una alternativa estática. |

## Dictamen final actualizado

**Aprobado para entrega y dictado.** No existen problemas críticos ni mayores abiertos. Las observaciones menores quedan registradas en `final_report.md` y no afectan cobertura, exactitud, legibilidad de la ruta central, editabilidad ni consistencia pedagógica.
