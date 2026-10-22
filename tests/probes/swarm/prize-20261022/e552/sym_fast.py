# Same model as sym_search.py, but C4 clauses are generated only for 4-cycles through orbit representatives
# (every C4 orbit under the Z_m action contains such a cycle), so large N is cheap.
# Usage: python3 sym_fast.py N d m f [timeout]
import sys, os, time
from satlib import CNF
import sym_search as S

def build_fast(N, d, m, f):
    k = (N - f) // m
    assert k * m + f == N and f in (0, 1)
    cnf = CNF()
    var = {}
    def V(key):
        if key not in var:
            var[key] = cnf.var()
        return var[key]
    def vid(o, x):
        return o * m + (x % m)
    FIX = k * m
    ev = [[0] * N for _ in range(N)]
    for o in range(k):
        for x in range(m):
            u = vid(o, x)
            for dd in range(1, m):
                w = vid(o, x + dd)
                ev[u][w] = V(('in', o, min(dd, m - dd)))
            for o2 in range(k):
                if o2 == o:
                    continue
                for y in range(m):
                    w = vid(o2, y)
                    ev[u][w] = V(('bt', o, o2, (y - x) % m)) if o < o2 else V(('bt', o2, o, (x - y) % m))
            if f:
                ev[u][FIX] = ev[FIX][u] = V(('fx', o))
    reps = [vid(o, 0) for o in range(k)] + ([FIX] if f else [])
    clauses = set()
    for r in reps:
        for a in range(N):
            if a == r:
                continue
            era = ev[r][a]
            for c in range(a + 1, N):
                if c == r:
                    continue
                erc = ev[r][c]
                for b in range(N):
                    if b == r or b == a or b == c:
                        continue
                    clauses.add(frozenset((era, ev[a][b], ev[b][c], erc)))
    for cl in clauses:
        cnf.add([-v for v in cl])
    for u in reps:
        lits = [ev[u][w] for w in range(N) if w != u]
        n = len(lits)
        R = [[None] * (d + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, min(i, d) + 1):
                R[i][j] = cnf.var()
        for i in range(1, n + 1):
            for j in range(1, min(i, d) + 1):
                ps = R[i - 1][j] if j <= i - 1 else None
                cnf.add([-R[i][j], lits[i - 1]] + ([ps] if ps else []))
                if j - 1 >= 1:
                    cnf.add([-R[i][j], R[i - 1][j - 1]] + ([ps] if ps else []))
        cnf.add([R[n][d]])
    return cnf, (lambda a, b: ev[a][b]), len(var), len(clauses)

if __name__ == '__main__':
    N, d, m, f = map(int, sys.argv[1:5])
    tmo = int(sys.argv[5]) if len(sys.argv) > 5 else 60
    solver = sys.argv[6] if len(sys.argv) > 6 else 'kissat'
    t0 = time.time()
    cnf, ev, nvar, ncl = build_fast(N, d, m, f)
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, 'cnf', 'symf_N%d_d%d_m%d_f%d.cnf' % (N, d, m, f))
    st, model, dt = cnf.solve(path, timeout=tmo, solver=solver)
    msg = 'symfast[%s] N=%d d=%d m=%d k=%d f=%d orbitvars=%d c4clauses=%d : %s (solve %.1fs, total %.1fs)' % (
        solver, N, d, m, (N - f) // m, f, nvar, ncl, st, dt, time.time() - t0)
    if st == 'SATISFIABLE':
        mind, c4, adj = S.verify(N, d, model, ev)
        msg += ' verified mindeg=%d C4=%s' % (mind, c4)
        assert mind >= d and not c4
        with open(os.path.join(here, 'graph_sym_N%d_d%d_m%d_f%d.txt' % (N, d, m, f)), 'w') as fo:
            for v in range(N):
                fo.write('%d: %s\n' % (v, ' '.join(map(str, adj[v]))))
    print(msg, flush=True)
    os.remove(path)
