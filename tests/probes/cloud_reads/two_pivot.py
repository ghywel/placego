"""CL489: the two-pivot pair boundary on one-hole pools.

Pair (X, Y), sizes a, b, m = a + b, in the frame where the pair's slack is a LOWER slack.  Pi = the m - 2 smallest
pool values.  A two-pivot choice is x != y outside Pi with x + y = t_X + t_Y - sum(Pi) and t_X - x in
Sigma_(a-1)(Pi); then X = Pi_X u {x}, Y = (Pi minus Pi_X) u {y} realise t_X, t_Y exactly.  It completes when some
other bin's target is in its spectrum on the complement S minus (Pi u {x, y}) (an interval minus <= 3 values).
Measured on pair-least I2 instances: window (some legal x exists), completion (some legal x completes), and the
complement-target margin for the completing x (distance of t_Z from the complement's extremes; G340 needs >= 5).
Prediction (written first): window 100%, completion >= 99%; completing cases mostly have complement margin >= 5.
Counterfactual: completion well below 99% means the plain two-pivot form is not the mechanism.
OUTCOME (33 s).  M = 12: 8,274 pair-least; window 8,274; completes 8,274; best complement margin 3: 900, 4: 1,668,
>= 5: 5,706.  M = 13: 59,688; window 59,388; completes 59,388 (99.5%); margin 3: 4,728, 4: 8,976, >= 5: 45,684.
Every miss has an EMPTY window (e.g. q3, 3334, (6,28,33,21), pair (A,D)); those are covered by the rank staircase
(CL484).  Prediction: window 100% FAILED at M = 13; completion >= 99% held; margin >= 5 in 69% / 77% only, so
G340 alone does not carry the complement side; depths 3-4 need the actual spectrum.
"""
import itertools, sys
from collections import Counter
T = lambda n: n * (n + 1) // 2
SUB = [J for s in (1, 2, 3) for J in itertools.combinations(range(4), s)]
PAIRS = list(itertools.combinations(range(4), 2))

def spectra(pool):
    sp = [set() for _ in range(len(pool) + 1)]; sp[0].add(0)
    for x in pool:
        for k in range(len(pool) - 1, -1, -1):
            if sp[k]: sp[k + 1] |= {s + x for s in sp[k]}
    return sp

def run(M):
    cnt = Counter(); marg = Counter(); ex = []
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
                cnt['n'] += 1
                _, side, (X, Y) = sl[0]
                Z, tt = (S, t) if side == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                a, b = C[X], C[Y]; m = a + b; Pi = Z[:m - 2]; need = tt[X] + tt[Y] - sum(Pi)
                spPi = spectra(Pi); outside = [v for v in Z if v not in Pi]; outs = set(outside)
                window = done = False; best_m = None
                for (A_, B_, ta) in ((X, Y, tt[X]), (Y, X, tt[Y])):
                    k = C[A_] - 1
                    for x in outside:
                        y = need - x
                        if y == x or y not in outs: continue
                        if ta - x not in spPi[k]: continue
                        window = True
                        rest = [v for v in outside if v not in (x, y)]; spR = spectra(rest)
                        for z in range(4):
                            if z in (X, Y): continue
                            if tt[z] in spR[C[z]]:
                                done = True
                                lo, hi = min(spR[C[z]]), max(spR[C[z]])
                                mz = min(tt[z] - lo, hi - tt[z]); best_m = mz if best_m is None else max(best_m, mz)
                        if done and best_m is not None and best_m >= 5: break
                    if done and best_m is not None and best_m >= 5: break
                cnt['window'] += window; cnt['done'] += done
                if done: marg[min(best_m, 5)] += 1
                elif len(ex) < 4: ex.append((q, C, t, (X, Y)))
    return cnt, marg, ex

if __name__ == '__main__':
    for M in map(int, sys.argv[1:]):
        cnt, marg, ex = run(M)
        print(M, 'pair-least', cnt['n'], 'window', cnt['window'], 'completes', cnt['done'], 'best complement margin (5 = >=5):', sorted(marg.items()), 'misses', ex, flush=True)
