# Unidad 9 — Necesidades iniciales de assets externos y multimedia

## Criterio

Este inventario registra necesidades de **imágenes técnicas y recursos multimedia**, no autoriza todavía su descarga ni uso. Los gráficos cuantitativos y diagramas propios se registran en archivos separados. Toda fuente externa deberá pasar por `asset-curation`, conservar URL, autor/organización, fecha de acceso, licencia, propósito pedagógico y estado.

Prioridades:

1. organismos, universidades, laboratorios y documentación técnica;
2. fabricantes solo cuando la imagen muestre construcción o montaje y no funcione como publicidad;
3. recursos con licencia abierta o permiso inequívoco;
4. alternativa propia o estática cuando no exista una fuente adecuada.

No se usarán fotografías decorativas, imágenes de stock sin función, ni “espuma acústica” como representación genérica de aislamiento.

## Imágenes externas

| asset_id | slides previstas | necesidad visual | propósito pedagógico | tipo de fuente preferida | requisitos de selección | alternativa sin asset externo | prioridad | estado |
|---|---|---|---|---|---|---|---|---|
| U09-IMG-001 | U09-020 | Montaje real de audiometría en campo sonoro con altavoz, punto de prueba y geometría visible. | Conectar distancia/directividad con posición, eje y punto de referencia. | Universidad, hospital docente, fabricante de equipamiento audiológico con documentación técnica. | Perspectiva que permita anotar distancias y orientación; sin pacientes identificables; licencia verificable. | U09-DG-014, montaje sintético totalmente editable. | alta | por curar |
| U09-IMG-002 | U09-066 | Corte o detalle técnico de puerta, junta o pasaje que muestre una ruta débil. | Mostrar que el conjunto puede quedar limitado por accesos o fugas. | Laboratorio de acústica arquitectónica, manual técnico o publicación universitaria. | Geometría legible; sin valores comerciales usados como universales; evitar foto promocional. | U09-DG-050, comparación de dos cerramientos conceptuales. | media | por curar |
| U09-IMG-003 | U09-076 | Vista exterior de cabina audiométrica con puerta, visor y uniones observables. | Trasladar el diagrama de sistema a un objeto real. | Universidad, clínica docente, organismo sanitario o fabricante técnico. | Marca secundaria o recortable; sin inferir certificación por apariencia; licencia y autor claros. | U09-DG-053 sin fotografía. | media | por curar |
| U09-IMG-004 | U09-076 | Vista interior o detalle de ventilación y pasacables de cabina. | Localizar rutas de ingreso y distinguir tratamiento interior de aislamiento. | Documentación técnica o laboratorio acreditado. | Componentes identificables; no usar una superficie absorbente como prueba de aislamiento. | U09-DG-054 sin fotografía. | media | por curar |
| U09-IMG-005 | Complemento posible de U09-044 | Barrera acústica real con fuente, borde superior y receptor en una geometría comprensible. | Dar escala física al diagrama de difracción. | Organismo vial, universidad o estudio técnico con licencia abierta. | Debe verse el borde y la relación de alturas; no atribuir rendimiento cuantitativo sin datos. | Mantener U09-DG-034 como visual principal. | baja | opcional |
| U09-IMG-006 | Complemento posible de U09-032 | Estación meteorológica o montaje de medición acústica exterior. | Mostrar qué variables y posiciones se registran en campo. | Organismo meteorológico, universidad o norma/guía pública. | Instrumentos y ubicación reconocibles; evitar sugerir que una foto sustituye el procedimiento. | Ficha propia U09-DG-025. | baja | opcional |

## Multimedia y demostraciones

| asset_id | slides previstas | recurso | propósito pedagógico | condiciones de seguridad y uso | alternativa estática | prioridad | estado |
|---|---|---|---|---|---|---|---|
| U09-MEDIA-001 | U09-055 | Par breve de habla seca y reverberada, o animación sincronizada del decaimiento. | Relacionar experiencia auditiva, envolvente temporal y `T_60`. | Nivel seguro y moderado; material propio o con licencia; advertir que no es medición; no pedir experiencias clínicas personales. | U09-CH-006 con línea temporal y envolvente. | media | por producir o curar |
| U09-MEDIA-002 | Complemento posible de U09-025 | Animación de dos gradientes térmicos con trayectorias reveladas por etapas. | Comparar estado uniforme, suelo cálido e inversión sin superponer todos los rayos. | Debe conservar sentido si la animación no se reproduce; sin datos meteorológicos simulados como reales. | U09-DG-018 con dos paneles estáticos. | media | producir desde diagrama propio |
| U09-MEDIA-003 | Complemento posible de U09-027 | Animación de viento uniforme frente a gradiente vertical. | Mostrar que solo el gradiente introduce curvatura en el modelo presentado. | Flechas y etiquetas legibles; control manual; versión estática completa. | U09-DG-019 y U09-DG-020. | media | producir desde diagramas propios |
| U09-MEDIA-004 | Complemento posible de U09-071 | Revelado progresivo de rutas de ingreso a la cabina. | Reducir carga visual y destacar una ruta limitante por vez. | El resultado final debe mostrar todas las rutas; no depender del orden automático. | U09-DG-054 estático. | media | producir desde diagrama propio |

## Assets descartados por ahora

- Foto genérica de ciudad o tránsito para la portada: no agrega información que no pueda comunicar el diagrama del caso.
- Muestras decorativas de paneles o espumas: refuerzan la confusión absorción–aislamiento.
- Captura real de una aplicación telefónica: puede parecer recomendación de herramienta o medición válida; U09-075 usará una interfaz ficticia claramente no instrumental.
- Videos de “pruebas caseras” de aislamiento: no controlan fuente, geometría, sellado ni medición.
- Imágenes de tablas normativas encontradas en buscadores: no garantizan edición, adopción, contexto ni permiso de reproducción.

## Dependencias y decisiones abiertas

1. U09-IMG-001 depende de decidir si la cátedra quiere mostrar un montaje institucional real o un esquema neutro.
2. U09-IMG-003/004 requieren aprobación de fuente, licencia y ausencia de datos personales o institucionales sensibles.
3. U09-MEDIA-001 requiere protocolo de reproducción seguro y una alternativa visual completa.
4. Ningún asset externo debe incorporarse antes de registrar sus metadatos en `asset_manifest.csv` durante la fase de curaduría.
5. La ausencia de assets externos no bloquea el storyboard: todas las slides centrales tienen una alternativa propia.
