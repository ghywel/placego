#!/usr/bin/env python3
"""rule30_cadical_certify.py: certify relaxed-record UNSATs without drat-trim: CaDiCaL writes an LRAT proof directly and
cake_lpr (the formally verified CakeML checker) checks it. RULE30-PRIZE.md 8.96 leans on two kinds of kissat verdict:
R_real(132) = 17 (L = 18 UNSAT, both phases) and R_real(125) <= 23 (L = 24 UNSAT, both phases). drat-trim is not on
the M5 (reference memory, 2026-10-12), and rebuilding it means downloading source; CaDiCaL 3.0.1 (installed) writes
LRAT with --lrat --no-binary, which is what cake_lpr reads, so the pipeline needs no new code from outside.

The instance is exactly RTU's and rule30_r125_bound.py's: RLK's relaxed model (rule30_relaxed_records_k.Relaxed) at
(d, L, phase) with the certified minimal forbidden words to 44 (mfw44all / mfw44allp1) and the verified cuts40, and no
extra clause. Its CNF's SHA-256 is printed so a reader can rebuild and compare.

RUN-ON:     cpu, one instance at a time (cake_lpr peaks near 8 GB through its lock wrapper)
COMMAND:    python3 tests/probes/lexicon/rule30_cadical_certify.py controls
            python3 tests/probes/lexicon/rule30_cadical_certify.py D L PHASE [CAP=10800]
COST:       the controls take seconds; each deep instance is a CaDiCaL solve (kissat took 20 to 24 minutes at d = 125,
            L = 24) plus the check.

Record searched (record_find): 'cake_lpr' -> the certificate pipeline (kissat, drat-trim -L, cake_lpr) across the probes
and reference notes; 'cadical' and 'lrat' -> CaDiCaL used as a second solver, never as the proof writer.

PREDICTIONS (written 2026-10-13 14:27 BST, before any run).
  K1 must hold: the control UNSAT formula (x, not x or y, not y) is VERIFIED UNSAT by cake_lpr from CaDiCaL's LRAT.
  K2 must fail (the check can say no): the same proof with one hint list corrupted is rejected by cake_lpr.
  K3 blind (0.6): d = 125, L = 24 in both phases and d = 132, L = 18 in both phases are each VERIFIED UNSAT within the
     cap. REFUTED-BY: a SAT (that would contradict a kissat UNSAT and mean an encoding difference), CAKE-FAILED, or a cap.
ADDENDUM PREDICTION (2026-10-13 15:40 BST, before the run): the pipeline as a decider at the open depths. 143 and
  145 .. 150 are open at 18: kissat with CUT rounds ended UNKNOWN at 14,400 s on a machine carrying 10 to 13 solvers
  (rule30_relaxed_records_k.py CUT-P26). CaDiCaL settled d = 132, L = 18, phase 0 here in 1,531 s, where kissat had taken
  5,078 s under load. Record searched (record_find): 'R_real\(143\)' -> 0 hits; '143' 'open at 18' -> 4 hits in 4 files
  (PERIOD-TWO 6, RULE30-PRIZE summary, CUT-P26, NOW.md); '145\.\.150' -> 2 hits (the summary, NOW.md).
  K4 blind (0.5): d = 143, L = 18, phase 0 is VERIFIED-UNSAT within a 4-hour cap (sampled R_real(143) >= 17, so with
     phase 1 it would be exact at 17). REFUTED-BY: SAT (then lifted with rule30_r125_bound.py), a cap, or CAKE-FAILED.
     Counterfactual: a cap here, on a machine carrying four solvers, says the instance is hard, not the old load.
ADDENDUM PREDICTION (2026-10-13 16:14 BST, before the run): certify R_real(125) = 21 (8.96's kissat value). Record
  searched (record_find): 'R_real\(125\) = 21' -> 2 hits in 2 files (8.96 and rule30_r125_bound.py P3); 'L = 22' with
  'cake_lpr' -> 2 hits in 2 files (the same, uncertified).
  K5 blind (0.8): d = 125, L = 22 is VERIFIED-UNSAT in both phases (phase 0 first) within 3-hour caps. REFUTED-BY: SAT
     (contradicting kissat), a cap, or CAKE-FAILED.
ADDENDUM PREDICTION (2026-10-13 16:22 BST, before the run): the next open depth, run beside 143. Record searched: as
  for K4 ('145\.\.150' -> 2 hits; CUT-P26 read: 145 was UNKNOWN at 14,400 s under load; sampled R_real(145) >= 16).
  K6 blind (0.45): d = 145, L = 18, phase 0 is VERIFIED-UNSAT within a 4-hour cap. REFUTED-BY: SAT (then lifted), a
     cap, or CAKE-FAILED.
ADDENDUM PREDICTION (2026-10-13 17:25 BST, before the run): K4 held in phase 0 (below), so the other phase.
  K7 blind (0.6): d = 143, L = 18, phase 1 is VERIFIED-UNSAT within a 4-hour cap; with the sampled witness of 17,
     R_real(143) = 17 exactly, certified. REFUTED-BY: SAT (then lifted), a cap, or CAKE-FAILED.
ADDENDUM PREDICTION (2026-10-13 18:12 BST, before the run): the next open depth at 18. Record searched: as for K4
  (CUT-P26: 146 was stopped before its solve; sampled R_real(146) >= 15).
  K8 blind (0.6): d = 146, L = 18, phase 0 is VERIFIED-UNSAT within a 4-hour cap. REFUTED-BY: SAT (then lifted), a
     cap, or CAKE-FAILED.
ADDENDUM PREDICTION (2026-10-13 18:21 BST, before the run): K6 held in phase 0 (below), so the other phase.
  K9 blind (0.6): d = 145, L = 18, phase 1 is VERIFIED-UNSAT within a 4-hour cap; then R_real(145) <= 17 (sampled 16).
     REFUTED-BY: SAT (then lifted), a cap, or CAKE-FAILED.
ADDENDUM PREDICTION (2026-10-13 19:30 BST, before the run): the next open depth at 18. Record searched: as for K4
  (CUT-P26: 147 UNKNOWN at 14,400 s under load; sampled R_real(147) >= 17).
  K10 blind (0.6): d = 147, L = 18, phase 0 is VERIFIED-UNSAT within a 4-hour cap. REFUTED-BY: SAT (then lifted), a
     cap, or CAKE-FAILED.

OUTCOME (2026-10-13, M5; machine output quoted): K1 HELD, K2 HELD, K3 HELD, K5 HELD, K4 HELD, K6 HELD, K7 HELD; K8, K9
  pending.
  K10 REFUTED (19:56): d=147 L=18 phase 0 (1156 words): SAT; cnf sha256
     50dbbbab61db226b0a6eb7c4b89b11d47ea64ec59823fc8a9ae1a56682e631e2; solve 1544 s. A relaxed SAT: lifted (or not) by
     rule30_cadical_lift.py; its partial LRAT (12.2 GB) was deleted.
  K7 (19:03): d=143 L=18 phase 1 (1226 words): VERIFIED-UNSAT; cnf sha256
     d0b5d054a7d4c11382864a0b401f376ed46f40d6a804035f0847c285a8a0db49; solve 4545 s, check 1349 s, lrat 29806.7 MB. With
     K4 and the sampled witness of 17 (SP, second-party), R_real(143) = 17 exactly, certified in both phases.
  K6 (18:20): d=145 L=18 phase 0 (1156 words): VERIFIED-UNSAT; cnf sha256
     5f81c4c71c57a1b339ae5a2c35aabd5b84ad85d45f05de258da2277790d53991; solve 5402 s, check 1343 s, lrat 33525.2 MB.
  K4 (17:23): d=143 L=18 phase 0 (1156 words): VERIFIED-UNSAT; cnf sha256
     27441f21cfc6b09bbcbafed1f4426784c4a1a73a0ce42bdf3d0128e072a8ebb6; solve 4902 s, check 1273 s, lrat 30353.6 MB.
  K5 (17:04): d=125 L=22 phase 0: VERIFIED-UNSAT, cnf sha256
     cce48cd7ebaef27bbb879832fbf287f498cb07bd0040b4c5f4cc7a579a7acf08, solve 1116 s, check 359 s, lrat 9791.4 MB;
     phase 1: VERIFIED-UNSAT, cnf sha256 41859aa2069b24da68ecb66108b24908926be1168b6547988f5de1e32b6e5722, solve 1121 s,
     check 357 s, lrat 9741.1 MB. With the lifted band of 21, R_real(125) = 21 is certified.
  K1, K2: the control proof is VERIFIED UNSAT, and the copy with one hint removed is rejected.
  K3: all four VERIFIED-UNSAT (CaDiCaL 3.0.1 LRAT, cake_lpr through the lock wrapper; proofs deleted after the check,
     CNFs kept with their digests):
     d=125 L=24 phase 1 (1226 words): cnf sha256 9f25850d65e7e5ca3cebfa882a92f0ba3d208d7f2cf1d923a3ebf9965f8ec2f3;
       solve 966 s, check 297 s, lrat 10301.7 MB
     d=125 L=24 phase 0 (1156 words): cnf sha256 c45d3ae480eee84403314562ad4d41816e528357e5aef956a9f37257506a0e6c;
       solve 851 s, check 262 s, lrat 9447.6 MB
     d=132 L=18 phase 0 (1156 words): cnf sha256 b01a50772ef5001b31f3e8d1c03f8c5fe8327cfa10c1fc8f8b53f970fc493875;
       solve 1531 s, check 429 s, lrat 14598.0 MB
     d=132 L=18 phase 1 (1226 words): cnf sha256 87e50000964b00f9c073edab62a37f303aaee1ab8762129b0fc15c7d7c8b458e;
       solve 1865 s, check 494 s, lrat 13729.1 MB
"""
import hashlib, os, subprocess, sys, tempfile, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule30_relaxed_records_k as rlk                                 # noqa: E402

CAKE = os.path.expanduser("~/np-build/cake_lpr/cake_lpr")
CADICAL = "cadical"

def cake(cnf, lrat):
    c = subprocess.run([CAKE, "--CML_HEAP_SIZE=6000", "--CML_STACK_SIZE=2000", cnf, lrat], capture_output=True, text=True)
    return "s VERIFIED UNSAT" in c.stdout

def controls():
    d = tempfile.mkdtemp()
    cnf = os.path.join(d, "c.cnf"); lrat = os.path.join(d, "c.lrat")
    open(cnf, "w").write("p cnf 2 3\n1 0\n-1 2 0\n-2 0\n")
    r = subprocess.run([CADICAL, "-q", "--lrat", "--no-binary", cnf, lrat], capture_output=True, text=True)
    print("control solve exit", r.returncode, "(20 = UNSAT)")
    k1 = r.returncode == 20 and cake(cnf, lrat)
    lines = open(lrat).read().splitlines()
    bad = os.path.join(d, "bad.lrat")
    out = []
    for line in lines:                              # corrupt the first addition step's hints: drop its last hint
        parts = line.split()
        if out == [] and len(parts) >= 4 and parts[1] != "d":
            z = parts.index("0")                    # "id lits 0 hints 0": remove the first hint after the lits
            if len(parts) > z + 2:
                parts = parts[:z + 1] + parts[z + 2:]
            line = " ".join(parts); out.append(line); continue
        out.append(line)
    open(bad, "w").write("\n".join(out) + "\n")
    k2_rejected = not cake(cnf, bad)
    print("K1 control proof VERIFIED:", k1, "| K2 corrupted proof rejected:", k2_rejected)
    print("lrat:", lines, "| corrupted:", out)
    return k1, k2_rejected

def certify(d, L, ph, cap):
    forb = rlk.load_forbidden("44all" if ph == 0 else "44allp1") + rlk.load_cuts(ph, 40)
    inst = rlk.Relaxed(d, L, ph, forb)
    base = os.path.join(rlk.DIR, "cad_cert_d%d_L%d_p%d" % (d, L, ph))
    text = "p cnf %d %d\n" % (inst.nv, len(inst.cl)) + "".join(" ".join(map(str, c)) + " 0\n" for c in inst.cl)
    open(base + ".cnf", "w").write(text)
    sha = hashlib.sha256(text.encode()).hexdigest()
    t0 = time.time()
    r = subprocess.run([CADICAL, "-q", "-t", str(cap), "--lrat", "--no-binary", base + ".cnf", base + ".lrat"],
                       capture_output=True, text=True)
    t1 = time.time()
    verdict = {10: "SAT", 20: "UNSAT"}.get(r.returncode, "UNKNOWN%d" % r.returncode)
    size = os.path.getsize(base + ".lrat") if os.path.exists(base + ".lrat") else 0
    if verdict == "UNSAT":
        verdict = "VERIFIED-UNSAT" if cake(base + ".cnf", base + ".lrat") else "CAKE-FAILED"
    if verdict == "VERIFIED-UNSAT" and os.path.exists(base + ".lrat"):
        os.unlink(base + ".lrat")                   # keep the CNF and its digest; the proof is regenerable
    print("CERT d=%d L=%d phase %d (%d words): %s; cnf sha256 %s; solve %.0f s, check %.0f s, lrat %.1f MB"
          % (d, L, ph, len(forb), verdict, sha, t1 - t0, time.time() - t1, size / 1e6), flush=True)
    return verdict

if __name__ == "__main__":
    if sys.argv[1] == "controls":
        controls()
    else:
        certify(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]) if len(sys.argv) > 4 else 10800)
