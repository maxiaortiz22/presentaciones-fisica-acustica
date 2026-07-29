# Prompt — Reparar diagramas generados de la Unidad 1 y reemplazarlos en el PowerPoint

Lee primero `AGENTS.md` y las siguientes skills:

- `diagram-generation`
- `chart-generation`
- `deck-review`
- `style-system`

## Objetivo

Revisar todos los gráficos y diagramas generados para la Unidad 1, corregir problemas de legibilidad y geometría, regenerar los assets afectados y reemplazar dentro del PowerPoint las versiones anteriores por las nuevas, sin alterar contenido no relacionado.

Los problemas observados incluyen:

- flechas que apuntan de forma imprecisa;
- puntas de flecha que cubren texto o símbolos;
- etiquetas de relaciones colocadas sobre conectores;
- conectores que atraviesan cajas o texto;
- texto que sale de los límites de las cajas;
- ecuaciones o anotaciones superpuestas;
- fuentes demasiado pequeñas cuando el visual se observa dentro de la slide completa;
- cajas con demasiado espacio vacío mientras el texto permanece pequeño.

## Archivos objetivo

1. Localiza la versión más reciente de la presentación de la Unidad 1 dentro de:

```text
units/unit_01/output/
```

Busca archivos con un patrón como:

```text
unidad_01_*_v*.pptx
```

2. No edites la presentación de referencia ubicada en `context/referencias_visuales/` salvo que se indique expresamente.

3. Si existen varias versiones candidatas con la misma prioridad y no puede determinarse cuál es la actual mediante `production_log.md`, `change_log.md` o fecha de versión, detén la edición y registra la ambigüedad.

4. Localiza los scripts y assets fuente en:

```text
units/unit_01/scripts/
units/unit_01/assets/
units/unit_01/
```

## Fase 1 — Crear respaldo e inventario

Antes de modificar:

1. crea una copia exacta del PowerPoint objetivo con sufijo `_backup_before_diagram_fix.pptx`;
2. renderiza todas las slides de la versión actual;
3. crea una vista mosaico anterior;
4. identifica todas las slides que contienen assets generados, especialmente:
   - diagramas de cajas y flechas;
   - ecuaciones anotadas;
   - cuadros comparativos;
   - diagramas de procesos;
   - figuras creadas mediante scripts;
5. crea `units/unit_01/diagram_repair_inventory.md` con:
   - slide;
   - objeto o asset;
   - ruta fuente;
   - tipo;
   - problema observado;
   - severidad;
   - método de reparación;
   - relación o ID del objeto dentro del PPTX si puede obtenerse.

No reemplaces todavía ningún objeto.

## Fase 2 — Reparar los assets fuente

Para cada diagrama estructural, aplicar `diagram-generation`.

### Reglas tipográficas

- texto principal de nodos: 22 pt como mínimo; 24 pt preferido;
- encabezados de nodos: 24–28 pt;
- etiquetas de conectores: 20–22 pt;
- ecuaciones: 28 pt o más;
- no usar auto-shrink por debajo de estos valores;
- si el contenido no entra, resumir, ampliar, redistribuir o dividir la slide.

### Reglas de cajas

- medir el texto antes de fijar el tamaño;
- padding interior mínimo: 0,18 in;
- dejar entre 10 % y 20 % de espacio libre;
- evitar más de tres líneas de cuerpo en una caja pequeña;
- no permitir texto fuera de límites;
- no usar cajas enormes con texto pequeño.

### Reglas de flechas

- usar conectores anclados a los bordes;
- definir lado de salida y entrada;
- reservar un corredor vacío;
- colocar etiquetas por encima o debajo de la línea;
- no permitir que una punta cubra texto, símbolos o contornos;
- mantener 0,10 in entre conectores y texto no relacionado;
- usar conectores en codo si una línea recta produce una colisión;
- comprobar que cada flecha llegue al destino semántico correcto.

### Reglas de callouts sobre ecuaciones

- medir el bounding box de la ecuación;
- colocar callouts fuera del área tipográfica;
- terminar el líder a 0,05–0,10 in del símbolo;
- no tocar letras, números, unidades, signos de igualdad o subíndices;
- evitar cruces entre líderes;
- dividir el gráfico si cuatro o más callouts vuelven ilegible la composición.

### Regla de implementación

Preferir diagramas editables de PowerPoint. Si el asset ya es una imagen y recrearlo como formas nativas no compromete la fidelidad, reemplazarlo por formas editables. Si se conserva como archivo externo, preferir SVG y mantener el script o fuente.

## Fase 3 — Bucle de validación por asset

Para cada asset corregido:

1. generarlo al tamaño real que tendrá en la slide;
2. renderizar una preview dentro del mismo espacio disponible;
3. comprobar:
   - cero desbordes;
   - cero clipping;
   - cero conectores sobre texto;
   - cero etiquetas sobre líneas;
   - flechas correctamente orientadas;
   - tamaños mínimos cumplidos;
   - legibilidad en vista de slide completa;
4. corregir;
5. volver a renderizar;
6. repetir hasta cumplir.

No aprobar un asset solo porque el script se ejecutó correctamente.

Si después de cinco iteraciones queda un problema crítico o mayor, no insertarlo: registrar el bloqueo y proponer dividir la slide.

## Fase 4 — Reemplazar los objetos dentro del PowerPoint

Una vez aprobado cada asset:

1. reemplaza explícitamente el objeto embebido en la slide; actualizar el archivo local no es suficiente;
2. conserva, salvo necesidad documentada:
   - slide de destino;
   - posición;
   - tamaño;
   - relación de aspecto;
   - rotación;
   - crop;
   - z-order;
   - nombre o ID de objeto;
   - texto alternativo;
   - hyperlink;
3. si el objeto era una imagen raster y se reemplaza por formas editables, agrupa y nombra el conjunto;
4. no muevas ni edites objetos no relacionados;
5. si la geometría corregida necesita más espacio, ajusta únicamente la región del visual y documenta el cambio;
6. no sobrescribas la versión original.

Guarda como:

```text
units/unit_01/output/unidad_01_[nombre_corto]_v02_diagram_fix.pptx
```

## Fase 5 — Verificación del PowerPoint reparado

1. abre nuevamente el archivo guardado;
2. renderiza todas las slides;
3. crea una vista mosaico posterior;
4. compara antes y después;
5. revisa especialmente las slides con diagramas;
6. confirma que no aparecieron:
   - cambios de layout accidentales;
   - imágenes deformadas;
   - pérdida de notas;
   - cambios de fuentes;
   - alteraciones de z-order;
   - enlaces rotos;
   - objetos fuera de la slide;
7. ejecuta `deck-review` sobre el archivo final;
8. corrige cualquier problema crítico o mayor y vuelve a renderizar.

## Entregables

Crear:

- presentación reparada `v02_diagram_fix.pptx`;
- previews corregidas;
- vista mosaico anterior y posterior;
- `units/unit_01/diagram_repair_inventory.md`;
- `units/unit_01/diagram_repair_report.md`;
- `units/unit_01/diagram_repair_change_log.md`.

En el informe final, listar por slide:

- asset anterior;
- problema;
- corrección;
- tamaño de fuente final;
- validaciones realizadas;
- estado;
- cualquier limitación pendiente.

No declares la tarea terminada mientras exista texto fuera de cajas, flechas sobre texto, etiquetas sobre líneas o fuentes por debajo de los mínimos definidos.
