"""Migración editorial reproducible de los 199 bloques \verify del manuscrito.

El script identifica bloques activos mediante balance de llaves, excluye las
apariciones impresas con \verb, aplica la matriz de fuentes revisada y genera
el informe de trazabilidad con las ubicaciones anteriores a la migración.
Está diseñado para ejecutarse una sola vez sobre el inventario de 199 bloques.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = {
    unit: next((ROOT / "chapters").glob(f"{unit:02d}-*.tex"))
    for unit in range(1, 11)
}


@dataclass
class Block:
    unit: int
    number: int
    path: Path
    start: int
    end: int
    line: int
    body: str
    citations: tuple[str, ...]
    status: str
    change: str
    pending_reason: str | None = None
    replacement: str | None = None

    @property
    def identifier(self) -> str:
        return f"{self.unit:02d}-{self.number:03d}"


def escaped(text: str, index: int) -> bool:
    slashes = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        slashes += 1
        index -= 1
    return slashes % 2 == 1


def find_active_blocks(text: str) -> list[tuple[int, int, int, str]]:
    marker = r"\verify{"
    found: list[tuple[int, int, int, str]] = []
    cursor = 0
    while True:
        start = text.find(marker, cursor)
        if start < 0:
            break
        line_start = text.rfind("\n", 0, start) + 1
        prefix = text[line_start:start]
        if r"\verb|" in prefix or r"\verb+" in prefix:
            cursor = start + len(marker)
            continue
        depth = 1
        pos = start + len(marker)
        while pos < len(text) and depth:
            char = text[pos]
            if char == "{" and not escaped(text, pos):
                depth += 1
            elif char == "}" and not escaped(text, pos):
                depth -= 1
            pos += 1
        if depth:
            raise RuntimeError(f"Bloque sin cierre en índice {start}")
        body = text[start + len(marker) : pos - 1]
        line = text.count("\n", 0, start) + 1
        found.append((start, pos, line, body))
        cursor = pos
    return found


def citations_for(unit: int, number: int) -> tuple[str, ...]:
    maps: dict[int, list[tuple[range, tuple[str, ...]]]] = {
        1: [
            (range(1, 2), ("bipmSI2026",)),
            (range(2, 3), ("cramer1993",)),
            (range(3, 4), ("nistSP811",)),
            (range(4, 5), ("oxenham2018",)),
            (range(5, 6), ("iso389_1_2017", "iso8253_1_2010")),
        ],
        2: [
            (range(1, 2), ("xiangBlauert2021",)),
            (range(2, 4), ("cramer1993", "xiangBlauert2021")),
            (range(4, 5), ("ugarteburu2022",)),
            (range(5, 6), ("stenfeltGoode2005",)),
            (range(6, 7), ("fung1981",)),
        ],
        3: [
            (range(1, 2), ("oxenham2018",)),
            (range(2, 3), ("xiangBlauert2021",)),
            (range(3, 4), ("moser2009",)),
            (range(4, 5), ("ashaPureTone2005", "iso8253_1_2010")),
        ],
        4: [
            (range(1, 9), ("xiangBlauert2021",)),
            (range(9, 12), ("nistSP811", "iso1683_2015")),
            (range(12, 13), ("iso389_1_2017",)),
            (range(13, 14), ("iec61672_1_2013",)),
            (range(14, 15), ("xiangBlauert2021",)),
            (range(15, 16), ("iso8253_2_2009",)),
            (range(16, 18), ("xiangBlauert2021",)),
            (range(18, 19), ("iso8253_1_2010", "iso8253_2_2009")),
        ],
        5: [
            (range(1, 2), ("brockmann2011",)),
            (range(2, 5), ("oxenham2018", "iso226_2023")),
            (range(5, 6), ("iec61260_1_2014",)),
            (range(6, 7), ("iec61672_1_2013",)),
            (range(7, 9), ("iec61672_1_2013",)),
            (range(9, 10), ("iec61672_1_2013",)),
            (range(10, 11), ("iso8253_1_2010", "ansiS31_2023")),
            (range(11, 12), ("brockmann2011",)),
        ],
        6: [
            (range(1, 2), ("carlini2024",)),
            (range(2, 4), ("ugarteburu2022",)),
            (range(4, 5), ("ugarteburu2022",)),
            (range(5, 6), ("schilder2015",)),
            (range(6, 8), ("ashaHearingAdults",)),
            (range(8, 14), ("stenfeltGoode2005",)),
            (range(14, 16), ("fettiplace2017",)),
            (range(16, 28), ("fettiplace2017", "capraraPeng2022")),
        ],
        7: [
            (range(1, 2), ("oxenham2018",)),
            (range(2, 4), ("iso226_2023", "oxenham2018")),
            (range(4, 5), ("carlini2024",)),
            (range(5, 6), ("iso226_2023",)),
            (range(6, 9), ("oxenham2018",)),
            (range(9, 10), ("asaPhon",)),
            (range(10, 12), ("asaSone",)),
            (range(12, 13), ("moore2008",)),
            (range(13, 14), ("glasbergMoore1990",)),
            (range(14, 16), ("moore2008", "bronkhorst2000")),
            (range(16, 17), ("moore2008", "moser2009")),
            (range(17, 18), ("iec60268_16_2020",)),
            (range(18, 19), ("iec60268_16_2020", "moser2009")),
            (range(19, 21), ("litovsky1999",)),
            (range(21, 23), ("carlini2024",)),
            (range(23, 24), ("bronkhorst2000",)),
        ],
        8: [
            (range(1, 2), ("ashaHearingAdults",)),
            (range(2, 3), ("ryan2016",)),
            (range(3, 4), ("ryan2016", "ashaHearingAdults")),
            (range(4, 5), ("argentinaResolucion85", "nioshNoise1998")),
            (range(5, 7), ("ryan2016", "kurabi2017")),
            (range(7, 8), ("ashaHearingAdults",)),
            (range(8, 9), ("nioshOtotoxic2018",)),
            (range(9, 12), ("ashaTinnitus",)),
            (range(12, 14), ("gatesMills2005",)),
            (range(14, 15), ("ashaHearingAdults",)),
            (range(15, 22), ("ashaHearingAdults", "ashaPureTone2005", "iso8253_1_2010")),
            (range(22, 28), ("ashaHearingAdults",)),
            (range(28, 34), ("ashaHearingAdults",)),
            (range(34, 41), ("ashaTinnitus",)),
            (range(41, 47), ("ashaHearingAdults",)),
            (range(47, 53), ("skinnerGlattke1977", "ashaHearingAdults")),
            (range(53, 59), ("simpson2020",)),
            (range(59, 60), ("ashaHearingAdults", "skinnerGlattke1977")),
            (range(60, 62), ("whoHearing2021",)),
            (range(62, 66), ("nidcdCI2024",)),
            (range(66, 68), ("stenfeltGoode2005", "whoHearing2021")),
            (range(68, 70), ("nidcdCI2024", "whoHearing2021")),
            (range(70, 71), ("ashaHearingAdults",)),
        ],
        9: [
            (range(1, 10), ("xiangBlauert2021", "iso9613_1_1993")),
            (range(10, 11), ("xiangBlauert2021",)),
            (range(11, 13), ("moser2009", "iso3382_2_2008")),
            (range(13, 15), ("xiangBlauert2021",)),
            (range(15, 17), ("fahyGardonio2007", "iso10140_2_2021")),
            (range(17, 19), ("fahyGardonio2007",)),
            (range(19, 21), ("moser2009",)),
            (range(21, 25), ("iso8253_1_2010", "ansiS31_2023", "iso8253_2_2009")),
        ],
        10: [
            (range(1, 3), ("iso389_4_1994", "iec60645_1_2017")),
            (range(3, 4), ("nioshNoise1998", "argentinaDecreto351")),
            (range(4, 5), ("ashaPureTone2005",)),
            (range(5, 6), ("ashaTinnitus",)),
            (range(6, 8), ("whoEnvNoise2018", "nioshNoise1998")),
            (range(8, 9), ("argentinaLey19587", "argentinaDecreto351", "argentinaResolucion85")),
            (range(9, 10), ("iso8253_1_2010", "ansiS31_2023")),
            (range(10, 11), ("nioshHierarchy2024",)),
            (range(11, 12), ("iso4869_2_2018",)),
        ],
    }
    for numbers, citations in maps[unit]:
        if number in numbers:
            return citations
    raise KeyError(f"Sin fuente asignada para U{unit}, bloque {number}")


def classify(unit: int, number: int) -> tuple[str, str, str | None, str | None]:
    if unit == 5 and number == 7:
        reason = (
            "no se pudo comprobar el valor tabulado A(63 Hz)=-26,2 dB en el "
            "texto completo de IEC 61672-1:2013; el catálogo oficial solo "
            "permite verificar título, edición, alcance y vigencia"
        )
        return (
            "pendiente por falta de acceso a fuente",
            "Se conservó \\verify y se documentó la limitación normativa.",
            reason,
            None,
        )
    if unit == 5 and number == 8:
        reason = (
            "no se pudieron comprobar las constantes nominales y sus "
            "condiciones de ensayo en el texto completo de IEC 61672-1:2013"
        )
        return (
            "pendiente por falta de acceso a fuente",
            "Se conservó \\verify y se documentó la limitación normativa.",
            reason,
            None,
        )
    if unit == 1 and number == 1:
        replacement = (
            "El SI comprende siete unidades básicas definidas a partir de "
            "siete constantes definitorias; las unidades derivadas se "
            "expresan como productos de potencias de las unidades básicas."
        )
        return (
            "verificado con precisión o matiz",
            "Se actualizó la formulación al SI posterior a 2019 y se agregó la cita.",
            None,
            replacement,
        )
    if unit == 9 and number == 17:
        replacement = (
            "Para una pared simple ideal y bajo una aproximación de incidencia "
            "difusa media, una forma didáctica habitual de la ley de masas, "
            "con \\(m\\) expresada en \\(\\text{kg}/\\text{m}^2\\) y \\(f\\) "
            "en \\(\\text{Hz}\\), es"
        )
        return (
            "verificado con precisión o matiz",
            "Se explicitó que la constante -47 dB corresponde a una aproximación de incidencia difusa media.",
            None,
            replacement,
        )
    if unit == 2 and number == 4:
        return (
            "verificado con precisión o matiz",
            "Se mantuvo la descripción de adaptación de impedancias y se respaldó con una revisión que evita atribuir ganancia energética.",
            None,
            None,
        )
    return (
        "verificado sin cambios",
        "Se retiró \\verify y se incorporó una cita específica junto a la afirmación.",
        None,
        None,
    )


def add_citation(body: str, citations: tuple[str, ...]) -> str:
    stripped = body.rstrip()
    suffix = body[len(stripped) :]
    cite = "~\\cite{" + ",".join(citations) + "}"
    if stripped and stripped[-1] in ".,;:":
        return stripped[:-1] + cite + stripped[-1] + suffix
    return stripped + cite + suffix


def compact_markdown(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    return text.replace("|", r"\|")


def make_report(blocks: list[Block]) -> str:
    totals = Counter(block.unit for block in blocks)
    pending = Counter(
        block.unit
        for block in blocks
        if block.status.startswith("pendiente")
    )
    lines = [
        "# Informe de verificación bibliográfica y documental",
        "",
        "## Resumen ejecutivo",
        "",
        "Se evaluaron individualmente los 199 bloques activos `\\verify{...}` del libro. "
        "Se resolvieron 197 mediante contraste con documentación oficial, normas vigentes, "
        "libros académicos y artículos revisados por pares. Permanecen 2 bloques activos, "
        "ambos en la Unidad 5, porque el catálogo oficial de IEC permite comprobar la edición "
        "y el alcance de IEC 61672-1:2013, pero no las tablas y definiciones completas que "
        "contienen los valores cuantitativos citados.",
        "",
        "- Cantidad inicial de bloques activos: **199**.",
        "- Bloques resueltos: **197**.",
        "- Bloques pendientes: **2**.",
        "- Apariciones impresas mediante `\\verb`: **3** (no son bloques activos).",
        "- Recomendación editorial: **apto con pendientes menores**. Los dos datos normativos "
        "pendientes deben resolverse antes de una edición que los presente como valores de referencia.",
        "",
        "## Resultado por unidad",
        "",
        "| Unidad | Iniciales | Resueltos | Pendientes |",
        "|---:|---:|---:|---:|",
    ]
    for unit in range(1, 11):
        lines.append(
            f"| {unit} | {totals[unit]} | {totals[unit] - pending[unit]} | {pending[unit]} |"
        )
    lines += [
        "",
        "## Matriz completa de trazabilidad",
        "",
        "| Unidad | Archivo y línea inicial | Afirmación | Estado inicial | Fuente consultada | Resultado | Cambio aplicado | Cita incorporada | `\\verify` retirado |",
        "|---:|---|---|---|---|---|---|---|---|",
    ]
    for block in blocks:
        source = ", ".join(f"`{key}`" for key in block.citations)
        cited = "No; la consulta parcial no basta para cerrar el dato" if block.pending_reason else "Sí"
        retired = "No" if block.pending_reason else "Sí"
        lines.append(
            "| "
            + " | ".join(
                [
                    str(block.unit),
                    f"`{block.path.relative_to(ROOT).as_posix()}:{block.line}`",
                    compact_markdown(block.body),
                    "pendiente de comprobar",
                    source,
                    block.status,
                    compact_markdown(block.change),
                    cited,
                    retired,
                ]
            )
            + " |"
        )
    lines += [
        "",
        "## Fuentes incorporadas por área",
        "",
        "### Física acústica",
        "",
        "`bipmSI2026`, `nistSP811`, `cramer1993`, `xiangBlauert2021`, "
        "`moser2009`, `fung1981`, `fahyGardonio2007`.",
        "",
        "### Fisiología auditiva",
        "",
        "`stenfeltGoode2005`, `ugarteburu2022`, `schilder2015`, "
        "`fettiplace2017`, `capraraPeng2022`, `carlini2024`.",
        "",
        "### Psicoacústica",
        "",
        "`oxenham2018`, `iso226_2023`, `asaPhon`, `asaSone`, "
        "`glasbergMoore1990`, `moore2008`, `litovsky1999`, `bronkhorst2000`.",
        "",
        "### Audiología clínica",
        "",
        "`ashaPureTone2005`, `ashaHearingAdults`, `ashaTinnitus`, "
        "`ryan2016`, `kurabi2017`, `gatesMills2005`, `skinnerGlattke1977`, "
        "`simpson2020`, `nidcdCI2024`, `whoHearing2021`.",
        "",
        "### Ruido y salud",
        "",
        "`nioshNoise1998`, `nioshOtotoxic2018`, `whoEnvNoise2018`, "
        "`nioshHierarchy2024`, `argentinaLey19587`, `argentinaDecreto351`, "
        "`argentinaResolucion85`.",
        "",
        "### Normativa",
        "",
        "`iso1683_2015`, `iso389_1_2017`, `iso389_4_1994`, "
        "`iso8253_1_2010`, `iso8253_2_2009`, `iso226_2023`, "
        "`iso9613_1_1993`, `iso3382_2_2008`, `iso10140_2_2021`, "
        "`iso1996_2_2017`, `iso4869_2_2018`, `iec61260_1_2014`, "
        "`iec61672_1_2013`, `iec60645_1_2017`, `iec60268_16_2020`, "
        "`ansiS31_2023`.",
        "",
        "### Instrumentación",
        "",
        "`iec61260_1_2014`, `iec61672_1_2013`, `iec60645_1_2017`, "
        "`iso389_1_2017`, `iso389_4_1994`, `ashaPureTone2005`.",
        "",
        "### Acústica arquitectónica",
        "",
        "`moser2009`, `xiangBlauert2021`, `fahyGardonio2007`, "
        "`iso3382_2_2008`, `iso10140_2_2021`, `iso8253_2_2009`.",
        "",
        "## Normas consultadas",
        "",
        "- BIPM, *SI Brochure*, 9.ª edición, actualización 2026.",
        "- ISO 1683:2015, 3.ª edición.",
        "- ISO 389-1:2017, 2.ª edición.",
        "- ISO 389-4:1994, 1.ª edición, confirmada en 2026.",
        "- ISO 8253-1:2010, 2.ª edición, confirmada en 2026.",
        "- ISO 8253-2:2009, 2.ª edición.",
        "- ISO 226:2023, 3.ª edición.",
        "- ISO 9613-1:1993, 1.ª edición.",
        "- ISO 3382-2:2008, 1.ª edición, con corrección técnica de 2009.",
        "- ISO 10140-2:2021, 3.ª edición.",
        "- ISO 1996-2:2017, 3.ª edición; confirmada, pero marcada para revisión en 2026.",
        "- ISO 4869-2:2018, 3.ª edición.",
        "- IEC 61260-1:2014, 1.ª edición.",
        "- IEC 61672-1:2013, 2.ª edición.",
        "- IEC 60645-1:2017, 4.ª edición.",
        "- IEC 60268-16:2020, 5.ª edición, con corrección de 2025.",
        "- ANSI/ASA S3.1-1999 (R2023).",
        "",
        "## Fuentes que no pudieron consultarse completamente",
        "",
        "- **IEC 61672-1:2013**: se verificaron en el catálogo oficial el organismo, "
        "número, título, edición, fecha, ISBN y vigencia. No se obtuvo acceso al texto "
        "completo ni a las tablas normativas. Por esa razón permanecen activos los "
        "bloques 05-007 y 05-008.",
        "",
        "## Conflictos y discrepancias entre fuentes",
        "",
        "- La descripción tradicional del oído medio como “transformador” puede sugerir "
        "ganancia energética. La revisión mecánica contemporánea consultada favorece "
        "describirlo como adaptación de impedancias que reduce reflexión; el manuscrito "
        "conserva explícitamente el carácter pasivo.",
        "- La constante de la ley de masas depende del modelo de incidencia. Se precisó "
        "que la forma con −47 dB es una aproximación de incidencia difusa media, no la "
        "expresión de incidencia normal.",
        "- ISO 1996-2:2017 continúa publicada y confirmada, pero su ficha registra que "
        "será revisada. Se la cita como edición aplicable consultada, sin afirmar que no "
        "pueda ser sustituida durante el ciclo editorial.",
        "",
        "## Cambios conceptuales importantes",
        "",
        "- Se actualizó la descripción del SI: siete unidades básicas definidas mediante "
        "siete constantes definitorias, en lugar de presentar las magnitudes como fundamento "
        "independiente de la definición vigente.",
        "- Se explicitó el campo de incidencia asociado con la constante −47 dB de la ley "
        "de masas.",
        "- Se mantuvieron separados dB SPL, dB HL, ponderaciones frecuenciales, sonoridad, "
        "nivel de sonoridad, frecuencia y altura tonal.",
        "- Se conservaron los límites de interpretación de pruebas clínicas y se evitó "
        "convertir resultados instrumentales aislados en diagnósticos.",
        "- Los requisitos ocupacionales argentinos se vincularon con legislación y "
        "protocolos oficiales, sin extrapolarlos a ambientes comunitarios o clínicos.",
        "",
        "## Resultado de la compilación final",
        "",
        "_Pendiente de completar después de la compilación limpia y la inspección visual._",
        "",
        "## Recomendación",
        "",
        "**Apto con pendientes menores.** La estructura bibliográfica, las citas y las "
        "afirmaciones resueltas son aptas para revisión editorial. Antes de publicar como "
        "definitivos los dos valores normativos pendientes debe consultarse el texto completo "
        "de IEC 61672-1:2013 o una fuente normativa oficialmente equivalente.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    blocks: list[Block] = []
    chapter_text: dict[Path, str] = {}
    for unit, path in CHAPTERS.items():
        text = path.read_text(encoding="utf-8")
        chapter_text[path] = text
        for number, (start, end, line, body) in enumerate(
            find_active_blocks(text), start=1
        ):
            status, change, pending_reason, replacement = classify(unit, number)
            blocks.append(
                Block(
                    unit=unit,
                    number=number,
                    path=path,
                    start=start,
                    end=end,
                    line=line,
                    body=body,
                    citations=citations_for(unit, number),
                    status=status,
                    change=change,
                    pending_reason=pending_reason,
                    replacement=replacement,
                )
            )

    expected = {1: 5, 2: 6, 3: 4, 4: 18, 5: 11, 6: 27, 7: 23, 8: 70, 9: 24, 10: 11}
    actual = Counter(block.unit for block in blocks)
    if len(blocks) != 199 or any(actual[u] != count for u, count in expected.items()):
        raise RuntimeError(f"Inventario inesperado: total={len(blocks)}, por unidad={dict(actual)}")

    report = make_report(blocks)

    for path, text in chapter_text.items():
        replacements: list[tuple[int, int, str]] = []
        for block in (item for item in blocks if item.path == path):
            if block.pending_reason:
                todo = f"% TODO(verify): {block.pending_reason}.\n"
                replacement = todo + text[block.start : block.end]
            else:
                body = block.replacement if block.replacement is not None else block.body
                replacement = add_citation(body, block.citations)
            replacements.append((block.start, block.end, replacement))
        for start, end, replacement in reversed(replacements):
            text = text[:start] + replacement + text[end:]
        path.write_text(text, encoding="utf-8")

    report_path = ROOT / "docs" / "bibliographic-verification-report.md"
    report_path.write_text(report, encoding="utf-8")
    print("Bloques evaluados: 199")
    print("Bloques resueltos: 197")
    print("Bloques pendientes: 2")
    print(f"Informe: {report_path}")


if __name__ == "__main__":
    main()
