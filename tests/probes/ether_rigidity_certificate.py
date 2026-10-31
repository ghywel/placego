#!/usr/bin/env python3
"""ether_rigidity_certificate.py: the finite checks behind M(k) = floor(2k/3) + 3 for every k = 0, 2 (mod 6) (L1259).

RUN-ON:     cpu (Python 3 + numpy + the kissat and cadical binaries), minutes
COMMAND:    python3 tests/probes/ether_rigidity_certificate.py

Frame: PR69's edge code (kit PR69 head fcffbaa9), X_0 = 1, X_1(t+1) = NOT X_1(t), and for j >= 2
X_j(t+1) = X_j(t) XOR (X_(j-1)(t) OR X_(j-2)(t)). The ether in the edge frame is E_j(t) = e(t + 2j + r) with
e = bits of 43 = (1,1,0,1,0,1,0,0); r is the phase at depth 0, tick 0 (the "edge phase" of GC2327). m(k) = floor(2k/3).
An episode of length L at depth k is X_k = E_k, X_(k+1) = E_(k+1) on ticks 0..L-1.

The argument these checks support (reports/inquisition-20261031.md, round 5):
  (T) GPT's tree (GC2327): for k = 0, 2 (mod 6), an episode of length m(k)+4 is impossible unless r = 7.
  (R) Rigidity: for K = 0, 2 (mod 6), K >= 14 and r = 7, every row with an episode of length L' = m(K)+4 at depth K
      also has X = E at depths K-6 and K-5 on ticks 0..L'-5. The same row then has an episode of length
      L'-4 = m(K-6)+4 at depth K-6.
  (B) Base: M(2) = 4, M(6) = 7, M(8) = 8, M(12) = 11 (exhaustive).
  So by induction in steps of 6, M(k) <= m(k)+3 for every k = 0, 2 (mod 6). The witness (CL669/GC2331) gives the
  matching lower bound.
Checks:
  1. TREE: the exact max-plus recursion of GC2327's dependency table, per prospective edge phase r and residue,
     with its eventual period. It gives delay + offset <= m+3 for every r != 7 and = m+4 for r = 7.
  2. BASE: exhaustive M(k) for k = 2, 6, 8, 12 over all prefixes and all 32 phases.
  3. DIRECT: (R) at K = 14, 18, 20, 24, 26, 30 with the full window. The region is depths K-14..K+1 and no edge;
     each target is checked UNSAT by kissat and cadical.
  4. ABSTRACT: (R) for every K >= 32 in the two residues. The local CSP of a target cell (depth K-6 or K-5, tick t,
     window t-10..t+10 clipped to 0..L'-1, depths K-14..K+1) is determined by the target's phase phi = t+2K+7 mod 8,
     its clip lengths and its depth. Interior: 8 phases x 2 depths. Left end: phases at tick 0 in {7, 3} x t = 0..9
     x 2 depths. Right end: phases at tick L'-1 in {2 (K = 0 mod 6), 7 (K = 2 mod 6)} x rho = L'-1-t = 4..9
     x 2 depths. For L' >= 25 (K >= 32) no window is clipped on both sides. All are run with two solvers.
  5. CONTROLS: an abstract CSP equals the concrete one at K = 48 and 50 (same clauses up to renaming); dropping the
     top constraint makes each target satisfiable (the checks are not vacuous); the induction's arithmetic
     m(K)+4-4 = m(K-6)+4 is checked.
"""
import itertools
import os
import subprocess
import sys
import tempfile

import numpy as np

E8 = (1, 1, 0, 1, 0, 1, 0, 0)
WORDS = (43, 202, 178, 172)
W, B = 10, 8
WORK = tempfile.mkdtemp(prefix='rigcert-', dir=os.environ.get('CAPPED_OUT', os.getcwd()))


def m(k):
    return (2 * k) // 3


def solve(solver, nv, cl):
    fd, path = tempfile.mkstemp(suffix='.cnf', dir=WORK)
    with os.fdopen(fd, 'w') as f:
        f.write(f"p cnf {nv} {len(cl)}\n" + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
    try:
        p = subprocess.run([solver, '-q', '-n', path], capture_output=True, text=True)
    finally:
        os.remove(path)
    assert p.returncode in (10, 20), (solver, p.returncode)
    return p.returncode == 10


# ---------------------------------------------------------------- 1. GPT's tree, exact max-plus
D = {0: (0, 1), 1: (0, 1), 2: (0, 1), 3: (-1, 0), 4: (0, 1), 5: (0, 1), 6: (0, 1, 2), 7: (0, 1)}


def tree_check(nmax=300):
    F = [[0] * 8]
    for n in range(1, nmax + 1):
        F.append([max(d + F[n - 1][(h + 2 + d) % 8] for d in D[h]) for h in range(8)])
    n0 = next(n for n in range(1, nmax - 3) if all(F[n + 3][h] == F[n][h] + 2 for h in range(8)))
    assert all(F[n + 3][h] == F[n][h] + 2 for n in range(n0, nmax - 3) for h in range(8))
    worst = {}
    for k in range(1, nmax + 1):
        if k % 6 not in (0, 2):
            continue
        for r in range(8):
            best = min(((h - r) % 8) + F[k][h] for h in (2, 4, 6))
            need = best - m(k)
            worst[r] = max(worst.get(r, -99), need)
            if r == 7:
                assert need == 4, (k, r, need)
            else:
                assert need <= 3, (k, r, need)
    print(f"TREE: F(h, n+3) = F(h, n) + 2 for all h from n0 = {n0} (so for all larger n by the recursion);"
          f" for k = 0, 2 mod 6 up to {nmax}, delay + max offset - m(k) by edge phase r: "
          f"{dict(sorted(worst.items()))}  -> r != 7 fits in m+4 ticks, r = 7 needs m+5")
    return n0


# ---------------------------------------------------------------- 2. base cases, exhaustive
def ether(i, t):
    return (WORDS[i % 4] >> (t % 8)) & 1


def exhaustive_M(k):
    H = m(k) + 6
    n = 1 << (k + 1)
    r_ = np.arange(n, dtype=np.int64)
    X = np.zeros((k + 2, n), dtype=np.uint8)
    X[0] = 1
    for j in range(1, k + 2):
        X[j] = (r_ >> (j - 1)) & 1
    a = np.empty((H, n), dtype=np.uint8)
    b = np.empty_like(a)
    for t in range(H):
        a[t], b[t] = X[k], X[k + 1]
        Y = X.copy()
        Y[1] = X[1] ^ X[0]
        Y[2:] = X[2:] ^ (X[1:-1] | X[:-2])
        X = Y
    best = 0
    for i in range(4):
        for q in range(8):
            alive = np.ones(n, dtype=bool)
            run = np.zeros(n, dtype=np.int64)
            for t in range(H):
                alive &= (a[t] == ether(i, t + q)) & (b[t] == ether(i + 1, t + q))
                run += alive
            best = max(best, int(run.max()))
    assert best < H
    return best


# ---------------------------------------------------------------- 3/4. rigidity CSPs
def rec(var, j, s):
    a, b, c, d = var(j, s), var(j, s + 1), var(j - 1, s), var(j - 2, s)
    return [[-a, b, c, d], [a, -b, c, d], [a, b, -c], [-a, -b, -c], [a, b, -d], [-a, -b, -d]]


def abstract_csp(phi, lo, hi, target, top=True):
    """Relative coordinates: depths 0..B+7 (top pair at B+6, B+7; targets at B (= K-6) or B+1 (= K-5)), ticks
    -lo..hi around the target tick 0. The ether value at relative (jr, s) is e(phi + s + 2(jr - (B+6)))."""
    T = lo + hi + 1
    var = lambda jr, s: jr * T + (s + lo) + 1
    val = lambda jr, s: E8[(phi + s + 2 * (jr - (B + 6))) % 8]
    cl = []
    for s in range(-lo, hi):
        for jr in range(2, B + 8):
            cl += rec(var, jr, s)
    if top:
        for s in range(-lo, hi + 1):
            for jr in (B + 6, B + 7):
                cl.append([var(jr, s) if val(jr, s) else -var(jr, s)])
    jt = B if target == 'K-6' else B + 1
    cl.append([-var(jt, 0)] if val(jt, 0) else [var(jt, 0)])
    return (B + 8) * T, cl


def concrete_csp(K, Lp, jj, t, top=True):
    j0 = K - 6 - B
    t0, t1 = max(0, t - W), min(Lp - 1, t + W)
    T = t1 - t0 + 1
    var = lambda j, s: (j - j0) * T + (s - t0) + 1
    val = lambda j, s: E8[(s + 2 * j + 7) % 8]
    cl = []
    for s in range(t0, t1):
        for j in range(j0 + 2, K + 2):
            cl += rec(var, j, s)
    if top:
        for s in range(t0, t1 + 1):
            for j in (K, K + 1):
                cl.append([var(j, s) if val(j, s) else -var(j, s)])
    cl.append([-var(jj, t)] if val(jj, t) else [var(jj, t)])
    return (K + 2 - j0) * T, cl, (t - t0, t1 - t)


def both_unsat(nv, cl):
    k, c = solve('kissat', nv, cl), solve('cadical', nv, cl)
    assert k == c, "solvers disagree"
    return not k


def direct_check(K):
    Lp = m(K) + 4
    j0 = K - 6 - B
    var = lambda j, s: (j - j0) * Lp + s + 1
    val = lambda j, s: E8[(s + 2 * j + 7) % 8]
    base = []
    for s in range(Lp - 1):
        for j in range(j0 + 2, K + 2):
            base += rec(var, j, s)
    for s in range(Lp):
        for j in (K, K + 1):
            base.append([var(j, s) if val(j, s) else -var(j, s)])
    nv = (K + 2 - j0) * Lp
    bad = []
    for jj in (K - 6, K - 5):
        for t in range(Lp - 4):
            cl = base + [[-var(jj, t)] if val(jj, t) else [var(jj, t)]]
            if not both_unsat(nv, cl):
                bad.append((jj - K, t))
    return Lp, bad


def main():
    tree_check()

    base = {k: exhaustive_M(k) for k in (2, 6, 8, 12)}
    assert base == {2: 4, 6: 7, 8: 8, 12: 11}, base
    assert all(base[k] == m(k) + 3 for k in base)
    print(f"BASE: exhaustive M(k) = {base} = m(k) + 3")

    for K in (14, 18, 20, 24, 26, 30):
        Lp, bad = direct_check(K)
        assert not bad, (K, bad)
        print(f"DIRECT: K={K} L'={Lp}: X = E forced at depths K-6, K-5 on ticks 0..{Lp - 5} (kissat and cadical)")

    n_abs = 0
    for phi in range(8):
        for tg in ('K-6', 'K-5'):
            assert both_unsat(*abstract_csp(phi, W, W, tg)), ('interior', phi, tg)
            n_abs += 1
    for phi0 in (7, 3):
        for t in range(W):
            for tg in ('K-6', 'K-5'):
                assert both_unsat(*abstract_csp((phi0 + t) % 8, t, W, tg)), ('left', phi0, t, tg)
                n_abs += 1
    for phiR in (2, 7):
        for rho in range(4, W):
            for tg in ('K-6', 'K-5'):
                assert both_unsat(*abstract_csp((phiR - rho) % 8, W, rho, tg)), ('right', phiR, rho, tg)
                n_abs += 1
    print(f"ABSTRACT: {n_abs} local CSPs UNSAT under both solvers (interior 16, left end 40, right end 24)")

    # controls
    for K in (48, 50):
        Lp = m(K) + 4
        for jj, t in ((K - 6, 0), (K - 5, 3), (K - 6, 17), (K - 5, Lp - 5), (K - 6, Lp - 7)):
            nv, cl, (lo, hi) = concrete_csp(K, Lp, jj, t)
            phi = (t + 2 * K + 7) % 8
            nv2, cl2 = abstract_csp(phi, lo, hi, 'K-6' if jj == K - 6 else 'K-5')
            canon = lambda c: sorted(tuple(sorted(x)) for x in c)
            assert nv == nv2 and canon(cl) == canon(cl2), ("abstract != concrete", K, jj, t)
    print("CONTROL: abstract CSPs equal the concrete local CSPs at K = 48, 50 (five targets each)")
    for phi in range(8):
        for tg in ('K-6', 'K-5'):
            assert not both_unsat(*abstract_csp(phi, W, W, tg, top=False)), "vacuous check"
    print("CONTROL: without the top constraint every interior target can be violated (checks are not vacuous)")
    for phiR in (2, 7):
        free = [tg for tg in ('K-6', 'K-5') if not both_unsat(*abstract_csp((phiR - 3) % 8, W, 3, tg))]
        assert free, ("one tick past the right end is forced too", phiR)
        print(f"CONTROL: right-end phase {phiR}: at tick L'-4 (one past the claimed end) {free} not forced")
    for K in range(14, 400):
        if K % 6 in (0, 2):
            assert m(K) + 4 - 4 == m(K - 6) + 4
            Lp = m(K) + 4
            if K >= 32:
                assert Lp >= 2 * W + 5
            phi0 = (2 * K + 7) % 8
            phiR = (Lp - 1 + 2 * K + 7) % 8
            assert phi0 in (7, 3) and phiR == (2 if K % 6 == 0 else 7)
    print("CONTROL: arithmetic of the step and the end phases checked for K < 400")
    os.rmdir(WORK)
    print("RIGIDITY_CERTIFICATE_PASS")


if __name__ == '__main__':
    main()
