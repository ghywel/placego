"""g127_mult_invariant.py: Erdős #582: colourings of G127 invariant under multiplication by a subgroup K of the cubes.

RUN-ON: cpu, python3 with python-sat. COMMAND: python3 tests/probes/swarm/ladder/e582/g127_mult_invariant.py
Why (CL553): x -> kx (k a cube residue) is an automorphism of G127 fixing 0. A K-invariant colouring gives the edges
of one K-orbit one colour: fewer variables, an easier SAT problem. A solution colours G127 and refutes Exoo's
conjecture; UNSAT for every K only rules out symmetric colourings. Subgroups of the cube group (order 42): orders 2
(the sign), 3, 6, 7, 14, 21, 42.
PREDICTIONS (before the run): UNSAT (or TIMEOUT) for every K; no colouring of G127. Counterfactual: SAT for some K, a
verified colouring of G127 and a refutation of Exoo's conjecture (to be re-checked independently before any claim).
"""
import time
from pysat.solvers import Cadical153
p = 127; S = {pow(3, 3 * i, p) for i in range(42)}
adj = [set((v + s) % p for s in S) for v in range(p)]
edges = sorted((u, v) for u in range(p) for v in adj[u] if u < v)
tris = [(u, v, w) for u in range(p) for v in adj[u] if v > u for w in adj[u] & adj[v] if w > v]
g3 = 27   # 3^3 generates the cube group (order 42)
assert len({pow(g3, i, p) for i in range(42)}) == 42
for order in (2, 3, 6, 7, 14, 21, 42):
    gen = pow(g3, 42 // order, p); K = {pow(gen, i, p) for i in range(order)}
    orbit = {}
    for (u, v) in edges:
        if (u, v) in orbit: continue
        idx = len(set(orbit.values())) + 1
        for k in K:
            a, b = sorted(((k * u) % p, (k * v) % p)); orbit[(a, b)] = idx
    nvar = len(set(orbit.values()))
    s = Cadical153(); seen = set()
    for u, v, w in tris:
        e = tuple(sorted((orbit[(u, v)], orbit[(u, w)], orbit[(v, w)])))
        if e in seen: continue
        seen.add(e)
        s.add_clause(list(e)); s.add_clause([-x for x in e])
    t0 = time.time(); res = None
    while time.time() - t0 < 40:
        s.conf_budget(20000); r = s.solve_limited()
        if r is not None: res = r; break
    verdict = ('SAT' if res else 'UNSAT') if res is not None else 'TIMEOUT'
    extra = ''
    if res:
        m = set(x for x in s.get_model() if x > 0); col = lambda a, b: orbit[(min(a, b), max(a, b))] in m
        extra = ' colouring check: ' + str(all(len({col(u, v), col(u, w), col(v, w)}) == 2 for u, v, w in tris))
    print(f'|K| = {order:2d}: {nvar} orbit variables, {len(seen)} distinct triangle patterns: {verdict} in {time.time()-t0:.1f}s{extra}', flush=True)
    s.delete()
# OUTCOME (2026-10-22 15:37 BST, Cloud, CL553): |K| = 3, 6, 7, 14, 21, 42: UNSAT at once (no K-invariant good colouring of
# G127); |K| = 2 (the sign, x -> -x; 1,344 orbit variables): TIMEOUT at 40 s. Prediction held; no colouring found.
# These UNSATs are solver verdicts without a DRAT check, and they only exclude symmetric colourings.
