# Cloud, CL448: statement check of GPT's G324. Two labelled intervals; row 1 counts (1,b,c,d) with b,c,d>=3 on [0,P-1];
# row 2 counts (a2,b2,c2,d2) all >=3 on [0,Q-1]; combined targets obeying total and all 14 combined fixed-count group
# bounds => partition. Oracle: the set of achievable row-1 sum vectors plus the set of achievable row-2 sum vectors
# (complete enumeration of ordered partitions), then a sumset membership test for every admitted target vector.
import itertools, sys, time
sys.path.insert(0, 'tests/probes/cloud_reads')
from p0_residual import L
def U(c, n): return c*(n-1) - L(c) if c > 0 else 0
def Lz(c): return L(c) if c > 0 else 0
def groups(k):
    for mask in range(1, (1 << k) - 1): yield [j for j in range(k) if mask >> j & 1]
def rowvectors(n, counts):
    out = set(); pool = list(range(n))
    def rec(i, rem, sums):
        if i == len(counts): out.add(tuple(sums)); return
        for comb in itertools.combinations(rem, counts[i]):
            rec(i + 1, [x for x in rem if x not in comb], sums + [sum(comb)])
    rec(0, pool, []); return out
T0 = time.time()
for (ls, ks) in [((1,3,3,3),(3,3,3,3)), ((1,3,3,4),(3,3,3,3)), ((1,3,3,3),(3,3,3,4)), ((1,3,4,4),(3,3,3,3))]:
    P, Q = sum(ls), sum(ks)
    S1 = rowvectors(P, ls); S2 = rowvectors(Q, ks)
    lo = [Lz(l) + Lz(k) for l, k in zip(ls, ks)]; hi = [U(l, P) + U(k, Q) for l, k in zip(ls, ks)]
    total = L(P) + L(Q); tot = bad = 0
    for v0 in range(lo[0], hi[0] + 1):
        for v1 in range(lo[1], hi[1] + 1):
            for v2 in range(lo[2], hi[2] + 1):
                v3 = total - v0 - v1 - v2
                if not (lo[3] <= v3 <= hi[3]): continue
                v = (v0, v1, v2, v3); ok = True
                for J in groups(4):
                    lJ = sum(ls[j] for j in J); kJ = sum(ks[j] for j in J); vJ = sum(v[j] for j in J)
                    if not (Lz(lJ) + Lz(kJ) <= vJ <= U(lJ, P) + U(kJ, Q)): ok = False; break
                if not ok: continue
                tot += 1
                if not any((v0 - s[0], v1 - s[1], v2 - s[2], v3 - s[3]) in S2 for s in S1): bad += 1; print("G324 FAIL", ls, ks, v)
    print(f"G324 rows {ls}/{ks}: row-1 vectors {len(S1)}, row-2 vectors {len(S2)}, admitted targets {tot}, failures {bad} ({time.time()-T0:.0f}s)", flush=True)
