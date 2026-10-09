#!/usr/bin/env python3
"""rule30_cloud_mahler_horizon.py: MC, a counting form for Mahler's 3/2 map (exact survival horizons, g < 2^LOG).

RUN-ON:     cpu (Python 3 standard library; exact fractions)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_mahler_horizon.py [LOG=20]
COST:       about a minute at LOG = 20.

Why. Local's MD (`rule30_mahler_carry_dial.py`, chat L457, L458) measured the survival horizons H(g) of Mahler's
question, the third corner the owner asked about: the largest N such that some xi in [g, g + 1) keeps
frac(xi (3/2)^n) < 1/2 for n = 0 .. N - 1. The survivors are one interval of x_n = xi (3/2)^n inside [g_n, g_n + 1/2),
with g_(n+1) = ceil(3 g_n / 2) (GC616). Heuristic (Cloud, CL091): if the fractional parts behave like coins, the
survivor set has measure about 2^-h, spread over one interval of length at most (1/2)(2/3)^h, so the number of
g <= G with H(g) >= h falls like G (3/4)^h and the record horizon is about log2 G / log2(4/3).

PREDICTIONS, pushed in CHAT-LEDGER.md CL091 (commit ef97296, 2026-10-09 18:39 BST) before the run, g < 2^20:
  MC-C (control): H(1 .. 5) = 4, 3, 2, 12, 6 and max H = 29 for g <= 4096, as MD measured.
  MC-P1 (0.6): the tail ratio N(h+1)/N(h), averaged over the last ten h with N(h+1) >= 100, lies in [0.70, 0.80].
  MC-P2 (0.5): the maximum H over g < 2^20 lies in [42, 54] (the 3/4 law says 48).
  Counterfactual: a ratio near 1/2 would mean surviving intervals are usually much shorter than their maximum.

OUTCOME, 2026-10-09 (g < 2^20, under a minute): MC-C PASS. MC-P1 HELD: the mean tail ratio is 0.7394. The ratio is
  within 0.01 of 0.75 at every h from 5 to 24, and noisier beyond (0.69 to 0.79 for h = 25 .. 38, as N(h) falls
  below 2,000). MC-P2 HELD: the maximum H is 47.
  Post hoc: for small h, N(h) + 1 is an exact 3-smooth multiple of a power of 2 (2^20, 3 * 2^18, 5 * 2^17, 2^19,
  3 * 2^17, 9 * 2^15, 27 * 2^13, ...), since whether H(g) >= h depends on few low bits of g at small h. That is the
  Mahler twin of the free bits paying exactly in Collatz (COLLATZ-PRIZE.md section 1) and in Rule 30. The 3/4 decay
  is the coin's price past them. A count below one for every G would exclude Z-numbers. As in the other two
  corners, the open part is a single case, not the set.
"""
import sys
from fractions import Fraction as F
from collections import Counter

def H(g):
    a, b, gn, n = F(g), F(g) + F(1, 2), g, 1
    while True:
        G = (3 * gn + 1) // 2                     # ceil(3 gn / 2)
        a, b = max(F(3, 2) * a, F(G)), min(F(3, 2) * b, G + F(1, 2))
        if a >= b:
            return n
        gn, n = G, n + 1

LOG = int(sys.argv[1]) if len(sys.argv) > 1 else 20
print('control H(1..5) =', [H(g) for g in range(1, 6)], 'max H for g <= 4096 =', max(H(g) for g in range(1, 4097)))
c = Counter(H(g) for g in range(1, 1 << LOG))
N, tot = {}, 0
for h in sorted(c, reverse=True):
    tot += c[h]; N[h] = tot                      # N[h] = #{g : H(g) >= h}
hs = sorted(N)
print('g < 2^%d: max H = %d' % (LOG, hs[-1]))
for h in hs:
    if h + 1 in N:
        print('  h = %2d  N(h) = %8d  N(h+1)/N(h) = %.4f' % (h, N[h], N[h + 1] / N[h]))
tail = [N[h + 1] / N[h] for h in hs if h + 1 in N and N[h + 1] >= 100]
print('mean tail ratio over N(h+1) >= 100: %.4f (%d ratios)' % (sum(tail[-10:]) / len(tail[-10:]), len(tail[-10:])))
