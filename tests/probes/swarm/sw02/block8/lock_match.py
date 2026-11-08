#!/usr/bin/env python3
"""Block 8 (Local): the lock windows read and replayed. Usage: lock_match.py BN13_DIR SEVENLOCK_LEAN
Window: bit i is column i + 1 of a right half driven by the alternating column (black at even ticks), at an odd tick.
Two input models for the double step from an odd tick, both sound for every actual right half:
  'cells': the cells of columns W + 1 and W + 2 at the odd tick are free, the rest is computed (BN-13's closure);
  'free':  column W + 1 is free at both ticks (the kit's Rule30GateTrap and rule30-open's SevenLock).
For each lock: closure failures under each model, the phase classes inside the lock and the word of column 1;
then the window-level comparison of BN-13's lock-7 (30 columns) with rule30-open's SevenLock (32 columns)."""
import math, re, sys
bn, lean = sys.argv[1:3]
def ints(p): return sorted(int(x) for x in open(p).read().split())
def st(e, c): return ((e << 1) | c) ^ (e | (e >> 1))
def succ(w, W, model):
    m = (1 << W) - 1
    if model == 'cells':
        return {st(st(w | (e << W), 0), 1) & m for e in range(4)}
    return {st((st(w | (x1 << W), 0) & m) | (x2 << W), 1) & m for x1 in (0, 1) for x2 in (0, 1)}
def analyse(S, W, model):
    S = set(S)
    bad = sum(1 for w in S for v in succ(w, W, model) if v not in S)
    if bad: return 'failures %d' % bad
    lab = {min(S): 0}; todo = [min(S)]; edges = []
    while todo:
        w = todo.pop()
        for v in succ(w, W, model):
            edges.append((w, v))
            if v not in lab: lab[v] = lab[w] + 1; todo.append(v)
    p = 0
    for w, v in edges: p = math.gcd(p, lab[w] + 1 - lab[v])
    word = {}; ok = True
    for w, l in lab.items():
        if word.setdefault(l % p, w & 1) != (w & 1): ok = False
    sizes = [sum(1 for w in lab if lab[w] % p == k) for k in range(p)]
    return 'closed; period %d; reached %d of %d; word %s%s; class sizes %s' % (
        p, len(lab), len(S), ''.join(str(word[k]) for k in range(p)), '' if ok else ' (INCONSISTENT)', sizes)
for name, W in (('lock5.txt', 34), ('lock7.txt', 30), ('lock7_w45.txt', 45)):
    S = ints(bn + '/' + name)
    for model in ('cells', 'free'):
        print('%-14s W %2d windows %2d %-5s %s' % (name, W, len(S), model, analyse(S, W, model)))
src = open(lean).read()
body = src[src.index('def lockCls'):src.index('def lockCheck')]
cls = [[int(x) for x in re.findall(r'\d+', m)] for m in re.findall(r'\[([\d,\s]+)\]', body)]
sl = sorted(c for k in cls for c in k)
for model in ('cells', 'free'):
    print('%-14s W 32 windows %d %-5s %s' % ('SevenLock', len(sl), model, analyse(sl, 32, model)))
l7 = set(ints(bn + '/lock7.txt'))
proj = {c & ((1 << 30) - 1) for c in sl}
print('SevenLock projected to 30 columns: %d windows; equal to BN-13 lock-7: %s; lock-7 minus projection %d; projection minus lock-7 %d'
      % (len(proj), proj == l7, len(l7 - proj), len(proj - l7)))
l7b = ints(bn + '/lock7_w45.txt'); l5 = ints(bn + '/lock5.txt')
print('lock-7b projected to 32 columns meets SevenLock:', len({c & ((1 << 32) - 1) for c in l7b} & set(sl)))
print('lock-5 projected to 30 columns meets lock-7:', len({c & ((1 << 30) - 1) for c in l5} & l7))
