"""g127_subgraphs_lib.py: the colouring routine of g127_subgraphs.py, importable (CL550)."""

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

