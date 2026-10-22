"""CL540 unexpected check: does CL524's blind middle-bin chain (lexmin / minmax / maxmin / refined for one small bin,
both orders, any triple for the other, big bin the rest) solve EVERY feasible (3, 3, X) target vector on [0, M] minus
nh holes, or only lexmin's children?  Run: python3 chain_general.py M nh X.

OUTCOME (CL540): NOT general.  [0, 15] minus 4 holes, X = 6: 1,041,891 feasible vectors, 276 misses (176 with UNEQUAL
small targets, e.g. holes 0 1 6 11 | 14, 18; holes 0 2 6 11 | 33, 37; targets near the spectrum ends).  The chain's
100% on lexmin's children (CL540) is a property of the children, not of every (3, 3, 6) instance.
By pool-relative key (CL539): misses at key 0: 274 of 276 ([0,15]-4, X = 6), 379 of 380 ([0,17]-4, X = 8); the three
key-1 misses all have EQUAL small targets (holes 1 5 8 12 | 14 14; holes 3 7 10 14 | 31 31).  So every unequal miss
sits at key 0, at the ends of the spectrum.
"""
import sys
from itertools import combinations
from collections import Counter

def run(M, nh, X):
    cnt = Counter(); ex = []
    for H in combinations(range(M + 1), nh):
        S = [x for x in range(M + 1) if x not in H]
        if len(S) != 6 + X: raise SystemExit('sizes')
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
        sums = sorted(by)
        for u1 in sums:
            for u2 in sums:
                if u2 < u1: continue
                if not any(free(u2, T) for T in by[u1]): continue      # infeasible
                cnt['feasible'] += 1
                ok = False
                for mid, last in ((u1, u2), (u2, u1)):
                    for rule in range(4):
                        Q = pick(mid, rule)
                        if Q is not None and free(last, Q): ok = True; break
                    if ok: break
                if ok: cnt['solved'] += 1
                else:
                    cnt['miss_eq' if u1 == u2 else 'miss_neq'] += 1
                    t = (u1, u2, sum(S) - u1 - u2); key = 1 << 30   # pool-relative key (CL539)
                    for J, r in (((0,), 3), ((1,), 3), ((2,), X), ((0, 1), 6), ((0, 2), 3 + X), ((1, 2), 3 + X)):
                        key = min(key, (sum(t[i] for i in J) - sum(S[:r])) // r)
                    cnt['miss_key%d' % key] += 1
                    if len(ex) < 6 and u1 != u2: ex.append((H, u1, u2))
    return cnt, ex

if __name__ == '__main__':
    M, nh, X = map(int, sys.argv[1:4]); print(M, nh, X, *run(M, nh, X), flush=True)
