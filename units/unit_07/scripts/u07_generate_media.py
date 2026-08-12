"""Genera las dos demostraciones auditivas esenciales de la Unidad 7.

Los archivos son supraliminales y no calibrados. Se normalizan a un pico digital
prudente; el nivel de reproducción debe ajustarse a un volumen confortable.
"""

from __future__ import annotations

import math
import struct
import wave
from pathlib import Path


SR = 48_000
PEAK = 0.22
OUT = Path(__file__).resolve().parents[1] / "assets" / "generated" / "media"


def fade(signal: list[float], seconds: float = 0.025) -> list[float]:
    n = min(int(SR * seconds), len(signal) // 2)
    out = signal[:]
    for i in range(n):
        g = 0.5 - 0.5 * math.cos(math.pi * i / max(1, n - 1))
        out[i] *= g
        out[-1 - i] *= g
    return out


def sine(freq: float, seconds: float) -> list[float]:
    return fade([math.sin(2 * math.pi * freq * i / SR) for i in range(int(SR * seconds))])


def harmonic_complex(f0: float, seconds: float) -> list[float]:
    raw = []
    for i in range(int(SR * seconds)):
        t = i / SR
        raw.append(sum(math.sin(2 * math.pi * f0 * h * t) / h for h in range(1, 9)))
    mx = max(abs(v) for v in raw)
    return fade([v / mx for v in raw], 0.04)


def normalize(signal: list[float], peak: float = PEAK) -> list[float]:
    mx = max(1e-12, max(abs(v) for v in signal))
    return [peak * v / mx for v in signal]


def delayed_mix(source: list[float], delay_ms: float, copy_gain_db: float = -6.0) -> list[float]:
    delay = round(SR * delay_ms / 1000)
    gain = 10 ** (copy_gain_db / 20)
    out = [0.0] * (len(source) + delay)
    for i, value in enumerate(source):
        out[i] += value
        out[i + delay] += gain * value
    return normalize(out)


def silence(seconds: float) -> list[float]:
    return [0.0] * int(SR * seconds)


def write_wav(path: Path, signal: list[float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pcm = b"".join(struct.pack("<h", max(-32767, min(32767, round(v * 32767)))) for v in signal)
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(SR)
        wav.writeframes(pcm)


def main() -> None:
    tones = normalize(sine(250, 1.0)) + silence(0.55) + normalize(sine(1000, 1.0))
    write_wav(OUT / "u07_media_001_tonos_250_1000hz.wav", tones)

    source = harmonic_complex(140, 0.95)
    examples: list[float] = []
    for delay in (5.0, 20.0, 50.0):
        examples.extend(delayed_mix(source, delay))
        examples.extend(silence(0.65))
    write_wav(OUT / "u07_media_006_directo_copia_retardada.wav", examples)


if __name__ == "__main__":
    main()
