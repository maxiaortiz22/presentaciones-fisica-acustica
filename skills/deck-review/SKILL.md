---
name: deck-review
description: Revisa una presentación PowerPoint de Física Acústica en contenido, pedagogía, diseño, editabilidad, fuentes y calidad técnica, incluyendo el render visual de todas las diapositivas. Usar sobre borradores y antes de declarar una unidad finalizada; no usar como sustituto del storyboard inicial.
---

# Deck Review

## Objetivo

Detectar y corregir:

- sobrecarga;
- desbordes;
- mala jerarquía;
- saltos pedagógicos;
- errores técnicos;
- inconsistencias;
- imágenes deficientes;
- falta de fuentes;
- apariencia genérica.

## Entradas

- `.pptx`;
- storyboard;
- slide text;
- notas;
- programa;
- capítulo fuente;
- guía de estilo;
- asset manifest;
- presentaciones previas;
- feedback docente.

## Revisión en cinco capas

### 1. Cobertura

Comparar deck con programa y storyboard.

Clasificar temas como:

- completo;
- parcial;
- ausente;
- ampliado;
- complementario.

### 2. Exactitud técnica

Verificar:

- definiciones;
- fórmulas;
- variables;
- unidades;
- gráficos;
- escalas;
- ejemplos;
- anatomía;
- terminología;
- relaciones causales;
- datos normativos o clínicos.

### 3. Pedagogía

Preguntar:

- qué debe entenderse;
- si están los conocimientos previos;
- si la secuencia construye significado;
- si se explica el visual;
- si el ejemplo ayuda;
- si hay demasiados conceptos;
- si existen recapitulaciones;
- si la aplicación es auténtica;
- si el ejercicio puede resolverse con lo explicado.

### 4. Revisión visual renderizada

Renderizar todas las slides y comprobar:

- texto cortado;
- texto reducido automáticamente por debajo del mínimo;
- solapamientos;
- texto que sale de cajas;
- conectores que cruzan texto;
- puntas de flecha que cubren palabras o caracteres;
- etiquetas de flecha apoyadas sobre líneas;
- flechas que llegan al nodo incorrecto;
- objetos fuera;
- tamaño;
- contraste;
- alineación;
- deformación;
- pixelado;
- ejes;
- captions;
- consistencia;
- espacios accidentales;
- monotonía;
- ruido visual.


### 4A. Auditoría geométrica de diagramas

Para cada visual con cajas, flechas, callouts o ecuaciones anotadas:

- identificar bounding boxes de nodos, textos, etiquetas y conectores;
- comprobar que no haya intersecciones no intencionales;
- confirmar que el conector esté anclado al borde correcto;
- confirmar que la etiqueta tenga un corredor independiente;
- comprobar padding interior;
- verificar que el texto principal sea de 22 pt o más y preferentemente 24 pt;
- verificar que las etiquetas sean de 20 pt o más;
- verificar que las ecuaciones centrales sean de 28 pt o más;
- confirmar que el diagrama fue diseñado al tamaño real de inserción;
- comparar el render a pantalla completa y en vista mosaico.

Todo desborde, conector sobre texto o reducción tipográfica por debajo del mínimo es al menos un problema `major`. Si altera el significado o impide leer, es `critical`.

### 5. Producción

Comprobar:

- formato 16:9;
- master;
- layouts;
- fuentes;
- editabilidad;
- enlaces;
- videos;
- notas;
- capas;
- tamaño de archivo;
- assets;
- créditos;
- texto alternativo;
- numeración.

## Severidad

- `critical`;
- `major`;
- `minor`;
- `suggestion`.

## Informe

Crear `review.md` con:

```text
review_id,slide_id,category,severity,finding,evidence,recommended_fix,status,owner
```

Agregar resumen, cobertura, fortalezas, bloqueos y cambios prioritarios.

## Corrección

1. corregir críticos;
2. renderizar;
3. corregir mayores;
4. volver a renderizar cada slide con diagramas modificados;
5. verificar slides afectadas;
5. revisar consistencia;
6. cerrar hallazgos;
7. registrar decisiones no aplicadas.

## Prueba de naturalidad

Buscar:

- slides idénticas;
- tarjetas repetidas;
- exceso de iconos;
- frases grandilocuentes;
- imágenes irrelevantes;
- títulos vacíos;
- simetría rígida;
- texto demasiado genérico.

## Aprobación

Una unidad puede aprobarse cuando:

- no hay críticos;
- los mayores están resueltos o aceptados;
- la cobertura es completa;
- todas las slides renderizan;
- el deck es legible;
- el manifest está actualizado;
- el archivo conserva editabilidad.

## No hacer

- no limitarse a ortografía;
- no declarar “se ve bien” sin render;
- no cambiar ciencia por layout;
- no borrar ejemplos sin evaluar impacto;
- no revisar solo slides iniciales;
- no reemplazar toda la plantilla por una corrección localizada.
