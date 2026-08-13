"""Lanzador reproducible de U10-CH-003."""
from pathlib import Path
import subprocess, sys
master=Path(__file__).resolve().parents[4]/"scripts"/"u10_generate_charts.py"
subprocess.run([sys.executable,str(master),"--id","U10-CH-003"],check=True)
