"""Genera las figuras calculadas de la Unidad 5.

Todas las señales y respuestas son modelos matemáticos deterministas. No se
emplean datos medidos ni valores experimentales. Las salidas se guardan como
PDF vectorial en ``figures/generated/unidad-5``.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


FIGURES_DIR = Path(__file__).resolve().parents[2]
OUTPUT_DIR = FIGURES_DIR / "generated" / "unidad-5"

BLUE = "#1f4e79"
ORANGE = "#b45f06"
GREEN = "#38761d"
GRAY = "#555555"
LIGHT_GRAY = "#b7b7b7"


def configure_style() -> None:
    """Configura una tipografía legible al ancho de texto del libro."""

    mpl.rcParams.update(
        {
            "font.family": "DejaVu Serif",
            "font.size": 8.5,
            "axes.labelsize": 8.5,
            "axes.titlesize": 8.5,
            "legend.fontsize": 7.5,
            "xtick.labelsize": 7.5,
            "ytick.labelsize": 7.5,
            "lines.linewidth": 1.35,
            "axes.linewidth": 0.7,
            "xtick.major.width": 0.7,
            "ytick.major.width": 0.7,
            "pdf.fonttype": 42,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.03,
        }
    )


def panel_label(axis: plt.Axes, label: str) -> None:
    axis.text(
        0.01,
        0.96,
        label,
        transform=axis.transAxes,
        ha="left",
        va="top",
        fontweight="bold",
    )


def save_figure(figure: plt.Figure, filename: str) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT_DIR / filename, format="pdf")
    plt.close(figure)


def time_magnitude_phase() -> None:
    """Relaciona una presión temporal con magnitud y fase de su DFT.

    Descripción accesible: tres paneles representan la misma señal. El primero
    muestra una presión periódica en el tiempo; el segundo, líneas de amplitud
    0,20 Pa y 0,050 Pa en 100 Hz y 200 Hz; el tercero muestra fases de -pi/2 y
    0 rad en esas frecuencias.
    """

    sampling_frequency_hz = 4000.0
    duration_s = 0.050
    sample_count = int(sampling_frequency_hz * duration_s)
    time_s = np.arange(sample_count) / sampling_frequency_hz
    pressure_pa = (
        0.20 * np.sin(2 * np.pi * 100.0 * time_s)
        + 0.050 * np.sin(2 * np.pi * 200.0 * time_s + np.pi / 2)
    )

    spectrum = np.fft.rfft(pressure_pa)
    frequency_hz = np.fft.rfftfreq(sample_count, d=1 / sampling_frequency_hz)
    peak_amplitude_pa = 2 * np.abs(spectrum) / sample_count
    phase_rad = np.angle(spectrum)
    visible = peak_amplitude_pa > 1e-8
    selected = visible & (frequency_hz <= 400)

    figure, axes = plt.subplots(
        3,
        1,
        figsize=(4.75, 5.25),
        gridspec_kw={"height_ratios": [1.25, 1, 1]},
        constrained_layout=True,
    )

    axes[0].plot(time_s * 1000, pressure_pa, color=BLUE)
    axes[0].axhline(0, color=LIGHT_GRAY, linewidth=0.7)
    axes[0].set_xlim(0, duration_s * 1000)
    axes[0].set_ylabel(r"$p(t)$ (Pa)")
    axes[0].set_xlabel(r"Tiempo $t$ (ms)")
    panel_label(axes[0], "(a)")

    markerline, stemlines, baseline = axes[1].stem(
        frequency_hz[selected],
        peak_amplitude_pa[selected],
        basefmt=" ",
    )
    plt.setp(markerline, color=ORANGE, markersize=4)
    plt.setp(stemlines, color=ORANGE, linewidth=1.4)
    axes[1].set_xlim(0, 400)
    axes[1].set_ylim(0, 0.23)
    axes[1].set_ylabel("Amplitud de pico (Pa)")
    axes[1].set_xlabel(r"Frecuencia $f$ (Hz)")
    panel_label(axes[1], "(b)")

    markerline, stemlines, baseline = axes[2].stem(
        frequency_hz[selected],
        phase_rad[selected],
        basefmt=" ",
    )
    plt.setp(markerline, color=GREEN, markersize=4)
    plt.setp(stemlines, color=GREEN, linewidth=1.4)
    axes[2].axhline(0, color=LIGHT_GRAY, linewidth=0.7)
    axes[2].set_xlim(0, 400)
    axes[2].set_ylim(-1.8, 1.8)
    axes[2].set_yticks([-np.pi / 2, 0, np.pi / 2])
    axes[2].set_yticklabels([r"$-\pi/2$", "0", r"$\pi/2$"])
    axes[2].set_ylabel("Fase (rad)")
    axes[2].set_xlabel(r"Frecuencia $f$ (Hz)")
    panel_label(axes[2], "(c)")

    for axis in axes:
        axis.grid(True, color="#dddddd", linewidth=0.5)

    save_figure(figure, "tiempo-magnitud-fase.pdf")


def progressive_fourier_series() -> None:
    """Muestra la aproximación de una onda rectangular con términos impares.

    Descripción accesible: tres paneles comparan la onda rectangular ideal con
    sumas de uno, tres y diez términos impares. La forma se aproxima a los
    tramos constantes al agregar términos, mientras persisten oscilaciones
    alrededor de cada discontinuidad.
    """

    fundamental_hz = 100.0
    time_s = np.linspace(-0.0125, 0.0125, 3000)
    ideal = np.sign(np.sin(2 * np.pi * fundamental_hz * time_s))
    term_counts = (1, 3, 10)

    figure, axes = plt.subplots(
        3,
        1,
        figsize=(4.75, 5.35),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    for axis, term_count, label in zip(axes, term_counts, ("(a)", "(b)", "(c)")):
        approximation = np.zeros_like(time_s)
        for index in range(term_count):
            harmonic = 2 * index + 1
            approximation += np.sin(
                2 * np.pi * harmonic * fundamental_hz * time_s
            ) / harmonic
        approximation *= 4 / np.pi

        axis.step(
            time_s * 1000,
            ideal,
            where="mid",
            color=LIGHT_GRAY,
            linestyle="--",
            linewidth=1.0,
            label="onda rectangular ideal",
        )
        axis.plot(
            time_s * 1000,
            approximation,
            color=BLUE,
            label="suma parcial",
        )
        axis.axhline(0, color="#dddddd", linewidth=0.6)
        axis.set_ylim(-1.55, 1.55)
        axis.set_ylabel(r"$p(t)/A$")
        axis.grid(True, color="#e4e4e4", linewidth=0.45)
        panel_label(axis, label)
        axis.text(
            0.98,
            0.92,
            f"{term_count} término"
            if term_count == 1
            else f"{term_count} términos impares",
            transform=axis.transAxes,
            ha="right",
            va="top",
        )

    axes[0].legend(loc="lower right", frameon=False)
    axes[-1].set_xlabel(r"Tiempo $t$ (ms), con $f_0=100$ Hz")

    save_figure(figure, "serie-fourier-progresiva.pdf")


def short_time_spectrum(
    signal: np.ndarray,
    sampling_frequency_hz: float,
    segment_samples: int,
    hop_samples: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Calcula una STFT de magnitud con ventana Hann y escala relativa."""

    window = np.hanning(segment_samples)
    starts = np.arange(0, signal.size - segment_samples + 1, hop_samples)
    spectra = []
    centers_s = []
    for start in starts:
        frame = signal[start : start + segment_samples] * window
        magnitude = 2 * np.abs(np.fft.rfft(frame)) / np.sum(window)
        spectra.append(magnitude)
        centers_s.append((start + segment_samples / 2) / sampling_frequency_hz)

    magnitude_matrix = np.asarray(spectra).T
    magnitude_matrix /= np.max(magnitude_matrix)
    relative_db = 20 * np.log10(np.maximum(magnitude_matrix, 1e-6))
    frequency_hz = np.fft.rfftfreq(
        segment_samples, d=1 / sampling_frequency_hz
    )
    return np.asarray(centers_s), frequency_hz, relative_db


def time_frequency_tradeoff() -> None:
    """Compara espectrogramas de una señal sintética con dos ventanas.

    Descripción accesible: el espectrograma con ventana de 25 ms localiza con
    nitidez el cambio ocurrido a 0,5 s, pero mezcla componentes separadas
    40 Hz. El de 200 ms separa las líneas, aunque difumina el cambio en el
    tiempo. El color representa magnitud relativa entre -45 dB y 0 dB.
    """

    sampling_frequency_hz = 8000.0
    duration_s = 1.0
    time_s = np.arange(int(sampling_frequency_hz * duration_s))
    time_s = time_s / sampling_frequency_hz

    first_half = time_s < 0.5
    signal = np.zeros_like(time_s)
    signal[first_half] = (
        np.sin(2 * np.pi * 1000.0 * time_s[first_half])
        + 0.8 * np.sin(2 * np.pi * 1040.0 * time_s[first_half])
    )
    signal[~first_half] = (
        np.sin(2 * np.pi * 1200.0 * time_s[~first_half])
        + 0.8 * np.sin(2 * np.pi * 1240.0 * time_s[~first_half])
    )

    settings = (
        (200, 50, "(a)", "Ventana de 25 ms; $\\Delta f=40$ Hz"),
        (1600, 200, "(b)", "Ventana de 200 ms; $\\Delta f=5$ Hz"),
    )
    figure, axes = plt.subplots(
        2,
        1,
        figsize=(4.75, 4.85),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    color_boundaries_db = np.arange(-45, 5, 5)
    color_map = mpl.colormaps["cividis"].resampled(
        len(color_boundaries_db) - 1
    )
    color_norm = mpl.colors.BoundaryNorm(
        color_boundaries_db,
        color_map.N,
    )
    image = None
    for axis, (segment, hop, label, annotation) in zip(axes, settings):
        centers, frequencies, relative_db = short_time_spectrum(
            signal,
            sampling_frequency_hz,
            segment,
            hop,
        )
        band = (frequencies >= 900) & (frequencies <= 1340)
        image = axis.pcolormesh(
            centers,
            frequencies[band],
            relative_db[band],
            shading="nearest",
            cmap=color_map,
            norm=color_norm,
            rasterized=False,
        )
        axis.axvline(0.5, color="white", linestyle="--", linewidth=0.8)
        axis.set_ylabel(r"Frecuencia $f$ (Hz)")
        panel_label(axis, label)
        axis.text(
            0.99,
            0.94,
            annotation,
            transform=axis.transAxes,
            ha="right",
            va="top",
            color="white",
            bbox={"facecolor": "black", "alpha": 0.45, "edgecolor": "none"},
        )

    axes[-1].set_xlabel(r"Tiempo central del segmento $t$ (s)")
    colorbar = figure.colorbar(
        image,
        ax=axes,
        boundaries=color_boundaries_db,
        ticks=[-45, -30, -15, 0],
        pad=0.02,
        aspect=30,
    )
    colorbar.set_label("Magnitud relativa (dB)")

    save_figure(figure, "compromiso-tiempo-frecuencia.pdf")


def filter_responses() -> None:
    """Compara respuestas ideales con modelos analíticos de filtros no ideales.

    Descripción accesible: cuatro paneles muestran pasa bajos, pasa altos, pasa
    banda y elimina banda. En cada uno, una línea discontinua cambia
    abruptamente entre paso y rechazo, mientras una curva continua presenta una
    transición gradual alrededor de las frecuencias límite.
    """

    frequency_hz = np.geomspace(100.0, 10000.0, 1600)
    low_cut_hz = 500.0
    center_hz = 1000.0
    high_cut_hz = 2000.0
    order = 4

    low_pass = 1 / np.sqrt(1 + (frequency_hz / center_hz) ** (2 * order))
    high_pass = 1 / np.sqrt(1 + (center_hz / frequency_hz) ** (2 * order))
    band_pass = (
        1 / np.sqrt(1 + (low_cut_hz / frequency_hz) ** (2 * order))
    ) * (1 / np.sqrt(1 + (frequency_hz / high_cut_hz) ** (2 * order)))

    quality_factor = center_hz / (high_cut_hz - low_cut_hz)
    numerator = np.abs(center_hz**2 - frequency_hz**2)
    denominator = np.sqrt(
        (center_hz**2 - frequency_hz**2) ** 2
        + (center_hz * frequency_hz / quality_factor) ** 2
    )
    band_stop = numerator / denominator

    ideal_low = (frequency_hz <= center_hz).astype(float)
    ideal_high = (frequency_hz >= center_hz).astype(float)
    ideal_band = (
        (frequency_hz >= low_cut_hz) & (frequency_hz <= high_cut_hz)
    ).astype(float)
    ideal_stop = 1 - ideal_band

    panels = (
        (low_pass, ideal_low, "(a)", "Pasa bajos", (center_hz,)),
        (high_pass, ideal_high, "(b)", "Pasa altos", (center_hz,)),
        (
            band_pass,
            ideal_band,
            "(c)",
            "Pasa banda",
            (low_cut_hz, high_cut_hz),
        ),
        (
            band_stop,
            ideal_stop,
            "(d)",
            "Elimina banda",
            (low_cut_hz, high_cut_hz),
        ),
    )

    figure, axes = plt.subplots(
        2,
        2,
        figsize=(4.75, 4.25),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    for axis, (real, ideal, label, name, limits) in zip(axes.flat, panels):
        axis.plot(frequency_hz, ideal, color=LIGHT_GRAY, linestyle="--")
        axis.plot(frequency_hz, real, color=BLUE)
        for limit in limits:
            axis.axvline(limit, color=GRAY, linestyle=":", linewidth=0.8)
        axis.set_xscale("log")
        axis.set_xlim(100, 10000)
        axis.set_ylim(-0.04, 1.08)
        axis.set_yticks([0, 0.5, 1])
        axis.grid(True, which="major", color="#dddddd", linewidth=0.5)
        panel_label(axis, label)
        axis.text(
            0.98,
            0.94,
            name,
            transform=axis.transAxes,
            ha="right",
            va="top",
        )

    axes[0, 0].set_ylabel(r"Magnitud $|H(f)|$")
    axes[1, 0].set_ylabel(r"Magnitud $|H(f)|$")
    axes[1, 0].set_xlabel(r"Frecuencia $f$ (Hz)")
    axes[1, 1].set_xlabel(r"Frecuencia $f$ (Hz)")
    axes[0, 0].legend(
        ["ideal", "modelo no ideal"],
        loc="center left",
        frameon=False,
    )

    save_figure(figure, "filtros-ideales-reales.pdf")


def main() -> None:
    configure_style()
    time_magnitude_phase()
    progressive_fourier_series()
    time_frequency_tradeoff()
    filter_responses()
    print(f"Figuras generadas en: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
