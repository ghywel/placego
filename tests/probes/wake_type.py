#!/usr/bin/env python3
"""L1314 T37 (a) (Local, 2026-11-02): the wake type of a phase under a black edge.
reports/rule30-genealogy.md section 42 (predictions written first). Run: python3 tests/probes/wake_type.py PHASE [T] [NALIGN]

Clean start: the phase's own digits directly below the black edge (depth -1), evolved by the edge map
Phi(x) = x ^ ((x << 1) | (x << 2) | 3). D(t) = Phi^t(X) xor E(t), front R(t) = deepest 1. A periodic wake shows as an
exact recurrence of (the 256 mismatch bits above the front, the front's class in the phase) at two times t1 < t2; the
first such pair after time 200 gives a period and a rational speed (R(t2) - R(t1)) / (t2 - t1). Reported per phase:
speed range, largest drawdown, alignments with a recurrence (period and speed), and alignments without one.
"""
import os
import random
import sys
import runpy
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
name = sys.argv[1]; T = int(sys.argv[2]) if len(sys.argv) > 2 else 4000; NAL = int(sys.argv[3]) if len(sys.argv) > 3 else 64
p, cols, _ = g['phases']()[name]; NC = len(cols)
depth = 2 * T + 16; mask = (1 << depth) - 1; WIN = 256
rng = random.Random(37)
if name == 'P1024':
    col0 = cols[0]
    aligns = [(th, 0) for th in rng.sample(range(p), NAL)]
    def E_bit(al, n, t):
        return (col0 >> ((al[0] + t + 195 * n) % p)) & 1
    def cls(al, R, t):
        return (al[0] + t + 195 * R) % p
else:
    allal = [(a, q) for a in range(NC) for q in range(p)]
    aligns = rng.sample(allal, min(NAL, len(allal)))
    def E_bit(al, n, t):
        return (cols[(n + al[0]) % NC] >> ((t + al[1]) % p)) & 1
    def cls(al, R, t):
        return ((R + al[0]) % NC, (t + al[1]) % p)
speeds = []; dds = []; periodic = []; aperiodic = 0
for al in aligns:
    rows = {}
    def erow(t):
        k = t % p
        if k not in rows:
            rows[k] = sum(E_bit(al, n, t) << n for n in range(depth))
        return rows[k]
    x = erow(0); best = -2; dd = 0; seen = {}; found = None
    for t in range(T + 1):
        d = (x ^ erow(t)) & mask
        R = d.bit_length() - 1
        best = max(best, R); dd = max(dd, best - R)
        if t >= 200 and found is None and R >= WIN:
            key = ((d >> (R - WIN)) & ((1 << WIN) - 1), cls(al, R, t))
            if key in seen:
                t1, R1 = seen[key]; found = (t - t1, R - R1)
            else:
                seen[key] = (t, R)
        x = (x ^ ((x << 1) | (x << 2) | 3)) & mask
    speeds.append(R / T); dds.append(dd)
    if found:
        periodic.append(found)
    else:
        aperiodic += 1
print('%s clean starts, %d alignments, %d ticks: speed min %.3f max %.3f; largest drawdown %d' % (
    name, len(aligns), T, min(speeds), max(speeds), max(dds)))
print('   window recurrence (periodic wake) at %d alignments, none at %d' % (len(periodic), aperiodic))
if periodic:
    per = sorted(set(periodic))[:8]
    print('   (period, front advance) pairs found: %s; speeds %s' % (per, sorted(set('%d/%d' % (b, a) for a, b in per))))
