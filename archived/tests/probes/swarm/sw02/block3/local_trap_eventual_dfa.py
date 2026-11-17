#!/usr/bin/env python3
"""local_trap_eventual_dfa.py (Local, 9 November 2026; L1611 S-16 block): the exact eventual gap language of the gate
trap at width W, as a fully explored deterministic automaton, with a numerical entropy estimate and minimal forbidden words.

Usage: python3 local_trap_eventual_dfa.py KIT_DIR GMAX W [W ...]

For each W: the lift (windows of columns 1..W whose first 16 columns are a window of the kit's trap; closed, column
W + 1 free), its recurrent core C (the stable set of black windows after gaps of 3 and 5), the windows reachable from
C (all double steps), and the automaton whose states are the path sets reached from C by gap words. It prints:
- the automaton's size and a finite-length estimate of entropy per sample: the growth rate of the number of accepted gap words by
  sample length, by a count over states to sample length 4000 (gaps 3 and 5 as transitions of length 3 and 5);
- the minimal forbidden words up to GMAX gaps (forbidden, but the word minus its first gap and the word minus its
  last gap are accepted), each also written as its runs of 5 between consecutive 3s.

PREDICTION (L1611 P-L1, before this probe ran): exact entropy 0.13246 at 16, 0.12707 at 18 to 22, between 0.124 and
0.127 at 24 and 26, above 0.12 at 28, decline below 0.002 bit per width step. Counterfactual: a drop above 0.005 in
one step.
First runs (widths 16 to 26, started 20:30:27 and 20:30:36 UTC): P-L1 HELD. Exact entropy 0.132464 (16), 0.127066 (18,
20, 22), 0.126938 (24), 0.125499 (26); automata of 9, 29, 44, 68, 366, 1326 states. Beyond 33, 3553, 3535353, width 24
has 18 new minimal words of 20 to 30 gaps, width 26 has 110 of 14 to 30 gaps.

LAW GUESS AND WIDTH-28 PREDICTION, written at 20:32 UTC before width 28 runs. In the run alphabet (runs of 5 between
consecutive 3s), the width-18 language is runs in {1, 3, 4, 5, ...} with no three 1s in a row. Every one of the 128
new minimal words at 24 and 26 contains a run of at least four next to a run of one. Guess G1: that holds for every
new minimal word at width 28 as well (the new constraints all tie a long run to an isolated 353). Also: entropy at 28
between 0.1235 and 0.1255; the automaton between 3,000 and 8,000 states; the shortest new word at most 14 gaps.
Counterfactual: a new word at 28 with no run of four or more next to a run of one, which kills G1.
Width 28 (started after that, 6.3 s): G1 HELD on all 101 new minimal words up to 24 gaps; automaton 3,319 states
(HELD); shortest new words 12 gaps, 353555535353 and 553535555353, the SW02 backlog candidates (HELD); entropy
0.122174, a drop of 0.0033 (MISSED the 0.1235-0.1255 range; above the stop rule's 0.002, below the 0.005 counterfactual).
"""
import math
import re
import sys
import time
from pathlib import Path

import numpy as np

KIT = Path(sys.argv[1])
GMAX = int(sys.argv[2])
WS = [int(x) for x in sys.argv[3:]]
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TRAP = np.array([int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))],
                dtype=np.int64)


def step(s, c, x, W):
    e = s | (x << W)
    return (((e << 1) | c) ^ (e | (e >> 1))) & ((1 << W) - 1)


def runs(word):
    """The runs of 5 between consecutive 3s, with the leading and trailing runs: 3553 -> [0 | 2 | 0]."""
    out, r = [], 0
    for g in word:
        if g == 5:
            r += 1
        else:
            out.append(r); r = 0
    out.append(r)
    return out


for W in WS:
    t0 = time.time()
    lift = (TRAP[:, None] | (np.arange(1 << (W - 16), dtype=np.int64)[None, :] << 16)).ravel()
    order = np.argsort(lift); sl = lift[order]
    succ = np.empty((len(lift), 4), dtype=np.int64)
    k = 0
    for a in (0, 1):
        for b in (0, 1):
            v = step(step(lift, 0, a, W), 1, b, W)
            succ[:, k] = order[np.searchsorted(sl, v)]; k += 1
    head = (lift & 1).astype(bool)

    def gap_full(S, g):
        for j in range(g):
            nxt = np.zeros(len(lift), dtype=bool)
            nxt[succ[S].ravel()] = True
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
    # windows reachable from C, and the successor table restricted to them
    seen = np.zeros(len(lift), dtype=bool); seen[C] = True
    fr = C
    while len(fr):
        nx = np.unique(succ[fr].ravel())
        nx = nx[~seen[nx]]
        seen[nx] = True; fr = nx
    R = np.flatnonzero(seen)
    pos = -np.ones(len(lift), dtype=np.int64); pos[R] = np.arange(len(R))
    sR = pos[succ[R]]
    hR = head[R]
    del succ, order, sl

    def gap(S, g):
        for j in range(g):
            nxt = np.zeros(len(R), dtype=bool)
            nxt[sR[S].ravel()] = True
            S = np.flatnonzero(nxt & (hR == (j == g - 1)))
            if len(S) == 0:
                break
        return S.astype(np.int32)

    start = pos[C].astype(np.int32)
    ids = {start.tobytes(): 0}
    trans = []                      # trans[i] = (id after 3, id after 5), -1 dead
    stack = [start]
    order_ids = [0]
    while stack:
        S = stack.pop()
        i = ids[S.tobytes()]
        row = []
        for g in (3, 5):
            T = gap(S, g)
            if len(T) == 0:
                row.append(-1); continue
            key = T.tobytes()
            if key not in ids:
                ids[key] = len(ids); stack.append(T)
            row.append(ids[key])
        while len(trans) <= i:
            trans.append(None)
        trans[i] = tuple(row)
    n = len(ids)
    tr = np.array(trans, dtype=np.int64)
    # finite-length entropy estimate: counts of accepted words by sample length L (words whose gaps sum to L), kept as
    # (vector, log2 scale) for the last five lengths; lc[L] = log2 of the total count
    N = 4000
    vec = {0: (np.eye(1, n, 0).ravel(), 0.0)}
    lc = {0: 0.0}
    ok3 = tr[:, 0] >= 0; ok5 = tr[:, 1] >= 0
    for L in range(1, N + 1):
        parts = []
        for g, ok, col in ((3, ok3, 0), (5, ok5, 1)):
            if L - g in vec:
                v0, s0 = vec[L - g]
                c = np.zeros(n)
                np.add.at(c, tr[ok, col], v0[ok])
                parts.append((c, s0))
        if parts:
            s = max(p_[1] for p_ in parts)
            v = sum(p_[0] * 2.0 ** (p_[1] - s) for p_ in parts)
            m = v.max()
            if m > 0:
                e = math.floor(math.log2(m)); v = v / 2.0 ** e; s += e
                vec[L] = (v, s); lc[L] = math.log2(v.sum()) + s
        vec.pop(L - 5, None)
    a, b = N - 1000, N
    sa = max(lc.get(a - j, float('-inf')) for j in range(5))
    sb = max(lc.get(b - j, float('-inf')) for j in range(5))
    ent = (sb - sa) / (b - a)
    # minimal forbidden words up to GMAX gaps
    def run(word):
        s = 0
        for g in word:
            s = tr[s, 0 if g == 3 else 1]
            if s < 0:
                return -1
        return s
    minimal = []
    frontier = [((), 0)]
    for depth in range(GMAX):
        nf = []
        for w, s in frontier:
            for g, col in ((3, 0), (5, 1)):
                t = tr[s, col]
                v = w + (g,)
                if t < 0:
                    if run(v[1:]) >= 0:
                        minimal.append(v)
                else:
                    nf.append((v, t))
        frontier = nf
    print(f'W={W}: core {len(C)}, reachable {len(R)}, automaton {n} states, entropy {ent:.6f} bit per sample, '
          f'{time.time() - t0:.1f} s', flush=True)
    for v in minimal:
        print(f'   {len(v):2d} gaps  {"".join(map(str, v))}  runs of 5 between 3s: {runs(v)}', flush=True)
