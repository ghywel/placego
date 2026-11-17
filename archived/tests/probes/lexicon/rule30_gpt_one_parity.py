#!/usr/bin/env python3
"""G58 controls published in commit57adc80 before this probe's first run.
OP1 MUST: all26 nonzero masks of periods2,4,6,8,256 steps, scalar
Rule210 = bit-vector XOR; parity support and wall equation hold.
OP2 MUST: depth1 = exact-integer Catalan convolution = dyadic filter.
CF MUST FAIL: these same witnesses also obey Rule30.
REFUTED-BY: local tuple(0,1,0), Rule30=1 versus Rule210/90=0.
Unexpected analytic guard in G58: nonzero one-parity walls have even period.
No blind prediction; finite controls do not replace the all-length proof.
"""
from math import comb


def rule(number, left, center, right):
    return (number >> (4*left + 2*center + right)) & 1


def main():
    horizon = 256
    width = horizon + 2
    cap = (1 << width) - 1
    catalan = [comb(2*j, j)//(j+1) for j in range(horizon//2)]
    walls = transitions = filters = mismatch30 = 0
    seen_guard = False
    for period in (2, 4, 6, 8):
        for mask in range(1, 1 << (period//2)):
            walls += 1
            def tau(t):
                return ((mask >> ((t//2) % (period//2))) & 1) if t % 2 else 0
            scalar = [0]*width
            bits = 0
            for t in range(horizon+1):
                assert bits == sum(c << j for j,c in enumerate(scalar))
                assert all(c == 0 for j,c in enumerate(scalar) if (t+j+1) % 2 == 0)
                pi = scalar[0]
                sigma = tau(t+1) ^ pi
                assert rule(210, pi, tau(t), sigma) == tau(t+1)
                if t % 2:
                    assert pi == sigma == 0
                else:
                    n = t//2
                    exact = 0
                    for m in range(n):
                        exact ^= tau(2*m+1) * (catalan[n-m-1] % 2)
                    dyadic = 0
                    power = 1
                    while power <= n:
                        dyadic ^= tau(2*(n-power)+1)
                        power *= 2
                    assert pi == exact == dyadic
                    filters += 1
                if t == horizon:
                    break
                new = []
                for j,c in enumerate(scalar):
                    left = scalar[j+1] if j+1 < width else 0
                    right = scalar[j-1] if j else tau(t)
                    out = rule(210, left, c, right)
                    new.append(out)
                    if rule(30, left, c, right) != out:
                        mismatch30 += 1
                    if (left,c,right) == (0,1,0):
                        assert out == 0 and rule(30,left,c,right) == 1
                        seen_guard = True
                scalar = new
                bits = ((bits << 1) ^ (bits >> 1) ^ tau(t)) & cap
                transitions += 1
    assert walls == 26 and seen_guard and mismatch30 > 0
    print('OP1 PASS:', walls, 'walls,', transitions, 'whole-row transitions')
    print('OP2 PASS:', filters, 'Catalan/dyadic/depth1 comparisons')
    print('CF REFUTED:', mismatch30, 'Rule30 cell disagreements; (0,1,0) seen')


if __name__ == '__main__':
    main()

# OUTCOME 2026-10-06: OP1 PASS26 walls/6656 transitions; OP2 PASS3354
# comparisons; CF REFUTED197914 Rule30 disagreements, concrete tuple seen.
