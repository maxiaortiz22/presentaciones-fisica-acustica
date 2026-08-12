# Informe final — Unidad 7

**Unidad:** Características subjetivas de la percepción auditiva y psicoacústica  
**Versión final:** `output/unidad_07_psicoacustica_final.pptx`  
**Fecha de cierre:** 11 de agosto de 2026  
**Estado:** terminada; 0 problemas críticos y 0 problemas mayores bloqueantes.

## Verificación de la definición de terminado

| Entregable o control | Estado | Evidencia |
|---|---|---|
| `brief.md` | completo | Objetivos, alcance, prerrequisitos, dificultades y ruta de cuatro encuentros. |
| `storyboard.md` | completo | 134 slides con bloques, objetivos, layouts, fuentes y transición. |
| `slide_text.md` | completo y sincronizado | 134/134 IDs; versión final; terminología y consigna isofónica corregidas. |
| `speaker_notes.md` | completo y sincronizado | 134/134 notas; rutas de audio reales y alternativas visuales para medios ausentes. |
| `asset_manifest.csv` | completo | Fuentes, licencias, rutas, estados y créditos; dos medios aprobados añadidos. |
| Scripts | presentes | Generación de gráficos, diagramas, multimedia, deck, alt text, PDF y validación. |
| Gráficos | presentes y organizados | 9 familias aprobadas con scripts, datos, SVG/PNG, README y validación. |
| Diagramas | presentes y organizados | 41 familias aprobadas más fuentes editables; cinco diagramas finales reconstruidos como formas nativas. |
| PowerPoint | final | `output/unidad_07_psicoacustica_final.pptx`; no reemplaza v01 ni v02. |
| PDF de revisión | final | `output/unidad_07_psicoacustica_final_review.pdf`, 134 páginas. |
| Render | final | `output/rendered_final/`, 134 PNG. |
| `review.md` | actualizado | Cierre integral, incidencias y limitaciones aceptadas. |
| Revisión pedagógica independiente | actualizada | IP07-01 a IP07-05 cerrados; resto aceptado o recomendado. |
| Revisión de consistencia | actualizada | Sin inconsistencias bloqueantes; dos decisiones globales preservadas. |

## Resumen cuantitativo

- **Cantidad de slides:** 134.
- **Ruta central:** 103 slides.
- **Slides complementarias:** 18, rotuladas `AMPLIACIÓN`.
- **Respaldo:** 13, rotuladas `A DEMANDA`.
- **Encuentros:** 4.
- **Bloques pedagógicos:** 12 (`B00` a `B11`).
- **Duración estimada de la ruta central:** 294–315 minutos en total, aproximadamente 74–79 minutos por encuentro.
- **Duración con todas las ampliaciones:** 353–382 minutos.
- **Duración máxima incluyendo respaldo:** 387–423 minutos; no se recomienda proyectar esta ruta completa de modo lineal.

## Bloques

| Bloque | Slides | Contenido principal |
|---|---:|---|
| B00 | 1–7 | Apertura, puente U6–U7, marco estímulo–tarea–respuesta y mapa de la unidad. |
| B01 | 8–19 | Umbral absoluto, criterio, función psicométrica, sensibilidad y campo audible. |
| B02 | 20–31 | Campo libre, CAE, tímpano, transferencia y curvas isofónicas. |
| B03 | 32–43 | Altura tonal, sonoridad, timbre y duración percibida. |
| B04 | 44–53 | Nivel de sonoridad, fones, sones y conversión acotada. |
| B05 | 54–65 | Enmascaramiento simultáneo, elevación de umbral, filtros auditivos y ERB. |
| B06 | 66–75 | Enmascaramiento temporal, energético e informacional. |
| B07 | 76–87 | Habla, SNR, reverberación, inteligibilidad y ALCons. |
| B08 | 88–97 | Reflexiones, retardo, efecto de precedencia y Haas. |
| B09 | 98–109 | Localización, audición binaural, ITD, ILD, pistas espectrales y movimiento. |
| B10 | 110–121 | Fuentes concurrentes, efecto *cocktail party*, aplicaciones y cierre. |
| B11 | 122–134 | Respaldo: glosario, fórmulas, ejercicios, índices y referencias. |

## Temas cubiertos

- psicoacústica como relación entre estímulo, tarea, condiciones y respuesta;
- umbral absoluto, detección probabilística, sensibilidad frecuencial y campo audible;
- campo libre, conducto auditivo externo, nivel próximo al tímpano y `G_CT`;
- construcción y lectura conceptual de curvas de igual sonoridad;
- altura tonal, sonoridad, timbre, duración percibida, resolución e integración temporal;
- nivel de sonoridad en fones y sonoridad en sones;
- enmascaramiento simultáneo y temporal, elevación del umbral, filtros auditivos y ERB;
- enmascaramiento energético e informacional;
- SNR, ruido, reverberación, inteligibilidad y pérdida de articulación de consonantes;
- reflexiones, retardo, efecto de precedencia y efecto Haas;
- audición binaural, localización, ITD, ILD, cono de confusión, pistas espectrales y dinámicas;
- fuentes concurrentes, segregación, liberación espacial y efecto *cocktail party*;
- aplicaciones fonoaudiológicas sin adelantar diagnóstico o protocolos de la Unidad 8.

## Recursos multimedia

1. `U07-MEDIA-001` — `assets/generated/media/u07_media_001_tonos_250_1000hz.wav`: dos tonos sintéticos de 250 Hz y 1 kHz, igual RMS digital nominal, PCM mono 48 kHz. Uso: distinguir nivel nominal y respuesta perceptual. No es una medición calibrada.
2. `U07-MEDIA-006` — `assets/generated/media/u07_media_006_directo_copia_retardada.wav`: complejo armónico sintético con copia a −6 dB y retardos de 5, 20 y 50 ms. Uso: comparar coloración, fusión y separación sin fijar un umbral universal.

Ambos recursos son supraliminales, no clínicos, reproducibles mediante `scripts/u07_generate_media.py` y poseen alternativa estática. Los otros seis medios planificados permanecen `proposed`; no hay instrucciones docentes que dependan de ellos.

## Gráficos propios

Nueve familias aprobadas y trazables:

- curva psicométrica;
- umbral condicionado;
- campo audible conceptual;
- transferencia campo–tímpano;
- fundamental ausente;
- relación fones–sones;
- patrón de enmascaramiento;
- filtro y ERB por igualdad de área;
- decaimiento y `T_60`.

Cada familia conserva script, datos o parámetros, SVG/PNG, README y validación. Los gráficos conceptuales están rotulados para impedir lectura cuantitativa indebida.

## Diagramas propios

- El manifiesto conserva 41 familias aprobadas y una relación de alias, con maestros `.pptx`, SVG/PNG y validaciones.
- Las slides 74, 85, 103, 107 y 117 fueron reconstruidas dentro del deck con formas y conectores nativos para corregir dirección causal y geometría.
- Los diagramas heredados que se insertan como PNG mantienen su fuente editable y su alt text; esta deuda de editabilidad queda aceptada y documentada.

## Slides complementarias

Las 18 ampliaciones son: 15, 16, 17, 26, 36, 40, 42, 61, 62, 63, 64, 71, 74, 92, 105, 108, 115 y 116. Están intercaladas donde aportan contexto, pero se distinguen visualmente de la ruta central. El docente puede omitirlas sin romper la secuencia conceptual.

## Fuentes principales

1. Programa oficial de Física Acústica de UCASAL.
2. Capítulo 7 del libro del curso en LaTeX.
3. Capítulo 7 del libro del curso en PDF, pp. 177–204.
4. ISO 226:2023 para alcance y condiciones de curvas normales de igual sonoridad; no se reproducen datos tabulados.
5. Bibliografía académica y normas citadas por el capítulo para psicoacústica, precedencia, filtros auditivos, STI/SII y terminología.
6. Guía de estilo, glosario, notación, mapa del curso, template y decisiones registradas del repositorio.

Cada slide contiene un único bloque `[Sources]` en sus notas. Los assets externos shortlisted conservan autor, organización, licencia, URL y fecha de acceso en el manifiesto aunque no se hayan incorporado al deck.

## Decisiones pedagógicas

- Se conserva una unidad extensa porque el programa y el capítulo requieren cuatro encuentros y una progresión gradual para primer año.
- La intuición y la escena de escucha preceden al formalismo; las fórmulas se acompañan con unidades, interpretación y límites.
- La actividad isofónica usa un trazado cualitativo resoluble. No se simula acceso a valores normativos no autorizados.
- Los ejemplos cuantitativos prioritarios muestran cuatro etapas visibles y separan resultado físico de inferencia perceptual.
- La ruta docente se hace operativa mediante `RUTA CENTRAL`, `AMPLIACIÓN` y `A DEMANDA`.
- Se mantienen recapitulaciones frecuentes por la densidad de U7, aunque no todas adoptan el mismo tipo de actividad.
- Las aplicaciones evitan diagnósticos y se formulan como preguntas de medición, tarea e inferencia válida.

## Editabilidad, navegación y estilo

- Textos, títulos, números, ejemplos nuevos y cinco diagramas corregidos son editables.
- El archivo conserva 2 masters y 27 layouts del sistema del curso.
- Las fórmulas permanecen como texto editable en Cambria Math; la adopción global de OMML sigue pendiente para todo el curso.
- Las 44 imágenes poseen texto alternativo.
- La numeración 1–134 es estable.
- No hay relaciones externas ni hipervínculos rotos.
- La paleta, tipografías, jerarquía y pies institucionales son coherentes con el template.
- No quedan avisos de producción, códigos internos o créditos `TEX/PDF` visibles.

## Limitaciones conocidas

1. No se incluye una familia cuantitativa de curvas ISO 226; requiere acceso y licencia para datos normativos.
2. Parte de los diagramas heredados se inserta como imagen validada, aunque conserva maestro editable separado.
3. Los dos WAV se entregan como archivos locales y no están incrustados en el PowerPoint; deben mantenerse junto a la carpeta de la unidad.
4. Seis medios opcionales siguen sin producirse; sus slides son autosuficientes sin ellos.
5. Algunas notas conservan fórmulas de transición repetidas y pueden naturalizarse con la voz del docente.
6. OMML y color canónico de títulos son decisiones transversales pendientes, no defectos específicos de U7.

## Recomendaciones para dictar la clase

1. Preparar cuatro sesiones y seleccionar de antemano las ampliaciones; no recorrer las 134 slides linealmente.
2. Probar los dos WAV antes de clase, usar volumen confortable y recordar que no están calibrados.
3. En la slide 30, pedir primero ejes y unidades; después comparar dos puntos; finalmente discutir condiciones y límites.
4. Resolver 24, 51, 58, 81, 91 y 105 haciendo que el grupo anticipe el signo y la unidad antes de mostrar el resultado.
5. En 74, 85, 103, 107 y 117 seguir las flechas en dirección causal y detenerse en qué dato permite —o no permite— cada inferencia.
6. Usar las recapitulaciones como recuperación activa: pedir una explicación, un límite o un contraejemplo, no solo leer las tarjetas.
7. Reservar las slides 122–134 para consulta, preguntas o evaluación formativa.

## Verificación técnica final

- PowerPoint: 134 slides, 4.271.742 bytes.
- SHA-256: `7EA7F9B51B474328AE79041593C895776738A006CAED4106FDA3E16DC97CA1D2`.
- PDF: 134 páginas.
- Render: 134 PNG.
- `slides_test.py`: aprobado, sin overflow.
- Inspección ampliada de slides afectadas: aprobada después de una segunda corrección geométrica.
- Problemas críticos abiertos: 0.
- Problemas mayores bloqueantes: 0.

