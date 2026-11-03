#!/usr/bin/env python3
"""L1453/L1454 (Local, 2026-11-03): a bounded model check of the 11/81 wall on 1010000. Run:
python3 tests/probes/wolfram/a4_wall_robustness.py DATA63.json PATTERN T0 W H MARGIN OUT.cnf [both|ahead|behind]
Fixed: PATTERN's exact row at T0 at and left of x = A0 + W (A0 = F(T0) - 1): the background half-line and the window. Free:
every cell right of it that can matter within H ticks (relative W + 1 .. W + H). Question: is there right content for which
the left front F leaves the band line(t) + [gmin - MARGIN, gmax + MARGIN] at some tick t <= H, where line(t) is the 11/81
line through F(T0) and [gmin, gmax] the actual front's own deviation over the same ticks? SAT gives such content (replayed by
plain simulation); UNSAT says no right content moves the front out of the band within H ticks (DRAT proof written).
"""
import json
import math
import sys

import numpy as np
from pysat.solvers import Solver

data = json.load(open(sys.argv[1])); PAT = int(sys.argv[2], 0); T0, W, H, MARGIN = map(int, sys.argv[3:7]); CNF = sys.argv[7]
SIDE = sys.argv[8] if len(sys.argv) > 8 else 'both'  # 'both', 'ahead' (F < lower edge: faster, towards 2/9), 'behind' (F > upper edge)
orb = [tuple(o) for o in data['orb']]; q = len(orb); N = data['N']; r0, s0 = data['r'], data['s']
E = lambda x, t: orb[(t + s0) % q][((t - x) + r0) % N]
rule = lambda a, b, c: a ^ (b | c)
TM = T0 + H + 5; lo = -2 * TM - 10; hi = TM + W + 30; c = -lo
row = np.array([E(x, 0) for x in range(lo, hi)], dtype=np.uint8); bg = row.copy()
for i in range(12):
    row[c + i] ^= (PAT >> i) & 1
rows = []
for t in range(1, T0 + H + 1):
    n = np.zeros_like(row); n[1:-1] = row[:-2] ^ (row[1:-1] | row[2:]); row = n
    m = np.zeros_like(bg); m[1:-1] = bg[:-2] ^ (bg[1:-1] | bg[2:]); bg = m
    if t >= T0:
        rows.append((row.copy(), bg.copy()))
Fact = [int(np.flatnonzero(X ^ B).min()) - c for X, B in rows]
F0 = Fact[0]; A0 = F0 - 1
line = [F0 - 11 * k / 81 for k in range(H + 1)]
dev = [Fact[k] - line[k] for k in range(H + 1)]
gmin, gmax = min(dev), max(dev)
lo_b = [math.ceil(line[k] + gmin - MARGIN) for k in range(H + 1)]   # F must stay >= lo_b
hi_b = [math.floor(line[k] + gmax + MARGIN) for k in range(H + 1)]  # F must stay <= hi_b
print('pattern %d, T0=%d: actual front deviation from the 11/81 line over %d ticks in [%.2f, %.2f]; band margin %d' % (
    PAT, T0, H, gmin, gmax, MARGIN))
X0 = rows[0][0]
XL = A0 - H - 3; XR = lambda k: A0 + W + H - k
vid = {}
def v(k, x):
    if (k, x) not in vid:
        vid[(k, x)] = len(vid) + 1
    return vid[(k, x)]
cl = []
for x in range(XL, XR(0) + 1):
    if x <= A0 + W:
        cl.append([v(0, x)] if X0[c + x] else [-v(0, x)])
for k in range(H):
    for x in range(XL + 1, XR(k + 1) + 1):
        a, b_, cc, o = v(k, x - 1), v(k, x), v(k, x + 1), v(k + 1, x)
        for la in (0, 1):
            for lb in (0, 1):
                for lc in (0, 1):
                    lit = lambda var, val: -var if val else var
                    cl.append([lit(a, la), lit(b_, lb), lit(cc, lc), o if rule(la, lb, lc) else -o])
    cl.append([v(k + 1, XL)] if E(XL, T0 + k + 1) else [-v(k + 1, XL)])
D = lambda k, x: v(k, x) if E(x, T0 + k) == 0 else -v(k, x)   # literal "cell (k, x) differs from the background"
viol = []
for k in range(1, H + 1):
    assert lo_b[k] - 1 >= XL and hi_b[k] <= XR(k)
    if SIDE in ('both', 'ahead'):
        viol += [D(k, x) for x in range(XL + 1, lo_b[k])]             # a difference left of the band: F < lo_b
    if SIDE == 'ahead':
        continue
    y = len(vid) + 1 + k * 0; vid[('y', k)] = len(vid) + 1; y = vid[('y', k)]
    cl += [[-y, -D(k, x)] for x in range(XL + 1, hi_b[k] + 1)]           # y_k: no difference at or left of hi_b: F > hi_b
    viol.append(y)
cl.append(viol)
print('violation side: %s; free cells %d (relative %d..%d); variables %d, clauses %d' % (SIDE, H, W + 1, W + H, len(vid), len(cl)))
with open(CNF, 'w') as f:
    f.write('p cnf %d %d\n' % (len(vid), len(cl)))
    for c_ in cl:
        f.write(' '.join(map(str, c_)) + ' 0\n')
# positive control: the actual content must NOT violate (the same CNF with the free cells fixed to the actual row is UNSAT)
ctl = cl + [[v(0, x)] if X0[c + x] else [-v(0, x)] for x in range(A0 + W + 1, XR(0) + 1)]
with Solver(name='cadical195', bootstrap_with=ctl) as s:
    print('control (free cells fixed to the actual content): %s (expected UNSAT: the actual front stays in its band)' % (
        'SAT' if s.solve() else 'UNSAT'))
with Solver(name='cadical195', bootstrap_with=cl) as s:
    sat = s.solve(); model = s.get_model() if sat else None
print('CaDiCaL, any right content: %s' % ('SAT' if sat else 'UNSAT'))
if sat:
    ms = set(l for l in model if l > 0)
    ext = [1 if v(0, x) in ms else 0 for x in range(A0 + W + 1, XR(0) + 1)]
    r2 = X0.copy(); b2 = rows[0][1].copy()
    for i, x in enumerate(range(A0 + W + 1, XR(0) + 1)):
        r2[c + x] = ext[i]
    out_at = None
    for k in range(1, H + 1):
        n = np.zeros_like(r2); n[1:-1] = r2[:-2] ^ (r2[1:-1] | r2[2:]); r2 = n
        m = np.zeros_like(b2); m[1:-1] = b2[:-2] ^ (b2[1:-1] | b2[2:]); b2 = m
        Fk = int(np.flatnonzero(r2 ^ b2).min()) - c
        if not (lo_b[k] <= Fk <= hi_b[k]):
            out_at = (k, Fk, lo_b[k], hi_b[k]); break
    print('replay by plain simulation: the front leaves the band at (tick, F, lo, hi) = %s' % (out_at,))
    print('the breaking right content (relative %d..%d): %s' % (W + 1, W + H, ''.join(map(str, ext))))
print('A4_WALL_ROBUSTNESS_DONE')
