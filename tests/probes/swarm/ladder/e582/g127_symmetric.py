"""g127_symmetric.py: Erdős #582: symmetric colourings of G127 and of its coset-structured subgraphs.

RUN-ON: cpu, python3 with python-sat. COMMAND: python3 tests/probes/swarm/ladder/e582/g127_symmetric.py
Why (CL553): a colouring invariant under a symmetry is a small SAT problem, and any solution colours the graph, killing
it as a Folkman candidate. (a) Translation-invariant colourings of G127: an edge {x, x+s} gets the colour of its
difference class {s, -s}; a triangle x, x+a, x+a+b (a, b, a+b in S) is good iff the classes of a, b, a+b are not all
one colour. (b) Plain SAT on the multiplicatively invariant subgraphs: two cosets of the cube residues (84 vertices)
and the same plus 0 (85 vertices).
PREDICTIONS (before the run): (a) UNSAT, since a SAT answer would colour G127 and refute Exoo's conjecture; (b) TIMEOUT
at 60 s, like random subgraphs of that size. Counterfactual: (a) SAT means a verified colouring of G127 (checked
triangle by triangle); (b) SAT kills those structured candidates.
"""
import time
from pysat.solvers import Cadical153
p = 127; S = sorted({pow(3, 3 * i, p) for i in range(42)})
cls = {}
for s in S: cls.setdefault(min(s, p - s), len(cls) + 1)
var = lambda s: cls[min(s, p - s)]
sv = Cadical153(); n = 0
for a in S:
    for b in S:
        c = (a + b) % p
        if c in S and c != 0:
            e = [var(a), var(b), var(c)]; sv.add_clause(e); sv.add_clause([-x for x in e]); n += 1
r = sv.solve()
print(f'(a) translation-invariant colourings of G127: {len(cls)} difference classes, {n} triangle clauses pairs: {"SAT" if r else "UNSAT"}')
if r:
    m = set(x for x in sv.get_model() if x > 0); col = lambda s: var(s) in m
    ok = all(len({col(a), col(b), col((a + b) % p)}) == 2 for a in S for b in S if (a + b) % p in S)
    print('   colouring check:', ok)
sv.delete()
adj = [set((v + s) % p for s in S) for v in range(p)]
g = 3; C0 = {pow(g, 3 * i, p) for i in range(42)}; C1 = {(g * x) % p for x in C0}; C2 = {(g * x) % p for x in C1}
for name, vs in (('C0 u C1 (84)', C0 | C1), ('C0 u C1 u {0} (85)', C0 | C1 | {0}), ('C0 u C2 u {0} (85)', C0 | C2 | {0})):
    vset = set(vs); eid = {}
    for u in sorted(vset):
        for v in adj[u] & vset:
            if u < v: eid[(u, v)] = len(eid) + 1
    s2 = Cadical153(); t = 0
    for u in sorted(vset):
        for v in adj[u] & vset:
            if v <= u: continue
            for w in adj[u] & adj[v] & vset:
                if w <= v: continue
                e = [eid[(u, v)], eid[(u, w)], eid[(v, w)]]; s2.add_clause(e); s2.add_clause([-x for x in e]); t += 1
    t0 = time.time(); res = None
    while time.time() - t0 < 60:
        s2.conf_budget(20000); rr = s2.solve_limited()
        if rr is not None: res = rr; break
    print(f'(b) {name}: {len(eid)} edges, {t} triangles: ' + (('SAT' if res else 'UNSAT') if res is not None else 'TIMEOUT') + f' in {time.time()-t0:.0f}s', flush=True)
    s2.delete()
# OUTCOME (2026-10-22 15:37 BST, Cloud, CL553): (a) UNSAT: G127 has no translation-invariant good colouring (21 difference
# classes). (b) the coset subgraphs C0 u C1 (84 vertices, 1,197 edges, 3,080 triangles), C0 u C1 u {0} (85) and
# C0 u C2 u {0} (85) are each a TIMEOUT at 60 s. Both predictions held.
