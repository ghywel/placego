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
  6. PROOFS: every UNSAT claimed in 3 and 4 also has a cadical LRAT proof checked by lrat_check() below, a short
     independent checker (unit propagation along the hints; fails on any RAT step, satisfied hint or missing
     conflict, and requires the empty clause). Controls: for EVERY such system the unflipped variant (target unit
     negated, the ether a model) is SAT and its replayed proof is rejected; a proof with a dropped hint and a proof
     for a different CNF are rejected. Every check is an explicit require(), so python3 -O does not remove it
     (L1259 hardening after the code lens; before it the checks were assert statements).
  The end phases hold for every K by algebra (K = 6a: phiR = 16a+10 = 2; K = 6a+2: phiR = 16a+15 = 7; phi0 = 2K+7 is
  7 or 3 for even K; m(K) - 4 = m(K-6)); the code checks them for K < 400. The abstract systems are identical to the
  concrete ones, with the same variable numbering (checked here at ten targets, and by the code lens at all 4,254
  targets with K <= 140).
"""
import itertools
import os
import subprocess
import sys
import tempfile

import numpy as np

E8 = (1, 1, 0, 1, 0, 1, 0, 0)
WORDS = (43, 202, 178, 172)


class CheckFailed(Exception):
    """A certificate check failed. Explicit, so the checks also run under python3 -O (no assert statements)."""


def require(cond, msg=''):
    if not cond:
        raise CheckFailed(msg)
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
    require(p.returncode in (10, 20), (solver, p.returncode))
    return p.returncode == 10


def lrat_proof(nv, cl):
    """cadical's textual LRAT proof of an UNSAT CNF, as a list of lines."""
    fd, path = tempfile.mkstemp(suffix='.cnf', dir=WORK)
    with os.fdopen(fd, 'w') as f:
        f.write(f"p cnf {nv} {len(cl)}\n" + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
    proof = path + '.lrat'
    try:
        p = subprocess.run(['cadical', '-q', '--lrat=true', '--no-binary', path, proof], capture_output=True, text=True)
        require(p.returncode == 20, ('cadical did not report UNSAT', p.returncode))
        with open(proof) as f:
            lines = f.read().split('\n')
    finally:
        os.remove(path)
        if os.path.exists(proof):
            os.remove(proof)
    return [ln for ln in lines if ln.strip()]


def lrat_check(cl, lines):
    """Check an LRAT refutation of the clause list cl (clauses numbered 1..len(cl)). RUP steps only."""
    db = {i + 1: list(c) for i, c in enumerate(cl)}
    empty = False
    for ln in lines:
        tok = [int(x) if x != 'd' else 'd' for x in ln.split()]
        cid = tok[0]
        if tok[1] == 'd':
            for x in tok[2:-1]:
                db.pop(x, None)
            continue
        z = tok.index(0, 1)
        lits, hints = tok[1:z], tok[z + 1:-1]
        require(tok[-1] == 0 and all(h > 0 for h in hints), "RAT step or malformed line")
        val = {}
        for l in lits:
            val[abs(l)] = (l < 0)            # the lemma's literals are made false
        conflict = False
        for h in hints:
            c = db[h]
            und = []
            for l in c:
                v = val.get(abs(l))
                if v is None:
                    und.append(l)
                elif v == (l > 0):
                    raise CheckFailed("hint already satisfied")
            if not und:
                conflict = True
                break
            require(len(und) == 1, "hint not unit")
            val[abs(und[0])] = und[0] > 0
        require(conflict, "no conflict along the hints")
        db[cid] = lits
        if not lits:
            empty = True
            break
    require(empty, "empty clause not derived")
    return True


N_PROOFS = [0]


N_REPLAYS = [0]


def certified_unsat(nv, cl):
    """UNSAT by kissat and cadical, and cadical's LRAT proof checked here. Controls on every call: the same system
    with the target unit (always the last clause) replaced by its negation is satisfiable (the ether is a model), and
    the proof replayed against that satisfiable system is rejected by the checker."""
    if solve('kissat', nv, cl) or solve('cadical', nv, cl):
        return False
    proof = lrat_proof(nv, cl)
    lrat_check(cl, proof)
    N_PROOFS[0] += 1
    sat_variant = cl[:-1] + [[-x for x in cl[-1]]]
    require(len(cl[-1]) == 1 and solve('kissat', nv, sat_variant), "unflipped system not satisfiable")
    try:
        lrat_check(sat_variant, proof)
        accepted = True
    except (CheckFailed, KeyError):
        accepted = False
    require(not accepted, "LRAT checker accepted a proof for a satisfiable system")
    N_REPLAYS[0] += 1
    return True


# ---------------------------------------------------------------- 1. GPT's tree, exact max-plus
D = {0: (0, 1), 1: (0, 1), 2: (0, 1), 3: (-1, 0), 4: (0, 1), 5: (0, 1), 6: (0, 1, 2), 7: (0, 1)}


def tree_check(nmax=300):
    F = [[0] * 8]
    for n in range(1, nmax + 1):
        F.append([max(d + F[n - 1][(h + 2 + d) % 8] for d in D[h]) for h in range(8)])
    n0 = next(n for n in range(1, nmax - 3) if all(F[n + 3][h] == F[n][h] + 2 for h in range(8)))
    require(all(F[n + 3][h] == F[n][h] + 2 for n in range(n0, nmax - 3) for h in range(8)))
    worst = {}
    for k in range(1, nmax + 1):
        if k % 6 not in (0, 2):
            continue
        for r in range(8):
            best = min(((h - r) % 8) + F[k][h] for h in (2, 4, 6))
            need = best - m(k)
            worst[r] = max(worst.get(r, -99), need)
            if r == 7:
                require(need == 4, (k, r, need))
            else:
                require(need <= 3, (k, r, need))
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
    require(best < H)
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
    require(k == c, "solvers disagree")
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
            if not certified_unsat(nv, cl):
                bad.append((jj - K, t))
    return Lp, bad


def main():
    tree_check()

    base = {k: exhaustive_M(k) for k in (2, 6, 8, 12)}
    require(base == {2: 4, 6: 7, 8: 8, 12: 11}, base)
    require(all(base[k] == m(k) + 3 for k in base))
    print(f"BASE: exhaustive M(k) = {base} = m(k) + 3")

    for K in (14, 18, 20, 24, 26, 30):
        Lp, bad = direct_check(K)
        require(not bad, (K, bad))
        print(f"DIRECT: K={K} L'={Lp}: X = E forced at depths K-6, K-5 on ticks 0..{Lp - 5} (kissat and cadical)")

    n_abs = 0
    for phi in range(8):
        for tg in ('K-6', 'K-5'):
            require(certified_unsat(*abstract_csp(phi, W, W, tg)), ('interior', phi, tg))
            n_abs += 1
    for phi0 in (7, 3):
        for t in range(W):
            for tg in ('K-6', 'K-5'):
                require(certified_unsat(*abstract_csp((phi0 + t) % 8, t, W, tg)), ('left', phi0, t, tg))
                n_abs += 1
    for phiR in (2, 7):
        for rho in range(4, W):
            for tg in ('K-6', 'K-5'):
                require(certified_unsat(*abstract_csp((phiR - rho) % 8, W, rho, tg)), ('right', phiR, rho, tg))
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
            require(nv == nv2 and canon(cl) == canon(cl2), ("abstract != concrete", K, jj, t))
    print("CONTROL: abstract CSPs equal the concrete local CSPs at K = 48, 50 (five targets each)")
    for phi in range(8):
        for tg in ('K-6', 'K-5'):
            require(not both_unsat(*abstract_csp(phi, W, W, tg, top=False)), "vacuous check")
    print("CONTROL: without the top constraint every interior target can be violated (checks are not vacuous)")
    for phiR in (2, 7):
        free = [tg for tg in ('K-6', 'K-5') if not both_unsat(*abstract_csp((phiR - 3) % 8, W, 3, tg))]
        require(free, ("one tick past the right end is forced too", phiR))
        print(f"CONTROL: right-end phase {phiR}: at tick L'-4 (one past the claimed end) {free} not forced")
    for K in range(14, 400):
        if K % 6 in (0, 2):
            require(m(K) + 4 - 4 == m(K - 6) + 4)
            Lp = m(K) + 4
            if K >= 32:
                require(Lp >= 2 * W + 5)
            phi0 = (2 * K + 7) % 8
            phiR = (Lp - 1 + 2 * K + 7) % 8
            require(phi0 in (7, 3) and phiR == (2 if K % 6 == 0 else 7))
    print("CONTROL: arithmetic of the step and the end phases checked for K < 400")
    nv, cl = abstract_csp(0, W, W, 'K-6')
    lines = lrat_proof(nv, cl)
    require(lrat_check(cl, lines))
    rejected = 0
    for idx, ln in enumerate(lines):
        tok = ln.split()
        if tok[1] == 'd':
            continue
        z = tok.index('0', 1)
        hints = tok[z + 1:-1]
        if len(hints) < 2:
            continue
        bad = lines[:idx] + [' '.join(tok[:z + 1] + hints[:-1] + ['0'])] + lines[idx + 1:]
        try:
            lrat_check(cl, bad)
        except (CheckFailed, KeyError):
            rejected += 1
            break
    require(rejected == 1, "a corrupted proof was accepted")
    nv2, cl2 = abstract_csp(1, W, W, 'K-6')
    try:
        lrat_check(cl2, lines)
        raise SystemExit("proof accepted for a different CNF")
    except (CheckFailed, KeyError):
        pass
    print(f"CONTROL: the LRAT checker rejects a proof with a dropped hint and a proof for a different CNF")
    print(f"PROOFS: {N_PROOFS[0]} LRAT refutations checked (DIRECT and ABSTRACT); for each, the unflipped system is "
          f"SAT and the proof replayed on it is rejected ({N_REPLAYS[0]} replays)")
    os.rmdir(WORK)
    print("RIGIDITY_CERTIFICATE_PASS")


if __name__ == '__main__':
    main()
