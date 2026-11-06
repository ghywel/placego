#!/usr/bin/env python3
"""Block 5: class counts along the target path, for rule 30 and its left-permutive siblings.

Rows are naturals, bit i the cell at depth i + 1 behind a white wall. One tick: F(Y) = (Y >> 1) xor g(Y, Y << 1), with
g(c, r) = c or r (rule 30), r (rule 90), c xor r (rule 150), (not c) and r (rule 210). Survivors at width W are rows of
width at most W black at depth 1 at every even tick so far; a class is a distinct row at the current tick. At t0, the last
tick of the exact range, survivors are the 2^floor(W/2) lanes. N_k = classes after k further checks.
beta_k = 2 N_k / N_(k-1) - 1. K(W) = max |beta_k| sqrt(N_(k-1)) over checks with N_(k-1) >= 2. Pmax = largest N with a plateau.

Predictions, written before the run.
P1 (0.8): for rule 30, K(W) <= 3.5 at every W <= 48, including W = 45 and 47, not yet tabulated; K(W)^2 / W <= 0.3.
P2 (0.85): the law separates rule 30 from its siblings: for rules 90 and 150, every check is constant on lanes, so at the
first composite check beta = +1 or -1 with N large: K(W) grows like 2^(W/4). Rule 210 fails the law in some other large way.
Counterfactual: a sibling keeps K(W) bounded: then the class law is not about rule 30, and CR-1's gate 1 objection stands.
P3 (0.7): for rule 30 max |z| over a width's checks tracks the largest of about 0.4 W fair coins, so K(W)^2 stays near
2 ln(0.4 W) on average. Counterfactual: a clear rise with W beyond that.
"""
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
def stats(tab):
    Q = [x[2] for x in tab]
    K = 0; arg = None; P = 0; zs = []
    for a, b in zip(Q, Q[1:]):
        if a >= 2:
            beta = 2 * b / a - 1
            z = abs(beta) * math.sqrt(a)
            zs.append(z)
            if z > K: K = z; arg = a
        if a == b: P = max(P, a)
    return K, arg, P, len(zs)
rule = int(sys.argv[1]); lo_w = int(sys.argv[2]); hi_w = int(sys.argv[3]); st = int(sys.argv[4]) if len(sys.argv) > 4 else 1
print('rule', rule); print('W D C=Q(t0) K at-N Pmax checks K^2/W 2ln(.4W) lastS')
for W in range(lo_w, hi_w + 1, st):
    tab = run(rule, W)
    K, arg, P, n = stats(tab)
    last = tab[-1]
    died = last[1] == 0
    D = last[0] - 2 if died else None
    print(W, D if died else 'alive>%d' % last[0], tab[0][2], '%.2f' % K, arg, P, n, '%.3f' % (K * K / W), '%.2f' % (2 * math.log(0.4 * W)), tab[-2][1] if died and len(tab) > 1 else last[1], flush=True)
