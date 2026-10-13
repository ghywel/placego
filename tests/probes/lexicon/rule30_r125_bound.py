#!/usr/bin/env python3
"""rule30_r125_bound.py: is R_real(125) below 24? The open part of RULE30-PRIZE.md 8.96 (are the 18s at 125..131 one
run or several?).

A single zero run giving at least 18 at both 125 and 131 covers depths 125 .. 148, a band of 24 from depth 125, so it
needs R_real(125) >= 24 (the sampled bound is 21, a witness ending at 146). This asks RLK's relaxed model (the left
light cone exact; the right side replaced by the visible word avoiding every certified minimal forbidden word to 44
and the verified cuts40, exactly as RTU used it) for a white band at depths 125 .. 148, in one phase. Relaxed UNSAT is
sound for the real problem (the relaxation only adds configurations): UNSAT in both phases gives R_real(125) <= 23, so
125 .. 131 is at least two runs. Relaxed SAT is lifted (right_half_for and the glued simulation, as CUT and RTU do); a
valid lift is a real band of 24 at 125, and then one run can serve 125 .. 131.

RUN-ON:     cpu (kissat 4.0.4 as KISSAT; one phase a process)
COMMAND:    KISSAT=kissat python3 tests/probes/lexicon/rule30_r125_bound.py PHASE [CAP=7200] [D=125] [L=24]
COST:       unknown in advance; capped. drat-trim and cake_lpr are not installed on the M5 today, so an UNSAT here is a
            kissat verdict, uncertified, like the R_real(132) = 17 bound that 8.96 already leans on.

Record searched (record_find): 'R_real(125)' -> RECORD-MAP (125 >= 21 sampled; 125..131 >= 18 witnesses), STRATEGY-PLAN
section 1 (R_real(125) >= 21); 'RLK' -> 57 hits, the relaxed model and RTU (rule30_local_trace_unique.py).

PREDICTIONS (written 2026-10-13 13:47 BST, before either run).
  P1 blind (0.55): both phases come back relaxed UNSAT within the cap: R_real(125) <= 23 and the 18s at 125 .. 131 are
     at least two runs (so at least three across 125 .. 138). REFUTED-BY: a valid lift in either phase.
  P2 blind (0.3): a phase ends UNKNOWN at the cap.
  C  control (must hold): at L = 21, phase 1, the same model is SAT and the model lifts (the published 125 witness has
     a band of 21 in phase 1), so the encoding can say yes. Run with L = 21 before the main runs.

OUTCOME: (filled in after the runs, below this line)
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule30_relaxed_records_k as rlk                                 # noqa: E402

def main():
    ph = int(sys.argv[1]); cap = int(sys.argv[2]) if len(sys.argv) > 2 else 7200
    d = int(sys.argv[3]) if len(sys.argv) > 3 else 125; L = int(sys.argv[4]) if len(sys.argv) > 4 else 24
    forb = rlk.load_forbidden('44all' if ph == 0 else '44allp1') + rlk.load_cuts(ph, 40)
    inst = rlk.Relaxed(d, L, ph, forb)
    print(f"R125 d={d} L={L} phase {ph}: {len(forb)} certified words, cap {cap} s", flush=True)
    v = inst.solve(cap, forb)
    print(f"R125 d={d} L={L} phase {ph}: relaxed {v}", flush=True)
    if v == 'SAT':
        code = inst.code
        right = rlk.right_half_for(code, ph)
        if right:
            ok, why = rlk.simulate_glued(inst.left0, right, inst.T, ph, d, L, code)
            print(f"R125 d={d} L={L} phase {ph}: visible word {code}; lift {'VALID' if ok else 'FAILED ' + str(why)}", flush=True)
        else:
            print(f"R125 d={d} L={L} phase {ph}: visible word {code} has no right half (outside the real language)", flush=True)
    print(f"R125 d={d} L={L} phase {ph}: done", flush=True)

if __name__ == "__main__":
    main()
