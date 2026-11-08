#!/usr/bin/env python3
"""Lock family, step 2 (Local, 8 November 2026): right halves near the two period-7 locks.
Usage: neighbours.py BN13_DIR KIT_DIR N SEED
For a lock with witness R, take its row at a late odd tick T (window in the lock), keep columns 1..k, set columns
k+1..k+200 uniformly at random (white beyond), run on with the same drive to tick T + 6000, and classify the end:
lock7 / lock7b / lock5 (window at an odd tick in the set; checked over the last 140 ticks), trap (16-column window in
the kit's gate trap and no such lock), period 2 (u of period 2 on the last 1000 steps), or CANDIDATE (a periodic u,
period 5 or 7 or other, in none of the known sets).
Prediction, written before the run: (controls) k = 45 for lock-7b and k = 30 for lock-7 give 100 % re-entry, since the
locks are closed at those widths. (main) Re-entry falls off quickly below the closed width; most samples go to the
trap; lock-7 is reached from lock-7b's neighbourhood for small k; P(at least one CANDIDATE among all samples) = 0.3.
Counterfactual: candidates appear; each then gets a forward closure test at widths up to 80 before any claim."""
import random, re, sys
bn, kit, N, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
def step(x, t): return ((x << 1) | (1 if t % 2 == 0 else 0)) ^ (x | (x >> 1))
def ints(p): return set(int(x) for x in open(p).read().split())
L7, L7b, L5 = ints(bn + '/lock7.txt'), ints(bn + '/lock7_w45.txt'), ints(bn + '/lock5.txt')
src = open(kit + '/lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read()
TRAP = set(int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1)))
M = lambda w: (1 << w) - 1
def classify(x, t0, H=6000):
    t = t0; us = []
    for i in range(H):
        x = step(x, t); t += 1
        if t % 2 == 1: us.append(x & 1)
    # last 140 ticks: membership at odd ticks
    tags = set(); per = None
    for i in range(140):
        if t % 2 == 1:
            if (x & M(30)) in L7: tags.add('lock7')
            if (x & M(45)) in L7b: tags.add('lock7b')
            if (x & M(34)) in L5: tags.add('lock5')
            if (x & M(16)) in TRAP: tags.add('trap16')
        x = step(x, t); t += 1
        if t % 2 == 1: us.append(x & 1)
    tail = us[-1000:]
    for q in range(1, 200):
        if all(tail[i] == tail[i - q] for i in range(q, len(tail))): per = q; break
    for name in ('lock7b', 'lock7', 'lock5'):
        if name in tags: return name, per
    if per == 2: return 'period2', per
    if per is None and 'trap16' in tags: return 'trap', per
    return 'CANDIDATE', per
def late_row(R, T):
    x = R
    for t in range(T): x = step(x, t)
    return x
rng = random.Random(seed)
T0 = 14 * 600 + 1                       # odd tick
out = {}
for name, R, W, ks in (('lock7b', 3793493, 45, (9, 12, 15, 20, 25, 30, 35, 40, 45)), ('lock7', 74, 30, (9, 12, 15, 20, 25, 30))):
    base = late_row(R, T0)
    assert (base & M(W)) in (L7b if name == 'lock7b' else L7), name
    for k in ks:
        counts = {}; cands = []
        for i in range(N):
            x = (base & M(k)) | (rng.getrandbits(200) << k)
            c, per = classify(x, T0)
            counts[c] = counts.get(c, 0) + 1
            if c == 'CANDIDATE': cands.append((per, hex(x)))
        print(name, 'k', k, dict(sorted(counts.items())), 'candidates:', cands[:3], flush=True)
        out[(name, k)] = (counts, cands)
