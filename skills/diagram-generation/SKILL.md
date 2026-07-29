---
name: diagram-generation
description: Diseña, genera y valida diagramas de cajas, flechas, procesos, relaciones, comparaciones, callouts y ecuaciones anotadas para las presentaciones de Física Acústica. Usar cuando una visualización contiene nodos, conectores o etiquetas espaciales; crear formas editables de PowerPoint por defecto y repetir el render hasta eliminar desbordes y colisiones.
---

# Diagram Generation

## Objetivo

Crear diagramas académicos claros y editables cuya geometría funcione a tamaño real de proyección.

Esta skill resuelve específicamente problemas frecuentes como:

- flechas que apuntan al lugar equivocado;
- conectores que cruzan texto;
- etiquetas apoyadas sobre flechas;
- puntas de flecha que cubren caracteres;
- texto que sale de las cajas;
- reducción automática a fuentes demasiado pequeñas;
- fórmulas, callouts o anotaciones superpuestas;
- diagramas que se ven correctos aislados pero pequeños al insertarlos en la slide.

## Cuándo usarla

Usar para:

- fuente → medio → receptor;
- procesos secuenciales;
- diagramas de bloques;
- cuadros comparativos conectados;
- mapas conceptuales;
- relaciones causa–efecto;
- magnitudes anotadas;
- ecuaciones con callouts;
- anatomía simplificada con etiquetas;
- flujos de medición o diagnóstico;
- esquemas con entradas, salidas y respuestas.

No usar para curvas, espectros o gráficos cuantitativos: esos corresponden a `chart-generation`.

## Principio de implementación

Por defecto, construir con:

- formas nativas de PowerPoint;
- cuadros de texto editables;
- conectores anclados;
- grupos de objetos identificables;
- ecuaciones editables o SVG cuando la ecuación nativa no sea viable.

No generar un PNG de todo el diagrama salvo que exista una limitación técnica documentada. Si se exporta SVG o PNG, diseñarlo en el tamaño final de inserción y conservar el archivo fuente.

## Entradas

- objetivo pedagógico;
- mensaje central;
- texto exacto de cada nodo;
- relaciones entre nodos;
- tamaño y posición disponibles en la slide;
- guía visual;
- tamaño mínimo de letra;
- layout de destino;
- orden de lectura;
- necesidades de edición posterior.

## Contrato de legibilidad

En formato 16:9 y para proyección en aula:

- título de nodo: 24–28 pt;
- cuerpo de nodo: 22–24 pt;
- etiqueta de conector: 20–22 pt;
- ecuación central: 28–40 pt;
- texto auxiliar: 20 pt mínimo;
- créditos: excepción permitida según guía de estilo.

No usar autoajuste que reduzca texto por debajo de estos valores.

Si el contenido no entra:

1. simplificar el texto sin perder significado;
2. ampliar la caja;
3. redistribuir nodos;
4. pasar detalle a notas;
5. dividir el diagrama;
6. dividir la slide.

Reducir la fuente por debajo del mínimo es la última opción y requiere justificación explícita en el review.

## Reglas para cajas

- medir el texto con la fuente y tamaño finales antes de fijar ancho y alto;
- usar margen interior mínimo de 0,18 in en los cuatro lados;
- dejar entre 10 % y 20 % de espacio libre;
- no superar tres líneas de cuerpo por nodo salvo justificación;
- no mezclar título, explicación extensa y ejemplos en una caja pequeña;
- centrar verticalmente solo si mejora la lectura;
- evitar que la última línea quede a menos de 0,12 in del borde;
- no usar cajas grandes con texto diminuto para “llenar” la composición.

## Reglas para conectores y flechas

- usar conectores reales anclados a los bordes de las formas;
- definir explícitamente el lado de salida y el lado de entrada;
- no conectar centro con centro si la línea atraviesa el contenido;
- reservar un corredor de conectores antes de colocar etiquetas;
- mantener 0,10 in o más entre líneas y texto no relacionado;
- colocar la punta en el borde del nodo, nunca sobre el texto interno;
- evitar que la punta de flecha cubra la línea de contorno;
- usar conectores en codo cuando el trayecto recto produzca una colisión;
- no cruzar conectores salvo que el cruce tenga significado y se marque;
- usar una relación semántica por flecha;
- mantener consistentes grosor, punta y color.

## Etiquetas de conectores

Las etiquetas deben:

- estar en una caja de texto independiente;
- ubicarse por encima o por debajo de la línea, no sobre ella;
- tener fondo transparente o del color de la slide;
- conservar un espacio vertical visible respecto de la flecha;
- permanecer dentro del corredor reservado;
- no invadir nodos;
- no tapar puntas de flecha.

Si una relación necesita una frase larga, convertirla en un nodo o nota, no comprimirla sobre el conector.

## Callouts y ecuaciones anotadas

Para diagramas que explican símbolos o partes de una ecuación:

- situar la ecuación primero y medir su bounding box real;
- colocar callouts fuera de ese bounding box;
- usar líderes cortos y sin cruces;
- terminar el líder a 0,05–0,10 in del símbolo señalado;
- no apoyar la punta sobre un carácter;
- no cruzar el signo de igualdad, subíndices o unidades;
- evitar más de cuatro callouts simultáneos si comprometen la claridad;
- dividir en dos slides cuando sea necesario.

## Algoritmo de composición

1. Definir el canvas con el tamaño real de inserción.
2. Crear la grilla y los márgenes seguros.
3. Medir textos y ecuaciones.
4. Calcular tamaños mínimos de nodos.
5. Colocar nodos siguiendo el orden de lectura.
6. Reservar corredores para conectores.
7. Dibujar conectores anclados.
8. Colocar etiquetas en los corredores.
9. Ajustar jerarquía y espacios.
10. Agrupar objetos relacionados.
11. Asignar IDs o nombres estables.
12. Renderizar.
13. Ejecutar validaciones.
14. Corregir y volver a renderizar.

## Validaciones automáticas y visuales

Comprobar como mínimo:

### Texto

- ningún texto excede su caja;
- ningún texto se corta;
- no existe auto-shrink por debajo del mínimo;
- ninguna palabra queda aislada por un ancho deficiente;
- el texto se lee al tamaño final de la slide.

### Geometría

- no hay intersección entre conectores y cajas de texto;
- no hay intersección entre etiquetas y conectores;
- no hay objetos fuera del canvas;
- no hay superposición entre nodos;
- las puntas llegan al nodo correcto;
- las flechas respetan el orden de lectura;
- los callouts apuntan al símbolo correcto.

### Composición

- hay márgenes externos consistentes;
- el diagrama no queda excesivamente pequeño dentro de la slide;
- la densidad está equilibrada;
- las cajas relacionadas tienen tamaños coherentes;
- el color no es la única forma de distinguir categorías.

## Bucle de corrección obligatorio

Realizar:

```text
generar → renderizar → inspeccionar → registrar hallazgos → corregir → renderizar nuevamente
```

Repetir hasta cumplir todos los gates de aceptación.

Si después de cinco iteraciones queda un problema crítico o mayor:

- no aprobar el diagrama;
- registrar el bloqueo;
- proponer dividir la slide o cambiar el tipo de visual.

## Gates de aceptación

Un diagrama solo se aprueba si:

- hay cero desbordes;
- hay cero textos cortados;
- hay cero conectores sobre texto;
- hay cero etiquetas sobre líneas;
- todas las flechas llegan al destino correcto;
- todos los textos respetan el tamaño mínimo;
- se renderizó dentro de la slide real;
- el visual sigue siendo legible en una vista de slide completa;
- los objetos son editables o la excepción está documentada.

## Salidas

- diagrama editable o archivo fuente;
- SVG o PNG de respaldo;
- preview renderizado;
- lista de objetos y IDs;
- texto alternativo;
- caption;
- informe de validación;
- registro de iteraciones.

## No hacer

- no usar flechas dibujadas a mano sin anclaje;
- no colocar etiquetas directamente sobre líneas;
- no reducir todo el diagrama para que “entre”;
- no confiar solo en que el código no produjo errores;
- no aprobar sin render;
- no usar una captura como solución si puede ser editable;
- no colocar contenido largo dentro de nodos pequeños;
- no ignorar superposiciones leves: en proyección se vuelven más visibles.
