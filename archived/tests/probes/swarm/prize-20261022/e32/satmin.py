"""Exact minimum window cover by SAT (kissat), as a control on the greedy.

min |A|, A subset [1, 2M), such that every n in [M, 2M) has n - a in Q (Q = primes or a Cramer sample).
Cardinality <= k by a sequential counter. Starts from the greedy value and walks down until UNSAT or timeout.
Usage: python3 satmin.py KIND SEED M PERCALL_SECONDS
"""
import sys, subprocess, time, os, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from greedy import model_set, greedy_cover

def cnf(M, Qind, k):
    nv = 2 * M - 1  # x_a for a = 1..2M-1  -> var a
    clauses = []
    qs = np.nonzero(Qind[:2 * M])[0]; qs = qs[qs >= 2]
    for n in range(M, 2 * M):
        a = n - qs; a = a[(a >= 1)]
        clauses.append([int(v) for v in a])
    # sequential counter (Sinz) for sum_{i=1..N} x_i <= k
    N = nv
    s = {}
    def S(i, j):
        nonlocal nv
        if (i, j) not in s:
            nv += 1; s[(i, j)] = nv
        return s[(i, j)]
    clauses.append([-1, S(1, 1)])
    for j in range(2, k + 1):
        clauses.append([-S(1, j)])
    for i in range(2, N):
        clauses.append([-i, S(i, 1)])
        clauses.append([-S(i - 1, 1), S(i, 1)])
        for j in range(2, k + 1):
            clauses.append([-i, -S(i - 1, j - 1), S(i, j)])
            clauses.append([-S(i - 1, j), S(i, j)])
        clauses.append([-i, -S(i - 1, k)])
    clauses.append([-N, -S(N - 1, k)])
    return nv, clauses

def solve(M, Qind, k, tl, path):
    nv, cl = cnf(M, Qind, k)
    with open(path, 'w') as f:
        f.write(f"p cnf {nv} {len(cl)}\n")
        for c in cl:
            f.write(' '.join(map(str, c)) + ' 0\n')
    r = subprocess.run(['nice', '-n', '10', 'kissat', '-q', f'--time={tl}', path], capture_output=True, text=True)
    out = r.stdout
    if 's SATISFIABLE' in out:
        vals = []
        for line in out.splitlines():
            if line.startswith('v '):
                vals += [int(v) for v in line[2:].split()]
        A = [v for v in vals if 0 < v < 2 * M]
        return 'SAT', A
    if 's UNSATISFIABLE' in out:
        return 'UNSAT', None
    return 'UNKNOWN', None

def main():
    kind, seed, M, tl = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    rng = np.random.default_rng(seed)
    L = 1
    while L < 4 * M: L *= 2
    Qind = model_set(L, kind, rng)
    A, _ = greedy_cover(M, Qind)
    g = len(A)
    best = g
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"sat_{kind}_{seed}_{M}.cnf")
    status = 'greedy'
    t0 = time.time()
    k = g - 1
    while k >= 1:
        if time.time() - t0 > 500: status = 'walltime'; break
        res, Ak = solve(M, Qind, k, tl, path)
        if res == 'SAT':
            # verify
            qs = np.nonzero(Qind[:2 * M])[0]; qs = qs[qs >= 2]
            cov = np.zeros(2 * M, dtype=bool)
            for a in Ak:
                idx = a + qs; idx = idx[idx < 2 * M]; cov[idx] = True
            assert cov[M:2 * M].all() and len(Ak) <= k
            best = len(Ak); k = best - 1; status = 'SAT'
        elif res == 'UNSAT':
            status = 'OPTIMAL'; break
        else:
            status = 'UNKNOWN_at_k=%d' % k; break
    os.remove(path) if os.path.exists(path) else None
    lm = math.log(M)
    print(f"{kind} seed={seed} M={M} greedy={g} best={best} status={status} best/lnM={best/lm:.3f} "
          f"best/lnM^2={best/lm**2:.3f} t={time.time()-t0:.0f}s", flush=True)

if __name__ == '__main__':
    main()
