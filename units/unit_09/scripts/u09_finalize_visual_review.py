"""Cierra estados después de la inspección visual manual de hojas de contacto."""

from __future__ import annotations

import json
from pathlib import Path


UNIT=Path(__file__).resolve().parents[1]
GEN=UNIT/"assets"/"generated"
CHART_IDS=[f"U09-CH-{n:03d}" for n in (1,2,3,4,5,6,7,9)]
DIAGRAM_IDS=[f"U09-DG-{n:03d}" for n in range(1,71) if n not in (32,48,67)]


def approve(folder:Path,kind:str):
    p=folder/"validation.json"
    data=json.loads(p.read_text(encoding="utf-8"))
    if data.get("critical_issues") or data.get("major_issues"):
        raise RuntimeError(f"No se puede aprobar {data.get('asset_id')}: quedan problemas")
    data["status"]="approved"
    data["visual_review"]={
        "date":"2026-08-12",
        "method":"render individual a tamaño final + hoja de contacto + reinspección de recursos corregidos",
        "critical_issues":0,
        "major_issues":0,
        "result":"approved",
    }
    if kind=="diagram":
        data.setdefault("iterations",[]).append({"iteration":3,"action":"inspección visual en hoja de contacto y revisión individual de familias corregidas","critical":0,"major":0})
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
    readme=folder/"README.md"
    text=readme.read_text(encoding="utf-8")
    text=text.replace("generado; pendiente de cierre de la inspección visual por contacto","aprobado tras inspección visual individual y por hoja de contacto")
    readme.write_text(text,encoding="utf-8")


def main():
    for cid in CHART_IDS: approve(GEN/"charts"/cid,"chart")
    for did in DIAGRAM_IDS: approve(GEN/"diagrams"/did,"diagram")
    chart_validations=[json.loads((GEN/"charts"/cid/"validation.json").read_text(encoding="utf-8")) for cid in CHART_IDS]
    diagram_validations=[json.loads((GEN/"diagrams"/did/"validation.json").read_text(encoding="utf-8")) for did in DIAGRAM_IDS]
    (GEN/"charts"/"generation_summary.json").write_text(json.dumps(chart_validations,ensure_ascii=False,indent=2),encoding="utf-8")
    (GEN/"diagrams"/"generation_summary.json").write_text(json.dumps(diagram_validations,ensure_ascii=False,indent=2),encoding="utf-8")
    review_path=GEN/"_review"/"u09_assets_structural_review.json"
    review=json.loads(review_path.read_text(encoding="utf-8"))
    if review.get("critical_issues") or review.get("major_issues"):
        raise RuntimeError("La revisión estructural aún contiene problemas")
    review["status"]="approved"
    review["visual_review"]={"date":"2026-08-12","contact_sheets":7,"result":"approved","critical_issues":0,"major_issues":0}
    review_path.write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding="utf-8")
    summary={"date":"2026-08-12","charts_approved":len(CHART_IDS),"diagrams_approved":len(DIAGRAM_IDS),"charts_conditioned_not_generated":["U09-CH-008","U09-CH-010","U09-CH-011"],"diagrams_conditioned_not_generated":["U09-DG-032","U09-DG-048","U09-DG-067"],"critical_issues":0,"major_issues":0,"status":"approved"}
    (GEN/"_review"/"u09_visual_approval_summary.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(summary,ensure_ascii=False))


if __name__=="__main__": main()
