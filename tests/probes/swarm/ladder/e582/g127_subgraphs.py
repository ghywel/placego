"""g127_subgraphs.py: Erdős #582: are induced subgraphs of Exoo's G127 on m <= 100 vertices easy to colour?

RUN-ON:  cpu, python3 with python-sat.  COST: about a minute.  COMMAND: python3 tests/probes/swarm/ladder/e582/g127_subgraphs.py
Why (CL550): if G127 -> (3,3)^e (Exoo's conjecture), a Folkman graph on <= 100 vertices could hide among its induced
subgraphs. Measure the solver's time to colour random induced subgraphs, by size m.
PREDICTIONS (before the run): every subgraph with m <= 100 is SAT in under a second; the median time climbs steeply
only near m = 127. Counterfactual: a TIMEOUT at m <= 100 is a lead (re-run long, then an UNSAT proof would be a
prize-won candidate). Unexpected check: the subgraph on the 2/3 of Z_127 that is an interval [0, 85) behaves like the
random ones.
"""
import random, time
from pysat.solvers import Cadical153
p = 127; H = {pow(3, 3 * i, p) for i in range(42)}
adj = [set((v + s) % p for s in H) for v in range(p)]

def colour(vs, budget=5.0):
    vs = sorted(vs); vset = set(vs); eid = {}
    for u in vs:
        for v in adj[u] & vset:
            if u < v: eid[(u, v)] = len(eid) + 1
    s = Cadical153(); t = 0
    for u in vs:
        for v in adj[u] & vset:
            if v <= u: continue
            for w in adj[u] & adj[v] & vset:
                if w <= v: continue
                e = [eid[(u, v)], eid[(u, w)], eid[(v, w)]]; s.add_clause(e); s.add_clause([-x for x in e]); t += 1
    t0 = time.time(); res = None
    while time.time() - t0 < budget:
        s.conf_budget(5000); r = s.solve_limited()
        if r is not None: res = r; break
    dt = time.time() - t0; s.delete()
    return ('SAT' if res else 'UNSAT') if res is not None else 'TIMEOUT', dt, t

rnd = random.Random(127)
for m in (60, 80, 90, 100, 110, 115, 120, 124, 126):
    rows = [colour(rnd.sample(range(p), m)) for _ in range(6)]
    res = sorted(r for r, _, _ in rows); ts = sorted(d for _, d, _ in rows)
    print(f'm={m:3d}: {res}  median time {ts[len(ts)//2]:.2f}s  triangles ~{rows[0][2]}')
print('interval [0,85):', colour(range(85)))
# OUTCOME (2026-10-22 15:03 BST, Cloud, CL550): the prediction FAILED. m = 60: all 6 SAT at once; m = 80, 90, 100, 110, 115, 120,
# 124 and 126: all 6 TIMEOUT at 5 s (about 2,500 to 9,500 triangles). The interval [0, 85) is also a TIMEOUT. So
# random induced subgraphs of G127 turn hard for the solver well below 100 vertices. g127_threshold.py places the turn.
