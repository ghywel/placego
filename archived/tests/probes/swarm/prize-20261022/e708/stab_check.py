#!/usr/bin/env python3
"""Independent cross-check of stab.py by direct enumeration over M (a different code path):
for each M, take every heavy a <= M (omega>=3), t_a = M // (a / Q(a)); find the smallest i with
#{a : t_a < i} >= i (a Hall-condition violation available to an adversary choosing A = these a's plus M)."""
import sys, time
sys.path.insert(0, '.')
from g708 import factor
T0 = time.time()
heavy = {}
first = None
minimal_i = 10 ** 9
for M in range(2, 6001):
    f = factor(M)
    if len(f) >= 3:
        Q = max(p ** k for p, k in f.items())
        heavy[M] = M // Q
    ts = sorted(M // w for w in heavy.values())
    # violation at level i iff ts[i-1] < i  (i-th smallest t below i)
    for i in range(1, len(ts) + 1):
        if ts[i - 1] < i:
            if i < minimal_i:
                minimal_i = i; first = (M, i)
            break
    if time.time() - T0 > 240:
        break
print('checked M up to', M, ' smallest violating level i =', minimal_i, ' first at (M, i) =', first, flush=True)
