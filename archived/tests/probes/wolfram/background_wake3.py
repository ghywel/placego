#!/usr/bin/env python3
"""bg_wake3.py: where and how the (34, 42) front law of the (12, 68) witness, alignment (0, 51), breaks; the law(s) after it."""
import numpy as np
exec(open('background_envelope.py').read().split("name, r, s = 's12_68'")[0])
name, r, s = 's12_68', 0, 51
T, J = 3200, 11600
X, E, R = evolve(name, r, s, T, J)
D = X ^ E
assert all(R[t] + 60 < J+1-2*t for t in range(T+1)), "trusted range"
inc = np.diff(R)
breaks = [t for t in range(145+34, T) if inc[t] != inc[t-34]]
print("first breaks of the (34, 42) law (t with inc[t] != inc[t-34]):", breaks[:20], "count", len(breaks))
tb = breaks[0]
print(f"around the first break t={tb}: fronts R[{tb-6}..{tb+8}] =", list(R[tb-6:tb+9]), "incs", list(inc[tb-6:tb+8]), "vs 34 earlier", list(inc[tb-40:tb-26]))
print("  D below the front at t-1, t, t+1 (offsets 0..12):", [list(D[tt, R[tt]-12:R[tt]+1][::-1]) for tt in (tb-1, tb, tb+1)])
print("  E_{R+1}, E_R, E_{R-1} at t-1, t:", [(int(E[tt, R[tt]+1]), int(E[tt, R[tt]]), int(E[tt, R[tt]-1])) for tt in (tb-1, tb)])
# laws after the break: eventual periodicity of increments on [tb, T] with periods <= 400
def law(segment):
    n = len(segment)
    for per in range(1, 401):
        if n < 3*per: break
        if np.array_equal(segment[n-2*per:n-per], segment[n-per:]):
            t0 = n - 2*per
            while t0 > 0 and segment[t0-1] == segment[t0-1+per]: t0 -= 1
            return t0, per, int(segment[t0:t0+per].sum())
    return None
l = law(inc[145:])
print("eventual law on [145, T] (start offset from 145, period, shift):", l)
print(f"R({T}) = {R[T]}; mean speed on [145, T] = {(R[T]-R[145])/(T-145):.4f}; on [145, 1400] = {(R[1400]-R[145])/(1400-145):.4f}")
# how many breaks of the 34-law in windows of 500 ticks
print("breaks per 500-tick window:", [sum(1 for t in breaks if a <= t < a+500) for a in range(145, T, 500)])
print("BG_WAKE3_DONE")
