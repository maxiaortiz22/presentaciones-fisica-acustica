---
name: asset-curation
description: Busca, selecciona, evalúa y registra imágenes, fotografías, ilustraciones, videos, animaciones, GIFs y otros recursos externos para las presentaciones de Física Acústica. Usar después del storyboard o para reemplazar un visual deficiente; priorizar recursos reales y técnicos y evitar imágenes generadas por IA salvo necesidad justificada.
---

# Asset Curation

## Objetivo

Conseguir recursos visuales y multimedia que mejoren la comprensión de un concepto concreto. La tarea no consiste en decorar diapositivas.

## Entradas

Leer:

- storyboard;
- guía de estilo;
- brief;
- asset manifest existente;
- texto de la slide, si ya existe;
- requisitos de formato;
- contexto pedagógico.

## Criterio de selección

Un asset es válido si:

- muestra un objeto, instrumento o anatomía;
- demuestra un fenómeno;
- compara condiciones;
- aporta evidencia;
- visualiza una escala;
- muestra una aplicación clínica o técnica;
- hace observable un proceso temporal;
- evita una explicación verbal innecesariamente compleja.

Descartar recursos atractivos pero irrelevantes.

## Orden de preferencia

1. figura o gráfico propio;
2. imagen técnica de fuente confiable;
3. fotografía real;
4. ilustración educativa;
5. animación, video o GIF;
6. imagen generada por IA, solo con justificación.

## Fuentes preferidas

Priorizar:

- universidades;
- organismos públicos;
- asociaciones científicas;
- publicaciones académicas;
- documentación técnica;
- fabricantes de instrumentos cuando se muestre su equipo;
- museos o colecciones con licencia clara;
- repositorios educativos;
- Wikimedia Commons cuando la atribución sea verificable.

No asumir que “está en Google” significa que puede reutilizarse sin registro.

## Estrategia de búsqueda

Buscar por concepto visual, no solo por nombre de unidad.

Usar términos en español e inglés cuando mejore los resultados.

## Evaluación por asset

Calificar:

- relevancia pedagógica;
- exactitud;
- legibilidad;
- resolución;
- compatibilidad con 16:9;
- posibilidad de recorte;
- presencia de etiquetas;
- idioma;
- licencia;
- confiabilidad de la fuente;
- adecuación al estilo.

## Video y GIF

Para cada recurso temporal especificar:

- duración total;
- fragmento recomendado;
- propósito;
- momento de reproducción;
- necesidad de audio;
- alternativa estática;
- comportamiento sin conexión;
- enlace original.

No depender exclusivamente de streaming durante la clase.

## Imágenes generadas por IA

Solo proponerlas cuando:

- no exista una imagen adecuada;
- el fenómeno no pueda fotografiarse;
- se necesite una escena sintética específica;
- una ilustración simplificada sea superior.

Toda propuesta debe indicar:

- por qué es necesaria;
- qué aspectos deben ser físicamente correctos;
- qué riesgo de error tiene;
- cómo verificarla.

## Manifiesto

Crear o actualizar `asset_manifest.csv`.

Columnas mínimas:

```text
asset_id,unit,slide_id,type,title,description,pedagogical_purpose,source_url,creator,organization,license,access_date,local_path,status,credit_text,notes
```

Estados:

- `proposed`;
- `shortlisted`;
- `downloaded`;
- `approved`;
- `rejected`;
- `replaced`.

## Manejo de archivos

- usar nombres definidos en `AGENTS.md`;
- conservar resolución original;
- no estirar imágenes;
- preservar transparencia si es útil;
- registrar modificaciones;
- crear versiones recortadas sin borrar el original;
- evitar archivos extremadamente pesados sin necesidad.

## Salidas

- manifest actualizado;
- carpeta de assets organizada;
- shortlist por slide;
- informe de assets faltantes;
- texto de crédito;
- alternativas.

## No hacer

- no usar imágenes con marcas de agua;
- no asumir que una imagen encontrada puede reutilizarse sin registro;
- no proponer fotos genéricas de personas con auriculares para cualquier tema;
- no llenar todas las slides con fotografías;
- no presentar como científica una ilustración artística.
