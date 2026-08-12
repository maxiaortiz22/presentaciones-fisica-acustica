# Necesidades iniciales de diagramas — Unidad 7

## Criterio

Los siguientes recursos son candidatos explícitos para `diagram-generation`. Deben construirse con formas, texto y conectores editables, medirse al tamaño final y pasar por el ciclo generar → renderizar → revisar → corregir. Los identificadores con sufijo A/B/C son variantes pedagógicas del mismo sistema visual, no assets independientes si pueden resolverse por estados editables.

| diagram_id | Slides | Tipo | Contenido estructural | Riesgo geométrico | Fuente | Prioridad | Estado |
|---|---|---|---|---|---|---|---|
| U07-DG-001–006 | U07-003–010 | mapas/flujo | Puente U6→U7, cadena físico–perceptual, mapa de clase y marco estímulo–tarea–respuesta | medio: mantener flechas fuera de etiquetas | MAP; TEX 7.1–7.3; PREV U6 | alta | propuesto |
| U07-DG-007–010 | U07-021–025 | geometría + ecuación anotada | Campo libre, transferencia al tímpano, `G_CT` y montaje de medición | alto: rutas y callouts pueden cruzarse | TEX 7.4.2–7.4.3; REF `carlini2024` | alta | propuesto |
| U07-DG-011 | U07-028 | proceso | Referencia 1 kHz → prueba → juicio → punto isofónico | medio: cinco etapas requieren dos niveles | TEX 7.5 | alta | propuesto |
| U07-DG-012/012B | U07-033, 043 | mapa conceptual | Pares físico–perceptuales y versión acumulada | alto: enlaces secundarios; dividir si se cruzan | TEX 7.6 | alta | propuesto |
| U07-DG-013–015B | U07-045–051 | comparación + ecuaciones | `L_p`, `L_N`, `N_son`, construcción de referencia y conversión | medio: símbolos deben conservar jerarquía | TEX 7.7–7.8; NOT | alta | propuesto |
| U07-DG-016–018 | U07-056–059 | mapa + ecuación + tiempo | Tres niveles de enmascaramiento, `M` y superposición temporal | medio | TEX 7.9 | alta | propuesto |
| U07-DG-019–020C | U07-063–065, 125–127 | banco de filtros + ERB + recap | Espectro, filtros solapados, rectángulo equivalente, cadena funcional y variante de ecuación | alto: curvas y cajas compiten por espacio | TEX 7.9.1; REF `oxenham2018` | media | propuesto; dividir si hace falta |
| U07-DG-021 | U07-067–071 | líneas temporales | Simultáneo, hacia adelante y hacia atrás | bajo si se alinean los tres ejes | TEX 7.9.1–7.9.2 | alta | propuesto |
| U07-DG-022A–C | U07-072–075, 113 | mapas funcionales | Enmascaramiento energético/informacional y matriz integradora | alto: dos mecanismos más eje temporal | TEX 7.9.3; REF `oxenham2018` | alta | propuesto |
| U07-DG-023 | U07-074 | escena funcional | Voz objetivo, voz competidora, filtros, atención y respuesta | medio | TEX 7.9.3, 7.12 | media | propuesto |
| U07-DG-024 | U07-078 | mapa de condiciones | Material, procedimiento y oyente en inteligibilidad | medio | TEX 7.10 | alta | propuesto |
| U07-DG-025/025B | U07-080–081 | ecuación anotada | SNR, condiciones de medición y ejemplo | bajo | TEX 7.10.1; NOT | alta | propuesto |
| U07-DG-026/026B | U07-083, 085 | proceso causal | Habla, respuestas del recinto, colas e interacción con ruido | alto: evitar cruces entre línea temporal y causal | TEX 7.10.1–7.10.2 | alta | propuesto |
| U07-DG-027 | U07-084 | gráfico anotado | `T_60`, tramo de 60 dB, ejes y definición | medio | TEX 7.10.2 | alta | propuesto |
| U07-DG-028/028B | U07-086–087, 131 | ecuación + síntesis | `ALCons`, conteos `n_p`/`n_c`, ejemplo y límite de interpretación | medio: separar cálculo de modelos predictivos no desarrollados | TEX ec. 7.6; NOT | alta | propuesto |
| U07-DG-029–030B | U07-089–091, 132 | geometría + ecuación | Caminos directo/reflejado, diferencia de recorrido y retardo | alto: reservar corredores de flechas | TEX 7.11 | alta | propuesto |
| U07-DG-031–033B | U07-093–097 | mapas de factores | Variables de fusión, familia de precedencia, comparación Haas y síntesis | alto: U07-DG-032 puede requerir dos slides | TEX 7.11; REF `litovsky1999` | alta | propuesto |
| U07-DG-034–036B | U07-099–105, 133 | geometría binaural + ecuación | Trayectorias, ITD/ILD, distancia interaural efectiva y cota `abs(Δt_LR)≈d/c` | alto: fórmulas y rayos deben quedar separados | TEX 7.12; NOT | alta | propuesto |
| U07-DG-037–038 | U07-107–109 | diagrama espacial + integración | Cono de confusión, movimiento y mapa de pistas | alto: perspectiva debe seguir siendo legible | TEX 7.12; REF `oxenham2018` | media | propuesto |
| U07-DG-039 | U07-111 | flujo multifuente | Tres fuentes → mezcla binaural → objetos perceptuales | alto: máximo tres fuentes y dos niveles visuales | TEX 7.12; U3/U6 | alta | propuesto |
| U07-DG-040 | U07-113–114 | mapa de segregación | Competencia energética/informacional y pistas de agrupamiento | alto: dividir si excede cinco pistas | TEX 7.9.3, 7.12 | alta | propuesto |
| U07-DG-041 | U07-117 | caso sistémico | Aula, fuente, competidores, reflexiones, oyente y tarea | crítico: evitar diagrama “todo en uno” ilegible | TEX 7.9–7.12; MAP | alta | prototipo obligatorio |
| U07-DG-042 | U07-119–120 | síntesis acumulativa | Señal → ambiente → transferencia → procesamiento → tarea → respuesta | crítico: síntesis central; considerar construcción progresiva | TEX cap. 7; BR | alta | prototipo obligatorio |
| U07-DG-043 | U07-121 | puente de curso | U7 hacia U8, U9 y U10 | bajo | MAP; DM; COV | media | propuesto |

## Reglas de diseño y aceptación

- Texto principal de diagrama: 24 pt preferido, 22 pt mínimo; etiquetas breves de conectores: 20 pt mínimo.
- Ecuaciones centrales: 28 pt o más; símbolos y unidades definidos fuera del área de operadores.
- Margen interno mínimo: 0,18 pulgadas y 10–20 % de espacio libre por caja.
- Conectores anclados a bordes; al menos 0,10 pulgadas entre líneas y texto no relacionado.
- Ninguna flecha o punta puede cruzar, tocar o terminar dentro de texto.
- Si U07-DG-032, 039, 041 o 042 no cumple los mínimos, dividir el contenido antes de reducir tipografía.
- Renderizar a 16:9 en el layout previsto y documentar cada corrección relevante.
