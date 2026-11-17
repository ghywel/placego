# Cloud, CL446. Two bounded checks on GPT's two-interval representation.
#  G323: counts left (a,1,1,1), right (0,k,k,k); every target vector obeying total + all fixed-count group bounds has a
#        partition. Independent oracle: enumerate the three left singleton values, then a right-row three-bin search.
#  SPLIT: for FOUR bins on two labelled intervals with arbitrary nonnegative counts, the combined fixed-count group bounds
#        (all 14 groups, both directions) imply an INTEGRAL rank split: low-row sums s_i with both rows satisfying their own
#        full-interval SS cuts. (The claim that Frank's g-polymatroid intersection theorem gives this for any k.)
import itertools, sys, time
sys.path.insert(0, 'tests/probes/cloud_reads')
from p0_residual import L, exists
def U(c, n): return c*(n-1) - L(c) if c > 0 else 0
def Lz(c): return L(c) if c > 0 else 0
def groups(k):
    for mask in range(1, (1 << k) - 1): yield [j for j in range(k) if mask >> j & 1]
def combined_ok(ls, ks, P, Q, v):
    k = len(ls)
    for J in groups(k):
        lJ = sum(ls[j] for j in J); kJ = sum(ks[j] for j in J); vJ = sum(v[j] for j in J)
        if not (Lz(lJ) + Lz(kJ) <= vJ <= U(lJ, P) + U(kJ, Q)): return False
    return True
def row_ok(cs, n, s):
    k = len(cs)
    for J in groups(k):
        cJ = sum(cs[j] for j in J); sJ = sum(s[j] for j in J)
        if not (Lz(cJ) <= sJ <= U(cJ, n)): return False
    return True
T0 = time.time()
def G323():
    tot = bad = 0
    for a in range(3, 7):
        for k in range(2, 5):
            P = a + 3; Q = 3*k; ls = (a, 1, 1, 1); ks = (0, k, k, k)
            lo = [Lz(l) + Lz(kk) for l, kk in zip(ls, ks)]; hi = [U(l, P) + U(kk, Q) for l, kk in zip(ls, ks)]
            total = L(P) + L(Q)
            for v0 in range(lo[0], hi[0] + 1):
                for v1 in range(lo[1], hi[1] + 1):
                    for v2 in range(lo[2], hi[2] + 1):
                        v3 = total - v0 - v1 - v2
                        if not (lo[3] <= v3 <= hi[3]): continue
                        v = (v0, v1, v2, v3)
                        if not combined_ok(ls, ks, P, Q, v): continue
                        tot += 1; ok = False
                        for xs in itertools.permutations(range(P), 3):
                            if sum(xs) != L(P) - v0: continue
                            ys = [v[i+1] - xs[i] for i in range(3)]
                            if min(ys) < Lz(k) or max(ys) > U(k, Q): continue
                            if exists(list(range(Q)), [k, k, k], ys): ok = True; break
                        if not ok: bad += 1; print("G323 FAIL", a, k, v)
            print(f"G323 a={a} k={k}: cumulative admitted {tot}, failures {bad} ({time.time()-T0:.0f}s)", flush=True)
def SPLIT():
    tot = bad = 0
    for P in range(2, 8):
        for Q in range(2, 8):
            for ls in itertools.product(range(0, P + 1), repeat=4):
                if sum(ls) != P: continue
                for ks in itertools.product(range(0, Q + 1), repeat=4):
                    if sum(ks) != Q: continue
                    if any(ls[i] + ks[i] == 0 for i in range(4)): continue
                    lo = [Lz(l) + Lz(kk) for l, kk in zip(ls, ks)]; hi = [U(l, P) + U(kk, Q) for l, kk in zip(ls, ks)]
                    total = L(P) + L(Q)
                    for v0 in range(lo[0], hi[0] + 1):
                        for v1 in range(lo[1], hi[1] + 1):
                            for v2 in range(lo[2], hi[2] + 1):
                                v3 = total - v0 - v1 - v2
                                if not (lo[3] <= v3 <= hi[3]): continue
                                v = (v0, v1, v2, v3)
                                if not combined_ok(ls, ks, P, Q, v): continue
                                tot += 1; found = False
                                for s0 in range(Lz(ls[0]), U(ls[0], P) + 1):
                                    for s1 in range(Lz(ls[1]), U(ls[1], P) + 1):
                                        for s2 in range(Lz(ls[2]), U(ls[2], P) + 1):
                                            s3 = L(P) - s0 - s1 - s2
                                            s = (s0, s1, s2, s3); t = tuple(v[i] - s[i] for i in range(4))
                                            if row_ok(ls, P, s) and row_ok(ks, Q, t): found = True; break
                                        if found: break
                                    if found: break
                                if not found: bad += 1; print("SPLIT FAIL", P, Q, ls, ks, v) if bad <= 5 else None
            print(f"SPLIT P={P} Q={Q}: cumulative admitted {tot}, no integral split {bad} ({time.time()-T0:.0f}s)", flush=True)
if __name__ == '__main__':
    for w in sys.argv[1:] or ['G323', 'SPLIT']: globals()[w]()
