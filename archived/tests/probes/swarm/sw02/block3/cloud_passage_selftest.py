# Self-test of the passage DAG (Cloud, CL755): at a small width, every right half (free row of 2W+... cells) beside the
# alternating centre whose column-1 samples match the trace on an arc has its exact W-windows inside the DAG's sets
# (soundness), and the DAG's sets equal a second, direct free-exterior simulation (same semantics, different code).
import sys, numpy as np, itertools
sys.argv = ['x', '5', 'none']; src = open(sys.argv[0] if False else 'cloud_passage_dag.py').read()
ns = {}; exec(src.split("def main():")[0], ns)
tr, move, forward, backward, Bstep, MASK = ns['tr'], ns['move'], ns['forward'], ns['backward'], ns['Bstep'], ns['MASK']
W = 5; L = 5                        # arc of L+1 phases, 2L ticks of exact evolution
def rows_evolve(rows, width, b):
    """one Rule 30 tick on rows (int array, bit i = cell i+1), centre bit b; valid cells 1..width-1."""
    one = np.uint64(1); left = (rows << one) | np.uint64(b)
    return (left ^ (rows | (rows >> one))) & MASK(width - 1)
bad = 0; checked = 0
for a in range(-34, 145 - L, 7):     # a sample of starting phases
    # exact: free rows of width W + 2L (+1 spare) at the odd tick of phase a
    width = W + 2 * L + 1
    rows = np.arange(1 << width, dtype=np.uint64)
    exact = {}
    cur = rows; w = width; ok = (cur & np.uint64(1)) == np.uint64(tr(a))
    hist = {a: cur}
    for s in range(a + 1, a + L + 1):
        cur = rows_evolve(cur, w, 0); w -= 1        # odd tick -> even tick, centre white
        cur = rows_evolve(cur, w, 1); w -= 1        # even tick -> odd tick, centre black
        ok &= (cur & np.uint64(1)) == np.uint64(tr(s)); hist[s] = cur
    for s in range(a, a + L + 1): exact[s] = hist[s][ok] & MASK(W)   # rows consistent on the whole arc
    F = forward(W, a, a + L); B = backward(W, F, a + L, a)
    for s in range(a, a + L + 1):
        ex = np.unique(exact[s]); dag = B[s]
        if not np.isin(ex, dag).all(): bad += 1; print("SOUNDNESS FAIL at phase", s, "start", a)
        checked += 1
    # second implementation of the relaxed semantics: explicit per-step exterior enumeration on sets of ints
    cur = set(int(x) for x in range(1 << W) if (x & 1) == tr(a)); rel = {a: set(cur)}
    for s in range(a + 1, a + L + 1):
        nxt = set()
        for x in cur:
            for e in range(4):
                y = x | (e << W)
                y = (((y << 1) | 0) ^ (y | (y >> 1))) & ((1 << (W + 1)) - 1)
                y = (((y << 1) | 1) ^ (y | (y >> 1))) & ((1 << W) - 1)
                if (y & 1) == tr(s): nxt.add(y)
        cur = nxt; rel[s] = set(cur)
    # backward prune by hand
    keep = {a + L: rel[a + L]}
    for s in range(a + L - 1, a - 1, -1):
        keep[s] = set()
        for x in rel[s]:
            for e in range(4):
                y = x | (e << W)
                y = (((y << 1) | 0) ^ (y | (y >> 1))) & ((1 << (W + 1)) - 1)
                y = (((y << 1) | 1) ^ (y | (y >> 1))) & ((1 << W) - 1)
                if y in keep[s + 1]: keep[s].add(x); break
    for s in range(a, a + L + 1):
        if set(int(v) for v in B[s].tolist()) != keep[s]: bad += 1; print("RELAXED-SEMANTICS MISMATCH at phase", s, "start", a)
        checked += 1
print(f"phase sets checked: {checked}; failures: {bad}; W={W}, arc length {L+1} phases, exact rows of {W+2*L+1} cells")
print("SELFTEST", "PASS" if bad == 0 else "FAIL")
