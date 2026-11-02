#!/usr/bin/env python3
"""L1309 T31 (Local, 2026-11-02): analysis of the rings written by rotators_census.c.
reports/rule30-genealogy.md section 36. Run: python3 tests/probes/rotators_census.py RINGDIR

For each ring (file name gives g, orientation, lag r, ring size M and period P), independently of the register:
- evolves it under c(y)_i = y_i ^ (y_(i-1) | y_(i-2)) with numpy and checks the least period P;
- checks c^g = rotation by r (forward: (c^g y)_n = y_(n-r); backward: y_(n+r));
- for every column (time series of one cell over one period): its weight parity, so the share of odd-weight columns
  (type 1; a phase with all columns odd is a rigid corridor with no exits at its own period);
- for up to 64 sampled columns: tau-adic valuation and least period;
- the twisted depth period m = gcd(r, M) and the number of distinct column classes up to time rotation (sampled).
Phases are grouped by their column-class signature, so lifts and repeats across registers are reported once.
"""
import math
import os
import re
import sys
import numpy as np

d = sys.argv[1]
rows = []
for fn in sorted(os.listdir(d)):
    mt = re.match(r'ring_g(\d)([fb])_r(\d+)_M(\d+)_P(\d+)\.txt', fn)
    if not mt:
        continue
    g, o, r, M, P = int(mt[1]), mt[2], int(mt[3]), int(mt[4]), int(mt[5])
    y0 = np.array([int(ch) for ch in open(os.path.join(d, fn)).read().strip()], dtype=np.uint8)
    assert len(y0) == M
    step = lambda z: z ^ (np.roll(z, 1) | np.roll(z, 2))
    z = y0.copy(); par = np.zeros(M, dtype=np.uint8); samp = list(range(0, M, max(1, M // 64)))[:64]
    series = np.zeros((len(samp), P), dtype=np.uint8); Pfound = 0; zg = None
    for t in range(P):
        par ^= z; series[:, t] = z[samp]
        z = step(z)
        if t + 1 == g:
            zg = z.copy()
        if t + 1 < P and np.array_equal(z, y0):
            Pfound = t + 1; break
    ok_period = (Pfound == 0) and np.array_equal(z, y0)
    rot = np.roll(y0, r) if o == 'f' else np.roll(y0, -r)
    ok_rot = zg is not None and np.array_equal(zg, rot)
    Mm = (1 << P) - 1

    def integ(c):
        yv, s = c, 1
        while s < P:
            yv ^= (yv << s) & Mm; s <<= 1
        return (yv << 1) & Mm

    def val(c):
        k = 0
        while c:
            if bin(c).count('1') & 1:
                return k
            c = integ(c); k += 1
        return P

    def lp(c):
        q = 1
        while q < P and (((c >> q) | (c << (P - q))) & Mm) != c:
            q *= 2
        return q

    def canon(c):
        return min((((c >> s) | (c << (P - s))) & Mm) for s in range(P))
    cols = [int(''.join(map(str, series[i][::-1])), 2) for i in range(len(samp))]
    vals = sorted(set(val(c) for c in cols)); lps = sorted(set(lp(c) for c in cols))
    classes = len(set(canon(c) for c in cols)) if P <= 1024 else None
    odd = int(par.sum())
    rows.append(dict(fn=fn, g=g, o=o, r=r, M=M, P=P, ok=ok_period and ok_rot, m=math.gcd(r, M), odd=odd,
                     vals=vals, lps=lps, classes=classes, sig=(M, P, odd, tuple(vals))))
seen = {}
for row in rows:
    seen.setdefault(row['sig'], []).append(row)
print('rings analysed %d; distinct phases (by ring size, period, odd-column count, valuations) %d' % (len(rows), len(seen)))
for sig, rs in sorted(seen.items(), key=lambda kv: (kv[0][1], kv[0][0])):
    r0 = rs[0]
    print('P=%5d ring M=%7d  m=gcd(r,M)=%5d  odd-weight columns %7d of %7d (%s)  sampled valuations %s  column least periods %s  classes(sampled) %s  checks %s  found as %s' % (
        r0['P'], r0['M'], r0['m'], r0['odd'], r0['M'], 'rigid corridor' if r0['odd'] == r0['M'] else 'has exits',
        r0['vals'], r0['lps'], r0['classes'], 'ok' if all(x['ok'] for x in rs) else 'FAILED',
        ', '.join('g%d%s r%d' % (x['g'], x['o'], x['r']) for x in rs[:4]) + (' …' if len(rs) > 4 else '')))
