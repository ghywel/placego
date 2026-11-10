# Carry check (Cloud, CL763) of flag 92: under the alternating centre, can drivenGamma = cell1 AND (cell2 OR cell3) vanish at
# every late black-to-white transition of the driver (every even tick, centre black)? Sound relaxation: W-windows at even
# ticks, the two cells beyond the window free at each double step; A_0 = windows with gamma = 0; A_(k+1) = those of A_0 with
# a successor in A_k. If A_k is empty, no right half keeps gamma = 0 at k+1 consecutive even ticks.
import numpy as np, sys
def run(W):
    M = lambda w: (np.uint64(1) << np.uint64(w)) - np.uint64(1); one = np.uint64(1)
    def tick(x, b, w): return (((x << one) | np.uint64(b)) ^ (x | (x >> one))) & M(w)
    def step(x, e):                       # even tick -> next even tick: centre black, then white; cells W+1, W+2 = e
        y = x | (np.uint64(e) << np.uint64(W)); y = tick(y, 1, W + 2) & M(W + 1); return tick(y, 0, W + 1) & M(W)
    allw = np.arange(1 << W, dtype=np.uint64)
    c1 = allw & one; c2 = (allw >> one) & one; c3 = (allw >> np.uint64(2)) & one
    ok0 = (c1 & (c2 | c3)) == 0
    succ = [step(allw, e).astype(np.int64) for e in range(4)]
    A = ok0.copy(); k = 0
    while True:
        B = ok0 & (A[succ[0]] | A[succ[1]] | A[succ[2]] | A[succ[3]]); k += 1
        if not B.any(): return k, 0
        if (B == A).all(): return k, int(B.sum())
        A = B
for W in (8, 12, 16):
    k, n = run(W); print(f"W={W}: " + (f"empty after {k} rounds: gamma cannot vanish at {k+1} consecutive even ticks" if n == 0 else f"nonempty fixed point of {n} windows after {k} rounds"))
