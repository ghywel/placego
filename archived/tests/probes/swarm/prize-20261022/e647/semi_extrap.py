# Per-block expected counts (scaled from the window to the dyadic block) for IND and SEMI models; fit and extrapolate.
import re, math, sys
blocks = {}
cur = None
for line in open(sys.argv[1]):
    m = re.match(r'BLOCK j=(\d+)', line)
    if m: cur = int(m.group(1)); blocks[cur] = {}; continue
    m = re.match(r'X=(\d+) W=(\d+)', line)
    if m: blocks[cur]['scale'] = 2**cur / int(m.group(2)); continue
    m = re.match(r'delta=(\d+) obs=(\d+) (.*)', line)
    if m:
        d = int(m.group(1)); vals = dict(kv.split('=') for kv in m.group(3).split())
        blocks[cur][d] = {k: float(v)*blocks[cur]['scale'] for k, v in vals.items()}
        blocks[cur][d]['obs'] = int(m.group(2))
models = ['IND', 'SEMI_y13', 'SEMI_y31']
for d in [2, 4, 8]:
    print(f"delta={d}: per-block expected count (block [2^j,2^(j+1)), window-scaled)")
    for j in sorted(blocks):
        r = blocks[j].get(d)
        if r: print(f"  j={j:2d} obs_window={r['obs']}  " + "  ".join(f"{mm}={r.get(mm,0):.3g}" for mm in models))
# fit log(count) = a + b * (j ln2)^0.69 for SEMI_y13 delta=2 over j>=20, and linear-in-j alternative
pts = [(j, blocks[j][2]['SEMI_y13']) for j in sorted(blocks) if j >= 20 and blocks[j][2]['SEMI_y13'] > 0]
def fit(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    b = sum((x-mx)*(y-my) for x, y in zip(xs, ys))/sum((x-mx)**2 for x in xs); return my - b*mx, b
for name, f in [('power (log x)^0.69', lambda j: (j*math.log(2))**0.69), ('linear in log x', lambda j: j*math.log(2))]:
    a, b = fit([f(j) for j, _ in pts], [math.log(c) for _, c in pts])
    tail37 = sum(math.exp(a + b*f(j)) for j in range(37, 400))
    tail73 = sum(math.exp(a + b*f(j)) for j in range(73, 400))
    print(f"SEMI_y13 delta=2 fit [{name}]: slope={b:.3f}; predicted expected #solutions in [2^37,inf): {tail37:.2e}; in [2^73~1e22,inf): {tail73:.2e}")
tot = sum(c for j, c in pts) * 2  # even j sampled; odd j assumed similar
print(f"SEMI_y13 delta=2 expected #solutions in [2^20, 2^37) (even-j samples x2): {tot:.2e}")
