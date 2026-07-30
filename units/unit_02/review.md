# Revisión integral — Unidad 02

## Identificación

- **Unidad:** 02 — Leyes de la mecánica clásica y principios de la termodinámica.
- **Archivo revisado:** `output/unidad_02_mecanica_termodinamica_v01.pptx`.
- **Archivo corregido:** `output/unidad_02_mecanica_termodinamica_v02.pptx`.
- **Cantidad de diapositivas:** 110.
- **Fecha de revisión:** 29 de julio de 2026.
- **Estado:** aprobada para uso, sin problemas `critical` ni `major` abiertos.

## Fuentes contrastadas

1. Programa oficial de Física Acústica: alcance obligatorio de la Unidad 2.
2. Capítulo 2 del libro del curso en LaTeX.
3. Capítulo 2 del libro del curso en PDF, pp. 37–60.
4. `brief.md`, `storyboard.md`, `slide_text.md` y `speaker_notes.md`.
5. Bibliografía académica citada en el capítulo y en las diapositivas.

## Método de revisión

La revisión no se limitó al texto ni al XML:

- se examinó el PowerPoint v01 completo;
- se revisó el render de las 110 diapositivas a tamaño final;
- se contrastó la cobertura con el programa y el capítulo del libro;
- se inspeccionaron fórmulas, unidades, definiciones, gráficos, diagramas, fuentes y notas;
- se corrigieron todos los problemas `major`;
- se produjo la versión v02;
- se volvió a renderizar la presentación completa;
- se revisaron nuevamente, a tamaño final, las diapositivas afectadas;
- se ejecutó la prueba automática de desbordes sobre la v02, sin hallazgos.

## Resultado por severidad

| Severidad | Detectados | Corregidos | Abiertos |
|---|---:|---:|---:|
| `critical` | 0 | 0 | 0 |
| `major` | 7 | 7 | 0 |
| `minor` | 3 | 1 | 2 |
| `suggestion` | 1 | 0 | 1 |

## Revisión por dimensión

### Contenido

- La presentación cubre el alcance obligatorio del programa: leyes de Newton, fuerzas relevantes, trabajo y energía, calor, primera y segunda ley, entropía, conservación de la energía y vínculo con la velocidad del sonido.
- La secuencia y el nivel de desarrollo se corresponden con el capítulo 2 del libro.
- Se verificaron, entre otras, las relaciones `F_neta = ma`, `F_pres = Δp A`, `F_el = −kx`, `F_amort = −bv`, `W = Fd`, las expresiones de energía, `ΔU = Q + W_sobre`, `ΔS_total ≥ 0`, `c = √(γRT/M)` y `c ≈ 331 + 0,6 θ`.
- La convención de signos de la primera ley se presenta de forma explícita: `W_sobre` es el trabajo realizado sobre el sistema.
- Las magnitudes y unidades son consistentes. Se corrigió el ejemplo de presión de la diapositiva 30 y se hicieron explícitas las unidades del coeficiente térmico de la diapositiva 103.
- No se detectaron datos inventados ni contradicciones sustantivas con el libro.

### Pedagogía

- La progresión parte de situaciones concretas, introduce fuerza y movimiento, continúa con trabajo y energía, y recién después aborda termodinámica y propagación sonora.
- Los prerrequisitos matemáticos se recuperan antes de utilizarlos.
- Hay ejemplos numéricos, preguntas de comprobación, aplicaciones a oído medio, voz y acústica, recapitulaciones parciales y un cierre integrador.
- Se anticipan errores frecuentes: confundir acción y reacción, masa y peso, fuerza con movimiento, temperatura con calor, y energía con potencia.
- La carga cognitiva está segmentada mediante bloques y rutas de uso. La extensión total exige seleccionar la ruta central para una clase ordinaria; las diapositivas complementarias y de respaldo no deberían proyectarse de manera lineal.

### Diseño

- La jerarquía tipográfica, el contraste y la lectura en aula son adecuados.
- Se revisaron alineaciones, márgenes, captions, fuentes, tamaños, ecuaciones e integración de imágenes en las 110 diapositivas.
- La presentación utiliza variedad controlada de layouts sin abandonar el sistema visual académico.
- Se corrigieron anotaciones y ejes que competían con las curvas en las diapositivas 18, 36, 38, 40, 80, 81 y 103.
- La diapositiva 30 ya no presenta salto ni recorte en la ecuación.
- Las referencias de las diapositivas 100 y 109 ahora son bibliografía visible y rastreable, no instrucciones internas de producción.

### Diagramas y esquemas

- Se revisaron específicamente puntas de flecha, conectores, etiquetas, cajas, desbordes, auto-shrink, tamaño de fuente, ecuaciones y equilibrio de composición.
- En las diapositivas 19, 44 y 96, la etiqueta `F_el + F_amort` se separó del conector y se reubicó debajo del sistema, con distancia suficiente respecto de la línea y de las cajas.
- En la v02 no quedan flechas sobre texto, etiquetas montadas sobre conectores, textos fuera de caja ni fuentes de diagrama demasiado pequeñas.
- Los diagramas corregidos fueron evaluados dentro de la diapositiva final, no solamente como recursos aislados.

### Producción

- Formato 16:9.
- 110 diapositivas y 110 páginas de notas.
- 2 masters y 27 layouts.
- 146 recursos multimedia internos; 78 imágenes relevantes con descripción alternativa.
- 2 enlaces externos verificados: Wikimedia Commons y PhET.
- Archivo v02: 1.702.148 bytes.
- El archivo conserva texto, cajas y estructura de diapositiva editables. Los gráficos y diagramas propios corregidos se insertaron como PNG para asegurar estabilidad de render; sus SVG y scripts reproducibles se conservan en `assets/` y `scripts/`.
- La prueba de desbordes no informó errores.

### Naturalidad

- El tono es académico y directo; no se detectaron portadas grandilocuentes, lenguaje publicitario ni frases de cierre típicas de IA.
- Las imágenes cumplen una función explicativa y no meramente decorativa.
- No hay una repetición mecánica de tarjetas o iconos genéricos.
- Se eliminaron de las diapositivas 100 y 109 instrucciones internas y claves bibliográficas que daban apariencia de material sin terminar.

## Registro de problemas y correcciones

| ID | Slides | Dimensión | Severidad | Problema observado en v01 | Corrección aplicada en v02 | Estado |
|---|---|---|---|---|---|---|
| DR-001 | 18, 36 | Diseño / gráficos | `major` | Anotaciones demasiado próximas a curvas, puntos y etiquetas; lectura ambigua. | Reubicación de rótulos, uso de fondo blanco y regeneración de los gráficos. | cerrado |
| DR-002 | 38, 40, 80, 81, 103 | Diseño / gráficos | `major` | Títulos de eje vertical y ticks con separación insuficiente; anotaciones muy próximas a las curvas. | Aumento del margen izquierdo, ajuste de anotaciones y regeneración de las figuras. | cerrado |
| DR-003 | 19, 44, 96 | Diagramas | `major` | La etiqueta `F_el + F_amort` estaba montada sobre el conector y demasiado próxima a la caja. | Etiqueta separada del conector y ubicada en un corredor libre debajo del sistema. | cerrado |
| DR-004 | 30 | Contenido / diseño | `major` | La ecuación del ejemplo de presión se partía y la unidad quedaba visualmente comprometida. | Ecuación recompuesta en una línea: `F_pres = 1,0×10⁻⁴ N`. | cerrado |
| DR-005 | 100, 109 | Contenido / naturalidad | `major` | Se mostraban instrucciones internas y claves de producción en lugar de referencias completas. | Sustitución por referencias bibliográficas completas, visibles y rastreables. | cerrado |
| DR-006 | 103 | Contenido / diseño | `major` | La aproximación térmica quedaba apretada y el coeficiente no explicitaba sus unidades. | Redacción y fórmula ajustadas; coeficiente expresado en `m·s⁻¹·°C⁻¹`. | cerrado |
| DR-007 | global | Producción / accesibilidad | `major` | Las imágenes del v01 no tenían descripciones alternativas. | Se incorporó descripción alternativa a las 78 imágenes relevantes. | cerrado |
| DR-008 | 19, 36, 44, 80, 96 | Diseño / fuentes | `minor` | Algunas líneas de fuente se recortaban o duplicaban después de sustituir recursos. | Reposición de las líneas de fuente y verificación en el render final. | cerrado |
| DR-009 | global | Notación | `minor` | Subíndices expresados con guion bajo (`F_neta`, `F_el`, `Q_calor`, etc.) en vez de subíndice tipográfico. La convención se define y es legible, pero el acabado puede mejorar. | No se hizo una sustitución global para evitar una modificación masiva fuera del alcance correctivo. | abierto |
| DR-010 | gráficos y diagramas propios | Producción / editabilidad | `minor` | Las figuras corregidas quedan como imágenes dentro del PPT, no como formas nativas de PowerPoint. | Se conservaron SVG y scripts reproducibles; el PNG se usó para estabilidad de render. | abierto |
| DR-011 | global | Pedagogía | `suggestion` | La secuencia completa de 110 diapositivas es demasiado extensa para una única clase lineal. | Mantener el uso por rutas ya previsto en el storyboard: central, complementaria y respaldo. | abierto |

## Revisión final de la v02

Se revisó el render completo de la v02 y, con mayor detalle, las diapositivas 18, 19, 30, 36, 38, 40, 44, 80, 81, 96, 100, 103 y 109. No se observan desbordes, clipping, colisiones entre flechas y texto, etiquetas sobre líneas ni ecuaciones ilegibles.

## Problemas abiertos

No quedan problemas `critical` ni `major`.

Permanecen dos cuestiones `minor` y una `suggestion`:

1. normalizar subíndices tipográficos en una futura pasada global de estilo;
2. convertir a formas nativas de PowerPoint los gráficos o diagramas que necesiten edición directa, conservando la geometría validada;
3. impartir la unidad mediante la ruta central y utilizar las diapositivas complementarias o de respaldo según el tiempo y las dificultades del grupo.

