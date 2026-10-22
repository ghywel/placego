#!/usr/bin/env python3
"""Find all 13-point subsets of the triangular-lattice hex patch (radius 3) with at most 6 distinct distances (SAT +
blocking of all 12 symmetric images and translates), print their multiplicity profiles. Time limit built in."""
import itertools, subprocess, os, tempfile, time
from collections import defaultdict
t0 = time.time()
R = 3
pts = [(a, b) for a in range(-R, R+1) for b in range(-R, R+1) if abs(a+b) <= R]
idx = {p: i for i, p in enumerate(pts)}
nrm = lambda u, v: u*u + u*v + v*v
cls = defaultdict(list)
for i, j in itertools.combinations(range(len(pts)), 2):
    cls[nrm(pts[i][0]-pts[j][0], pts[i][1]-pts[j][1])].append((i, j))
def rot(p):  # 60 degree rotation in axial coords (basis 1, e^{i pi/3}): (a,b) -> (-b, a+b)
    return (-p[1], p[0] + p[1])
def refl(p):  # reflection swapping basis vectors
    return (p[1], p[0])
def images(S):
    out = set()
    T = list(S)
    for r in range(6):
        for f in (False, True):
            U = [refl(p) if f else p for p in T]
            for _ in range(r): U = [rot(p) for p in U]
            # translates inside the patch
            for da in range(-2*R, 2*R+1):
                for db in range(-2*R, 2*R+1):
                    V = [(p[0]+da, p[1]+db) for p in U]
                    if all(v in idx for v in V): out.add(frozenset(V))
    return out
def canon(S):
    best = None
    T = list(S)
    for r in range(6):
        for f in (False, True):
            U = [refl(p) if f else p for p in T]
            for _ in range(r): U = [rot(p) for p in U]
            m0 = min(U); V = tuple(sorted((p[0]-m0[0], p[1]-m0[1]) for p in U))
            if best is None or V < best: best = V
    return best
class CNF:
    def __init__(s): s.nv = 0; s.cl = []
    def var(s): s.nv += 1; return s.nv
import importlib.util
spec = importlib.util.spec_from_file_location('s', 'sat132.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
F = m.CNF()
x = [F.var() for _ in pts]
m.atmost_seq(F, x, 13); o = m.atleast_seq(F, x, 13); F.add([o])
us = []
for d, prs in cls.items():
    u = F.var(); us.append(u)
    for i, j in prs: F.add([-x[i], -x[j], u])
m.atmost_seq(F, us, 6)
shapes = {}
blocks = []
while time.time() - t0 < 300:
    fd, path = tempfile.mkstemp(suffix='.cnf', dir='runs')
    with os.fdopen(fd, 'w') as f:
        f.write('p cnf %d %d\n' % (F.nv, len(F.cl) + len(blocks)))
        for c in F.cl + blocks: f.write(' '.join(map(str, c)) + ' 0\n')
    out = subprocess.run(['nice', '-n', '10', 'kissat', '-q', '--time=120', path], capture_output=True, text=True).stdout
    os.unlink(path)
    if 's SATISFIABLE' not in out:
        print('# search ended:', [l for l in out.splitlines() if l.startswith('s ')]); break
    val = set(int(t) for l in out.splitlines() if l.startswith('v ') for t in l[2:].split() if int(t) > 0)
    S = [pts[i] for i in range(len(pts)) if x[i] in val]
    c = canon(S)
    prof = defaultdict(int)
    for p, q in itertools.combinations(S, 2): prof[nrm(p[0]-q[0], p[1]-q[1])] += 1
    shapes[c] = dict(sorted(prof.items()))
    print('shape', len(shapes), c, 'profile', shapes[c], flush=True)
    for I in images(S):
        blocks.append([-x[idx[p]] for p in I])
print('# distinct shapes:', len(shapes), 'secs', round(time.time()-t0, 1))
