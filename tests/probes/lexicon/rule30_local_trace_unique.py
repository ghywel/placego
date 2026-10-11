#!/usr/bin/env python3
"""rule30_local_trace_unique.py: RTU, is the visible word of the exact 17-record at d = 132 and 139 (phase 0) unique?

RUN-ON:     cpu (kissat; one relaxed solve a depth, 4-hour cap)
COMMAND:    KISSAT=kissat python3 tests/probes/lexicon/rule30_local_trace_unique.py D PHASE [CAP] [K]
            (K > 0, RTU2: block only on visible bits K .. end, so a new word must differ from bit K on)

WHY. GC1155 reads the endpoint of the actual 139/17 record from Local's published row. In the data folder every source
that carries 17 at 132 or 139 in phase 0 (two sampling runs with fresh seeds, 2^31 samples a phase each, and CUT's SAT
lift at 131) gives ONE column-1 trace (rule30_local_record_traces.txt, the sharp-17 section, L643). If the record word
is unique, the endpoint analysis of that one row is the whole story at that depth and phase.

HOW. RLK's relaxed model (rule30_relaxed_records_k.py: the left light cone exact, the right side replaced by the
visible word under every certified minimal forbidden word to 44, mfw44all or mfw44allp1, plus the verified cuts40
lists; cuts44's newer cuts are not yet certified and are left out) at d, L = 17, with one more clause: the visible word
differs from the published one somewhere. Relaxed UNSAT is sound for the actual problem (the relaxation only adds
configurations), so UNSAT proves: every configuration with a white band d .. d + 16 beside the wall clamped through
d + 16 (in that phase) has exactly this visible word. Relaxed SAT gives
a different word in the language to 44; it is lifted (right_half_for and the glued simulation, as CUT does), and a
lift is a second, distinct real 17-record. An unlifted SAT leaves the question open.

PREDICTIONS (registered 2026-10-11 before the runs, L643):
  RTU-C1 (control, must hold): at 142 phase 1 the data hold two distinct 17-words (they differ in their first bits);
         blocking the first must leave the model SAT. UNSAT there would mean the block over-constrains.
  RTU-P1 (blind, 0.4): 132 phase 0 is UNSAT with the block (the record word at 132 is unique in phase 0).
  RTU-P2 (blind, 0.4): 139 phase 0 is UNSAT with the block.
  RTU-P3 (blind, 0.5): at least one of the two ends UNKNOWN at the 4-hour cap (CUT44's 132 instance, one length
         longer, took 5,078 s to UNSAT under lighter load).
  Record searched: 'unique|uniqueness' in RECORD-MAP.md and the RT probe -> no hit on record words.
OUTCOME, RTU-P1 (2026-10-11 16:53 BST, about 12 minutes): REFUTED. 132 phase 0 is relaxed SAT with the block, and the
  new word lifts (glued simulation VALID): 00001000101000010001000101000100001010000101000010010010000100100001000010,
  which differs from the published word at bit 0 only. So R_real(132) = 17 has at least two phase-0 record words.
RTU2 (registered 2026-10-11 16:54 BST, before its run): the same test blocking only bits K .. end (a new word must
  differ at some bit >= K); its lifts are saved (rtu_w_d<d>_p<ph>_K<K>.txt) and replayed by rule30_witness_check.
  RTU2-P1 (blind, 0.5): 132 phase 0 at K = 1 is UNSAT: the record word at 132 is unique apart from its first bit.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule30_relaxed_records_k as rlk                                 # noqa: E402
import rule30_local_record_traces as rt                                # noqa: E402
from rule30_witness_check import check as wcheck                         # noqa: E402


def published(d, phase):
    for dd, L, ph, T, status, tr, vis, left, right in rt.blocks(rt.OUT):
        if dd == d and L == 17 and ph == phase:
            return vis
    raise SystemExit('no published 17-row at %d phase %d' % (d, phase))


def main():
    d, ph = int(sys.argv[1]), int(sys.argv[2])
    cap = int(sys.argv[3]) if len(sys.argv) > 3 else 14400
    K = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    L = 17
    vis = published(d, ph)
    forb = rlk.load_forbidden('44all' if ph == 0 else '44allp1') + rlk.load_cuts(ph, 40)     # certified only
    inst = rlk.Relaxed(d, L, ph, forb)
    assert len(inst.vis) == len(vis), (len(inst.vis), len(vis))
    inst.cl.append([(-v if b == '1' else v) for v, b in list(zip(inst.vis, vis))[K:]])   # differs at a bit >= K
    print('RTU d=%d L=%d phase %d: %d words, block on bits %d .. %d of a %d-bit visible word' % (
        d, L, ph, len(forb), K, len(vis) - 1, len(vis)), flush=True)
    v = inst.solve(cap, forb)
    print('RTU d=%d: relaxed %s' % (d, v), flush=True)
    if v == 'SAT':
        code = inst.code
        assert code[K:] != vis[K:]
        diff = [i for i in range(len(vis)) if code[i] != vis[i]]
        right = rlk.right_half_for(code, ph)
        if right:
            ok, why = rlk.simulate_glued(inst.left0, right, inst.T, ph, d, L, code)
            T = inst.T
            cells = ''.join(str(inst.left0[i]) for i in range(-T, 1))
            rgt = ''.join(str(right.get(i, 0)) for i in range(1, max(right) + 1))
            band, clock, same = wcheck(d, L, ph, cells, rgt, code)
            ok2 = band and clock and same
            out = os.path.join(rlk.DIR, 'rtu_w_d%d_p%d_K%d.txt' % (d, ph, K))
            open(out, 'w').write('W %d %d %d %s %s\n' % (d, L, ph, cells, rgt))
            print('RTU d=%d: a second word %s (differs at bits %s); lift %s, rule30_witness_check %s; saved %s' % (
                d, code, diff, 'VALID' if ok else 'FAILED %s' % why, 'VALID' if ok2 else 'NOT VALID', out))
        else:
            print('RTU d=%d: a second word %s in the language to 44, no lift (open)' % (d, code))
    print('RTU d=%d: done' % d)


if __name__ == '__main__':
    main()
