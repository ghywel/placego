#!/usr/bin/env python3
"""rule30_cloud_left_boundary.py: where the single cell's ordered left band ends, as an exact curve.

RUN-ON:     cpu (Python 3 standard library; big-integer rows)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_left_boundary.py [LOG2T=19] [LOG2P=10]
COST:       a few minutes at LOG2T = 19.

Why (the owner, 2026-10-09): "I am also interested in where the left edge loses logical coherence ... there must be a
formal line or curve where the left edge goes from orderly pattern to random ... It does map the light cone line down
to a certain small depth, but the pattern-random boundary goes off the straight edge."

The record so far. The band of stripes fills the left of each row and its inner edge moves left at about 0.25 cells
per step (§8.30), Rule 30's leftward speed of information on random rows, 0.246 (§8.30 LB5, §8.66). Wolfram's 2019
prize announcement: about 0.252 per step over the first 100,000 steps. §8.68's pre-registered `edge` run: the
settled edge at x/t = -0.254 at t = 40,000 and -0.252 at t = 80,000. The triangle law turns uniform from
x/t = -0.24 +- 0.02.

The exact curve (definition, and why it is exact). Read row t from the left edge: V_t has bit e = x_t(-t + e), so
diagonal e sits at depth e from the edge. Left diagonals depend only on diagonals nearer the edge (§8.31), so the
first e diagonals form a closed deterministic system, V' = ((V << 2) XOR ((V << 1) OR V)) restricted to e bits. A
deterministic system that repeats once, V_t = V_(t+P) on those e bits, is periodic from t for ever. So with P a
multiple of every period in the band (powers of 2: 16 out to depth 2,047, §8.30; P = 2^10 here), define
    B(t) = the number of diagonals, from the edge, on which row t and row t + P agree
         = the position of the lowest 1 in V_t XOR V_(t+P).
Every diagonal shallower than B(t) is in its eternal stripe pattern from time t on, and diagonal B(t) is not yet.
B(t) never decreases. In the picture the boundary is the curve x(t) = -t + B(t). It hugs the light cone (x = -t)
while B is small, and it leaves it where the band starts to grow.

A line with a late start: if B(t) = (1 - v)(t - t0) for t >= t0, the boundary runs down the light cone to depth t0
and leaves it at speed v. Then x/t = -v - (1 - v) t0 / t, which drifts towards -v, and §8.68's -0.254 and -0.252
fit v = 0.246 with t0 near 400 to 500. That reading was made from the record before this run, not measured.

PREDICTIONS, written 2026-10-09 by 08:52 BST, before any run of this script (LOG2T = 19, LOG2P = 10).
  LE1 (control). B(t) never decreases; lag 2P gives the same B at every t (so P covers the band's periods); and x/t
      at t = 40,000 and 80,000 is within 0.004 of §8.68's -0.254 and -0.252. The two definitions differ: §8.68 asked
      for period 16 already reached, this asks for repetition after 2^10 steps.
  LE2 (blind). A least-squares line B(t) = a t + b over t in [2^16, 2^19] has leftward speed v = 1 - a in
      [0.240, 0.252], nearer the random rows' 0.246 than the 0.252 average. Confidence 0.5.
  LE3 (blind; the owner's departure). The same line meets the light cone at t0 = -b / a between 100 and 2,000 steps:
      the boundary hugs the edge down to a few hundred rows, then leaves it. Confidence 0.5.
  LE4 (blind). The boundary's wobble about that line grows with t. The root-mean-square residual in the dyadic window
      [2^k, 2^(k+1)) grows like 2^(alpha k) with alpha between 0.25 and 0.6 (a random walk gives 0.5; a KPZ-type
      front gives 1/3). Confidence 0.4.
UNEXPECTED CHECK, LE5: the band does not grow smoothly. At least one single step after t = 1,000 moves B by more than
  100 diagonals at once, a long stretch settling together. Confidence 0.5.
Counterfactual: a curve that bends for ever (v drifting with t) would mean there is no single speed, and a t0 near 0
  would mean the boundary leaves the light cone at once, so the owner's departure would be a trick of the eye.
REFUTED-BY: LE1 failing (the definition or the instrument); LE2 to LE5 failing as worded.
"""
import math, sys
from collections import deque

LOG2T = int(sys.argv[1]) if len(sys.argv) > 1 else 19
LOG2P = int(sys.argv[2]) if len(sys.argv) > 2 else 10
T, P = 1 << LOG2T, 1 << LOG2P
K = int(0.85 * T) + 8192                                    # diagonals tracked: deeper than the band will reach
MASK = (1 << K) - 1


def main():
    V = 1                                                   # t = 0: the single cell is the left edge
    buf = deque()
    B, B2 = [], []                                          # with lag P, and with lag 2P as a control
    for t in range(T + 2 * P + 1):
        buf.append(V)
        if len(buf) > P:
            d = buf[-1 - P] ^ V                             # row t - P against row t
            B.append((d & -d).bit_length() - 1 if d else K)
        if len(buf) > 2 * P:
            old = buf.popleft()                             # row t - 2P
            d = old ^ V
            B2.append((d & -d).bit_length() - 1 if d else K)
        V = ((V << 2) ^ ((V << 1) | V)) & MASK
    B, B2 = B[:T + 1], B2[:T + 1]                           # B[t] for t = 0 .. T
    mono = all(B[i] <= B[i + 1] for i in range(T))
    lagdiff = sum(1 for x, y in zip(B, B2) if x != y)
    print(f"T = 2^{LOG2T}, P = 2^{LOG2P}, diagonals tracked {K}; B never decreases: {mono}; "
          f"times where lag 2P gives a different B: {lagdiff}")
    print("t, B(t), boundary x/t = (-t + B)/t:")
    for t in [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 40000, 65536, 80000, 131072, 262144,
              524288]:
        if t <= T:
            print(f"  t = {t:7d}  B = {B[t]:7d}  x/t = {(-t + B[t]) / t:+.4f}")
    le1 = mono and lagdiff == 0
    if T >= 80000:
        le1 = le1 and abs(B[40000] / 40000 - 1 + 0.254) <= 0.004 and abs(B[80000] / 80000 - 1 + 0.252) <= 0.004
    # least-squares line over [2^16, 2^19], sampled every 16 steps
    lo = min(1 << 16, T // 8)
    xs = list(range(lo, T + 1, 16))
    ys = [B[t] for t in xs]
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    a = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    b = my - a * mx
    v, t0 = 1 - a, -b / a
    print(f"line over [{lo}, {T}]: B = {a:.5f} t {b:+.1f}; leftward speed v = {v:.5f}; "
          f"leaves the cone at t0 = {t0:.0f}")
    # wobble about the line, in dyadic windows
    rms = []
    for k in range(8, LOG2T):
        ws = range(1 << k, 1 << (k + 1), max(1, (1 << k) // 4096))
        r = math.sqrt(sum((B[t] - (a * t + b)) ** 2 for t in ws) / len(ws))
        rms.append((k, r))
    print("rms residual about the line in [2^k, 2^(k+1)):")
    for k, r in rms:
        print(f"  k = {k:2d}: {r:9.1f}")
    pts = [(k, math.log2(r)) for k, r in rms if k >= 12 and r > 0]
    if len(pts) >= 2:
        mk = sum(k for k, _ in pts) / len(pts); ml = sum(l for _, l in pts) / len(pts)
        alpha = sum((k - mk) * (l - ml) for k, l in pts) / sum((k - mk) ** 2 for k, _ in pts)
    else:
        alpha = float("nan")
    print(f"growth exponent of the wobble over k >= 12: alpha = {alpha:.3f}")
    jumps = [(B[t + 1] - B[t], t) for t in range(1000, T)]
    big = max(jumps)
    print(f"largest single-step advance after t = 1000: {big[0]} diagonals at t = {big[1]}")
    print(f"LE1 {'PASS' if le1 else 'FAIL'}")
    print(f"LE2 {'HELD' if 0.240 <= v <= 0.252 else 'REFUTED'}")
    print(f"LE3 {'HELD' if 100 <= t0 <= 2000 else 'REFUTED'}")
    print(f"LE4 {'HELD' if 0.25 <= alpha <= 0.6 else 'REFUTED'}")
    print(f"LE5 {'HELD' if big[0] > 100 else 'REFUTED'}")


if __name__ == "__main__":
    main()
