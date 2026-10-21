"""CL491: can the prefix-plus-pair boundary be certified by THEOREMS rather than by search?

For a pair-least I2 instance, in the pair's lower frame, a PPP choice {x, y} is CERTIFIED if
  (P side)  t_X is in Sigma_a(P) (exact, P has m <= 8 values here: a finite, explicit check), and
  (complement) for some other bin Z with c = c_Z, k-sums of the complement W = S minus P (an interval minus x, y and
  possibly the hole: <= 3 internal deletions after trimming, |W| >= 7), the target t_Z has distance d >= 3 from both
  extremes of Sigma_c(W), and either d >= 5 (G340) or W's deletion pattern is not one of Lemma G3's (CL490)
  depth-3 patterns at that end (G3).
Then completion follows from G340 / G3 without searching W.  Prediction (written first): certified 100% at M = 12,
13.  Counterfactual: uncertified instances need the depth-1/2 theory (two-hole scalar lemma) or the exact
spectrum, i.e. lemma (a) needs one more ingredient.
OUTCOME.  First version (no |W| >= 7 gate): "certified" 8,274 / 8,274 and 59,688 / 59,688, but the unexpected check
against the actual spectrum found 12 FALSE certificates at M = 13: the gate was missing (G340/G3 need |W| >= 7).
With the gate (2.5 min): M = 12 certified 0 / 8,274 (every complement has 6 values); M = 13 29,844 / 59,688;
M = 14 184,098 / 253,356; false certificates 0 in 213,942.  Every uncertified instance has a 6-value complement,
the regime of the cores and of G339's 21-pool table.  Prediction (100% certified) FAILED; the residue is a finite
six-value table, not an unknown.
"""
import itertools, sys
from collections import Counter
T = lambda n: n * (n + 1) // 2
SUB = [J for s in (1, 2, 3) for J in itertools.combinations(range(4), s)]
PAIRS = list(itertools.combinations(range(4), 2))

def spectra(pool):
    sp = [set() for _ in range(len(pool) + 1)]; sp[0].add(0)
    for x in pool:
        for k in range(len(pool) - 1, -1, -1):
            if sp[k]: sp[k + 1] |= {s + x for s in sp[k]}
    return sp

def g3_bad(W, c, end):
    """is W (sorted, <= 3 internal deletions) in a Lemma G3 depth-3 pattern for c-sums at the given end?"""
    if end == 'hi':
        W = [W[-1] - v for v in reversed(W)]
    base = W[0]; Wn = [v - base for v in W]; N = Wn[-1]
    D = set(range(N + 1)) - set(Wn)
    n = len(Wn)
    for k in (c, n - c):
        pats = [{k, k + 1, k + 2}, {k - 1, k + 1, k + 3}, {k - 1, k, k + 4}, {k - 2, k + 2, k + 3}]
        if D in pats or (k == 3 and D == {4, 5, 6}): return True
    # complementation maps the low end of c-sums to the high end of (n-c)-sums: check the reflected pool too
    Wr = [N - v for v in reversed(Wn)]; Dr = set(range(N + 1)) - set(Wr)
    for k in (c, n - c):
        pats = [{k, k + 1, k + 2}, {k - 1, k + 1, k + 3}, {k - 1, k, k + 4}, {k - 2, k + 2, k + 3}]
        if Dr in pats or (k == 3 and Dr == {4, 5, 6}): return True
    return False

def run(M):
    cnt = Counter(); ex = []
    for C in itertools.product(range(3, M - 8), repeat=4):
        if sum(C) != M: continue
        CJ = {J: sum(C[i] for i in J) for J in SUB}
        for q in range(1, M):
            S = [x for x in range(M + 1) if x != q]; tot = sum(S); N = len(S)
            sp = spectra(S); mins = lambda c: sum(S[:c]); maxs = lambda c: sum(S[N - c:]); Rf = [M - x for x in reversed(S)]
            for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i]) + 1) for i in range(3)]):
                t = t3 + (tot - sum(t3),)
                tJ = {J: sum(t[i] for i in J) for J in SUB}
                if not all(tJ[J] in sp[CJ[J]] and tJ[J] - mins(CJ[J]) >= 2 and maxs(CJ[J]) - tJ[J] >= 2 for J in SUB): continue
                sl = sorted([(tJ[p] - mins(CJ[p]), 'lo', p) for p in PAIRS] + [(maxs(CJ[p]) - tJ[p], 'up', p) for p in PAIRS])
                sing = min(min(t[i] - mins(C[i]), maxs(C[i]) - t[i]) for i in range(4))
                if not sl[0][0] < sing: continue
                cnt['n'] += 1
                _, side, (X, Y) = sl[0]
                Z, tt = (S, t) if side == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                m = C[X] + C[Y]; pre = Z[:m - 2]; need = tt[X] + tt[Y] - sum(pre)
                cert = False; best = -1
                for x in Z[m - 2:]:
                    y = need - x
                    if y <= x or y not in Z or y in pre: continue
                    P = pre + [x, y]; spP = spectra(P)
                    if not (tt[X] in spP[C[X]] or tt[Y] in spP[C[Y]]): continue
                    W = [v for v in Z if v not in P]
                    if len(W) < 7: continue          # G340 and G3 need |W| >= 7 (the n = 6 cores are outside both)
                    # trim endpoint deletions: W is sorted; internal deletions = gaps inside [W0, W-1]
                    for zb in range(4):
                        if zb in (X, Y): continue
                        c = C[zb]; lo = sum(W[:c]); hi = sum(W[len(W) - c:])
                        d = min(tt[zb] - lo, hi - tt[zb]); best = max(best, d)
                        if d >= 5: cert = True; cnt['chk'] += 1; cnt['bad'] += tt[zb] not in spectra(W)[c]
                        elif d >= 3:
                            end = 'lo' if tt[zb] - lo <= hi - tt[zb] else 'hi'
                            if not g3_bad(W, c, end): cert = True; cnt['chk'] += 1; cnt['bad'] += tt[zb] not in spectra(W)[c]
                        if cert: break
                    if cert: break
                cnt['cert'] += cert
                if not cert:
                    cnt[('best', best)] += 1
                    if len(ex) < 4: ex.append((q, C, t, (X, Y), best))
    return cnt, ex

if __name__ == '__main__':
    for M in map(int, sys.argv[1:]):
        cnt, ex = run(M)
        print(M, 'pair-least', cnt['n'], 'certified by G340/G3', cnt['cert'], 'false certificates', cnt['bad'], 'uncertified by best margin', sorted((k[1], v) for k, v in cnt.items() if isinstance(k, tuple)), ex, flush=True)
