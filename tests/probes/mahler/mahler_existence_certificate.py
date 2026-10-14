#!/usr/bin/env python3
"""mahler_existence_certificate.py: the existence-threshold door (drawn in L718; MAHLER.md section 2; the swarm's L3-C2(d)).

The question (existence side, off the main line). For the symmetric window U = [a, 1 - a], does every unit interval
[k, k + 1], k >= 1, contain a real xi with every fractional part of xi (3/2)^n in U? The swarm's computability skeptic
found a memory-1 "residue-uniform interval certificate" (RUIC) proving yes at a = 7/57, inside Dubickas's (5/48, 43/48).
That certificate exists in one implementation only, the skeptic's scratch. Its conjecture: the memory-1 threshold is
exactly 7/57.

This file is an independent implementation, written from the game below, not from the skeptic's code.
- The game: write xi = k + v, with v in U and c = k mod 2. Then xi * 3/2 = (3k - c)/2 + (3v + c)/2. So the next
  fractional part is (3v + c)/2 - t for t in {0, 1}, and the next integer part k' = (3k - c)/2 + t has parity
  (sigma + t) mod 2, where sigma = ((3k - c)/2) mod 2 depends on k's next bit, which the certificate does not control.
- A state is (V, c): a closed grid interval V = [x/G, y/G] inside U, and a parity c. State (V, c) is winning when, for
  both values of sigma, some t in {0, 1} sends V's image (3V + c)/2 - t, cut to U and rounded inward to the grid, to a
  winning state of parity (sigma + t) mod 2.
- Winning is upward closed: a larger V has a larger image. So the inward-rounded image is the only candidate to check.
  The winning set W is the greatest fixed point of that rule, computed by deletion until stable.
- Soundness: if some (V0, 0) and (V0', 1) are winning, every k >= 1 has, by compactness, a xi in k + V whose orbit stays
  in U. The k-th bit sequence plays sigma; the certificate answers with t and a nested interval; nonempty compact
  intersections give xi. This is the skeptic's RUIC soundness argument at memory 1.

RUN-ON:     cpu, exact integers, seconds to minutes.
COMMAND:    python3 tests/probes/mahler/mahler_existence_certificate.py

Record searched (record_find, 2026-10-14 12:16 BST): '7/57|RUIC|residue-uniform' -> MAHLER.md section 2 and the ledger
summaries only; '5/48|Dubickas.*2008' -> PRIOR-ART's Dubickas lines. No implementation in the record.

PREDICTIONS (written 2026-10-14 12:16 BST, before any run of this file).
  E1 (the replication): at G = 912 and a = 7/57 (x from 112 to 800), W is nonempty and contains states of both
     parities. So every [k, k + 1], k >= 1, holds a xi with all fractional parts in [7/57, 50/57]: COMPUTED
     certificate, PROOF-SKETCH soundness, now from two implementations.
  E2 (the threshold, 0.7): at G = 912 and a = 113/912, the next grid point above 7/57, W is empty.
  E3 (the threshold on a second grid, 0.6): at G = 1140 = 20 * 57, W is nonempty at a = 140/1140 = 7/57 and empty at
     a = 141/1140.
  Counterfactuals: E1 empty would be an instrument disagreement with the skeptic, to be resolved before any claim. A
  nonempty W above 7/57 on a grid refutes the exact-threshold conjecture at memory 1.
  Unexpected check: at a = 1/7 (G = 912 * 7 / 57 is not an integer, so G = 7 * 114 = 798, x from 114 to 684) W is
     empty. The skeptic found dead residues there, so no certificate can exist.
"""
import sys, time
from fractions import Fraction as F


def winning_set(G, lo, hi):
    """Greatest fixed point of the memory-1 game on grid 1/G, window [lo/G, hi/G] (integers lo < hi)."""
    states = {(x, y, c) for x in range(lo, hi) for y in range(x + 1, hi + 1) for c in (0, 1)}

    def image(x, y, c, t):
        # (3V + c)/2 - t on the grid, in units of 1/G: [ (3x + cG)/2 - tG, (3y + cG)/2 - tG ], cut to [lo, hi], inward
        a2, b2 = 3 * x + c * G - 2 * t * G, 3 * y + c * G - 2 * t * G     # doubled endpoints
        x1 = max(-(-a2 // 2), lo)                    # ceil(a2 / 2), cut to the window
        y1 = min(b2 // 2, hi)                        # floor(b2 / 2)
        return (x1, y1) if x1 < y1 else None

    succ = {}
    for (x, y, c) in states:
        succ[(x, y, c)] = [image(x, y, c, t) for t in (0, 1)]
    changed = True
    while changed:
        changed = False
        dead = []
        for (x, y, c) in states:
            ims = succ[(x, y, c)]
            ok = True
            for sigma in (0, 1):
                if not any(ims[t] is not None and (ims[t][0], ims[t][1], (sigma + t) % 2) in states for t in (0, 1)):
                    ok = False
                    break
            if not ok:
                dead.append((x, y, c))
        if dead:
            changed = True
            for s in dead:
                states.discard(s)
    return states


def report(label, G, lo, hi):
    t0 = time.time()
    W = winning_set(G, lo, hi)
    par = {c for (_, _, c) in W}
    print('%s: G=%d, window [%s, %s]: |W| = %d, parities %s, %.1f s' % (
        label, G, F(lo, G), F(hi, G), len(W), sorted(par), time.time() - t0), flush=True)
    return W


if __name__ == '__main__':
    report('E1 a=7/57', 912, 112, 800)
    report('E2 a=113/912', 912, 113, 799)
    report('E3 a=7/57', 1140, 140, 1000)
    report('E3 a=141/1140', 1140, 141, 999)
    report('unexpected a=1/7', 798, 114, 684)
