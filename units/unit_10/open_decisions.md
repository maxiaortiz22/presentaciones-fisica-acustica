# Unidad 10 — Decisiones abiertas

## Propósito

Este registro reúne decisiones que afectan alcance, secuencia, notación, fuentes, recursos, seguridad y tiempo. No constituye un storyboard. Las decisiones de prioridad alta deben resolverse antes de aprobar una secuencia slide por slide.

## Decisiones adoptadas en esta etapa

| ID | Decisión | Justificación |
|---|---|---|
| DA-U10-01 | No crear storyboard, texto de slides, notas ni PowerPoint. | Solicitud explícita y flujo del repositorio. |
| DA-U10-02 | Usar `units/unit_10/` como carpeta normalizada. | Convención de `AGENTS.md`; `[10]` se interpretó como marcador. |
| DA-U10-03 | Priorizar el alcance del programa y distinguir ampliaciones. | Jerarquía de fuentes. |
| DA-U10-04 | Tratar U10 como carga alta, con estadística y espectro en carga muy alta. | Arquitectura, prerrequisitos y densidad del capítulo. |
| DA-U10-05 | Usar el caso del consultorio junto a una avenida como hilo conductor preliminar. | Integra tarea, medición, comunicación, cabina y control. |
| DA-U10-06 | Usar “ruido con espectro de habla” como término preferido y vincularlo con “ruido vocal”. | Glosario y curso. |
| DA-U10-07 | Cubrir enmascaramiento de manera funcional, no como receta clínica. | El libro no contiene protocolo completo. |
| DA-U10-08 | Considerar LaTeX y PDF concordantes. | Lectura completa y verificación visual de PDF 261–290. |
| DA-U10-09 | Adoptar la guía transversal de notación para el futuro deck. | Evita colisiones y mantiene continuidad. |
| DA-U10-10 | Tratar figuras y TikZ del libro como fuentes conceptuales, no assets finales. | Su tipografía y geometría corresponden a página impresa. |
| DA-U10-11 | No incorporar límites normativos ni fuentes externas nuevas en esta etapa. | No son necesarios para el brief y requieren verificación específica. |
| DA-U10-12 | No modificar mapas globales ni matriz en esta entrega. | El pedido limita las salidas a cuatro documentos de U10. |

## Decisiones pendientes

| ID | Prioridad | Decisión | Evidencia o tensión | Recomendación preliminar | Estado |
|---|---|---|---|---|---|
| OD-U10-01 | Alta | Confirmar cantidad y duración de encuentros. | Se estiman 65–90 slides con complemento y respaldo. | Dos encuentros largos o tres con práctica distribuida. | Pendiente docente. |
| OD-U10-02 | Alta | Definir el título visible. | Programa: “Ruidos”; pedido/libro: “El ruido y su caracterización”. | Usar el título solicitado y conservar el oficial en metadatos. | Pendiente editorial. |
| OD-U10-03 | Alta | Definir profundidad del repaso de U4/U5. | RMS, niveles, bandas y `L_eq` son prerrequisitos, pero no pueden asumirse dominados. | Recuperación diagnóstica breve; no repetir derivaciones completas. | Pendiente para storyboard. |
| OD-U10-04 | Alta | Fijar profundidad estadística. | Media, RMS, varianza y distribución sostienen “aleatorio”, pero pueden sobrecargar. | Mantener interpretación y un cálculo; inferencia y probabilidad formal fuera. | Recomendación preliminar. |
| OD-U10-05 | Alta | Decidir si la identidad `p_rms²=σ_p²+p̄²` es central. | Es útil contra errores, pero suma formalismo. | Central si se trabaja el ejemplo constante; si no, complemento. | Pendiente según tiempo. |
| OD-U10-06 | Alta | Definir tratamiento del símbolo integral. | PSD requiere integrar sobre banda; el público puede no dominar cálculo. | Introducir como área/suma; derivación matemática en complemento. | Recomendación preliminar. |
| OD-U10-07 | Alta | Definir profundidad de la ley `K/f`. | El mensaje por octava es obligatorio; la integral no. | Criterio blanco/rosa central; demostración `K ln 2` complementaria. | Recomendación preliminar. |
| OD-U10-08 | Alta | Normalizar `p_ref`, `L_Aeq,T`, máximo/pico y símbolo de reducción. | Hay diferencias entre capítulo y guía. | Adoptar guía; documentar equivalencias con el libro. | Pendiente de consistencia. |
| OD-U10-09 | Media | Definir si incluir pseudoaleatoriedad. | Aclara señales de ensayo, pero no es programa. | Ejemplo breve o respaldo. | Pendiente. |
| OD-U10-10 | Alta | Definir el peso de percentiles `L_n,T`. | Útiles para ambiente residual, pero pueden dispersar el foco. | Complementario salvo necesidad en práctica local. | Pendiente docente. |
| OD-U10-11 | Alta | Definir peso central de exposición y dosis. | El libro amplía mucho; el programa solo alude a efectos en objetivos generales. | `L_eq,T` y lectura crítica centrales; dosis y normalización a respaldo. | Recomendación preliminar. |
| OD-U10-12 | Alta | Seleccionar norma y jurisdicción para cualquier cifra de exposición. | ISO, NIOSH y normativa argentina cumplen funciones distintas. | No mostrar límites hasta decidir autoridad, edición, jornada y población. | Pendiente documental. |
| OD-U10-13 | Alta | Definir el alcance clínico de “técnica de enmascaramiento”. | La matriz la marca como expansión externa. | Acordar con Audiología si se agrega protocolo y qué fuente institucional usar. | Pendiente de cátedra. |
| OD-U10-14 | Alta | Conseguir fuente clínica completa si se desarrolla masking. | El libro solo contiene guía funcional. | No redactar niveles, incrementos o meseta sin fuente y validación. | Bloqueante para protocolo. |
| OD-U10-15 | Media | Decidir si incluir acufenometría. | Aplicación relevante, no exigida por programa y sensible clínicamente. | Complemento breve con advertencia; sin terapia ni niveles. | Pendiente. |
| OD-U10-16 | Alta | Elegir ejemplo documentado de ruido con espectro de habla. | No existe curva universal. | Usar señal/equipo/norma claramente identificados o mantener solo esquema cualitativo. | Pendiente de fuente. |
| OD-U10-17 | Alta | Diseñar audios comparativos. | Blanco, rosa, NBN y espectro de habla se benefician de escucha. | Normalizar criterio, limitar nivel/duración, indicar qué escuchar y ofrecer alternativa visual. | Pendiente de assets/seguridad. |
| OD-U10-18 | Alta | Definir demostración de medición. | Un sonómetro o app puede enseñar descriptores, pero no certificar. | Si se usa, rotularla exploratoria y documentar configuración. | Pendiente docente. |
| OD-U10-19 | Alta | Seleccionar actividades centrales. | Hay 32 grupos; no caben todos en enseñanza sin perder ritmo. | Una comprobación por bloque, 3–4 cálculos y caso integrador. | Pendiente para storyboard. |
| OD-U10-20 | Alta | Reconstruir cuatro gráficos. | Los scripts son reproducibles, pero el estilo es de libro. | Regenerar con `chart-generation`; dividir gráficos densos y validar ejes/unidades. | Pendiente de producción. |
| OD-U10-21 | Alta | Reconstruir tres diagramas. | Los TikZ contienen tipografía pequeña para aula. | Usar `diagram-generation`, formas editables y ciclo renderizado. | Pendiente de producción. |
| OD-U10-22 | Media | Decidir animaciones. | Integración por bandas, ruta cruzada y controles pueden beneficiarse. | Revelados funcionales con versión estática completa. | Pendiente para storyboard. |
| OD-U10-23 | Media | Definir necesidad de fotografías. | No hay imágenes U10 y el recurso puede volverse decorativo. | Solo montajes o contextos técnicos que enseñen posición, equipo o trayecto. | Pendiente de curación. |
| OD-U10-24 | Alta | Definir cómo separar `L_max`, `L_peak` e Impulse. | Error explícito y frecuente. | Comparación central con una misma señal y configuración declarada. | Pendiente de gráfico/ejemplo. |
| OD-U10-25 | Media | Añadir ejemplo con intervalos de distinta duración. | La fórmula del capítulo cubre intervalos iguales. | Complemento si se enseña combinación general; evitar generalizar la fórmula actual. | Pendiente. |
| OD-U10-26 | Alta | Definir si usar datos reales. | El capítulo solo usa señales sintéticas. | Mantener sintéticos para concepto; datos reales solo con fuente, método e incertidumbre. | Pendiente de assets. |
| OD-U10-27 | Alta | Delimitar control de ruido. | Puede derivar a diseño, selección de protectores o consejo ocupacional. | Enseñar elección de eslabón y mecanismo; cálculos profesionales fuera. | Recomendación preliminar. |
| OD-U10-28 | Alta | Decidir norma para cabinas si se muestran valores. | U9 y U10 advierten que dB(A) global no basta. | Coordinar con decisiones U9; no duplicar ni mezclar tablas. | Pendiente global. |
| OD-U10-29 | Media | Actualizar localizadores de `content_coverage_matrix.csv`. | La numeración ya no coincide con el PDF. | Tarea posterior con `course-architecture`, sin cambiar estados. | Fuera de esta entrega. |
| OD-U10-30 | Media | Programar revisión pedagógica específica. | U10 no está entre U4–U7, pero integra estadística, clínica y normativa. | Revisar storyboard antes de redacción con foco en carga y fronteras. | Pendiente de responsable. |

## Decisiones de frontera curricular recomendadas

| Tema | Núcleo U10 | Puente permitido | Desarrollo reservado |
|---|---|---|---|
| Estadística | Media, RMS, varianza, distribución intuitiva. | Identidad y ejemplos adicionales. | Probabilidad, inferencia y procesos estocásticos formales. |
| Frecuencia | PSD, integración de banda y blanco/rosa. | Demostración por octavas. | Wiener–Khinchin, estimación PSD avanzada. |
| Medición | Máximo, pico, equivalente, ponderación e intervalo. | Percentiles y combinación de intervalos. | Metrología completa, incertidumbre normativa y certificación. |
| Exposición | Nivel + duración y lectura de documentos. | Ejemplo normativo elegido. | Asesoramiento legal/ocupacional y selección profesional de protección. |
| Psicoacústica | SNR y enmascaramiento como función. | Comunicación en ruido y acufenometría. | Modelos perceptuales completos ya tratados en U7. |
| Audiometría | Ruta cruzada, oído no evaluado y señal enmascarante. | Protocolo institucional validado. | Diagnóstico, prescripción y técnica clínica sin fuente. |
| Control | Fuente, trayecto y receptor; mecanismos correctos. | Caso antes/después. | Diseño acústico, cálculo profesional y compra de soluciones. |

## Condiciones mínimas para avanzar

Antes del storyboard deben quedar resueltas al menos:

1. número y duración de encuentros;
2. profundidad del repaso y de estadística/PSD;
3. núcleo frente a complemento para percentiles y exposición;
4. alcance y fuente del enmascaramiento clínico;
5. término y ejemplo para ruido con espectro de habla;
6. notación visible definitiva;
7. selección de actividades;
8. estrategia y seguridad de audios/demostraciones;
9. reconstrucción de siete visuales;
10. uso o no de datos reales e imágenes técnicas;
11. norma/jurisdicción para cualquier cifra;
12. coordinación con U9 y responsable de revisión.

Mientras falten la fuente clínica y las decisiones normativas, el futuro storyboard puede reservar espacios conceptuales, pero no debe redactar cifras, protocolos ni recomendaciones reconstruidas de memoria.
