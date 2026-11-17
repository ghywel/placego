"""g127_long.py: Erdős #582: long solver budgets on hard induced subgraphs of G127 (80 to 100 vertices).

RUN-ON: cpu, python3 with python-sat. COMMAND: python3 tests/probes/swarm/ladder/e582/g127_long.py SEED M COUNT BUDGET
Why (CL551): CL550 found G127's random induced subgraphs hard to colour from about 80 vertices (heavy tail). A long
budget asks whether any is UNSAT (it would arrow, a prize-won lead needing a checked DRAT proof) or all colour.
PREDICTIONS (before the run): every sample is SAT within 60 s at m = 80 and 90; at m = 100 most are SAT, a few may
TIMEOUT. Counterfactual: an UNSAT result. Each SAT answer is checked: the colouring is verified triangle by triangle.
"""
import random, sys, time
sys.path.insert(0, 'tests/probes/swarm/ladder/e582')
from pysat.solvers import Cadical153
p = 127; H = {pow(3, 3 * i, p) for i in range(42)}
adj = [set((v + s) % p for s in H) for v in range(p)]

def run(vs, budget):
    vs = sorted(vs); vset = set(vs); eid = {}
    for u in vs:
        for v in adj[u] & vset:
            if u < v: eid[(u, v)] = len(eid) + 1
    tris = [(u, v, w) for u in vs for v in adj[u] & vset if v > u for w in adj[u] & adj[v] & vset if w > v]
    s = Cadical153()
    for u, v, w in tris:
        e = [eid[(u, v)], eid[(u, w)], eid[(v, w)]]; s.add_clause(e); s.add_clause([-x for x in e])
    t0 = time.time(); res = None
    while time.time() - t0 < budget:
        s.conf_budget(20000); r = s.solve_limited()
        if r is not None: res = r; break
    dt = time.time() - t0
    if res:
        model = set(x for x in s.get_model() if x > 0)
        col = lambda a, b: eid[(min(a, b), max(a, b))] in model
        ok = all(len({col(u, v), col(u, w), col(v, w)}) == 2 for u, v, w in tris)
        out = 'SAT (colouring verified)' if ok else 'SAT BUT CHECK FAILED'
    else:
        out = 'UNSAT' if res is not None else 'TIMEOUT'
    s.delete()
    return out, dt, len(tris)

if __name__ == '__main__':
    seed, m, count, budget = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
    rnd = random.Random(seed)
    for i in range(count):
        vs = rnd.sample(range(p), m)
        r, dt, t = run(vs, budget)
        print(f'seed {seed} m={m} #{i}: {r} in {dt:.1f}s ({t} triangles)', flush=True)
# OUTCOME (2026-10-22 15:23 BST, Cloud, CL551): m = 80, seed 55180: all 6 SAT, colourings verified, in 0.8 to 33.4 s (prediction
# held). m = 90 (seed 55190) and m = 100 (seed 551100): 4 of 4 each a TIMEOUT at 60 s, with three runs sharing 4
# cores (prediction FAILED for m = 90). No UNSAT.
