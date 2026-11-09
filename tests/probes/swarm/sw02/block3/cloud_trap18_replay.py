# Third replay (Cloud, CL760) of L1608's 18-column lift: the 829 trap windows extended by columns 17, 18 (3,316 windows),
# the double step with column 19 free at both ticks; closure, and the path sets of 3535353 (27 samples) and the five words.
import sys
codes = [int(x) for x in open(sys.argv[1]).read().split()]; T16 = set(codes)
W = 18
T18 = {w | (a << 16) | (b << 17) for w in codes for a in (0, 1) for b in (0, 1)}
def tick(cells, c):
    n = len(cells); return [(c if i == 0 else cells[i-1]) ^ (cells[i] | cells[i+1]) for i in range(n - 1)]
def step2(w, x1, x2):
    cells = [(w >> i) & 1 for i in range(W)] + [x1]
    e = tick(cells, 0) + [x2]
    o = tick(e, 1)
    return sum(b << i for i, b in enumerate(o))
succ = {}; bad = 0
for w in T18:
    succ[w] = {step2(w, x1, x2) for x1 in (0, 1) for x2 in (0, 1)}
    bad += sum(1 for v in succ[w] if v not in T18)
print(f"18-column lift: {len(T18)} windows, closure violations {bad}; every 18-window's low 16 bits in the 16-trap: {all((w & 0xFFFF) in T16 for w in T18)}")
def pathsets(bits):
    layer = {w for w in T18 if (w & 1) == bits[0]}; sizes = [len(layer)]
    for b in bits[1:]:
        layer = {v for w in layer for v in succ[w] if (v & 1) == b}; sizes.append(len(layer))
        if not layer: break
    return sizes
def bits_of_gaps(g):
    u = [0] * (sum(g) + 1); p = 0; u[0] = 1
    for x in g: p += x; u[p] = 1
    return u
for name, g in (("3535353", [3,5,3,5,3,5,3]), ("333", [3,3,3]), ("3353", [3,3,5,3]), ("3533", [3,5,3,3]), ("3553", [3,5,5,3]), ("5533", [5,5,3,3]), ("35353", [3,5,3,5,3]), ("535353", [5,3,5,3,5,3]), ("5555", [5,5,5,5]), ("35", [3,5])):
    s = pathsets(bits_of_gaps(g)); print(f"  {name}: layers {s[-6:]}{' DIES' if s[-1]==0 else ' survives'} ({len(s)} layers)")
# the 16-column graph keeps 3535353 alive (L1608: 47 final windows)
succ16 = {w: {None} for w in codes}
def step2_16(w, x1, x2):
    cells = [(w >> i) & 1 for i in range(16)] + [x1]; e = tick(cells, 0) + [x2]; o = tick(e, 1); return sum(b << i for i, b in enumerate(o))
succ16 = {w: {step2_16(w, x1, x2) for x1 in (0,1) for x2 in (0,1)} for w in codes}
layer = {w for w in codes if (w & 1) == 1}
for b in bits_of_gaps([3,5,3,5,3,5,3])[1:]:
    layer = {v for w in layer for v in succ16[w] if (v & 1) == b}
print(f"16-column graph, 3535353 final layer: {len(layer)} windows (L1608: 47)")
