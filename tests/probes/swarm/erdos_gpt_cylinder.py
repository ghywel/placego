#!/usr/bin/env python3
"""Small controls for GC1262/W298's hand cylinder construction; not a DFA census.

Owner-authorized strongest-pull block, 2026-10-15 12:20 BST. Hand derivation
preceded these controls; the following predictions are written before execution.
RUN-ON: Intel CPU, Python standard library, below one second expected.
COMMAND: python3 tests/probes/swarm/erdos_gpt_cylinder.py

Record searched: regular + closure + 3.adic -> GC1258; Cobham/Furstenberg/K2
-> SW01-OBJECTS proposals 5/7 and judge 2. Read proposal 5's subset-sum
congruence observation, CONSTELLATION G.1 and MAHLER's periodic-tail identity.
B.star/backward.orbit/3.adic.dens -> no matching theorem. This applies the
proposal's elementary congruence mechanism; no literature novelty claim.

P1: for k=1..5, j=0..3 and two separated-digit choices, every constructed
    positive y has only ternary 0/1 digits, 4**j divides y, and x=y/4**j
    has residue inverse(4**j) modulo 3**k. The larger choice gives x>3**k.
P2: multiplying x,y by 3**a, a=0..3, preserves the hit and gives valuation a
    with lowest nonzero digit 1. Both controls should all pass.
C1: powers of 4 modulo 3**k, k=1..7, give exactly the residues 1 mod 3.
C2 (independent literal example): 205*4=820=(1010101)_3, with 205=7 mod9.
U (unexpected distinction): zero is not a positive hitting witness; 3**a
    approaches zero 3-adically through positive 0/1 numbers. A density claim
    must include zero only in the closure.
Counterfactual: any failed digit/divisibility/residue check halts filing of
the construction pending repair. A regular dense test language with both
accepting and rejecting completions MUST fail x4 closure (64 -> 256); if it
does not, inspect it as a K2 counterexample before any other work. An
inconclusive check tips to halt this block, never to claiming K2.
"""


def digits(x):
    out = []
    while x:
        x, d = divmod(x, 3)
        out.append(d)
    return out


def hit(k, j, extra=0):
    modulus = 4 ** j
    period = 1
    while pow(3, period, modulus) != 1 % modulus:
        period += 1
    count = (-pow(3 ** k, -1, modulus)) % modulus + (extra + 1) * modulus
    y = 1 + sum(3 ** (k + t * period) for t in range(count))
    return y // modulus, y


def model_accepts(x):
    """The regular language 'unit residue 1, most significant digit 2'."""
    w = digits(x)
    return bool(w) and w[0] == 1 and w[-1] == 2


def main():
    cases = 0
    for k in range(1, 6):
        for j in range(4):
            for extra in range(2):
                x, y = hit(k, j, extra)
                assert y > 0 and set(digits(y)) <= {0, 1}
                assert x * 4 ** j == y
                assert x % 3 ** k == pow(4 ** j, -1, 3 ** k)
                assert x > 3 ** k
                cases += 1
                for a in range(4):
                    xx, yy = x * 3 ** a, y * 3 ** a
                    assert xx * 4 ** j == yy and set(digits(yy)) <= {0, 1}
                    w = digits(xx)
                    assert w[:a] == [0] * a and w[a] == 1
    for k in range(1, 8):
        assert {pow(4, j, 3 ** k) for j in range(3 ** (k - 1))} == set(range(1, 3 ** k, 3))
    assert 205 * 4 == 820 and digits(820) == [1, 0, 1, 0, 1, 0, 1] and 205 % 9 == 7
    assert digits(0) == []
    for a in range(8):
        assert digits(3 ** a) == [0] * a + [1]
    assert model_accepts(64) and not model_accepts(256) and 4 * 64 == 256
    print('P1 PASS: %d constructions; P2 PASS: %d valuation lifts' % (cases, 4 * cases))
    print('C1 PASS: seven unit groups; C2 PASS: independent 205 -> 820 example')
    print('U PASS: zero is a closure point only; regular dense control fails closure at 64 -> 256')
    print('Finite hand-proof controls only; no K2 verdict, automaton search, or census.')


if __name__ == '__main__':
    main()
