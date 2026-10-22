# Average the SEMI_y13 delta=2 (and delta=4, 8) per-n probability over 3 windows per block, scale to the block,
# fit log(count) vs (log x)^0.69 and vs log x, extrapolate tails. Also compare delta=8,12,16 with exact block counts.
import re, math
from collections import defaultdict
rows = defaultdict(list); cur = None; W = None
for line in open('semi_multi_out.txt'):
    m = re.match(r'BLOCK j=(\d+) f=([\d.]+)', line)
    if m: cur = int(m.group(1)); continue
    m = re.match(r'X=(\d+) W=(\d+)', line)
    if m: W = int(m.group(2)); continue
    m = re.match(r'delta=(\d+) obs=(\d+) (.*)', line)
    if m:
        vals = dict(kv.split('=') for kv in m.group(3).split())
        rows[(cur, int(m.group(1)))].append((int(m.group(2)), {k: float(v)/W for k, v in vals.items()}))
# exact block counts from the long scan
obsD = {}
for line in open('hist_1e11.txt'):
    p = line.split()
    if p[0] != 'D': continue
    j = int(p[1]); h = {int(a): int(b) for a, b in (q.split(':') for q in p[3:])}
    obsD[j] = h
def obs_le(j, d): return sum(c for dd, c in obsD.get(j, {}).items() if dd <= d)
print(" j | d2 SEMI13/blk | d4 SEMI13 | d8 SEMI13 / SEMI31 / obs | d12 SEMI31 / obs | d16 SEMI31 / SEMI97 / obs")
pts = []
for j in range(20, 37):
    out = [f"{j:2d}"]
    blk = 2**j
    for d, models in [(2, ['SEMI_y13']), (4, ['SEMI_y13']), (8, ['SEMI_y13', 'SEMI_y31']), (12, ['SEMI_y31']), (16, ['SEMI_y31', 'SEMI_y97'])]:
        r = rows[(j, d)]
        vals = [blk*sum(x[1][mdl] for x in r)/len(r) for mdl in models]
        s = " / ".join(f"{v:.3g}" for v in vals)
        if d >= 8 and j <= 35: s += f" / {obs_le(j, d)}" + ("(partial)" if j == 35 else "")
        out.append(s)
        if d == 2: pts.append((j, vals[0]))
    print(" | ".join(out))
def fit(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    b = sum((x-mx)*(y-my) for x, y in zip(xs, ys))/sum((x-mx)**2 for x in xs); return my-b*mx, b
good = [(j, c) for j, c in pts if c > 0]
for name, f in [('(log x)^0.69', lambda j: (j*math.log(2))**0.69), ('log x', lambda j: j*math.log(2))]:
    a, b = fit([f(j) for j, _ in good], [math.log(c) for _, c in good])
    t37 = sum(math.exp(a+b*f(j)) for j in range(37, 600)); t73 = sum(math.exp(a+b*f(j)) for j in range(73, 600))
    print(f"fit vs {name}: slope {b:.3f}; tail [2^37,inf) = {t37:.2e}; tail [2^73,inf) = {t73:.2e}")
print("sum over blocks 20..36 of SEMI_y13 delta=2 expectation:", f"{sum(c for _, c in pts):.2e}")
