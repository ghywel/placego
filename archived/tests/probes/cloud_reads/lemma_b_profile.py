"""CL494: lemma (b) profile.  In singleton-least instances where the least pair's boundary fails, take the least
singleton's repaired recipes.  For each recipe's three-bin remainder (a pool with <= 2 holes plus at most 2 repair
displacements), compare scalar spectrum feasibility of the three remaining targets (all six groups) with actual
three-bin feasibility.  Prediction (written first): every recipe whose remainder is spectrum-feasible completes
except remainders matching the A2 exception shapes (cores beside a pinned bin); and some recipe is always
spectrum-feasible.  Counterfactual: a non-A2 spectrum-feasible failure is a new obstruction.
OUTCOME.  M = 12: 4,743 fallback instances, 5,128 recipes, every one spectrum-feasible AND feasible.  M = 13
(84 s): 38,544 fallback instances, 42,008 recipes, all spectrum-feasible and feasible.  No A2 exception is ever
reached from a least-singleton recipe in the fallback case.  Prediction held, more strongly than stated.
M = 14 (about 6 min): 174,985 fallback instances, 188,510 recipes, all spectrum-feasible and feasible.
"""
import sys, itertools
from collections import Counter
_a = sys.argv; sys.argv = ['x']
exec(open('tests/probes/cloud_reads/singleton_or_pair.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
sys.argv = _a

def run(M):
    cnt = Counter(); ex = []
    for C in itertools.product(range(3, M - 8), repeat=4):
        if sum(C) != M: continue
        CJ = {J: sum(C[i] for i in J) for J in SUB}
        for q in range(1, M):
            S = [x for x in range(M + 1) if x != q]; tot = sum(S); N = len(S)
            sp = spectra(S); mins = lambda c: sum(S[:c]); maxs = lambda c: sum(S[N - c:]); Rf = [M - x for x in reversed(S)]
            for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i]) + 1) for i in range(3)]):
                t = t3 + (tot - sum(t3),)
                tJ = {J: sum(t[i] for i in J) for J in SUB}
                if not all(tJ[J] in sp[CJ[J]] and tJ[J] - mins(CJ[J]) >= 2 and maxs(CJ[J]) - tJ[J] >= 2 for J in SUB): continue
                sl = sorted([(tJ[p] - mins(CJ[p]), 'lo', p) for p in PAIRS] + [(maxs(CJ[p]) - tJ[p], 'up', p) for p in PAIRS])
                ss = sorted([(t[i] - mins(C[i]), 'lo', i) for i in range(4)] + [(maxs(C[i]) - t[i], 'up', i) for i in range(4)])
                if not ss[0][0] <= sl[0][0]: continue
                _, side, (X, Y) = sl[0]
                Z, tt = (S, t) if side == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                if pair_boundary_ok(Z, C, tt, X, Y, M, N, None): continue
                cnt['fallback'] += 1
                _, side1, A = ss[0]
                Z1, t1 = (S, t) if side1 == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                oth = [i for i in range(4) if i != A]; any_spec = any_ok = False
                for Aset in recipes(Z1, C[A], t1[A], None):
                    rem = [x for x in Z1 if x not in Aset]; spR = spectra(rem)
                    sizes = [C[i] for i in oth]; tg = [t1[i] for i in oth]
                    specok = all(sum(tg[j] for j in J) in spR[sum(sizes[j] for j in J)] for r in (1, 2) for J in itertools.combinations(range(3), r))
                    real = (tg[0], tg[1]) in three_bin(tuple(rem), tuple(sizes))
                    cnt[('spec', specok, 'real', real)] += 1
                    any_spec |= specok; any_ok |= real
                    if specok and not real and len(ex) < 6: ex.append((q, C, t, 'remainder', tuple(rem), list(zip(sizes, tg))))
                cnt['some_spec'] += any_spec; cnt['some_ok'] += any_ok
    return cnt, ex

if __name__ == '__main__':
    for M in map(int, sys.argv[1:]):
        cnt, ex = run(M)
        print(M, dict(cnt)); print('  spectrum-feasible but infeasible remainders:', ex, flush=True)
