"""error_process.py: the error process at the edge (CL740). With the strip fixed at the seed's phase (A0 = the seed's row
at a multiple of 32), e_j(t) = a_j(t) XOR C_j(t) and the edge m(t) = the lowest erroneous wheel. Every tick: m(t), the 64
errors above the edge, the edge parent's strip bit, the jump. Reports: whether m ever decreases and the exact settling
tick; the density of black at the edge's parent and the jump law at a death, whose product is the speed; the error density
at each offset above the edge; and the cell of CL739's table with rate 0.014, read with the actual and strip bits of three
wheels over the three ticks before the arrival. Predictions P-D1 … P-D4 in CL740.
Usage: python3 error_process.py ROWSDIR   (the rows of tree16_data.py at 165,750 wheels; A0.bin at phase 0)"""
import sys, time, collections
import numpy as np
K = 165750; MASK = (1 << K) - 1; P = 32
ROWS = sys.argv[1]
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
A0 = int.from_bytes(open(f"{ROWS}/A0.bin", 'rb').read(), 'little')
cyc = [A0]
for _ in range(P): cyc.append(step(cyc[-1]))
assert cyc[P] == A0; cyc = cyc[:P]
t0 = time.time()
x = 1; t = 0; m_prev = 0; decreases = 0
tau = np.full(K, -1, dtype=np.int64)
dens = np.zeros(65, dtype=np.int64); nwin = 0
parent_black = [0, 0]                 # ticks with the edge's parent white / black
jumps = collections.Counter()         # jump size at a death (parent black)
stay_err = 0                          # checks of e_m(t+1) = not C_{m-1}(t)
MW = (1 << 64) - 1
hist_a = []                           # (t, m) history for the cell analysis: keep arrays of a and C bits near arrivals
E_prev = None
while True:
    C = cyc[t % P]; e = x ^ C; m = lowbit(e)
    if m < m_prev: decreases += 1
    for j in range(m_prev, min(m, K)): tau[j] = t          # wheels m_prev..m-1 became settled at t (first tick with m(t) > j)
    if m >= K: break
    w = (e >> (m + 1)) & MW
    for d in range(1, 65): dens[d] += (w >> (d - 1)) & 1
    nwin += 1
    pb = (C >> (m - 1)) & 1 if m >= 1 else 1
    parent_black[pb] += 1
    x2 = step(x); t2 = t + 1; C2 = cyc[t2 % P]; e2 = x2 ^ C2; m2 = lowbit(e2)
    if m >= 2: stay_err += int(((e2 >> m) & 1) != (1 - pb))
    if pb: jumps[min(m2 - m, 9)] += 1
    m_prev = m; x = x2; t = t2
    if t > 3_000_000: raise RuntimeError("no settling")
T_settle = t
print(f"exact settling through {K-1} at tick {T_settle} (the edge reached {K}); edge decreases {decreases}; {time.time()-t0:.0f} s")
print(f"P-D1: tau({K-1}) exact = {tau[K-1]} (detector 220307 - 32 = 220275)")
pb_dens = parent_black[1] / sum(parent_black)
tot = sum(jumps.values()); jd = {k: round(v / tot, 4) for k, v in sorted(jumps.items())}
mean_jump = sum(k * v for k, v in jumps.items()) / tot
print(f"edge parent black density {pb_dens:.4f} over {sum(parent_black)} ticks; the edge error dies exactly when the parent is black: violations {stay_err}")
print(f"jump at a death: {jd}; mean {mean_jump:.4f}; speed = density x mean jump = {pb_dens * mean_jump:.4f}; measured speed {K-1}/{tau[K-1]} = {(K-1)/tau[K-1]:.4f}")
print(f"error density at offsets 1..64 above the edge: {[round(float(dens[d]) / nwin, 3) for d in range(1, 65)]}")
# the cell: parent arrived by coincidence (tau_{k-1} == tau_{k-2}), strip bits C_{k-1}(a-1) = 1, C_{k-1}(a) = 0, C_{k-2}(a-1) = 1
# collect actual bits by re-evolving to the needed ticks: store the rows at ticks a-2, a-1, a for the cell's arrivals
cells = []
for k in range(3, K):
    a = int(tau[k - 1])
    if a < 2 or tau[k - 1] != tau[k - 2]: continue
    if ((cyc[(a - 1) % P] >> (k - 1)) & 1) != 1 or ((cyc[a % P] >> (k - 1)) & 1) != 0 or ((cyc[(a - 1) % P] >> (k - 2)) & 1) != 1: continue
    cells.append((a, k))
cells.sort()
print(f"cell instances: {len(cells)}")
x = 1; t = 0; i = 0; pats = collections.Counter(); coinc = 0; black_before = 0
rows_at = {}
need = sorted(set(a - 2 for a, _ in cells) | set(a - 1 for a, _ in cells) | set(a for a, _ in cells))
need_set = set(need); nmax = max(need) if need else 0
while t <= nmax:
    if t in need_set: rows_at[t] = x
    x = step(x); t += 1
for a, k in cells:
    def ab(j, tt): return (rows_at[tt] >> j) & 1
    def cb(j, tt): return (cyc[tt % P] >> j) & 1
    pat = tuple((ab(k - 2 + dj, a - 2 + dt), cb(k - 2 + dj, a - 2 + dt)) for dt in range(3) for dj in range(3))
    pats[pat] += 1
    coinc += int(ab(k, a) == cb(k, a)); black_before += ab(k, a - 1)
print(f"cell coincidence rate {coinc/len(cells):.4f}; child's actual bit black at a-1: {black_before/len(cells):.4f}")
print("most frequent 3x3 (actual, strip) patterns, rows t = a-2, a-1, a; columns wheels k-2, k-1, k:")
for pat, n in pats.most_common(6):
    rows_s = [" ".join(f"{pat[dt*3+dj][0]}/{pat[dt*3+dj][1]}" for dj in range(3)) for dt in range(3)]
    print(f"  {n:6d} ({n/len(cells):.3f}): " + " | ".join(rows_s))
