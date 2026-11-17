#!/usr/bin/env python3
"""rule30_local_trace_unique.py: RTU, is the visible word of the exact 17-record at d = 132 and 139 (phase 0) unique?

RUN-ON:     cpu (kissat; one relaxed solve a depth, 4-hour cap)
COMMAND:    KISSAT=kissat python3 tests/probes/lexicon/rule30_local_trace_unique.py D PHASE [CAP] [K] [MAXIT]
            KISSAT=kissat python3 tests/probes/lexicon/rule30_local_trace_unique.py cert D PHASE K   (cake_lpr)
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
OUTCOME, the rest of RTU (17:34 BST): RTU-C1 PASS: 142 phase 1 with its first word blocked is SAT, and the word lifts
  (glued simulation VALID): 0010100001000101010101010101010101000100001010101010101010100010000101000010100, a THIRD
  phase-1 word at 142, differing from the first at bits 8 and 9 only. RTU-P2 REFUTED as worded: 139 phase 0 with the
  block is relaxed SAT within a minute, but its word (below) has no right half (absent from L beyond length 44), so
  uniqueness at 139 is open. RTU-P3 REFUTED: no solve reached the cap (12 minutes, 52 minutes, 1 minute).
    010000100100001000010100001010101000100001010000100100001000010100001000010000
OUTCOME, RTU2-P1 (17:56 BST, 61 minutes): HELD (kissat). 132 phase 0 with the block on bits 1 .. 73 is relaxed UNSAT,
  on certified words only, so every configuration with a white band 132 .. 148 beside the wall clamped through 148
  (phase 0) has the published visible word in bits 1 .. 73: exactly two phase-0 record words, both realized, which
  differ in bit 0 alone. The cake_lpr certificate (`cert 132 0 1`) follows.
RTU3 (registered 2026-10-11 17:35 BST, before its run): 139 phase 0, the full block, iterating as CUT does: an unlifted
  word gives its shortest absent factors (length >= 45) as cuts (rtu_cuts_p0.txt, to be certified by MFC before any
  verdict rests on them), up to 40 rounds at 4-hour caps.
  RTU3-P1 (blind, 0.3): it ends UNSAT (with the cuts certified, 139's record word is unique in phase 0).
  RTU3-P2 (blind, 0.55): it ends with a lifted second word, differing from the published one only within its first
  ten bits (as at 132 and 142).
"""
import os
import sys
import time

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
    maxit = int(sys.argv[5]) if len(sys.argv) > 5 else 1             # RTU3: > 1 iterates with language cuts
    L = 17
    vis = published(d, ph)
    base = rlk.load_forbidden('44all' if ph == 0 else '44allp1') + rlk.load_cuts(ph, 40)     # certified only
    cutfile = os.path.join(rlk.DIR, 'rtu_cuts_p%d.txt' % ph)
    extra = []                                          # RTU's own cuts: absent words, certified afterwards (MFC)
    for p in ((0,) if ph == 0 else (0, 1)):
        f = os.path.join(rlk.DIR, 'rtu_cuts_p%d.txt' % p)
        if os.path.exists(f):
            extra += [line.split()[0] for line in open(f) if line.strip()]
    for it in range(maxit):
        forb = base + extra
        inst = rlk.Relaxed(d, L, ph, forb)
        assert len(inst.vis) == len(vis), (len(inst.vis), len(vis))
        inst.cl.append([(-v if b == '1' else v) for v, b in list(zip(inst.vis, vis))[K:]])   # differs at a bit >= K
        print('RTU d=%d L=%d phase %d it %d: %d words (%d RTU cuts), block on bits %d .. %d of a %d-bit visible word'
              % (d, L, ph, it, len(forb), len(extra), K, len(vis) - 1, len(vis)), flush=True)
        v = inst.solve(cap, forb)
        print('RTU d=%d: relaxed %s' % (d, v), flush=True)
        if v != 'SAT':
            break
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
            break
        print('RTU d=%d: a second word %s in the language to 44, no lift' % (d, code), flush=True)
        if it + 1 == maxit:
            print('RTU d=%d: open (MAXIT)' % d)
            break
        new = rlk.shortest_absent(code, ph, 45)
        assert new and not set(new) & set(forb), new
        with open(cutfile, 'a') as f:
            f.writelines('%s d=%d it=%d %s\n' % (w, d, it, time.strftime('%H:%M')) for w in new)
        extra += new
        print('  %d cut(s), length %d: %s' % (len(new), len(new[0]), ' '.join(new)), flush=True)
    print('RTU d=%d: done' % d)


def certify(d, ph, K):
    """A relaxed UNSAT with the block from bit K, checked as RLK's `cert` checks: kissat DRAT, drat-trim -L, cake_lpr
    (through the one-at-a-time lock wrapper). Certified words only (no RTU cuts)."""
    import hashlib
    import subprocess
    L, vis = 17, published(d, ph)
    forb = rlk.load_forbidden('44all' if ph == 0 else '44allp1') + rlk.load_cuts(ph, 40)
    inst = rlk.Relaxed(d, L, ph, forb)
    inst.cl.append([(-v if b == '1' else v) for v, b in list(zip(inst.vis, vis))[K:]])
    base = os.path.join(rlk.DIR, 'rtu_cert_d%d_p%d_K%d' % (d, ph, K))
    text = 'p cnf %d %d\n' % (inst.nv, len(inst.cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in inst.cl)
    open(base + '.cnf', 'w').write(text)
    sha = hashlib.sha256(text.encode()).hexdigest()[:16]
    t0 = time.time()
    k = subprocess.run([rlk.KISSAT, '-q', '-f', '--no-binary', base + '.cnf', base + '.drat'], capture_output=True)
    t1 = time.time()
    verdict = 'UNKNOWN%d' % k.returncode
    if k.returncode == 10:
        verdict = 'SAT'
    elif k.returncode == 20:
        v = subprocess.run(['drat-trim', base + '.cnf', base + '.drat', '-L', base + '.lrat', '-t', '400000'],
                           capture_output=True, text=True)
        verdict = 'ELAB-FAILED'
        if 's VERIFIED' in [z.strip() for z in v.stdout.splitlines()]:
            os.unlink(base + '.drat')
            c = subprocess.run([os.path.expanduser('~/np-build/cake_lpr/cake_lpr'), '--CML_HEAP_SIZE=6000',
                                '--CML_STACK_SIZE=2000', base + '.cnf', base + '.lrat'], capture_output=True, text=True)
            verdict = 'VERIFIED-UNSAT' if 's VERIFIED UNSAT' in c.stdout else 'CAKE-FAILED'
    print('RTU cert d=%d phase %d K=%d (%d words): %s, cnf %s, solve %.0f s, check %.0f s' % (
        d, ph, K, len(forb), verdict, sha, t1 - t0, time.time() - t1), flush=True)


if __name__ == '__main__':
    if sys.argv[1] == 'cert':
        certify(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    else:
        main()
