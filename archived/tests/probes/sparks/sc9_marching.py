#!/usr/bin/env python3
"""sc9_marching.py: spark SC9 (SPARKS.md). A beat for many feet.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/sparks/sc9_marching.py
COST:       about a minute.

Model: 30 walkers in single file, target gap d0 = 1 m, base speed v0 = 0.75 m stride x 2 steps a second; each walker
has a personal cadence and a personal stride, each 3 per cent (standard deviation) from the mean, and 1 per cent
jitter per half-second tick; 1,000 ticks; 200 runs per condition. A shared beat sets every cadence to the mean.
Following: walker i > 0 scales its speed by 1 + k (gap it saw tau seconds ago - d0) / d0, k = 0.5, clipped to
[0.2, 2] v0. The linear theory of this model (first-order following with a delay) says ripples in the gaps grow
down the column exactly when (k v0 / d0) tau > 1/2.
Predictions (published in SPARKS.md before this ran): (1) without following, a shared beat cuts the spread of the
column's change in length by a factor between 1.2 and 1.7; (2) following with tau = 0.5 s keeps the back's gap
ripple within 1.2 times the front's; (3) following with tau = 1 s makes it at least twice the front's.
Fail: a factor above 3 or below 1.1 in (1), or (2) and (3) failing together.
Control: with no variability and no jitter, every gap stays exactly 1 m.
"""
import math, random, statistics

N, D0, V0, DT, TICKS, RUNS, K = 30, 1.0, 1.5, 0.5, 1000, 200, 0.5


def run(rng, beat, follow, tau_ticks, var=0.03, jit=0.01):
    cad = [1.0 if beat else 1 + var * rng.gauss(0, 1) for _ in range(N)]
    stri = [1 + var * rng.gauss(0, 1) for _ in range(N)]
    base = [V0 * c * s for c, s in zip(cad, stri)]
    x = [-(i * D0) for i in range(N)]
    hist = [[D0] * N for _ in range(tau_ticks + 1)]  # past gaps
    front, back = [], []
    for t in range(TICKS):
        gaps = [D0] + [x[i - 1] - x[i] for i in range(1, N)]
        hist.append(gaps); seen = hist[-1 - tau_ticks]; hist.pop(0)
        for i in range(N):
            v = base[i]
            if follow and i > 0:
                v *= min(2.0, max(0.2, 1 + K * (seen[i] - D0) / D0))
            x[i] += v * (1 + jit * rng.gauss(0, 1)) * DT
        if t >= 200:
            front.append(gaps[1]); back.append(gaps[N - 1])
    length_change = (x[0] - x[N - 1]) - (N - 1) * D0
    return length_change, statistics.pstdev(front), statistics.pstdev(back)


def main():
    rng = random.Random(20261007)
    lc, f, b = run(rng, True, True, 1, var=0.0, jit=0.0)
    assert abs(lc) < 1e-9 and f < 1e-12 and b < 1e-12
    out = {}
    for name, beat, follow, tau in (("no beat, no following", False, False, 0), ("beat, no following", True, False, 0),
                                    ("beat, following, tau 0.5 s", True, True, 1),
                                    ("beat, following, tau 1 s", True, True, 2)):
        res = [run(rng, beat, follow, tau) for _ in range(RUNS)]
        spread = statistics.pstdev([r[0] for r in res])
        fr = statistics.mean(r[1] for r in res); bk = statistics.mean(r[2] for r in res)
        out[name] = (spread, fr, bk)
        print(f"{name:28s} column length change sd {spread:8.2f} m   gap ripple front {fr:.4f} m, back {bk:.4f} m,"
              f" ratio {bk / fr if fr else float('nan'):.2f}")
    f1 = out["no beat, no following"][0] / out["beat, no following"][0]
    r2 = out["beat, following, tau 0.5 s"][2] / out["beat, following, tau 0.5 s"][1]
    r3 = out["beat, following, tau 1 s"][2] / out["beat, following, tau 1 s"][1]
    p1, p2, p3 = 1.2 <= f1 <= 1.7, r2 <= 1.2, r3 >= 2.0
    print(f"(1) beat cuts the length-change spread by {f1:.2f} (predicted 1.2 to 1.7): {p1}")
    print(f"(2) tau 0.5 s, back/front ripple {r2:.2f} (predicted <= 1.2): {p2}")
    print(f"(3) tau 1 s, back/front ripple {r3:.2f} (predicted >= 2): {p3}")
    fail = f1 > 3 or f1 < 1.1 or (not p2 and not p3)
    print("PASS" if p1 and p2 and p3 else ("FAIL" if fail else "PARTIAL: see the lines above"))


if __name__ == "__main__":
    main()
