#!/usr/bin/env python3
"""closed_set.py NAME P S WLIST [NALIGN|-] [CAP]: the closed-set (wall-trap) certificate for the inserted edge's front law
x_B(t+P) = x_B(t) + S - P on a ring background. Cloud, Block 24. See PREDICTIONS Block 24 for the statement."""
import sys, numpy as np
from collections import deque
name, P, S = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); WLIST = [int(w) for w in sys.argv[4].split(',')]
NAL = int(sys.argv[5]) if len(sys.argv) > 5 and sys.argv[5] != '-' else None
CAP = int(sys.argv[6]) if len(sys.argv) > 6 else 60000
WORDS = {'G8': '1000', 'c7_28': '1000000', 's7_63': '1010000', 's9_57': '100100000', 's12_68': '100100000000'}
y = np.array([int(c) for c in WORDS[name]], dtype=np.uint8); N = len(y)
def cst(s): return s ^ (np.roll(s, 1) | np.roll(s, 2))
orb = [y.copy()]; cur = cst(y)
while not np.array_equal(cur, y): orb.append(cur.copy()); cur = cst(cur)
orb = [tuple(int(v) for v in o) for o in orb]; q = len(orb)
def rule(a, b, c): return a ^ (b | c)
def E(x, t, r, s): return orb[(t + s) % q][((t - x) + r) % N]
def step(rw):
    n = np.zeros_like(rw); n[1:-1] = rw[:-2] ^ (rw[1:-1] | rw[2:]); return n
def transitions(state, r, s, W):
    """Lowry's anchor: the window's left column moves left only when its own cell becomes a mismatch (a retreat, one successor,
    no branch); otherwise it stays and the strip's far cell needs the cell beyond (two successors). Returns [(newstate, motion)],
    or None if the strip holds no mismatch (the front is beyond the window)."""
    (tq, dq, strip) = state; L = len(strip)          # dq = (t - x_B) mod N: the ether's phase at the anchor
    def Eb(i, dt=0): return orb[(tq + dt + s) % q][((dq + dt - i) + r) % N]
    outs = []
    for b in (0, 1):
        def cell(i):
            if i <= 0: return Eb(i)
            if i <= L: return strip[i - 1]
            return b
        new = {i: rule(cell(i - 1), cell(i), cell(i + 1)) for i in range(0, L + 1)}
        if new[0] != Eb(0, 1):
            ns = tuple(new[i] for i in range(0, L)); ndq = (dq + 2) % N; mv = -1          # retreat, independent of b
        else:
            ns = tuple(new[i] for i in range(1, L + 1)); ndq = (dq + 1) % N; mv = 0
        def Enew(i): return orb[(tq + 1 + s) % q][((ndq - i) + r) % N]
        if not any(ns[i] != Enew(i + 1) for i in range(len(ns))): return None   # no mismatch in the window
        outs.append((((tq + 1) % q, ndq, ns), mv))
        if mv == -1: break
    return outs
def certify(r, s, t0, W, T):
    # the real state at t0: simulate
    WL = 2*T + 100; WR = T + 60; c = WL
    bg = np.array([E(x, 0, r, s) for x in range(-WL, WR)], dtype=np.uint8); pert = bg.copy(); pert[c] = 1; pert[c+1:] = 0
    a, bb = bg.copy(), pert.copy()
    for t in range(t0): a, bb = step(a), step(bb)
    d = np.flatnonzero(a ^ bb); xmin = int(d.min()) - c; xB = xmin - 1
    strip = tuple(int(v) for v in bb[c + xB + 1: c + xB + 1 + W])
    # start witness (GC2402, CL687): the truncated simulation is exact on [-(WL - t0), WR - t0) at t0; the anchor must lie at
    # x >= -(t0 + 1) by causality, the window must end inside the exact region, and the real row must equal the background's
    # analytic value on the whole exact region left of the anchor (the certificate's matching half-line premise)
    assert xB >= -(t0 + 1) and xB + W < WR - t0, (xB, W, t0)
    assert all(int(bb[c + x]) == E(x, t0, r, s) for x in range(-(WL - t0), xB + 1)), "left half-line differs from the background at t0"
    if NAL is not None and NAL <= 8: print(f"  start witness: t0={t0} anchor A={xB} W={W} exact region [{-(WL - t0)},{WR - t0}) half-line [{-(WL - t0)},{xB}] equals E", flush=True)
    start = (t0 % q, (t0 - xB) % N, strip)
    # closure
    seen = {start: 0}; dq = deque([start]); edges = {}
    while dq:
        st = dq.popleft()
        outs = transitions(st, r, s, W)
        if outs is None: return ('undetermined', len(seen), st)
        for nst, mv in outs:
            if nst not in seen:
                seen[nst] = len(seen)
                if len(seen) > CAP: return ('exceeded cap', len(seen), None)
                dq.append(nst)
        edges[st] = outs
    # the law: every path of length P from every state moves the boundary by exactly S - P
    target = S - P
    # DP: motion ranges over paths of length n
    # recurrent part: states reachable from the start after K steps (forward-closed); the real trajectory is there from t0 + K on
    K = len(seen); front = {start}
    for _ in range(K):
        front = {nst for st in front for nst, mv in edges[st]}
    rec = set(front)
    while True:
        more = {nst for st in rec for nst, mv in edges[st]} - rec
        if not more: break
        rec |= more
    rng = {st: (0, 0) for st in rec}
    for n in range(P):
        new = {}
        for st in rec:
            outs = edges[st]
            lo = min(rng[nst][0] + mv for nst, mv in outs); hi = max(rng[nst][1] + mv for nst, mv in outs)
            new[st] = (lo, hi)
        rng = new
    bad = [st for st, (lo, hi) in rng.items() if (lo, hi) != (target, target)]
    return ('PASS' if not bad else 'law fails', len(seen), (len(rec), len(bad)))
T = 400
res_by_al = {}
als = [(r, s) for r in range(N) for s in range(q)]
if NAL: 
    rng_ = np.random.default_rng(1); als = [als[i] for i in rng_.choice(len(als), NAL, replace=False)]
from collections import Counter
summary = Counter(); sizes = []
for (r, s) in als:
    verdict = None
    for W in WLIST:
        v, size, info = certify(r, s, 300, W, T)
        if v == 'PASS': verdict = (W, size, info[0]); break
    summary[verdict is not None] += 1
    res_by_al[(r, s)] = verdict if verdict else (v, size, info)
    if verdict: sizes.append((W, size))
print(f"{name} law (P,S)=({P},{S}), lab speed {(P-S)/P:.4f}; widths {WLIST}; closure cap {CAP}; alignments tried {len(als)}; certified {summary[True]}, not certified {summary[False]}")
if sizes: print("  closure sizes (W, states) for certified alignments: min", min(sizes, key=lambda x: x[1]), "max", max(sizes, key=lambda x: x[1]), "distinct", sorted(set(sizes))[:12])
fails = [(k, v) for k, v in res_by_al.items() if not isinstance(v[0], int)]
print("  not certified (first 6):", [(k, v[0], v[1]) for k, v in fails[:6]])
print("CLOSED_SET_DONE")
