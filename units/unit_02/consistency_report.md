# Informe de consistencia — Unidad 02

## Dictamen

La Unidad 2 pertenece claramente al mismo curso que la Unidad 1 y utiliza correctamente el template académico v01. Mantiene la identidad, la progresión pedagógica, la semántica visual y el tratamiento introductorio de las magnitudes físicas.

Las diferencias de extensión, cantidad de ecuaciones, frecuencia de recapitulaciones y densidad de diagramas son **intencionales**: responden a la carga conceptual de mecánica y termodinámica y no deben homogeneizarse con la Unidad 1.

El control deja:

- ninguna incompatibilidad curricular o terminológica grave;
- una inconsistencia menor abierta: subíndices visibles mediante guion bajo;
- cuatro cuestiones que requieren una decisión o una tarea transversal posterior;
- dos decisiones globales adoptadas: D-052 para notación mecánica y D-053 para promover glosario y guía de notación.

## Línea de base utilizada

1. `AGENTS.md`.
2. `style/presentation_style_guide.md`.
3. `style/glossary.md`.
4. `style/notation_guide.md`.
5. `style/decision_log.md`.
6. `style/layout_catalog.md`, `style/component_catalog.md` y `style/slide_master_spec.md`.
7. `output/fisica_acustica_template_v01.pptx` y su render.
8. `course_map.md` y `course_dependency_map.md`.
9. Unidad 1 final: PowerPoint, render de 94 slides, storyboard, notas, revisión y assets.
10. Unidad 2 v02: PowerPoint, render de 110 slides, storyboard, notas, revisión y assets.

## Evidencia estructural

| Control | Template v01 | Unidad 1 final | Unidad 2 v02 | Lectura |
|---|---:|---:|---:|---|
| Tamaño | 13,333 × 7,5 in | 13,333 × 7,5 in | 13,333 × 7,5 in | consistente |
| Slides | 27 | 94 | 110 | diferencia curricular, no visual |
| Masters | 2 | 2 | 2 | consistente |
| Layouts disponibles | 27 | 27 | 27 | consistente |
| Layouts utilizados | 27 | 25 | 25 | variedad equivalente |
| Notas | 27/27 | 94/94 | 110/110 | consistente |
| Bloques `[Sources]` serializados | 2 | 4 | 110 | U2 adopta trazabilidad más granular |
| Descripciones alternativas | 2 | 16 | 78 | cobertura acorde con los objetos visuales |
| Familias principales | Calibri, Calibri Light, Cambria Math | iguales | iguales | consistente |
| Recursos vectoriales/raster | muestra mixta | diagramas principalmente nativos; 8 PNG y 1 GIF | 68 SVG y 78 PNG/fallbacks | implementación diferente, apariencia coherente |

La Unidad 2 usa 25 de los 27 layouts reales, igual que la Unidad 1. Cambia su distribución: utiliza más `FA_09_ECUACION_INTERPRETACION` y `FA_23_APENDICE`, mientras que la Unidad 1 utiliza más comparación, matemática básica y gráficos de funciones. La diferencia responde al contenido.

## Matriz de diferencias

Clasificaciones:

- **intencional:** diferencia necesaria por función pedagógica o contenido;
- **aceptable:** variación que no altera el sistema;
- **inconsistente:** contradice una regla común y conviene corregir;
- **requiere decisión:** no debe resolverse localmente sin fijar una norma transversal.

| ID | Dimensión | Línea de base | Unidad 2 | Diferencia / impacto | Clasificación | Acción |
|---|---|---|---|---|---|---|
| CG-001 | Terminología | U1 usa “sistema” de manera funcional | U2 formaliza sistema, frontera y entorno antes de sumar fuerzas | Cambio de nivel necesario para Newton y balances | intencional | Se agregó `sistema físico` al glosario |
| CG-002 | Terminología | U1 distingue masa, fuerza, presión y medición | U2 distingue además calor, temperatura, energía interna y entropía | Profundización compatible con el glosario | aceptable | Sin corrección del deck |
| CG-003 | Símbolos | La guía proponía `ΣF` | U2 usa `F_neta` de manera sostenida y define la resultante | El rótulo verbal facilita la lectura inicial | intencional | D-052 admite `F_neta` después de definir `ΣF` |
| CG-004 | Símbolos | U1 puede usar símbolos breves sin muchas colisiones | U2 usa `k_s`, `Q_calor`, `W_trab`, `W_sobre`, `S_ent`, `F_el` y `F_amort` | Evita colisiones con onda, directividad, área, potencia y watt | intencional | Convención consolidada en la guía de notación |
| CG-005 | Notación visible | La guía exige subíndices tipográficos | Muchas expresiones de U2 muestran `F_neta`, `Q_calor` o `S_ent` con guion bajo | El significado es claro, pero el acabado no cumple plenamente la norma tipográfica | inconsistente | Corregir en una futura pasada global; no requiere reestructurar slides |
| CG-006 | Unidades | Forma canónica con punto centrado y exponentes | Algunos rótulos introductorios usan `N/m`, `m/s` o `N/m²` | Cociente equivalente y más familiar para primer año | aceptable | Conservar en la introducción; usar forma canónica en tablas de referencia |
| CG-007 | Mapa del curso | La fila de U2 aún enumera `k`, `S` y `W_trabajo` sin todos los calificadores | La unidad final sigue D-052 y la guía canónica | El mapa quedó menos preciso que el deck | requiere decisión | Actualizar la fila de U2 mediante `course-architecture`, no en esta revisión |
| CG-008 | Definiciones | U1 define magnitudes elementales | U2 añade fuerza neta y energía interna | Son conceptos que reaparecen en U3, U4 y U6 | intencional | Se incorporaron al glosario transversal |
| CG-009 | Profundidad | U1: 94 slides, 72 centrales | U2: 110 slides, 72 centrales | La ruta central no crece; aumentan complementarias y respaldos | intencional | Mantener las rutas separadas |
| CG-010 | Fórmulas | U1 usa 7 layouts de ecuación | U2 usa 16 | Mecánica y balances requieren más lectura algebraica | intencional | No reducir por simetría entre unidades |
| CG-011 | Fórmulas / producción | Guía: OMML para ecuaciones estructuradas; D-048 admite texto editable en ejemplos | U1 y U2 contienen 0 objetos OMML y usan Cambria Math editable | Falta fijar qué ecuaciones ameritan migración | requiere decisión | Definir un umbral transversal y probar una migración selectiva |
| CG-012 | Tratamiento de fórmulas | Ecuación + símbolos + unidades + significado | U2 mantiene esa secuencia y agrega signos/hipótesis | Misma gramática pedagógica | aceptable | Conservar |
| CG-013 | Gráficos | Bordó/teal, fondo blanco, rejilla gris, coma decimal, ejes con unidades | U2 conserva tokens y aumenta texto interno a 18–20 pt | Ajuste para lectura en el tamaño final ocupado | intencional | Conservar el tamaño mayor |
| CG-014 | Gráficos | U1 incluye funciones y espectros | U2 usa relaciones lineales fuerza–aceleración, Hooke, amortiguamiento y `c(θ)` | Cambia el objeto representado, no el estilo | aceptable | Conservar |
| CG-015 | Diagramas / producción | U1 reparó muchos diagramas como formas nativas | U2 usa principalmente SVG reproducible y fallback PNG; algunos recursos corregidos quedaron raster | La apariencia es coherente, pero la editabilidad directa no es equivalente | requiere decisión | Definir qué familias futuras deben ser nativas y cuáles pueden permanecer como SVG/PNG reproducible |
| CG-016 | Diagramas / estilo | 3–7 nodos, rectángulos planos, conectores detrás, colores semánticos | U2 mantiene esas reglas y aumenta la cantidad de diagramas | Mayor frecuencia justificada por sistemas, fuerzas y energía | intencional | No reducir por uniformidad |
| CG-017 | Ejemplos | U1 usa dato → relación → cálculo → resultado → control | U2 conserva el patrón y agrega elección de sistema, eje y signo | Extensión necesaria para evitar fórmulas-receta | intencional | Conservar |
| CG-018 | Recapitulaciones | U1 usa 4 layouts de recapitulación parcial | U2 usa 7, uno después de casi cada bloque denso | Mayor frecuencia coherente con la carga conceptual | intencional | No homogeneizar |
| CG-019 | Aplicaciones | U1 integra voz, medición y Audiología a lo largo del recorrido | U2 concentra aplicaciones auditivas en un bloque y las anticipa en ejemplos mecánicos | Ritmo distinto, pero las conexiones son específicas y limitadas | aceptable | Conservar |
| CG-020 | Notas | U1 registra desarrollo, pregunta, error, transición y duración | U2 añade guía de visual/diagrama, multimedia y `[Sources]` en cada slide | Mayor granularidad útil para una unidad con 68 diagramas/SVG | intencional | Adoptar el patrón en unidades diagramáticas futuras |
| CG-021 | Pies y fuentes | Template y U1 usan pie fijo y fuentes visibles solo cuando ayudan a leer | U2 conserva el pie y agrega fuentes breves en gráficos, diagramas y aplicaciones | Mayor trazabilidad sin invadir el contenido | aceptable | Conservar |
| CG-022 | Créditos | Manifiesto con autor, organización, licencia, acceso y crédito | U2 tiene 102 IDs únicos y no presenta créditos, creadores o licencias vacíos | Misma estructura documental | aceptable | Conservar |
| CG-023 | Metadata de assets | U1 usa tipos descriptivos en español | U2 usa valores técnicos en inglés como `mixed`, `chart` y `diagram` | No afecta al aula, pero dificulta consultas globales | requiere decisión | Definir un vocabulario controlado común antes de U3 |
| CG-024 | Numeración | U1 oculta el número de portada; el template lo muestra | U2 muestra `1` en portada y numera 110/110 | Ambas variantes están permitidas por el master bordó | aceptable | No corregir sin decisión docente |
| CG-025 | Layouts | U1 y template evitan más de tres siluetas idénticas seguidas | U2 reutiliza más ecuación/apéndice, pero alterna divisores, procesos, ejemplos y recaps | Distribución funcional, no repetición mecánica | intencional | Conservar |
| CG-026 | Paleta | Bordó institucional, carbón, gris, teal físico y ocre clínico | U2 usa la misma semántica; el ocre aparece sobre todo en transferencias/aplicaciones | Uso más restringido, no contradictorio | aceptable | Conservar |
| CG-027 | Tipografía | Calibri Light, Calibri y Cambria Math | U2 usa las mismas familias y jerarquías | La diferencia de cantidad de Cambria Math responde a las fórmulas | aceptable | Conservar |
| CG-028 | Tema interno | Template y U1 conservan tres partes de tema; U2 serializa una | Masters, layouts, fuentes y render final permanecen correctos | Diferencia interna sin efecto visible ni funcional detectado | aceptable | Vigilar en futuras exportaciones; no reconstruir |
| CG-029 | Documentación global | Solo existían `glossary_draft.md` y `notation_guide_draft.md` | Dos unidades ya validan convenciones comunes | El carácter provisional dejó de ser útil | requiere decisión | Resuelto mediante D-053 y promoción a archivos canónicos |
| CG-030 | Cierre y continuidad | U1 abre U2–U4 | U2 cierra con fuerza restauradora y abre U3 | Puente específico de la dependencia curricular | intencional | Conservar |

## Revisión específica por área solicitada

### Terminología, símbolos, unidades y definiciones

La terminología es coherente con el libro, el programa y el glosario. Las distinciones `calor ≠ temperatura`, `energía interna ≠ calor almacenado`, `fuerza ≠ presión` y `fuerza neta ≠ ausencia de fuerzas` preservan el nivel conceptual establecido por la Unidad 1.

La unidad adopta correctamente calificadores para evitar colisiones. La única desviación material es tipográfica: en el texto visible todavía aparecen guiones bajos en lugar de subíndices reales.

### Profundidad, fórmulas, ejemplos y recapitulaciones

La profundidad coincide con el mapa: modelos unidimensionales y balances cualitativos o algebraicos, sin termodinámica formal completa. El mayor número total de slides se concentra en material complementario y de respaldo; la ruta central conserva 72 slides, igual que U1.

Las fórmulas se introducen después de la intuición, definen variables y unidades, y se acompañan con ejemplos. La falta de OMML no bloquea el uso, pero requiere una norma común antes de producir unidades con ecuaciones más complejas.

### Gráficos y diagramas

Los gráficos comparten paleta, tipografía, rejilla, ejes, coma decimal y estilo de anotación con U1. El aumento del tamaño interno es una mejora deliberada para aula.

Los diagramas conservan la gramática del curso: nodos rectangulares, conectores simples, rótulos semánticos y lectura izquierda–derecha. La diferencia nativo/SVG/PNG es técnica, no estética; debe decidirse por familia y necesidad de edición, no por uniformidad.

### Aplicaciones y notas

Las aplicaciones a membrana timpánica, oído medio, vibrador óseo, tejidos y propagación en aire son específicas y explicitan los límites del modelo. No se infiere diagnóstico ni anatomía literal a partir de un esquema mecánico.

Las notas de U2 son más estructuradas que las de U1 porque cada diagrama necesita recorrido y fuente. Esta diferencia se considera una mejora intencional.

### Pies, créditos, numeración, layouts, paleta y tipografía

Se conservan la firma superior segmentada, el pie institucional, la numeración, los dos masters, los 27 layouts, la paleta y las familias tipográficas. U2 muestra el número en portada, mientras U1 lo oculta; ambas variantes son compatibles con el master bordó actual.

Los créditos visibles y el manifiesto son completos. Queda pendiente normalizar el vocabulario interno de `type` y `status` de los manifests.

## Documentación global actualizada

1. `style/glossary.md`
   - promovido a referencia canónica;
   - nuevas entradas: sistema físico, fuerza neta/resultante y energía interna.
2. `style/notation_guide.md`
   - promovida a referencia canónica;
   - `ΣF` como forma formal y `F_neta` como rótulo didáctico;
   - convenciones para `F_pres`, `F_el`, `F_amort` y trabajo sobre el sistema;
   - regla explícita para subíndices tipográficos.
3. `style/decision_log.md`
   - D-052: notación mecánica y resolución de colisiones;
   - D-053: promoción del glosario y la guía de notación.
4. `style/presentation_style_guide.md`
   - referencia actualizada hacia la guía canónica.
5. Los archivos `_draft.md` se conservan como enlaces de compatibilidad para documentos históricos.

## Problemas y decisiones abiertas

| ID | Tipo | Pendiente | Responsable sugerido |
|---|---|---|---|
| CG-A01 | inconsistente | Sustituir guiones bajos visibles por subíndices tipográficos en una futura versión del deck. | corrección localizada de U2 |
| CG-A02 | requiere decisión | Definir qué ecuaciones estructuradas deben migrarse a OMML. | sistema visual + producción |
| CG-A03 | requiere decisión | Alinear la fila de notación de U2 en `course_map.md` con D-052. | `course-architecture` |
| CG-A04 | requiere decisión | Fijar vocabulario controlado para tipos y estados de `asset_manifest.csv`. | `consistency-guard` + `asset-curation` |
| CG-A05 | requiere decisión | Establecer criterio nativo/SVG/PNG por familia de diagramas y necesidad de edición. | `diagram-generation` + producción |

Ninguno de estos pendientes modifica la validez conceptual o el uso en aula de la v02.

## Resultado

**Consistencia aprobada con pendientes menores y decisiones transversales documentadas.**

La Unidad 2 mantiene la identidad y continuidad del curso. No se recomienda reducir su cantidad de diagramas, ecuaciones o recapitulaciones para imitar la Unidad 1: esas diferencias cumplen una función pedagógica explícita.

