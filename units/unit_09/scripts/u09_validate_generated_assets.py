"""Validación estructural y hojas de contacto de los recursos visuales U09."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


UNIT=Path(__file__).resolve().parents[1]
GENERATED=UNIT/"assets"/"generated"
REVIEW=GENERATED/"_review"
CHART_IDS=[f"U09-CH-{n:03d}" for n in (1,2,3,4,5,6,7,9)]
DIAGRAM_IDS=[f"U09-DG-{n:03d}" for n in range(1,71) if n not in (32,48,67)]


def font(size=28):
    candidates=[Path("C:/Windows/Fonts/arial.ttf"),Path("C:/Windows/Fonts/calibri.ttf")]
    for p in candidates:
        if p.exists(): return ImageFont.truetype(str(p),size)
    return ImageFont.load_default()


def contact_sheet(items:list[tuple[str,Path]],out:Path,cols=3,thumb=(640,360)):
    rows=(len(items)+cols-1)//cols
    cell=(thumb[0],thumb[1]+44)
    sheet=Image.new("RGB",(cols*cell[0],rows*cell[1]),"#D9DCE0")
    draw=ImageDraw.Draw(sheet); f=font(26)
    for i,(label,p) in enumerate(items):
        im=Image.open(p).convert("RGB"); im.thumbnail(thumb,Image.Resampling.LANCZOS)
        x=(i%cols)*cell[0]+(thumb[0]-im.width)//2; y=(i//cols)*cell[1]
        sheet.paste(im,(x,y)); draw.rectangle(((i%cols)*cell[0],y+thumb[1],(i%cols+1)*cell[0],y+cell[1]),fill="white")
        draw.text(((i%cols)*cell[0]+14,y+thumb[1]+7),label,font=f,fill="#3D3D3D")
    sheet.save(out,quality=92)


def main():
    REVIEW.mkdir(parents=True,exist_ok=True)
    report={"charts":[],"diagrams":[],"critical_issues":0,"major_issues":0}
    chart_items=[]
    for cid in CHART_IDS:
        d=GENERATED/"charts"/cid
        required=["figure.svg","figure.png","slide_preview.png","data.csv","parameters.json","README.md","caption.txt","alt_text.txt","source.txt","validation.json"]
        missing=[x for x in required if not (d/x).exists()]
        v=json.loads((d/"validation.json").read_text(encoding="utf-8")) if not missing else {}
        size=Image.open(d/"figure.png").size if (d/"figure.png").exists() else (0,0)
        issues=[]
        if missing: issues.append({"severity":"critical","code":"missing_files","files":missing})
        if size[0]<2400 or size[1]<1350: issues.append({"severity":"major","code":"png_resolution","size":size})
        if v.get("critical_issues") or v.get("major_issues"): issues.append({"severity":"major","code":"asset_validation"})
        report["charts"].append({"asset_id":cid,"png_px":list(size),"issues":issues,"status":"pass" if not issues else "fail"})
        chart_items.append((cid,d/"slide_preview.png"))
    contact_sheet(chart_items,REVIEW/"u09_charts_contact_sheet.png",cols=2,thumb=(960,540))

    diagram_items=[]
    for did in DIAGRAM_IDS:
        d=GENERATED/"diagrams"/did
        required=["figure.svg","figure.png","editable.pptx","diagram_source.json","figure.layout.json","README.md","caption.txt","alt_text.txt","validation.json"]
        missing=[x for x in required if not (d/x).exists()]
        v=json.loads((d/"validation.json").read_text(encoding="utf-8")) if not missing else {}
        size=Image.open(d/"figure.png").size if (d/"figure.png").exists() else (0,0)
        issues=[]
        if missing: issues.append({"severity":"critical","code":"missing_files","files":missing})
        if size!=(2560,1440): issues.append({"severity":"major","code":"render_size","size":size})
        if v.get("critical_issues") or v.get("major_issues"): issues.append({"severity":"major","code":"geometry_validation"})
        if v.get("font_floor",{}).get("node_title_pt",0)<22: issues.append({"severity":"major","code":"font_floor"})
        if v.get("padding_inches",0)<0.18: issues.append({"severity":"major","code":"padding"})
        report["diagrams"].append({"asset_id":did,"png_px":list(size),"object_count":len(v.get("object_ids",[])),"connector_count":len(v.get("connector_ids",[])),"issues":issues,"status":"pass" if not issues else "fail"})
        diagram_items.append((did,d/"figure.png"))
    for i in range(0,len(diagram_items),12):
        contact_sheet(diagram_items[i:i+12],REVIEW/f"u09_diagrams_contact_sheet_{i//12+1:02d}.png",cols=3,thumb=(640,360))
    all_items=report["charts"]+report["diagrams"]
    report["critical_issues"]=sum(1 for x in all_items for i in x["issues"] if i["severity"]=="critical")
    report["major_issues"]=sum(1 for x in all_items for i in x["issues"] if i["severity"]=="major")
    report["status"]="pending_visual_review" if not (report["critical_issues"] or report["major_issues"]) else "failed"
    (REVIEW/"u09_assets_structural_review.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({"charts":len(report["charts"]),"diagrams":len(report["diagrams"]),"critical":report["critical_issues"],"major":report["major_issues"],"status":report["status"]},ensure_ascii=False))


if __name__=="__main__": main()
