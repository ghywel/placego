#!/usr/bin/env python3
"""f_structure.py TABLE: the structure of the crystal's recurrence F (round 14, seventh block; Cloud, CL697). F(u, w)(t+1) =
NOT (parity of w over [last black of u at or before t, t]); F(u, .) affine and bijective; the strip reversible; the coincidence
criterion C_(k-1) = dC_k (derivative = C_k XOR shift); the pair map's cycle structure at period 8 by full enumeration. Predictions
in the tracker. Output: f_structure.out."""
import sys, numpy as np, collections
table = sys.argv[1]
C = [tuple(int(ch) for ch in l.strip()) for l in open(table) if l and not l.startswith('#')]
K = len(C); p = 16
def F_closed(u, w):
    p = len(u); d = [None] * p
    for t in range(p):
        # last black of u at or before t (cyclic)
        s = t; par = 0; steps = 0
        while True:
            par ^= w[s % p]
            if u[s % p] == 1 or steps >= p: break
            s -= 1; steps += 1
        d[(t + 1) % p] = 1 - par
    return tuple(d)
def shift(c): return tuple(c[(i + 1) % len(c)] for i in range(len(c)))
def deriv(c): return tuple(a ^ b for a, b in zip(c, shift(c)))
def backward(ck, ck1):   # C_(k-1) from C_k and C_(k+1)
    return tuple((1 - ck1[(t + 1) % p]) ^ ((1 - ck[t]) & (1 - ck1[t])) for t in range(p))
# P-F1: closed form
ok = bad = 0
for k in range(2, K):
    u, w = C[k - 1], C[k - 2]
    if not any(u): continue
    if F_closed(u, w) == C[k]: ok += 1
    else: bad += 1
print(f"P-F1 closed form F(u,w) = NOT running parity of w restarted at u's blacks: {ok} agree, {bad} disagree (wheels with a black parent)")
# P-F2: reversibility, backward from the top
cur, nxt = C[K - 2], C[K - 1]; agree = disagree = 0; first_bad = None
for k in range(K - 2, 1, -1):          # compute C_(k-1) from (C_k, C_(k+1)) = (cur, nxt)
    prev = backward(cur, nxt)
    if prev == C[k - 1]: agree += 1
    else:
        disagree += 1
        if first_bad is None: first_bad = k - 1
    cur, nxt = C[k - 1], cur           # continue from the TRUE values so one error does not cascade
print(f"P-F2 backward strip C_(k-1) = NOT C_(k+1)(t+1) XOR (NOT C_k(t) AND NOT C_(k+1)(t)) from wheel {K-2} down to 2: {agree} agree, {disagree} disagree (first disagreement at wheel {first_bad})")
# P-F3: coincidence criterion and the distance to the derivative
hits = []; dists = []
for k in range(2, K - 1):
    d = sum(a != b for a, b in zip(C[k - 1], deriv(C[k])))
    dists.append(d)
    if d == 0: hits.append(k)
dists = np.array(dists)
print(f"P-F3 wheels k with C_(k-1) = dC_k (derivative): {hits}; white wheels two on: {[k + 2 for k in hits]}; distance mean {dists.mean():.3f} (p/2 = 8), histogram {np.bincount(dists, minlength=17).tolist()}")
print(f"      binomial(16,1/2) reference x {len(dists)}: {[round(len(dists) * __import__('math').comb(16, i) / 65536) for i in range(17)]}")
# P-F4: the pair map at period 8, full enumeration
q = 8
def F8(u, w): return F_closed(u, w)
words8 = [tuple((i >> j) & 1 for j in range(q)) for i in range(1 << q)]
idx = {w: i for i, w in enumerate(words8)}
nxt = np.full((1 << q) * (1 << q), -1, dtype=np.int64)       # pair (a,b) -> (b, F(b,a)); index a*256+b
for a in words8:
    for b in words8:
        if not any(b): continue
        c = F8(b, a); nxt[idx[a] * 256 + idx[b]] = idx[b] * 256 + idx[c]
# check bijectivity on the domain (b != 0)
dom = np.flatnonzero(nxt >= 0); img = nxt[dom]
print(f"P-F4 period 8: pair map defined on {len(dom)} pairs (b != 0); image distinct {len(set(img.tolist()))} of {len(dom)} -> {'bijective on its image' if len(set(img.tolist())) == len(dom) else 'NOT injective'}")
# cycle decomposition of the permutation restricted to pairs whose orbit never leaves the domain: follow from each pair until a repeat or a white parent
seen = {}; cycles = []
for s in dom:
    if s in seen: continue
    path = []; x = s
    while x >= 0 and x not in seen:
        seen[x] = True; path.append(x); x = nxt[x] if x in dom else -1
    cycles.append(path)
# classify: a path ending in a white parent (c = 0 or b = 0) vs a true cycle
coinc = set(idx[deriv(b)] * 256 + idx[b] for b in words8 if any(b))   # pairs (dC_k, C_k): the next is a coincidence
lens = collections.Counter(len(c) for c in cycles)
print(f"      orbits from distinct starts: {len(cycles)}; length histogram (top 10): {lens.most_common(10)}; coincidence pairs {len(coinc)}")
# the strip's period-8 segment: starts after wheel 28 (white): pairs (C_29, C_30) ... up to (C_397, C_398) = (dC_398?, ...)
seg = [(C[k][:8], C[k + 1][:8]) for k in range(29, 398)]
starts = idx[seg[0][0]] * 256 + idx[seg[0][1]]; x = starts; L = 0
while x >= 0 and x not in coinc and L < 70000: x = nxt[x]; L += 1
print(f"      the strip's period-8 segment from the pair at wheels (29, 30): steps to the first coincidence pair {L} (the record's 398 - 29 = {398 - 29}); {'consistent' if L == 398 - 29 - 1 or L == 398 - 29 else 'check the offset'}")
print("F_STRUCTURE_DONE")
