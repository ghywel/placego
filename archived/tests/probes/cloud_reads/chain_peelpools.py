"""CL541 follow-up: run the generic blind chain (chain_general.py) on PEEL-SHAPED pools only: [0, M] minus h base holes,
minus one of the base pool's top three values, minus any pair below it (the shape of lexmin's child, CL538), over ALL
feasible (3, 3, X) target vectors.  Misses are tallied by the record's H-key relative to nh = h + 3.
PARENT=1 keeps only vectors whose parent (u_A = a + b + z, u_B, u_C, u_X) is in H(h) on [0, M] minus h holes.
Run: [PARENT=1] python3 chain_peelpools.py M h X.

OUTCOME (CL541 addendum).  Peel-shaped pools, H-key >= nh - 3: (15,1,6) 1,105 pools, 516,134 feasible, misses 54 + 27 eq
at nh - 3 and 2 at nh - 2; (16,2,6) 4,186 pools, 1,622,052 feasible, 126 + 74 eq at nh - 3, 2 + 3 eq at nh - 2.
PARENT=1 (15,1,6): 1,302,125 feasible (pool, u_A) vectors, 137 + 78 eq at nh - 3, 6 at nh - 2.  So neither the pool's
shape nor the parent's H(h) membership explains why lexmin's children never miss: top-tightness of A or lexmin's choice
of the pair is essential.
"""
import sys
from itertools import combinations
from collections import Counter

def chain_pool(S, X, cnt, ex, nh, seen, parent=None):
    by = {}
    for T in combinations(S, 3): by.setdefault(sum(T), []).append(T)
    def pick(u, rule):
        Ts = by.get(u)
        if not Ts: return None
        if rule == 0: return Ts[0]
        if rule == 1: return min(Ts, key=lambda T: (T[2], T))
        if rule == 2: return max(Ts, key=lambda T: (T[0], [-x for x in T]))
        Z = [T for T in Ts if T[0] == S[0]]
        return max(Z, key=lambda T: T[2]) if Z else None
    def free(v, Q): return any(not set(T) & set(Q) for T in by.get(v, ()))
    sums = sorted(by); tot = sum(S)
    for u1 in sums:
        for u2 in sums:
            if u2 < u1: continue
            t = (u1, u2, tot - u1 - u2)
            hk = min((sum(t[i] for i in J) - r * (r - 1) // 2) // r for J, r in (((0,), 3), ((1,), 3), ((2,), X), ((0, 1), 6), ((0, 2), 3 + X), ((1, 2), 3 + X)))
            if hk < nh - 3: continue
            if parent is not None:   # PARENT=1: keep only vectors whose parent (u_A, t) is in H(h) on [0, M] minus h holes
                uA, h0 = parent; P = (uA, u1, u2, t[2]); Cs = (3, 3, 3, X)
                if any((sum(P[i] for i in J) - L(r) - h0 * r) < 0 for J, r in GROUPS(Cs)): continue
            if not any(free(u2, T) for T in by[u1]): continue
            cnt['feasible'] += 1
            ok = any((Q := pick(mid, r)) is not None and free(last, Q) for mid, last in ((u1, u2), (u2, u1)) for r in range(4))
            if not ok:
                cnt['miss_H%+d_%s' % (hk - nh, 'eq' if u1 == u2 else 'neq')] += 1
                if len(ex) < 6: ex.append((S, t))

def L(r): return r * (r - 1) // 2
def GROUPS(Cs):
    return [(J, sum(Cs[i] for i in J)) for s_ in (1, 2, 3) for J in combinations(range(4), s_)]
PARENT = __import__('os').environ.get('PARENT') == '1'

def run(M, h, X):
    cnt = Counter(); ex = []; seen = set()
    for H in combinations(range(M + 1), h):
        B = [x for x in range(M + 1) if x not in H]
        for z in B[-3:]:
            low = [x for x in B if x < z]
            for a, b in combinations(low, 2):
                S = tuple(x for x in B if x not in (a, b, z))
                if PARENT:   # the same child pool can arise from different peels with different u_A
                    if (S, a + b + z) in seen: continue
                    seen.add((S, a + b + z)); chain_pool(list(S), X, cnt, ex, h + 3, seen, (a + b + z, h)); continue
                if S in seen: continue
                seen.add(S); assert len(S) == 6 + X
                chain_pool(list(S), X, cnt, ex, h + 3, seen)
    cnt['pools'] = len(seen)
    return cnt, ex

if __name__ == '__main__':
    M, h, X = map(int, sys.argv[1:4]); c, ex = run(M, h, X); print(M, h, X, sorted(c.items()), ex[:4], flush=True)
