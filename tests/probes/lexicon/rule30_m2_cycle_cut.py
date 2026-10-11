#!/usr/bin/env python3
"""rule30_m2_cycle_cut.py: a cake_lpr receipt for L591's "5,5,3,3,3 is absent at length 120" (GC1111) (M2C).

RUN-ON:     cpu (Python 3; kissat, drat-trim, cake_lpr through rule30_mfw_certify.certify); minutes
COMMAND:    python3 tests/probes/lexicon/rule30_m2_cycle_cut.py

Why. L591 (and SLC2's header, an unregistered observation at 13:06 on 2026-10-10) reported that the spelled power of
the zero-entropy S/L cycle with gaps 5,5,3,3,3 is absent from L at length 120. GC1111 builds a uniform cap on it (GC1103's
M2 = SLLSS is the same cycle) and asks for the retained word and phase, or a verified cut inside the cyclic word. None
was retained, and no word of the verified lists (mfw40, mfw40p1, cuts40_p0, cuts40_p1, the 83 SLC cuts) occurs in the
periodic word (checked 2026-10-11 before this probe, 0 hits). So this probe makes the receipt.

How. The cycle spells c = S L L S S = 001 00001 00001 001 001 (19 bits; S = 001, L = 00001 as rule30_sl_cuts.BLOCK), and
P = c c c ... is the bi-infinite periodic visible word. Its factors of length n are the 19 rotations' prefixes, and
"some factor of length n is absent" is monotone in n (a longer factor contains a shorter one at every offset). So a
binary search finds the least n with an absent factor, per phase; every absent factor of that length is a minimal
absent word of P's language, i.e. a cut inside the cyclic word. Each word goes through rule30_mfw_certify.certify:
cone CNF, kissat (SAT means present), DRAT, drat-trim -L, cake_lpr (VERIFIED-UNSAT means absent, verified). The 19
length-120 rotations are also certified in both phases, to answer L591's statement as written. Receipts in m2c.ck.

PREDICTIONS, registered 2026-10-11 06:03 BST before the run:
  M2C-P0 (control, must hold): the known-absent 11 is VERIFIED-UNSAT in phase 0 and the word 1 is SAT.
  M2C-P1 (blind, 0.6): the least absent length in phase 0 lies in 91 .. 102, so every length-120 rotation contains an
      absent factor and all 19 are absent, in both phases (L1 is contained in L).
  M2C-P2 (blind, 0.5): phase 1's least absent length is strictly below phase 0's.
  Record searched: '5,5,3,3,3' -> SLC2's header and L591 only.
REFUTED-BY: M2C-P0 failing (the instrument); M2C-P1, M2C-P2 as stated.
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_mfw_certify as mfc                               # noqa: E402  (certify, DIR)
sys.argv = _argv

CYC = '001' + '00001' + '00001' + '001' + '001'                # S L L S S, the M2 cycle (gaps 3,5,5,3,3 cyclically)
assert len(CYC) == 19
CK = os.path.join(mfc.DIR, 'm2c.ck')


def rot(r, n):
    return ((CYC * (n // 19 + 3))[r:r + n])


def receipt(w, ph):
    t0 = time.time()
    v = mfc.certify(w, ph)
    with open(CK, 'a') as f:
        f.write('%d %d %s %s %.1f\n' % (ph, len(w), w, v, time.time() - t0))
    assert v in ('SAT', 'VERIFIED-UNSAT'), (w, ph, v)
    return v == 'VERIFIED-UNSAT'


def absent_at(n, ph):
    return [r for r in range(19) if receipt(rot(r, n), ph)]


def least(ph, lo=2, hi=120):
    assert absent_at(hi, ph), 'nothing absent at %d' % hi
    while lo < hi:
        mid = (lo + hi) // 2
        if absent_at(mid, ph):
            hi = mid
        else:
            lo = mid + 1
    return lo, absent_at(lo, ph)


def main():
    ok0 = receipt('11', 0) and not receipt('1', 0)
    print('M2C-P0 %s  (11 VERIFIED-UNSAT, 1 SAT in phase 0)' % ('PASS' if ok0 else 'FAIL'), flush=True)
    res = {}
    for ph in (0, 1):
        n, rs = least(ph)
        res[ph] = n
        print('phase %d: least absent length %d; absent rotations %s' % (ph, n, rs), flush=True)
        for r in rs:
            print('  cut (rotation %d): %s' % (r, rot(r, n)), flush=True)
        a120 = absent_at(120, ph)
        print('phase %d: length-120 rotations absent: %d of 19 %s' % (ph, len(a120), a120), flush=True)
    print('M2C-P1 %s  (phase 0 least %d)' % ('HELD' if 91 <= res[0] <= 102 else 'REFUTED', res[0]))
    print('M2C-P2 %s  (phase 1 least %d, phase 0 least %d)' % ('HELD' if res[1] < res[0] else 'REFUTED', res[1], res[0]))


if __name__ == '__main__':
    main()
