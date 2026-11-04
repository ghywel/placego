#!/usr/bin/env python3
"""crosscheck.py: evolve actual rows and see which of the four strips each lands on (L1513). Independent of the Lean.
Prediction: every row lands on exactly one strip at one phase. Generic rows land on A0 (8.31). Flips late in the seed's
strip at 53,208 / 58,287 / both land on the matching branch. Counterfactual: a row matching none refutes the classification."""
import pickle, random, sys, time
sys.set_int_max_str_digits(0)
K = 87867
M = (1 << K) - 1
def step(v): return ((v << 2) ^ ((v << 1) | v)) & M
d = pickle.load(open('leaves.pkl', 'rb'))
table = {}
for name in ('A0', 'A1', 'B0', 'B1'):
    v = d[name]
    for p in range(16):
        table.setdefault(v, []).append((name, p))
        v = step(v)
print('distinct rows in the four cycles', len(table), '(64 means no two strips share a row at any phase)')
def land(v, T):
    for _ in range(T): v = step(v)
    return table.get(v)
rng = random.Random(1509)
cases = []
for w in (2, 3, 8, 24, 64, 200, 1000, 10000, 60000, 87867):
    for _ in range(2):
        cases.append(('random width %d' % w, rng.getrandbits(w) | 1))
s = 1
for _ in range(16 * 8000): s = step(s)
cases.append(('seed itself', 1))
cases.append(('row 101', 5))
cases.append(('seed strip, flip 53208', s ^ (1 << 53208)))
cases.append(('seed strip, flip 58287', s ^ (1 << 58287)))
cases.append(('seed strip, flip 53208 and 72576', s ^ (1 << 53208) ^ (1 << 72576)))
cases.append(('seed strip, flip 60000', s ^ (1 << 60000)))
cases.append(('seed strip, flip 80000', s ^ (1 << 80000)))
cases.append(('seed strip, flip 53209', s ^ (1 << 53209)))
t0 = time.time(); tally = {}; miss = 0
for name, v in cases:
    r = land(v, 16 * 8300)
    if r is None or len(r) != 1:
        miss += 1
    key = r[0][0] if r else 'NONE'
    tally[key] = tally.get(key, 0) + 1
    print(name.ljust(34), r)
print('tally', tally, 'rows matching none or several:', miss, 'seconds', round(time.time() - t0, 1))
