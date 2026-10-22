# Direct SAT: is there a C4-free graph on N vertices with minimum degree >= d?
# Symmetry breaking (sound): vertex 0 ~ 1..d; for i in 1..d, vertex i ~ a block B_i of d-2 fresh vertices,
# blocks consecutive and pairwise disjoint, none adjacent to 0 (C4-freeness makes the outside-neighbourhoods
# of the vertices of N(0) pairwise disjoint, and each has >= d-2 elements since N(0) induces a matching).
# Usage: python3 direct.py N d [timeout] [solver]
import sys, os, itertools, time
from satlib import CNF

def build(N, d, symbreak=True):
    cnf = CNF()
    E = {}
    for i in range(N):
        for j in range(i + 1, N):
            E[(i, j)] = cnf.var()
    def e(i, j):
        return E[(i, j)] if i < j else E[(j, i)]
    # C4-free: every 4-cycle forbidden (3 cycles per 4-set)
    for a, b, c, dd in itertools.combinations(range(N), 4):
        for (w, x, y, z) in ((a, b, c, dd), (a, b, dd, c), (a, c, b, dd)):
            cnf.add([-e(w, x), -e(x, y), -e(y, z), -e(z, w)])
    # min degree >= d : sequential "at least" counter
    for v in range(N):
        xs = [e(v, u) for u in range(N) if u != v]
        n = len(xs)
        R = [[None] * (d + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, min(i, d) + 1):
                R[i][j] = cnf.var()
        for i in range(1, n + 1):
            for j in range(1, min(i, d) + 1):
                prev_same = R[i - 1][j] if j <= i - 1 else None
                prev_less = R[i - 1][j - 1] if j - 1 >= 1 else 'T'
                # R[i][j] -> prev_same or x_i
                c = [-R[i][j], xs[i - 1]]
                if prev_same is not None:
                    c.append(prev_same)
                cnf.add(c)
                # R[i][j] -> prev_same or prev_less
                if prev_less != 'T':
                    c = [-R[i][j], prev_less]
                    if prev_same is not None:
                        c.append(prev_same)
                    cnf.add(c)
        cnf.add([R[n][d]])
    if symbreak and 1 + d + d * (d - 2) <= N:
        for j in range(1, d + 1):
            cnf.add([e(0, j)])
        nxt = d + 1
        for i in range(1, d + 1):
            for k in range(d - 2):
                cnf.add([e(i, nxt)])
                cnf.add([-e(0, nxt)])
                nxt += 1
    return cnf, e

def verify(N, d, model, e):
    adj = [[u for u in range(N) if u != v and e(v, u) in model] for v in range(N)]
    mind = min(len(a) for a in adj)
    S = [set(a) for a in adj]
    c4 = any(len(S[i] & S[j]) > 1 for i in range(N) for j in range(i + 1, N))
    return mind, c4, adj

if __name__ == '__main__':
    N, d = int(sys.argv[1]), int(sys.argv[2])
    tmo = int(sys.argv[3]) if len(sys.argv) > 3 else 120
    solver = sys.argv[4] if len(sys.argv) > 4 else 'kissat'
    cnf, e = build(N, d)
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, 'cnf', 'direct_N%d_d%d.cnf' % (N, d))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    st, model, dt = cnf.solve(path, timeout=tmo, solver=solver)
    msg = 'direct N=%d d=%d (n=N-d=%d) vars=%d clauses=%d : %s (%.1fs)' % (N, d, N - d, cnf.nv, len(cnf.clauses), st, dt)
    if st == 'SATISFIABLE':
        mind, c4, adj = verify(N, d, model, e)
        msg += ' verified mindeg=%d C4=%s' % (mind, c4)
        assert mind >= d and not c4
        with open(os.path.join(here, 'graph_N%d_d%d.txt' % (N, d)), 'w') as f:
            for v in range(N):
                f.write('%d: %s\n' % (v, ' '.join(map(str, adj[v]))))
    print(msg, flush=True)
    os.remove(path)
