"""CL474 perspective instrument: real admission as a core (Bondareva-Shapley) question.

For a protected four-bin instance let rho_J = least admissible high count of group J (the lower end
of K(C_J, t_J)).  Because K(complement) = H - K exactly, P(t) is the core of the game v(J) = rho_J,
v(V) = H, so P(t) is nonempty iff  sum_J lam_J rho_J <= H  for every MINIMAL balanced collection
(Bondareva 1963, Shapley 1967).  This enumerates the minimal balanced collections on four labels
(independent incidence vectors with a positive solution to sum lam_J 1_J = 1), groups them by
symmetry type, and over every protected instance with all sizes >= 3, M = 12..MMAX, records each
type's least slack H - sum lam rho.
Prediction: every slack >= 0 (P nonempty, as G334's I3 run found); the partition types are
the only ones ever tight.  Counterfactual: a tight non-partition type is the one a proof must face.

OUTCOME (M = 12..13, 565,503 instances, 4m39s): 41 minimal balanced collections in 9 types. No slack
is negative. Every type is tight somewhere except {1, 23, 24, 34} at weights 1, 1/2, 1/2, 1/2 (least
slack 1/2). The partition-only prediction FAILED: the four non-partition types with weights 1/2 or
1/3 are each tight in 28,292 to 81,850 instances.
"""
import itertools, sys
from fractions import Fraction as F

L = lambda n: n * (n - 1) // 2
T = lambda n: n * (n + 1) // 2
SUB = [J for s in (1, 2, 3) for J in itertools.combinations(range(4), s)]

def solve(cols):
    """Solve sum lam_j * cols_j = 1-vector exactly; return lam if unique, else None."""
    n = len(cols); A = [[F(cols[j][i]) for j in range(n)] + [F(1)] for i in range(4)]
    r = 0; piv = []
    for c in range(n):
        p = next((i for i in range(r, 4) if A[i][c] != 0), None)
        if p is None: return None
        A[r], A[p] = A[p], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(4):
            if i != r and A[i][c] != 0: A[i] = [a - A[i][c] * b for a, b in zip(A[i], A[r])]
        piv.append(c); r += 1
    if any(A[i][n] != 0 for i in range(r, 4)): return None
    return [A[i][n] for i in range(n)]

def minimal_balanced():
    out = []
    for n in range(2, 5):
        for coll in itertools.combinations(SUB, n):
            lam = solve([[1 if i in J else 0 for i in range(4)] for J in coll])
            if lam and all(x > 0 for x in lam): out.append((coll, lam))
    return out

def canon(coll, lam):
    best = None
    for p in itertools.permutations(range(4)):
        key = tuple(sorted((tuple(sorted(p[i] for i in J)), l) for J, l in zip(coll, lam)))
        best = key if best is None or key < best else best
    return best

def run(MMAX):
    MB = minimal_balanced()
    types = {}
    for coll, lam in MB: types.setdefault(canon(coll, lam), []).append((coll, lam))
    slack = {k: None for k in types}; tight = {k: 0 for k in types}; n = 0
    for M in range(12, MMAX + 1):
        for C in itertools.product(range(3, M), repeat=4):
            if sum(C) != M: continue
            for q in range(1, M):
                H = M - q; S = T(M) - q
                memo = {}
                def rho(c, t):
                    if (c, t) not in memo:
                        v = [r for r in range(max(0, c - q), min(c, H) + 1)
                             if L(c - r) + (q + 1) * r + L(r) <= t <= (c - r) * (q - 1) - L(c - r) + M * r - L(r)]
                        memo[(c, t)] = min(v) if v else None
                    return memo[(c, t)]
                CJ = {J: sum(C[i] for i in J) for J in SUB}
                for t3 in itertools.product(*[range(T(C[i]), S - T(M - C[i]) + 1) for i in range(3)]):
                    t = t3 + (S - sum(t3),)
                    tJ = {J: sum(t[i] for i in J) for J in SUB}
                    if not all(tJ[J] >= T(CJ[J]) for J in SUB): continue
                    n += 1
                    rh = {J: rho(CJ[J], tJ[J]) for J in SUB}
                    for k, members in types.items():
                        s = min(H - sum(l * rh[J] for J, l in zip(coll, lam)) for coll, lam in members)
                        if slack[k] is None or s < slack[k]: slack[k] = s
                        if s == 0: tight[k] += 1
    print('instances', n, 'minimal balanced collections', len(MB), 'types', len(types))
    for k in sorted(types, key=lambda k: (len(k), k)):
        desc = ' '.join(''.join(str(i + 1) for i in J) + ('' if l == 1 else '@' + str(l)) for J, l in k)
        print(f'{desc:40s} least slack {slack[k]}  tight in {tight[k]}')

if __name__ == '__main__':
    run(int(sys.argv[1]))
