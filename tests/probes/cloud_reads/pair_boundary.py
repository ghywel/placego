"""CL480: can the one-hole four-bin problem be solved by a pair boundary with a bounded hole budget?

Instance: pool S = [0, M] minus q, sizes >= 3, targets in I2 (all 14 group targets in their spectra, every
margin >= 2).  For a pair {X, Y} a BOUNDARY is a set P of size c_X + c_Y and sum t_X + t_Y; it completes the
instance iff t_X in Sigma_(c_X)(P) and t_Z in Sigma_(c_Z)(S \ P) for one of the other bins Z (two scalar
choices on disjoint sides).  Family tested: P = a bottom block of S (the first c_X + c_Y + e available values
with e <= 2 of them skipped) or the mirror top block.  Both P and S \ P then carry at most 2 skips plus the
hole: a bounded deletion budget on both sides.
Question: does such a P exist (i) for the least-slack pair, (ii) for some pair?
Predictions (written first): (ii) in every instance, M = 12..14; (i) fails in a few percent (the least pair
is not always the right boundary).  Counterfactual: (ii) failing would mean a bounded-budget boundary is not a
universal selector and another representation really is needed.

OUTCOME (M = 12, 5 s): 122,977 I2 instances; least pair completed by a block boundary in 83,406; SOME pair
in 95,022 (77%).  Prediction (ii) FAILED: a bottom/top block with <= 2 skips is the wrong family.  First miss:
q = 1, 3333, (8,20,20,29), whose solution has A u B = {0,2,3,5,6,12}.  Superseded by staircase_boundary.py.
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

def run(M):
    n = 0; ok_least = ok_any = 0; ex = []; which = Counter()
    for C in itertools.product(range(3, M - 8), repeat=4):
        if sum(C) != M: continue
        CJ = {J: sum(C[i] for i in J) for J in SUB}
        for q in range(1, M):
            S = [x for x in range(M + 1) if x != q]; tot = sum(S); N = len(S)
            sp = spectra(S); mins = lambda c: sum(S[:c]); maxs = lambda c: sum(S[N - c:])
            # candidate boundaries by size m: bottom blocks (first m+e ranks minus e skips) and top blocks
            cand = {}
            for m in {C[i] + C[j] for i, j in PAIRS}:
                lst = []
                for e in range(0, 3):
                    for skips in itertools.combinations(range(1, m + e), e):      # never skip rank 0
                        P = [S[r] for r in range(m + e) if r not in skips]
                        lst.append(('bot', P))
                        Pt = [S[N - 1 - r] for r in range(m + e) if r not in skips]
                        lst.append(('top', sorted(Pt)))
                seen = set(); uniq = []
                for tag, P in lst:
                    key = tuple(P)
                    if key in seen: continue
                    seen.add(key); R = [x for x in S if x not in key]
                    uniq.append((tag, key, sum(key), spectra(list(key)), spectra(R)))
                cand[m] = uniq
            for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i]) + 1) for i in range(3)]):
                t = t3 + (tot - sum(t3),)
                tJ = {J: sum(t[i] for i in J) for J in SUB}
                if not all(tJ[J] in sp[CJ[J]] and tJ[J] - mins(CJ[J]) >= 2 and maxs(CJ[J]) - tJ[J] >= 2 for J in SUB): continue
                n += 1
                slack = {(i, j): min(tJ[(i, j)] - mins(CJ[(i, j)]), maxs(CJ[(i, j)]) - tJ[(i, j)]) for i, j in PAIRS}
                least = min(PAIRS, key=lambda p: slack[p])
                found_any = False; found_least = False
                for (i, j) in sorted(PAIRS, key=lambda p: slack[p]):
                    k, l = [z for z in range(4) if z not in (i, j)]
                    hit = False
                    for tag, P, sP, spP, spR in cand[C[i] + C[j]]:
                        if sP != tJ[(i, j)]: continue
                        if t[i] in spP[C[i]] and t[k] in spR[C[k]]: hit = True; break
                    if hit:
                        found_any = True
                        if (i, j) == least: found_least = True
                        which[tag] += 1
                        break
                ok_any += found_any; ok_least += found_least
                if not found_any and len(ex) < 5: ex.append((q, C, t))
    return dict(instances=n, least_pair_ok=ok_least, some_pair_ok=ok_any, examples_no_boundary=ex)

if __name__ == '__main__':
    for M in map(int, sys.argv[1:]):
        print(M, run(M), flush=True)
