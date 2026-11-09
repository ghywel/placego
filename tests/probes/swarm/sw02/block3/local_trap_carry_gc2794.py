#!/usr/bin/env python3
"""local_trap_carry_gc2794.py (Local, 9 November 2026): independent checks for the carrying read of GPT's GC2794 and
GC2796, with Local's own automata (local_trap_eventual_dfa.py's construction), and the width-30 test.

Usage: python3 local_trap_carry_gc2794.py KIT_DIR W [W ...]

For each width W, from the recurrent core C_W of the width-W lift:
 (a) the deterministic automaton of path sets on gap words (subset states, all explored);
 (b) GPT's pumped family at W = 24: 35553 (53535555355553)^k 535355553555353 for k = 0..6 must be forbidden with its
     proper prefix and its proper suffix (first letter deleted) accepted;
 (c) G1 at all lengths: the product of (full-word state, first-letter-deleted state, P-monitor) explored to closure.
     A completed minimal forbidden word that avoids P (no internal run of four or more 5s next to an internal run of
     one) and is not 33, 3553 or 3535353 is a counterexample, printed with its letters;
 (d) the free code {5, 3555}: the automaton on whole blocks A = 5 and B = 3555 from C_W, explored to closure; an
     empty state is a rejected code word.
 It prints the core size, the automaton size, the exact-presentation entropy slope (numerical, lengths 3000-4000),
 the G1 product size and counterexamples, and the code automaton size and rejections.

PREDICTION (written before the first run; clock read 21:48:13 UTC):
 - (b) holds for every k at W = 24 (GPT's loop and terminal check, replayed by other code).
 - (c) no counterexample at W = 24, 26, 28 (GPT's all-length G1), product sizes of the same order as GPT's 63, 167, 456
   (my subset automaton is larger than GPT's minimal one, so my product can be larger).
 - (d) no rejected code word at 16 to 28 (GPT's code automaton).
 - At W = 30, if run: G1 still has no counterexample, the code is not rejected, and the entropy slope is between
   0.115 and 0.1215 (GPT froze [0.115, 0.123] for 30; my narrower guess says the decline keeps growing).
 Counterfactuals: any failure in (b)-(d) through 28 is a disagreement with GPT to resolve before anything else; a G1
 counterexample or a rejected code word at 30 ends the 1/18 floor route at that width.
Result (16-28 started 21:48:51 UTC; 30 started 21:49:19 UTC): (b), (c), (d) HELD through 28, matching GPT exactly
(code automaton 3, 6, 8, 10, 21, 80, 298 states). At 30: slope 0.119193 (HELD), code not rejected (2,180 states, HELD),
but G1 MISSED: 10 counterexamples, shortest 355535355535353 (runs 3,1,3,1,1), and a pumped family of runs
3,1,3,1,3,4,4,5^m,6. Every counterexample contains 353; G1' below replaces G1.
"""
import math
import re
import sys
import time
from pathlib import Path

import numpy as np

KIT = Path(sys.argv[1])
WS = [int(x) for x in sys.argv[2:]]
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TRAP = np.array([int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))],
                dtype=np.int64)
F = {(3, 3), (3, 5, 5, 3), (3, 5, 3, 5, 3, 5, 3)}


def step(s, c, x, W):
    e = s | (x << W)
    return (((e << 1) | c) ^ (e | (e >> 1))) & ((1 << W) - 1)


def build(W):
    lift = (TRAP[:, None] | (np.arange(1 << (W - 16), dtype=np.int64)[None, :] << 16)).ravel()
    order = np.argsort(lift); sl = lift[order]
    succ = np.empty((len(lift), 4), dtype=np.int64); k = 0
    for a in (0, 1):
        for b in (0, 1):
            succ[:, k] = order[np.searchsorted(sl, step(step(lift, 0, a, W), 1, b, W))]; k += 1
    head = (lift & 1).astype(bool)
    del order, sl

    def gap_full(S, g):
        for j in range(g):
            nxt = np.zeros(len(lift), dtype=bool); nxt[succ[S].ravel()] = True
            S = np.flatnonzero(nxt & (head == (j == g - 1)))
            if len(S) == 0:
                break
        return S
    B = np.flatnonzero(head)
    while True:
        B2 = np.union1d(gap_full(B, 3), gap_full(B, 5))
        if len(B2) == len(B):
            break
        B = B2
    C = B
    seen = np.zeros(len(lift), dtype=bool); seen[C] = True; fr = C
    while len(fr):
        nx = np.unique(succ[fr].ravel()); nx = nx[~seen[nx]]; seen[nx] = True; fr = nx
    R = np.flatnonzero(seen)
    pos = -np.ones(len(lift), dtype=np.int64); pos[R] = np.arange(len(R))
    sR = pos[succ[R]]; hR = head[R]
    return C, pos[C].astype(np.int32), sR, hR, len(lift), len(R)


def gap(S, g, sR, hR):
    for j in range(g):
        nxt = np.zeros(len(hR), dtype=bool); nxt[sR[S].ravel()] = True
        S = np.flatnonzero(nxt & (hR == (j == g - 1)))
        if len(S) == 0:
            break
    return S.astype(np.int32)


def automaton(start, letters, sR, hR):
    """Subset automaton from `start` on `letters` (each a tuple of gaps read as one letter)."""
    ids = {start.tobytes(): 0}; trans = {}; stack = [start]
    while stack:
        S = stack.pop(); i = ids[S.tobytes()]; row = []
        for lt in letters:
            T = S
            for g in lt:
                T = gap(T, g, sR, hR)
                if len(T) == 0:
                    break
            if len(T) == 0:
                row.append(-1); continue
            key = T.tobytes()
            if key not in ids:
                ids[key] = len(ids); stack.append(T)
            row.append(ids[key])
        trans[i] = row
    return np.array([trans[i] for i in range(len(ids))], dtype=np.int64)


def slope(tr):
    n = len(tr); N = 4000; vec = {0: (np.eye(1, n, 0).ravel(), 0.0)}; lc = {}
    for L in range(1, N + 1):
        parts = []
        for g, col in ((3, 0), (5, 1)):
            if L - g in vec:
                v0, s0 = vec[L - g]; ok = tr[:, col] >= 0
                c = np.zeros(n); np.add.at(c, tr[ok, col], v0[ok]); parts.append((c, s0))
        if parts:
            s = max(p[1] for p in parts); v = sum(p[0] * 2.0 ** (p[1] - s) for p in parts); m = v.max()
            if m > 0:
                e = math.floor(math.log2(m)); v = v / 2.0 ** e; s += e; vec[L] = (v, s); lc[L] = math.log2(v.sum()) + s
        vec.pop(L - 5, None)
    a, b = N - 1000, N
    return (max(lc.get(b - j, -1e9) for j in range(5)) - max(lc.get(a - j, -1e9) for j in range(5))) / (b - a)


def monitor(m, g):
    """P-monitor: m = (matched, seen3, prev_run or -1, cur_run capped at 4)."""
    matched, seen3, prev, cur = m
    if matched:
        return m
    if g == 5:
        return (False, seen3, prev, min(cur + 1, 4))
    if seen3:
        r = cur
        if prev >= 0 and ((prev >= 4 and r == 1) or (prev == 1 and r >= 4)):
            return (True, True, r, 0)
        return (False, True, r, 0)
    return (False, True, -1, 0)


def g1_product(tr):
    col = {3: 0, 5: 1}
    m0 = (False, False, -1, 0)
    start = []
    for x in (3, 5):
        p = tr[0, col[x]]
        if p >= 0:
            start.append(((int(p), 0, monitor(m0, x)), (x,)))
    seen = {s for s, _ in start}; todo = list(start); bad = []
    while todo:
        (p, s, m), w = todo.pop()
        for y in (3, 5):
            p2 = tr[p, col[y]]; s2 = tr[s, col[y]]; m2 = monitor(m, y); w2 = w + (y,)
            if p2 < 0:
                if s2 >= 0 and not m2[0] and w2 not in F:
                    bad.append(''.join(map(str, w2)))
                continue
            if m2[0]:
                continue
            st = (int(p2), int(s2), m2)
            if st not in seen:
                seen.add(st); todo.append((st, w2))
    return len(seen), bad


def run(tr, word):
    s = 0
    for g in word:
        s = tr[s, 0 if g == 3 else 1]
        if s < 0:
            return -1
    return s


for W in WS:
    t0 = time.time()
    C, start, sR, hR, nl, nr = build(W)
    tr = automaton(start, [(3,), (5,)], sR, hR)
    out = [f'W={W}: lift {nl}, core {len(C)}, reachable {nr}, automaton {len(tr)} states, slope {slope(tr):.6f}']
    if W == 24:
        res = []
        for k in range(7):
            w = [3, 5, 5, 5, 3] + [5, 3, 5, 3, 5, 5, 5, 5, 3, 5, 5, 5, 5, 3] * k + [5, 3, 5, 3, 5, 5, 5, 5, 3, 5, 5, 5, 3, 5, 3]
            res.append(run(tr, w) < 0 and run(tr, w[:-1]) >= 0 and run(tr, w[1:]) >= 0)
        out.append(f'   pumped family k=0..6 minimal forbidden: {res}')
    nps, bad = g1_product(tr)
    out.append(f'   G1 all-length product: {nps} states, counterexamples {bad[:5]} ({len(bad)})')
    code = automaton(start, [(5,), (3, 5, 5, 5)], sR, hR)
    out.append(f'   free code {{5, 3555}}: {len(code)} states, rejections {int((code < 0).sum())}; {time.time() - t0:.1f} s')
    print('\n'.join(out), flush=True)
