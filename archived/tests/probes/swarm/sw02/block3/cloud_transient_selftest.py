# Self-test (Cloud, CL757): the packed evolution against a per-cell simulator; the E and passage detectors on synthetic traces.
import numpy as np, sys
sys.argv = ['x']; ns = {}; exec(open('cloud_transient_scan.py').read().split("def main():")[0], ns)
evolve, match, E_T, PASS_T, lock_times = ns['evolve'], ns['match'], ns['E_T'], ns['PASS_T'], ns['lock_times']
rng = np.random.default_rng(7); bad = 0
for trial in range(300):
    k = int(rng.integers(1, 40)); T = int(rng.integers(50, 400))
    r = (1 << (k - 1)) | int(rng.integers(0, 1 << (k - 1))) if k > 1 else 1
    # per-cell: row array of k+T+2 cells, cell i at index i-1
    row = np.zeros(k + T + 2, dtype=np.uint8)
    for j in range(k): row[j] = (r >> j) & 1
    col1 = [int(row[0])]
    for t in range(1, T):
        c = 1 if t % 2 == 0 else 0
        left = np.empty_like(row); left[0] = c; left[1:] = row[:-1]
        right = np.empty_like(row); right[:-1] = row[1:]; right[-1] = 0
        row = left ^ (row | right); col1.append(int(row[0]))
    direct = np.array(col1[0::2], dtype=np.uint8)           # ticks 1,3,5,...
    packed = evolve([r], T)[0]
    if not np.array_equal(direct, packed): bad += 1; print("MISMATCH", k, T, r)
print(f"300 rows: packed evolution vs per-cell: {bad} mismatches")
# detectors on a synthetic trace: the periodic word's bits with an E at a known offset, the passage at offset 10
A=[2,5]; E=[3,3,5,3,5,5,5,5]; gaps = A*3 + (E + A*4 + E + A*7 + E) + A*5
u = np.zeros(sum(gaps) + 1, dtype=np.uint8); p = 0; u[0] = 1
for g in gaps: p += g; u[p] = 1
U = u[None, :]
me = np.flatnonzero(match(U, E_T)[0]).tolist(); mp = np.flatnonzero(match(U, PASS_T)[0]).tolist()
print("E offsets found:", me, "expected [21, 83, 166]; passage offsets:", mp, "expected [21]")
ok2 = (me == [21, 83, 166]) and (mp == [21])
# lock detection: a trace that is random then period 7 from sample 100
v = np.concatenate([rng.integers(0, 2, 100, dtype=np.uint8), np.tile(np.array([1,0,1,0,0,0,0], dtype=np.uint8), 60)])
s0, per = lock_times(v[None, :]); print("lock:", int(s0[0]), int(per[0]), "expected s0 <= 100 and period 7")
ok3 = (per[0] == 7 and s0[0] <= 100)
print("SELFTEST", "PASS" if bad == 0 and ok2 and ok3 else "FAIL")
