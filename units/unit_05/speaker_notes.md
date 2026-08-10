# Unidad 5 — Notas del orador

Versión: final · 2026-08-03
Las duraciones son aproximadas. Las slides complementarias y de respaldo se usan a demanda; no forman una secuencia obligatoria de proyección.

## B00 · Apertura y orientación

### U05-001 · 2 min
Explicar que la unidad no busca “aprender a mirar FFT”, sino decidir qué objeto y magnitud representa cada visual. Recuperar U4: una señal compleja puede resumirse con RMS sin quedar completamente descripta. **Transición:** mostrar dos señales con igual RMS.

### U05-002 · 4 min
Pedir una predicción individual antes de comparar. Respuesta esperada: no son iguales; el RMS común solo informa tamaño eficaz. Evitar revelar todavía sus espectros. Error frecuente: identificar “misma energía” con “misma señal” o “misma percepción”. **Transición:** preguntar qué gráfico permitiría distinguirlas.

### U05-003 · 5 min
Dar 60–90 s para clasificar los cuatro mini gráficos. No sancionar errores; anotar si confunden espectro con respuesta y eje vertical con intensidad. Respuesta esperada: la forma visual no basta; deben nombrarse objeto, ejes, unidades y condiciones. **Transición:** recuperar prerrequisitos de U3/U4.

### U05-004 · 4 min
Recorrer primero U3 y luego U4; no volver a enseñar ambos temas. Preguntar: “¿qué unidad tiene `p(t)`?” Respuesta: Pa. “¿Cómo se relacionan `f` y `T`?” Respuesta: inversamente. **Transición:** convertir conocimientos previos en acciones observables.

### U05-005 · 3 min
Leer los objetivos como tareas que podrán demostrar, no como temario. Elegir dos y pedir ejemplos de evidencia. Señalar que calcular sin interpretar ni declarar condiciones no alcanza. **Transición:** ubicar esas acciones en el mapa de la unidad.

### U05-006 · 4 min
Guiar el diagrama de izquierda a derecha: representar, analizar, organizar/modificar, medir/decidir. Explicar que el mapa reaparecerá con más detalle. Aclarar la ruta central y el material complementario. **Transición:** presentar una rutina que funcionará en todos los tramos.

### U05-007 · 5 min
Aplicar las cinco preguntas a uno de los gráficos diagnósticos. Respuesta esperada debe incluir una conclusión limitada, no una interpretación perceptual. Pedir que mantengan esta rutina en sus apuntes. **Transición:** usarla sobre una misma señal en varias vistas.

## B01 · Una señal, varias representaciones

### U05-008 · 1 min
Recuperar U05-002: una vista temporal no responde todas las preguntas. Anticipar que tiempo, frecuencia y fase no compiten; se complementan. **Transición:** comenzar por el dominio temporal.

### U05-009 · 4 min
Leer ejes antes de la curva. Señalar duración, transitorio y periodicidad aproximada. Preguntar qué magnitud está graficada; respuesta: presión, no “sonido” genérico. Error frecuente: confundir altura temporal con frecuencia. **Transición:** preguntar qué no se ve con facilidad.

### U05-010 · 5 min
Insistir en que “FFT” no nombra la ordenada. Dar ejemplos: magnitud, potencia o nivel producen números y unidades distintos. Pregunta: “¿puedo comparar dos espectros si no conozco normalización?” Respuesta: no de forma cuantitativa segura. **Transición:** mostrar una señal en tres vistas coordinadas.

### U05-011 · 6 min
Guía visual: 1) tiempo, 2) magnitud, 3) fase. Hacer que identifiquen 100 y 200 Hz y luego vinculen cada línea con la suma temporal. No afirmar que un panel es “más real”. **Transición:** convertir la lectura en actividad.

### U05-012 · 4 min
Dar respuesta después de la descripción: variable temporal `p(t)` en Pa; frecuencia en Hz; fase en rad. Pregunta final esperada: no puede inferirse percepción, causa ni respuesta de un sistema. **Transición:** aislar el papel de la fase.

### U05-013 · 5 min
Mostrar primero magnitudes iguales y pedir predicción sobre la forma. Luego revelar señales temporales distintas. Explicar fase como ubicación relativa dentro del ciclo, sin números complejos. Error: “si la magnitud es igual, la señal es igual”. **Transición:** comparar el conjunto completo.

### U05-014 · 4 min · complementaria
Usar solo si la clase domina U05-013. Señalar que reconstrucción requiere convención, magnitud y fase. No realizar operaciones complejas. Pregunta: “¿qué panel explica la diferencia temporal?” Respuesta: fase. **Transición:** volver a clasificación temporal.

### U05-015 · 6 min
Marcar un período y verificar que la forma reaparece. Resolver `0,010 s → 100 Hz` con unidades. Aclarar que registros reales pueden ser aproximadamente periódicos en un tramo. Error: elegir un período múltiplo y llamarlo fundamental. **Transición:** observar una vocal con bordes transitorios.

### U05-016 · 5 min
Usar el esquema conceptual mientras no exista U05-MED-003. Explicar ataque, tramo casi estable y final; “aperiódica” no significa automáticamente ruido. Pregunta: “¿puede una misma vocal recibir dos etiquetas?” Respuesta: sí, según tramo y escala. **Transición:** elegir la vista adecuada.

### U05-017 · 4 min
Pedir una elección: transitorio→tiempo; componentes→magnitud; reconstrucción temporal→magnitud y fase. No repetir definiciones completas; enfatizar relación pregunta–vista. **Transición:** preguntar cómo construir una forma compleja con senoides.

## B02 · Herramientas de Fourier

### U05-018 · 2 min
Declarar el principio: Fourier cambia la base matemática, no crea piezas ni describe por sí mismo un mecanismo auditivo. Mostrar suma progresiva sin fórmula. **Transición:** proponer una predicción con tres tonos.

### U05-019 · 5 min
Pedir que anticipen la suma y qué efecto tendría cambiar fase. Respuesta esperada: la suma depende de frecuencia, amplitud y fase. Hacer una demostración gráfica rápida si es posible. **Transición:** escuchar o ver la suma.

### U05-020 · 4 min · complementaria
Si hay audio propio aprobado, reproducir tonos breves a nivel seguro y luego la suma; si no, usar cuatro paneles estáticos. No discutir timbre o sonoridad en profundidad. **Transición:** aumentar el número de componentes.

### U05-021 · 6 min
Revelar 1, 3 y 5 términos manteniendo ejes fijos. Preguntar dónde mejora y dónde persisten oscilaciones. Explicar Gibbs solo como límite visual; no llamarlo ruido. **Transición:** compactar la construcción en una serie.

### U05-022 · 7 min
Leer la ecuación por partes: media, índice, frecuencia `nf_0`, coeficientes. Preguntar qué cambia al pasar de `n=1` a `n=2`; respuesta: frecuencia y coeficientes asociados. No derivar. **Transición:** responder de dónde salen los coeficientes.

### U05-023 · 5 min · complementaria
Presentar las integrales como comparación acumulada en `t∈[t₀,t₀+T₀]`; el límite puede trasladarse sin cambiar el período. No pedir cálculo. Mostrar que las unidades de los coeficientes coinciden con `x`. Error: creer que la integral “crea” la componente. **Transición:** volver a un ejemplo sin integrales.

### U05-024 · 6 min
Pedir estimación del período común. Resolver períodos individuales y luego el patrón de 10 ms. Aclarar que en este ejemplo la fundamental también es componente presente, pero no siempre. **Transición:** evaluar qué ocurre al sumar más términos.

### U05-025 · 4 min · complementaria
Respuesta esperada: mejora lejos de discontinuidades; persisten sobreoscilaciones cerca de ellas; no son ruido experimental. Verificar que nadie compare paneles con autoscale distinto. **Transición:** señalar que una frase no repite un período ideal.

### U05-026 · 5 min
Comparar periodicidad ideal con señal general sin afirmar que todo registro real tenga espectro continuo. Presentar la transformada como extensión conceptual. **Transición:** mostrar la fórmula solo como referencia.

### U05-027 · 5 min · complementaria
Explicar `j` como notación que reúne seno y coseno. Leer límites, variable y unidad; no operar números complejos. Pregunta: “¿por qué la unidad puede incluir segundos?” Respuesta: por la integración en tiempo bajo esta convención. **Transición:** separar magnitud y fase.

### U05-028 · 5 min
Conectar directamente con U05-013. Señalar que magnitud tiene la unidad definida por la convención y fase se expresa en radianes. Error: tratar `e^{jφ}` como fenómeno físico. **Transición:** recapitular herramienta y objeto.

### U05-029 · 5 min
Pedir que completen oralmente: serie→señal periódica; transformada→señal general; DFT→registro discreto; FFT→algoritmo. Respuesta de control: ninguna “crea” componentes. **Transición:** preguntar cómo se obtiene el gráfico desde datos reales.

## B03 · Del registro a la DFT

### U05-030 · 2 min
Separar fenómeno, sensor, datos y algoritmo. Pregunta: “¿en qué etapa aparece el número digital?” Respuesta: después de transducción y conversión/muestreo. **Transición:** desmontar la frase “el micrófono entrega una FFT”.

### U05-031 · 5 min · complementaria
Recorrer unidades por etapa. Enfatizar que el micrófono entrega señal eléctrica, no espectro. Error frecuente: usar FFT como nombre del instrumento. **Transición:** definir muestreo.

### U05-032 · 6 min · complementaria
Marcar puntos sobre la curva y calcular `T_s` para 8 kHz. Aclarar que Hz equivale aquí a muestras por segundo por el contexto. Mencionar aliasing solo como límite posterior. **Transición:** agregar `N` para conocer duración.

### U05-033 · 6 min
Hacer control dimensional: muestras/(muestras/s)=s. Comparar dos registros con igual `f_s`. Pregunta: “si duplica N, qué cambia?” Respuesta provisional: duración. **Transición:** distinguir DFT, FFT y gráfico.

### U05-034 · 5 min
Pedir ejemplos de frases correctas: “calculo la DFT con una FFT” y “grafico su magnitud”. Corregir “la FFT es el espectro”. **Transición:** ubicar los valores discretos.

### U05-035 · 5 min
Explicar bin como posición, no recipiente físico universal. Señalar `k=0` y separaciones iguales. Pregunta: “¿una línea ocupa siempre un bin?” Respuesta: no; depende de duración y ventana. **Transición:** relacionar separación y duración.

### U05-036 · 6 min
Leer las tres formas de la ecuación y sus unidades. Comparar dos rejillas. Repetir “separación nominal”, no “exactitud”. **Transición:** resolver un caso numérico.

### U05-037 · 6 min · complementaria
Pedir estimación: 2000 muestras a 8000/s deben durar menos de un segundo. Resolver cada paso y terminar con interpretación de 4 Hz. **Transición:** duplicar `N` mentalmente.

### U05-038 · 4 min · complementaria
Respuestas correctas: B y C. D es falsa: exactitud depende de más factores. Pedir explicación causal, no solo marcar opciones. **Transición:** nombrar esos factores.

### U05-039 · 5 min
Mostrar un contraejemplo de picos anchos o inestables. Explicar que resolución del eje y capacidad de estimar son problemas relacionados, no idénticos. **Transición:** cerrar vocabulario digital.

### U05-040 · 4 min
Pregunta esperada: faltan ordenada, unidad, normalización y condiciones. Hacer que un estudiante reconstruya la cadena completa. **Transición:** preguntar por qué un tono puede aparecer en varios bins.

## B04 · Ventanas y tiempo–frecuencia

### U05-041 · 2 min
Marcar el segmento elegido y preguntar qué ocurre en sus bordes. Señalar que seleccionar ya es una decisión analítica. **Transición:** expresar la selección como ventana.

### U05-042 · 5 min
Nombrar el resultado como señal ventaneada y explicar la multiplicación como ponderación temporal: donde la ventana vale cero, el registro no aporta. No confundir esta ventana con un filtro frecuencial. **Transición:** comparar ciclos enteros y no enteros.

### U05-043 · 6 min · complementaria
Leer primero tiempo y luego espectro, con escalas idénticas. Respuesta esperada: el caso no entero distribuye la contribución. Error: llamarla ruido o nuevas frecuencias físicas. **Transición:** definir fuga.

### U05-044 · 5 min
Dar definición y pedir que identifiquen causa, efecto y condiciones. Aclarar que la fuga no es una única “falla del software”. **Transición:** presentar el compromiso de otras ventanas.

### U05-045 · 5 min · complementaria
Mientras CH-009 esté pendiente, usar solo comparación cualitativa. No dar cifras de lóbulos. Pregunta: “¿qué ventana es mejor?” Respuesta: depende de la pregunta y del criterio. **Transición:** introducir compromiso tiempo–frecuencia.

### U05-046 · 6 min
Guía visual: leer eje tiempo, eje frecuencia, barra de color y parámetros. Preguntar qué configuración localiza mejor un cambio; corta. Cuál separa tonos próximos; larga. **Transición:** construir el espectrograma por etapas.

### U05-047 · 6 min
Recorrer segmentos sucesivos; cada espectro forma una columna. Evitar exigir la sigla STFT. Pregunta: “¿qué significa un color más intenso?” Respuesta: mayor valor de la ordenada declarada, no “más frecuencia”. **Transición:** aplicación vocal.

### U05-048 · 5 min · complementaria
Leer el ejemplo sintético del libro: ejes, barra de color y aparición de 500, 1500 y 3000 Hz. Pedir observaciones descriptivas; aclarar que no es un registro vocal ni una evidencia diagnóstica. Error: diagnóstico por una imagen. **Transición:** separar bin y banda.

### U05-049 · 5 min
Modificar mentalmente `T_obs`: cambian bins, permanecen límites definidos de la banda. Pedir una frase comparativa completa. **Transición:** mostrar cómo se integran niveles.

### U05-050 · 6 min · complementaria
Recuperar suma energética de U4. Resolver dos niveles iguales y verificar 53,01 dB. Aclarar condiciones de referencia y compatibilidad. **Transición:** recapitular metadatos del análisis.

### U05-051 · 5 min
Pedir que elijan ventana corta o larga para un ataque y justifiquen. Respuesta: corta para localización temporal, con costo frecuencial. Repetir el checklist sin copiar definiciones. **Transición:** cambiar de cómo se analiza a qué objeto se analiza.

## B05 · Señal frente a sistema

### U05-052 · 2 min
Mostrar dos curvas parecidas y preguntar si podrían pertenecer a objetos distintos. Respuesta: sí. Declarar este bloque como nudo central. **Transición:** definir espectro de señal.

### U05-053 · 5 min
Recorrer los cinco condicionantes de una vocal. Evitar la expresión universal “espectro de la voz”. Pregunta: “¿cambiar de tramo puede cambiar el espectro?” Respuesta: sí. **Transición:** contrastar con una propiedad entrada–salida.

### U05-054 · 5 min
Explicar sistema mediante filtro, audífono y tracto. Pregunta: “¿basta una salida para hallar respuesta?” Respuesta: no; hace falta entrada comparable y procedimiento. **Transición:** comparar objetos con criterios iguales.

### U05-055 · 6 min
Hacer que la diferencia sea semántica: usar ejes visualmente semejantes. Pedir qué datos necesita cada columna. Error: decidir por el aspecto de la curva. **Transición:** reunir entrada, sistema y salida.

### U05-056 · 6 min
Guiar X→H→Y frecuencia por frecuencia. Mostrar que una frecuencia puede ser fuerte en la salida por entrada fuerte, ganancia alta o ambas. Pregunta: “¿Y determina X y H por separado?” Respuesta: no. **Transición:** definir H mediante razón.

### U05-057 · 6 min
Leer condición `X≠0` antes de dividir. Explicar magnitud y fase de H. Error: dividir registros incompatibles o frecuencias distintas. **Transición:** expresar magnitud como ganancia.

### U05-058 · 6 min
Pedir estimación del signo: una mitad debe dar ganancia negativa. Resolver logaritmo y aclarar que −6,02 dB describe la razón en 1000 Hz. **Transición:** mostrar un cambio de fase sin cambio de magnitud.

### U05-059 · 5 min · complementaria
Desplazar una señal en pantalla o con gesto temporal. Explicar pendiente de fase sin derivar. Pregunta: “si |H|=1, el sistema no cambia nada?” Respuesta: puede cambiar fase. **Transición:** aplicar la cadena a voz.

### U05-060 · 6 min · complementaria
Guía: fuente glótica, tracto, radiación/registro. Distinguir líneas y envolvente. Aclarar que es modelo introductorio y no diagnóstico. **Transición:** aplicar la misma lógica a un dispositivo.

### U05-061 · 6 min
Pedir clasificación de cada dato: voz o audífono. No anticipar prescripción clínica. Respuesta esperada: `G(f)` pertenece al dispositivo bajo prueba. **Transición:** hacer una recap de señal/sistema/salida.

### U05-062 · 5 min
Dar tres mini casos y exigir frase completa: objeto, datos y conclusión. Corregir “espectro de salida = respuesta”. **Transición:** preguntar cómo se nombran las líneas periódicas.

## B06 · Componentes espectrales y voz

### U05-063 · 2 min
Mostrar el pico dominante sin rótulo y recoger intuiciones. Anticipar que la amplitud será distractor. **Transición:** recuperar definición temporal de fundamental.

### U05-064 · 5 min
Conectar período y espaciado. Aclarar que pitch se estudia en U7. Pregunta: “¿la línea fundamental debe ser la mayor?” Respuesta: no. **Transición:** ordenar términos por criterio.

### U05-065 · 6 min
Leer la tabla con inclusión lógica: todo armónico es parcial. Resolver el caso de 200 Hz con `f_0=100 Hz`: segundo armónico y primer sobretono. Error: primer sobretono = primer armónico. **Transición:** ver el distractor de amplitud.

### U05-066 · 5 min
Pedir identificar `f_0` antes de mostrar rótulos. Respuesta: 100 Hz aunque 200 Hz sea mayor. Justificación: periodicidad/espaciado. **Transición:** retirar la línea de 100 Hz.

### U05-067 · 6 min
Marcar diferencias 300−200 y 400−300. Respuesta: ambas 100 Hz; periodicidad compatible con `f_0=100 Hz`. No explicar pitch ausente. **Transición:** contrastar con espaciados no enteros.

### U05-068 · 5 min · complementaria
Dividir frecuencias por 100 Hz. Identificar razones no enteras. Mantener el ejemplo en terminología, sin acústica musical avanzada. **Transición:** reunir tres contraejemplos.

### U05-069 · 5 min
Asignar un caso por pareja. Pedir evidencia de periodicidad, no solo respuesta. Corregir “pico máximo decide”. **Transición:** diferenciar líneas de resonancias amplias.

### U05-070 · 6 min · complementaria
Señalar líneas y envolvente con gestos distintos. Definir formante con dependencia de método. No asignar valores universales ni diagnósticos. **Transición:** leer un caso vocal.

### U05-071 · 6 min · complementaria
Usar sintético hasta contar con registro autorizado. Pedir dos observaciones: espaciado y regiones de envolvente. Respuesta: 100 Hz de separación; máximos cerca de 700/1100 Hz. **Transición:** clasificar términos.

### U05-072 · 6 min
Admitir etiquetas múltiples cuando el criterio lo permite. Exigir justificación: múltiplo, posición sobre fundamental o resonancia. **Transición:** sintetizar fuente y sistema.

### U05-073 · 5 min
Reconstruir mapa con aportes de estudiantes. Preguntar qué pertenece a fuente y qué a tracto. Recordar límite hacia pitch. **Transición:** pasar de líneas a regiones del espectro.

## B07 · Rangos de frecuencia y dinámicos

### U05-074 · 2 min
Presentar fronteras como convenciones bajo condiciones. Evitar hablar aún de sensibilidad. **Transición:** leer el eje logarítmico.

### U05-075 · 5 min
Explicar que 20 Hz/20 kHz no forman paredes ni sensibilidad uniforme. Pregunta: “¿qué variables faltan?” Respuesta: oyente, nivel, estímulo y condiciones. **Transición:** profundizar baja frecuencia.

### U05-076 · 5 min
Desarmar “infra = siempre imperceptible”. Nombrar nivel, duración, vibración y distorsión. No dar ejemplos alarmistas. **Transición:** formular audible como relación.

### U05-077 · 5 min
Seguir estímulo–condición–oyente. Aclarar detectabilidad ≠ sonoridad ≠ comodidad. Anticipar curvas de U7 sin explicarlas. **Transición:** cerrar con ultrasonido.

### U05-078 · 4 min · complementaria
Definir por frecuencia y usar imagenología solo como ejemplo general. Preguntar por OEA; respuesta: no es automáticamente ultrasonido. **Transición:** cambiar de frecuencias a niveles.

### U05-079 · 6 min
Control dimensional: dB−dB=dB cuando descriptores son compatibles. Diferenciar rango dinámico de rango de frecuencia. **Transición:** aplicar a voz.

### U05-080 · 6 min
Mostrar el valor como caso hipotético. Preguntar qué ocurriría al cambiar distancia o tarea; respuesta: extremos pueden cambiar. Error: confundir con rango de pitch. **Transición:** comparar con instrumento.

### U05-081 · 4 min · complementaria
Usar plantilla sin cifras. Pedir qué variables controlarían en un registro instrumental. No incorporar tabla genérica. **Transición:** trasladar condiciones al oído.

### U05-082 · 6 min
Explicitar la tensión programa/libro. No negar el término, sino definir condiciones. Pregunta: “¿qué criterio superior usaríamos?” Respuesta: uno definido y documentado. **Transición:** recapitular frecuencia, nivel y condición.

### U05-083 · 5 min
Comparar los dos ejes. Dar una cifra aislada y preguntar qué información falta. Respuesta: descriptor, estímulo, procedimiento y población. **Transición:** agrupar frecuencias en bandas.

## B08 · Octavas y bandas

### U05-084 · 2 min
Recordar bin/banda. Mostrar que las bandas se organizan por razón. **Transición:** explicar para qué agrupar.

### U05-085 · 5 min
Comparar espectro fino y barras. Pedir qué se conserva y qué se pierde. Respuesta: energía por intervalo; se pierde detalle de ubicación. **Transición:** definir razón de octava.

### U05-086 · 6 min
Calcular `2^(1/3)` solo si ayuda; prioridad a interpretación multiplicativa. Mostrar distancias iguales en eje log. **Transición:** comparar con armónicos.

### U05-087 · 6 min
Marcar pares 1→2 y 2→4; preguntar por 2→3. Respuesta: no es octava. Error: toda separación armónica es octava. **Transición:** encontrar centro.

### U05-088 · 6 min
Comparar media aritmética 1250 Hz con geométrica 1000 Hz para 500–2000 Hz. Verificar razones 2 y 2. **Transición:** obtener límites desde centro.

### U05-089 · 7 min
Leer exponentes como factores recíprocos. No derivar logaritmos. Identificar `b`. **Transición:** restar límites para ancho absoluto.

### U05-090 · 5 min
Mostrar dos bandas iguales en eje log y desiguales en Hz. Pregunta: “¿B y Δf son lo mismo?” Respuesta: no. **Transición:** reunir relaciones en tres tercios.

### U05-091 · 6 min
Mientras CH-014 esté pendiente, enseñar relaciones sin centros nominales. Multiplicar tres razones `2^(1/3)` para obtener 2. **Transición:** resolver banda central.

### U05-092 · 8 min
Calcular con calculadora, mostrar redondeo al final y verificar `B=231,6 Hz`. Señalar corrección respecto del capítulo. Diferenciar exacto y nominal. **Transición:** comparar otro centro.

### U05-093 · 5 min · complementaria
Respuesta esperada: la banda centrada en 2000 Hz tiene mayor ancho en Hz. Pedir explicación multiplicativa antes de números. **Transición:** cerrar bin/banda/octava/tercio.

### U05-094 · 5 min
Pedir cuatro definiciones de una línea. Pregunta de control: al cambiar `T_obs`, cambia el bin, no los límites de una banda normalizada. **Transición:** preguntar cómo modificar regiones.

## B09 · Filtros

### U05-095 · 2 min
Recuperar H(f): un filtro es un sistema. Mostrar cuatro siluetas y evitar todavía asociarlas a sonidos. **Transición:** definir parámetros.

### U05-096 · 6 min
Recorrer paso, rechazo, transición y criterio. Preguntar qué significa `f_c`; respuesta: depende de criterio. **Transición:** comparar un solo límite.

### U05-097 · 5 min
Leer ambas curvas con la misma escala. Pedir región conservada y atenuada. **Transición:** pasar a dos límites.

### U05-098 · 5 min
Marcar `f_L`, `f_H`, `f_c` y `B`. Mencionar notch como caso estrecho, no como diseño. **Transición:** confrontar ideal y real.

### U05-099 · 7 min
Guía: ideal esquemático, Butterworth real, corte, transición. Explicar que el gráfico es modelo documentado. No afirmar respuesta universal. **Transición:** definir criterio de corte.

### U05-100 · 5 min
Mostrar el error “pared”. Preguntar si −3 dB vale siempre; respuesta: no. Exigir criterio en futuras respuestas. **Transición:** reutilizar centro y ancho.

### U05-101 · 6 min · complementaria
Resolver centro geométrico y ancho. Repetir que aquí `f_L/f_H` pertenecen a un sistema, no a una banda normativa. **Transición:** ofrecer escucha opcional.

### U05-102 · 5 min · complementaria
Reproducir audio solo si está producido y nivelado; anunciar orden antes. Pedir predicción desde curvas y luego escuchar. Alternativa obligatoria: espectros estáticos. **Transición:** reconocer filtros sin audio.

### U05-103 · 5 min
Dar 90 s para clasificar. Respuesta: pasa bajos, altos, banda y elimina banda; justificar paso/rechazo. **Transición:** separar propósitos de filtrado.

### U05-104 · 6 min
Recorrer objeto y salida de cada columna. Pregunta: “¿ponderación A convierte SPL en HL?” Respuesta: no. **Transición:** sintetizar lectura de filtros.

### U05-105 · 4 min
Pedir una frase que incluya tipo, límites, transición y propósito. Corregir descripciones que omitan objeto. **Transición:** ubicar el filtro dentro de un sistema de medición.

## B10 · Ponderaciones

### U05-106 · 2 min
Usar cadena conceptual sin curvas hasta verificar norma. Señalar el lugar exacto de ponderación. **Transición:** dividir una misma señal en A/C/Z.

### U05-107 · 5 min
Explicar que cada rama procesa el espectro antes de integrar. No asignar resultados numéricos. Pregunta: “¿puedo elegir una sola corrección para banda ancha?” Respuesta: no. **Transición:** comparar respuestas nominales.

### U05-108 · 6 min
Mantener cualitativa mientras CH-017 esté bloqueado. Diferenciar A, C y Z sin reproducir valores/tolerancias. Aclarar que Z no significa “sin instrumento”. **Transición:** definir nomenclatura A.

### U05-109 · 5 min
Desarmar un descriptor: L, subíndice A, eq/Fmax, intervalo. Explicar que dBA es forma del programa y se adopta dB(A). **Transición:** tratar un tono.

### U05-110 · 5 min
Leer condición “tono”. Explicar que A(f) es corrección del filtro, no nivel de otra fuente. **Transición:** sustituir un valor del capítulo con advertencia normativa.

### U05-111 · 6 min
Resolver la aritmética con la corrección −26,2 dB citada y pedir interpretación: resultado A para ese tono, no percepción ni corrección única para banda ancha. **Transición:** preguntar por banda ancha.

### U05-112 · 6 min
Mostrar por qué una constante falla: cada frecuencia recibe corrección diferente y luego se integra. Error central: trasladar el ejemplo tonal. **Transición:** separar medición y audición.

### U05-113 · 6 min
Pedir un ejemplo de pregunta que responde cada entidad. No desarrollar U7/U8. Respuesta clave: no hay conversión automática entre ellas. **Transición:** auditar una lectura.

### U05-114 · 5 min
Dar “72 dB(A)” y pedir completar campos. Respuesta esperada: descriptor, tiempo, intervalo, condiciones e instrumento. dB HL no puede inferirse. **Transición:** discutir nominal versus tolerancia.

### U05-115 · 4 min · complementaria
Usar solo concepto; no dibujar tolerancias cuantitativas. Explicar que una curva objetivo y una prueba de conformidad son evidencias diferentes. **Transición:** volver a interpretación básica.

### U05-116 · 5 min
Pedir comparar tono y banda ancha. Recuperar cadena: filtro, integración, descriptor, condiciones. **Transición:** preguntar qué etapas contiene un sonómetro.

## B11 · Sonómetro y descriptores

### U05-117 · 2 min
Enmarcar “medidor de nivel de presión sonora” como sonómetro. Mostrar grupos funcionales, no marca comercial. **Transición:** reconocer equipo.

### U05-118 · 5 min · complementaria
Si hay equipo, señalar sin manipular como protocolo. Distinguir micrófono, cuerpo y calibrador. Error: una foto demuestra clase o calibración. **Transición:** seguir recorrido de señal.

### U05-119 · 7 min
Guía paso a paso por seis nodos. Nombrar la unidad o tipo de salida de cada etapa. Aclarar que es arquitectura conceptual. **Transición:** formalizar nivel equivalente.

### U05-120 · 6 min
Recuperar RMS: cuadrar, promediar, raíz o nivel. Presentar nivel constante equivalente antes de integral. Pregunta: “¿por qué no promedio dB?” Respuesta: escala logarítmica. **Transición:** resolver dos tramos.

### U05-121 · 8 min
Pedir estimación entre 75 y 80; resultado debe acercarse a 80. Resolver conversiones y 77,4 dB. Error: promedio aritmético. **Transición:** comparar otros descriptores.

### U05-122 · 6 min · complementaria
Usar una señal con impulso. Mostrar que equivalente, máximo Fast y pico pueden ordenar resultados distinto. No enseñar ensayo normativo. **Transición:** aplicación audiométrica.

### U05-123 · 7 min
Dar 2 min para identificar bandas que exceden límite; la trama evita depender solo de color. Repetir “hipotético/no normativo”. Explicar por qué un dB(A) global o app no reemplaza procedimiento. **Transición:** completar ficha de medición.

### U05-124 · 5 min
Volver a “72 dB” y hacer completar seis campos. Aceptar varias configuraciones si son explícitas. **Transición:** elegir herramientas desde preguntas profesionales.

## B12 · Integración y cierre

### U05-125 · 6 min
Leer pregunta primero, representación después. Pedir justificación por objeto, ejes y condiciones. El diagrama debe guiar, no contener explicaciones largas. **Transición:** presentar caso con señal y dispositivo.

### U05-126 · 12 min
Dar 6–8 min de trabajo con los datos numéricos visibles. Pedir que marquen cada dato S (señal), R (registro) o H (sistema). Observar supuestos y unidades. No revelar la solución. **Transición:** mostrar ruta resumida.

### U05-127 · 7 min · complementaria
Revelar por capas: `T_obs=0,50 s`, `Δf=2 Hz`, `f_0=200 Hz`; luego `|H|=0,50`, `G=−6,02 dB` y fase `−180°` a 1000 Hz. Separar el máximo de envolvente de la fundamental. Remitir a U05-149 para detalle. **Transición:** convertir fallas en atajos frecuentes.

### U05-128 · 8 min
Asignar dos errores por pareja y pedir corrección con evidencia. Respuestas esperadas provienen de recaps previos. Elegir los errores más persistentes para discusión. **Transición:** reconstruir mapa final.

### U05-129 · 7 min
Recorrer el mapa completo sin reenumerar títulos. Hacer que estudiantes nombren relaciones ancla. Enfatizar trazabilidad y límite de conclusión. **Transición:** autoevaluar objetivos.

### U05-130 · 8 min
Comparar respuestas con diagnóstico inicial. Usar escala de seguridad y pedir una evidencia por objetivo. No calificar punitivamente. **Transición:** abrir sistema auditivo.

### U05-131 · 3 min
Explicar que respuesta frecuencial es concepto de sistema, pero la cóclea no “hace una FFT”. Formular pregunta de U6 sobre transformación física. **Transición:** cierre de ruta central.

### U05-132 · 2 min · complementaria
No leer referencias en clase. Indicar dónde consultar y qué recursos siguen pendientes de verificación. **Transición:** respaldo a demanda.

## B13 · Respaldo

### U05-133 · 5 min · respaldo
Usar solo si `j` bloquea U05-027/028. Dibujar vector y separar módulo/ángulo. No convertirlo en clase de complejos. **Retorno:** U05-027/028.

### U05-134 · 5 min · respaldo
Explicar integración como acumulación de semejanza. Señalar simetría cualitativa. No evaluar cálculo integral. **Retorno:** U05-022/023.

### U05-135 · 5 min · respaldo
Comparar unidades y convenciones. Preguntar por qué dos softwares podrían mostrar amplitudes distintas; respuesta: normalización/representación. **Retorno:** U05-010/027.

### U05-136 · 6 min · respaldo
Leer índices y asociar `k` con frecuencia. Mostrar checklist de escala unilateral/bilateral. No mezclar con ruta central si no hace falta. **Retorno:** U05-034–036.

### U05-137 · 5 min · respaldo
Mostrar primero puntos y luego dos curvas continuas. Pregunta: “¿las muestras permiten decidir cuál era?” Respuesta: no. Mantener Nyquist conceptual. **Retorno:** U05-032.

### U05-138 · 5 min · respaldo
No proyectar cuantitativamente hasta aprobar CH-009. Explicar criterios cualitativos y por qué no existe ganadora universal. **Retorno:** U05-045/046.

### U05-139 · 5 min · respaldo
Resolver `50+50→53,01 dB`. Preguntar distractores 100 y 50. Aclarar referencia común. **Retorno:** U05-050/085.

### U05-140 · 6 min · respaldo
Resolver magnitud y fase por separado. Convertir −90° a −π/2 rad si ayuda. Pregunta: “¿ganancia 6 dB informa retardo?” Respuesta: no. **Retorno:** U05-057–059.

### U05-141 · 6 min · respaldo
Recorrer seis etapas y registrar parámetros mínimos. No introducir jitter/shimmer. Repetir límite no diagnóstico. **Retorno:** U05-060/070–071.

### U05-142 · 4 min · respaldo
Usar como contrato para evaluar una cifra externa. Pedir identificar campos faltantes en un dato inventado sin validarlo. **Retorno:** U05-079–082.

### U05-143 · 4 min · respaldo
Diferenciar exacto y nominal. No completar tabla hasta verificar norma. **Retorno:** U05-091/092.

### U05-144 · 5 min · respaldo
Comparar curvas con misma escala y corte. Explicar orden sin polos/ceros. **Retorno:** U05-099/100.

### U05-145 · 2 min · respaldo bloqueado
No proyectar ni completar. Explicar, si surge, que la reproducibilidad exige norma autorizada y chequeos de ancla. **Retorno:** U05-108.

### U05-146 · 6 min · respaldo
Leer cadena de operaciones antes de símbolos. Relacionar con RMS y U05-121. Verificar `p_ref=20 µPa` en aire. **Retorno:** U05-120/121.

### U05-147 · 5 min · respaldo
Separar Fast/Slow de pico. Valores se presentan como referencias de diseño, no prueba de conformidad. **Retorno:** U05-122.

### U05-148 · 5 min · respaldo
Comparar propósito, actor, momento y evidencia. Evitar usar “calibración” como bolsa única. No dar protocolo. **Retorno:** U05-118/119.

### U05-149 · 12 min · respaldo
Entregar después de la actividad. Resolver por zonas con los resultados numéricos verificados; comprobar unidades y asignar cada resultado a objeto. Dividir visualmente si el texto baja de 22 pt. **Retorno:** U05-126/127.

### U05-150 · 3 min · respaldo
Usar como índice de consulta, no como cierre oral. Pedir que estudiantes busquen un término y su slide de retorno. Dividir en dos slides durante producción si la fuente no alcanza 22 pt. **Fin del respaldo.**
