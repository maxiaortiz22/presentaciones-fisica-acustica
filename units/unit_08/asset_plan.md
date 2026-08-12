# Unidad 8 — Plan integral de recursos visuales y multimedia

Versión de planificación · 2026-08-11

## Decisión general

El storyboard aprobado es la autoridad slide por slide. Antes de producir cualquier visual se conserva una de estas clases: `chart`, `diagram`, `mixed`, `external_image`, `video_or_gif` o `equation_only`. `none` se registra como decisión negativa explícita para una slide que debe resolverse con tipografía, tabla o espacio de trabajo y no recibir decoración.

La estrategia dominante es:

1. gráficos propios reproducibles para ejes, curvas y datos;
2. diagramas y ecuaciones editables en PowerPoint;
3. imágenes técnicas reales solo para mostrar transductores, sondas, electrodos o dispositivos;
4. animaciones propias breves cuando el tiempo sea parte del fenómeno;
5. recursos externos únicamente con fuente y licencia trazables.

No se justifican imágenes generadas con IA. Los procesos y objetos de esta unidad pueden representarse con diagramas controlados, gráficos, fotografías técnicas o ilustraciones institucionales. Una imagen sintética introduciría riesgo anatómico o instrumental sin aportar una ventaja pedagógica clara.

## Enrutamiento por skill

| Clase | Skill responsable | Producto previsto |
|---|---|---|
| `chart` | `chart-generation` | script, datos/modelo, SVG y PNG |
| `diagram` | `diagram-generation` | PPTX editable con formas/conectores; SVG/PNG de respaldo |
| `equation_only` | `diagram-generation` | ecuación OMML/SVG + callouts editables |
| `external_image` | `asset-curation` | original preservado, recorte derivado, crédito y texto alternativo |
| `video_or_gif` | `asset-curation` y producción propia | MP4/GIF/audio local + captura estática |
| `mixed` | coordinación de rutas | capas separadas; nunca una slide aplanada |
| `none` | composición nativa | tipografía, tabla o actividad sin imagen |

## Decisión por modalidad

| Modalidad solicitada | Uso en Unidad 8 | Criterio |
|---|---|---|
| Fotografía real | U08-065–066, U08-074, U08-086/089 y U08-093, siempre opcional | Solo hace visible equipo, sonda o dispositivo real; nunca decoración o promesa clínica. |
| Ilustración técnica | U08-046, U08-077 y U08-090 | Se prefiere reconstrucción editable; la ilustración externa solo sirve si su licencia y rotulado son controlables. |
| Imagen anatómica | U08-090; referencia anatómica simplificada en U08-041 | La ilustración NIDCD puede apoyar el implante; no se reutiliza anatomía completa de U6. |
| Gráfico propio | U08-017, 022–025, 030, 035–036, 045, 048–050, 057–060, 065, 069–070, 075, 078–079, 089 y 110–112 | Todo eje, curva o dato pasa por `chart-generation`. |
| Diagrama editable | Recurso dominante en B01, B04 y B08–B10 | Formas y conectores nativos; no aplanar. |
| Tabla | U08-011, 019, 031, 039–040, 047, 058–060, 064, 082–083, 096–097 y 103–114 cuando corresponda | Tabla nativa; máximo recomendado 6 columnas × 8 filas; dividir antes de reducir fuente. |
| Animación | U08-068, U08-074 y U08-091 | Solo para revelar tiempo o transformación; debe existir estado estático equivalente. |
| GIF | Respaldo silencioso posible de U08-MEDIA-002/003 | No es formato maestro; evitar loop distractor. |
| Video | U08-MEDIA-005 como alternativa externa | Fragmento breve, sin depender de audio ni conexión. |
| Audio | U08-MEDIA-001 opcional | Habla supraliminal, no calibrada, no diagnóstica y con transcripción. |
| Captura de instrumento | Ninguna como opción base | Las pantallas dependen del fabricante/protocolo y envejecen; se reemplazan por gráficos propios. Solo se añadiría una captura si una interfaz concreta fuese objeto de estudio. |
| Ecuación anotada | U08-020–021, 026, 051–052, 063, 087–088 y 107–109 | Ecuación editable, símbolos/unidades y callouts mediante `diagram-generation`. |
| Ninguna imagen | U08-003, 005, 059, 064, 067, 097, 103–106, 113–114 | Tipografía, tabla o espacio de trabajo; no agregar decoración. |

## Fuentes externas verificadas y shortlist

Fecha de acceso: 2026-08-11.

| asset_id | autor/organización | título y URL | licencia conocida | slides | propósito | decisión | alternativa disponible |
|---|---|---|---|---|---|---|---|
| U08-IMG-001 | Interacoustics A/S | [AD226 — Instructions for Use](https://www.interacoustics.com/images/files/manuals/en/d_0133701_a_2022_09_en_ad226_instructions_for_use_copy_2.pdf) | © fabricante; reutilización de imágenes no concedida | U08-046 | Validar forma y denominación de auricular DD45 y vibrador B71 | Referencia técnica, no descargar ni copiar imagen; buscar foto libre solo si el diagrama no alcanza | U08-DG-020 editable |
| U08-IMG-002 | AraujoLN · Wikimedia Commons | [Tympanometer.png](https://commons.wikimedia.org/wiki/File:Tympanometer.png) | CC BY 4.0 | U08-065–066 | Mostrar un equipo real y su sonda | `shortlisted`; reutilizable con crédito y recorte | U08-DG-030 sin foto |
| U08-IMG-003 | Centro de Pesquisas Audiológicas de Bauru, USP-Bauru | [Sonda de OEA en triagem auditiva neonatal](https://commons.wikimedia.org/wiki/File:Sonda_do_exame_de_emiss%C3%B5es_otoac%C3%BAsticas_inserida_na_orelha_da_crian%C3%A7a_para_triagem_auditiva_neonatal.jpg) | CC BY-SA 4.0 | U08-074 | Mostrar colocación real de la sonda OEA | `shortlisted`; usar recorte centrado en la sonda y revisar privacidad/contexto | U08-DG-033 y corte esquemático propio |
| U08-IMG-004 | Interacoustics A/S | [Basic ABR testing with Eclipse](https://www.interacoustics.com/abr-equipment/eclipse/support/basic-abr-testing-with-eclipse) | © fabricante; licencia de imagen no indicada | U08-077 | Referencia para montaje superficial de electrodos | Referencia técnica solamente; no descargar la imagen | U08-DG-035 con cabeza esquemática |
| U08-IMG-005 | Bastique · Wikimedia Commons | [Oticon hearing aid top view](https://commons.wikimedia.org/wiki/File:Oticon_hearing_aid_top_view.jpg) | CC BY 4.0 | U08-086, U08-089 | Mostrar un audífono retroauricular real sin usar una foto de paciente | `shortlisted`; recortar para reducir marca y no comparar productos | U08-DG-040 |
| U08-IMG-006 | NIH/NIDCD | [Cochlear Implants](https://www.nidcd.nih.gov/health/cochlear-implants) | Dominio público para contenido NIDCD salvo indicación específica; crédito solicitado | U08-090 | Ubicar partes externas/internas y guía de electrodos | `shortlisted`; preferir ilustración NIDCD y reconstruir rótulos en español | U08-DG-043 editable |
| U08-IMG-007 | Shabash12! · Wikimedia Commons | [Active bone conduction implant](https://commons.wikimedia.org/wiki/File:Active_bone_conduction_implant.png) | CC BY-SA 4.0 | U08-093 | Mostrar una realización real de salida mecánica | `shortlisted`; usar como apoyo complementario, no como modelo universal | U08-DG-046 |
| U08-IMG-008 | — | No se seleccionó una imagen externa de estimulación electroacústica con licencia y neutralidad suficientes | — | U08-093 | Mostrar coexistencia de salida acústica y eléctrica | `replaced`: no descargar; producir diagrama propio sin frecuencia de corte fija | U08-DG-046 |
| U08-MEDIA-005 | AraujoLN · Wikimedia Commons | [Tympanometry — placing the probe](https://commons.wikimedia.org/wiki/File:Tympanometry_-_placing_the_probe.webm) | CC BY 4.0 | U08-066/068 | Mostrar colocación y sellado reales | `shortlisted`; fragmento de 10–15 s tras revisión local | U08-MEDIA-002 + U08-DG-031 |

La política de NIDCD verificada en <https://www.nidcd.nih.gov/policies> indica que, salvo declaración contraria, su contenido está en dominio público; los logotipos no se consideran reutilizables por esa regla. Cada archivo debe volver a comprobarse en su página específica antes de descargarlo.

Fuentes técnicas para gráficos, no assets visuales directos:

- NIOSH, [*Criteria for a Recommended Standard: Occupational Noise Exposure*](https://www.cdc.gov/niosh/docs/98-126/pdfs/98-126.pdf), tabla 3-3: fuente candidata para U08-CH-004; publicación oficial de gobierno de EE. UU.
- Klein y Mills, [*Physiological and psychophysical measures from humans with temporary threshold shift*](https://pubmed.ncbi.nlm.nih.gov/7288041/), DOI `10.1121/1.386955`: fuente primaria candidata para U08-CH-002 bajo su exposición específica.
- Ryan et al., [*Temporary and Permanent Noise-Induced Threshold Shifts*](https://pmc.ncbi.nlm.nih.gov/articles/PMC4988324/): revisión de contexto; no se extraerán datos como si fueran una cohorte única.
- NIDCD, [*Hearing Aids*](https://www.nidcd.nih.gov/health/hearing-aids): referencia institucional para partes y límites del audífono.
- Interacoustics Academy, [*Tympanometry: An Introduction*](https://www.interacoustics.com/academy/tympanometry-training/traditional-tympanometry/tympanometry): referencia técnica del sistema sonda–presión–micrófono; no copiar figuras.

## Matriz slide por slide

| slide_id | visual_class | apoyo visual o multimedia decidido | asset/familia | decisión de producción |
|---|---|---|---|---|
| U08-001 | mixed | Motivo vectorial oído–instrumento–dispositivo; ninguna foto | composición nativa | Producir con formas editables |
| U08-002 | diagram | Caso ramificado | U08-DG-001 | Producir editable |
| U08-003 | none | Tres zonas tipográficas | — | No agregar imagen |
| U08-004 | diagram | Mapa de U4–U7 reutilizado | mapa de curso editable | Reutilizar, no crear asset externo |
| U08-005 | none | Objetivos jerarquizados | — | No agregar imagen |
| U08-006 | mixed | Mini cadena de salidas físicas | miniatura U08-DG-039 | Reutilizar formas editables |
| U08-007 | diagram | Mapa de cuatro encuentros | U08-DG-002 | Prototipo temprano |
| U08-008 | mixed | Divisor tipográfico con cinco términos | composición nativa | Sin asset independiente |
| U08-009 | diagram | Cinco clases de evidencia | U08-DG-003 | Producir editable |
| U08-010 | diagram | Seis preguntas del caso | U08-DG-004 | Prototipo temprano |
| U08-011 | mixed | Tarjetas movibles/tabla | tabla nativa | Producir dentro del deck |
| U08-012 | diagram | Clasificación funcional por regiones | U08-DG-005 | Complementario |
| U08-013 | diagram | Patrón → preguntas abiertas | U08-DG-006 | Producir editable |
| U08-014 | mixed | Comparación TTS/tinnitus + línea temporal | formas nativas | Sin asset externo |
| U08-015 | diagram | Batería convergente | U08-DG-007 | Producir editable |
| U08-016 | diagram | Recapitulación de clases | U08-DG-003 variante | Reutilizar con nueva anotación |
| U08-017 | chart | Antes/después temporal | U08-CH-001 estado inicial | Producir con el gráfico |
| U08-018 | diagram | Variables de exposición | U08-DG-008 | Producir editable |
| U08-019 | mixed | Dos mediciones alineadas | formas/tabla nativa | Sin asset independiente |
| U08-020 | equation_only | TTS anotada | U08-DG-009 | Producir editable |
| U08-021 | equation_only | Ejemplo TTS | U08-DG-010 | Producir editable |
| U08-022 | chart | Serie temporal conceptual | U08-CH-001 | Listo como esquema |
| U08-023 | chart | Curvas cuantitativas pos-exposición | U08-CH-002 | Bloqueado por selección de fuente |
| U08-024 | chart | Lectura guiada de curva | U08-CH-002 o U08-CH-001 | Usar alternativa conceptual mientras esté bloqueado |
| U08-025 | chart | Comparación de dos trayectorias temporales | U08-CH-001 variante | Producir conceptual |
| U08-026 | equation_only | Normalización temporal | U08-DG-011 | Complementario; validar descriptor |
| U08-027 | mixed | Línea temporal + ecuación + alerta | U08-CH-001 + U08-DG-009 | Reutilizar capas |
| U08-028 | mixed | Divisor con triángulo de evidencia | formas nativas | Sin asset independiente |
| U08-029 | diagram | Evidencia compatible con PAIR/NIHL | U08-DG-012 | Producir editable |
| U08-030 | chart | Escotadura audiométrica ficticia | U08-CH-003 | Producir tras validar símbolos |
| U08-031 | mixed | Comparación trauma/ototoxicidad | tabla nativa | Sin fotografía clínica |
| U08-032 | diagram | Señal externa ausente vs percepto | formas nativas, patrón U08-DG-028 | Producir editable sin onda interna |
| U08-033 | diagram | Modelo multifactorial | U08-DG-013 | Producir editable |
| U08-034 | diagram | Checklist para porcentajes | U08-DG-014 | Prototipo temprano |
| U08-035 | chart | Riesgo excedente por edad/exposición | U08-CH-004 | Fuente NIOSH identificada; pendiente aprobación |
| U08-036 | mixed | Gráfico + checklist | U08-CH-004 + U08-DG-014 | Producir después de aprobar métrica |
| U08-037 | diagram | Divisor con cadena tenue | U08-DG-015 miniatura | Reutilizar formas |
| U08-038 | diagram | Cadena común de medición | U08-DG-015 | Producir editable |
| U08-039 | diagram | Seis preguntas comunes | U08-DG-016 | Prototipo temprano |
| U08-040 | mixed | Tarea conductual vs sensor | pictogramas técnicos propios | Sin imagen externa |
| U08-041 | diagram | Mapa anatómico-funcional | U08-DG-017 | Prototipo temprano |
| U08-042 | diagram | Condiciones del registro | U08-DG-018 | Producir editable |
| U08-043 | diagram | Batería y discrepancia | U08-DG-019 | Producir editable |
| U08-044 | diagram | Recapitulación de matriz | U08-DG-016 variante | Reutilizar con campos incompletos |
| U08-045 | chart | Audiograma vacío | U08-CH-005A estado inicial | Producir con gráfico |
| U08-046 | mixed | Foto/referencia de transductores + rutas | U08-IMG-001 + U08-DG-020 | Base editable; foto solo si aparece alternativa libre adecuada |
| U08-047 | diagram | SPL/HL/SL | U08-DG-021 | Prototipo temprano |
| U08-048 | chart | Construcción de ejes | U08-CH-005A | Producir en estados |
| U08-049 | chart | Audiograma por vías | U08-CH-005 | Producir tras validar simbología |
| U08-050 | chart | Actividad sobre audiograma | U08-CH-005 variante | Reutilizar con callouts |
| U08-051 | equation_only | Diferencia aérea–ósea | U08-DG-022 | Producir editable |
| U08-052 | equation_only | Ejemplo aérea–ósea | U08-DG-023 | Producir editable |
| U08-053 | diagram | Condiciones de audiometría | U08-DG-024 | Complementario; prototipo |
| U08-054 | mixed | Audiograma + ecuación + límite | U08-CH-005 + U08-DG-022 | Reutilizar capas |
| U08-055 | diagram | Tres tareas verbales | U08-DG-025 | Producir editable |
| U08-056 | diagram | Cadena de logoaudiometría | U08-DG-026; U08-MEDIA-001 opcional | Audio no indispensable |
| U08-057 | chart | Curva desempeño–nivel | U08-CH-006 | Producir sintética tras elegir escala |
| U08-058 | mixed | Tabla antes/después + mini curva | U08-CH-006 variante | Reutilizar gráfico |
| U08-059 | none | Formulario didáctico | tabla nativa | No agregar imagen |
| U08-060 | mixed | Audiograma vs curva verbal | U08-CH-005 + U08-CH-006 | Composición de dos miniaturas |
| U08-061 | diagram | Bucle de correspondencia | U08-DG-027 | Producir editable |
| U08-062 | diagram | Físico vs perceptual | U08-DG-028 | Producir editable |
| U08-063 | equation_only | dB SL individual | U08-DG-029 | Complementario; validar notación |
| U08-064 | none | Tabla comparativa | tabla nativa | No agregar imagen |
| U08-065 | mixed | Equipo real + curva vacía | U08-IMG-002 + U08-CH-007 | Foto opcional; funciona sin ella |
| U08-066 | mixed | Foto de equipo + cadena instrumental | U08-IMG-002 + U08-DG-030; U08-MEDIA-005 opcional | Shortlist externo; diagrama obligatorio |
| U08-067 | none | Definición con mini eje | formas nativas | No asset independiente |
| U08-068 | video_or_gif | Barrido que construye la curva | U08-MEDIA-002 + U08-DG-031 | Animación propia; video externo solo alternativa |
| U08-069 | chart | Familia de timpanogramas | U08-CH-007 | Producir tras elegir unidad |
| U08-070 | chart | Actividad sobre morfologías | U08-CH-007 variante | Reutilizar con paneles numerados |
| U08-071 | diagram | Curva plana → condiciones | U08-DG-032 | Producir editable |
| U08-072 | diagram | Recapitulación instrumental | U08-DG-030/031 | Reutilizar reducido |
| U08-073 | mixed | Divisor con tres trazas | formas propias | Sin captura de instrumento |
| U08-074 | mixed | Foto de sonda + ida/retorno | U08-IMG-003 + U08-DG-033 + U08-MEDIA-003 | Foto opcional; diagrama y estático obligatorios |
| U08-075 | chart | OEA y piso de ruido | U08-CH-010 | Producir conceptual |
| U08-076 | diagram | OEA dentro de batería | U08-DG-034 | Producir editable |
| U08-077 | mixed | Montaje de electrodos + cadena PEAT | U08-IMG-004 + U08-DG-035 | Usar esquema; imagen de fabricante solo referencia |
| U08-078 | chart | Forma de onda PEAT | U08-CH-008 | Producir conceptual |
| U08-079 | mixed | Forma de onda vs palabra “respuesta” | U08-CH-008 variante | Reutilizar miniatura |
| U08-080 | diagram | Cadena ECoG | U08-DG-036 | Producir editable |
| U08-081 | diagram | Componentes ECoG | U08-DG-037 | Complementario |
| U08-082 | diagram | Matriz OEA/PEAT/ECoG | U08-DG-038 | Prototipo temprano |
| U08-083 | diagram | Actividad de discrepancia | U08-DG-038 variante | Reutilizar dos cadenas |
| U08-084 | mixed | Divisor con salidas acústica/eléctrica/mecánica | U08-DG-039 miniatura | Reutilizar formas |
| U08-085 | diagram | Cadena común de dispositivos | U08-DG-039 | Producir editable |
| U08-086 | mixed | Audífono real + cadena | U08-IMG-005 + U08-DG-040 | Foto opcional y acreditada |
| U08-087 | equation_only | Ganancia anotada | U08-DG-041 | Producir editable |
| U08-088 | equation_only | Ejemplo de ganancia | U08-DG-042 | Producir editable |
| U08-089 | mixed | Entrada–salida + audífono | U08-CH-009 + U08-IMG-005 | Priorizar gráfico; foto opcional |
| U08-090 | mixed | Ilustración de implante + cadena | U08-IMG-006 + U08-DG-043 | Shortlist NIDCD + rótulos propios |
| U08-091 | mixed | Bandas/canales/electrodos + animación | U08-DG-044 + U08-MEDIA-004 | Sin audio de “simulación” |
| U08-092 | diagram | Audífono vs implante | U08-DG-045 | Producir editable |
| U08-093 | mixed | Dispositivo óseo real + dos mini-cadenas | U08-IMG-007 + U08-DG-046 | U08-IMG-008 reemplazado por esquema |
| U08-094 | diagram | Síntesis de dispositivos | U08-DG-047 | Prototipo temprano |
| U08-095 | mixed | Divisor con miniatura del caso | U08-DG-001 variante | Reutilizar, sin asset nuevo |
| U08-096 | diagram | Matriz caso–dato–pregunta | U08-DG-048 | Prototipo temprano |
| U08-097 | none | Matriz para completar | tabla nativa | No agregar imagen |
| U08-098 | diagram | Inferencia permitida y límite | U08-DG-049 | Producir editable |
| U08-099 | diagram | Identificación por tipo de salida | U08-DG-047 variante | Reutilizar reducido |
| U08-100 | diagram | Proceso profesional | U08-DG-050 | Producir editable |
| U08-101 | diagram | Síntesis acumulativa | U08-DG-051 | Prototipo temprano |
| U08-102 | diagram | Puente U8→U10 | U08-DG-052 | Producir editable |
| U08-103 | none | Índice de respaldo | tabla nativa | No agregar imagen |
| U08-104 | none | Tabla SPL/HL/SL | tabla nativa | No agregar imagen |
| U08-105 | none | Matriz de estudios | tabla nativa | Dividir antes de reducir fuente |
| U08-106 | none | Matriz de dispositivos | tabla nativa | No agregar imagen |
| U08-107 | equation_only | Ejercicio TTS | U08-DG-009 variante | Reutilizar ecuación; datos nuevos |
| U08-108 | equation_only | Ejercicio `L_Aeq,T` | U08-DG-011 variante | Reutilizar ecuación; validar descriptor |
| U08-109 | equation_only | Ejercicio aérea–ósea | U08-DG-022 variante | Reutilizar ecuación; datos nuevos |
| U08-110 | chart | Ganancia por frecuencia | U08-CH-011 | Producir solo si se usa respaldo |
| U08-111 | chart | Ficha de trazabilidad TTS | U08-CH-002 | Mantener bloqueada con metadatos |
| U08-112 | chart | Ficha de riesgo | U08-CH-004 | Usar tabla NIOSH solo tras aprobación |
| U08-113 | none | Glosario de siglas | tabla nativa | No agregar imagen |
| U08-114 | none | Fuentes y límites | texto jerarquizado | No agregar imagen |

## Decisión de descarga

No se descargó ningún recurso externo en esta fase. Aunque U08-IMG-002, U08-IMG-003, U08-IMG-005, U08-IMG-006, U08-IMG-007 y U08-MEDIA-005 poseen licencias o condiciones claramente reutilizables, todavía son una shortlist y la mayoría son opcionales. La descarga se hará después de aprobar el recorte/uso exacto, evitando duplicar archivos que luego se descarten. Los recursos de fabricante U08-IMG-001 y U08-IMG-004 son solo referencias técnicas y no se copiarán sin permiso.

## Faltantes y decisiones antes de producción

- Confirmar si U08-046 necesita foto real; el diagrama editable puede ser suficiente.
- Aprobar el uso de fotografías con pacientes en U08-IMG-003; si genera dudas, usar únicamente el esquema.
- Elegir unidad de inmitancia para U08-CH-007 antes de diseñar U08-MEDIA-002.
- Validar siglas, simbología audiométrica y dB SL antes de producir ecuaciones y gráficos.
- Resolver adopción del modelo NIOSH para U08-CH-004 y de una fuente humana específica para U08-CH-002.
- Decidir si el video externo U08-MEDIA-005 aporta algo que la animación propia no muestra; no usar ambos por redundancia.
