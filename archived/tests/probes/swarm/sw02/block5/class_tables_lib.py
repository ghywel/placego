import math, sys, time
import numpy as np
one = np.uint64(1); s63 = np.uint64(63)
def sr(lo, hi): return (lo >> one) | (hi << s63), hi >> one
def sl(lo, hi): return lo << one, (hi << one) | (lo >> s63)
def step(rule, lo, hi):
    rl, rh = sr(lo, hi); ll, lh = sl(lo, hi)
    if rule == 30: gl, gh = lo | ll, hi | lh
    elif rule == 90: gl, gh = ll, lh
    elif rule == 150: gl, gh = lo ^ ll, hi ^ lh
    elif rule == 210: gl, gh = (~lo) & ll, (~hi) & lh
    return rl ^ gl, rh ^ gh
def extend(rule, R, k):
    lo = R.copy(); hi = np.zeros_like(lo)
    for s in range(k): lo, hi = step(rule, lo, hi)
    return R | (((lo & one) ^ one) << np.uint64(k))
def lanes(rule, W):
    R = np.array([0], dtype=np.uint64); k = 0
    while k + 1 < W:
        R = extend(rule, R, k)
        R = np.concatenate([R, R | (one << np.uint64(k + 1))])
        k += 2
    if k < W: R = extend(rule, R, k)
    return R
def distinct(lo, hi):
    o = np.lexsort((hi, lo)); l, h = lo[o], hi[o]
    b = np.concatenate([[True], (l[1:] != l[:-1]) | (h[1:] != h[:-1])])
    return int(b.sum())
def run(rule, W, tmax=None):
    R = lanes(rule, W)
    t0 = W - 2 if W % 2 == 0 else W - 1
    lo = R; hi = np.zeros_like(lo); t = 0; tab = []
    tmax = tmax or 3 * W + 60
    while t <= tmax:
        if t % 2 == 0 and t >= t0:
            al = (lo & one) == 1
            lo, hi = lo[al], hi[al]
            if lo.size == 0:
                tab.append((t, 0, 0)); break
            tab.append((t, lo.size, distinct(lo, hi)))
        lo, hi = step(rule, lo, hi); t += 1
    return tab
