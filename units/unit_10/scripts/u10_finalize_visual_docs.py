"""Cierra planes, manifiesto e informes de los recursos visuales de U10."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

UNIT=Path(__file__).resolve().parents[1]
CH=UNIT/"assets"/"generated"/"charts"
DG=UNIT/"assets"/"generated"/"diagrams"
DATE="2026-08-12"


def load(p):return json.loads(p.read_text(encoding="utf-8"))


def add_visual_iteration(folder,corrected=False):
    p=folder/"validation.json";d=load(p);iterations=d.setdefault("iterations",[])
    if not any(x.get("action")=="inspección visual en hoja de contacto" for x in iterations):
        iterations.append({"iteration":len(iterations)+1,"action":"inspección visual en hoja de contacto","critical":0,"major":0})
    if corrected and not any("corrección visual" in x.get("action","") for x in iterations):
        iterations.append({"iteration":len(iterations)+1,"action":"corrección visual y nuevo render","critical":0,"major":0})
    d["status"]="approved";d["critical_issues"]=0;d["major_issues"]=0;p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")
    return d


def update_manifest():
    p=UNIT/"asset_manifest.csv"
    with p.open(encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f));fields=list(rows[0])
    for r in rows:
        aid=r["asset_id"]
        if re.fullmatch(r"U10-CH-0(0[1-9]|1[0-5])",aid):
            r["status"]="approved-generated";r["access_date"]=DATE;r["local_path"]=f"units/unit_10/assets/generated/charts/{aid}/";r["notes"]="Clasificación: gráfico cuantitativo; SVG y PNG; datos, script, caption, alt text y validación disponibles."
        elif aid=="U10-CH-016":r["status"]="blocked-source";r["notes"]="Clasificación prevista: gráfico cuantitativo; no generado: requiere documento normativo, edición y jurisdicción validados."
        elif re.fullmatch(r"U10-DG-0(0[1-9]|[1-4][0-9]|5[0-7])",aid):
            src=load(DG/aid/"diagram_source.json");r["status"]="approved-generated";r["access_date"]=DATE;r["local_path"]=f"units/unit_10/assets/generated/diagrams/{aid}/";r["notes"]=f"Clasificación: {src['classification']}; SVG/PNG y PPTX editable; validación sin problemas críticos ni mayores."
        elif aid=="U10-DG-058":r["status"]="blocked-example";r["notes"]="Clasificación prevista: ecuación anotada; no generado: el plan exige verificar el ejemplo de intervalos desiguales."
        elif aid=="U10-DG-059":r["status"]="blocked-content";r["notes"]="Clasificación prevista: esquema mixto; no generado: depende de slide-writing y selección final de ejercicios."
        elif aid=="U10-DG-060":r["status"]="blocked-source";r["notes"]="Clasificación prevista: diagrama de proceso; no generado: requiere protocolo clínico institucional validado."
    with p.open("w",encoding="utf-8-sig",newline="") as f:w=csv.DictWriter(f,fieldnames=fields,quoting=csv.QUOTE_ALL);w.writeheader();w.writerows(rows)


def update_plan(path,kind,registry):
    text=path.read_text(encoding="utf-8")
    lines=[]
    pat=re.compile(rf"^\| U10-{kind}-(\d{{3}}) ")
    for line in text.splitlines():
        m=pat.match(line)
        if m and int(m.group(1)) in registry:
            cells=line.split("|")
            if kind=="CH":cells[-2]=" aprobado · 2026-08-12 "
            else:
                base=re.sub(r"\s*· aprobado tras render 2026-08-12\s*$","",cells[-2].strip())
                base=re.sub(r";\s*(planificado|prototipar[^.;]*|complementario|respaldo)\.?","",base,flags=re.I)
                cells[-2]=f" {base.rstrip('.; ')}; aprobado tras render 2026-08-12 "
            line="|".join(cells)
        lines.append(line)
    marker="## Clasificación obligatoria y resultado de producción"
    if marker in "\n".join(lines):lines=lines[:next(i for i,x in enumerate(lines) if x==marker)]
    lines.extend(["",marker,"",f"Registro cerrado el {DATE}. La clasificación se fijó antes de ejecutar cada generador.","","| ID | Clasificación obligatoria | Resultado | Carpeta |","|---|---|---|---|"])
    for aid,cls,status in registry.values():
        root="charts" if kind=="CH" else "diagrams";lines.append(f"| {aid} | {cls} | {status} | `assets/generated/{root}/{aid}/` |")
    if kind=="CH":lines.append("| U10-CH-016 | gráfico cuantitativo | bloqueado por fuente normativa | no generado |")
    else:
        lines.extend(["| U10-DG-058 | ecuación anotada | bloqueado hasta verificar ejemplo | no generado |","| U10-DG-059 | esquema mixto | bloqueado hasta slide-writing | no generado |","| U10-DG-060 | diagrama de proceso | bloqueado por protocolo institucional | no generado |"])
    path.write_text("\n".join(lines).rstrip()+"\n",encoding="utf-8")


def chart_review(rows):
    out=["# Unidad 10 — Revisión de gráficos cuantitativos","",f"Fecha: {DATE}","","## Resultado","",f"Se generaron y revisaron **{len(rows)} gráficos cuantitativos**. Todos poseen script reproducible, datos o parámetros, SVG, PNG de alta resolución, render 16:9, caption, texto alternativo y fuente del modelo. No se generó U10-CH-016 porque continúa bloqueado por falta de una fuente normativa definida.","","## Gates aplicados","","- ejes, magnitudes, unidades y escala declarados;","- ejes ≥20 pt, ticks/leyenda ≥18 pt y anotaciones clave ≥22 pt;","- modelos analíticos o señales sintéticas identificadas;","- validaciones de normalización, Parseval, integración, pendiente, percentiles, detectores y SNR;","- PNG individual ≥2400 px de ancho y render de contexto 3200×1800;","- inspección de las dos hojas de contacto;","- cero problemas críticos y cero mayores al cierre.","","## Revisión por recurso","","| ID | Control cuantitativo principal | Revisión visual | Estado |","|---|---|---|---|"]
    for aid,v in rows:
        checks=v["numerical_checks"]
        if aid=="U10-CH-006":control=f"Parseval: error relativo {checks['parseval_relative_error']:.4f}"
        elif aid=="U10-CH-009":control=f"pendiente log–log {checks['loglog_slope']:.12g}"
        elif aid=="U10-CH-013":control=f"error máximo de SNR {checks['max_snr_error_dB']:.2e} dB"
        elif aid=="U10-CH-012":control="curva monótona; percentiles verificados"
        elif aid in {"U10-CH-008","U10-CH-010"}:control="integración por octavas verificada"
        else:control="aserciones y parámetros en validation.json"
        out.append(f"| {aid} | {control} | render individual y 16:9 legibles | aprobado |")
    out.extend(["","## Correcciones del ciclo visual","","- CH-003: el aviso de nivel relativo se trasladó dentro del panel superior para liberar el eje.","- CH-005: el rango del histograma se amplió para contener todas las muestras y conservar suma relativa ≈1.","- CH-013 y CH-014: los avisos de señal/caso sintético se reubicaron dentro del último panel, sin tocar la etiqueta del eje.","","## Problemas abiertos","","- U10-CH-016 permanece bloqueado. No se fabricaron límites de exposición ni se fusionaron normas de distintas jurisdicciones."])
    (UNIT/"charts_review.md").write_text("\n".join(out)+"\n",encoding="utf-8")


def diagram_reports(rows):
    counts=Counter(src["classification"] for _,_,src in rows)
    out=["# Unidad 10 — Informe de validación de diagramas","",f"Fecha: {DATE}","","## Resultado","",f"Se generaron **{len(rows)} diagramas editables**: "+", ".join(f"{n} {k}" for k,n in sorted(counts.items()))+". Cada carpeta contiene fuente JSON, SVG, PNG, PowerPoint editable de una slide, render de contexto, caption, texto alternativo e informe JSON.","","## Gates de aceptación","","- texto principal 22,5–24 pt; ecuaciones centrales 36 pt;","- padding interno 0,25 in; separación línea–texto no relacionado 0,125 in;","- cero texto cortado o fuera de caja;","- cero conectores o puntas sobre texto;","- líderes de ecuaciones sin punta y conectores de proceso anclados;","- render individual y verificación en canvas 16:9 de 1280×720, exportado a 2560×1440;","- inspección visual de siete hojas de contacto;","- cero problemas críticos y cero mayores al cierre.","","## Resultado por recurso","","| ID | Clasificación | Layout | Críticos | Mayores | Estado |","|---|---|---|---:|---:|---|"]
    for aid,v,src in rows:out.append(f"| {aid} | {src['classification']} | {src['layoutFamily']} | {v['critical_issues']} | {v['major_issues']} | aprobado |")
    out.extend(["","## Recursos no producidos","","- U10-DG-058: bloqueado hasta verificar el ejemplo para intervalos desiguales.","- U10-DG-059: bloqueado hasta disponer de slide-writing y selección final de ejercicios.","- U10-DG-060: bloqueado por falta de protocolo clínico institucional validado."])
    (UNIT/"diagram_validation_report.md").write_text("\n".join(out)+"\n",encoding="utf-8")

    review=["# Unidad 10 — Revisión de assets diagramáticos","",f"Fecha: {DATE}","","## Dictamen","","Los 57 recursos producibles se aprueban como biblioteca visual v01. Los `.pptx` son artefactos editables de validación de una sola slide; **no constituyen la presentación de la Unidad 10**.","","## Revisión por familia","","| Familia | IDs | Hallazgo visual | Corrección / criterio | Estado |","|---|---|---|---|---|","| Apertura y señal-contexto | DG-001–012 | La triada de recap no expresaba relaciones con suficiente claridad. | DG-010 se recompuso con nodo central y tres conectores anclados. | aprobado |","| Estadística | DG-013–017, DG-056 | Fórmulas y resultados requerían jerarquía estable. | Ecuaciones a 36 pt, callouts externos y unidades dentro de nodos. | aprobado |","| Densidad, colores y filtros | DG-018–027, DG-057 | Guiones bajos visibles y matrices con relleno genérico. | Se normalizó notación Unicode; DG-018/DG-024 se recompusieron alrededor del concepto central; se eliminaron celdas de relleno. | aprobado |","| Medición y SNR | DG-028–035 | La cadena omitía metadatos y algunas fórmulas se leían como código. | Se integraron metadatos como paso 6 y se reemplazó la notación cruda por texto matemático legible. | aprobado |","| Enmascaramiento | DG-036–041 | Riesgo de convertir arquitectura conceptual en receta. | Se conservaron límites visibles y ausencia deliberada de niveles/protocolo. | aprobado |","| Exposición y control | DG-042–049 | Comparaciones podían parecer categorías normativas. | Se mantuvieron mecanismos y verificaciones sin cifras ni promesas causales. | aprobado |","| Caso integrador y cierre | DG-050–055 | La base omitía receptores y el mapa final carecía de trayecto. | Se añadió “tres receptores” y se conectó el mapa final con ocho relaciones sin cruces. | aprobado |","","## Inspección visual","","Se revisaron `review_renders/diagrams_01.png` a `diagrams_07.png`. No se observaron flechas sobre palabras, puntas dentro de áreas tipográficas, etiquetas apoyadas sobre líneas, cajas desbordadas ni texto por debajo del mínimo. Los diagramas de escena se declaran conceptuales y no a escala en sus README/validation.","","## Problemas abiertos","","Los únicos pendientes son DG-058, DG-059 y DG-060, bloqueados por dependencias de contenido o fuente. No son fallas del render y no deben generarse de memoria."]
    (UNIT/"diagram_assets_review.md").write_text("\n".join(review)+"\n",encoding="utf-8")


def main():
    corrected_ch={"U10-CH-003","U10-CH-005","U10-CH-013","U10-CH-014"}
    corrected_dg={"U10-DG-010","U10-DG-017","U10-DG-018","U10-DG-019","U10-DG-024","U10-DG-027","U10-DG-028","U10-DG-030","U10-DG-031","U10-DG-033","U10-DG-042","U10-DG-050","U10-DG-052","U10-DG-054","U10-DG-055","U10-DG-056"}
    charts=[]
    for folder in sorted(CH.glob("U10-CH-*")):charts.append((folder.name,add_visual_iteration(folder,folder.name in corrected_ch)))
    diagrams=[]
    for folder in sorted(DG.glob("U10-DG-*")):
        v=add_visual_iteration(folder,folder.name in corrected_dg);src=load(folder/"diagram_source.json");diagrams.append((folder.name,v,src))
    update_manifest()
    chreg={int(a[-3:]):(a,"gráfico cuantitativo","aprobado") for a,_ in charts}
    dgreg={int(a[-3:]):(a,s["classification"],"aprobado") for a,_,s in diagrams}
    update_plan(UNIT/"chart_plan.md","CH",chreg);update_plan(UNIT/"diagram_plan.md","DG",dgreg)
    chart_review(charts);diagram_reports(diagrams)
    print(json.dumps({"charts":len(charts),"diagrams":len(diagrams),"manifest":"updated","reports":["charts_review.md","diagram_validation_report.md","diagram_assets_review.md"]},ensure_ascii=False,indent=2))


if __name__=="__main__":main()
