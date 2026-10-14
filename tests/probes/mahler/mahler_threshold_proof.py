#!/usr/bin/env python3
"""mahler_threshold_proof.py: is 7/57 the exact memory-1 existence threshold for real intervals? (GC1235.1's forced-phase
obligation; GPT's and Local's shared pull, L721/GC1236; MAHLER.md section 2.)

The memory-1 game of mahler_existence_certificate.py, with real intervals instead of a grid. Window U = [a, 1 - a].
A state is (V, c): a closed interval V inside U of positive width, and a parity c. From (V, c), for each sigma chosen
by the adversary, the defender picks t in {0, 1} with V' = ((3V + c)/2 - t) cut to U, of positive width; the new state
is (V', (sigma + t) mod 2).

Two reductions, both by monotonicity:
- Winning is upward closed in V, since a larger V has a larger image. So the full window ([a, 1 - a], c) wins iff any
  state of parity c does, and the defender loses nothing by always taking the maximal cut image.
- Winning is monotone in a: a smaller a gives a larger window. So the threshold a* = sup{a : the game is won} is
  well defined.

The proof method. Take a = 7/57 + d with d a formal positive infinitesimal: numbers are pairs (r, s) meaning r + s d,
ordered lexicographically. If the adversary wins the maximal-image game within finite depth N in this model, the
same moves win for every real d in (0, eps_N). So the game is lost for those a, and by monotonicity for every
a > 7/57. With the 15-state witness at a = 7/57 (L721), that would make 7/57 the exact memory-1 threshold for real
intervals. A symbolic defender that survives to the depth cap is inconclusive, not a proof of winning.

RUN-ON:     cpu, exact Fractions, seconds.
COMMAND:    python3 tests/probes/mahler/mahler_threshold_proof.py

Record searched (record_find, 2026-10-14 12:43 BST): '7/57|RUIC|memory-1' -> MAHLER.md section 2, the existence probe,
the ledger (L719 .. L721, GC1235/1235.1, GC1236); no threshold proof in the record.

PREDICTIONS (written 2026-10-14 12:43 BST, before any run).
  T1 (control): at d = 0 exactly (a = 7/57), the defender survives the maximal-image game to depth 40 from both
     parities. This is consistent with the 15-state witness.
  T2 (the proof, 0.65): at d = +0 the adversary wins from both parities within depth 40. That would prove the exact
     memory-1 threshold 7/57 for real intervals. Counterfactual: the symbolic defender survives to depth 40 at +0,
     and the method is inconclusive at that depth.
  T3 (control): at d = -0 (a just below 7/57) the defender survives to depth 40.
  Unexpected check: the adversary's winning line at +0 passes through an interval whose endpoint is one of the tight
     edges, 13/19 or 6/19 (GC1235.1's identities (3a + 1)/2 <= 13/19 and 3(1 - a)/2 - 1 >= 6/19).
"""
import sys
from fractions import Fraction as F
from functools import lru_cache

A0 = F(7, 57)
DEPTH = 40


def run(s_sign):
    """s_sign: 0 for a = 7/57 exactly, +1 for 7/57 + d, -1 for 7/57 - d. Numbers are (r, s)."""
    a = (A0, F(s_sign))
    b = (1 - A0, F(-s_sign))                       # 1 - a

    def lt(x, y):
        return x < y                                 # tuples compare lexicographically: exact first-order order

    def img(V, c, t):
        (p, q) = V
        p2 = ((3 * p[0] + c) / 2 - t, 3 * p[1] / 2)
        q2 = ((3 * q[0] + c) / 2 - t, 3 * q[1] / 2)
        lo = max(p2, a)
        hi = min(q2, b)
        return (lo, hi) if lt(lo, hi) else None

    @lru_cache(maxsize=None)
    def defender_survives(V, c, depth):
        """True if the defender survives `depth` more rounds from (V, c) taking maximal images."""
        if depth == 0:
            return True
        for sigma in (0, 1):
            ok = False
            for t in (0, 1):
                W2 = img(V, c, t)
                if W2 is not None and defender_survives(W2, (sigma + t) % 2, depth - 1):
                    ok = True
                    break
            if not ok:
                return False                         # this sigma defeats every t
        return True

    full = (a, b)
    res = {c: defender_survives(full, c, DEPTH) for c in (0, 1)}
    return res, defender_survives


def adversary_line(s_sign, c0):
    """One winning line for the adversary (the first sigma that defeats every t, recursively), with the depth used."""
    res, ds = run(s_sign)
    a = (A0, F(s_sign)); b = (1 - A0, F(-s_sign))

    def img(V, c, t):
        (p, q) = V
        p2 = ((3 * p[0] + c) / 2 - t, 3 * p[1] / 2); q2 = ((3 * q[0] + c) / 2 - t, 3 * q[1] / 2)
        lo, hi = max(p2, a), min(q2, b)
        return (lo, hi) if lo < hi else None

    line, V, c = [], (a, b), c0
    for depth in range(DEPTH, 0, -1):
        for sigma in (0, 1):
            if all(img(V, c, t) is None or not ds(img(V, c, t), (sigma + t) % 2, depth - 1) for t in (0, 1)):
                line.append((V, c, sigma))
                live = [t for t in (0, 1) if img(V, c, t) is not None]
                if not live:
                    return line
                t = live[0]
                V, c = img(V, c, t), (sigma + t) % 2
                break
        else:
            return line
    return line


if __name__ == '__main__':
    for name, sg in (('T1 a = 7/57', 0), ('T2 a = 7/57 + d', 1), ('T3 a = 7/57 - d', -1)):
        res, _ = run(sg)
        print('%s: defender survives depth %d from parity 0: %s, parity 1: %s' % (name, DEPTH, res[0], res[1]), flush=True)
    for c0 in (0, 1):
        ln = adversary_line(1, c0)
        print('adversary line at +d from parity %d, %d moves:' % (c0, len(ln)))
        for V, c, sigma in ln:
            fmt = lambda x: '%s%+sd' % (x[0], x[1]) if x[1] else str(x[0])
            print('   [%s, %s] c=%d  sigma=%d' % (fmt(V[0]), fmt(V[1]), c, sigma))
