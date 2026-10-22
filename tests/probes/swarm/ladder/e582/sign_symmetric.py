"""sign_symmetric.py: Erdős #582: sign-invariant colourings of sign-symmetric induced subgraphs of G127 (90-100 vertices).

RUN-ON: cpu, python3 with python-sat. COMMAND: python3 tests/probes/swarm/ladder/e582/sign_symmetric.py
Why (CL554): x -> -x is an automorphism of G127 (the cubes contain -1). On a vertex set V = -V it acts on the induced
subgraph; a colouring constant on its edge orbits is a SAT problem of half the size. A solution colours the subgraph
(killing it as a Folkman candidate); UNSAT only excludes symmetric colourings. Third angle on #582 after CL550-553.
PREDICTIONS (before the run): at 90 to 100 vertices every sample is TIMEOUT or UNSAT at 30 s, so no subgraph is killed.
Counterfactual: SAT colourings at 94-100 vertices would show these subgraphs are colourable and only hard for plain SAT.
Unexpected check: the same at 80 vertices, where plain SAT finds colourings: does a symmetric colouring exist there?
"""
import random, time
from pysat.solvers import Cadical153
p = 127; S = {pow(3, 3 * i, p) for i in range(42)}
adj = [set((v + s) % p for s in S) for v in range(p)]
def run(V, budget=30):
    V = set(V); edges = sorted((u, v) for u in V for v in adj[u] & V if u < v)
    orb = {}
    for u, v in edges:
        if (u, v) in orb: continue
        k = len(set(orb.values())) + 1
        orb[(u, v)] = k; a, b = sorted(((-u) % p, (-v) % p)); orb[(a, b)] = k
    tris = [(u, v, w) for u in V for v in adj[u] & V if v > u for w in adj[u] & adj[v] & V if w > v]
    s = Cadical153(); seen = set()
    for u, v, w in tris:
        e = tuple(sorted({orb[(u, v)], orb[(u, w)], orb[(v, w)]}))
        if e in seen: continue
        seen.add(e)
        if len(e) == 1: s.add_clause([e[0]]); s.add_clause([-e[0]])   # all three edges in one orbit: impossible
        else: s.add_clause(list(e)); s.add_clause([-x for x in e])
    t0 = time.time(); res = None
    while time.time() - t0 < budget:
        s.conf_budget(20000); r = s.solve_limited()
        if r is not None: res = r; break
    out = ('SAT' if res else 'UNSAT') if res is not None else 'TIMEOUT'
    if res:
        m = set(x for x in s.get_model() if x > 0); col = lambda a, b: orb[(min(a, b), max(a, b))] in m
        out += ' (verified)' if all(len({col(u, v), col(u, w), col(v, w)}) == 2 for u, v, w in tris) else ' (CHECK FAILED)'
    s.delete(); return out, time.time() - t0, len(set(orb.values()))
rnd = random.Random(554)
pairs = list(range(1, 64))
for m in (80, 90, 94, 100):
    for i in range(3):
        k = m // 2; V = set()
        for x in rnd.sample(pairs, k): V |= {x, p - x}
        if m % 2: V.add(0)
        r, dt, nv = run(V)
        print(f'm={len(V)} #{i}: {r} in {dt:.1f}s ({nv} orbit variables)', flush=True)
# OUTCOME (2026-10-22 15:58 BST, Cloud, CL554): m = 80: 3 of 3 SAT with verified symmetric colourings (at most 0.6 s); m = 90,
# 94 and 100: 9 of 9 TIMEOUT at 30 s (669 to 838 orbit variables). The prediction held. Unexpected check: the
# threshold between 80 and 90 vertices survives halving the problem by the sign symmetry.
