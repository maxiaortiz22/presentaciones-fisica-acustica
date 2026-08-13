# Registro de cambios — Unidad 10: Ruidos

## Versiones conservadas

| Versión | Archivo | Estado | Observación |
|---|---|---|---|
| v01 | `output/unidad_10_ruidos_v01.pptx` | Conservada | Primera producción completa; base de la revisión integral. |
| v02 | `output/unidad_10_ruidos_v02.pptx` | Conservada | Versión corregida tras cerrar todos los problemas críticos y mayores. |
| final | `output/unidad_10_ruidos_final.pptx` | Entregable final | Copia binaria verificada de v02; no sobrescribe versiones anteriores. |

## Cambios incorporados en v02

La revisión de v01 produjo diez grupos de correcciones mayores:

1. Redistribución de etiquetas diagramáticas que el generador recortaba al superar dos líneas.
2. Restitución de la condición temporal `T` en el esquema de nivel equivalente.
3. Corrección de la igualdad de integración del ruido rosa para mantener `K·ln 2` legible y sin separación ambigua.
4. Replanteo de U10-078 para que el diagrama se leyera dentro de la composición final.
5. Corrección de rótulos y advertencias superpuestos al gráfico de U10-078.
6. Reconstrucción de las tablas U10-042, U10-068, U10-085 y U10-090 con tipografía apta para aula.
7. Ampliación del texto principal y mejora de jerarquía en U10-074.
8. Aumento de tipografía y reorganización de las doce afirmaciones de U10-082.
9. Síntesis de resultados y traslado del procedimiento extendido a notas en U10-089.
10. Reagrupación de la bibliografía de U10-093 con mayor legibilidad.

Además:

- el generador de diagramas pasó a fallar el preflight si una etiqueta no entra;
- se volvieron a generar y revisar los diagramas afectados;
- se renderizaron nuevamente las 93 slides;
- se produjo un PDF de revisión de 93 páginas;
- se ejecutaron validación estructural, prueba de overflow e inspección visual completa;
- `review.md`, `production_log.md`, `diagram_validation_report.md` y `asset_manifest.csv` quedaron actualizados.

## Revisión de consistencia

La comparación con el mapa del curso, el template, las guías y las Unidades 1–9 produjo `consistency_report.md`.

Se conservaron como diferencias pedagógicas intencionales:

- la mayor presencia de diagramas de clasificación y decisión;
- las recapitulaciones de encuentro;
- la integración reiterada de fuente, señal, contexto, receptor y control;
- la separación entre ruta central, complementaria, respaldo y fuente bloqueada.

Se actualizaron las convenciones globales para `S_pp(f)`, `p_{B,\mathrm{rms}}`, `L_max,F`, `L_peak`, `L_N,T`, ruido de fondo, señal enmascarante y protección auditiva. Las decisiones quedaron registradas como D-080 a D-083.

## Cierre final

En esta etapa se crearon:

- `output/unidad_10_ruidos_final.pptx`;
- `final_report.md`;
- `change_log.md`.

No se modificó el contenido de las slides durante el cierre. La versión final se copió desde v02 únicamente después de comprobar:

- 93 slides y 93 notas;
- 2 masters y 27 layouts;
- 93 renders y PDF de 93 páginas;
- 0 placeholders vacíos;
- 0 slides aplanadas;
- 0 problemas críticos;
- 0 problemas mayores;
- ausencia de overflow;
- integridad del paquete PPTX;
- 93 bloques `[Sources]`;
- numeración completa;
- 0 hipervínculos externos y 0 medios embebidos susceptibles de rotura.

La identidad binaria quedó confirmada:

```text
v02 SHA-256  = 74D0E838F7D8930E4C3BC98D87441E517EF76BAA671DDBC088182C1D116AD88D
final SHA-256 = 74D0E838F7D8930E4C3BC98D87441E517EF76BAA671DDBC088182C1D116AD88D
```

## Pendientes aceptados

- Variar algunas retículas de cajas en una futura revisión global.
- Evaluar captions y créditos 1–2 pt mayores si deben leerse desde el fondo del aula.
- Refinar subíndices tipográficos y formato decimal de algunos gráficos.
- Depurar consignas genéricas en notas del orador.
- Incorporar audio comparativo solo con archivo, licencia y nivel de reproducción aprobados.
- Completar contenido normativo o clínico condicionado únicamente con fuente institucional vigente.
- Resolver de forma transversal OMML/texto/SVG, color de títulos y tablas nativas frente a formas editables.

Ninguno de estos pendientes es crítico o mayor para la versión final actual.
