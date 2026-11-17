#!/usr/bin/env python3
"""collatz_blocks.py: the Collatz avenue Rule 30 lacks: the state after the free bits is an explicit integer
(COLLATZ-PRIZE.md section 2).

RUN-ON:     cpu (Python 3 and a C compiler; collatz_blocks.c; exact)
COMMAND:    python3 tests/probes/prizes/collatz_blocks.py [W=26] [JMAX=12]   or   ... collatz_blocks.py scaling
COST:       under a minute on one core.

Background (COLLATZ-PRIZE.md section 1). For a w-bit number n = 2^(w-1) + r, Terras's affine formula gives, after
the w - 1 free steps, T^(w-1)(n) = 3^a + T^(w-1)(r), with a the number of odd steps. Call it y. Its low j bits fix
the next j parities (Terras again). So "past the free bits the count follows the coin" is exactly the statement that
y mod 2^j is close to uniform over the numbers still above their start: an equidistribution question about explicit
integers, open to exponential sums (Tao's method, 2019, used the 3-adic analogue for "almost all" orbits). Rule 30's
right part has no such formula. The random baselines for M samples in K = 2^j bins: total-variation distance about
sqrt(K / (2 pi M)); the largest odd Fourier coefficient about sqrt(ln K / M).

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

OUTCOME, 2026-10-05 (the first run, 10 seconds, W = 26: 33,554,432 numbers, 573,162 survivors after 25 steps):
  CB0 PASSED: the affine formula holds for every n at w = 20, 22, 24, 26.
  CB1 REFUTED: over all n the TV distance reaches 3.18 times the baseline at j = 12 (TV 0.014). A size effect: the
     orbits that dropped have small y, and small numbers are not uniform mod 2^12.
  CB2 HELD: over the survivors, TV is 0.41 to 1.09 times the random baseline at every j to 12.
  CB3 HELD: the largest odd Fourier coefficient is within 4 times the baseline (3.49 at j = 12).
  CB4 HELD: y mod 3 has TV 0.333 (it is never 0 mod 3).
  Post hoc (the binary run with a third argument "top", no prediction): the j = 12 and 13 coefficients are real
  structure, not noise. At w = 26, |F| = 0.0133 at h = 753 (j = 12) and 0.0116 at h = 6355 (j = 13), where random
  samples would give |F| that large with probability about e^-100. The frequency 1837 recurs (w = 24, j = 11; w = 26,
  j = 12 and 13). At w = 24 the same scales give 0.0166 and 0.0186: smaller at the larger width.

MODE scaling. The largest odd Fourier coefficient over survivors, F(w, j), at j = 10, 12, 14 for w = 20, 22, 24, 26,
28. The sampling-noise floor falls by about 0.5 in log2 per bit of w (the survivors double with each bit), so a
slope of log2 F near -0.5 means noise, near 0 a persistent structure, and between them a structure that fades.
PREDICTIONS for scaling, written 2026-10-05 before scaling's first run:
  CS0 (control, must hold): the affine formula holds at w = 28.
  CS1 (blind): at j = 12 and j = 14 the least-squares slope of log2 F against w (w = 20 .. 28) lies between -0.5
      and -0.1: a real structure that fades with width.
  CS2 (blind): at w = 28 and j = 12, F is more than 2 times the noise baseline sqrt(ln 2^j / M).

OUTCOME of scaling, 2026-10-05 (73 seconds). F at j = 10, 12, 14:
  w = 20 (14,990 survivors): 0.0454, 0.0528, 0.0521;  w = 22 (46,611): 0.0137, 0.0196, 0.0361;
  w = 24 (168,807): 0.0083, 0.0166, 0.0378;  w = 26 (573,162): 0.0045, 0.0133, 0.0074;
  w = 28 (1,762,293): 0.0022, 0.0036, 0.0071.
  CS0 PASSED.
  CS1 HELD: the slope of log2 F is -0.415 per bit at j = 12 and -0.401 at j = 14. The structure fades with width,
     nearly as fast as noise.
  CS2 REFUTED: at w = 28 and j = 12, F is 1.67 times the noise baseline, no longer detectable.
"""
import math, pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
W = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 26
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


def scaling(exe):
    global JMAX
    JMAX = 14
    F, ok28, M = {}, False, {}
    for w in (20, 22, 24, 26, 28):
        B, _, ok = run(exe, w)
        if w == 28:
            ok28 = ok
        for j in (10, 12, 14):
            F[(w, j)], M[w] = B[j][5], B[j][3]
        print(f"   w = {w}: survivors {M[w]}; F at j = 10, 12, 14: "
              + ", ".join(f"{F[(w, j)]:.5f}" for j in (10, 12, 14)), flush=True)
    report("CS0 the affine formula holds at w = 28", ok28)
    ws = (20, 22, 24, 26, 28)
    sl = {}
    for j in (12, 14):
        ys = [math.log2(F[(w, j)]) for w in ws]
        mx, my = sum(ws) / 5, sum(ys) / 5
        sl[j] = sum((w - mx) * (y - my) for w, y in zip(ws, ys)) / sum((w - mx) ** 2 for w in ws)
    print("   slope of log2 F per bit of w: " + ", ".join(f"j = {j}: {v:.3f}" for j, v in sl.items()))
    verdict("CS1 slope between -0.5 and -0.1 at j = 12 and 14", all(-0.5 <= v <= -0.1 for v in sl.values()),
            ", ".join(f"{v:.3f}" for v in sl.values()))
    ratio = F[(28, 12)] / math.sqrt(math.log(2 ** 12) / M[28])
    verdict("CS2 at w = 28, j = 12, F above 2 times the noise baseline", ratio > 2, f"{ratio:.2f} times")


def main():
    exe = pathlib.Path(tempfile.gettempdir()) / "collatz_blocks_c"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "collatz_blocks.c"), "-lm"], check=True)
    if len(sys.argv) > 1 and sys.argv[1] == "scaling":
        scaling(exe)
        return
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
