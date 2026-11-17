#!/usr/bin/env python3
"""Exec one serial worker inside the outer capped artifact directory."""
import os
import sys
from pathlib import Path

root = Path(os.environ['CAPPED_OUT']).resolve()
work = Path(sys.argv[1]).resolve()
assert work == root or root in work.parents, 'artifact directory escapes capped root'
work.mkdir(parents=True, exist_ok=True)
os.chdir(work)
os.execvpe(sys.argv[2], sys.argv[2:], os.environ)
