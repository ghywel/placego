#!/usr/bin/env python3
"""L1446 (Local, 2026-11-03): GC2545's request. The shortest input word that empties A4's one-way window from a settled slow
wall's actual state on 1010000. Run: python3 tests/probes/wolfram/a4_emptying_word.py DATA63.json T0 PATTERN W OUT.json
Breadth-first over both values of the cell beyond the window (A4's transitions) from PATTERN's anchored state at T0; the first
state with a successor that loses its difference ends a shortest emptying word. Exports the start state, the input word, every
state and move on the path, and the actual inputs the real evolution supplied over the same ticks (to compare). Also the fair
null for L1444: per shuffle, the same maximum over 63 rotations.
"""
import json
import sys
from collections import deque

import numpy as np

data = json.load(open(sys.argv[1])); T0 = int(sys.argv[2]); PAT = int(sys.argv[3], 0); W = int(sys.argv[4]); OUT = sys.argv[5]
orb = [tuple(o) for o in data['orb']]; q = len(orb); N = data['N']; r0, s0 = data['r'], data['s']
rule = lambda a, b, c: a ^ (b | c)
E = lambda x, t: orb[(t + s0) % q][((t - x) + r0) % N]


def step1(state, b):
    tq, dq, strip = state; L = len(strip)
    Eb = lambda i, dt=0: orb[(tq + dt + s0) % q][((dq + dt - i) + r0) % N]
    cell = lambda i: Eb(i) if i <= 0 else (strip[i - 1] if i <= L else b)
    new = {i: rule(cell(i - 1), cell(i), cell(i + 1)) for i in range(0, L + 1)}
    if new[0] != Eb(0, 1):
        ns = tuple(new[i] for i in range(0, L)); ndq = (dq + 2) % N; mv = -1
    else:
        ns = tuple(new[i] for i in range(1, L + 1)); ndq = (dq + 1) % N; mv = 0
    Enew = lambda i: orb[(tq + 1 + s0) % q][((ndq - i) + r0) % N]
    alive = any(ns[i] != Enew(i + 1) for i in range(len(ns)))
    return ((tq + 1) % q, ndq, ns), mv, alive


TM = T0 + 400; lo = -2 * TM - 10; hi = TM + 22; c = -lo
row = np.array([E(x, 0) for x in range(lo, hi)], dtype=np.uint8); bg = row.copy()
for i in range(12):
    row[c + i] ^= (PAT >> i) & 1
rows = {}
for t in range(1, TM + 1):
    n = np.zeros_like(row); n[1:-1] = row[:-2] ^ (row[1:-1] | row[2:]); row = n
    m = np.zeros_like(bg); m[1:-1] = bg[:-2] ^ (bg[1:-1] | bg[2:]); bg = m
    if t >= T0:
        rows[t] = (row.copy(), bg.copy())
X, B = rows[T0]; Fi = int(np.flatnonzero(X ^ B).min()); A = Fi - 1 - c
assert Fi - 1 > TM + 1 and Fi + W + 400 < len(row) - TM - 1
start = (T0 % q, (T0 - A) % N, tuple(int(v) for v in X[Fi: Fi + W]))
# the actual inputs: follow the real evolution with the one-way anchor; input at tick t is the cell A(t) + W + 1 at time t
act = []; st = start; Aa = A
for t in range(T0, T0 + 400):
    Xt = rows[t][0]; b = int(Xt[c + Aa + W + 1]); act.append(b)
    nst, mv, alive = step1(st, b)
    Xn = rows[t + 1][0]; Aa += mv
    assert nst[2] == tuple(int(v) for v in Xn[c + Aa + 1: c + Aa + 1 + W]), 'window replay mismatch'
    assert alive
    st = nst
print('pattern %d at T0=%d, W=%d: actual-evolution replay of 400 ticks through the window: consistent, never empty' % (PAT, T0, W))
seen = {start: None}; dq_ = deque([start]); found = None; nproc = 0
while dq_ and found is None:
    s_ = dq_.popleft(); nproc += 1
    for b in (0, 1):
        nst, mv, alive = step1(s_, b)
        if not alive:
            found = (s_, b); break
        if nst not in seen:
            seen[nst] = (s_, b, mv); dq_.append(nst)
        if mv == -1:
            break  # a retreat does not read the cell beyond the window
if found is None:
    print('no emptying word: closure of %d states' % len(seen)); sys.exit()
path = []; s_ = found[0]
while seen[s_] is not None:
    prv, b, mv = seen[s_]; path.append((prv, b, mv)); s_ = prv
path.reverse()
word = [b for _, b, _ in path] + [found[1]]
enc = lambda st: [st[0], st[1], ''.join(map(str, st[2]))]
print('shortest emptying word: length %d (after %d states processed): %s' % (len(word), nproc, ''.join(map(str, word))))
print('the actual evolution\'s inputs over the same %d ticks:         %s' % (len(word), ''.join(map(str, act[:len(word)]))))
agree = sum(1 for i in range(len(word)) if word[i] == act[i])
first = next((i for i in range(len(word)) if word[i] != act[i]), None)
print('agreement with the actual inputs: %d of %d; first difference at tick %s' % (agree, len(word), first))
json.dump({'pattern': PAT, 'T0': T0, 'W': W, 'start': enc(start), 'word': word, 'actual_inputs': act[:len(word)],
           'path': [[enc(s_), b, mv] for s_, b, mv in path] + [[enc(found[0]), found[1], None]]}, open(OUT, 'w'))
print('wrote %s (kept outside git)' % OUT.rsplit('/', 1)[-1])
