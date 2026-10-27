"""staircase_end_check.py: every staircase in the single cell's picture ends (L1007, Theorem S; DQ-021).

Local, 2026-10-27. The theorem is proved by hand in reports/rule30-staircases-end.md. This script replays its two
ingredients and its explicit bound on the single seed's rows, where the bound is small enough to observe.

Theorem S. In the single seed's picture, let a maximal alternating stretch of length >= 3 have its front (left end) at
distance W from the right edge at time t0.
- If W >= 2, its continuation dies (length < 3) by the first t1 >= t0 with p_(W+2) dividing t1, where p_k is the period
  of the single seed's edge code mod 2^k. At such a t1 the cells at distances 1..W+1 are all white, and a stretch of
  length >= 3 pinned within distance W of the edge cannot be alternating there.
- If W <= 1, it is the 0,1,0 pattern around the edge cell at an emission, and it dies after one step.
The front moves right exactly one cell per row while the stretch lives (GC847, L999 S3), and so does the right edge.

Predictions (written before the run):
  E1  Along every tracked stretch, the front advances exactly one cell per row while the length stays >= 3.
  E2  Every stretch with W in 2..20 born at t0 <= 2,000 dies by its bound t1 (p_22 = 256, so t1 <= t0 + 256).
  E3  Every stretch with W <= 1 dies after exactly one step.
Counterfactual: a stretch alive at its t1 refutes Theorem S's bound, or my front-tracking.
Record searched: "staircase.{0,60}(end|finite|die|termin)" (L999's open question only), "(rain|alternating
stretch).{0,60}(finite|dies|lifetime|eternal)" (GC847: an infinite left stretch can live for ever),
"bounded distance.{0,40}edge" (an unrelated carrier). No termination theorem was found.

Run: python3 -I tests/probes/wolfram/staircase_end_check.py   (exit 1 on any failure)

Outcome (2026-10-27, M5, 3.1 s): ALL CHECKS PASS, exit 0. E1 held on 937,161 front steps, E2 on all 4,438 stretches with
W in 2..20, and E3 on all 1,000 edge stretches (one per emission). The longest-lived stretch in the window lasted 43 rows,
born at t0 = 974 with W = 228, deep in the core, where the bound p_230 is astronomically large and says nothing in practice.
The first draft carried three dead lines guarded by "if False"; they were removed before the run.
"""
import sys

T = 2300
OFF = T + 2
W_ROW = 2 * T + 5


def step(x):
    return [(x[i - 1] if i else 0) ^ (x[i] | (x[i + 1] if i + 1 < len(x) else 0)) for i in range(len(x))]


rows = [[0] * W_ROW]
rows[0][OFF] = 1
for t in range(T):
    rows.append(step(rows[-1]))

# p_k from the edge code T(R) = R XOR (2R OR 4R), modulo 2^64
MASK = (1 << 64) - 1
R = 1
orbit = [1]
for _ in range(1 << 12):
    R = (R ^ ((R << 1) | (R << 2))) & MASK
    orbit.append(R)
p = {}
for k in range(1, 30):
    m = (1 << k) - 1
    p[k] = next(s for s in range(1, len(orbit)) if (orbit[s] & m) == 1)


def stretches(row):
    out = []
    i = 1
    n = len(row)
    while i < n - 1:
        j = i
        while j + 1 < n - 1 and row[j + 1] != row[j]:
            j += 1
        if j - i >= 2 and row[i - 1] == row[i] and row[j + 1] == row[j]:
            out.append((i, j))
        i = j + 1
    return out


fails = []
count = {"E1": 0, "E2": 0, "E3": 0}
longest = (0, None)
# Theorem S applies to a stretch present at any time t0, so every stretch at every t0 is tracked (a continuation
# tracked again from a later t0 gets its own, later, bound).
for t0 in range(1, 2001):
    edge = max(i for i in range(W_ROW) if rows[t0][i])
    for a, r in stretches(rows[t0]):
        W = edge - a
        t, fa, fr = t0, a, r
        alive = True
        while True:
            if t + 1 > T:
                break
            nxt = rows[t + 1]
            # continuation: maximal alternating run of nxt containing fa+1
            i = fa + 1
            if not (nxt[i] != nxt[i + 1]):
                alive = False
            else:
                lo = i
                while lo - 1 >= 0 and nxt[lo - 1] != nxt[lo]:
                    lo -= 1
                hi = i
                while hi + 1 < W_ROW and nxt[hi + 1] != nxt[hi]:
                    hi += 1
                if hi - lo < 2:
                    alive = False
                else:
                    count["E1"] += 1
                    if lo != fa + 1:
                        fails.append(("E1", t0, a, t + 1, lo, fa + 1))
                        alive = False
                    fa, fr = lo, hi
            if not alive:
                break
            t += 1
        life = t - t0 + 1
        if life > longest[0]:
            longest = (life, (t0, a, W))
        if W <= 1:
            count["E3"] += 1
            if life != 1:
                fails.append(("E3", t0, a, W, life))
        elif W <= 20:
            count["E2"] += 1
            t1 = t0 if t0 % p[W + 2] == 0 else (t0 // p[W + 2] + 1) * p[W + 2]
            if t1 <= T and t >= t1:
                fails.append(("E2", t0, a, W, t, t1))
        if len(fails) > 10:
            break

print("instances:", count, "| longest-lived stretch:", longest[0], "rows (born t0, front, W):", longest[1])
print("failures:", len(fails), fails[:5])
print("ALL CHECKS PASS" if not fails else "FAIL")
sys.exit(1 if fails else 0)
