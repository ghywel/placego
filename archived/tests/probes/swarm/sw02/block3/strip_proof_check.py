#!/usr/bin/env python3
"""Exec the native checker only for a returned strip UNSAT proof."""
import os
import sys
from pathlib import Path

stem, checker = Path(sys.argv[1]), sys.argv[2]
if stem.with_suffix('.drat').exists():
    os.execv(checker, [checker, str(stem.with_suffix('.cnf')),
                      str(stem.with_suffix('.drat')), '-U'])
print('NO_UNSAT_PROOF', stem.name)
