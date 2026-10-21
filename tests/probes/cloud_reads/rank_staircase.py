"""CL484: an explicit one-hole pair boundary: FOUR s7's staircase P_m(H) / Q_m(H) transported to the pool by RANKS.

Pool S = [0, M] minus q with sorted values z_0 < ... < z_(N-1).  For a rank set R let P = {z_r : r in R}.  FOUR s7:
  H = T_s + t (0 <= t <= s), p = m - s:  P_m(H) = {0..p-1} u {p + 2j + 1 + [j >= s - t] : 0 <= j < s}
  t >= 1, S' = s + 1, q' = m - S':      Q_m(H) = {0..q'-1} u {q' + 2j + 1 - [j >= t] : 0 <= j < S'}
For a pair-least instance (least slack is a pair's, strictly below every singleton's), reflected so that it is the
pair's LOWER slack, try every H with sum(z_R) = t_X + t_Y (the rank displacement H differs from the value slack by
the number of chosen ranks at or above the hole), both families, and test completion directly:
t_X in Sigma_(c_X)(P) and some other t_Z in Sigma_(c_Z)(S minus P).
Prediction (written first): >= 95% of pair-least I2 instances at M = 12 complete; the misses have the hole inside
the boundary's high part.  Counterfactual: <= 80% would say rank transport is the wrong formula.
OUTCOME (CL484).  Rank staircase alone: M = 12 8,226 / 8,274 (99.4%); M = 13 59,256 / 59,688 (99.3%); M = 14
251,628 / 253,356 (99.3%).  Misses: two bins of size 3 (or 3,4) at h = 6, 8, specific hole positions; e.g. hole 1,
pair 13/13: the only staircase {0,2,3,5,7,9} has no 13+13 split.  Value staircase (formula read on values,
legal iff it avoids the hole): rescues 0 (prediction FAILED; at hole 1 it is the same set).  Prefix-plus-pair
(the m-2 smallest pool values and one pair {x,y} of the right sum): rescues ALL residual misses, 48 / 432 / 1,728,
so rank staircase + prefix-plus-pair covers 100% of pair-least I2 instances at M = 12, 13, 14 (321,318).
Unexpected check: prefix-plus-pair ALONE covers all 8,274 at M = 12.
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

def stair_sets(m, H):
    out = []
    if H == 0: return [list(range(m))]
    s = 1
    while T(s + 1) <= H: s += 1
    t = H - T(s)
    if t > s: return out
    p = m - s
    if p >= 1: out.append(list(range(p)) + [p + 2 * j + 1 + (j >= s - t) for j in range(s)])
    if t >= 1:
        S1 = s + 1; q1 = m - S1
        if q1 >= 1: out.append(list(range(q1)) + [q1 + 2 * j + 1 - (j >= t) for j in range(S1)])
    return out

def run(M):
    cnt = Counter(); ex = []
    for C in itertools.product(range(3, M - 8), repeat=4):
        if sum(C) != M: continue
        CJ = {J: sum(C[i] for i in J) for J in SUB}
        for q in range(1, M):
            S = [x for x in range(M + 1) if x != q]; tot = sum(S); N = len(S)
            sp = spectra(S); mins = lambda c: sum(S[:c]); maxs = lambda c: sum(S[N - c:])
            for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i]) + 1) for i in range(3)]):
                t = t3 + (tot - sum(t3),)
                tJ = {J: sum(t[i] for i in J) for J in SUB}
                if not all(tJ[J] in sp[CJ[J]] and tJ[J] - mins(CJ[J]) >= 2 and maxs(CJ[J]) - tJ[J] >= 2 for J in SUB): continue
                best = None
                for pr in PAIRS:
                    for val, side in ((tJ[pr] - mins(CJ[pr]), 'lo'), (maxs(CJ[pr]) - tJ[pr], 'up')):
                        if best is None or val < best[0]: best = (val, side, pr)
                h, side, (X, Y) = best
                sing = min(min(t[i] - mins(C[i]), maxs(C[i]) - t[i]) for i in range(4))
                if not h < sing: continue
                if side == 'up':
                    Z = [M - x for x in reversed(S)]; tt = tuple(C[i] * M - t[i] for i in range(4)); hole = M - q
                else:
                    Z, tt, hole = S, t, q
                m = C[X] + C[Y]; target = tt[X] + tt[Y]
                cnt['n'] += 1
                ok = False; sum_hit = False
                for H in range(0, m * (N - m) + 1):
                    for R in stair_sets(m, H):
                        if max(R) >= N: continue
                        P = [Z[r] for r in R]
                        if sum(P) != target: continue
                        sum_hit = True
                        rest = [x for x in Z if x not in P]
                        spP = spectra(P); spR = spectra(rest)
                        if tt[X] in spP[C[X]] and any(tt[z] in spR[C[z]] for z in range(4) if z not in (X, Y)):
                            ok = True; break
                    if ok: break
                okv = False
                if not ok:
                    # value staircase: the same formula read as VALUES of [0, M]; legal iff it avoids the hole
                    for R in stair_sets(m, target - m * (m - 1) // 2) if target - m * (m - 1) // 2 >= 0 else []:
                        if max(R) > M or hole in R: continue
                        P = list(R); rest = [x for x in Z if x not in P]
                        spP = spectra(P); spR = spectra(rest)
                        if tt[X] in spP[C[X]] and any(tt[z] in spR[C[z]] for z in range(4) if z not in (X, Y)):
                            okv = True; break
                    # and the pair's two bins swapped in the role of X (X only matters through t_X in Sigma(P))
                okp = False
                if not ok and not okv:
                    # prefix-plus-pair: the m-2 smallest pool values and one pair {x, y} with the right sum
                    pre = Z[:m - 2]; need = target - sum(pre)
                    for x in Z[m - 2:]:
                        y = need - x
                        if y <= x or y not in Z or y in pre: continue
                        P = pre + [x, y]; rest = [v for v in Z if v not in P]
                        spP = spectra(P); spR = spectra(rest)
                        if tt[X] in spP[C[X]] and any(tt[z] in spR[C[z]] for z in range(4) if z not in (X, Y)):
                            okp = True; break
                cnt['okp'] += okp
                cnt['ok'] += ok; cnt['okv'] += okv; cnt['sum_hit'] += sum_hit
                ok = ok or okp
                ok = ok or okv
                if not (ok or okv) and len(ex) < 6: ex.append((q, C, t, (X, Y), side, h, 'sum reachable' if sum_hit else 'no staircase of that sum'))
    return cnt, ex

if __name__ == '__main__':
    for M in map(int, sys.argv[1:]):
        cnt, ex = run(M)
        print(M, 'pair-least instances', cnt['n'], 'rank staircase of the right sum exists', cnt['sum_hit'], 'rank staircase completes', cnt['ok'], 'value staircase rescues', cnt['okv'], 'prefix-plus-pair rescues', cnt['okp'])
        print('  misses:', ex, flush=True)
