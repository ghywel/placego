"""min_diameter.py: Erdős #99: best-found minimal-diameter sets of n points at mutual distance >= 1; unit triangles?

RUN-ON: cpu, python3 with numpy and scipy. COMMAND: python3 tests/probes/swarm/ladder/e99/min_diameter.py N_MIN N_MAX STARTS
Why (CL554): #99 asks whether, for all large n, every n-point set with minimum distance 1 and least diameter contains a
unit equilateral triangle ($100 for a counterexample, $50 for a proof). Exact minimisers are known only to n = 8
(n = 4, 5, 6 and 8 have no unit triangle; 7 has). A numerical survey cannot settle the question (minimality is not
certified); it maps which structures win and where triangle-free near-optimisers survive.
Method: minimise D over x subject to 1 <= |x_i - x_j| <= D (SLSQP), from random and hexagonal-lattice starts; count
unit triangles (all three sides within 1e-4 of 1) in the best configuration.
PREDICTIONS (before the run): calibration reproduces d(7) = 2 (with unit triangles) and d(8) = 1/(2 sin(pi/14)) =
2.2470 (none). For 9 <= n <= 16 the best-found configurations contain unit triangles except possibly n = 9 and 10.
Counterfactual: a triangle-free best at n >= 12 would be the first hint for the $100 direction.
"""
import itertools, math, sys
import numpy as np
from scipy.optimize import minimize

def solve(n, starts, rng):
    best = None
    pairs = list(itertools.combinations(range(n), 2))
    I = np.array([a for a, b in pairs]); J = np.array([b for a, b in pairs])
    def cons(z):
        x = z[:-1].reshape(n, 2); D = z[-1]
        d2 = ((x[I] - x[J]) ** 2).sum(1)
        return np.concatenate([d2 - 1.0, D * D - d2])
    for s in range(starts):
        if s % 3 == 0:     # hexagonal-lattice seed, randomly placed and jittered
            pts = [(i + 0.5 * j, j * math.sqrt(3) / 2) for i in range(-4, 5) for j in range(-4, 5)]
            c = rng.normal(0, 0.6, 2)
            pts.sort(key=lambda q: (q[0] - c[0]) ** 2 + (q[1] - c[1]) ** 2)
            x0 = np.array(pts[:n]) + rng.normal(0, 0.05, (n, 2))
        else:
            x0 = rng.uniform(-1, 1, (n, 2)) * math.sqrt(n) * 0.6
        x0 = x0 / max(1e-9, min(math.dist(a, b) for a, b in itertools.combinations(x0, 2)))
        D0 = max(math.dist(a, b) for a, b in itertools.combinations(x0, 2))
        res = minimize(lambda z: z[-1], np.concatenate([x0.ravel(), [D0]]), method='SLSQP',
                       constraints=[{'type': 'ineq', 'fun': cons}], options={'maxiter': 500, 'ftol': 1e-12})
        x = res.x[:-1].reshape(n, 2)
        dmin = min(math.dist(a, b) for a, b in itertools.combinations(x, 2))
        if dmin < 1 - 1e-6: continue
        x = x / dmin; D = max(math.dist(a, b) for a, b in itertools.combinations(x, 2))
        if best is None or D < best[0] - 1e-9: best = (D, x)
    return best

def unit_triangles(x, tol=1e-4):
    n = len(x); close = lambda a, b: abs(math.dist(x[a], x[b]) - 1) < tol
    return sum(1 for a, b, c in itertools.combinations(range(n), 3) if close(a, b) and close(a, c) and close(b, c))

if __name__ == '__main__':
    lo, hi, starts = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(99)
    for n in range(lo, hi + 1):
        D, x = solve(n, starts, rng)
        print(f'n={n:2d}: best diameter {D:.5f}, unit triangles {unit_triangles(x)}', flush=True)
# OUTCOME (2026-10-22 15:59 BST, Cloud, CL555): calibration PASS: d(6) = 1.90211 (2 sin 72°), d(7) = 2.00000 (6 unit triangles),
# d(8) = 2.24698 = 1/(2 sin(pi/14)) (none). Best found, 30 starts (n <= 12) and 24 starts (n >= 13):
# n=9 2.56924 (0 triangles; equals the published upper bound, about 2.5693), n=10 2.77731 (2), n=11 2.86745 (1),
# n=12 2.90931 (7), n=13 3.15120 (2), n=14 3.31583 (1), n=15 3.50448 (2), n=16 3.59016 (1), n=17 3.75373 (5),
# n=18 3.83856 (4), n=19 3.86370 (12), n=20 4.09079 (2). The prediction held (triangles from n = 10 on). Not
# certified optima; few triangles per configuration, so they look incidental rather than lattice-forced.
