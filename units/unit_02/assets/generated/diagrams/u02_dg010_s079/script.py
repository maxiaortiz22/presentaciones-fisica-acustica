from pathlib import Path
import sys

here = Path(__file__).resolve()
unit_dir = next(parent for parent in here.parents if parent.name == "unit_02")
sys.path.insert(0, str(unit_dir / "scripts"))
from u02_diagram_lib import generate_one

if __name__ == "__main__":
    generate_one("U02-079")
