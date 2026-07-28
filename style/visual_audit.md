# Auditoría visual de las presentaciones de referencia

## Estado y alcance

- Fecha de auditoría: 2026-07-28.
- Referencia primaria: `context/referencias_visuales/Unidad 1 - Nociones básicas e introducción a la acústica.pptx`.
- Referencia secundaria: `context/referencias_visuales/The_Acoustic_Blueprint.pptx`.
- Objetivo: definir qué conservar, mejorar, reemplazar, descartar o reservar para casos particulares al construir el sistema visual de las diez unidades.
- Esta auditoría no decide qué deck es “mejor” en términos absolutos. Evalúa qué aporta cada uno al nuevo sistema.

## Método

1. Se leyeron `AGENTS.md`, la skill `style-system` y las instrucciones de auditoría de presentaciones.
2. Se renderizaron todas las diapositivas con PowerPoint 16.0 a 1600 × 900 px:
   - deck del docente: 20 de 20 diapositivas;
   - deck de Gemini: 15 de 15 diapositivas.
3. Se inspeccionó cada render a tamaño completo y se revisó el flujo completo mediante montajes.
4. Se inspeccionó la estructura interna de ambos PPTX: dimensiones, masters, layouts, placeholders, tipos de objeto, tipografías, ecuaciones, recursos y texto alternativo.
5. Se contrastaron las decisiones con el propósito del curso: clases universitarias extensas, primer año, rigor académico, legibilidad en aula y editabilidad.

Incidencia técnica: el renderizador empaquetado no pudo localizar su dependencia `@oai/artifact-tool`. Para no omitir la revisión visual, se utilizó el motor nativo de PowerPoint. Los archivos fuente no fueron modificados.

## Conclusión ejecutiva

La base identitaria debe provenir del deck del docente: formato 16:9, fondo claro, bordó institucional, presencia de UCASAL, tono directo, estructura académica y uso de ecuaciones nativas. Sus principales problemas no son de identidad, sino de ejecución: barra superior demasiado alta, jerarquías variables, márgenes irregulares, exceso de texto en algunas slides, imágenes heterogéneas y uso efectivo de solo dos layouts.

Gemini aporta buenas ideas de organización: comparación en paralelo, secuencias fuente–medio–receptor, distinción entre magnitud física y atributo perceptual, síntesis visual y anticipación de errores. Sin embargo, no puede funcionar como base material ni estilística: cada slide es una única imagen rasterizada, no hay objetos editables ni texto alternativo, el fondo cuadriculado es omnipresente, hay glows, tarjetas, iconografía genérica, ilustraciones de aspecto automático y títulos con tono publicitario.

La dirección resultante es:

- conservar el carácter universitario, sobrio e institucional del docente;
- reducir el peso de la banda bordó y convertirla en una firma más liviana;
- usar una grilla real para alinear, no una cuadrícula decorativa visible;
- adoptar de Gemini únicamente estructuras pedagógicas útiles;
- reconstruir diagramas, tablas, ecuaciones y gráficos como objetos editables;
- evitar que la coherencia se convierta en repetición mecánica.

## Datos estructurales

| Indicador | Deck del docente | Deck de Gemini | Implicación |
|---|---:|---:|---|
| Diapositivas | 20 | 15 | Ambas referencias fueron revisadas en su totalidad. |
| Relación de aspecto | 16:9 | 16:9 | Se conserva 16:9. |
| Tamaño físico | 13,333 × 7,5 in | 17,778 × 10 in | Se normaliza al formato PowerPoint panorámico estándar de 13,333 × 7,5 in. |
| Masters | 1 | 1 | Conviene mantener un sistema simple de un master principal. |
| Layouts disponibles | 11 | 11 | La cantidad no garantiza variedad real. |
| Layouts usados | 2 | 1 (`Blank`) | El nuevo sistema necesita un catálogo funcional y uso efectivo. |
| Objetos de imagen | 29 | 15 | En Gemini hay exactamente una imagen a pantalla completa por slide. |
| Texto editable | Sí | No | La organización de Gemini debe reconstruirse, no copiarse. |
| Ecuaciones OMML nativas | 39 | 0 | La editabilidad matemática del docente es un rasgo a conservar. |
| Tablas o gráficos nativos | No se detectaron | No | Deben definirse componentes nativos nuevos. |
| Objetos con texto alternativo | 10 | 0 | El nuevo sistema debe exigir accesibilidad sistemática. |
| Tipografía de tema | Gill Sans MT | No evaluable por rasterización | Gill Sans MT no está disponible en el equipo; PowerPoint sustituye parte del contenido. |
| Fuentes efectivamente detectadas | Calibri, Arial y Google Sans | No evaluables | Se unifica en fuentes instaladas y previsibles. |

## Auditoría por elemento y clasificación

Las clasificaciones se aplican a cada referencia. La columna “Decisión del nuevo sistema” resuelve la combinación.

| Elemento | Docente | Gemini | Decisión del nuevo sistema |
|---|---|---|---|
| Relación de aspecto | **Conservar.** 16:9 adecuado para aula y pantallas actuales. | **Conservar.** También 16:9. | 13,333 × 7,5 in, sin formatos físicos alternativos. |
| Portada | **Mejorar.** Conserva institución, unidad, docente y sobriedad; el logo domina demasiado y el bloque bordó es pesado. | **Usar solo en casos particulares.** La relación onda–oído comunica el campo, pero la ilustración es decorativa, la composición es cinematográfica y aparece la marca NotebookLM. | Portada académica mínima con identidad UCASAL, un solo visual disciplinar opcional y sin slogans. |
| Tipografías | **Reemplazar la configuración, conservar el carácter.** La mezcla Gill Sans/Calibri/Arial/Google Sans genera sustituciones. | **Reemplazar.** Mezcla visual de serif y sans dentro de una imagen; no es editable. | Calibri Light para títulos, Calibri para texto y Cambria Math para ecuaciones. |
| Tamaños | **Mejorar.** Oscilan entre 16 y 48 pt; varias slides densas dependen de 20 pt. | **Mejorar.** Títulos muy grandes y textos internos pequeños o densos. | Escala fija con cuerpo habitual de 22–24 pt y mínimo de 20 pt; títulos habituales de 36 pt. |
| Paleta | **Conservar.** Bordó `#4D1434`, acento `#903163`, gris `#969FA7`, carbón `#3D3D3D` y colores institucionales del logo. | **Usar solo en casos particulares.** El contraste turquesa–naranja sirve para distinguir físico/perceptual, pero es excesivamente brillante. | Bordó como identidad; teal y ocre apagados solo como semántica disciplinar secundaria. |
| Fondos | **Conservar y mejorar.** El blanco es legible y académico; falta una variante cálida y una lógica de sección. | **Descartar como fondo general.** La cuadrícula constante añade ruido y vuelve todas las slides “planos” artificiales. | Blanco predominante; marfil muy claro para recapitulaciones o aplicaciones; cuadrícula solo dentro de gráficos o esquemas que la necesiten. |
| Títulos | **Mejorar.** Son descriptivos, pero alternan centrado/izquierda, mayúsculas, bandas y alturas. Algunos ocupan dos líneas dentro de una banda rígida. | **Reemplazar.** Abundan fórmulas publicitarias: “El gran puente”, “Caja de herramientas”, “Desmitificando”, “Plano acústico completo”. | Títulos informativos, naturales y preferentemente alineados a la izquierda; hasta dos líneas diseñadas, no forzadas. |
| Subtítulos | **Mejorar.** Poco sistemáticos y a veces sustituidos por encabezados subrayados dentro del cuerpo. | **Usar solo en casos particulares.** Ayudan a contextualizar, pero compiten con títulos grandes. | Subtítulo opcional de 22–24 pt, una línea, solo cuando añade una relación o pregunta pedagógica. |
| Pie de página | **Mejorar.** Logo y numeración dan identidad, pero el logo es grande y desaparece en varias slides. Hay placeholders de fecha y pie vacíos en el master. | **Descartar.** La marca NotebookLM no pertenece al curso y no aporta orientación. | Pie discreto y consistente: wordmark pequeño, unidad/sección y número de slide. Sin fecha por defecto. |
| Numeración | **Mejorar.** `n/20` orienta, pero el total manual puede quedar obsoleto. | **Reemplazar la ausencia.** No hay numeración útil. | Número actual automático; total opcional solo en una versión cerrada o generada. |
| Márgenes | **Mejorar.** Algunos contenidos respetan 0,6 in; otros llegan al borde o pierden el master (slides 4, 6, 8, 10, 12, 16 y 18). | **Mejorar.** Hay marco exterior, pero muchos títulos y componentes quedan demasiado próximos a él. | Margen seguro horizontal de 0,67 in; zona superior e inferior reservada y estable. |
| Alineaciones | **Mejorar.** La estructura general existe, pero cambia entre slides y algunos elementos “flotan”. | **Usar solo en casos particulares.** La alineación interna es fuerte, aunque a veces parece una infografía de plantilla. | Grilla de 12 columnas y alineación óptica; cada slide debe tener un eje dominante visible. |
| Densidad de texto | **Mejorar.** Slides 4, 5, 6, 7, 11, 13 y 14 concentran demasiadas ideas o líneas. | **Mejorar.** Varias slides son legibles de cerca, pero no desde el fondo de un aula; 12–14 son particularmente densas. | Una idea principal; 55–75 palabras visibles como rango habitual, hasta 90 solo en layouts explícitamente textuales. |
| Uso de imágenes | **Mejorar.** Hay imágenes pertinentes, pero con estilos y resoluciones variables; el meme de la slide 16 es culturalmente dependiente y no tiene función académica suficiente. | **Usar solo en casos particulares.** Algunas ilustraciones explican relaciones, pero otras son pseudo-3D o decorativas; todas están aplanadas. | Priorizar gráficos propios, fotografías técnicas y diagramas simples. No usar stock conceptual ni ilustración automática como relleno. |
| Ecuaciones | **Conservar y mejorar.** Hay 39 ecuaciones nativas y editables. Falta uniformar tamaño, variables, unidades y espacio alrededor. | **Descartar como implementación.** Cualquier fórmula queda rasterizada y no puede corregirse. | OMML/Cambria Math, definición de símbolos, unidades y lectura física; ecuación nunca como imagen salvo fuente histórica. |
| Gráficos | **Mejorar.** Algunos gráficos son útiles pero provienen de imágenes heterogéneas, con etiquetas pequeñas o estilos externos. | **Usar solo en casos particulares.** Son valiosas las relaciones visuales, pero se confunden diagramas con decoración y se usan glows. | Gráficos reproducibles, ejes y unidades claros, estilo mate, sin brillos; SVG o chart nativo según el caso. |
| Tablas | **Reemplazar.** La tabla de prefijos de la slide 8 está rasterizada, sin jerarquía y aislada de una explicación. | **Usar solo en casos particulares.** La comparación masa/peso organiza bien, pero es una imagen y usa un bloque naranja demasiado agresivo. | Tablas nativas con pocas columnas, encabezados claros, bandas suaves y lectura guiada. |
| Jerarquía | **Mejorar.** La banda bordó compite con el contenido y los títulos internos cambian de peso. | **Usar solo en casos particulares.** Buena focalización mediante contraste, pero con demasiados marcos y llamadas simultáneas. | Un foco primario, uno secundario y detalles; no más de dos niveles de cajas por slide. |
| Consistencia | **Mejorar.** Hay identidad reconocible, pero varios elementos del master desaparecen y cambia el tratamiento de títulos, cuerpo e imágenes. | **Conservar la disciplina, descartar la repetición.** Es coherente, pero demasiado uniforme y mecánico. | Tokens estables con variación controlada de siluetas. |
| Variedad de layouts | **Mejorar.** Solo se usan portada y título+contenido, aunque el archivo contiene 11 layouts. | **Usar solo en casos particulares.** Cambian las composiciones, pero casi todas son infografías densas. | Catálogo de layouts pedagógicos; la elección depende de la función de la slide. |
| Sensación académica | **Conservar.** Se siente producido para una clase real y vinculado con la institución. | **Usar solo en casos particulares.** La intención pedagógica existe, pero el acabado de infografía automática reduce naturalidad. | Académica, humana y editorial; moderna sin apariencia corporativa. |
| Señales de diseño automático | **Conservar la ausencia general; mejorar irregularidades.** Las variaciones revelan autoría humana, aunque no deben convertirse en errores. | **Descartar.** Glows, tarjetas, cuadrícula constante, iconos repetidos, pseudo-3D, titulares grandilocuentes y marca de la herramienta. | Sin glows, sin decoraciones por sistema y sin textos que suenen a campaña. |
| Legibilidad desde aula | **Mejorar.** Varias slides son legibles, pero las densas y algunos gráficos externos tienen texto pequeño. | **Mejorar.** Buen contraste general; la densidad y la rasterización limitan ampliación y lectura distante. | Cuerpo 22–24 pt, captions 14–16 pt, tablas 18 pt mínimo, contraste WCAG equivalente y prueba a 25 % de zoom. |
| Editabilidad | **Conservar y ampliar.** Texto, placeholders y ecuaciones son editables; muchas figuras siguen siendo imágenes. | **Descartar como implementación.** Cada slide es un bitmap completo. | Todo elemento importante debe ser texto, forma, tabla, gráfico, SVG o ecuación editable. |

## Revisión slide por slide: deck del docente

| Slide | Observación visual | Decisión |
|---:|---|---|
| 1 | Identidad UCASAL clara; logo sobredimensionado y bloque bordó pesado. | Conservar identidad; mejorar proporciones. |
| 2 | Buena definición inicial y pregunta clara; título y párrafo compiten; figura pequeña y gris. | Conservar secuencia; mejorar jerarquía y visual. |
| 3 | Relación texto–figura comprensible; imagen externa en inglés y estilos ajenos. | Reemplazar figura por diagrama propio. |
| 4 | Aplicación clínica pertinente; exceso de texto; desaparecen header y logo. | Conservar contenido tipo; reemplazar layout. |
| 5 | Título largo y cuerpo denso; categorías útiles. | Dividir en dos slides o usar comparación guiada. |
| 6 | Introducción a SI útil; lista centrada sin eje claro; header incompleto y sin logo. | Reemplazar composición. |
| 7 | Distinción fundamental/derivada importante; demasiadas líneas. | Usar dos columnas o secuencia. |
| 8 | Tabla de prefijos aislada, rasterizada y sin título visible. | Reemplazar por tabla nativa con foco progresivo. |
| 9 | Fórmula central y ejemplo aplicable; buen uso de espacio. | Conservar patrón, mejorar definición de símbolos. |
| 10 | Masa/peso/fuerza y diagrama; buen puente visual, pero falta master y sobra texto en una sola línea. | Conservar idea; reconstruir layout. |
| 11 | Ecuaciones editables y conceptos correctos visualmente; tres bloques densos. | Dividir o usar tabs semánticos no interactivos. |
| 12 | Imagen y texto en dos columnas; buena silueta, pero la imagen externa domina y desaparece el pie. | Conservar proporción; reemplazar asset. |
| 13 | Título de dos líneas correcto como tema, pero demasiado largo para la banda; cuerpo denso. | Acortar título y secuenciar. |
| 14 | Continuación sin título visible; dificulta orientación. | Reemplazar por layout “continuación” con rótulo de sección. |
| 15 | Gráfico pertinente; buen balance 2/3–1/3; etiquetas externas pequeñas. | Conservar estructura; recrear gráfico propio. |
| 16 | Analogía mediante meme; rompe tono y carece de fuente visible. | Descartar como patrón; usar solo si el docente lo justifica y registra. |
| 17 | Dos columnas claras; figura con texto pequeño y borde pesado. | Conservar silueta; recrear figura. |
| 18 | Comparación seno/coseno valiosa; falta header y hay dos estilos gráficos incompatibles. | Reemplazar con gráfico reproducible y anotación propia. |
| 19 | Figura central simple y legible, aunque usa mucho espacio vacío. | Conservar como layout de definición visual. |
| 20 | Cierre humano y sobrio; “Muchas gracias” no sintetiza aprendizaje. | Reemplazar por recapitulación + puente a la unidad siguiente; contacto opcional. |

## Revisión slide por slide: deck de Gemini

| Slide | Observación visual | Decisión |
|---:|---|---|
| 1 | Onda–oído comunica el campo; ilustración automática, serif de portada y marca NotebookLM. | Usar solo la idea conceptual; no el estilo ni el asset. |
| 2 | Buena relación Física–Clínica–Percepción; muy cargada, con brillo y título retórico. | Conservar la estructura ternaria; reconstruir en estilo sobrio. |
| 3 | Fuente–medio–receptor es una excelente organización. Cajas, iconos y glows son genéricos. | Conservar la organización; reemplazar forma visual. |
| 4 | Distingue oscilación local de propagación con una secuencia comprensible. | Conservar idea; redibujar científicamente y sin efectos. |
| 5 | Selección de magnitudes relevantes es útil; diseño tipo dashboard y símbolos/unidades requieren revisión disciplinar. | Usar solo como antecedente de mapa conceptual. |
| 6 | Construcción de magnitudes derivadas muestra dependencias. | Conservar lógica de flujo; simplificar y corregir notación. |
| 7 | Comparación masa/peso es legible; 3D, tabla pesada y frase “destruye las ecuaciones” son impropios. | Conservar comparación; reemplazar tono y tratamiento. |
| 8 | Contraste velocidad de partícula/propagación es didáctico; ilustración puede inducir movimiento circular. | Conservar la distinción; reemplazar visual por onda longitudinal correcta. |
| 9 | Metáfora entrada–proceso–salida es útil; demasiado texto y engranajes genéricos. | Usar solo la estructura funcional. |
| 10 | Relación círculo–seno aporta intuición. Tres tarjetas inferiores repiten formato automático. | Conservar gráfico principal; integrar etiquetas sin tarjetas. |
| 11 | Comparación lineal/logarítmica es pedagógica. El papel rasgado y la prosa grandilocuente distraen. | Conservar comparación de escalas; reemplazar narrativa y decoración. |
| 12 | “Sí/no” organiza errores; exceso de marcos, cruces, checks y caja final. | Conservar contraste conceptual; usar componente “error frecuente”. |
| 13 | Mapea magnitudes físicas a atributos perceptuales. Es una de las mejores ideas organizativas del deck. | Conservar estructura 2 columnas + relaciones; reconstruir sin circuitos decorativos. |
| 14 | Anticipa tres errores clínicos; demasiado densa y mecánica. | Repartir en 2–3 slides o usar un error por slide. |
| 15 | Síntesis fuente–medio–receptor y puente a Unidad 2. Título publicitario e ilustración automática. | Conservar función de síntesis y puente; reemplazar título y visual. |

## Rasgos identitarios que deben sobrevivir

1. Bordó oscuro como ancla visual principal.
2. Fondo claro y alto contraste.
3. Presencia institucional de UCASAL sin convertir el deck en folleto.
4. Tono docente directo, descriptivo y sin slogans.
5. Ecuaciones editables y explicadas.
6. Numeración y orientación dentro de una unidad larga.
7. Aplicaciones a Fonoaudiología integradas con el contenido, no añadidas como decoración.
8. Cierta variación manual y editorial entre slides, siempre dentro de una grilla.

## Ideas de Gemini que sí se incorporan

1. Comparaciones paralelas cuando existe una distinción conceptual real.
2. Secuencias causales simples: fuente → medio → receptor.
3. Mapeos entre magnitud física y experiencia perceptual.
4. Resúmenes visuales que conectan conceptos ya enseñados.
5. Errores frecuentes como herramienta de aprendizaje.
6. Puentes explícitos entre una unidad y la siguiente.
7. Diagramas con una lectura direccional clara.

Estas ideas se incorporan como layouts y componentes editables, no como imágenes ni como una estética de “blueprint”.

## Señales que el nuevo sistema debe evitar

- cuadrícula como textura permanente;
- glows, halos y contornos luminosos;
- cajas redondeadas para cada frase;
- iconos de check/cruz como recurso dominante;
- engranajes, cerebros, ondas y oídos genéricos usados como relleno;
- pseudo-3D;
- títulos de campaña o metáforas no necesarias;
- texto completo dentro de una imagen;
- marca de herramientas de generación;
- una infografía autónoma por slide sin continuidad de clase;
- footers o logos que desaparecen al cambiar de layout.

## Riesgos que deben controlarse al construir el template

1. Verificar el archivo oficial y la versión correcta del logo UCASAL antes de incorporarlo al master.
2. No heredar placeholders vacíos de fecha o pie.
3. Probar que Calibri y Cambria Math se resuelvan sin sustitución en el equipo docente.
4. Construir diagramas de ejemplo con formas nativas o SVG y comprobar su editabilidad.
5. Validar el sistema con una unidad real de al menos 30 slides antes de congelar la versión 1.
6. Revisar que la variante de dos líneas de título no reduzca el cuerpo por debajo del mínimo.

## Verificación del template v01

La especificación se materializó en `output/fisica_acustica_template_v01.pptx` y fue revisada el 2026-07-28.

### Resultado visual

- 27 diapositivas de demostración renderizadas a 1600 × 900 px;
- revisión individual y vista mosaico completadas;
- sin desbordes, solapamientos ni objetos fuera del lienzo;
- títulos, cuerpo, pies y numeración legibles desde aula;
- fondos simples y contraste suficiente;
- variedad controlada sin repetición mecánica;
- continuidad visible con el bordó, la regla superior y la presencia institucional del deck docente;
- sin cuadrículas decorativas, glows, stock conceptual ni iconografía genérica repetida.

### Resultado estructural

- formato 16:9;
- 2 Slide Masters reales;
- 27 layouts reales;
- numeración dinámica y pie coherente en todos los layouts;
- placeholders reales y transparentes;
- fuentes limitadas a Calibri, Calibri Light y Cambria Math;
- gráfico, tabla, formas, conectores y fórmulas de muestra editables;
- GIF preservado como archivo multimedia;
- notas del orador en las 27 diapositivas;
- texto alternativo en los recursos visuales incorporados.

### Ajustes derivados del render

1. Se hicieron transparentes los placeholders para que la estructura editable no cubra el contenido demostrativo.
2. Se corrigió la codificación del pie institucional.
3. Se reemplazó la numeración dibujada por un placeholder dinámico.
4. Se redujo la escala de los rótulos de ejes del chart nativo.
5. Se reconstruyó el mapa de recapitulación con conectores y dirección explícita.
6. Se restauró el texto alternativo de las imágenes después de la exportación.

La revisión detallada queda registrada en `style/template_review.md`. Permanece abierto el control con una unidad real de 30–50 o más diapositivas y la sustitución del logo raster por el activo vectorial institucional cuando esté disponible.
