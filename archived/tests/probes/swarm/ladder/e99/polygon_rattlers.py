"""polygon_rattlers.py: Erdős #99: how many loose points fit inside a regular unit-side odd polygon?

RUN-ON: cpu, python3 with numpy and scipy. COMMAND: python3 tests/probes/swarm/ladder/e99/polygon_rattlers.py M KMAX STARTS
Why (CL559): plateau.py found the triangle-free local minima at diameters 3.513337 and 4.148115, which are exactly the
diameters of the regular unit-side 11-gon and 13-gon, GPT's exact KKT points of GC1689. Points strictly inside such
a polygon, at distance >= 1 from its vertices and from each other, change nothing in the diameter, so the plateau
should last while the interior has room. For each k, maximize t = the smallest distance among the k interior points
and between them and the M vertices (vertices fixed), with many starts. Capacity = the largest k with t >= 1.
Record searched: CL557 (plateau 4.148115 at n = 18, 19, 20; then 4.469734 at n = 21, 22), GC1689.
PREDICTIONS (before the run): the 13-gon holds exactly 7 interior points (t >= 1 at k = 7, t < 1 at k = 8), which
matches the plateau ending at n = 20. Counterfactual: capacity 6 or 8 or more, in which case the plateau is not this
family alone, or the search misses packings.
"""
import itertools, math, sys
import numpy as np
from scipy.optimize import minimize


def capacity_t(M, k, starts, rng):
    R = 1 / (2 * math.sin(math.pi / M))
    V = np.array([(R * math.cos(2 * math.pi * i / M), R * math.sin(2 * math.pi * i / M)) for i in range(M)])
    P = list(itertools.combinations(range(k), 2))
    best = 0
    for _ in range(starts):
        r = R * np.sqrt(rng.uniform(0, 1, k)); th = rng.uniform(0, 2 * math.pi, k)
        z0 = np.concatenate([np.c_[r * np.cos(th), r * np.sin(th)].ravel(), [0.1]])
        def cons(z):
            y = z[:-1].reshape(k, 2); t2 = z[-1] ** 2
            a = [((y[i] - y[j]) ** 2).sum() - t2 for i, j in P]
            b = (((y[:, None, :] - V[None, :, :]) ** 2).sum(2) - t2).ravel()
            # stay inside the polygon: inside every edge's half-plane
            c = [R * math.cos(math.pi / M) - (y @ np.array([math.cos(2 * math.pi * (i + .5) / M),
                 math.sin(2 * math.pi * (i + .5) / M)])) for i in range(M)]
            return np.concatenate([a, b, np.concatenate(c)])
        res = minimize(lambda z: -z[-1], z0, method='SLSQP', constraints=[{'type': 'ineq', 'fun': cons}],
                       options={'maxiter': 500, 'ftol': 1e-12})
        if res.success and min(cons(res.x)) > -1e-9: best = max(best, abs(res.x[-1]))
    return best


if __name__ == '__main__':
    M, kmax, starts = (int(a) for a in sys.argv[1:4])
    rng = np.random.default_rng(1)
    for k in range(1, kmax + 1):
        print(f'M={M} k={k}: best t = {capacity_t(M, k, starts, rng):.6f}', flush=True)


def polygon_plus_interior(M, k, rng, starts=40):
    """Return the M-gon vertices plus the best k-point interior packing found (for the stay-put check)."""
    R = 1 / (2 * math.sin(math.pi / M))
    V = np.array([(R * math.cos(2 * math.pi * i / M), R * math.sin(2 * math.pi * i / M)) for i in range(M)])
    best, by = 0, None
    P = list(itertools.combinations(range(k), 2))
    for _ in range(starts):
        r = R * np.sqrt(rng.uniform(0, 1, k)); th = rng.uniform(0, 2 * math.pi, k)
        z0 = np.concatenate([np.c_[r * np.cos(th), r * np.sin(th)].ravel(), [0.1]])
        def cons(z):
            y = z[:-1].reshape(k, 2); t2 = z[-1] ** 2
            a = [((y[i] - y[j]) ** 2).sum() - t2 for i, j in P]
            b = (((y[:, None, :] - V[None, :, :]) ** 2).sum(2) - t2).ravel()
            c = [R * math.cos(math.pi / M) - (y @ np.array([math.cos(2 * math.pi * (i + .5) / M),
                 math.sin(2 * math.pi * (i + .5) / M)])) for i in range(M)]
            return np.concatenate([a, b, np.concatenate(c)])
        res = minimize(lambda z: -z[-1], z0, method='SLSQP', constraints=[{'type': 'ineq', 'fun': cons}],
                       options={'maxiter': 500, 'ftol': 1e-12})
        if res.success and min(cons(res.x)) > -1e-9 and abs(res.x[-1]) > best:
            best, by = abs(res.x[-1]), res.x[:-1].reshape(k, 2)
    return np.vstack([V, by]), best

# OUTCOME (2026-10-22 17:24 BST, Cloud, CL559): 40 starts per k. 13-gon: t = 2.0893, 1.4100, 1.3349, 1.2351, 1.1393,
# 1.0683, 1.0572 for k = 1..7, then 0.9804 at k = 8: capacity 7 (measured, a lower bound on t, so k = 8 failing is not
# proved). Prediction HELD: the 4.148115 plateau is n = 13 + k for k <= 7, and CL557 saw it at n = 18, 19, 20 and not
# at 21. 11-gon: t >= 1 up to k = 4 (1.0496), 0.9742 at k = 5: capacity 4, so the 11-gon family covers n = 11..15.
# Unexpected check (scratch stay.py): SLSQP started at 1e-3 from the 13-gon with 5 and with 7 interior points, and the
# 11-gon with 4, returns to D = 4.148115, 4.148115, 3.513337 with no contact triangle: these are numerical local
# minima of the full problem, triangle-free, and they are GPT's exact KKT polygons of GC1689 plus loose points.
