# Registro de decisiones del sistema visual

## Convenciones

Clasificaciones:

- **Conservar:** el rasgo pasa al nuevo sistema con cambios mínimos.
- **Mejorar:** se mantiene la intención, pero se corrige su ejecución.
- **Reemplazar:** se conserva la función y se cambia la solución visual o técnica.
- **Descartar:** no se incorpora.
- **Caso particular:** se permite solo bajo una condición explícita.

Estados:

- `Adoptada`: decisión vigente para la especificación v1.
- `Validar en template`: decisión adoptada que debe probarse en el futuro `.pptx`.
- `Pendiente de activo`: requiere un archivo institucional o una fuente todavía no verificada.

## Decisiones

| ID | Decisión | Clasificación | Evidencia/origen | Razón | Estado |
|---|---|---|---|---|---|
| D-001 | Usar relación 16:9. | Conservar | Ambos decks. | Adecuada para pantallas y aula. | Adoptada |
| D-002 | Normalizar a 13,333 × 7,5 in. | Mejorar | Docente usa tamaño estándar; Gemini usa 17,778 × 10 in. | Evita escalas físicas inusuales y facilita compatibilidad. | Adoptada |
| D-003 | Tomar el deck docente como referencia identitaria principal. | Conservar | `AGENTS.md` y auditoría. | Tiene tono académico, institucional y humano. | Adoptada |
| D-004 | Usar Gemini solo como referencia de organización. | Caso particular | Slides Gemini 2, 3, 4, 6, 7, 10, 13 y 15. | Sus estructuras ayudan; su implementación es raster y automática. | Adoptada |
| D-005 | No reutilizar imágenes full-slide de Gemini. | Descartar | Las 15 slides son un único bitmap. | No hay editabilidad, accesibilidad ni control de corrección. | Adoptada |
| D-006 | Mantener un master claro y uno bordó. | Mejorar | El docente tiene un solo master y furniture inconsistente. | Separa contenido de transiciones sin overlays. | Validar en template |
| D-007 | Conservar la regla superior segmentada, reducida. | Mejorar | Firma visible del deck docente. | Aporta identidad sin consumir altura. | Validar en template |
| D-008 | Reservar la banda bordó completa para transiciones. | Mejorar | La banda docente domina todas las slides. | Libera espacio y reduce monotonía. | Adoptada |
| D-009 | Usar `#4D1434` como bordó principal. | Conservar | Tema “Dividendo” y renders docentes. | Es el ancla más reconocible de la referencia. | Adoptada |
| D-010 | Mantener `#903163`, `#969FA7` y `#3D3D3D` como secundarios. | Conservar | Tema docente. | Dan continuidad con la referencia. | Adoptada |
| D-011 | Incorporar teal y ocre apagados con semántica físico/perceptual. | Caso particular | Organización de Gemini. | Mejora comparaciones sin adoptar estética neón. | Validar en template |
| D-012 | Usar fondo blanco y marfil claro; eliminar cuadrícula general. | Reemplazar/descartar | Blanco docente y grid Gemini. | Mejora sobriedad, contraste y continuidad en decks largos. | Adoptada |
| D-013 | Usar Calibri Light, Calibri y Cambria Math. | Reemplazar | Tema docente declara Gill Sans MT no instalada; aparecen sustituciones. | Fuentes disponibles, legibles y compatibles con ecuaciones. | Validar en template |
| D-014 | Título habitual de 36 pt y cuerpo de 22–24 pt. | Mejorar | Docente oscila entre 16 y 48 pt; Gemini mezcla escalas dentro de imágenes. | Asegura lectura desde aula. | Validar en template |
| D-015 | No reducir cuerpo por debajo de 20 pt. | Reemplazar | Densidad en ambos decks. | La solución al exceso es editar o dividir. | Adoptada |
| D-016 | Alinear títulos a la izquierda por defecto. | Mejorar | El docente alterna centrado e izquierda; Gemini centra muchos títulos. | Mejora continuidad y velocidad de lectura. | Adoptada |
| D-017 | Permitir título de dos líneas solo en placeholder específico. | Mejorar | Docente slides 13–15. | Evita wrapping accidental y bandas demasiado altas. | Validar en template |
| D-018 | Usar margen horizontal seguro de 0,67 in. | Mejorar | Márgenes variables en ambos decks. | Crea consistencia sin desperdiciar espacio. | Adoptada |
| D-019 | Mantener número de slide automático. | Mejorar | Docente usa `n/20`; Gemini no numera. | Orienta en unidades extensas. | Validar en template |
| D-020 | No mostrar total de slides por defecto. | Mejorar | El total manual del docente puede quedar obsoleto. | Reduce mantenimiento y errores. | Adoptada |
| D-021 | Mantener presencia UCASAL discreta en el pie. | Mejorar | Logo grande o ausente en slides docentes; NotebookLM en Gemini. | Conserva identidad sin competir con el contenido. | Pendiente de activo |
| D-022 | Eliminar placeholder de fecha y cualquier footer vacío. | Reemplazar | Master docente contiene fecha y pie vacíos. | Evita prompts o metadatos accidentales. | Validar en template |
| D-023 | Conservar ecuaciones OMML y normalizarlas con Cambria Math. | Conservar/mejorar | 39 ecuaciones nativas en el deck docente. | Editabilidad y precisión. | Adoptada |
| D-024 | Toda ecuación debe definir símbolos y unidades. | Mejorar | Variación en slides docentes 9–19. | Atiende el nivel de primer año y consistencia dimensional. | Adoptada |
| D-025 | Rehacer gráficos como SVG reproducible o chart nativo. | Reemplazar | Gráficos externos en slides docentes 12, 15, 17–19; raster en Gemini. | Permite corregir etiquetas, escalas y estilos. | Adoptada |
| D-026 | Construir tablas como objetos nativos. | Reemplazar | Tabla raster de prefijos, slide docente 8. | Mejora legibilidad y editabilidad. | Adoptada |
| D-027 | No usar una slide completa como imagen. | Descartar | Estructura completa del deck Gemini. | Bloquea edición, accesibilidad y corrección. | Adoptada |
| D-028 | Priorizar diagramas propios y fotografías técnicas. | Mejorar | Assets heterogéneos del docente y visuales automáticos de Gemini. | Alinea recursos con la función pedagógica. | Adoptada |
| D-029 | No usar memes por defecto. | Caso particular | Slide docente 16. | Pueden romper tono, envejecer y requerir contexto/licencia. | Adoptada |
| D-030 | No usar stock conceptual, pseudo-3D, glows ni iconos repetidos. | Descartar | Señales recurrentes en Gemini. | Evita apariencia automática y decoración irrelevante. | Adoptada |
| D-031 | Usar títulos descriptivos y naturales. | Reemplazar | Títulos publicitarios de Gemini y algunos títulos temáticos largos del docente. | Mantiene voz docente y precisión. | Adoptada |
| D-032 | Limitar el texto visible a rangos según tipo de slide. | Mejorar | Densidad en slides docentes 4–7, 11, 13–14 y Gemini 12–14. | Evita depender de fuente pequeña. | Adoptada |
| D-033 | Crear un catálogo de layouts por función pedagógica. | Mejorar | Docente usa solo 2 layouts; Gemini varía infografías sin objetos editables. | Permite variedad controlada en 30–50+ slides. | Adoptada |
| D-034 | Incluir layouts específicos para definición, ecuación, ejemplo, comparación, proceso, clínica, pregunta y recapitulación. | Reemplazar | Necesidades del curso y buenas estructuras de ambas referencias. | Reduce improvisación y repetición. | Adoptada |
| D-035 | Usar pocos componentes con semántica estable. | Reemplazar | Exceso de cajas y tarjetas en Gemini. | Conserva consistencia sin look de interfaz. | Adoptada |
| D-036 | Un error frecuente por slide. | Mejorar | Gemini slide 14 acumula tres. | Facilita discusión y lectura desde aula. | Adoptada |
| D-037 | Integrar aplicaciones clínicas específicas. | Conservar/mejorar | Docente slides 4–5; Gemini slides 2, 8, 13–14. | Es central para la audiencia. | Adoptada |
| D-038 | Cerrar con recapitulación y puente, no solo “Muchas gracias”. | Reemplazar | Docente slide 20; Gemini slide 15. | Convierte el cierre en aprendizaje y continuidad. | Adoptada |
| D-039 | Exigir texto alternativo y orden de lectura. | Reemplazar | Docente tiene cobertura parcial; Gemini no tiene. | Accesibilidad y calidad editorial. | Validar en template |
| D-040 | Registrar créditos visibles y bloques `[Sources]` en notas. | Mejorar | Fuentes no sistemáticas en referencias. | Trazabilidad académica. | Validar en template |
| D-041 | Probar cada layout con contenido real y render completo. | Mejorar | Inconsistencias visibles en layouts docentes. | Evita furniture ausente, clipping y auto-fit. | Validar en template |
| D-042 | Validar la versión 1 del template con una unidad de al menos 30 slides. | Mejorar | Requisito de escalabilidad del proyecto. | Comprueba ritmo, flexibilidad y mantenimiento. | Validada con U1–U4; incluye decks de más de 100 slides |
| D-043 | Implementar dos Slide Masters reales y 27 layouts reales. | Mejorar | Template v01 y requisitos mínimos. | Asegura reutilización, variedad controlada y mantenimiento en decks extensos. | Validada en template |
| D-044 | Añadir layouts propios para conocimientos previos, dos columnas y mini ejercicio. | Mejorar | Funciones pedagógicas solicitadas que no quedaban diferenciadas en el catálogo inicial. | Evita variantes manuales y mantiene intención didáctica explícita. | Validada en template |
| D-045 | Usar placeholders reales con relleno y línea transparentes. | Mejorar | Primer render del template. | Conserva estructura y editabilidad sin cubrir el contenido de demostración. | Validada en template |
| D-046 | Ubicar número dinámico en todos los layouts y no como objeto manual. | Mejorar | Revisión estructural y visual. | Evita errores al insertar, borrar o reordenar slides. | Validada en template |
| D-047 | Reutilizar provisionalmente el logo presente en el deck docente. | Caso particular | Presentación original del docente. | Mantiene continuidad institucional hasta recibir un activo vectorial oficial. | Adoptada con reemplazo pendiente |
| D-048 | Mostrar fórmulas de ejemplo como texto editable en Cambria Math y reservar OMML para ecuaciones estructuradas de las unidades. | Caso particular | Compatibilidad y prueba del template v01. | Evita rasterizar; permite edición inmediata sin renunciar a ecuaciones nativas posteriores. | Validada en template |
| D-049 | Preservar GIF como multimedia embebida y aceptar que el preview muestre su primer cuadro. | Conservar | Recurso del deck docente y comportamiento del render de PowerPoint. | Mantiene la demostración animada en clase y una vista previa estable. | Validada en template |
| D-050 | Ensamblar masters y layouts con la API nativa de PowerPoint tras generar el contenido editable con artifact-tool. | Reemplazar | Limitación verificada del exportador disponible al serializar masters/layouts nuevos. | Entrega jerarquía real sin aplanar objetos ni renunciar a editabilidad. | Validada en template |
| D-051 | Incorporar texto alternativo en logos, imágenes y multimedia del template. | Mejorar | Revisión de accesibilidad posterior a la exportación. | Preserva contexto y función pedagógica de los recursos visuales. | Validada en template |
| D-052 | Usar `ΣF` como suma formal y admitir `F_neta` como rótulo didáctico; calificar símbolos que colisionan mediante `F_pres`, `F_el`, `F_amort`, `k_s`, `Q_calor`, `W_trab`, `W_sobre` y `S_ent`. | Mejorar | Comparación de las Unidades 1 y 2 con el mapa del curso y la guía de notación. | Evita colisiones entre mecánica, termodinámica, ondas y acústica sin ocultar el significado físico. Los subíndices deben verse tipográficamente en el material final; el guion bajo queda para fuentes editables o limitaciones documentadas. | Adoptada tras validar la Unidad 2 |
| D-053 | Promover `style/glossary.md` y `style/notation_guide.md` como referencias canónicas después de comparar las dos primeras unidades terminadas. | Mejorar | Pendientes de consistencia registrados en U1 y U2; coincidencia comprobada en términos, unidades y colisiones de símbolos. | Evita que unidades futuras dependan de borradores divergentes. Los antiguos archivos `_draft.md` quedan solo como enlaces de compatibilidad. | Adoptada tras validar las Unidades 1 y 2 |
| D-054 | Preferir “rapidez de propagación” para el escalar `c` cuando se contraste con velocidades locales o vectoriales; admitir “velocidad de propagación” como uso acústico convencional sin ambigüedad. | Mejorar | U1 distingue rapidez, velocidad y propagación; U2 alterna ambas expresiones; U3 usa `u` frente a `c` como referentes distintos. | Conserva precisión física sin prohibir una expresión extendida en la bibliografía acústica. | Adoptada tras validar la Unidad 3 |
| D-055 | Admitir `ξ(x,t)` como variable genérica en U3 y exigir una variable física específica desde su formalización posterior. | Caso particular | U3 necesita separar forma matemática, desplazamiento, presión y tensión antes de que U4 formalice magnitudes acústicas. | Evita identificar una sinusoide con una única magnitud y conserva continuidad hacia `p(x,t)` y `u(x,t)`. | Adoptada tras validar la Unidad 3 |
| D-056 | Para recursos propios, usar un único caption funcional y registrar autoría, validación y reproducibilidad en notas y manifiesto; no repetir etiquetas de producción ni avisos como “no está a escala”. | Mejorar | En U3, 56 slides repiten el aviso “no está a escala” dentro de la misma diapositiva; U1 y U2 usan captions más selectivos. | Reduce ruido editorial y preserva la función pedagógica del caption sin perder trazabilidad. | Adoptada; retrocorrecciones de U3 y U4 pendientes |
| D-057 | Adoptar `W_ac` como símbolo transversal de potencia acústica y reservar `P_ac` para citas o fuentes externas cuya notación deba conservarse. | Mejorar | U2 ya usa `P` para potencia mecánica; U4 formaliza potencia acústica y adopta `W_ac` de manera sistemática. | Evita alternancias dentro del curso y mantiene visible la diferencia entre potencia mecánica genérica, potencia acústica y la unidad watt. | Adoptada tras validar la Unidad 4 |
| D-058 | Reservar `K_s` para módulo volumétrico adiabático, `i(t)` para intensidad acústica instantánea, `I` para su promedio temporal y `Z_0` para la impedancia característica del caso ideal. | Mejorar | U4 introduce estas magnitudes y revela colisiones o ambigüedades no resueltas por la guía previa. | Conserva la distinción entre `K_s` y la constante elástica `k_s`, entre intensidad instantánea y media, y entre impedancia general y el caso de onda plana progresiva ideal. | Adoptada tras validar la Unidad 4 |
| D-059 | Usar `R_p` para el coeficiente de reflexión de presión y `R_I` para la razón de intensidades reflejada/incidente; reservar `R_E` para una fracción energética genérica explícitamente definida. | Mejorar | U4 necesita distinguir signo o fase de la amplitud reflejada de la fracción media de flujo reflejado; U9 reutilizará balances energéticos. | Evita tratar una amplitud como energía y permite conservar la notación del libro sin dejar `R` ambiguo. La relación `R_I=|R_p|²` se limita al caso ideal cuyas condiciones se declaran. | Adoptada en el cierre de la Unidad 4 |
| D-060 | Separar de forma estable `espectro`/`respuesta en frecuencia`, DFT/FFT/gráfico, bin/banda y filtro/ponderación. | Mejorar | U5 muestra que estas parejas concentran errores de interpretación y reaparecen en voz, audífonos, medición y ruido. | Mantiene claro qué pertenece a la señal, al algoritmo, al sistema o al procedimiento de medición y evita convertir términos próximos en sinónimos. | Adoptada tras revisar la Unidad 5 |
| D-061 | Adoptar `x_w(t)`, `f_k`, `φ_H(f)`, `τ_d`, `G(f)` y `L_B` como notación transversal del análisis frecuencial. | Mejorar | U5 introduce ventanas, DFT, fase de sistema, ganancia y niveles por banda; `τ` colisionará con transmisión en U9. | Fija subíndices y calificadores antes de reutilizar los conceptos en U6–U10. FFT se mantiene como nombre de algoritmo, sin un símbolo matemático propio. | Adoptada tras revisar la Unidad 5 |
| D-062 | Permitir en U5 más gráficos, separadores y recapitulaciones que en U1–U3, pero no convertir sus tarjetas repetidas ni su paleta original azul–verde–violeta en una variante global. | Caso particular | U5 tiene 150 slides y una carga cognitiva alta; `AGENTS.md` exige bloques cortos en U4–U7. | Preserva la diferencia pedagógica justificada sin confundirla con una autorización para cambiar la identidad visual del curso. La versión final recupera carbón, bordó, teal y ocre. | Adoptada tras revisar y corregir la Unidad 5 |

## Decisiones explícitamente no tomadas todavía

1. El template usa provisionalmente el logo del deck docente; debe verificarse y reemplazarse por el activo vectorial institucional oficial.
2. No se definieron animaciones específicas de una unidad.
3. No se aprobaron assets finales ni fuentes externas para las unidades.
4. Sigue pendiente decidir el umbral entre ecuaciones OMML, texto matemático editable y SVG/PNG cuando una familia completa de diagramas no pueda mantenerse nativa sin perder legibilidad.

## Criterio para modificar una decisión

Una decisión cambia solo si:

- una prueba renderizada demuestra un problema;
- una restricción institucional lo exige;
- una unidad real muestra que el layout no soporta el contenido;
- una revisión pedagógica identifica una barrera;
- una decisión nueva mejora legibilidad o editabilidad sin diluir identidad.

Toda modificación debe registrar:

- ID nuevo o referencia al ID modificado;
- motivo;
- evidencia;
- archivos afectados;
- fecha;
- estado de validación.
