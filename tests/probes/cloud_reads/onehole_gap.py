"""Companion of onehole_feasible.py (CL478): spectrum-feasible vs feasible, least margins, reading F_*.pkl from the
scratch feas/ folder (data outside git; regenerate with onehole_feasible.py)."""
import itertools, pickle, sys, glob
from collections import Counter
L = lambda n: n*(n-1)//2; T = lambda n: n*(n+1)//2
SUB = [J for s in (1,2,3) for J in itertools.combinations(range(4), s)]
FE = '/tmp/claude-0/-home-user-placego/65b2700f-7c0c-5a5c-bf6d-c51aa7c63cf1/scratchpad/feas/'
def spectra(pool, M):
    """achievable k-subset sums of pool, k = 0..len(pool), by DP"""
    sp = [set() for _ in range(len(pool)+1)]; sp[0].add(0)
    for x in pool:
        for k in range(len(pool)-1, -1, -1):
            if sp[k]: sp[k+1] |= {s + x for s in sp[k]}
    return sp
for f in sorted(glob.glob(FE + 'F_*.pkl')):
    M = int(f.split('_')[1]); C = tuple(int(ch) for ch in f.split('_')[2].split('.')[0])
    if M > int(sys.argv[1]): continue
    res = pickle.load(open(f, 'rb'))
    CJ = {J: sum(C[i] for i in J) for J in SUB}
    prof = Counter(); ex = {}
    nspec = ninf = 0
    for q in range(1, M):
        pool = sorted(x for x in range(M+1) if x != q); S = sum(pool); sp = spectra(pool, M)
        mins = lambda c: sum(pool[:c]); maxs = lambda c: sum(pool[len(pool)-c:])
        F = res[q]
        for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i])+1) for i in range(3)]):
            t = t3 + (S - sum(t3),)
            tJ = {J: sum(t[i] for i in J) for J in SUB}
            if not all(tJ[J] in sp[CJ[J]] for J in SUB): continue
            nspec += 1
            if t3 in F: continue
            ninf += 1
            m = min(min(tJ[J] - mins(CJ[J]), maxs(CJ[J]) - tJ[J]) for J in SUB)
            prof[m] += 1
            if m >= 1 and len(ex.setdefault(m, [])) < 3: ex[m].append((q, t))
    print(M, C, 'spectrum-feasible', nspec, 'infeasible', ninf, 'by least margin:', sorted(prof.items()), {k: v for k, v in ex.items()})
