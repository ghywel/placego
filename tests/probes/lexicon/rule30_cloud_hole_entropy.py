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
OUTCOME of the first run, 2026-10-09 21:41 BST (SAMPLES 2000, HOLES 400, SEED 1; about a minute, one core, run at
commit 9c670d1): HE-C1 PASS, HE-C2 PASS, HE-P1 REFUTED, HE-P2 REFUTED, HE-P3 HELD, HE-U REFUTED.
  - p = 5 locks. In 1,262 of 2,000 samples the last 200 hole bits are periodic: period 2 in 1,146, period 4 in 116.
    Its h_0 .. h_12 fall steadily, from 1.000 and 0.530 to 0.106, and are still falling at m = 12.
  - p = 7 and p = 9 do not lock: 2 and 0 samples are periodic. h_12 = 0.364 and 0.556, falling slowly (0.383,
    0.371, 0.364 and 0.574, 0.566, 0.556 at m = 10, 11, 12). The late densities of 1s are 0.181 and 0.237.
  - p = 11: every hole after the first is 0 (C1). For p = 5, no sample shows 10000, and the sampled distinct words of
    5, 6 and 7 holes number 31, 58 and 99, against the true 31, 60 and 108 (C2).
  - HE-P1 fails only at p = 5. HE-P2 fails only at p = 9 (0.556 > 0.5). HE-U fails only at p = 5, whose locked word
    alternates and so has density 1/2.
  - Reading. The three periods part ways. At p = 5 the typical right half locks onto a short period, which points the
    zero-entropy question towards a lock argument, though atypical right halves could still carry positive
    topological entropy. At p = 7 and 9 randomness keeps reaching column 1 at a measured rate of about a third and
    a half a bit per hole. A measured rate is not a certified lower bound.
EXTENSION HE2 (registered 2026-10-09 21:44 BST, before running; COMMAND: ... rule30_cloud_hole_entropy.py ext
  [SAMPLES=500] [SEED=2]): p = 5 to 1,600 holes; p = 7 and 9 to 1,000 holes. Exact as before (width T + 2).
  HE2-P1 (0.6): p = 5: at least 95% of samples are locked by hole 1,600 (their last 400 hole bits periodic with
         period at most 4), and the unlocked fraction falls roughly geometrically with the hole index.
  HE2-P2 (0.6): p = 7 and 9: h_12 over holes 500 .. 1,000 is within 0.05 of the first run's 0.364 and 0.556, so the
         late rate is stationary, not decaying.
  HE2-P3 (0.5): p = 5: more than 90% of locked samples lock with period 2.
  HE2-U, the unexpected check (0.5): at p = 5, column 1 is time-periodic with period 10 (all times, not just holes)
         over the last 50 holes of every period-2 locked sample.
  Counterfactual. If HE2-P1 fails with a heavy tail of unlocked samples, p = 5 has two regimes, and its lock is not
  the typical fate. If HE2-P2 fails with h_12 decaying, p = 7 and 9 may lock late, and the first run saw a
  transient.
"""
import math
import random
import sys

EXT = len(sys.argv) > 1 and sys.argv[1] == 'ext'
_a = sys.argv[2:] if EXT else sys.argv[1:]
SAMPLES = int(_a[0]) if len(_a) > 0 else (500 if EXT else 2000)
HOLES = int(_a[1]) if len(_a) > 1 and not EXT else 400
SEED = int(_a[1 if EXT else 2]) if len(_a) > (1 if EXT else 2) else (2 if EXT else 1)
LATE = 150
M = 12


def hole_word(p, holes, rng, col1=None):
    T = (holes - 1) * p
    W = T + 2
    mask = (1 << W) - 1
    x = rng.getrandbits(W - 1)                          # cells x1 .. x(W-1) random, x(W) white; bit j is x(j+1)
    out = []
    for t in range(T + 1):
        if col1 is not None:
            col1.append(x & 1)
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


def lock_index(w, qmax=4):
    """The first hole from which w is periodic with some period q <= qmax to its end, with that q."""
    best = None
    for q in range(1, qmax + 1):
        k = len(w) - q
        while k > 0 and w[k - 1] == w[k - 1 + q]:
            k -= 1
        if best is None or k < best[0]:
            best = (k, q)
    return best


def ext():
    rng = random.Random(SEED)
    print('HE2: SAMPLES %d, SEED %d' % (SAMPLES, SEED), flush=True)
    # p = 5
    holes = 1600
    locks, per2, col_ok, col_bad = [], 0, 0, 0
    for _ in range(SAMPLES):
        col = []
        w = hole_word(5, holes, rng, col)
        k, q = lock_index(w)
        locked = k <= holes - 400
        locks.append(k if locked else None)
        if locked and q == 2:
            per2 += 1
            tail = col[-50 * 5:]
            if all(tail[i] == tail[i + 10] for i in range(len(tail) - 10)):
                col_ok += 1
            else:
                col_bad += 1
    nl = sum(1 for k in locks if k is not None)
    print('p = 5: locked (period <= 4 over the last 400 holes) in %d of %d; period 2 in %d' % (nl, SAMPLES, per2))
    for h in (50, 100, 200, 400, 800, 1200):
        print('  unlocked fraction at hole %4d: %.4f' % (h, sum(1 for k in locks if k is None or k > h) / SAMPLES))
    print('HE2-P1 (>= 95%% locked): %s' % ('HELD' if nl >= 0.95 * SAMPLES else 'REFUTED'))
    print('HE2-P3 (> 90%% of locked have period 2): %s' % ('HELD' if nl and per2 > 0.9 * nl else 'REFUTED'))
    print('HE2-U (column 1 has period 10 over the last 50 holes): %d of %d period-2 samples: %s' % (
        col_ok, per2, 'HELD' if col_bad == 0 and per2 else 'REFUTED'))
    res = {}
    for p, ref in ((7, 0.364), (9, 0.556)):
        words = [hole_word(p, 1000, rng) for _ in range(SAMPLES)]
        out = []
        for start, stop in ((150, 400), (500, 1000)):
            cut = [w[:stop] for w in words]
            H = [block_entropy(cut, m, start) for m in (12, 13)]
            out.append(H[1] - H[0])
        nper = sum(1 for w in words if least_period(w[-200:]) is not None)
        res[p] = (out, ref)
        print('p = %d: h_12 over holes 150 .. 400: %.4f; over 500 .. 1000: %.4f; late periodic %d of %d' % (
            p, out[0], out[1], nper, SAMPLES), flush=True)
    ok = all(abs(res[p][0][1] - res[p][1]) <= 0.05 for p in res)
    print('HE2-P2 (late h_12 within 0.05 of 0.364, 0.556): %s' % ('HELD' if ok else 'REFUTED'))


if __name__ == '__main__':
    ext() if EXT else main()
