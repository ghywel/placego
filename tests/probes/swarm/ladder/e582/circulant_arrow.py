"""circulant_arrow.py: Erdős #582 (Graham's $100): look for a K4-free graph on at most 100 vertices that arrows (3,3)^e.

RUN-ON:  cpu (4 cores), python3 with python-sat (pip install python-sat).  COST: minutes.
COMMAND: python3 tests/probes/swarm/ladder/e582/circulant_arrow.py [seconds_per_instance]
Why (CL550): G -> (3,3)^e means every red/blue colouring of G's edges has a one-colour triangle. The prize asks whether
some K4-free G on at most 100 vertices does it (known: 21 <= F_e(3,3;4) <= 786; Exoo conjectured that the cube-residue
Cayley graph G127 on Z_127 arrows, which would still be 127 > 100). Encoding: one variable per edge, and for every
triangle two clauses (not all red, not all blue). SAT = a good colouring exists (G does not arrow); UNSAT = G arrows.
Candidates: (a) Cayley graphs on Z_p, p prime <= 100, whose connection set is a union of cosets of the k-th power
residues (the family G127 comes from), for every k | p - 1 with k <= 12 and every union; (b) random symmetric circulants.
Each is kept if it is K4-free. (A first version also demanded that every edge lie in a triangle; that is wrong as a
filter, since edges outside triangles never stop a graph arrowing, so the corrected run keeps every K4-free graph.)
Record searched: Folkman, arrow triangle -> no prior work in the record (only the ladder row).
PREDICTIONS (written before the run): every K4-free candidate on <= 100 vertices is SAT, found in under a second
(dense-enough small Folkman graphs are believed not to exist; the 786 bound needed a large graph). Counterfactual:
any UNSAT within the time limit is a prize-won candidate and must be re-proved with a checked DRAT certificate.
Unexpected check: the same code on G127 itself (k = 3 residues mod 127), whose status is famously unknown: predict
the solver does NOT finish within the limit (neither SAT nor UNSAT).
"""
import itertools, random, sys, time
from pysat.solvers import Cadical153

LIMIT = float(sys.argv[1]) if len(sys.argv) > 1 else 20.0

def graph(n, S):
    S = {s % n for s in S} - {0}
    S |= {(-s) % n for s in S}
    adj = [set((v + s) % n for s in S) for v in range(n)]
    return S, adj

def k4_free_and_triangles(n, S, adj):
    # Cayley graph: check through vertex 0 only (vertex-transitive)
    nb = sorted(adj[0])
    tri_edge = {s: False for s in S}
    for a, b in itertools.combinations(nb, 2):
        if b in adj[a]:
            tri_edge[a] = tri_edge[b] = True
            for c in nb:
                if c > b and c in adj[a] and c in adj[b]:
                    return False, False
    return True, all(tri_edge.values())

def arrows(n, adj, limit):
    eid = {}
    for u in range(n):
        for v in adj[u]:
            if u < v: eid[(u, v)] = len(eid) + 1
    s = Cadical153()
    ntri = 0
    for u in range(n):
        for v in adj[u]:
            if v <= u: continue
            for w in adj[u] & adj[v]:
                if w <= v: continue
                e = [eid[(u, v)], eid[(u, w)], eid[(v, w)]]
                s.add_clause(e); s.add_clause([-x for x in e]); ntri += 1
    if ntri == 0: return 'SAT', 0, len(eid)
    t0 = time.time()
    # pysat: solve_limited with a time budget via conflict budget loop
    res = None
    while time.time() - t0 < limit:
        s.conf_budget(20000)
        r = s.solve_limited()
        if r is not None: res = r; break
    s.delete()
    return ('SAT' if res else 'UNSAT') if res is not None else 'TIMEOUT', ntri, len(eid)

def residue_family(p):
    g = next(g for g in range(2, p) if all(pow(g, (p - 1) // q, p) != 1 for q in {q for q in range(2, p) if (p - 1) % q == 0 and all(q % r for r in range(2, q))}))
    for k in range(2, 13):                       # at most 12 cosets, so at most 2^12 unions per prime
        if (p - 1) % k: continue
        H = {pow(g, k * i, p) for i in range((p - 1) // k)}
        cosets = [{(pow(g, j, p) * h) % p for h in H} for j in range(k)]
        for r in range(1, k):
            for idx in itertools.combinations(range(k), r):
                S = set().union(*(cosets[i] for i in idx))
                yield k, idx, S

def run():
    primes = [p for p in range(7, 101) if all(p % q for q in range(2, int(p ** .5) + 1))]
    seen, out = set(), {'SAT': 0, 'UNSAT': 0, 'TIMEOUT': 0}
    cands = []
    for p in primes:
        for k, idx, S in residue_family(p):
            if len(S) > 40 or len(S) < 4: continue
            S, adj = graph(p, S)
            key = (p, frozenset(S))
            if key in seen: continue
            seen.add(key)
            ok, tri = k4_free_and_triangles(p, S, adj)
            if ok: cands.append((f'Z{p} k={k} cosets={idx}', p, adj))
    rnd = random.Random(582)
    for _ in range(4000):
        n = rnd.randint(20, 100); d = rnd.randint(3, min(12, n // 2))
        S, adj = graph(n, rnd.sample(range(1, n // 2 + 1), d))
        key = (n, frozenset(S))
        if key in seen: continue
        seen.add(key)
        ok, tri = k4_free_and_triangles(n, S, adj)
        if ok: cands.append((f'C{n} S={sorted(x for x in S if x <= n // 2)}', n, adj))
    print(f'{len(cands)} K4-free candidates')
    for name, n, adj in cands:
        r, ntri, ne = arrows(n, adj, LIMIT)
        out[r] += 1
        if r != 'SAT': print(f'  {r}: {name}  ({ne} edges, {ntri} triangles)')
    print('totals:', out)
    p = 127
    g = 3
    H = {pow(g, 3 * i, p) for i in range(42)}
    S, adj = graph(p, H)
    ok, tri = k4_free_and_triangles(p, S, adj)
    print(f'G127 (cube residues): K4-free={ok}, every edge in a triangle={tri}, |S|={len(S)}')
    print('G127 arrowing within limit:', arrows(p, adj, LIMIT))

if __name__ == '__main__':
    run()
# OUTCOME (2026-10-22 15:03 BST, Cloud, CL550): corrected run (K4-free only, no triangle filter), 3 s per instance: 3,468
# K4-free circulants and residue-coset Cayley graphs on <= 100 vertices, ALL SAT (each has a colouring with no
# one-colour triangle, so none arrows). The first run, with the wrong triangle filter, had 1,359 candidates, all SAT.
# Prediction held. Unexpected check: G127 itself (K4-free, every edge in a triangle, degree 42, 2,667 edges, 9,779
# triangles) is a TIMEOUT at 3 s, as predicted.
