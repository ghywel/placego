# Cloud, CL450. After GPT's two countercontrols (MI464), two exact measurements instead of estimates:
#  GAPS  for every three-hole pool [0,M]\H (M<=14, |H|=3) and every r with r>=3 and |pool|-r>=3: the missing values of
#        the r-subset spectrum inside [min,max], recorded by distance from the minimum and from the maximum.
#  BANDS for every H2 instance (M<=14, all holes q, counts (2,b,c)) and every legal pair: is t_B within [min_b(R), max_b(R)]
#        of the remainder R for EVERY pair (the corrected one-sided claim), and when a pair fails, how far t_B sits from the
#        nearer extreme of that pair's spectrum.
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
def GAPS():
    from collections import Counter
    dlo = Counter(); dhi = Counter(); worst = {}
    for M in range(8, 15):
        for H in itertools.combinations(range(M + 1), 3):
            pool = [x for x in range(M + 1) if x not in H]
            for r in range(3, len(pool) - 2):
                sp = spec(pool, r); lo = sum(pool[:r]); hi = sum(pool[-r:])
                for t in range(lo, hi + 1):
                    if t not in sp:
                        a, b = t - lo, hi - t; d = min(a, b)
                        if a <= b: dlo[a] += 1
                        else: dhi[b] += 1
                        if d > worst.get('d', -1): worst = {'d': d, 'M': M, 'H': H, 'r': r, 't': t, 'lo': lo, 'hi': hi}
        print(f"GAPS M<={M}: missing-by-distance-from-min {dict(sorted(dlo.items()))}, from-max {dict(sorted(dhi.items()))}, worst {worst} ({time.time()-T0:.0f}s)", flush=True)
def BANDS():
    tot = pairs_n = outside = 0; fail_dist = {}; cases = []
    for M in range(8, 15):
        for q in range(0, M + 1):
            pool = [x for x in range(M + 1) if x != q]; n = len(pool)
            for b in range(3, n - 4):
                c = n - 2 - b
                if c < 3 or c < b: continue
                for sums in enum_targets(pool, [2, b, c], lambda s, u: margin_ok(s, u, 1)):
                    u, tB, tC = sums; tot += 1
                    for i in range(0, (u + 1) // 2):
                        j = u - i
                        if i == j or i not in pool or j not in pool: continue
                        R = [x for x in pool if x not in (i, j)]; lo = sum(R[:b]); hi = sum(R[-b:]); pairs_n += 1
                        if not (lo <= tB <= hi): outside += 1; cases.append((M, q, b, c, sums, (i, j), lo, hi)) if len(cases) < 6 else None; continue
                        if tB not in spec(R, b):
                            d = min(tB - lo, hi - tB); fail_dist[d] = fail_dist.get(d, 0) + 1
        print(f"BANDS M<={M}: instances {tot}, (instance,pair) {pairs_n}, t_B outside [min,max] of the remainder {outside}; pairs where t_B is inside but missing, by distance from the nearer extreme {dict(sorted(fail_dist.items()))} ({time.time()-T0:.0f}s)", flush=True)
    print("outside cases:", cases)
if __name__ == '__main__':
    for w in sys.argv[1:] or ['GAPS', 'BANDS']: globals()[w]()
