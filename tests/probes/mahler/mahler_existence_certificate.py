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

OUTCOME (2026-10-14 12:18 BST, M5, seconds each; machine output quoted; log ~/np-scratch-int/mahler/existence_cert.log):
  E1 HELD: at G = 912 and a = 7/57, |W| = 322070 with both parities. That is the skeptic's count exactly, from an
     independent implementation. So every [k, k + 1], k >= 1, holds a xi with every fractional part of xi (3/2)^n in
     [7/57, 50/57]: COMPUTED certificate, two implementations; PROOF-SKETCH soundness, single-party.
  E2 HELD: W is empty at a = 113/912.
  E3 HELD: at G = 1140, |W| = 502230 at a = 7/57, and W is empty at a = 141/1140.
  Unexpected check HELD: W is empty at a = 1/7 (G = 798).
  WITNESS (2026-10-14, at GPT's request in GC1235/GC1235.1): a 15-state closed sub-strategy was extracted from the
     G = 912 winning set (shortest minimal winning intervals, breadth first from one root of each parity). It is listed
     as _W15 below with t chosen for both sigma, and check_witness() verifies it with exact fractions, independently of
     the grid code: closed, inside [7/57, 50/57], both parities. Run: python3 ... witness. Its endpoints are the (100)
     cycle 4/19, 6/19, 9/19, its mirror 10/19, 13/19, 15/19, and /57 points (7/57, 11/57, 20/57, 26/57, 31/57, 37/57,
     46/57, 50/57). The tight edges are [7/57, ...] (c = 1, t = 0) -> left end 13/19 and [725/912, 50/57] (c = 0,
     t = 1) -> right end 6/19. GPT's soundness argument (GC1235) is read by Local: k fixes sigma; t is the genuine carry
     since the image lies in U, inside (0, 1); the pullbacks are nested compact intervals shrinking by 2/3. So the
     15-state witness alone proves the existence window. Why every strategy must use those edges (the exact threshold)
     stays OPEN.
  Reading: the memory-1 threshold sits exactly at 7/57 on both grids. Why 7/57 = 7/(3 x 19), with 19 the (100) cycle's
     denominator, is parked in INSTINCT.md's incubator. Off the main line: an existence window, not an exclusion.
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


if __name__ == '__main__' and not (len(sys.argv) > 1 and sys.argv[1] == 'witness'):
    report('E1 a=7/57', 912, 112, 800)
    report('E2 a=113/912', 912, 113, 799)
    report('E3 a=7/57', 1140, 140, 1000)
    report('E3 a=141/1140', 1140, 141, 999)
    report('unexpected a=1/7', 798, 114, 684)


# The 15-state witness (extracted 2026-10-14 from the G = 912, a = 7/57 winning set at GPT's request, GC1235/GC1235.1):
# each state is (left, right, parity); WITNESS[(state, sigma)] = (t, successor). Checkable by hand, and by check_witness()
# with exact fractions independently of the grid code.
_W15 = [
    ((F(39, 304), F(4, 19), 0), (0, (F(71, 304), F(6, 19), 0)), (0, (F(11, 57), F(115, 456), 1))),
    ((F(71, 304), F(6, 19), 0), (0, (F(20, 57), F(395, 912), 0)), (0, (F(63, 152), F(9, 19), 1))),
    ((F(277, 912), F(331, 912), 0), (0, (F(26, 57), F(491, 912), 0)), (0, (F(421, 912), F(31, 57), 1))),
    ((F(20, 57), F(395, 912), 0), (0, (F(10, 19), F(89, 152), 0)), (0, (F(517, 912), F(37, 57), 1))),
    ((F(26, 57), F(491, 912), 0), (0, (F(341, 456), F(46, 57), 0)), (0, (F(13, 19), F(233, 304), 1))),
    ((F(10, 19), F(89, 152), 0), (0, (F(725, 912), F(50, 57), 0)), (0, (F(15, 19), F(265, 304), 1))),
    ((F(341, 456), F(46, 57), 0), (1, (F(7, 57), F(187, 912), 1)), (1, (F(39, 304), F(4, 19), 0))),
    ((F(725, 912), F(50, 57), 0), (1, (F(11, 57), F(115, 456), 1)), (1, (F(71, 304), F(6, 19), 0))),
    ((F(7, 57), F(187, 912), 1), (0, (F(341, 456), F(46, 57), 0)), (0, (F(13, 19), F(233, 304), 1))),
    ((F(11, 57), F(115, 456), 1), (0, (F(725, 912), F(50, 57), 0)), (0, (F(15, 19), F(265, 304), 1))),
    ((F(63, 152), F(9, 19), 1), (1, (F(7, 57), F(187, 912), 1)), (1, (F(39, 304), F(4, 19), 0))),
    ((F(421, 912), F(31, 57), 1), (1, (F(11, 57), F(115, 456), 1)), (1, (F(71, 304), F(6, 19), 0))),
    ((F(517, 912), F(37, 57), 1), (1, (F(63, 152), F(9, 19), 1)), (1, (F(20, 57), F(395, 912), 0))),
    ((F(13, 19), F(233, 304), 1), (1, (F(517, 912), F(37, 57), 1)), (1, (F(10, 19), F(89, 152), 0))),
    ((F(15, 19), F(265, 304), 1), (1, (F(13, 19), F(233, 304), 1)), (1, (F(341, 456), F(46, 57), 0))),
]


def check_witness(a=F(7, 57)):
    """Exact closure check: every successor lies in U = [a, 1-a], inside the image (3V + c)/2 - t, and is a state of
    parity (sigma + t) mod 2 in the witness; both parities occur."""
    states = {s for s, _, _ in _W15}
    ok = True
    for s, r0, r1 in _W15:
        p, q, c = s
        for sigma, (t, nxt) in ((0, r0), (1, r1)):
            p2, q2, c2 = nxt
            lo_img, hi_img = (3 * p + c) / 2 - t, (3 * q + c) / 2 - t
            good = (nxt in states and c2 == (sigma + t) % 2 and lo_img <= p2 < q2 <= hi_img and a <= p2 and q2 <= 1 - a)
            ok &= good
    return ok and {s[2] for s in states} == {0, 1}, len(states)


if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'witness':
    print('15-state witness closed and sound at a = 7/57:', check_witness())
