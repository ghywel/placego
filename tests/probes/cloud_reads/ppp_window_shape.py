"""CL496: shape of the set of completing x for the PPP boundary in pair-least I2 instances.

For each instance list the candidate x (increasing; y = need - x > x, both outside the prefix) and mark which
complete.  Record whether the completing ones form one contiguous run of candidates, and whether that run contains
the most balanced candidate (largest x).  Prediction (written first): one contiguous run in >= 99% of instances,
containing the balanced end in >= 99%.  Counterfactual: scattered completing x would mean no window lemma exists.

OUTCOME: M = 12: one run 8,226, two runs 48 (equal pair targets 12/12, middle x fails); balanced end 8,256.
M = 13: one run 59,328, two runs 360; balanced end 59,544.  Prediction held (>= 99%).
"""
import itertools, sys
from collections import Counter
_a = sys.argv; sys.argv = ['x']
exec(open('tests/probes/cloud_reads/ppp_rules.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
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
                sing = min(min(t[i] - mins(C[i]), maxs(C[i]) - t[i]) for i in range(4))
                if not sl[0][0] < sing: continue
                _, side, (X, Y) = sl[0]
                Z, tt = (S, t) if side == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                cands = ppp_candidates(Z, C[X] + C[Y], tt[X] + tt[Y])
                marks = [completes(Z, c[2], C, tt, X, Y) or completes(Z, c[2], C, tt, Y, X) for c in cands]
                cnt['n'] += 1
                runs = sum(1 for i, m in enumerate(marks) if m and (i == 0 or not marks[i - 1]))
                cnt[('runs', runs)] += 1
                cnt['balanced_in'] += bool(marks) and marks[-1]
                if runs > 1 and len(ex) < 4: ex.append((q, C, t, [c[0] for c in cands], marks))
    return cnt, ex

if __name__ == '__main__':
    for M in map(int, sys.argv[1:]):
        cnt, ex = run(M)
        print(M, 'pair-least', cnt['n'], 'number of completing runs:', sorted((k[1], v) for k, v in cnt.items() if isinstance(k, tuple)), 'balanced candidate completes', cnt['balanced_in'], ex, flush=True)
