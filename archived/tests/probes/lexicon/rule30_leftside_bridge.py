#!/usr/bin/env python3
"""rule30_leftside_bridge.py: the left horizon and the records are one quantity (RULE30-PRIZE.md 8.94, addendum 2).

Through 8.39's wall form, R(d) is (first failing odd time) + 1 - d, maximised over rows white from depth d on, which
are the white-start left seeds of width at most d - 1. So
    R(d)  + d - 1 = max over W <= d - 1 of H_L(W) in the white-start phase  (wall 01, phase 0, condition at odd times),
    R°(d) + d - 1 = max over W <= d - 1 of H_L(W) in the black-start phase  (wall 01, phase 1, condition at even times,
                     GC1043's phase-correct game; 8.82's R°).
This replays the comparison with three independent engines: records.c (the anti-diagonal forced walk, 8.36), the
survivor census leftside_survivors.c (8.94), and KIMI-QUESTIONS-3.md's brute-force R°(1..12).

RUN-ON:     cpu, 10 threads (OpenMP; ompflags.py)
COMMAND:    python3 tests/probes/lexicon/rule30_leftside_bridge.py [DMAX=33]
COST:       a few minutes (records.c to depth 33 dominates).

Record searched: 'wall form', 'R(d)', 'R°', 'black-even' -> 8.36, 8.39 (WA2: wall run = R(d), d = 3..27), 8.82 (R° by
lane q2; R°(1..62) third-party, "largest excess 7 at d = 12 only"), GC1043, KIMI-QUESTIONS-3.md (R°(1..12)).

PREDICTIONS (2026-10-13; B1 to 27 and B2 were already seen in the session, so they are replays; B1 beyond 27 and B3
are new).
  B1 must hold: R(d) + d - 1 equals the white-start prefix maximum at every d = 3 .. DMAX (records.c).
  B2 must hold: R°(d) + d - 1 equals the black-start prefix maximum for d = 1 .. 12 (KIMI-QUESTIONS-3.md's table).
  B3 must hold if 8.82's third-party summary is right: the census-derived R°(d) - d is at most 6 for every
     d = 1 .. DMAX other than 12, and is 7 at d = 12.
  C  cap alarm: the census's maximum stays below its cap of 90.

OUTCOME (2026-10-13, M5, a few minutes; machine output quoted): B1 HELD, B2 HELD, B3 HELD, C HELD.
  B1: records.c's R(d) equals the white-start bridge at all 31 depths d = 3 .. 33 (R(28 .. 33) = 16, 19, 20, 23, 24, 33).
  B2: the black-start bridge reproduces KIMI-QUESTIONS-3.md's R°(1 .. 12) = 0, 1, 4, 3, 2, 3, 4, 5, 4, 9, 8, 19.
  B3: the census-derived R°(d) - d for d = 1 .. 33 is -1, -1, 1, -1, -3, -3, -3, -3, -5, -1, -3, 7, 5, 3, 3, 1, -1, -3,
      -5, -1, -3, -5, -5, -7, -7, -7, -9, -7, -9, -11, -9, 3, 1: at most 6 except 7 at d = 12, as 8.82's summary says.
  Post hoc: the census's +13 jumps (black start, W = 11 and 31) are R°(12) = 19 and R°(32) = 35, the black-start
  record peaks; 8.82 traces the first to its coupling's black-run term ("both record peaks are one black run").
"""
import pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ompflags import OMP

RCIRC_KIMI = [0, 1, 4, 3, 2, 3, 4, 5, 4, 9, 8, 19]          # R°(1 .. 12), KIMI-QUESTIONS-3.md

def main():
    dmax = int(sys.argv[1]) if len(sys.argv) > 1 else 33
    tmp = pathlib.Path(tempfile.mkdtemp())
    arch = ["-mcpu=native"] if sys.platform == "darwin" else ["-march=native"]
    subprocess.run(["cc", "-O3", *arch, *OMP, "-o", str(tmp / "ls"), str(HERE / "leftside_survivors.c")], check=True)
    subprocess.run(["cc", "-O2", *OMP, "-o", str(tmp / "records"), str(HERE / "records.c")], check=True)
    out = subprocess.run([str(tmp / "ls"), "01", "0", str(dmax - 1), "90", "10"], capture_output=True, text=True,
                         check=True).stdout
    H = {}
    for line in out.splitlines():
        head, _, body = line.partition(":"); _, _, W, ph = head.split()
        H[(int(W), int(ph))] = max(int(x.split()[0]) for x in body.strip().strip(",").split(",") if x.strip())
    pm = lambda ph, d: max(H[(W, ph)] for W in range(0, d))
    ok = {}
    b1 = True
    for d in range(3, dmax + 1):
        R = int(subprocess.run([str(tmp / "records"), str(d), "0"], capture_output=True, text=True,
                               check=True).stdout.split()[2])
        Rc = pm(1, d) - (d - 1)
        print(f"  d={d:2d}: R(d) records.c {R:2d}, white-start bridge {pm(0, d) - (d - 1):2d};  R°(d) from the census {Rc:2d}"
              f"  (R° - d = {Rc - d:+d})", flush=True)
        b1 &= R + d - 1 == pm(0, d)
    ok["B1"] = b1
    ok["B2"] = all(RCIRC_KIMI[d - 1] + d - 1 == pm(1, d) for d in range(1, 13))
    exc = {d: pm(1, d) - (d - 1) - d for d in range(1, dmax + 1)}
    ok["B3"] = exc[12] == 7 and all(v <= 6 for d, v in exc.items() if d != 12)
    ok["C"] = max(H.values()) < 90
    print("  R°(d) - d, d = 1 ..", dmax, ":", [exc[d] for d in range(1, dmax + 1)])
    print("\n" + "  ".join(f"{k} {'HELD' if v else 'FAILED'}" for k, v in ok.items()))
    print("ALL CHECKS PASS" if all(ok.values()) else "SOME CHECKS FAILED")

if __name__ == "__main__":
    main()
