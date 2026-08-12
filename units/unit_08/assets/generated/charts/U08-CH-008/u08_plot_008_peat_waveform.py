#!/usr/bin/env python3
"""Regenera 008."""
import importlib.util
from pathlib import Path
p=Path(__file__).resolve().parent/"../../../../scripts/u08_generate_visuals.py"
s=importlib.util.spec_from_file_location("u08_visuals",p.resolve())
m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
m.generate_one("chart","008")
