# Seeded search: take a C4-free graph G (file), delete vertex set D, keep all remaining edges, and ask SAT for
# extra edges so the result is C4-free with min degree >= d.  Usage: python3 seeded.py graphfile d trials size seed timeout
import sys, os, random, itertools, time
from satlib import CNF
import numpy as np

def load(fn):
    rows = [l.split(':') for l in open(fn) if l.strip()]
    N = len(rows)
    adj = [set() for _ in range(N)]
    for r in rows:
        for u in r[1].split():
            adj[int(r[0])].add(int(u))
    return adj

def attempt(adj, D, d, tmo, tag):
    keep = [v for v in range(len(adj)) if v not in D]
    idx = {v: i for i, v in enumerate(keep)}
    N = len(keep)
    E = [[False] * N for _ in range(N)]
    for v in keep:
        for u in adj[v]:
            if u in idx:
                E[idx[v]][idx[u]] = True
    cnf = CNF()
    X = {}
    for i in range(N):
        for j in range(i + 1, N):
            if not E[i][j]:
                X[(i, j)] = cnf.var()
    def lit(i, j):
        if i > j:
            i, j = j, i
        return None if E[i][j] else X[(i, j)]
    for a, b, c, e in itertools.combinations(range(N), 4):
        for (w, x, y, z) in ((a, b, c, e), (a, b, e, c), (a, c, b, e)):
            ls = [lit(w, x), lit(x, y), lit(y, z), lit(z, w)]
            vs = [l for l in ls if l is not None]
            assert vs, 'seed has a C4'
            cnf.add([-v for v in set(vs)])
    for i in range(N):
        have = sum(E[i])
        need = d - have
        if need > 0:
            cnf.atleast([lit(i, j) for j in range(N) if j != i and lit(i, j) is not None], need)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cnf', 'seed_%s.cnf' % tag)
    st, model, dt = cnf.solve(path, timeout=tmo)
    os.remove(path)
    if st == 'SATISFIABLE':
        A = np.array([[1 if (i != j and (E[i][j] or (lit(i, j) in model))) else 0 for j in range(N)] for i in range(N)])
        B = A @ A
        np.fill_diagonal(B, 0)
        assert (A == A.T).all() and B.max() <= 1 and A.sum(1).min() >= d
        fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'graph_seeded_N%d_d%d_%s.txt' % (N, d, tag))
        with open(fn, 'w') as f:
            for i in range(N):
                f.write('%d: %s\n' % (i, ' '.join(str(j) for j in range(N) if A[i, j])))
        return st, dt, fn
    return st, dt, None

if __name__ == '__main__':
    fn, d, trials, size, seed, tmo = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    adj = load(fn)
    rnd = random.Random(seed)
    T0 = time.time()
    for t in range(trials):
        if time.time() - T0 > 400:
            break
        mode = t % 3
        if mode == 0:   # random set
            D = set(rnd.sample(range(len(adj)), size))
        elif mode == 1:  # a vertex and some neighbours
            v = rnd.randrange(len(adj)); D = {v} | set(rnd.sample(sorted(adj[v]), min(size - 1, len(adj[v]))))
            while len(D) < size: D.add(rnd.randrange(len(adj)))
        else:            # a vertex and vertices at distance 2 (a path-like spread)
            v = rnd.randrange(len(adj)); far = [u for u in range(len(adj)) if u != v and u not in adj[v]]
            D = {v} | set(rnd.sample(far, size - 1))
        st, dt, out = attempt(adj, D, d, tmo, '%s_%d_%d' % (os.path.basename(fn)[:-4], seed, t))
        print('seed-trial %d mode %d D=%s : %s (%.1fs) %s' % (t, mode, sorted(D), st, dt, out or ''), flush=True)
        if out:
            break
