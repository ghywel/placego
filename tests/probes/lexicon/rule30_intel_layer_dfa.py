#!/usr/bin/env python3
"""rule30_intel_layer_dfa.py: the width-m layer automaton of column 1 (the free exterior's visible words, 8.14, 8.20,
8.41) for the forced-only engine of rule30_intel_forced_only.py, by a vectorised subset construction.
Layer: sites 1..m beside the alternating wall, site m+1 fed an arbitrary bit each step; one visible step is two time
steps (white tick then black tick) and the visible bit is column 1 at the white tick; phase 0 reads at even t (every
layer row is a start), phase 1 at odd t (the starts are the images of every row under one black-tick step). The NFA
state is the layer row at a white tick; the DFA state is a set of rows, kept as a packed bitset of the 2^m rows and
keyed by a 128-bit digest. Output: 'n_states' then one line 'next0 next1' per state (-1: no transition), start 0.
Growth rate (bits per visible bit) by power iteration on A + I, and by dense eigenvalues up to 3000 states.
Controls: widths 8 and 12 give 56/60 and 402/407 states (phase 0/1) and 0.35621, 0.25784, the record's values and
state counts; width 16 gives 2,260 states (the record's count) and 0.21158 under the certified bound 0.2130.
Usage: python3 rule30_intel_layer_dfa.py m phase out.dfa     (width 20: about three minutes, 12,749 states)"""
import sys, time, hashlib
import numpy as np

def build(m, phase):
    N = 1 << m; mask = N - 1
    n = np.arange(N, dtype=np.int64)
    def step(x, wall, ext):
        L = ((x << 1) | wall) & mask           # left neighbours (site 1 sees the wall)
        R = (x >> 1) | (ext << (m - 1))        # right neighbours (site m sees the exterior bit)
        return L ^ (x | R)
    img = [step(step(n, 0, e1), 1, e2) for e1 in (0, 1) for e2 in (0, 1)]   # white tick then black tick
    col1 = (n & 1).astype(bool)
    if phase == 0:
        start = np.ones(N, dtype=bool)
    else:
        start = np.zeros(N, dtype=bool)
        for e in (0, 1): start[step(n, 1, e)] = True
    def key(S): return hashlib.blake2b(np.packbits(S).tobytes(), digest_size=16).digest()
    states = {key(start): 0}; queue = [np.packbits(start)]; trans = []
    i = 0; t0 = time.time()
    while i < len(queue):
        S = np.unpackbits(queue[i], count=N).astype(bool); row = []
        for b in (0, 1):
            sel = np.flatnonzero(S & (col1 if b else ~col1))
            if sel.size == 0: row.append(-1); continue
            T = np.zeros(N, dtype=bool)
            for e in range(4): T[img[e][sel]] = True
            kk = key(T)
            if kk not in states: states[kk] = len(queue); queue.append(np.packbits(T))
            row.append(states[kk])
        trans.append(row); i += 1
        if i % 2000 == 0: print(f"  {i} states processed, {len(queue)} found, {time.time() - t0:.0f} s", file=sys.stderr)
    return trans

def growth(trans):
    n = len(trans)
    src = np.array([i for i, r in enumerate(trans) for j in r if j >= 0]); dst = np.array([j for r in trans for j in r if j >= 0])
    v = np.ones(n); lam = 0.0
    for it in range(20000):
        w = v.copy(); np.add.at(w, src, v[dst])          # w = (A + I) v
        lam2 = float(w @ v / (v @ v)); v = w / np.linalg.norm(w)
        if it > 50 and abs(lam2 - lam) < 1e-12: lam = lam2; break
        lam = lam2
    out = {'power': float(np.log2(lam - 1)), 'iterations': it + 1}
    if n <= 3000:
        A = np.zeros((n, n))
        for i, r in enumerate(trans):
            for j in r:
                if j >= 0: A[i, j] += 1
        out['dense'] = float(np.log2(max(abs(np.linalg.eigvals(A)))))
    return out

if __name__ == '__main__':
    m, phase, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    t0 = time.time(); trans = build(m, phase); tb = time.time() - t0
    with open(out, 'w') as f:
        f.write(f"{len(trans)}\n")
        for row in trans: f.write(f"{row[0]} {row[1]}\n")
    g = growth(trans)
    print(f"m={m} phase={phase}: {len(trans)} DFA states in {tb:.1f} s, growth {g} bits per visible bit -> {out}")
