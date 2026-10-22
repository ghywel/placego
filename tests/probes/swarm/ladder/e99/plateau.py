"""plateau.py: Erdős #99: what are the repeating triangle-free local minima of CL557?

RUN-ON: cpu, python3 with numpy and scipy. COMMAND: python3 tests/probes/swarm/ladder/e99/plateau.py N STARTS SEED
Why (CL559): CL557 found the best triangle-free local minima repeating their diameter across n (3.196227 at n = 11, 13;
4.148115 at n = 18, 19, 20). For each triangle-free local minimum found, split the points into a STRESSED CORE
(points on a contact pair or a diameter pair, tolerance 1e-6) and RATTLERS (points on neither), and report the core
size, contact and diameter pair counts, and the core's contact degree sequence.
Record searched: CL555-557, contact_catalog.py, kkt_check.py; GC1686, GC1689.
PREDICTIONS (before the run): each plateau diameter is ONE stressed core plus rattlers, the same core at every n on
the plateau (same core size, contact and diameter counts). Counterfactual: different cores with equal diameter (a
coincidence of the readout), or no rattlers at the larger n (the plateau would then be a different rigid family).
"""
import itertools, math, sys
import numpy as np
sys.path.insert(0, 'tests/probes/swarm/ladder/e99')
from contact_catalog import local_min, contact_triangles


def anatomy(x, tol=1e-6):
    n = len(x)
    D = max(math.dist(a, b) for a, b in itertools.combinations(x, 2))
    unit = [(a, b) for a, b in itertools.combinations(range(n), 2) if abs(math.dist(x[a], x[b]) - 1) < tol]
    diam = [(a, b) for a, b in itertools.combinations(range(n), 2) if abs(math.dist(x[a], x[b]) - D) < tol]
    core = sorted({p for e in unit + diam for p in e})
    deg = sorted((sum(p in e for e in unit) for p in core), reverse=True)
    return D, len(core), len(unit), len(diam), deg


if __name__ == '__main__':
    n, starts, seed = (int(a) for a in sys.argv[1:4])
    rng = np.random.default_rng(seed)
    seen = {}
    for s in range(starts):
        if s % 3 == 0:
            pts = [(i + 0.5 * j, j * math.sqrt(3) / 2) for i in range(-5, 6) for j in range(-5, 6)]
            c = rng.normal(0, 0.7, 2); pts.sort(key=lambda q: (q[0] - c[0]) ** 2 + (q[1] - c[1]) ** 2)
            x0 = np.array(pts[:n]) + rng.normal(0, 0.08, (n, 2))
        else:
            x0 = rng.uniform(-1, 1, (n, 2)) * math.sqrt(n) * 0.6
        x0 = x0 / max(1e-9, min(math.dist(a, b) for a, b in itertools.combinations(x0, 2)))
        r = local_min(n, x0)
        if not r or contact_triangles(r[1])[0]: continue
        D, core, nu, nd, deg = anatomy(r[1])
        key = round(D, 5)
        if key not in seen:
            seen[key] = (core, nu, nd, deg)
            np.save(f'{sys.argv[4]}/tf_n{n}_D{key}.npy', r[1]) if len(sys.argv) > 4 else None
    for key in sorted(seen)[:4]:
        core, nu, nd, deg = seen[key]
        print(f'n={n} D={key:.5f}: core {core}, rattlers {n - core}, unit pairs {nu}, diameter pairs {nd}, degrees {deg}',
              flush=True)

# OUTCOME (2026-10-22 17:20 BST, Cloud, CL559): 36 starts, seed 7. n=11 found NO compact triangle-free minimum with this
# seed (only unconverged spread-out ones, D > 8), a reminder that local_min does not check res.success; the readout is
# sorted, so the junk is harmless but the seed matters. n=13: triangle-free minima at 3.21151 (core 12, 1 rattler),
# 3.51334, 3.52310 (core 11, 2 rattlers) and 3.83065 (core 12, 1 rattler, irregular). The decisive reading: 3.513337
# and 4.148115 are EXACTLY the diameters of the regular unit-side 11-gon and 13-gon (polygon_rattlers.py). Prediction
# (one core plus rattlers per plateau) held for 4.148115; 3.196227, 3.830649 and 4.469734 are not regular polygons and
# were not identified this block.
