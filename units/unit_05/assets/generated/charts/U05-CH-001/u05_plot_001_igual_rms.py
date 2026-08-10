"""Lanzador reproducible de U05-CH-001."""
from pathlib import Path
import subprocess
import sys
master = Path(__file__).resolve().parents[4] / "scripts" / "u05_generate_charts.py"
subprocess.run([sys.executable, str(master), "--id", "U05-CH-001"], check=True)
