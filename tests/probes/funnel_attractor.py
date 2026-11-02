#!/usr/bin/env python3
"""L1330 T48 (Local, 2026-11-02): the attractor of S_E in the whole W-window automaton of P1024, and how early real paths
reach it. reports/rule30-genealogy.md section 52 (predictions written first).
Run: python3 tests/probes/funnel_attractor.py S_E_FILE W N K

The automaton is front_cert.py's build_generic (section 39), rebuilt here with a per-state FAIL flag (a branch in which the
front and its whole window heal). A = least set of states outside S_E with no FAIL branch and every successor in S_E or A;
rank(v) = the step at which v joins (1 = all successors in S_E). Real paths: N random prefixes of length K at random
theta, every tick at R >= 12 until the first S_E state; recorded: first tick in A or S_E, the rank there, the capture tick,
and whether capture came within the rank (a soundness alarm if not).
"""
import os
import random
import sys
import runpy
import numpy as np
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
sefile, W, N, K = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
p, cols, _ = g['phases']()['P1024']; col0 = cols[0]
NS = p << W
SE = np.zeros(NS, dtype=bool)
for line in open(sefile):
    if not line.startswith('#') and line.strip():
        c, w = line.split(); assert len(w) == W; SE[(int(c) << W) | int(w, 2)] = True
src, dst = [], []; fail = np.zeros(NS, dtype=bool)
for cl in range(p):
    E = {o: (col0 >> ((cl + 195 * o) % p)) & 1 for o in range(-W - 2, 3)}
    for win in range(1 << W):
        v = (cl << W) | win; outs = set()
        for unk in range(4):
            D = {o: 0 for o in range(-W - 2, 3)}; D[0] = 1
            for j in range(1, W + 1):
                D[-j] = (win >> (j - 1)) & 1
            D[-W - 1] = unk & 1; D[-W - 2] = (unk >> 1) & 1
            Nn = {}
            for o in range(-W, 3):
                e1, e2 = E[o - 1], E[o - 2]
                Nn[o] = D[o] ^ (((e1 ^ D[o - 1]) | (e2 ^ D[o - 2])) ^ (e1 | e2))
            ones = [o for o in range(-W, 3) if Nn[o]]
            if not ones:
                fail[v] = True; continue
            a = max(ones)
            known = [Nn[a - j] if a - j >= -W else None for j in range(1, W + 1)]
            free = [i for i, x in enumerate(known) if x is None]
            c2 = (cl + 1 + 195 * a) % p
            for f in range(1 << len(free)):
                w2 = 0
                for i, x in enumerate(known):
                    if x is None:
                        x = (f >> free.index(i)) & 1
                    w2 |= x << i
                outs.add((c2 << W) | w2)
        for u in outs:
            src.append(v); dst.append(u)
src = np.array(src, dtype=np.int64); dst = np.array(dst, dtype=np.int64)
print('P1024 W=%d: %d states, %d distinct edges, %d states with a FAIL branch; S_E %d' % (
    W, NS, len(src), int(fail.sum()), int(SE.sum())), flush=True)
# attractor by backward counting
outdeg = np.bincount(src, minlength=NS)
order = np.argsort(dst, kind='stable'); rsrc = src[order]; rdst = dst[order]
rptr = np.zeros(NS + 1, dtype=np.int64); np.add.at(rptr, rdst + 1, 1); rptr = np.cumsum(rptr)
need = outdeg.copy(); rank = np.full(NS, -1, dtype=np.int64); rank[SE] = 0
frontier = np.flatnonzero(SE); r = 0
while len(frontier):
    r += 1
    preds = np.concatenate([rsrc[rptr[u]:rptr[u + 1]] for u in frontier]) if len(frontier) else np.array([], np.int64)
    np.subtract.at(need, preds, 1)
    cand = np.unique(preds)
    new = cand[(need[cand] == 0) & (rank[cand] < 0) & (~fail[cand]) & (outdeg[cand] > 0)]
    rank[new] = r; frontier = new
A = (rank > 0)
print('   attractor A of S_E (outside S_E): %d states (%.2f%% of the automaton); largest rank %d; rank counts (first 12): %s' % (
    int(A.sum()), 100.0 * A.sum() / NS, int(rank.max()), np.bincount(rank[rank > 0])[1:13].tolist()), flush=True)
# real paths
T = 6 * K + 2400; depth = 2 * T + K + 16; mask = (1 << depth) - 1
bits = [(col0 >> i) & 1 for i in range(p)]
base = [int(''.join(str(bits[(k + 195 * n) % p]) for n in range(depth))[::-1], 2) for k in range(p)]
rev = [int(format(v, '0%db' % W)[::-1], 2) for v in range(1 << W)]
rng = random.Random(48); leads = []; inA_share = []; alarms = 0; entry_ranks = []; uncapt = 0
for it in range(N):
    th = rng.randrange(p)
    x = rng.getrandbits(K) | (base[th] >> K << K)
    first = None; capt = None; nticks = 0; nA = 0
    for t in range(T + 1):
        d = (x ^ base[(th + t) % p]) & mask; R = d.bit_length() - 1
        if R >= 12:
            v = (((th + t + 195 * R) % p) << W) | rev[(d >> (R - W)) & ((1 << W) - 1)]
            if SE[v]:
                capt = t; break
            nticks += 1
            if A[v]:
                nA += 1
                if first is None:
                    first = (t, int(rank[v]))
        x = (x ^ ((x << 1) | (x << 2) | 3)) & mask
    if capt is None:
        uncapt += 1; continue
    if first is not None:
        leads.append(capt - first[0]); entry_ranks.append(first[1])
        if capt - first[0] > first[1]:
            alarms += 1
    else:
        leads.append(0)
    inA_share.append(nA / max(1, nticks))
def pct(v, q):
    v = sorted(v); return v[min(len(v) - 1, int(q * len(v)))] if v else None
print('   real paths (%d prefixes, K=%d): not captured %d; entered A before capture: %d; lead from first A state to capture: '
      'median %s, 90%% %s, max %s; rank at entry: median %s, max %s; captures later than the entry rank (alarm): %d' % (
          N, K, uncapt, len(entry_ranks), pct(leads, 0.5), pct(leads, 0.9), max(leads), pct(entry_ranks, 0.5),
          max(entry_ranks) if entry_ranks else None, alarms), flush=True)
print('   share of pre-capture ticks spent in A: median %.3f, max %.3f' % (pct(inA_share, 0.5), max(inA_share)), flush=True)
print('FUNNEL_ATTRACTOR_DONE')
