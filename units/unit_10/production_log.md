# Unidad 10 — Registro de producción del PowerPoint

## Actualización v02 — revisión integral

Fecha: 2026-08-12  
Salida: `output/unidad_10_ruidos_v02.pptx`

La v02 preserva el formato 16:9, los 2 masters, los 27 layouts y las 93 notas de v01. Se corrigieron todos los problemas críticos y mayores detectados por `deck-review`; el detalle completo y los problemas menores abiertos se registran en `review.md`.

Correcciones principales:

- eliminación del recorte silencioso de etiquetas en el generador de diagramas;
- restauración de unidades y condiciones perdidas, incluida `T` en U10-049;
- ecuación de la integral rosa inequívoca en U10-087;
- tablas legibles en U10-042, U10-068, U10-085 y U10-090;
- aumento de escala y reducción de carga en U10-074, U10-082, U10-089 y U10-093;
- recomposición de U10-078 con U10-CH-014 ampliado, cajas editables y un único eje vertical compartido.

Entregables v02:

- `output/unidad_10_ruidos_v02.pptx`;
- `output/unidad_10_ruidos_v02/` — 93 renders PNG;
- `output/unidad_10_ruidos_v02_preview.pdf` — 93 páginas;
- `output/unidad_10_ruidos_v02_contact_sheet.png`;
- `review.md`.

Verificación v02:

| Control | Resultado |
|---|---|
| `slides_test.py` | aprobado; sin overflow |
| Validación estructural | 93 slides, 93 notas, 0 críticos, 0 mayores |
| Diagramas en contexto | 57 slides / 57 instancias, 0 críticos, 0 mayores |
| Render y PDF | 93/93 |
| Masters / layouts | 2 / 27 preservados |
| Alt text | completo en todas las imágenes |
| Medios externos | 0 enlaces, 0 audio/video embebido |
| Peso | 1.439.017 bytes |
| SHA-256 | `74D0E838F7D8930E4C3BC98D87441E517EF76BAA671DDBC088182C1D116AD88D` |

---

Fecha de cierre: 2026-08-12  
Versión: v01  
Nombre corto: `ruidos`

## Entregables

- `output/unidad_10_ruidos_v01.pptx`
- `output/unidad_10_ruidos_preview.pdf`
- `output/contact_sheet.png`
- `output/unidad_10_ruidos_v01/` — 93 renders PNG para revisión

## Base y trazabilidad

- plantilla aprobada: `output/fisica_acustica_template_v01.pptx`;
- storyboard aprobado: 93 slides, U10-001 a U10-093;
- redacción: `slide_text.md` y `speaker_notes.md`;
- recursos: `asset_manifest.csv`, `chart_plan.md`, `diagram_plan.md` y `diagram_validation_report.md`;
- guía visual: `style/style_guide.md` y layouts FA del template;
- construcción reproducible: `scripts/u10_generate_template_plan.mjs` y `scripts/u10_build_presentation.mjs`;
- validación reproducible: `scripts/u10_validate_final_deck.py` y `scripts/u10_validate_diagram_context.py`;
- exportación del PDF: `scripts/u10_create_preview_pdf.py`.

El deck conserva formato panorámico 16:9, 2 Slide Masters y 27 layouts del template. No se modificó el sistema visual global. Los textos, las tablas construidas para esta unidad, las formas, los conectores y las ecuaciones diagramáticas permanecen editables. Los gráficos se insertaron como SVG y ninguna slide fue aplanada como imagen completa.

## Producción realizada

- 93 slides y 93 juegos de notas del orador;
- numeración y pie institucional en todas las slides;
- fuentes de contenido y texto alternativo incorporados en notas;
- texto alternativo XML en los gráficos y diagramas insertados;
- 72 recursos propios aprobados usados, sin omisiones: 57 diagramas, ecuaciones o esquemas y 15 gráficos únicos;
- 74 instancias de assets: U10-DG-038 aparece en U10-060/U10-061 y U10-CH-010 en U10-034/U10-035;
- U10-078 integra U10-DG-051 y U10-CH-014;
- U10-035 identifica U10-AS-001 y U10-AS-002 en notas y utiliza U10-CH-010 como alternativa estática; no se embebió multimedia sin archivo local aprobado;
- las tablas de U10-042, U10-068, U10-085 y U10-090 se construyeron como celdas editables;
- U10-001 incorpora U10-DG-001 sin competir con la jerarquía de portada;
- U10-083 usa U10-DG-055 como mapa final, en lugar de repetir una lista textual.

## Recursos no insertados

- U10-DG-058, U10-DG-059, U10-DG-060 y U10-CH-016: bloqueados en los planes aprobados;
- assets externos con estado `proposed` o `shortlisted`: no se insertaron como si estuvieran aprobados;
- U10-088, U10-091 y U10-092 conservan una formulación cualitativa y visible de su límite de alcance; no se fabricaron fórmulas, valores, protocolos ni límites normativos.

No se agregaron hipervínculos externos en v01: las URL del manifiesto corresponden a recursos todavía no aprobados para inserción. Por ello no hay enlaces de producción susceptibles de quedar rotos.

## Reemplazos y correcciones durante la producción

No existía una versión anterior del PowerPoint de la Unidad 10; por lo tanto, no hubo reemplazos respecto de otro deck publicado. En la iteración interna se sustituyeron explícitamente:

- la ausencia del visual de U10-035 por la alternativa estática aprobada U10-CH-010;
- tablas de texto plano por tablas de formas editables en U10-042, U10-068, U10-085 y U10-090;
- la composición incompleta de U10-082 por las doce afirmaciones del storyboard;
- la solución parcial de U10-089 por los cinco resultados previstos;
- el caption incorrecto de U10-078 por la identificación coherente de su composición;
- las omisiones de U10-DG-001 y U10-DG-055 por sus versiones aprobadas;
- el tamaño serializado de texto diagramático por una compensación que mantiene un mínimo real de 22 pt y 28 pt o más en ecuaciones centrales.

La reconstrucción final se hizo desde los assets validados; no queda ninguna versión preliminar insertada.

## Verificación posterior

| Control | Resultado |
|---|---|
| Conteo | 93 slides; 93 notas |
| Formato | 16:9; 12192000 × 6858000 EMU |
| Template | 2 masters; 27 layouts preservados |
| Renders | 93/93 PNG |
| PDF de revisión | 93/93 páginas |
| `slides_test.py` | aprobado; sin contenido fuera del canvas |
| Validación estructural final | aprobado; 0 críticos, 0 mayores |
| Diagramas en contexto | 58 usos revisados; 0 críticos, 0 mayores |
| Assets aprobados | 72/72 recursos únicos insertados |
| Recursos bloqueados | 0 insertados |
| Imágenes a slide completa | 0 |

La revisión visual se realizó sobre la vista mosaico completa, siete lotes ampliados y una segunda inspección a tamaño real de las slides más densas o corregidas. Se comprobó legibilidad, clipping, desbordes, deformación, z-order, cajas, conectores, puntas y etiquetas.

El verificador genérico de fidelidad de plantilla también se ejecutó. Sus 222 alertas no describen fallas del deck: compara el contenido demostrativo de Unidad 1 del starter con el contenido nuevo de Unidad 10 y considera la sustitución intencional de las formas de demo como “overlay”; además busca las llamadas de importación/exportación dentro de su carpeta temporal y no en el script reproducible de la unidad. La fidelidad efectiva se verificó estructuralmente mediante conservación de masters/layouts, tamaño de slide, fuente de construcción y revisión renderizada.

## Desviaciones respecto del storyboard

- No fue necesario dividir slides ni cambiar la numeración.
- U10-035 usa la alternativa estática aprobada y deja el audio como indicación de notas, porque los archivos de audio permanecen propuestos.
- U10-088, U10-091 y U10-092 no muestran contenido técnico bloqueado; explicitan el límite de interpretación sin inventar datos.

## Integridad de los entregables

| Archivo | Tamaño | SHA-256 |
|---|---:|---|
| `unidad_10_ruidos_v01.pptx` | 1.440.453 bytes | `BE6A86B119023DCFCA43F0164D85531A565F44F4ED8DA8DEF15BA9050F2D9B7A` |
| `unidad_10_ruidos_preview.pdf` | 8.129.175 bytes | `062EA6E54F31407F00450D99C39E4B6569630F80E406B21AC0A168BBB8B957A7` |
| `contact_sheet.png` | 1.811.032 bytes | `2784D19D84589BE32574278EBE360B94F3E060E7A148E32745832657289AA36E` |

## Estado final

Aprobado para revisión docente: cero problemas críticos y cero mayores. Permanecen abiertas únicamente las decisiones de contenido ya registradas para U10-DG-058, U10-DG-059, U10-DG-060, U10-CH-016 y el multimedia propuesto.
