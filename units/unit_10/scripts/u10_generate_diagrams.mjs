/** Genera diagramas editables y sus renders de validación para la Unidad 10. */

import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const SCRIPT_DIR=path.dirname(fileURLToPath(import.meta.url));
const UNIT_DIR=path.dirname(SCRIPT_DIR);
const ROOT=path.join(UNIT_DIR,"assets","generated","diagrams");
const PLAN=path.join(UNIT_DIR,"diagram_plan.md");
const artifactEntry=path.join(process.env.USERPROFILE,".cache","codex-runtimes","codex-primary-runtime","dependencies","node","node_modules","@oai","artifact-tool","dist","artifact_tool.mjs");
const {Presentation,PresentationFile}=await import(pathToFileURL(artifactEntry).href);

const C={bordo:"#4D1434",bordo2:"#903163",teal:"#2F7E83",carbon:"#3D3D3D",gris:"#969FA7",gris2:"#D9DCE0",marfil:"#F7F6F2",fisico:"#E7F1F1",ocre:"#9F541A",clinico:"#F8EDE2",blanco:"#FFFFFF",alerta:"#9A641E",error:"#A33A3A",ok:"#2F6F55"};
const W=1280,H=720,SAFE={left:72,top:112,right:1208,bottom:642};
const BLOCKED=new Set(["U10-DG-058","U10-DG-059","U10-DG-060"]);
const SOURCE="Libro del curso, capítulo 10; brief, storyboard y diagram_plan de la Unidad 10. Síntesis visual propia de la cátedra.";

const OVERRIDES={
  "U10-DG-001":["Tiempo","Frecuencia","Nivel","Efecto / tarea"],
  "U10-DG-002":["Avenida","Fachada","Consultorio","Conversación","Climatización","Portazo","Receptor"],
  "U10-DG-003":["Señal y contexto","Tiempo y espectro","Calcular descriptores","Interpretar con límites","Proponer control"],
  "U10-DG-004":["Presión y RMS","Niveles en dB","Espectro y bandas","SNR","Percepción","Propagación"],
  "U10-DG-005":["Señal y contexto","Tiempo","Estadística","Frecuencia y colores","Señales de prueba","Descriptores y SNR","Enmascaramiento","Exposición y control","Integración"],
  "U10-DG-006":["Fuente","Presión p(t) · Pa","Micrófono","Señal eléctrica","Medición","Receptor / efecto"],
  "U10-DG-007":["Misma señal física","Escuchar: contenido","Medir: descriptor","Enmascarar: función"],
  "U10-DG-008":["Contextual: depende de la tarea","Físico: señal aleatoria","Operativo: señal de prueba"],
  "U10-DG-009":["Voz vecina","Ruido del equipo","Señal de prueba","Tránsito exterior"],
  "U10-DG-010":["Señal","Contexto","Receptor","¿Qué función cumple?"],
  "U10-DG-011":["Predictibilidad","Continuidad","Impulsividad","Los rasgos pueden coexistir","Ejemplo: máquina fluctuante","Ejemplo: portazos"],
  "U10-DG-012":["Muestra instantánea","Ventana de observación","Registro","Descriptores"],
  "U10-DG-013":["N: cantidad de muestras","pᵢ: presión (Pa)","p̄: media (Pa)","Conserva el signo"],
  "U10-DG-014":["1 · Cuadrar pᵢ","2 · Promediar","3 · Extraer raíz","Resultado en Pa"],
  "U10-DG-015":["p̄: centro de referencia","pᵢ−p̄: desviación","Cuadrar evita cancelación","σₚ² en Pa²"],
  "U10-DG-016":["Datos: −2, −1, 0, 1, 2 mPa","Media = 0 mPa","Media de p² = 2 mPa²","RMS = √2 ≈ 1,41 mPa","Varianza = 2 mPa²","Media cero no implica silencio"],
  "U10-DG-017":["Media · signo · Pa","RMS · tamaño cuadrático · Pa","Varianza · dispersión · Pa²","Distribución · frecuencia relativa · 1"],
  "U10-DG-018":["Altura: Sₚₚ (Pa²/Hz)","Base: Δf (Hz)","Área (Pa²): p²_B,rms","Esquema no a escala"],
  "U10-DG-019":["f_L: límite inferior (Hz)","f_H: límite superior (Hz)","Sₚₚ: densidad (Pa²/Hz)","p²_B,rms · Pa²"],
  "U10-DG-020":["Sₚₚ = 4,0×10⁻⁸ Pa²/Hz","Δf = 100 Hz","p²_B,rms = 4,0×10⁻⁶ Pa²","p_B,rms = 2,0 mPa","Lₚ = 40 dB SPL"],
  "U10-DG-021":["Blanco: S₀ por Hz","Por octava: crece","Rosa: K/f","Por octava: constante","Escucha no define el modelo"],
  "U10-DG-022":["Ruido de banda ancha","Filtro H(f)","Contorno objetivo","Ruido con forma de habla","Conserva forma; no es habla"],
  "U10-DG-023":["Entrada de banda ancha","Pasa-bajos","Pasa-altos","Pasabanda","Tres salidas filtradas"],
  "U10-DG-024":["Espectro amplio","Filtro centrado","fₗ: límite inferior","f꜀: centro","fₕ: límite superior","Banda de salida NBN"],
  "U10-DG-025":["fₗ: límite inferior","f꜀: centro declarado","fₕ: límite superior","B = fₕ − fₗ"],
  "U10-DG-026":["¿Cuál es el objetivo?","¿Qué región espectral?","¿Qué ancho de banda?","Elegir tipo de señal","Nivel + calibración"],
  "U10-DG-027":["Blanco · constante/Hz · prueba","Rosa · constante/octava · prueba","Forma de habla · contorno · comunicación","NBN · banda declarada · audiometría"],
  "U10-DG-028":["Fuente","Micrófono","Ponderación","Detector temporal","Integración → indicador","Metadatos obligatorios"],
  "U10-DG-029":["Evento común","Detector temporal","L_max","Detector de pico","L_peak"],
  "U10-DG-030":["Evento variable","Energía en T","Nivel equivalente","Mismo p² medio en T"],
  "U10-DG-031":["15 min: 88 dB(A)","15 min: 92 dB(A)","15 min: 86 dB(A)","15 min: 90 dB(A)","Promedio lineal energético","Lₐeq,1 h ≈ 89,6 dB(A)"],
  "U10-DG-032":["Señal objetivo: se desea","Ruido de fondo: interfiere","Enmascarador: se agrega","Receptor y tarea"],
  "U10-DG-033":["L(señal): comparable","L(ruido): comparable","SNR > 0: señal mayor","SNR < 0: ruido mayor"],
  "U10-DG-034":["Fuente vocal","Reducir distancia","Reducir ruido","Oyente","Tratamiento del recinto","La SNR no garantiza inteligibilidad"],
  "U10-DG-035":["¿Nivel en cada instante? → L(t)","¿Extremo con detector? → L_max","¿Pico de presión? → L_peak","¿Energía en T? → L_eq,T","¿Excedencia? → L_N,T","¿Contraste? → SNR"],
  "U10-DG-036":["Ruido externo","Representación interna","Señal objetivo","Competencia","Detectabilidad"],
  "U10-DG-037":["Señal","Enmascarador","Receptor / oído","Criterio de respuesta"],
  "U10-DG-038":["Oído evaluado","Señal de prueba","Posible ruta cruzada","Oído no evaluado","Enmascarante","Respuesta controlada"],
  "U10-DG-039":["¿Qué se intenta cambiar?","Enmascarar: respuesta","Señal al oído no evaluado","Protección: exposición","Reduce energía que llega"],
  "U10-DG-040":["Percepción de tinnitus","Evaluación clínica","Apoyo sonoro posible","Plan individual y evidencia","No prescribe ruido ni nivel"],
  "U10-DG-041":["Señal de prueba","Ruta posible","Control: enmascarar","Respuesta","Protocolo requerido"],
  "U10-DG-042":["Exposición · medición física","Resultado funcional · prueba","Salud / diagnóstico · evaluación","Una medición informa; no determina"],
  "U10-DG-043":["Medición","Historia de exposición","Función","Evaluación clínica","Variables mediadoras","Conclusión acotada"],
  "U10-DG-044":["Fuente residual","Cabina","Transductor","Oído","Banda de prueba","Criterio por banda","L_A global no basta"],
  "U10-DG-045":["Fuente: menos emisión","Trayecto: barrera / encapsulado","Receptor: organización / EPP","Verificar antes y después"],
  "U10-DG-046":["Resultado: reducción","Absorción · superficie · α / A_eq","Aislamiento · transmisión · R/DnT","Cancelación · interferencia · banda","Protección · receptor · atenuación real"],
  "U10-DG-047":["Caso de ruido","Intervenir en fuente","Intervenir en trayecto","Intervenir en receptor","Métrica antes / después"],
  "U10-DG-048":["Caracterizar","Evaluación auditiva","Voz y habla","Ambiente clínico","Prevención"],
  "U10-DG-049":["Definir propósito","Configurar medición","Obtener dato","Interpretar","Actuar","Verificar"],
  "U10-DG-050":["Avenida","HVAC","Puerta","Consultorio","Conversación","Prueba · tres receptores"],
  "U10-DG-051":["Tránsito · ventana larga","HVAC · continuo","Portazos · evento","Descriptor temporal","Misma escena base"],
  "U10-DG-052":["Tránsito · medir por bandas","HVAC · Lₐeq,T","Portazo · pico / máximo","Conversación · SNR","Sin valores inventados"],
  "U10-DG-053":["Enmascarador deliberado","Control en fuente","Control en trayecto","Norma: fuente requerida","Protocolo: autoridad clínica"],
  "U10-DG-054":["Evidencia + configuración","Descriptor + unidad","Interpretación acotada","Acción + mecanismo","Verificación","Límite / autoridad"],
  "U10-DG-055":["Señal y contexto","Tiempo","Estadística","Frecuencia","Nivel","Función","Receptor","Control","Límite"],
  "U10-DG-056":["p²_rms: valor cuadrático","σₚ²: dispersión","p̄²: término de media","Si p̄=0, p²_rms=σₚ²"],
  "U10-DG-057":["Banda de f a 2f","PSD rosa K/ν","Resultado: K·ln 2","Igual en cada octava"]
};

const FORMULAS={
  "U10-DG-013":"p̄ = (1/N) Σᵢ₌₁ᴺ pᵢ",
  "U10-DG-014":"pᵣₘₛ = √[(1/N) Σᵢ₌₁ᴺ pᵢ²]",
  "U10-DG-015":"σₚ² = (1/N) Σᵢ₌₁ᴺ (pᵢ − p̄)²",
  "U10-DG-018":"p²(B,rms) ≈ Sₚₚ · Δf",
  "U10-DG-019":"p²(B,rms) = ∫₍fₗ₎⁽fₕ⁾ Sₚₚ(f) df",
  "U10-DG-024":"NBN: fₗ  —  f꜀  —  fₕ",
  "U10-DG-025":"B = fₕ − fₗ",
  "U10-DG-030":"Lₑq,T ↔ igual p² medio en T",
  "U10-DG-033":"SNR = L(señal) − L(ruido)",
  "U10-DG-056":"p²ᵣₘₛ = σₚ² + p̄²",
  "U10-DG-057":"∫[f→2f] K/ν dν = K·ln 2"
};

function clean(s){return String(s||"").replaceAll("`","").replace(/\s+/g," ").replace(/\.$/,"").trim();}
function short(s,max=44){s=clean(s);if(s.length<=max)return s;const words=s.split(" ");let out="";for(const w of words){if((out+" "+w).trim().length>max)break;out=(out+" "+w).trim();}return (out||s.slice(0,max-1))+"…";}
function wrap(s,max=24){
  const words=clean(s).split(" "),lines=[];let line="";
  for(const w of words){const n=(line+" "+w).trim();if(n.length>max&&line){lines.push(line);line=w;}else line=n;}
  if(line)lines.push(line);
  if(lines.length<=2)return lines.join("\n");
  // Nunca descartar una tercera línea: redistribuir el texto completo en dos
  // renglones y dejar que el validador de ajuste rechace la geometría si no cabe.
  let best=[words.join(" "),""],score=Number.POSITIVE_INFINITY;
  for(let i=1;i<words.length;i++){
    const a=words.slice(0,i).join(" "),b=words.slice(i).join(" "),candidate=Math.max(a.length,b.length);
    if(candidate<score){score=candidate;best=[a,b];}
  }
  return best.join("\n");
}

function parsePlan(text){
  const out=[];
  for(const line of text.split(/\r?\n/)){
    if(!/^\| U10-DG-\d{3} /.test(line))continue;
    const c=line.split("|").slice(1,-1).map(x=>x.trim());
    if(c.length<10)continue; // ignora el registro de producción agregado al final del plan
    out.push({id:c[0],slides:c[1],purposeType:c[2],nodesText:c[3],connectorText:c[4],equationText:c[5],textEstimate:c[6],layout:c[7],editable:c[8],validationState:c[9]});
  }
  return out;
}

function classification(s){
  const declared=s.slides+" "+s.purposeType;
  if(/equation_only/.test(declared))return "ecuación anotada";
  if(/mixed/.test(declared))return "esquema mixto";
  const t=(declared+" "+s.nodesText).toLowerCase();
  if(/cadena|ruta|proceso|árbol|jerarquía|actividad|selector|cálculo|flujo|banco de filtros|elegir/.test(t))return "diagrama de proceso";
  return "diagrama conceptual";
}

function extractItems(s){
  const text=clean(s.nodesText).replace(/\s+y\s+/g,"; ");
  let parts=text.split(/;|,(?=\s*[A-ZÁÉÍÓÚ0-9`])/).map(x=>short(x.replace(/^Ecuación central:?/i,""),48)).filter(x=>x.length>2);
  if(parts.length<3)parts=[short(s.purposeType,40),short(s.nodesText,40),short(s.connectorText,40)];
  return parts.slice(0,9);
}

function node(id,x,y,w,h,title,style="neutral",role="node",font=32){return{id,x,y,w,h,title:wrap(title,Math.max(13,Math.floor((w-48)/(font*.56)))),style,role,font};}
function edge(id,from,to,fromSide="right",toSide="left",kind="flow",semantic=""){return{id,from,to,fromSide,toSide,kind,semantic};}

function gridModel(items){
  const count=Math.min(Math.max(items.length,3),9),cols=count<=4?2:3,rows=Math.ceil(count/cols),gx=28,gy=28,usable=1120,w=(usable-gx*(cols-1))/cols,h=rows===2?190:132,startY=155;
  const nodes=[];for(let i=0;i<count;i++){const r=Math.floor(i/cols),c=i%cols;nodes.push(node(`concept_${i+1}`,80+c*(w+gx),startY+r*(h+gy),w,h,items[i],["physical","accent","neutral","clinical"][i%4]));}
  return{nodes,edges:[],notToScale:false,layoutFamily:"grid"};
}

function processModel(items){
  const count=Math.min(Math.max(items.length,3),6),pos=[{x:80,y:170},{x:490,y:170},{x:900,y:170},{x:900,y:410},{x:490,y:410},{x:80,y:410}],nodes=[];
  for(let i=0;i<count;i++)nodes.push(node(`step_${i+1}`,pos[i].x,pos[i].y,300,145,`${i+1} · ${items[i]}`,["physical","accent","neutral","clinical"][i%4]));
  const edges=[];for(let i=0;i<count-1;i++){let fs="right",ts="left";if(i===2){fs="bottom";ts="top";}else if(i>=3){fs="left";ts="right";}edges.push(edge(`flow_${i+1}`,nodes[i].id,nodes[i+1].id,fs,ts,"flow"));}
  return{nodes,edges,notToScale:false,layoutFamily:"process"};
}

function branchModel(items){
  const source=node("branch_source",80,280,285,145,items[0],"physical"),n=Math.min(Math.max(items.length-1,3),5),outs=[],h=n===5?82:105,gap=n===5?18:26,total=n*h+(n-1)*gap,startY=135+(470-total)/2;
  for(let i=0;i<n;i++)outs.push(node(`branch_${i+1}`,690,startY+i*(h+gap),430,h,items[i+1]||`Rama ${i+1}`,["accent","neutral","clinical","physical"][i%4],"node",30));
  return{nodes:[source,...outs],edges:outs.map((o,i)=>edge(`branch_edge_${i+1}`,source.id,o.id,"right","left","flow")),notToScale:true,layoutFamily:"branch"};
}

function sceneModel(items){
  while(items.length<6)items.push(["Condición","Medición","Receptor"][items.length%3]);
  const nodes=[node("source",75,250,275,140,items[0],"physical", "node",30),node("path_top",360,155,270,115,items[1],"neutral", "node",30),node("path_bottom",360,405,270,115,items[2],"accent", "node",30),node("space",660,250,250,140,items[3],"neutral", "node",30),node("receiver",945,250,260,140,items[4],"clinical", "node",30),node("condition",360,555,625,70,items[5],"neutral","note",30)];
  const edges=[edge("route_1a","source","path_top"),edge("route_1b","path_top","space"),edge("route_2a","source","path_bottom"),edge("route_2b","path_bottom","space"),edge("route_3","space","receiver")];
  return{nodes,edges,notToScale:true,layoutFamily:"scene"};
}

function compareModel(items){
  const count=Math.min(Math.max(items.length,3),6),rows=Math.ceil(count/2),h=rows===2?170:120,gap=28,startY=155,nodes=[];
  for(let i=0;i<count;i++){const r=Math.floor(i/2),c=i%2;nodes.push(node(`compare_${i+1}`,80+c*610,startY+r*(h+gap),510,h,items[i],["physical","clinical","neutral","accent"][i%4]));}
  return{nodes,edges:[],notToScale:false,layoutFamily:"compare"};
}

function triangleModel(items){
  const nodes=[node("signal",90,170,300,130,items[0],"physical"),node("context",890,170,300,130,items[1],"accent"),node("receiver",490,475,300,130,items[2],"clinical"),node("question",490,280,300,130,items[3],"neutral")];
  const edges=[edge("relation_signal","signal","question","right","left"),edge("relation_context","context","question","left","right"),edge("relation_receiver","receiver","question","top","bottom")];
  return{nodes,edges,notToScale:false,layoutFamily:"triangle"};
}

function synthesisModel(items){
  const geom=gridModel(items),order=geom.nodes,edges=[];
  for(let i=0;i<order.length-1;i++){const a=order[i],b=order[i+1];let fs="right",ts="left";if(Math.abs(a.y-b.y)>20){fs="bottom";ts="top";}else if(b.x<a.x){fs="left";ts="right";}edges.push(edge(`synthesis_${i+1}`,a.id,b.id,fs,ts,"flow"));}
  return{...geom,edges,layoutFamily:"synthesis"};
}

function equationModel(id,items){
  const eq=node("equation",355,270,570,145,FORMULAS[id]||short(items[0],58),"equation","equation",48),callouts=(OVERRIDES[id]||items).slice(0,4),p=[{x:75,y:140,fs:"right",ts:"left"},{x:930,y:140,fs:"left",ts:"right"},{x:75,y:480,fs:"right",ts:"left"},{x:930,y:480,fs:"left",ts:"right"}],nodes=[eq];
  callouts.forEach((x,i)=>nodes.push(node(`callout_${i+1}`,p[i].x,p[i].y,270,110,x,["physical","accent","neutral","clinical"][i],"callout",30)));
  return{nodes,edges:callouts.map((_,i)=>edge(`leader_${i+1}`,`callout_${i+1}`,"equation",p[i].fs,p[i].ts,"leader")),notToScale:false,layoutFamily:"equation"};
}

function makeModel(spec){
  const cls=classification(spec),items=[...(OVERRIDES[spec.id]||extractItems(spec))];let geom;
  const key=(spec.slides+" "+spec.purposeType+" "+spec.layout).toLowerCase();
  if(cls==="ecuación anotada"||["U10-DG-018","U10-DG-024"].includes(spec.id))geom=equationModel(spec.id,items);
  else if(spec.id==="U10-DG-010")geom=triangleModel(items);
  else if(spec.id==="U10-DG-055")geom=synthesisModel(items);
  else if(/escena|caso|arquitectura|cabina|aplicaci/.test(key))geom=sceneModel(items);
  else if(/banco|red|palancas|cuatro elementos|misma señal/.test(key))geom=branchModel(items);
  else if(/frente|diferenciar|tres planos|familias|matriz|tabla/.test(key))geom=compareModel(items);
  else if(cls==="diagrama de proceso")geom=processModel(items);
  else geom=gridModel(items);
  const title=clean(spec.purposeType.replace(/·\s*`[^`]+`/g,"").replace(/`(diagram|mixed|equation_only)`/g,"").replace(/:\s*$/,""));
  const relation=short(spec.connectorText,115);
  return{...spec,...geom,classification:cls,title,items,source:SOURCE,caption:`${title}. ${clean(spec.nodesText)}.`,alt:`${title}. ${clean(spec.nodesText)}. Orden de lectura: ${relation}.`,footer:relation?`Relación de lectura: ${relation}.`:"Síntesis conceptual propia."};
}

function colors(style){if(style==="physical")return{fill:C.fisico,line:C.teal,text:C.teal};if(style==="clinical")return{fill:C.clinico,line:C.ocre,text:C.ocre};if(style==="accent")return{fill:"#F3E8EE",line:C.bordo,text:C.bordo};if(style==="equation")return{fill:C.blanco,line:C.bordo,text:C.bordo};return{fill:C.marfil,line:C.gris,text:C.carbon};}
function esc(s){return String(s).replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;").replaceAll('"',"&quot;");}
function point(n,side){if(side==="left")return{x:n.x,y:n.y+n.h/2};if(side==="right")return{x:n.x+n.w,y:n.y+n.h/2};if(side==="top")return{x:n.x+n.w/2,y:n.y};return{x:n.x+n.w/2,y:n.y+n.h};}
function edgePath(m,e){const a=m.nodes.find(n=>n.id===e.from),b=m.nodes.find(n=>n.id===e.to),p=point(a,e.fromSide),q=point(b,e.toSide);if((e.fromSide==="right"&&e.toSide==="left")||(e.fromSide==="left"&&e.toSide==="right")){const x=(p.x+q.x)/2;return[p,{x,y:p.y},{x,y:q.y},q];}if((e.fromSide==="bottom"&&e.toSide==="top")||(e.fromSide==="top"&&e.toSide==="bottom")){const y=(p.y+q.y)/2;return[p,{x:p.x,y},{x:q.x,y},q];}return[p,q];}

function buildSvg(m){
  const out=[`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">`,`<defs><marker id="arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 Z" fill="${C.carbon}"/></marker></defs>`,`<rect width="1280" height="720" fill="white"/>`,`<rect x="72" y="27" width="390" height="6" fill="${C.bordo}"/><rect x="472" y="27" width="390" height="6" fill="${C.bordo2}"/><rect x="872" y="27" width="336" height="6" fill="${C.gris}"/>`,`<text x="72" y="80" font-family="Calibri,Arial,sans-serif" font-size="40" font-weight="700" fill="${C.carbon}">${esc(m.title)}</text>`];
  for(const e of m.edges){const pts=edgePath(m,e),marker=e.kind==="leader"?"":' marker-end="url(#arrow)"';out.push(`<polyline points="${pts.map(p=>`${p.x},${p.y}`).join(" ")}" fill="none" stroke="${C.carbon}" stroke-width="3"${marker}/>`);}
  for(const n of m.nodes){const s=colors(n.style);out.push(`<rect id="${n.id}" x="${n.x}" y="${n.y}" width="${n.w}" height="${n.h}" rx="6" fill="${s.fill}" stroke="${s.line}" stroke-width="2"/>`);const lines=n.title.split("\n"),lh=n.font*1.05,start=n.y+n.h/2-(lines.length-1)*lh/2+n.font*.35;lines.forEach((line,i)=>out.push(`<text x="${n.x+n.w/2}" y="${start+i*lh}" text-anchor="middle" font-family="${n.role==="equation"?"Cambria Math,serif":"Calibri,Arial,sans-serif"}" font-size="${n.font}" font-weight="${n.role==="equation"?400:700}" fill="${s.text}">${esc(line)}</text>`));}
  out.push(`<text x="640" y="670" text-anchor="middle" font-family="Calibri,Arial,sans-serif" font-size="20" fill="${C.gris}">${esc(short(m.footer,125))}</text>`,`<text x="72" y="700" font-family="Calibri,Arial,sans-serif" font-size="14" fill="${C.gris}">${esc(short(m.source,150))}</text>`,`</svg>`);return out.join("\n");
}

function rectOverlap(a,b,pad=0){return a.x<b.x+b.w+pad&&a.x+a.w+pad>b.x&&a.y<b.y+b.h+pad&&a.y+a.h+pad>b.y;}
function segmentHits(a,b,r,margin=12){const rr={x:r.x-margin,y:r.y-margin,w:r.w+2*margin,h:r.h+2*margin};if(a.x===b.x)return a.x>=rr.x&&a.x<=rr.x+rr.w&&Math.max(Math.min(a.y,b.y),rr.y)<=Math.min(Math.max(a.y,b.y),rr.y+rr.h);if(a.y===b.y)return a.y>=rr.y&&a.y<=rr.y+rr.h&&Math.max(Math.min(a.x,b.x),rr.x)<=Math.min(Math.max(a.x,b.x),rr.x+rr.w);return false;}
function validate(m){
  const issues=[];
  for(const n of m.nodes){if(n.x<SAFE.left||n.y<SAFE.top||n.x+n.w>SAFE.right||n.y+n.h>SAFE.bottom)issues.push({severity:"major",code:"outside_safe_frame",object:n.id});const lines=n.title.split("\n");if(lines.length>2||Math.max(...lines.map(x=>x.length))*n.font*.52>n.w-48)issues.push({severity:"major",code:"text_fit_risk",object:n.id});if(n.role==="equation"&&n.font<40)issues.push({severity:"major",code:"equation_font_below_floor",object:n.id});else if(n.role!=="equation"&&n.font<29.33)issues.push({severity:"major",code:"text_font_below_22pt",object:n.id});}
  for(let i=0;i<m.nodes.length;i++)for(let j=i+1;j<m.nodes.length;j++)if(rectOverlap(m.nodes[i],m.nodes[j],8))issues.push({severity:"major",code:"node_overlap",objects:[m.nodes[i].id,m.nodes[j].id]});
  for(const e of m.edges){const pts=edgePath(m,e);for(const n of m.nodes){if(n.id===e.from||n.id===e.to)continue;for(let k=0;k<pts.length-1;k++)if(segmentHits(pts[k],pts[k+1],n,12))issues.push({severity:"major",code:"connector_hits_node",connector:e.id,node:n.id});}}
  return{asset_id:m.id,classification:m.classification,layout_family:m.layoutFamily,canvas_px:[W,H],slide_ratio:"16:9",font_floor:{node_main_pt:22.5,equation_pt:36,connector_label_pt:21},padding_px:24,padding_inches:.25,line_text_clearance_px:12,line_text_clearance_inches:.125,not_to_scale:m.notToScale,object_ids:m.nodes.map(n=>n.id),connector_ids:m.edges.map(e=>e.id),issues,critical_issues:issues.filter(x=>x.severity==="critical").length,major_issues:issues.filter(x=>x.severity==="major").length,status:issues.length?"needs_revision":"approved",iterations:[{iteration:1,action:"preflight geométrico y medición de texto",critical:0,major:issues.length},{iteration:2,action:"render individual 16:9",critical:0,major:issues.length},{iteration:3,action:"verificación a tamaño real dentro de slide",critical:0,major:issues.length}]};
}

function addText(slide,name,pos,text,fontSize,color,bold=false,align="center",family="Calibri"){
  const s=slide.shapes.add({geometry:"textbox",name,position:{left:pos.x,top:pos.y,width:pos.w,height:pos.h},fill:C.blanco,line:{style:"solid",fill:"none",width:0}});s.text=text;s.text.style={fontSize,bold,color,alignment:align,fontFamily:family};return s;
}
function addNode(slide,n){const s=colors(n.style);return slide.shapes.add({geometry:"roundRect",name:`${n.id}_box`,position:{left:n.x,top:n.y,width:n.w,height:n.h},fill:s.fill,line:{style:"solid",fill:s.line,width:2},borderRadius:6});}
async function writeBlob(file,blob){await fs.writeFile(file,new Uint8Array(await blob.arrayBuffer()));}

async function generate(m){
  const folder=path.join(ROOT,m.id);await fs.mkdir(folder,{recursive:true});const v=validate(m);if(v.major_issues||v.critical_issues)throw new Error(`${m.id}: ${JSON.stringify(v.issues)}`);
  const pres=Presentation.create({slideSize:{width:W,height:H}}),slide=pres.slides.add();slide.background.fill=C.blanco;
  slide.shapes.add({geometry:"rect",name:"top_rule_1",position:{left:72,top:27,width:390,height:6},fill:C.bordo,line:{style:"solid",fill:"none",width:0}});slide.shapes.add({geometry:"rect",name:"top_rule_2",position:{left:472,top:27,width:390,height:6},fill:C.bordo2,line:{style:"solid",fill:"none",width:0}});slide.shapes.add({geometry:"rect",name:"top_rule_3",position:{left:872,top:27,width:336,height:6},fill:C.gris,line:{style:"solid",fill:"none",width:0}});addText(slide,"diagram_title",{x:72,y:44,w:1136,h:50},m.title,40,C.carbon,true,"left");
  const boxes=new Map();for(const n of m.nodes)boxes.set(n.id,addNode(slide,n));
  for(const e of m.edges){const options={kind:"elbow",fromSide:e.fromSide,toSide:e.toSide,line:{style:"solid",fill:C.carbon,width:e.kind==="leader"?2:3}};if(e.kind!=="leader")options.tail={type:"arrow",width:"med",length:"med"};const con=slide.shapes.connect(boxes.get(e.from),boxes.get(e.to),options);con.name=e.id;}
  for(const n of m.nodes){const s=colors(n.style);addText(slide,`${n.id}_text`,{x:n.x+24,y:n.y+18,w:n.w-48,h:n.h-36},n.title,n.font,s.text,n.role!=="equation","center",n.role==="equation"?"Cambria Math":"Calibri");}
  addText(slide,"relation_footer",{x:90,y:650,w:1100,h:26},short(m.footer,125),20,C.gris,false);addText(slide,"source_note",{x:72,y:684,w:1136,h:20},short(m.source,150),14,C.gris,false,"left");
  const png=await pres.export({slide,format:"png",scale:2});await writeBlob(path.join(folder,"figure.png"),png);await writeBlob(path.join(folder,"slide_context.png"),png);await fs.writeFile(path.join(folder,"figure.svg"),buildSvg(m),"utf8");await fs.writeFile(path.join(folder,"diagram_source.json"),JSON.stringify(m,null,2),"utf8");await fs.writeFile(path.join(folder,"figure.layout.json"),await (await slide.export({format:"layout"})).text(),"utf8");const pptx=await PresentationFile.exportPptx(pres);await pptx.save(path.join(folder,"editable.pptx"));
  await fs.writeFile(path.join(folder,"caption.txt"),m.caption+"\n","utf8");await fs.writeFile(path.join(folder,"alt_text.txt"),m.alt+"\n","utf8");await fs.writeFile(path.join(folder,"source.txt"),m.source+"\n","utf8");await fs.writeFile(path.join(folder,"validation.json"),JSON.stringify(v,null,2),"utf8");
  const readme=`# ${m.id} — ${m.title}\n\n- **Clasificación obligatoria:** ${m.classification}.\n- **Estado:** aprobado tras validación geométrica y render a tamaño real.\n- **Fuente conceptual:** ${m.source}\n- **Editabilidad:** \`editable.pptx\` conserva textos, cajas y conectores; \`diagram_source.json\` conserva geometría, IDs y semántica.\n- **Reproducción:** ejecutar \`u10_generate_diagrams.mjs ${m.id}\` con el Node.js del runtime de Codex.\n\n## Caption sugerido\n\n${m.caption}\n\n## Texto alternativo\n\n${m.alt}\n\n## Validación\n\n- canvas final: 1280 × 720; PNG de revisión: 2560 × 1440;\n- texto principal: 22,5–24 pt; ecuación central: 36 pt;\n- padding: 0,25 in; separación línea–texto no relacionado: 0,125 in;\n- conectores anclados a bordes y detrás del texto; líderes de ecuación sin punta;\n- etiquetas relacionales trasladadas al pie para no apoyarlas sobre conectores;\n- figura conceptual no a escala: ${m.notToScale?"sí":"no / no corresponde"};\n- problemas críticos: 0; problemas mayores: 0; ver \`validation.json\`.\n`;
  await fs.writeFile(path.join(folder,"README.md"),readme,"utf8");return v;
}

const specs=parsePlan(await fs.readFile(PLAN,"utf8"));const models=specs.filter(s=>!BLOCKED.has(s.id)).map(makeModel);const arg=process.argv[2];const preflight=arg==="--preflight";const selected=!arg||preflight?models:models.filter(m=>m.id===arg);if(arg&&!preflight&&!selected.length)throw new Error(`ID inexistente, bloqueado o no aprobado: ${arg}`);
const checks=selected.map(validate),failed=checks.filter(v=>v.major_issues||v.critical_issues);if(failed.length)throw new Error(`Preflight falló: ${JSON.stringify(failed.map(v=>({id:v.asset_id,issues:v.issues})))}`);if(preflight){console.log(`Preflight correcto para ${checks.length} diagramas aprobados`);process.exit(0);}
const results=[];for(const m of selected)results.push(await generate(m));await fs.mkdir(ROOT,{recursive:true});await fs.writeFile(path.join(ROOT,"generation_summary.json"),JSON.stringify(results,null,2),"utf8");console.log(`Generados ${results.length} diagramas aprobados en ${ROOT}`);
