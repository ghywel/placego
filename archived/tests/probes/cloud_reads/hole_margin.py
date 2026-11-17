# Follow-up to p0_residual.py (CL440). Three independent checks on the hole-count/margin representation:
#  SPEC  spectrum lemma: for S=[0,M]\H with |H|=h, r>=3, is every t in [L(r)+h*r, T_r(M)-h*r] the sum of an r-subset of S?
#  INF   are the H(2, r) failures of E3 (two holes, margin r) all individually infeasible (a spectrum gap)?
#  STEP  inductive step: for every P_0 instance (one hole, four bins, margin r) at m=12,13, take the bins attaining the least
#        margin-adjusted slack, realize each by every canonical recipe (first l pool elements, one pivot, last k pool
#        elements), and test whether the three-bin remainder satisfies the two-hole margin 2r (H(2)); and whether it partitions.
import itertools, sys, time
sys.path.insert(0, 'tests/probes/cloud_reads')
from p0_residual import L, exists, margin_ok, enum_targets, pool_cuts, groups
def spectrum(S, r): return {sum(c) for c in itertools.combinations(S, r)}
def SPEC():
    print("== SPEC ==", flush=True); bad = 0; tot = 0
    for M in range(8, 15):
        for h in range(0, 4):
            for H in itertools.combinations(range(M + 1), h):
                S = [x for x in range(M + 1) if x not in H]
                for r in range(3, len(S) - 2):
                    sp = spectrum(S, r); lo = L(r) + h*r; hi = sum(range(M - r + 1, M + 1)) - h*r
                    tot += 1
                    miss = [t for t in range(lo, hi + 1) if t not in sp]
                    if miss: bad += 1; print("gap", M, H, r, miss[:5]) if bad <= 8 else None
        print(f"M={M}: pairs (pool,r) {tot}, with a gap inside [L(r)+hr, T_r-hr]: {bad}", flush=True)
def INF():
    print("== INF ==", flush=True)
    m = 12; fails = []; indiv = 0
    for q1, q2 in itertools.combinations(range(m + 2), 2):
        pool = [x for x in range(m + 2) if x not in (q1, q2)]
        for sizes in itertools.combinations_with_replacement(range(3, m), 4):
            if sum(sizes) != m: continue
            sp = {c: spectrum(pool, c) for c in set(sizes)}
            for sums in enum_targets(pool, sizes, lambda s, u: margin_ok(s, u, 1) and pool_cuts(pool, s, u)):
                if not exists(pool, list(sizes), sums):
                    fails.append((q1, q2, sizes, tuple(sums)))
                    if any(sums[j] not in sp[sizes[j]] for j in range(4)): indiv += 1
    holes = {}
    for f in fails: holes[(f[0], f[1])] = holes.get((f[0], f[1]), 0) + 1
    print(f"m=12 H(2,r) failures {len(fails)}, individually infeasible {indiv}; by hole pair: {sorted(holes.items())}")
    print("joint-only failures (first 6):", [f for f in fails if all(f[3][j] in spectrum([x for x in range(m+2) if x not in (f[0],f[1])], f[2][j]) for j in range(4))][:6])
def STEP():
    print("== STEP ==", flush=True)
    for m in (12, 13):
        n_inst = n_single = n_pair = good = part = norecipe = 0; bad_ex = []
        for q in range(0, m + 1):
            pool = [x for x in range(m + 1) if x != q]
            for sizes in itertools.combinations_with_replacement(range(3, m), 4):
                if sum(sizes) != m: continue
                for sums in enum_targets(pool, sizes, lambda s, u: margin_ok(s, u, 1)):
                    n_inst += 1
                    sl = {}
                    for mask in groups(4):
                        r = sum(sizes[j] for j in range(4) if mask >> j & 1); s = sum(sums[j] for j in range(4) if mask >> j & 1)
                        sl[mask] = s - L(r) - r
                    hmin = min(sl.values()); singles = [j for j in range(4) if sl[1 << j] == hmin]
                    if not singles: n_pair += 1; continue
                    n_single += 1
                    found = found_part = False; nrec = 0
                    for j in singles:
                        a = sizes[j]; u = sums[j]
                        for k in range(0, a):
                            l = a - 1 - k
                            prefix = pool[:l]; suffix = pool[len(pool) - k:] if k else []
                            mid = pool[l:len(pool) - k]
                            need = u - sum(prefix) - sum(suffix)
                            if need not in mid: continue
                            A = prefix + [need] + suffix; nrec += 1
                            R = [x for x in pool if x not in A]
                            base = R[0]; R2 = [x - base for x in R]
                            rs = [sizes[b] for b in range(4) if b != j]; ru = [sums[b] - base*sizes[b] for b in range(4) if b != j]
                            holes = (R2[-1] + 1) - len(R2)
                            ok = margin_ok(rs, ru, holes)
                            if ok: found = True
                            if ok and exists(R2, rs, ru): found_part = True
                    if found: good += 1
                    if found_part: part += 1
                    elif nrec == 0: norecipe += 1
                    elif len(bad_ex) < 4: bad_ex.append((q, sizes, tuple(sums), singles))
        print(f"m={m}: P_0 instances {n_inst}; least margin-slack at a singleton {n_single}, pair/triple only {n_pair}; "
              f"some canonical recipe leaves an H(holes)-remainder {good}; ...and that remainder partitions {part}; no canonical recipe exists at all (pivot would be the hole or off the pool) {norecipe}; recipe exists but no H-remainder {bad_ex}", flush=True)
if __name__ == '__main__':
    for w in sys.argv[1:] or ['SPEC', 'INF', 'STEP']: globals()[w]()
