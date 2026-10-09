#!/usr/bin/env python3
"""rule30_cloud_left_apex.py: the single cell's left band at the apex, and how close its edge comes back to the centre.

RUN-ON:     cpu (Python 3 standard library; big-integer rows)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_left_apex.py [LOG2T=19]
COST:       about 45 s at LOG2T = 19.
Exploratory and post hoc: no prediction was pushed before the run. Cloud, 2026-10-09, from the owner's questions on
the left front of that morning: "right at the beginning the coherent wavefront starts to the chaotic right of the
centre column not its left, crosses it then carries on its descent ... is this an illusion or does the right hand
side of the column really start orderly ... Is it possible for the wavefront to ever wander back to the centre line
and cross it". Expectations stated to the owner before the run, not pushed: the band reaches right of the centre only
in the first 20 or so rows, and after row 100 the edge stays below x/t = -0.15.

The definition is rule30_cloud_left_boundary.py's (RULE30-PRIZE.md §8.74), unchanged: V_t has bit e = x_t(-t + e),
V' = (V << 2) ^ ((V << 1) | V), and B(t) = the lowest set bit of V_t ^ V_(t+P), P = 2^10. Diagonals shallower than
B(t) are P-periodic from t on, for ever; the edge is the cell x = B(t) - t. Left diagonal e is born on the pyramid's
right edge at t = ceil(e/2) and crosses the centre column at t = e, so its settling time tau(e) = min{t : B(t) > e}
says on which side of the centre it settled.

OUTCOME of the first run, 2026-10-09 (10:18 BST, 42 s at LOG2T = 19). Both expectations held.
  The apex is real. Rows 0 to 4 are ordered across their whole width (B(t) >= 2t + 1). The band reaches right of the
    centre at rows 2 to 14 and 16, and contains the centre cell at rows 0 to 17. The edge is at or right of the
    centre for the last time at row 20.
  Diagonals 0 to 17 settle before or as they cross the centre: diagonals 3 to 8 are periodic from t = 2, as soon as
    they are born, and 17 settles at row 16. From diagonal 18 on, every diagonal settles after it has crossed (18 and
    19 at row 20, 30 at 33, 59 at 85), about 1.32 rows per diagonal on average (§8.74).
  The edge never comes back. The largest x/t in each dyadic window from 2^7 to 2^19 lies between -0.176 (t = 540) and
    -0.251; the closest approach measured in units of sqrt(t) grows from 2.0 at t = 64 to 7.1 near 1,000, 28.8 near
    14,000 and 174 near 506,000. B advances by at most 12 in one step below 2^14 (14 to 2^19, §8.74), so the edge does
    step back towards the centre locally, which is its jaggedness, by up to about a dozen cells.
  Not proved: that the edge never returns. A return at row t would mean that the whole left half of row t, centre cell
    included, already lies on the left edge's eternal stripes.
"""
import sys
from collections import deque

LOG2T = int(sys.argv[1]) if len(sys.argv) > 1 else 19
P = 1 << 10
T = 1 << LOG2T


def main():
    win, V, B = deque(), 1, []
    for s in range(T + P + 1):
        win.append(V)
        if len(win) > P:
            d = win.popleft() ^ V
            B.append((d & -d).bit_length() - 1)
        V = (V << 2) ^ ((V << 1) | V)
    assert all(B[i + 1] >= B[i] for i in range(T - 1)), "B should never decrease"
    print(f"T = 2^{LOG2T}, P = 2^10")
    print("the apex: row t, B(t), the edge cell x = B - t, and the band's rightmost cell x = B - t - 1")
    for t in range(0, 24):
        print(f"  t = {t:2d}: B = {B[t]:2d}, edge at x = {B[t] - t:+d}, band to x = {B[t] - t - 1:+d}"
              + ("  (the whole row)" if B[t] >= 2 * t + 1 else ""))
    print("rows whose band reaches right of the centre:", [t for t in range(T) if B[t] - t - 1 >= 1])
    print("rows whose band contains the centre cell:", [t for t in range(T) if B[t] - t - 1 >= 0])
    print("last row with the edge at or right of the centre:", max(t for t in range(T) if B[t] >= t))
    print("diagonal e: born at ceil(e/2), crosses the centre at e, settles at tau(e)")
    t = 0
    for e in range(0, 32):
        while B[t] <= e:
            t += 1
        side = "before crossing" if t < e else ("as it crosses" if t == e else "after crossing")
        print(f"  e = {e:2d}: born {(e + 1) // 2:2d}, crosses {e:2d}, settles {t:3d} ({side})")
    print("closest return in each dyadic window: largest x/t, where, and the gap to the centre in units of sqrt(t)")
    for k in range(5, LOG2T):
        lo, hi = 1 << k, 1 << (k + 1)
        m = max(range(lo, hi), key=lambda u: (B[u] - u) / u)
        x = B[m] - m
        print(f"  [2^{k}, 2^{k + 1}): x/t = {x / m:+.4f} at t = {m}, x = {x}, gap {-x / m ** 0.5:.1f} sqrt(t)")
    top = max(range(min(T, 1 << 14) - 1), key=lambda u: B[u + 1] - B[u])
    print(f"largest one-step advance of B below 2^14: {B[top + 1] - B[top]} at t = {top}")


if __name__ == "__main__":
    main()
