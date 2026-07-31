# Unidad 3 — Informe de validación de diagramas

## Resultado global

**Aprobado.** Se generaron 25 familias y 62 variantes. Todas fueron renderizadas individualmente a 2400 × 1100 px y nuevamente dentro de una slide 16:9 a 2400 × 1350 px.

Clasificaciones aplicadas antes de generar:

- diagrama conceptual;
- diagrama de proceso;
- ecuación anotada;
- esquema mixto.

## Gates de aceptación

| gate | criterio | resultado |
|---|---|---|
| Texto | cero desbordes y cero clipping | pass |
| Tipografía principal | 22 pt mínimo | pass |
| Etiquetas de conectores | 20 pt mínimo | pass |
| Ecuaciones | 28 pt mínimo | pass |
| Padding | 0,18 in nominal o superior | pass |
| Conectores | ninguna línea ni punta sobre texto | pass |
| Etiquetas | separadas del conector | pass |
| Destino | flechas terminan en el objeto correcto | pass |
| Canvas | ningún objeto fuera del área útil | pass |
| Contexto | legible dentro de una slide completa | pass |
| Editabilidad | SVG y `source.json` por variante | pass |
| Problemas abiertos | cero críticos y cero mayores | pass |

## Iteraciones

### Iteración 1

Se produjeron todas las variantes y seis hojas de contacto. El control automático detectó una falla mayor en U03-DG017-S049: la cuadrícula `ξ(x,t)` usaba 19 pt.

La inspección visual detectó además:

| recurso | hallazgo | severidad |
|---|---|---|
| U03-DG012-S037 | etiquetas de conectores demasiado próximas a cajas | mayor |
| U03-DG014 | “modifica presión” ocupaba un corredor demasiado corto | mayor |
| U03-DG022-S076 | fuente secundaria y zona de reducción competían espacialmente | mayor |
| U03-DG024-S095 | flechas verticales quedaban casi ocultas entre pasos | mayor |
| U03-DG025-S087 | ecuación textual demasiado larga para una línea | mayor |
| U03-DG021-S071 | faltaban flechas explícitas de contribución a la suma | menor |

### Iteración 2

Correcciones:

- U03-DG017-S049: cuadrícula ampliada y texto a 22 pt.
- U03-DG012-S037: escalera vertical, corredores libres y etiquetas laterales.
- U03-DG014: etiqueta dividida en dos líneas sin reducir fuente.
- U03-DG022-S076: nodos acortados y zona espacial separada.
- U03-DG024-S095: pasos más bajos y separaciones mayores.
- U03-DG025-S087: relación dividida en dos líneas a tamaño de ecuación.
- U03-DG021-S071: dos flechas breves por columna, sin cruces.

Se volvieron a generar los 62 renders individuales y los 62 contextos 16:9. Los controles automáticos quedaron sin fallas y la segunda inspección visual aprobó las correcciones.

## Editabilidad y límite de alcance

Los diagramas se entregan como SVG editable y `source.json` con IDs, cajas, texto, tamaños y conectores. No se creó un deck ni archivos PowerPoint de montaje porque la consigna indica no construir todavía la presentación. La traducción a formas nativas de PowerPoint se realizará en la fase de montaje usando esta geometría validada.

Registro máquina: `assets/generated/_review/u03_diagrams_generation_report.json`, los `validation.json` individuales y `u03_final_assets_audit.json`.
