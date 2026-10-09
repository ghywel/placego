#!/usr/bin/env python3
"""rule30_template_coupling.py: TC, GPT's GC831 bounded periodic coupling gate for GC828's retained template, run by
Local (chat L451). The specification, predictions and controls are GPT's (RULE30-GPT.md GC831, published before this
file); the implementation choices below were pushed before any run.

RUN-ON:     cpu (Python 3, kissat; drat-trim, cadical and cake_lpr for an UNSAT certificate); minutes
COMMAND:    python3 tests/probes/lexicon/rule30_template_coupling.py

The query (GC831). V0 = D = (00000001011)(01011)^4, repeated five times, q = 155 ticks (cyclic). Unknown q-periodic
profiles V1 .. V_(K+1) satisfy, at every tick t mod q,
    V_i(t + 1) xor V_i(t) = V_(i+1)(t) OR V_(i+2)(t),     i = 0 .. K - 1;
the driver V0 OR V1 has an odd count over q (equivalently V1 has an even count on D's 80 white ticks); and every
adjacent pair (V_i, V_(i+1)), i = 0 .. K, is NOT jointly invariant under the shift q/p for each prime p dividing q
(shifts 31 and 5 at q = 155), so that each pair's joint least period is q. Nothing else is imposed (no background, no
last profiles, no individual period guards, no word-language constraint).
Encoding (Local's): one variable per profile bit; Delta V_i = V_(i+1) OR V_(i+2) by an OR auxiliary and a three-term
XOR, with V0's constants folded in; the driver parity by a Tseitin XOR chain; a guard as one clause over one-way
difference indicators d -> (V(t) != V(t + s)). A SAT model is decoded and checked by separate code: every cyclic
equation including the wraparound at t = q - 1 -> 0, the driver count, and each adjacent pair's least joint period
computed from the words. A and B are then integrated literally (Delta A = D OR V1 over 2q, Delta B = A OR D) and E's
parity from B(t + q) xor B(t), compared with G.GPT263's even prediction; whether B closes at period 2q is reported, not
imposed. An UNSAT is certified: kissat DRAT, drat-trim to LRAT (cadical's native LRAT as fallback), cake_lpr.

PREDICTIONS (GPT's, GC831): P1, K = 4 SAT (0.60). P2, K = 6 SAT given K = 4 SAT and its checks (0.55).
Controls (GPT's): C0, the same builder at q = 5 with V0 = P = 01011 accepts GC817's genuine tail P, D, U, U, P, Q, R, S
(D = 11100, U = 00101, Q = 01101, R = 10101, S = 10110) with every profile fixed, at K = 4 (first six) and K = 6 (first
eight). Local adds C0b: with only V0 fixed, the q = 5 builder is SAT. Unexpected check (GPT's): the wraparound equations
at t = q - 1 are verified explicitly in every SAT model. Plan: K = 4; then K = 6 only if K = 4 is SAT and its checks
pass; then stop. A checked UNSAT rejects this D; a SAT is a finite periodic fragment only.
"""
import os
import subprocess
import sys

DIR = os.path.expanduser('~/np-scratch-int/rule30-tc')
CAKE = os.path.expanduser('~/np-build/cake_lpr/cake_lpr')
D155 = [int(c) for c in ('00000001011' + '01011' * 4) * 5]
TAIL5 = ['11100', '00101', '00101', '01011', '01101', '10101', '10110']          # V1 .. V7 of GC817 after P


class CNF:
    def __init__(self):
        self.n, self.cl = 0, []

    def new(self):
        self.n += 1
        return self.n

    def add(self, c):
        self.cl.append(c)

    def text(self):
        return 'p cnf %d %d\n' % (self.n, len(self.cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in self.cl)


def build(q, V0, K, fixed=None):
    """returns (cnf, var) with var[(i, t)] a literal for i >= 1; V0 is a constant word"""
    f = CNF()
    var = {(i, t): f.new() for i in range(1, K + 2) for t in range(q)}

    def lit(i, t):                                       # (True/False constant) or literal
        return bool(V0[t % q]) if i == 0 else var[(i, t % q)]

    def xor_zero(terms):
        """XOR of terms (literals or bools) = 0"""
        par, lits = 0, []
        for x in terms:
            if isinstance(x, bool):
                par ^= int(x)
            else:
                lits.append(x)
        if not lits:
            if par:
                f.add([])                                # contradiction
            return
        # chain through auxiliaries for more than 3 literals
        while len(lits) > 3:
            a, b = lits.pop(), lits.pop()
            y = f.new()
            f.add([-a, -b, -y]); f.add([a, b, -y]); f.add([a, -b, y]); f.add([-a, b, y])
            lits.append(y)
        k = len(lits)
        for mask in range(1 << k):                       # forbid assignments with XOR != par
            vals = [(mask >> j) & 1 for j in range(k)]
            if sum(vals) % 2 != par:
                f.add([(-l if v else l) for l, v in zip(lits, vals)])

    for i in range(K):
        for t in range(q):
            a, a1, b, c = lit(i, t), lit(i, t + 1), lit(i + 1, t), lit(i + 2, t)
            # o = b OR c
            if isinstance(b, bool) and isinstance(c, bool):
                o = b or c
            elif b is True or c is True:
                o = True
            else:
                o = f.new()
                xs = [x for x in (b, c) if not isinstance(x, bool)]
                for x in xs:
                    f.add([-x, o])
                f.add(xs + [-o])
            xor_zero([a, a1, o])
    # odd driver: V0 OR V1 has odd count  <=>  V1's count on V0-white ticks has parity 1 xor (V0 black count) mod 2
    whites = [var[(1, t)] for t in range(q) if not V0[t]]
    xor_zero(whites + [bool((1 + sum(V0)) % 2)])        # XOR(whites) = 1 xor black count
    # pair guards
    primes = [p for p in range(2, q + 1) if q % p == 0 and all(p % r for r in range(2, p))]
    for p in primes:
        s = q // p
        for i in range(K + 1):
            clause, sat = [], False
            for j in (i, i + 1):
                for t in range(q):
                    x, y = lit(j, t), lit(j, t + s)
                    if isinstance(x, bool) and isinstance(y, bool):
                        if x != y:
                            sat = True
                        continue
                    d = f.new()
                    for xx, yy in ((x, y),):
                        if isinstance(xx, bool):
                            f.add([-d, (-yy if xx else yy)])
                        elif isinstance(yy, bool):
                            f.add([-d, (-xx if yy else xx)])
                        else:
                            f.add([-d, xx, yy]); f.add([-d, -xx, -yy])
                    clause.append(d)
            if not sat:
                f.add(clause)
    if fixed:
        for (i, t), v in fixed.items():
            f.add([var[(i, t)] if v else -var[(i, t)]])
    return f, var


def solve(cnf_text, name, proof=False):
    os.makedirs(DIR, exist_ok=True)
    path = os.path.join(DIR, name + '.cnf')
    open(path, 'w').write(cnf_text)
    args = ['kissat', '-q'] + (['-f', '--no-binary', path, path[:-4] + '.drat'] if proof else [path])
    r = subprocess.run(args, capture_output=True, text=True)
    model = set()
    for line in r.stdout.splitlines():
        if line.startswith('v '):
            model.update(int(x) for x in line[2:].split() if x != '0')
    return {10: 'SAT', 20: 'UNSAT'}.get(r.returncode, 'UNKNOWN'), model, path


def certify(path):
    drat, lrat = path[:-4] + '.drat', path[:-4] + '.lrat'
    v = subprocess.run(['drat-trim', path, drat, '-L', lrat], capture_output=True, text=True)
    ok = 's VERIFIED' in [l.replace('\r', '').strip() for l in v.stdout.splitlines()]
    c = subprocess.run([CAKE, path, lrat], capture_output=True, text=True) if ok else None
    if c is not None and 's VERIFIED UNSAT' in c.stdout:
        return 'VERIFIED-UNSAT (drat-trim LRAT, cake_lpr)'
    lrat2 = path[:-4] + '.cad.lrat'
    subprocess.run(['cadical', '-q', '--lrat=true', path, lrat2], capture_output=True, text=True)
    c2 = subprocess.run([CAKE, path, lrat2], capture_output=True, text=True)
    return 'VERIFIED-UNSAT (cadical LRAT, cake_lpr)' if 's VERIFIED UNSAT' in c2.stdout else 'NOT-VERIFIED'


def least_period(words):
    q = len(words[0])
    for s in range(1, q + 1):
        if q % s == 0 and all(w[t] == w[(t + s) % q] for w in words for t in range(q)):
            return s


def check(q, V, K):
    """independent literal checks of a model: V is the list of words V0 .. V_(K+1)"""
    eq = all((V[i][(t + 1) % q] ^ V[i][t]) == (V[i + 1][t] | V[i + 2][t]) for i in range(K) for t in range(q))
    wrap = all((V[i][0] ^ V[i][q - 1]) == (V[i + 1][q - 1] | V[i + 2][q - 1]) for i in range(K))
    driver = sum(V[0][t] | V[1][t] for t in range(q)) % 2 == 1
    joint = [least_period([V[i], V[i + 1]]) for i in range(K + 1)]
    return eq, wrap, driver, joint


def ab_e(q, D, V1):
    drv = [D[t % q] | V1[t % q] for t in range(2 * q)]
    A = [0]
    for t in range(2 * q - 1):
        A.append(A[-1] ^ drv[t])
    complement = all(A[t + q] == 1 - A[t] for t in range(q)) and (A[-1] ^ drv[-1]) == A[0]
    bd = [A[t] | D[t % q] for t in range(2 * q)]
    if sum(bd) % 2:
        return complement, None, None
    B = [0]
    for t in range(2 * q - 1):
        B.append(B[-1] ^ bd[t])
    E = [B[(t + q) % (2 * q)] ^ B[t] for t in range(q)]
    return complement, True, sum(E) % 2


def words(var, model, q, K, V0):
    return [V0] + [[1 if var[(i, t)] in model else 0 for t in range(q)] for i in range(1, K + 2)]


def main():
    P = [0, 1, 0, 1, 1]
    for K in (4, 6):
        fixed = {(i + 1, t): int(TAIL5[i][t]) for i in range(K + 1) for t in range(5)}
        f, var = build(5, P, K, fixed)
        v, model, _ = solve(f.text(), 'c0-k%d' % K)
        ok = v == 'SAT' and all(x for x in check(5, words(var, model, 5, K, P), K)[:3])
        print('C0 (q = 5, GC817 tail fixed, K = %d): %s, literal checks %s' % (K, v, 'pass' if ok else 'FAIL'), flush=True)
        f, var = build(5, P, K)
        v, model, _ = solve(f.text(), 'c0b-k%d' % K)
        print('C0b (q = 5, only V0 fixed, K = %d): %s' % (K, v), flush=True)
    for K in (4, 6):
        f, var = build(155, D155, K)
        v, model, path = solve(f.text(), 'tc-k%d' % K, proof=True)
        print('K = %d: %s (%d variables, %d clauses)' % (K, v, f.n, len(f.cl)), flush=True)
        if v == 'UNSAT':
            print('  certificate:', certify(path))
            print('P1' if K == 4 else 'P2', 'REFUTED: this D is rejected by the checked K = %d projection' % K)
            break
        if v != 'SAT':
            print('  UNKNOWN: no verdict')
            break
        W = words(var, model, 155, K, D155)
        eq, wrap, driver, joint = check(155, W, K)
        comp, bok, epar = ab_e(155, D155, W[1])
        print('  literal checks: equations %s, wraparound %s, odd driver %s, adjacent joint periods %s' % (
            eq, wrap, driver, joint))
        print('  A complements after 155: %s; B closes at 310: %s; E parity: %s (G.GPT263 predicts even)' % (
            comp, bok, epar))
        print('  V1 =', ''.join(map(str, W[1])))
        good = eq and wrap and driver and all(j == 155 for j in joint)
        print('P1' if K == 4 else 'P2', 'HELD' if good else 'MODEL FAILS CHECKS')
        if not good:
            break
    print('COMPLETE')


if __name__ == '__main__':
    main()
