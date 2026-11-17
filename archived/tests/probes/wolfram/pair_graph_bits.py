#!/usr/bin/env python3
"""Local, 2026-10-28 (L1066): complete right-diagonal pair graph at a dyadic cap P, bit-packed.

Independent of GPT's right_period_graph.py. A state is (a, b) = (D_(d-1), D_d) over exactly P ticks, each packed in a
P-bit integer (bit t = value at time t). Start (0, all ones). The forcing is g = a OR b; odd popcount exits to period
2P. Otherwise the two children are (b, c) with c(t) = s XOR (XOR of g over ticks < t), s in {0, 1}. Breadth-first
closure is exact for every row whose diagonals all have period dividing P (every 2-adic code: start bits are free).
Reports states, exits, period drops (least period of c below that of b), every cyclic strongly connected component,
and the longest path above period 2 before an exit. Also prints a witness: the start bits of a longest path from the start (to the first exit), as a finite seed read
from the right edge inward, and the longest plateau at each period q <= P (consecutive diagonals with largest period
exactly q, free start bits). Usage: pair_graph_bits.py P
"""
import sys, collections
P = int(sys.argv[1]); M = (1 << P) - 1
def prefix_excl(g):  # bit t = XOR of g bits 0..t-1
    y = (g << 1) & M; k = 1
    while k < P: y ^= (y << k) & M; k <<= 1
    return y
def lp(x):
    n = P
    while n > 1:
        h = n // 2; lo = x & ((1 << h) - 1)
        if ((x >> h) & ((1 << h) - 1)) == lo and all(((x >> (i * h)) & ((1 << h) - 1)) == lo for i in range(P // h)): n = h; x = x
        else: break
    return n
start = (0, M)
idx = {start: 0}; order = [start]; succ = []; exits = 0; drops = []
i = 0
while i < len(order):
    a, b = order[i]; i += 1
    g = a | b
    if bin(g).count("1") & 1: succ.append(None); exits += 1; continue
    base = prefix_excl(g); kids = []
    for s in (0, M):
        c = base ^ s; v = (b, c)
        if lp(b) > 1 and lp(c) < lp(b): drops.append((a, b, c))
        if v not in idx: idx[v] = len(order); order.append(v)
        kids.append(idx[v])
    succ.append(kids)
n = len(order)
# iterative Tarjan for cyclic SCCs
index = [-1] * n; low = [0] * n; onst = [False] * n; st = []; comps = []; cnt = 0
for r in range(n):
    if index[r] != -1: continue
    work = [(r, 0)]; index[r] = low[r] = cnt; cnt += 1; st.append(r); onst[r] = True
    while work:
        v, k = work[-1]; kids = succ[v] or []
        if k < len(kids):
            work[-1] = (v, k + 1); w = kids[k]
            if index[w] == -1:
                index[w] = low[w] = cnt; cnt += 1; st.append(w); onst[w] = True; work.append((w, 0))
            elif onst[w]: low[v] = min(low[v], index[w])
        else:
            work.pop()
            if work: low[work[-1][0]] = min(low[work[-1][0]], low[v])
            if low[v] == index[v]:
                comp = []
                while True:
                    w = st.pop(); onst[w] = False; comp.append(w)
                    if w == v: break
                if len(comp) > 1 or v in (succ[v] or []): comps.append(comp)
cyc = set(x for c in comps for x in c)
# longest path (in diagonals) among states with lp(b) > 2, ending at an exit; graph outside cycles is a DAG
memo = {}
sys.setrecursionlimit(1000000)
def longest(v):
    if v in memo: return memo[v]
    best = 0
    for w in succ[v] or []:
        if w in cyc: continue
        best = max(best, 1 + longest(w))
    memo[v] = best; return best
above = [v for v in range(n) if v not in cyc and lp(order[v][1]) > 2]
L = max((longest(v) for v in above), default=0)
print(f"P={P}: states {n}, exits {exits}, period drops {len(drops)}, cyclic components {len(comps)}"
      f" (sizes {[len(c) for c in comps]}), longest stretch above period 2: {L + 1} diagonals")
for c in comps: print("  cycle:", [(lp(order[v][0]), lp(order[v][1])) for v in c])

# witness: longest path from the start through non-cycle states (cycle states may be traversed at most once each)
memo2 = {}
def far(v, depth=0):
    if v in memo2: return memo2[v]
    best = (0, None)
    for k, w in enumerate(succ[v] or []):
        if w in cyc and v in cyc: continue
        r = far(w)[0] + 1
        if r > best[0]: best = (r, k)
    memo2[v] = best; return best
v = 0; bits = []
while succ[v]:
    r, k = far(v)
    if k is None: break
    bits.append(k); v = succ[v][k]
print("witness seed (cells 0, -1, -2, ... from the right edge):", "1" + "".join(map(str, bits)), "length", len(bits) + 1)

# longest plateau at each period q: longest run of consecutive states whose newer diagonal b has period exactly q,
# among states reachable with all earlier periods <= q (monotone: the running maximum equals lp(b) by no-drop)
memo3 = {}
def run(v, q):
    key = (v, q)
    if key in memo3: return memo3[key]
    best = 1
    for w in succ[v] or []:
        if w in cyc: continue
        if lp(order[w][1]) == q: best = max(best, 1 + run(w, q))
    memo3[key] = best; return best
for q in [2 ** e for e in range(2, P.bit_length())]:
    if q > P: break
    vs = [v for v in range(n) if v not in cyc and lp(order[v][1]) == q]
    print(f"  longest plateau at period {q}: {max((run(v, q) for v in vs), default=0)} diagonals")
