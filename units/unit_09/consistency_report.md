# Informe de consistencia — Unidad 9

**Unidad:** Factores que afectan la propagación del sonido
**Deck revisado:** `output/unidad_09_propagacion_sonido_final.pptx`
**Fecha de revisión:** 2026-08-12
**Skill aplicada:** `consistency-guard`
**Estado:** consistente en estructura, identidad visual, profundidad y producción; no quedan inconsistencias locales críticas o mayores.

## Alcance y baseline

Se comparó la Unidad 9 con:

- `AGENTS.md`;
- `style/presentation_style_guide.md`;
- `style/slide_master_spec.md`;
- `style/template_review.md` y `style/template_mosaic.png`;
- `output/fisica_acustica_template_v01.pptx`;
- `course_map.md`, `course_dependency_map.md` y `course_consistency_report.md`;
- `style/glossary.md`, `style/notation_guide.md` y `style/decision_log.md`;
- los PPTX finales y los informes de consistencia de U1–U8;
- el PPTX final, sus 96 notas, el PDF y el render completo de U9. Se inspeccionó el mosaico general y, a tamaño final, las slides 37, 58, 59, 86 y 90 después de corregir la notación.

La línea base vigente es el sistema de dos masters y 27 layouts del template; formato 16:9; Calibri Light/Calibri/Cambria Math; paleta bordó, magenta, carbón, gris, teal y ocre; títulos informativos; cuerpo de aula; ecuaciones acompañadas por significado, símbolos, unidades e hipótesis; bloques `[Sources]` en notas; numeración visible y preferentemente dinámica cuando el layout la renderiza; y separación física entre medición, nivel, percepción y conclusión.

## Evidencia estructural

| Evidencia | U9 final | Comparación |
|---|---:|---|
| Slides | 96 | Dentro del rango real U1–U8: 94–150. |
| Notas | 96/96 | Cobertura completa, como U1–U8. |
| Masters / layouts | 2 / 27 | Coincide con template y U1–U8. |
| Bloques `[Sources]` | 96 | Uno por slide. |
| Rutas | 75 centrales, 9 ampliaciones, 11 de respaldo y 1 con fuente restringida | Clasificación operativa y coherente con D-070. |
| Numeración local visible | 96 slides | Solución aceptada: el campo dinámico del layout no se visualiza en el render de las slides importadas. |
| Ecuaciones OMML | 0 | También 0 en template y U1–U8 actuales; la decisión de implementación sigue abierta. |
| Imágenes de contenido | 4 inspeccionadas, todas con alt text | Los restantes recursos principales son formas y textos editables. |
| Códigos internos visibles | 0 slides | Los códigos permanecen en notas y manifiesto, de acuerdo con D-066. |
| Peso del PPTX | 0,51 MB | Menor que todas las unidades previas salvo diferencias marginales; no hay señal de rasterización masiva. |

## Matriz de comparación

| Dimensión | Hallazgo | Clasificación | Acción / criterio |
|---|---|---|---|
| Terminología | “Reflexión”, “absorción”, “transmisión”, “refracción”, “difracción”, “acondicionamiento”, “aislamiento” e “insonorización” mantienen distinciones físicas compatibles con el glosario y con la puerta de entrada de U9. | aceptable | Se ampliaron en el glosario los términos propios que faltaban. |
| Terminología de recintos | La unidad distingue acondicionar, aislar e insonorizar, y presenta la cabina como sistema verificable. | intencional | Mantener: evita homogeneizar una distinción central de U9. |
| Símbolos energéticos | Las slides 35–37, 58–59, 86 y 90 muestran `Rₑ`, `α` y `τₑ`; `R` se reserva para el índice de reducción sonora. | aceptable | La representación tipográfica mantiene la distinción canónica `R_E`/`τ_E` y coincide con D-077. |
| Otros símbolos | `Q_dir`, `DI`, `A_eq`, `T_60`, `m_s`, `c`, `λ`, `f`, `V` y `ΔR` mantienen significado y contexto. | aceptable | La guía de notación fue ampliada para U9. |
| Unidades | Se usan m, m·s⁻¹, Hz, Pa, m², m³, kg·m⁻², s, dB SPL, dB(A), dB y m² sabin con separador decimal español. | aceptable | Conservar; no se detectaron unidades dimensionalmente incompatibles. |
| Definiciones | Divergencia no se confunde con absorción; absorción no equivale a aislamiento; reflexión no equivale a reverberación; cabina no equivale a caja con espuma. | aceptable | Coincide con el mapa de dependencias y sus errores a diagnosticar. |
| Nivel de profundidad | La unidad estima y reconoce mecanismos, pero evita diseño profesional, tablas normativas inventadas y formalización modal sin fuente primaria. | intencional | Coincide con el alcance del mapa del curso. No profundizar por uniformidad con U4–U5. |
| Tratamiento de fórmulas | Las secuencias distancia, directividad, balance, Sabine, transmisión e incremento por ley de masas presentan significado, unidades, ejemplo o límite. | aceptable | Mantener el patrón mecanismo → modelo → estimación → límite. |
| Implementación de ecuaciones | U9, como U1–U8 y el template actual, usa texto editable en lugar de OMML. La guía escrita reserva OMML para ecuaciones estructuradas. | requiere decisión | Resolver globalmente el umbral OMML/texto matemático/SVG; no corregir solo U9. |
| Estilo de gráficos | Curvas con fondo claro, ejes rotulados, unidades, teal/bordó/ocre y advertencias cuando son conceptuales; las imágenes gráficas inspeccionadas tienen alt text. | aceptable | Coherente con U4, U5, U7 y U8. |
| Estilo de diagramas | U9 usa más mapas de trayecto, balances y rutas laterales que U7–U8, con formas editables y semántica cromática estable. | intencional | Diferencia pedagógica registrada en D-078; no convertirla en layout obligatorio del curso. |
| Estilo de ejemplos | Predomina dato → relación → cálculo/estimación → interpretación condicionada, igual que en U4 y las secuencias cuantitativas de U7–U8. | aceptable | Mantener. |
| Recapitulaciones | Hay cierres por encuentro, actividades breves, recapitulación final y respaldo separado. La frecuencia es menor que en U5–U7, pero la carga conceptual también está más agrupada. | aceptable | No agregar recapitulaciones solo para igualar conteos. |
| Aplicaciones | Exterior, fachada, consultorio, sala, cabina y audiometría sustituyen las matrices perceptuales/clínicas de U7–U8. | intencional | La diferencia sigue el puente U8 → U9 → U10 y no debe homogeneizarse. |
| Notas del orador | Hay 96 notas y 96 bloques de fuentes; se retiraron 84 campos sin acción y las tres consignas genéricas recurrentes. | aceptable | D-076 aplicado en la versión final. |
| Pies | Logo, nombre de carrera, línea inferior y posición visual coinciden con template y unidades anteriores. | aceptable | Conservar furniture. |
| Créditos | Los captions visibles son funcionales y no muestran identificadores técnicos; la trazabilidad permanece en notas y manifiesto. | aceptable | D-056/D-066 aplicadas. |
| Numeración | Los 96 números locales se ven correctos y son editables. El placeholder dinámico existe, pero no se visualiza en el render de las slides importadas. | aceptable | Mantener hasta una futura migración de template que haga funcionar el campo dinámico en todos los layouts. |
| Layouts | Mantiene la familia de portadas bordó, contenido claro, pregunta, ecuación, gráfico, proceso, comparación, recapitulación y respaldo. | aceptable | Coincide con 2 masters/27 layouts del template. |
| Paleta | Usa `#4D1434`, `#903163`, `#3D3D3D`, `#969FA7`, `#2F7E83`, `#9F541A` y fondos claros del sistema. | aceptable | Coherente con U7–U8 y con el template. |
| Tipografía | Calibri Light/Calibri/Cambria Math, tamaños y jerarquías coinciden con el curso; el render no muestra una excepción tipográfica propia de U9. | aceptable | Conservar. |
| Color de títulos | El deck usa bordó, como la práctica consolidada de varias unidades, mientras la guía escrita aún indica carbón. | requiere decisión | Resolver globalmente; no recolorear solo U9. |
| Mapa del curso | El alcance, los prerrequisitos y la conexión con U8/U10 coinciden, pero la línea de notación de U9 aún lista `Q`, `A`, `τ` y `TL`. | requiere decisión | Actualizar mediante `course-architecture` a `Q_dir`, `A_eq`, `τ_E` y `R`, o documentar equivalencias de fuente. No se modificó el mapa en esta tarea. |
| Norma de cabina | U9 bloquea correctamente un “máximo permitido” universal, pero todavía no existe norma/edición institucional adoptada. | requiere decisión | Mantener el respaldo no habilitado hasta contar con norma, vía, transductor, bandas, menor nivel de prueba y jurisdicción. |

## Diferencias intencionales que se conservan

1. **Mayor densidad de diagramas de mecanismo y trayecto.** U9 necesita separar causas físicas que pueden coexistir; U7 y U8, en cambio, necesitan matrices perceptuales y clínicas.
2. **Más estimaciones y menos tablas clínicas.** La unidad prepara decisiones de medición y control, no diagnósticos ni protocolos audiológicos completos.
3. **Tres encuentros más integración y respaldo.** La extensión de 96 slides es suficiente para el alcance y no debe crecer hasta el tamaño de U5 por uniformidad.
4. **Uso de casos de ambiente, sala y cabina.** Es el puente curricular apropiado entre los estudios de U8 y el ruido de U10.
5. **Bloqueo explícito de datos normativos incompletos.** La ausencia de una tabla no es un faltante pedagógico cuando evita inventar valores o jurisdicciones.

## Inconsistencias localizadas

### CG-U09-01 — Colisión de `R` y `τ`

- **Clasificación:** inconsistente.
- **Slides revisadas:** 35–37, 58–59, 86 y 90.
- **Problema:** alternancia entre `R_E`/`τ_E`, subíndices `e` minúsculos y símbolos sin subíndice; `R` también designa el índice en dB.
- **Corrección recomendada:** usar `R_E`, `α`, `τ_E` en el balance y `R` solo para reducción sonora. Actualizar la tabla de la slide 86.
- **Estado:** **resuelto en la versión final**. Se usa `Rₑ`, `α` y `τₑ` como representación tipográfica de `R_E`, `α` y `τ_E`; `R` queda reservado para el índice en dB. La decisión canónica permanece registrada como D-077.

### CG-U09-02 — Códigos internos en captions

- **Clasificación:** inconsistente.
- **Slides:** 51 de 96; entre ellas 2, 5, 7, 9–11, 13–15, 17–21, 23–24, 26, 28–29, 31–33, 35–36, 40, 42–43, 45–46, 48–49, 53, 56, 58, 60–62, 64, 67, 69, 71–72, 74–75, 77, 79–82, 85 y 91.
- **Problema:** `U09-DG/CH-…` es información de producción, no un crédito legible para el aula.
- **Corrección recomendada:** dejar caption funcional; conservar código, autoría y fuente en notas/manifiesto.
- **Estado:** **resuelto en la versión final**. Se retiraron 51 códigos visibles; los identificadores y la trazabilidad permanecen en notas y manifiesto.

### CG-U09-03 — Numeración local visible

- **Clasificación:** aceptable por compatibilidad de producción.
- **Slides:** 1–96.
- **Diferencia:** existe un objeto local `slide-number` en todas las slides y también un placeholder dinámico en los layouts.
- **Decisión:** se probó la eliminación del objeto local, pero el placeholder del layout no se visualizó en el render de las slides importadas. Se conservó el número local, editable y consistente, para asegurar numeración efectiva en el aula.
- **Estado:** **aceptado** para la versión final. No produce duplicación visual. Una migración futura del template podrá sustituirlo cuando el campo dinámico funcione en todos los layouts.

### CG-U09-04 — Notas con campos vacíos y preguntas genéricas

- **Clasificación:** inconsistente.
- **Problema:** 84 apariciones de “Demostración o revelado: No corresponde” y alta repetición de consignas intercambiables.
- **Corrección recomendada:** omitir campos sin acción y escribir solo revelados, preguntas, transiciones o demostraciones específicas.
- **Estado:** **resuelto en la versión final**. Se eliminaron 84 campos sin acción y se reemplazaron las tres consignas genéricas recurrentes; las 96 slides conservan notas.

## Decisiones requeridas

1. **Ecuaciones:** fijar el criterio global de uso de OMML frente a texto matemático editable y SVG/PNG.
2. **Color de títulos:** resolver carbón escrito frente a bordó consolidado en renders.
3. **Mapa de notación de U9:** armonizar `Q`, `A`, `τ`, `TL` con la guía canónica mediante `course-architecture`.
4. **Cabina audiométrica:** adoptar norma, edición y alcance institucional antes de publicar máximos permitidos.

## Documentación actualizada

- `style/glossary.md`: se añadieron divergencia geométrica, absorción atmosférica, área de absorción equivalente, índice de reducción sonora, masa superficial, ley de masas, transmisión lateral/flanqueo y cabina audiométrica.
- `style/notation_guide.md`: se normalizó `τ_E`, se explicitó `R=10 log₁₀(1/τ_E)` y se añadieron `m_s`, `ΔR` y la aproximación con `v_viento`/`c_ef`.
- `style/decision_log.md`: se añadieron D-077 a D-079.

## Cierre

U9 es consistente con el resto del curso en alcance, profundidad, secuencia, paleta, tipografía, layouts, estilo de gráficos, tratamiento pedagógico de fórmulas y puente curricular. Las diferencias de ritmo y de proporción de diagramas son intencionales y se conservan. En la versión final quedaron resueltas CG-U09-01, CG-U09-02 y CG-U09-04; CG-U09-03 se acepta como solución de compatibilidad verificada en render. Las decisiones globales sobre OMML, color canónico de títulos y fuente normativa institucional continúan fuera del alcance de una corrección localizada y no bloquean la unidad.
