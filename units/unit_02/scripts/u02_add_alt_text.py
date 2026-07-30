from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path


PIC_CNVPR = re.compile(
    rb"(<p:pic>.*?<p:nvPicPr>.*?<p:cNvPr\b)([^>]*?)(/?>)",
    flags=re.DOTALL,
)
NAME = re.compile(rb'\bname="([^"]*)"')
DESCR = re.compile(rb'\bdescr="[^"]*"')


def add_alt_text(xml_bytes: bytes) -> tuple[bytes, int]:
    updated = 0

    def replace(match: re.Match[bytes]) -> bytes:
        nonlocal updated
        attrs = match.group(2)
        if DESCR.search(attrs):
            return match.group(0)
        name_match = NAME.search(attrs)
        if not name_match or not name_match.group(1):
            return match.group(0)
        updated += 1
        return match.group(1) + attrs + b' descr="' + name_match.group(1) + b'"' + match.group(3)

    return PIC_CNVPR.sub(replace, xml_bytes), updated


def patch_pptx(pptx_path: Path) -> int:
    temp_path = pptx_path.with_suffix(pptx_path.suffix + ".alt-text.tmp")
    total = 0
    with zipfile.ZipFile(pptx_path, "r") as source, zipfile.ZipFile(
        temp_path, "w", compression=zipfile.ZIP_DEFLATED
    ) as target:
        for item in source.infolist():
            data = source.read(item.filename)
            if re.fullmatch(r"ppt/slides/slide\d+\.xml", item.filename):
                data, count = add_alt_text(data)
                total += count
            target.writestr(item, data)
    temp_path.replace(pptx_path)
    return total


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Uso: python u02_add_alt_text.py <presentacion.pptx>")
    pptx_path = Path(sys.argv[1]).resolve()
    if not pptx_path.is_file():
        raise SystemExit(f"No existe: {pptx_path}")
    count = patch_pptx(pptx_path)
    print(f"Alt text agregado a {count} imágenes.")


if __name__ == "__main__":
    main()
