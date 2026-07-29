# Informe de consistencia del curso

## Alcance

Revisión de la Unidad 1 contra:

- programa oficial;
- `course_map.md`;
- `course_dependency_map.md`;
- `content_coverage_matrix.csv`;
- `style/presentation_style_guide.md`;
- `style/notation_guide_draft.md`;
- `style/glossary_draft.md`;
- decisiones y artefactos aprobados de `units/unit_01/`.

La Unidad 1 es la primera unidad terminada. Por lo tanto, esta revisión confirma su coherencia con la arquitectura global y establece una línea de base para comparar las unidades 2–10.

## Matriz de consistencia

| dimensión | línea de base | Unidad 1 | diferencia | impacto | recomendación | estado |
|---|---|---|---|---|---|---|
| curricular | programa y matriz de cobertura | cubre nociones básicas, medición, magnitudes, matemática introductoria y vínculo con acústica | no se detectan omisiones obligatorias | ninguno | conservar trazabilidad programa–slide | consistente |
| dependencias | U1 prepara U2–U7 | introduce SI, dimensiones, funciones, trigonometría, logaritmos y dB | la profundización queda correctamente diferida | positivo | reutilizar definiciones sin redefinirlas de modo incompatible | consistente |
| terminología | glosario local | magnitud, unidad, referencia, fuente, medio, receptor, percepción y conclusión se distinguen | algunas entradas del glosario siguen en estado borrador | bajo | consolidar estas definiciones al cerrar U2 | aceptable |
| notación | guía local de notación | usa `d`, `t`, `m`, `F`, `p`, `ρ`, `f`, `S`, SI y coma decimal | no se detectan símbolos incompatibles | ninguno | mantener `S` para área y reservar cada símbolo por contexto | consistente |
| unidades | SI y referencias técnicas | espacio entre valor y unidad; símbolos no pluralizados; prefijos normalizados | 340 m/s aparece solo como redondeo didáctico declarado | bajo y controlado | conservar la distinción entre valor condicionado y redondeo | consistente |
| escalas dB | razón y referencia explícitas | diferencia dB genérico, dB SPL, dB HL y dB SL | la formalización completa se difiere a U4 y U8 | positivo | no intercambiar escalas ni omitir referencia | consistente |
| pedagogía | primer año, intuición antes del formalismo | diagnóstico, ejemplo, formalización, práctica y recapitulación | 94 slides requieren selección por ritmo | medio | mantener 72 centrales y usar 12 complementarias a demanda | aceptable |
| aplicaciones | vínculo con Fonoaudiología | voz, micrófono, audiometría, percepción y límites clínicos | no incluye demostración sonora embebida | bajo | decidir demostración en vivo según condiciones | aceptable |
| sistema visual | identidad académica del template | jerarquía, divisores, contenido, recapitulaciones y respaldo coherentes | ninguna desviación material | ninguno | reutilizar layouts y variedad controlada | consistente |
| producción | editabilidad, notas y accesibilidad | 94 notas con fuentes, 1.639 formas, 49 conectores, 16/16 imágenes con alt text, 2 masters y 27 layouts | ecuaciones editables como texto, no siempre OMML; formas no agrupadas | bajo | mantener Cambria Math y nombres estables `U01-CHxxx`; migrar selectivamente a OMML si aporta valor | aceptable |
| fuentes | jerarquía de AGENTS.md | programa, libro, mapas, BIPM y NIST trazados | no se detectan fuentes importantes sin registrar | ninguno | mantener bloque `[Sources]` en notas futuras | consistente |
| assets | preferencia por producción propia | 26 gráficos reproducibles y un GIF propio | no hay audio ni video externo | ninguno | continuar priorizando figuras propias y respaldo estático | consistente |

## Decisiones que deben conservarse

1. Separar dato físico, nivel referido, atributo perceptual y conclusión clínica.
2. Usar fuente–medio–receptor como modelo mínimo, aclarando que no agota todos los fenómenos.
3. Definir símbolos y unidades en la primera aparición y mantenerlos estables.
4. Usar `S` para área y `p` para presión; no confundir `p` con peso.
5. Expresar valores y unidades con espacio: `20 Pa`, `3,5 kg`, `343 m/s`.
6. Declarar condiciones cuando se use una velocidad de propagación y marcar 340 m/s como redondeo didáctico cuando corresponda.
7. No calcular logaritmos de magnitudes dimensionales aisladas; usar razones compatibles.
8. No usar dB SPL, dB HL y dB SL como escalas intercambiables.
9. Conservar recapitulaciones y material de respaldo como componentes distintos de la ruta central.
10. Mantener fuentes importantes en las notas y captions visibles cuando la trazabilidad lo requiera.

## Dependencias hacia unidades futuras

- **U2:** masa, fuerza, presión, densidad, dimensiones y unidades.
- **U3:** propagación, funciones, trigonometría, radianes y ciclo.
- **U4:** magnitudes sonoras, presión acústica y niveles en dB.
- **U5:** funciones, escalas, espectro y representación de señales.
- **U6–U7:** separación entre medición física y experiencia perceptual.
- **U8:** referencias audiométricas, interpretación y límites de una conclusión clínica.

## Inconsistencias y decisiones abiertas

No se detectaron inconsistencias que requieran modificar el estilo global, la notación o el glosario. Quedan decisiones de baja prioridad:

- consolidar las entradas actualmente marcadas como borrador en glosario y notación cuando exista una segunda unidad terminada para comparar;
- decidir en cada unidad si las ecuaciones críticas se mantienen como texto editable o se migran selectivamente a objetos OMML;
- conservar una prueba previa de multimedia en el equipo del aula.

## Resultado

**Consistencia aprobada.** La Unidad 1 puede usarse como línea de base académica, pedagógica, terminológica y visual para el resto del curso.

## Revalidación de cierre — 2026-07-29

Se comparó `units/unit_01/output/unidad_01_nociones_basicas_final.pptx` con el programa, los mapas de curso y dependencias, el glosario, la guía de notación y el sistema visual.

- La reparación de diagramas no alteró el alcance curricular ni la secuencia de 94 slides.
- Se conservan los diez bloques B00–B09 y los respaldos RB01–RB02.
- La notación `d`, `t`, `m`, `F`, `p`, `ρ`, `f`, `S`, SI y coma decimal sigue alineada con la guía.
- La distinción entre medición física, nivel referido, atributo perceptual y conclusión clínica permanece como norma transversal.
- El puente U1 → U2/U3/U4 conserva el sentido definido en `course_dependency_map.md`.
- Paleta, masters, layouts, pies, numeración, captions y créditos permanecen coherentes con la línea de base.
- Los assets nuevos están registrados en `asset_manifest.csv`; no se introdujeron fuentes externas nuevas.

Resultado de la revalidación: **consistente**, sin decisiones globales pendientes.
