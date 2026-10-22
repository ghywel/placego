"""CL529: the big-bin top-tight case is LOCAL.  If the pair {A, B} (two size-3 bins) has strictly least H(h) slack, then
sigma_AB < sigma_A gives u2 < 12 + 3h (and u1 likewise), so u_i = 3 + 3h + e_i with 0 <= e_i <= 8, e1 + e2 >= 9
(sigma_AB >= 0), and every element used is <= 10 + 3h.  Lemma L(h): for every set of at most h holes in [0, 10 + 3h]
and all such e1 <= e2, the rest of [0, 10 + 3h] contains disjoint triples with sums 3 + 3h + e1 and 3 + 3h + e2.
Truncated pools (M < 10 + 3h; n >= 12 forces M >= 11 + h) are checked separately with the big bin's H(h) cuts.

OUTCOME (CL529): no failure for h = 0..6 (h = 6: 621,616 window configurations + 1,528,956 truncated pools); without
the big-bin cuts, the only truncated failure (h = 5, pool [0,11], 26 + 26) is not an H(5) instance.  With the
localisation argument this proves the strictly-pair-least (3,3,X >= 6) case of H(h) for every h <= 6, all M and X.

import sys
from itertools import combinations
from collections import Counter

def ok(T, a, b):
    Ts = set(T)
    for X in combinations(T, 3):
        if sum(X) != a: continue
        rest = [x for x in T if x not in X]
        for Y in combinations(rest, 3):
            if sum(Y) == b: return True
    return False

if __name__ == '__main__':
    for h in range(0, int(sys.argv[1]) + 1):
        W = 10 + 3 * h; fails = Counter(); ex = []; configs = 0
        for k in range(0, h + 1):
            for H in combinations(range(W + 1), k):
                T = [x for x in range(W + 1) if x not in H]; configs += 1
                for e1 in range(0, 9):
                    for e2 in range(max(e1, 9 - e1), 9):
                        if not ok(T, 3 + 3 * h + e1, 3 + 3 * h + e2):
                            fails['equal' if e1 == e2 else ('adjacent' if e2 == e1 + 1 else 'gap>=2')] += 1
                            if len(ex) < 4: ex.append((H, e1, e2))
        # truncated pools: M in [11 + h, 9 + 3h] (n = M + 1 - h >= 12), all h holes inside [0, M]
        tconf = 0
        for Mt in range(11 + h, 10 + 3 * h):
            for H in combinations(range(Mt + 1), h):
                T = [x for x in range(Mt + 1) if x not in H]; tconf += 1
                n = len(T); tot = sum(T); X = n - 6
                for e1 in range(0, 9):
                    for e2 in range(max(e1, 9 - e1), 9):
                        a, b = 3 + 3 * h + e1, 3 + 3 * h + e2
                        c = tot - a - b
                        Lr = lambda r: r * (r - 1) // 2
                        if c - Lr(X) - h * X < 0 or a + c - Lr(3 + X) - h * (3 + X) < 0 or b + c - Lr(3 + X) - h * (3 + X) < 0:
                            fails['trunc_not_admitted'] += 0; continue    # not an H(h) instance (big-bin cuts)
                        if not ok(T, a, b):
                            fails['trunc_' + ('equal' if e1 == e2 else 'unequal')] += 1
                            if len(ex) < 6: ex.append(('trunc', Mt, H, e1, e2))
        print('h', h, 'window [0,%d]' % W, 'hole configurations', configs, '+ truncated', tconf, 'failures', dict(fails), ex, flush=True)
