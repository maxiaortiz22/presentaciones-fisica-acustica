# Inventario inicial del proyecto

Fecha de auditoría: 28 de julio de 2026.

## Alcance y método

Este inventario se realizó antes de crear el mapa del curso, el sistema visual o cualquier presentación nueva. Se inspeccionaron la estructura del repositorio, los archivos fuente, los metadatos básicos de PDF y PowerPoint, las referencias internas del LaTeX y los hashes SHA-256 de todos los archivos.

Se encontraron **122 archivos** antes de generar este informe:

| Grupo | Cantidad |
|---|---:|
| LaTeX (`.tex`) | 68 |
| Imágenes raster (`.png`, `.jpg`) | 28 |
| PDF, incluido el programa, el libro y figuras | 10 |
| Markdown | 10 |
| Python | 3 |
| PowerPoint | 2 |
| Bibliografía BibTeX | 1 |

## Estructura requerida

Todas las carpetas solicitadas ya existían. No fue necesario crear ninguna.

| Carpeta | Estado | Observaciones |
|---|---|---|
| `context/programa/` | Existe | Contiene el programa oficial 2025. |
| `context/libro_pdf/` | Existe | Contiene un libro completo de 296 páginas. |
| `context/libro_latex/` | Existe | Contiene el archivo raíz, los capítulos, la bibliografía, las figuras y los scripts. |
| `context/referencias_visuales/` | Existe | Contiene el PowerPoint original de Unidad 1 y el deck secundario atribuido a Gemini. |
| `style/` | Existe, vacía | Aún no hay guía, auditoría visual ni especificación de master. |
| `units/` | Existe | Contiene `unit_01/` a `unit_10/`, todas vacías. |
| `scripts/` | Existe, vacía | No hay automatización general del proyecto. |
| `output/` | Existe, vacía | No hay entregables finales ni temporales. |

También existen dos carpetas `__pycache__/` vacías dentro de los scripts de figuras. No se modificaron.

## Inventario de gobernanza y skills

| Nombre | Ruta | Tipo | Propósito probable | Unidad relacionada | Observaciones |
|---|---|---|---|---|---|
| `AGENTS.md` | `AGENTS.md` | Markdown | Reglas globales del proyecto, flujo, fuentes, estilo y definición de terminado. | Todas | Fuente normativa principal para el trabajo del agente. |
| `README.md` | `README.md` | Markdown | Instrucciones breves de instalación y secuencia de skills. | Todas | Documento de configuración inicial; no describe el estado real del proyecto. |
| `SKILL.md` | `skills/course-architecture/SKILL.md` | Skill | Construcción del mapa global, dependencias y cobertura. | Todas | Disponible; no se activó porque se pidió no crear todavía el mapa del curso. |
| `SKILL.md` | `skills/style-system/SKILL.md` | Skill | Auditoría visual, guía de estilo, layouts y master. | Todas | Disponible; no se activó para producir el sistema visual. |
| `SKILL.md` | `skills/unit-storyboard/SKILL.md` | Skill | Brief y storyboard pedagógico por unidad. | Cada unidad | Disponible; requiere previamente mapa y guía de estilo. |
| `SKILL.md` | `skills/asset-curation/SKILL.md` | Skill | Búsqueda, evaluación y manifiesto de recursos externos. | Cada unidad | Disponible; aún no hay `asset_manifest.csv`. |
| `SKILL.md` | `skills/chart-generation/SKILL.md` | Skill | Figuras y gráficos reproducibles. | Cada unidad | Disponible; ya hay antecedentes de scripts y figuras en el libro. |
| `SKILL.md` | `skills/slide-writing/SKILL.md` | Skill | Texto visible y notas del orador a partir del storyboard. | Cada unidad | Disponible; no debe usarse antes del storyboard. |
| `SKILL.md` | `skills/deck-review/SKILL.md` | Skill | Revisión de cobertura, ciencia, pedagogía, visual y producción. | Cada unidad | Disponible; no hay decks de unidad en producción para revisar. |
| `SKILL.md` | `skills/consistency-guard/SKILL.md` | Skill | Coherencia curricular, terminológica, notacional y visual entre unidades. | Todas | Disponible; se usará después de completar unidades. |

## Fuentes académicas principales

| Nombre | Ruta | Tipo | Propósito probable | Unidad relacionada | Observaciones |
|---|---|---|---|---|---|
| `Programa de Física Acústica.pdf` | `context/programa/Programa de Física Acústica.pdf` | PDF, 6 páginas, A4 | Programa oficial y alcance mínimo obligatorio. | Unidades 1–10 | Año 2025; autor Ing. Maximiliano Adriel Ortiz. Incluye objetivos, metodología, evaluación, contenidos y bibliografía. Debe confirmarse su vigencia frente al libro 2026. |
| `Física Acústica para Fonoaudiología.pdf` | `context/libro_pdf/Física Acústica para Fonoaudiología.pdf` | PDF, 296 páginas, carta | Libro completo de consulta y verificación visual. | Unidades 1–10 | Edición fechada 2026; generado el 27/07/2026. Sigue las diez unidades del programa e incluye ejercicios, respuestas y glosarios. Carece de metadatos PDF de título y autor. |
| `main.tex` | `context/libro_latex/main.tex` | LaTeX | Punto de entrada y configuración de compilación del libro. | Todas | Disponible. Carga los paquetes, define título y autor, incorpora la introducción y las diez unidades en orden, y enlaza `bibliography/references`. Su compilación aún no fue verificada en esta auditoría. |
| `00-introduccion.tex` | `context/libro_latex/chapters/00-introduccion.tex` | LaTeX | Introducción, fundamentación, objetivos y recorrido del libro. | Todas | Declara correctamente `% !TeX root = ../main.tex`. |
| `01-nociones-basicas-introduccion-acustica.tex` | `context/libro_latex/chapters/01-nociones-basicas-introduccion-acustica.tex` | LaTeX | Capítulo editable de nociones básicas e introducción. | U1 | Incluye ejercicios, soluciones y glosario. |
| `02-mecanica-clasica-termodinamica.tex` | `context/libro_latex/chapters/02-mecanica-clasica-termodinamica.tex` | LaTeX | Capítulo editable de mecánica clásica y termodinámica. | U2 | Incluye ejercicios, soluciones y glosario. |
| `03-mecanica-ondulatoria.tex` | `context/libro_latex/chapters/03-mecanica-ondulatoria.tex` | LaTeX | Capítulo editable de mecánica ondulatoria. | U3 | Incluye ejercicios, soluciones y glosario. |
| `04-sonido-propiedades-magnitudes.tex` | `context/libro_latex/chapters/04-sonido-propiedades-magnitudes.tex` | LaTeX | Capítulo editable sobre sonido, propiedades y magnitudes. | U4 | Incluye ejercicios, soluciones y glosario. |
| `05-analisis-frecuencial.tex` | `context/libro_latex/chapters/05-analisis-frecuencial.tex` | LaTeX | Capítulo editable de análisis frecuencial. | U5 | Incluye ejercicios, soluciones y glosario. Mantiene un `TODO` para evaluar una figura original de curvas A, C y Z. |
| `06-percepcion-auditiva.tex` | `context/libro_latex/chapters/06-percepcion-auditiva.tex` | LaTeX | Capítulo editable del mecanismo periférico de la percepción auditiva. | U6 | Incluye ejercicios, soluciones y glosario. El título largo amplía el del programa con “periférico”. |
| `07-psicoacustica.tex` | `context/libro_latex/chapters/07-psicoacustica.tex` | LaTeX | Capítulo editable de psicoacústica. | U7 | Incluye ejercicios, soluciones y glosario. Conserva un comentario con nueve figuras “pendientes de diseño y aprobación”, aunque ya existen nueve TikZ temáticos; debe aclararse el estado de aprobación. |
| `08-enfermedades-diagnostico-rehabilitacion.tex` | `context/libro_latex/chapters/08-enfermedades-diagnostico-rehabilitacion.tex` | LaTeX | Capítulo editable de alteraciones, estudios y rehabilitación. | U8 | Incluye ejercicios, respuestas orientativas y glosario. El título amplía el alcance del programa. |
| `09-propagacion-sonido.tex` | `context/libro_latex/chapters/09-propagacion-sonido.tex` | LaTeX | Capítulo editable sobre propagación. | U9 | Incluye ejercicios, soluciones y glosario. |
| `10-ruido-caracterizacion.tex` | `context/libro_latex/chapters/10-ruido-caracterizacion.tex` | LaTeX | Capítulo editable sobre ruido y caracterización. | U10 | Incluye ejercicios, soluciones y glosario. |
| `references.bib` | `context/libro_latex/bibliography/references.bib` | BibTeX | Bibliografía académica y normativa del libro. | Todas | Contiene 56 entradas; las 56 claves citadas por los capítulos están presentes. |
| `resolve_verify_blocks.py` | `context/libro_latex/scripts/resolve_verify_blocks.py` | Python | Resolución y control de bloques de verificación documental. | Todas | El script documenta la revisión de 199 bloques; no quedan bloques `\verify{...}` activos en los capítulos. |

## Presentaciones de referencia

| Nombre | Ruta | Tipo | Propósito probable | Unidad relacionada | Observaciones |
|---|---|---|---|---|---|
| `Unidad 1 - Nociones básicas e introducción a la acústica.pptx` | `context/referencias_visuales/Unidad 1 - Nociones básicas e introducción a la acústica.pptx` | PowerPoint, 20 slides, 16:9 | Referencia visual primaria creada por el docente. | U1 y estilo global | Autor y último editor: Maximiliano Ortiz. Tiene 1 master, 11 layouts, 22 medios y contenido mayormente editable. No contiene notas del orador ni fuentes incrustadas. |
| `The_Acoustic_Blueprint.pptx` | `context/referencias_visuales/The_Acoustic_Blueprint.pptx` | PowerPoint, 15 slides, 16:9 | Referencia secundaria de composición atribuida a Gemini por `AGENTS.md`. | Estilo global | Cada slide es una única imagen PNG de 1376×768; no hay texto ni formas editables, notas o autor en metadatos. Sirve como referencia visual, no como plantilla editable. El nombre no identifica por sí solo origen, versión ni unidad. |

## Figuras reproducibles generadas por script

| Nombre | Ruta | Tipo | Propósito probable | Unidad relacionada | Observaciones |
|---|---|---|---|---|---|
| `generate_unit5_figures.py` | `context/libro_latex/figures/scripts/unidad-5/generate_unit5_figures.py` | Python | Generar las cuatro figuras cuantitativas de análisis frecuencial. | U5 | Fuente reproducible disponible. |
| `tiempo-magnitud-fase.pdf` | `context/libro_latex/figures/generated/unidad-5/tiempo-magnitud-fase.pdf` | PDF vectorial, 1 página | Comparar tiempo, magnitud y fase. | U5 | Referenciado por el capítulo y presente. |
| `serie-fourier-progresiva.pdf` | `context/libro_latex/figures/generated/unidad-5/serie-fourier-progresiva.pdf` | PDF vectorial, 1 página | Mostrar aproximación progresiva mediante serie de Fourier. | U5 | Referenciado por el capítulo y presente. |
| `compromiso-tiempo-frecuencia.pdf` | `context/libro_latex/figures/generated/unidad-5/compromiso-tiempo-frecuencia.pdf` | PDF vectorial, 1 página | Explicar el compromiso tiempo–frecuencia. | U5 | Referenciado por el capítulo y presente. |
| `filtros-ideales-reales.pdf` | `context/libro_latex/figures/generated/unidad-5/filtros-ideales-reales.pdf` | PDF vectorial, 1 página | Comparar filtros ideales y modelos no ideales. | U5 | Referenciado por el capítulo y presente. |
| `generate_unit10_figures.py` | `context/libro_latex/figures/scripts/unidad-10/generate_unit10_figures.py` | Python | Generar las cuatro figuras cuantitativas sobre ruido. | U10 | Fuente reproducible disponible. |
| `realizaciones-temporales-ruido.pdf` | `context/libro_latex/figures/generated/unidad-10/realizaciones-temporales-ruido.pdf` | PDF vectorial, 1 página | Comparar realizaciones temporales de ruido. | U10 | Referenciado por el capítulo y presente. |
| `estadistica-mismo-rms.pdf` | `context/libro_latex/figures/generated/unidad-10/estadistica-mismo-rms.pdf` | PDF vectorial, 1 página | Comparar señales con igual RMS y diferente estadística. | U10 | Referenciado por el capítulo y presente. |
| `blanco-rosa-energia-bandas.pdf` | `context/libro_latex/figures/generated/unidad-10/blanco-rosa-energia-bandas.pdf` | PDF vectorial, 1 página | Comparar ruido blanco y rosa por banda. | U10 | Referenciado por el capítulo y presente. |
| `relaciones-senal-ruido.pdf` | `context/libro_latex/figures/generated/unidad-10/relaciones-senal-ruido.pdf` | PDF vectorial, 1 página | Mostrar relaciones señal–ruido. | U10 | Referenciado por el capítulo y presente. |

## Figuras TikZ del libro

Todos los archivos de esta sección están referenciados por su capítulo y existen en la ruta esperada.

| Nombre | Ruta | Tipo | Propósito probable | Unidad relacionada | Observaciones |
|---|---|---|---|---|---|
| `fuente-medio-receptor.tex` | `context/libro_latex/figures/tikz/unidad-1/fuente-medio-receptor.tex` | TikZ/LaTeX | Modelo fuente–medio–receptor. | U1 | Editable. |
| `dependencias-dimensionales.tex` | `context/libro_latex/figures/tikz/unidad-1/dependencias-dimensionales.tex` | TikZ/LaTeX | Relaciones entre magnitudes y dimensiones. | U1 | Editable. |
| `funcion-directa-inversa.tex` | `context/libro_latex/figures/tikz/unidad-1/funcion-directa-inversa.tex` | TikZ/LaTeX | Función y función inversa. | U1 | Editable. |
| `circulo-trigonometrico.tex` | `context/libro_latex/figures/tikz/unidad-1/circulo-trigonometrico.tex` | TikZ/LaTeX | Círculo trigonométrico. | U1 | Editable. |
| `escala-lineal-logaritmica.tex` | `context/libro_latex/figures/tikz/unidad-1/escala-lineal-logaritmica.tex` | TikZ/LaTeX | Comparar escalas lineal y logarítmica. | U1 | Editable. |
| `fuerza-sobre-area.tex` | `context/libro_latex/figures/tikz/unidad-2/fuerza-sobre-area.tex` | TikZ/LaTeX | Relación entre fuerza, superficie y presión. | U2 | Editable. |
| `masa-resorte-amortiguador.tex` | `context/libro_latex/figures/tikz/unidad-2/masa-resorte-amortiguador.tex` | TikZ/LaTeX | Modelo masa–resorte–amortiguador. | U2 | Editable. |
| `velocidad-temperatura.tex` | `context/libro_latex/figures/tikz/unidad-2/velocidad-temperatura.tex` | TikZ/LaTeX | Dependencia de velocidad y temperatura. | U2 | Editable. |
| `balance-energia-cadena-auditiva.tex` | `context/libro_latex/figures/tikz/unidad-2/balance-energia-cadena-auditiva.tex` | TikZ/LaTeX | Balance de energía en una cadena auditiva. | U2 | Editable. |
| `oscilacion-propagacion.tex` | `context/libro_latex/figures/tikz/unidad-3/oscilacion-propagacion.tex` | TikZ/LaTeX | Diferenciar oscilación y propagación. | U3 | Editable. |
| `longitudinal-transversal.tex` | `context/libro_latex/figures/tikz/unidad-3/longitudinal-transversal.tex` | TikZ/LaTeX | Comparar ondas longitudinales y transversales. | U3 | Editable. |
| `mas-cinematica.tex` | `context/libro_latex/figures/tikz/unidad-3/mas-cinematica.tex` | TikZ/LaTeX | Cinemática del movimiento armónico simple. | U3 | Editable. |
| `parlante-medio.tex` | `context/libro_latex/figures/tikz/unidad-3/parlante-medio.tex` | TikZ/LaTeX | Relación entre parlante y medio. | U3 | Editable. |
| `onda-tiempo-espacio.tex` | `context/libro_latex/figures/tikz/unidad-3/onda-tiempo-espacio.tex` | TikZ/LaTeX | Representaciones temporal y espacial de una onda. | U3 | Editable. |
| `superposicion-desfase.tex` | `context/libro_latex/figures/tikz/unidad-3/superposicion-desfase.tex` | TikZ/LaTeX | Superposición y desfase. | U3 | Editable. |
| `impedancia-reflexion-interfaz.tex` | `context/libro_latex/figures/tikz/unidad-4/impedancia-reflexion-interfaz.tex` | TikZ/LaTeX | Impedancia y reflexión en una interfaz. | U4 | Editable. |
| `presion-velocidad-intensidad.tex` | `context/libro_latex/figures/tikz/unidad-4/presion-velocidad-intensidad.tex` | TikZ/LaTeX | Relación entre presión, velocidad e intensidad. | U4 | Editable. |
| `rms-sinusoide.tex` | `context/libro_latex/figures/tikz/unidad-4/rms-sinusoide.tex` | TikZ/LaTeX | Valor RMS de una sinusoide. | U4 | Editable. |
| `escala-presion-db-spl.tex` | `context/libro_latex/figures/tikz/unidad-4/escala-presion-db-spl.tex` | TikZ/LaTeX | Presión acústica y dB SPL. | U4 | Editable. |
| `suma-coherente-no-correlacionada.tex` | `context/libro_latex/figures/tikz/unidad-4/suma-coherente-no-correlacionada.tex` | TikZ/LaTeX | Suma coherente y no correlacionada. | U4 | Editable. |
| `propagacion-esferica.tex` | `context/libro_latex/figures/tikz/unidad-4/propagacion-esferica.tex` | TikZ/LaTeX | Propagación esférica y distancia. | U4 | Editable. |
| `directividad-q.tex` | `context/libro_latex/figures/tikz/unidad-4/directividad-q.tex` | TikZ/LaTeX | Directividad y factor Q. | U4 | Editable. |
| `espectro-respuesta-sistema.tex` | `context/libro_latex/figures/tikz/unidad-5/espectro-respuesta-sistema.tex` | TikZ/LaTeX | Espectro y respuesta de un sistema. | U5 | Editable. |
| `componentes-espectrales.tex` | `context/libro_latex/figures/tikz/unidad-5/componentes-espectrales.tex` | TikZ/LaTeX | Armónicos, parciales y componentes espectrales. | U5 | Editable. |
| `bandas-octava-tercio.tex` | `context/libro_latex/figures/tikz/unidad-5/bandas-octava-tercio.tex` | TikZ/LaTeX | Bandas de octava y tercio de octava. | U5 | Editable. |
| `cadena-sonometro.tex` | `context/libro_latex/figures/tikz/unidad-5/cadena-sonometro.tex` | TikZ/LaTeX | Cadena funcional de un sonómetro. | U5 | Editable. |
| `cadena-transduccion.tex` | `context/libro_latex/figures/tikz/unidad-6/cadena-transduccion.tex` | TikZ/LaTeX | Cadena acústico–mecánico–eléctrica. | U6 | Editable. |
| `organizacion-oido-periferico.tex` | `context/libro_latex/figures/tikz/unidad-6/organizacion-oido-periferico.tex` | TikZ/LaTeX | Organización del oído periférico. | U6 | Editable. |
| `adaptacion-oido-medio.tex` | `context/libro_latex/figures/tikz/unidad-6/adaptacion-oido-medio.tex` | TikZ/LaTeX | Adaptación mecánica del oído medio. | U6 | Editable. |
| `conduccion-osea-multimecanismo.tex` | `context/libro_latex/figures/tikz/unidad-6/conduccion-osea-multimecanismo.tex` | TikZ/LaTeX | Mecanismos de conducción ósea. | U6 | Editable. |
| `arquitectura-coclear.tex` | `context/libro_latex/figures/tikz/unidad-6/arquitectura-coclear.tex` | TikZ/LaTeX | Arquitectura coclear. | U6 | Editable. |
| `onda-viajera-tonotopia.tex` | `context/libro_latex/figures/tikz/unidad-6/onda-viajera-tonotopia.tex` | TikZ/LaTeX | Onda viajera y tonotopía. | U6 | Editable. |
| `funciones-cci-cce.tex` | `context/libro_latex/figures/tikz/unidad-6/funciones-cci-cce.tex` | TikZ/LaTeX | Funciones de células ciliadas internas y externas. | U6 | Editable. |
| `umbral-campo-audible.tex` | `context/libro_latex/figures/tikz/unidad-7/umbral-campo-audible.tex` | TikZ/LaTeX | Umbral y campo audible. | U7 | Editable; aparece también en la lista comentada de figuras pendientes. |
| `campo-cae-timpano.tex` | `context/libro_latex/figures/tikz/unidad-7/campo-cae-timpano.tex` | TikZ/LaTeX | Campo libre, CAE y tímpano. | U7 | Editable; estado de aprobación no documentado. |
| `construccion-isofonica.tex` | `context/libro_latex/figures/tikz/unidad-7/construccion-isofonica.tex` | TikZ/LaTeX | Construcción conceptual de curvas isofónicas. | U7 | Editable; el texto advierte que no sustituye datos normalizados. |
| `fones-sones.tex` | `context/libro_latex/figures/tikz/unidad-7/fones-sones.tex` | TikZ/LaTeX | Relación entre fones y sones. | U7 | Editable; estado de aprobación no documentado. |
| `enmascaramiento-erb.tex` | `context/libro_latex/figures/tikz/unidad-7/enmascaramiento-erb.tex` | TikZ/LaTeX | Enmascaramiento y banda rectangular equivalente. | U7 | Editable; estado de aprobación no documentado. |
| `enmascaramiento-temporal.tex` | `context/libro_latex/figures/tikz/unidad-7/enmascaramiento-temporal.tex` | TikZ/LaTeX | Ventana temporal de enmascaramiento. | U7 | Editable; estado de aprobación no documentado. |
| `precedencia-reflexiones.tex` | `context/libro_latex/figures/tikz/unidad-7/precedencia-reflexiones.tex` | TikZ/LaTeX | Señal directa, reflexiones y precedencia. | U7 | Editable; estado de aprobación no documentado. |
| `audicion-espacial.tex` | `context/libro_latex/figures/tikz/unidad-7/audicion-espacial.tex` | TikZ/LaTeX | ITD, ILD y pistas espaciales. | U7 | Editable; estado de aprobación no documentado. |
| `fuentes-concurrentes.tex` | `context/libro_latex/figures/tikz/unidad-7/fuentes-concurrentes.tex` | TikZ/LaTeX | Escena de fuentes concurrentes. | U7 | Editable; estado de aprobación no documentado. |
| `audiograma-conceptual.tex` | `context/libro_latex/figures/tikz/unidad-8/audiograma-conceptual.tex` | TikZ/LaTeX | Audiograma conceptual. | U8 | Editable. |
| `curva-logoaudiometrica-conceptual.tex` | `context/libro_latex/figures/tikz/unidad-8/curva-logoaudiometrica-conceptual.tex` | TikZ/LaTeX | Curva logoaudiométrica conceptual. | U8 | Editable. |
| `timpanogramas-esquematicos.tex` | `context/libro_latex/figures/tikz/unidad-8/timpanogramas-esquematicos.tex` | TikZ/LaTeX | Timpanogramas esquemáticos. | U8 | Editable. |
| `cadenas-oea-peat.tex` | `context/libro_latex/figures/tikz/unidad-8/cadenas-oea-peat.tex` | TikZ/LaTeX | Cadenas funcionales de OEA y PEAT. | U8 | Editable. |
| `cadenas-dispositivos.tex` | `context/libro_latex/figures/tikz/unidad-8/cadenas-dispositivos.tex` | TikZ/LaTeX | Cadenas de audífonos e implantes. | U8 | Editable. |
| `gradientes-termicos.tex` | `context/libro_latex/figures/tikz/unidad-9/gradientes-termicos.tex` | TikZ/LaTeX | Refracción por gradientes térmicos. | U9 | Editable. |
| `gradiente-viento.tex` | `context/libro_latex/figures/tikz/unidad-9/gradiente-viento.tex` | TikZ/LaTeX | Efecto del gradiente de viento. | U9 | Editable. |
| `balance-superficie.tex` | `context/libro_latex/figures/tikz/unidad-9/balance-superficie.tex` | TikZ/LaTeX | Reflexión, absorción y transmisión en superficies. | U9 | Editable. |
| `difraccion-barrera.tex` | `context/libro_latex/figures/tikz/unidad-9/difraccion-barrera.tex` | TikZ/LaTeX | Difracción por barrera. | U9 | Editable. |
| `ley-masas-pared-simple.tex` | `context/libro_latex/figures/tikz/unidad-9/ley-masas-pared-simple.tex` | TikZ/LaTeX | Ley de masas para pared simple. | U9 | Editable. |
| `cabina-sistema.tex` | `context/libro_latex/figures/tikz/unidad-9/cabina-sistema.tex` | TikZ/LaTeX | Cabina como sistema acústico. | U9 | Editable. |
| `conformacion-espectral.tex` | `context/libro_latex/figures/tikz/unidad-10/conformacion-espectral.tex` | TikZ/LaTeX | Conformación espectral del ruido. | U10 | Editable. |
| `enmascaramiento-audiometrico-conceptual.tex` | `context/libro_latex/figures/tikz/unidad-10/enmascaramiento-audiometrico-conceptual.tex` | TikZ/LaTeX | Enmascaramiento audiométrico conceptual. | U10 | Editable. |
| `control-fuente-trayecto-receptor.tex` | `context/libro_latex/figures/tikz/unidad-10/control-fuente-trayecto-receptor.tex` | TikZ/LaTeX | Jerarquía de control en fuente, trayecto y receptor. | U10 | Editable. |

## Imágenes raster heredadas o no vinculadas al LaTeX actual

Ninguno de los 28 archivos de esta sección aparece en una instrucción `\includegraphics` de los capítulos actuales. No son duplicados binarios exactos, pero varios se superponen temáticamente con figuras TikZ o PDF más recientes. No hay manifiesto de procedencia, licencia, autoría, resolución objetivo ni estado de aprobación.

| Nombre | Ruta | Tipo | Propósito probable | Unidad relacionada | Observaciones |
|---|---|---|---|---|---|
| `armonicos.png` | `context/libro_latex/figures/armonicos.png` | PNG | Ilustrar armónicos. | U5 | No referenciado; posible antecedente de figuras espectrales actuales. |
| `atenuacion_atmosferica.png` | `context/libro_latex/figures/atenuacion_atmosferica.png` | PNG | Atenuación atmosférica. | U9 | No referenciado; falta procedencia. |
| `cuadrado_inverso.png` | `context/libro_latex/figures/cuadrado_inverso.png` | PNG | Ley del cuadrado inverso. | U4/U9 | No referenciado; se superpone con `propagacion-esferica.tex`. |
| `densidad_espectro_ruidos.png` | `context/libro_latex/figures/densidad_espectro_ruidos.png` | PNG | Densidad espectral de distintos ruidos. | U10 | No referenciado; se superpone con PDF generado de ruido blanco/rosa. |
| `directividad.png` | `context/libro_latex/figures/directividad.png` | PNG | Directividad de fuentes. | U4/U9 | No referenciado; se superpone con `directividad-q.tex`. |
| `enmascaramiento.png` | `context/libro_latex/figures/enmascaramiento.png` | PNG | Enmascaramiento auditivo. | U7/U10 | No referenciado; se superpone con figuras TikZ actuales. |
| `espectrograma.png` | `context/libro_latex/figures/espectrograma.png` | PNG | Ejemplo de espectrograma. | U5 | No referenciado; es la imagen raster más pesada del grupo. |
| `filtros.png` | `context/libro_latex/figures/filtros.png` | PNG | Tipos o respuestas de filtros. | U5 | No referenciado; se superpone con `filtros-ideales-reales.pdf`. |
| `FletcherMunson.png` | `context/libro_latex/figures/FletcherMunson.png` | PNG | Curvas isofónicas históricas. | U7 | No referenciado; requiere verificación de fuente, edición normativa y licencia. |
| `fourier.png` | `context/libro_latex/figures/fourier.png` | PNG | Síntesis o análisis de Fourier. | U5 | No referenciado; posible antecedente de figuras generadas actuales. |
| `huesecillos.png` | `context/libro_latex/figures/huesecillos.png` | PNG | Anatomía o mecánica de la cadena osicular. | U6 | No referenciado; falta procedencia. |
| `localizacion_fuentes.png` | `context/libro_latex/figures/localizacion_fuentes.png` | PNG | Localización de fuentes. | U7 | No referenciado; se superpone con `audicion-espacial.tex`. |
| `longitudinales_transversales.png` | `context/libro_latex/figures/longitudinales_transversales.png` | PNG | Ondas longitudinales y transversales. | U3 | No referenciado; se superpone con `longitudinal-transversal.tex`. |
| `oido.png` | `context/libro_latex/figures/oido.png` | PNG | Anatomía general del oído. | U6 | No referenciado; falta procedencia y licencia. |
| `ondas_aire_agua.png` | `context/libro_latex/figures/ondas_aire_agua.png` | PNG | Propagación en aire y agua. | U3/U4 | No referenciado; falta procedencia. |
| `ponderacion.jpg` | `context/libro_latex/figures/ponderacion.jpg` | JPEG | Curvas de ponderación. | U5 | No referenciado; puede relacionarse con el `TODO` de curvas A, C y Z, pero su exactitud y origen no están documentados. |
| `presbiacusia.png` | `context/libro_latex/figures/presbiacusia.png` | PNG | Ejemplo o patrón asociado a presbiacusia. | U8 | No referenciado; requiere cautela clínica y fuente explícita. |
| `propagacion_sonido.png` | `context/libro_latex/figures/propagacion_sonido.png` | PNG | Propagación del sonido. | U3/U4/U9 | No referenciado; propósito demasiado amplio. |
| `reflexion_absorcion.png` | `context/libro_latex/figures/reflexion_absorcion.png` | PNG | Reflexión y absorción. | U9 | No referenciado; se superpone con `balance-superficie.tex`. |
| `rta_freq_vocal.png` | `context/libro_latex/figures/rta_freq_vocal.png` | PNG | Respuesta o rango frecuencial vocal. | U5/U7 | No referenciado; abreviatura y fuente ambiguas. |
| `suma_fuentes.jpg` | `context/libro_latex/figures/suma_fuentes.jpg` | JPEG | Suma de fuentes sonoras. | U4 | No referenciado; se superpone con figura de suma actual. |
| `suma_ondas.png` | `context/libro_latex/figures/suma_ondas.png` | PNG | Superposición de ondas. | U3/U4 | No referenciado; se superpone con `superposicion-desfase.tex`. |
| `timpanometria.png` | `context/libro_latex/figures/timpanometria.png` | PNG | Timpanometría. | U8 | No referenciado; se superpone con `timpanogramas-esquematicos.tex`. |
| `tipos_de_onda.jpg` | `context/libro_latex/figures/tipos_de_onda.jpg` | JPEG | Clasificación de ondas. | U3 | No referenciado; falta procedencia. |
| `tono.png` | `context/libro_latex/figures/tono.png` | PNG | Forma temporal de un tono. | U3 | No referenciado; nombre demasiado genérico. |
| `tono_1000.png` | `context/libro_latex/figures/tono_1000.png` | PNG | Tono de 1000 Hz. | U3/U5 | No referenciado; no se documentan amplitud, muestreo ni unidades. |
| `tono_vs_ruido.png` | `context/libro_latex/figures/tono_vs_ruido.png` | PNG | Comparar tono y ruido. | U10 | No referenciado; posible antecedente conceptual. |
| `velocidad_propagacion_sonido.png` | `context/libro_latex/figures/velocidad_propagacion_sonido.png` | PNG | Velocidad de propagación. | U4/U9 | No referenciado; no se documentan medio, condiciones o fuente de datos. |

## Duplicados, faltantes y ambigüedades

### Duplicados

- No se detectaron archivos binariamente idénticos mediante SHA-256.
- El único nombre de archivo repetido es `SKILL.md`, esperado por la estructura modular.
- Hay solapamientos temáticos entre las 28 imágenes raster no referenciadas y figuras TikZ/PDF actuales; no son duplicados exactos y no deben eliminarse sin revisión de procedencia y calidad.
- No se detectaron etiquetas LaTeX duplicadas.

### Faltantes confirmados

- Guía de ejercicios independiente; el libro sí incluye ejercicios y respuestas en cada unidad.
- Evaluaciones, parciales, recuperatorios, rúbricas o banco de preguntas.
- Material adicional mencionado en el programa, como documentos o videos de la plataforma.
- Manifiesto de procedencia/licencia para las 28 imágenes raster heredadas.
- Documentación de versión y aprobación de las figuras pendientes o reemplazadas.
- Notas del orador y registro de fuentes en los dos decks de referencia.

### Ambigüedades

- El programa disponible es de 2025 y el libro es de 2026; debe confirmarse cuál es el programa vigente para el ciclo de producción.
- `The_Acoustic_Blueprint.pptx` es identificado por `AGENTS.md` como referencia de Gemini, pero el archivo no contiene metadatos que confirmen autor, fecha conceptual, unidad ni versión.
- El archivo raíz ya está disponible, pero todavía no se realizó una compilación limpia para confirmar que reproduce el PDF canónico de 296 páginas.
- La Unidad 7 enumera nueve figuras pendientes de aprobación, pero existen y se insertan nueve figuras TikZ relacionadas. Falta decidir si están aprobadas o todavía son borradores.
- La Unidad 5 mantiene pendiente una figura de curvas A, C y Z, mientras existe `ponderacion.jpg` sin procedencia ni vínculo.
- Los títulos LaTeX de las unidades 6 y 8 amplían el enunciado del programa. La ampliación parece pedagógica, pero debe documentarse al comparar cobertura.
- Las imágenes raster no usadas carecen de origen, licencia y estado; su propósito se infiere únicamente por el nombre.
