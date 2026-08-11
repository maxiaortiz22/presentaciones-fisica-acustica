# Unidad 6 — Plan integral de assets

Versión inicial · 2026-08-10

## Decisión general

El storyboard es la autoridad de asignación slide por slide. Los visuales se enrutan así: `chart-generation` para curvas, ejes y datos; `diagram-generation` para relaciones, flujos, tablas editables y ecuaciones anotadas; `asset-curation` para fotografías, imágenes anatómicas, videos y recursos externos. `mixed` exige coordinar dos de esas capas sin aplanar la slide. `none` no es una clase de visual: registra explícitamente que la slide no necesita imagen.

No se incorporó ningún recurso a PowerPoint. Se descargaron solamente tres fuentes reutilizables con licencia clara para inspección y recorte futuro; el resto sigue preseleccionado, bloqueado o previsto como producción propia.

## Prioridad de producción

1. Construir diagramas y gráficos propios que expliquen relaciones y modelos del capítulo.
2. Usar imágenes académicas o técnicas para validar anatomía y mostrar instrumentos reales.
3. Reservar animación para movimiento y secuencia temporal que no pueda explicarse igual de bien con estados fijos.
4. No usar imagen generada por IA: no existe aquí una necesidad pedagógica que supere un esquema editable o una fuente anatómica verificable.
5. Mantener siempre una alternativa sin conexión y una versión estática de todo recurso dinámico.

## Evaluación de fuentes externas

| id | organización/autor | título y URL | licencia conocida | slides | decisión pedagógica | alternativa disponible |
|---|---|---|---|---|---|---|
| U06-IMG-001/003 | Jmarchn · Wikimedia Commons | [Anatomy of the Human Ear 1 Intl](https://commons.wikimedia.org/wiki/File:Anatomy_of_the_Human_Ear_1_Intl.svg) | CC BY-SA 3.0; también GFDL | 001, 009, 010, 019, 029 | Útil como referencia y recorte; sus 23 números son demasiado densos para proyección directa. | U06-DG-005, 012 y 015. |
| U06-IMG-002 | Cstokesrees · Wikimedia Commons | [RealEarMeasurement](https://commons.wikimedia.org/wiki/File:RealEarMeasurement.png) | CC BY-SA 3.0 | 012 | Fotografía real pertinente: sonda y micrófono de referencia visibles. | U06-DG-006 con dos posiciones de medición. |
| U06-IMG-004 | Pearson Scott Foresman | [Eustachian Tube (PSF)](https://commons.wikimedia.org/wiki/File:Eustachian_Tube_(PSF).png) | Dominio público | 026 | Preseleccionada; comparar claridad con un recorte de U06-IMG-003 antes de descargar. | U06-DG-014. |
| U06-IMG-006 | Hsebasti · Wikimedia Commons | [Organ of Corti multilingual updated version](https://commons.wikimedia.org/wiki/File:Organ_of_Corti_multilingual_updated_version.svg) | CC BY-SA 4.0 | 056, 073 | Buena referencia de estructuras; demasiado densa y multilingüe como visual central sin reconstrucción. | U06-DG-035B y 041. |
| U06-IMG-007/REF-003 | Henry Vandyke Carter · Gray's Anatomy | [Gray 932 — Tunnel of Corti](https://commons.wikimedia.org/wiki/File:Gray932.png) | Dominio público · PDM 1.0 | 057, 073, 116 | Fuente histórica trazable; debe triangularse con una fuente moderna. | U06-IMG-006 + U06-DG-036/036B. |
| U06-IMG-008/REF-001 | Rice University · OpenStax | [Anatomy and Physiology 2e — Sensory Perception](https://openstax.org/books/anatomy-and-physiology-2e/pages/14-1-sensory-perception) | CC BY-NC-SA 4.0; verificar crédito individual | 051, 052, 060, 073, 088 | Referencia introductoria para orientación y vocabulario; no copiar una figura sin revisar su crédito específico. | U06-DG-032–037 y 041. |
| U06-IMG-009 | Ray Soares Nogueira · Wikimedia Commons | [Equipo portátil de OEA](https://commons.wikimedia.org/wiki/File:Equipamento_port%C3%A1til_de_Emiss%C3%B5es_Otoac%C3%BAsticas_OAE.png) | CC BY-SA 4.0 | 080, 100 | Captura de instrumento posible; no usar como diagrama científico ni como evidencia diagnóstica. | U06-DG-047 y 060. |
| U06-IMG-011 | Robert Fettiplace · Wiley | [Hair Cell Transduction, Tuning, and Synaptic Transmission in the Mammalian Cochlea](https://doi.org/10.1002/cphy.c160049) | Copyright editorial; referencia, no reutilización automática de figuras | 085 | Fuente técnica para cerrar el potencial de reposo y diferenciar potencial receptor/acción. | U06-DG-050 propio, sin copiar figuras. |
| U06-REF-002 | Franz Zenker Castro · Auditio | [Medidas en oído real mediante sonda microfónica](https://doi.org/10.51445/sja.auditio.vol3.2006.0037) | CC BY 3.0 España para el archivo histórico | 011, 012 | Sustento técnico de dependencia espacial y medición con sonda. | Explicación del libro + U06-DG-006. |
| U06-MEDIA-REF-001 | NIH/NIDCD | [Journey of Sound to the Brain](https://www.nidcd.nih.gov/news/multimedia/journey-of-sound-video) | Dominio público según NIDCD; atribución solicitada | 002, 062, 105 | Alternativa breve para apertura/cierre; no reemplaza el modelo por etapas ni debe anticipar el diagnóstico inicial. | U06-DG-001 y U06-MEDIA-001. |
| U06-IMG-005/010 | Equipo docente · UCASAL | Fotografía propia de vibrador óseo / montaje de potencial evocado | Producción propia con seguridad y consentimiento | 047, 101 | Preferible a stock o captura clínica; no producir si no hay equipo adecuado o consentimiento. | U06-DG-029 y 061. |

## Recursos descargados para evaluación

| id | archivo local | inspección | uso autorizado en esta fase |
|---|---|---|---|
| U06-IMG-002 | `assets/external/u06_img_002_medicion_oido_real.png` | Sonda y referencia visibles; resolución suficiente. | Recorte futuro con atribución CC BY-SA 3.0. |
| U06-IMG-003 | `assets/external/u06_img_003_anatomia_oido_humano.svg` | SVG nítido pero excesivamente rotulado. | Referencia y recortes; no proyectar completo como slide central. |
| U06-IMG-006 | `assets/external/u06_img_006_organo_corti_multilingue.svg` | Anatomía útil, rótulos densos; requiere revisión independiente. | Referencia para reconstrucción; no aprobar todavía como visual central. |

U06-IMG-007 y U06-IMG-009 quedaron preseleccionados, pero no se descargaron porque Wikimedia respondió con límite HTTP 429. No se conservaron archivos parciales ni se sustituyeron por copias de origen dudoso.

## Matriz slide por slide

La columna `visual_class` conserva la clasificación aprobada. Las slides `none` quedan registradas para impedir que se agregue decoración en producción.

| slide_id | bloque | visual_class | apoyo recomendado | asset/familia | decisión |
|---|---|---|---|---|---|
| U06-001 | B00 | external_image | imagen anatómica o técnica externa | U06-IMG-001 | usar recorte validado; conservar alternativa propia |
| U06-002 | B00 | diagram | diagrama editable | U06-DG-001 | producir según el plan especializado |
| U06-003 | B00 | diagram | diagrama editable | U06-DG-002 | producir según el plan especializado |
| U06-004 | B00 | diagram | diagrama editable | U06-DG-003 | producir según el plan especializado |
| U06-005 | B00 | mixed | visual mixto propio/externo | U06-DG-001 (miniatura) | producir según el plan especializado |
| U06-006 | B00 | mixed | visual mixto propio/externo | U06-DG-040; U06-DG-044 (miniaturas) | producir según el plan especializado |
| U06-007 | B00 | diagram | diagrama editable | U06-DG-004 | producir según el plan especializado |
| U06-008 | B01 | none | ninguna imagen | — | sin asset; composición tipográfica |
| U06-009 | B01 | mixed | visual mixto propio/externo | U06-DG-005; U06-IMG-001 | producir según el plan especializado |
| U06-010 | B01 | diagram | diagrama editable | U06-DG-005 | producir según el plan especializado |
| U06-011 | B01 | diagram | diagrama editable | U06-DG-006 | producir según el plan especializado |
| U06-012 | B01 | mixed | visual mixto propio/externo | U06-IMG-002; callouts editables | validar/curar antes de usar |
| U06-013 | B01 | diagram | diagrama editable | U06-DG-007 | esperar validación docente |
| U06-014 | B01 | diagram | diagrama editable | U06-DG-008 | producir según el plan especializado |
| U06-015 | B01 | equation_only | ecuación anotada editable | U06-DG-009 | producir según el plan especializado |
| U06-016 | B01 | equation_only | ecuación anotada editable | U06-DG-009B | producir según el plan especializado |
| U06-017 | B01 | diagram | diagrama editable | U06-DG-001 | producir según el plan especializado |
| U06-018 | B02 | none | ninguna imagen | — | sin asset; composición tipográfica |
| U06-019 | B02 | external_image | imagen anatómica o técnica externa | U06-IMG-003 | validar/curar antes de usar |
| U06-020 | B02 | diagram | diagrama editable | U06-DG-010 | producir según el plan especializado |
| U06-021 | B02 | equation_only | ecuación anotada editable | U06-DG-011 | esperar decisión de notación |
| U06-022 | B02 | equation_only | ecuación anotada editable | U06-DG-011B | producir según el plan especializado |
| U06-023 | B02 | diagram | diagrama editable | U06-DG-003 | producir según el plan especializado |
| U06-024 | B02 | diagram | diagrama editable | U06-DG-012 | producir según el plan especializado |
| U06-025 | B02 | diagram | diagrama editable | U06-DG-013 | producir según el plan especializado |
| U06-026 | B02 | mixed | visual mixto propio/externo | U06-DG-014; U06-IMG-004 | producir según el plan especializado |
| U06-027 | B02 | diagram | diagrama editable | U06-DG-001 | producir según el plan especializado |
| U06-028 | B03 | none | ninguna imagen | — | sin asset; composición tipográfica |
| U06-029 | B03 | diagram | diagrama editable | U06-DG-015 | producir según el plan especializado |
| U06-030 | B03 | diagram | diagrama editable | U06-DG-016 | producir según el plan especializado |
| U06-031 | B03 | diagram | diagrama editable | U06-DG-017 | producir según el plan especializado |
| U06-032 | B03 | equation_only | ecuación anotada editable | U06-DG-018 | esperar decisión de notación |
| U06-033 | B03 | diagram | diagrama editable | U06-DG-019 | producir según el plan especializado |
| U06-034 | B03 | equation_only | ecuación anotada editable | U06-DG-020 | esperar decisión de notación |
| U06-035 | B03 | diagram | diagrama editable | U06-DG-021 | producir según el plan especializado |
| U06-036 | B03 | equation_only | ecuación anotada editable | U06-DG-020B | esperar decisión de notación |
| U06-037 | B03 | mixed | visual mixto propio/externo | U06-DG-022 | producir según el plan especializado |
| U06-038 | B03 | diagram | diagrama editable | U06-DG-023 | producir según el plan especializado |
| U06-039 | B03 | mixed | visual mixto propio/externo | U06-DG-001; U06-DG-023 | producir según el plan especializado |
| U06-040 | B04 | none | ninguna imagen | — | sin asset; composición tipográfica |
| U06-041 | B04 | diagram | diagrama editable | U06-DG-024; U06-MEDIA-004 (opcional) | producir según el plan especializado |
| U06-042 | B04 | diagram | diagrama editable | U06-DG-024 | producir según el plan especializado |
| U06-043 | B04 | diagram | diagrama editable | U06-DG-025 | producir según el plan especializado |
| U06-044 | B04 | diagram | diagrama editable | U06-DG-026 | producir según el plan especializado |
| U06-045 | B04 | diagram | diagrama editable | U06-DG-027 | producir según el plan especializado |
| U06-046 | B04 | diagram | diagrama editable | U06-DG-028 | producir según el plan especializado |
| U06-047 | B04 | mixed | visual mixto propio/externo | U06-IMG-005; U06-DG-029; U06-MEDIA-004 (opcional) | validar/curar antes de usar |
| U06-048 | B04 | diagram | diagrama editable | U06-DG-024 | producir según el plan especializado |
| U06-049 | B05 | none | ninguna imagen | — | sin asset; composición tipográfica |
| U06-050 | B05 | diagram | diagrama editable | U06-DG-030 | producir según el plan especializado |
| U06-051 | B05 | diagram | diagrama editable | U06-DG-031 | producir según el plan especializado |
| U06-052 | B05 | diagram | diagrama editable | U06-DG-032 | producir según el plan especializado |
| U06-053 | B05 | diagram | diagrama editable | U06-DG-033 | producir según el plan especializado |
| U06-054 | B05 | diagram | diagrama editable | U06-DG-034 | producir según el plan especializado |
| U06-055 | B05 | diagram | diagrama editable | U06-DG-035 | producir según el plan especializado |
| U06-056 | B05 | mixed | visual mixto propio/externo | U06-IMG-006; U06-DG-035B | validar/curar antes de usar |
| U06-057 | B05 | mixed | visual mixto propio/externo | U06-IMG-007; U06-DG-036 | bloqueado: cerrar fuente antes de producir |
| U06-058 | B05 | diagram | diagrama editable | U06-DG-031 | producir según el plan especializado |
| U06-059 | B05 | diagram | diagrama editable | U06-DG-030 | producir según el plan especializado |
| U06-060 | B05 | diagram | diagrama editable | U06-DG-037 | producir según el plan especializado |
| U06-061 | B06 | none | ninguna imagen | — | sin asset; composición tipográfica |
| U06-062 | B06 | video_or_gif | animación o video | U06-MEDIA-001; U06-DG-038; U06-MEDIA-REF-001 (alternativa) | producir según el plan especializado |
| U06-063 | B06 | diagram | diagrama editable | U06-DG-039 | producir según el plan especializado |
| U06-064 | B06 | chart | gráfico propio | U06-CH-001 | producir según el plan especializado |
| U06-065 | B06 | diagram | diagrama editable | U06-DG-040 | producir según el plan especializado |
| U06-066 | B06 | chart | gráfico propio | U06-CH-001 | producir según el plan especializado |
| U06-067 | B06 | chart | gráfico propio | U06-CH-001 | producir según el plan especializado |
| U06-068 | B06 | chart | gráfico propio | U06-CH-002A | producir según el plan especializado |
| U06-069 | B06 | chart | gráfico propio | U06-CH-002B | producir según el plan especializado |
| U06-070 | B06 | mixed | visual mixto propio/externo | U06-CH-003 | producir según el plan especializado |
| U06-071 | B06 | mixed | visual mixto propio/externo | U06-CH-001; U06-DG-001 | producir según el plan especializado |
| U06-072 | B07 | none | ninguna imagen | — | sin asset; composición tipográfica |
| U06-073 | B07 | mixed | visual mixto propio/externo | U06-IMG-006; U06-DG-041 | validar/curar antes de usar |
| U06-074 | B07 | video_or_gif | animación o video | U06-MEDIA-002; U06-DG-042 | producir según el plan especializado |
| U06-075 | B07 | diagram | diagrama editable | U06-DG-043 | producir según el plan especializado |
| U06-076 | B07 | diagram | diagrama editable | U06-DG-044 | producir según el plan especializado |
| U06-077 | B07 | diagram | diagrama editable | U06-DG-045 | producir según el plan especializado |
| U06-078 | B07 | diagram | diagrama editable | U06-DG-046 | producir según el plan especializado |
| U06-079 | B07 | diagram | diagrama editable | U06-DG-044 | producir según el plan especializado |
| U06-080 | B07 | diagram | diagrama editable | U06-DG-047 | producir según el plan especializado |
| U06-081 | B07 | diagram | diagrama editable | U06-DG-044 | producir según el plan especializado |
| U06-082 | B08 | none | ninguna imagen | — | sin asset; composición tipográfica |
| U06-083 | B08 | diagram | diagrama editable | U06-DG-048 | producir según el plan especializado |
| U06-084 | B08 | diagram | diagrama editable | U06-DG-049 | producir según el plan especializado |
| U06-085 | B08 | mixed | visual mixto propio/externo | U06-IMG-011; U06-DG-050 | bloqueado: cerrar fuente antes de producir |
| U06-086 | B08 | diagram | diagrama editable | U06-DG-051 | producir según el plan especializado |
| U06-087 | B08 | diagram | diagrama editable | U06-DG-052 | producir según el plan especializado |
| U06-088 | B08 | diagram | diagrama editable | U06-DG-053; U06-MEDIA-003 (opcional) | producir según el plan especializado |
| U06-089 | B08 | diagram | diagrama editable | U06-DG-054 | producir según el plan especializado |
| U06-090 | B08 | diagram | diagrama editable | U06-DG-055; U06-MEDIA-003 (opcional) | producir según el plan especializado |
| U06-091 | B08 | diagram | diagrama editable | U06-DG-056; U06-MEDIA-003 (opcional) | producir según el plan especializado |
| U06-092 | B08 | diagram | diagrama editable | U06-DG-055 | producir según el plan especializado |
| U06-093 | B08 | diagram | diagrama editable | U06-DG-057 | producir según el plan especializado |
| U06-094 | B09 | none | ninguna imagen | — | sin asset; composición tipográfica |
| U06-095 | B09 | mixed | visual mixto propio/externo | U06-CH-004; U06-DG-058 | producir según el plan especializado |
| U06-096 | B09 | chart | gráfico propio | U06-CH-005 | bloqueado: cerrar fuente antes de producir |
| U06-097 | B09 | diagram | diagrama editable | U06-DG-058B | producir según el plan especializado |
| U06-098 | B09 | mixed | visual mixto propio/externo | U06-CH-006; U06-DG-059 | producir según el plan especializado |
| U06-099 | B09 | diagram | diagrama editable | U06-DG-059B | producir según el plan especializado |
| U06-100 | B09 | diagram | diagrama editable | U06-DG-060 | producir según el plan especializado |
| U06-101 | B09 | mixed | visual mixto propio/externo | U06-IMG-010; U06-DG-061 | validar/curar antes de usar |
| U06-102 | B09 | diagram | diagrama editable | U06-DG-062 | producir según el plan especializado |
| U06-103 | B09 | diagram | diagrama editable | U06-DG-063 | producir según el plan especializado |
| U06-104 | B09 | diagram | diagrama editable | U06-DG-064 | producir según el plan especializado |
| U06-105 | B09 | none | ninguna imagen | U06-MEDIA-REF-001 (alternativa; no necesaria) | sin asset; composición tipográfica |
| U06-106 | B10 | none | ninguna imagen | — | sin asset; composición tipográfica |
| U06-107 | B10 | diagram | tabla editable | U06-DG-032B | producir según el plan especializado |
| U06-108 | B10 | equation_only | ecuación anotada editable | U06-DG-020B | esperar decisión de notación |
| U06-109 | B10 | equation_only | ecuación anotada editable | U06-DG-009B | producir según el plan especializado |
| U06-110 | B10 | equation_only | ecuación anotada editable | U06-DG-011B | producir según el plan especializado |
| U06-111 | B10 | equation_only | ecuación anotada editable | U06-DG-020C | esperar decisión de notación |
| U06-112 | B10 | none | ninguna imagen | — | sin asset; composición tipográfica |
| U06-113 | B10 | diagram | diagrama editable | U06-DG-026B | producir según el plan especializado |
| U06-114 | B10 | diagram | diagrama editable | U06-DG-053B; U06-DG-054B | producir según el plan especializado |
| U06-115 | B10 | chart | gráfico propio | U06-CH-009 | bloqueado: cerrar fuente antes de producir |
| U06-116 | B10 | mixed | visual mixto propio/externo | U06-IMG-007; U06-DG-036B | bloqueado: cerrar fuente antes de producir |
| U06-117 | B10 | none | ninguna imagen | — | sin asset; composición tipográfica |

## Resumen de carga visual

- `chart`: 7 slides.
- `diagram`: 64 slides.
- `mixed`: 18 slides.
- `external_image`: 2 slides.
- `video_or_gif`: 2 slides.
- `equation_only`: 11 slides.
- `none`: 13 slides con decisión explícita de no usar imagen.

## Puertas de aprobación

- **Anatomía:** U06-057/U06-116 (túnel de Corti) y U06-073/U06-074 deben pasar revisión anatómica independiente.
- **Fuente:** U06-085, U06-096 y U06-115 no se producen hasta cerrar referencia y condiciones.
- **Notación:** U06-021, 032, 034, 036, 108 y 111 esperan la decisión registrada en `open_decisions.md`.
- **Modelo:** U06-013 requiere validación docente de la formulación “esférica a cilíndrica”.
- **Editabilidad:** diagramas, tablas, flechas y ecuaciones deben quedar editables en PowerPoint; SVG/PNG es solo respaldo.
- **Accesibilidad:** todo recurso externo debe tener alt text, crédito y contraste; todo video debe tener descripción y captura estática.

Los detalles cuantitativos, geométricos y temporales se encuentran respectivamente en `chart_plan.md`, `diagram_plan.md` y `media_plan.md`; la licencia, URL, estado y ruta local están en `asset_manifest.csv`.
