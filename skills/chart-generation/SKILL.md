---
name: chart-generation
description: Diseña y genera con código gráficos, curvas, señales, espectros, diagramas cuantitativos y figuras reproducibles para las presentaciones de Física Acústica. Usar cuando un concepto requiere una visualización propia, datos controlados o una figura editable y verificable; no usar para buscar fotografías o videos.
---

# Chart Generation

## Objetivo

Crear figuras didácticas técnicamente correctas, reproducibles y legibles en PowerPoint.

## Casos de uso

Aplicar a:

- funciones matemáticas;
- seno, coseno y tangente;
- exponenciales y logaritmos;
- movimiento armónico;
- tono puro;
- frecuencia, período, amplitud y fase;
- longitud de onda;
- presión y nivel;
- escala logarítmica;
- ley del cuadrado inverso;
- suma energética;
- espectros;
- Fourier;
- filtros;
- bandas de octava y tercio de octava;
- ponderación A;
- curvas isofónicas;
- enmascaramiento;
- respuestas en frecuencia;
- propagación;
- tipos de ruido.

## Entradas

- objetivo pedagógico;
- variables;
- unidades;
- rango;
- valores o modelo;
- estilo visual;
- tamaño;
- fuente de datos;
- formato de salida.

No completar datos faltantes con valores inventados.

## Diseño previo

Especificar:

- pregunta que responde el gráfico;
- mensaje central;
- tipo;
- escala;
- anotaciones;
- datos;
- comparaciones;
- riesgos de interpretación.

## Herramientas

Preferir:

- Python;
- NumPy;
- SciPy;
- Matplotlib;
- pandas;
- SVG;
- PNG;
- CSV o JSON.

## Reglas visuales

- fondo compatible con la plantilla;
- tipografía legible;
- ejes con nombre y unidad;
- ticks significativos;
- grilla tenue solo si ayuda;
- leyenda breve;
- anotaciones directas;
- colores consistentes;
- patrones o etiquetas cuando no baste el color;
- márgenes seguros.

No duplicar títulos si PowerPoint ya tendrá uno.

## Exactitud

Comprobar:

- unidades;
- escalas;
- frecuencias;
- relaciones;
- consistencia dimensional;
- normalización;
- referencia logarítmica;
- signo;
- rango;
- muestreo;
- resolución;
- aliasing;
- conversión entre amplitud, potencia y decibeles.

Cuando una figura sea conceptual y no esté a escala, declararlo.

## Animaciones

Cuando ayuden:

- crear GIF o MP4 corto;
- ofrecer figura estática;
- usar velocidad observable;
- evitar loops distractores;
- registrar parámetros.

## Archivos

Conservar por figura:

```text
script.py
data.csv
figure.svg
figure.png
README.md
```

El script debe ejecutarse nuevamente sin edición manual.

## Verificación

- el script termina;
- los archivos existen;
- no hay textos cortados;
- la resolución es suficiente;
- el mensaje se entiende;
- los datos coinciden con la fuente;
- el gráfico insertado es legible.

## Salidas

- script;
- datos;
- SVG o PNG;
- descripción pedagógica;
- caption;
- texto alternativo;
- parámetros;
- fuente de datos.

## No hacer

- no fabricar datos experimentales;
- no usar ejes sin unidades;
- no ocultar normalizaciones;
- no suavizar sin indicarlo;
- no usar 3D decorativo;
- no exportar baja resolución;
- no incluir demasiadas curvas.
