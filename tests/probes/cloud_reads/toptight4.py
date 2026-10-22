"""CL509: the irreducible (top-tight) four-bin H(h) instances after CL508's reduction: least slack attained only by
triples (co-singletons).  For each: (1) delete the top-tight bin A by some realization, child in H(h') lower;
(2) else upper (reflected); (3) else ANY singleton or pair deletion, lower or upper; residual.  Exact condition used
in (1) (CL509): the child is lower-good iff sigma_K >= (a - (M - c)) * r_K for each proper K of A's complement.

OUTCOME (CL509, 3333, kholek DUMPEVERY samples).  h = 1, M = 12: 21,085 instances; reducible 9,379; top-tight 11,706:
A lower 6,255, A upper 1,992, another single 1,162, another pair 2,065, RESIDUAL 232 (2.0%).  h = 2, M = 13: 19,871;
reducible 6,645; top-tight 13,226: A lower 5,244, upper 1,672, other single 3,498, other pair 2,485, RESIDUAL 327
(2.5%).  Residual example [0,12] minus 4, (8,17,20,29): every child of 29 has h' = 2 and the 8 below 9.
"""
import sys
from collections import Counter
from itertools import combinations
_argv_tt = sys.argv; sys.argv = ["x"]
exec(open('tests/probes/cloud_reads/descent_pair.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
sys.argv = _argv_tt

def deletion_ok(S, C, t, P):
    """some realization of the bins P (split if |P| = 2) leaves a child in H(h') lower / upper"""
    m = sum(C[i] for i in P); tot = sum(t[i] for i in P); lo_any = up_any = False
    for R in combinations(S, m):
        if sum(R) != tot: continue
        if len(P) == 2 and not splits(R, C[P[0]], t[P[0]]): continue
        rest = [x for x in S if x not in R]; a, b = rest[0], rest[-1]; hh = (b - a + 1) - len(rest)
        oth = [i for i in range(len(C)) if i not in P]; sz = [C[i] for i in oth]; tt = [t[i] for i in oth]
        if len(oth) == 1: return True, True
        lo_any |= key([u - a * c for u, c in zip(tt, sz)], sz) >= hh
        up_any |= key([c * b - u for u, c in zip(tt, sz)], sz) >= hh
        if lo_any and up_any: break
    return lo_any, up_any

def run(M, h, files, C=(3, 3, 3, 3)):
    cnt = Counter(); resid = []
    for f in files:
        for line in open(f):
            if not line.startswith('V'): continue
            hs, ts = line[len('V holes'):].split('|')
            H = list(map(int, hs.split())); t = list(map(int, ts.split()))
            S = [x for x in range(M + 1) if x not in H]; k = len(C)
            sig = {J: sum(t[i] for i in J) - sum(C[i] for i in J) * (sum(C[i] for i in J) - 1) // 2 - h * sum(C[i] for i in J)
                   for s in range(1, k) for J in combinations(range(k), s)}
            mn = min(sig.values()); arg = [J for J in sig if sig[J] == mn]
            cnt['n'] += 1
            if any(len(J) <= k - 2 for J in arg): cnt['reducible'] += 1; continue
            cnt['toptight'] += 1
            A = [i for i in range(k) if i not in arg[0]][0]
            lo, up = deletion_ok(S, C, t, (A,))
            if lo: cnt['A_lower'] += 1; continue
            if up: cnt['A_upper'] += 1; continue
            ok = False
            for P in [(i,) for i in range(k) if i != A] + list(combinations(range(k), 2)):
                l2, u2 = deletion_ok(S, C, t, P)
                if l2 or u2: ok = True; cnt['other_' + ('single' if len(P) == 1 else 'pair') + ('_lower' if l2 else '_upper')] += 1; break
            if not ok:
                cnt['residual'] += 1; resid.append((H, t, A, mn))
    return cnt, resid

if __name__ == '__main__':
    M, h = int(sys.argv[1]), int(sys.argv[2])
    cnt, resid = run(M, h, sys.argv[3:])
    print(M, h, dict(sorted(cnt.items())))
    print('residual examples:', resid[:8], flush=True)
