#!/usr/bin/env python3
"""Block 3: independent replay of lift.c in numpy and scipy. It uses the fixed target data and optionally a digest-bound, already independently verified prefix dump. Graph edges, sparse matrices and SCC labels are reconstructed separately. The degree-peel algorithm is standard and shared in kind with C, not claimed algorithmically independent.

Replays from W = 16 (or a digest-bound, already independently checked prefix): the gate's greatest fixed point, the certified targets, the lift, the linear degree peel, the
components (scipy), and for each component with a cycle its nodes, edges, gcd, kind and gaps. Compares with the
C's jsonl, and with its core dumps when --dumps is given. Exit 0 and a line PASS only if every width agrees.

Usage: check_lift.py --targets FILE --mode xx|pq --wmax N --scc JSONL [--dumps DIR] [--wfrom N]
"""
import argparse, json, sys, time, collections
from math import gcd
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components, dijkstra

ap = argparse.ArgumentParser()
ap.add_argument('--targets', required=True); ap.add_argument('--mode', default='xx'); ap.add_argument('--wmax', type=int, default=30)
ap.add_argument('--scc', required=True); ap.add_argument('--dumps'); ap.add_argument('--wfrom', type=int, default=16)
ap.add_argument('--resume-width', type=int); ap.add_argument('--resume-dump'); ap.add_argument('--resume-sha256')
a = ap.parse_args()
T = {}
for line in open(a.targets):
    if line[0] != '#':
        p = line.split(); T[p[0]] = p[1:]
wall = np.zeros((4, 1 << 13), dtype=bool)
w = T['wall'][1:]
for i in range(0, len(w), 2): wall[int(w[i]), int(w[i + 1])] = True
L7 = np.array(sorted(map(int, T['lock7'][2:])), dtype=np.int64)
L7B = np.array(sorted(map(int, T['lock7b'][2:])), dtype=np.int64)
S7 = np.array(sorted(map(int, T['sevenlock'][2:])), dtype=np.int64)
lock, lockw = (L7, 30) if a.mode == 'xx' else (S7, 32)
ETH = ['0011', '0110', '1101', '0101', '0011', '0001', '0001']
def pattern(q): return sum(int(ETH[(3 + p) % 7][q]) << (p - 1) for p in range(1, 63))
PAT = {0: pattern(0), 2: pattern(2)}

def moves(c, W):
    """All four moves as an array (4, n)."""
    mask = np.int64((1 << W) - 1); out = []
    for x in range(4):
        if a.mode == 'xx':
            b = c | (np.int64(x) << np.int64(W))
            b = (b << 1) ^ (b | (b >> 1))
            b = ((b << 1) | 1) ^ (b | (b >> 1))
            out.append(b & mask)
        else:
            x1, x2 = x >> 1, x & 1; top = np.int64(1) << np.int64(W - 1)
            b = c
            for cen, bey in ((0, x1), (1, x2)):
                b = (((b << 1) | cen) & mask) ^ (b | (b >> 1) | (top if bey else np.int64(0)))
            out.append(b)
    return np.stack(out)

def gate():
    n = 1 << 16
    mv = moves(np.arange(n, dtype=np.int64), 16)
    bad = np.zeros((n, 6), dtype=bool)
    while True:
        new = bad.copy()
        for d in range(6):
            for j in range(4):
                v = mv[j]; b = (v & 1).astype(bool)
                if d == 5:
                    ok = np.ones(n, dtype=bool); nx = np.where(b, 0, 5)
                else:
                    g = d + 1
                    ok = np.where(b, g in (3, 5), g < 5); nx = np.where(b, 0, min(g, 4))
                new[:, d] |= ~ok | bad[v, nx]
        if (new == bad).all(): break
        bad = new
    e = ~bad[:, 0]; e[0::2] = False
    return e

G = gate()
print('gate entry windows', int(G.sum()), flush=True)

def target(c, W):
    t = G[c & 0xFFFF].copy()
    for q in (0, 2):
        for k in range(6, W - 12, 7):
            t |= (((c ^ np.int64(PAT[q] & ((1 << k) - 1))) & np.int64((1 << k) - 1)) == 0) & wall[q, (c >> np.int64(k)) & 0x1FFF]
    if W >= lockw: t |= np.isin(c & np.int64((1 << lockw) - 1), lock)
    if a.mode == 'xx' and W >= 45: t |= np.isin(c & np.int64((1 << 45) - 1), L7B)
    return t

def edges(c, W):
    if not len(c):
        return np.array([], dtype=np.int64), np.array([], dtype=np.int64)
    mv = moves(c, W); n = len(c); S = []; D = []; ids = np.arange(n)
    for j in range(4):
        p = np.searchsorted(c, mv[j]); p[p >= n] = 0
        ok = c[p] == mv[j]
        S.append(ids[ok]); D.append(p[ok])
    k = np.unique(np.concatenate(S) * n + np.concatenate(D))
    return k // n, k % n

def peel(c, W):
    # Same standard directed-core criterion as C; independent sparse matrices,
    # degree accounting and remapping. Avoid rebuilding every peel round.
    S, D = edges(c, W); n = len(c)
    if not n: return c, S, D
    g = csr_matrix((np.ones(len(S), dtype=np.int8), (S, D)), shape=(n, n))
    rev = g.T.tocsr()
    din = np.diff(rev.indptr).astype(np.int64)
    dout = np.diff(g.indptr).astype(np.int64)
    dead = (din == 0) | (dout == 0)
    q = np.empty(n, dtype=np.int64)
    initial = np.flatnonzero(dead); q[:len(initial)] = initial
    head, tail = 0, len(initial)
    while head < tail:
        v = q[head]; head += 1
        for j in range(g.indptr[v], g.indptr[v + 1]):
            x = g.indices[j]
            if not dead[x]:
                din[x] -= 1
                if din[x] == 0:
                    dead[x] = True; q[tail] = x; tail += 1
        for j in range(rev.indptr[v], rev.indptr[v + 1]):
            x = rev.indices[j]
            if not dead[x]:
                dout[x] -= 1
                if dout[x] == 0:
                    dead[x] = True; q[tail] = x; tail += 1
    keep = ~dead
    remap = np.full(n, -1, dtype=np.int64)
    remap[keep] = np.arange(int(keep.sum()))
    good = keep[S] & keep[D]
    return c[keep], remap[S[good]], remap[D[good]]

def comps(c, S, D):
    n = len(c)
    if not n: return []
    g = csr_matrix((np.ones(len(S), dtype=np.int8), (S, D)), shape=(n, n))
    nc, lab = connected_components(g, directed=True, connection='strong')
    size = np.bincount(lab, minlength=nc)
    loop = np.zeros(nc, bool); loop[lab[S[S == D]]] = True
    res = []
    for k in np.nonzero((size > 1) | loop)[0]:
        v = np.nonzero(lab == k)[0]
        sub = g[v][:, v].tocsr().astype(np.int32)
        cs = sub.tocoo()
        dist = dijkstra(sub, unweighted=True, indices=0).astype(np.int64)
        gg = int(np.gcd.reduce(np.abs(dist[cs.row] + 1 - dist[cs.col])))
        black = (c[v] & 1).astype(bool)
        cls = dist % gg if gg else dist * 0
        locked = bool(gg) and all(len(set(black[cls == r].tolist())) <= 1 for r in range(gg))
        cur = black.copy(); gaps = []
        A = sub.T.tocsr()
        for gp in range(1, 31):
            if not cur.any(): break
            nx = (A @ cur.astype(np.int32)) > 0
            if (nx & black).any(): gaps.append(gp)
            cur = nx & ~black
        kind = 'LOCKED' if locked else ('GAP35' if set(gaps) <= {3, 5} and not cur.any() else 'UNRESOLVED')
        res.append((len(v), int(cs.nnz), gg, kind, '[' + ','.join(map(str, gaps)) + ']'))
    return sorted(res, reverse=True)

ref = collections.defaultdict(list)
for line in open(a.scc):
    r = json.loads(line)
    if r['stage'] == 'CORE': ref[r['W']].append((r['nodes'], r['edges'], r['gcd'], r['kind'], r['gaps']))
W = 16
c = np.nonzero(~G)[0].astype(np.int64)
fails = 0; t0 = time.process_time()
if a.resume_dump:
    import hashlib
    from pathlib import Path
    data = Path(a.resume_dump).read_bytes()
    assert a.resume_width and a.resume_sha256 and len(data) % 8 == 0
    assert hashlib.sha256(data).hexdigest() == a.resume_sha256, 'resume digest'
    W = a.resume_width
    c = np.frombuffer(data, dtype=np.uint64).astype(np.int64)
    assert ((c[1:] > c[:-1]).all() and (c >= 0).all() and (c < (1 << W)).all())
    assert a.wfrom > W, 'resume requires independently checked prefix through W'
    S, D = edges(c, W)
else:
    c, S, D = peel(c, W)
while True:
    if W >= a.wfrom:
        mine = comps(c, S, D)
        theirs = sorted(ref[W], reverse=True)
        same = mine == theirs
        dig = ''
        if a.dumps:
            import os
            p = '%s/core_%d_%s.bin' % (a.dumps, W, a.mode)
            assert os.path.isfile(p) and os.path.getsize(p) % 8 == 0, ('missing/truncated dump', p)
            d = np.fromfile(p, dtype=np.uint64).astype(np.int64)
            dig = ' dump %s' % ('same' if len(d) == len(c) and (d == c).all() else 'DIFFERENT')
            fails += 'DIFFERENT' in dig
        print('W', W, 'core', len(c), 'components', len(mine), 'agree' if same else 'DISAGREE', dig, 'cpu', round(time.process_time() - t0, 1), flush=True)
        if not same:
            fails += 1
            print(' mine  ', mine[:6]); print(' theirs', theirs[:6])
    if W >= a.wmax: break
    W += 1
    c = np.concatenate([c, c | (np.int64(1) << np.int64(W - 1))])
    c = c[~target(c, W)]
    c, S, D = peel(c, W)
print('PASS' if not fails else 'FAIL %d' % fails)
sys.exit(1 if fails else 0)
