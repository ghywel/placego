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
EXITS = '--exits' in sys.argv; br = {}
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
            if EXITS:
                br.setdefault(v, []).append((unk, a, len(free), [None]))
            for f in range(1 << len(free)):
                w2 = 0
                for i, x in enumerate(known):
                    if x is None:
                        x = (f >> free.index(i)) & 1
                    w2 |= x << i
                outs.add((c2 << W) | w2)
                if EXITS:
                    br[v][-1][3].append((c2 << W) | w2)
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
if '--core' in sys.argv:
    # L1338 T50: the bad core B computed independently (greatest set outside S_E in which every state has an edge into the set)
    aliveB = ~SE.copy()
    while True:
        ok = aliveB[src] & aliveB[dst]
        has = np.zeros(NS, dtype=bool); has[src[ok]] = True
        new = aliveB & has
        if new.sum() == aliveB.sum():
            break
        aliveB = new
    savep = next((a[7:] for a in sys.argv if a.startswith('--save=')), None)
    if savep:
        np.savez_compressed(savep, SE=SE, A=(rank > 0), B=aliveB, W=W)   # L1340 T51: masks for refine_check.py (local data)
    print('   bad core B: %d states (%.2f%%); S_E + A + B = %d of %d; A and B disjoint: %s' % (
        int(aliveB.sum()), 100.0 * aliveB.sum() / NS, int(SE.sum() + A.sum() + aliveB.sum()), NS,
        not bool((A & aliveB).any())), flush=True)
print('   attractor A of S_E (outside S_E): %d states (%.2f%% of the automaton); largest rank %d; rank counts (first 12): %s' % (
    int(A.sum()), 100.0 * A.sum() / NS, int(rank.max()), np.bincount(rank[rank > 0])[1:13].tolist()), flush=True)
# L1333: the depth guard. Edge advances from classes (a = -21 (c' - c - 1) mod 1024, in -512 .. 511); F = largest fall
# below the start on paths to S_E, G = largest net fall at entry; computed in rank order.
GUARD = '--guard' in sys.argv
if GUARD:
    a_e = ((-21 * ((dst >> W) - (src >> W) - 1)) % p + 512) % p - 512
    Ff = np.full(NS, -1, dtype=np.int64); Gg = np.full(NS, -1, dtype=np.int64)
    Ff[SE] = 0; Gg[SE] = 0
    order_s = np.argsort(src, kind='stable'); s_src, s_dst, s_a = src[order_s], dst[order_s], a_e[order_s]
    sptr = np.zeros(NS + 1, dtype=np.int64); np.add.at(sptr, s_src + 1, 1); sptr = np.cumsum(sptr)
    for rr in range(1, int(rank.max()) + 1):
        for v in np.flatnonzero(rank == rr):
            us = s_dst[sptr[v]:sptr[v + 1]]; aa = s_a[sptr[v]:sptr[v + 1]]
            Ff[v] = int(np.max(-aa + np.maximum(0, Ff[us])))
            Gg[v] = int(np.max(-aa + Gg[us]))
    need_R = np.maximum(W + 2 + np.maximum(0, Ff), W + 4 + Gg)   # L1338: floors W + 2 on the way, W + 4 at entry; F clipped at 0
    print('   depth guard over A: F (largest fall on the way) max %d, median %d; G (net fall at entry) max %d; '
          'required depth max(W + 2 + max(0, F), W + 4 + G): max %d, median %d; advances seen on A edges: %s' % (
              int(Ff[A].max()), int(np.median(Ff[A])), int(Gg[A].max()), int(need_R[A].max()), int(np.median(need_R[A])),
              sorted(set(a_e.tolist()))[:16]), flush=True)
# real paths
T = 6 * K + 2400; depth = 2 * T + K + 16; mask = (1 << depth) - 1
bits = [(col0 >> i) & 1 for i in range(p)]
base = [int(''.join(str(bits[(k + 195 * n) % p]) for n in range(depth))[::-1], 2) for k in range(p)]
rev = [int(format(v, '0%db' % W)[::-1], 2) for v in range(1 << W)]
guard_rows = []; exit_rows = []; entry_R = []; minR_after = []
Bset = ~(SE | A)
def prev_unk(d, R):
    return ((d >> (R - W - 1)) & 1) | (((d >> (R - W - 2)) & 1) << 1)
rng = random.Random(48); leads = []; inA_share = []; alarms = 0; entry_ranks = []; uncapt = 0
for it in range(N):
    th = rng.randrange(p)
    x = rng.getrandbits(K) | (base[th] >> K << K)
    first = None; capt = None; nticks = 0; nA = 0
    prev = None
    for t in range(T + 1):
        d = (x ^ base[(th + t) % p]) & mask; R = d.bit_length() - 1
        if R >= 12:
            v = (((th + t + 195 * R) % p) << W) | rev[(d >> (R - W)) & ((1 << W) - 1)]
            if EXITS and prev is not None and Bset[prev[0]] and not Bset[v]:
                exit_rows.append((prev[0], prev[1], R - prev[2]))
            prev = (v, prev_unk(d, R), R)
            if SE[v]:
                capt = t; break
            nticks += 1
            if A[v]:
                nA += 1
                if first is None:
                    first = (t, int(rank[v]))
                    if GUARD:
                        guard_rows.append((R, int(need_R[v])))
                    entry_R.append(R); minR_after.append(R)
            if first is not None:
                minR_after[-1] = min(minR_after[-1], R)
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
if EXITS:
    from collections import Counter
    advs = Counter(); pair_only = 0; stay_frac = []
    for v, u_real, a_real in exit_rows:
        bl = [(unk, a, [x for x in succ[1:]]) for unk, a, nf, succ in br[v]]
        brs = [(unk, x) for unk, a, xs in bl for x in xs]
        stay = [Bset[x] for unk, x in brs]
        stay_frac.append(sum(stay) / len(stay))
        real_pair = [Bset[x] for unk, x in brs if unk == u_real]
        other = [Bset[x] for unk, x in brs if unk != u_real]
        if real_pair and not any(real_pair) and any(other):
            pair_only += 1
        advs[a_real] += 1
    print('   exits from B on real paths: %d; real advance at exit: %s; decided by the unknown pair alone: %d (%.1f%%); '
          'share of branches staying in B at the exit state: median %.2f' % (
              len(exit_rows), sorted(advs.items()), pair_only, 100.0 * pair_only / max(1, len(exit_rows)),
              sorted(stay_frac)[len(stay_frac) // 2] if stay_frac else -1), flush=True)
if GUARD:
    print('   real entries into A: %d; satisfying the depth guard of their state: %d; least margin (R - required) %d' % (
        len(guard_rows), sum(1 for R_, q in guard_rows if R_ >= q), min(R_ - q for R_, q in guard_rows)), flush=True)
if '--depths' in sys.argv:
    print('   logged depths: first entry into A at depth min %d, median %d; least depth from that entry to capture: min %d, median %d' % (
        min(entry_R), sorted(entry_R)[len(entry_R) // 2], min(minR_after), sorted(minR_after)[len(minR_after) // 2]), flush=True)
print('FUNNEL_ATTRACTOR_DONE')
