#!/usr/bin/env python3
"""Exec the native checker in place, so aggregate accounting has one child."""
import os
import json
import sys
from pathlib import Path

out, tick, checker = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
if tick == 'prefix':
    r = json.loads((out / 'result.json').read_text())
    args = [checker, str(out / 'original.cnf'), str(out / 'lemma-prefix.drup'), '-U', '-f']
else:
    stem = out / f'guard{int(tick)}'
    args = [checker, str(stem.with_suffix('.cnf')), str(stem.with_suffix('.drat')), '-U']
os.execv(checker, args)
