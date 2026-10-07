#!/usr/bin/env python3
"""Independent scalar audit of Local L118's known G2.3 first-branch witness.
RUN-ON: CPU, Python 3 standard library; COMMAND: python3 tests/probes/lexicon/rule30_fbr16_review.py
No forward search or larger-period experiment. Time order is explicit lists, not packed shifts.
"""
from collections import Counter
import time

Q = 16
WITNESS = '0000110001010011'

def shift(w, d=1):
    return w[d:] + w[:d]

def period(a, b):
    return next(q for q in (1, 2, 4, 8, 16) if shift(a, q % Q) == a and shift(b, q % Q) == b)

def backward(a, b):
    return [b[(t + 1) % Q] ^ (a[t] | b[t]) for t in range(Q)], a[:]

def integrate(a, start):
    c, value = [], start
    for x in a:
        c.append(value)
        value ^= x
    return c, value == start

def order(a):
    w = a[:]
    for m in range(1, Q + 1):
        w = [w[(t + 1) % Q] ^ w[t] for t in range(Q)]
        if not any(w):
            return m
    raise AssertionError('not dyadic periodic')

def newton_degree(a):
    # Direct binomial transform: C(r,t) is odd exactly when t is a submask of r.
    coefficients = [sum(a[t] for t in range(Q) if (t & r) == t) % 2 for r in range(Q)]
    return max(r for r, value in enumerate(coefficients) if value)

def main():
    started = time.process_time()
    witness = [int(x) for x in WITNESS]
    assert sum(witness) == 6 and period(witness, [0] * Q) == Q
    root = ([0] * Q, [1] * Q)
    a, b = witness[:], [0] * Q
    steps, counts, earlier_even = 0, Counter(), 0
    while True:
        q = period(a, b)
        counts[q] += 1
        assert any(a) or any(b), 'zero reached before root'
        if not any(b):
            even = sum(a[:q]) % 2 == 0
            assert even == (steps == 0), 'earlier branch or terminal mismatch'
            earlier_even += int(even and steps > 0)
        if (a, b) == root:
            break
        assert steps < 53208, 'root not reached within expected certificate bound'
        a, b = backward(a, b)
        steps += 1
    assert steps == 53207 and not earlier_even
    assert counts == {1: 3, 2: 5, 4: 21, 8: 371, 16: 52808}
    assert backward(*root) == ([0] * Q, [0] * Q)
    children = [integrate(witness, bit) for bit in (0, 1)]
    assert all(closes for _, closes in children)
    for c, _ in children:
        assert backward([0] * Q, c) == (witness, [0] * Q)
        assert period(c, [0] * Q) == Q
    assert all(shift(children[0][0], r) != children[1][0] for r in range(Q))
    nu = order(witness)
    assert nu == 14 and all(order(c) == nu + 1 for c, _ in children)
    assert newton_degree(witness) == 13 and all(newton_degree(c) == 14 for c, _ in children)
    mutant = witness[:]
    mutant[0] ^= 1
    assert sum(mutant) % 2 == 1 and order(mutant) == Q and newton_degree(mutant) == 15
    assert all(not integrate(mutant, bit)[1] for bit in (0, 1)), 'odd-parity mutation not detected'
    print('PASS: scalar backward depth=%d; periods=%s; no earlier genuine branch' % (steps, dict(sorted(counts.items()))))
    print('PASS: two closed, non-rotation-equivalent children; difference order=%d -> %d; direct Newton degrees=13 -> 14' % (nu, nu + 1))
    print('PASS: one-bit mutation rejects both period-16 integrations; CPU=%.3fs' % (time.process_time() - started))

if __name__ == '__main__':
    main()
