# Unidad 8 — Revisión de gráficos propios

Fecha: 2026-08-12

## Resultado

Se aprobaron **6 gráficos cuantitativos** y se mantuvieron **6 recursos bloqueados** por fuentes, convenciones o decisiones docentes pendientes. Los gráficos aprobados tienen cero problemas críticos o mayores en la inspección individual y en el montaje de revisión.

| Recurso | Clasificación | Estado | Iteraciones | Revisión / fuente de datos |
|---|---|---|---:|---|
| U08-CH-001 | gráfico cuantitativo | aprobado | 1 | Modelo sintético/paramétrico declarado; SVG y PNG 2560×1440 legibles. |
| U08-CH-005A | gráfico cuantitativo | aprobado | 2 | Modelo sintético/paramétrico declarado; SVG y PNG 2560×1440 legibles. |
| U08-CH-008 | gráfico cuantitativo | aprobado | 1 | Modelo sintético/paramétrico declarado; SVG y PNG 2560×1440 legibles. |
| U08-CH-009 | gráfico cuantitativo | aprobado | 1 | Modelo sintético/paramétrico declarado; SVG y PNG 2560×1440 legibles. |
| U08-CH-010 | gráfico cuantitativo | aprobado | 1 | Modelo sintético/paramétrico declarado; SVG y PNG 2560×1440 legibles. |
| U08-CH-011 | gráfico cuantitativo | aprobado | 1 | Modelo sintético/paramétrico declarado; SVG y PNG 2560×1440 legibles. |
| U08-CH-002 | gráfico cuantitativo | bloqueado | 0 | fuente primaria y transcripción autorizada pendientes. No se generó una curva o convención ficticia. |
| U08-CH-003 | gráfico cuantitativo | bloqueado | 0 | simbología audiométrica pendiente (OD-U08-19). No se generó una curva o convención ficticia. |
| U08-CH-004 | gráfico cuantitativo | bloqueado | 0 | métrica/contexto NIOSH pendientes de aprobación docente. No se generó una curva o convención ficticia. |
| U08-CH-005 | gráfico cuantitativo | bloqueado | 0 | simbología y rótulo del bloque pendientes (OD-U08-10/19). No se generó una curva o convención ficticia. |
| U08-CH-006 | gráfico cuantitativo | bloqueado | 0 | escala dB HL o dB SL pendiente (OD-U08-15). No se generó una curva o convención ficticia. |
| U08-CH-007 | gráfico cuantitativo | bloqueado | 0 | unidad/profundidad timpanométrica pendiente (OD-U08-18/20). No se generó una curva o convención ficticia. |

## Verificaciones realizadas

- scripts reproducibles y datos/parametrizaciones locales;
- SVG válido y PNG 2560×1440;
- ejes, unidades y escala explícitos;
- tipografías de ejes ≥20 pt, ticks/leyendas ≥18 pt y anotaciones clave ≥22 pt;
- rótulo conceptual visible cuando no hay datos observacionales;
- no se usaron gráficos 3D, ejes truncados engañosos ni suavizados no declarados;
- captions, textos alternativos y fuente de datos presentes.

## Problemas corregidos

| Problema | Severidad inicial | Corrección | Estado |
|---|---|---|---|
| U08-CH-005A: la flecha de orientación se aproximaba al rótulo HL. | mayor | Se acortó el corredor y se separó verticalmente “Referencia HL”. | cerrado |
| Posible lectura clínica de modelos sintéticos. | mayor | Rótulo no normativo dentro de cada canvas y aclaración en README/caption. | cerrado |
| Datos humanos o porcentajes no autorizados en U08-CH-002/004. | crítico potencial | Recursos bloqueados; no se generaron datos. | controlado |

## Abiertos

Permanecen bloqueados U08-CH-002, 003, 004, 005, 006 y 007. Sus condiciones están registradas en `chart_plan.md` y `open_decisions.md`.
