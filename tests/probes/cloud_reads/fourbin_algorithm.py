# End-to-end machine implementation of GPT's four-bin construction (MI338 + MI339 + MI337 via search), tested against
# EVERY SS-feasible four-bin instance with sizes >= 3 on n <= 14. Checks the construction's steps, not the prose.
import itertools, sys, time
sys.path.insert(0, '.')
from fourbin_lemmas import staircase, L, spectrum, exists3
def U(N, r): return r*(2*N - r - 1)//2
def subset_with_sum(P, r, s):
    for c in itertools.combinations(sorted(P), r):
        if sum(c) == s: return set(c)
    return None
def solve(N, sizes, targets):
    """returns (branch, partition) or (branch, None) on a construction failure"""
    k = 4; idx = range(k)
    cuts = []
    for mask in range(1, (1 << k) - 1):
        I = [i for i in idx if mask >> i & 1]; C = sum(sizes[i] for i in I); S = sum(targets[i] for i in I)
        cuts.append((S - L(C), mask))
    h = min(c[0] for c in cuts)
    attaining = [m for (v, m) in cuts if v == h]
    # ties: any singleton or triple attaining h goes to the singleton branch (MI343 section 3)
    st = [m for m in attaining if bin(m).count('1') in (1, 3)]
    mask = st[0] if st else attaining[0]
    I = [i for i in idx if mask >> i & 1]
    if len(I) in (1, 3):
        # singleton branch: reflect so that a singleton has lower slack h
        if len(I) == 3:   # lower slack of a triple = upper slack of the singleton complement: reflect
            A = [i for i in idx if i not in I][0]
            tgt = [(N - 1)*sizes[i] - targets[i] for i in idx]; refl = True
        else:
            A = I[0]; tgt = list(targets); refl = False
        a = sizes[A]; sA = tgt[A]; others = [i for i in idx if i != A]
        for l in range(0, a):
            kk = a - 1 - l
            lowsum = L(l); highsum = sum(range(N - kk, N))
            p = sA - lowsum - highsum
            if not (l <= p < N - kk): continue
            Aset = set(range(l)) | {p} | set(range(N - kk, N)); assert len(Aset) == a
            R = [x for x in range(N) if x not in Aset]
            # residual individual feasibility (MI338's claim) then completion (MI337's statement, verified separately)
            if all(tgt[i] in spectrum(R, sizes[i]) for i in others):
                part = exists3_parts(R, [sizes[i] for i in others], [tgt[i] for i in others])
                if part is None: return ("singleton-nocompletion", None)
                bins = {A: Aset}; 
                for i, bset in zip(others, part): bins[i] = bset
                if refl: bins = {i: {N - 1 - x for x in b} for i, b in bins.items()}
                return ("singleton", bins)
        return ("singleton-noA", None)
    # strict pair branch: I is the pair with least lower slack h
    A, B = I; C, D = [i for i in idx if i not in I]
    a, b, c, d = sizes[A], sizes[B], sizes[C], sizes[D]; m = a + b
    x = targets[A] - L(a); z = U(N, c) - targets[C]
    if not (h < x < a*b and h < z < c*d): return ("pair-bounds", None)
    P0 = staircase(m, h)
    if max(P0) > N - 1 or sum(P0) != L(m) + h: return ("pair-pool", None)
    Aset = subset_with_sum(P0, a, L(a) + x)
    if Aset is None: return ("pair-Aspectrum", None)
    Bset = set(P0) - Aset
    Q = [v for v in range(N) if v not in set(P0)]; Qr = [N - 1 - v for v in Q]
    Cr = subset_with_sum(Qr, c, L(c) + z)
    if Cr is None: return ("pair-Cspectrum", None)
    Cset = {N - 1 - v for v in Cr}; Dset = set(Q) - Cset
    return ("pair", {A: Aset, B: Bset, C: Cset, D: Dset})
def exists3_parts(P, sizes, targets):
    P = sorted(P); rem_c = list(sizes); rem_s = list(targets); assign = {}
    def rec(i):
        if i == len(P): return all(v == 0 for v in rem_c)
        xv = P[i]; tried = set()
        for b in range(3):
            key = (rem_c[b], rem_s[b])
            if rem_c[b] == 0 or rem_s[b] < xv or key in tried: continue
            tried.add(key); rem_c[b] -= 1; rem_s[b] -= xv; assign[xv] = b
            if rec(i + 1): return True
            rem_c[b] += 1; rem_s[b] += xv
        return False
    if not rec(0): return None
    return [{v for v, b in assign.items() if b == j} for j in range(3)]
def SS(N, sizes, sums):
    for mask in range(1, (1 << 4) - 1):
        C = sum(sizes[j] for j in range(4) if mask >> j & 1); S = sum(sums[j] for j in range(4) if mask >> j & 1)
        if not (L(C) <= S <= U(N, C)): return False
    return True
t0 = time.time()
from collections import Counter
for N in range(12, 15):
    T = L(N); br = Counter(); fails = []
    for sizes in itertools.combinations_with_replacement(range(3, N), 4):
        if sum(sizes) != N: continue
        for sums in itertools.product(*[range(L(c), U(N, c) + 1) for c in sizes]):
            if sum(sums) != T or not SS(N, sizes, sums): continue
            branch, bins = solve(N, list(sizes), list(sums))
            if bins is None: fails.append((sizes, sums, branch)); br[branch] += 1; continue
            # verify the partition
            allv = sorted(v for b in bins.values() for v in b)
            ok = allv == list(range(N)) and all(len(bins[i]) == sizes[i] and sum(bins[i]) == sums[i] for i in range(4))
            if not ok: fails.append((sizes, sums, branch + "-BAD")); br[branch + "-BAD"] += 1
            else: br[branch] += 1
    print(f"N={N}: {dict(br)}; construction failures {len(fails)} {fails[:4]} ({time.time()-t0:.0f}s)", flush=True)
