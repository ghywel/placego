# Cloud's independent check of MI175 (B77): moves (p, q, -2d_1..-2d_N), p,q odd positive, on positions 0..M-1 with folded
# labels min(x, M-1-x). Criterion: a folded-distinct cyclic placement exists iff max(p,q) <= M-3 and the d's split into
# two groups of sum <= M/2 - 1, when gcd(d) >= 2. Exhaustive truth via the two-run structure (every cyclic order is
# p, run A, q, run B up to rotation), all orders within runs, all roots.
import itertools, math, time, collections
def label(x, M): return min(x, M - 1 - x)
def exists_cycle(M, p, q, d):
    N = len(d); idx = range(N)
    for mask in range(1 << N):
        A = [d[i] for i in idx if mask >> i & 1]; B = [d[i] for i in idx if not mask >> i & 1]
        for pa in set(itertools.permutations(A)):
            for pb in set(itertools.permutations(B)):
                verts = [0, p]; s = p
                for x in pa: s -= 2*x; verts.append(s)
                s += q; verts.append(s)
                for x in pb[:-1] if pb else []: s -= 2*x; verts.append(s)
                # verts has N+2 entries (closing vertex omitted); check all roots
                lo, hi = min(verts), max(verts)
                for h in range(-lo, M - hi):
                    P = [v + h for v in verts]
                    if len({label(x, M) for x in P}) == N + 2: return True
    return False
def criterion(M, p, q, d):
    n = M // 2; K = sum(d)
    if max(p, q) > M - 3: return False
    return any(K - (n - 1) <= sum(d[i] for i in range(len(d)) if m >> i & 1) <= n - 1 for m in range(1 << len(d)))
def construct(M, p, q, d):
    """MI175's rule: any feasible split, any order, root L or L+1 avoiding H mod g. Returns vertex positions."""
    n = M // 2; K = sum(d); g = math.gcd(*d)
    for m in range(1 << len(d)):
        A = [d[i] for i in range(len(d)) if m >> i & 1]; B = [d[i] for i in range(len(d)) if not m >> i & 1]
        s, t = sum(A), sum(B)
        if not (s <= n - 1 and t <= n - 1): continue
        w = p - 2*s; L = max(0, -w); R = min(M - 1 - p, M - 1 - 2*t); assert R >= L + 1
        H = (M - 1 - w) // 2; assert (M - 1 - w) % 2 == 0
        h = L if (L - H) % g else L + 1
        verts = [h, h + p]; x = h + p
        for a in A: x -= 2*a; verts.append(x)
        x += q; verts.append(x)
        for b in B[:-1]: x -= 2*b; verts.append(x)
        assert all(0 <= v <= M - 1 for v in verts) and len({label(v, M) for v in verts}) == len(verts), (M, p, q, d, verts)
        return verts
    return None
# (1) small windows, all N <= 4, exhaustive truth vs criterion, gcd >= 2
t0 = time.time(); agree = 0; cases = 0; mism = []
for M in (6, 8, 10, 12, 14, 16):
    n = M // 2
    for N in range(1, 5):
        for d in itertools.combinations_with_replacement(range(1, n), N):
            if math.gcd(*d) < 2: continue
            K = sum(d)
            for p in range(1, 2*K, 2):
                q = 2*K - p
                if q < p or q > M + 2: continue
                cases += 1
                truth = exists_cycle(M, p, q, list(d)); crit = criterion(M, p, q, d)
                if truth == crit:
                    agree += 1
                    if crit: construct(M, p, q, list(d))
                else: mism.append((M, p, q, d, truth, crit))
print(f"small windows M=6..16, gcd>=2: {cases} questions, criterion agrees with exhaustive truth on {agree}, mismatches {mism[:5]}  ({time.time()-t0:.1f}s)")
# (2) GPT's M=28 domain: N 1..6, sorted d in 1..11, K 14..25, gcd>=2, odd p<=q<=25, p+q=2K; construct or refuse by capacity
M = 28; n = 14; con = ref = 0; refusals = []
for N in range(1, 7):
    for d in itertools.combinations_with_replacement(range(1, 12), N):
        K = sum(d)
        if not (14 <= K <= 25) or math.gcd(*d) < 2: continue
        for p in range(1, 26, 2):
            q = 2*K - p
            if q < p or q > 25: continue
            if criterion(M, p, q, d): construct(M, p, q, list(d)); con += 1
            else: ref += 1; refusals.append((p, q, d))
print("M=28 gcd>=2 domain: constructions", con, "capacity refusals", ref)
# confirm the refusals are genuine by exhaustive search (N <= 6)
bad = [r for r in refusals if exists_cycle(M, r[0], r[1], list(r[2]))]
print("refusals contradicted by exhaustive search:", bad)
