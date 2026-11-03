#!/usr/bin/env python3
"""L1440 (Local, 2026-11-03): P-i. What follows the 11/81 wall on 1010000? For single finite perturbations, evolve exactly and,
at several times, look right of the left front F for the longest segment on which the row is spatially periodic with a
period N' <= 16 (row[x] = row[x + N']), starting within 40 cells of F. Report N', where the segment starts and ends
(relative to F), and whether it is the original background there. Run:
python3 tests/probes/wolfram/a4_slow_wall_wake.py DATA63.json TMAX PATTERN [PATTERN ...]
"""
import json
import sys

import numpy as np

data = json.load(open(sys.argv[1])); TMAX = int(sys.argv[2]); PATS = [int(p, 0) for p in sys.argv[3:]]
orb = [tuple(o) for o in data['orb']]; q = len(orb); N = data['N']; r0, s0 = data['r'], data['s']
E = lambda x, t: orb[(t + s0) % q][((t - x) + r0) % N]
TIMES = [t for t in range(500, TMAX + 1, 500)]
lo = -2 * TMAX - 10; hi = TMAX + 22; c = -lo
for pat in PATS:
    row = np.array([E(x, 0) for x in range(lo, hi)], dtype=np.uint8); bg = row.copy()
    for i in range(12):
        row[c + i] ^= (pat >> i) & 1
    out = []
    for t in range(1, TMAX + 1):
        n = np.zeros_like(row); n[1:-1] = row[:-2] ^ (row[1:-1] | row[2:]); row = n
        m = np.zeros_like(bg); m[1:-1] = bg[:-2] ^ (bg[1:-1] | bg[2:]); bg = m
        if t not in TIMES:
            continue
        d = np.flatnonzero(row ^ bg); F = int(d.min()); R = int(d.max())
        valid_hi = len(row) - t - 2  # exact range
        best = None
        for Np in range(1, 17):
            eq = row[F + 1: valid_hi - Np] == row[F + 1 + Np: valid_hi]
            # longest run of True starting within 40 cells of F
            dd = np.diff(np.concatenate([[0], eq.astype(np.int8), [0]]))
            ss = np.flatnonzero(dd == 1); ee = np.flatnonzero(dd == -1)
            for s_, e_ in zip(ss, ee):
                if s_ <= 40 and (best is None or (e_ - s_) > best[2]):
                    best = (Np, int(s_) + 1, int(e_ - s_) + Np)
        Np, st, ln = best
        seg = slice(F + st, F + st + ln)
        isbg = bool((row[seg] == bg[seg]).all())
        word = ''.join(map(str, row[F + st: F + st + Np]))
        out.append('t=%d F=%d R-F=%d: periodic segment N\'=%d from F+%d, length %d (%.2f of R-F), word %s, original background: %s' % (
            t, F - c, R - F, Np, st, ln, ln / max(1, R - F), word, isbg))
    print('pattern %d (0x%x):' % (pat, pat)); print('  ' + '\n  '.join(out), flush=True)
print('A4_SLOW_WALL_WAKE_DONE')
