#!/usr/bin/env python3
"""Extract a native checked original-proof core, no new search."""
import os
import sys
from pathlib import Path

old, out, tick, checker = Path(sys.argv[1]), Path(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
out.mkdir(parents=True, exist_ok=True)
os.execv(checker, [checker, str(old / f'guard{tick}.cnf'), str(old / f'guard{tick}.drat'),
                  '-U', '-c', str(out / f'core{tick}.cnf')])
