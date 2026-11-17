#!/usr/bin/env python3
"""L1282 (Local, 2026-11-01): what Rule 30's Boolean derivatives control. Predictions in reports/rule30-genealogy.md
section 11, written before the first run. Run: python3 tests/probes/genealogy_derivatives.py  (under a minute)

(A) one-step identities, every case: polarization F(x+y) = F(x)+F(y)+B(x,y); forward damage D' = F(D) + B(x,D);
    backward invisible damage D_(i-1) = (1+x_(i+1))D_i + (1+x_i)D_(i+1) + D_i D_(i+1) for equal children.
(B) T4: one flip inside the single-seed pattern at time 1000 (positions -200, 0, +200); left edges of the actual
    damage, of first-order influence (support of sensitivity paths) and of the mod-2 tangent, for 5000 steps.
"""
from itertools import product
import numpy as np


def f(a, b, c):
    return a ^ (b | c)


# (A) one step, local form: cell i reads (i-1, i, i+1); B(x,y)_i = x_i y_(i+1) + x_(i+1) y_i
n_pol = n_dmg = n_back = 0
for xs in product((0, 1), repeat=3):
    for ys in product((0, 1), repeat=3):
        xa, xb, xc = xs
        ya, yb, yc = ys
        s = (xa ^ ya, xb ^ yb, xc ^ yc)
        Bxy = (xb & yc) ^ (xc & yb)
        assert f(*s) == f(*xs) ^ f(*ys) ^ Bxy
        n_pol += 1
        # damage D = y: F(x+D) - F(x) = F(D) + B(x, D)
        assert f(*s) ^ f(*xs) == f(*ys) ^ Bxy
        n_dmg += 1
# backward: rows x and x+D with equal children on positions i-1..; check the right-to-left law on all 5-cell windows
for xw in product((0, 1), repeat=5):
    for dw in product((0, 1), repeat=5):
        yw = tuple(a ^ b for a, b in zip(xw, dw))
        # child at window position 1 (reads 0,1,2) equal, so D_0 is fixed by D_1, D_2 and x_1, x_2
        if f(*xw[0:3]) == f(*yw[0:3]):
            pred = ((1 ^ xw[2]) & dw[1]) ^ ((1 ^ xw[1]) & dw[2]) ^ (dw[1] & dw[2])
            assert dw[0] == pred
            n_back += 1
print(f'(A) polarization {n_pol}/64, forward damage {n_dmg}/64, backward invisible damage {n_back} windows: PASS')

# (B) T4
T0, S = 1000, 5000
T = T0 + S
W = 2 * T + 9
C = T + 4
x = np.zeros(W, dtype=bool)
x[C] = True
for _ in range(T0):
    x = np.concatenate(([False], x[:-2] ^ (x[1:-1] | x[2:]), [False]))
sites = (-200, 0, 200)
ys = np.array([x.copy() for _ in sites])
for k, j in enumerate(sites):
    ys[k, C + j] ^= True
sup = np.zeros((len(sites), W), dtype=bool)
tan = np.zeros((len(sites), W), dtype=bool)
for k, j in enumerate(sites):
    sup[k, C + j] = tan[k, C + j] = True
edges = {k: [] for k in range(len(sites))}
for s in range(S):
    nx = np.concatenate(([False], x[:-2] ^ (x[1:-1] | x[2:]), [False]))
    ny = np.zeros_like(ys)
    ny[:, 1:-1] = ys[:, :-2] ^ (ys[:, 1:-1] | ys[:, 2:])
    open_c = ~x[2:]          # centre input of cell i open iff x_(i+1) white
    open_r = ~x[1:-1]        # right input of cell i open iff x_i white
    nsup = np.zeros_like(sup)
    nsup[:, 1:-1] = sup[:, :-2] | (sup[:, 1:-1] & open_c) | (sup[:, 2:] & open_r)
    ntan = np.zeros_like(tan)
    ntan[:, 1:-1] = tan[:, :-2] ^ (tan[:, 1:-1] & open_c) ^ (tan[:, 2:] & open_r)
    x, ys, sup, tan = nx, ny, nsup, ntan
    for k in range(len(sites)):
        d = np.flatnonzero(ys[k] ^ x)
        a = np.flatnonzero(sup[k])
        h = np.flatnonzero(tan[k])
        edges[k].append((d[0] - C if d.size else None, a[0] - C, h[0] - C if h.size else None,
                         d[-1] - C if d.size else None))
for k, j in enumerate(sites):
    e = edges[k]
    act = np.array([v[0] for v in e], dtype=float)
    sp = np.array([v[1] for v in e], dtype=float)
    tg = np.array([v[2] for v in e], dtype=float)
    right = np.array([v[3] for v in e], dtype=float)
    assert np.all(right == j + np.arange(1, S + 1))          # the right edge of damage moves at exactly +1
    half = S // 2
    v_act = (act[-1] - act[half]) / (S - 1 - half)
    v_sup = (sp[-1] - sp[half]) / (S - 1 - half)
    v_tan = (tg[-1] - tg[half]) / (S - 1 - half)
    same_tan = np.mean(tg == sp)
    ahead = np.mean(act < sp)          # actual edge strictly left of the first-order edge
    print(f'(B) flip at {j:+d}: left-edge speeds over steps {half}..{S}: actual {v_act:+.4f}, first-order {v_sup:+.4f}, '
          f'mod-2 tangent {v_tan:+.4f}; at step {S}: actual {act[-1]:+.0f}, first-order {sp[-1]:+.0f}, tangent {tg[-1]:+.0f} '
          f'(from {j:+d}); tangent edge = first-order edge in {same_tan:.3f} of steps; actual strictly ahead of first-order in {ahead:.3f}')
print('GENEALOGY_DERIVATIVES_DONE')
