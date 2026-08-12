"""Wrapper reproducible para U07-CH-008."""
from pathlib import Path
import subprocess, sys
subprocess.run([sys.executable, str(Path(__file__).resolve().parents[3] / "scripts" / "u07_generate_charts.py"), "U07-CH-008"], check=True)
