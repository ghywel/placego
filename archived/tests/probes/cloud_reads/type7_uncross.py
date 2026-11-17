"""CL475 bounded test: can core row 7 be uncrossed into two-group inequalities that always hold?

Row 7 (labels a,b,c,d):  s7 = 2H - (rho_a + rho_cd + rho_bd + rho_abc) >= 0.  Three exact decompositions
uncross one crossing pair each:
 U1 (cd, bd -> d, bcd):   s7 = [H - rho_a - rho_bcd] + [H - rho_d - rho_abc] + [rho_d + rho_bcd - rho_cd - rho_bd]
 U2 (cd, abc -> c, V):    s7 = [H - rho_a - rho_bd - rho_c] + [rho_c + H - rho_cd - rho_abc]
 U3 (bd, abc -> b, V):    s7 = [H - rho_a - rho_cd - rho_b] + [rho_b + H - rho_bd - rho_abc]
The first brackets are proved partition rows.  The last bracket of each is a two-group SUPERMODULARITY
term sigma(X, Y) = rho(X & Y) + rho(X | Y) - rho(X) - rho(Y).
Question: over every protected min3 instance and every labelling, is max(sigma_U1, sigma_U2, sigma_U3) >= 0?
If so, row 7 follows from 'one of three local supermodularities' plus proved rows.
Predictions: no single sigma is always >= 0; the max is >= 0 in every instance.  Counterfactual: an instance
with all three negative means uncrossing alone cannot prove row 7.

OUTCOME: M = 12: 1,682,856 labelled rows, s7 < 0 never, each sigma negative in ~1.6%, never all three.
M = 12..14: 63,541,704 labelled rows, s7 < 0 never, all three negative in 264 (first: M13, q2, sizes
3334, targets 14/23/34/18, s7 = 1).  Prediction FAILED at M = 13: uncrossing alone cannot prove row 7.
"""
import itertools, sys
from collections import Counter
L = lambda n: n * (n - 1) // 2
T = lambda n: n * (n + 1) // 2
SUB = [J for s in (1, 2, 3, 4) for J in itertools.combinations(range(4), s)]

def run(MMAX):
    st = Counter(); ex = []
    for M in range(12, MMAX + 1):
        for C in itertools.product(range(3, M), repeat=4):
            if sum(C) != M: continue
            for q in range(1, M):
                H = M - q; S = T(M) - q; memo = {}
                def rho(c, t):
                    if (c, t) not in memo:
                        v = [r for r in range(max(0, c - q), min(c, H) + 1)
                             if L(c - r) + (q + 1) * r + L(r) <= t <= (c - r) * (q - 1) - L(c - r) + M * r - L(r)]
                        memo[(c, t)] = min(v)
                    return memo[(c, t)]
                for t3 in itertools.product(*[range(T(C[i]), S - T(M - C[i]) + 1) for i in range(3)]):
                    t = t3 + (S - sum(t3),)
                    if not all(sum(t[i] for i in J) >= T(sum(C[i] for i in J)) for J in SUB[:-1]): continue
                    R = {frozenset(J): rho(sum(C[i] for i in J), sum(t[i] for i in J)) for J in SUB}
                    r = lambda *xs: R[frozenset(xs)]
                    for a, b, c, d in itertools.permutations(range(4)):
                        s7 = 2 * H - (r(a) + r(c, d) + r(b, d) + r(a, b, c))
                        u1 = r(d) + r(b, c, d) - r(c, d) - r(b, d)
                        u2 = r(c) + H - r(c, d) - r(a, b, c)
                        u3 = r(b) + H - r(b, d) - r(a, b, c)
                        st['rows'] += 1
                        st['s7<0'] += s7 < 0
                        for k, u in (('u1', u1), ('u2', u2), ('u3', u3)): st[k + '<0'] += u < 0
                        if max(u1, u2, u3) < 0:
                            st['all_neg'] += 1
                            if len(ex) < 4: ex.append((M, q, C, t, (a, b, c, d), s7, u1, u2, u3))
    print(dict(st)); print(ex)

if __name__ == '__main__':
    run(int(sys.argv[1]))
