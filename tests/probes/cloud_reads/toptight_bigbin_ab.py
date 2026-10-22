"""CL526: CL524's selector for top-tight big-bin instances with small bins of sizes (a, b), a, b in {3, 4}, big bin X.
Strictly top-tight: the least H(h) slack is attained only by the pair {A, B}.  Rules for A's realization (then any
B-set in the remainder): lexmin, minmax (smallest maximum), maxmin (largest minimum), refined (through min S, largest
maximum); each also with A and B exchanged.  Exact.

OUTCOME (CL526): (3,4,6) h<=3, (4,4,6) h<=3, (3,4,8) h=2: 88,524 instances; minmax+swap ALONE 100% on every domain.
"""
import sys
from itertools import combinations
from collections import Counter

def L(r): return r * (r - 1) // 2

def run(M, h, a, b, X):
    n = a + b + X; assert M + 1 - h == n
    cnt = Counter(); ex = []
    for H in combinations(range(M + 1), h):
        S = [x for x in range(M + 1) if x not in H]; tot = sum(S)
        subs = {a: {}, b: {}}
        for c in set((a, b)):
            for T in combinations(S, c): subs[c].setdefault(sum(T), []).append(T)
        def works(T, c, v):
            rest = [x for x in S if x not in T]
            return any(sum(Y) == v for Y in combinations(rest, c))
        for u1 in subs[a]:
            for u2 in subs[b]:
                u3 = tot - u1 - u2
                groups = [((0,), a, u1), ((1,), b, u2), ((2,), X, u3), ((0, 1), a + b, u1 + u2), ((0, 2), a + X, u1 + u3), ((1, 2), b + X, u2 + u3)]
                sl = {J: u - L(r) - h * r for J, r, u in groups}
                mn = min(sl.values())
                if mn < 0 or not (sl[(0, 1)] == mn and all(sl[J] > mn for J in sl if J != (0, 1))): continue
                if not any(works(T, b, u2) for T in subs[a][u1]): cnt['infeasible'] += 1; continue
                cnt['n'] += 1
                def pick(c, u, rule):
                    Ts = subs[c][u]
                    if rule == 'lexmin': return min(Ts)
                    if rule == 'minmax': return min(Ts, key=lambda T: (max(T), T))
                    if rule == 'maxmin': return max(Ts, key=lambda T: (min(T), [-x for x in T]))
                    thr = [T for T in Ts if T[0] == S[0]]
                    return max(thr, key=lambda T: (T[-1], T)) if thr else min(Ts, key=lambda T: (max(T), T))
                anyok = False; mm = False
                for rule in ('lexmin', 'minmax', 'maxmin', 'refined'):
                    ok = works(pick(a, u1, rule), b, u2) or works(pick(b, u2, rule), a, u1)
                    anyok |= ok
                    if rule == 'minmax': mm = ok
                cnt['any4+swap'] += anyok; cnt['minmax+swap'] += mm
                if not anyok and len(ex) < 4: ex.append((H, (u1, u2, u3)))
    return cnt, ex

if __name__ == '__main__':
    for M, h, a, b, X in ((13, 1, 3, 4, 6), (14, 2, 3, 4, 6), (15, 3, 3, 4, 6), (14, 1, 4, 4, 6), (15, 2, 4, 4, 6), (16, 3, 4, 4, 6), (16, 2, 3, 4, 8)):
        cnt, ex = run(M, h, a, b, X)
        print('M', M, 'h', h, 'sizes', (a, b, X), dict(cnt), 'all-rule failures:', ex, flush=True)
