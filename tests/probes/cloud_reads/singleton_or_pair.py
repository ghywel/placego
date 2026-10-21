"""CL486: does every singleton-least I2 instance admit EITHER a completing least-pair boundary (rank staircase, value
staircase or PPP) OR a least-singleton recipe whose three-bin remainder completes?

Singleton recipe (G315/G316 section 5, on the actual pool): the least-slack singleton A (reflected to a lower slack)
takes the l smallest and k largest pool values plus one pivot, l + k = c_A - 1, with sum t_A.  The remainder is a
pool with at most two holes; three-bin completion is decided by brute force (cached per remainder pool).
Prediction (written first): 100% at M = 12 (the union covers everything).  Counterfactual: residual instances
would be the genuine joint-selector obstruction, the place a proof must work hardest.

OUTCOME (CL486).  Without missing-pivot repairs, M = 12: least-pair boundary 109,960 of 114,703, canonical
recipe +4,186, NEITHER 557 (prediction failed); adding any singleton and any pair: 13 left, all q6 3333
(7,18,18,29), whose A sets {0,2,5}, {0,3,4} are G315 repairs of the missing pivot 6.  With the repairs in the
recipe: M = 12: 109,960 + 4,743 = 114,703, NONE 0; M = 13: 758,160 + 38,544 = 796,704, NONE 0 (84 s).
Prediction 4 held.
"""
import itertools, sys
from functools import lru_cache
from collections import Counter
sys.argv_saved = sys.argv; sys.argv = ['x']
exec(open('tests/probes/cloud_reads/rank_staircase.py').read().split("if __name__")[0])
sys.argv = sys.argv_saved

@lru_cache(maxsize=None)
def three_bin(pool, sizes):
    """set of (sB, sC) achievable by disjoint subsets of sizes (b, c) of pool; D gets the rest"""
    b, c = sizes[0], sizes[1]; out = set(); pool = list(pool)
    for B in itertools.combinations(pool, b):
        sB = sum(B); rest = [x for x in pool if x not in B]
        for Cc in itertools.combinations(rest, c): out.add((sB, sum(Cc)))
    return frozenset(out)


def recipes(Z, a, target, hole_vals):
    """prefix/suffix/pivot sets of size a and sum target on the sorted pool Z, plus G315's missing-pivot repairs:
    if the needed pivot is a missing value v (inside the span), replace {v, u} by {v+1, u-1} (u = least suffix value)
    or {l-1, v} by {l, v-1} (l-1 = greatest prefix value), when the new values are present and unused."""
    N = len(Z); Zs = set(Z); out = []
    for k in range(0, a):
        l = a - 1 - k; low = Z[:l]; high = Z[N - k:] if k else []
        need = target - sum(low) - sum(high)
        lo_b = Z[l] if l < N else None; hi_b = Z[N - k - 1] if N - k - 1 >= 0 else None
        if lo_b is None or hi_b is None or need < lo_b or need > hi_b: continue
        if need in Zs and need not in low and need not in high:
            out.append(tuple(low) + tuple(high) + (need,)); continue
        if need in Zs: continue
        # missing pivot: repairs
        used = set(low) | set(high)
        if high:
            u = min(high)
            if need + 1 in Zs and u - 1 in Zs and need + 1 not in used and u - 1 not in used and need + 1 != u - 1:
                out.append(tuple(low) + tuple(h for h in high if h != u) + (need + 1, u - 1))
        if low:
            w = max(low)
            if w + 1 in Zs and need - 1 in Zs and w + 1 not in used and need - 1 not in used and w + 1 != need - 1:
                out.append(tuple(lw for lw in low if lw != w) + tuple(high) + (w + 1, need - 1))
    return out

def pair_boundary_ok(Z, C, tt, X, Y, M, N, hole):
    m = C[X] + C[Y]; target = tt[X] + tt[Y]
    def comp(P):
        rest = [x for x in Z if x not in P]; spP = spectra(P); spR = spectra(rest)
        return (tt[X] in spP[C[X]] or tt[Y] in spP[C[Y]]) and any(tt[z] in spR[C[z]] for z in range(4) if z not in (X, Y))
    for H in range(0, m * (N - m) + 1):
        for R in stair_sets(m, H):
            if max(R) >= N: continue
            P = [Z[r] for r in R]
            if sum(P) == target and comp(P): return True
    pre = Z[:m - 2]; need = target - sum(pre)
    for x in Z[m - 2:]:
        y = need - x
        if y > x and y in Z and y not in pre and comp(pre + [x, y]): return True
    return False

def run(M, limit=None):
    cnt = Counter(); ex = []
    for C in itertools.product(range(3, M - 8), repeat=4):
        if sum(C) != M: continue
        CJ = {J: sum(C[i] for i in J) for J in SUB}
        for q in range(1, M):
            S = [x for x in range(M + 1) if x != q]; tot = sum(S); N = len(S)
            sp = spectra(S); mins = lambda c: sum(S[:c]); maxs = lambda c: sum(S[N - c:])
            Rf = [M - x for x in reversed(S)]
            for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i]) + 1) for i in range(3)]):
                t = t3 + (tot - sum(t3),)
                tJ = {J: sum(t[i] for i in J) for J in SUB}
                if not all(tJ[J] in sp[CJ[J]] and tJ[J] - mins(CJ[J]) >= 2 and maxs(CJ[J]) - tJ[J] >= 2 for J in SUB): continue
                sl = sorted([(tJ[p] - mins(CJ[p]), 'lo', p) for p in PAIRS] + [(maxs(CJ[p]) - tJ[p], 'up', p) for p in PAIRS])
                ss = sorted([(t[i] - mins(C[i]), 'lo', i) for i in range(4)] + [(maxs(C[i]) - t[i], 'up', i) for i in range(4)])
                if not ss[0][0] <= sl[0][0]: continue        # singleton-least (ties included)
                cnt['n'] += 1
                h, side, (X, Y) = sl[0]
                Z, tt = (S, t) if side == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                if pair_boundary_ok(Z, C, tt, X, Y, M, N, None):
                    cnt['pair'] += 1; continue
                # singleton recipe for the least singleton
                h1, side1, A = ss[0]
                Z1, t1 = (S, t) if side1 == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                a = C[A]; others = [i for i in range(4) if i != A]; ok = False
                for Aset in recipes(Z1, a, t1[A], None):
                    rem = tuple(x for x in Z1 if x not in Aset)
                    if (t1[others[0]], t1[others[1]]) in three_bin(rem, tuple(C[i] for i in others)): ok = True; break
                cnt['singleton'] += ok
                if not ok:
                    # ANY singleton, either frame, any recipe
                    for h2, side2, A2 in ss[1:]:
                        Z2, t2 = (S, t) if side2 == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                        a2 = C[A2]; oth = [i for i in range(4) if i != A2]
                        for Aset in recipes(Z2, a2, t2[A2], None):
                            rem = tuple(x for x in Z2 if x not in Aset)
                            if (t2[oth[0]], t2[oth[1]]) in three_bin(rem, tuple(C[i] for i in oth)): ok = True; break
                        if ok: break
                    cnt['other_singleton'] += ok
                    if not ok:
                        for h3, side3, (X3, Y3) in sl[1:]:
                            Z3, t3_ = (S, t) if side3 == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                            if pair_boundary_ok(Z3, C, t3_, X3, Y3, M, N, None): ok = True; break
                        cnt['other_pair'] += ok
                if not ok:
                    cnt['neither'] += 1
                    if len(ex) < 6: ex.append((q, C, t))
                if limit and cnt['n'] >= limit: return cnt, ex
    return cnt, ex

if __name__ == '__main__':
    M = int(sys.argv[1]); limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
    cnt, ex = run(M, limit)
    print(M, 'singleton-least instances', cnt['n'], 'least-pair boundary', cnt['pair'], 'else canonical singleton recipe', cnt['singleton'], 'else other singleton recipe', cnt['other_singleton'], 'else other pair boundary', cnt['other_pair'], 'NONE', cnt['neither'])
    print('neither examples:', ex, flush=True)
