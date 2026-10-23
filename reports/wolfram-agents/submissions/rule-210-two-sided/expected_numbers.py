# Numbers for the rule 210 two-sided essay, computed first (Cloud, 2026-10-23). Physical coordinates, Bool as 0/1.
# rule 210: new = left xor (not center and right). Clock: center = t mod 2 (white at even times).
def step210(x):  # x: dict position -> bit, finite support; returns next
    keys = set()
    for p in x: keys.update((p - 1, p, p + 1))
    def g(p): return x.get(p, 0)
    y = {}
    for p in keys:
        v = g(p - 1) ^ ((1 - g(p)) & g(p + 1))
        if v: y[p] = 1
    return y
def clock_survival(x, T):
    """number of consecutive times t < T with center == t mod 2."""
    for t in range(T):
        if x.get(0, 0) != t % 2: return t
        x = step210(x)
    return T
# 1. every finite seed in [-4, 8] dies: the longest clock survival
import itertools
best = (0, None)
for bits in itertools.product([0, 1], repeat=13):
    x = {i - 4: b for i, b in enumerate(bits) if b}
    if not x: continue
    s = clock_survival(x, 200)
    if s > best[0]: best = (s, bits)
print("finite seeds in [-4, 8]: longest clock survival", best[0], "steps, seed", ''.join(map(str, best[1])), "(positions -4..8)")
# 2. the background of the empty left row, built sideways (rule 90 with the clock at the wall), first 64 right sites
def background(L, width, T):
    # lft: left half by rule 90 Dirichlet with clock at 0; columns right by right-permutivity. Returns y0[-width..width]
    clk = lambda t: t % 2
    # left half
    lft = {}
    for t in range(T + width + 2):
        for i in range(-width - 1, 1):
            if t == 0: lft[(0, i)] = (L[-i] if i < 0 and -i < len(L) else 0) if i < 0 else 0
            else: lft[(t, i)] = clk(t) if i == 0 else (lft.get((t - 1, i - 1), 0) ^ lft.get((t - 1, i + 1), 0))
    col = {0: lambda t: clk(t), 1: lambda t: clk(t + 1) ^ lft[(t, -1)]}
    cols = {0: [clk(t) for t in range(T + width + 1)], 1: [clk(t + 1) ^ lft[(t, -1)] for t in range(T + width + 1)]}
    for j in range(2, width + 1):
        cols[j] = [cols[j - 1][t + 1] ^ cols[j - 2][t] for t in range(T + width + 1 - j)]
    y0 = {}
    for i in range(-width, 0):
        if lft[(0, i)]: y0[i] = 1
    for j in range(1, width + 1):
        if cols[j][0]: y0[j] = 1
    return y0
y0 = background([0], 160, 160)
right = ''.join(str(y0.get(i, 0)) for i in range(1, 65))
print("background of the empty left row, sites 1..64:", right)
print("  truncated at site 160, its clock survives", clock_survival(dict(y0), 400), "steps (the light cone from the cut)")
# 3. a left row with a black cell at depth 3: the realization, and its clock
y1 = background([0, 0, 0, 1], 160, 160)
print("background of L = black at depth 3, sites -4..40:", ''.join(str(y1.get(i, 0)) for i in range(-4, 41)), "; truncated at 160 the clock survives", clock_survival(dict(y1), 400), "steps")
# 4. deviations from the empty-row background at the first positive site e: the clock's failure time
for e in [1, 2, 3, 4, 6, 8]:
    x = dict(y0); x[e] = 1 - x.get(e, 0)
    if x[e] == 0: del x[e]
    # truncate far right to keep it finite (sites > 64 are already zero in our construction)
    s = clock_survival(x, 200)
    # background gate w: least j with y0[e+2j+1] = 1 (for even e)
    w = None
    if e % 2 == 0:
        j = 0
        while e + 2 * j + 1 <= 64 and not y0.get(e + 2 * j + 1, 0): j += 1
        w = j
    print("flip site", e, ": clock fails at time", s, "" if w is None else f"(even e: w = {w}, predicted failure e + 2w + 1 = {e + 2 * w + 1})")
