# Revisión integral y corrección — Unidad 09

Fecha de cierre: 2026-08-12
Deck de entrada: `output/unidad_09_propagacion_sonido_v01.pptx`
Deck corregido: `output/unidad_09_propagacion_sonido_v02.pptx`
Render final: `output/unidad_09_propagacion_sonido_v02/` (96 PNG)

## Dictamen

La versión v02 queda **aprobada para revisión docente**.

- Problemas críticos abiertos: **0**.
- Problemas mayores abiertos: **0**.
- Problemas menores abiertos: **1** (audio opcional no disponible).
- Sugerencias/documentación pendiente: **3**.
- Diapositivas revisadas visualmente: **96/96 en v01 y 96/96 en v02**.
- Diapositivas corregidas con revisión ampliada posterior: 8, 25, 27, 30, 37–39, 41, 44, 50–52, 54–55, 59, 63, 65–66, 70, 73, 76 y 86–96.

No se conservaron diapositivas de “estado bloqueado” visibles para el alumnado. Cuando falta una fuente cuantitativa completa, la v02 presenta una explicación cualitativa útil y declara los datos necesarios para calcular o aplicar un criterio sin inventar cifras.

## Cobertura del programa y correspondencia con el libro

| Tema obligatorio | Slides v02 | Correspondencia principal | Resultado |
|---|---:|---|---|
| Distancia y divergencia | 13–16, 21, 85, 87 | Libro 9.4; ejercicios del capítulo | Cubierto con ecuación, hipótesis y ejercicios resueltos. |
| Fuentes direccionales | 17–21, 87 | Libro 9.4 | Cubierto con `Q`, `DI`, patrón por frecuencia y aplicación. |
| Temperatura y rapidez | 22–25 | Libro 9.5 | Cubierto con gráfico, ecuación y ejemplo. |
| Viento: velocidad, dirección y gradiente | 26–27, 31–33 | Libro 9.5 | Cubierto; se distingue viento uniforme de gradiente. |
| Presión, densidad, humedad y absorción atmosférica | 28–30, 88 | Libro 9.5 | Cubierto cualitativamente y con variables declaradas; sin curva numérica no trazable. |
| Reflexión, absorción y transmisión | 34–41, 46, 58–60, 90 | Libro 9.6–9.7 | Cubierto con balance energético, definiciones y problemas. |
| Refracción en atmósfera y sólidos | 25–27, 40–41, 89 | Libro 9.5–9.6 | Cubierto cualitativamente; no se agregaron ecuaciones modales no documentadas. |
| Difracción y longitud de onda | 42–45 | Libro 9.6 | Cubierto con comparación 125/500/4000 Hz. |
| Recintos, absorción equivalente y Sabine | 47–56, 86, 90–91 | Libro 9.7 | Cubierto con definiciones, unidades y ejemplos completos. |
| Aislamiento, insonorización y ley de masas | 57–67 | Libro 9.7 | Cubierto con relación `τ–R`, tendencia relativa y límites del modelo. |
| Cabinas sonoamortiguadas y verificación | 68–77, 81, 92–95 | Libro 9.8 | Cubierto como sistema: envolvente, sellos, ventilación, bandas y protocolo. |
| Ruido máximo admisible para audiometría | 72–75, 92 | Programa p. 5; cierre documental del libro p. 259 | Cobertura conceptual completa. No se reproducen cifras porque el material fuente no contiene la norma completa, vigente y contextualizada. |

No se detectaron contradicciones con el capítulo 9. Las fórmulas utilizadas tienen símbolos, unidades e interpretación; los resultados numéricos revisados coinciden con los ejercicios del libro.

## Hallazgos y correcciones

| ID | Slide(s) | Dimensión | Severidad | Hallazgo en v01 | Corrección en v02 | Estado |
|---|---:|---|---|---|---|---|
| REV-U09-001 | 52 | Contenido/pedagogía | **critical** | La slide se presentaba como “ejemplo resuelto”, pero solo mostraba rótulos de proceso; faltaban cálculo y resultado. | Se incorporaron `V = 144 m³`, `S = 180 m²`, `Aₑq = 45 m² sabin`, `T₆₀ ≈ 0,52 s` e interpretación. | Resuelto |
| REV-U09-002 | Todas las claras | Producción/diseño | **major** | El pie añadido sobre el master se superponía al logo UCASAL y simulaba un logo duplicado. | Se eliminó el pie redundante y se conservó el pie del master. | Resuelto |
| REV-U09-003 | 30, 38, 40, 44 y otros títulos largos | Diseño | **major** | Primer carácter recortado o excesivamente próximo al borde. | Se desplazó el título, se redujo el ancho útil y se aplicó tamaño adaptativo a títulos largos. | Resuelto |
| REV-U09-004 | 37 | Diagramas | **major** | Texto fuera de caja y cálculo incompleto. | Se reconstruyó el ejercicio con tres cajas de 23–25 pt y comprobación explícita; no hay overflow. | Resuelto |
| REV-U09-005 | 14, 19, 26, 28, 50–52, 58–64 | Contenido/diseño | **major** | Subíndices escritos como `_`, `log10` ambiguo y variables poco legibles. | Se normalizó la notación con subíndices Unicode, `log₁₀`, unidades y separación entre símbolos. | Resuelto |
| REV-U09-006 | 8, 25, 27, 30 | Pedagogía/naturalidad | **major** | Diagramas de tarjetas mostraban categorías de producción, no relaciones físicas suficientes. | Se reemplazaron por comparaciones fuente–trayecto–receptor, gradientes y mecanismos diferenciados. | Resuelto |
| REV-U09-007 | 38–39 | Contenido/naturalidad | **major** | Callouts incompletos y código interno de asset visible. | Se reescribieron definiciones completas de reflexión, eco y reverberación; se retiraron códigos editoriales. | Resuelto |
| REV-U09-008 | 41 | Contenido/producción | **major** | Mensaje de “fuente pendiente” visible, sin valor didáctico para el alumnado. | Se convirtió en ampliación cualitativa sobre rapidez, normal y dirección; se aclaró el límite del modelo. | Resuelto |
| REV-U09-009 | 44 | Pedagogía | **major** | La comparación prometía tres frecuencias, pero no mostraba sus longitudes de onda ni consecuencias. | Se agregaron 125, 500 y 4000 Hz con `λ` y lectura de difracción. | Resuelto |
| REV-U09-010 | 50–51 | Diagramas/ecuaciones | **major** | Etiquetas incompletas, ecuaciones poco jerarquizadas y grandes áreas vacías. | Se reconstruyeron `Aₑq` y Sabine con ecuación central, variables, unidades y conclusión. | Resuelto |
| REV-U09-011 | 54–55 | Pedagogía/producción | **major** | Acondicionamiento y aislamiento quedaban en rótulos genéricos; el recurso multimedia no tenía una alternativa autosuficiente. | Se incorporó comparación conceptual y actividad estática de habla seca/reverberada. | Resuelto |
| REV-U09-012 | 59 | Diseño/gráfico | **major** | El gráfico tenía anotación recortada y exceso de elementos pequeños. | Se reemplazó por una relación logarítmica editable y tres valores de referencia. | Resuelto |
| REV-U09-013 | 63, 65 | Contenido/naturalidad | **major** | Mensajes editoriales sobre convención pendiente y “gráfico conceptual” sin gráfico. | Se dejó la relación relativa segura de ley de masas y una comparación clara de tres regiones. | Resuelto |
| REV-U09-014 | 66, 70 | Diagramas/pedagogía | **major** | La pared con puerta débil y la cabina aparecían como tarjetas sin estructura sistémica suficiente. | Se explicitó la vía dominante y se construyó un diagrama editable con conectores y seis componentes de cabina. | Resuelto |
| REV-U09-015 | 73 | Diseño/gráfico | **major** | Comparación global/bandas congestionada, con ejes y rótulos difíciles de leer en aula. | Se reemplazó por comparación directa de qué resume y qué oculta cada descriptor. | Resuelto |
| REV-U09-016 | 76 | Producción/naturalidad | **major** | La slide prometía una fotografía inexistente y mostraba instrucciones de producción. | Se convirtió en checklist funcional de cierre, servicios y estructura. | Resuelto |
| REV-U09-017 | 86–87 | Contenido | **major** | La tabla de símbolos y los ejercicios anunciados no estaban desarrollados. | Se agregó tabla real de seis magnitudes y dos ejercicios resueltos de distancia/directividad. | Resuelto |
| REV-U09-018 | 88–89 | Contenido/producción | **major** | Pantallas de “material bloqueado” sin desarrollo conceptual. | Se incorporaron dependencias de absorción atmosférica y comparación de modos longitudinal/transversal. | Resuelto |
| REV-U09-019 | 90 | Contenido | **major** | “Solución extendida” sin soluciones. | Se incluyeron los problemas resueltos de balance y Sabine. | Resuelto |
| REV-U09-020 | 92 | Contenido/naturalidad | **major** | Estado bloqueado e instrucciones editoriales visibles. | Se organizó una guía académica de norma, condición de medida y criterio audiométrico, sin cifras inventadas. | Resuelto |
| REV-U09-021 | 93–95 | Contenido/pedagogía | **major** | Tabla, banco de errores y resolución integradora anunciados pero ausentes. | Se agregaron comparación de campos, doce afirmaciones discutibles y matriz fuente–trayecto–receptor. | Resuelto |
| REV-U09-022 | 96 | Fuentes | **major** | La bibliografía era una instrucción genérica, no una lista trazable. | Se incorporaron programa, libro, LaTeX, guía del proyecto e identificadores ISO a verificar. | Resuelto |
| REV-U09-023 | Diversas | Diseño/naturalidad | **major** | Repetición de tarjetas genéricas y rótulos propios de una etapa de storyboard. | Se introdujeron ejemplos, tablas, ecuaciones, comparaciones y diagramas sistémicos en las slides afectadas. | Resuelto |
| REV-U09-024 | Captions | Producción | **minor** | Algunos captions terminaban con elipsis y ocultaban el identificador del asset. | Se acortó el texto preservando siempre ID y crédito UCASAL. | Resuelto |
| REV-U09-025 | 55 | Multimedia | **minor** | `U09-MEDIA-001` no tiene archivo local aprobado. | La slide es autosuficiente sin audio y las notas indican cómo usarlo si se incorpora. | **Abierto** |
| REV-U09-026 | Todas | Accesibilidad | **major** | Era necesario confirmar notas y texto alternativo después de reconstruir los visuales. | Las 96 slides conservan notas; el objeto visual representativo recibe descripción OOXML y las notas incluyen alt text. | Resuelto |

## Revisión específica de diagramas y esquemas

- No quedan flechas sobre texto o fórmulas.
- No quedan puntas dentro del área tipográfica de una caja.
- No quedan conectores atravesando cajas ajenas ni etiquetas apoyadas sobre líneas.
- No quedan textos fuera de caja ni auto-shrink utilizado como solución.
- Los diagramas corregidos usan 22 pt o más en nodos principales; las ecuaciones centrales usan 28 pt o más.
- El diagrama de cabina (slide 70) se revisó nuevamente dentro de la slide final: los conectores terminan en los bordes y permanecen detrás de las cajas.
- El ejercicio de balance (slide 37), que tenía desborde en v01, quedó sin clipping y con margen interno suficiente.

## Producción

- Formato: 16:9.
- Slides: 96.
- Notas del orador: 96/96.
- Masters: 2; layouts: 27.
- Elementos: texto, formas, conectores y tablas editables; gráficos SVG no aplanan la slide completa.
- Numeración: 1–96, consistente.
- Relaciones externas rotas: no detectadas.
- Archivo v02: 537.155 bytes.
- SHA-256: `4CBBBE5B68A7229DA8D22AACB333E71F3988A04C3E67BA6962382803F83F374B`.

## Verificación final

- Render final: 96/96 PNG generados después de la última corrección.
- Inspección visual: mosaicos completos y ampliación individual de todas las slides afectadas.
- `slides_test.py`: aprobado, sin contenido fuera del lienzo.
- `u09_validate_final_deck.py`: `status: pass`, 0 critical, 0 major.
- Archivo PowerPoint: abre, exporta y conserva 96 slides, 96 notas, 2 masters y 27 layouts.

## Problemas abiertos y límites documentales

1. **Minor — audio opcional:** falta el archivo aprobado de `U09-MEDIA-001`; la slide 55 funciona sin él.
2. **Suggestion — límites audiométricos:** para añadir cifras a la slide 92 debe incorporarse la norma completa, edición vigente, adopción local, vía, transductor, bandas y escenario de prueba. No se debe completar desde memoria.
3. **Suggestion — absorción atmosférica cuantitativa:** una curva por bandas requiere fuente primaria y condiciones de temperatura, humedad, presión y distancia.
4. **Suggestion — conversión modal:** cualquier relación angular o ecuación elástica adicional debe basarse en una fuente académica primaria explícita.

Ninguno de estos puntos abiertos es crítico ni mayor en la v02: el contenido obligatorio está cubierto de forma cualitativa y las limitaciones se explican sin presentar datos no trazables.

## Cierre de la versión final

- Archivo de producción: `output/unidad_09_propagacion_sonido_final.pptx`; copia publicada idéntica en `../../output/unidad_09_propagacion_sonido_final.pptx`.
- Derivación: corrección localizada de v02; v01 y v02 se conservaron sin sobrescritura.
- Render final: 96/96 PNG.
- PDF de revisión: 96 páginas.
- Notas: 96/96, todas con marcador `[Sources]`.
- Accesibilidad: 4/4 imágenes con texto alternativo OOXML; los diagramas nativos conservan descripción en notas.
- Consistencia: normalización de `Rₑ`/`τₑ`, retiro de 51 códigos internos visibles y limpieza de 84 campos de notas sin acción.
- Numeración: 96 números visibles y editables. Se conservaron porque el campo dinámico del layout no se visualiza en el render de las slides importadas; no hay duplicación visual.
- Enlaces externos: 0; enlaces rotos detectados: 0.
- Multimedia embebida: 0. `U09-MEDIA-001` permanece opcional y la slide 55 es autosuficiente.
- `slides_test.py`: aprobado, sin overflow.
- `u09_validate_final_deck.py`: `status: pass`, 0 critical, 0 major.
- Inspección visual: mosaico de las 96 slides y ampliación individual de las slides 37, 58, 59, 86 y 90 después de la última corrección visible.
- Tamaño del PPTX final: 528.448 bytes.
- SHA-256 PPTX: `0071FA5B817A01284F8891B1D70D9152C37CF7CCA5EEBA69197099683F64A8FA`.

**Dictamen final:** 0 problemas críticos y 0 problemas mayores. La única incidencia abierta es menor y opcional (`U09-MEDIA-001`); no impide el dictado ni la definición de terminado.
