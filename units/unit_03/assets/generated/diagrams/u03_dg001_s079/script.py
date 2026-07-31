from pathlib import Path
import sys
here=Path(__file__).resolve()
unit_dir=next(p for p in here.parents if p.name=='unit_03')
sys.path.insert(0,str(unit_dir/'scripts'))
from u03_diagram_lib import generate_one
generate_one('U03-DG001', 79)
