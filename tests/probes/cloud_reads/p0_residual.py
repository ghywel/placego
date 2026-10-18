# Cloud's bounded diagnostic for GPT's MI362 protected one-hole four-bin statement P_0 and the actual five-bin
# least-slack residual (CL439 preregistration). Three parts, each capped:
#  E1  P_0 direct: pool R=[0,m]\{q}, four sizes>=3 summing to m, targets with correct total and u_J >= L(r)+r for every
#      proper nonempty group J (GPT's P_0, lower cuts only). Does a joint partition exist? m = 12..15, all q.
#  E2  Actual residual: every five-bin SS instance on [0,N-1], sizes>=3 (N=15,16), whose global least lower slack h
#      is attained by a singleton (or its complement: reflect first). For every canonical recipe (l,k,q) of that bin,
#      check that the residual satisfies P_0 and the exact lift gate, and whether the residual partitions. Plus the
#      N=17 fixture of MI366 and the MI350 negative as controls.
#  E3  Unexpected check: two-hole pools [0,m]\{q1,q2}, sizes>=3, with margin mu*r for mu in (1,2): does the family
#      H(2,mu) hold at m=12,13? (The shape of the remainder in an inductive proof.)
import itertools, sys, time
def L(t): return t*(t-1)//2
def exists(pool, sizes, sums):
    pool = sorted(pool); k = len(sizes); n = len(pool); rc = list(sizes); rs = list(sums)
    suf_lo = [0]*(n+1); suf_hi = [0]*(n+1)   # not used for exact bounds; use prefix sums for pruning
    pre = [0]*(n+1)
    for i, x in enumerate(pool): pre[i+1] = pre[i] + x
    def lo_from(i, c): return pre[i+c] - pre[i] if i + c <= n else None
    def hi_from(i, c): return pre[n] - pre[n-c] if c <= n - i else None
    def rec(i):
        if i == n: return all(x == 0 for x in rc)
        x = pool[i]; tried = set()
        for b in range(k):
            key = (rc[b], rs[b])
            if rc[b] == 0 or rs[b] < x or key in tried: continue
            tried.add(key); rc[b] -= 1; rs[b] -= x
            c = rc[b]; r = rs[b]
            ok = (c == 0 and r == 0) or (c > 0 and i + 1 + c <= n and lo_from(i+1, c) <= r <= hi_from(i+1, c))
            if ok and rec(i+1): return True
            rc[b] += 1; rs[b] += x
        return False
    return rec(0)
def groups(k):
    for mask in range(1, (1 << k) - 1): yield mask
def margin_ok(sizes, sums, mu):
    k = len(sizes)
    for mask in groups(k):
        r = sum(sizes[j] for j in range(k) if mask >> j & 1); s = sum(sums[j] for j in range(k) if mask >> j & 1)
        if s < L(r) + mu*r: return False
    return True
def enum_targets(pool, sizes, cond):
    tot = sum(pool); k = len(sizes); n = len(pool)
    rng = []
    for c in sizes:
        rng.append(range(L(c), c*(max(pool)) + 1))
    for us in itertools.product(*rng[:-1]):
        last = tot - sum(us)
        if last < 0: continue
        sums = list(us) + [last]
        if any(sizes[j] == sizes[j+1] and sums[j] > sums[j+1] for j in range(k-1)): continue
        if cond(sizes, sums): yield sums
T0 = time.time(); CAP = 1500
def E1():
    print("== E1: P_0 direct (one hole, four bins, sizes>=3, margin r) ==", flush=True)
    for m in range(12, 16):
        cnt = fail = 0; fails = []
        for q in range(0, m + 1):
            pool = [x for x in range(m + 1) if x != q]
            for sizes in itertools.combinations_with_replacement(range(3, m), 4):
                if sum(sizes) != m: continue
                for sums in enum_targets(pool, sizes, lambda s, u: margin_ok(s, u, 1)):
                    cnt += 1
                    if not exists(pool, list(sizes), sums): fail += 1; fails.append((q, sizes, tuple(sums)))
            if time.time() - T0 > CAP: print("E1 time cap at m", m, "q", q); break
        print(f"m={m}: P_0 instances {cnt}, no partition {fail} {fails[:5]} ({time.time()-T0:.0f}s)", flush=True)
        if time.time() - T0 > CAP: return
def slacks5(N, sizes, sums):
    k = len(sizes); out = {}
    for mask in groups(k):
        r = sum(sizes[j] for j in range(k) if mask >> j & 1); s = sum(sums[j] for j in range(k) if mask >> j & 1)
        out[mask] = s - L(r)
    return out
def lift_gate(l, k, m, q, sizes, sums):
    h = q + k*m; r_all = sum(sizes)
    if sum(sums) != L(m+1) - q: return False
    if m*(l + 1 - k) < 2*q: return False
    for mask in groups(4):
        r = sum(sizes[j] for j in range(4) if mask >> j & 1); s = sum(sums[j] for j in range(4) if mask >> j & 1)
        if s < L(r) + max((k+1)*r, h - l*r): return False
    return True
def E2():
    print("== E2: actual five-bin least-slack singleton residuals (N=15,16) ==", flush=True)
    stats = dict(instances=0, singleton_min=0, pair_or_triple_only=0, recipes=0, residuals=set(), p0_fail=0, gate_fail=0, nopart=0, nopart_list=[], reflected=0)
    for N in (15, 16):
        full = list(range(N))
        for sizes in itertools.combinations_with_replacement(range(3, N), 5):
            if sum(sizes) != N: continue
            def ss(s, u):
                for mask in groups(5):
                    r = sum(s[j] for j in range(5) if mask >> j & 1); v = sum(u[j] for j in range(5) if mask >> j & 1)
                    if not (L(r) <= v <= r*(N-1) - L(r)): return False
                return True
            for sums in enum_targets(full, sizes, ss):
                stats['instances'] += 1
                sl = slacks5(N, sizes, sums); h = min(sl.values())
                att = [mask for mask, v in sl.items() if v == h]
                singles = [mask for mask in att if bin(mask).count('1') == 1]
                comps = [mask for mask in att if bin(mask).count('1') == 4]
                if not singles and not comps: stats['pair_or_triple_only'] += 1; continue
                stats['singleton_min'] += 1
                cases = [(j, sizes, sums) for j in range(5) if (1 << j) in singles]
                for mask in comps:   # reflect original: x -> N-1-x; sums -> c*(N-1) - u
                    j = [b for b in range(5) if not mask >> b & 1][0]
                    rs = [sizes[b]*(N-1) - sums[b] for b in range(5)]
                    cases.append((j, sizes, rs)); stats['reflected'] += 1
                for (j, sz, su) in cases:
                    a = sz[j]; m = N - a; hh = su[j] - L(a)
                    others = [b for b in range(5) if b != j]
                    for k in range(0, a):
                        l = a - 1 - k; q = hh - k*m
                        if not (0 <= q <= m): continue
                        stats['recipes'] += 1
                        A = list(range(l)) + [l + q] + list(range(l + m + 1, N))
                        assert len(set(A)) == a and sum(A) == su[j]
                        pool = sorted(set(full) - set(A)); R = [x - l for x in pool]
                        assert R == [x for x in range(m + 1) if x != q]
                        rsz = [sz[b] for b in others]; rsu = [su[b] - l*sz[b] for b in others]   # translate values by -l: each bin's sum drops by l*size
                        assert sum(rsu) == sum(R)
                        key = (m, q, tuple(sorted(zip(rsz, rsu))))
                        p0 = margin_ok(rsz, rsu, 1); gate = lift_gate(l, k, m, q, rsz, rsu)
                        if not p0: stats['p0_fail'] += 1
                        if not gate: stats['gate_fail'] += 1
                        if key in stats['residuals']: continue
                        stats['residuals'].add(key)
                        if not exists(R, rsz, rsu): stats['nopart'] += 1; stats['nopart_list'].append((N, sz, su, j, l, k, q))
            if time.time() - T0 > 2*CAP: print("E2 time cap"); break
        print(f"N={N} done ({time.time()-T0:.0f}s)", flush=True)
    stats['residuals'] = len(stats['residuals'])
    print("E2 stats:", {k: (v if k != 'nopart_list' else v[:5]) for k, v in stats.items()}, flush=True)
def controls():
    print("== controls ==")
    R = [x for x in range(15) if x != 1]
    print("MI366 fixture R=[0,14]\\{1} sizes(3,3,4,4) targets(14,14,38,38): P_0", margin_ok([3,3,4,4],[14,14,38,38],1), "lift gate(l=2,k=0,m=14,q=1)", lift_gate(2,0,14,1,[3,3,4,4],[14,14,38,38]), "partition", exists(R,[3,3,4,4],[14,14,38,38]))
    print("MI366 lift [0,16] sizes(3,3,3,4,4) sums(4,20,20,46,46): h =", min(slacks5(17,[3,3,3,4,4],[4,20,20,46,46]).values()), "attained by", [m for m,v in slacks5(17,[3,3,3,4,4],[4,20,20,46,46]).items() if v == 1])
    P = [x for x in range(13) if x != 6]
    print("MI350 negative (4,18,18,32) on [0,12]\\{6}: P_0", margin_ok([3,3,3,3],[4,18,18,32],1), "plain cuts only", all(sum(u) >= L(r) for u, r in [([4],3)]), "partition", exists(P,[3,3,3,3],[4,18,18,32]))
    print("MI364 protected (18,18,20,16):", margin_ok([3,3,3,3],[18,18,20,16],1), exists(P,[3,3,3,3],[18,18,20,16]))
def pool_cuts(pool, sizes, sums):
    pool = sorted(pool); k = len(sizes); n = len(pool); pre = [0]
    for x in pool: pre.append(pre[-1] + x)
    for mask in groups(k):
        r = sum(sizes[j] for j in range(k) if mask >> j & 1); s = sum(sums[j] for j in range(k) if mask >> j & 1)
        if not (pre[r] <= s <= pre[n] - pre[n-r]): return False
    return True
def E3():
    print("== E3: two holes, four bins sizes>=3, margin mu*r AND the pool's own cuts (m=12,13) ==", flush=True)
    for mu in (2, 1):
        for m in (12, 13):
            cnt = fail = 0; fails = []
            for q1, q2 in itertools.combinations(range(m + 2), 2):
                pool = [x for x in range(m + 2) if x not in (q1, q2)]
                for sizes in itertools.combinations_with_replacement(range(3, m), 4):
                    if sum(sizes) != m: continue
                    for sums in enum_targets(pool, sizes, lambda s, u: margin_ok(s, u, mu) and pool_cuts(pool, s, u)):
                        cnt += 1
                        if not exists(pool, list(sizes), sums): fail += 1; fails.append((q1, q2, sizes, tuple(sums)))
                if time.time() - T0 > 3*CAP: break
            print(f"mu={mu} m={m}: instances {cnt}, no partition {fail} {fails[:4]} ({time.time()-T0:.0f}s)", flush=True)
            if time.time() - T0 > 3*CAP: print("E3 time cap"); return
if __name__ == '__main__':
    which = sys.argv[1:] or ['controls', 'E1', 'E2', 'E3']
    for w in which: globals()[w]()
