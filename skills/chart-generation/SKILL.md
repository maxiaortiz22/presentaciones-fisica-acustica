---
name: chart-generation
description: Diseña y genera con código gráficos cuantitativos, curvas, señales, espectros y figuras reproducibles para las presentaciones de Física Acústica. Usar para visualizaciones con ejes, escalas o datos; derivar diagramas de cajas, flechas, procesos y callouts a la skill diagram-generation.
---

# Chart Generation

## Objetivo

Crear gráficos cuantitativos técnicamente correctos, reproducibles y legibles en PowerPoint.

Los diagramas de cajas, conectores, procesos o ecuaciones anotadas no pertenecen a esta skill: usar `diagram-generation`.

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

Diseñar cada gráfico en el tamaño físico final que tendrá en la slide, no en un canvas arbitrario que luego será reducido.

Tamaños recomendados al insertarlo en 16:9:

- anotaciones clave: 22 pt o más;
- etiquetas de ejes: 20 pt o más;
- ticks y leyendas: 18 pt como mínimo;
- ecuaciones o resultados destacados: 28 pt o más.

Además:

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

El script correcto no implica una figura aprobada. Aplicar el siguiente ciclo:

1. generar;
2. insertar o simular la inserción al tamaño final;
3. renderizar la slide;
4. revisar;
5. corregir;
6. volver a renderizar.

Comprobar:

- el script termina;
- los archivos existen;
- no hay textos cortados;
- ningún elemento queda fuera del canvas;
- etiquetas, leyendas y anotaciones no se superponen;
- la fuente no baja del mínimo;
- la resolución es suficiente;
- el mensaje se entiende en vista de slide completa;
- los datos coinciden con la fuente;
- el gráfico insertado es legible.

Repetir hasta no encontrar problemas críticos o mayores.

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
