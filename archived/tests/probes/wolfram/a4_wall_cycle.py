#!/usr/bin/env python3
"""L1443 (Local, 2026-11-03): P-k. The 11/81 wall by hand against the 2/9 wall on 1010000. Run:
python3 tests/probes/wolfram/a4_wall_cycle.py DATA63.json T0 SLOWPAT FASTPAT
Prints, for one cycle of each settled wall (81 ticks slow, 63 fast, from T0): the front's moves dF, the deviation from the
2/9 line G(t) = F(t) - F(T0) + 2 (t - T0) / 9, and the mismatch D = X xor background in the co-moving window F-3 .. F+36
('#' = difference, '.' = agreement). Then the longest common runs of the slow move sequence against every rotation of the
fast cycle.
"""
import json
import sys

import numpy as np

data = json.load(open(sys.argv[1])); T0 = int(sys.argv[2]); SP = int(sys.argv[3], 0); FP = int(sys.argv[4], 0)
orb = [tuple(o) for o in data['orb']]; q = len(orb); N = data['N']; r0, s0 = data['r'], data['s']
E = lambda x, t: orb[(t + s0) % q][((t - x) + r0) % N]
TM = T0 + 82; lo = -2 * TM - 10; hi = TM + 22; c = -lo


def run(pat, L):
    row = np.array([E(x, 0) for x in range(lo, hi)], dtype=np.uint8); bg = row.copy()
    for i in range(12):
        row[c + i] ^= (pat >> i) & 1
    Fs = []; pics = []
    for t in range(1, T0 + L + 1):
        n = np.zeros_like(row); n[1:-1] = row[:-2] ^ (row[1:-1] | row[2:]); row = n
        m = np.zeros_like(bg); m[1:-1] = bg[:-2] ^ (bg[1:-1] | bg[2:]); bg = m
        if t >= T0:
            D = row ^ bg; F = int(np.flatnonzero(D).min())
            Fs.append(F - c); pics.append(''.join('#' if v else '.' for v in D[F - 3: F + 37]))
    return Fs, pics


out = {}
for name, pat, L in (('slow', SP, 81), ('fast', FP, 63)):
    Fs, pics = run(pat, L)
    dF = [Fs[i + 1] - Fs[i] for i in range(L)]
    G = [Fs[i] - Fs[0] + 2 * i / 9 for i in range(L + 1)]
    out[name] = dF
    print('%s wall, pattern %d, t = %d .. %d: net %d cells in %d ticks' % (name, pat, T0, T0 + L, Fs[-1] - Fs[0], L))
    print('  moves dF: %s' % ' '.join('%+d' % d for d in dF))
    print('  deviation from the 2/9 line G: %s' % ' '.join('%.1f' % g for g in G[::3]))
    print('  co-moving mismatch, every 3rd tick (window F-3 .. F+36; the front is column 4):')
    for i in range(0, L + 1, 3):
        print('    t=%d  %s' % (T0 + i, pics[i]))
sl, fa = out['slow'], out['fast']
best = []
for rot in range(63):
    f = (fa[rot:] + fa[:rot]) * 3
    # longest common run between sl and f, aligned at the same index
    run_ = 0; mx = 0; at = None
    for i in range(81):
        run_ = run_ + 1 if sl[i] == f[i] else 0
        if run_ > mx:
            mx = run_; at = i - run_ + 1
    best.append((mx, rot, at))
best.sort(reverse=True)
print('longest aligned common runs of slow moves with a rotated fast cycle (length, rotation, start): %s' % best[:5])
# control: the same statistic against a random +-1/0 sequence with the slow sequence's move frequencies
rng = np.random.default_rng(1443); ctl = []
for _ in range(200):
    f = list(rng.permutation(sl)) * 2; mx = 0; run_ = 0
    for i in range(81):
        run_ = run_ + 1 if sl[i] == f[i] else 0; mx = max(mx, run_)
    ctl.append(mx)
print('control: same statistic against 200 shuffles of the slow moves: max %d, 95%% %d' % (max(ctl), int(np.percentile(ctl, 95))))
print('A4_WALL_CYCLE_DONE')
