#!/usr/bin/env python3
"""rule30_cloud_ruler_kicks.py: KR, does the right edge's ruler send a wave back that kicks the wheel?

RUN-ON:     cpu (Python 3 standard library; big-integer rows)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_ruler_kicks.py [N=8192] [SEEDS=64]
COST:       expected a few minutes.

Why (the owner, 2026-10-09, after CL095). The left front separates the ordered band from the random core. At the right
edge, the edge ruler (RULE30-PRIZE.md, "Two fronts, one rule") is an ordered strip about 2.5 log2 t cells wide that
steps at every power of 2. The owner asks: "does the ruler provide an interference shockwave that travels back
down/through the row and could this be the cause of the kicks?"

Set-up. The wheel and its kicks live in the period-2 world: column 0 clamped to 0101..., the right half driven by it.
A finite right half has a right edge with its own ruler. A right half that is random out to beyond the light cone has
no edge the wheel could hear. The test is counterfactual: three worlds share the same random cells 1 .. W.
  A: those cells, then white for ever. There is a right edge, and its news can reach the wheel.
  B: those cells, then random for ever (no edge within reach in the run).
  C: as B, but sites 13 .. 76 are refilled with fresh coin flips every step (the record's N1: a coin interior).
The wheel runs clean at row t when column 1 over rows t .. t + 55 is a rotation of U
(as in rule30_cloud_velocimetry.py).
A kick is a row where a clean run ends.

Reasoning before the run. Rule 30 sends news leftwards only through the OR, at about 0.246 cells a row on random
rows (§8.66), so the edge's news reaches column 1 late and scrambled. PIV (CL095) found no correlation that travels
left. The wide-random world of CL095 kicked the wheel with no edge in reach at all. So the edge is not needed for
kicks. The question is whether it adds any.

PREDICTIONS, written 2026-10-09 20:06 BST, before any run of this script (N = 8192 rows, 64 seeds per world,
W = 12 for A).
  KR-C (control, exact): A and B agree on column 1 for every row t < W, for W = 12, 64 and 128 (the light cone).
  KR-P1 (0.5): the edge's first news reaches column 1 at about the leftward speed. Over 32 seeds, the mean of
        W / t1 (t1 the first row where A and B differ in column 1) lies in [0.2, 0.3] for W = 64 and W = 128.
  KR-P2 (0.6): the edge adds no kicks. Over rows 2048 .. N - 57, A's kick rate and clean fraction differ from B's by
        less than 3 standard errors, taken across seeds.
  KR-P3 (0.7): no ruler rhythm. In A, the kick rate in 8 bins of frac(log2 t) over rows 256 .. N - 57 differs from
        B's in the same bins by less than 3 standard errors in every bin.
  KR-U, the unexpected check (0.5): a real random interior kicks like coin flips. B's clean fraction is within 0.05
        of C's.
  Counterfactual. A kicking more than B, or a dyadic rhythm in A's kicks, would make the ruler's back-travelling news
  a real cause of kicks, and the owner's shockwave would be measurable.
"""
import random
import sys
from math import log2, sqrt

N = int(sys.argv[1]) if len(sys.argv) > 1 else 8192
SEEDS = int(sys.argv[2]) if len(sys.argv) > 2 else 64
U = '00010011010001001101000100110100010011010001001101001101'
ROT = {sum(int(U[(p + j) % 56]) << j for j in range(56)): p for p in range(56)}


def column1(cells, n, world, rnd=None):
    """Column 1 for n rows. cells: the initial row (bit k = site k, sites >= 1); site 0 is clamped to t mod 2."""
    row = cells
    band = ((1 << 64) - 1) << 13
    out = []
    for t in range(n):
        if world == 'C':
            row = (row & ~band) | (rnd.getrandbits(64) << 13)
        row = (row & ~1) | (t % 2)
        out.append((row >> 1) & 1)
        row = (row << 1) ^ (row | (row >> 1))
    return out


def clean_flags(c1):
    n = len(c1) - 56
    win = sum(c1[j] << j for j in range(56))
    flags = []
    for t in range(n):
        if t:
            win = (win >> 1) | (c1[t + 55] << 55)
        flags.append(win in ROT)
    return flags


def stats(flags, lo, hi):
    f = sum(flags[lo:hi]) / (hi - lo)
    kicks = sum(1 for t in range(lo, hi) if flags[t - 1] and not flags[t])
    return f, kicks / (hi - lo)


def kick_bins(flags, lo, hi):
    cnt, rows = [0] * 8, [0] * 8
    for t in range(lo, hi):
        b = int(8 * (log2(t) % 1))
        rows[b] += 1
        cnt[b] += flags[t - 1] and not flags[t]
    return [c / r for c, r in zip(cnt, rows)]


def mean_se(xs):
    m = sum(xs) / len(xs)
    v = sum((x - m) ** 2 for x in xs) / (len(xs) - 1)
    return m, sqrt(v / len(xs))


def main():
    for W in (12, 64, 128):
        ok, speeds = 0, []
        for seed in range(32):
            rnd = random.Random(7000 + seed)
            base = rnd.getrandbits(W) << 1
            beyond = rnd.getrandbits(2 * 2048 + 64) << (W + 1)
            n = 2048
            a = column1(base, n, 'A')
            b = column1(base | beyond, n, 'B')
            t1 = next((t for t in range(n) if a[t] != b[t]), None)
            ok += all(a[t] == b[t] for t in range(min(W, n)))
            if t1:
                speeds.append(W / t1)
        m, se = mean_se(speeds) if len(speeds) > 1 else (float('nan'), 0)
        print('KR-C/P1: W = %3d: light cone held in %d of 32; first difference found in %d; mean W/t1 = %.3f (se %.3f)'
              % (W, ok, len(speeds), m, se))
    W = 12
    res = {'A': [], 'B': [], 'C': []}
    bins = {'A': [], 'B': []}
    for seed in range(SEEDS):
        rnd = random.Random(9000 + seed)
        base = rnd.getrandbits(W) << 1
        beyond = rnd.getrandbits(2 * N + 128) << (W + 1)
        for world in 'ABC':
            cells = base if world == 'A' else base | beyond
            c1 = column1(cells, N, world, random.Random(5000 + seed))
            fl = clean_flags(c1)
            res[world].append(stats(fl, 2048, N - 57))
            if world in bins:
                bins[world].append(kick_bins(fl, 256, N - 57))
    for world in 'ABC':
        f = mean_se([x[0] for x in res[world]])
        k = mean_se([x[1] for x in res[world]])
        print('world %s: clean fraction %.4f (se %.4f), kicks per row %.5f (se %.5f)' % (world, f[0], f[1], k[0], k[1]))
    for name, i in (('clean fraction', 0), ('kick rate', 1)):
        d = [a[i] - b[i] for a, b in zip(res['A'], res['B'])]
        m, se = mean_se(d)
        print('KR-P2 %s, A - B: %.5f (se %.5f, %.1f se)' % (name, m, se, m / se if se else 0))
    worst = 0
    for b in range(8):
        d = [x[b] - y[b] for x, y in zip(bins['A'], bins['B'])]
        m, se = mean_se(d)
        z = m / se if se else 0
        worst = max(worst, abs(z))
        print('KR-P3 bin %d: A %.5f, B %.5f, A - B %+.1f se' % (b, mean_se([x[b] for x in bins['A']])[0],
                                                              mean_se([y[b] for y in bins['B']])[0], z))
    print('KR-P3 largest |A - B| over bins: %.1f se' % worst)
    fb = mean_se([x[0] for x in res['B']])[0]
    fc = mean_se([x[0] for x in res['C']])[0]
    print('KR-U: clean fraction B %.4f, C %.4f, difference %.4f' % (fb, fc, fb - fc))


if __name__ == '__main__':
    main()
