# Registro de producción — Unidad 02

## Resultado

- Presentación: `output/unidad_02_mecanica_termodinamica_v01.pptx`
- PDF de revisión: `output/unidad_02_mecanica_termodinamica_preview.pdf`
- Vista mosaico: `output/contact_sheet.png`
- Cantidad final: 110 slides.
- Formato: 16:9, 12192000 × 6858000 EMU.
- Estado: aprobado para revisión docente; sin problemas críticos ni mayores abiertos.

## Base utilizada

- Template aprobado: `output/fisica_acustica_template_v01.pptx`.
- Storyboard, `slide_text.md`, `speaker_notes.md`, `asset_manifest.csv`, planes de gráficos y diagramas, informe de validación de diagramas y sistema visual de la Unidad 02.
- Se duplicaron las slides demostrativas correspondientes del template. Se conservan 2 masters, 27 layouts, regla superior, paleta, pie institucional, logo y numeración.
- Se utilizaron 25 de las 27 slides/layouts demostrativos como marcos de producción.
- El contenido demostrativo local del template se eliminó de forma explícita; no se construyeron slides en blanco ni se aplanó ninguna slide completa.

## Construcción y editabilidad

- Títulos, subtítulos, texto visible, tablas, ecuaciones breves, paneles y formas de apoyo permanecen editables.
- Los gráficos y diagramas validados se insertaron como SVG independientes.
- Se conservaron las notas del orador en las 110 slides.
- Las 110 slides conservan el placeholder de numeración.
- Las 78 imágenes insertadas tienen texto alternativo en sus propiedades no visuales.
- Se verificaron dos vínculos externos funcionales en las relaciones del PPTX: PhET y Wikimedia Commons.

## Assets insertados

| Tipo | Instancias | Criterio |
|---|---:|---|
| Diagramas validados | 69 | SVG final aprobado |
| Gráficos cuantitativos | 7 | 4 gráficos únicos reutilizados en los contextos previstos |
| Alternativa estática | 1 | Reutilización del diagrama validado de U02-078 en U02-077 |
| Imagen externa | 1 | Corte transversal de membrana timpánica, dominio público |

Los cuatro diagramas aprobados de U02-036, U02-038, U02-040 y U02-103 no se insertaron porque esas slides usan la versión cuantitativa aprobada del gráfico correspondiente. No se insertó ninguna versión preliminar.

## Multimedia

- U02-002, U02-034, U02-069 y U02-077 no tenían un archivo audiovisual local aprobado para incrustar.
- Se conservaron alternativas estáticas explícitas.
- U02-034 incluye un vínculo funcional a la simulación PhET prevista.
- La ausencia del archivo multimedia y la acción docente esperada quedaron registradas en las notas.

## Desviaciones respecto del storyboard

- No se agregaron, quitaron ni dividieron slides: se mantienen las 110 previstas.
- No hubo cambios pedagógicos de secuencia.
- Ajustes de producción:
  - títulos largos: 40 pt y mayor reserva vertical;
  - listas introductorias de 4–5 pasos: franja ampliada, sin reducir fuente;
  - ecuaciones largas ya incluidas dentro de un asset: se eliminó su duplicación secundaria en la cabecera;
  - medios sin archivo local: alternativa estática y nota de trazabilidad.

## Correcciones durante el ciclo render–revisión

1. Slide 43: se detectó una ecuación secundaria recortada. Se eliminó la duplicación; el diagrama validado permaneció intacto.
2. Slides 45, 48 y 54: títulos de dos líneas invadían el primer renglón. Se corrigió la regla global de encabezados largos.
3. Slides 92, 96, 107 y 108: listas de pasos requerían más altura. Se redistribuyó el layout sin reducir fuente.
4. Cada corrección se volvió a renderizar y revisar a 1600 × 900 px.

## Revisión de diagramas dentro de la slide

- Se revisaron individualmente las 69 inserciones de diagramas y la alternativa estática.
- No se observaron flechas sobre texto, puntas sobre símbolos, etiquetas apoyadas sobre líneas, cajas desbordadas ni recortes.
- Los assets se insertaron con `fit: contain`, sin deformación ni crop.
- La ampliación de franjas introductorias mantuvo corredores y legibilidad del recurso principal.
- Las declaraciones “no está a escala” permanecen visibles cuando corresponden.

## Controles automáticos

| Control | Resultado |
|---|---|
| Reimportación del PPTX | 110/110 slides |
| Render completo | 110 PNG, todos 1600 × 900 |
| Detección de overflow fuera del lienzo | Aprobado |
| Slides en blanco o de varianza anómala | Ninguna |
| Notas | 110/110, no vacías |
| Masters/layouts | 2/27 presentes |
| Numeración | 110/110 placeholders |
| Assets declarados | 78/78 existentes |
| Texto alternativo | 78/78 imágenes |
| PDF de revisión | 110 páginas, 16:9 |

El verificador genérico de fidelidad del template emitió 11 alertas no aplicables:

- una alerta por el helper de extracción usado solo para inspección de lectura del template; no modificó el PPTX;
- diez alertas de “máscara opaca” sobre paneles legítimos de preguntas, recapitulaciones, definiciones y medios. El contenido demostrativo señalado había sido eliminado antes de insertar el contenido aprobado.

Estas alertas se resolvieron por inspección de geometría, render individual y revisión de masters/layouts. No representan defectos del deck final.

## PDF y mosaico

- El PDF de revisión se generó a partir de los 110 renders finales verificados, porque la automatización COM de PowerPoint no estuvo disponible de forma estable en la sesión.
- El PDF se reabrió con Poppler: 110 páginas, 959,976 × 540 pt, sin cifrado.
- `contact_sheet.png` corresponde a la última versión renderizada del PPTX.

## Reemplazos respecto de una versión anterior

- No existe una versión anterior de la presentación de la Unidad 02: esta es la versión inicial `v01`.
- Durante la producción se sobrescribió únicamente el archivo de trabajo `v01` antes de su entrega.
- Los paths de assets finales no cambiaron y no hubo reemplazos de assets respecto de otro deck.
