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

OUTCOME: (filled in after the runs, below this line)
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
