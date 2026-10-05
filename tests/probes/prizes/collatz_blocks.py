#!/usr/bin/env python3
"""collatz_blocks.py: the Collatz avenue Rule 30 lacks: the state after the free bits is an explicit integer
(PRIZE-PROBLEMS.md section 7.2).

RUN-ON:     cpu (Python 3 and a C compiler; collatz_blocks.c; exact)
COMMAND:    python3 tests/probes/prizes/collatz_blocks.py [W=26] [JMAX=12]
COST:       under a minute on one core.

Background (section 7.1). For a w-bit number n = 2^(w-1) + r, Terras's affine formula gives, after the w - 1 free
steps, T^(w-1)(n) = 3^a + T^(w-1)(r), with a the number of odd steps. Call it y. Its low j bits fix the next j
parities (Terras again). So "past the free bits the count follows the coin" is exactly the statement that y mod 2^j
is close to uniform over the numbers still above their start: an equidistribution question about explicit
integers, open to exponential sums (Tao's method, 2019, used the 3-adic analogue for "almost all" orbits). Rule
30's right part has no such formula. The random baselines for M samples in K = 2^j bins: total-variation distance
about sqrt(K / (2 pi M)); the largest odd Fourier coefficient about sqrt(ln K / M).

PREDICTIONS, written 2026-10-05 before this script's first run:
  CB0 (control, must hold): the affine formula holds for every n, at w = 20, 22, 24 and W.
  CB1 (blind): at w = W, over all n, the TV distance of y mod 2^j from uniform is at most 3 times the random
      baseline for every j from 1 to JMAX.
  CB2 (blind): the same over the survivors (orbits that stayed >= n for the w - 1 free steps).
  CB3 (blind; the Fourier route): at w = W, over the survivors, the largest odd Fourier coefficient of y mod 2^j is
      at most 4 times sqrt(ln 2^j / M) for every j from 1 to JMAX.
  CB4 (counterfactual, must fail to be uniform): y mod 3 over the survivors has TV distance above 0.1 (every odd
      step lands on 2 mod 3, so the arithmetic must show).
REFUTED-BY: CB0 failing (the instrument); CB1 to CB3 failing; CB4 coming out uniform (the instrument blind).
"""
import math, pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
W = int(sys.argv[1]) if len(sys.argv) > 1 else 26
JMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 12
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def run(exe, w):
    out = subprocess.run([str(exe), str(w), str(JMAX)], check=True, capture_output=True, text=True).stdout
    B, m3, ok = {}, None, False
    for line in out.split("\n"):
        f = line.split()
        if f and f[0] == "B":
            B[int(f[1])] = (int(f[2]), float(f[3]), float(f[4]), int(f[5]), float(f[6]), float(f[7]))
        elif f and f[0] == "M3":
            m3 = (float(f[1]), float(f[2]))
        elif f and f[0] == "AFFINE":
            ok = f[1] == "ok"
    return B, m3, ok


def main():
    exe = pathlib.Path(tempfile.gettempdir()) / "collatz_blocks_c"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "collatz_blocks.c"), "-lm"], check=True)
    oks = []
    for w in (20, 22, 24):
        oks.append(run(exe, w)[2])
    B, m3, okW = run(exe, W)
    report("CB0 Terras's affine formula holds for every n at w = 20, 22, 24 and W", all(oks) and okW)
    print(f"   w = {W}: {B[1][0]} numbers, {B[1][3]} survivors after {W - 1} steps")
    print("   j   TV all / baseline   TV surv / baseline   F surv / baseline")
    r1, r2, r3 = [], [], []
    for j in range(1, JMAX + 1):
        Ma, ta, fa, Ms, ts, fs = B[j]
        K = 2 ** j
        ba, bs, bf = math.sqrt(K / (2 * math.pi * Ma)), math.sqrt(K / (2 * math.pi * Ms)), math.sqrt(math.log(K) / Ms)
        r1.append(ta / ba); r2.append(ts / bs); r3.append(fs / bf)
        print(f"   {j:2d}  {ta / ba:8.2f}            {ts / bs:8.2f}             {fs / bf:8.2f}")
    verdict("CB1 TV over all n within 3 times the random baseline, j = 1 .. JMAX", all(x <= 3 for x in r1),
            f"largest {max(r1):.2f}")
    verdict("CB2 TV over survivors within 3 times the baseline", all(x <= 3 for x in r2), f"largest {max(r2):.2f}")
    verdict("CB3 Fourier over survivors within 4 times the baseline", all(x <= 4 for x in r3), f"largest {max(r3):.2f}")
    verdict("CB4 y mod 3 over survivors is far from uniform (TV > 0.1)", m3[1] > 0.1, f"TV {m3[1]:.3f} (all n: {m3[0]:.3f})")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
