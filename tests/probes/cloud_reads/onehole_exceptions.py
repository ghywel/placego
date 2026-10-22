"""List every spectrum-feasible infeasible instance, sizes >= 3, M <= 16, up to bin relabelling and reflection."""
import itertools, pickle, glob, os, tempfile
# scratch data folder: $SCRATCH, else the system temp folder (was a session path; made portable 2026-10-22)
SCRATCH = os.environ.get('SCRATCH', tempfile.gettempdir())
L = lambda n: n*(n-1)//2; T = lambda n: n*(n+1)//2
SUB = [J for s in (1,2,3) for J in itertools.combinations(range(4), s)]
FE = os.path.join(SCRATCH, 'feas', '')
def spectra(pool):
    sp = [set() for _ in range(len(pool)+1)]; sp[0].add(0)
    for x in pool:
        for k in range(len(pool)-1, -1, -1):
            if sp[k]: sp[k+1] |= {s + x for s in sp[k]}
    return sp
seen = set()
for f in sorted(glob.glob(FE + 'F_*.pkl')):
    M = int(f.split('_')[1]); C = tuple(int(ch) for ch in f.split('_')[2].split('.')[0])
    res = pickle.load(open(f, 'rb')); CJ = {J: sum(C[i] for i in J) for J in SUB}
    for q in range(1, M):
        pool = sorted(x for x in range(M+1) if x != q); S = sum(pool); sp = spectra(pool)
        mins = lambda c: sum(pool[:c]); maxs = lambda c: sum(pool[len(pool)-c:])
        for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i])+1) for i in range(3)]):
            t = t3 + (S - sum(t3),)
            if not all(sum(t[i] for i in J) in sp[CJ[J]] for J in SUB): continue
            if t3 in res[q]: continue
            # canonical form: sort bins by (size, target); reflect if q > M/2
            def canon(q, C, t):
                return (q,) + tuple(sorted(zip(C, t)))
            k1 = canon(q, C, t); k2 = canon(M - q, C, tuple(C[i]*M - t[i] for i in range(4)))
            key = min(k1, k2)
            if (M, key) in seen: continue
            seen.add((M, key))
            tight = [(''.join('ABCD'[i] for i in J), sum(t[i] for i in J) - mins(CJ[J]), maxs(CJ[J]) - sum(t[i] for i in J)) for J in SUB]
            tight = [x for x in tight if min(x[1], x[2]) <= 1]
            print(M, 'q', q, 'sizes', C, 'targets', t, ' groups within 1 of an end:', tight)
