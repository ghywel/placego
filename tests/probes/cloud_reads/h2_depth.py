# Cloud, CL450. Selector by depth: for each H2 instance choose the legal pair whose remainder spectrum holds t_B deepest
# inside [min_b(R), max_b(R)] (depth = min(t_B - min, max - t_B)); score it, and tabulate the best depth available.
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
T0 = time.time(); tot = 0; depth_ok = 0; best_depth = {}; shallow_fail = []; deep_fail = 0
for M in range(9, 15):
    for q in range(0, M + 1):
        pool = [x for x in range(M + 1) if x != q]; n = len(pool)
        for b in range(3, n - 4):
            c = n - 2 - b
            if c < 3 or c < b: continue
            for sums in enum_targets(pool, [2, b, c], lambda s, u: margin_ok(s, u, 1)):
                u, tB, tC = sums; tot += 1; cand = []
                for i in range(0, (u + 1) // 2):
                    j = u - i
                    if i == j or i not in pool or j not in pool: continue
                    R = [x for x in pool if x not in (i, j)]; lo = sum(R[:b]); hi = sum(R[-b:])
                    cand.append((min(tB - lo, hi - tB), (i, j), R))
                cand.sort(key=lambda z: -z[0]); d, pr, R = cand[0]
                best_depth[d] = best_depth.get(d, 0) + 1
                ok = tB in spec(R, b)
                if ok: depth_ok += 1
                else:
                    if d >= 5: deep_fail += 1
                    elif len(shallow_fail) < 6: shallow_fail.append((M, q, b, c, tuple(sums), pr, d))
    print(f"M<={M}: instances {tot}; deepest-pair rule succeeds {depth_ok}; best available depth distribution {dict(sorted(best_depth.items()))}; deepest-pair failures with depth>=5: {deep_fail} ({time.time()-T0:.0f}s)", flush=True)
print("deepest-pair failures at depth<=4 (first 6):", shallow_fail)
