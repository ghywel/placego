"""Cloud's machine checks for GPT's G340 and G341 (CL480): scalar gap depth after deletions.

G340: R = interval minus <= 3 values, n = |R| >= 7, r, t >= 3, r + t = n: every integer in [alpha_r + 5,
      beta_r - 5] is an r-sum.  Checked for every deletion pattern inside [0, N], N <= 17.
G341(a): D >= 4, R = [0, N] minus <= D internal values, N >= 4D + 1: every missing triple sum has depth
      <= 2D - 3.  Checked exhaustively for D = 4 (N = 17..22) and by random patterns for D = 5, 6 (N up to 40).
G341(b): r + t = |R|, max(r, t) >= 4D - 1: [alpha_r + 2D - 2, beta_r - 2D + 2] inside Sigma_r.  Checked for
      D = 4, r = 3..6, t >= 15, random patterns.
Also the two "cannot be dropped" claims: n = 6 with 3 deletions reaches depth 9; D = 3 with holes {4,5,6}
misses 7 at depth 4.
Prediction: 0 violations.  Counterfactual: a violation names the failing clause.

OUTCOME (13 s): G340 23,745 (pool, r) cases, 0 violations; G341(a) 37,266 cases, 0; G341(b) 29 random
cases, 0.  Controls: {0,1,2,6,7,8} misses 12 at depth 9; holes {4,5,6} miss 7 at depth 4.  Prediction held.
"""
import itertools, random, sys

def sig(R, k):
    s = set()
    for c in itertools.combinations(R, k): s.add(sum(c))
    return s

def depth_ok(R, r, margin):
    s = sig(R, r); a, b = min(s), max(s)
    return all(v in s for v in range(a + margin, b - margin + 1))

def g340(NMAX):
    bad = n = 0
    for N in range(6, NMAX + 1):
        for d in range(0, 4):
            for D in itertools.combinations(range(1, N), d):
                R = [x for x in range(N + 1) if x not in D]
                if len(R) < 7: continue
                for r in range(3, len(R) - 2):
                    n += 1
                    if not depth_ok(R, r, 5): bad += 1; print('G340 violation', N, D, r)
    return n, bad

def g341a(rnd):
    bad = n = 0
    for D in (4, 5, 6):
        for N in range(4 * D + 1, 4 * D + 20):
            pats = list(itertools.combinations(range(1, N), D)) if D == 4 and N <= 22 else \
                   [tuple(sorted(rnd.sample(range(1, N), D))) for _ in range(300)]
            for H in pats:
                R = [x for x in range(N + 1) if x not in H]; n += 1
                if not depth_ok(R, 3, 2 * D - 2): bad += 1; print('G341a violation', D, N, H)
    return n, bad

def g341b(rnd):
    bad = n = 0; D = 4
    for _ in range(400):
        t = rnd.randint(15, 20); r = rnd.randint(3, 6); N = r + t + D - 1 + rnd.randint(0, 3)
        H = sorted(rnd.sample(range(1, N), rnd.randint(0, D)))
        R = [x for x in range(N + 1) if x not in H]
        if len(R) != r + t: continue
        n += 1
        if not depth_ok(R, r, 2 * D - 2): bad += 1; print('G341b violation', r, t, N, H)
    return n, bad

if __name__ == '__main__':
    rnd = random.Random(11)
    print('G340 (N <= 17):', g340(17))
    print('G341(a):', g341a(rnd))
    print('G341(b) D=4:', g341b(rnd))
    R6 = [0, 1, 2, 6, 7, 8]; s = sig(R6, 3); print('n=6 core depth:', min(12 - min(s), max(s) - 12), '(12 missing:', 12 not in s, ')')
    R = [x for x in range(20) if x not in (4, 5, 6)]; s = sig(R, 3); print('D=3 holes 4,5,6: 7 missing', 7 not in s, 'depth', 7 - min(s))
