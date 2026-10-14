#!/usr/bin/env python3
"""rule30_cut_core_context.py: the left contexts of the core shared by tonight's two long cuts at 147. Loop check 4
(L705) drew door 2, long cuts at the frontier; Local's block there as the maths lead (AGENTS.md item 19).

The two certified minimal cuts (rule30_cadical_certify.py K12, K15) are
    00001000010101010001000010010010000100001001001000                         (50 bits)
    0100010001010101000100001001001000010000100100100001000010000100001001     (70 bits)
and both contain, from index 10, the 40-bit core c = 0101010001000010010010000100001001001000 (present, since a minimal
cut's proper factors are). So c is real, but not after either head 0000100001 or 0100010001 (in the second case with
a 20-bit tail). Question: which 10-bit heads h make h.c a real phase-0 visible word (RLK's membership query)? The
phase-0 language is factor-closed (every visible sample is at a white tick), so h.c in L_0 is the right test.

RUN-ON:     cpu, kissat (RLK membership); minutes.
COMMAND:    KISSAT=kissat python3 tests/probes/lexicon/rule30_cut_core_context.py

Record searched (record_find, 2026-10-14 02:36 BST): 'left context|predecessor set|left extension' -> 6 hits in 3
files; 'common core|shared core' -> no hit outside the ledgers. K12, K15 and the lift rounds (rule30_cadical_lift.py)
read.

PREDICTIONS (written 2026-10-14 02:37 BST, before the run).
  C1 must hold (instrument): c itself is real; both cut heads fail (0000100001.c and 0100010001.c are absent: the first
     is the 50-bit cut itself; the second must fail too, or the 70-bit cut would not be minimal); and the heads
     contain no factor 11 (a word containing 11 is absent).
  C2 blind (0.5): fewer than 10% of the 10-bit heads with no 11 and no 00000 (and no 11 at the join with c) give a real
     h.c. Counterfactual: 25% or more are real, so the core is not a narrow gate.
  C3 (reported, no prediction): the real heads, grouped by their last white-time gap before c, and whether every real
     head ends in an S or L gap (100 or 10000 before the core's leading 0101).

OUTCOME (2026-10-14 02:37 BST, M5, seconds; machine output quoted): C1 FAILED (a wrong prediction, not a wrong
  instrument), C2 HELD, but read below.
  C1: the core is real and the 50-bit cut (0000100001.c) is absent, as required. But 0100010001.c is REAL. My C1 claimed
     it must be absent; the opposite follows from minimality. That 50-bit word is a factor of the 70-bit cut's 69-bit
     prefix, which minimality makes present. So the instrument agrees with the logic, and C1's wording was the error.
  C2: admissible heads 94; real h.c 7 (7.4%). Real heads: 0000101000 0010100001 0100001000 0100010001 1000101000
     1010000100 1010100001. C3, by the head's last 1 and trailing zeros: ending 1: 3; ending 100: 1; ending 1000: 3.
  Reading: the 7.4% is unremarkable. At the channel bound's 0.1236 bits per visible bit, ten more samples multiply a
  real word's count by about 2^1.24 = 2.4 on average, so 7 of 94 is about what the language's entropy allows, not a
  narrow gate. The counterfactual threshold (25%) was mis-scaled. No structural claim is made about the core.
"""
import os, sys
from itertools import product
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule30_relaxed_records_k as rlk                                  # noqa: E402

CORE = '0101010001000010010010000100001001001000'


def main():
    real = lambda w: bool(rlk.in_language_phase(w, 0))
    c1 = real(CORE) and not real('0000100001' + CORE) and not real('0100010001' + CORE)
    print('C1 core real, both cut heads absent:', 'HELD' if c1 else 'FAILED', flush=True)
    heads = [''.join(h) for h in product('01', repeat=10)]
    ok = [h for h in heads if '11' not in h + CORE[:1] and '00000' not in h and '00000' not in (h + CORE)[:15]]
    good = [h for h in ok if real(h + CORE)]
    frac = len(good) / len(ok)
    print('admissible heads %d; real h.c %d (%.1f%%)' % (len(ok), len(good), 100 * frac), flush=True)
    print('C2 fewer than 10%% real:', 'HELD' if frac < 0.10 else 'REFUTED', '| counterfactual >= 25%%:', frac >= 0.25)
    tails = {}
    for h in good:
        i = h.rfind('1')
        tails.setdefault(h[i:] if i >= 0 else h, []).append(h)
    print('C3 real heads by their last 1 and trailing zeros:', {k: len(v) for k, v in sorted(tails.items())})
    print('real heads:', ' '.join(good))


if __name__ == '__main__':
    main()
