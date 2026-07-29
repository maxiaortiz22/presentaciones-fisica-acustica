from pathlib import Path
import sys

scripts_dir = Path(__file__).resolve().parents[3] / "scripts"
if str(scripts_dir) not in sys.path:
    sys.path.insert(0, str(scripts_dir))

from u01_chartlib import generate_one

generate_one("U01-CH023")
