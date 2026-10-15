#!/usr/bin/env python3
"""erdos_k2prime_barrier.py: the Erdős automaton barrier, K2' (RULE30-PRIZE.md 8.113; SW-01's wounded proposals 5 and
7, which both judges overruled in scope and named as the next block; GPT's conventions GC1257; split L731/GC1257:
Local the SAT search with verified certificates, GPT the source read and the hand attempt).

K2' (open). Every 3-recognisable set L of positive integers that is closed under x -> 4x and holds a number whose
lowest nonzero ternary digit is 1 meets C* = {x >= 1 : every ternary digit of x is 0 or 1}.

Why it matters. For n > 8 Erdős says 2^n is not in C*. Odd n are free (2^n = 2 mod 3 ends in the digit 2), so Erdős is
4^m not in C* for m >= 5, and 4^5 = 1024 = (1101221)_3 has lowest nonzero digit 1. A regular x4-closed L holding 1024
and missing C* would be a finite, exactly checkable proof of Erdős. K2' says no such L exists, so automatic induction
of this kind cannot prove Erdős. A null through n states is a bounded nonexistence theorem only (GC1257).

Conventions (GPT, GC1257).
- L is a set of POSITIVE integers recognised on canonical ternary numerals: MSB-first [12][012]*, or LSD-first
  [012]*[12]. The DFA's answers on noncanonical words are ignored. Both reading directions are searched and reported
  separately, since fixed state bounds depend on the direction.
- Closure is forward image inclusion, 4L subset L: x in L implies 4x in L.
- C* is the positive canonical words over {0, 1}.
- Seed-free: L holds an actual x whose lowest nonzero ternary digit is 1 (x may be divisible by 3). The seed-1024
  variant (1024 in L) is kept separate; it implies the seed-free condition, so a seed-free null implies a seed-1024
  null at the same size and direction.

The encoding (a complete DFA with n states, start 0, transitions one-hot, an accepting set F).
- Closure, LSD: the product of A on x, A on 4x and the x4 transducer (carry c in 0..3, digit d: v = 4d + c, output
  v mod 3, next carry v div 3; final flush 0: nothing, 1: "1", 2: "2", 3: "0" then "1"), with a flag for "last digit
  read nonzero" (canonical input). Reachable-set variables R must contain the start and be closed under transitions,
  and every R-state with a canonical input and p in F must reach F on the output after the flush. Sound both ways: a
  model gives closure on every word, and a closed DFA makes its exact reachable set a model.
- Closure, MSB: the same product with x4 run most-significant first: guess the overflow c0 in 0..3 (output starts with
  its numeral: "", "1", "2", "10"), then at each digit d with outgoing carry c choose the incoming carry c' in 0..3 with
  o = 4d + c' - 3c in {0, 1, 2}; a run is valid when the final incoming carry is 0. Every valid run outputs exactly 4x
  (telescoping), so the reachable-set encoding is sound both ways as in the LSD case.
- Avoidance: reachable-set variables over {0, 1}-words; no canonical one is accepted.
- Witness (existential, so EXACT): layered reachability in the product of A with the witness automaton (LSD
  0*1(e | [012]*[12]); MSB canonical with last nonzero digit 1), at most 4n (LSD) or 3n (MSB) layers, which bounds a
  shortest accepted path. Implications run from a layer to an actual predecessor, so a model holds a real path.
- Seed variant: the fixed word of the seed is run through A and must end in F.
- Literal verifier: every SAT model is decoded and checked by integers (closure for every x < 3^10 in L, avoidance for
  every C* word of at most 14 digits, a witness found below 3^10).
- Certificates: an UNSAT instance is re-solved by CaDiCaL with an LRAT proof and checked by cake_lpr (the lock wrapper,
  one check at a time). kissat gives the first verdict.

RUN-ON:     cpu, M5; kissat, cadical, ~/np-build/cake_lpr/cake_lpr; files under ~/np-scratch-int/rule30-k2prime (outside
            git).
COMMAND:    python3 tests/probes/swarm/erdos_k2prime_barrier.py controls
            python3 tests/probes/swarm/erdos_k2prime_barrier.py run NMIN NMAX [lsd|msb|both] [free|unit|1024|both|all]

Record searched (record_find, 2026-10-15 11:53 BST): 'x4-closed' -> 1 hit, '3-recognisable' -> 1, 'automaton barrier'
-> 2 (all in 8.113 / SW01-OBJECTS.md); 'Abram' -> 2 (PRIOR-ART names only); 'K2' -> 252 substring hits, none on K2'.

PREDICTIONS (written 2026-10-15 11:57 BST, before any run of this probe).
  Controls (gates: the run does not count unless all pass).
  C1 the empty language (F empty, n = 1) satisfies closure and avoidance, and fails the seed-free witness.
  C2 L2 = {x : lowest nonzero ternary digit is 2} (3-state DFAs, both directions, fixed by unit clauses) satisfies
     closure and avoidance and fails the seed-free witness; the literal verifier agrees.
  C3 the seed-64 variant is UNSAT at n = 1 .. 5 in both directions (4 x 64 = 256 = (100111)_3 is in C*).
  C4 the transducers: LSD and MSB x4 of every x < 3^8 match 4x as integers, including x = 8 -> 32 = (1012)_3, which
     exercises the flush of carry 3.
  C5 positive control for the search: with the witness dropped and "L nonempty" required, n = 2 is SAT in both
     directions (for example {x = 2 mod 3}), and the literal verifier accepts the model.
  C6 replication: n = 1 .. 4 seed-free is UNSAT in both directions, as both judges' brute-force censuses found.
  P1 (0.95): seed-free is UNSAT at every n = 5 .. 10 in both directions, each with a cake_lpr-verified LRAT proof.
  P2 (0.97, implied by P1 where P1 holds): the seed-1024 variant is UNSAT at every n = 5 .. 10 in both directions.
  P3 (cost, 0.5): every instance up to n = 10 decides within one hour of kissat; if not, the instance is reported as
     UNKNOWN at its size, and symmetry breaking (BFS state order) is added only with a control that it leaves the
     verdicts at n <= 6 unchanged.
  P4 (0.99; added 2026-10-15 after GC1258 and before any run): the unit-witness mode (an accepted u = 1 mod 3) gives
     the same verdict as the seed-free mode at every n and direction. GPT's W297 (Local's carrying read, L732) says the
     two searches are equivalent at the same state bound; a mismatch would refute W297's state claim or show a bug.
  U, the unexpected check (0.6): the MSB direction is harder than the LSD direction (longer kissat time) at every
     n >= 7, because x4 is a sequential transducer LSD-first but needs guessed carries MSB-first.
  Counterfactual: a SAT model at any n, confirmed by the literal verifier, refutes K2' and is the first regular
  x4-invariant structure in the record beyond congruences; it is reported at once with its DFA, before anything else.
"""
import os
import subprocess
import sys
import time

OUT = os.path.expanduser('~/np-scratch-int/rule30-k2prime')
CAKE = os.path.expanduser('~/np-build/cake_lpr/cake_lpr')


# ---------------------------------------------------------------- numerals and transducers (checked in C4)
def tern_msb(x):
    s = ''
    while x:
        s = str(x % 3) + s
        x //= 3
    return s


def times4_lsd(w):
    """w: canonical LSD-first digits of x; returns LSD-first digits of 4x by the carry transducer."""
    c, out = 0, []
    for ch in w:
        v = 4 * int(ch) + c
        out.append(str(v % 3))
        c = v // 3
    out += {0: [], 1: ['1'], 2: ['2'], 3: ['0', '1']}[c]
    return ''.join(out)


def times4_msb(w):
    """w: canonical MSB-first digits; returns MSB-first digits of 4x via the guessed-carry runs (unique valid run)."""
    runs = set()

    def go(i, c, out):
        if i == len(w):
            if c == 0:
                runs.add(out)
            return
        d = int(w[i])
        for ci in range(4):
            o = 4 * d + ci - 3 * c
            if 0 <= o <= 2:
                go(i + 1, ci, out + str(o))

    for c0 in range(4):
        go(0, c0, {0: '', 1: '1', 2: '2', 3: '10'}[c0])
    assert len(runs) == 1, (w, runs)
    return runs.pop()


# ---------------------------------------------------------------- CNF builder
class CNF:
    def __init__(self):
        self.n = 0
        self.cl = []

    def var(self):
        self.n += 1
        return self.n

    def add(self, *lits):
        self.cl.append(lits)

    def exactly_one(self, vs):
        self.add(*vs)
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)):
                self.add(-vs[i], -vs[j])

    def dimacs(self):
        return 'p cnf %d %d\n' % (self.n, len(self.cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in self.cl)


def build(n, direction, mode, fixed=None, need_witness=True, need_nonempty=False):
    """mode: 'free' | '1024' | '64' | None. fixed: (delta, F) to pin a DFA (controls)."""
    f = CNF()
    T = [[[f.var() for _ in range(n)] for _ in range(3)] for _ in range(n)]
    F = [f.var() for _ in range(n)]
    for s in range(n):
        for d in range(3):
            f.exactly_one(T[s][d])
    if fixed:
        delta, acc = fixed
        for s in range(n):
            for d in range(3):
                f.add(T[s][d][delta[s][d]])
            f.add(F[s] if s in acc else -F[s])

    # closure
    if direction == 'lsd':
        R = {(p, q, c, z): f.var() for p in range(n) for q in range(n) for c in range(4) for z in range(2)}
        f.add(R[(0, 0, 0, 0)])
        for (p, q, c, z), r in R.items():
            for d in range(3):
                v = 4 * d + c
                o, c2, z2 = v % 3, v // 3, int(d != 0)
                for p2 in range(n):
                    for q2 in range(n):
                        f.add(-r, -T[p][d][p2], -T[q][o][q2], R[(p2, q2, c2, z2)])
            if z == 1:
                if c == 0:
                    f.add(-r, -F[p], F[q])
                elif c in (1, 2):
                    for q1 in range(n):
                        f.add(-r, -F[p], -T[q][c][q1], F[q1])
                else:
                    for q1 in range(n):
                        for q2 in range(n):
                            f.add(-r, -F[p], -T[q][0][q1], -T[q1][1][q2], F[q2])
    else:
        R = {(p, q, c, g): f.var() for p in range(n) for q in range(n) for c in range(4) for g in range(3)}
        f.add(R[(0, 0, 0, 0)])
        for q in range(n):
            f.add(-T[0][1][q], R[(0, q, 1, 0)])
            f.add(-T[0][2][q], R[(0, q, 2, 0)])
            for q2 in range(n):
                f.add(-T[0][1][q], -T[q][0][q2], R[(0, q2, 3, 0)])
        for (p, q, c, g), r in R.items():
            for d in range(3):
                g2 = g if g else (1 if d else 2)
                for ci in range(4):
                    o = 4 * d + ci - 3 * c
                    if not 0 <= o <= 2:
                        continue
                    for p2 in range(n):
                        for q2 in range(n):
                            f.add(-r, -T[p][d][p2], -T[q][o][q2], R[(p2, q2, ci, g2)])
            if c == 0 and g == 1:
                f.add(-r, -F[p], F[q])

    # avoidance of C*
    S = {(p, z): f.var() for p in range(n) for z in range(3)}
    f.add(S[(0, 0)])
    for (p, z), s in S.items():
        for d in (0, 1):
            if direction == 'lsd':
                z2 = 1 if d == 1 else 2        # 1: last digit 1 (canonical so far), 2: last digit 0
            else:
                z2 = z if z else (1 if d == 1 else 2)
            for p2 in range(n):
                f.add(-s, -T[p][d][p2], S[(p2, z2)])
        if z == 1:
            f.add(-s, -F[p])

    # witness (exact layered reachability) or seed
    if mode in ('free', 'unit') and need_witness:
        if direction == 'lsd' and mode == 'free':      # 0*1(e | [012]*[12])
            W = {0: {0: 0, 1: 1}, 1: {0: 2, 1: 3, 2: 3}, 2: {0: 2, 1: 3, 2: 3}, 3: {0: 2, 1: 3, 2: 3}}
            wacc, nw = (1, 3), 4
        elif direction == 'lsd':                        # unit (W297): 1(e | [012]*[12])
            W = {0: {1: 1}, 1: {0: 2, 1: 3, 2: 3}, 2: {0: 2, 1: 3, 2: 3}, 3: {0: 2, 1: 3, 2: 3}}
            wacc, nw = (1, 3), 4
        elif mode == 'free':                            # canonical, last NONZERO digit 1
            W = {0: {1: 1, 2: 2}, 1: {0: 1, 1: 1, 2: 2}, 2: {0: 2, 1: 1, 2: 2}}
            wacc, nw = (1,), 3
        else:                                           # unit (W297): canonical, last digit 1
            W = {0: {1: 1, 2: 2}, 1: {0: 3, 1: 1, 2: 2}, 2: {0: 3, 1: 1, 2: 2}, 3: {0: 3, 1: 1, 2: 2}}
            wacc, nw = (1,), 4
        K = nw * n
        Reach = [{(p, w): f.var() for p in range(n) for w in range(nw)} for _ in range(K + 1)]
        for (p, w), v in Reach[0].items():
            f.add(v if (p, w) == (0, 0) else -v)
        for k in range(1, K + 1):
            for (p2, w2), v in Reach[k].items():
                pre = []
                for p in range(n):
                    for w in range(nw):
                        for d, wn in W[w].items():
                            if wn != w2:
                                continue
                            a = f.var()
                            f.add(-a, Reach[k - 1][(p, w)])
                            f.add(-a, T[p][d][p2])
                            pre.append(a)
                f.add(-v, *pre)
        fin = []
        for k in range(K + 1):
            for p in range(n):
                for w in wacc:
                    b = f.var()
                    f.add(-b, Reach[k][(p, w)])
                    f.add(-b, F[p])
                    fin.append(b)
        f.add(*fin)
    elif mode in ('1024', '64'):
        x = int(mode)
        word = tern_msb(x) if direction == 'msb' else tern_msb(x)[::-1]
        Q = [[f.var() for _ in range(n)] for _ in range(len(word) + 1)]
        f.add(Q[0][0])
        for i, ch in enumerate(word):
            for s in range(n):
                for t in range(n):
                    f.add(-Q[i][s], -T[s][int(ch)][t], Q[i + 1][t])
        for s in range(n):
            f.add(-Q[len(word)][s], F[s])
    if need_nonempty:
        # some canonical word is accepted: layered reachability with a canonical tracker
        K = 2 * n
        Reach = [{(p, z): f.var() for p in range(n) for z in range(3)} for _ in range(K + 1)]
        for (p, z), v in Reach[0].items():
            f.add(v if (p, z) == (0, 0) else -v)
        for k in range(1, K + 1):
            for (p2, z2), v in Reach[k].items():
                pre = []
                for p in range(n):
                    for z in range(3):
                        for d in range(3):
                            if direction == 'lsd':
                                zn = 1 if d else 2
                            else:
                                zn = z if z else (1 if d else 2)
                            if zn != z2:
                                continue
                            a = f.var()
                            f.add(-a, Reach[k - 1][(p, z)])
                            f.add(-a, T[p][d][p2])
                            pre.append(a)
                f.add(-v, *pre)
        fin = []
        for k in range(K + 1):
            for p in range(n):
                b = f.var()
                f.add(-b, Reach[k][(p, 1)])
                f.add(-b, F[p])
                fin.append(b)
        f.add(*fin)
    return f, T, F


# ---------------------------------------------------------------- solving, decoding, verifying
def solve(f, tag, cert=True, cap=3600):
    os.makedirs(OUT, exist_ok=True)
    cnf = os.path.join(OUT, tag + '.cnf')
    open(cnf, 'w').write(f.dimacs())
    t0 = time.time()
    try:
        r = subprocess.run(['kissat', '-q', cnf], capture_output=True, text=True, timeout=cap)
        rc = r.returncode
    except subprocess.TimeoutExpired:
        return 'UNKNOWN', None, time.time() - t0, None
    secs = time.time() - t0
    if rc == 10:
        model = set()
        for line in r.stdout.splitlines():
            if line.startswith('v'):
                model.update(int(x) for x in line.split()[1:] if int(x) > 0)
        os.unlink(cnf)
        return 'SAT', model, secs, None
    if rc != 20:
        return 'ERROR%d' % rc, None, secs, None
    chk = None
    if cert:
        lrat = os.path.join(OUT, tag + '.lrat')
        c = subprocess.run(['cadical', '-q', '--lrat', '--no-binary', cnf, lrat], capture_output=True, text=True)
        if c.returncode == 20:
            k = subprocess.run([CAKE, '--CML_HEAP_SIZE=6000', '--CML_STACK_SIZE=2000', cnf, lrat], capture_output=True,
                               text=True)
            chk = 'VERIFIED' if 's VERIFIED UNSAT' in k.stdout else 'REJECTED'
        else:
            chk = 'CADICAL%d' % c.returncode
        if os.path.exists(lrat):
            os.unlink(lrat)
    os.unlink(cnf)
    return 'UNSAT', None, secs, chk


def decode(model, T, F, n):
    delta = [[next(t for t in range(n) if T[s][d][t] in model) for d in range(3)] for s in range(n)]
    acc = {s for s in range(n) if F[s] in model}
    return delta, acc


def accepts(delta, acc, word):
    s = 0
    for ch in word:
        s = delta[s][int(ch)]
    return s in acc


def in_L(delta, acc, x, direction):
    w = tern_msb(x)
    return accepts(delta, acc, w if direction == 'msb' else w[::-1])


def literal_verify(delta, acc, direction, mode, need_witness=True):
    for x in range(1, 3 ** 10):
        if in_L(delta, acc, x, direction) and not in_L(delta, acc, 4 * x, direction):
            return 'closure fails at %d' % x
    for k in range(1, 15):
        for bits in range(2 ** (k - 1)):
            w = '1' + format(bits, '0%db' % (k - 1)) if k > 1 else '1'
            x = int(w, 3)
            if in_L(delta, acc, x, direction):
                return 'avoidance fails at %d' % x
    if mode in ('free', 'unit') and need_witness:
        for x in range(1, 3 ** 10):
            y = x
            while mode == 'free' and y % 3 == 0:
                y //= 3
            if y % 3 == 1 and in_L(delta, acc, x, direction):
                return 'OK witness %d' % x
        return 'no witness below 3^10'
    if mode in ('1024', '64'):
        return 'OK seed' if in_L(delta, acc, int(mode), direction) else 'seed missing'
    return 'OK'


# ---------------------------------------------------------------- controls
L2 = {'lsd': ([[0, 2, 1], [1, 1, 1], [2, 2, 2]], {1}),      # s0 zeros; 2 -> s1 accept-all; 1 -> sink s2
      'msb': ([[0, 1, 2], [1, 1, 2], [2, 1, 2]], {2})}      # state = last nonzero digit (0 none, 1, 2)


def controls():
    ok = True
    # C4 transducers
    c4 = all(int(times4_lsd(tern_msb(x)[::-1])[::-1], 3) == 4 * x and int(times4_msb(tern_msb(x)), 3) == 4 * x
             for x in range(1, 3 ** 8))
    c4 = c4 and times4_lsd('22') == '2101' and times4_msb('22') == '1012'
    print('C4', 'PASS' if c4 else 'FAIL', flush=True)
    ok &= c4
    for dr in ('lsd', 'msb'):
        # C1 empty language
        f, T, F = build(1, dr, 'free', fixed=([[0, 0, 0]], set()), need_witness=False)
        a = solve(f, 'c1a_%s' % dr, cert=False)[0]
        f, T, F = build(1, dr, 'free', fixed=([[0, 0, 0]], set()))
        b = solve(f, 'c1b_%s' % dr, cert=False)[0]
        c1 = a == 'SAT' and b == 'UNSAT'
        print('C1 %s' % dr, 'PASS' if c1 else 'FAIL', a, b, flush=True)
        # C2 lowest nonzero digit 2
        f, T, F = build(3, dr, 'free', fixed=L2[dr], need_witness=False)
        a, model, _, _ = solve(f, 'c2a_%s' % dr, cert=False)
        lv = literal_verify(*L2[dr], dr, 'free', need_witness=False)
        f, T, F = build(3, dr, 'free', fixed=L2[dr])
        b = solve(f, 'c2b_%s' % dr, cert=False)[0]
        lw = literal_verify(*L2[dr], dr, 'free')
        c2 = a == 'SAT' and b == 'UNSAT' and lv == 'OK' and lw == 'no witness below 3^10'
        print('C2 %s' % dr, 'PASS' if c2 else 'FAIL', a, b, lv, lw, flush=True)
        # C3 seed 64
        c3v = [solve(build(m, dr, '64')[0], 'c3_%s_%d' % (dr, m), cert=True)[::3] for m in range(1, 6)]
        c3 = all(v == ('UNSAT', 'VERIFIED') for v in c3v)
        print('C3 %s' % dr, 'PASS' if c3 else 'FAIL', c3v, flush=True)
        # C5 positive control
        f, T, F = build(2, dr, None, need_witness=False, need_nonempty=True)
        st, model, _, _ = solve(f, 'c5_%s' % dr, cert=False)
        lv = literal_verify(*decode(model, T, F, 2), dr, None) if st == 'SAT' else st
        c5 = st == 'SAT' and lv == 'OK'
        print('C5 %s' % dr, 'PASS' if c5 else 'FAIL', st, lv, flush=True)
        # C6 replication of the judges' censuses
        c6v = [solve(build(m, dr, 'free')[0], 'c6_%s_%d' % (dr, m), cert=True)[::3] for m in range(1, 5)]
        c6 = all(v == ('UNSAT', 'VERIFIED') for v in c6v)
        print('C6 %s' % dr, 'PASS' if c6 else 'FAIL', c6v, flush=True)
        ok &= c1 and c2 and c3 and c5 and c6
    print('CONTROLS', 'ALL PASS' if ok else 'FAILED', flush=True)
    return ok


def run(nmin, nmax, dirs, modes):
    for n in range(nmin, nmax + 1):
        for dr in dirs:
            for md in modes:
                f, T, F = build(n, dr, md)
                st, model, secs, chk = solve(f, 'k2p_%s_%s_%d' % (dr, md, n))
                line = 'n=%d %s %s: %s %.1f s vars %d clauses %d' % (n, dr, md, st, secs, f.n, len(f.cl))
                if st == 'UNSAT':
                    line += ' cake_lpr %s' % chk
                if st == 'SAT':
                    delta, acc = decode(model, T, F, n)
                    line += ' MODEL delta=%s F=%s verify: %s' % (delta, sorted(acc), literal_verify(delta, acc, dr, md))
                print(line, flush=True)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'controls'
    if cmd == 'controls':
        controls()
    else:
        nmin, nmax = int(sys.argv[2]), int(sys.argv[3])
        dsel = sys.argv[4] if len(sys.argv) > 4 else 'both'
        msel = sys.argv[5] if len(sys.argv) > 5 else 'both'
        dirs = ['lsd', 'msb'] if dsel == 'both' else [dsel]
        modes = ['free', 'unit', '1024'] if msel == 'all' else (['free', '1024'] if msel == 'both' else [msel])
        run(nmin, nmax, dirs, modes)
