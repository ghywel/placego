# Cloud, CL443: three bounded tests behind the proposed trunk statement
#   T(h): pool [0,M]\H, |H|=h, k bins of sizes>=3, correct total, lower margin u_J >= L(r)+h*r on every proper group => partition.
#  T3    T(h) for k=3, h=0..5, M<=14.
#  SPEC  spectrum lemma for h=4,5,6 at M<=15, t>=3: every integer in [L(r)+hr, U_r(M)-hr] is an r-subset sum.
#  SEL   on P_0 instances (m=12,13) whose least adjusted slack is attained by a triple and by no singleton: for the complementary
#        top-tight singleton D, enumerate EVERY realization; does some realization leave a child in T(h') for its actual hole
#        count h'? does that child partition? Control: singleton-minimum instances, all realizations (MI368's inheritance).
import itertools, sys, time
sys.path.insert(0, 'tests/probes/cloud_reads')
from p0_residual import L, exists, margin_ok, enum_targets, groups
T0 = time.time()
def T3():
    for h in range(0, 6):
        tot = bad = 0
        for M in range(8, 15):
            for H in itertools.combinations(range(M + 1), h):
                S = [x for x in range(M + 1) if x not in H]
                if len(S) < 9: continue
                for sizes in itertools.combinations_with_replacement(range(3, M), 3):
                    if sum(sizes) != len(S): continue
                    for sums in enum_targets(S, sizes, lambda s, u: margin_ok(s, u, h)):
                        tot += 1
                        if not exists(S, list(sizes), sums): bad += 1; print("T3 FAIL", h, M, H, sizes, sums) if bad <= 5 else None
        print(f"T3 h={h}: instances {tot}, failures {bad} ({time.time()-T0:.0f}s)", flush=True)
def SPEC():
    for h in (4, 5, 6):
        tot = bad = 0
        for M in range(9, 16):
            for H in itertools.combinations(range(M + 1), h):
                S = [x for x in range(M + 1) if x not in H]
                for r in range(3, len(S) - 2):
                    sp = {sum(c) for c in itertools.combinations(S, r)}; tot += 1
                    lo = L(r) + h*r; hi = r*M - L(r) - h*r
                    if lo <= hi and any(t not in sp for t in range(lo, hi + 1)): bad += 1; print("SPEC gap", h, M, H, r) if bad <= 6 else None
        print(f"SPEC h={h}: (pool,r) pairs {tot}, gaps {bad} ({time.time()-T0:.0f}s)", flush=True)
def child_ok(pool, A, sizes, sums, j):
    R = [x for x in pool if x not in A]; base = R[0]; R2 = [x - base for x in R]
    rs = [sizes[b] for b in range(4) if b != j]; ru = [sums[b] - base*sizes[b] for b in range(4) if b != j]
    hh = (R2[-1] + 1) - len(R2)
    return margin_ok(rs, ru, hh), (lambda: exists(R2, rs, ru)), hh
def SEL():
    for m in (12, 13):
        st = dict(tri=0, tri_some=0, tri_some_part=0, tri_none_ex=[], single=0, single_all=0, single_all_ex=[])
        for q in range(0, m + 1):
            pool = [x for x in range(m + 1) if x != q]
            for sizes in itertools.combinations_with_replacement(range(3, m), 4):
                if sum(sizes) != m: continue
                for sums in enum_targets(pool, sizes, lambda s, u: margin_ok(s, u, 1)):
                    sl = {}
                    for mask in groups(4):
                        r = sum(sizes[j] for j in range(4) if mask >> j & 1); s = sum(sums[j] for j in range(4) if mask >> j & 1)
                        sl[mask] = s - L(r) - r
                    hmin = min(sl.values()); att = {mask for mask, v in sl.items() if v == hmin}
                    singles = [j for j in range(4) if (1 << j) in att]
                    triples = [mask for mask in att if bin(mask).count('1') == 3]
                    if singles:
                        st['single'] += 1; allok = True
                        for j in singles:
                            for A in itertools.combinations(pool, sizes[j]):
                                if sum(A) != sums[j]: continue
                                ok, _, hh = child_ok(pool, A, sizes, sums, j)
                                if not ok: allok = False
                        if allok: st['single_all'] += 1
                        elif len(st['single_all_ex']) < 3: st['single_all_ex'].append((q, sizes, tuple(sums)))
                    elif triples:
                        st['tri'] += 1; some = some_part = False
                        for mask in triples:
                            j = [b for b in range(4) if not mask >> b & 1][0]
                            for A in itertools.combinations(pool, sizes[j]):
                                if sum(A) != sums[j]: continue
                                ok, part, hh = child_ok(pool, A, sizes, sums, j)
                                if ok:
                                    some = True
                                    if part(): some_part = True; break
                            if some_part: break
                        if some: st['tri_some'] += 1
                        if some_part: st['tri_some_part'] += 1
                        elif len(st['tri_none_ex']) < 4: st['tri_none_ex'].append((q, sizes, tuple(sums)))
        print(f"SEL m={m}: singleton-min instances {st['single']}, every realization inherits T(h') {st['single_all']} (exceptions {st['single_all_ex']}); "
              f"triple-only-min instances {st['tri']}, some realization of the top singleton leaves a T(h') child {st['tri_some']}, "
              f"...and that child partitions {st['tri_some_part']}; otherwise {st['tri_none_ex']} ({time.time()-T0:.0f}s)", flush=True)
if __name__ == '__main__':
    for w in sys.argv[1:] or ['T3', 'SPEC', 'SEL']: globals()[w]()
