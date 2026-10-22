"""kkt_check.py: Erdős #99: are triangle-free local minima of the diameter problem genuine KKT points?

RUN-ON: cpu, python3 with numpy and scipy. COMMAND: python3 tests/probes/swarm/ladder/e99/kkt_check.py N STARTS SEED
Why (CL557): CL556 proposed a force-balance (KKT) route to forcing a unit triangle. At a local minimum of D subject to
|x_i - x_j| >= 1 and |x_i - x_j| <= D there are lambda_ij >= 0 on the contact pairs and mu_kl >= 0 on the diameter
pairs with sum(mu) = 1 and, at every point i, sum_j lambda_ij (x_i - x_j)/|.| = sum_l mu_il (x_i - x_l)/|.|. If a
triangle-free local minimum satisfies this, first-order conditions cannot force a triangle.
PREDICTIONS (before the run): the best triangle-free local minimum for n = 10 (and 11) is a KKT point: the
nonnegative least-squares force-balance residual is below 1e-6. Counterfactual: a residual far from 0 would mean the
"minima" are not genuine (solver artefacts) and the KKT route stays open.
"""
import itertools, math, sys
import numpy as np
from scipy.optimize import nnls
sys.path.insert(0, 'tests/probes/swarm/ladder/e99')
from contact_catalog import local_min, contact_triangles

def kkt_residual(x, tol=1e-6):
    n = len(x); pairs = list(itertools.combinations(range(n), 2))
    D = max(math.dist(x[a], x[b]) for a, b in pairs)
    contact = [(a, b) for a, b in pairs if abs(math.dist(x[a], x[b]) - 1) < tol]
    diam = [(a, b) for a, b in pairs if abs(math.dist(x[a], x[b]) - D) < tol]
    cols = []
    for (a, b), sign in [(c, 1) for c in contact] + [(d, -1) for d in diam]:
        u = (x[a] - x[b]) / math.dist(x[a], x[b]); col = np.zeros(2 * n + 1)
        col[2 * a:2 * a + 2] += sign * u; col[2 * b:2 * b + 2] -= sign * u   # contact pushes apart, diameter pulls in
        if sign < 0: col[-1] = 1.0
        cols.append(col)
    A = np.array(cols).T; rhs = np.zeros(2 * n + 1); rhs[-1] = 1.0     # sum(mu) = 1
    w, res = nnls(A, rhs)
    return res, len(contact), len(diam)

if __name__ == '__main__':
    n, starts, seed = (int(a) for a in sys.argv[1:4])
    rng = np.random.default_rng(seed); found = []
    for s in range(starts):
        if s % 3 == 0:
            pts = [(i + 0.5 * j, j * math.sqrt(3) / 2) for i in range(-5, 6) for j in range(-5, 6)]
            c = rng.normal(0, 0.7, 2); pts.sort(key=lambda q: (q[0] - c[0]) ** 2 + (q[1] - c[1]) ** 2)
            x0 = np.array(pts[:n]) + rng.normal(0, 0.08, (n, 2))
        else:
            x0 = rng.uniform(-1, 1, (n, 2)) * math.sqrt(n) * 0.6
        x0 = x0 / max(1e-9, min(math.dist(a, b) for a, b in itertools.combinations(x0, 2)))
        r = local_min(n, x0)
        if r: found.append((r[0], contact_triangles(r[1])[0], r[1]))
    found.sort(key=lambda f: f[0])
    best = found[0]; tf = next(f for f in found if f[1] == 0)
    for name, (D, tri, x) in (('best', best), ('best triangle-free', tf)):
        res, nc, nd = kkt_residual(x)
        print(f'n={n} {name}: D = {D:.6f}, contact triangles {tri}, {nc} contact and {nd} diameter pairs, KKT residual {res:.2e}', flush=True)
# OUTCOME (2026-10-22 16:37 BST, Cloud, CL557): the prediction held. n = 10: best D = 2.777311 (2 contact triangles) and best
# triangle-free D = 2.788420 are BOTH KKT points (NNLS force-balance residuals 1.6e-16 and 9.0e-17). n = 11: best
# 2.867455 (1 triangle) and triangle-free 3.211508, residuals 9.1e-17 and 1.4e-16. So first-order conditions cannot
# force a unit triangle; any proof must compare diameters globally.
