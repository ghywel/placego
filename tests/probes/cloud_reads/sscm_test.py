# Cloud, CL443: is "lower margin h*r AND count capacity at every cut point" sufficient where margin alone fails?
# Count capacity at cut c: low = pool elements < c, high = the rest; for bin i, K_i = {k : minsum_i(k) <= u_i <= maxsum_i(k)}
# where minsum_i(k) takes the k smallest low and s_i-k smallest high values (maxsum: largest). Necessary for any partition:
# every K_i nonempty and sum(min K_i) <= |low| <= sum(max K_i).
import itertools, sys, time
sys.path.insert(0, 'tests/probes/cloud_reads')
from p0_residual import L, exists, margin_ok, enum_targets
def count_capacity(pool, sizes, sums):
    pool = sorted(pool)
    for c in range(pool[0] + 1, pool[-1] + 1):
        low = [x for x in pool if x < c]; high = [x for x in pool if x >= c]
        if not low or not high or c - 1 in pool and c in pool and False: pass
        mins = []; maxs = []
        for s, u in zip(sizes, sums):
            K = []
            for k in range(max(0, s - len(high)), min(s, len(low)) + 1):
                mn = sum(low[:k]) + sum(high[:s - k]); mx = sum(low[len(low) - k:]) + sum(high[len(high) - (s - k):] if s - k else [])
                if mn <= u <= mx: K.append(k)
            if not K: return False
            mins.append(min(K)); maxs.append(max(K))
        if not (sum(mins) <= len(low) <= sum(maxs)): return False
    return True
T0 = time.time()
def run(k, hs, Mmax, name):
    for h in hs:
        tot = tot_cc = bad_margin = bad_cc = 0
        for M in range(8, Mmax + 1):
            for H in itertools.combinations(range(M + 1), h):
                S = [x for x in range(M + 1) if x not in H]
                if len(S) < 3 * k: continue
                for sizes in itertools.combinations_with_replacement(range(3, M), k):
                    if sum(sizes) != len(S): continue
                    for sums in enum_targets(S, sizes, lambda s, u: margin_ok(s, u, h)):
                        tot += 1; ok = exists(S, list(sizes), sums)
                        if not ok: bad_margin += 1
                        if count_capacity(S, sizes, sums):
                            tot_cc += 1
                            if not ok: bad_cc += 1; print(name, "SSCM FAIL", h, M, H, sizes, sums)
        print(f"{name} h={h}: margin-admitted {tot} (no partition {bad_margin}); margin+count-capacity admitted {tot_cc} (no partition {bad_cc}) ({time.time()-T0:.0f}s)", flush=True)
if __name__ == '__main__':
    w = sys.argv[1] if len(sys.argv) > 1 else 'k3'
    if w == 'k3': run(3, (3, 4, 5), 14, 'k3')
    if w == 'k4': run(4, (2, 3), 14, 'k4')
    if w == 'mi350':
        P = [x for x in range(13) if x != 6]
        print("MI350 negative (4,18,18,32): count capacity", count_capacity(P, [3,3,3,3], [4,18,18,32]), "margin r", margin_ok([3,3,3,3],[4,18,18,32],1))
        print("T3 failure {0..3,7..11} (17,17,17): count capacity", count_capacity([0,1,2,3,7,8,9,10,11],[3,3,3],[17,17,17]))
