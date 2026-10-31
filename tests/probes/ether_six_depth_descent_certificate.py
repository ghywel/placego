#!/usr/bin/env python3
"""ether_six_depth_descent_certificate.py -- a complete computer-assisted proof that no exact ether-pair episode of
length floor(2k/3)+4 exists at any depth k = 0 or 2 (mod 6), k >= 1, behind a black edge (PR69 edge frame), for any
row and any phase. It is an induction on six-depth slabs whose invariant is the exact episode itself.

RUN-ON:     cpu (Python 3 + numpy + kissat and cadical), about 10 seconds
COMMAND:    python3 tests/probes/ether_six_depth_descent_certificate.py

Provenance (L1259): written by a sub-agent of Local in the round-5 proof workflow (route "alternative certificate")
and read in full by Local before it entered the record. Same worker: GPT's carrying read of the hand steps D and I
is still required. It is a stronger form of Local's own rigidity step (ether_rigidity_certificate.py: edge phase 7,
L' = m(K)+4, free-column region): here every phase and every window of length >= 11, on the exact light cone.

FRAME. Digits X_j(t), t >= 0. Generic model: j in Z, X_j(t+1) = X_j(t) XOR (X_{j-1}(t) OR X_{j-2}(t)), any initial
state. Edge model (PR69): X_0 = 1, X_1(t+1) = NOT X_1(t), X_j(t+1) = X_j(t) XOR (X_{j-1}(t) OR X_{j-2}(t)) for j >= 2.
The edge model is the generic model restricted to initial states ...0001 x_1 x_2 ... (check G0 below).
Ether: E_j(t) = e(t + 2j + c), e = bits of 43 = (1,1,0,1,0,1,0,0); PR69's ether(i,t) = bit (t mod 8) of
(43,202,178,172)[i mod 4] equals e(t + 2i). A pair at depth j is (X_{j+1}, X_j); "exact at tick t" means it equals
(E_{j+1}(t), E_j(t)). An episode of length L at depth k: the pair at depth k exact on ticks 0..L-1.

THE CERTIFICATE.
 W  (window instances, finite and exhaustive). For every phase c' in Z/8 of the ether at the top depth (relative depth
    0, E_0(t) = e(t + c')) and every (s, b) in INSTANCES: for EVERY assignment of the initial digits at relative depths
    lo..1 (lo = min(-2(s+b), -6-2s)), if the pair at relative depth 0 is exact on ticks 0..s+b, then the pair at
    relative depth -6 is exact at tick s. By the light cone (X_j(t) depends only on X_{j-2t..j}(0)) no other digit can
    influence any cell involved, so this quantifies over every generic configuration. Checked three ways: packed
    bit-parallel enumeration, unpacked numpy enumeration, and SAT (kissat and cadical, UNSAT of the negation).
    Controls: with one tick less look-ahead every s fails for some phase (the checker sees violations; windows tight).
 D  (six-depth descent, by hand from W). For every generic configuration, phase, depth j and L >= 11: if the pair at
    depth j is exact on 0..L-1 then the pair at depth j-6 is exact on 0..L-5. For s in 6..L-5 apply W(6,4) to the
    time-shifted configuration X(. + s - 6) (any state is an initial state; its window [s-6, s+4] lies in [0, L-1]);
    for s in 0..5 apply W(s, b_s) directly (its window [0, s+b_s] lies in [0, 10] subset of [0, L-1]). Depth
    translation moves the top to relative depth 0 and shifts the phase by 2 per level; all 8 phases are covered.
 B  (base, exhaustive). No episode of length m+4 at k = 2, 6, 8 (all prefixes, all 32 PR69 phases; and SAT).
 I  (induction, by hand). If k = 0, 2 (mod 6), k >= 12, had an episode of length m(k)+4 >= 12 >= 11, D gives one of
    length m(k) = m(k-6)+4 at depth k-6; descending reaches k = 6 or 8, contradicting B. So M(k) <= m+3 for all such k
    (k = 2 is in B). With the two-party witness (M(k) >= m+3) this gives M(k) = floor(2k/3)+3 there.
 Corollary (same lemma, base k <= 8): M(k) <= L_w(k) = ceil((4 ceil(k/2)+8)/3) for every k >= 1 (episode of length
    L_w(k)+1 >= 11 for k >= 9 descends to k-6 with length L_w(k-6)+1); so M(k) = floor(2k/3)+4-[k = 0,2 mod 6] for all
    k >= 1 given the witness, independently of GC2327's upper bound.
"""
import hashlib
import os
import random
import subprocess
import sys
import tempfile

import numpy as np

WORDS = (43, 202, 178, 172)
E8 = [(43 >> s) & 1 for s in range(8)]
INSTANCES = [(0, 10), (1, 6), (2, 6), (3, 5), (4, 5), (5, 4), (6, 4)]     # (s, look-ahead b); window 0..s+b
DEPTH = 6
HERE = os.path.dirname(os.path.abspath(__file__))
WORK = tempfile.mkdtemp(prefix='cert-', dir=os.environ.get('CAPPED_OUT', HERE))
ONES = np.uint64(0xFFFFFFFFFFFFFFFF)


def ether(i, t):
    return (WORDS[i % 4] >> (t % 8)) & 1


# ---------------------------------------------------------------- G: ground facts about the frame
def check_ground():
    for i in range(4):
        for t in range(8):
            assert ether(i, t) == E8[(t + 2 * i) % 8]
            assert ether(i, t + 1) == ether(i, t) ^ (ether(i + 3, t) | ether(i + 2, t))       # PR69 ether_step
            assert ether(i + 2, t + 4) == ether(i, t)                                         # glide
    for c in range(8):
        for j in range(-12, 12):
            for t in range(16):
                E = lambda jj, tt: E8[(tt + 2 * jj + c) % 8]
                assert E(j, t + 1) == E(j, t) ^ (E(j - 1, t) | E(j - 2, t))                   # ether solves the recurrence
                assert E(j + 6, t + 4) == E(j, t) and E(j + 3, t + 2) == E(j, t)             # (6,4) and (3,2) symmetries
    # G0: edge model = generic model on initial states ...0 0 1 x_1 x_2 ...
    rng = random.Random(20261031)
    for _ in range(300):
        n = 30
        x = [rng.randrange(2) for _ in range(n)]
        edge = [1] + x                                   # depths 0..n
        gen = {j: 0 for j in range(-80, 0)}
        gen.update({j: edge[j] for j in range(n + 1)})
        for t in range(20):
            for j in range(n + 1):
                assert gen[j] == edge[j]
            ne = edge[:]
            ne[1] = 1 - edge[1]
            for j in range(2, n + 1):
                ne[j] = edge[j] ^ (edge[j - 1] | edge[j - 2])
            ng = {}
            for j in gen:
                if (j - 1) in gen and (j - 2) in gen:
                    ng[j] = gen[j] ^ (gen[j - 1] | gen[j - 2])
            edge, gen = ne, ng
    # G1: light cone -- flipping a digit outside [j-2t, j] never changes X_j(t)
    for _ in range(200):
        lo, hi = -40, 2
        x = {j: rng.randrange(2) for j in range(lo, hi + 1)}
        jj, tt = rng.randrange(-10, 2), rng.randrange(0, 8)
        flip = rng.choice([d for d in range(lo, hi + 1) if d < jj - 2 * tt or d > jj])
        vals = []
        for xx in (x, {**x, flip: 1 - x[flip]}):
            X = dict(xx)
            for t in range(tt):
                X = {j: X[j] ^ (X[j - 1] | X[j - 2]) for j in X if (j - 1) in X and (j - 2) in X}
            vals.append(X[jj])
        assert vals[0] == vals[1]
    print("G: ether identities, (6,4)/(3,2) symmetries, edge = generic on ...001x (300 rows x 20 ticks), light cone: PASS")


# ---------------------------------------------------------------- W: window instances, three independent checkers
def digit_bitsets(n):
    W = 1 << (max(n, 6) - 6)
    w = np.arange(W, dtype=np.uint64)
    out = []
    for i in range(max(n, 6)):
        if i < 6:
            pat = sum(1 << b for b in range(64) if (b >> i) & 1)
            out.append(np.full(W, np.uint64(pat), dtype=np.uint64))
        else:
            out.append(np.where(((w >> np.uint64(i - 6)) & np.uint64(1)) == 1, ONES, np.uint64(0)))
    return out[:n]


def popcount(a):
    return int(sum(bin(int(x)).count('1') for x in a[a != 0]))


def check_packed(cp, s, b, D=DEPTH):
    T = s + b
    lo = min(-2 * T, -D - 2 * s)
    n = 2 - lo
    bits = digit_bitsets(n)
    X = {lo + i: bits[i] for i in range(n)}
    E = lambda j, t: E8[(t + 2 * j + cp) % 8]
    ok = np.full(len(bits[0]), ONES, dtype=np.uint64)
    bad = None
    for t in range(T + 1):
        for j in (0, 1):
            ok &= X[j] if E(j, t) else ~X[j]
        if t == s:
            bad = np.zeros_like(ok)
            for j in (-D, -D + 1):
                bad |= (~X[j]) if E(j, t) else X[j]
        if t < T:
            X = {j: X[j] ^ (X[j - 1] | X[j - 2]) for j in X if (j - 1) in X and (j - 2) in X}
    return popcount(ok & bad), popcount(ok)


def check_unpacked(cp, s, b, D=DEPTH):
    T = s + b
    lo = min(-2 * T, -D - 2 * s)
    n = 2 - lo
    N = 1 << n
    idx = np.arange(N, dtype=np.int64)
    X = {lo + i: ((idx >> i) & 1).astype(np.uint8) for i in range(n)}
    E = lambda j, t: E8[(t + 2 * j + cp) % 8]
    ok = np.ones(N, dtype=bool)
    bad = None
    for t in range(T + 1):
        ok &= (X[0] == E(0, t)) & (X[1] == E(1, t))
        if t == s:
            bad = (X[-D] != E(-D, t)) | (X[-D + 1] != E(-D + 1, t))
        if t < T:
            X = {j: X[j] ^ (X[j - 1] | X[j - 2]) for j in X if (j - 1) in X and (j - 2) in X}
    return int((ok & bad).sum()), int(ok.sum())


def sat_solve(nv, cl, solver):
    fd, path = tempfile.mkstemp(suffix='.cnf', dir=WORK)
    with os.fdopen(fd, 'w') as f:
        f.write(f"p cnf {nv} {len(cl)}\n" + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
    try:
        p = subprocess.run([solver, '-q', '-n', path], capture_output=True, text=True)
    finally:
        os.remove(path)
    assert p.returncode in (10, 20), (solver, p.returncode, p.stderr[-300:])
    return p.returncode == 10


def check_sat(cp, s, b, solver, D=DEPTH):
    """SAT of: generic cone, top exact on 0..s+b, pair at -D not exact at s. Expect UNSAT."""
    T = s + b
    lo0 = min(-2 * T, -D - 2 * s) - 4
    v = {}

    def var(j, t):
        if (j, t) not in v:
            v[(j, t)] = len(v) + 1
        return v[(j, t)]
    cl = []
    for t in range(T + 1):
        for j in range(lo0 + 2 * t, 2):
            var(j, t)
    for t in range(T):
        for j in range(lo0 + 2 * (t + 1), 2):
            a, bb, c, d = var(j, t), var(j, t + 1), var(j - 1, t), var(j - 2, t)
            cl += [[-a, bb, c, d], [a, -bb, c, d], [a, bb, -c], [-a, -bb, -c], [a, bb, -d], [-a, -bb, -d]]
    E = lambda j, t: E8[(t + 2 * j + cp) % 8]
    for t in range(T + 1):
        for j in (0, 1):
            cl.append([var(j, t)] if E(j, t) else [-var(j, t)])
    cl.append([(-var(j, s) if E(j, s) else var(j, s)) for j in (-D, -D + 1)])
    return sat_solve(len(v), cl, solver)


def check_windows():
    total = 0
    for s, b in INSTANCES:
        packed, unpacked, nsol = [], [], []
        for cp in range(8):
            pv, pn = check_packed(cp, s, b)
            uv, un = check_unpacked(cp, s, b)
            assert pn == un, "checkers disagree on the number of exact-top assignments"
            assert not check_sat(cp, s, b, 'kissat') and not check_sat(cp, s, b, 'cadical'), "SAT finds a violation"
            packed.append(pv)
            unpacked.append(uv)
            nsol.append(pn)
            total += 1
        assert not any(packed) and not any(unpacked), f"window instance (s={s}, b={b}) FAILS"
        # control: one tick less look-ahead fails for some phase (all three checkers must see it)
        ctrl = [check_packed(cp, s, b - 1)[0] for cp in range(8)]
        ctrl_u = [check_unpacked(cp, s, b - 1)[0] for cp in range(8)]
        ctrl_s = [check_sat(cp, s, b - 1, 'kissat') for cp in range(8)]
        assert ctrl == ctrl_u and [c > 0 for c in ctrl] == ctrl_s and any(ctrl), "control failed"
        print(f"W(s={s}, b={b}): window 0..{s + b}, {2 - min(-2 * (s + b), -6 - 2 * s)} digits; violations 0 in all 8 "
              f"phases (packed, unpacked, kissat, cadical); exact-top assignments per phase {nsol}; "
              f"control b={b - 1}: violations {ctrl}", flush=True)
    print(f"W: all {total} (phase, window) instances hold under four checkers: PASS")
    # sharpness table (documentation): minimal look-ahead per (s, phase)
    print("W: minimal look-ahead b(s, c') for s = 0..6 (packed checker):")
    for cp in range(8):
        row = []
        for s in range(7):
            b = 0
            while check_packed(cp, s, b)[0]:
                b += 1
            row.append(b)
        print(f"   c'={cp}: {row}")


# ---------------------------------------------------------------- B: base cases, exhaustive with PR69's own words
def edge_traces(k, H):
    n = 1 << (k + 1)
    idx = np.arange(n, dtype=np.int64)
    X = np.zeros((k + 2, n), dtype=np.uint8)
    X[0] = 1
    for j in range(1, k + 2):
        X[j] = (idx >> (j - 1)) & 1
    a = np.empty((H, n), dtype=np.uint8)
    bb = np.empty_like(a)
    for t in range(H):
        a[t], bb[t] = X[k], X[k + 1]
        Y = np.empty_like(X)
        Y[0] = 1
        Y[1] = X[1] ^ X[0]
        Y[2:] = X[2:] ^ (X[1:-1] | X[:-2])
        X = Y
    return a, bb


def M_exhaustive(k):
    H = (2 * k) // 3 + 8
    a, bb = edge_traces(k, H)
    best = 0
    for i in range(4):
        for q in range(8):
            alive = np.ones(a.shape[1], dtype=bool)
            run = np.zeros(a.shape[1], dtype=np.int64)
            for t in range(H):
                alive &= (a[t] == ether(i, t + q)) & (bb[t] == ether(i + 1, t + q))
                run += alive
            best = max(best, int(run.max()))
    assert best < H
    return best


def edge_sat(k, L, i, q, solver):
    var = lambda j, t: (j - 1) * L + t + 1
    cl = []
    for t in range(L - 1):
        for j in (1, 2):
            x, y = var(j, t), var(j, t + 1)
            cl += [[x, y], [-x, -y]]
        for j in range(3, k + 2):
            x, y, c, d = var(j, t), var(j, t + 1), var(j - 1, t), var(j - 2, t)
            cl += [[-x, y, c, d], [x, -y, c, d], [x, y, -c], [-x, -y, -c], [x, y, -d], [-x, -y, -d]]
    for t in range(L):
        u, w = var(k + 1, t, ), var(k, t)
        cl += [[w if ether(i, t + q) else -w], [u if ether(i + 1, t + q) else -u]]
    return sat_solve((k + 1) * L, cl, solver)


def Lw(k):
    return -(-(4 * (-(-k // 2)) + 8) // 3)


def check_base():
    table = {k: M_exhaustive(k) for k in range(1, 9)}
    print(f"B: exhaustive M(k), k = 1..8 (all 2^(k+1) prefixes, all 32 phases): {[table[k] for k in range(1, 9)]}")
    for k in range(1, 9):
        assert table[k] == Lw(k), (k, table[k], Lw(k))
    for k in (2, 6, 8):
        m = (2 * k) // 3
        assert table[k] == m + 3
        for solver in ('kissat', 'cadical'):
            assert not any(edge_sat(k, m + 4, i, q, solver) for i in range(4) for q in range(8))
            assert any(edge_sat(k, m + 3, i, q, solver) for i in range(4) for q in range(8))
    print("B: M(k) = L_w(k) for k = 1..8; at k = 2, 6, 8 no episode of length m+4 (exhaustive; kissat and cadical "
          "UNSAT in all 32 phases, m+3 SAT): PASS")


# ---------------------------------------------------------------- I: the arithmetic of the induction
def check_induction(KMAX=100000):
    m = lambda k: (2 * k) // 3
    for k in range(12, KMAX):
        if k % 6 in (0, 2):
            assert m(k) == m(k - 6) + 4 and m(k) + 4 >= 11
    for k in range(9, KMAX):
        assert Lw(k) == Lw(k - 6) + 4 and Lw(k) + 1 >= 11
        assert Lw(k) == m(k) + 4 - (1 if k % 6 in (0, 2) else 0)
    assert all(Lw(k) == m(k) + 4 - (1 if k % 6 in (0, 2) else 0) for k in range(1, 9))
    print(f"I: for 12 <= k < {KMAX}, k = 0,2 mod 6: m(k) = m(k-6)+4 and m(k)+4 >= 11 (the descent applies); "
          f"for 9 <= k: L_w(k) = L_w(k-6)+4, L_w(k)+1 >= 11, L_w = m+4-[k=0,2 mod 6]: PASS")


if __name__ == '__main__':
    me = open(__file__, 'rb').read()
    print(f"ether_six_depth_descent_certificate.py sha256 {hashlib.sha256(me).hexdigest()}")
    check_ground()
    check_windows()
    check_base()
    check_induction()
    os.rmdir(WORK)
    print("CERTIFICATE COMPLETE: no exact ether-pair episode of length floor(2k/3)+4 at any depth k = 0, 2 (mod 6), "
          "any row, any phase; and M(k) <= L_w(k) for all k >= 1.")
