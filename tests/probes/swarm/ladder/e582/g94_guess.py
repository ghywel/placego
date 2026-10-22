"""g94_guess.py: Erdős #582: a guess at Exoo's G94 (G127 minus 33 vertices) and a long solver run on it.

RUN-ON: cpu, python3 with python-sat. COMMAND: python3 tests/probes/swarm/ladder/e582/g94_guess.py BUDGET
Why (CL551): Radziszowski's 2018 slides record Graham's challenge ("Determine whether Fe(3,3;4) <= 100", $100, 2012)
and Exoo's conjecture that G127 -> (3,3)^e and that "removing 33 vertices from G127 gives graph G94, which still looks
good for arrowing, if so, worth $100". Which 33 vertices is not stated there. Guess: alpha(G127) = 11 and 33 = 3 x 11,
so remove three disjoint maximum independent sets. This is a guess about Exoo's construction, not a quotation.
PREDICTIONS (before the run): three disjoint independent 11-sets exist; the 94-vertex remainder is K4-free (inherited)
and the solver neither colours it nor refutes it within the budget (TIMEOUT), like the random 90- to 100-vertex
subgraphs. Counterfactual: SAT (a verified colouring) kills this guess at G94; UNSAT would be a prize-won lead needing a
DRAT proof and confirmation that this is a K4-free graph on 94 vertices.
"""
import sys, time
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
p = 127; H = {pow(3, 3 * i, p) for i in range(42)}
adj = [set((v + s) % p for s in H) for v in range(p)]

def independent_set(avail, k):
    """An independent k-set inside avail, by SAT (one variable per vertex)."""
    avail = sorted(avail); var = {v: i + 1 for i, v in enumerate(avail)}
    s = Cadical153()
    for u in avail:
        for w in adj[u]:
            if w in var and u < w: s.add_clause([-var[u], -var[w]])
    cnf = CardEnc.atleast(lits=list(var.values()), bound=k, top_id=len(avail), encoding=EncType.seqcounter)
    s.append_formula(cnf.clauses)
    if not s.solve(): return None
    m = set(x for x in s.get_model() if x > 0)
    return {v for v in avail if var[v] in m}

budget = float(sys.argv[1]) if len(sys.argv) > 1 else 120
avail = set(range(p)); removed = []
print('alpha >= 12?', independent_set(avail, 12) is not None, flush=True)
for _ in range(3):
    I = independent_set(avail, 11); print('independent 11-set:', sorted(I), flush=True)
    removed.append(I); avail -= I
vs = sorted(avail); vset = set(vs); print('G94 vertices:', len(vs), flush=True)
eid = {}
for u in vs:
    for v in adj[u] & vset:
        if u < v: eid[(u, v)] = len(eid) + 1
tris = [(u, v, w) for u in vs for v in adj[u] & vset if v > u for w in adj[u] & adj[v] & vset if w > v]
k4 = any(adj[a] & adj[b] & adj[c] & vset for a, b, c in tris)
print(f'edges {len(eid)}, triangles {len(tris)}, K4 present: {k4}', flush=True)
s = Cadical153()
for u, v, w in tris:
    e = [eid[(u, v)], eid[(u, w)], eid[(v, w)]]; s.add_clause(e); s.add_clause([-x for x in e])
t0 = time.time(); res = None
while time.time() - t0 < budget:
    s.conf_budget(50000); r = s.solve_limited()
    if r is not None: res = r; break
print('G94 guess:', ('SAT' if res else 'UNSAT') if res is not None else 'TIMEOUT', f'after {time.time()-t0:.0f}s', flush=True)
# OUTCOME (2026-10-22 15:23 BST, Cloud, CL551): alpha(G127) = 11 confirmed (no independent 12-set). Three disjoint independent
# 11-sets found ([11,42,45,68,71,102,114,117,120,123,126], its translate by -1, and [9,33,40,69,76,100,112,115,118,121,
# 124]); the remainder has 94 vertices, 1,463 edges, 3,977 triangles, K4-free. Solver: TIMEOUT at 158 s (prediction
# held). A 420 s run is logged in CL552. Whether this is Exoo's G94 is unknown.
