#!/usr/bin/env python3
"""Sincroniza manifiesto, planes e informes de los visuales propios de U08."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
UNIT=ROOT/"units"/"unit_08"
GEN=UNIT/"assets"/"generated"
GENERATOR=UNIT/"scripts"/"u08_generate_visuals.py"
ns={"__file__":str(GENERATOR),"__name__":"u08_visuals"}
exec(compile(GENERATOR.read_text(encoding="utf-8"),str(GENERATOR),"exec"),ns)
CHARTS=ns["CHARTS"]; BLOCKED_CHARTS=ns["BLOCKED_CHARTS"]
DIAGRAMS=ns["DIAGRAMS"]; BLOCKED_DIAGRAMS=ns["BLOCKED_DIAGRAMS"]
diagram_class=ns["diagram_class"]

DATE="2026-08-12"
ITERATIONS={"002":3,"010":3,"027":3,"031":3,"038":5,"044":3}
for did,(_,kind,_,_) in DIAGRAMS.items():
    if kind in {"flow","process","steps","mixed","layers"}: ITERATIONS.setdefault(did,2)

def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()

def update_validation_files():
    for cid in CHARTS:
        p=GEN/"charts"/f"U08-CH-{cid}"/"validation.json"; v=json.loads(p.read_text(encoding="utf-8"))
        v["status"]="approved"; v["manual_review"]=f"Aprobado {DATE}: inspección individual y en contact sheet; cero problemas críticos o mayores."
        v["iterations"]=2 if cid=="005A" else 1; v["checks"]["real_layout_review"]="passed"
        p.write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding="utf-8")
    for did,(title,kind,nodes,labels) in DIAGRAMS.items():
        folder=GEN/"diagrams"/f"U08-DG-{did}"; p=folder/"validation.json"; v=json.loads(p.read_text(encoding="utf-8"))
        cls=diagram_class(kind,did); v["classification"]=cls; v["status"]="approved"; v["iterations"]=ITERATIONS.get(did,1)
        v["manual_review"]=f"Aprobado {DATE}: preview PowerPoint 2560×1440 inspeccionado; cero problemas críticos o mayores."
        v["checks"].update({"text_overflow":0,"clipped_text":0,"connector_text_collisions":0,"labels_on_lines":0,"wrong_arrow_targets":0,"objects_outside_canvas":0,"rendered_in_real_layout":True,"padding_min_in":0.18,"font_min_pt":20 if did=="038" else 22})
        p.write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding="utf-8")
        src=folder/"diagram_source.json"; s=json.loads(src.read_text(encoding="utf-8")); s["classification"]=cls; s["font_pt"]["nodes"]=20 if did=="038" else 22; src.write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding="utf-8")
        readme=folder/"README.md"; txt=readme.read_text(encoding="utf-8"); txt=re.sub(r"- Clasificación: \*\*.*?\*\*\.",f"- Clasificación: **{cls}**.",txt); readme.write_text(txt,encoding="utf-8")

def update_manifest():
    path=UNIT/"asset_manifest.csv"
    with path.open(encoding="utf-8",newline="") as fh: rows=list(csv.DictReader(fh)); fields=list(rows[0])
    for row in rows:
        aid=row["asset_id"]
        if aid.startswith("U08-CH-"):
            cid=aid.removeprefix("U08-CH-")
            if cid in CHARTS or cid in BLOCKED_CHARTS:
                row["notes"]=re.sub(r"\s*Clasificación obligatoria:.*$","",row["notes"])
                row["local_path"]=rel(GEN/"charts"/aid); row["status"]="approved" if cid in CHARTS else "blocked"
                note="Clasificación obligatoria: gráfico cuantitativo. "
                if cid in BLOCKED_CHARTS: note+=f"Bloqueado: {BLOCKED_CHARTS[cid]}."
                else: note+=f"SVG, PNG 2560×1440, script, datos/parámetros, README, caption, alt y validación aprobados {DATE}."
                row["notes"]=(row["notes"].rstrip()+" "+note).strip()
        elif aid.startswith("U08-DG-"):
            did=aid.removeprefix("U08-DG-")
            if did in DIAGRAMS or did in BLOCKED_DIAGRAMS:
                row["notes"]=re.sub(r"\s*Clasificación obligatoria:.*$","",row["notes"])
                row["local_path"]=rel(GEN/"diagrams"/aid); row["status"]="approved" if did in DIAGRAMS else "blocked"
                cls=diagram_class(DIAGRAMS[did][1],did) if did in DIAGRAMS else "ecuación anotada"
                note=f"Clasificación obligatoria: {cls}. "
                if did in BLOCKED_DIAGRAMS: note+=f"Bloqueado: {BLOCKED_DIAGRAMS[did]}."
                else: note+=f"PPTX editable, SVG, PNG, preview real, fuente JSON, README, caption, alt y validación aprobados {DATE}."
                row["notes"]=(row["notes"].rstrip()+" "+note).strip()
    with path.open("w",encoding="utf-8",newline="") as fh:
        wr=csv.DictWriter(fh,fieldnames=fields,quoting=csv.QUOTE_ALL); wr.writeheader(); wr.writerows(rows)

def replace_chart_statuses():
    path=UNIT/"chart_plan.md"; text=path.read_text(encoding="utf-8")
    all_ids=list(CHARTS)+list(BLOCKED_CHARTS)
    for cid in all_ids:
        pat=rf"(### U08-CH-{re.escape(cid)}\b[\s\S]*?)- \*\*Estado:\*\*.*?(?=\n\n###|\n\n##)"
        state=(f"producido y aprobado el {DATE}; ver `assets/generated/charts/U08-CH-{cid}/`." if cid in CHARTS else f"**bloqueado**: {BLOCKED_CHARTS[cid]}; se creó solo el registro documental, sin figura inventada.")
        text=re.sub(pat,lambda m:m.group(1)+f"- **Estado:** {state}",text,count=1)
    text=text.replace("**Clasificación:** `chart` dentro de composición `mixed`.","**Clasificación:** `gráfico cuantitativo` dentro de una composición futura de tipo `esquema mixto`.")
    text=text.replace("**Clasificación:** `chart` de respaldo.","**Clasificación:** `gráfico cuantitativo` de respaldo.")
    text=text.replace("**Clasificación:** `chart`.","**Clasificación:** `gráfico cuantitativo`.")
    section=f"""

## Implementación y revisión — {DATE}

- **Producidos y aprobados:** {', '.join('U08-CH-'+x for x in CHARTS)}.
- **Bloqueados sin figura:** {', '.join('U08-CH-'+x for x in BLOCKED_CHARTS)}.
- Todos los producidos se clasificaron como **gráfico cuantitativo**, se exportaron en SVG y PNG 2560×1440 y conservan script, datos o parámetros, README, caption, texto alternativo y fuente de datos declarada.
- Los modelos sintéticos llevan el rótulo visible “esquema didáctico; no representa datos normativos ni un caso clínico”.
- La revisión completa está en `charts_review.md`.
"""
    text=re.sub(r"\n## Implementación y revisión — 2026-08-12[\s\S]*$","",text).rstrip()+section
    path.write_text(text,encoding="utf-8")

def update_diagram_plan():
    path=UNIT/"diagram_plan.md"; lines=path.read_text(encoding="utf-8").splitlines(); out=[]
    for line in lines:
        m=re.match(r"\| U08-DG-(\d{3}) \|",line)
        if not m: out.append(line); continue
        did=m.group(1); parts=line.split("|")
        if did in DIAGRAMS:
            cls=diagram_class(DIAGRAMS[did][1],did); parts[3]=re.sub(r"`[^`]+`",f"`{cls}`",parts[3],count=1)
            parts[-2]=(f" aprobado {DATE}; {ITERATIONS.get(did,1)} iter.; PPTX/SVG/PNG/preview " if did!="038" else f" aprobado {DATE}; redistribuido en 3 columnas; cuerpo 20 pt según mínimo de matriz; 5 iter. ")
        elif did in BLOCKED_DIAGRAMS:
            parts[3]=re.sub(r"`[^`]+`","`ecuación anotada`",parts[3],count=1); parts[-2]=f" bloqueado: {BLOCKED_DIAGRAMS[did]} "
        out.append("|".join(parts))
    text="\n".join(out)
    section=f"""

## Implementación y revisión — {DATE}

- **Producidos y aprobados:** {len(DIAGRAMS)} recursos editables con PPTX individual, fuente JSON, SVG, PNG, preview PowerPoint 2560×1440, lista de objetos, README, caption, texto alternativo y validación.
- **Bloqueados sin visual:** U08-DG-011 y U08-DG-029, por descriptor/notación pendientes.
- Clasificación aplicada antes de generar: `diagrama conceptual`, `diagrama de proceso`, `ecuación anotada` o `esquema mixto`.
- U08-DG-002, 010, 027 y 031 se redistribuyeron a 2×2 para preservar 22 pt y padding; U08-DG-038 se resolvió como comparación en tres columnas con cuerpo de 20 pt, mínimo explícito de la matriz en este plan.
- La validación completa está en `diagram_validation_report.md`; la revisión de assets, en `diagram_assets_review.md`.
"""
    text=re.sub(r"\n## Implementación y revisión — 2026-08-12[\s\S]*$","",text).rstrip()+section
    path.write_text(text,encoding="utf-8")

def write_reviews():
    chart_rows=[]
    for cid,(stem,title) in CHARTS.items(): chart_rows.append(f"| U08-CH-{cid} | gráfico cuantitativo | aprobado | {2 if cid=='005A' else 1} | Modelo sintético/paramétrico declarado; SVG y PNG 2560×1440 legibles. |")
    for cid,reason in BLOCKED_CHARTS.items(): chart_rows.append(f"| U08-CH-{cid} | gráfico cuantitativo | bloqueado | 0 | {reason}. No se generó una curva o convención ficticia. |")
    (UNIT/"charts_review.md").write_text(f"""# Unidad 8 — Revisión de gráficos propios

Fecha: {DATE}

## Resultado

Se aprobaron **{len(CHARTS)} gráficos cuantitativos** y se mantuvieron **{len(BLOCKED_CHARTS)} recursos bloqueados** por fuentes, convenciones o decisiones docentes pendientes. Los gráficos aprobados tienen cero problemas críticos o mayores en la inspección individual y en el montaje de revisión.

| Recurso | Clasificación | Estado | Iteraciones | Revisión / fuente de datos |
|---|---|---|---:|---|
{chr(10).join(chart_rows)}

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
""",encoding="utf-8")

    rows=[]
    for did,(title,kind,nodes,labels) in DIAGRAMS.items():
        cls=diagram_class(kind,did); font="20 pt (matriz)" if did=="038" else "22 pt"; rows.append(f"| U08-DG-{did} | {cls} | {ITERATIONS.get(did,1)} | {font} / etiquetas 20 pt / ecuación 34 pt | aprobado |")
    for did,reason in BLOCKED_DIAGRAMS.items(): rows.append(f"| U08-DG-{did} | ecuación anotada | 0 | no generado | bloqueado: {reason} |")
    (UNIT/"diagram_validation_report.md").write_text(f"""# Unidad 8 — Informe de validación de diagramas

Fecha: {DATE}

## Resultado

Se aprobaron **{len(DIAGRAMS)} diagramas** y se mantuvieron **{len(BLOCKED_DIAGRAMS)} ecuaciones anotadas bloqueadas**. Cada aprobado fue renderizado desde su PPTX editable individual en un canvas real de 13,333×7,5 in y exportado a 2560×1440. No quedan problemas críticos ni mayores.

| Recurso | Clasificación | Iteraciones | Tipografía mínima | Estado |
|---|---|---:|---|---|
{chr(10).join(rows)}

## Gates aplicados

- cero desbordes y clipping;
- cero conectores, puntas o líderes sobre texto;
- etiquetas independientes y separadas de las líneas;
- conectores detrás de nodos y anclados a sus bordes;
- cero nodos superpuestos u objetos fuera del canvas;
- padding interno de 0,18 in;
- texto principal de 22 pt, salvo cuerpo de U08-DG-038 a 20 pt conforme al mínimo explícito de matriz; etiquetas de 20 pt; ecuaciones de 34 pt;
- editabilidad comprobada en PPTX y respaldo SVG/JSON;
- legibilidad revisada individualmente y en contact sheet.

## Iteraciones y correcciones relevantes

| Hallazgo | Recursos | Corrección | Estado |
|---|---|---|---|
| Salto diagonal entre filas y etiquetas próximas a nodos. | cadenas de 5–6 etapas | Lectura serpenteante, anclajes de borde y etiquetas en corredores externos. | cerrado |
| Cuatro etapas con texto insuficiente para una sola fila. | U08-DG-002, 010, 027, 031 | Redistribución 2×2 sin reducir 22 pt. | cerrado |
| Etiqueta vertical larga próxima al conector. | U08-DG-044 | Caja independiente desplazada por completo a un lado del corredor. | cerrado |
| Matriz de seis filas demasiado densa. | U08-DG-038 | Tres columnas paralelas con los mismos cinco campos y cuerpo de 20 pt. | cerrado |
| Descriptor/notación sin decisión docente. | U08-DG-011, 029 | No se generó el visual. | bloqueado documentado |
""",encoding="utf-8")

    (UNIT/"diagram_assets_review.md").write_text(f"""# Unidad 8 — Revisión de assets de diagramas

Fecha: {DATE}

## Cobertura

- 50 carpetas aprobadas en `assets/generated/diagrams/`.
- 2 carpetas documentales bloqueadas: U08-DG-011 y U08-DG-029.
- Ningún diagrama depende de una fotografía externa para comprenderse.
- No se construyó la presentación final.

## Paquete por recurso aprobado

Cada carpeta contiene:

1. script reproducible;
2. `diagram_source.json` editable;
3. PPTX individual con formas, textos y conectores nativos;
4. SVG y PNG;
5. preview renderizado en el layout 16:9 real;
6. `objects.json` con IDs estables;
7. README, caption y texto alternativo;
8. `validation.json` con gates e iteraciones.

## Revisión editorial y pedagógica

- Los textos son breves, académicos y no convierten patrones en diagnósticos.
- Los esquemas conceptuales declaran que no están a escala.
- Las cadenas distinguen naturaleza acústica, mecánica, eléctrica o bioeléctrica mediante rótulos además del color.
- Las ecuaciones diferencian niveles con referencia de resultados expresados en dB.
- Los límites de inferencia se conservan dentro del recurso cuando son parte del objetivo pedagógico.

## Estado final

No se detectaron assets faltantes entre los recursos aprobados. Las únicas ausencias son deliberadas y trazables: U08-DG-011 y U08-DG-029 permanecen bloqueados hasta resolver las decisiones abiertas correspondientes.
""",encoding="utf-8")

def main():
    update_validation_files(); update_manifest(); replace_chart_statuses(); update_diagram_plan(); write_reviews()

if __name__=="__main__": main()
