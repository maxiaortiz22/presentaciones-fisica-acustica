# Unidad 5 — Revisión de redacción de slides y notas

Fecha: 2026-08-03
Alcance: `slide_text.md`, `speaker_notes.md` y `source_map.md`. No se creó ni modificó un PowerPoint.

## Dictamen

**Aprobado para pasar a producción visual, con recursos normativos, vocales y multimedia todavía bloqueados.** La redacción conserva los 150 IDs, el orden, los títulos de trabajo y la clasificación central/complementaria/respaldo del storyboard aprobado.

- Problemas críticos: **0**.
- Problemas mayores: **0**.
- Problemas menores abiertos: **4**, todos dependientes de producción o fuentes externas.

## Verificación estructural

| Control | Resultado | Estado |
|---|---:|---|
| IDs en `slide_text.md` | 150, secuencia U05-001–U05-150 | conforme |
| IDs en `speaker_notes.md` | 150, secuencia U05-001–U05-150 | conforme |
| Slides centrales | 104 | conforme |
| Slides complementarias | 28 | conforme |
| Slides de respaldo | 18 | conforme |
| Campos por slide | título, subtítulo, contenido, ecuación, definición/ejemplo, caption, visual, layout, fuente y alt | conforme |
| Fuente y texto alternativo | exactamente uno por slide | conforme |
| Recursos visuales citados | 28 IDs; todos presentes en `asset_manifest.csv` | conforme |
| Contenido visible mayor a 55 palabras en una línea | 0 slides | conforme |
| Tono publicitario o frases genéricas de IA | no detectado | conforme |

## Revisión pedagógica independiente

| Criterio | Evidencia | Estado |
|---|---|---|
| Intuición antes del formalismo | suma visual antes de serie; registro antes de DFT; promedio energético antes de integral | aprobado |
| Nivel de primer año | números complejos, coeficientes, normalización y normas quedan en complemento/respaldo | aprobado |
| Símbolos y unidades | `T_0`, `f_0`, `f_s`, `N`, `T_obs`, `Δf`, `H`, bandas y descriptores se definen al introducirse | aprobado |
| Ejemplos por pasos | periodicidad, bins, ganancia, tercio de octava y `L_eq` incluyen cálculo e interpretación | aprobado |
| Aplicación fonoaudiológica | voz, audífonos, audiometría, ruido de fondo y puente al oído | aprobado |
| Preguntas resolubles | notas incluyen respuesta esperada en diagnósticos, predicciones y mini ejercicios | aprobado |
| Recapitulaciones | U05-017, 029, 040, 051, 062, 073, 083, 094, 105, 116, 124 y 129 agregan una relación nueva | aprobado |
| Errores frecuentes | FFT/intensidad, espectro/respuesta, máximo/`f_0`, bin/banda, octava/Hz, A/audición y promedio de dB | aprobado |
| Límites clínicos/perceptuales | aplicaciones de voz y audición declaran límites de inferencia | aprobado |

## Revisión específica de diagramas

- El texto de nodos se mantiene en títulos breves y cuerpos de dos o tres líneas.
- La explicación extensa se trasladó a notas del orador.
- Los conectores no requieren frases largas; las relaciones se explican mediante orden, rótulos o guía oral.
- Cada slide señala la idea central del esquema en título, subtítulo o caption.
- DG-004, DG-012 y DG-014 ya prevén recorridos en dos filas cuando la secuencia es larga.
- U05-149 y U05-150 deben dividirse durante producción si no conservan texto de 22 pt; no se autoriza reducir la fuente.

## Exactitud y cautelas

1. La ordenada de un espectro nunca se denomina “intensidad” sin definición.
2. Fourier se presenta como representación, no como mecanismo ni creador de componentes.
3. `H(f)=Y(f)/X(f)` conserva la condición `X(f)≠0` y compatibilidad de procedimiento.
4. `f_0` se obtiene de periodicidad/espaciado, no del máximo espectral.
5. Octava se define por razón; `B` no se confunde con `Δf`.
6. Ponderación A no se convierte en dB HL, sonoridad o audición individual.
7. `L_eq` se calcula en escala energética, no mediante promedio aritmético de dB.
8. Los casos hipotéticos se rotulan como didácticos y no normativos.

## Problemas abiertos

| Problema | Severidad | Tratamiento aplicado | Acción pendiente | Estado |
|---|---|---|---|---|
| Registro vocal U05-MED-003 ausente | menor | esquemas o señales sintéticas; lenguaje no diagnóstico | producir/autorizar audio y regenerar CH-004/010/012 | abierto |
| Ventanas CH-009 sin fuente/normalización cerrada | menor | comparación cualitativa sin cifras | aprobar definición y normalización reproducible | abierto |
| IEC 61260-1 e IEC 61672-1 sin verificación autorizada | menor | no se muestran tablas, curvas ni tolerancias definitivas; U05-111 queda provisional | verificar edición y actualizar CH-014/017, DG-011 y slides asociadas | abierto |
| Equipos, audios e imágenes técnicas no confirmados | menor | alternativa estática o esquema propio | curar recursos y comprobar disponibilidad antes de clase | abierto |

## Decisiones de redacción

- Se mantuvieron las 150 slides; no se agregó, eliminó ni reordenó contenido.
- Los objetivos se redactaron como acciones observables.
- Las ecuaciones centrales aparecen después de una intuición o visual previo.
- Las definiciones completas se conservan solo cuando la precisión lo exige; las recapitulaciones usan relaciones y preguntas.
- Las notas incluyen duración, guía de explicación, respuesta esperada, error frecuente, demostración o indicación multimedia cuando corresponde.
- La escritura `dB(A)` y los descriptores completos tienen prioridad, explicando que el programa utiliza `dBA`.
- El valor del ejemplo de 63 Hz se conserva porque pertenece al storyboard/libro, pero queda rotulado como provisional hasta verificar IEC 61672-1.

## Verificaciones ejecutadas

- Comparación automática de secuencia e IDs con U05-001–U05-150.
- Comparación de cantidades central/complementaria/respaldo con el storyboard.
- Comprobación de todos los campos obligatorios por slide.
- Comprobación de referencias de assets contra `asset_manifest.csv`.
- Auditoría de densidad visible y búsqueda de lenguaje promocional/genérico.
- Revisión manual de continuidad, preguntas, respuestas, ecuaciones, unidades y transiciones.

## Estado final

Los cuatro documentos de escritura quedan listos para una futura fase de producción del deck. Las decisiones abiertas están localizadas y no impiden usar la ruta central salvo en las slides que dependen de recursos normativos o multimedia explícitamente señalados.
