#!/usr/bin/env python3
"""mahler_swarm_tests.py: the first tests of the swarm's survivors (MAHLER.md section 2; the swarm of 2026-10-14, L711).

The swarm (four lanes of solver plus blind skeptic, then a judge; self-checks only) ranked two cheap tests first.
- S1, the rung-3 straggler count (judge's item 1). Rung 3 is the swarm's window ladder at g = 3: for a in [9/19, 13/27],
  a positive xi has every {xi (3/2)^j} in [0, a) iff its T-code has every two 1s at distance >= 3, iff every odd
  T-iterate is 5 mod 8 (proved by two lanes, re-derived by both skeptics; single-party). The judge noticed that the
  w = 63 record holder 1541211973603965806 has a rung-3-pure surviving prefix of 156 bits, a 1-2% event under the coin
  model on its own. The decisive free test: among the starts below 2^63 still alive at step 124 (the census
  stragglers), count those whose first 124 code bits are rung-3-pure.
- S2, the sign-dual census (judge's item 2). T(-1-x) = -1-T(x) complements the code, so a negative start x in S_strict
  is exactly a positive eta = -xi with every {eta (3/2)^j} in (1/2, 1). MAHLER.md and the 2^63 census covered xi > 0
  only; Akiyama, Frougny and Sakarovitch state Mahler's question for nonzero xi. The census walker's dual mode
  (mahler_census.c, 'dual') runs the negative starts -2^w < x <= -1.

RUN-ON:     cpu (M5), mahler_census.py at w = 63 in both signs, saving the stragglers to ~/np-scratch-int/mahler; then
            this file's analysis (seconds).
COMMAND:    python3 tests/probes/mahler/mahler_census.py 63 9 6 save=$HOME/np-scratch-int/mahler/strag63.txt
            python3 tests/probes/mahler/mahler_census.py 63 9 6 dual save=$HOME/np-scratch-int/mahler/strag63d.txt
            python3 tests/probes/mahler/mahler_swarm_tests.py

Record searched (record_find, 2026-10-14 10:45 BST): 'rung|5 mod 8' 'Mahler|Z-number' -> 0 hits (ledgers included);
'negative' 'census' 'Mahler|Z-number' -> 3 hits in 3 files (MAHLER.md's scope, GC1221, GPT's review probe; no negative
census); 'straggler' -> 8 hits in 3 files (the census's own). Coin expectations computed first (this session, exact):
A(124) = 10615502910197484579481 gives 2^-61 A(124) = 4603.7 stragglers (observed 4499); Y3(124) =
504968333952204613761 rung-3 words give 2^-61 Y3(124) = 219.0 pure stragglers, a pure fraction of 0.0476, or 214.0
scaled to the observed 4499.

PREDICTIONS (written 2026-10-14 10:45 BST, before either w = 63 run and before any straggler was examined. S0, the
  dual walker's instrument control, was run first and is recorded as done.)
  S0 must hold (done before this file, recorded): at w = 16 the dual walker's histogram equals the exact-fraction H on
     every negative start -2^16 < x <= -1 (it did: True; maximum 40 at x = -40082; 65535 starts).
  S1 (the decisive one): the positive w = 63 run reproduces 4499 stragglers and H* = 157 at 1541211973603965806 (a
     replay check). The number of stragglers whose first 124 code bits are rung-3-pure lies in [150, 280], centre 214
     (coin). Counterfactual: outside [150, 280], a count well above or below the coin, would be the first
     integer-specific bias in the record. The forced phase would then prefer (or avoid) odd terms 5 mod 8 over
     1 mod 8, and the record holder's purity would be structural, not chance. Also reported: the same count over
     chain roots only (stragglers with no straggler T-preimage), and over the negative stragglers (same prediction).
  S2 (the sign dual):
     (a) instrument: the dual histogram totals 2^63 - 1, and (positive survivors + 1) / 2^(63 - T) is an integer
         equal to the positive A(T) at every T < 63 (the free phase is sign-blind);
     (b) the verification: every negative start -2^63 < x <= -1 has a finite horizon. So no eta in (0, 2^63 - 1]
         has every {eta (3/2)^n} in (1/2, 1). A failure is a candidate, replayed exactly before any claim;
     (c) blind (0.7): the record horizon H*_neg(63) lies in [140, 175], and the dual death-bin tail mean lies in
         [0.74, 0.76], like the positive side;
     (d) unexpected check: the dual stragglers' count is within 15% of the positive 4499 (the coin is sign-blind).
         A large asymmetry would mean the forced phase sees the sign statistically.
"""
OUTCOME (2026-10-14 11:20 BST, M5, 9 workers; machine output quoted; run log ~/np-scratch-int/mahler/swarm_block1.log):
  S0 HELD (recorded above). S1 HELD. S2 HELD in (a), (b), (c) and (d).
  S1: the positive rerun reproduced the receipt exactly (4499 stragglers, H* = 157 at 1541211973603965806, mass
     2^63 - 1, RECEIPT OK; 1053 s). Rung-3-pure stragglers: 217 of 4499 (0.0482), inside [150, 280] and beside the
     coin's 214. Over chain roots: 103 of 2269 (0.0454). Negative side: 221 of 4622 (0.0478). Minimum gaps over the
     first 124 bits: {2: 4282, 3: 216, 4: 1} (positive), {2: 4401, 3: 221} (negative). Reading (MEASURED): no
     integer-specific preference for odd terms 5 mod 8 in the forced phase. The record holder's 156-bit rung-3 purity
     is consistent with chance, under GC1227's caution that a single selected start is not a sample.
  S2: (a) the dual total is exactly 2^63 - 1, and A(T) equals the positive A(T) at every T < 63. (b) Every negative
     start -2^63 < x <= -1 has a finite horizon, and all 4622 stragglers died in exact replay (COMPUTED): no eta in
     (0, 2^63 - 1] has every {eta (3/2)^n} in (1/2, 1). (c) H*_neg(63) = 153 at x = -6964446546082240544 (2.429 w),
     inside [140, 175]; the death-bin tail mean is 0.7494. (d) 4622 dual stragglers against 4499, a difference of
     2.7%. Reading: on the negative side the census follows the same coin law as on the positive side; no sign
     effect was seen.
"""
import os, sys
from collections import Counter

SCR = os.path.expanduser('~/np-scratch-int/mahler')


def T(x):
    return (3 * x + (x & 1)) // 2                     # ceil(3x/2) for every integer, both signs (G50)


def code(n, length):
    out = []
    for _ in range(length):
        out.append(n & 1)
        n = T(n)
    return out


def min_gap(bits):
    ones = [i for i, b in enumerate(bits) if b]
    return min((b - a for a, b in zip(ones, ones[1:])), default=10 ** 9)


def rung3_pure(bits):
    return min_gap(bits) >= 3


def analyse(path, label):
    xs = [int(l) for l in open(path) if l.strip()]
    pure = [x for x in xs if rung3_pure(code(x, 124))]
    S = set(xs)
    def preimage(n):                                  # T is injective on Z: T(2m) = 3m, T(2m+1) = 3m+2
        r = n % 3
        return 2 * n // 3 if r == 0 else (2 * n - 1) // 3 if r == 2 else None
    roots = [x for x in xs if preimage(x) not in S]
    pure_roots = [x for x in roots if rung3_pure(code(x, 124))]
    gaps = Counter(min(min_gap(code(x, 124)), 9) for x in xs)
    print('%s: %d stragglers; rung-3-pure %d (%.4f); chain roots %d, of them pure %d (%.4f)' % (
        label, len(xs), len(pure), len(pure) / len(xs), len(roots), len(pure_roots),
        len(pure_roots) / max(1, len(roots))))
    print('   minimum gap between 1s in the first 124 bits:', dict(sorted(gaps.items())))
    return xs, pure


if __name__ == '__main__':
    rec = 1541211973603965806
    print('record holder 1541211973603965806: minimum gap over its first 156 bits =', min_gap(code(rec, 156)))
    for f, lab in (('strag63.txt', 'positive w=63'), ('strag63d.txt', 'negative w=63')):
        p = os.path.join(SCR, f)
        if os.path.exists(p):
            analyse(p, lab)
        else:
            print(lab, ': no straggler file yet')
