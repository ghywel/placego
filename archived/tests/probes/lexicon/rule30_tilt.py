#!/usr/bin/env python3
"""rule30_tilt.py: the owner's matter-antimatter question. Does Rule 30's coin tip?

RUN-ON:     cpu (tilt.c via cc, driven from Python 3 with the standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_tilt.py [LOGN=21] [CONTROLS=8]
COST:       a few minutes per run on one core (the runs go in parallel).

The owner (2026-10-05): "I am thinking of the universal problem of why there is more matter than antimatter. The coin
flip tips towards the matter side, and I believe the reason isn't known."
In physics, Sakharov's conditions (1967) for a matter excess are: a number that is not conserved, violation of C and
of CP, and departure from equilibrium. Rule 30 has all three. The number of black cells is not conserved. Swapping
colours gives a different rule (Rule 135), mirroring gives Rule 86, and both together give Rule 149. And the single seed
starts as far from balance as possible: one black cell in a white world. Yet 4 of its 8 outputs are black, and it maps
a row of fair coins to a row of fair coins (it is surjective), so a balanced state is preserved. Problem 2 asks
whether the centre column's colours balance in the long run, that is, whether Rule 30 makes any matter excess at all.
Wolfram's table (2019; PRIOR-ART.md) shows an excess of black at every decade from 10^4 to 10^9, of 64, 196, 1,536,
4,440, 19,952 and 50,076 cells: 0.6 to 2.0 standard deviations of a fair coin, always positive. Seen before writing
this: rule30_core.py's centre column over 131,072 steps has 139 more white than black, so the walk crossed zero after
10^5 at least once.
The test. A fair random walk and a tilted one differ in how the excess grows. A tilt makes it grow like n, and
long-range persistence like n^H with H above 1/2. Detrended fluctuation analysis (DFA) measures H from the column
itself. Controls: the centre column of Rule 30 run from a row of fair coins, whose rows are exactly fair coins at every
step. Any tilt or persistence specific to the single seed shows up against them.

PREDICTIONS, written 2026-10-05 before this script's first run (no exploratory run of tilt.c):
  TI0 (control, exact): the single seed's black counts after 10, 100, 1,000, 10,000, 100,000 and 1,000,000 steps are
      Wolfram's: 7, 52, 481, 5,032, 50,098 and 500,768.
  TI1 (blind; no persistence): the single seed's centre column has a DFA exponent between 0.45 and 0.55 over scales 16
      to 2^(LOGN-4), within 0.05 of the controls' mean.
  TI2 (blind; no tilt beyond chance): at N = 2^LOGN the single seed's excess, in units of the controls' standard
      deviation of the excess at N, lies within +-2.5.
REFUTED-BY: TI0 failing (the instrument); TI1 or TI2 failing.

OUTCOME of the first run, 2026-10-05 (LOGN = 21, 8 controls, 4 minutes 47 seconds): TI0 PASSED (7, 52, 481, 5,032,
50,098, 500,768, exactly Wolfram's). The single seed's excess of black over white at 2^10, 2^11, .., 2^21: -44, -44,
-40, +16, +170, +282, +218, -138, +634, +738, +1,376, +1,224. TI1 HELD: DFA exponent 0.5045 against the controls'
0.4905 to 0.5092 (mean 0.4992). TI2 HELD: the excess at 2^21 is +1,224 (+0.85 coin standard deviations; +0.85 of the
controls' RMS of 1,439, whose own excesses run from -2,224 to +1,558). The centre column's colour count is a fair
random walk, crossing zero and with no long memory. Wolfram's positive checkpoints from 10^4 to 10^9 are what such a
walk does when it happens to sit on one side. No tilt is seen, at the precision a walk of 2 million steps allows.
"""
import math, pathlib, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
LOGN = int(sys.argv[1]) if len(sys.argv) > 1 else 21
CONTROLS = int(sys.argv[2]) if len(sys.argv) > 2 else 8
N = 1 << LOGN
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def column(exe, mode, seed=0):
    out = subprocess.run([str(exe), str(N), str(mode), str(seed)], check=True, capture_output=True).stdout
    return [b - 48 for b in out]


def dfa(x, scales):
    """F(s) for each scale: the RMS residual of a linear fit to the profile in non-overlapping windows of s."""
    m = sum(x) / len(x)
    Y, acc = [], 0.0
    for v in x:
        acc += v - m
        Y.append(acc)
    P1, P2, Pi = [0.0], [0.0], [0.0]                   # prefix sums of Y, Y^2, i Y
    for i, y in enumerate(Y):
        P1.append(P1[-1] + y)
        P2.append(P2[-1] + y * y)
        Pi.append(Pi[-1] + i * y)
    F = {}
    for s in scales:
        su, suu = s * (s - 1) / 2, (s - 1) * s * (2 * s - 1) / 6
        sxx = suu - su * su / s
        tot, nw = 0.0, 0
        for a in range(0, len(Y) - s + 1, s):
            sy, syy = P1[a + s] - P1[a], P2[a + s] - P2[a]
            suy = (Pi[a + s] - Pi[a]) - a * sy
            sxy = suy - su * sy / s
            res = (syy - sy * sy / s) - sxy * sxy / sxx
            tot += res / s
            nw += 1
        F[s] = math.sqrt(tot / nw)
    return F


def slope(F):
    xs = [math.log2(s) for s in F]
    ys = [math.log2(v) for v in F.values()]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)


def main():
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_tilt"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "tilt.c")], check=True)
    with ThreadPoolExecutor(max_workers=CONTROLS + 1) as ex:
        jobs = [ex.submit(column, exe, 0)] + [ex.submit(column, exe, 1, k + 1) for k in range(CONTROLS)]
        cols = [j.result() for j in jobs]
    seed, ctrl = cols[0], cols[1:]
    want = {10: 7, 100: 52, 1000: 481, 10000: 5032, 100000: 50098, 1000000: 500768}
    got = {n: sum(seed[:n]) for n in want if n <= N}
    report("TI0 the single seed's black counts match Wolfram's table", got == {n: want[n] for n in got},
           ", ".join(f"{n}: {c}" for n, c in got.items()))
    ex_s = 2 * sum(seed) - N
    marks = [1 << k for k in range(10, LOGN + 1)]
    print("   single seed, excess of black over white at 2^10 .. 2^LOGN: "
          + ", ".join(f"{2 * sum(seed[:n]) - n:+d}" for n in marks), flush=True)
    scales = [1 << k for k in range(4, LOGN - 3)]
    h_s = slope(dfa(seed, scales))
    h_c = [slope(dfa(c, scales)) for c in ctrl]
    ex_c = [2 * sum(c) - N for c in ctrl]
    sd = math.sqrt(sum(e * e for e in ex_c) / len(ex_c))
    print(f"   DFA exponent: single seed {h_s:.4f}; controls " + ", ".join(f"{h:.4f}" for h in h_c), flush=True)
    print(f"   excess at N = {N}: single seed {ex_s:+d} ({ex_s / math.sqrt(N):+.2f} coin standard deviations); controls "
          + ", ".join(f"{e:+d}" for e in ex_c) + f" (RMS {sd:.0f}, {sd / math.sqrt(N):.2f} coin standard deviations)",
          flush=True)
    hm = sum(h_c) / len(h_c)
    verdict("TI1 no persistence: DFA exponent in [0.45, 0.55], within 0.05 of the controls'",
            0.45 <= h_s <= 0.55 and abs(h_s - hm) <= 0.05, f"{h_s:.4f} against {hm:.4f}")
    verdict("TI2 no tilt beyond chance: the excess within 2.5 of the controls' spread", abs(ex_s) <= 2.5 * sd,
            f"{ex_s / sd:+.2f} control standard deviations")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
