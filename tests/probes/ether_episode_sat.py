#!/usr/bin/env python3
"""ether_episode_sat.py: M(k) and G(k) by SAT, far beyond the exhaustive range (L1259, round 5 of the inquisition).

RUN-ON:     cpu (Python 3 + the kissat and cadical binaries), minutes
COMMAND:    python3 tests/probes/ether_episode_sat.py KMAX [CONTROL_KMAX=40] [WORKERS=6]

Frame and quantifiers as in ether_episode_exact.py: PR69's edge code (kit PR69 head fcffbaa9), X_0 constant black,
X_1(t+1) = NOT X_1(t), X_j(t+1) = X_j(t) XOR (X_(j-1)(t) OR X_(j-2)(t)) for j >= 2 (so X_2 also alternates).
Every onset is an initial prefix, so M(k) >= L iff, for some ether phase (i, q), the CNF "digits 1..k+1 on ticks
0..L-1 obey the recurrence, and X_k(t) = ether(i, t+q), X_(k+1)(t) = ether(i+1, t+q) for t < L" is satisfiable.
The first row is free. G(k) is the same with PR69's `good` predicate at phase p, good(t+p, X_(k+1)(t), X_k(t)), in
place of the exact pair.

The two-party bounds (GC2327, GC2330, CL669/GC2331) give m+3 <= M(k) <= G(k) <= m+4 with m = floor(2k/3), and
M(k) = m+4 for k = 1, 3, 4, 5 (mod 6). The open question is L = m+4 at k = 0, 2 (mod 6). For those k the probe
decides L = m+4 for every exact phase class (16, by the glide ether(i+2, t+4) = ether(i, t)) and every good phase
(8), and checks each UNSAT with a second solver (cadical). Controls, for k <= CONTROL_KMAX:
- L = m+3 SAT, L = m+5 UNSAT (both modes);
- L = m+4 SAT at the other residues;
- all 32 exact phases agree with the 16 classes for k <= 20.
Every SAT model is re-simulated forward from its prefix and must satisfy the top constraint on every tick.
Predictions P-S1..P-S4: reports/inquisition-20261031.md (round 5), committed before this ran.
"""
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 60
CONTROL_KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 40
WORKERS = int(sys.argv[3]) if len(sys.argv) > 3 else 6
WORDS = (43, 202, 178, 172)          # PR69 `ether`: column i mod 4, bit t mod 8
WORK = tempfile.mkdtemp(prefix='ether-sat-', dir=os.environ.get('CAPPED_OUT', os.getcwd()))   # CNFs, deleted after use


def ether(i, t):
    return (WORDS[i % 4] >> (t % 8)) & 1


def good(r, u, v):
    return [(not u) and v, u, (not u) and (not v), u, (not u) and (not v), u != v, u and (not v), u][r % 8]


def var(j, t, L):
    return (j - 1) * L + t + 1        # digit j in 1..k+1, tick t in 0..L-1


def cnf(k, L, mode, phase):
    cl = []
    for t in range(L - 1):
        for j in (1, 2):
            a, b = var(j, t, L), var(j, t + 1, L)
            cl += [[a, b], [-a, -b]]
        for j in range(3, k + 2):
            a, b = var(j, t, L), var(j, t + 1, L)
            c, d = var(j - 1, t, L), var(j - 2, t, L)
            cl += [[-a, b, c, d], [a, -b, c, d], [a, b, -c], [-a, -b, -c], [a, b, -d], [-a, -b, -d]]
    for t in range(L):
        u, v = var(k + 1, t, L), var(k, t, L)
        if mode == 'exact':
            i, q = phase
            cl += [[v if ether(i, t + q) else -v], [u if ether(i + 1, t + q) else -u]]
        else:
            r = (t + phase) % 8
            cl += {0: [[-u], [v]], 1: [[u]], 2: [[-u], [-v]], 3: [[u]], 4: [[-u], [-v]],
                   5: [[u, v], [-u, -v]], 6: [[u], [-v]], 7: [[u]]}[r]
    return (k + 1) * L, cl


def solve(solver, k, L, mode, phase):
    nv, cl = cnf(k, L, mode, phase)
    fd, path = tempfile.mkstemp(suffix='.cnf', dir=WORK)
    with os.fdopen(fd, 'w') as f:
        f.write(f"p cnf {nv} {len(cl)}\n")
        f.write(''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
    try:
        p = subprocess.run([solver, '-q', path], capture_output=True, text=True)
    finally:
        os.remove(path)
    if p.returncode == 20:
        return None
    assert p.returncode == 10, (solver, p.returncode, p.stdout[-200:], p.stderr[-200:])
    lits = [int(x) for line in p.stdout.splitlines() if line.startswith('v') for x in line.split()[1:]]
    val = {abs(x): x > 0 for x in lits if x}
    prefix = [1] + [int(val.get(var(j, 0, L), False)) for j in range(1, k + 2)]
    check_model(k, L, mode, phase, prefix)
    return prefix


def check_model(k, L, mode, phase, X):
    X = list(X)
    for t in range(L):
        u, v = X[k + 1], X[k]
        if mode == 'exact':
            i, q = phase
            assert v == ether(i, t + q) and u == ether(i + 1, t + q), "model fails exact pair"
        else:
            assert good(t + phase, u, v), "model fails good"
        Y = X[:]
        Y[1] = X[1] ^ X[0]
        for j in range(2, k + 2):
            Y[j] = X[j] ^ (X[j - 1] | X[j - 2])
        X = Y


def phases(mode, allphases=False):
    if mode == 'good':
        return list(range(8))
    return [(i, q) for i in range(4 if allphases else 2) for q in range(8)]


def decide(k, L, mode, allphases=False, second=False):
    """SAT iff some phase is satisfiable. Returns (sat, phase or None, n_unsat_rechecked)."""
    ph = phases(mode, allphases)
    with ThreadPoolExecutor(WORKERS) as ex:
        res = list(ex.map(lambda p: (p, solve('kissat', k, L, mode, p)), ph))
    sats = [p for p, r in res if r is not None]
    rechecked = 0
    if second and not sats:
        with ThreadPoolExecutor(WORKERS) as ex:
            res2 = list(ex.map(lambda p: solve('cadical', k, L, mode, p), ph))
        assert all(r is None for r in res2), "kissat UNSAT but cadical SAT"
        rechecked = len(ph)
    if allphases:
        cls = {}
        for p, r in res:
            i, q = p
            cls.setdefault((i % 2, (q + 4 * (i // 2)) % 8), set()).add(r is not None)
        assert all(len(s) == 1 for s in cls.values()), "glide classes disagree"
    return bool(sats), (sats[0] if sats else None), rechecked


def main():
    print(f"KMAX={KMAX} CONTROL_KMAX={CONTROL_KMAX} WORKERS={WORKERS}")
    bad = badg = 0
    for k in range(1, KMAX + 1):
        m = (2 * k) // 3
        even = k % 6 in (0, 2)
        line = [f"k={k:3d} m+4={m + 4:3d}"]
        for mode in ('exact', 'good'):
            open_case = even if mode == 'exact' else (k % 6 in (0, 2))
            out = []
            if open_case or k <= CONTROL_KMAX:
                s4, ph, rc = decide(k, m + 4, mode, allphases=(mode == 'exact' and k <= 20), second=open_case)
                out.append(f"L=m+4 {'SAT' if s4 else 'UNSAT'}" + (f" (cadical {rc} UNSAT)" if rc else "") +
                           (f" at {ph}" if s4 else ""))
                want = (not even) if mode == 'exact' else (k % 6 != 0)
                if s4 != want:
                    if mode == 'exact':
                        bad += 1
                        out.append("<-- AGAINST THE CONJECTURE")
                    else:
                        badg += 1
                        out.append("<-- AGAINST CLOUD'S G(k) PATTERN")
            if k <= CONTROL_KMAX:
                s3, _, _ = decide(k, m + 3, mode)
                s5, _, _ = decide(k, m + 5, mode)
                assert s3 and not s5, f"control failed at k={k} {mode}: m+3 {s3} m+5 {s5}"
                out.append("m+3 SAT, m+5 UNSAT")
            line.append(f"{mode}: " + "; ".join(out))
        print(" | ".join(line), flush=True)
    print(f"cases against the conjecture M(k) = m+4 - [k = 0,2 mod 6]: {bad}")
    print(f"cases against G(k) = m+4 - [k = 0 mod 6]: {badg}")
    os.rmdir(WORK)
    print("ETHER_SAT_DONE")


if __name__ == '__main__':
    main()
