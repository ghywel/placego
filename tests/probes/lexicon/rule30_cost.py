#!/usr/bin/env python3
"""rule30_cost.py: what the seed's right part pays per condition, position by position (RULE30-PRIZE.md section
8.52; the cost side of PERIOD-TWO.md section 7, question 1).

RUN-ON:     cpu (Python 3 and a C compiler; count_j.c counts; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_cost.py [WMAX=22]
COST:       under a minute on one core.

Background (section 8.51). N_{w,j}(T) counts the configurations of exact hull width w whose column 0, at distance j
from the hull's left end, reads 0101... (either phase) at times 0 .. T-1. The lemma of section 8.51: for T <= j the
count halves exactly at every step (the seed's left part pays one bit per condition, by left-permutivity). From
T = j on, every condition must be paid by the right part. The step ratio rho(w, j, T) = N_{w,j}(T+1) / N_{w,j}(T)
for T >= j is what the right part pays. If it is bounded below 1 at every single step, the cost side is a per-step
statement, the kind an induction proves; if not, it holds only on average.

PREDICTIONS, written 2026-10-05 before this script's first run (word 0101..., both phases):
  CJ0 (control, must hold): summed over j, N_{w,j}(T) equals count.c's N_w(T) for w = 12 .. 18; and the lemma holds
      exactly: N_{w,j}(T) = N_{w,j}(1) / 2^(T-1) for every T <= j, every j, every w up to WMAX.
  CJ1 (blind; per step): for w = 16 .. WMAX, every j and every T >= j with N_{w,j}(T) >= 256, rho <= 0.75.
  CJ2 (blind; on average): the mean of log2 rho over those steps lies between -1.2 and -0.9.
  CJ3 (blind; not exact): at least one of those steps has rho above 0.55, so the right part's cost is not exactly
      one bit at every step.
  CJ4 (counterfactual, the word 0, which Condrey's theorem closes): over the same steps, the word 0's largest rho
      is at most 0101's largest rho.
REFUTED-BY: CJ0 failing (the instrument); CJ1 to CJ4 failing.
"""
import math, pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 22
TMAX = 50
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def run(exe, wmin, wmax, word, per):
    out = subprocess.run([str(exe), str(wmin), str(wmax), str(TMAX), word, str(per)], check=True,
                         capture_output=True, text=True).stdout
    J, C = {}, {}
    for line in out.split("\n"):
        f = line.split()
        if f and f[0] == "J":
            J[(int(f[1]), int(f[2]), int(f[3]))] = int(f[4])
        elif f and f[0] == "C":
            C[(int(f[1]), int(f[2]))] = int(f[3])
    return J, C


def steps(J, wlo, whi):
    """(w, j, T, rho) for every right-paid step with N_{w,j}(T) >= 256."""
    out = []
    for (w, j, T), n in J.items():
        if wlo <= w <= whi and T >= max(j, 1) and n >= 256:
            out.append((w, j, T, J.get((w, j, T + 1), 0) / n))
    return out


def main():
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_cost_c"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "count_j.c")], check=True)
    w01 = "01" * 200
    J, C = run(exe, 1, WMAX, w01, 2)
    ok_sum = all(sum(J.get((w, j, T), 0) for j in range(w)) == C[(w, T)] for w in range(12, 19) for T in range(1, TMAX))
    ok_lem = all(J.get((w, j, T), 0) * 2 ** (T - 1) == J.get((w, j, 1), 0)
                 for w in range(1, WMAX + 1) for j in range(w) for T in range(1, j + 1))
    report("CJ0 the positions sum to count.c's totals, and the lemma holds exactly for T <= j", ok_sum and ok_lem,
           f"sums {'agree' if ok_sum else 'DIFFER'}; lemma {'exact' if ok_lem else 'BROKEN'}")
    st = steps(J, 16, WMAX)
    worst = max(st, key=lambda s: s[3])
    mean = sum(math.log2(s[3]) for s in st if s[3] > 0) / len([s for s in st if s[3] > 0])
    print(f"   0101: {len(st)} right-paid steps with N >= 256; largest rho {worst[3]:.3f} at w, j, T = {worst[:3]};"
          f" mean log2 rho {mean:.3f}")
    hist = {}
    for s in st:
        b = min(int(s[3] * 20), 19) / 20
        hist[b] = hist.get(b, 0) + 1
    print("   0101: rho histogram (lower edge: count): " + ", ".join(f"{b:.2f}: {c}" for b, c in sorted(hist.items())))
    for w in (WMAX,):
        for j in (2, w // 2, w - 3):
            row = [J.get((w, j, T), 0) for T in range(1, TMAX)]
            print(f"   0101, w = {w}, j = {j}: N for T = 1 ..: " + " ".join(str(n) for n in row if n))
    verdict("CJ1 rho <= 0.75 at every right-paid step", worst[3] <= 0.75, f"largest {worst[3]:.3f} at {worst[:3]}")
    verdict("CJ2 mean log2 rho between -1.2 and -0.9", -1.2 <= mean <= -0.9, f"{mean:.3f}")
    verdict("CJ3 some step has rho above 0.55", worst[3] > 0.55, f"largest {worst[3]:.3f}")
    J0, _ = run(exe, 1, WMAX, "0" * 400, 1)
    st0 = steps(J0, 16, WMAX)
    w0 = max(st0, key=lambda s: s[3]) if st0 else (0, 0, 0, 0.0)
    m0 = sum(math.log2(s[3]) for s in st0 if s[3] > 0) / max(1, len([s for s in st0 if s[3] > 0]))
    print(f"   word 0: {len(st0)} right-paid steps; largest rho {w0[3]:.3f} at {w0[:3]}; mean log2 rho {m0:.3f}")
    verdict("CJ4 the word 0's largest rho is at most 0101's", w0[3] <= worst[3], f"{w0[3]:.3f} against {worst[3]:.3f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
