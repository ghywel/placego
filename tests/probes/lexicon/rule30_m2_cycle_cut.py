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

OUTCOME, 2026-10-11 06:21 BST (about 15 minutes beside the solvers; 332 receipts in m2c.ck, every one SAT or
VERIFIED-UNSAT by cake_lpr, none failed):
  M2C-P0 PASS.
  Phase 0 and phase 1 alike: the least absent length is 114, with one absent rotation (3), and that cut is exactly
      (L L S S S)^6 = (00001 00001 001 001 001)^6, 114 bits, VERIFIED-UNSAT in both phases.
  Length 120: 11 of the 19 rotations are absent in each phase (rotations 0, 1, 2, 3, 10, 11, 12, 13, 16, 17, 18; each
      contains the cut), and 8 are present. So L591's "absent at length 120" held for the rotation it tested, not for all.
  Any M2-periodic stretch of 114 + 18 = 132 visible bits (seven periods, 133 bits) contains (LLSSS)^6, so it is absent.
  M2C-P1 REFUTED (114, not 91 .. 102; and only 11 of 19 length-120 rotations are absent). M2C-P2 REFUTED (equal, 114).
  (recorded 06:22)

SCAN (CL292's question, registered 2026-10-11 06:29 BST before its run): `scan` certifies every rotation at lengths
115 .. 119 in both phases (114 and 120 are in m2c.ck), and names every minimal absent factor of the periodic word up to
length 120: absent at n, with both of its length-(n - 1) factors present.
  M2C-P3 (blind, 0.7): there is a second minimal cut, of length 115 .. 120, inside the windows starting at rotations
      10 .. 13 (which cannot contain (LLSSS)^6, as CL292 counts), the same in both phases.
  SCAN OUTCOME (06:49; both phases identical, every receipt SAT or VERIFIED-UNSAT, none failed):
      absent rotations by length: 114: 3; 115: 2, 3; 116: 1 .. 3; 117: 0 .. 3, 13; 118: 0 .. 3, 12, 13, 18;
      119: 0 .. 3, 11 .. 13, 17, 18; 120: 0 .. 3, 10 .. 13, 16 .. 18.
      Minimal cuts of the periodic word to length 120: exactly two, (LLSSS)^6 (length 114, rotation 3) and
      (SSSLL)^6 S (length 117, rotation 13), both VERIFIED-UNSAT by cake_lpr in phase 0 and in phase 1.
  M2C-P3 HELD: the second cut, (SSSLL)^6 S, is what rotations 10 .. 13 contain at 120; CL292's count of seven windows for
      (LLSSS)^6 is right, and the other four are this cut's. (recorded 06:49)
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


def scan():
    for ph in (0, 1):
        ab = {n: set(absent_at(n, ph)) for n in range(114, 121)}
        print('phase %d: absent rotations by length: %s' % (ph, ' '.join('%d:%s' % (n, sorted(ab[n])) for n in ab)))
        for n in range(115, 121):
            for r in sorted(ab[n]):
                if r not in ab[n - 1] and (r + 1) % 19 not in ab[n - 1]:
                    print('  minimal cut, phase %d, length %d, rotation %d: %s' % (ph, n, r, rot(r, n)), flush=True)


if __name__ == '__main__':
    scan() if len(sys.argv) > 1 and sys.argv[1] == 'scan' else main()
