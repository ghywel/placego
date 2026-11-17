"""CL480: does a staircase pair boundary exist on one-hole pools?  (The mechanism of FOUR-BIN-PARTITIONS 7-8.)

Instance in I2 (all 14 group targets in their spectra, every margin >= 2), reflected so that the global least
pair slack is a LOWER slack h of the pair (X, Y).  A boundary is P subset S with |P| = c_X + c_Y and sum
t_X + t_Y; it completes the instance if t_X in Sigma_(c_X)(P) and t_Z in Sigma_(c_Z)(S minus P) for some other
bin Z.  Shapes recorded for completing P (sorted values): prefix = number of initial pool values it contains,
high gaps = consecutive differences among its remaining values.
  staircase  : prefix >= 1 and every high gap in {1, 2, 3}  (P_m(h)/Q_m(h) have gaps 2 with one exception)
  strict     : prefix >= 1, all high gaps 2 except at most one in {1, 3}
Categories: pair-least (the least pair slack is strictly below every singleton slack) vs singleton-least.
Predictions (written first): a completing P exists in every instance (trivial, from a solution); a STAIRCASE
completing P exists in >= 95% of pair-least instances and in fewer singleton-least ones; the strict family
covers less.  Counterfactual: staircase coverage well below 90% would say the full-interval mechanism does not
transfer to one hole without a new shape.

OUTCOME.  M = 12 (8 s): pair-least 8,274 instances, staircase 8,022 (97.0%), strict 7,248; singleton-least
114,703, staircase 114,274 (99.6%), strict 74,700.  M = 13, first 400,000 instances (33 s): pair-least 27,948,
staircase 27,204 (97.3%); singleton-least 372,052, staircase 370,902 (99.7%).  A completing P exists always.
The misses are balanced targets, e.g. q2 (19,19,19,19), q3 (18,18,18,21), q2 3334 (6,24,24,35): every
completing boundary there has one jump of 4-6 between its low part and its high part (e.g. {0,1,7,8,10,12}).
Prediction held on coverage; the strict family covers less.  So the full-interval staircase nearly transfers,
and the data names the one extra shape it needs.
CL483 (jump shape added: prefix >= 1, high gaps <= 3 except at most one gap <= JUMPMAX = 6): coverage 100% at
M = 12 (8,274 + 114,703) and of the first 400,000 at M = 13 (27,948 + 372,052).  JUMPMAX = 5 still 100% at
M = 12; JUMPMAX = 4 misses 12 singleton-least instances (pair-least still 100%).  BASE RATE (jump_base_rate.py):
the jump shape holds for 43-57% of ALL m-subsets at M = 12 (staircase 10-25%), so this coverage is weak
evidence at these sizes; the real test is an explicit construction.
"""
import itertools, sys
from collections import Counter

T = lambda n: n * (n + 1) // 2
SUB = [J for s in (1, 2, 3) for J in itertools.combinations(range(4), s)]
PAIRS = list(itertools.combinations(range(4), 2))
JUMPMAX = 6

def spectra(pool):
    sp = [set() for _ in range(len(pool) + 1)]; sp[0].add(0)
    for x in pool:
        for k in range(len(pool) - 1, -1, -1):
            if sp[k]: sp[k + 1] |= {s + x for s in sp[k]}
    return sp

def shapes(P, S):
    pre = 0
    while pre < len(P) and P[pre] == S[pre]: pre += 1
    high = P[pre:]; gaps = [high[i + 1] - high[i] for i in range(len(high) - 1)]
    if pre >= 1 and high: gaps = [high[0] - S[pre - 1]] + gaps        # gap from the prefix to the first high value
    stair = pre >= 1 and all(g in (1, 2, 3) for g in gaps)
    strict = pre >= 1 and sum(1 for g in gaps if g != 2) <= 1 and all(g in (1, 2, 3) for g in gaps)
    big = [g for g in gaps if g > 3]
    jump = pre >= 1 and (len(big) == 0 or (len(big) == 1 and big[0] <= JUMPMAX))
    return stair, strict, jump

def run(M, limit=None):
    cnt = Counter(); ex = []
    for C in itertools.product(range(3, M - 8), repeat=4):
        if sum(C) != M: continue
        CJ = {J: sum(C[i] for i in J) for J in SUB}
        for q in range(1, M):
            S = [x for x in range(M + 1) if x != q]; tot = sum(S); N = len(S)
            sp = spectra(S); mins = lambda c: sum(S[:c]); maxs = lambda c: sum(S[N - c:])
            fib = {}      # (size, sum) -> list of P with spectra of both sides
            def fibre(m, s):
                if (m, s) not in fib:
                    L = []
                    for P in itertools.combinations(S, m):
                        if sum(P) == s:
                            R = [x for x in S if x not in P]
                            L.append((P, spectra(list(P)), spectra(R)))
                    fib[(m, s)] = L
                return fib[(m, s)]
            for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i]) + 1) for i in range(3)]):
                t = t3 + (tot - sum(t3),)
                tJ = {J: sum(t[i] for i in J) for J in SUB}
                if not all(tJ[J] in sp[CJ[J]] and tJ[J] - mins(CJ[J]) >= 2 and maxs(CJ[J]) - tJ[J] >= 2 for J in SUB): continue
                # least pair slack, lower or upper; reflect if upper
                best = None
                for p in PAIRS:
                    lo = tJ[p] - mins(CJ[p]); up = maxs(CJ[p]) - tJ[p]
                    for val, side in ((lo, 'lo'), (up, 'up')):
                        if best is None or val < best[0]: best = (val, side, p)
                h, side, (X, Y) = best
                sing = min(min(tJ[(i,)] - mins(C[i]), maxs(C[i]) - tJ[(i,)]) for i in range(4))
                cat = 'pair-least' if h < sing else 'singleton-least'
                if side == 'up':
                    S2 = [M - x for x in reversed(S)]; t2 = tuple(C[i] * M - t[i] for i in range(4))
                else:
                    S2, t2 = S, t
                if S2 is not S:
                    # recompute fibre on the reflected pool (cache per pool)
                    key = ('refl', q)
                    if key not in fib:
                        fib[key] = {}
                    fibR = fib[key]
                    def fibre2(m, s):
                        if (m, s) not in fibR:
                            L = []
                            for P in itertools.combinations(S2, m):
                                if sum(P) == s:
                                    R = [x for x in S2 if x not in P]
                                    L.append((P, spectra(list(P)), spectra(R)))
                            fibR[(m, s)] = L
                        return fibR[(m, s)]
                    F = fibre2(C[X] + C[Y], t2[X] + t2[Y])
                else:
                    F = fibre(C[X] + C[Y], t2[X] + t2[Y])
                others = [z for z in range(4) if z not in (X, Y)]
                any_c = stair_c = strict_c = jump_c = False
                for P, spP, spR in F:
                    if t2[X] not in spP[C[X]]: continue
                    if not any(t2[z] in spR[C[z]] for z in others): continue
                    any_c = True
                    st, sr, jp = shapes(list(P), S2)
                    stair_c |= st; strict_c |= sr; jump_c |= jp
                    if strict_c and jump_c: break
                cnt[(cat, 'n')] += 1; cnt[(cat, 'any')] += any_c; cnt[(cat, 'stair')] += stair_c; cnt[(cat, 'strict')] += strict_c; cnt[(cat, 'jump')] += jump_c
                if not jump_c and len(ex) < 6: ex.append((cat, q, C, t, (X, Y), h))
                if limit and sum(v for k, v in cnt.items() if k[1] == 'n') >= limit: return cnt, ex
    return cnt, ex

if __name__ == '__main__':
    M = int(sys.argv[1]); limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
    cnt, ex = run(M, limit)
    for cat in ('pair-least', 'singleton-least'):
        n = cnt[(cat, 'n')]
        print(M, cat, 'instances', n, 'completing P exists', cnt[(cat, 'any')], 'staircase', cnt[(cat, 'stair')], 'strict', cnt[(cat, 'strict')], 'jump<=6', cnt[(cat, 'jump')])
    print('examples without a one-jump boundary:', ex)
