#!/usr/bin/env python3
"""L1315 T40 (Local, 2026-11-02): is the clean-start wake of a periodic-wake phase a space-time periodic background?
reports/rule30-genealogy.md section 43. Run: python3 tests/probes/wake_background.py PHASE PERIOD ADVANCE [T]

Clean start: the phase directly below a black edge (P1024 at theta = 0, or the 480-state phase at alignment (0, 0)),
evolved T ticks by the edge map. In the middle of the wake (depths between a quarter and three quarters of the front's
depth at the last time), test the moving-frame recurrence X_(n + ADVANCE)(t + PERIOD) = X_n(t) (edge-frame depth n). If
it holds on the whole middle region, the wake is space-time periodic there; its lab velocity is
1 - ADVANCE/PERIOD. Also reported: the smallest spatial period of the middle region at one time (in the edge frame a
lab-spatial period shows as a depth period at fixed time).
"""
import os
import sys
import runpy
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
name, PER, ADV = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); T = int(sys.argv[4]) if len(sys.argv) > 4 else 3000
p, cols, _ = g['phases']()[name]; NC = len(cols)
depth = 2 * T + 16; mask = (1 << depth) - 1
if name == 'P1024':
    E = lambda n, t: (cols[0] >> ((t + 195 * n) % p)) & 1
else:
    E = lambda n, t: (cols[n % NC] >> (t % p)) & 1
x = sum(E(n, 0) << n for n in range(depth))
hist = []
for t in range(T + 1):
    hist.append(x); x = (x ^ ((x << 1) | (x << 2) | 3)) & mask
Erow = lambda t: sum(E(n, t) << n for n in range(depth))
R = ((hist[T] ^ Erow(T)) & mask).bit_length() - 1
lo, hi = R // 4, 3 * R // 4
bit = lambda t, n: (hist[t] >> n) & 1
ok = all(bit(t + PER, n + ADV) == bit(t, n) for t in range(T - PER - 600, T - PER) for n in range(lo, hi - ADV))
print('%s clean start, %d ticks: front at depth %d; middle region depths %d..%d' % (name, T, R, lo, hi))
print('   moving-frame recurrence X(n + %d, t + %d) = X(n, t) on the middle region over the last 600 ticks: %s; lab velocity %s' % (
    ADV, PER, ok, '1 - %d/%d' % (ADV, PER)))
row = [bit(T, n) for n in range(lo, hi)]
sp = next((q for q in range(1, len(row) // 2) if all(row[i] == row[i + q] for i in range(len(row) - q))), None)
print('   smallest depth period of the middle region at time T: %s' % sp)
