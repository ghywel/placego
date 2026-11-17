"""contact_catalog.py: Erdős #99: local minima of the diameter problem and the triangles of their contact graphs.

RUN-ON: cpu, python3 with numpy and scipy. COMMAND: python3 tests/probes/swarm/ladder/e99/contact_catalog.py N_MIN N_MAX STARTS SEED
Why (CL556): GPT's GC1686 is right that a triangle-free constraint has the unconstrained infimum (perturb and rescale),
so the live question is ATTAINMENT: does a minimiser's contact graph (pairs at distance exactly 1) contain a triangle?
For each n, record every converged local minimum, its diameter and the number of triangles in its contact graph
(tolerance 1e-6), and compare the best overall with the best triangle-free LOCAL MINIMUM (not an infimum).
PREDICTIONS (before the run): for 10 <= n <= 20 the best triangle-free local minimum is strictly worse than the best
overall, by about 1e-3 or more, except at a few n. Counterfactual: a triangle-free local minimum that ties or beats the
best at some n >= 10 (an attainment instance, still uncertified).
"""
import itertools, math, sys
import numpy as np
sys.path.insert(0, 'tests/probes/swarm/ladder/e99')
from min_diameter import minimize

def local_min(n, x0):
    pairs = list(itertools.combinations(range(n), 2))
    I = np.array([a for a, b in pairs]); J = np.array([b for a, b in pairs])
    def cons(z):
        x = z[:-1].reshape(n, 2); d2 = ((x[I] - x[J]) ** 2).sum(1)
        return np.concatenate([d2 - 1.0, z[-1] ** 2 - d2])
    D0 = max(math.dist(a, b) for a, b in itertools.combinations(x0, 2))
    res = minimize(lambda z: z[-1], np.concatenate([x0.ravel(), [D0]]), method='SLSQP',
                   constraints=[{'type': 'ineq', 'fun': cons}], options={'maxiter': 800, 'ftol': 1e-14})
    x = res.x[:-1].reshape(n, 2)
    dmin = min(math.dist(a, b) for a, b in itertools.combinations(x, 2))
    if dmin < 1 - 1e-7: return None
    x = x / dmin
    return max(math.dist(a, b) for a, b in itertools.combinations(x, 2)), x

def contact_triangles(x, tol=1e-6):
    n = len(x); unit = {(a, b) for a, b in itertools.combinations(range(n), 2) if abs(math.dist(x[a], x[b]) - 1) < tol}
    return sum(1 for a, b, c in itertools.combinations(range(n), 3) if (a, b) in unit and (a, c) in unit and (b, c) in unit), len(unit)

if __name__ == '__main__':
    lo, hi, starts, seed = (int(a) for a in sys.argv[1:5])
    rng = np.random.default_rng(seed)
    for n in range(lo, hi + 1):
        found = []
        for s in range(starts):
            if s % 3 == 0:
                pts = [(i + 0.5 * j, j * math.sqrt(3) / 2) for i in range(-5, 6) for j in range(-5, 6)]
                c = rng.normal(0, 0.7, 2); pts.sort(key=lambda q: (q[0] - c[0]) ** 2 + (q[1] - c[1]) ** 2)
                x0 = np.array(pts[:n]) + rng.normal(0, 0.08, (n, 2))
            else:
                x0 = rng.uniform(-1, 1, (n, 2)) * math.sqrt(n) * 0.6
            x0 = x0 / max(1e-9, min(math.dist(a, b) for a, b in itertools.combinations(x0, 2)))
            r = local_min(n, x0)
            if r: found.append((r[0],) + contact_triangles(r[1]))
        found.sort()
        best = found[0]; tf = next((f for f in found if f[1] == 0), None)
        gap = (tf[0] - best[0]) if tf else float('nan')
        print(f'n={n:2d}: best {best[0]:.6f} ({best[1]} contact triangles, {best[2]} unit pairs); '
              f'best triangle-free local min {tf[0] if tf else float("nan"):.6f}; gap {gap:.2e}; '
              f'{len(found)} minima', flush=True)
# OUTCOME (2026-10-22 16:24 BST, Cloud, CL556): 60 starts per n (n = 18 and 20 hit the 470 s limit). Best overall vs best
# triangle-free LOCAL minimum (contact triangles at tolerance 1e-6):
# n=10 2.777311 (2 tri) vs 2.788420, gap 1.1e-2;  n=11 2.867455 (1) vs 3.196227, gap 0.33;
# n=12 2.909313 (7) vs 3.211508, gap 0.30;        n=13 3.151196 (2) vs 3.196227, gap 4.5e-2;
# n=14 3.315828 (1) vs 3.323172, gap 7.3e-3;      n=15 3.469645 (2) vs 3.492585, gap 2.3e-2;
# n=16 3.590157 (1) vs 3.830649, gap 0.24;        n=17 3.753734 (5) vs 3.830649, gap 7.7e-2;
# n=19 3.863703 (12) vs 4.148115, gap 0.28.
# The prediction held at every n: each best-found minimum has a contact triangle, and no triangle-free local minimum
# comes within 7e-3. (n = 15 also improved on min_diameter.py's 3.50448.) Measurements only; nothing certified.
# OUTCOME 2 (2026-10-22 16:37 BST, Cloud, CL557): 36 starts each. n=18 3.837353 (3 tri) vs triangle-free 4.148115, gap 0.31;
# n=20 4.090785 (2) vs 4.148115, gap 5.7e-2; n=21 4.216038 (1) vs 4.469734, gap 0.25; n=22 4.365087 (2) vs 4.469734,
# gap 0.10. Unexpected: the best triangle-free diameters repeat across n (3.196227 at n = 11, 13; 3.830649 at 16, 17;
# 4.148115 at 18, 19, 20; 4.469734 at 21, 22), so triangle-free local minima look like fixed families with loose points.
