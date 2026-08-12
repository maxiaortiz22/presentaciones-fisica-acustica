# Unidad 9 — Necesidades iniciales de diagramas y ecuaciones anotadas

## Alcance

Todos los recursos de esta lista son **candidatos para `diagram-generation`**. Deben construirse en el tamaño real que ocuparán en la slide, preferentemente con formas, texto y conectores editables de PowerPoint. Las ecuaciones anotadas deben conservar símbolos editables cuando sea posible.

Reglas de producción posteriores:

- texto principal 22–24 pt como mínimo; ecuaciones centrales 28 pt o más;
- margen interior mínimo de 0,18 pulgadas y 10–20 % de espacio libre en cajas;
- conectores anclados a bordes, dibujados detrás de nodos y con corredores libres;
- ninguna flecha o líder puede tocar texto;
- revelar por etapas solo si la versión estática final sigue siendo comprensible;
- dividir el recurso si no supera el ciclo generar → renderizar → revisar → corregir.

## Inventario por bloque

| diagram_id | slides | función | estructura editable prevista | complejidad/riesgo | fuente base | estado |
|---|---|---|---|---|---|---|
| U09-DG-001 | U09-001 | Portada conceptual. | Fuente, trayecto urbano, clínica y receptor unidos por una onda/ruta simple. | media; evitar aspecto publicitario. | Brief U9; caso organizador. | planificado |
| U09-DG-002 | U09-002 | Mapa del caso disparador. | Avenida, fachada, consultorio, cabina, dos receptores y rutas numeradas. | alta; reservar corredores y no anticipar soluciones. | Brief U9; aplicaciones del capítulo. | prototipar temprano |
| U09-DG-003 | U09-005 | Mapa de tres encuentros. | Ocho bloques, hitos y recapitulaciones con flecha de progresión. | media; demasiados bloques para una sola fila. | course_map; brief U9. | planificado |
| U09-DG-004 | U09-007 | Organizador fuente–trayecto–receptor. | Tres zonas más condiciones de medición; ejemplos bajo cada zona. | alta; será código visual recurrente. | LaTeX cap. 9; course_map. | prototipar temprano |
| U09-DG-005 | U09-008 | Comparar emisión y recepción. | Dos cajas de magnitud, flecha de propagación y tabla corta `L_W`/`L_p`. | media; colisión de símbolos y unidades. | LaTeX 9.1–9.2; notation_guide. | planificado |
| U09-DG-006 | U09-009 | Matriz de mecanismos. | Ocho mecanismos agrupados por qué cambia, dependencia y modelo. | alta; puede requerir dos niveles o revelado. | Brief e inventario U9. | prototipar temprano |
| U09-DG-007 | U09-010 | Actividad de clasificación. | Seis tarjetas conectables a fuente, trayecto o medición. | media; admitir pertenencia múltiple sin flechas cruzadas. | Diagnóstico del brief. | planificado |
| U09-DG-008 | U09-011 | Checklist de cuatro preguntas. | Qué cambia → qué se conserva → qué se estima → qué se mide. | baja–media. | Brief U9. | planificado |
| U09-DG-009 | U09-013 | Propagación esférica. | Fuente y tres frentes con radios/áreas; llamadas a potencia, intensidad y presión eficaz. | alta; adaptar figura impresa a aula. | U4 `propagacion-esferica.tex`. | reconstrucción requerida |
| U09-DG-010 | U09-014 | Ecuación de distancia anotada. | Fórmula central, llamadas a niveles, radios, signo e hipótesis; área para U09-CH-001. | alta; proteger fórmula de líderes. | LaTeX ec. 9.1; PDF p. 237. | prototipar temprano |
| U09-DG-011 | U09-015 | Ejemplo 0,50 → 1,00 m. | Datos → sustitución → resultado → interpretación, con unidad en cada etapa. | media. | Ejemplo del capítulo. | planificado |
| U09-DG-012 | U09-017 | Omnidireccional frente a direccional. | Dos patrones, misma potencia/distancia, dirección y punto de comparación. | media; no usar áreas engañosas. | U4 `directividad-q.tex`; LaTeX 9.2. | reconstrucción requerida |
| U09-DG-013 | U09-019 | `Q_dir` y `DI` anotados. | Comparador omnidireccional, razón lineal y ecuación logarítmica. | alta; evitar doble conteo visual. | LaTeX ec. 9.2; notation_guide. | planificado |
| U09-DG-014 | U09-020 | Montaje de campo sonoro alternativo. | Altavoz, eje, distancias, punto de referencia, paciente/micrófono y superficies. | alta; debe ser técnicamente neutro. | U8; LaTeX 9.2/9.8. | alternativa a imagen externa |
| U09-DG-015 | U09-021 | Decisión distancia/directividad. | Tres casos con árbol modelo–hipótesis–dato faltante. | media. | Síntesis B02. | planificado |
| U09-DG-016 | U09-023 | Ecuación `c(θ)` anotada. | Fórmula, unidades, intervalo y enlace al gráfico U09-CH-003. | media. | LaTeX ec. 9.3. | planificado |
| U09-DG-017 | U09-024 | Dos estados térmicos. | 5 °C y 25 °C; `c`, `f` conservada, `λ` resultante y conclusión. | alta; tres magnitudes por panel. | Ejemplo del capítulo. | prototipar temprano |
| U09-DG-018 | U09-025 | Gradientes térmicos. | Dos paneles con perfiles `θ(z)`, `c(z)`, rayos y zona de sombra. | muy alta; flechas y perfiles pueden colisionar. | Figura 9.1 `gradientes-termicos.tex`. | reconstrucción prioritaria |
| U09-DG-019 | U09-026 | Viento uniforme y ecuación efectiva. | Vector de viento, ángulo `ψ`, tres direcciones y ecuación anotada. | alta; normalizar `v_viento`. | LaTeX ec. 9.4. | planificado |
| U09-DG-020 | U09-027 | Gradiente vertical de viento. | Dos paneles a favor/en contra con `c_ef(z)` y trayectorias. | muy alta; reservar corredores separados. | Figura 9.2 `gradiente-viento.tex`. | reconstrucción prioritaria |
| U09-DG-021 | U09-028 | Presión–densidad–rapidez. | Ecuación central y mapa de variables acopladas con pregunta “¿qué se fija?”. | alta; evitar causalidad lineal falsa. | LaTeX ec. 9.5. | prototipar temprano |
| U09-DG-022 | U09-029 | Altitud y humedad. | Mapa de influencias relacionadas y datos necesarios para comparar. | alta; riesgo de “spaghetti”. | LaTeX 9.5.3–9.6. | complementario; dividir si hace falta |
| U09-DG-023 | U09-030 | Divergencia frente a absorción atmosférica. | Ecuación estructural en dos términos y dos mecanismos dibujados. | alta; no sugerir coeficiente constante universal. | LaTeX ec. 9.6. | planificado |
| U09-DG-024 | U09-031 | Turbulencia cualitativa. | Trayectorias perturbadas y registro fluctuante vinculados sin cifras. | media; no parecer simulación medida. | LaTeX 9.6. | complementario |
| U09-DG-025 | U09-032 | Ficha de campo. | Checklist jerárquico con geometría, atmósfera, superficie, bandas y tiempo. | alta; densidad textual. | Brief U9; aplicaciones. | prototipar temprano |
| U09-DG-026 | U09-033 | Matriz de recapitulación atmosférica. | Casos frente a columnas `c`, `λ`, trayectoria, `L_p` y “no concluye”. | alta; diseñar como matriz, no tarjetas estrechas. | Síntesis B03. | prototipar temprano |
| U09-DG-027 | U09-035 | Balance de superficie. | Incidente, reflejada, absorbida y transmitida con rutas separadas. | alta; flechas y rótulos deben quedar fuera del material. | Figura 9.3 `balance-superficie.tex`. | reconstrucción prioritaria |
| U09-DG-028 | U09-036 | Balance energético anotado. | `R_E + α + τ_E = 1`, llamadas de definición y correspondencia con U09-DG-027. | alta; tres símbolos parecidos. | LaTeX ec. 9.7; notation_guide. | prototipar temprano |
| U09-DG-029 | U09-038 | Geometría de reflexión. | Interfaz, normal, incidencia/reflexión y llamada a impedancias. | media. | LaTeX 9.7.1; U4. | planificado |
| U09-DG-030 | U09-039 | Anotaciones de línea temporal. | Líderes a directa, reflexión aislada y cola en U09-CH-004. | alta; no apoyar etiquetas sobre curvas. | LaTeX 9.7.1/9.7.3. | planificado |
| U09-DG-031 | U09-040 | Interfaz aire–sólido. | Incidente, reflejada, transmitida, normal y dos modos cualitativos. | muy alta; riesgo de demasiadas flechas/ángulos. | Programa; LaTeX 9.7.4. | prototipar temprano |
| U09-DG-032 | U09-041 | Snell acústica anotada. | Ecuación simple, triángulos/ángulos y advertencia sobre modos. | muy alta; fuente externa pendiente. | LaTeX 9.7.4; fuente académica por seleccionar. | complementario; condicionado |
| U09-DG-033 | U09-042 | Difracción en borde. | Frente, borde, sombra geométrica y frentes difractados. | alta; no dibujar ruta a través del panel. | Figura 9.4 `difraccion-barrera.tex`. | reconstrucción prioritaria |
| U09-DG-034 | U09-044 | Misma barrera, tres frecuencias. | Tres paneles sincronizados con `λ`, obstáculo y receptor constantes. | muy alta; necesita consistencia geométrica. | LaTeX 9.7.5; figura 9.4. | prototipar temprano |
| U09-DG-035 | U09-045 | Difracción frente a transmisión. | Dos rutas paralelas alrededor y a través del mismo obstáculo. | alta; separar colores y leyenda sin ambigüedad. | Brief U9; LaTeX 9.7/9.7.5. | planificado |
| U09-DG-036 | U09-046 | Árbol de mecanismos en interfaz. | Retorna, se disipa, atraviesa, cambia dirección, rodea; preguntas de evidencia. | muy alta; probable división en dos niveles. | Síntesis B04. | prototipar temprano |
| U09-DG-037 | U09-048 | Secuencia de llegadas en sala. | Directa → tempranas → densidad de reflexiones → cola. | alta; conectores temporales y espaciales. | LaTeX 9.7.3. | planificado |
| U09-DG-038 | U09-050 | Construcción de `A_eq`. | Superficies `S_i`, coeficientes `α_i` y sumatoria hacia un bloque resultado. | alta; unidades visibles y cajas amplias. | LaTeX ec. 9.8. | prototipar temprano |
| U09-DG-039 | U09-051 | Ecuación de Sabine anotada. | Fórmula, unidades, flechas de proporcionalidad y caja de hipótesis. | alta; evitar que límites compitan con ecuación. | LaTeX ec. 9.8; notation_guide. | prototipar temprano |
| U09-DG-040 | U09-052 | Ejemplo de aula. | Geometría → `V`/superficie → `A_eq` → `T_60` → interpretación. | muy alta; quizá dos etapas con revelado. | Ejemplo del capítulo. | prototipar temprano |
| U09-DG-041 | U09-053 | Igual absorción, distinta distribución. | Dos plantas de sala con la misma suma y ubicaciones diferentes. | media–alta; mantener escala y receptores equivalentes. | Brief U9; ampliación didáctica. | complementario |
| U09-DG-042 | U09-054 | `T_60` frente a aislamiento. | Dos recintos, dos preguntas, dos magnitudes y flechas separadas. | alta; clave para prevenir error. | Programa; LaTeX 9.7.3–9.8. | prototipar temprano |
| U09-DG-043 | U09-056 | Cadena de recapitulación de recinto. | Geometría → llegadas → decaimiento → descriptor, con límites laterales. | alta. | Síntesis B05. | planificado |
| U09-DG-044 | U09-058 | `τ_E` a `R`. | Fórmula, fracción transmitida, escala log y ejemplos 0,01/0,001. | alta; diferenciar `R` de `R_E`. | LaTeX ec. 9.9; notation_guide. | prototipar temprano |
| U09-DG-045 | U09-060 | Rutas entre recintos. | Pared, puerta, junta, ventilación, estructura y flanqueo con conectores. | muy alta; crear rutas por capas y detrás de objetos. | LaTeX 9.8–9.8.1. | reconstrucción prioritaria |
| U09-DG-046 | U09-061 | Acondicionar–aislar–insonorizar. | Matriz de tres objetivos con mecanismo, magnitud y verificación. | alta; evitar tarjetas angostas. | Programa; glossary; capítulo 9. | prototipar temprano |
| U09-DG-047 | U09-062 | Masa superficial. | Paneles, masa, área y definición `m_s`; dos comparaciones controladas. | media. | LaTeX 9.8; open_decisions. | planificado |
| U09-DG-048 | U09-063 | Ley de masas anotada. | Fórmula didáctica, término relativo seguro y caja de convención. | alta; valor absoluto pendiente. | LaTeX ec. 9.10. | condicionado a validación técnica |
| U09-DG-049 | U09-064 | Duplicación relativa. | Dos cadenas de cálculo `m_s×2` y `f×2`, conclusión común. | media. | Ejemplo del capítulo. | planificado |
| U09-DG-050 | U09-066 | Ruta débil alternativa a foto. | Dos cerramientos iguales con puerta/junta diferente y ruta dominante. | alta; no sugerir valores absolutos. | LaTeX 9.8–9.8.1. | complementario |
| U09-DG-051 | U09-067 | Actividad elemento–conjunto–ruta. | Tres casos con elección de descriptor/intervención y justificación. | alta. | Síntesis B06. | planificado |
| U09-DG-052 | U09-069 | Espuma frente a envolvente. | Dos cabinas conceptuales con campo interior y fuga exterior contrastados. | alta; no caricaturizar materiales. | LaTeX 9.8.1; glossary. | prototipar temprano |
| U09-DG-053 | U09-070, alternativa U09-076 | Elementos de cabina. | Envolvente, puerta, visor, sellos, ventilación, pasacables, uniones y apoyos. | muy alta; una slide completa y texto mínimo. | Figura 9.6 `cabina-sistema.tex`. | reconstrucción prioritaria |
| U09-DG-054 | U09-071, alternativa U09-076 | Rutas de ingreso a cabina. | Misma geometría que DG-053 con rutas directa, fuga, conducto, flanqueo, vibración y ruido propio. | muy alta; revelar por etapas y mantener versión final completa. | Figura 9.6; LaTeX 9.8.1. | reconstrucción prioritaria |
| U09-DG-055 | U09-072 | Cadena de verificación. | Prueba → criterio → medición por bandas → comparación → documentación. | alta; etapas con entradas/salidas claras. | Programa; capítulo 9. | prototipar temprano |
| U09-DG-056 | U09-074 | Checklist normativo. | Norma, edición, adopción, vía, transductor, bandas y menor nivel. | alta; siete campos y estado de fuente. | Open decisions OD-U09-22–26. | planificado |
| U09-DG-057 | U09-075 | Matriz de faltantes para 28 dB(A). | Valor aislado al centro y preguntas metrológicas alrededor, sin líder sobre texto. | alta; muchos callouts. | Brief U9; U5/U8. | prototipar temprano |
| U09-DG-058 | U09-077 | Actividad de rutas de cabina. | Caso con cuatro fuentes/rutas, evidencia y conclusión permitida. | muy alta; separar información dada de inferencia. | Síntesis B07. | prototipar temprano |
| U09-DG-059 | U09-079 | Caso final, capa fuente. | Mapa base y variables de potencia, espectro y directividad. | alta; debe alinearse con DG-060/061. | Caso U09-002; LaTeX 9.1–9.2. | serie coordinada |
| U09-DG-060 | U09-080 | Caso final, capa trayecto. | Mismo mapa con distancia, atmósfera, suelo, fachada, difracción y transmisión. | muy alta; demasiadas rutas si no se revelan. | Capítulo 9. | serie coordinada; prototipar temprano |
| U09-DG-061 | U09-081 | Caso final, capa receptor/medición. | Mismo mapa con posición, cabina, transductor, bandas y norma. | muy alta; sostener continuidad visual. | Capítulo 9; U8. | serie coordinada |
| U09-DG-062 | U09-082 | Matriz estimar–medir–consultar. | Seis decisiones y columnas mecanismo, modelo, dato, medición, límite. | alta; riesgo de tabla ilegible. | Banco de ejercicios U9. | prototipar temprano |
| U09-DG-063 | U09-083 | Mapa acumulativo final. | Fuente–trayecto–receptor con modelos ubicados y cinco pasos de decisión. | muy alta; puede requerir dos capas. | Programa; capítulo 9; course_map. | prototipar temprano |
| U09-DG-064 | U09-084 | Puente U9→U10. | Trayecto de U9 hacia caracterización y control de ruido en U10. | media. | course_dependency_map. | planificado |
| U09-DG-065 | U09-085 | Derivación de distancia. | Potencia → área → intensidad → presión → nivel, con proporcionalidades. | muy alta; respaldo de fundamento. | LaTeX U4; capítulo 9. | backup |
| U09-DG-066 | U09-087 | Soluciones distancia/directividad. | Datos, operaciones, unidades, hipótesis y conclusiones en dos problemas. | alta; dividir si baja de 22 pt. | Ejercicios cap. 9. | backup |
| U09-DG-067 | U09-089 | Conversión modal ampliada. | Interfaz, modos longitudinal/transversal y relación angular general. | muy alta; fuente académica pendiente. | Programa; LaTeX 9.7.4. | backup condicionado |
| U09-DG-068 | U09-090 | Soluciones balance/Sabine. | Dos rutas de cálculo completas con control dimensional. | muy alta; probablemente dos estados o slide doble. | Ejercicios cap. 9. | backup |
| U09-DG-069 | U09-091 | Árbol de límites de Sabine. | Condición observada → límite → medición/modelo alternativo. | alta. | Source_analysis; bibliografía por confirmar. | backup |
| U09-DG-070 | U09-095 | Resolución del caso integrador. | Matriz fuente–trayecto–receptor con evidencia, incertidumbre y límite. | muy alta; debe reflejar DG-059–061. | Síntesis U9. | backup; prototipar después de la serie |

## Priorización de prototipos

### Prototipo temprano obligatorio

U09-DG-002, 004, 006, 009–010, 017–021, 025–028, 031, 033–036, 038–040, 042, 044–046, 048, 052–058 y 059–063.

Estos recursos concentran los mayores riesgos de colisión, reducción tipográfica o confusión causal. Deben probarse antes de redactar el contenido visible definitivo.

### Familias que deben compartir geometría

- **Modelo organizador:** U09-DG-004, 008, 059–064 y 070.
- **Atmósfera:** U09-DG-018–026.
- **Superficie/interfaz:** U09-DG-027–036.
- **Recinto/aislamiento:** U09-DG-037–051.
- **Cabina:** U09-DG-052–058.

Compartir geometría significa conservar códigos visuales y posiciones reconocibles, no duplicar texto o repetir la misma slide.

## Dependencias que bloquean producción

1. U09-DG-032 y U09-DG-067 requieren una fuente académica completa para Snell y conversión modal.
2. U09-DG-048 requiere validar la convención visible de la ley de masas y el símbolo de masa superficial.
3. U09-DG-056 y U09-DG-057 pueden producirse sin cifras; la tabla asociada U09-092 seguirá bloqueada hasta resolver norma y escenario.
4. U09-DG-053/054 deben dividir la figura 9.6; no se acepta comprimir elementos y rutas en media slide.
5. Toda ecuación debe verificarse contra `style/notation_guide.md` antes de aprobar el diagrama.
