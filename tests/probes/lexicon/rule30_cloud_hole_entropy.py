#!/usr/bin/env python3
"""rule30_cloud_hole_entropy.py: HE, the one-hole channel driven by random right halves (Local's offer (1), 21:17).

RUN-ON:     cpu, one core (Python 3 standard library); about a minute
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_hole_entropy.py [SAMPLES=2000] [HOLES=400] [SEED=1]

Why. Local's OH and OHC (rule30_one_hole_widths.py) certify upper bounds on the true one-sided growth of the hole
language for the walls 0 1^(p - 1): at most 1.543759, 1.652210 and 1.742260 words per hole for p = 5, 7 and 9
(GC859), and exactly 2 words of every length for odd p >= 11. Whether the true entropy at p = 5, 7, 9 is zero is
open. Local's offer names two routes: a lower-bound construction (exponentially many words realised by actual right
halves), or a lock over several periods in the style of GC850. This probe does not decide it. It asks which route
the typical right half points to: under iid fair right halves, does the hole word settle into a periodic pattern (a
lock, pointing to zero), or does randomness keep reaching column 1 at a positive rate (pointing to a construction)?
The period-2 wall is the precedent: there column 1 locks onto the wheel and is kicked at a positive rate (§8.43).

Model, as OHD's (rule30_one_hole_direct.c): Rule 30 on the half-line x1, x2, ... with the wall as left boundary,
white at t = 0 mod p and black otherwise; the hole bit is x1 at t = 0 mod p, read before that step. An initial right
half on W = T + 2 cells, T = (HOLES - 1) p, cells beyond white; no cell beyond W can reach x1 by time T, so every
hole bit is the true system's.

Record searched: "one.hole" (headings), wall + front + (speed|moves|grows): the hits are OH, OHC, OHD (the header
of rule30_one_hole_widths.py), G11.2, G15 .. G20, entry 38 and §8.60's far-end item; none measures the hole word
under random right halves.

PREDICTIONS, written 2026-10-09 21:40 BST, before any run of this script.
  HE-C1 (control, must hold): p = 11: in every sample, every hole bit after the first is 0 (OH: one macro step ends
         with x1 = 0 for odd p >= 11).
  HE-C2 (control, must hold): p = 5: no sampled hole word contains 10000 (OHD's true forbidden word), and the
         sampled numbers of distinct words of 5, 6 and 7 holes are at most the true 31, 60 and 108 (OHD).
  HE-P1 (0.6): for p = 5, 7 and 9, the late hole word is not eventually periodic in most samples: fewer than half
         the samples have their last 200 hole bits periodic with a period of at most 64.
  HE-P2 (0.55): for each of p = 5, 7, 9, the late conditional entropy h_12 (of a hole bit given the 12 before it,
         from holes 150 onward) lies between 0.05 and 0.5 bits.
  HE-P3 (0.5): h_12 increases with p: p = 5 < p = 7 < p = 9, the order of the certified upper bounds.
  HE-U, the unexpected check (0.5): the late density of 1s at the holes is below 0.4 for all three periods.
  Counterfactual. If HE-P1 fails, the typical right half locks, and the zero-entropy route (a lock over several
  periods) is the one to try first; a construction would then need atypical right halves. If HE-P1 and HE-P2 hold,
  the measure entropy of the typical right half is positive as measured, which points to a construction from typical
  right halves. Neither outcome is a proof: a positive measured rate is not a certified lower bound.
"""
import math
import random
import sys

SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
HOLES = int(sys.argv[2]) if len(sys.argv) > 2 else 400
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 1
LATE = 150
M = 12


def hole_word(p, holes, rng):
    T = (holes - 1) * p
    W = T + 2
    mask = (1 << W) - 1
    x = rng.getrandbits(W - 1)                          # cells x1 .. x(W-1) random, x(W) white; bit j is x(j+1)
    out = []
    for t in range(T + 1):
        if t % p == 0:
            out.append(x & 1)
            if t == T:
                break
        wall = 0 if t % p == 0 else 1
        x = (((x << 1) | wall) & mask) ^ (x | (x >> 1))
    return out


def least_period(bits, qmax=64):
    for q in range(1, qmax + 1):
        if all(bits[i] == bits[i + q] for i in range(len(bits) - q)):
            return q
    return None


def block_entropy(words, m, start):
    counts = {}
    n = 0
    for w in words:
        for i in range(start, len(w) - m + 1):
            k = tuple(w[i:i + m])
            counts[k] = counts.get(k, 0) + 1
            n += 1
    return -sum(c / n * math.log2(c / n) for c in counts.values()) if n else 0.0


def main():
    rng = random.Random(SEED)
    res = {}
    for p in (5, 7, 9, 11):
        words = [hole_word(p, HOLES, rng) for _ in range(SAMPLES)]
        periodic = [least_period(w[-200:]) for w in words]
        nper = sum(1 for q in periodic if q is not None)
        dens = sum(sum(w[LATE:]) for w in words) / (SAMPLES * (HOLES - LATE))
        H = [block_entropy(words, m, LATE) for m in range(0, M + 2)]
        h = [H[m + 1] - H[m] for m in range(M + 1)]
        res[p] = (words, nper, dens, h, periodic)
        qs = {}
        for q in periodic:
            qs[q] = qs.get(q, 0) + 1
        print('p = %2d: late periodic (q <= 64) in %d of %d samples; periods %s' % (
            p, nper, SAMPLES, sorted(qs.items(), key=lambda kv: -kv[1])[:6]), flush=True)
        print('        late density of 1s %.4f; conditional entropies h_0 .. h_%d: %s' % (
            dens, M, ' '.join('%.3f' % v for v in h)), flush=True)
    w11 = res[11][0]
    c1 = all(all(b == 0 for b in w[1:]) for w in w11)
    print('HE-C1 (p = 11, every hole after the first is 0): %s' % ('PASS' if c1 else 'FAIL'))
    w5 = res[5][0]
    bad = sum(1 for w in w5 if '10000' in ''.join(map(str, w)))
    dist = [len({tuple(w[:n]) for w in w5}) for n in (5, 6, 7)]
    c2 = bad == 0 and dist[0] <= 31 and dist[1] <= 60 and dist[2] <= 108
    print('HE-C2 (p = 5): words containing 10000: %d; distinct words of 5, 6, 7 holes: %s (true 31, 60, 108): %s'
          % (bad, dist, 'PASS' if c2 else 'FAIL'))
    p1 = all(res[p][1] < SAMPLES / 2 for p in (5, 7, 9))
    print('HE-P1 (most late words not periodic, p = 5, 7, 9): %s' % ('HELD' if p1 else 'REFUTED'))
    h12 = {p: res[p][3][M] for p in (5, 7, 9)}
    p2 = all(0.05 <= h12[p] <= 0.5 for p in h12)
    print('HE-P2 (0.05 <= h_12 <= 0.5): %s %s' % ({p: round(v, 4) for p, v in h12.items()},
                                                 'HELD' if p2 else 'REFUTED'))
    p3 = h12[5] < h12[7] < h12[9]
    print('HE-P3 (h_12 increases with p): %s' % ('HELD' if p3 else 'REFUTED'))
    u = all(res[p][2] < 0.4 for p in (5, 7, 9))
    print('HE-U (late density below 0.4): %s %s' % ({p: round(res[p][2], 4) for p in (5, 7, 9)},
                                                   'HELD' if u else 'REFUTED'))


if __name__ == '__main__':
    main()
