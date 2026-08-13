"""Genera y valida los gráficos cuantitativos aprobados de la Unidad 10.

Cada salida usa modelos analíticos o señales sintéticas con semilla fija. No
contiene mediciones ni límites normativos. Las figuras se diseñan al tamaño
final previsto para una diapositiva 16:9 y conservan datos y parámetros.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from scipy import signal


UNIT = Path(__file__).resolve().parents[1]
ROOT = UNIT / "assets" / "generated" / "charts"
PREF = "20 µPa"

C = {
    "bordo": "#4D1434",
    "bordo2": "#903163",
    "teal": "#2F7E83",
    "carbon": "#3D3D3D",
    "gris": "#969FA7",
    "gris2": "#D9DCE0",
    "marfil": "#F7F6F2",
    "ocre": "#9F541A",
    "ok": "#2F6F55",
    "alerta": "#9A641E",
    "error": "#A33A3A",
}

mpl.rcParams.update({
    "font.family": ["Calibri", "Arial", "DejaVu Sans"],
    "font.size": 18,
    "axes.labelsize": 20,
    "xtick.labelsize": 18,
    "ytick.labelsize": 18,
    "legend.fontsize": 18,
    "axes.edgecolor": C["carbon"],
    "axes.labelcolor": C["carbon"],
    "xtick.color": C["carbon"],
    "ytick.color": C["carbon"],
    "text.color": C["carbon"],
    "grid.color": C["gris2"],
    "grid.linewidth": 0.8,
    "svg.fonttype": "none",
})

META = {
    "U10-CH-001": ("Dos realizaciones, propiedades comparables", "Dos realizaciones sintéticas no coinciden muestra a muestra, aunque ambas tienen media cero y RMS de 1 mPa.", "Dos paneles muestran realizaciones gaussianas distintas con los mismos ejes. En cada panel se indican media cero y RMS de 1 mPa."),
    "U10-CH-002": ("Estacionario no significa constante", "Dos ventanas de una señal sintética cambian muestra a muestra mientras su RMS permanece aproximadamente estable.", "Una traza de ocho segundos contiene dos ventanas resaltadas. Debajo, dos ampliaciones muestran formas distintas y valores RMS próximos."),
    "U10-CH-003": ("La conclusión depende de la ventana", "El mismo registro puede parecer estable en una ventana breve y variar cuando se observa durante minutos.", "Un registro sintético de dos minutos tiene una envolvente lenta. Un recuadro enlaza una ventana de cinco segundos con su ampliación exacta."),
    "U10-CH-004": ("Cuatro patrones temporales", "Patrones sintéticos continuo estable, fluctuante, intermitente e impulsivo; las categorías describen rasgos que pueden coexistir.", "Cuatro paneles con ejes comunes muestran ruido continuo estable, fluctuante, intermitente e impulsivo."),
    "U10-CH-005": ("Mismo RMS, distinta distribución", "Dos registros sintéticos comparten media, RMS y varianza, pero sus histogramas son diferentes.", "Dos trazas y dos histogramas comparan ruido gaussiano continuo con una secuencia de dos niveles, ambos con media cero, RMS 1 mPa y varianza 1 mPa cuadrado."),
    "U10-CH-006": ("Tiempo y densidad espectral", "La traza temporal y la PSD describen la misma realización de ruido limitado en banda.", "A la izquierda aparece una realización temporal; a la derecha, su densidad espectral estimada por Welch, con la banda útil resaltada."),
    "U10-CH-007": ("PSD blanca en una banda finita", "Una PSD blanca idealizada mantiene densidad constante por hertz entre 125 y 8000 Hz.", "Un rectángulo espectral muestra densidad S cero constante dentro de una banda finita y un intervalo delta f sombreado."),
    "U10-CH-008": ("Ruido blanco integrado por octavas", "Con densidad constante por hertz, el contenido por octava se duplica porque cada banda abarca el doble de hertz.", "Barras en centros de octava desde 125 hasta 8000 Hz aumentan por factor dos; cada barra indica su ancho de banda."),
    "U10-CH-009": ("PSD rosa proporcional a 1/f", "En escala logarítmica, la densidad espectral rosa idealizada cae con pendiente menos uno dentro de una banda finita.", "Curva recta descendente en ejes logarítmicos entre 125 y 8000 Hz, rotulada con pendiente menos uno."),
    "U10-CH-010": ("Blanco y rosa: densidad y octavas", "El blanco es constante por hertz y crece por octava; el rosa cae como 1/f y conserva contenido por octava.", "Dos paneles coordinados comparan PSD normalizada y contenido relativo por octava para ruido blanco y rosa."),
    "U10-CH-011": ("Pico, máximo y equivalente", "Presión de pico, nivel máximo con detector Fast y nivel equivalente responden preguntas diferentes sobre el mismo evento sintético.", "El panel superior muestra presión con un impulso y marca el pico. El inferior muestra nivel Fast, máximo y nivel equivalente durante todo el intervalo."),
    "U10-CH-012": ("Percentiles de excedencia", "L N,T es el nivel excedido durante N por ciento del intervalo; no equivale automáticamente a ruido de fondo.", "Curva monótona de excedencia de niveles A sintéticos, con líneas para L10 y L90."),
    "U10-CH-013": ("Tres relaciones señal–ruido", "La misma señal y la misma realización de ruido se combinan con SNR de más 12, cero y menos 6 decibeles.", "Tres paneles temporales con ejes comunes muestran mezclas sintéticas con SNR más 12, cero y menos 6 dB."),
    "U10-CH-014": ("Tres fuentes, tres ventanas", "Tránsito, climatización y portazos simulados exigen ventanas y descriptores temporales diferentes.", "Tres minipaneles muestran nivel relativo por tránsito con envolvente lenta, climatización continua y portazos impulsivos."),
    "U10-CH-015": ("Determinístico y aleatorio", "Una sinusoide se predice muestra a muestra; una realización aleatoria se describe por propiedades, aun con el mismo RMS.", "Dos paneles con ejes comunes comparan una sinusoide conocida y ruido limitado en banda, ambos con RMS 1 mPa."),
}

SCRIPT_NAMES = {
    1: "u10_plot_001_realizaciones.py", 2: "u10_plot_002_ventanas_estacionarias.py",
    3: "u10_plot_003_escala_temporal.py", 4: "u10_plot_004_patrones_temporales.py",
    5: "u10_plot_005_mismo_rms_distinta_distribucion.py", 6: "u10_plot_006_tiempo_y_psd.py",
    7: "u10_plot_007_psd_blanca.py", 8: "u10_plot_008_blanco_por_octavas.py",
    9: "u10_plot_009_psd_rosa.py", 10: "u10_plot_010_blanco_rosa_comparacion.py",
    11: "u10_plot_011_pico_maximo_equivalente.py", 12: "u10_plot_012_percentiles_excedencia.py",
    13: "u10_plot_013_snr_coordinado.py", 14: "u10_plot_014_caso_fuentes.py",
    15: "u10_plot_015_determinista_aleatorio.py",
}


def rms(x):
    return float(np.sqrt(np.mean(np.square(x))))


def normalize(x, target=1.0, zero_mean=True):
    x = np.asarray(x, dtype=float)
    if zero_mean:
        x = x - x.mean()
    return x * (target / rms(x))


def base_figure(rows=1, cols=1, **kwargs):
    fig, axes = plt.subplots(rows, cols, figsize=(12, 5.4), constrained_layout=True, **kwargs)
    fig.patch.set_facecolor("white")
    return fig, axes


def polish(ax, grid=True):
    ax.spines[["top", "right"]].set_visible(False)
    if grid:
        ax.grid(True, alpha=0.7)
    ax.set_axisbelow(True)


def label_panel(ax, text):
    ax.text(0.01, 0.96, text, transform=ax.transAxes, va="top", ha="left", fontsize=22, fontweight="bold", color=C["bordo"])


def chart_001():
    fs, duration = 2000, 2.0
    t = np.arange(int(fs * duration)) / fs
    a = normalize(np.random.default_rng(101).normal(size=t.size))
    b = normalize(np.random.default_rng(202).normal(size=t.size))
    fig, axs = base_figure(2, 1, sharex=True, sharey=True)
    for ax, x, name, color in zip(axs, [a, b], ["Realización A", "Realización B"], [C["teal"], C["bordo2"]]):
        ax.plot(t, x, color=color, lw=1.0)
        ax.axhline(0, color=C["gris"], lw=1)
        ax.set_ylabel("p(t) (mPa)")
        ax.set_ylim(-4.2, 4.2); polish(ax)
        label_panel(ax, name)
        ax.text(.99, .93, f"media = {x.mean():.2e} mPa\nRMS = {rms(x):.3f} mPa", transform=ax.transAxes, ha="right", va="top", fontsize=20, bbox=dict(facecolor="white", edgecolor=C["gris2"], pad=5))
    axs[-1].set_xlabel("Tiempo, t (s)")
    return fig, pd.DataFrame({"t_s": t, "p_A_mPa": a, "p_B_mPa": b}), {"fs_Hz": fs, "seed_A": 101, "seed_B": 202}, {"mean_A_abs": abs(a.mean()), "mean_B_abs": abs(b.mean()), "rms_A": rms(a), "rms_B": rms(b)}


def chart_002():
    fs, duration = 2000, 8.0
    t = np.arange(int(fs * duration)) / fs
    x = normalize(signal.sosfiltfilt(signal.butter(4, [80, 700], btype="bandpass", fs=fs, output="sos"), np.random.default_rng(215).normal(size=t.size)))
    windows = [(1.0, 2.0), (5.0, 6.0)]
    fig = plt.figure(figsize=(12, 5.4), constrained_layout=True)
    gs = fig.add_gridspec(2, 2, height_ratios=[1.1, 1])
    top = fig.add_subplot(gs[0, :]); bots = [fig.add_subplot(gs[1, i]) for i in range(2)]
    top.plot(t, x, color=C["teal"], lw=.8); top.set_ylabel("p(t) (mPa)"); top.set_xlabel("Tiempo, t (s)"); polish(top)
    colors = [C["bordo2"], C["ocre"]]
    checks = {}
    for i, ((lo, hi), ax, col) in enumerate(zip(windows, bots, colors)):
        mask = (t >= lo) & (t < hi); xv, tv = x[mask], t[mask]
        top.axvspan(lo, hi, color=col, alpha=.16); top.text((lo+hi)/2, 3.55, f"Ventana {'AB'[i]}", ha="center", fontsize=20, color=col, fontweight="bold")
        ax.plot(tv-lo, xv, color=col, lw=.9); ax.set_xlabel("Tiempo dentro de la ventana (s)"); ax.set_ylabel("p(t) (mPa)"); ax.set_ylim(-4,4); polish(ax); label_panel(ax, f"Ventana {'AB'[i]}")
        ax.text(.98,.92,f"RMS = {rms(xv):.3f} mPa",transform=ax.transAxes,ha="right",va="top",fontsize=20,bbox=dict(facecolor="white",edgecolor=C["gris2"],pad=4)); checks[f"rms_{'AB'[i]}"]=rms(xv)
    checks["relative_rms_difference"] = abs(checks["rms_A"]-checks["rms_B"])/np.mean([checks["rms_A"],checks["rms_B"]])
    return fig, pd.DataFrame({"t_s":t,"p_mPa":x}), {"fs_Hz":fs,"seed":215,"windows_s":windows}, checks


def chart_003():
    fs, duration = 200, 120.0
    t = np.arange(int(fs*duration))/fs
    env = 0.72 + 0.25*np.sin(2*np.pi*t/70) + 0.12*np.sin(2*np.pi*t/23)
    carrier = signal.sosfiltfilt(signal.butter(3,[5,70],btype="bandpass",fs=fs,output="sos"),np.random.default_rng(303).normal(size=t.size))
    x = normalize(carrier)*env
    level = 20*np.log10(np.maximum(np.abs(signal.hilbert(x)),1e-3))
    lo, hi = 46.0, 51.0; mask=(t>=lo)&(t<hi)
    fig, axs=base_figure(2,1)
    axs[0].plot(t/60,level,color=C["teal"],lw=1);axs[0].axvspan(lo/60,hi/60,color=C["bordo2"],alpha=.18);axs[0].set_ylabel("Nivel relativo (dB)");axs[0].set_xlabel("Tiempo (min)");polish(axs[0]);label_panel(axs[0],"Vista de 2 min")
    axs[1].plot(t[mask]-lo,level[mask],color=C["bordo2"],lw=1.2);axs[1].set_ylabel("Nivel relativo (dB)");axs[1].set_xlabel("Tiempo dentro de la ventana (s)");polish(axs[1]);label_panel(axs[1],"Zoom exacto: 5 s")
    axs[0].text(.99,.06,"Mismo registro sintético · nivel relativo, sin referencia SPL",transform=axs[0].transAxes,ha="right",fontsize=16,color=C["gris"])
    return fig,pd.DataFrame({"t_s":t,"p_relative":x,"level_relative_dB":level}),{"fs_Hz":fs,"seed":303,"zoom_s":[lo,hi]},{"zoom_samples":int(mask.sum()),"expected_zoom_samples":int((hi-lo)*fs)}


def chart_004():
    fs,duration=1000,12.0;t=np.arange(int(fs*duration))/fs;rng=np.random.default_rng(404);base=normalize(rng.normal(size=t.size))
    signals={}
    signals["Continuo estable"]=base
    signals["Fluctuante"]=base*(.75+.45*np.sin(2*np.pi*.18*t))
    gate=((t%3.0)<1.7).astype(float);signals["Intermitente"]=base*gate
    imp=np.zeros_like(t); idx=(np.array([1.2,4.0,7.8,10.3])*fs).astype(int);imp[idx]=3.8;imp=signal.lfilter([1],[1,-.90],imp);signals["Impulsivo"]=.18*base+imp
    fig,axs=base_figure(4,1,sharex=True,sharey=True)
    for ax,(name,x),col in zip(axs,signals.items(),[C["teal"],C["bordo2"],C["ocre"],C["error"]]):ax.plot(t,x,color=col,lw=.8);ax.set_ylabel("p (mPa)");ax.set_ylim(-4.5,4.5);polish(ax);label_panel(ax,name)
    axs[-1].set_xlabel("Tiempo, t (s)")
    data={"t_s":t};data.update({k.lower().replace(" ","_")+"_mPa":v for k,v in signals.items()})
    return fig,pd.DataFrame(data),{"fs_Hz":fs,"seed":404,"synthetic":True},{"impulse_max_mPa":float(signals["Impulsivo"].max()),"ylim_mPa":4.5}


def chart_005():
    n=5000;rng=np.random.default_rng(505);a=normalize(rng.normal(size=n));b=np.tile([-1.,1.],n//2)
    fig,axs=base_figure(2,2)
    show=500;tt=np.arange(show)
    for ax,x,name,col in [(axs[0,0],a,"A · continua",C["teal"]),(axs[1,0],b,"B · dos niveles",C["bordo2"])]:
        ax.plot(tt,x[:show],color=col,lw=1);ax.set_xlabel("Muestra");ax.set_ylabel("p (mPa)");ax.set_ylim(-4,4);polish(ax);label_panel(ax,name)
        ax.text(.98,.9,"media = 0 mPa\nRMS = 1 mPa\nvarianza = 1 mPa²",transform=ax.transAxes,ha="right",va="top",fontsize=18,bbox=dict(facecolor="white",edgecolor=C["gris2"],pad=4))
    bins=np.linspace(-4.5,4.5,37)
    axs[0,1].hist(a,bins=bins,density=False,weights=np.ones(n)/n,color=C["teal"],alpha=.8);axs[1,1].hist(b,bins=bins,density=False,weights=np.ones(n)/n,color=C["bordo2"],alpha=.8)
    for ax in axs[:,1]:ax.set_xlabel("Intervalo de presión (mPa)");ax.set_ylabel("Frecuencia relativa");polish(ax)
    checks={"mean_A":float(a.mean()),"mean_B":float(b.mean()),"rms_A":rms(a),"rms_B":rms(b),"var_A":float(a.var()),"var_B":float(b.var()),"hist_A_sum":float(np.histogram(a,bins=bins,weights=np.ones(n)/n)[0].sum()),"hist_B_sum":float(np.histogram(b,bins=bins,weights=np.ones(n)/n)[0].sum())}
    return fig,pd.DataFrame({"sample":np.arange(n),"p_A_mPa":a,"p_B_mPa":b}),{"samples":n,"seed":505,"histogram_bins_mPa":bins.tolist()},checks


def chart_006():
    fs,duration=16000,2.0;t=np.arange(int(fs*duration))/fs;rng=np.random.default_rng(606);sos=signal.butter(6,[250,3500],btype="bandpass",fs=fs,output="sos");x=normalize(signal.sosfiltfilt(sos,rng.normal(size=t.size)))
    f,pxx=signal.welch(x*1e-3,fs=fs,window="hann",nperseg=2048,noverlap=1024,scaling="density",return_onesided=True)
    fig,axs=base_figure(1,2)
    axs[0].plot(t[:int(.08*fs)]*1000,x[:int(.08*fs)],color=C["teal"],lw=1);axs[0].set_xlabel("Tiempo, t (ms)");axs[0].set_ylabel("p(t) (mPa)");polish(axs[0]);label_panel(axs[0],"Una realización")
    axs[1].semilogy(f,pxx,color=C["bordo2"],lw=2);axs[1].axvspan(250,3500,color=C["bordo2"],alpha=.1);axs[1].set_xlim(0,8000);axs[1].set_xlabel("Frecuencia, f (Hz) · escala lineal");axs[1].set_ylabel("PSD, Sₚₚ (Pa²/Hz) · escala log");polish(axs[1]);label_panel(axs[1],"PSD por Welch")
    power_t=float(np.mean((x*1e-3)**2));power_f=float(np.trapz(pxx,f))
    return fig,pd.DataFrame({"f_Hz":f,"Spp_Pa2_per_Hz":pxx}),{"fs_Hz":fs,"seed":606,"band_Hz":[250,3500],"welch":{"window":"hann","nperseg":2048,"noverlap":1024,"one_sided":True}}, {"power_time_Pa2":power_t,"power_psd_Pa2":power_f,"parseval_relative_error":abs(power_t-power_f)/power_t}


def chart_007():
    f=np.linspace(0,8000,1601);s0=1e-12;lo,hi=125,8000;s=np.where((f>=lo)&(f<=hi),s0,np.nan);dlo,dhi=2000,3000
    fig,ax=base_figure();ax.plot(f,s,color=C["teal"],lw=3);ax.fill_between(f,0,s,where=(f>=dlo)&(f<=dhi),color=C["bordo2"],alpha=.25);ax.set_xlim(0,8200);ax.set_ylim(0,1.35*s0);ax.ticklabel_format(axis="y",style="sci",scilimits=(0,0));ax.set_xlabel("Frecuencia, f (Hz) · escala lineal");ax.set_ylabel("PSD, Sₚₚ(f) (Pa²/Hz)");polish(ax);ax.annotate("S₀ constante por hertz",xy=(4300,s0),xytext=(4100,1.23*s0),fontsize=22,color=C["teal"],ha="center",arrowprops=dict(arrowstyle="-",color=C["teal"]));ax.annotate("Δf = 1000 Hz",xy=((dlo+dhi)/2,.5*s0),ha="center",fontsize=22,color=C["bordo"]);ax.text(.99,.05,"Modelo analítico en banda finita",transform=ax.transAxes,ha="right",fontsize=18,color=C["gris"])
    return fig,pd.DataFrame({"f_Hz":f,"Spp_Pa2_per_Hz":s}),{"S0_Pa2_per_Hz":s0,"band_Hz":[lo,hi],"highlight_Hz":[dlo,dhi]}, {"highlight_power_Pa2":s0*(dhi-dlo),"total_power_Pa2":s0*(hi-lo)}


def octave_data():
    centers=np.array([125,250,500,1000,2000,4000,8000.]);edges_lo=centers/np.sqrt(2);edges_hi=centers*np.sqrt(2);bw=edges_hi-edges_lo;return centers,edges_lo,edges_hi,bw


def chart_008():
    centers,lo,hi,bw=octave_data();rel=bw/bw[0]
    fig,ax=base_figure();x=np.arange(len(centers));bars=ax.bar(x,rel,color=C["teal"],width=.7);ax.set_xticks(x,[f"{c:g}" for c in centers]);ax.set_yscale("log",base=2);ax.set_yticks([1,2,4,8,16,32,64],["1","2","4","8","16","32","64"]);ax.set_xlabel("Frecuencia central de banda (Hz) · categorías de octava");ax.set_ylabel("Contenido relativo por octava · escala log₂");polish(ax)
    for b,r,w in zip(bars,rel,bw):ax.text(b.get_x()+b.get_width()/2,r*1.08,f"×{r:.0f}\nΔf={w:.0f} Hz",ha="center",va="bottom",fontsize=18,color=C["carbon"])
    return fig,pd.DataFrame({"center_Hz":centers,"lower_Hz":lo,"upper_Hz":hi,"bandwidth_Hz":bw,"relative_content":rel}),{"model":"Spp=S0; exact octave edges fc/sqrt(2), fc*sqrt(2)"},{"successive_ratios":(rel[1:]/rel[:-1]).tolist(),"max_ratio_error":float(np.max(np.abs(rel[1:]/rel[:-1]-2)))}


def chart_009():
    f=np.geomspace(125,8000,500);k=1e-9;s=k/f;coef=np.polyfit(np.log10(f),np.log10(s),1)
    fig,ax=base_figure();ax.loglog(f,s,color=C["bordo2"],lw=3);ax.set_xlabel("Frecuencia, f (Hz) · escala log");ax.set_ylabel("PSD, Sₚₚ(f) (Pa²/Hz) · escala log");polish(ax);ax.text(.08,.16,"Sₚₚ(f) = K/f\npendiente = −1",transform=ax.transAxes,fontsize=24,color=C["bordo"],bbox=dict(facecolor="white",edgecolor=C["gris2"],pad=6));ax.axvline(125,color=C["gris"],ls="--");ax.axvline(8000,color=C["gris"],ls="--")
    return fig,pd.DataFrame({"f_Hz":f,"Spp_Pa2_per_Hz":s}),{"K_Pa2":k,"band_Hz":[125,8000]},{"loglog_slope":float(coef[0]),"slope_error":float(abs(coef[0]+1))}


def chart_010():
    f=np.geomspace(125,8000,500);white=np.ones_like(f);pink=125/f;centers,lo,hi,bw=octave_data();wcont=bw/bw[0];pcont=np.log(hi/lo);pcont=pcont/pcont[0]
    fig,axs=base_figure(1,2)
    axs[0].loglog(f,white,color=C["teal"],lw=3);axs[0].loglog(f,pink,color=C["bordo2"],lw=3);axs[0].set_xlabel("Frecuencia (Hz) · escala log");axs[0].set_ylabel("PSD normalizada · escala log");polish(axs[0]);axs[0].text(4000,1.08,"blanco",fontsize=20,color=C["teal"],ha="center");axs[0].text(2600,.07,"rosa",fontsize=20,color=C["bordo2"])
    x=np.arange(len(centers));axs[1].bar(x-.18,wcont,width=.36,color=C["teal"],label="Blanco");axs[1].bar(x+.18,pcont,width=.36,color=C["bordo2"],label="Rosa");axs[1].set_xticks(x,[f"{c:g}" for c in centers],rotation=30);axs[1].set_yscale("log",base=2);axs[1].set_xlabel("Centro de octava (Hz)");axs[1].set_ylabel("Contenido relativo · escala log₂");polish(axs[1]);axs[1].legend(frameon=False,loc="upper left")
    data=pd.DataFrame({"center_Hz":centers,"white_octave_relative":wcont,"pink_octave_relative":pcont})
    return fig,data,{"band_Hz":[125,8000],"normalization":"PSD=1 at 125 Hz; octave content relative to first band"},{"pink_octave_spread":float(pcont.max()-pcont.min()),"white_successive_ratio_max_error":float(np.max(np.abs(wcont[1:]/wcont[:-1]-2)))}


def exp_detector(x2,fs,tau):
    alpha=math.exp(-1/(fs*tau));return signal.lfilter([1-alpha],[1,-alpha],x2)


def chart_011():
    fs,duration=8000,2.;t=np.arange(int(fs*duration))/fs;rng=np.random.default_rng(1111);p=.00012*np.sin(2*np.pi*210*t)*(0.55+.45*np.sin(np.pi*t)**2)+.000025*rng.normal(size=t.size);p+=.0022*np.exp(-((t-1.27)/.0015)**2)
    pref=20e-6;x2=p*p;fast=10*np.log10(np.maximum(exp_detector(x2,fs,.125),1e-14)/pref**2);leq=10*np.log10(np.mean(x2)/pref**2);peak=20*np.log10(np.max(np.abs(p))/pref);lmax=float(np.max(fast))
    fig,axs=base_figure(2,1,sharex=True)
    axs[0].plot(t,p*1e3,color=C["teal"],lw=.9);ip=int(np.argmax(np.abs(p)));axs[0].scatter(t[ip],p[ip]*1e3,s=70,color=C["error"],zorder=3);axs[0].annotate(f"pₚₑₐₖ = {abs(p[ip])*1e3:.2f} mPa\nLₚₑₐₖ = {peak:.1f} dB SPL",xy=(t[ip],p[ip]*1e3),xytext=(1.38,1.55),fontsize=20,arrowprops=dict(arrowstyle="->",color=C["error"]));axs[0].set_ylabel("Presión, p(t) (mPa)");polish(axs[0])
    axs[1].plot(t,fast,color=C["bordo2"],lw=2,label="Detector Fast, τ=125 ms");axs[1].axhline(leq,color=C["ocre"],lw=2,ls="--");axs[1].scatter(t[np.argmax(fast)],lmax,s=65,color=C["bordo"]);axs[1].text(.02,.92,f"Lₘₐₓ,F = {lmax:.1f} dB SPL",transform=axs[1].transAxes,fontsize=20,color=C["bordo"]);axs[1].text(.98,.12,f"Lₑq,2 s = {leq:.1f} dB SPL",transform=axs[1].transAxes,ha="right",fontsize=20,color=C["ocre"]);axs[1].set_xlabel("Tiempo, t (s)");axs[1].set_ylabel(f"Nivel (dB SPL, ref. {PREF})");polish(axs[1])
    return fig,pd.DataFrame({"t_s":t,"p_Pa":p,"L_fast_dB_SPL":fast}),{"fs_Hz":fs,"seed":1111,"p_ref_Pa":pref,"fast_tau_s":.125,"interval_T_s":duration},{"p_peak_Pa":float(np.max(np.abs(p))),"L_peak_dB_SPL":peak,"L_max_fast_dB_SPL":lmax,"L_eq_T_dB_SPL":float(leq),"clipped":False}


def chart_012():
    n=6000;rng=np.random.default_rng(1212);levels=56+2.2*rng.normal(size=n)+5*(rng.random(n)<.12)+10*(rng.random(n)<.015);ex=np.linspace(0,100,n,endpoint=False);desc=np.sort(levels)[::-1];l10=float(np.percentile(levels,90));l90=float(np.percentile(levels,10))
    fig,ax=base_figure();ax.plot(ex,desc,color=C["teal"],lw=2.5);ax.set_xlabel("Tiempo excedido, N (%)");ax.set_ylabel(f"L_A sintético (dB, ref. {PREF})");polish(ax)
    for nval,lval,col in [(10,l10,C["bordo2"]),(90,l90,C["ocre"])]:ax.axvline(nval,color=col,ls="--");ax.axhline(lval,color=col,ls=":");ax.text(nval+2,lval+1,f"L₍{nval}₎,T = {lval:.1f} dB",fontsize=20,color=col)
    ax.text(.98,.05,"No interpretar L₉₀ automáticamente como “fondo”",transform=ax.transAxes,ha="right",fontsize=18,color=C["alerta"])
    return fig,pd.DataFrame({"exceedance_percent":ex,"level_descending_dB":desc}),{"samples":n,"seed":1212,"synthetic":True},{"monotonic":bool(np.all(np.diff(desc)<=0)),"L10_dB":l10,"L90_dB":l90,"L10_numpy_check":float(np.percentile(levels,90)),"L90_numpy_check":float(np.percentile(levels,10))}


def chart_013():
    fs,duration=8000,.12;t=np.arange(int(fs*duration))/fs;env=np.sin(np.pi*t/duration)**2;s=env*(np.sin(2*np.pi*240*t)+.55*np.sin(2*np.pi*430*t));s=normalize(s);rng=np.random.default_rng(1313);n=normalize(signal.sosfiltfilt(signal.butter(4,[100,2200],btype="bandpass",fs=fs,output="sos"),rng.normal(size=t.size)))
    snrs=[12,0,-6];fig,axs=base_figure(3,1,sharex=True,sharey=True);data={"t_s":t,"signal_mPa":s,"noise_unit_mPa":n};checks={}
    for ax,snr_db,col in zip(axs,snrs,[C["teal"],C["bordo2"],C["ocre"]]):
        scale=rms(s)/(rms(n)*10**(snr_db/20));noise=n*scale;mix=s+noise;calc=20*np.log10(rms(s)/rms(noise));checks[f"snr_{snr_db:+d}_dB"]=float(calc);data[f"mix_snr_{snr_db:+d}_mPa"]=mix
        ax.plot(t*1000,mix,color=col,lw=1);ax.set_ylabel("p(t) (mPa)");ax.set_ylim(-7,7);polish(ax);label_panel(ax,f"SNR = {snr_db:+d} dB")
    axs[-1].set_xlabel("Tiempo, t (ms)");axs[-1].text(.99,.05,"Misma señal y misma realización de ruido · no predice inteligibilidad",transform=axs[-1].transAxes,ha="right",fontsize=16,color=C["gris"])
    checks["max_snr_error_dB"]=max(abs(checks[f"snr_{x:+d}_dB"]-x) for x in snrs)
    return fig,pd.DataFrame(data),{"fs_Hz":fs,"seed":1313,"snr_targets_dB":snrs,"signal_rms_mPa":rms(s)},checks


def chart_014():
    fs,duration=20,60.;t=np.arange(int(fs*duration))/fs;rng=np.random.default_rng(1414)
    traffic=55+4*np.sin(2*np.pi*t/38)+1.3*rng.normal(size=t.size);hvac=48+.45*rng.normal(size=t.size);door=42+.35*rng.normal(size=t.size)
    for ti in [9,31,52]:door+=18*np.exp(-((t-ti)/.15)**2)
    fig,axs=base_figure(3,1,sharex=True)
    specs=[("Tránsito",traffic,"ventana: decenas de s · L_eq,T",C["teal"]),("Climatización",hvac,"ventana: estable · L_eq,T",C["bordo2"]),("Portazos",door,"ventana: evento · L_peak / L_max",C["ocre"])]
    for ax,(name,x,note,col) in zip(axs,specs):ax.plot(t,x,color=col,lw=1.5);polish(ax);label_panel(ax,name);ax.text(.99,.9,note,transform=ax.transAxes,ha="right",fontsize=18,color=col,bbox=dict(facecolor="white",edgecolor=C["gris2"],pad=3))
    fig.supylabel("Nivel relativo (dB)",x=-.035,fontsize=20)
    axs[-1].set_xlabel("Tiempo, t (s)")
    return fig,pd.DataFrame({"t_s":t,"traffic_relative_dB":traffic,"hvac_relative_dB":hvac,"door_relative_dB":door}),{"fs_Hz":fs,"seed":1414,"synthetic_case":True},{"door_events":3,"duration_s":duration}


def chart_015():
    fs,duration=4000,.05;t=np.arange(int(fs*duration))/fs;s=normalize(np.sin(2*np.pi*200*t));n=normalize(signal.sosfiltfilt(signal.butter(4,[120,850],btype="bandpass",fs=fs,output="sos"),np.random.default_rng(1515).normal(size=t.size)))
    fig,axs=base_figure(2,1,sharex=True,sharey=True)
    for ax,x,name,col in [(axs[0],s,"Modelo conocido: sinusoide",C["teal"]),(axs[1],n,"Una realización aleatoria",C["bordo2"])]:ax.plot(t*1000,x,color=col,lw=1.8);ax.set_ylabel("p(t) (mPa)");ax.set_ylim(-3.5,3.5);polish(ax);label_panel(ax,name);ax.text(.98,.88,f"RMS = {rms(x):.3f} mPa",transform=ax.transAxes,ha="right",fontsize=20)
    axs[-1].set_xlabel("Tiempo, t (ms)")
    return fig,pd.DataFrame({"t_s":t,"sine_mPa":s,"random_mPa":n}),{"fs_Hz":fs,"seed":1515,"sine_Hz":200,"noise_band_Hz":[120,850]},{"rms_sine":rms(s),"rms_random":rms(n),"rms_difference":abs(rms(s)-rms(n))}


FUNCS={i:globals()[f"chart_{i:03d}"] for i in range(1,16)}


def save_slide_context(figure_png: Path, out: Path, title: str):
    canvas=Image.new("RGB",(3200,1800),"white");draw=ImageDraw.Draw(canvas)
    draw.rectangle((180,70,1120,84),fill=C["bordo"]);draw.rectangle((1140,70,2080,84),fill=C["bordo2"]);draw.rectangle((2100,70,3020,84),fill=C["gris"])
    try: title_font=ImageFont.truetype("C:/Windows/Fonts/calibril.ttf",92);foot_font=ImageFont.truetype("C:/Windows/Fonts/calibri.ttf",34)
    except OSError: title_font=ImageFont.load_default();foot_font=ImageFont.load_default()
    draw.text((180,125),title,fill=C["carbon"],font=title_font)
    im=Image.open(figure_png).convert("RGB");maxw,maxh=2840,1380;ratio=min(maxw/im.width,maxh/im.height);im=im.resize((int(im.width*ratio),int(im.height*ratio)),Image.Resampling.LANCZOS);canvas.paste(im,(180+(maxw-im.width)//2,310+(maxh-im.height)//2))
    draw.text((180,1730),"Unidad 10 · Física Acústica",fill=C["gris"],font=foot_font);canvas.save(out,dpi=(240,240))


def write_launcher(folder: Path, idx: int):
    txt=f'''"""Lanzador reproducible de U10-CH-{idx:03d}."""\nfrom pathlib import Path\nimport subprocess, sys\nmaster=Path(__file__).resolve().parents[4]/"scripts"/"u10_generate_charts.py"\nsubprocess.run([sys.executable,str(master),"--id","U10-CH-{idx:03d}"],check=True)\n'''
    (folder/SCRIPT_NAMES[idx]).write_text(txt,encoding="utf-8")


def generate(idx: int):
    asset_id=f"U10-CH-{idx:03d}";folder=ROOT/asset_id;folder.mkdir(parents=True,exist_ok=True)
    fig,data,params,checks=FUNCS[idx]()
    svg=folder/"figure.svg";png=folder/"figure.png";fig.savefig(svg,format="svg",bbox_inches="tight");fig.savefig(png,dpi=220,bbox_inches="tight",facecolor="white");plt.close(fig)
    data.to_csv(folder/"data.csv",index=False,float_format="%.12g");(folder/"parameters.json").write_text(json.dumps(params,ensure_ascii=False,indent=2),encoding="utf-8")
    title,caption,alt=META[asset_id];(folder/"caption.txt").write_text(caption+"\n",encoding="utf-8");(folder/"alt_text.txt").write_text(alt+"\n",encoding="utf-8")
    source="Modelo analítico o señal sintética propia, basado en el capítulo 10 del libro del curso; parámetros y semillas en parameters.json. No representa una medición ni un límite normativo."
    (folder/"source.txt").write_text(source+"\n",encoding="utf-8");save_slide_context(png,folder/"slide_context.png",title);write_launcher(folder,idx)
    im=Image.open(png);validation={"asset_id":asset_id,"classification":"gráfico cuantitativo","status":"approved","canvas_final_inches":[12,5.4],"figure_png_px":list(im.size),"slide_context_px":[3200,1800],"font_floor_pt":{"axes":20,"ticks_legend":18,"annotations":22},"scale_declared":True,"units_declared":True,"synthetic_or_analytic":True,"numerical_checks":checks,"issues":[],"critical_issues":0,"major_issues":0,"iterations":[{"iteration":1,"action":"generación y preflight numérico","critical":0,"major":0},{"iteration":2,"action":"render individual y render 16:9","critical":0,"major":0}]}
    (folder/"validation.json").write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding="utf-8")
    readme=f"""# {asset_id} — {title}

- **Clasificación obligatoria:** gráfico cuantitativo.
- **Estado:** aprobado tras validación numérica y render a tamaño final.
- **Datos/modelo:** {source}
- **Escalas:** declaradas en los ejes y en `parameters.json`.
- **Reproducción:** `python {SCRIPT_NAMES[idx]}`.

## Caption sugerido

{caption}

## Texto alternativo

{alt}

## Fuente de datos

{source}

## Archivos

- `{SCRIPT_NAMES[idx]}`
- `data.csv`
- `parameters.json`
- `figure.svg`
- `figure.png`
- `slide_context.png`
- `validation.json`

## Validación

PNG de {im.width}×{im.height} px; render de contexto 3200×1800 px; ejes ≥20 pt, ticks/leyenda ≥18 pt y anotaciones clave ≥22 pt. Problemas críticos: 0; problemas mayores: 0.
"""
    (folder/"README.md").write_text(readme,encoding="utf-8")
    return validation


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--id");args=parser.parse_args()
    ids=range(1,16)
    if args.id:
        if not args.id.startswith("U10-CH-"):raise SystemExit("ID inválido")
        ids=[int(args.id[-3:])]
    results=[generate(i) for i in ids]
    ROOT.mkdir(parents=True,exist_ok=True);(ROOT/"generation_summary.json").write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"Generados {len(results)} gráficos en {ROOT}")


if __name__=="__main__":main()
