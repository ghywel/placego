#!/usr/bin/env python3
"""L1316 T41 (Local, 2026-11-02): the boundary layer behind a periodic-wake front: decoupling gap, riding particles,
linearity. reports/rule30-genealogy.md section 44 (predictions written first).
Run: python3 tests/probes/layer_linear.py PHASE census|pairs [GMAX] [NPAIRS]   (PHASE: P1024 or 480)

Clean start: the phase's digits directly below the black edge, evolved by Phi(x) = x ^ ((x << 1) | (x << 2) | 3); its
front R(t) is the deepest 1 of x(t) ^ E(t). A flip at gap g at tick tf changes bit R(tf) - g; the disturbance
delta(t) = (flipped run) ^ (clean run) has its deepest cell m(t) and gap R(t) - m(t). The flip changes the main front
exactly when that gap reaches 0 (section 44.1).

census: flips at every g = 1 .. GMAX at the eight comoving phases tf = 5 PER + j PER / 8, each run NP = 10 wake periods.
  Per phase j: gaps whose flip ever changes the front (P41a), and how the rest end: riding (the pair (gap, the 64
  disturbance bits above m) recurs after one, two or four wake periods at the last checkpoints; P41b named one or
  two), falling behind (the gap grows over the last three checkpoints), or other. The opening table gives the least
  period of the window above the clean front, per window width (a period-doubling band, found in the smoke test). For j = 0 also the tangent evolution (quadratic term dropped) and
  the first tick its deepest cell leaves the true one (P41d).
pairs: NPAIRS random pairs of riding gaps from the j = 0 census, flipped together; the interaction
  I = Delta_AB ^ Delta_A ^ Delta_B (section 44.1, G12.2's four-case test). Reported: pairs whose run changes the front,
  pairs with I = 0 at the end, and the least over the run of gap(I) - min(gap(A), gap(B)) (P41c).
"""
import os
import sys
import random
import runpy
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
name = sys.argv[1]; mode = sys.argv[2]
GMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 400
NPAIRS = int(sys.argv[4]) if len(sys.argv) > 4 else 200
p, cols, _ = g['phases']()[name]; NC = len(cols)
PER, ADV = {'P1024': (208, 272), '480': (288, 480)}[name]
NP = 10; T0 = 5 * PER; T = T0 + PER + NP * PER
depth = 2 * T + 16; mask = (1 << depth) - 1; M64 = (1 << 64) - 1
rng = random.Random(41)
if name == 'P1024':
    th = rng.randrange(p); col0 = cols[0]
    def E_bit(n, t):
        return (col0 >> ((th + t + 195 * n) % p)) & 1
    def cls(R, t):
        return (th + t + 195 * R) % p
    align = 'theta %d' % th
else:
    a0, q0 = rng.randrange(NC), rng.randrange(p)
    def E_bit(n, t):
        return (cols[(n + a0) % NC] >> ((t + q0) % p)) & 1
    def cls(R, t):
        return ((R + a0) % NC, (t + q0) % p)
    align = 'a %d q %d' % (a0, q0)
rows = {}
def erow(t):
    k = t % p
    if k not in rows:
        rows[k] = sum(E_bit(n, t) << n for n in range(depth))
    return rows[k]
def phi(x):
    return (x ^ ((x << 1) | (x << 2) | 3)) & mask

xs = [erow(0)]
for t in range(T):
    xs.append(phi(xs[-1]))
R = [(xs[t] ^ erow(t)).bit_length() - 1 for t in range(T + 1)]
def key(t, W):
    d = xs[t] ^ erow(t)
    return ((d >> (R[t] - W)) & ((1 << W) - 1), cls(R[t], t))
print('%s clean start (%s), %d ticks. Least period (ticks, front advance) of the W-cell window above the front, '
      'searched from tick t1:' % (name, align, T), flush=True)
for W in (32, 64, 128, 192, 256, 320):
    res = []
    for t1 in (400, 800, T0, 1600, 2400):
        found = next(((P, R[t1 + P] - R[t1]) for P in range(1, T - t1 + 1) if key(t1, W) == key(t1 + P, W)), None)
        res.append('t1=%d: %s' % (t1, found))
    print('   W=%3d  %s' % (W, '; '.join(res)), flush=True)


def run(tf, flips, ticks, tangent=False):
    """Evolve the clean row at tf with the given gaps flipped. Returns per tick the disturbance (as an int)."""
    y = xs[tf]
    for gg in flips:
        y ^= 1 << (R[tf] - gg)
    dl = y ^ xs[tf]; first_split = None
    out = [y ^ xs[tf]]
    for t in range(tf, tf + ticks):
        if tangent:
            nX = ~xs[t] & mask
            dl = (dl ^ ((dl << 1) & (nX << 2)) ^ ((dl << 2) & (nX << 1))) & mask
        y = phi(y)
        d = y ^ xs[t + 1]; out.append(d)
        if tangent and first_split is None and dl.bit_length() != d.bit_length():
            first_split = t + 1 - tf
    return out, first_split


def gap(d, t):
    return R[t] - (d.bit_length() - 1)


def classify(tf, ds):
    gaps = [gap(d, tf + i) for i, d in enumerate(ds)]
    front = next((i for i, x in enumerate(gaps) if x <= 0), None)
    if front is not None:
        return 'front', front, gaps[-1]
    ck = []
    for k in range(NP - 5, NP + 1):
        i = k * PER; d = ds[i]; m = d.bit_length() - 1
        ck.append((gaps[i], (d >> max(m - 63, 0)) & M64))
    if ck[-1] == ck[-2]:
        return 'ride1', None, gaps[-1]
    if ck[-1] == ck[-3]:
        return 'ride2', None, gaps[-1]
    if ck[-1] == ck[-5]:
        return 'ride4', None, gaps[-1]
    g3 = [c[0] for c in ck[-3:]]
    if g3[0] < g3[1] < g3[2]:
        return 'behind', None, gaps[-1]
    return 'other', None, gaps[-1]


if mode == 'census':
    riding0 = []
    for j in range(8):
        tf = T0 + j * PER // 8
        kinds = Counter(); fronts = []; ridegaps = Counter(); splits = []; others = []
        for gg in range(1, GMAX + 1):
            ds, split = run(tf, [gg], NP * PER, tangent=(j == 0))
            kind, ft, gend = classify(tf, ds)
            kinds[kind] += 1
            if kind == 'front':
                fronts.append((gg, ft))
            elif kind.startswith('ride'):
                ridegaps[gend] += 1
                if j == 0:
                    riding0.append(gg)
            elif kind == 'other':
                others.append((gg, gend))
            if j == 0:
                splits.append(split)
        print('j=%d (tf=%d): %s' % (j, tf, dict(kinds)), flush=True)
        print('   gaps changing the front (gap, tick): %s' % fronts[:40], flush=True)
        print('   final gaps of riding flips (gap: count): %s' % dict(sorted(ridegaps.items())), flush=True)
        if others:
            print('   other (gap, final gap): %s' % others[:20], flush=True)
        if j == 0:
            within = sum(1 for s in splits if s is not None and s <= PER)
            never = sum(1 for s in splits if s is None)
            print('   tangent map: deepest cell leaves the true one within one period at %d of %d gaps; never at %d; '
                  'first split ticks (first 30 gaps): %s' % (within, GMAX, never, splits[:30]), flush=True)
    print('riding gaps at j=0: %s' % riding0, flush=True)

elif mode == 'pairs':
    tf = T0
    riding = []
    for gg in range(1, GMAX + 1):
        ds, _ = run(tf, [gg], NP * PER)
        if classify(tf, ds)[0].startswith('ride'):
            riding.append(gg)
    print('riding gaps at j=0: %d' % len(riding), flush=True)
    prng = random.Random(4141)
    res = Counter(); worst = []; zero = 0; frontpairs = []
    for it in range(NPAIRS):
        a, b = sorted(prng.sample(riding, 2))
        dA, _ = run(tf, [a], NP * PER); dB, _ = run(tf, [b], NP * PER); dAB, _ = run(tf, [a, b], NP * PER)
        gAB = [gap(d, tf + i) for i, d in enumerate(dAB)]
        if min(gAB) <= 0:
            frontpairs.append((a, b)); res['front'] += 1
        least = None
        for i in range(len(dAB)):
            I = dAB[i] ^ dA[i] ^ dB[i]
            if I:
                s = gap(I, tf + i) - min(gap(dA[i], tf + i), gap(dB[i], tf + i))
                least = s if least is None else min(least, s)
        if not (dAB[-1] ^ dA[-1] ^ dB[-1]):
            zero += 1
        if least is None:
            res['I zero throughout'] += 1
        elif least >= 0:
            res['I never deeper than the deeper single response'] += 1
        else:
            res['I deeper than both at some tick'] += 1; worst.append((least, a, b))
    print('%d pairs of riding flips at tf=%d, %d ticks: %s; I = 0 at the end: %d' % (NPAIRS, tf, NP * PER, dict(res), zero),
          flush=True)
    print('   pairs changing the front: %s' % frontpairs[:20], flush=True)
    print('   deepest interactions (least gap(I) - min single gap, a, b): %s' % sorted(worst)[:12], flush=True)
