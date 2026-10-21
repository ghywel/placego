"""CL501: read the two-hole selector's 694 misses (M = 13, 3333, REPAIR_SHIFTS = (1, 2)).
For each miss: (i) canonical singleton with displacement up to 3; (ii) CL486's cascade: any singleton recipe in
either frame, then any pair boundary; (iii) a two-value pivot: l smallest + k largest + ANY two further values
(l + k = c - 2), for any singleton; residuals are printed with a witness partition.
Prediction (written first): (i) < 300 left; (ii) clears every miss without repeated (size, target).
Counterfactual: non-repeat residuals mean two holes needs a construction beyond the one-pivot family.

OUTCOME (CL501, 2 min): all 694 complete: displacement-3 canonical 12; another singleton recipe (either frame,
shifts <= 3) 596; another pair boundary 84; a two-value pivot 2; residual 0.  (i) failed (682 left after d3);
(ii) held, and more: the cascade clears every miss, repeated targets included.
"""
import itertools, sys
from collections import Counter
_a = sys.argv; sys.argv = ['x']
exec(open('tests/probes/cloud_reads/twohole_selector.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
sys.argv = _a
src_run = run

def frames(S, t, C, M):
    Rf = [M - x for x in reversed(S)]
    return {'lo': (S, t), 'up': (Rf, tuple(C[i] * M - t[i] for i in range(4)))}

def single_ok(Z, t1, C, A, shifts):
    global REPAIR_SHIFTS
    old = REPAIR_SHIFTS; REPAIR_SHIFTS = shifts
    try:
        oth = [i for i in range(4) if i != A]
        for Aset in recipes(Z, C[A], t1[A], None):
            rem = tuple(x for x in Z if x not in Aset)
            if (t1[oth[0]], t1[oth[1]]) in three_bin(rem, tuple(C[i] for i in oth)): return True
        return False
    finally:
        REPAIR_SHIFTS = old

def two_pivot_ok(Z, t1, C, A):
    a = C[A]; N = len(Z); oth = [i for i in range(4) if i != A]
    for k in range(0, a - 1):
        l = a - 2 - k; low = list(Z[:l]); high = list(Z[N - k:]) if k else []
        mid = Z[l:N - k]; need = t1[A] - sum(low) - sum(high)
        for x, y in itertools.combinations(mid, 2):
            if x + y == need:
                rem = tuple(z for z in Z if z not in low + high + [x, y])
                if (t1[oth[0]], t1[oth[1]]) in three_bin(rem, tuple(C[i] for i in oth)): return True
    return False

def misses(M, C):
    out = []
    CJ = {J: sum(C[i] for i in J) for J in SUB}
    for q1 in range(1, M):
        for q2 in range(q1 + 1, M):
            S = [x for x in range(M + 1) if x not in (q1, q2)]; tot = sum(S); N = len(S)
            if N != sum(C): continue
            sp = spectra(S); F = feas_set(S, C); mins = lambda c: sum(S[:c]); maxs = lambda c: sum(S[N - c:])
            fr0 = None
            for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i]) + 1) for i in range(3)]):
                t = t3 + (tot - sum(t3),)
                tJ = {J: sum(t[i] for i in J) for J in SUB}
                if not all(tJ[J] in sp[CJ[J]] and tJ[J] - mins(CJ[J]) >= 2 and maxs(CJ[J]) - tJ[J] >= 2 for J in SUB): continue
                if t3 not in F: continue
                fr = frames(S, t, C, M)
                sl = sorted([(tJ[p] - mins(CJ[p]), 'lo', p) for p in PAIRS] + [(maxs(CJ[p]) - tJ[p], 'up', p) for p in PAIRS])
                ss = sorted([(t[i] - mins(C[i]), 'lo', i) for i in range(4)] + [(maxs(C[i]) - t[i], 'up', i) for i in range(4)])
                _, side, (X, Y) = sl[0]
                if pair_boundary_ok(fr[side][0], C, fr[side][1], X, Y, M, N, None): continue
                _, s1, A = ss[0]
                if single_ok(fr[s1][0], fr[s1][1], C, A, (1, 2)): continue
                out.append(((q1, q2), t, S, fr, sl, ss))
    return out

if __name__ == '__main__':
    M, C = 13, (3, 3, 3, 3)
    ms = misses(M, C); cnt = Counter(); resid = []
    for (h, t, S, fr, sl, ss) in ms:
        rep = any(t[i] == t[j] and C[i] == C[j] for i in range(4) for j in range(i + 1, 4))
        cnt['miss'] += 1; cnt['repeat'] += rep
        _, s1, A = ss[0]
        if single_ok(fr[s1][0], fr[s1][1], C, A, (1, 2, 3)): cnt['d3'] += 1; continue
        if any(single_ok(fr[s][0], fr[s][1], C, B, (1, 2, 3)) for _, s, B in ss[1:]): cnt['other_single'] += 1; continue
        if any(pair_boundary_ok(fr[s][0], C, fr[s][1], X, Y, M, len(S), None) for _, s, (X, Y) in sl[1:]): cnt['other_pair'] += 1; continue
        if any(two_pivot_ok(fr[s][0], fr[s][1], C, B) for _, s, B in ss): cnt['two_pivot'] += 1; continue
        cnt['resid'] += 1; cnt['resid_repeat'] += rep; resid.append((h, t, rep))
    print(dict(cnt))
    print('residual by hole pair:', sorted(Counter(h for h, t, r in resid).items()))
    print('residual examples:', resid[:12], flush=True)
