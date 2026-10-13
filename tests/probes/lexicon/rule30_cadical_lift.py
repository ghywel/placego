#!/usr/bin/env python3
"""rule30_cadical_lift.py: lift a relaxed-SAT verdict of rule30_cadical_certify.py to a real witness, with CaDiCaL as the
solver (kissat had reached its 4-hour cap at 147 under load, CUT-P26; CaDiCaL found SAT at d = 147, L = 18, phase 0 in
1,544 s, K10).

The model is RLK's relaxed model (rule30_relaxed_records_k.Relaxed, certified words to 44 and cuts40, the same CNF as
the certify run, compared by SHA-256). A relaxed model is checked by RLK's own simulation (Relaxed.check), then lifted as
CUT and RTU do: right_half_for(code) finds a right half producing the visible code (kissat, as in RLK), and
simulate_glued runs the glued configuration for T = d + L - 1 steps. A VALID lift is a real band of L at depth d.
If membership is UNSAT (no right half produces the code), the model is an artefact of the relaxation: the code and its
shortest absent factor (a cut candidate, which must then be certified) are reported. If membership is SAT, the glued
replay must be VALID by the reviewed join (GC549.16/22, GPT's GC1201 audit); a FAILED replay after membership SAT would
be an instrument, model or horizon mismatch, never a language-absence result. The relaxed model is saved (RLK's
save_model) right after Relaxed.check and before membership, so an interruption needs no re-solve (GC1201; added after
the first run started, which was already in its solve).

RUN-ON:     cpu; one CaDiCaL solve plus kissat for the right half.
COMMAND:    KISSAT=kissat python3 tests/probes/lexicon/rule30_cadical_lift.py D L PHASE [CAP=7200]

Record searched (record_find, 2026-10-13 20:02 BST): 'R_real\\(147\\)' -> 3 hits in 2 files (K10 in rule30_cadical_certify.py and
this file);
'lift' -> 819 hits in 160 files (the generic word; RLK's lift, CUT and RTU read). CUT-P26 in rule30_relaxed_records_k.py
read (147 UNKNOWN at 14,400 s; sampled R_real(147) >= 17).

PREDICTIONS (written 2026-10-13 20:02 BST, before the run).
  L1 must hold (the instrument): the CNF built here has the certify run's SHA-256
     50dbbbab61db226b0a6eb7c4b89b11d47ea64ec59823fc8a9ae1a56682e631e2, and the CaDiCaL model passes Relaxed.check.
  L2 blind (0.4): the model lifts (glued simulation VALID), so R_real(147) >= 18 and the 18s extend past 141.
     REFUTED-BY: no right half for the code (membership UNSAT); then the code and its shortest absent factor are
     reported, a cut candidate to certify before any rerun. (Wording corrected 20:25 BST after GPT's GC1201: a failed
     glued replay after membership SAT is a mismatch to fix, not a refutation.)

OUTCOME: (filled in after the run, below this line)
"""
import hashlib, os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule30_relaxed_records_k as rlk                                 # noqa: E402


def main():
    d, L, ph = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    cap = int(sys.argv[4]) if len(sys.argv) > 4 else 7200
    forb = rlk.load_forbidden('44all' if ph == 0 else '44allp1') + rlk.load_cuts(ph, 40)
    inst = rlk.Relaxed(d, L, ph, forb)
    text = 'p cnf %d %d\n' % (inst.nv, len(inst.cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in inst.cl)
    sha = hashlib.sha256(text.encode()).hexdigest()
    name = os.path.join(rlk.DIR, 'lift_d%d_L%d_p%d.cnf' % (d, L, ph))
    open(name, 'w').write(text)
    print('LIFT d=%d L=%d phase %d: cnf sha256 %s' % (d, L, ph, sha), flush=True)
    t0 = time.time()
    p = subprocess.run(['cadical', '-q', '-t', str(cap), name], capture_output=True, text=True)
    print('LIFT solve exit %d in %.0f s' % (p.returncode, time.time() - t0), flush=True)
    if p.returncode != 10:
        print('LIFT: not SAT (exit %d); nothing to lift' % p.returncode)
        return
    m = set()
    for line in p.stdout.splitlines():
        if line.startswith('v'):
            m.update(int(z) for z in line.split()[1:] if int(z) > 0)
    inst.check(m, forb)                                               # raises if the model is not a relaxed model
    code = inst.code
    saved = rlk.save_model(inst, d, L, ph, 'cadical_lift')            # before membership (GC1201)
    print('LIFT relaxed model checked; visible code %s; saved %s' % (code, os.path.basename(saved)), flush=True)
    right = rlk.right_half_for(code, ph)
    if right is None:
        print('LIFT: no right half produces the code (outside the real language); shortest absent factors:',
              rlk.shortest_absent(code, ph, 2)[:4])
        return
    ok, why = rlk.simulate_glued(inst.left0, right, inst.T, ph, d, L, code)
    print('LIFT glued simulation: %s (%s)%s' % ('VALID' if ok else 'FAILED', why,
                                                '' if ok else ' -- membership was SAT, so this is a MISMATCH to fix'))
    if ok:
        left = ''.join(str(inst.left0.get(-j, 0)) for j in range(1, inst.T + 1))
        rgt = ''.join(str(right[i]) for i in sorted(right))
        print('LIFT witness: left (depths 1..T) %s' % left)
        print('LIFT witness: right (sites 1..) %s' % rgt)


if __name__ == '__main__':
    main()
