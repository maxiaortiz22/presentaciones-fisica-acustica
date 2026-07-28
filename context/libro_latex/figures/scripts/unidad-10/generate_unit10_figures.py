"""Genera las figuras calculadas de la Unidad 10.

Las señales son realizaciones sintéticas o modelos analíticos. No se emplean
datos medidos, valores normativos ni resultados clínicos. Las semillas y los
parámetros se fijan para obtener salidas reproducibles. Los PDF vectoriales se
guardan en ``figures/generated/unidad-10``.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


FIGURES_DIR = Path(__file__).resolve().parents[2]
OUTPUT_DIR = FIGURES_DIR / "generated" / "unidad-10"

BLUE = "#1f4e79"
ORANGE = "#b45f06"
GREEN = "#38761d"
GRAY = "#555555"
LIGHT_GRAY = "#b7b7b7"
GRID_GRAY = "#dddddd"


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
            "lines.linewidth": 1.2,
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
        0.95,
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


def temporal_realizations() -> None:
    """Compara realizaciones sintéticas con cuatro evoluciones temporales.

    Descripción accesible: cuatro paneles comparten los mismos ejes. El ruido
    continuo estable mantiene una dispersión semejante; el fluctuante aumenta
    y disminuye gradualmente; el intermitente alterna actividad y pausas; el
    impulsivo contiene tres picos breves sobre un fondo de menor amplitud.
    """

    sampling_frequency_hz = 1000.0
    duration_s = 1.0
    time_s = np.arange(int(sampling_frequency_hz * duration_s))
    time_s = time_s / sampling_frequency_hz
    rng = np.random.default_rng(1010)

    stable_mpa = 0.55 * rng.standard_normal(time_s.size)

    fluctuation_envelope = 0.18 + 0.82 * (
        0.5 + 0.5 * np.sin(2 * np.pi * 1.25 * time_s - np.pi / 2)
    )
    fluctuating_mpa = (
        0.78 * fluctuation_envelope * rng.standard_normal(time_s.size)
    )

    intermittent_gate = np.zeros_like(time_s)
    for start_s, end_s in ((0.05, 0.25), (0.39, 0.60), (0.75, 0.94)):
        intermittent_gate[(time_s >= start_s) & (time_s < end_s)] = 1.0
    intermittent_mpa = (
        0.62 * intermittent_gate * rng.standard_normal(time_s.size)
    )

    impulsive_mpa = 0.08 * rng.standard_normal(time_s.size)
    for center_s, amplitude_mpa in ((0.18, 3.0), (0.49, 2.7), (0.80, 3.2)):
        impulsive_mpa += amplitude_mpa * np.exp(
            -0.5 * ((time_s - center_s) / 0.004) ** 2
        )

    panels = (
        (stable_mpa, "(a)", "Continuo aproximadamente estable"),
        (fluctuating_mpa, "(b)", "Continuo fluctuante"),
        (intermittent_mpa, "(c)", "Intermitente"),
        (impulsive_mpa, "(d)", "Impulsivo"),
    )

    figure, axes = plt.subplots(
        4,
        1,
        figsize=(4.75, 5.25),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    for axis, (pressure_mpa, label, name) in zip(axes, panels):
        axis.plot(time_s, pressure_mpa, color=BLUE, linewidth=0.8)
        axis.axhline(0, color=LIGHT_GRAY, linewidth=0.6)
        axis.set_ylim(-3.6, 3.6)
        axis.set_ylabel(r"$p(t)$ (mPa)")
        axis.grid(True, color=GRID_GRAY, linewidth=0.45)
        panel_label(axis, label)
        axis.text(
            0.99,
            0.94,
            name,
            transform=axis.transAxes,
            ha="right",
            va="top",
        )

    axes[-1].set_xlabel(r"Tiempo $t$ (s)")
    axes[-1].set_xlim(0, duration_s)

    save_figure(figure, "realizaciones-temporales-ruido.pdf")


def _zero_mean_unit_rms(values: np.ndarray) -> np.ndarray:
    centered = values - np.mean(values)
    return centered / np.sqrt(np.mean(centered**2))


def statistics_same_rms() -> None:
    """Muestra dos señales con media, RMS y varianza iguales pero otra distribución.

    Descripción accesible: las señales A y B tienen media cero, RMS de 1 mPa y
    varianza de 1 mPa cuadrado. A adopta muchos valores alrededor de cero; B
    solo adopta -1 mPa y +1 mPa. Sus fragmentos temporales e histogramas son
    diferentes a pesar de compartir los tres descriptores.
    """

    sample_count = 5000
    sampling_frequency_hz = 1000.0
    rng = np.random.default_rng(1020)

    gaussian_mpa = _zero_mean_unit_rms(rng.standard_normal(sample_count))
    two_level_mpa = np.concatenate(
        (
            -np.ones(sample_count // 2),
            np.ones(sample_count - sample_count // 2),
        )
    )
    rng.shuffle(two_level_mpa)

    for values in (gaussian_mpa, two_level_mpa):
        assert abs(np.mean(values)) < 1e-12
        assert abs(np.sqrt(np.mean(values**2)) - 1.0) < 1e-12
        assert abs(np.mean((values - np.mean(values)) ** 2) - 1.0) < 1e-12

    excerpt_count = 200
    time_ms = (
        np.arange(excerpt_count) / sampling_frequency_hz * 1000
    )
    bin_edges_mpa = np.linspace(-4.0, 4.0, 33)

    figure, axes = plt.subplots(
        2,
        2,
        figsize=(4.75, 4.35),
        constrained_layout=True,
    )

    signals = (
        (gaussian_mpa, "(a)", "Señal A: valores continuos"),
        (two_level_mpa, "(b)", "Señal B: dos valores"),
    )

    for column, (values, label, name) in enumerate(signals):
        time_axis = axes[0, column]
        histogram_axis = axes[1, column]

        time_axis.plot(
            time_ms,
            values[:excerpt_count],
            color=BLUE if column == 0 else ORANGE,
            linewidth=0.8,
        )
        time_axis.axhline(0, color=LIGHT_GRAY, linewidth=0.6)
        time_axis.set_xlim(0, time_ms[-1])
        time_axis.set_ylim(-4.0, 4.0)
        time_axis.set_xlabel(r"Tiempo $t$ (ms)")
        time_axis.set_ylabel(r"$p(t)$ (mPa)")
        time_axis.grid(True, color=GRID_GRAY, linewidth=0.45)
        panel_label(time_axis, label)
        time_axis.text(
            0.99,
            0.94,
            name,
            transform=time_axis.transAxes,
            ha="right",
            va="top",
            fontsize=7.5,
        )

        histogram_axis.hist(
            values,
            bins=bin_edges_mpa,
            weights=np.ones(values.size) / values.size,
            color=BLUE if column == 0 else ORANGE,
            edgecolor="black",
            linewidth=0.35,
        )
        histogram_axis.set_xlim(-4.0, 4.0)
        histogram_axis.set_ylim(0, 0.55)
        histogram_axis.set_xlabel(r"Intervalo de presión $p$ (mPa)")
        histogram_axis.set_ylabel("Frecuencia relativa")
        histogram_axis.grid(
            True,
            axis="y",
            color=GRID_GRAY,
            linewidth=0.45,
        )
        histogram_axis.text(
            0.02,
            0.94,
            r"$\overline{p}=0$ mPa"
            "\n"
            r"$p_{\mathrm{rms}}=1$ mPa"
            "\n"
            r"$\sigma_p^2=1$ mPa$^2$",
            transform=histogram_axis.transAxes,
            ha="left",
            va="top",
            fontsize=7.5,
        )

    save_figure(figure, "estadistica-mismo-rms.pdf")


def white_pink_band_energy() -> None:
    """Compara densidades blanco/rosa y sus integrales por octava.

    Descripción accesible: el panel superior muestra densidad blanca
    horizontal y densidad rosa decreciente como uno sobre frecuencia entre
    125 Hz y 8000 Hz. El panel inferior muestra seis octavas: el contenido
    blanco se duplica en cada octava y el rosa permanece constante.
    """

    lower_frequency_hz = 125.0
    upper_frequency_hz = 8000.0
    reference_frequency_hz = 1000.0
    white_density_pa2_hz = 1.0e-8
    pink_constant_pa2 = (
        white_density_pa2_hz * reference_frequency_hz
    )

    frequency_hz = np.geomspace(
        lower_frequency_hz,
        upper_frequency_hz,
        1000,
    )
    white_density = np.full_like(frequency_hz, white_density_pa2_hz)
    pink_density = pink_constant_pa2 / frequency_hz

    octave_edges_hz = lower_frequency_hz * 2 ** np.arange(7)
    white_band_pa2 = white_density_pa2_hz * np.diff(octave_edges_hz)
    pink_band_pa2 = pink_constant_pa2 * np.log(
        octave_edges_hz[1:] / octave_edges_hz[:-1]
    )
    white_relative = white_band_pa2 / white_band_pa2[0]
    pink_relative = pink_band_pa2 / pink_band_pa2[0]

    assert np.allclose(white_relative, 2 ** np.arange(6))
    assert np.allclose(pink_relative, np.ones(6))

    figure, axes = plt.subplots(
        2,
        1,
        figsize=(4.75, 4.80),
        constrained_layout=True,
        gridspec_kw={"height_ratios": [1.05, 1.0]},
    )

    axes[0].plot(
        frequency_hz,
        white_density,
        color=BLUE,
        label="blanco: $S_0$",
    )
    axes[0].plot(
        frequency_hz,
        pink_density,
        color=ORANGE,
        linestyle="--",
        label="rosa: $K/f$",
    )
    axes[0].set_xscale("log", base=2)
    axes[0].set_yscale("log")
    axes[0].set_xlim(lower_frequency_hz, upper_frequency_hz)
    axes[0].set_xticks([125, 250, 500, 1000, 2000, 4000, 8000])
    axes[0].set_xticklabels(
        ["125", "250", "500", "1k", "2k", "4k", "8k"]
    )
    axes[0].set_xlabel(r"Frecuencia $f$ (Hz; escala logarítmica)")
    axes[0].set_ylabel(r"$S_{pp}(f)$ ($\mathrm{Pa^2/Hz}$)")
    axes[0].grid(True, which="both", color=GRID_GRAY, linewidth=0.45)
    axes[0].legend(frameon=False, loc="lower left")
    panel_label(axes[0], "(a)")

    positions = np.arange(6)
    width = 0.36
    axes[1].bar(
        positions - width / 2,
        white_relative,
        width,
        color=BLUE,
        edgecolor="black",
        linewidth=0.4,
        label="blanco",
    )
    axes[1].bar(
        positions + width / 2,
        pink_relative,
        width,
        color="white",
        edgecolor=ORANGE,
        hatch="///",
        linewidth=0.8,
        label="rosa",
    )
    axes[1].set_xticks(positions)
    axes[1].set_xticklabels(
        ["125–\n250", "250–\n500", "500–\n1k", "1k–\n2k", "2k–\n4k", "4k–\n8k"]
    )
    axes[1].set_xlabel("Banda de octava (Hz)")
    axes[1].set_ylabel(
        r"$p_{B,\mathrm{rms}}^2/p_{B1,\mathrm{rms}}^2$ (adimensional)"
    )
    axes[1].set_ylim(0, 35)
    axes[1].grid(True, axis="y", color=GRID_GRAY, linewidth=0.45)
    axes[1].legend(frameon=False, loc="upper left")
    axes[1].text(
        0.99,
        0.95,
        "(b)",
        transform=axes[1].transAxes,
        ha="right",
        va="top",
        fontweight="bold",
    )

    save_figure(figure, "blanco-rosa-energia-bandas.pdf")


def signal_to_noise_ratios() -> None:
    """Muestra una señal sintética sumada al mismo ruido con tres SNR.

    Descripción accesible: tres paneles muestran la misma señal determinística
    con ruido a SNR de +12 dB, 0 dB y -6 dB. Al disminuir la SNR, la mezcla
    sólida se aparta cada vez más de la señal limpia dibujada con línea
    discontinua.
    """

    sampling_frequency_hz = 4000.0
    duration_s = 0.250
    time_s = np.arange(int(sampling_frequency_hz * duration_s))
    time_s = time_s / sampling_frequency_hz

    envelope = np.sin(np.pi * time_s / duration_s) ** 2
    signal_mpa = envelope * (
        np.sin(2 * np.pi * 240.0 * time_s)
        + 0.45 * np.sin(2 * np.pi * 430.0 * time_s + np.pi / 4)
    )
    signal_mpa = signal_mpa / np.sqrt(np.mean(signal_mpa**2))

    rng = np.random.default_rng(1050)
    base_noise = _zero_mean_unit_rms(rng.standard_normal(time_s.size))
    target_snr_db = (12.0, 0.0, -6.0)

    figure, axes = plt.subplots(
        3,
        1,
        figsize=(4.75, 4.75),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    signal_rms_mpa = np.sqrt(np.mean(signal_mpa**2))
    mixtures = []
    for snr_db in target_snr_db:
        noise_rms_mpa = signal_rms_mpa / (10 ** (snr_db / 20))
        noise_mpa = base_noise * noise_rms_mpa
        achieved_snr_db = 20 * np.log10(
            signal_rms_mpa / np.sqrt(np.mean(noise_mpa**2))
        )
        assert abs(achieved_snr_db - snr_db) < 1e-12
        mixtures.append(signal_mpa + noise_mpa)

    maximum = max(
        np.max(np.abs(signal_mpa)),
        *(np.max(np.abs(mixture)) for mixture in mixtures),
    )
    vertical_limit = np.ceil(maximum * 2) / 2

    for axis, mixture, snr_db, label in zip(
        axes,
        mixtures,
        target_snr_db,
        ("(a)", "(b)", "(c)"),
    ):
        axis.plot(
            time_s * 1000,
            mixture,
            color=BLUE,
            linewidth=0.75,
            label="mezcla",
        )
        axis.plot(
            time_s * 1000,
            signal_mpa,
            color=ORANGE,
            linestyle="--",
            linewidth=1.1,
            label="señal sin ruido",
        )
        axis.axhline(0, color=LIGHT_GRAY, linewidth=0.6)
        axis.set_ylim(-vertical_limit, vertical_limit)
        axis.set_ylabel(r"$p(t)$ (mPa)")
        axis.grid(True, color=GRID_GRAY, linewidth=0.45)
        panel_label(axis, label)
        sign = "+" if snr_db > 0 else ""
        axis.text(
            0.99,
            0.94,
            f"SNR = {sign}{snr_db:.0f} dB",
            transform=axis.transAxes,
            ha="right",
            va="top",
        )

    axes[0].legend(frameon=False, loc="lower right")
    axes[-1].set_xlabel(r"Tiempo $t$ (ms)")
    axes[-1].set_xlim(0, duration_s * 1000)

    save_figure(figure, "relaciones-senal-ruido.pdf")


def main() -> None:
    configure_style()
    temporal_realizations()
    statistics_same_rms()
    white_pink_band_energy()
    signal_to_noise_ratios()
    print(f"Figuras generadas en: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
