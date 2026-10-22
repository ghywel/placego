# Search for C4-free graphs on N = k*m + f vertices (f in {0,1}) with minimum degree >= d that are invariant
# under a semiregular Z_m action with k orbits (plus f fixed points). Orbit variables -> tiny SAT instance.
# Usage: python3 sym_search.py N d m f [timeout]
import sys, os, itertools, time
from satlib import CNF

def build(N, d, m, f):
    k = (N - f) // m
    assert k * m + f == N and f in (0, 1)
    cnf = CNF()
    var = {}
    def V(key):
        if key not in var:
            var[key] = cnf.var()
        return var[key]
    def vid(o, x):  # vertex id
        return o * m + (x % m)
    FIX = k * m
    edgevar = {}
    for o in range(k):
        for x in range(m):
            u = vid(o, x)
            for dd in range(1, m):
                w = vid(o, x + dd)
                r = min(dd, m - dd)
                edgevar[(u, w)] = V(('in', o, r))
            for o2 in range(k):
                if o2 == o:
                    continue
                for y in range(m):
                    w = vid(o2, y)
                    if o < o2:
                        edgevar[(u, w)] = V(('bt', o, o2, (y - x) % m))
                    else:
                        edgevar[(u, w)] = V(('bt', o2, o, (x - y) % m))
            if f:
                edgevar[(u, FIX)] = V(('fx', o))
                edgevar[(FIX, u)] = V(('fx', o))
    def ev(a, b):
        return edgevar[(a, b)]
    clauses = set()
    for a, b, c, e in itertools.combinations(range(N), 4):
        for (w, x, y, z) in ((a, b, c, e), (a, b, e, c), (a, c, b, e)):
            cl = frozenset((ev(w, x), ev(x, y), ev(y, z), ev(z, w)))
            clauses.add(cl)
    for cl in clauses:
        cnf.add([-v for v in cl])
    # degree constraints, one representative per orbit (+ fixed point)
    reps = [vid(o, 0) for o in range(k)] + ([FIX] if f else [])
    for u in reps:
        lits = [ev(u, w) for w in range(N) if w != u]
        n = len(lits)
        R = [[None] * (d + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, min(i, d) + 1):
                R[i][j] = cnf.var()
        for i in range(1, n + 1):
            for j in range(1, min(i, d) + 1):
                ps = R[i - 1][j] if j <= i - 1 else None
                pl = R[i - 1][j - 1] if j - 1 >= 1 else None
                c = [-R[i][j], lits[i - 1]] + ([ps] if ps else [])
                cnf.add(c)
                if j - 1 >= 1:
                    cnf.add([-R[i][j], pl] + ([ps] if ps else []))
        if n < d:
            cnf.add([])
        else:
            cnf.add([R[n][d]])
    return cnf, ev, len(var), len(clauses)

def verify(N, d, model, ev):
    adj = [[w for w in range(N) if w != u and ev(u, w) in model] for u in range(N)]
    S = [set(a) for a in adj]
    for u in range(N):
        for w in adj[u]:
            assert u in S[w]
    mind = min(len(a) for a in adj)
    c4 = any(len(S[i] & S[j]) > 1 for i in range(N) for j in range(i + 1, N))
    return mind, c4, adj

if __name__ == '__main__':
    N, d, m, f = map(int, sys.argv[1:5])
    tmo = int(sys.argv[5]) if len(sys.argv) > 5 else 60
    t0 = time.time()
    cnf, ev, nvar, ncl = build(N, d, m, f)
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, 'cnf', 'sym_N%d_d%d_m%d_f%d.cnf' % (N, d, m, f))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    st, model, dt = cnf.solve(path, timeout=tmo)
    msg = 'sym N=%d d=%d m=%d k=%d f=%d orbitvars=%d c4clauses=%d : %s (solve %.1fs, total %.1fs)' % (
        N, d, m, (N - f) // m, f, nvar, ncl, st, dt, time.time() - t0)
    if st == 'SATISFIABLE':
        mind, c4, adj = verify(N, d, model, ev)
        msg += ' verified mindeg=%d C4=%s' % (mind, c4)
        assert mind >= d and not c4
        with open(os.path.join(here, 'graph_sym_N%d_d%d_m%d_f%d.txt' % (N, d, m, f)), 'w') as fo:
            for v in range(N):
                fo.write('%d: %s\n' % (v, ' '.join(map(str, adj[v]))))
    print(msg, flush=True)
    os.remove(path)
