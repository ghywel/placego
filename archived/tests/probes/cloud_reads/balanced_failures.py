"""CL496: characterise the balanced-rule failures (CL493).  Claim tested: every failure has a complement W with
exactly 6 values, W (normalised) is one of CL492's seven deep-gap pools, the two remaining targets are equal, and
the next candidate (x - 1 step) completes.  Prediction (written first): all four hold for every failure at M = 12, 13.

OUTCOME: M = 12: 18 failures, all six-value complements, all deep pools, all equal remaining targets, next
candidate completes in all 18.  M = 13: the same for all 144.  M = 14: the same for all 396.  Prediction held exactly.
"""
import itertools, sys
from collections import Counter
_a = sys.argv; sys.argv = ['x']
exec(open('tests/probes/cloud_reads/ppp_rules.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
sys.argv = _a
DEEP = {(0,2,3,5,6,8), (0,2,3,4,7,8), (0,1,4,5,6,8), (0,1,5,6,7,8), (0,1,2,3,7,8), (0,1,3,5,7,8), (0,1,2,6,7,8)}

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
                if not cands: continue
                x, y, P = cands[-1]
                if completes(Z, P, C, tt, X, Y) or completes(Z, P, C, tt, Y, X): continue
                cnt['fail'] += 1
                W = [v for v in Z if v not in P]; Wn = tuple(v - W[0] for v in W)
                oth = [z for z in range(4) if z not in (X, Y)]
                cnt['six'] += len(W) == 6
                cnt['deep'] += Wn in DEEP
                cnt['equal'] += tt[oth[0]] == tt[oth[1]]
                nxt = cands[-2] if len(cands) >= 2 else None
                cnt['next_ok'] += bool(nxt) and (completes(Z, nxt[2], C, tt, X, Y) or completes(Z, nxt[2], C, tt, Y, X))
                if not (len(W) == 6 and Wn in DEEP and tt[oth[0]] == tt[oth[1]]) and len(ex) < 4: ex.append((q, C, t, Wn, [tt[z] for z in oth]))
    return cnt, ex

if __name__ == '__main__':
    for M in map(int, sys.argv[1:]):
        cnt, ex = run(M)
        print(M, dict(cnt), 'not matching the claim:', ex, flush=True)
