# Registro de producción — Unidad 7

**Deck:** `unidad_07_psicoacustica_v01.pptx`  
**Fecha de producción:** 11 de agosto de 2026  
**Estado:** producido y verificado; sin problemas críticos o mayores detectados en el render final.

## Alcance

- Se construyeron 134 diapositivas en formato 16:9 a partir del storyboard y la redacción aprobados.
- Se importó el `template-starter.pptx` derivado del template aprobado y se conservaron sus dos Slide Masters y sus 27 layouts.
- Se mantuvo la secuencia U07-001–U07-134. No fue necesario dividir diapositivas ni modificar el storyboard.
- Los títulos, cuerpos, ecuaciones, cajas, numeración y captions son objetos editables. Los gráficos se insertaron como SVG y los diagramas como PNG validados de 2560 × 1440 px dentro de slides editables.
- Se incorporaron 134 páginas de notas del orador. El texto alternativo de cada recurso visual insertado también quedó registrado en las notas.

## Recursos insertados

- 73 inserciones visuales en total, correspondientes a 48 assets propios únicos.
- 9 gráficos cuantitativos únicos (`U07-CH-*`), insertados desde sus SVG aprobados.
- 39 diagramas únicos (`U07-DG-*`), insertados desde sus PNG maestros validados.
- Solo se utilizaron registros con estado `approved` en `asset_manifest.csv` y ruta local resoluble.
- No se insertaron los recursos bloqueados `U07-CH-004`, `U07-CH-010`, `U07-DG-010` ni `U07-DG-020C`; se conservaron las alternativas conceptuales o estáticas previstas en la redacción.
- Las propuestas de audio, video o GIF siguen identificadas en las notas del orador, pero no se incrustaron archivos sin autorización o fuente cerrada. Las slides correspondientes incluyen alternativa estática.

## Reemplazos y trazabilidad

- No existe una versión anterior del deck de Unidad 7 contra la cual registrar reemplazos: este archivo es `v01`.
- Durante la producción se descartó una prueba de reconstrucción nativa de diagramas porque el exportador omitía algunos conectores. Antes del render final se reemplazaron esas pruebas por los 39 PNG maestros validados `u07_dg_*_master.png`.
- El archivo final contiene únicamente las versiones corregidas y validadas; no quedaron diagramas preliminares ni duplicados ocultos.
- La posición final de cada diagrama respeta el área de contenido del layout: `left=0`, `top=100`, `width=1280`, `height=520`; título, rail superior, caption, crédito, numeración y notas permanecen editables.

## Desviaciones respecto del storyboard

- **Cantidad, orden e idea central:** sin desviaciones.
- **Editabilidad de diagramas:** los diagramas se insertaron como imágenes de alta resolución en vez de formas editables, porque la reconstrucción nativa no preservó todos los conectores. Esta decisión prioriza la versión aprobada y la legibilidad del diagrama.
- **Recursos externos preseleccionados:** no se incorporaron fotografías externas no aprobadas; se utilizaron recursos propios aprobados o alternativas textuales/estáticas.
- **Multimedia:** no se incrustó audio, video ni GIF. La consigna y la alternativa estática permanecen visibles y la activación opcional está indicada en notas.
- **Enlaces:** no hay hipervínculos externos en el deck final, por lo que no existen enlaces rotos que validar.

## Verificación automática

- Render completo: 134/134 slides a 1600 × 900 px.
- Vista mosaico: generada en `output/contact_sheet.png`.
- PDF de revisión: 134 páginas, 16:9, renderizado nuevamente con Poppler; 134/134 páginas producidas.
- `slides_test.py`: aprobado; no detectó desbordes.
- Inspección estructural: 134 slides, 134 notas, 73 imágenes y 73 imágenes con texto alternativo; 0 placeholders sin resolver.
- Estructura del template: 2 masters y 27 layouts presentes en el archivo final.
- El control heurístico `check_template_fidelity.mjs` marcó alertas de superposición al comparar el contenido final con las diapositivas demostrativas del starter. Se revisaron visualmente esas alertas en el render y corresponden al reemplazo intencional del contenido de demostración, no a máscaras sobre texto residual. El deck sí fue importado con `PresentationFile.importPptx` y exportado con `PresentationFile.exportPptx`.

## Revisión contextual de diagramas

- Se revisó cada slide con diagrama en el render final y se hizo inspección ampliada de las slides 3, 28, 99, 117 y 133.
- No se observaron flechas sobre texto, puntas sobre palabras o ecuaciones, etiquetas apoyadas en conectores, clipping, desborde de cajas ni reducción tipográfica ilegible.
- Los captions declaran que las figuras conceptuales no están a escala; la slide 133 explicita además el límite del modelo rectilíneo sin difracción.
- No se detectaron errores críticos ni mayores en los diagramas insertados en contexto.

## Entregables y huellas

| Archivo | Tamaño | SHA-256 |
|---|---:|---|
| `output/unidad_07_psicoacustica_v01.pptx` | 6 966 535 bytes | `9C3AEE19933E7E9A04A6B59074C0425E47E12779C258A6B22F67B991AAD2BA11` |
| `output/unidad_07_psicoacustica_preview.pdf` | 11 080 868 bytes | `BA7A88E022C7ABF4A5565E38296A55BCF3DCCCC76856B15B261B2B1F1842D676` |
| `output/contact_sheet.png` | 3 372 742 bytes | `7902F519BCD8654C0421289DE94A8277A83146C0EA58C4C243C81DA1E09A7C01` |

## Pendientes no bloqueantes

- Realizar la revisión pedagógica independiente prevista por `AGENTS.md` para las unidades 4–7.
- Si se autorizan fuentes externas o archivos de reproducción, incorporar la multimedia y volver a ejecutar el ciclo completo de render y revisión.

## Corrección integral v02 — 11 de agosto de 2026

Esta sección reemplaza el dictamen visual de v01. La revisión integral posterior detectó y corrigió problemas críticos y mayores que no habían quedado registrados en la primera producción.

- Archivo: `output/unidad_07_psicoacustica_v02.pptx`.
- Se revisaron 134/134 slides del PowerPoint y sus renders.
- Se retiró texto editorial visible, se corrigieron las etiquetas temporales del enmascaramiento y la representación de recorridos directo/reflejado.
- Se completó la cobertura conceptual y metodológica de curvas isofónicas normalizadas con referencia a ISO 226:2023, sin reproducir datos normativos.
- Se corrigieron desbordes de ecuaciones, repeticiones indebidas de assets, divisores duplicados y paneles de multimedia.
- Se agregó texto alternativo real a 49/49 imágenes mediante `scripts/u07_add_alt_text.ps1`.
- Render final: `output/rendered_v02/`, 134/134 slides a 1600 × 900 px.
- Contact sheet: `output/contact_sheet_v02.png`.
- `slides_test.py`: aprobado después del posprocesado final.
- Archivo final: 4.874.097 bytes; SHA-256 `57D9BCAED246165368B679D6152E08CFCC02AB982D33FBFB2B93A15CB6B1C7F0`.
- Matriz completa de hallazgos y pendientes: `review.md`.
