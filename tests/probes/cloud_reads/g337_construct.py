"""Cloud's machine check for GPT's G337 (CL478): run the construction on random instances.

Build: a transitive run R of n >= 12 vertices with colour counts r_i >= 3 (random colouring), a rainbow strong
component K (random strong tournament on r in {3,4,5} vertices, random distinct colours, * included or not),
K placed above or below R with offsets.  Then follow G337 steps 1-4: slack chain (check it IS a chain), the
chain ordering of K's ordinary vertices, the compensated run targets s', check every run cut h' >= 0 and the
upper cuts, and finally check by brute force that the corrected run targets ARE realised by a partition of R's
score interval with R's colour counts (the G316 step), so that the final colour totals and q are restored.
Prediction: 0 failures.  Counterfactual: a failing case names a step of G337 that is wrong.
"""
import itertools, random, sys
L = lambda n: n * (n - 1) // 2
COL = 'ABCD'

def strong_tournament(r, rnd):
    while True:
        A = {(u, v): 0 for u in range(r) for v in range(r) if u != v}
        for u in range(r):
            for v in range(u + 1, r):
                if rnd.random() < 0.5: A[(u, v)] = 1
                else: A[(v, u)] = 1
        # strong?
        reach = lambda s: _reach(A, r, s)
        if all(len(reach(s)) == r for s in range(r)): return A

def _reach(A, r, s):
    seen = {s}; st = [s]
    while st:
        u = st.pop()
        for v in range(r):
            if v != u and A[(u, v)] and v not in seen: seen.add(v); st.append(v)
    return seen

def partition_exists(vals, counts, sums):
    """is there a partition of vals into classes with given counts and sums? (4 classes, brute force)"""
    vals = sorted(vals); cols = [c for c in counts]
    def go(i, rc, rs, rest):
        if i == 4: return not rest
        for S in itertools.combinations(rest, rc[i]):
            if sum(S) == rs[i]:
                if go(i + 1, rc, rs, [x for x in rest if x not in S]): return True
        return False
    return go(0, [counts[c] for c in COL], [sums[c] for c in COL], vals)

def trial(rnd):
    n = rnd.randint(12, 16)
    while True:
        col = [rnd.choice(COL) for _ in range(n)]
        if all(col.count(c) >= 3 for c in COL): break
    r = rnd.choice([3, 4, 5]); star = (r == 5) or rnd.random() < 0.5   # G337: r = 5 only with * in K
    kcols = rnd.sample(list(COL), r - (1 if star else 0)) + (['*'] if star else [])
    rnd.shuffle(kcols)
    A = strong_tournament(r, rnd)
    d = [sum(A[(u, v)] for v in range(r) if v != u) for u in range(r)]      # internal scores
    # cyclic triangles in K
    tau = sum(1 for a, b, c in itertools.combinations(range(r), 3)
              if (A[(a, b)] and A[(b, c)] and A[(c, a)]) or (A[(b, a)] and A[(c, b)] and A[(a, c)]))
    a = rnd.randint(0, 6)                                   # run's global offset (vertices below R)
    # run scores a..a+n-1 ; colour sums
    s = {c: sum(a + i for i in range(n) if col[i] == c) for c in COL}
    rc = {c: col.count(c) for c in COL}
    # step 1: slacks and chain
    subsets = [frozenset(J) for k in range(1, 4) for J in itertools.combinations(COL, k)]
    h = {J: sum(s[c] for c in J) - a * sum(rc[c] for c in J) - L(sum(rc[c] for c in J)) for J in subsets}
    assert all(v >= 0 for v in h.values())
    chain = sorted([J for J in subsets if h[J] <= 4], key=len)
    for X, Y in itertools.combinations(chain, 2):
        if not (X <= Y or Y <= X): return 'chain-fail'
    # step 2/3: core internal data
    ordinary = [i for i in range(r) if kcols[i] != '*']
    b = d[kcols.index('*')] if star else None
    V = [x for x in range(r) if x != b] if star else list(range(r))
    # order ordinary vertices by first chain member containing their colour (others last)
    def rank(i):
        for k, J in enumerate(chain):
            if kcols[i] in J: return k
        return len(chain)
    order = sorted(ordinary, key=rank)
    P = {}; D = {}
    for idx, i in enumerate(order): P[kcols[i]] = V[idx]; D[kcols[i]] = d[i]
    # step 3 claim: for J in chain, P_J <= D_J
    for J in chain:
        if sum(P.get(c, 0) for c in J) > sum(D.get(c, 0) for c in J): return 'chain-order-fail'
    # step 2 claim: every ordinary subset overshoot <= 5
    for J in subsets:
        if sum(P.get(c, 0) for c in J) - sum(D.get(c, 0) for c in J) > 5: return 'overshoot-fail'
    # step 4: compensated run sums and all cuts
    s2 = {c: s[c] + D.get(c, 0) - P.get(c, 0) for c in COL}
    for J in subsets:
        rJ = sum(rc[c] for c in J); sJ = sum(s2[c] for c in J)
        if sJ < a * rJ + L(rJ): return 'lower-cut-fail'
        if sJ > a * rJ + (rJ * (2 * n - rJ - 1)) // 2: return 'upper-cut-fail'
    if sum(s2.values()) != sum(s.values()): return 'total-fail'
    # G316 step: brute-force realisation of s2 on the run's interval
    if not partition_exists(list(range(a, a + n)), rc, s2): return 'G316-fail'
    return 'ok', tau

if __name__ == '__main__':
    rnd = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
    from collections import Counter
    res = Counter(); gains = 0
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    for _ in range(N):
        out = trial(rnd)
        if isinstance(out, tuple): res['ok'] += 1; gains += 2 * out[1]
        else: res[out] += 1
    print(dict(res), 'total Phi gain', gains)
