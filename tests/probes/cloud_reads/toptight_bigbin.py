"""CL524: top-tight big-bin instances (CL515): three bins (3, 3, X), X >= 6, in H(h) on [0, M] minus h holes, whose
least slack is the pair {A, B} of small bins (so the big bin C is top-tight).  Solving = choosing disjoint triples
X1, X2 with sums u1, u2 (C takes the rest).  Blind greedy selectors for X1, then any X2 in the remainder:
  lexmin  - lexicographically smallest triple of sum u1;
  minmax  - triple of sum u1 with the smallest maximum (ties: lexmin);
  maxmin  - triple of sum u1 with the largest minimum;
  refined - minmax, except for equal targets: the triple through min S with the largest maximum;
  swap    - also try the same rules with the roles of A and B exchanged.

OUTCOME (CL524).  Strictly top-tight (3,3,X) instances, X = 6..8, h <= 4, M <= 16 (eight domains, 41,950 instances):
no single blind rule is 100% (minmax+swap misses 3, 11, 4 at (14,3,6), (15,4,6), (16,4,7); the misses have equal small
targets and clustered holes); ANY of the four rules with swap: 100% on every domain.  CL525: also (16,5,6), (17,5,7);
minmax misses are equal targets except two with u2 = u1 + 1 and a 4-hole run; 74,594 instances in all, any-of-4 100%.
"""
import sys
from itertools import combinations
from collections import Counter

def L(r): return r * (r - 1) // 2

def run(M, h, X):
    n = 6 + X; assert M + 1 - h == n
    cnt = Counter(); ex = []
    for H in combinations(range(M + 1), h):
        S = [x for x in range(M + 1) if x not in H]; tot = sum(S)
        trip = {}
        for T in combinations(S, 3): trip.setdefault(sum(T), []).append(T)
        for u1 in range(3, 3 * M):
            for u2 in range(u1, 3 * M):
                u3 = tot - u1 - u2
                C = (3, 3, X); t = (u1, u2, u3)
                groups = [((0,), 3, u1), ((1,), 3, u2), ((2,), X, u3), ((0, 1), 6, u1 + u2), ((0, 2), 3 + X, u1 + u3), ((1, 2), 3 + X, u2 + u3)]
                sl = {J: u - L(r) - h * r for J, r, u in groups}
                if min(sl.values()) < 0: continue
                mn = min(sl.values())
                if not (sl[(0, 1)] == mn and all(sl[J] > mn for J in sl if J != (0, 1))): continue   # strictly top-tight C
                if u1 not in trip or u2 not in trip: continue
                feas = any(sum(Y) == u2 for X1 in trip[u1] for Y in combinations([x for x in S if x not in X1], 3))
                if not feas: cnt['infeasible'] += 1; continue
                cnt['n'] += 1
                def works(X1, v):
                    rest = [x for x in S if x not in X1]
                    return any(sum(Y) == v for Y in combinations(rest, 3))
                rules = {
                    'lexmin': lambda us, v: works(min(trip[us]), v),
                    'minmax': lambda us, v: works(min(trip[us], key=lambda T: (max(T), T)), v),
                    'maxmin': lambda us, v: works(max(trip[us], key=lambda T: (min(T), [-x for x in T])), v),
                    'refined': lambda us, v: works(min(trip[us], key=lambda T: (max(T), T)) if us != v or not [T for T in trip[us] if T[0] == S[0]]
                                                   else max([T for T in trip[us] if T[0] == S[0]], key=lambda T: (T[2], T)), v),
                }
                anyok = False
                for name, f in rules.items():
                    ok = f(u1, u2); ok2 = ok or f(u2, u1)
                    cnt[name] += ok; cnt[name + '+swap'] += ok2; anyok |= ok2
                cnt['any4+swap'] += anyok
                if not anyok and len(ex) < 4: ex.append((H, t))
    return cnt, ex

if __name__ == '__main__':
    for M, h, X in ((12, 1, 6), (13, 2, 6), (14, 3, 6), (14, 2, 7), (15, 3, 7), (15, 4, 6), (16, 4, 7), (16, 3, 8)):
        cnt, ex = run(M, h, X)
        print('M', M, 'h', h, 'X', X, dict(cnt), 'examples of all-rule failures:', ex, flush=True)
