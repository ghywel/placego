# Chaos test 2 (Cloud, CL758): is GPT's shielding (GC2777: root cells above a fixed low 70 redrawn, every sampled head
# through 193 preserved) typical? Random rows of support 120; rows whose first E launches at a tick in [70, 300]; cells
# 71..120 redrawn once at random (cell 120 kept black); does the first E survive at the same tick? Own code.
import sys, numpy as np
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 11
sys.argv = ['x', 'none', 'none', 'none']; ns = {}
src = open('trap_measure.py').read().split("def main():")[0].replace("codes = [int(x) for x in open(sys.argv[1]).read().split()]; assert len(codes) == 829", "codes = list(range(829))")
exec(src, ns); evolve, match, E_T = ns['evolve'], ns['match'], ns['E_T']
rng = np.random.default_rng(SEED)
K, N, T = 120, 3000, 400
rows = [(1 << (K - 1)) | int(rng.integers(0, 1 << 63)) | (int(rng.integers(0, 1 << 56)) << 63) for _ in range(N)]
U, _ = evolve(rows, T); ME = match(U, E_T)
first = np.where(ME.any(axis=1), np.argmax(ME, axis=1), -1); first_tick = 2 * first + 1
sel = [i for i in range(N) if first[i] >= 0 and 70 <= first_tick[i] <= 300]
print(f"{N} rows of support {K}, horizon {T}: {int((first>=0).sum())} with an E, {len(sel)} with the first E launching in ticks [70, 300]")
low_mask = (1 << 70) - 1
new_rows = []
for i in sel:
    hi = (int(rng.integers(0, 1 << 49)) << 70) | (1 << (K - 1))       # cells 71..119 random, cell 120 black
    new_rows.append((rows[i] & low_mask) | hi)
U2, _ = evolve(new_rows, T); ME2 = match(U2, E_T)
first2 = np.where(ME2.any(axis=1), np.argmax(ME2, axis=1), -1)
same = sum(1 for j, i in enumerate(sel) if first2[j] == first[i]); anyE = sum(1 for j in range(len(sel)) if first2[j] >= 0)
# the heads: how far do the sampled traces agree after the redraw?
agree_to = []
for j, i in enumerate(sel):
    d = np.flatnonzero(U[i] != U2[j]); agree_to.append(int(2 * d[0] + 1) if d.size else T)
agree_to = np.array(agree_to)
print(f"redraw of cells 71..120 (cell 120 kept black): first E preserved at the same tick in {same} of {len(sel)} ({100*same/len(sel):.1f}%); some E still present in {anyE}")
print(f"first differing sampled head after the redraw: median tick {int(np.median(agree_to))}, min {agree_to.min()}, 10th/90th percentile {int(np.percentile(agree_to,10))}/{int(np.percentile(agree_to,90))}; rows agreeing through tick 193: {int((agree_to > 193).sum())} of {len(sel)}")
by_launch = {}
for j, i in enumerate(sel):
    b = (int(first_tick[i]) // 50) * 50; by_launch.setdefault(b, [0, 0]); by_launch[b][1] += 1; by_launch[b][0] += int(first2[j] == first[i])
print("preserved by first-launch tick bin (preserved/total):", {k: f"{v[0]}/{v[1]}" for k, v in sorted(by_launch.items())})
