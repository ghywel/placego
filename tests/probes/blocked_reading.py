#!/usr/bin/env python3
"""L1325 T45 (Local, 2026-11-02): how far behind the front does a blocked move read? reports/rule30-genealogy.md section 49
(predictions written first). Run: python3 tests/probes/blocked_reading.py PHASE S_E_FILE N K

Edge frame and phases as in own_wake_fuel.py. At a tick with front R >= 12, the class is open if the look-ahead bit
E_(R+1) is 0 (the move is then +2, by the mask lemma) and blocked otherwise. The move's reading depth is the least k in
0 .. 10 such that the actual D_(R-1) .. D_(R-k) fix the new front for every completion of D_(R-k-1) .. D_(R-10); deeper
cells are never consulted, and "> 10" means the cells out to depth 10 do not fix it (the new front lies 9 or more cells
behind). Reported before capture (first S_E state at R >= 12) and for 300 ticks after it.
"""
import os
import random
import sys
import runpy
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
name, sefile, N, K = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
p, cols, _ = g['phases']()[name]; NC = len(cols)
W = 8; NB = 10
SE = set()
for line in open(sefile):
    if not line.startswith('#') and line.strip():
        c, w = line.split(); SE.add((int(c), int(w, 2)))
rev = [int(format(v, '0%db' % W)[::-1], 2) for v in range(1 << W)]
T = 6 * K + 2400; depth = 2 * T + K + 16; mask = (1 << depth) - 1


def new_front(Eo, Db):
    """Eo[o] = E_(R+o) for o in -NB-2 .. 2; Db[j] = D_(R-j) for j = 1 .. n (n <= NB). Returns the new front offset if
    the known cells fix it, else None."""
    n = len(Db) - 1
    D = {0: 1, 1: 0, 2: 0}
    for j in range(1, n + 1):
        D[-j] = Db[j]
    for o in range(2, -n + 1, -1):           # outputs whose inputs o-1, o-2 are known: o >= -n + 2
        e1, e2 = Eo[o - 1], Eo[o - 2]
        if D[o] ^ (((e1 ^ D[o - 1]) | (e2 ^ D[o - 2])) ^ (e1 | e2)):
            return o
    return None


def reading_depth(Eo, Dfull):
    """Dfull[j] = actual D_(R-j), j = 1 .. NB. Least k with the move fixed by Dfull[1..k] for every completion."""
    a_true = new_front(Eo, Dfull)
    for k in range(0, NB + 1):
        ok = True
        for comp in range(1 << (NB - k)):
            Db = Dfull[:k + 1] + [(comp >> i) & 1 for i in range(NB - k)]
            if new_front(Eo, Db) != a_true:
                ok = False; break
        if ok:
            return k, a_true
    return None, a_true


if name == 'P1024':
    col0 = cols[0]
    bits = [(col0 >> i) & 1 for i in range(p)]
    base = [int(''.join(str(bits[(k + 195 * n) % p]) for n in range(depth))[::-1], 2) for k in range(p)]
rng = random.Random(45)
pre = Counter(); post = Counter(); pre_adv = Counter(); post_adv = Counter(); open_bad = 0; open_n = 0; uncapt = 0
for it in range(N):
    if name == 'P1024':
        th = rng.randrange(p)
        erow = lambda t: base[(th + t) % p]
        cls = lambda R, t: (th + t + 195 * R) % p
    else:
        a0, q0 = rng.randrange(NC), rng.randrange(p)
        cache = {}
        def erow(t, a0=a0, q0=q0, cache=cache):
            k = (t + q0) % p
            if k not in cache:
                s0 = ''.join(str((cols[(n + a0) % NC] >> k) & 1) for n in range(NC)) * (depth // NC + 2)
                cache[k] = int(s0[:depth][::-1], 2)
            return cache[k]
        cls = lambda R, t, a0=a0, q0=q0: ((R + a0) % NC) * p + (t + q0) % p
    x = rng.getrandbits(K) | (erow(0) >> K << K)
    capt = None
    for t in range(T + 1):
        e = erow(t); d = (x ^ e) & mask; R = d.bit_length() - 1
        if R >= 12:
            if capt is None and (cls(R, t), rev[(d >> (R - W)) & 255]) in SE:
                capt = t
            Eo = {o: (e >> (R + o)) & 1 for o in range(-NB - 2, 3)}
            Dfull = [None] + [(d >> (R - j)) & 1 for j in range(1, NB + 1)]
            k, a = reading_depth(Eo, Dfull)
            if Eo[1] == 0:
                open_n += 1; open_bad += (a != 2 or k != 0)
            else:
                tgt, tadv = (post, post_adv) if capt is not None else (pre, pre_adv)
                tgt['> 10' if k is None else k] += 1; tadv[a] += 1
        if capt is not None and t >= capt + 300:
            break
        x = (x ^ ((x << 1) | (x << 2) | 3)) & mask
    uncapt += capt is None
def show(c):
    n = sum(c.values())
    return ', '.join('%s: %d (%.1f%%)' % (k, v, 100.0 * v / n) for k, v in sorted(c.items(), key=lambda z: (isinstance(z[0], str), z[0])))
print('%s K=%d, %d runs (%d not captured): open ticks %d, of which not (+2, depth 0): %d' % (name, K, N, uncapt, open_n, open_bad), flush=True)
print('   before capture, blocked ticks %d; reading depth: %s' % (sum(pre.values()), show(pre)), flush=True)
print('      moves (new front offset; None = beyond depth 10): %s' % show(pre_adv), flush=True)
print('   after capture (300 ticks), blocked ticks %d; reading depth: %s' % (sum(post.values()), show(post)), flush=True)
print('      moves: %s' % show(post_adv), flush=True)
print('BLOCKED_READING_DONE')
