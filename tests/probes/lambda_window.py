#!/usr/bin/env python3
"""L1305 T27 (Local, 2026-11-02): the coin as a window function, and the lambda-recursion.
reports/rule30-genealogy.md section 31 (predictions written first). Run: python3 tests/probes/lambda_window.py

Digits are time-0 digits behind the front, with the front (1) and the white region (0) prepended; the white-boundary
map c(x) = x ^ ((x << 1) | (x << 2)) on that sequence is Phi = a on the digits. A window of 2L digits is an integer
whose bit 2L-1 is the node's digit n. F_L(window) = parity over t < L of (bit 2L-1 OR bit 2L-2) of c^t(window).
Parts: A (P27a) depth of lambda_L; B (P27b) the halving identity and agreement with the tree's coin; C (P27c) the
influence profile over uniform windows; D (P27d) the profile at actual top-layer windows of T_64 and T_128.
"""
import random


def c_step(x, mask):
    return (x ^ ((x << 1) | (x << 2))) & mask


def a_step(x):
    return x ^ ((x << 1) | (x << 2) | 3)


def F(w, L):
    """Coin of a window of 2L digits (bit 2L-1 = the node's digit)."""
    W = 2 * L; mask = (1 << W) - 1; x = w; s = 0
    for _ in range(L):
        s ^= ((x >> (W - 1)) | (x >> (W - 2))) & 1
        x = c_step(x, mask)
    return s


def influence(w, L):
    base = F(w, L)
    return [F(w ^ (1 << (2 * L - 1 - j)), L) ^ base for j in range(2 * L)]


def profile(rows, L, bins=20):
    n = len(rows); out = []
    for b in range(bins):
        lo, hi = int(b * 2 * L / bins), int((b + 1) * 2 * L / bins)
        tot = sum(sum(r[lo:hi]) for r in rows); out.append(tot / (n * (hi - lo)))
    return out


def crossing(rows, L, level=0.25):
    n = len(rows); I = [sum(r[j] for r in rows) / n for j in range(2 * L)]
    for j in range(2 * L):
        if all(I[k] < level for k in range(j, min(2 * L, j + 4))):
            return j / L, I
    return None, I


rng = random.Random(27)
print('== A (P27a): depth of lambda_L = a^L c^-L')
ok = True
for L in range(1, 65):
    z = 0
    for _ in range(L):
        z = a_step(z)
    if z.bit_length() != 2 * L:            # lambda_L(0) = a^L(0) has highest bit 2L-1
        ok = False
    for _ in range(20):                    # a^L z xor c^L z has no bit >= 2L
        N = 2 * L + 16; mask = (1 << N) - 1; x = y = rng.getrandbits(N)
        for _ in range(L):
            x = a_step(x) & mask; y = c_step(y, mask)
        if (x ^ y) >> (2 * L):
            ok = False
print('depth exactly 2L for L = 1..64 (lambda_L(0) top bit 2L-1; no change at bits >= 2L on random inputs):', ok)

print('== B (P27b): F_2L(z) = F_L(z) xor F_L(c^L z) on random windows')
bad = 0
for L in (1, 2, 4, 8, 16, 32):
    for _ in range(300):
        w4 = rng.getrandbits(4 * L); mask = (1 << (4 * L)) - 1
        x = w4
        for _ in range(L):
            x = c_step(x, mask)
        top = lambda v: v >> (2 * L)
        if F(w4, 2 * L) != F(top(w4), L) ^ F(top(x), L):
            bad += 1
print('failures', bad, 'of', 6 * 300)


def layer_windows(p, every=1, cap=None):
    """Windows of top-layer nodes of T_p (shortest rain prefix: columns 0, 1, a, a), with the tree's own coin."""
    M = (1 << p) - 1; A = sum(1 << t for t in range(1, p, 2))

    def integ(d, L):
        w, acc = 0, 0
        for t in range(L):
            if acc:
                w |= 1 << t
            acc ^= (d >> t) & 1
        return w

    def per(w, L):
        out = 0
        for t in range(p):
            out |= ((w >> (t % L)) & 1) << t
        return out
    out = []; count = 0
    # nodes are (parent, column, depth of that column); the chain starts at the front: depth -2 (0), -1 (all ones)
    root = (((None, 0, -2), M, -1), A, 0)
    st = [(((root, A, 1)), 1)]
    while st:
        node, H = st.pop()
        (parent, v, n) = node; u = parent[1]; L = 2 * H
        d = (u | v) & ((1 << L) - 1); sp = bin(d).count('1') & 1
        if L == p:
            count += 1
            if count % every == 0:
                win = 0; x = node
                for j in range(2 * p - 1, -1, -1):     # window bit j <- digit n - (2p - 1 - j)
                    k = n - (2 * p - 1 - j)
                    if x is not None and x[2] == k:
                        bit = x[1] & 1; x = x[0]
                    else:
                        bit = 0                        # above the front: white
                    win |= bit << j
                out.append((win, sp))
                if cap and len(out) >= cap:
                    break
        H2 = 2 * H if sp else H
        if 2 * H2 > p:
            continue
        L2 = 2 * H2; w0 = integ(u | v, L2)
        for w in ([per(w0, L2)] if sp else [per(w0, L2), per(w0 ^ ((1 << L2) - 1), L2)]):
            st.append(((node, w, n + 1), H2))
    return out, count


print('== B continued: F_p(window) equals the tree coin at top-layer nodes')
for p, every in ((64, 1), (128, 400)):
    wins, count = layer_windows(p, every)
    bad = sum(1 for w, sp in wins if F(w, p) != sp)
    print('p %d: top-layer nodes %d, checked %d, coin mismatches %d' % (p, count, len(wins), bad))

print('== C (P27c): influence profile over uniform windows (bins of j/L, width 0.1)')
for L, n in ((16, 2000), (32, 1500), (64, 800)):
    rows = [influence(rng.getrandbits(2 * L), L) for _ in range(n)]
    pr = profile(rows, L); cr, _ = crossing(rows, L)
    print('L %d, %d windows: crossing of 0.25 at j/L = %s' % (L, n, None if cr is None else '%.3f' % cr))
    print('  ' + ' '.join('%.2f' % x for x in pr))

print('== D (P27d): influence profile at actual top-layer windows')
for p, every, cap in ((64, 1, None), (128, 700, 1600)):
    wins, count = layer_windows(p, every, cap)
    rows = [influence(w, p) for w, _ in wins]
    uni = [influence(rng.getrandbits(2 * p), p) for _ in range(len(rows))]
    pr, pu = profile(rows, p), profile(uni, p); cr, _ = crossing(rows, p)
    print('p %d: %d actual windows; crossing of 0.25 at j/L = %s' % (p, len(rows), None if cr is None else '%.3f' % cr))
    print('  actual  ' + ' '.join('%.2f' % x for x in pr))
    print('  uniform ' + ' '.join('%.2f' % x for x in pu))
    print('  largest |difference| %.3f' % max(abs(x - y) for x, y in zip(pr, pu)))

print('== D continued: p = 128 windows split by whether they reach into the white region above the front')
wins, count = layer_windows(128, 350, 3200)
shallow = [w for w, _ in wins if (w & 0xF) == 0]   # four shallowest digits white: the window reaches above the front
deep = [w for w, _ in wins if (w & 0xF) != 0]
for name, ws in (('reaching above the front', shallow), ('starting below the front', deep)):
    rows = [influence(w, 128) for w in ws[:900]]
    print('  %-25s %4d windows: %s' % (name, len(ws), ' '.join('%.2f' % x for x in profile(rows, 128))))

