#!/usr/bin/env python3
"""GC1274/G302: small exact controls for joint leading/trailing cylinders.

Registered at 62219a4a before execution. Not an automaton or orbit census.
Record searched: B.star|backward.hitting with leading|mantissa|length.residue
(one GC1262 countercontrol); G298 and SW01 proposal5 steps3(a)-(e) read.
C1: 162 constructions j,k,h=1..3; length modulus M=1..3, every class.
C2: adding the joint exponent period preserves every condition and grows n.
Counterfactual: omit the leading power in the divisibility correction; fail.
Unexpected: 190 begins with2 but 4*190=760 is ternary01.
Wrong-sign residue2 stays residue2 under multiplication by4.
REFUTED-BY: a failed assertion. Finite controls do not prove the density
or general finite-state obstruction. Large symbolic witnesses are not stored.
OUTCOME GC1275: 162 bases and162 lifts PASS;162 wrong corrections rejected;
15 wrong-sign controls PASS; largest tested ternary length2542;190->760 PASS.
"""

from math import lcm
import json


def ternary(n):
    assert n > 0
    out = []
    while n:
        n, r = divmod(n, 3)
        out.append(str(r))
    return ''.join(reversed(out))


def order_three(m):
    p, v = 1, 3 % m
    while v != 1:
        p += 1
        v = v * 3 % m
    return p


def construct(j, k, h, length_modulus, length_class):
    m = 4 ** j
    period = lcm(order_three(m), length_modulus)
    d = 0
    while 3 ** d < m * 3 ** (h - 1):
        d += 1
    prefix = 3 ** d // m
    assert prefix * m < 3 ** d < (prefix + 1) * m
    n0 = (length_class + d - h) % length_modulus
    count = (-(pow(3, n0, m) + 1) * pow(3 ** k, -1, m)) % m
    low = 1 + sum(3 ** (k + t * period) for t in range(count))
    e = k + (count - 1) * period if count else 0
    threshold = max(k, e + d + 1)
    top = n0 + period * max(0, (threshold - n0 + period - 1) // period)
    return m, period, d, prefix, n0, low, top


def verify(m, k, h, modulus, residue, prefix, low, top):
    y = 3 ** top + low
    n, rem = divmod(y, m)
    assert rem == 0
    assert set(ternary(y)) <= {'0', '1'}
    text = ternary(n)
    assert text[:h] == ternary(prefix)
    assert len(text) % modulus == residue
    assert n % (3 ** k) == pow(m, -1, 3 ** k)
    return n


def main():
    cases = lifts = bad_rejected = 0
    largest_length = 0
    for j in range(1, 4):
        for k in range(1, 4):
            for h in range(1, 4):
                for modulus in range(1, 4):
                    for residue in range(modulus):
                        m, period, d, prefix, n0, low, top = construct(
                            j, k, h, modulus, residue)
                        n = verify(m, k, h, modulus, residue, prefix, low, top)
                        n2 = verify(m, k, h, modulus, residue, prefix, low, top + period)
                        assert n2 > n
                        largest_length = max(largest_length, len(ternary(n2)))
                        # G298's old correction ignores the separately added top digit.
                        wrong_count = -pow(3 ** k, -1, m) % m
                        wrong_low = 1 + sum(3 ** (k + t * period)
                                            for t in range(wrong_count))
                        assert (3 ** top + wrong_low) % m != 0
                        bad_rejected += 1
                        cases += 1
                        lifts += 1
    assert cases == 162
    m, period, d, prefix, n0, low, top = construct(1, 1, 1, 1, 0)
    n = verify(m, 1, 1, 1, 0, prefix, low, top)
    assert (n, n * m, ternary(n), ternary(n * m)) == (190, 760, '21001', '1001011')
    wrong_sign = 0
    for x in (2, 5, 8):
        for j in range(5):
            assert (x * 4 ** j) % 3 == 2
            assert '2' in ternary(x * 4 ** j)
            wrong_sign += 1
    print(json.dumps(dict(base_constructions=cases, larger_lifts=lifts,
                          wrong_correction_rejected=bad_rejected,
                          wrong_sign_controls=wrong_sign,
                          largest_ternary_length=largest_length,
                          unexpected_190='PASS', verdict='ALL CONTROLS PASS')))


if __name__ == '__main__':
    main()
