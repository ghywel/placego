#!/usr/bin/env python3
"""Lock family, step 4 (Local, 8 November 2026): Block 3's period-21 LOCKED component at W = 40 (GC2696 xx core, rank
15, word (0101000)^3, 78 nodes, no lock-7/lock-7b cut windows, leaky inside the core). Is it realized by right halves,
and does it lift to a closed lock at a larger width?
Usage: third.py BN13_DIR KIT_DIR N SEED
Start right halves at an odd tick with cells 1..40 = the component's first window 5522065728 and cells 41..40+r random
(r = 0, 20, 60, 200), run 6000 ticks, classify as in neighbours.py. For every CANDIDATE (periodic u in no known set),
run a forward closure of its late window in the two-cell model at widths 40, 45, ..., 80 with a cap of 200,000 windows
and a phase-label check of column 1; report the first width at which it closes.
Prediction, before the run: P(some sample holds a period-7 u in no known set) = 0.35; P(a new closed lock at W <= 80)
= 0.2; most samples go to the trap, some to lock-7. Counterfactual: a closed set at some W <= 80 with word 0101000
distinct from lock-7 and lock-7b: a third period-7 lock, to be certified by the kernel as in Rule30SidewaysLocks."""
import random, re, sys, importlib.util
spec = importlib.util.spec_from_file_location('nb', __file__.replace('third.py', 'neighbours.py'))
bn, kit, N, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
src = open(__file__.replace('third.py', 'neighbours.py')).read().split('rng = random.Random(seed)')[0]
N_keep = N
sys.argv = ['x', bn, kit, '0', '0']
exec(src)
N = N_keep  # the exec'd header resets N from argv; first run lost the samples this way (fixed)
def st(e, c): return ((e << 1) | c) ^ (e | (e >> 1))
def succ(w, W): return [st(st(w | (e << W), 0), 1) & ((1 << W) - 1) for e in range(4)]
def closure(w0, W, cap=200000):
    lab = {w0: 0}; todo = [w0]; word = {}
    while todo:
        w = todo.pop()
        k = lab[w] % 7
        if word.setdefault(k, w & 1) != (w & 1): return 'label conflict', len(lab)
        for v in succ(w, W):
            if v in lab:
                if (lab[v] - lab[w] - 1) % 7: return 'phase conflict', len(lab)
            else:
                lab[v] = lab[w] + 1; todo.append(v)
                if len(lab) > cap: return 'cap', len(lab)
    return 'CLOSED', len(lab)
w0 = 5522065728
rng = random.Random(seed); T0 = 14 * 600 + 1
for r in (0, 20, 60, 200):
    counts = {}; cands = []
    for i in range(N if r else 1):
        x = w0 | ((rng.getrandbits(r) if r else 0) << 40)
        c, per = classify(x, T0)
        counts[c] = counts.get(c, 0) + 1
        if c == 'CANDIDATE': cands.append((per, x))
    print('random tail', r, dict(sorted(counts.items())), 'candidates', len(cands), flush=True)
    for per, x in cands[:5]:
        t = T0
        for _ in range(6000): x = step(x, t); t += 1
        if t % 2 == 0: x = step(x, t); t += 1
        res = [(W, closure(x & ((1 << W) - 1), W)) for W in range(40, 81, 5)]
        print('  candidate period', per, 'closures', res, flush=True)
