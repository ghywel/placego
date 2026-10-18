# Cloud, CL449: GPT's H2 (one hole, counts (2,b,c), b,c>=3, lower margin r on every proper group, conserved total)
# tested directly for M<=14, every hole q (endpoint and internal), every (b,c); and for each instance, WHICH legal pairs
# {i,u-i} for the size-2 bin complete to a partition, so that selector rules can be scored:
#   spread  = the legal pair with the smallest i (most spread), central = the legal pair with the largest i (closest to u/2),
#   any     = some legal pair completes.
import itertools, sys, time
sys.path.insert(0, 'tests/probes/cloud_reads')
from p0_residual import L, enum_targets, groups
def margin_ok(sizes, sums, mu):
    k = len(sizes)
    for mask in groups(k):
        r = sum(sizes[j] for j in range(k) if mask >> j & 1); s = sum(sums[j] for j in range(k) if mask >> j & 1)
        if s < L(r) + mu*r: return False
    return True
def spec(pool, r): return {sum(c) for c in itertools.combinations(pool, r)}
T0 = time.time()
tot = fail_end = fail_int = 0; rule = {'spread': 0, 'central': 0, 'any': 0}; fails = []
for M in range(8, 15):
    for q in range(0, M + 1):
        pool = [x for x in range(M + 1) if x != q]; n = len(pool)
        for b in range(3, n - 4):
            c = n - 2 - b
            if c < 3 or c < b: continue
            sizes = [2, b, c]
            for sums in enum_targets(pool, sizes, lambda s, u: margin_ok(s, u, 1)):
                u, tB, tC = sums; tot += 1
                pairs = [(i, u - i) for i in range(0, (u + 1) // 2) if i in pool and (u - i) in pool and i != u - i]
                works = []
                for (i, j) in pairs:
                    rest = [x for x in pool if x not in (i, j)]
                    if tB in spec(rest, b): works.append((i, j))
                if not works:
                    if q in (0, M): fail_end += 1
                    else: fail_int += 1; fails.append((M, q, sizes, tuple(sums), pairs))
                    continue
                rule['any'] += 1
                if pairs[0] in works: rule['spread'] += 1
                if pairs[-1] in works: rule['central'] += 1
    print(f"M={M}: cumulative H2 instances {tot}; failures endpoint-hole {fail_end}, internal-hole {fail_int}; "
          f"of solvable: spread pair works {rule['spread']}, central pair works {rule['central']}, any {rule['any']} ({time.time()-T0:.0f}s)", flush=True)
print("internal-hole failures (first 8):", fails[:8])
