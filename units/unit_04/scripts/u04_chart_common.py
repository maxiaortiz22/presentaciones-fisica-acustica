"""Generador reproducible de gráficos cuantitativos de la Unidad 4.

Cada wrapper u04_plot_*.py llama a ``generate`` con un ID. Los datos son
modelos analíticos didácticos o señales sintéticas declaradas; no representan
mediciones. CH-012 se excluye porque su dataset externo requiere aprobación
para una descarga masiva.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter, LogLocator

ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = ROOT / "assets" / "generated" / "charts"

COL = {
    "bordo": "#4D1434",
    "bordo2": "#903163",
    "teal": "#2F7E83",
    "teal_light": "#E7F1F1",
    "ocre": "#9F541A",
    "ocre_light": "#F8EDE2",
    "carbon": "#242A2E",
    "gray": "#969FA7",
    "grid": "#D9DCE0",
    "white": "#FFFFFF",
}

mpl.rcParams.update({
    "font.family": "Calibri",
    "font.size": 18,
    "axes.labelsize": 20,
    "xtick.labelsize": 18,
    "ytick.labelsize": 18,
    "legend.fontsize": 18,
    "axes.edgecolor": COL["carbon"],
    "axes.labelcolor": COL["carbon"],
    "xtick.color": COL["carbon"],
    "ytick.color": COL["carbon"],
    "text.color": COL["carbon"],
    "axes.grid": True,
    "grid.color": COL["grid"],
    "grid.linewidth": 0.8,
    "grid.alpha": 0.65,
    "svg.fonttype": "none",
    "savefig.facecolor": "white",
})


def comma(x, _pos=None):
    if abs(x) >= 1000 or (abs(x) > 0 and abs(x) < 1e-3):
        return f"{x:g}".replace(".", ",")
    return f"{x:.2f}".rstrip("0").rstrip(".").replace(".", ",")


FMT = FuncFormatter(comma)


def fig_axes(n=1, *, height=5.35, polar=False):
    if polar:
        return plt.subplots(figsize=(8.4, 6.1), subplot_kw={"projection": "polar"}, constrained_layout=True)
    return plt.subplots(n, 1, figsize=(11.6, height), sharex=n > 1, constrained_layout=True)


def style_ax(ax, xlabel=None, ylabel=None, xlim=None, ylim=None):
    ax.spines[["top", "right"]].set_visible(False)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    if xlim:
        ax.set_xlim(*xlim)
    if ylim:
        ax.set_ylim(*ylim)
    ax.xaxis.set_major_formatter(FMT)
    ax.yaxis.set_major_formatter(FMT)


def resource_dir(cid):
    d = OUT_ROOT / cid
    d.mkdir(parents=True, exist_ok=True)
    return d


def save_fig(fig, d, stem):
    fig.savefig(d / f"{stem}.svg", bbox_inches="tight")
    fig.savefig(d / f"{stem}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


META = {
    "U04-CH-001": ("Presión total y presión acústica", "La presión acústica es una pequeña variación respecto de la presión estática.", "Dos paneles temporales muestran una presión total siempre positiva y la variación acústica centrada en cero.", "Modelo sinusoidal ilustrativo basado en TEX 4.5.1; p0=101325 Pa, amplitud 0,20 Pa, 500 Hz."),
    "U04-CH-002": ("Presión, velocidad e intensidad", "En una onda progresiva ideal, presión y velocidad están en fase; su producto es no negativo.", "Tres paneles coordinados muestran presión y velocidad normalizadas sinusoidales e intensidad instantánea proporcional a seno al cuadrado.", "Modelo analítico basado en TEX 4.5.5 y figura 4.2."),
    "U04-CH-003": ("Descriptores temporales", "Cada descriptor responde una pregunta diferente sobre la misma señal.", "Señal sintética asimétrica con media distinta de cero y marcadores progresivos de instante, extremos, pico a pico y media.", "Señal sintética didáctica; parámetros documentados en data.csv."),
    "U04-CH-004": ("Media cero", "Media cero no implica ausencia de señal.", "Comparación entre una sinusoide de media cero y una señal nula, con valores RMS diferentes.", "Modelo sinusoidal analítico basado en TEX 4.6.4–4.6.5."),
    "U04-CH-005": ("Construcción del RMS", "Cuadrar elimina el signo, promediar resume y la raíz recupera la unidad.", "Cuatro etapas coordinadas muestran presión, cuadrado, media cuadrática y valor RMS.", "Modelo sinusoidal analítico basado en TEX 4.6.5 y figura 4.3."),
    "U04-CH-006": ("Igual RMS, distinta forma", "Dos señales pueden tener igual RMS y distinta forma o contenido frecuencial.", "Se comparan una sinusoide y una suma de tres componentes normalizadas al mismo RMS.", "Señales sintéticas didácticas basadas en TEX 4.6.6."),
    "U04-CH-007": ("Presión y nivel", "Cada década de presión eficaz agrega 20 dB SPL.", "Escalas alineadas relacionan presión eficaz logarítmica entre 20 micropascales y 20 pascales con 0 a 120 dB SPL.", "Relación analítica Lp=20 log10(p/pref), pref=20 µPa; TEX 4.7."),
    "U04-CH-008": ("Suma coherente y fase", "La diferencia de fase fija la amplitud resultante de dos tonos coherentes.", "Familia de curvas para fase cero, pi sobre dos y pi, con señales fuente y suma.", "Modelo analítico basado en TEX 4.8.1."),
    "U04-CH-009": ("Suma no correlacionada", "Para señales no correlacionadas se suman cuadrados RMS.", "Dos ruidos gaussianos independientes y su suma muestran un incremento esperado cercano a 3,01 dB.", "Señales sintéticas con semilla fija 40467; TEX 4.8.2."),
    "U04-CH-010": ("Geometría y decaimiento", "El crecimiento del área determina caídas r⁰, r⁻¹ y r⁻².", "Curvas normalizadas comparan modelos plano, cilíndrico y esférico.", "Modelos geométricos ideales basados en TEX 4.9; no son datos experimentales."),
    "U04-CH-011": ("Nivel y distancia", "En campo esférico ideal, cada duplicación de distancia reduce 6,02 dB.", "Curva de diferencia de nivel frente a distancia relativa con anclas en uno, dos, cuatro y ocho.", "Modelo analítico basado en TEX 4.10."),
    "U04-CH-013": ("Reflexión e impedancias", "El signo del coeficiente de presión y la fracción de intensidad informan aspectos distintos.", "Coeficiente de reflexión de presión y fracción de intensidad frente al cociente de impedancias.", "Modelo analítico de incidencia normal, medios sin pérdidas; TEX 4.5.4."),
    "U04-CH-014": ("Incremento al sumar niveles", "La contribución de una segunda fuente cae al aumentar la diferencia de niveles.", "Curva del incremento total en decibeles para dos fuentes no correlacionadas.", "Relación analítica basada en TEX 4.8.2."),
    "U04-CH-015": ("Suma en cuadratura", "Un desfase pi sobre dos produce una resultante intermedia.", "Dos sinusoides iguales en cuadratura y su suma, con amplitud resultante raíz de dos.", "Derivado del modelo de U04-CH-008; TEX 4.8.1."),
}


def readme(cid, d, variants, metrics=""):
    title, caption, alt, source = META[cid]
    text = f"""# {cid} — {title}

- Clasificación: gráfico cuantitativo.
- Skill: `chart-generation`.
- Variantes: {', '.join(variants)}.
- Caption sugerido: {caption}
- Texto alternativo: {alt}
- Fuente de datos/modelo: {source}
- Escala: indicada en los ejes de cada variante; toda escala logarítmica se rotula explícitamente.
- Nota: las señales sintéticas y modelos ideales se declaran como tales; no representan mediciones.
{metrics}
"""
    (d / "README.md").write_text(text, encoding="utf-8")


def ch001(d):
    t = np.linspace(0, .006, 1201); p0=101325.; p=.2*np.sin(2*np.pi*500*t); total=p0+p
    pd.DataFrame({"t_s":t,"t_ms":t*1000,"p_acustica_Pa":p,"p_total_Pa":total}).to_csv(d/"data.csv",index=False)
    fig,axs=fig_axes(2,height=6.2)
    axs[0].plot(t*1000,total,color=COL["teal"],lw=3); axs[0].axhline(p0,color=COL["gray"],ls="--",lw=2); style_ax(axs[0],ylabel="p_total (Pa)",ylim=(101324.72,101325.28)); axs[0].yaxis.set_major_formatter(FuncFormatter(lambda x,_: f"{x:.1f}".replace(".",",")))
    axs[0].annotate("equilibrio p₀",(4.25,p0),xytext=(4.25,p0+.12),fontsize=20,color=COL["gray"],ha="center",arrowprops={"arrowstyle":"-","color":COL["gray"]})
    axs[1].plot(t*1000,p,color=COL["bordo2"],lw=3); axs[1].axhline(0,color=COL["gray"],lw=1.5); style_ax(axs[1],xlabel="Tiempo (ms)",ylabel="p(t) (Pa)",ylim=(-.28,.28))
    axs[1].annotate("sobrepresión",(.5,.2),xytext=(1.0,.235),fontsize=20,color=COL["teal"],arrowprops={"arrowstyle":"->","color":COL["teal"]}); axs[1].annotate("rarefacción",(1.5,-.2),xytext=(2.1,-.245),fontsize=20,color=COL["bordo"] ,arrowprops={"arrowstyle":"->","color":COL["bordo"]})
    save_fig(fig,d,"u04_fig_001_presion_total_acustica")
    fig,ax=fig_axes(); ax.plot(t*1000,p,color=COL["teal"],lw=3); ax.axhline(0,color=COL["gray"],lw=1.5); style_ax(ax,xlabel="Tiempo (ms)",ylabel="p(t) (Pa)",ylim=(-.28,.28)); save_fig(fig,d,"u04_fig_001b_presion_acustica_simple")
    return ["u04_fig_001_presion_total_acustica","u04_fig_001b_presion_acustica_simple"]


def ch002(d):
    x=np.linspace(0,2,1001); p=np.sin(2*np.pi*x); u=p.copy(); i=p*u
    pd.DataFrame({"t_sobre_T":x,"p_norm":p,"u_norm":u,"i_norm":i}).to_csv(d/"data.csv",index=False)
    fig,axs=fig_axes(3,height=6.4)
    for ax,y,c,lab in zip(axs,[p,u,i],[COL["teal"],COL["bordo"],COL["ocre"]],["p(t) / p̂","u(t) / û","i(t) / î"]):
        ax.plot(x,y,color=c,lw=3); ax.axhline(0,color=COL["gray"],lw=1); style_ax(ax,ylabel=lab,xlim=(0,2),ylim=(-1.15,1.15 if lab!="i(t) / î" else 1.15))
    axs[2].set_ylim(-.08,1.15); axs[2].set_xlabel("Tiempo normalizado t/T (escala lineal)")
    axs[2].annotate("p<0 y u<0: i>0",(1.25,1),xytext=(1.05,.58),fontsize=20,color=COL["ocre"],arrowprops={"arrowstyle":"->","color":COL["ocre"]})
    save_fig(fig,d,"u04_fig_002_presion_velocidad_intensidad"); return ["u04_fig_002_presion_velocidad_intensidad"]


def signal3():
    t=np.linspace(0,.04,2001); y=.04+.14*np.sin(2*np.pi*100*t)+.035*np.sin(2*np.pi*200*t+.8)
    return t,y


def ch003(d):
    t,y=signal3(); imax=np.argmax(y); imin=np.argmin(y); mean=np.mean(y); idx=np.argmin(abs(t-.011))
    pd.DataFrame({"t_s":t,"t_ms":1000*t,"p_Pa":y}).to_csv(d/"data.csv",index=False)
    specs=[("base",[]),("instante",["inst"]),("maximo",["inst","max"]),("minimo",["inst","max","min"]),("pico_a_pico",["max","min","pp"]),("media",["max","min","pp","mean"])]
    for k,(name,marks) in enumerate(specs,1):
        fig,ax=fig_axes(); ax.plot(t*1000,y,color=COL["teal"],lw=3); style_ax(ax,xlabel="Tiempo (ms)",ylabel="p(t) (Pa)",xlim=(0,40),ylim=(-.17,.24)); ax.axhline(0,color=COL["gray"],lw=1)
        if "inst" in marks: ax.scatter(t[idx]*1000,y[idx],s=85,color=COL["ocre"],zorder=5); ax.annotate("p(t₁)",(t[idx]*1000,y[idx]),xytext=(t[idx]*1000+3,y[idx]+.065),fontsize=22,arrowprops={"arrowstyle":"->","color":COL["ocre"]})
        if "max" in marks: ax.scatter(t[imax]*1000,y[imax],s=75,color=COL["bordo"],zorder=5); ax.text(t[imax]*1000+1,y[imax]-.03,"pₘₐₓ",fontsize=22,color=COL["bordo"])
        if "min" in marks: ax.scatter(t[imin]*1000,y[imin],s=75,color=COL["bordo2"],zorder=5); ax.text(t[imin]*1000+1,y[imin]+.02,"pₘᵢₙ",fontsize=22,color=COL["bordo2"])
        if "pp" in marks: ax.annotate("",(36,y[imax]),(36,y[imin]),arrowprops={"arrowstyle":"<->","color":COL["ocre"],"lw":2.5}); ax.text(34.5,(y[imax]+y[imin])/2,"pₚₚ",fontsize=22,color=COL["ocre"],ha="right")
        if "mean" in marks: ax.axhline(mean,color=COL["ocre"],ls="--",lw=2.5); ax.text(27,mean+.018,f"media = {mean:.3f} Pa".replace(".",","),fontsize=20,color=COL["ocre"])
        save_fig(fig,d,f"u04_fig_003_{k}_{name}")
    metrics=f"- Verificación: p_pp={y[imax]-y[imin]:.6f} Pa; 2·pico_abs={2*np.max(abs(y)):.6f} Pa; no son iguales.\n"
    return [f"u04_fig_003_{k}_{n}" for k,(n,_) in enumerate(specs,1)],metrics


def ch004(d):
    t=np.linspace(0,.02,1001); y=.2*np.sin(2*np.pi*100*t); z=np.zeros_like(t)
    pd.DataFrame({"t_s":t,"t_ms":t*1000,"seno_Pa":y,"nula_Pa":z}).to_csv(d/"data.csv",index=False)
    fig,axs=fig_axes(2,height=5.8)
    for ax,a,c,lab in [(axs[0],y,COL["teal"],"Señal sinusoidal"),(axs[1],z,COL["gray"],"Señal nula")]:
        ax.plot(t*1000,a,color=c,lw=3); ax.axhline(0,color=COL["gray"],lw=1); style_ax(ax,ylabel="p (Pa)",xlim=(0,20),ylim=(-.23,.23)); ax.text(.98,.82,lab,transform=ax.transAxes,ha="right",fontsize=22,color=c)
    axs[1].set_xlabel("Tiempo (ms)"); axs[0].text(.02,.08,"media = 0 Pa · RMS = 0,141 Pa",transform=axs[0].transAxes,fontsize=20,color=COL["ocre"]); axs[1].text(.02,.08,"media = 0 Pa · RMS = 0 Pa",transform=axs[1].transAxes,fontsize=20,color=COL["ocre"])
    save_fig(fig,d,"u04_fig_004_media_cero"); return ["u04_fig_004_media_cero"]


def ch005(d):
    x=np.linspace(0,2,1201); p=.2*np.sin(2*np.pi*x); sq=p*p; ms=np.mean(sq); rms=math.sqrt(ms)
    pd.DataFrame({"t_sobre_T":x,"p_Pa":p,"p2_Pa2":sq,"media_p2_Pa2":ms,"rms_Pa":rms}).to_csv(d/"data.csv",index=False)
    def draw(k,stem):
        fig,axs=fig_axes(4,height=7.0); vals=[p,sq,np.full_like(x,ms),np.full_like(x,rms)]; labs=["p (Pa)","p² (Pa²)","media p² (Pa²)","RMS (Pa)"]; steps=["1 · señal","2 · cuadrar","3 · promediar","4 · raíz"]; cols=[COL["teal"],COL["bordo"],COL["ocre"],COL["ocre"]]
        for j,(ax,v,lab,c) in enumerate(zip(axs,vals,labs,cols)):
            ax.plot(x,v,color=c if j<k else COL["grid"],lw=3); style_ax(ax,ylabel=lab,xlim=(0,2)); ax.grid(j<k); ax.text(.01,.80,steps[j],transform=ax.transAxes,fontsize=19,color=c if j<k else COL["gray"])
        axs[-1].set_xlabel("Tiempo normalizado t/T (escala lineal)"); axs[-1].set_ylim(0,.22); axs[-1].text(1.05,rms+.012,"0,1414 Pa",fontsize=20,color=COL["ocre"])
        save_fig(fig,d,stem)
    stems=[]
    for k in range(1,5): stems.append(f"u04_fig_005_paso_{k}"); draw(k,stems[-1])
    stems.append("u04_fig_005_construccion_rms"); draw(4,stems[-1]); return stems,f"- Verificación: p_rms numérico={rms:.8f} Pa; analítico={.2/math.sqrt(2):.8f} Pa.\n"


def ch006(d):
    t=np.linspace(0,.02,4001,endpoint=False); a=np.sin(2*np.pi*200*t); b=np.sin(2*np.pi*100*t)+.7*np.sin(2*np.pi*300*t+.3)+.45*np.sin(2*np.pi*500*t+1.1)
    target=.2; a*=target/np.sqrt(np.mean(a*a)); b*=target/np.sqrt(np.mean(b*b))
    pd.DataFrame({"t_s":t,"t_ms":1000*t,"seno_Pa":a,"compleja_Pa":b}).to_csv(d/"data.csv",index=False)
    fig,axs=fig_axes(2,height=5.8)
    for ax,y,c,lab in [(axs[0],a,COL["teal"],"Seno 200 Hz"),(axs[1],b,COL["bordo"],"Suma 100 + 300 + 500 Hz")]:
        ax.plot(1000*t,y,color=c,lw=2.5); style_ax(ax,ylabel="p (Pa)",xlim=(0,20),ylim=(-.48,.48)); ax.text(.99,.90,lab+" · RMS=0,20 Pa",transform=ax.transAxes,ha="right",fontsize=20,color=c,bbox={"facecolor":"white","alpha":.88,"edgecolor":"none","pad":1.5})
    axs[1].set_xlabel("Tiempo (ms)"); save_fig(fig,d,"u04_fig_006_igual_rms")
    fig,axs=plt.subplots(2,2,figsize=(11.6,6.1),constrained_layout=True)
    for row,y,c,lab in [(0,a,COL["teal"],"Seno"),(1,b,COL["bordo"],"Compleja")]:
        axs[row,0].plot(1000*t,y,color=c,lw=2); style_ax(axs[row,0],ylabel="p (Pa)",xlim=(0,20),ylim=(-.48,.48));
        freq=np.fft.rfftfreq(len(t),t[1]-t[0]); mag=np.abs(np.fft.rfft(y)); axs[row,1].stem(freq[freq<=700],mag[freq<=700]/mag.max(),linefmt=c,markerfmt=" ",basefmt=" "); style_ax(axs[row,1],ylabel="Magnitud relativa (1)",xlim=(0,700),ylim=(0,1.12)); axs[row,0].text(.02,.8,lab,transform=axs[row,0].transAxes,fontsize=20,color=c)
    axs[1,0].set_xlabel("Tiempo (ms)"); axs[1,1].set_xlabel("Frecuencia (Hz) · anticipo U5"); save_fig(fig,d,"u04_fig_006b_igual_rms_espectro_anticipo")
    diff=abs(np.sqrt(np.mean(a*a))-np.sqrt(np.mean(b*b)))/target*100
    return ["u04_fig_006_igual_rms","u04_fig_006b_igual_rms_espectro_anticipo"],f"- Verificación: diferencia relativa de RMS={diff:.6f} %.\n"


def ch007(d):
    levels=np.arange(0,121,20); p=20e-6*10**(levels/20)
    pd.DataFrame({"Lp_dB_SPL":levels,"p_rms_Pa":p}).to_csv(d/"data.csv",index=False)
    fig,ax=plt.subplots(figsize=(11.6,5.2),constrained_layout=True); ax.semilogx(p,levels,color=COL["teal"],lw=3,marker="o",ms=8); ax.set_xscale("log"); style_ax(ax,xlabel="Presión eficaz pᵣₘₛ (Pa) · escala logarítmica",ylabel="Nivel Lₚ (dB SPL)",ylim=(-3,123)); ax.set_yticks(levels)
    for x,y in zip(p,levels): ax.annotate(f"{y} dB",(x,y),xytext=(0,10),textcoords="offset points",ha="center",fontsize=18,color=COL["bordo"])
    ax.text(.02,.95,"p_ref = 20 µPa",transform=ax.transAxes,va="top",fontsize=20,color=COL["ocre"]); save_fig(fig,d,"u04_fig_007_presion_nivel_horizontal")
    fig,ax=plt.subplots(figsize=(7.2,6.2),constrained_layout=True); ax.semilogy(levels,p,color=COL["teal"],lw=3,marker="o",ms=8); ax.set_yscale("log"); style_ax(ax,xlabel="Nivel Lₚ (dB SPL)",ylabel="pᵣₘₛ (Pa) · escala logarítmica",xlim=(-3,123)); ax.set_xticks(levels); save_fig(fig,d,"u04_fig_007_presion_nivel_vertical")
    return ["u04_fig_007_presion_nivel_horizontal","u04_fig_007_presion_nivel_vertical"]


def coherent_plot(d,phi,stem,label):
    x=np.linspace(0,2,1201); a=np.sin(2*np.pi*x); b=np.sin(2*np.pi*x+phi); s=a+b
    fig,ax=plt.subplots(figsize=(11.6,5.35)); fig.subplots_adjust(left=.10,right=.985,bottom=.18,top=.78)
    ax.plot(x,a,color=COL["teal"],lw=2.5,ls="-",label="fuente A"); ax.plot(x,b,color=COL["bordo"],lw=2.5,ls="--",label="fuente B"); ax.plot(x,s,color=COL["ocre"],lw=3.5,label="suma")
    style_ax(ax,xlabel="Tiempo normalizado t/T (escala lineal)",ylabel="Presión normalizada (1)",xlim=(0,2),ylim=(-2.25,2.25))
    fig.text(.10,.90,label,fontsize=22,color=COL["carbon"],ha="left",va="center")
    fig.legend(*ax.get_legend_handles_labels(),ncol=3,loc="upper right",bbox_to_anchor=(.985,.96),fontsize=16,frameon=False)
    save_fig(fig,d,stem); return x,a,b,s


def ch008(d):
    variants=[(0,"fase_0","φ = 0 · refuerzo máximo"),(np.pi/2,"fase_pi_2","φ = π/2 · caso intermedio"),(np.pi,"fase_pi","φ = π · cancelación ideal")]
    frames=[]
    rows=[]
    for phi,name,label in variants:
        stem=f"u04_fig_008_{name}"; x,a,b,s=coherent_plot(d,phi,stem,label); frames.append(stem); rows.extend(pd.DataFrame({"t_sobre_T":x,"phi_rad":phi,"p_A":a,"p_B":b,"p_suma":s}).to_dict("records"))
    pd.DataFrame(rows).to_csv(d/"data.csv",index=False)
    fig,axs=fig_axes(3,height=6.4)
    for ax,(phi,name,label) in zip(axs,variants):
        x=np.linspace(0,2,1000); a=np.sin(2*np.pi*x); b=np.sin(2*np.pi*x+phi); ax.plot(x,a+b,color=COL["ocre"],lw=3); style_ax(ax,ylabel=label.split(" · ")[0],xlim=(0,2),ylim=(-2.2,2.2))
    axs[-1].set_xlabel("Tiempo normalizado t/T"); save_fig(fig,d,"u04_fig_008_resumen_fases"); frames.append("u04_fig_008_resumen_fases")
    x=np.linspace(0,2,1201); phi=np.pi/3; a=np.sin(2*np.pi*x); b=np.sin(2*np.pi*x+phi); fig,ax=fig_axes(); ax.plot(x,a+b,color=COL["ocre"],lw=3); style_ax(ax,xlabel="Tiempo normalizado t/T",ylabel="Suma normalizada (1)",xlim=(0,2),ylim=(-2.2,2.2)); ax.text(.02,.9,"Frame estático alternativo · φ = π/3",transform=ax.transAxes,fontsize=22); save_fig(fig,d,"u04_fig_008_frame_estatico"); frames.append("u04_fig_008_frame_estatico")
    return frames,"- Verificación: incremento en fase=6,0206 dB; en cuadratura=3,0103 dB; oposición ideal=0.\n"


def ch009(d):
    fs=48000; n=fs; rng=np.random.default_rng(40467); a=rng.standard_normal(n); b=rng.standard_normal(n); a-=np.mean(a); b-=np.mean(b); a*=.2/np.sqrt(np.mean(a*a)); b*=.2/np.sqrt(np.mean(b*b)); s=a+b; corr=np.corrcoef(a,b)[0,1]
    rmsa=np.sqrt(np.mean(a*a)); rmsb=np.sqrt(np.mean(b*b)); rmss=np.sqrt(np.mean(s*s)); inc=20*np.log10(rmss/rmsa)
    pd.DataFrame({"t_s":np.arange(n)/fs,"ruido_A_Pa":a,"ruido_B_Pa":b,"suma_Pa":s}).to_csv(d/"data.csv",index=False)
    pd.DataFrame([{"seed":40467,"fs_Hz":fs,"rms_A_Pa":rmsa,"rms_B_Pa":rmsb,"rms_suma_Pa":rmss,"correlacion":corr,"incremento_dB":inc}]).to_csv(d/"metrics.csv",index=False)
    for ms,stem in [(25,"u04_fig_009_zoom_25ms"),(1000,"u04_fig_009_ventana_1s")]:
        m=int(fs*ms/1000); stride=1 if ms==25 else 40; tt=np.arange(m)[::stride]/fs*1000; fig,axs=fig_axes(3,height=6.3)
        for ax,y,c,lab in zip(axs,[a,b,s],[COL["teal"],COL["bordo"],COL["ocre"]],["ruido A","ruido B","suma"]): ax.plot(tt,y[:m:stride],color=c,lw=1.6); style_ax(ax,ylabel=f"{lab} (Pa)",xlim=(0,ms),ylim=(-1.05,1.05))
        axs[-1].set_xlabel(f"Tiempo (ms) · ventana {ms/1000:g} s".replace(".",",")); axs[-1].text(.02,.08,f"r={corr:.4f} · ΔL={inc:.2f} dB".replace(".",","),transform=axs[-1].transAxes,fontsize=20,color=COL["ocre"]); save_fig(fig,d,stem)
    return ["u04_fig_009_zoom_25ms","u04_fig_009_ventana_1s"],f"- Verificación: correlación={corr:.6f}; incremento={inc:.5f} dB; RMS suma={rmss:.8f} Pa.\n"


def ch010(d):
    r=np.linspace(1,8,600); vals={"plano":np.ones_like(r),"cilindrico":1/r,"esferico":1/r**2}; pd.DataFrame({"r_sobre_r0":r,**vals}).to_csv(d/"data.csv",index=False)
    fig,ax=fig_axes();
    for lab,c,ls in [("plano",COL["gray"],":"),("cilíndrico",COL["teal"],"--"),("esférico",COL["bordo"],"-")]: ax.loglog(r,vals[lab.replace("í","i").replace("é","e")],color=c,lw=3,ls=ls,label=lab)
    style_ax(ax,xlabel="Distancia relativa r/r₀ · escala logarítmica",ylabel="I/I₀ · escala log",xlim=(1,8),ylim=(1/70,1.15)); ax.legend(); ax.set_xticks([1,2,4,8]); ax.set_yticks([1,.5,.25,.125,.0625,.03125,.015625]); ax.xaxis.set_major_formatter(FMT); ax.yaxis.set_major_formatter(FMT); save_fig(fig,d,"u04_fig_010_geometrias_loglog")
    fig,ax=fig_axes();
    for lab,c,ls in [("plano",COL["gray"],":"),("cilíndrico",COL["teal"],"--"),("esférico",COL["bordo"],"-")]: ax.plot(r,vals[lab.replace("í","i").replace("é","e")],color=c,lw=3,ls=ls,label=lab)
    style_ax(ax,xlabel="Distancia relativa r/r₀ (escala lineal)",ylabel="I/I₀",xlim=(1,8),ylim=(0,1.05)); ax.legend(); [ax.axvline(x,color=COL["grid"],lw=1) for x in [2,4,8]]; save_fig(fig,d,"u04_fig_010b_geometrias_lineal")
    return ["u04_fig_010_geometrias_loglog","u04_fig_010b_geometrias_lineal"]


def ch011(d):
    r=np.geomspace(1,8,300); dl=20*np.log10(1/r); pd.DataFrame({"r_sobre_r0":r,"delta_Lp_dB":dl}).to_csv(d/"data.csv",index=False)
    fig,ax=fig_axes(); ax.plot(r,dl,color=COL["teal"],lw=3); ax.set_xscale("log",base=2); style_ax(ax,xlabel="Distancia relativa r/r₀ · escala log₂",ylabel="ΔLₚ (dB)",xlim=(.92,8.8),ylim=(-19,1)); ax.set_xticks([1,2,4,8]); ax.xaxis.set_major_formatter(FMT)
    for x in [1,2,4,8]:
        y=20*np.log10(1/x); ax.scatter(x,y,s=70,color=COL["bordo"],zorder=4)
        dx,ha=((8,"left") if x == 1 else ((-8,"right") if x == 8 else (0,"center")))
        ax.annotate(f"{y:.2f} dB".replace(".",","),(x,y),xytext=(dx,12),textcoords="offset points",ha=ha,fontsize=20,color=COL["bordo"])
    save_fig(fig,d,"u04_fig_011_nivel_distancia"); return ["u04_fig_011_nivel_distancia"]


def ch013(d):
    eta=np.geomspace(.1,10,600); rp=(eta-1)/(eta+1); ri=rp*rp; pd.DataFrame({"eta_Z2_sobre_Z1":eta,"R_p":rp,"R_I":ri}).to_csv(d/"data.csv",index=False)
    fig,ax=fig_axes(); ax.plot(eta,rp,color=COL["teal"],lw=3,label="Rₚ (amplitud y signo)"); ax.plot(eta,ri,color=COL["ocre"],lw=3,ls="--",label="Rᵢ = Rₚ² (fracción)"); ax.set_xscale("log"); style_ax(ax,xlabel="Cociente η = Z₂/Z₁ · escala logarítmica",ylabel="Coeficiente adimensional",xlim=(.1,10),ylim=(-1.05,1.05)); ax.axvline(1,color=COL["gray"],lw=1.5); ax.axhline(0,color=COL["gray"],lw=1); ax.legend(loc="upper left"); ax.text(1.05,.08,"η=1: sin reflexión ideal",fontsize=20,color=COL["gray"]); save_fig(fig,d,"u04_fig_013_reflexion_impedancias"); return ["u04_fig_013_reflexion_impedancias"]


def ch014(d):
    x=np.linspace(0,20,500); inc=10*np.log10(1+10**(-x/10)); pd.DataFrame({"diferencia_nivel_dB":x,"incremento_total_dB":inc}).to_csv(d/"data.csv",index=False)
    fig,ax=fig_axes(); ax.plot(x,inc,color=COL["teal"],lw=3); style_ax(ax,xlabel="Diferencia entre niveles ΔL (dB)",ylabel="Incremento total (dB)",xlim=(-.35,20.5),ylim=(0,3.30))
    for v in [0,3,6,10,20]:
        y=10*np.log10(1+10**(-v/10)); ax.scatter(v,y,s=65,color=COL["bordo"],zorder=4)
        ax.annotate(f"{y:.2f}".replace(".",","),(v,y),xytext=((10 if v == 0 else 0),10),textcoords="offset points",ha=("left" if v == 0 else "center"),fontsize=19)
    save_fig(fig,d,"u04_fig_014_incremento_suma_niveles"); return ["u04_fig_014_incremento_suma_niveles"]


def ch015(d):
    x,a,b,s=coherent_plot(d,np.pi/2,"u04_fig_015_suma_cuadratura","φ = π/2 · amplitud resultante = √2"); pd.DataFrame({"t_sobre_T":x,"p_A":a,"p_B":b,"p_suma":s}).to_csv(d/"data.csv",index=False); return ["u04_fig_015_suma_cuadratura"],"- Verificación: aumento de nivel para amplitudes iguales=3,0103 dB.\n"


GEN={"U04-CH-001":ch001,"U04-CH-002":ch002,"U04-CH-003":ch003,"U04-CH-004":ch004,"U04-CH-005":ch005,"U04-CH-006":ch006,"U04-CH-007":ch007,"U04-CH-008":ch008,"U04-CH-009":ch009,"U04-CH-010":ch010,"U04-CH-011":ch011,"U04-CH-013":ch013,"U04-CH-014":ch014,"U04-CH-015":ch015}


def generate(cid):
    if cid == "U04-CH-012":
        raise RuntimeError("CH-012 requiere aprobación para descargar 326–466 MB del dataset Zenodo.")
    d=resource_dir(cid); result=GEN[cid](d)
    if isinstance(result,tuple): variants,metrics=result
    else: variants,metrics=result,""
    readme(cid,d,variants,metrics)
    return d


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("ids",nargs="*",default=list(GEN)); ns=ap.parse_args()
    for cid in ns.ids: print(generate(cid))


if __name__ == "__main__": main()
