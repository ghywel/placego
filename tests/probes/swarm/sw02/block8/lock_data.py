#!/usr/bin/env python3
"""Block 8 (Local): classes and entry witnesses for the three locks, in the 'cells' model of lock_match.py.
Usage: lock_data.py BN13_DIR OUT_JSON. The driven right half: column 0 alternates, black at even ticks; a finite
R (bit p - 1 = column p) evolves as D(t + 1) = ((D << 1) | c(t)) ^ (D | (D >> 1)), exact for finite rows."""
import json, math, sys
bn, out = sys.argv[1:3]
def ints(p): return sorted(int(x) for x in open(p).read().split())
def st(e, c): return ((e << 1) | c) ^ (e | (e >> 1))
def succ(w, W): return {st(st(w | (e << W), 0), 1) & ((1 << W) - 1) for e in range(4)}
def classes(S, W):
    S = set(S); lab = {min(S): 0}; todo = [min(S)]; edges = []
    while todo:
        w = todo.pop()
        for v in succ(w, W):
            assert v in S
            edges.append((w, v))
            if v not in lab: lab[v] = lab[w] + 1; todo.append(v)
    p = 0
    for w, v in edges: p = math.gcd(p, lab[w] + 1 - lab[v])
    cls = [sorted(w for w in lab if lab[w] % p == k) for k in range(p)]
    word = [cls[k][0] & 1 for k in range(p)]
    assert all(all((w & 1) == word[k] for w in cls[k]) for k in range(p))
    assert all(all(v in cls[(k + 1) % p] for w in cls[k] for v in succ(w, W)) for k in range(p))
    return p, word, cls
def entry(R, W, S, cap=6000):
    D = R
    for t in range(cap + 1):
        if t % 2 == 1 and (D & ((1 << W) - 1)) in S: return t
        D = st(D, 1 if t % 2 == 0 else 0)
    return None
res = {}
p5 = [int(x) for x in open(bn + '/period5.txt').read().split()] if open(bn + '/period5.txt').read().split() else []
for name, W, cands in (('lock5', 34, None), ('lock7', 30, list(range(1, 4096))), ('lock7b', 45, [3793493])):
    S = ints(bn + '/' + {'lock5': 'lock5.txt', 'lock7': 'lock7.txt', 'lock7b': 'lock7_w45.txt'}[name])
    p, word, cls = classes(S, W)
    Sset = set(S)
    if cands is None:
        import re
        rep = open(bn + '/report.txt').read()
        cands = sorted({int(x) for x in re.findall(r'\b(\d{5,8})\b', open(bn + '/results.txt').read())} )
    ents = []
    for R in cands:
        t = entry(R, W, Sset)
        if t is not None: ents.append((t + R.bit_length(), t, R))
    ents.sort()
    best = ents[:3]
    res[name] = {'W': W, 'p': p, 'word': word, 'classes': cls, 'sizes': [len(c) for c in cls], 'witnesses': best}
    print(name, 'W', W, 'p', p, 'word', ''.join(map(str, word)), 'sizes', [len(c) for c in cls], 'candidates', len(cands), 'entering', len(ents), 'best (cost, tick, R)', best)
json.dump(res, open(out, 'w'))
