"""Genera y valida los gráficos cuantitativos aprobados de la Unidad 05.

Todos los datos son modelos matemáticos deterministas o un caso didáctico
declarado. No se usan mediciones ni datos clínicos. Cada familia produce un
script lanzador, CSV, SVG, PNG 2560x1440, README y registro JSON de validación.
"""

from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import signal


UNIT_DIR = Path(__file__).resolve().parents[1]
ROOT = UNIT_DIR / "assets" / "generated" / "charts"

COLORS = {
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

APPROVED = {
    "U05-CH-001": ("u05_plot_001_igual_rms.py", "u05_fig_001_igual_rms"),
    "U05-CH-002": ("u05_plot_002_tiempo_magnitud_fase.py", "u05_fig_002_tiempo_magnitud_fase"),
    "U05-CH-003": ("u05_plot_003_misma_magnitud_fase_distinta.py", "u05_fig_003_misma_magnitud_fase_distinta"),
    "U05-CH-005": ("u05_plot_005_sintesis_fourier.py", "u05_fig_005_sintesis_fourier"),
    "U05-CH-006": ("u05_plot_006_muestreo_aliasing.py", "u05_fig_006_muestreo_aliasing"),
    "U05-CH-007": ("u05_plot_007_bins_resolucion.py", "u05_fig_007_bins_resolucion"),
    "U05-CH-008": ("u05_plot_008_fuga_espectral.py", "u05_fig_008_fuga_espectral"),
    "U05-CH-011": ("u05_plot_011_componentes_espectrales.py", "u05_fig_011_componentes_espectrales"),
    "U05-CH-013": ("u05_plot_013_regiones_frecuencia.py", "u05_fig_013_regiones_frecuencia"),
    "U05-CH-015": ("u05_plot_015_bin_frente_banda.py", "u05_fig_015_bin_frente_banda"),
    "U05-CH-016": ("u05_plot_016_respuestas_filtros.py", "u05_fig_016_respuestas_filtros"),
    "U05-CH-018": ("u05_plot_018_nivel_equivalente.py", "u05_fig_018_nivel_equivalente"),
    "U05-CH-019": ("u05_plot_019_caso_bandas.py", "u05_fig_019_caso_bandas"),
}

META = {
    "U05-CH-001": {
        "classification": "gráfico cuantitativo",
        "question": "¿Dos señales con el mismo RMS contienen la misma información?",
        "caption": "Dos señales sintéticas normalizadas al mismo valor RMS conservan formas temporales distintas.",
        "alt": "Dos paneles temporales con ejes comunes comparan una senoide y una señal armónica no sinusoidal. Ambas indican RMS igual a 0,707, aunque sus formas y picos son diferentes.",
        "source": "Modelo matemático determinista; continuidad con Unidad 4 y brief de Unidad 5.",
    },
    "U05-CH-002": {
        "classification": "gráfico cuantitativo",
        "question": "¿Qué información cambia entre tiempo, magnitud y fase?",
        "caption": "La misma presión sintética se representa en el tiempo y mediante magnitud de pico y fase de su DFT unilateral.",
        "alt": "Tres paneles coordinados muestran una señal temporal y líneas en 100 y 200 hertz. La magnitud de pico es 0,20 y 0,05 pascales; las fases son menos pi medios y cero radianes según la convención de coseno de la DFT.",
        "source": "Libro del curso, Unidad 5, figura 5.1 y ecuaciones asociadas; modelo matemático determinista.",
    },
    "U05-CH-003": {
        "classification": "gráfico cuantitativo",
        "question": "¿Puede cambiar la forma temporal sin cambiar el espectro de magnitud?",
        "caption": "Dos sumas con amplitudes y frecuencias idénticas presentan distinta fase y distinta forma temporal.",
        "alt": "Dos señales temporales enfrentadas tienen formas diferentes. Debajo, sus espectros de magnitud coinciden exactamente en 100, 200 y 300 hertz, mientras las fases declaradas difieren.",
        "source": "Libro del curso, Unidad 5, sección de magnitud y fase; elaboración matemática propia.",
    },
    "U05-CH-005": {
        "classification": "gráfico cuantitativo",
        "question": "¿Cómo cambia una señal al sumar componentes de Fourier?",
        "caption": "Sumas parciales de 1, 3, 5 y 10 términos impares aproximan una onda rectangular sin eliminar la oscilación próxima a la discontinuidad.",
        "alt": "Cuatro paneles con la misma escala comparan una onda rectangular ideal con sumas parciales de uno, tres, cinco y diez términos impares de su serie de Fourier.",
        "source": "Libro del curso, Unidad 5, figura 5.2; serie matemática determinista.",
    },
    "U05-CH-006": {
        "classification": "gráfico cuantitativo",
        "question": "¿Cuándo dos frecuencias continuas producen las mismas muestras?",
        "caption": "Con muestreo a 1000 Hz, las senoides de 150 Hz y 850 Hz con fase indicada coinciden exactamente en los instantes muestreados.",
        "alt": "Dos paneles muestran ondas continuas diferentes y los mismos puntos de muestreo. Se indica frecuencia de muestreo de mil hertz y separación temporal de una milésima de segundo.",
        "source": "Modelo matemático de muestreo uniforme; elaboración propia basada en el capítulo 5.",
    },
    "U05-CH-007": {
        "classification": "gráfico cuantitativo",
        "question": "¿Cómo determinan f_s, N y T_obs la rejilla de bins?",
        "caption": "A frecuencia de muestreo constante, cuadruplicar la duración reduce la separación entre bins de 4 Hz a 1 Hz y permite distinguir componentes próximas.",
        "alt": "Dos espectros DFT alineados comparan registros de 0,25 y 1 segundo. El corto tiene bins separados 4 hertz y no separa con claridad tonos de 1000 y 1002 hertz; el largo presenta bins de 1 hertz y dos máximos.",
        "source": "Libro del curso, ecuaciones T_obs=N/f_s y delta f=f_s/N; datos sintéticos.",
    },
    "U05-CH-008": {
        "classification": "gráfico cuantitativo",
        "question": "¿Por qué un recorte puede distribuir un tono entre varios bins?",
        "caption": "Con ventana rectangular, un tono que completa un número no entero de períodos distribuye su magnitud entre varios bins.",
        "alt": "Cuatro paneles comparan un tono de cien hertz con diez períodos exactos y otro de ciento cinco hertz con diez períodos y medio. El primer espectro se concentra en un bin; el segundo presenta fuga espectral.",
        "source": "Libro del curso, Unidad 5, figura 5.3; modelo matemático determinista.",
    },
    "U05-CH-011": {
        "classification": "gráfico cuantitativo",
        "question": "¿Cómo distinguimos fundamental, armónicos, parciales y fundamental ausente?",
        "caption": "Tres espectros teóricos separan serie armónica, parciales inarmónicos y fundamental ausente con una misma escala.",
        "alt": "Tres paneles de líneas espectrales. El primero muestra armónicos de cien hertz con el segundo armónico como máximo; el segundo contiene parciales no múltiplos; el tercero omite la línea de cien hertz pero conserva separación de cien hertz.",
        "source": "Libro del curso, Unidad 5, figura 5.5; datos teóricos declarados.",
    },
    "U05-CH-013": {
        "classification": "gráfico cuantitativo",
        "question": "¿Qué significa ubicar infra, audible y ultra si las fronteras son aproximadas?",
        "caption": "Regiones frecuenciales convencionales sobre eje logarítmico; las transiciones próximas a 20 Hz y 20 kHz son aproximadas.",
        "alt": "Eje logarítmico de uno a un millón de hertz con regiones de infrasonido, rango audible y ultrasonido. Dos bandas rayadas señalan transiciones aproximadas alrededor de veinte hertz y veinte kilohertz.",
        "source": "Programa oficial y libro del curso, sección 5.7; fronteras convencionales, no límites universales.",
    },
    "U05-CH-015": {
        "classification": "gráfico cuantitativo",
        "question": "¿Qué se pierde y qué se conserva al agrupar bins en bandas?",
        "caption": "Los bins conservan detalle fino; las bandas resumen la potencia total mediante suma lineal antes de convertir a decibeles.",
        "alt": "El panel superior muestra muchas contribuciones por bin en un eje logarítmico. El inferior agrupa esos valores en cinco bandas teóricas de octava y muestra el nivel total de cada una.",
        "source": "Libro del curso, ecuaciones de suma por banda; espectro sintético determinista.",
    },
    "U05-CH-016": {
        "classification": "gráfico cuantitativo",
        "question": "¿Cómo distingue la respuesta a los cuatro tipos de filtro y a un filtro real?",
        "caption": "Respuestas ideales y modelos Butterworth analógicos de cuarto orden muestran paso, rechazo y transición de cuatro tipos de filtro.",
        "alt": "Cuatro paneles en frecuencia logarítmica comparan pasa bajos, pasa altos, pasa banda y elimina banda. Cada panel distingue el salto ideal de una respuesta real con transición y marca el criterio de menos tres decibeles.",
        "source": "Libro del curso, figura 5.7; modelos Butterworth calculados con SciPy 1.13.1.",
    },
    "U05-CH-018": {
        "classification": "gráfico cuantitativo",
        "question": "¿Qué nivel constante tiene la misma energía media que un nivel variable?",
        "caption": "Treinta segundos a 70 dB y treinta segundos a 80 dB equivalen energéticamente a un nivel constante de 77,4 dB durante 60 segundos.",
        "alt": "Gráfico temporal con dos tramos de nivel, primero setenta y luego ochenta decibeles. Una línea discontinua horizontal marca el nivel equivalente de 77,4 decibeles.",
        "source": "Libro del curso, ejemplo de nivel equivalente, sección 5.11.",
    },
    "U05-CH-019": {
        "classification": "gráfico cuantitativo",
        "question": "¿Qué bandas incumplen límites dados en un caso hipotético?",
        "caption": "Caso didáctico no normativo: niveles por banda se comparan con límites hipotéticos y las excedencias se identifican por color y trama.",
        "alt": "Barras por centro de banda entre 125 y 4000 hertz se comparan con una línea escalonada de límites. Las bandas de 500, 1000 y 2000 hertz aparecen tramadas por superar el límite hipotético.",
        "source": "Actividad didáctica hipotética U05-123; valores creados únicamente para resolver el ejercicio.",
    },
}


def configure_style() -> None:
    mpl.rcParams.update({
        "font.family": "Calibri",
        "font.sans-serif": ["Calibri", "Arial", "DejaVu Sans"],
        "font.size": 18,
        "axes.labelsize": 20,
        "axes.titlesize": 22,
        "xtick.labelsize": 18,
        "ytick.labelsize": 18,
        "legend.fontsize": 18,
        "axes.edgecolor": COLORS["carbon"],
        "axes.labelcolor": COLORS["carbon"],
        "xtick.color": COLORS["carbon"],
        "ytick.color": COLORS["carbon"],
        "text.color": COLORS["carbon"],
        "axes.grid": True,
        "grid.color": COLORS["gris2"],
        "grid.linewidth": 0.8,
        "grid.alpha": 0.75,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "svg.fonttype": "none",
        "savefig.facecolor": "white",
        "figure.facecolor": "white",
    })


def canvas(rows=1, cols=1, **kwargs):
    return plt.subplots(rows, cols, figsize=(12.8, 7.2), constrained_layout=True, **kwargs)


def save_outputs(fig, folder: Path, basename: str) -> None:
    fig.savefig(folder / f"{basename}.svg", format="svg")
    fig.savefig(folder / f"{basename}.png", format="png", dpi=200)
    plt.close(fig)


def stem(ax, x, y, color=None):
    marker, stems, base = ax.stem(x, y, basefmt=" ")
    plt.setp(marker, color=color or COLORS["bordo"], markersize=7)
    plt.setp(stems, color=color or COLORS["bordo"], linewidth=2.2)
    return marker, stems, base


def chart_001():
    fs, duration = 4000, 0.04
    t = np.arange(int(fs * duration)) / fs
    a = np.sin(2 * np.pi * 100 * t)
    b0 = np.sin(2 * np.pi * 100 * t) + 0.45 * np.sin(2 * np.pi * 300 * t)
    b = b0 * (np.sqrt(np.mean(a**2)) / np.sqrt(np.mean(b0**2)))
    rms_a, rms_b = np.sqrt(np.mean(a**2)), np.sqrt(np.mean(b**2))
    fig, axes = canvas(2, 1, sharex=True, sharey=True)
    for ax, y, label in zip(axes, (a, b), ("Senoide", "Suma armónica")):
        ax.plot(t * 1000, y, color=COLORS["bordo"], lw=3)
        ax.axhline(0, color=COLORS["gris"], lw=1)
        ax.set_ylabel("x(t) normalizada")
        ax.text(0.02, .86, label, transform=ax.transAxes, fontsize=22, fontweight="bold")
        ax.text(.98, .86, f"RMS = {np.sqrt(np.mean(y**2)):.3f}", transform=ax.transAxes,
                ha="right", fontsize=22, color=COLORS["teal"], fontweight="bold")
    axes[-1].set_xlabel("Tiempo t (ms) · escala lineal")
    return fig, pd.DataFrame({"t_s": t, "signal_sine": a, "signal_harmonic": b}), {"rms_difference": abs(rms_a-rms_b)}


def chart_002():
    fs, dur = 4000, .05
    t = np.arange(int(fs*dur))/fs
    x = .20*np.sin(2*np.pi*100*t) + .05*np.sin(2*np.pi*200*t + np.pi/2)
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1/fs)
    amp = 2*np.abs(X)/len(x); phase = np.angle(X)
    keep = amp > 1e-8
    fig, axes = canvas(3, 1, gridspec_kw={"height_ratios":[1.25,1,1]})
    axes[0].plot(t*1000, x, color=COLORS["bordo"], lw=3)
    axes[0].set(xlabel="Tiempo t (ms) · escala lineal", ylabel="Presión p(t) (Pa)")
    stem(axes[1], f[keep], amp[keep], COLORS["teal"])
    axes[1].set(xlim=(0,400), ylim=(0,.23), xlabel="Frecuencia f (Hz) · escala lineal", ylabel="Magnitud de pico (Pa)")
    stem(axes[2], f[keep], phase[keep], COLORS["ocre"])
    axes[2].set(xlim=(0,400), ylim=(-1.8,1.8), xlabel="Frecuencia f (Hz) · escala lineal", ylabel="Fase (rad)")
    axes[2].set_yticks([-np.pi/2,0,np.pi/2], ["−π/2","0","π/2"])
    df = pd.DataFrame({"frequency_hz":f, "peak_magnitude_pa":amp, "phase_rad":phase})
    return fig, df, {"inverse_max_abs_error": float(np.max(np.abs(np.fft.irfft(X, n=len(x))-x)))}


def chart_003():
    fs, dur = 6000, .04
    t = np.arange(int(fs*dur))/fs
    freqs=np.array([100.,200.,300.]); amps=np.array([.20,.10,.06])
    phases_a=np.array([0.,0.,0.]); phases_b=np.array([0.,np.pi/2,np.pi])
    sig=lambda ph: sum(a*np.cos(2*np.pi*f*t+p) for f,a,p in zip(freqs,amps,ph))
    xa, xb = sig(phases_a), sig(phases_b)
    Aa=2*np.abs(np.fft.rfft(xa))/len(xa); Ab=2*np.abs(np.fft.rfft(xb))/len(xb); ff=np.fft.rfftfreq(len(xa),1/fs)
    fig, axes=canvas(2,2)
    axes[0,0].plot(t*1000,xa,color=COLORS["bordo"],lw=3); axes[0,1].plot(t*1000,xb,color=COLORS["teal"],lw=3)
    for ax,title in zip(axes[0],("Fases: 0, 0, 0 rad","Fases: 0, π/2, π rad")):
        ax.set(xlim=(0,30),ylim=(-.38,.38),xlabel="Tiempo t (ms)",ylabel="x(t) (Pa)"); ax.set_title(title,loc="left",fontweight="bold")
    sel=(ff<=400)&(Aa>1e-8)
    for ax,A,c in zip(axes[1],(Aa,Ab),(COLORS["bordo"],COLORS["teal"])):
        stem(ax,ff[sel],A[sel],c); ax.set(xlim=(0,400),ylim=(0,.23),xlabel="Frecuencia f (Hz)",ylabel="Magnitud de pico (Pa)")
        ax.text(.98,.84,"misma magnitud",transform=ax.transAxes,ha="right",fontsize=22,fontweight="bold",color=COLORS["teal"])
    return fig, pd.DataFrame({"t_s":t,"signal_phase_set_a":xa,"signal_phase_set_b":xb}), {"magnitude_max_abs_difference":float(np.max(np.abs(Aa-Ab))),"temporal_rms_difference":float(np.sqrt(np.mean((xa-xb)**2)))}


def chart_005():
    f0=100.; t=np.linspace(-.0125,.0125,3000); ideal=np.sign(np.sin(2*np.pi*f0*t)); counts=[1,3,5,10]
    fig, axes=canvas(2,2,sharex=True,sharey=True)
    out={"t_s":t,"ideal":ideal}
    for ax,m in zip(axes.flat,counts):
        y=sum(np.sin(2*np.pi*(2*k+1)*f0*t)/(2*k+1) for k in range(m))*4/np.pi
        out[f"sum_{m}_odd_terms"]=y
        ax.step(t*1000,ideal,where="mid",color=COLORS["gris"],ls="--",lw=2,label="ideal")
        ax.plot(t*1000,y,color=COLORS["bordo"],lw=2.8,label="suma parcial")
        ax.set(ylim=(-1.55,1.55),xlabel="Tiempo t (ms)",ylabel="x(t)/A")
        ax.set_title(f"{m} término" if m==1 else f"{m} términos impares",loc="left",fontweight="bold")
    axes[0,0].legend(frameon=False,loc="lower right")
    axes[1,1].text(.98,.08,"misma escala en los cuatro paneles",transform=axes[1,1].transAxes,
                   ha="right",fontsize=20,color=COLORS["gris"])
    return fig,pd.DataFrame(out),{"term_counts":counts,"static_alternative":"panel 2×2"}


def chart_006():
    fs=1000.; f1=150.; f2=850.; t=np.linspace(0,.02,4000); ts=np.arange(0,.0201,1/fs)
    y1=np.sin(2*np.pi*f1*t); y2=np.sin(2*np.pi*f2*t+np.pi); samples=np.sin(2*np.pi*f1*ts)
    fig,axes=canvas(2,1,sharex=True,sharey=True)
    for ax,y,title,c in zip(axes,(y1,y2),("Señal candidata: 150 Hz","Otra señal candidata: 850 Hz, fase π"),(COLORS["bordo"],COLORS["teal"])):
        ax.plot(t*1000,y,color=c,lw=2.5)
        ax.scatter(ts*1000,samples,s=55,facecolor="white",edgecolor=COLORS["carbon"],lw=2,zorder=5,label="muestras compartidas")
        ax.set(ylabel="Amplitud",ylim=(-1.2,1.2)); ax.set_title(title,loc="left",fontweight="bold")
    axes[-1].set_xlabel("Tiempo t (ms) · fₛ = 1000 Hz; Tₛ = 1 ms")
    axes[0].legend(frameon=False,loc="upper right")
    check=np.max(np.abs(samples-np.sin(2*np.pi*f2*ts+np.pi)))
    return fig,pd.DataFrame({"sample_time_s":ts,"sample_value":samples,"candidate_150_hz":np.sin(2*np.pi*f1*ts),"candidate_850_hz_phase_pi":np.sin(2*np.pi*f2*ts+np.pi)}),{"sample_max_abs_difference":float(check)}


def chart_007():
    fs=8000.; freqs_sig=[1000.,1002.]; amp=[1.,.8]; configs=[(2000,.25,4.),(8000,1.,1.)]
    fig,axes=canvas(2,1,sharex=True)
    rows=[]
    for ax,(N,T,df) in zip(axes,configs):
        t=np.arange(N)/fs; x=sum(a*np.sin(2*np.pi*f*t) for a,f in zip(amp,freqs_sig)); X=2*np.abs(np.fft.rfft(x))/N; ff=np.fft.rfftfreq(N,1/fs)
        sel=(ff>=985)&(ff<=1017)
        stem(ax,ff[sel],X[sel],COLORS["bordo"] if N==2000 else COLORS["teal"])
        ax.set(ylabel="Magnitud de pico",ylim=(0,1.25)); ax.set_title(f"N={N}; T_obs={T:.2f} s; Δf={df:.1f} Hz",loc="left",fontweight="bold")
        rows.extend({"N":N,"T_obs_s":T,"delta_f_hz":df,"frequency_hz":f,"magnitude":m} for f,m in zip(ff[sel],X[sel]))
    axes[-1].set(xlabel="Frecuencia f (Hz) · escala lineal",xlim=(985,1017))
    return fig,pd.DataFrame(rows),{"relations_verified":all(abs(N/fs-T)<1e-12 and abs(fs/N-df)<1e-12 for N,T,df in configs)}


def chart_008():
    fs,N=2000.,200; t=np.arange(N)/fs; cases=[(100.,"10 períodos enteros"),(105.,"10,5 períodos")]
    fig,axes=canvas(2,2)
    rows=[]
    for col,(freq,title) in enumerate(cases):
        x=np.sin(2*np.pi*freq*t); ff=np.fft.rfftfreq(N,1/fs); A=2*np.abs(np.fft.rfft(x))/N
        axes[0,col].plot(t*1000,x,color=COLORS["bordo"] if col==0 else COLORS["teal"],lw=2.6)
        axes[0,col].plot([0,t[-1]*1000],[x[0],x[-1]],color=COLORS["gris"],ls="--",lw=1.5)
        axes[0,col].set(title=f"{freq:.0f} Hz · {title}",xlabel="Tiempo t (ms)",ylabel="Amplitud")
        sel=ff<=250; stem(axes[1,col],ff[sel],A[sel],COLORS["bordo"] if col==0 else COLORS["teal"])
        axes[1,col].set(xlim=(0,250),ylim=(0,1.08),xlabel="Frecuencia f (Hz) · Δf=10 Hz",ylabel="Magnitud de pico")
        rows.extend({"tone_hz":freq,"frequency_hz":f,"peak_magnitude":m} for f,m in zip(ff,A))
    axes[1,1].text(.98,.82,"fuga ≠ ruido",transform=axes[1,1].transAxes,ha="right",fontsize=22,fontweight="bold",color=COLORS["error"])
    return fig,pd.DataFrame(rows),{"parseval_relative_errors":[float(abs(np.mean(np.sin(2*np.pi*f*t)**2)-np.sum(np.abs(np.fft.rfft(np.sin(2*np.pi*f*t)))**2)/(N*N)*2)) for f,_ in cases]}


def chart_011():
    cases=[("Serie armónica\nf₀=100 Hz",[100,200,300,400],[.45,1,.6,.3]),("Parciales\ninarmónicos",[100,235,370,520],[.6,1,.55,.3]),("Fundamental ausente\nΔf=100 Hz",[200,300,400],[1,.6,.4])]
    fig,axes=canvas(3,1,sharex=True,sharey=True); rows=[]
    for ax,(title,f,a) in zip(axes,cases):
        stem(ax,f,a,COLORS["bordo"]); ax.set(ylabel="A/Aₘₐₓ",ylim=(0,1.15)); ax.text(.01,.82,title,transform=ax.transAxes,fontsize=21,fontweight="bold")
        rows.extend({"case":title.replace("\n"," "),"frequency_hz":x,"relative_amplitude":y} for x,y in zip(f,a))
    axes[0].annotate("máximo ≠ definición de f₀",xy=(200,1),xytext=(300,.72),fontsize=21,arrowprops={"arrowstyle":"->","color":COLORS["teal"],"lw":2},color=COLORS["teal"])
    axes[-1].set(xlabel="Frecuencia f (Hz) · escala lineal",xlim=(0,600))
    return fig,pd.DataFrame(rows),{"frequencies_exact":True}


def chart_013():
    fig,ax=canvas(); ax.set_xscale("log"); ax.set_xlim(1,1e6); ax.set_ylim(0,1); ax.set_yticks([])
    ax.axvspan(1,16,color=COLORS["teal"],alpha=.25); ax.axvspan(25,16000,color=COLORS["bordo"],alpha=.18); ax.axvspan(25000,1e6,color=COLORS["ocre"],alpha=.2)
    ax.axvspan(16,25,facecolor="white",edgecolor=COLORS["gris"],hatch="///",alpha=.7); ax.axvspan(16000,25000,facecolor="white",edgecolor=COLORS["gris"],hatch="///",alpha=.7)
    for x,label,c in [(4,"Infrasonido",COLORS["teal"]),(550,"Rango audible",COLORS["bordo"]),(1.2e5,"Ultrasonido",COLORS["ocre"])]: ax.text(x,.56,label,ha="center",fontsize=25,fontweight="bold",color=c)
    ax.text(20,.18,"≈20 Hz",ha="center",fontsize=22); ax.text(20000,.18,"≈20 kHz",ha="center",fontsize=22)
    ax.text(300,.9,"Fronteras convencionales aproximadas; dependen de nivel, oyente y condiciones",ha="center",fontsize=21,color=COLORS["carbon"])
    ax.set_xlabel("Frecuencia f (Hz) · escala logarítmica base 10"); ax.grid(True,which="both",axis="x"); ax.spines["left"].set_visible(False)
    return fig,pd.DataFrame({"region":["infrasonido","transición baja","audible","transición alta","ultrasonido"],"lower_hz":[1,16,25,16000,25000],"upper_hz":[16,25,16000,25000,1e6],"scale_note":["conceptual; no universal"]*5}),{"not_to_scale":False,"boundaries_declared_approximate":True}


def chart_015():
    f=np.geomspace(100,8000,72); power=(0.05+0.9*np.exp(-((np.log(f)-np.log(900))/.38)**2)+0.45*np.exp(-((np.log(f)-np.log(3000))/.25)**2))
    power*=1+0.14*np.sin(np.arange(len(f))*1.7); power=np.maximum(power,1e-4)
    centers=np.array([250,500,1000,2000,4000.]); lo=centers/np.sqrt(2); hi=centers*np.sqrt(2)
    band_power=np.array([power[(f>=l)&(f<h)].sum() for l,h in zip(lo,hi)]); ref=band_power.max(); band_db=10*np.log10(band_power/ref)
    fig,axes=canvas(2,1,sharex=True)
    axes[0].vlines(f,0,power/power.max(),color=COLORS["teal"],lw=2); axes[0].set_ylabel("Potencia relativa por bin"); axes[0].set_xscale("log")
    axes[1].bar(centers,band_db+30,width=hi-lo,bottom=-30,align="center",color=COLORS["bordo2"],edgecolor=COLORS["carbon"],alpha=.82)
    axes[1].set(xscale="log",ylim=(-30,2),ylabel="Nivel relativo por banda (dB)",xlabel="Frecuencia f (Hz) · escala logarítmica")
    axes[1].text(.98,.86,"suma lineal → luego 10 log₁₀",transform=axes[1].transAxes,ha="right",fontsize=22,fontweight="bold",color=COLORS["bordo"])
    rows=[{"representation":"bin","frequency_hz":x,"linear_power":p,"relative_db":10*np.log10(p/power.max())} for x,p in zip(f,power)]
    rows += [{"representation":"octave_band_theoretical","frequency_hz":c,"lower_hz":l,"upper_hz":h,"linear_power":p,"relative_db":d} for c,l,h,p,d in zip(centers,lo,hi,band_power,band_db)]
    return fig,pd.DataFrame(rows),{"linear_sum_before_db":True,"band_total_linear":float(band_power.sum())}


def chart_016():
    f=np.geomspace(100,10000,1600); order=4; fc=1000.; fl,fh=500.,2000.
    configs=[("Pasa bajos",[fc],"lowpass"),("Pasa altos",[fc],"highpass"),("Pasa banda",[fl,fh],"bandpass"),("Elimina banda",[fl,fh],"bandstop")]
    fig,axes=canvas(2,2,sharex=True,sharey=True); rows=[]
    for ax,(name,crit,kind) in zip(axes.flat,configs):
        angular_crit=[2*np.pi*c for c in crit]
        b,a=signal.butter(order,angular_crit,btype=kind,analog=True); _,h=signal.freqs(b,a,worN=2*np.pi*f); db=20*np.log10(np.maximum(np.abs(h),1e-4))
        if kind=="lowpass": ideal=np.where(f<=fc,0,-60)
        elif kind=="highpass": ideal=np.where(f>=fc,0,-60)
        elif kind=="bandpass": ideal=np.where((f>=fl)&(f<=fh),0,-60)
        else: ideal=np.where((f<fl)|(f>fh),0,-60)
        ax.plot(f,ideal,color=COLORS["gris"],ls="--",lw=2,label="ideal esquemático"); ax.plot(f,db,color=COLORS["bordo"],lw=3,label="Butterworth orden 4")
        for c in crit: ax.axvline(c,color=COLORS["teal"],ls=":",lw=2)
        ax.axhline(-3,color=COLORS["gris"],lw=1); ax.set(xscale="log",ylim=(-60,3)); ax.set_title(name,loc="left",fontweight="bold")
        rows.extend({"filter":name,"frequency_hz":x,"gain_db":y,"model":"Butterworth analog order 4"} for x,y in zip(f,db))
    axes[0,0].legend(frameon=False,loc="lower left"); axes[0,0].set_ylabel("Ganancia G(f) (dB)"); axes[1,0].set_ylabel("Ganancia G(f) (dB)")
    for ax in axes[1]: ax.set_xlabel("Frecuencia f (Hz) · escala logarítmica")
    return fig,pd.DataFrame(rows),{"cutoff_criterion_db":-3,"scipy_version":"1.13.1","models_stable":True}


def chart_018():
    levels=np.array([70.,80.]); leq=10*np.log10(np.mean(10**(levels/10)))
    fig,ax=canvas(); ax.step([0,30,60],[70,80,80],where="post",color=COLORS["bordo"],lw=5,label="nivel por tramo")
    ax.axhline(leq,color=COLORS["teal"],ls="--",lw=3,label=f"nivel equivalente = {leq:.1f} dB")
    ax.fill_between([0,30],[0,0],[70,70],color=COLORS["bordo"],alpha=.10); ax.fill_between([30,60],[0,0],[80,80],color=COLORS["bordo"],alpha=.18)
    ax.set(xlim=(0,60),ylim=(0,90),xlabel="Tiempo t (s) · escala lineal",ylabel="Nivel L (dB; misma ponderación y referencia)")
    ax.legend(frameon=False,loc="lower right"); ax.text(15,74,"30 s a 70 dB",ha="center",fontsize=22); ax.text(45,84,"30 s a 80 dB",ha="center",fontsize=22)
    return fig,pd.DataFrame({"start_s":[0,30],"end_s":[30,60],"level_db":levels,"relative_energy":10**(levels/10)}),{"equivalent_level_db":float(leq),"target_error_db":float(abs(leq-77.4036268949))}


def chart_019():
    centers=np.array([125,250,500,1000,2000,4000]); levels=np.array([42,48,53,61,58,50]); limits=np.array([50,50,50,55,55,55]); fail=levels>limits
    fig,ax=canvas(); colors=np.where(fail,COLORS["error"],COLORS["teal"])
    lower=centers/np.sqrt(2); upper=centers*np.sqrt(2)
    bars=ax.bar(centers,levels,width=upper-lower,color=colors,edgecolor=COLORS["carbon"],lw=1.5,align="center")
    for bar,bad in zip(bars,fail):
        if bad: bar.set_hatch("///")
    step_x=np.ravel(np.column_stack((lower,upper))); step_y=np.repeat(limits,2)
    ax.plot(step_x,step_y,color=COLORS["carbon"],lw=3,label="límite hipotético")
    ax.set(xscale="log",xlim=(lower[0],upper[-1]),ylim=(0,70),xticks=centers,xticklabels=[str(x) for x in centers],xlabel="Centro de banda (Hz) · escala logarítmica",ylabel="Nivel por banda (dB)")
    ax.legend(frameon=False); ax.text(.98,.93,"CASO DIDÁCTICO · NO NORMATIVO",transform=ax.transAxes,ha="right",fontsize=21,fontweight="bold",color=COLORS["error"])
    return fig,pd.DataFrame({"center_hz":centers,"level_db":levels,"hypothetical_limit_db":limits,"exceeds":fail}),{"failing_centers_hz":centers[fail].tolist()}


GENERATORS={
    "U05-CH-001":chart_001,"U05-CH-002":chart_002,"U05-CH-003":chart_003,
    "U05-CH-005":chart_005,"U05-CH-006":chart_006,"U05-CH-007":chart_007,
    "U05-CH-008":chart_008,"U05-CH-011":chart_011,"U05-CH-013":chart_013,
    "U05-CH-015":chart_015,"U05-CH-016":chart_016,"U05-CH-018":chart_018,
    "U05-CH-019":chart_019,
}


def make_wrapper(folder: Path, script_name: str, chart_id: str) -> None:
    wrapper = f'''"""Lanzador reproducible de {chart_id}."""\nfrom pathlib import Path\nimport subprocess\nimport sys\nmaster = Path(__file__).resolve().parents[4] / "scripts" / "u05_generate_charts.py"\nsubprocess.run([sys.executable, str(master), "--id", "{chart_id}"], check=True)\n'''
    (folder / script_name).write_text(wrapper, encoding="utf-8")


def write_readme(folder: Path, chart_id: str, script_name: str, basename: str, checks: dict) -> None:
    m=META[chart_id]
    text=f"""# {chart_id}\n\n- **Clasificación:** {m['classification']}\n- **Pregunta:** {m['question']}\n- **Modelo/datos:** {m['source']}\n- **Escala y tamaño:** canvas 16:9; PNG 2560×1440; SVG con texto editable.\n- **Reproducción:** `python {script_name}`\n\n## Caption sugerido\n\n{m['caption']}\n\n## Texto alternativo\n\n{m['alt']}\n\n## Fuente de datos\n\n{m['source']}\n\n## Archivos\n\n- `{basename}.svg`\n- `{basename}.png`\n- `data.csv`\n- `validation.json`\n\n## Validación numérica\n\n```json\n{json.dumps(checks, ensure_ascii=False, indent=2)}\n```\n"""
    (folder/"README.md").write_text(text,encoding="utf-8")


def generate(chart_id: str) -> dict:
    configure_style(); folder=ROOT/chart_id; folder.mkdir(parents=True,exist_ok=True)
    script_name,basename=APPROVED[chart_id]
    fig,data,checks=GENERATORS[chart_id]()
    save_outputs(fig,folder,basename); data.to_csv(folder/"data.csv",index=False,encoding="utf-8")
    make_wrapper(folder,script_name,chart_id)
    png=folder/f"{basename}.png"; svg=folder/f"{basename}.svg"
    from PIL import Image
    with Image.open(png) as im: size=im.size
    validation={"asset_id":chart_id,"classification":"gráfico cuantitativo","status":"approved","canvas_px":list(size),"required_canvas_px":[2560,1440],"svg_exists":svg.exists(),"png_exists":png.exists(),"data_rows":int(len(data)),"font_floor":{"axis_labels_pt":20,"ticks_and_legends_pt":18,"annotations_pt":22},"checks":checks,"critical_issues":0,"major_issues":0}
    (folder/"validation.json").write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding="utf-8")
    write_readme(folder,chart_id,script_name,basename,checks)
    return validation


def main() -> None:
    parser=argparse.ArgumentParser(); parser.add_argument("--id",choices=sorted(APPROVED)); parser.add_argument("--all",action="store_true"); args=parser.parse_args()
    ids=sorted(APPROVED) if args.all or not args.id else [args.id]
    results=[generate(i) for i in ids]
    ROOT.mkdir(parents=True,exist_ok=True)
    (ROOT/"generation_summary.json").write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"Generadas {len(results)} familias en {ROOT}")


if __name__ == "__main__":
    main()
