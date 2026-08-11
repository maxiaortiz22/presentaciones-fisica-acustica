"""Wrapper reproducible para U06-CH-002B."""
from pathlib import Path
import subprocess, sys
script = Path(__file__).resolve().parents[3] / "scripts" / "u06_generate_charts.py"
raise SystemExit(subprocess.call([sys.executable, str(script), "U06-CH-002B", "--condition", "compare"]))
