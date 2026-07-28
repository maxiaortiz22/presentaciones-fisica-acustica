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
- solapamientos;
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
4. verificar slides afectadas;
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
