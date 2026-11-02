#!/usr/bin/env python3
"""L1318 T42 (Local, 2026-11-02): capture route C1, the bad core of the window automaton.
reports/rule30-genealogy.md section 45 (predictions written first). Run: python3 tests/probes/capture_core.py PHASE W
(PHASE: 480 or P1024)

The whole W-window automaton of section 39, built with front_cert.py's build_generic (FAIL edges are counted there and
are not edges). S_E: the states reachable from the clean front's states (ticks 600 .. 600 + 4 wake periods of a clean
start, the alignments of front_closure.py). The bad core B: the largest set of states outside S_E in which every state
has an edge into the set (a greatest fixed point), i.e. the states with an infinite FAIL-free path avoiding S_E.
Reported: |S_E| (against section 44.5), |B|, the least advance over paths of length k inside B, the states of B with a
600-path of total advance <= 0, and one cycle of the greedy least-advance policy inside B, with its windows.
"""
import os
import sys
import runpy
import numpy as np
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
fc = runpy.run_path(os.path.join(here, 'front_cert.py'), run_name='lib')
name = sys.argv[1]; W = int(sys.argv[2])
p, cols, _ = g['phases']()[name]; NC = len(cols)
PER = {'P1024': 208, '480': 288}[name]
if name == 'P1024':
    th0 = 780; col0 = cols[0]
    NS, src, dst, adv, fails = fc['build_single_column'](col0, p, 195, W)
    def E_bit(n, t):
        return (col0 >> ((th0 + t + 195 * n) % p)) & 1
    def cls(R, t):
        return (th0 + t + 195 * R) % p
else:
    a0, q0 = 195, 21
    NS, src, dst, adv, fails = fc['build'](p, cols, W)
    def E_bit(n, t):
        return (cols[(n + a0) % NC] >> ((t + q0) % p)) & 1
    def cls(R, t):
        return ((R + a0) % NC) * p + (t + q0) % p
print('%s W=%d: whole automaton %d states, %d edges, %d FAIL edges' % (name, W, NS, len(src), fails), flush=True)

# the clean front's states
T = 600 + 4 * PER; depth = 2 * T + 16; mask = (1 << depth) - 1; rows = {}
def erow(t):
    k = t % p
    if k not in rows:
        rows[k] = sum(E_bit(n, t) << n for n in range(depth))
    return rows[k]
x = erow(0); clean = set()
for t in range(T + 1):
    d = x ^ erow(t); R = d.bit_length() - 1
    if t >= 600:
        win = 0
        for j in range(1, W + 1):
            win |= ((d >> (R - j)) & 1) << (j - 1)
        clean.add((cls(R, t) << W) | win)
    x = (x ^ ((x << 1) | (x << 2) | 3)) & mask

# CSR adjacency and S_E by breadth-first search
order = np.argsort(src, kind='stable'); s_src, s_dst, s_adv = src[order], dst[order], adv[order]
indptr = np.zeros(NS + 1, dtype=np.int64); np.add.at(indptr, s_src + 1, 1); indptr = np.cumsum(indptr)
inS = np.zeros(NS, dtype=bool); frontier = np.array(sorted(clean), dtype=np.int64); inS[frontier] = True
while len(frontier):
    nb = np.concatenate([s_dst[indptr[v]:indptr[v + 1]] for v in frontier]) if len(frontier) else np.array([], np.int64)
    nb = np.unique(nb); nb = nb[~inS[nb]]; inS[nb] = True; frontier = nb
print('   clean states %d; S_E (reachable from them in the whole automaton) %d states' % (len(clean), int(inS.sum())), flush=True)

# the bad core
alive = ~inS; it = 0
while True:
    it += 1
    ok = alive[src] & alive[dst]
    has = np.zeros(NS, dtype=bool); has[src[ok]] = True
    new = alive & has
    if new.sum() == alive.sum():
        break
    alive = new
B = np.flatnonzero(alive)
print('   bad core B: %d states (%.1f%% of the automaton; %d deletion rounds); outside S_E and B: %d states' % (
    len(B), 100.0 * len(B) / NS, it, NS - int(inS.sum()) - len(B)), flush=True)
if len(B):
    idx = -np.ones(NS, dtype=np.int64); idx[B] = np.arange(len(B))
    ok = alive[src] & alive[dst]
    bs, bd, ba = idx[src[ok]], idx[dst[ok]], adv[ok]
    k, trace = fc['certify'](len(B), bs, bd, ba)
    print('   inside B, least advance over paths of length k: %s; %s' % (
        trace, 'every path of length %d advances' % k if k else 'NOT every long path advances'), flush=True)
    # least advance over 600-paths from each state of B, and the greedy policy for a witness cycle
    v = np.zeros(len(B), dtype=np.int64); INF = 1 << 40
    for _ in range(600):
        nv = np.full(len(B), INF, dtype=np.int64); np.minimum.at(nv, bs, ba + v[bd]); v = nv
    print('   states of B with a 600-path of total advance <= 0: %d (%.2f%% of B); least 600-path advance %d' % (
        int((v <= 0).sum()), 100.0 * (v <= 0).sum() / len(B), int(v.min())), flush=True)
    best = np.full(len(B), INF, dtype=np.int64); arg = -np.ones(len(B), dtype=np.int64)
    val = ba + v[bd]
    for e in np.argsort(val, kind='stable')[::-1]:
        if val[e] <= best[bs[e]]:
            best[bs[e]] = val[e]; arg[bs[e]] = e
    s = int(np.argmin(v)); seen = {}; path = []
    while s not in seen:
        seen[s] = len(path); e = int(arg[s]); path.append(e); s = int(bd[e])
    cyc = path[seen[s]:]
    tot = int(sum(ba[e] for e in cyc))
    print('   greedy witness cycle in B: length %d, total advance %d' % (len(cyc), tot), flush=True)
    for e in cyc[:12]:
        st = B[bs[e]]; cl, win = st >> W, st & ((1 << W) - 1)
        print('      class %4d  window (D_(R-1) .. D_(R-%d)) %s  advance %+d' % (
            cl, W, ''.join(str((win >> j) & 1) for j in range(W)), int(ba[e])), flush=True)

if '--fails' in sys.argv:
    # route C3: which windows allow a deep retreat (a FAIL edge: the front and its whole window heal in one tick)?
    from collections import Counter
    if name == 'P1024':
        NCL = p
        def bg(cl, o):
            return (col0 >> ((cl + 195 * o) % p)) & 1
    else:
        NCL = NC * p
        def bg(cl, o):
            return (cols[(cl // p + o) % NC] >> (cl % p)) & 1
    pats = Counter(); fail_states = set()
    for cl in range(NCL):
        E = {o: bg(cl, o) for o in range(-W - 2, 3)}
        for win in range(1 << W):
            for unk in range(4):
                D = {o: 0 for o in range(-W - 2, 3)}; D[0] = 1
                for j in range(1, W + 1):
                    D[-j] = (win >> (j - 1)) & 1
                D[-W - 1] = unk & 1; D[-W - 2] = (unk >> 1) & 1
                if not any(D[o] ^ (((E[o - 1] ^ D[o - 1]) | (E[o - 2] ^ D[o - 2])) ^ (E[o - 1] | E[o - 2]))
                           for o in range(-W, 3)):
                    s = ''.join(str(D[-j]) for j in range(W + 2, 0, -1)) + '|1'
                    e = ''.join(str(E[o]) for o in range(-W - 2, 3))
                    pats[(s, e)] += 1; fail_states.add((cl << W) | win)
    fs = np.array(sorted(fail_states), dtype=np.int64)
    print('   FAIL edges: %d, from %d states; in S_E %d, in B %d' % (
        sum(pats.values()), len(fs), int(inS[fs].sum()), int(alive[fs].sum())), flush=True)
    print('   distinct (mismatch D_(R-W-2) .. D_R, phase E_(R-W-2) .. E_(R+2)) patterns: %d; the first 12:' % len(pats), flush=True)
    for (s, e), c in sorted(pats.items(), key=lambda z: -z[1])[:12]:
        print('      D %s   E %s   x%d' % (s, e, c), flush=True)
