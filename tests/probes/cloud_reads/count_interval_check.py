"""CL472 bounded test: four-bin count selection as an interval system on subset counts.

Setting: tokens S = [0, M] minus a hole q, low row 0..q-1, high row q+1..M, four bins with
counts C (sum M) and targets t (sum = sum S).  For a high-count vector k and group J,
  f_J(k_J) = L(C_J-k_J) + (q+1)k_J + L(k_J)          (least sum, convex in k_J)
  g_J(k_J) = (C_J-k_J)(q-1) - L(C_J-k_J) + k_J*M - L(k_J)   (greatest sum, concave in k_J)
so {k_J : f_J <= t_J <= g_J} is an integer interval I_J.  P(t) = {k : sum k = |high|,
0 <= k <= C, C-k <= ... , k(J) in I_J for all 14 proper J}.

Predictions (written before the run).  (A) partition => P(t) nonempty, 0 exceptions (trivial
direction).  (B) P(t) nonempty and no partition happens only with a row of a bin of size <= 2
(the inherited thin-row exceptions).  (C) the symmetrised interval ends are NOT always
super/submodular: some failures.  Counterfactual: any (A) failure means the interval
reformulation is wrong; a (B) failure with all per-side counts >= 3 means CL446's split step
does not carry over.

OUTCOME (M = 6..8, every q, all full-cut instances, 376,739): (A) 0.  (B) 32,708, all with a
per-side count <= 2 (vacuous at M <= 8, where no k makes all eight sides >= 3).  (C) 201,904
failures of super/submodularity among P(t) nonempty.  Gap scan (`gap 6 7 8`): integer-empty 99,840,
rational-nonempty 6, all permutations of q=4, counts 2222, targets 5/5/11/11 (k = 1/2,1/2,3/2,3/2).
Protected instances: 79, all with P(t) nonempty.
"""
import itertools, sys
import numpy as np

L = lambda n: n * (n - 1) // 2
SUBSETS = [J for r in range(1, 4) for J in itertools.combinations(range(4), r)]

def achievable(M, q):
    toks = np.array([x for x in range(M + 1) if x != q])
    n = len(toks)
    out = set()
    for chunk in range(0, 4 ** n, 1 << 20):
        idx = np.arange(chunk, min(4 ** n, chunk + (1 << 20)))
        lab = (idx[:, None] // (4 ** np.arange(n))[None, :]) % 4
        cs = np.stack([(lab == b).sum(1) for b in range(4)], 1)
        ss = np.stack([((lab == b) * toks).sum(1) for b in range(4)], 1)
        hs = np.stack([((lab == b) * (toks > q)).sum(1) for b in range(4)], 1)
        for row in np.concatenate([cs, ss, hs], 1).tolist():
            out.add(tuple(row))
    return out

def run(M):
    stats = dict(inst=0, A=0, B=0, B_thick=0, C_bad=0, P_empty_protected=0, protected=0)
    for q in range(1, M):
        S = [x for x in range(M + 1) if x != q]
        H = M - q
        ach = achievable(M, q)
        part = {r[:8] for r in ach}
        ks_of = {}
        for r in ach:
            ks_of.setdefault(r[:8], set()).add(r[8:])
        srt = sorted(S)
        mins = lambda c: sum(srt[:c]); maxs = lambda c: sum(srt[len(srt) - c:])
        for C in itertools.product(range(1, M + 1), repeat=4):
            if sum(C) != M: continue
            ranges = [range(mins(c), maxs(c) + 1) for c in C[:3]]
            for t3 in itertools.product(*ranges):
                t = t3 + (sum(S) - sum(t3),)
                ok = all(mins(sum(C[i] for i in J)) <= sum(t[i] for i in J) <= maxs(sum(C[i] for i in J))
                         for J in SUBSETS)
                if not ok: continue
                stats['inst'] += 1
                prot = all(mins(cJ) + cJ <= tJ <= maxs(cJ) - cJ for J in SUBSETS
                           for cJ, tJ in [(sum(C[i] for i in J), sum(t[i] for i in J))])
                def ok_k(k):
                    for J in SUBSETS + [(0, 1, 2, 3)]:
                        cJ = sum(C[i] for i in J); kJ = sum(k[i] for i in J); tJ = sum(t[i] for i in J)
                        if cJ - kJ > q or kJ > H: return False
                        f = L(cJ - kJ) + (q + 1) * kJ + L(kJ)
                        g = (cJ - kJ) * (q - 1) - L(cJ - kJ) + kJ * M - L(kJ)
                        if not f <= tJ <= g: return False
                    return True
                Pk = [k for k in itertools.product(*[range(c + 1) for c in C]) if sum(k) == H and ok_k(k)]
                inP = bool(Pk)
                key = C + t
                if key in part and not inP: stats['A'] += 1
                if inP and key not in part:
                    stats['B'] += 1
                    if any(min(k[i], C[i] - k[i]) >= 3 for k in Pk for i in range(1)) and \
                       any(all(min(k[i], C[i] - k[i]) >= 3 for i in range(4)) for k in Pk):
                        stats['B_thick'] += 1
                if prot:
                    stats['protected'] += 1
                    if not inP: stats['P_empty_protected'] += 1
                # (C) symmetrised interval ends from per-J intervals (k(J) range allowed by J alone)
                lo, hi = {}, {}
                for J in SUBSETS:
                    cJ = sum(C[i] for i in J); tJ = sum(t[i] for i in J)
                    vals = [kJ for kJ in range(0, min(cJ, H) + 1) if cJ - kJ <= q and
                            L(cJ - kJ) + (q + 1) * kJ + L(kJ) <= tJ <= (cJ - kJ) * (q - 1) - L(cJ - kJ) + kJ * M - L(kJ)]
                    lo[J], hi[J] = (min(vals), max(vals)) if vals else (H + 1, -1)
                full = (0, 1, 2, 3)
                lo[()] = hi[()] = 0; lo[full] = hi[full] = H
                cm = lambda J: tuple(i for i in range(4) if i not in J)
                lo2 = {J: max(lo[J], H - hi[cm(J)]) for J in lo}
                hi2 = {J: min(hi[J], H - lo[cm(J)]) for J in lo}
                sub = list(lo2)
                good = all(lo2[tuple(sorted(set(X) | set(Y)))] + lo2[tuple(sorted(set(X) & set(Y)))] >= lo2[X] + lo2[Y]
                           and hi2[tuple(sorted(set(X) | set(Y)))] + hi2[tuple(sorted(set(X) & set(Y)))] <= hi2[X] + hi2[Y]
                           for X in sub for Y in sub)
                if inP and not good: stats['C_bad'] += 1
    return stats

if __name__ == "__main__" and sys.argv[1] != "gap":
    for M in map(int, sys.argv[1:]):
        print(M, run(M), flush=True)

def gap_scan(M):
    """Cut-feasible instances with P(t) integer-empty: is the rational polytope also empty?
    Vertices of {x(J) in [lo_J, hi_J]} (k4 eliminated, 3x3 minors in {-1,0,1} have |det| <= 4)
    lie on the 1/12 grid, so a 1/12-grid scan decides rational feasibility exactly."""
    gaps = empties = 0
    examples = []
    for q in range(1, M):
        S = sorted(x for x in range(M + 1) if x != q); H = M - q
        mins = lambda c: sum(S[:c]); maxs = lambda c: sum(S[len(S) - c:])
        for C in itertools.product(range(1, M + 1), repeat=4):
            if sum(C) != M: continue
            for t3 in itertools.product(*[range(mins(c), maxs(c) + 1) for c in C[:3]]):
                t = t3 + (sum(S) - sum(t3),)
                if not all(mins(sum(C[i] for i in J)) <= sum(t[i] for i in J) <= maxs(sum(C[i] for i in J)) for J in SUBSETS):
                    continue
                iv = {}
                for J in SUBSETS:
                    cJ = sum(C[i] for i in J); tJ = sum(t[i] for i in J)
                    vals = [kJ for kJ in range(0, min(cJ, H) + 1) if cJ - kJ <= q and
                            L(cJ - kJ) + (q + 1) * kJ + L(kJ) <= tJ <= (cJ - kJ) * (q - 1) - L(cJ - kJ) + kJ * M - L(kJ)]
                    iv[J] = (min(vals), max(vals)) if vals else None
                if any(v is None for v in iv.values()):
                    empties += 1; continue
                ints = [k for k in itertools.product(*[range(c + 1) for c in C]) if sum(k) == H and
                        all(iv[J][0] <= sum(k[i] for i in J) <= iv[J][1] for J in SUBSETS)]
                if ints: continue
                empties += 1
                g = [np.arange(0, 12 * C[i] + 1) for i in range(3)]
                a, b, c = np.meshgrid(*g, indexing='ij')
                d = 12 * H - a - b - c
                X = [a, b, c, d]
                m = (d >= 0) & (d <= 12 * C[3])
                for J in SUBSETS:
                    s = sum(X[i] for i in J)
                    m &= (s >= 12 * iv[J][0]) & (s <= 12 * iv[J][1])
                if m.any():
                    gaps += 1
                    if len(examples) < 3: examples.append((M, q, C, t))
    return dict(int_empty=empties, rational_nonempty=gaps, examples=examples)
if __name__ == '__main__' and sys.argv[1] == 'gap':
    for M in map(int, sys.argv[2:]):
        print('gap', M, gap_scan(M), flush=True)
