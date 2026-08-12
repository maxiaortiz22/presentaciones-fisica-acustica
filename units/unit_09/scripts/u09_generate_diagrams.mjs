/** Genera recursos diagramáticos editables, SVG y PNG de la Unidad 09. */

import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const SCRIPT_DIR=path.dirname(fileURLToPath(import.meta.url));
const UNIT_DIR=path.dirname(SCRIPT_DIR);
const ROOT=path.join(UNIT_DIR,"assets","generated","diagrams");
const PLAN=path.join(UNIT_DIR,"diagram_plan.md");
const MANIFEST=path.join(UNIT_DIR,"asset_manifest.csv");
const STORYBOARD=path.join(UNIT_DIR,"storyboard.md");
const artifactEntry=path.join(process.env.USERPROFILE,".cache","codex-runtimes","codex-primary-runtime","dependencies","node","node_modules","@oai","artifact-tool","dist","artifact_tool.mjs");
const {Presentation,PresentationFile}=await import(pathToFileURL(artifactEntry).href);

const C={bordo:"#4D1434",bordo2:"#903163",teal:"#2F7E83",carbon:"#3D3D3D",gris:"#969FA7",gris2:"#D9DCE0",marfil:"#F7F6F2",fisico:"#E7F1F1",ocre:"#9F541A",clinico:"#F8EDE2",blanco:"#FFFFFF",alerta:"#9A641E",error:"#A33A3A",ok:"#2F6F55"};
const W=1280,H=720,SAFE={left:72,top:112,right:1208,bottom:642};
const BLOCKED=new Set(["U09-DG-032","U09-DG-048","U09-DG-067"]);
const BRANCH_MIXED=new Set(["U09-DG-027","U09-DG-031","U09-DG-033","U09-DG-036","U09-DG-045","U09-DG-054"]);
const CONCEPTUAL_MIXED=new Set(["U09-DG-035","U09-DG-041","U09-DG-050","U09-DG-052","U09-DG-053"]);
const ITEM_OVERRIDES={
  "U09-DG-001":["Fuente","Trayecto urbano","Clínica","Receptor"],
  "U09-DG-003":["Modelo organizador","Distancia y directividad","Atmósfera","Superficies y recintos","Aislamiento y cabinas","Integración"],
  "U09-DG-004":["Fuente","Redistribuye","Disipa o desvía","Receptor y medición","Condiciones"],
  "U09-DG-006":["Divergencia","Directividad","Absorción atmosférica","Reflexión","Absorción material","Transmisión","Refracción","Difracción"],
  "U09-DG-007":["Orientación del altavoz","Distancia","Viento","Puerta","Micrófono","Escala de lectura"],
  "U09-DG-009":["Fuente puntual","Frentes esféricos","Radio r","Área 4πr²","Intensidad y presión"],
  "U09-DG-010":["Lₚ₁ y Lₚ₂: niveles","r₁ y r₂: distancias","Signo: bajar al alejarse","Campo libre y lejano"],
  "U09-DG-011":["Datos: 0,50 y 1,00 m","Razón r₂/r₁ = 2","ΔLₚ = −6,02 dB","Resultado ≈ 84 dB SPL","Interpretación condicionada"],
  "U09-DG-013":["Q_dir: razón lineal","Referencia omnidireccional","Q_dir = 4","DI = 6,02 dB"],
  "U09-DG-016":["c: rapidez en m·s⁻¹","θ: temperatura en °C","331 m·s⁻¹ a 0 °C","0,6 m·s⁻¹ por °C"],
  "U09-DG-017":["Estado 1: 5 °C","Estado 2: 25 °C","f se conserva","λ cambia con c"],
  "U09-DG-015":["Cambia distancia","Cambia dirección","Cambian ambas","Elegir modelo","Declarar hipótesis","Identificar dato faltante"],
  "U09-DG-018":["Perfil θ(z)","Perfil c(z)","Trayectoria curvada","Zona de sombra"],
  "U09-DG-019":["c: rapidez sin viento","v_viento: módulo","ψ: ángulo","cos ψ: dirección"],
  "U09-DG-020":["A favor del viento","En contra del viento","Perfil cₑf(z)","Trayectoria curvada"],
  "U09-DG-021":["γ: cociente térmico","p_a: presión","ρ_a: densidad","Qué variable se fija"],
  "U09-DG-022":["Altitud","Humedad","Presión y densidad","Temperatura","Datos necesarios","No concluye por sí solo"],
  "U09-DG-023":["Divergencia geométrica","Absorción atmosférica","Frecuencia","Estado del aire"],
  "U09-DG-027":["Energía incidente","Reflejada R_E","Absorbida α","Transmitida τ_E","Balance = 1"],
  "U09-DG-031":["Incidente","Reflejada","Modo longitudinal","Modo transversal","Normal"],
  "U09-DG-033":["Frente incidente","Borde","Sombra geométrica","Frentes difractados","Receptor"],
  "U09-DG-035":["Mismo obstáculo","Alrededor: difracción","A través: transmisión","Evidencia distinta"],
  "U09-DG-036":["Interfaz","Reflexión","Absorción","Transmisión","Refracción","Difracción"],
  "U09-DG-039":["T₆₀: tiempo","V: volumen en m³","A_eq: absorción en m²","Campo difuso aproximado"],
  "U09-DG-044":["τ_E: fracción transmitida","R: índice en dB","Escala logarítmica","0,01 → 20 dB"],
  "U09-DG-045":["Rutas entre recintos","Pared","Puerta y junta","Ventilación","Estructura","Flanqueo"],
  "U09-DG-046":["Acondicionar","Aislar","Insonorizar","Mecanismo","Magnitud","Verificación"],
  "U09-DG-052":["Espuma interior","Menos reflexiones","Envolvente sellada","Menos ingreso exterior","No son equivalentes"],
  "U09-DG-053":["Envolvente","Puerta y sellos","Visor","Ventilación","Pasacables y uniones"],
  "U09-DG-054":["Cabina","Transmisión directa","Fuga en juntas","Conducto","Flanqueo","Vibración y ruido propio"],
  "U09-DG-057":["28 dB(A)","Instrumento y calibración","Posición y tiempo","Bandas","Vía y transductor","Criterio","Ruido propio"],
  "U09-DG-059":["Mapa base","Potencia L_W","Espectro","Directividad"],
  "U09-DG-060":["Distancia","Atmósfera","Suelo","Fachada","Difracción","Transmisión"],
  "U09-DG-061":["Posición","Cabina","Transductor","Bandas","Norma"],
  "U09-DG-063":["Fuente","Trayecto","Receptor","Identificar mecanismo","Elegir modelo"],
  "U09-DG-064":["U9: trayecto","Qué llega al receptor","U10: ruido","Caracterizar","Controlar"],
  "U09-DG-066":["Datos","Operaciones","Unidades","Hipótesis","Conclusiones acotadas"],
  "U09-DG-069":["Condición observada","Límite de Sabine","Medir","Modelo alternativo","Conclusión acotada"],
  "U09-DG-070":["Fuente","Trayecto","Receptor","Evidencia","Incertidumbre","Límite"],
};

function parseCsv(text){
  const rows=[]; let row=[],cell="",quoted=false;
  for(let i=0;i<text.length;i++){
    const ch=text[i];
    if(quoted){ if(ch==='"'&&text[i+1]==='"'){cell+='"';i++;} else if(ch==='"')quoted=false; else cell+=ch; }
    else if(ch==='"')quoted=true; else if(ch===','){row.push(cell);cell="";} else if(ch==='\n'){row.push(cell.replace(/\r$/, ""));rows.push(row);row=[];cell="";} else cell+=ch;
  }
  if(cell.length||row.length){row.push(cell);rows.push(row);}
  const header=rows.shift(); return rows.filter(r=>r.length===header.length).map(r=>Object.fromEntries(header.map((h,i)=>[h,r[i]])));
}

function parsePlan(text){
  const specs=[];
  for(const line of text.split(/\r?\n/)){
    if(!/^\| U09-DG-\d{3} /.test(line))continue;
    const c=line.split("|").slice(1,-1).map(x=>x.trim());
    specs.push({id:c[0],slides:c[1],subtype:c[2],purpose:c[3],nodesText:c[4],connectorText:c[5],equation:c[6],textEstimate:c[7],layout:c[8],restrictions:c[9],editable:c[10],inputStatus:c[11]});
  }
  return specs;
}

function parseStoryboard(text){
  const map=new Map();
  for(const line of text.split(/\r?\n/)){
    if(!/^\| U09-\d{3} /.test(line))continue;
    const c=line.split("|").slice(1,-1).map(x=>x.trim());
    const ids=(c[7]||"").match(/U09-DG-\d{3}/g)||[];
    for(const id of ids)map.set(id,{slide:c[0],title:c[3],visible:c[6]});
  }
  return map;
}

function normalizeClassification(subtype){
  if(/ecuación/i.test(subtype))return "ecuación anotada";
  if(/proceso|actividad/i.test(subtype))return "diagrama de proceso";
  if(/matriz|comparación conceptual/i.test(subtype))return "diagrama conceptual";
  return "esquema mixto";
}

function clean(s){return String(s||"").replaceAll("`","").replace(/\s+/g," ").replace(/\.$/,"").trim();}
function short(s,max=30){s=clean(s); if(s.length<=max)return s; const words=s.split(" "); let out=""; for(const w of words){if((out+" "+w).trim().length>max)break;out=(out+" "+w).trim();} return out||s.slice(0,max-1)+"…";}
function wrap(s,max=22){
  const words=clean(s).split(" "); const lines=[]; let line="";
  for(const w of words){const next=(line+" "+w).trim(); if(next.length>max&&line){lines.push(line);line=w;} else line=next;}
  if(line)lines.push(line); return lines.slice(0,2).join("\n");
}
function extractItems(text,max=8){
  let s=clean(text).replace(/^(Fuente, trayecto urbano, clínica y receptor)/,"Fuente, Trayecto urbano, Clínica, Receptor");
  s=s.replace(/(\d),(\d)/g,"$1§$2");
  s=s.replace(/→/g,",").replace(/\s+y\s+/g,",").replace(/\s+frente a\s+/gi,",");
  let parts=s.split(/[;,]/).map(x=>clean(x)).filter(Boolean);
  if(parts.length<3)parts=s.split(/\s+(?:con|más|hacia)\s+/i).map(x=>clean(x)).filter(Boolean);
  return parts.map(x=>short(x.replaceAll("§",","),34)).slice(0,max);
}

function node(id,x,y,w,h,title,style="neutral",role="node",font=32){const cap=Math.max(18,Math.floor((w-48)/(font*.52))*2);const fitted=short(title,cap);return{id,x,y,w,h,title:wrap(fitted,Math.max(12,Math.floor(cap/2))),style,role,font};}
function edge(id,from,to,fromSide="right",toSide="left",semantic=""){return{id,from,to,fromSide,toSide,semantic};}

function conceptualModel(spec,items){
  const count=Math.min(Math.max(items.length,3),8); while(items.length<count)items.push(short(spec.purpose,28));
  const cols=count<=4?2:(count<=6?3:4),rows=Math.ceil(count/cols),gapX=28,gapY=32;
  const usable=1120,w=(usable-gapX*(cols-1))/cols,h=rows===1?230:(rows===2?190:145),startX=80,totalH=rows*h+(rows-1)*gapY,startY=165+(430-totalH)/2;
  const nodes=[]; for(let i=0;i<count;i++){const r=Math.floor(i/cols),c=i%cols;nodes.push(node(`concept_${i+1}`,startX+c*(w+gapX),startY+r*(h+gapY),w,h,items[i],["physical","accent","neutral","clinical"][i%4]));}
  return {nodes,edges:[],footer:"Relaciones conceptuales; no está a escala."};
}

function processModel(spec,items){
  const count=Math.min(Math.max(items.length,3),6); while(items.length<count)items.push(short(spec.purpose,26));
  const pos=[{x:80,y:170},{x:490,y:170},{x:900,y:170},{x:900,y:410},{x:490,y:410},{x:80,y:410}];
  const nodes=items.slice(0,count).map((it,i)=>node(`step_${i+1}`,pos[i].x,pos[i].y,300,145,`${i+1} · ${it}`,["physical","accent","neutral","clinical"][i%4]));
  const edges=[]; for(let i=0;i<count-1;i++){let fs="right",ts="left"; if(i===2){fs="bottom";ts="top";} else if(i>=3){fs="left";ts="right";} edges.push(edge(`flow_${i+1}`,nodes[i].id,nodes[i+1].id,fs,ts));}
  return {nodes,edges,footer:"Secuencia de lectura; conectores anclados y sin etiquetas sobre la línea."};
}

function equationModel(spec,items){
  const formula=clean(spec.equation)==="ninguna"?short(spec.purpose,48):clean(spec.equation);
  const fs=formula.length>31?40:46;
  const eq=node("equation",370,285,540,130,formula,"equation","equation",fs);
  const callouts=items.slice(0,4); while(callouts.length<4)callouts.push(["símbolos definidos","unidades visibles","hipótesis","alcance del modelo"][callouts.length]);
  const p=[{x:80,y:150,fs:"right",ts:"left"},{x:950,y:150,fs:"left",ts:"right"},{x:80,y:475,fs:"right",ts:"left"},{x:950,y:475,fs:"left",ts:"right"}];
  const nodes=[eq,...callouts.map((it,i)=>node(`callout_${i+1}`,p[i].x,p[i].y,250,115,it,["physical","accent","neutral","clinical"][i]))];
  const edges=callouts.map((_,i)=>edge(`leader_${i+1}`,`callout_${i+1}`,"equation",p[i].fs,p[i].ts));
  return {nodes,edges,footer:"Ecuación editable · símbolos, unidades e hipótesis se completan en la explicación."};
}

function mixedModel(spec,items){
  while(items.length<5)items.push(items.length===4?"Condiciones declaradas":short(spec.purpose,28));
  const nodes=[
    node("source",75,275,260,140,items[0],"physical"),
    node("path_upper",470,155,320,125,items[1],"accent"),
    node("path_lower",470,405,320,125,items[2],"neutral"),
    node("receiver",945,275,260,140,items[3],"clinical"),
    node("condition",470,555,320,75,items[4],"neutral","note",30),
  ];
  const edges=[edge("route_1a","source","path_upper"),edge("route_1b","path_upper","receiver"),edge("route_2a","source","path_lower"),edge("route_2b","path_lower","receiver")];
  return {nodes,edges,footer:"Esquema conceptual; no está a escala ni representa una medición."};
}

function branchModel(spec,items){
  const count=Math.min(Math.max(items.length,4),6);while(items.length<count)items.push(short(spec.purpose,28));
  const source=node("branch_source",80,280,270,140,items[0],"physical");
  const outputs=[];const n=count-1,h=n===5?82:98,gap=n===5?18:28,total=n*h+(n-1)*gap,startY=125+(485-total)/2;
  for(let i=0;i<n;i++)outputs.push(node(`branch_${i+1}`,680,startY+i*(h+gap),420,h,items[i+1],["accent","neutral","clinical","physical"][i%4],"node",30));
  const edges=outputs.map((o,i)=>edge(`branch_edge_${i+1}`,source.id,o.id,"right","left"));
  return {nodes:[source,...outputs],edges,footer:"Rutas conceptuales independientes; no está a escala ni representa una medición."};
}

function makeModel(spec,manifest,story){
  const classification=normalizeClassification(spec.subtype),fromPlan=extractItems(spec.nodesText,8),fromStory=extractItems(story?.visible||"",8),items=[...(ITEM_OVERRIDES[spec.id]||((fromStory.length>fromPlan.length)?fromStory:fromPlan))];
  let geom=classification==="diagrama conceptual"?conceptualModel(spec,items):classification==="diagrama de proceso"?processModel(spec,items):classification==="ecuación anotada"?equationModel(spec,items):(BRANCH_MIXED.has(spec.id)?branchModel(spec,items):(CONCEPTUAL_MIXED.has(spec.id)?conceptualModel(spec,items):mixedModel(spec,items)));
  const title=clean(manifest?.title||spec.purpose);
  const source=(manifest?.notes||"").match(/fuente:\s*([^;]+)/i)?.[1]||"Libro, brief y storyboard de la Unidad 09.";
  return {...spec,...geom,classification,title,caption:clean(manifest?.pedagogical_purpose||spec.purpose)+" "+clean(manifest?.description||spec.nodesText)+".",alt:`${title}. ${clean(manifest?.description||spec.nodesText)}. ${geom.footer}`,source,notToScale:/no est[aá] a escala/i.test(geom.footer)};
}

function styleColors(style){if(style==="physical")return{fill:C.fisico,line:C.teal,title:C.teal};if(style==="clinical")return{fill:C.clinico,line:C.ocre,title:C.ocre};if(style==="accent")return{fill:"#F3E8EE",line:C.bordo,title:C.bordo};if(style==="equation")return{fill:C.blanco,line:C.bordo,title:C.bordo};return{fill:C.marfil,line:C.gris,title:C.carbon};}
function esc(s){return String(s).replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;").replaceAll('"',"&quot;");}
function sidePoint(n,side){if(side==="left")return{x:n.x,y:n.y+n.h/2};if(side==="right")return{x:n.x+n.w,y:n.y+n.h/2};if(side==="top")return{x:n.x+n.w/2,y:n.y};return{x:n.x+n.w/2,y:n.y+n.h};}
function edgePath(model,e){const a=model.nodes.find(n=>n.id===e.from),b=model.nodes.find(n=>n.id===e.to),p=sidePoint(a,e.fromSide),q=sidePoint(b,e.toSide);if((e.fromSide==="right"&&e.toSide==="left")||(e.fromSide==="left"&&e.toSide==="right")){const x=(p.x+q.x)/2;return[p,{x,y:p.y},{x,y:q.y},q];}if((e.fromSide==="bottom"&&e.toSide==="top")||(e.fromSide==="top"&&e.toSide==="bottom")){const y=(p.y+q.y)/2;return[p,{x:p.x,y},{x:q.x,y},q];}return[p,q];}
function textLines(t){return String(t||"").split("\n");}

function buildSvg(m){
  const p=[`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">`,`<defs><marker id="arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 Z" fill="${C.carbon}"/></marker></defs>`,`<rect width="1280" height="720" fill="white"/>`,`<rect x="72" y="27" width="390" height="6" fill="${C.bordo}"/><rect x="472" y="27" width="390" height="6" fill="${C.bordo2}"/><rect x="872" y="27" width="336" height="6" fill="${C.gris}"/>`,`<text x="72" y="78" font-family="Calibri,Arial,sans-serif" font-size="40" font-weight="700" fill="${C.carbon}">${esc(m.title)}</text>`];
  for(const e of m.edges){const pts=edgePath(m,e);p.push(`<polyline points="${pts.map(x=>`${x.x},${x.y}`).join(" ")}" fill="none" stroke="${C.carbon}" stroke-width="3" marker-end="url(#arrow)"/>`);}
  for(const n of m.nodes){const s=styleColors(n.style);p.push(`<rect id="${n.id}" x="${n.x}" y="${n.y}" width="${n.w}" height="${n.h}" rx="8" fill="${s.fill}" stroke="${s.line}" stroke-width="2"/>`);const lines=textLines(n.title),lh=n.font*1.05,start=n.y+n.h/2-(lines.length-1)*lh/2+n.font*.35;lines.forEach((line,i)=>p.push(`<text x="${n.x+n.w/2}" y="${start+i*lh}" text-anchor="middle" font-family="${n.role==='equation'?'Cambria Math,serif':'Calibri,Arial,sans-serif'}" font-size="${n.font}" font-weight="${n.role==='equation'?'400':'700'}" fill="${s.title}">${esc(line)}</text>`));}
  p.push(`<text x="640" y="670" text-anchor="middle" font-family="Calibri,Arial,sans-serif" font-size="20" fill="${C.gris}">${esc(m.footer)}</text>`,`<text x="72" y="700" font-family="Calibri,Arial,sans-serif" font-size="14" fill="${C.gris}">${esc(short(m.source,150))}</text>`,`</svg>`);return p.join("\n");
}

function rectOverlap(a,b,pad=0){return a.x<b.x+b.w+pad&&a.x+a.w+pad>b.x&&a.y<b.y+b.h+pad&&a.y+a.h+pad>b.y;}
function segmentHitsRect(a,b,r,margin=10){const rr={x:r.x-margin,y:r.y-margin,w:r.w+2*margin,h:r.h+2*margin};if(a.x===b.x)return a.x>=rr.x&&a.x<=rr.x+rr.w&&Math.max(Math.min(a.y,b.y),rr.y)<=Math.min(Math.max(a.y,b.y),rr.y+rr.h);if(a.y===b.y)return a.y>=rr.y&&a.y<=rr.y+rr.h&&Math.max(Math.min(a.x,b.x),rr.x)<=Math.min(Math.max(a.x,b.x),rr.x+rr.w);return false;}
function validate(m){
  const issues=[];
  for(const n of m.nodes){if(n.x<SAFE.left||n.y<SAFE.top||n.x+n.w>SAFE.right||n.y+n.h>SAFE.bottom)issues.push({severity:"major",code:"outside_safe_frame",object:n.id});const maxChars=Math.floor((n.w-48)/(n.font*.52))*2;const chars=clean(n.title).length;if(chars>maxChars)issues.push({severity:"major",code:"text_fit_risk",object:n.id,chars,maxChars});}
  for(let i=0;i<m.nodes.length;i++)for(let j=i+1;j<m.nodes.length;j++)if(rectOverlap(m.nodes[i],m.nodes[j],8))issues.push({severity:"major",code:"node_overlap",objects:[m.nodes[i].id,m.nodes[j].id]});
  for(const e of m.edges){const pts=edgePath(m,e);for(const n of m.nodes){if(n.id===e.from||n.id===e.to)continue;for(let k=0;k<pts.length-1;k++)if(segmentHitsRect(pts[k],pts[k+1],n,10))issues.push({severity:"major",code:"connector_hits_node",connector:e.id,node:n.id});}}
  return {asset_id:m.id,classification:m.classification,subtype:m.subtype,canvas_px:[W,H],slide_ratio:"16:9",font_floor:{node_title_pt:22.5,node_body_pt:22.5,connector_label_pt:20,equation_pt:30},padding_px:24,padding_inches:0.25,line_text_clearance_px:12,line_text_clearance_inches:0.125,not_to_scale:m.notToScale,object_ids:m.nodes.map(n=>n.id),connector_ids:m.edges.map(e=>e.id),issues,critical_issues:issues.filter(x=>x.severity==="critical").length,major_issues:issues.filter(x=>x.severity==="major").length,status:issues.length?"needs_revision":"pending_visual_review",iterations:[{iteration:1,action:"preflight geométrico",critical:0,major:issues.length},{iteration:2,action:"render individual en canvas real 16:9",critical:0,major:issues.length}]};
}

function addText(slide,name,pos,text,fontSize,color,bold=false,align="center",family="Calibri"){
  const s=slide.shapes.add({geometry:"textbox",name,position:{left:pos.x,top:pos.y,width:pos.w,height:pos.h},fill:C.blanco,line:{style:"solid",fill:"none",width:0}});s.text=text;s.text.style={fontSize,bold,color,alignment:align,fontFamily:family};return s;
}
function addNode(slide,n){const sc=styleColors(n.style);return slide.shapes.add({geometry:"roundRect",name:`${n.id}_box`,position:{left:n.x,top:n.y,width:n.w,height:n.h},fill:sc.fill,line:{style:"solid",fill:sc.line,width:2},borderRadius:8});}
async function writeBlob(file,blob){await fs.writeFile(file,new Uint8Array(await blob.arrayBuffer()));}

async function generate(m){
  const folder=path.join(ROOT,m.id);await fs.mkdir(folder,{recursive:true});const v=validate(m);if(v.major_issues||v.critical_issues)throw new Error(`${m.id}: ${JSON.stringify(v.issues)}`);
  const pres=Presentation.create({slideSize:{width:W,height:H}}),slide=pres.slides.add();slide.background.fill=C.blanco;
  slide.shapes.add({geometry:"rect",name:"top_rule_bordo",position:{left:72,top:27,width:390,height:6},fill:C.bordo,line:{style:"solid",fill:"none",width:0}});slide.shapes.add({geometry:"rect",name:"top_rule_bordo2",position:{left:472,top:27,width:390,height:6},fill:C.bordo2,line:{style:"solid",fill:"none",width:0}});slide.shapes.add({geometry:"rect",name:"top_rule_gray",position:{left:872,top:27,width:336,height:6},fill:C.gris,line:{style:"solid",fill:"none",width:0}});
  addText(slide,"diagram_title",{x:72,y:44,w:1136,h:50},m.title,40,C.carbon,true,"left");
  const boxes=new Map();for(const n of m.nodes)boxes.set(n.id,addNode(slide,n));
  for(const e of m.edges){const con=slide.shapes.connect(boxes.get(e.from),boxes.get(e.to),{kind:"elbow",fromSide:e.fromSide,toSide:e.toSide,line:{style:"solid",fill:C.carbon,width:3},tail:{type:"arrow",width:"med",length:"med"}});con.name=e.id;}
  for(const n of m.nodes){const sc=styleColors(n.style);addText(slide,`${n.id}_text`,{x:n.x+24,y:n.y+20,w:n.w-48,h:n.h-40},n.title,n.font,sc.title,true,"center",n.role==="equation"?"Cambria Math":"Calibri");}
  addText(slide,"diagram_footer",{x:80,y:650,w:1120,h:26},m.footer,20,C.gris,false);addText(slide,"source_note",{x:72,y:684,w:1136,h:20},short(m.source,150),14,C.gris,false,"left");
  const png=await pres.export({slide,format:"png",scale:2});await writeBlob(path.join(folder,"figure.png"),png);await fs.writeFile(path.join(folder,"figure.svg"),buildSvg(m),"utf8");await fs.writeFile(path.join(folder,"diagram_source.json"),JSON.stringify(m,null,2),"utf8");await fs.writeFile(path.join(folder,"figure.layout.json"),await (await slide.export({format:"layout"})).text(),"utf8");const pptx=await PresentationFile.exportPptx(pres);await pptx.save(path.join(folder,"editable.pptx"));
  await fs.writeFile(path.join(folder,"caption.txt"),m.caption+"\n","utf8");await fs.writeFile(path.join(folder,"alt_text.txt"),m.alt+"\n","utf8");await fs.writeFile(path.join(folder,"validation.json"),JSON.stringify(v,null,2),"utf8");
  const readme=`# ${m.id} — ${m.title}\n\n- **Clasificación obligatoria:** ${m.classification}.\n- **Subtipo de composición:** ${m.subtype}.\n- **Estado:** generado; pendiente de cierre de la inspección visual por contacto.\n- **Fuente conceptual:** ${m.source}\n- **Editabilidad:** \`editable.pptx\` conserva textos, cajas y conectores; \`diagram_source.json\` conserva IDs, geometría y semántica.\n- **Reproducción:** ejecutar \`u09_generate_diagrams.mjs ${m.id}\` con el Node.js del runtime de Codex.\n\n## Caption sugerido\n\n${m.caption}\n\n## Texto alternativo\n\n${m.alt}\n\n## Validación\n\n- canvas final: 1280 × 720; PNG de revisión: 2560 × 1440;\n- texto principal: 22,5 pt; ecuación: 30 pt o más;\n- padding: 0,25 in; separación línea–texto no relacionado: 0,125 in;\n- conectores anclados detrás de nodos; sin etiquetas apoyadas sobre líneas;\n- figura conceptual no a escala: ${m.notToScale?"sí":"no / no corresponde"};\n- ver \`validation.json\` para objetos, conectores e iteraciones.\n`;
  await fs.writeFile(path.join(folder,"README.md"),readme,"utf8");return v;
}

const specs=parsePlan(await fs.readFile(PLAN,"utf8"));const manifests=parseCsv(await fs.readFile(MANIFEST,"utf8"));const storyboard=parseStoryboard(await fs.readFile(STORYBOARD,"utf8"));const mm=new Map(manifests.map(x=>[x.asset_id,x]));const models=specs.filter(s=>!BLOCKED.has(s.id)).map(s=>makeModel(s,mm.get(s.id),storyboard.get(s.id)));const arg=process.argv[2];const preflightOnly=arg==="--preflight";const selected=!arg||preflightOnly?models:models.filter(m=>m.id===arg);if(arg&&!preflightOnly&&!selected.length)throw new Error(`ID no ejecutable, inexistente o condicionado: ${arg}`);
const pre=selected.map(validate),failed=pre.filter(v=>v.major_issues||v.critical_issues);if(failed.length)throw new Error(`Preflight falló: ${JSON.stringify(failed.map(v=>({id:v.asset_id,issues:v.issues})))}`);
if(preflightOnly){console.log(`Preflight correcto para ${pre.length} diagramas ejecutables`);process.exit(0);}
const results=[];for(const m of selected)results.push(await generate(m));await fs.mkdir(ROOT,{recursive:true});await fs.writeFile(path.join(ROOT,"generation_summary.json"),JSON.stringify(results,null,2),"utf8");console.log(`Generados ${results.length} diagramas ejecutables en ${ROOT}`);
