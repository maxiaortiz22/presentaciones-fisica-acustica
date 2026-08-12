# Unidad 7 — Plan integral de recursos visuales y multimedia

Versión de planificación · 2026-08-11

## Decisión general

El storyboard aprobado es la autoridad slide por slide. Antes de producir cada visual se conserva su clasificación: `chart`, `diagram`, `mixed`, `external_image`, `video_or_gif` o `equation_only`. `none` se usa únicamente como decisión negativa explícita: la slide no tiene un visual que clasificar y no debe recibir decoración.

La estrategia dominante es reconstruir como formas editables o gráficos reproducibles las nueve figuras TikZ del capítulo. Las fotografías externas se limitan a montajes o instrumentos reales que un esquema no puede mostrar con la misma autenticidad. No se justifica generar imágenes con IA: los fenómenos pueden representarse con gráficos, diagramas, fotografías técnicas o animaciones controladas.

## Enrutamiento por skill

| Clase | Skill responsable | Producto previsto |
|---|---|---|
| `chart` | `chart-generation` | SVG editable y PNG de respaldo; script y datos/modelo |
| `diagram` | `diagram-generation` | formas y conectores nativos de PowerPoint; SVG/PNG de respaldo |
| `equation_only` | `diagram-generation` | ecuación editable o SVG con callouts editables |
| `external_image` | `asset-curation` | original preservado, recorte derivado, crédito y texto alternativo |
| `video_or_gif` | `asset-curation` y producción propia | MP4/GIF/audio local + captura estática |
| `mixed` | coordinación de dos rutas | capas separadas; nunca una slide completa aplanada |

## Fuentes externas verificadas

| id | autor/organización | título y URL | licencia conocida | slides | decisión | alternativa |
|---|---|---|---|---|---|---|
| U07-IMG-002 | Cstokesrees · Wikimedia Commons | [RealEarMeasurement](https://commons.wikimedia.org/wiki/File:RealEarMeasurement.png) | CC BY-SA 3.0 | U07-025 | Reutilizable; ya existe original inspeccionado en U6. Usar recorte vertical con sonda visible y callouts propios. | U07-DG-010 sin fotografía. |
| U07-IMG-003 | Steve Johnson · Wikimedia Commons | [Behind-the-Ear Hearing Aid grayscale photo](https://commons.wikimedia.org/wiki/File:Behind-the-Ear_Hearing_Aid_grayscale_photo.jpg) | CC BY 2.0 | U07-116 | Shortlist opcional: muestra el dispositivo real, pero el patrón polar debe ser propio. | Silueta genérica editable + patrón polar propio. |
| U07-IMG-004 | EJ Posselius · Wikimedia Commons | [Georg Neumann KU 100 Dummy Head](https://commons.wikimedia.org/wiki/File:Georg_Neumann_Ku_100_Dummy_Head.jpg) | CC BY-SA 2.0 | U07-106–107 | Shortlist complementario para mostrar captura binaural; no explica por sí solo HRTF ni cono de confusión. | Cabeza/pabellón esquemáticos U07-DG-034/037. |
| U07-REF-001 | Algazi, Duda, Thompson y Avendano · UC Davis CIPIC | [The CIPIC HRTF Database](https://www.ece.ucdavis.edu/cipic/wp-content/uploads/sites/12/2015/04/cipic_CIPIC_HRTF_Database.pdf) | Dataset declarado de dominio público en el artículo; artículo como referencia | U07-102, 106–108 | Fuente técnica para validar direcciones, individualidad y medición; no copiar figuras automáticamente. | Libro + referencia `carlini2024`. |
| U07-REF-002 | Brinkmann et al. · TU Berlin/SOFA | [HUTUBS HRTF Database documentation](https://www.sofaconventions.org/data/database_sofa_0.6/hutubs/Documentation.pdf) | CC BY 4.0 para los datos | U07-106 | Fuente de datos posible si se decide mostrar espectros HRTF reales. No descargar en esta fase. | Espectros sintéticos rotulados “conceptuales”. |
| U07-REF-003 | NIH/NIDCD | [Hearing Aids](https://www.nidcd.nih.gov/health/hearing-aids) | Contenido NIDCD en dominio público salvo indicación específica | U07-116 | Referencia institucional sobre partes y límites; no usar logotipo ni inferir aval. | Libro + NCBI U07-REF-004. |
| U07-REF-004 | National Guideline Centre · NCBI Bookshelf | [Hearing aid microphones and noise reduction algorithms](https://www.ncbi.nlm.nih.gov/books/NBK536536/) | Uso como referencia; no reutilizar figuras sin permiso específico | U07-116 | Sustenta diferencia omnidireccional/direccional y sus límites. | NIDCD + explicación del libro. |
| U07-REF-005 | ISO | [ISO 226:2023 — Normal equal-loudness-level contours](https://www.iso.org/standard/83117.html) | © ISO; metadatos/abstract consultables, datos normativos no asumidos como reutilizables | U07-029–030, 123 | Usar para condiciones y edición; no reproducir Annex A/B sin autorización. | U07-DG-011 y curva esquemática no normativa. |
| U07-REF-006 | ASA/ANSI | [ANSI/ASA S3.5-1997 (R2024)](https://webstore.ansi.org/standards/asa/asaansis31997r2024) | Estándar comercial con copyright | U07-128 | Solo referencia bibliográfica para SII; no copiar tablas/fórmulas. | Comparación conceptual STI/SII sin cálculo. |

**Fecha de acceso de todas las fuentes web:** 2026-08-11.

## Recursos locales reutilizables

- `context/libro_latex/figures/tikz/unidad-7/`: nueve figuras con propósito, origen y descripción accesible; deben reconstruirse para 16:9, no capturarse como imagen pequeña.
- `units/unit_06/assets/external/u06_img_002_medicion_oido_real.png`: original de U07-IMG-002 ya descargado e inspeccionado; se referencia sin duplicarlo.
- `units/unit_06/output/unidad_06_mecanismo_periferico_final.pptx`: precedente para colores semánticos, anatomía simplificada y ritmo, no fuente de datos U7.

## Matriz slide por slide

| slide_id | bloque | visual_class | apoyo recomendado | asset/familia | layout | decisión |
|---|---|---|---|---|---|---|
| U07-001 | B00 | mixed | motivo técnico editable señal–oyente + composición tipográfica; sin fotografía | U07-DG-001 (variante de portada) | FA_00_PORTADA | producir según plan especializado |
| U07-002 | B00 | video_or_gif | audio guiado + respaldo estático | U07-MEDIA-001 | FA_19_MEDIA_AUDIO_VIDEO | producción propia; multimedia opcional y supraliminal |
| U07-003 | B00 | diagram | diagrama editable | U07-DG-001 | FA_12_PROCESO | producir según plan especializado |
| U07-004 | B00 | none | ninguna imagen | — | FA_02B_CONOCIMIENTOS_PREVIOS | no agregar decoración |
| U07-005 | B00 | diagram | tabla o matriz editable | U07-DG-002 | FA_14B_MINI_EJERCICIO | producir según plan especializado |
| U07-006 | B00 | mixed | tipografía de objetivos + mini diagrama físico–perceptual | U07-DG-012 (miniatura) | FA_02_OBJETIVOS | producir según plan especializado |
| U07-007 | B00 | diagram | diagrama editable | U07-DG-003 | FA_03_MAPA_CLASE | producir según plan especializado |
| U07-008 | B01 | chart | gráfico propio | — | FA_01_DIVISOR | producir según plan especializado |
| U07-009 | B01 | diagram | diagrama editable | U07-DG-004 | FA_08_DEFINICION | producir según plan especializado |
| U07-010 | B01 | diagram | diagrama editable | U07-DG-005 | FA_12_PROCESO | producir según plan especializado |
| U07-011 | B01 | none | ninguna imagen | — | FA_18_TABLA_DATOS | no agregar decoración |
| U07-012 | B01 | diagram | tabla o matriz editable | — | FA_05_TEXTO_VISUAL_60_40 | producir según plan especializado |
| U07-013 | B01 | mixed | definición tipográfica + mini escala/curva conceptual | U07-CH-001 (recorte conceptual) | FA_08_DEFINICION | producir según plan especializado |
| U07-014 | B01 | chart | gráfico propio | U07-CH-001 | FA_07_GRAFICO_EXPLICACION | producir según plan especializado |
| U07-015 | B01 | chart | gráfico propio | U07-CH-002A | FA_07_GRAFICO_EXPLICACION | producir según plan especializado |
| U07-016 | B01 | chart | gráfico propio | U07-CH-002B | FA_22_VISUAL_COMPLETO | producir según plan especializado |
| U07-017 | B01 | mixed | escala de nivel editable + curva conceptual de umbral | U07-CH-002B | FA_15_ERROR_FRECUENTE | producir según plan especializado |
| U07-018 | B01 | diagram | diagrama editable | U07-DG-006 | FA_14B_MINI_EJERCICIO | producir según plan especializado |
| U07-019 | B01 | mixed | recap tipográfica + marco estímulo–tarea–respuesta | U07-DG-004 | FA_16_RECAP_PARCIAL | producir según plan especializado |
| U07-020 | B02 | diagram | diagrama editable | — | FA_01_DIVISOR | producir según plan especializado |
| U07-021 | B02 | diagram | diagrama editable | U07-DG-007 | FA_05_TEXTO_VISUAL_60_40 | producir según plan especializado |
| U07-022 | B02 | diagram | diagrama editable | U07-DG-008 | FA_22_VISUAL_COMPLETO | producir según plan especializado |
| U07-023 | B02 | equation_only | ecuación anotada editable | U07-DG-009 | FA_09_ECUACION_INTERPRETACION | producir según plan especializado |
| U07-024 | B02 | equation_only | ecuación anotada editable | U07-DG-009B | FA_10_EJEMPLO_RESUELTO | producir según plan especializado |
| U07-025 | B02 | mixed | fotografía real + callouts editables | U07-IMG-002; U07-DG-010 | FA_13_APLICACION_CLINICA | shortlist: reutilizar foto CC BY-SA 3.0 ya descargada en U6 |
| U07-026 | B02 | mixed | composición mixta propia | U07-CH-003 | FA_06_VISUAL_TEXTO_40_60 | producir según plan especializado |
| U07-027 | B02 | diagram | diagrama editable | — | FA_14_PREGUNTA_EJERCICIO | producir según plan especializado |
| U07-028 | B02 | diagram | diagrama editable | U07-DG-011 | FA_12_PROCESO | producir según plan especializado |
| U07-029 | B02 | chart | gráfico propio | U07-CH-004 | FA_07_GRAFICO_EXPLICACION | bloqueado: datos ISO no reutilizables sin autorización; usar esquema conceptual |
| U07-030 | B02 | chart | gráfico propio | U07-CH-004 | FA_14_PREGUNTA_EJERCICIO | bloqueado: datos ISO no reutilizables sin autorización; usar esquema conceptual |
| U07-031 | B02 | diagram | diagrama editable | — | FA_16_RECAP_PARCIAL | producir según plan especializado |
| U07-032 | B03 | mixed | señal esquemática + cuatro rótulos perceptuales | U07-DG-012 (estado inicial) | FA_01_DIVISOR | producir según plan especializado |
| U07-033 | B03 | diagram | diagrama editable | U07-DG-012 | FA_03_MAPA_CLASE | producir según plan especializado |
| U07-034 | B03 | mixed | onda temporal + eje de frecuencia editable | componente propio derivado de U07-CH-005 | FA_08_DEFINICION | producir según plan especializado |
| U07-035 | B03 | mixed | tabla comparativa + mini espectro propio | componente propio; base U07-CH-005 | FA_11_COMPARACION | producir según plan especializado |
| U07-036 | B03 | mixed | audio guiado + respaldo estático | U07-MEDIA-002; U07-CH-005 | FA_19_MEDIA_AUDIO_VIDEO | producción propia; multimedia opcional y supraliminal |
| U07-037 | B03 | diagram | diagrama editable | — | FA_08_DEFINICION | producir según plan especializado |
| U07-038 | B03 | mixed | composición mixta propia | U07-CH-004 | FA_11_COMPARACION | bloqueado: datos ISO no reutilizables sin autorización; usar esquema conceptual |
| U07-039 | B03 | mixed | espectro propio + envolvente temporal coordinada | componente propio compartido con U07-MEDIA-003 | FA_08_DEFINICION | producir según plan especializado |
| U07-040 | B03 | video_or_gif | audio guiado + respaldo estático | U07-MEDIA-003 | FA_19_MEDIA_AUDIO_VIDEO | producción propia; multimedia opcional y supraliminal |
| U07-041 | B03 | diagram | diagrama editable | — | FA_11_COMPARACION | producir según plan especializado |
| U07-042 | B03 | mixed | tabla editable + tres líneas temporales | U07-DG-021 (variante conceptual) | FA_18_TABLA_DATOS | producir según plan especializado |
| U07-043 | B03 | diagram | diagrama editable | U07-DG-012B | FA_16_RECAP_PARCIAL | producir según plan especializado |
| U07-044 | B04 | diagram | diagrama editable | — | FA_01_DIVISOR | producir según plan especializado |
| U07-045 | B04 | diagram | diagrama editable | U07-DG-013 | FA_11_COMPARACION | producir según plan especializado |
| U07-046 | B04 | diagram | diagrama editable | — | FA_08_DEFINICION | producir según plan especializado |
| U07-047 | B04 | diagram | diagrama editable | — | FA_08_DEFINICION | producir según plan especializado |
| U07-048 | B04 | diagram | diagrama editable | U07-DG-014 | FA_12_PROCESO | producir según plan especializado |
| U07-049 | B04 | equation_only | ecuación anotada editable | U07-DG-015 | FA_09_ECUACION_INTERPRETACION | producir según plan especializado |
| U07-050 | B04 | chart | gráfico propio | U07-CH-006 | FA_07_GRAFICO_EXPLICACION | producir según plan especializado |
| U07-051 | B04 | equation_only | ecuación anotada editable | U07-DG-015B | FA_10_EJEMPLO_RESUELTO | producir según plan especializado |
| U07-052 | B04 | none | ninguna imagen | — | FA_14B_MINI_EJERCICIO | no agregar decoración |
| U07-053 | B04 | diagram | diagrama editable | U07-DG-013 | FA_16_RECAP_PARCIAL | producir según plan especializado |
| U07-054 | B05 | mixed | señal objetivo y enmascarador + silueta de umbral | U07-DG-016 (estado inicial) | FA_01_DIVISOR | producir según plan especializado |
| U07-055 | B05 | mixed | dos curvas psicométricas conceptuales + condiciones | U07-CH-001 (variante) + U07-DG-016 | FA_08_DEFINICION | producir según plan especializado |
| U07-056 | B05 | diagram | diagrama editable | U07-DG-016 | FA_03_MAPA_CLASE | producir según plan especializado |
| U07-057 | B05 | equation_only | ecuación anotada editable | U07-DG-017 | FA_09_ECUACION_INTERPRETACION | producir según plan especializado |
| U07-058 | B05 | equation_only | ecuación anotada editable | U07-DG-017B | FA_10_EJEMPLO_RESUELTO | producir según plan especializado |
| U07-059 | B05 | diagram | diagrama editable | U07-DG-018 | FA_12_PROCESO | producir según plan especializado |
| U07-060 | B05 | chart | gráfico propio | U07-CH-007 | FA_07_GRAFICO_EXPLICACION | producir según plan especializado |
| U07-061 | B05 | chart | gráfico propio | U07-CH-007 | FA_14_PREGUNTA_EJERCICIO | producir según plan especializado |
| U07-062 | B05 | diagram | diagrama editable | — | FA_05_TEXTO_VISUAL_60_40 | producir según plan especializado |
| U07-063 | B05 | mixed | composición mixta propia | U07-DG-019 | FA_22_VISUAL_COMPLETO | producir según plan especializado |
| U07-064 | B05 | mixed | gráfico propio + diagrama editable | U07-CH-008; U07-DG-020 | FA_09_ECUACION_INTERPRETACION | producir según plan especializado |
| U07-065 | B05 | diagram | diagrama editable | U07-DG-020B | FA_16_RECAP_PARCIAL | producir según plan especializado |
| U07-066 | B06 | mixed | tres líneas temporales + dos rótulos de mecanismo | U07-DG-021 + U07-DG-022C | FA_01_DIVISOR | producir según plan especializado |
| U07-067 | B06 | diagram | diagrama editable | U07-DG-021 | FA_11_COMPARACION | producir según plan especializado |
| U07-068 | B06 | diagram | diagrama editable | — | FA_05_TEXTO_VISUAL_60_40 | producir según plan especializado |
| U07-069 | B06 | diagram | diagrama editable | — | FA_05_TEXTO_VISUAL_60_40 | producir según plan especializado |
| U07-070 | B06 | diagram | diagrama editable | U07-DG-021 | FA_16_RECAP_PARCIAL | producir según plan especializado |
| U07-071 | B06 | diagram | diagrama editable | — | FA_14B_MINI_EJERCICIO | producir según plan especializado |
| U07-072 | B06 | diagram | diagrama editable | U07-DG-022A | FA_08_DEFINICION | producir según plan especializado |
| U07-073 | B06 | diagram | diagrama editable | U07-DG-022B | FA_08_DEFINICION | producir según plan especializado |
| U07-074 | B06 | mixed | audio guiado + respaldo estático | U07-DG-023; U07-MEDIA-004 | FA_13_APLICACION_CLINICA | producción propia; multimedia opcional y supraliminal |
| U07-075 | B06 | diagram | tabla o matriz editable | U07-DG-022C | FA_16_RECAP_PARCIAL | producir según plan especializado |
| U07-076 | B07 | mixed | contraste detectar/reconocer + cadena mínima | U07-DG-024 (estado inicial) | FA_01_DIVISOR | producir según plan especializado |
| U07-077 | B07 | diagram | diagrama editable | — | FA_08_DEFINICION | producir según plan especializado |
| U07-078 | B07 | diagram | diagrama editable | U07-DG-024 | FA_03_MAPA_CLASE | producir según plan especializado |
| U07-079 | B07 | diagram | diagrama editable | — | FA_05_TEXTO_VISUAL_60_40 | producir según plan especializado |
| U07-080 | B07 | equation_only | ecuación anotada editable | U07-DG-025 | FA_09_ECUACION_INTERPRETACION | producir según plan especializado |
| U07-081 | B07 | equation_only | ecuación anotada editable | U07-DG-025B | FA_10_EJEMPLO_RESUELTO | producir según plan especializado |
| U07-082 | B07 | mixed | audio guiado + respaldo estático | U07-MEDIA-005 | FA_11_COMPARACION | producción propia; multimedia opcional y supraliminal |
| U07-083 | B07 | mixed | gráfico propio + diagrama editable | U07-DG-026; U07-CH-009 | FA_12_PROCESO | producir según plan especializado |
| U07-084 | B07 | mixed | gráfico propio + diagrama editable | U07-CH-009; U07-DG-027 | FA_07_GRAFICO_EXPLICACION | producir según plan especializado |
| U07-085 | B07 | diagram | diagrama editable | U07-DG-026B | FA_05_TEXTO_VISUAL_60_40 | producir según plan especializado |
| U07-086 | B07 | equation_only | ecuación anotada editable | U07-DG-028 | FA_10_EJEMPLO_RESUELTO | producir según plan especializado |
| U07-087 | B07 | diagram | diagrama editable | U07-DG-028B | FA_16_RECAP_PARCIAL | producir según plan especializado |
| U07-088 | B08 | diagram | diagrama editable | — | FA_01_DIVISOR | producir según plan especializado |
| U07-089 | B08 | diagram | diagrama editable | U07-DG-029 | FA_22_VISUAL_COMPLETO | producir según plan especializado |
| U07-090 | B08 | equation_only | ecuación anotada editable | U07-DG-030 | FA_09_ECUACION_INTERPRETACION | producir según plan especializado |
| U07-091 | B08 | equation_only | ecuación anotada editable | U07-DG-030B | FA_10_EJEMPLO_RESUELTO | producir según plan especializado |
| U07-092 | B08 | video_or_gif | audio guiado + respaldo estático | U07-MEDIA-006 | FA_19_MEDIA_AUDIO_VIDEO | producción propia; multimedia opcional y supraliminal |
| U07-093 | B08 | diagram | diagrama editable | U07-DG-031 | FA_03_MAPA_CLASE | producir según plan especializado |
| U07-094 | B08 | diagram | diagrama editable | — | FA_08_DEFINICION | producir según plan especializado |
| U07-095 | B08 | diagram | diagrama editable | U07-DG-032 | FA_22_VISUAL_COMPLETO | producir según plan especializado |
| U07-096 | B08 | diagram | diagrama editable | U07-DG-033 | FA_11_COMPARACION | producir según plan especializado |
| U07-097 | B08 | diagram | diagrama editable | U07-DG-033B | FA_16_RECAP_PARCIAL | producir según plan especializado |
| U07-098 | B09 | diagram | diagrama editable | — | FA_01_DIVISOR | producir según plan especializado |
| U07-099 | B09 | diagram | diagrama editable | U07-DG-034 | FA_08_DEFINICION | producir según plan especializado |
| U07-100 | B09 | diagram | diagrama editable | — | FA_08_DEFINICION | producir según plan especializado |
| U07-101 | B09 | mixed | cabeza esquemática + barras de nivel L/R | U07-DG-034 | FA_08_DEFINICION | producir según plan especializado |
| U07-102 | B09 | mixed | tabla ITD/ILD + bandas cualitativas propias | U07-DG-034 (variante comparativa) | FA_11_COMPARACION | producir según plan especializado |
| U07-103 | B09 | diagram | diagrama editable | U07-DG-035 | FA_22_VISUAL_COMPLETO | producir según plan especializado |
| U07-104 | B09 | equation_only | ecuación anotada editable | U07-DG-036 | FA_09_ECUACION_INTERPRETACION | producir según plan especializado |
| U07-105 | B09 | equation_only | ecuación anotada editable | U07-DG-036B | FA_10_EJEMPLO_RESUELTO | producir según plan especializado |
| U07-106 | B09 | mixed | ilustración técnica/anatómica + gráfico propio | U07-IMG-004 | FA_05_TEXTO_VISUAL_60_40 | shortlist externo; mantener alternativa propia |
| U07-107 | B09 | diagram | diagrama editable | U07-DG-037 | FA_22_VISUAL_COMPLETO | producir según plan especializado |
| U07-108 | B09 | video_or_gif | animación/GIF + dos fotogramas | U07-MEDIA-007 | FA_19_MEDIA_AUDIO_VIDEO | producción propia; multimedia opcional y supraliminal |
| U07-109 | B09 | diagram | diagrama editable | U07-DG-038 | FA_16_RECAP_PARCIAL | producir según plan especializado |
| U07-110 | B10 | mixed | escena multifuente + ruta binaural mínima | U07-DG-039 (estado inicial) | FA_01_DIVISOR | producir según plan especializado |
| U07-111 | B10 | diagram | diagrama editable | U07-DG-039 | FA_12_PROCESO | producir según plan especializado |
| U07-112 | B10 | mixed | audio guiado + respaldo estático | U07-MEDIA-008 | FA_08_DEFINICION | producción propia; multimedia opcional y supraliminal |
| U07-113 | B10 | diagram | diagrama editable | U07-DG-022; U07-DG-040 | FA_03_MAPA_CLASE | producir según plan especializado |
| U07-114 | B10 | diagram | diagrama editable | U07-DG-040 | FA_05_TEXTO_VISUAL_60_40 | producir según plan especializado |
| U07-115 | B10 | diagram | diagrama editable | — | FA_11_COMPARACION | producir según plan especializado |
| U07-116 | B10 | mixed | fotografía real o captura técnica + diagrama | U07-IMG-003 | FA_13_APLICACION_CLINICA | shortlist externo; mantener alternativa propia |
| U07-117 | B10 | mixed | composición mixta propia | U07-DG-041 | FA_13_APLICACION_CLINICA | producir según plan especializado |
| U07-118 | B10 | mixed | tabla/matriz editable de clasificación curricular | componente nativo del layout; sin imagen externa | FA_14_PREGUNTA_EJERCICIO | producir según plan especializado |
| U07-119 | B10 | diagram | diagrama editable | U07-DG-042 | FA_22_VISUAL_COMPLETO | producir según plan especializado |
| U07-120 | B10 | diagram | diagrama editable | U07-DG-042 | FA_17_RECAP_FINAL | producir según plan especializado |
| U07-121 | B10 | diagram | diagrama editable | U07-DG-043 | FA_21_CIERRE_PUENTE | producir según plan especializado |
| U07-122 | B11 | none | ninguna imagen | — | FA_03_MAPA_CLASE | no agregar decoración |
| U07-123 | B11 | chart | gráfico propio | U07-CH-004 | FA_23_APENDICE | bloqueado: datos ISO no reutilizables sin autorización; usar esquema conceptual |
| U07-124 | B11 | none | ninguna imagen | — | FA_18_TABLA_DATOS | no agregar decoración |
| U07-125 | B11 | equation_only | ecuación anotada editable | U07-DG-020C | FA_09_ECUACION_INTERPRETACION | producir solo después del núcleo |
| U07-126 | B11 | equation_only | ecuación anotada editable | U07-DG-020C | FA_10_EJEMPLO_RESUELTO | producir solo después del núcleo |
| U07-127 | B11 | mixed | tabla de variantes + mini curvas propias | U07-CH-008 | FA_18_TABLA_DATOS | producir solo después del núcleo |
| U07-128 | B11 | none | ninguna imagen | — | FA_11_COMPARACION | no agregar decoración |
| U07-129 | B11 | chart | gráfico propio | U07-CH-009 | FA_23_APENDICE | producir solo después del núcleo |
| U07-130 | B11 | equation_only | ecuación anotada editable | — | FA_14_PREGUNTA_EJERCICIO | producir solo después del núcleo |
| U07-131 | B11 | equation_only | ecuación anotada editable | U07-DG-028 | FA_14_PREGUNTA_EJERCICIO | producir solo después del núcleo |
| U07-132 | B11 | mixed | composición mixta propia | U07-DG-029 | FA_14_PREGUNTA_EJERCICIO | producir solo después del núcleo |
| U07-133 | B11 | equation_only | ecuación anotada editable | U07-DG-035 | FA_14_PREGUNTA_EJERCICIO | producir solo después del núcleo |
| U07-134 | B11 | none | ninguna imagen | — | FA_20_BIBLIO_RECURSOS | no agregar decoración |

## Resumen de carga visual

- `chart`: 11 slides.
- `diagram`: 60 slides.
- `equation_only`: 18 slides.
- `mixed`: 34 slides.
- `none`: 7 slides con decisión explícita de no usar imagen.
- `video_or_gif`: 4 slides.

## Política de descarga y producción

No se descargó ningún recurso nuevo. U07-IMG-002 reutiliza un original ya preservado en U6; los demás externos permanecen `shortlisted` o como referencias. Solo se descargará un original después de aprobar su uso, confirmar licencia en la página del archivo y fijar la slide. Los recursos generados se crearán en fases posteriores dentro de `units/unit_07/assets/generated/`.

## Puertas de aprobación

1. Toda slide conserva una sola pregunta visual dominante.
2. `mixed` mantiene capas editables y no duplica el mismo mensaje en gráfico y texto.
3. Ningún asset externo entra sin crédito, licencia, URL, fecha y alternativa.
4. Toda multimedia tiene archivo local, captura estática y variante sin audio.
5. Ningún gráfico normativo usa datos cuya reutilización no esté resuelta.
6. Diagramas y gráficos se validan al tamaño real del layout; cero clipping, colisiones o texto por debajo del mínimo.
7. No se insertó ningún asset en PowerPoint durante esta etapa.
