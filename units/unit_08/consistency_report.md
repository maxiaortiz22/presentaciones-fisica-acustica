# Informe de consistencia — Unidad 8

**Unidad:** Enfermedades y estudios auditivos; técnicas de rehabilitación

**Versión revisada:** `output/unidad_08_salud_auditiva_v02.pptx`

**Fecha:** 2026-08-12

**Skill aplicada:** `consistency-guard`

## Dictamen

La Unidad 8 es **coherente en contenido, profundidad, arquitectura pedagógica e identidad visual** con el curso. Las diferencias más visibles —mayor presencia de matrices comparativas, límites de inferencia y aplicaciones clínicas distribuidas— son **intencionales**: responden al riesgo de convertir un resultado aislado en diagnóstico y no deben homogeneizarse con unidades de física más formal.

La revisión detectó cuatro inconsistencias de producción/editoriales que conviene corregir en una futura revisión localizada del deck: subíndices visibles escritos con guion bajo, numeración manual, códigos internos en captions y notas excesivamente formularias. No se encontró una divergencia conceptual que requiera rehacer la presentación.

También quedan decisiones globales abiertas: siglas institucionales, color definitivo de títulos, criterio OMML y actualización del mapa del curso. Ninguna debe resolverse modificando solo U8.

## Baseline comparado

- `AGENTS.md`.
- `course_map.md` y `course_dependency_map.md`.
- `style/presentation_style_guide.md`, `style/slide_master_spec.md`, `style/layout_catalog.md` y `style/template_review.md`.
- `style/glossary.md`, `style/notation_guide.md` y `style/decision_log.md`.
- `course_consistency_report.md`.
- Presentaciones finales y reportes de consistencia de las Unidades 1–7.
- PowerPoint U8 v02, sus 114 slides renderizadas y la plancha de contacto completa.

## Evidencia estructural

| Indicador | U8 v02 | Baseline del curso | Evaluación |
|---|---:|---|---|
| Relación de aspecto | 16:9 | 16:9 | Coincide. |
| Slides | 114 | U1–U7: 94, 110, 96, 125, 150, 117 y 134 | Profundidad alta, pero dentro del rango real del curso. |
| Notas | 114/114 | Notas completas en unidades finalizadas | Cobertura completa; calidad editorial mejorable. |
| Masters / layouts disponibles | 2 / 27 | 2 / 27 en U1–U7 | Coincide con el template. |
| Layouts usados | 23 | 21–25 en unidades comparables | Variedad suficiente y controlada. |
| Tipografías | Calibri Light, Calibri, Cambria Math | Familia canónica | Coincide. |
| Paleta dominante | carbón, bordó, teal, ocre, gris y blanco cálido | Paleta canónica | Coincide. No hereda la excepción cromática histórica de U5. |
| Imágenes de contenido | 5, todas con alt text | Alt text exigido | Cumple. |
| Fuentes en notas | 114 bloques `[Sources]` | Trazabilidad por slide | Cumple. |
| Tamaño del PPTX | 0,63 MB | Preferencia por archivo liviano y editable | Adecuado. |

## Matriz de diferencias

| Dimensión | Evidencia en U8 | Comparación con el curso | Clasificación | Acción |
|---|---|---|---|---|
| Cobertura del mapa | Incluye TTS, alteraciones, tinnitus, presbiacusia, riesgo, pruebas y dispositivos. | Cubre el alcance obligatorio y conecta U4–U7 con U10. | aceptable | Sin cambio en U8. |
| Estado del mapa del curso | Slides 20–24 desarrollan recuperación pos-exposición y 35/112 incorporan riesgo porcentual con contexto NIOSH. | `course_map.md` todavía declara ambos componentes parciales o ausentes. | requiere decisión | Actualizar el mapa mediante `course-architecture`; no se modificó desde esta skill. |
| Nivel de profundidad | 114 slides, cuatro encuentros y respaldo final. | Se ubica entre U6/U7 y por debajo de U5; el mapa asigna alta carga clínica y comparativa. | intencional | Conservar rutas y material de respaldo. |
| Secuencia | dato → condiciones → respuesta → límite; luego batería e intervención. | Continúa estímulo/sistema/respuesta de U5–U7 y prepara exposición/ruido de U10. | aceptable | Sin cambio. |
| Terminología clínica central | “desplazamiento temporal del umbral”, “audiometría tonal”, “logoaudiometría”, “timpanometría”, “OEA”, “PEAT”, “ECoG”. | Coincide con programa, libro y uso estabilizado en U6–U7. | aceptable | Se incorporaron definiciones faltantes al glosario. |
| Tinnitus / acúfeno | La primera definición usa “tinnitus o acúfeno”; luego predomina tinnitus y aparece acufenometría. | El glosario admite equivalencia, pero la preferencia institucional sigue abierta. | requiere decisión | Mantener equivalencia explícita hasta decisión docente. |
| HIR / PAIR / NIHL | U8 usa principalmente `PAIR/NIHL` y advierte en notas que la sigla española no está fijada. | El mapa usa PAIR/NIHL; la guía previa decía HIR/NIHL. | requiere decisión | El glosario y la guía ahora registran las tres formas sin imponer una. |
| PEAT / PEATC / ABR | U8 adopta PEAT y desarrolla su significado. | La sigla institucional sigue pendiente desde unidades previas. | requiere decisión | No homogeneizar hasta validación de cátedra. |
| Inmitancia / admitancia | Slide 67 distingue categoría y magnitud `Y`. | Precisa una ambigüedad que las unidades anteriores no necesitaban resolver. | aceptable | Distinción incorporada al glosario, notación y D-074. |
| Definiciones | Cada prueba separa qué estimula, qué registra, qué magnitud entrega y qué no concluye. | Es más explícito que U1–U7 por necesidad clínica. | intencional | Conservar el énfasis en límites de inferencia. |
| Escalas y unidades | Se distinguen dB SPL, dB HL, dB SL, dB(A), Hz, daPa, µV y ms. | Mantiene referencias separadas como exige U4/U7 y la guía de notación. | aceptable | Sin cambio conceptual. |
| Símbolos visibles | En slides 4, 20–21, 26–27, 51–52, 63, 67, 87, 96 y 108–109 aparecen formas como `L_Aeq,T`, `ΔL_T`, `G_AO`, `L_SL`, `Y/Y_max` o `L_salida`. | La regla global exige subíndices tipográficos en el material visible. | inconsistente | Sustituir guiones bajos por subíndices reales en una revisión localizada del PPTX y de su generador. |
| Familia notacional de U8 | `ΔL_T`, `G_AO`, `L_SL`, `Y`, `ΔV(t)` y `G(f)` se usan con condiciones y límites. | Amplía de forma compatible la notación de niveles, sistemas y potenciales de U4–U7. | aceptable | Convenciones añadidas a la guía y D-073. |
| Tratamiento de fórmulas | Fórmula → símbolos/unidades → ejemplo → interpretación → límite. | Coincide con el patrón de U2–U7 y con el nivel de primer año. | aceptable | Conservar. |
| OMML | Las ecuaciones son texto editable en Cambria Math, no objetos OMML. | El curso aún no fijó el umbral entre OMML y texto matemático editable. | requiere decisión | Resolver globalmente; no convertir solo U8. |
| Estilo de gráficos | Fondo claro, ejes legibles, gris para grilla y bordó/teal para series; se declaran esquemas conceptuales. | Coincide con la guía y con U4–U7. | aceptable | Sin cambio. |
| Cantidad de gráficos | U8 usa pocos gráficos y más matrices/diagramas. | La comparación de estudios y dispositivos exige estructura, no curvas en cada slide. | intencional | No aumentar gráficos por uniformidad estética. |
| Estilo de diagramas | Formas nativas, cajas claras, conectores detrás, 22–24 pt y colores semánticos acotados. | Coincide con el sistema de diagramas y evita copiar el código cromático especial de U7. | aceptable | Sin cambio. |
| Matrices comparativas | Repite criterios de estímulo, sistema, sensor/tarea, respuesta, magnitud y límite. | Mayor recurrencia que en U1–U7, justificada por la batería audiológica. | intencional | Registrado como D-072; no convertirlo en obligación global. |
| Estilo de ejemplos | Datos → operación → resultado con unidad → conclusión permitida/no permitida. | Continúa el patrón didáctico de U2–U7. | aceptable | Sin cambio. |
| Recapitulaciones | Hay cierres parciales después de bloques densos y recapitulación integradora. | Frecuencia proporcional a la carga, sin copiar mecánicamente U5/U7. | intencional | Conservar. |
| Aplicaciones | La aplicación fonoaudiológica está integrada en casi toda la unidad. | En unidades físicas aparece como panel específico; aquí es el contenido nuclear. | intencional | No agregar paneles clínicos redundantes. |
| Notas del orador | 114/114 notas, con alt text y fuentes; 111 repiten “No corresponde reproducción multimedia”, 57 “No corresponde guía” y 53 “Revelar y explicar”. | La estructura está completa, pero la repetición es más mecánica que el estándar de notas específicas consolidado en U7. | inconsistente | Podar campos vacíos y redactar consignas específicas; D-076. |
| Pies | Identidad UCASAL discreta y ubicación estable. | Coincide con template y unidades finalizadas. | aceptable | Sin cambio. |
| Créditos | Fuentes externas y cuantitativas están trazadas en notas y manifiesto. | Coincide con el estándar de trazabilidad. | aceptable | Conservar. |
| Códigos visibles de assets | Se detectan 7 captions con “Producción propia UCASAL · U08-CH-…”. | D-066 reserva códigos internos para notas, storyboard y manifiesto. | inconsistente | Dejar un caption funcional; mover el ID solo a metadatos y notas. |
| Numeración | Las 114 slides muestran el número correcto mediante un textbox `slide-number`. | D-065 exige numeración automática inferior; la numeración manual es frágil ante inserciones o reordenamiento. | inconsistente | Vincular al placeholder automático del layout en la próxima edición. |
| Layouts y master | 23 layouts usados sobre 27; 2 masters; distribución variada. | Se mantiene dentro del rango observado en U1–U7. | aceptable | Sin cambio. |
| Paleta | Carbón, bordó, teal, ocre y grises sobre blanco cálido. | Coincide con la identidad canónica; U5 permanece como excepción documentada. | aceptable | Sin cambio. |
| Tipografía | Calibri Light para títulos, Calibri para texto y Cambria Math para fórmulas. | Coincide con guía, template y unidades finalizadas. | aceptable | Sin cambio. |
| Color de títulos | Predomina bordó en títulos de contenido. | La guía escrita indica carbón, pero varias unidades finalizadas consolidaron bordó. | requiere decisión | Resolver globalmente; no corregir U8 de manera aislada. |
| Naturalidad visible | Títulos informativos, preguntas concretas y ausencia de portadas publicitarias o iconos decorativos. | Mejora la naturalidad respecto de patrones genéricos sin romper identidad. | aceptable | Sin cambio. |
| Editabilidad y peso | Texto, formas y diagramas son editables; no hay slides completas aplanadas; 0,63 MB. | Cumple la política de producción del curso. | aceptable | Sin cambio. |

## Diferencias que se preservan por razón pedagógica

1. **Más comparación y más límites de inferencia.** U8 no se reduce al patrón de “definición + fórmula” de las primeras unidades porque debe entrenar lectura de evidencia clínica sin diagnóstico automático.
2. **Aplicación clínica distribuida.** No se agregan tarjetas de “aplicación” como componente separado: estudios, alteraciones y rehabilitación ya constituyen la aplicación profesional.
3. **Menor proporción de gráficos.** La unidad necesita matrices de pruebas, cadenas de medición y decisiones; forzar curvas adicionales aumentaría decoración y carga cognitiva.
4. **Banco de respaldo.** Las slides 103–114 amplían práctica y fuentes sin inflar la ruta central; la diferencia es operativa y está rotulada.

## Cambios realizados en documentos globales

- `style/glossary.md`: se añadieron términos clínicos y de evaluación propios de U8; se registraron HIR/PAIR/NIHL sin resolver la preferencia institucional; se estabilizó la distinción inmitancia/admitancia.
- `style/notation_guide.md`: se añadieron `ΔL_T(f,Δt)`, `G_AO(f)`, fórmula de dB SL, `Y`, `Y/Y_max`, potencial bioeléctrico con referencia, ECoG y ganancia electroacústica.
- `style/decision_log.md`: se registraron D-072 a D-076 sobre matrices clínicas, notación, inmitancia/admitancia, porcentajes de riesgo y naturalidad de notas.

## Problemas abiertos

| ID | Clasificación | Problema | Próxima acción |
|---|---|---|---|
| U08-CG-01 | inconsistente | Subíndices visibles escritos con guion bajo. | Corregir PPTX y generador; volver a renderizar slides afectadas. |
| U08-CG-02 | inconsistente | Códigos internos `U08-CH-*` visibles en 7 captions. | Sustituir por captions funcionales y conservar IDs en notas/manifiesto. |
| U08-CG-03 | inconsistente | Numeración manual en las 114 slides. | Usar el placeholder automático del master/layout. |
| U08-CG-04 | inconsistente | Notas con campos vacíos y consignas genéricas repetidas. | Editar por bloques prioritarios y eliminar “No corresponde” sin función. |
| U08-CG-05 | requiere decisión | El mapa del curso no refleja la cobertura nueva de recuperación y riesgo. | Revisar con `course-architecture`. |
| U08-CG-06 | requiere decisión | Siglas HIR/PAIR/NIHL y PEAT/PEATC/ABR. | Validación docente/institucional. |
| U08-CG-07 | requiere decisión | Títulos bordó frente a carbón. | Resolver para todo el template y las unidades, no solo U8. |
| U08-CG-08 | requiere decisión | Umbral entre OMML y texto matemático editable. | Definir criterio global y aplicarlo por familia de ecuaciones. |

## Cierre

La consistencia pedagógica y visual de U8 queda aprobada. El deck puede utilizarse como versión v02, pero el informe no considera cerradas las cuatro inconsistencias editoriales/de producción ni las decisiones globales pendientes. No se modificó el PowerPoint durante esta tarea porque las correcciones requieren una edición localizada y posterior renderizado, mientras que el alcance solicitado fue la comparación transversal y la actualización de referencias globales.
