#!/usr/bin/env python3
"""Erdos #132 lattice search.
Find an n-point subset S of a finite ground set G (lattice patch) such that at most K distance classes
have multiplicity in [1, n] (all other occurring classes have multiplicity >= n+1).
K = 1 is a counterexample to the Erdos-Pach question (two distances with multiplicity in [1, n]).
Usage: sat132.py LATTICE PARAM n K [timelimit_s]
  LATTICE = tri (hex patch radius PARAM) | sq (PARAM x PARAM grid) | tridisc (disc of squared radius PARAM)
Prints SAT + the subset and its exact multiplicity profile, or UNSAT, or UNKNOWN (timeout)."""
import sys, subprocess, os, itertools, time, tempfile
from collections import defaultdict

def ground(lat, P):
    if lat == 'tri':
        R = P
        pts = [(a, b) for a in range(-R, R+1) for b in range(-R, R+1) if abs(a+b) <= R]
        nrm = lambda u, v: u*u + u*v + v*v
    elif lat == 'tridisc':
        R2 = P; r = int(R2**0.5) + 2
        pts = [(a, b) for a in range(-r, r+1) for b in range(-r, r+1) if a*a + a*b + b*b <= R2]
        nrm = lambda u, v: u*u + u*v + v*v
    elif lat == 'sq':
        k = P
        pts = [(a, b) for a in range(k) for b in range(k)]
        nrm = lambda u, v: u*u + v*v
    elif lat == 'z12':
        # points a + b z + c z^2 + d z^3, z = exp(i pi/6), coefficients in [-P, P]; exact 4|w|^2 = A + B sqrt3
        r = range(-P, P + 1)
        pts = [(a, b, c, d) for a in r for b in r for c in r for d in r]
        C4 = {0: (4, 0), 1: (0, 2), 2: (2, 0), 3: (0, 0)}  # 4cos(k pi/6) for |k| = 0..3 as (int, coeff of sqrt3)
        def d2(p, q):
            w = [p[i] - q[i] for i in range(4)]
            A = B = 0
            for j in range(4):
                for k in range(4):
                    a, b = C4[abs(j - k)]
                    A += w[j] * w[k] * a; B += w[j] * w[k] * b
            return (A, B)
        return pts, d2
    else:
        raise SystemExit('bad lattice')
    return pts, (lambda p, q: nrm(p[0] - q[0], p[1] - q[1]))

class CNF:
    def __init__(s): s.nv = 0; s.cl = []
    def var(s): s.nv += 1; return s.nv
    def add(s, c): s.cl.append(c)

def atleast_seq(F, lits, K):
    """returns literal o such that o -> (sum lits >= K)."""
    m = len(lits)
    if K <= 0:
        t = F.var(); F.add([t]); return t
    if K > m:
        f = F.var(); F.add([-f]); return f
    prev = {}  # prev[j] for j=1..K : var 's_{i-1,j}', None means false
    for i, y in enumerate(lits, start=1):
        cur = {}
        for j in range(1, min(i, K) + 1):
            s = F.var(); cur[j] = s
            a = prev.get(j)          # s_{i-1,j}
            b = prev.get(j-1) if j >= 2 else 'T'  # s_{i-1,j-1}
            # s -> a or y
            F.add([-s] + ([a] if a else []) + [y])
            # s -> a or b
            if b != 'T':
                F.add([-s] + ([a] if a else []) + ([b] if b else []))
        prev = cur
    return prev[K]

def atmost_seq(F, lits, K):
    """hard constraint sum lits <= K (Sinz)."""
    m = len(lits)
    if K >= m: return
    if K == 0:
        for x in lits: F.add([-x])
        return
    s = [[F.var() for j in range(K)] for i in range(m)]
    F.add([-lits[0], s[0][0]])
    for j in range(1, K): F.add([-s[0][j]])
    for i in range(1, m):
        F.add([-lits[i], s[i][0]])
        F.add([-s[i-1][0], s[i][0]])
        for j in range(1, K):
            F.add([-lits[i], -s[i-1][j-1], s[i][j]])
            F.add([-s[i-1][j], s[i][j]])
        F.add([-lits[i], -s[i-1][K-1]])

def build(lat, P, n, K, T=None):
    if T is None: T = n + 1
    pts, nrm = ground(lat, P)
    M = len(pts)
    cls = defaultdict(list)
    for i, j in itertools.combinations(range(M), 2):
        d = nrm(pts[i], pts[j])
        cls[d].append((i, j))
    F = CNF()
    x = [F.var() for _ in range(M)]
    # exactly n points
    atmost_seq(F, x, n)
    o = atleast_seq(F, x, n); F.add([o])
    evars = []
    for d, prs in sorted(cls.items()):
        u = F.var(); e = F.var(); evars.append(e)
        ys = []
        for (i, j) in prs:
            F.add([-x[i], -x[j], u])
            y = F.var(); F.add([-y, x[i]]); F.add([-y, x[j]]); ys.append(y)
        if len(prs) < T:
            F.add([-u, e])   # class can never reach T: if used it is exceptional
        else:
            oc = atleast_seq(F, ys, T)
            F.add([-u, e, oc])
    atmost_seq(F, evars, K)
    # symmetry/translation breaking (light): none (keeps the search exhaustive and simple)
    return pts, nrm, cls, F, x

def profile(S, nrm):
    mult = defaultdict(int)
    for p, q in itertools.combinations(S, 2):
        mult[nrm(p, q)] += 1
    return dict(sorted(mult.items()))

def main():
    lat, P, n, K = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    tl = int(sys.argv[5]) if len(sys.argv) > 5 else 120
    T = int(sys.argv[6]) if len(sys.argv) > 6 else n + 1
    t0 = time.time()
    pts, nrm, cls, F, x = build(lat, P, n, K, T)
    fd, path = tempfile.mkstemp(suffix='.cnf', dir=os.path.dirname(os.path.abspath(__file__)) + '/runs')
    with os.fdopen(fd, 'w') as f:
        f.write('p cnf %d %d\n' % (F.nv, len(F.cl)))
        for c in F.cl: f.write(' '.join(map(str, c)) + ' 0\n')
    try:
        r = subprocess.run(['nice', '-n', '10', 'kissat', '-q', '--time=%d' % tl, path], capture_output=True, text=True,
                           timeout=tl + 30)
        out = r.stdout
    except subprocess.TimeoutExpired:
        out = 's UNKNOWN'
    finally:
        os.unlink(path)
    st = 'UNKNOWN'
    for line in out.splitlines():
        if line.startswith('s '):
            st = line[2:].strip()
    res = {'lat': lat, 'P': P, 'M': len(pts), 'n': n, 'K': K, 'T': T, 'classes': len(cls), 'vars': F.nv, 'clauses': len(F.cl),
           'status': st, 'secs': round(time.time() - t0, 1)}
    if st == 'SATISFIABLE':
        val = set()
        for line in out.splitlines():
            if line.startswith('v '):
                for t in line[2:].split():
                    v = int(t)
                    if v > 0: val.add(v)
        S = [pts[i] for i in range(len(pts)) if x[i] in val]
        pr = profile(S, nrm)
        rare = [d for d, m in pr.items() if 1 <= m <= n]
        low = [d for d, m in pr.items() if m < T]
        ms = sorted(pr.values())
        res.update({'S': S, 'profile': pr, 'rare': rare, 'nrare': len(rare), 'm2': ms[1] if len(ms) > 1 else None,
                    'check': (len(S) == n and len(low) <= K)})
    print(res, flush=True)

if __name__ == '__main__':
    main()
