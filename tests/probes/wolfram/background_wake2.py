#!/usr/bin/env python3
"""bg_wake2.py: the near-front layer of the (12, 68) witness, alignment (0, 51), tested for exact periodicity at periods 68*2^m
(offsets 0..40 below the front), on t in [145, T], trusted range asserted. Cloud, Block 15 follow-up."""
import numpy as np
exec(open('background_envelope.py').read().split("name, r, s = 's12_68'")[0])
name, r, s = 's12_68', 0, 51
T, J = 3200, 11600
X, E, R = evolve(name, r, s, T, J)
D = X ^ E
assert all(R[t] + 60 < J+1-2*t for t in range(T+1)), "trusted range (prefix autonomy): front + 60 < J+1-2t at every t"
inc = np.diff(R[145:]); assert np.array_equal(inc[34:], inc[:-34]), "front law (34, 42) on [145, T]"
print(f"front law (34, 42) exact on [145, {T}]; R({T}) = {R[T]}")
for P in (68, 136, 272, 544, 1088, 2176):
    n = T + 1 - P - 145
    prof = []
    for o in range(0, 41):
        bad = [t for t in range(145, T+1-P) if D[t, R[t]-o] != D[t+P, R[t+P]-o]]
        prof.append(len(bad))
    first_exact = next((o for o in range(41) if prof[o] > 0), 41)
    print(f"P={P:5d} (samples {n}): exceptions per offset 0..40: {prof}; exact to offset {first_exact - 1}")
print("BG_WAKE2_DONE")
