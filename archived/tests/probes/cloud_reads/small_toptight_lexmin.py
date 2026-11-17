"""CL536: the SMALL-bin top-tight case with a big bin, (3, 3, 3, X), X >= 4 (CL535): realize the top-tight small bin A
by the LEXICOGRAPHICALLY SMALLEST triple of sum u_A; is the three-bin child feasible?  (CL527 found lexmin the best
blind rule for 3333, with misses there.)  Exact feasibility by backtracking.  Run: python3 small_toptight_lexmin.py [M,h,X ...].

OUTCOME (CL536): lexmin leaves a feasible child in EVERY instance: (X,h) = (4,1) 12,173; (4,2) 46,998; (6,1) 29,799;
(6,2) 133,684; (8,1) 58,370; (8,2) 295,134; (10,1) 101,650.  Total 677,808, no miss (cf. 3333, CL527: misses exist).
"""
import sys
from itertools import combinations
from collections import Counter
_argv_sl = sys.argv; sys.argv = ['x']
exec(open('tests/probes/cloud_reads/small_toptight_census.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
sys.argv = _argv_sl

def run2(M, h, X):
    C = (3, 3, 3, X); cnt = Counter(); ex = []
    groups = [J for s in (1, 2, 3) for J in combinations(range(4), s)]
    for H in combinations(range(M + 1), h):
        S = [x for x in range(M + 1) if x not in H]; tot = sum(S)
        trip = {}
        for T in combinations(S, 3): trip.setdefault(sum(T), []).append(T)
        for u1 in range(3 + 3 * h, 3 * M):
            for u2 in range(u1, 3 * M):
                for u3 in range(u2, 3 * M):
                    t = (u1, u2, u3, tot - u1 - u2 - u3); sig = {}; bad = False
                    for J in groups:
                        r = sum(C[i] for i in J); u = sum(t[i] for i in J); s_ = u - L(r) - h * r
                        if s_ < 0: bad = True; break
                        sig[J] = s_
                    if bad: continue
                    mn = min(sig.values()); arg = [J for J in sig if sig[J] == mn]
                    if any(len(J) <= 2 for J in arg): continue
                    tops = {[i for i in range(4) if i not in J][0] for J in arg}
                    if tops == {3}: continue
                    A = min(i for i in tops if i < 3); cnt['n'] += 1
                    oth = [i for i in range(4) if i != A]
                    R = min(trip[t[A]])
                    rest = [x for x in S if x not in R]
                    ok = feasible(rest, [C[i] for i in oth], [t[i] for i in oth])
                    cnt['lexmin'] += ok
                    if not ok and len(ex) < 4: ex.append((H, t, A))
    return cnt, ex

if __name__ == '__main__':
    doms = [tuple(map(int, a.split(','))) for a in sys.argv[1:]] or [(13, 1, 4), (14, 2, 4), (15, 1, 6), (16, 2, 6), (17, 1, 8)]
    for M, h, X in doms:
        cnt, ex = run2(M, h, X); print('X', X, 'h', h, 'M', M, dict(cnt), ex, flush=True)
