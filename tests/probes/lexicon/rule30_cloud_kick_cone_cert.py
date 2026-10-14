#!/usr/bin/env python3
"""rule30_cloud_kick_cone_cert.py: KC, INSTINCT-CLOUD.md S8. Are 8.105's two local facts at a kick forced?

RUN-ON:     cpu (Python 3; python-sat with CaDiCaL 1.5.3 and Glucose 4; PYTHONPATH may point at a scratch install)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_kick_cone_cert.py [K ...]   (default: 16 56 140)
COST:       to be recorded (expected minutes at K = 140).

Why. 8.105 measured, over 1,138 kicks after at least 56 steps on the wheel:
  F1: four rows before every kick, sites 3..5 read 110 at class 52 and 011 at every other class;
  F2: ten rows before a class-52 kick, sites 6..8 read 110, and sites 9..11 avoid 010, 011 and 110.
Measured is not proved. This probe asks the question exactly, as entries 26 and 27 did for the kick alphabet: over
every right half whatsoever, with column 1 on the wheel U for K steps and departing at the next one.

Setting (as in entries 26 and 27, and the world of rule30_cloud_echo_wall.py). Site 0 is the wall, x_t(0) = t mod 2. A
kick of class a departs at row r: column 1 equals U((a + j) mod 56) at row r - 56 + j for every j < 56 back to row r - K,
and x_r(1) != U(a). Since the phase is even, r = a (mod 2), so the wall at row r - K + t is (a - K + t) mod 2. The
unknowns are row r - K at sites 1 .. K + 1, plus a free column at site K + 2 at every row. That column can stand for
any right half beyond, and it cannot reach column 1 within K rows, nor sites 3..5 by row r - 4, nor sites 6..11 by row
r - 10. Each step is y = left XOR (centre OR right), in Tseitin clauses.

Queries, for each K and each class a = 0 .. 55:
  Q0: is a departure of class a possible after K steps on the wheel?
  Q1: if so, which values of sites 3..5 at row r - 4 are possible? Enumerated by SAT with blocking clauses.
  Q2 (class 52): which values of sites 6..8 and of sites 9..11 at row r - 10 are possible?

PREDICTIONS, written 2026-10-14 before any run and pushed before it.
  C1 (exact control): every real kick of the echo-wall world (seeds 0 .. 3) satisfies the encoding at K = 56, with its
     own trajectory as the assignment.
  C2 (exact control): at K = 16, exhaustive brute force over all 2^17 rows (sites 1..17, the boundary white) gives the
     same possible classes and the same sets of r - 4 patterns as SAT.
  C3 (exact control): CaDiCaL and Glucose agree on every Q0 verdict and every pattern set.
  P1 (0.5): at K = 140, departures are possible at exactly classes 32, 42 and 52.
  P2 (0.65): at K = 140 the r - 4 pattern is forced at each possible class: 110 at 52, 011 at 32 and 42.
  P3 (0.55): at K = 140, class 52 forces 110 at sites 6..8 of row r - 10, and sites 9..11 take only values in
     {111, 101, 100, 000, 001}.
  P4 (0.5): K = 56 already forces P2's patterns at classes 32, 42 and 52.
  U, the unexpected check (0.4): the smallest K at which class 52's r - 4 pattern is forced is at most 24.
  Counterfactual. A possible departure with another r - 4 pattern refutes F1 as a lemma. Its model is a witness to
  record, and it would mean the 1,138 measured kicks were a biased sample of the possible ones.

OUTCOME, 2026-10-14 18:02 BST (predictions pushed in f096977 at 18:00 BST; python-sat with CaDiCaL 1.5.3 and Glucose
4; drat-trim built in scratch from the upstream source; 50 s for K = 56 and 140, 34 s to certify K = 140).
  C1 PASS: 265 real kicks satisfy the encoding at K = 56, with no violated clause.
  C2 PASS: at K = 16, brute force over 2^17 rows gives the same classes and pattern sets as SAT.
  C3 PASS: CaDiCaL and Glucose agree on every class and every pattern set.
  K = 16: not yet forced. Class 52 allows 110 and 111; classes 9, 19, 29, 39 and 49 allow 000, 001 and 011; classes
    2, 12, 22, 32 and 42 force 011.
  U REFUTED by one step: K = 25 is the first horizon at which class 52's r - 4 pattern is forced (110).
  K = 56 (P4 HELD): departures are possible at classes 2, 12, 19, 22, 32, 39, 42, 49 and 52, each with one forced r - 4
    pattern. It is 011 at 2, 12, 22, 32 and 42; 000 at 19, 39 and 49; and 110 at 52. So 8.105's measured "011 at every
    other class" is false after 56 steps: classes 19, 39 and 49 force 000, and none of them was among the 1,138 sampled
    kicks. At class 52, sites 6..8 of row r - 10 are 011 or 110, so they are not yet forced.
  K = 140 (P1, P2 and P3 HELD): departures are possible at exactly classes 32, 42 and 52, forcing 011, 011 and 110 at
    r - 4. Class 52 forces 110 at sites 6..8 of row r - 10, and sites 9..11 there take exactly 000, 001, 100, 101 and
    111.
  CERTIFIED (certify mode; Glucose 4 DRUP proofs, every one VERIFIED by drat-trim).
    - All 56 classes at K = 140 (53 with no departure; 32, 42 and 52 complete), and all 56 at K = 56 (47 with no
      departure; nine complete).
    - Negative control: a proof cut in half fails both times.
    - The class-52 facts at row r - 10, K = 140: sites 6..8 differ from 110, UNSAT, 12,528 proof lines, cnf sha256
      218e9b7ba7c88701...; sites 9..11 outside the five patterns, UNSAT, 25,981 lines, cnf cc099190d87cca16....
    - K = 140 completeness cnfs: class 32 75fa4bf12f83272d..., 42 172f4690dc80c25b..., 52 108eb51819b0bf90....
    - The CNFs are deterministic, so certify mode rebuilds them and regenerates the proofs. The files themselves were
      kept in the session's scratch only.
  A departure after K' >= K steps on the wheel is also one after K steps, so each result covers every longer settling.
"""
import random
import sys

from pysat.solvers import Cadical153, Glucose4

U = '00010011010001001101000100110100010011010001001101001101'


class Cone:
    """CNF for K rows of the clamped half-line, column 1 on the wheel at class a, departing at row K."""

    def __init__(self, K, a):
        self.K, self.a = K, a
        self.n = 0
        self.var = {}
        self.clauses = []
        W = K + 2
        for t in range(K + 1):
            for k in range(1, W + 1):
                self.var[t, k] = self.new()
        for t in range(K):
            wall = (a - K + t) % 2
            for k in range(1, W):
                y, b, c = self.var[t + 1, k], self.var[t, k], self.var[t, k + 1]
                o = self.new()
                self.clauses += [[-o, b, c], [o, -b], [o, -c]]
                if k == 1:
                    self.clauses += [[-y, o], [y, -o]] if wall == 0 else [[y, o], [-y, -o]]
                else:
                    l = self.var[t, k - 1]
                    self.clauses += [[-y, l, o], [-y, -l, -o], [y, -l, o], [y, l, -o]]
        for t in range(K):
            bit = int(U[(a + 56 - K + t) % 56])
            self.clauses.append([self.var[t, 1] if bit else -self.var[t, 1]])
        bit = int(U[a])
        self.clauses.append([-self.var[K, 1] if bit else self.var[K, 1]])

    def new(self):
        self.n += 1
        return self.n

    def cells(self, t, ks):
        return [self.var[t, k] for k in ks]


def patterns(solver_cls, cone, t, ks, limit=64):
    """Every value of the given cells at row t over all models, by SAT with blocking clauses."""
    found = []
    with solver_cls(bootstrap_with=cone.clauses) as s:
        while len(found) < limit and s.solve():
            m = set(x for x in s.get_model() if x > 0)
            vals = tuple(int(v in m) for v in cone.cells(t, ks))
            found.append(vals)
            s.add_clause([-v if b else v for v, b in zip(cone.cells(t, ks), vals)])
    return sorted(found)


def fmt(ps):
    return [''.join(map(str, p)) for p in ps]


def brute(K):
    """Exhaustive at small K: every row of sites 1..K+1 (bit k = site k), boundary white."""
    out = {}
    for a in range(56):
        res = set()
        for bits in range(1 << (K + 1)):
            row = bits << 1
            ok = True
            hist = []
            for t in range(K + 1):
                row = (row & ~1) | ((a - K + t) % 2)
                hist.append(row)
                if t < K and ((row >> 1) & 1) != int(U[(a + 56 - K + t) % 56]):
                    ok = False
                    break
                row = ((row << 1) ^ (row | (row >> 1))) & ((1 << (K + 3)) - 1)
            if ok and ((hist[K] >> 1) & 1) != int(U[a]):
                h = hist[K - 4]
                res.add(((h >> 3) & 1, (h >> 4) & 1, (h >> 5) & 1))
        if res:
            out[a] = sorted(res)
    return out


def real_kicks_check(K, seeds=4, N=3072, LO=1024):
    """C1: the real trajectory of each kick satisfies the encoding."""
    ROT = {sum(int(U[(p + j) % 56]) << j for j in range(56)): p for p in range(56)}
    bad = total = 0
    for seed in range(seeds):
        rnd = random.Random(9100 + seed)
        row = rnd.getrandbits(2 * N + 64) << 1
        states, col1 = [], []
        for t in range(N):
            row = (row & ~1) | (t % 2)
            states.append(row)
            col1.append((row >> 1) & 1)
            row = (row << 1) ^ (row | (row >> 1))
        win = sum(col1[j] << j for j in range(56))
        ph = [ROT.get(win)]
        for t in range(1, N - 55):
            win = (win >> 1) | (col1[t + 55] << 55)
            ph.append(ROT.get(win))
        cones = {}
        for r in range(LO, N):
            if ph[r - 56] is None or ph[r - 55] is not None:
                continue
            a = ph[r - 56]
            if any(ph[r - 56 - i] != (a - i) % 56 for i in range(K - 56 + 1)):
                continue
            total += 1
            cone = cones.setdefault(a, Cone(K, a))
            assign = {}
            for (t, k), v in cone.var.items():
                assign[v] = (states[r - K + t] >> k) & 1
            for cl in cone.clauses:
                if all(abs(l) in assign for l in cl) and not any((assign[abs(l)] == 1) == (l > 0) for l in cl):
                    bad += 1
                    break
    return total, bad


def certify(K, outdir, drat_trim):
    """Post hoc (added after the predictions, before any certify run): DRUP proofs for every UNSAT claim at K.
    For each class: if no departure is possible, the cone itself is UNSAT. Otherwise the cone plus blocking clauses for
    every pattern SAT found at r - 4 (sites 3..5) is UNSAT, which proves that set complete. Glucose 4 writes the proof
    and drat-trim checks it. Negative control: the first proof with its last half cut off must fail."""
    import hashlib, os, subprocess
    os.makedirs(outdir, exist_ok=True)
    verified = failed = 0
    neg_done = False
    for a in range(56):
        cone = Cone(K, a)
        found = patterns(Cadical153, cone, K - 4, (3, 4, 5))
        clauses = cone.clauses + [[-v if b else v for v, b in zip(cone.cells(K - 4, (3, 4, 5)), p)] for p in found]
        with Glucose4(bootstrap_with=clauses, with_proof=True) as g:
            assert not g.solve()
            proof = g.get_proof() or []
        cnf = os.path.join(outdir, 'k%d_c%02d.cnf' % (K, a))
        prf = cnf[:-4] + '.drup'
        with open(cnf, 'w') as f:
            f.write('p cnf %d %d\n' % (cone.n, len(clauses)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in clauses))
        with open(prf, 'w') as f:
            f.write('\n'.join(proof) + '\n')
        out = subprocess.run([drat_trim, cnf, prf], capture_output=True, text=True).stdout
        ok = '\ns VERIFIED' in '\n' + out
        verified += ok
        failed += not ok
        digest = hashlib.sha256(open(cnf, 'rb').read()).hexdigest()[:16]
        print('  class %2d: %s, patterns %s, cnf %s, proof lines %d: %s'
              % (a, 'departure possible' if found else 'no departure', fmt(found), digest, len(proof),
                 'VERIFIED' if ok else 'NOT VERIFIED'))
        if not neg_done and len(proof) > 10:
            bad = prf + '.cut'
            with open(bad, 'w') as f:
                f.write('\n'.join(proof[:len(proof) // 2]) + '\n')
            out = subprocess.run([drat_trim, cnf, bad], capture_output=True, text=True).stdout
            print('  negative control (half proof, class %d): %s' % (a, 'FAILS as it should' if '\ns VERIFIED' not in '\n' + out else 'VERIFIED (control broken)'))
            neg_done = True
    print('certify K = %d: %d verified, %d not verified' % (K, verified, failed))


def main():
    if sys.argv[1:2] == ['certify']:
        certify(int(sys.argv[2]), sys.argv[3], sys.argv[4])
        return
    Ks = [int(x) for x in sys.argv[1:]] or [16, 56, 140]
    total, bad = real_kicks_check(56)
    print('C1: real kicks checked at K = 56: %d, violating the encoding: %d' % (total, bad))
    for K in Ks:
        print('\nK = %d' % K)
        res = {}
        for a in range(56):
            cone = Cone(K, a)
            pc = patterns(Cadical153, cone, K - 4, (3, 4, 5))
            if not pc:
                continue
            pg = patterns(Glucose4, cone, K - 4, (3, 4, 5))
            res[a] = pc
            print('  class %2d: r-4 sites 3..5 possible: %s%s' % (a, fmt(pc), '' if pc == pg else '  (C3 MISMATCH: %s)' % fmt(pg)))
            if a == 52:
                p68 = patterns(Cadical153, cone, K - 10, (6, 7, 8))
                p911 = patterns(Cadical153, cone, K - 10, (9, 10, 11))
                print('            r-10 sites 6..8: %s; sites 9..11: %s' % (fmt(p68), fmt(p911)))
        print('  possible classes: %s' % sorted(res))
        if K <= 18:
            b = brute(K)
            print('  C2 brute force agrees with SAT: %s' % (b == res))


if __name__ == '__main__':
    main()
