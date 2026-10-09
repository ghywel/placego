#!/usr/bin/env python3
"""rule30_critical_bridge_sat.py: CX, is there a non-ring critical all-L row with a bounded bridge and a periodic tail?
(The bounded form of the critical-uniqueness question left open by GPT's GC731, GC747, GC758 to GC760 and GC769.)
Local's run (chat L403), claimed in CLOUD-LOCAL.md with these predictions pushed before it.

RUN-ON:     cpu (Python 3 and kissat); minutes
COMMAND:    python3 tests/probes/lexicon/rule30_critical_bridge_sat.py

Write G = shift-left F, G(x)(i) = x(i) xor (x(i+1) or x(i+2)). A critical all-L row with period p satisfies G^p(x) = x, and
its column profiles V_i(t) = G^t(x)(i), t mod p, obey V_i(t+1) xor V_i(t) = V_(i+1)(t) or V_(i+2)(t) (GC759). Every actual
critical all-L candidate is left-asymptotic to the 155-ring R (GC726, GC731) with 310 | p (GC747), and GC759 replaces any
infinite right side by an eventually spatially periodic one. The bounded question asked here, at p = 310: columns -1 and 0
are R's G-profiles; columns 1 .. W are free (the bridge); columns W+1 .. W+P are free and repeat with spatial period P
(the tail), optionally with every tail column 155-periodic (GC769's q = 155 background). Each column's equation is encoded
exactly (8 clauses per cell over the four cells it reads). With P < 155 a solution cannot be R itself, and by GC750 and
GC751 it cannot be a finite-defect copy of R at p = 310, so any SAT answer is a genuinely new critical row with an
infinite right defect. Every SAT model would be checked by evolving its columns literally.

PREDICTIONS (Local's, published before the run):
  CX-C1 (control): with the tail fixed to R's own columns (sites W+1, W+2 given), the instance is SAT, and the bridge it
        returns satisfies every column equation.
  CX-C2 (control): GC732's interface at p = 2 (left columns: the checkerboard's G-profiles, tail white, P = 1) is SAT.
  CX-P1 (blind, confidence 0.7): at p = 310 with 155-periodic tail columns, every W in {0, 4, 8, 16, 24} and P in
        {1, 2, 3, 4, 5, 6, 8, 10} is UNSAT.
  CX-P2 (blind, confidence 0.6): the same with unrestricted (310-periodic) tail columns is UNSAT.
  CX-D1 (descriptive): the table of verdicts and solve times.
Counterfactual: any SAT at p = 310 is an explicit non-ring critical all-L row, which would answer the uniqueness question
negatively in this bounded class. UNSAT answers are bounded evidence only (finite W and P).
Smoke before the push, controls only: C1 SAT with a checked bridge, C2 SAT with a checked model. The first C2 draft used a
cyclic checkerboard's profiles, which are not GC732's interface; it now evolves the actual interface row on a window.
EXTENSION CXE (registered 2026-10-09 after GPT's GC772 audit, before its run; COMMAND: ... rule30_critical_bridge_sat.py ext):
  the tail periods the registered list skipped, P = 7 and P = 9, for W in {0, 4, 8, 16, 24}, q155 and unrestricted, with
  hardened gates: a SAT counts only after the decoded diagram passes every column equation and (for q155) every tail
  column's 155-repeat, and its profiles are saved to OUTDIR/cxe-models.json; UNKNOWN is reported as such, never as
  REFUTED; every UNSAT is re-solved with a DRAT proof and checked by drat-trim; a failing control aborts the run.
  CXE-P1 (blind, confidence 0.75): all 20 instances are UNSAT with verified proofs.
OUTCOME: not yet run.
"""
import itertools
import os
import subprocess
import sys
import time

RING = 0x35409b1caa645d715104db5291a2fe8415260ce
N = 155


def g_profiles(row, sites, p):
    """V_i(t) = G^t(row)(i) for t in 0 .. p-1, on a cyclic row"""
    n = len(row)
    x = list(row)
    prof = {i: [] for i in sites}
    for t in range(p):
        for i in sites:
            prof[i].append(x[i % n])
        f = [x[(j - 1) % n] ^ (x[j] | x[(j + 1) % n]) for j in range(n)]
        x = [f[(j + 1) % n] for j in range(n)]
    assert x == list(row), 'not G-periodic with this p'
    return prof


class CNF:
    def __init__(self):
        self.n = 0
        self.cl = []

    def var(self):
        self.n += 1
        return self.n

    def add(self, lits):
        self.cl.append(lits)

    def text(self):
        return 'p cnf %d %d\n' % (self.n, len(self.cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in self.cl)


def eq_clauses(cnf, a, a1, b, c):
    """a xor a1 = b or c; each argument a literal (int) or a constant (bool)"""
    for va, va1, vb, vc in itertools.product((0, 1), repeat=4):
        if (va ^ va1) == (vb | vc):
            continue
        clause, sat = [], False
        for lit, val in ((a, va), (a1, va1), (b, vb), (c, vc)):
            if isinstance(lit, bool):
                if lit != bool(val):
                    sat = True
                    break
            else:
                clause.append(-lit if val else lit)
        if not sat:
            cnf.add(clause)


def build(p, left, W, P, q_tail=None, tail_given=None):
    """left: profiles of columns -1 and 0; free columns 1 .. W (+ tail W+1 .. W+P, periodic) or given tail columns"""
    cnf = CNF()
    col = {-1: [bool(v) for v in left[-1]], 0: [bool(v) for v in left[0]]}
    for i in range(1, W + 1):
        col[i] = [cnf.var() for _ in range(p)]
    if tail_given is not None:
        col[W + 1] = [bool(v) for v in tail_given[0]]
        col[W + 2] = [bool(v) for v in tail_given[1]]
        last = W                                     # equations for columns -1 .. W
    else:
        for j in range(P):
            col[W + 1 + j] = [cnf.var() for _ in range(p)]
        col[W + 1 + P] = col[W + 1]
        col[W + 2 + P] = col[W + 2] if P >= 2 else col[W + 1]
        if P == 1:
            col[W + 2] = col[W + 1]
        last = W + P
        if q_tail:
            for j in range(P):
                for t in range(p - q_tail):
                    a, b = col[W + 1 + j][t], col[W + 1 + j][t + q_tail]
                    cnf.add([-a, b]); cnf.add([a, -b])
    for i in range(-1, last + 1):
        for t in range(p):
            eq_clauses(cnf, col[i][t], col[i][(t + 1) % p], col[i + 1][t], col[i + 2][t])
    return cnf, col


def solve(cnf, cap=1800):
    t0 = time.time()
    r = subprocess.run(['kissat', '-q', '--time=%d' % cap], input=cnf.text(), capture_output=True, text=True)
    verdict = {10: 'SAT', 20: 'UNSAT'}.get(r.returncode, 'UNKNOWN')
    model = set()
    if verdict == 'SAT':
        for line in r.stdout.splitlines():
            if line.startswith('v '):
                model.update(int(x) for x in line[2:].split() if int(x) > 0)
    return verdict, time.time() - t0, model


def value(lit, model):
    return lit if isinstance(lit, bool) else (lit in model)


def check(col, last, p, model):
    return all((value(col[i][(t + 1) % p], model) ^ value(col[i][t], model)) ==
               (value(col[i + 1][t], model) | value(col[i + 2][t], model))
               for i in range(-1, last + 1) for t in range(p))


def main():
    p = 310
    R = [(RING >> i) & 1 for i in range(N)]
    prof = g_profiles(R, range(-1, 40), p)
    left = {-1: prof[-1], 0: prof[0]}
    # CX-C1: tail fixed to R's own columns W+1, W+2: SAT (R itself)
    W = 6
    cnf, col = build(p, left, W, 0, tail_given=(prof[W + 1], prof[W + 2]))
    v, dt, m = solve(cnf)
    c1 = v == 'SAT' and check(col, W, p, m)
    print('CX-C1', 'PASS' if c1 else 'FAIL', '(%s, %.1f s)' % (v, dt), flush=True)
    # CX-C2: GC732 at p = 2: checkerboard (black at even sites) on the left, white tail
    def gx(x):                                          # G on a dict row, white beyond its keys (G reads rightwards)
        return {i: x.get(i, 0) ^ (x.get(i + 1, 0) | x.get(i + 2, 0)) for i in x}
    x0 = {i: (1 if i <= 0 and i % 2 == 0 else 0) for i in range(-12, 12)}
    x1 = gx(x0)
    assert {i: v for i, v in gx(x1).items() if -8 <= i <= 6} == {i: v for i, v in x0.items() if -8 <= i <= 6}, 'G^2 != id'
    cnf2, col2 = build(2, {-1: [x0[-1], x1[-1]], 0: [x0[0], x1[0]]}, 3, 1)
    v2, dt2, m2 = solve(cnf2)
    print('CX-C2', 'PASS' if v2 == 'SAT' and check(col2, 3 + 1, 2, m2) else 'FAIL', '(%s, %.1f s)' % (v2, dt2), flush=True)
    results = {}
    for q_tail, tag in ((155, 'q155'), (None, 'q310')):
        for W in (0, 4, 8, 16, 24):
            for P in (1, 2, 3, 4, 5, 6, 8, 10):
                cnf, col = build(p, left, W, P, q_tail=q_tail)
                v, dt, m = solve(cnf)
                ok = (v != 'SAT') or check(col, W + P, p, m)
                results[(tag, W, P)] = v
                print('%s W=%2d P=%2d: %-7s %6.1f s%s' % (tag, W, P, v, dt, '' if ok else '  MODEL FAILS CHECK'), flush=True)
    p1 = all(results[('q155', W, P)] == 'UNSAT' for (t, W, P) in results if t == 'q155')
    p2 = all(results[('q310', W, P)] == 'UNSAT' for (t, W, P) in results if t == 'q310')
    print('CX-P1', 'HELD' if p1 else 'REFUTED')
    print('CX-P2', 'HELD' if p2 else 'REFUTED')
    print('COMPLETE')


def ext():
    """CXE: P = 7 and 9 with hardened verdict gates (GC772)"""
    import json
    out = os.path.expanduser(os.environ.get('OUTDIR', '~/np-scratch-int/rule30-al/cxe'))
    os.makedirs(out, exist_ok=True)
    p = 310
    R = [(RING >> i) & 1 for i in range(N)]
    prof = g_profiles(R, range(-1, 12), p)
    left = {-1: prof[-1], 0: prof[0]}
    cnf, col = build(p, left, 6, 0, tail_given=(prof[7], prof[8]))
    v, dt, m = solve(cnf)
    if not (v == 'SAT' and check(col, 6, p, m)):
        print('CXE control FAIL (%s): aborting' % v); sys.exit(1)
    print('CXE control PASS (the ring recovered)', flush=True)
    verdicts, models = {}, {}
    for q_tail, tag in ((155, 'q155'), (None, 'q310')):
        for W in (0, 4, 8, 16, 24):
            for P in (7, 9):
                cnf, col = build(p, left, W, P, q_tail=q_tail)
                v, dt, m = solve(cnf)
                key = '%s W=%d P=%d' % (tag, W, P)
                if v == 'SAT':
                    last = W + P
                    good = check(col, last, p, m)
                    if q_tail:
                        good &= all(value(col[W + 1 + j][t], m) == value(col[W + 1 + j][t + q_tail], m)
                                    for j in range(P) for t in range(p - q_tail))
                    if good:
                        models[key] = {str(i): ''.join('1' if value(col[i][t], m) else '0' for t in range(p))
                                       for i in range(1, last + 1)}
                    v = 'SAT-CHECKED' if good else 'SAT-FAILED-CHECK'
                elif v == 'UNSAT':
                    f = os.path.join(out, key.replace(' ', '_').replace('=', ''))
                    with open(f + '.cnf', 'w') as fh:
                        fh.write(cnf.text())
                    subprocess.run(['kissat', '-q', '-f', '--no-binary', f + '.cnf', f + '.drat'], capture_output=True)
                    chk = subprocess.run(['drat-trim', f + '.cnf', f + '.drat'], capture_output=True, text=True)
                    v = 'UNSAT-VERIFIED' if any(l.strip() == 's VERIFIED' for l in chk.stdout.splitlines()) else 'UNSAT-UNVERIFIED'
                verdicts[key] = v
                print('%-16s %s (%.1f s)' % (key, v, dt), flush=True)
    with open(os.path.join(out, 'cxe-models.json'), 'w') as fh:
        json.dump(models, fh)
    if any(x.startswith('SAT-CHECKED') for x in verdicts.values()):
        print('CXE-P1 REFUTED: a checked non-ring critical diagram exists (profiles saved)')
    elif all(x == 'UNSAT-VERIFIED' for x in verdicts.values()):
        print('CXE-P1 HELD')
    else:
        print('CXE-P1 UNDECIDED (some verdicts neither verified UNSAT nor checked SAT)')
    print('COMPLETE')


if __name__ == '__main__':
    ext() if sys.argv[1:2] == ['ext'] else main()
