# Confirming test for Chaos 2's explanation (Cloud, CL758, P-W4): redraw cells above c on random support-120 rows and
# measure the tick of the first differing sampled head; Rule 30's left damage speed 0.2428 predicts a median near c/0.243.
import sys, numpy as np
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 5
sys.argv = ['x', 'none', 'none', 'none']; ns = {}
src = open('trap_measure.py').read().split("def main():")[0].replace("codes = [int(x) for x in open(sys.argv[1]).read().split()]; assert len(codes) == 829", "codes = list(range(829))")
exec(src, ns); evolve = ns['evolve']
rng = np.random.default_rng(SEED); K, N, T = 120, 2000, 600
rows = [(1 << (K - 1)) | int(rng.integers(0, 1 << 63)) | (int(rng.integers(0, 1 << 56)) << 63) for _ in range(N)]
U, _ = evolve(rows, T)
print(f"{N} rows of support {K}, horizon {T}; first differing sampled head after redrawing cells above c (cell {K} kept black)")
print("|  c | predicted c/0.243 | median tick | 10th pct | 90th pct | rows unchanged through the horizon |")
print("|---:|---:|---:|---:|---:|---:|")
for c in (20, 40, 60, 80, 100):
    low_mask = (1 << c) - 1; new = []
    for r in rows:
        hi = (int(rng.integers(0, 1 << (K - 1 - c))) << c) | (1 << (K - 1))
        new.append((r & low_mask) | hi)
    U2, _ = evolve(new, T); d = []
    for i in range(N):
        diff = np.flatnonzero(U[i] != U2[i]); d.append(int(2 * diff[0] + 1) if diff.size else T + 1)
    d = np.array(d); same = int((d > T).sum())
    print(f"| {c} | {c/0.243:.0f} | {int(np.median(d))} | {int(np.percentile(d,10))} | {int(np.percentile(d,90))} | {same} |", flush=True)
