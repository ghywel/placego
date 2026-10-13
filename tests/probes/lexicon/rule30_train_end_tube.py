#!/usr/bin/env python3
"""rule30_train_end_tube.py: Local's second read of GPT's GC1195 (the bounded diagonal tube for finite ends of the train
ray) and the R = 3 packet test GPT registered there, by direct crop evolution written here.

The slice (GC1193 .. GC1195): r = 0, p = 0, N = 2, T = 1. The reference S = 1011 (0000111)^infinity gives the child row
A = (0110010)^infinity with clamped rows A_t(j) = R_(t mod 4)[(-j) mod 7] (L679 M1). A finite seed v (here the minimal
completions v(k) of S's first k bits, GC1193/1194) first differs from S at seed index q; the child's first differing
depth at tick 0 is ell = q - 2. The tube d_s(t) = b_t(n + s) XOR A_t(n + s), n = ell - t, 0 <= s <= R, d_0 = 1, evolves
by GC1195's update until the front reaches depth 1 at tick ell - 1; then the cells b_(ell-1)(1 .. R+1) are rebuilt and
evolved with the real wall for R ticks. GC1195 proves the endpoint row and that R + 1 tick trace repeat with k modulo
M_R = 28 * 2^R, and the guard W = ell + R <= h + R - 1 <= J needs L >= R - 1.

RUN-ON:     cpu, numpy, the certified cut lists in the RLK scratch; seconds.
COMMAND:    python3 tests/probes/lexicon/rule30_train_end_tube.py

Record searched (record_find, 2026-10-13 19:08 BST): 'tube' -> 24 hits in 5 files (GC1195 and its predecessors' uses, a
SPARKS note, this file); 'train ray|train-ray' -> 5 hits in 3 files (GC1193 .. GC1195, a board line, this file);
GC1193 .. GC1195 and L677 .. L679 read.

PREDICTIONS (written 2026-10-13 19:08 BST, before any run).
  U1 must hold (tube = direct): for k = 6 .. 400, GC1195's tube with R = 3, run from the directly computed initial
     packet, gives endpoint cells b_(ell-1)(1 .. 4) equal to the direct clamped evolution's child row at tick ell - 1.
  U2 must hold (the carrying period, directly): for every k = 6 .. 400 the endpoint 4-cell row and the 4-tick trace at
     ticks ell - 1 .. ell + 2 are the same at k and k + 224.
  U3 must hold (the R = 1 control): the k whose first arrival and next black tick pass are exactly k mod 56 in
     {10, 11, 27, 30, 35, 47, 50} (L679 M4).
  U4 must hold (the wall handoff): carrying the free tube past depth 1 (a fictitious wall difference) disagrees with the
     clamped evolution of the rebuilt cells on the 4-tick trace for some k.
  U5 blind (0.55, GPT's GC1195 prediction): of the 28 representatives k = 224 + r lifting the seven classes, exactly 14
     packets are OPEN under the four-tick test (clock at the two black ticks, 11 against the previous train white
     sample). Counterfactual: all 28 fail. The full verdict at window ell + 3 (every certified cut) is reported too.

OUTCOME (2026-10-13 19:09 BST, M5, 1 s; machine output quoted): U1 HELD, U2 HELD, U3 HELD, U4 HELD, U5 HELD.
  R3 packets OPEN: 14 of 28 (GPT's predicted number exactly). By endpoint row and four-tick trace: [1,0,1,0] / 1111 OPEN
     (10 representatives: k = 234, 235, 251, 315, 327, 346, 347, 363, 427, 439, i.e. k mod 224 in {10, 11, 27, 91, 103,
     122, 123, 139, 203, 215}); [1,0,0,0] / 1101 OPEN under the four-tick test (k = 274, 310, 386, 422); [1,0,1,1] / 1110
     and [1,0,0,1] / 1100 fail. The full verdict at window ell + 3 (every certified cut) agrees except on the four 1101
     packets, which it fails, leaving 10 of 28 open.

ADDENDUM PREDICTION (2026-10-13 19:19 BST, before the run): GPT's GC1196 cause for the four extra rejections.
  V1 must hold: for k = 50, 86, 162, 198 and their lifts k + 224, k + 448, the child's visible word over the window
     ell + 3 is (10)^n 0 1 with n >= 2, its last six symbols are 101001, that word is in the phase-0 certified list
     (mfw44all), and no proper suffix of 101001 is in the list (so 101001 is the cut that fires at tick ell + 1).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
from rule30_seed_prefix_tree import AhoCorasick, child_alive               # Local's own (L677 .. L679)

RR = ['0100110', '1111101', '0000001', '1000011']
SEVEN = {10, 11, 27, 30, 35, 47, 50}


def A(t, j):
    return int(RR[t % 4][(-j) % 7])


def S_bits(n):
    return ([1, 0, 1, 1] + [0, 0, 0, 0, 1, 1, 1] * (n // 7 + 2))[:n]


def decode(bits):
    b0, b1 = 0, 1 - (bits[3] ^ bits[1])
    for u in bits[4:]:
        b0, b1 = b1, u ^ (b0 | b1)
    return b0, b1


def completion(k):
    pre = S_bits(k)
    return pre + ([1, 1] if decode(pre) == (1, 0) else [1])


def child_row0(v, W):
    """Child depths 1 .. W at tick 0: V_(kk+2)(1) of the ordinary seed v (zero padded), by one full-line step."""
    vv = list(v) + [0] * (W + 6)
    x = np.zeros(len(vv) + 6, dtype=np.uint8)
    off = len(vv) + 2                                    # site s at index off + s, sites -len .. 2
    for i, b in enumerate(vv):
        x[off - i] = b
    x1 = np.zeros_like(x)
    x1[1:-1] = x[:-2] ^ (x[1:-1] | x[2:])               # new(i) = x(i-1) XOR (x(i) OR x(i+1))
    return [int(x1[off - kk - 1]) for kk in range(1, W + 1)]


def clamped(row, ticks, p=0):
    """Rows of the clamped child evolution: list of numpy rows (index 0 = wall) for ticks 0 .. ticks."""
    W = len(row)
    r = np.zeros(W + 2, dtype=np.uint8)
    r[1:W + 1] = row
    out = []
    for t in range(ticks + 1):
        r[0] = (t + p) % 2
        out.append(r.copy())
        nr = r.copy()
        nr[1:W + 1] = r[2:W + 2] ^ (r[1:W + 1] | r[0:W])
        r = nr
    return out


def first_q(v):
    S = S_bits(len(v) + 20)
    return next(i for i in range(len(S)) if (v[i] if i < len(v) else 0) != S[i])


def tube(ell, init, R, steps):
    """GC1195's tube from t = 0 for `steps` updates; init = d_0 .. d_R at t = 0."""
    d = list(init)
    for t in range(steps):
        n = ell - t
        nd = d[:]
        for s in range(1, R + 1):
            a, c = A(t, n - 1 + s), A(t, n - 2 + s)
            dm1 = d[s - 1]
            dm2 = d[s - 2] if s >= 2 else 0
            nd[s] = d[s] ^ ((a ^ dm1) | (c ^ dm2)) ^ (a | c)
        d = nd
    return d


def packet(k, R=3):
    v = completion(k)
    q = first_q(v)
    ell = q - 2
    W = ell + R
    row0 = child_row0(v, W + 2)[:W + 1]
    rows = clamped(row0, ell + R)
    end_direct = [int(rows[ell - 1][j]) for j in range(1, R + 2)]
    init = [row0[ell - 1 + s] ^ A(0, ell + s) for s in range(R + 1)]
    d = tube(ell, init, R, ell - 1)
    end_tube = [A(ell - 1, j) ^ d[j - 1] for j in range(1, R + 2)]
    trace = [int(rows[t][1]) for t in range(ell - 1, ell + R)]
    return dict(k=k, q=q, ell=ell, W=W, row0=row0, end_direct=end_direct, end_tube=end_tube, trace=trace, d=d, v=v)


def four_tick_open(P):
    """Clock at black ticks and 11 (with the previous train white sample) over ticks ell - 1 .. ell + 2."""
    ell, tr = P['ell'], P['trace']
    prev_vis = 1 - [0, 1, 1, 1][(ell - 3) % 4]
    vis = [prev_vis]
    for i, t in enumerate(range(ell - 1, ell + 3)):
        if t % 2 == 1:
            if tr[i] != 1:
                return False
        else:
            vis.append(1 - tr[i])
            if vis[-1] == 1 and vis[-2] == 1:
                return False
    return True


def main():
    import rule30_relaxed_records_k as rlk
    ac0 = AhoCorasick(rlk.load_forbidden('44all') + rlk.load_cuts(0, 40))
    ok = {}
    U1 = U2 = True
    cache = {}
    for k in range(6, 401):
        P = cache.setdefault(k, packet(k))
        Q = cache.setdefault(k + 224, packet(k + 224))
        U1 &= P['end_tube'] == P['end_direct']
        U2 &= P['end_direct'] == Q['end_direct'] and P['trace'] == Q['trace']
    ok['U1'], ok['U2'] = U1, U2
    two = set()
    for k in range(6, 4 + 7 * 24 + 1):
        P = cache.setdefault(k, packet(k))
        ell, tr = P['ell'], P['trace']
        a = ell - 1
        g1 = a % 2 == 0 and a % 4 != 2 and tr[0] != [0, 1, 1, 1][a % 4]
        if g1 and tr[1] == 1:
            two.add(k % 56)
    ok['U3'] = two == SEVEN
    U4 = False
    for k in range(6, 401):
        P = cache[k]
        if P['ell'] < 2:
            continue
        d = tube(P['ell'], [P['row0'][P['ell'] - 1 + s] ^ A(0, P['ell'] + s) for s in range(4)], 3, P['ell'] - 1 + 3)
        fake = [A(P['ell'] - 1 + 3, 1) ^ d[3]]                # after 3 more steps the front is at n = -2, so depth 1 is s = 3
        if fake[0] != P['trace'][3]:
            U4 = True
            break
    ok['U4'] = U4
    reps = [k for k in range(224, 448) if k % 56 in SEVEN]
    opens, rows = 0, []
    for k in reps:
        P = cache.setdefault(k, packet(k))
        o = four_tick_open(P)
        full = bool(child_alive(np.array([P['row0'][:P['W']]], dtype=np.uint8), 0, ac0)[0])
        opens += o
        rows.append((k, k % 56, P['end_direct'], ''.join(map(str, P['trace'])), 'OPEN' if o else 'fail', 'full ' + ('pass' if full else 'fail')))
    ok['U5'] = opens == 14
    print('GC1195 read:', {kk: ('HELD' if vv else 'FAILED') for kk, vv in ok.items()}, '| R3 packets OPEN: %d of %d' % (opens, len(reps)))
    for r in rows:
        print('  k=%d (mod 56 = %d): endpoint row %s, trace %s, %s, %s' % r)


def suffix_check():
    import rule30_relaxed_records_k as rlk
    L0 = set(rlk.load_forbidden('44all') + rlk.load_cuts(0, 40))
    ok = '101001' in L0 and not any('101001'[i:] in L0 for i in range(1, 6))
    for k0 in (50, 86, 162, 198):
        for k in (k0, k0 + 224, k0 + 448):
            P = packet(k)
            rows = clamped(P['row0'], P['W'] - 1)
            vis = ''.join(str(1 - int(rows[t][1])) for t in range(0, P['W'], 2))
            n = (len(vis) - 2) // 2
            ok &= vis == '10' * n + '01' and n >= 2 and vis.endswith('101001')
    print('V1 GC1196 suffix 101001 at k = 50, 86, 162, 198 and lifts:', 'HELD' if ok else 'FAILED')
    return ok


if __name__ == '__main__':
    main()
