# Statement-level machine checks (Cloud, CL441) of GPT's waiting-room candidates G318-G322, independent of GPT's code.
# G318: S=[0,M]\H, |H|<=3, M>=9, r>=3, t=|S|-r>=3: every integer in [L(r)+hr, U_r(M)-hr] is an r-subset sum.   (M=9..16)
# G319: two labelled intervals [0,P-1],[0,Q-1]; counts l_i,k_i>=1 (three bins); targets v_i with total L(P)+L(Q) and
#       L(l_i)+L(k_i) <= v_i <= l_i(P-1)-L(l_i)+k_i(Q-1)-L(k_i)  =>  partition with those counts.               (P,Q<=7)
# G321: S=[0,M]\{1,p,p+1}, three sizes>=3, margin 3r on every proper group, total  =>  partition.                (M<=15)
# G322: R=[0,M]\{1,q}, three sizes>=3, margin 2r, total  =>  partition.                                            (M<=15)
import itertools, sys, time
sys.path.insert(0, 'tests/probes/cloud_reads')
from p0_residual import L, exists, margin_ok, enum_targets
T0 = time.time()
def G318():
    bad = tot = 0
    for M in range(9, 17):
        for h in range(0, 4):
            for H in itertools.combinations(range(M + 1), h):
                S = [x for x in range(M + 1) if x not in H]
                for r in range(3, len(S) - 2):
                    sp = {sum(c) for c in itertools.combinations(S, r)}; tot += 1
                    lo = L(r) + h*r; hi = r*M - L(r) - h*r
                    if any(t not in sp for t in range(lo, hi + 1)): bad += 1; print("G318 gap", M, H, r)
        print(f"G318 M={M}: cumulative (pool,r) {tot}, gaps {bad} ({time.time()-T0:.0f}s)", flush=True)
def G319():
    tot = bad = 0
    for P in range(3, 8):
        for Q in range(3, 8):
            for ls in itertools.product(range(1, P), repeat=3):
                if sum(ls) != P: continue
                for ks in itertools.product(range(1, Q), repeat=3):
                    if sum(ks) != Q: continue
                    lo = [L(l) + L(k) for l, k in zip(ls, ks)]; hi = [l*(P-1) - L(l) + k*(Q-1) - L(k) for l, k in zip(ls, ks)]
                    for v0 in range(lo[0], hi[0] + 1):
                        for v1 in range(lo[1], hi[1] + 1):
                            v2 = L(P) + L(Q) - v0 - v1
                            if not (lo[2] <= v2 <= hi[2]): continue
                            tot += 1
                            # pool: two labelled copies; encode copy 2 as values shifted by a big offset with counts enforced
                            # via a direct search over low-row subsets
                            ok = False
                            for A1 in itertools.combinations(range(P), ls[0]):
                                rest1 = [x for x in range(P) if x not in A1]
                                for B1 in itertools.combinations(rest1, ls[1]):
                                    C1 = [x for x in rest1 if x not in B1]
                                    need = [v0 - sum(A1), v1 - sum(B1), v2 - sum(C1)]
                                    if exists(list(range(Q)), list(ks), need): ok = True; break
                                if ok: break
                            if not ok: bad += 1; print("G319 FAIL", P, Q, ls, ks, (v0, v1, v2))
            print(f"G319 P={P} Q={Q}: cumulative {tot}, failures {bad} ({time.time()-T0:.0f}s)", flush=True)
def three_bin(name, pools, mu, Mmax):
    tot = bad = 0
    for M in range(8, Mmax + 1):
        for H in pools(M):
            S = [x for x in range(M + 1) if x not in H]
            for sizes in itertools.combinations_with_replacement(range(3, M), 3):
                if sum(sizes) != len(S): continue
                for sums in enum_targets(S, sizes, lambda s, u: margin_ok(s, u, mu)):
                    tot += 1
                    if not exists(S, list(sizes), sums): bad += 1; print(name, "FAIL", M, H, sizes, sums)
        print(f"{name} M={M}: cumulative {tot}, failures {bad} ({time.time()-T0:.0f}s)", flush=True)
def G321(): three_bin("G321", lambda M: [(1, p, p + 1) for p in range(2, M - 1)], 3, 15)
def G322(): three_bin("G322", lambda M: [(1, q) for q in range(2, M + 1)], 2, 15)
if __name__ == '__main__':
    for w in sys.argv[1:] or ['G318', 'G319', 'G321', 'G322']: globals()[w]()
