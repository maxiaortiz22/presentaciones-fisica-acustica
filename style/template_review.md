# Revisión del template académico v01

**Archivo revisado:** `output/fisica_acustica_template_v01.pptx`  
**Fecha:** 2026-07-28  
**Alcance:** estructura, render, legibilidad, consistencia, editabilidad y soporte de contenidos.

## Resultado

**Aprobado para comenzar storyboards y borradores de unidades.** No se detectaron problemas críticos, desbordes ni objetos fuera del área de diapositiva.

El archivo es un template demostrativo, no una presentación completa de la Unidad 1. Contiene 27 diapositivas breves: una demostración por cada layout implementado.

## Estructura verificada

| Comprobación | Resultado |
|---|---|
| Relación de aspecto | 16:9, 960 × 540 pt |
| Diapositivas de demostración | 27 |
| Slide Masters reales | 2 |
| Layouts reales | 27 |
| Master claro | `FA_MASTER_CLARO`, 24 layouts |
| Master bordó | `FA_MASTER_BORDO`, 3 layouts |
| Placeholders por layout | entre 3 y 4 |
| Layouts sin placeholders | 0 |
| Layouts sin numeración dinámica | 0 |
| Notas del orador | 27 |
| Fuentes detectadas | Calibri, Calibri Light y Cambria Math |

Los tres layouts agregados al catálogo original son:

- `FA_02B_CONOCIMIENTOS_PREVIOS`;
- `FA_06B_DOS_COLUMNAS`;
- `FA_14B_MINI_EJERCICIO`.

Se incorporaron para cumplir funciones pedagógicas distintas que no debían quedar resueltas como simples variantes manuales.

## Objetos y editabilidad

| Tipo de objeto | Verificación |
|---|---|
| Formas y textos | 423 formas, de las cuales 234 contienen texto editable |
| Gráfico | 1 chart nativo editable |
| Tabla | 1 tabla nativa editable |
| Diagramas | formas y conectores nativos |
| Fórmulas de muestra | texto editable en Cambria Math; no raster |
| Imágenes | 2 imágenes conservadas como objetos independientes |
| GIF | archivo `.gif` preservado dentro del paquete PowerPoint |
| Logo | objeto de imagen ubicado en ambos masters |
| Texto alternativo | presente en logo, imagen de referencia y GIF |

El render de PowerPoint muestra el primer cuadro del GIF; la animación se conserva para el modo presentación.

## Revisión visual

Se renderizaron las 27 diapositivas a 1600 × 900 px. Se revisó la vista mosaico y cada layout a tamaño completo.

| Criterio | Resultado |
|---|---|
| Desbordes y recortes | sin incidencias |
| Objetos fuera de la diapositiva | 0 |
| Alineaciones | consistentes con la grilla y los márgenes definidos |
| Títulos | legibles y alineados a izquierda por defecto |
| Cuerpo | mantiene tamaños aptos para aula en los ejemplos |
| Pie y numeración | estables en todos los layouts |
| Contraste | suficiente en fondos claros y bordó |
| Imágenes | sin deformación; caption y fuente separados |
| Gráficos | ejes, escala y rótulos legibles |
| Ecuaciones | editables y acompañadas por símbolos e interpretación |
| Tablas | encabezado claro y densidad moderada |
| Variedad | suficiente para decks extensos sin apariencia mecánica |

La prueba automatizada de overflow finalizó con `Test passed. No overflow detected.`

## Problemas encontrados y correcciones

| Problema | Severidad | Corrección | Estado |
|---|---|---|---|
| Los placeholders reales cubrían parte del contenido de demostración. | Alta | Se mantuvieron como placeholders editables con relleno y línea transparentes. | Corregido |
| La lectura de un script por Windows PowerShell alteraba caracteres españoles del pie. | Alta | Se normalizó la ejecución en UTF-8 y se verificó el texto renderizado. | Corregido |
| La numeración inicial era un objeto de demostración. | Alta | Se sustituyó por placeholder dinámico de número de diapositiva en cada layout. | Corregido |
| Los títulos de ejes del gráfico eran demasiado grandes. | Media | Se redujeron y normalizaron dentro del chart nativo. | Corregido |
| El mapa de recapitulación no mostraba con claridad la bifurcación y convergencia. | Media | Se reconstruyó con conectores nativos y dirección explícita. | Corregido |
| El exportador no conservó el texto alternativo de dos imágenes. | Media | Se añadió y verificó el texto alternativo en PowerPoint. | Corregido |

## Decisiones técnicas

El contenido editable se construyó con `@oai/artifact-tool`. La versión disponible del exportador presentó una limitación al serializar masters y layouts creados desde cero. Para no degradar el archivo a una colección de slides planas, la jerarquía final de los dos masters, los 27 layouts, los placeholders y la numeración dinámica se ensambló y verificó mediante la API nativa de PowerPoint.

La inspección del paquete OOXML confirma:

- 27 archivos de diapositiva;
- 2 archivos de Slide Master;
- 27 archivos de layout;
- 27 archivos de notas;
- el GIF original embebido.

## Limitaciones y próximos controles

1. Las fórmulas de demostración son texto editable en Cambria Math. En las unidades, usar ecuaciones nativas de PowerPoint/OMML cuando la estructura matemática lo requiera.
2. El logo se recuperó de la presentación original del docente. Debe reemplazarse por el activo vectorial institucional cuando UCASAL lo provea.
3. La validación de escalabilidad definitiva se realizará con una unidad real de 30–50 o más diapositivas.
4. Los placeholders son transparentes por diseño: indican estructura y mantienen editabilidad sin tapar el contenido de las slides de demostración.

## Artefactos de revisión

- `style/template_mosaic.png`;
- `output/fisica_acustica_template_preview.pdf`;
- render completo temporal de 27 diapositivas utilizado para la inspección.
