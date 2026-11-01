#!/usr/bin/env python3
"""bg_wake.py: how periodic is the wake of the (12, 68) witness on alignment (0, 51)? Column periods (fixed depth, in t) and the
diagonal profile (agreement of D at offset o below the front between t and t+68), Cloud Block 15 follow-up."""
import numpy as np
exec(open('background_envelope.py').read().split("name, r, s = 's12_68'")[0])
name, r, s = 's12_68', 0, 51
T, J = 1400, 5400
X, E, R = evolve(name, r, s, T, J)
D = X ^ E
assert all(R[t] + 60 < J+1-2*t for t in range(T+1)), "trusted range (prefix autonomy): front + 60 < J+1-2t at every t"
def period(col, lo, hi):
    seg = col[lo:hi]
    for P in range(1, (hi-lo)//2):
        if np.array_equal(seg[P:], seg[:-P]): return P
    return None
print("column periods in t on [300, 1400] (None = longer than 550), depths 0..40:")
print(" ", [(j, period(X[:, j], 300, T+1)) for j in range(0, 41)])
print("diagonal profile: fraction of t in [145, 1332] with D(t+68, R(t+68)-o) == D(t, R(t)-o), offsets o = 0..60:")
prof = []
for o in range(0, 61):
    agree = sum(1 for t in range(145, T+1-68) if D[t, R[t]-o] == D[t+68, R[t+68]-o])
    prof.append(round(agree / (T+1-68-145), 3))
print(" ", prof)
print("same with period 34:", [round(sum(1 for t in range(145, T+1-34) if D[t, R[t]-o] == D[t+34, R[t+34]-o]) / (T+1-34-145), 3) for o in range(0, 25)])
inc = np.diff(R[145:]); 
per = next((P for P in range(1, 400) if np.array_equal(inc[P:], inc[:-P])), None)
print(f"front increments on [145, {T}]: exact period {per}; sum over one period {int(inc[:per].sum()) if per else None}; R({T}) = {R[T]}")
print("BG_WAKE_DONE")
