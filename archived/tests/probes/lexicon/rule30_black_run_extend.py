#!/usr/bin/env python3
"""rule30_black_run_extend.py: 8.95's black-run records beyond depth 40, against the bounds that would give the doubling
conjecture by 8.82's coupling (RULE30-PRIZE.md 8.95, addendum).

By the coupling, Q_B, P_B <= 2d + 5 and Q_S, P_S <= 2d + 8 at every depth give R(d) <= d + 4 and R°(d) <= d + 7 by
induction (8.82's c = max(beta_B, beta_S - 3), restated in 8.95 and offered to GPT as a tier-2 step in L659). This
extends the committed tables from 40 to DMAX with records_pattern.c and rechecks the coupling at the new depths.

RUN-ON:     cpu, 10 threads (OpenMP; ompflags.py)
COMMAND:    python3 tests/probes/lexicon/rule30_black_run_extend.py [DMIN=40] [DMAX=48]
COST:       minutes to an hour; each depth costs about 1.4 times the last.

PREDICTIONS (written 2026-10-13 13:25 BST, before the run; announced in the ledger entry that reports it).
  X1 blind: the black-run ends stay inside the bounds, Q_B, P_B <= 2d + 5 and Q_S, P_S <= 2d + 8, at d = 41 .. 48
     (the measured excess fell after d = 13, so I expect no new maximum). REFUTED-BY: one end beyond its bound.
  X2 must hold: both coupling identities are exact at d = 41 .. 48.
  C  cap alarm: no run reaches records_pattern.c's cap.

OUTCOME (2026-10-13, M5, about a minute; machine output quoted): X1 HELD, X2 HELD, C HELD.
  d = 41 .. 48: R = 37, 36, 35, 34, 43, 42, 41, 40; R° = 36, 37, 36, 35, 34, 41, 40, 39.
  Q_S = 76, 80, 80, 80, 80, 80, 88, 88; P_S = 74, 74, 76, 78, 78, 88, 84, 86;
  Q_B = 79, 79, 79, 79, 89, 89, 89, 89; P_B = 71, 77, 79, 75, 79, 75, 79, 89.
  Largest black-run end minus 2d: black start -1 (d = 45, bound +5), white start -4 (d = 42, 46, bound +8).
  Spot check against the frozen records.c: R(45) = 43 and R(48) = 40 agree.
"""
import pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ompflags import OMP

def main():
    dmin = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    dmax = int(sys.argv[2]) if len(sys.argv) > 2 else 48
    tmp = pathlib.Path(tempfile.mkdtemp())
    arch = ["-mcpu=native"] if sys.platform == "darwin" else ["-march=native"]
    subprocess.run(["cc", "-O3", *arch, *OMP, "-o", str(tmp / "rp"), str(HERE / "records_pattern.c")], check=True)
    caps = []
    def run(ph, mode, d):
        out = subprocess.run([str(tmp / "rp"), str(ph), mode, str(d), "10"], capture_output=True, text=True,
                             check=True).stdout.split()
        if len(out) > 6 and out[6] == "CAP": caps.append((ph, mode, d))
        return int(out[4])
    E, Q, P = {}, {}, {}
    ok = {"X1": True, "X2": True}
    for d in range(dmin, dmax + 1):
        for ph in (0, 1):
            E[(ph, d)] = run(ph, "Z", d); Q[(ph, d)] = run(ph, "Q", d); P[(ph, d)] = run(ph, "P", d)
        line = f"d={d}: R={E[(0, d)] - d} R°={E[(1, d)] - d}  Q_S={Q[(0, d)]} P_S={P[(0, d)]} Q_B={Q[(1, d)]} P_B={P[(1, d)]}"
        if d > dmin:
            for ph, other in ((1, 0), (0, 1)):
                m = max(d, E[(other, d - 1)] - 1, Q[(other, d)] - 1, P[(other, d)] - 1)
                ok["X2"] &= m == E[(ph, d)]
            ok["X1"] &= max(Q[(1, d)], P[(1, d)]) <= 2 * d + 5 and max(Q[(0, d)], P[(0, d)]) <= 2 * d + 8
            line += (f"  excess: B {max(Q[(1, d)], P[(1, d)]) - 2 * d:+d} (bound +5), S {max(Q[(0, d)], P[(0, d)]) - 2 * d:+d}"
                     f" (bound +8)")
        print(line, flush=True)
    ok["C"] = not caps
    print("\n" + "  ".join(f"{k} {'HELD' if v else 'FAILED'}" for k, v in ok.items()))

if __name__ == "__main__":
    main()
