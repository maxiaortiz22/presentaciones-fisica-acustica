"""Valida integridad de los visuales U10 y genera contactos para inspección."""

from __future__ import annotations

import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

UNIT=Path(__file__).resolve().parents[1]
GEN=UNIT/"assets"/"generated"
REVIEW=GEN/"review_renders"
REQUIRED_CHART=["figure.svg","figure.png","slide_context.png","data.csv","parameters.json","README.md","caption.txt","alt_text.txt","source.txt","validation.json"]
REQUIRED_DIAGRAM=["figure.svg","figure.png","slide_context.png","editable.pptx","diagram_source.json","figure.layout.json","README.md","caption.txt","alt_text.txt","source.txt","validation.json"]


def font(size):
    try:return ImageFont.truetype("C:/Windows/Fonts/calibri.ttf",size)
    except OSError:return ImageFont.load_default()


def contacts(paths,out_prefix,cols=3,rows=3):
    REVIEW.mkdir(parents=True,exist_ok=True);pages=[];thumb_w,thumb_h=640,360;label_h=44
    for page,start in enumerate(range(0,len(paths),cols*rows),1):
        subset=paths[start:start+cols*rows];sheet=Image.new("RGB",(cols*thumb_w,rows*(thumb_h+label_h)),"#D9DCE0");draw=ImageDraw.Draw(sheet)
        for k,p in enumerate(subset):
            im=Image.open(p).convert("RGB");im.thumbnail((thumb_w,thumb_h),Image.Resampling.LANCZOS);x=(k%cols)*thumb_w+(thumb_w-im.width)//2;y=(k//cols)*(thumb_h+label_h)+(thumb_h-im.height)//2;sheet.paste(im,(x,y));draw.text(((k%cols)*thumb_w+18,(k//cols)*(thumb_h+label_h)+thumb_h+7),p.parent.name,fill="#3D3D3D",font=font(26))
        out=REVIEW/f"{out_prefix}_{page:02d}.png";sheet.save(out);pages.append(str(out.relative_to(UNIT)).replace("\\","/"))
    return pages


def main():
    report={"charts":[],"diagrams":[],"issues":[]}
    charts=sorted((GEN/"charts").glob("U10-CH-*"));diagrams=sorted((GEN/"diagrams").glob("U10-DG-*"))
    for folder,kind,needed in [(x,"chart",REQUIRED_CHART) for x in charts]+[(x,"diagram",REQUIRED_DIAGRAM) for x in diagrams]:
        missing=[n for n in needed if not (folder/n).exists()]
        validation=json.loads((folder/"validation.json").read_text(encoding="utf-8")) if (folder/"validation.json").exists() else {}
        png=Image.open(folder/"figure.png") if (folder/"figure.png").exists() else None
        item={"id":folder.name,"missing":missing,"critical":validation.get("critical_issues"),"major":validation.get("major_issues"),"png_px":list(png.size) if png else None,"status":validation.get("status")}
        report["charts" if kind=="chart" else "diagrams"].append(item)
        if missing or item["critical"] or item["major"]:report["issues"].append(item)
    if len(charts)!=15:report["issues"].append({"code":"chart_count","actual":len(charts),"expected":15})
    if len(diagrams)!=57:report["issues"].append({"code":"diagram_count","actual":len(diagrams),"expected":57})
    report["contact_sheets"]={"charts":contacts([x/"slide_context.png" for x in charts],"charts",3,3),"diagrams":contacts([x/"slide_context.png" for x in diagrams],"diagrams",3,3)}
    report["status"]="approved" if not report["issues"] else "needs_revision"
    (GEN/"visual_validation_summary.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({"charts":len(charts),"diagrams":len(diagrams),"issues":len(report["issues"]),"status":report["status"],"sheets":report["contact_sheets"]},ensure_ascii=False,indent=2))
    raise SystemExit(1 if report["issues"] else 0)


if __name__=="__main__":main()
