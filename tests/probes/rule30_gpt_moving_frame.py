"""G96 MC1-MC2, preregistered at e2c6a02; PASS 2026-10-06.
MC1 MUST HOLD: all rings width3..8, frames -1/0/1: transported Rule30
update and difference identities; fixed-cell Rule210 evaluation identity.
MC2 MUST HOLD: padded finite seed derivative-dynamics guard, tracked
pulse zero differences vs fixed-cell second difference one, dyadic lags to8.
UNEXPECTED COUNTERFACTUAL MUST FAIL: the Rule30 change field itself
evolves by Rule210. REFUTED-BY: actual next change at sites0,1 is1,
while Rule210 applied to the initial change gives0 there.
No centre profile, shader change, particle tracking claim or prize result.
"""
from itertools import product
from math import comb


def ring(row, rule):
    n = len(row)
    return tuple((rule >> (4*row[(i-1)%n]+2*row[i]+row[(i+1)%n])) & 1
                 for i in range(n))


def shift(row, v):
    return tuple(row[(i+v)%len(row)] for i in range(len(row)))


def xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def finite(points, rule):
    return {i for i in range(min(points)-1,max(points)+2)
            if (rule >> (4*(i-1 in points)+2*(i in points)+(i+1 in points))) & 1}


def main():
    rows = frames = 0
    for n in range(3, 9):
        for row in product((0, 1), repeat=n):
            next_row = ring(row, 30)
            assert xor(next_row,row) == ring(row,210)
            rows += 1
            for v in (-1,0,1):
                # Time1 pullback and a direct update in the moving frame.
                z1 = shift(next_row,v)
                assert z1 == shift(ring(row,30),v)
                # Verify at time2, where the frame shift is nonzero.
                z2 = shift(ring(next_row,30),2*v)
                assert z2 == shift(ring(z1,30),v)
                assert xor(z2,z1) == xor(shift(ring(z1,30),v),z1)
                frames += 1
    seed = {0}
    first = finite(seed,30)
    second = finite(first,30)
    u0, u1 = seed ^ first, first ^ second
    wrong = finite(u0,210)
    assert first == {-1,0,1} and second == {-2,-1,2}
    assert u0 == {-1,1} and u1 == {-2,0,1,2} and wrong == {-2,2}
    assert u1 ^ wrong == {0,1}
    pulse = lambda t,i: int(i == t)
    assert pulse(2,0)-2*pulse(1,0)+pulse(0,0) == 1
    assert all(pulse(t+1,t+1) == pulse(t,t) for t in range(8))
    checks = 0
    for lag in (1,2,4,8):
        for v in (-1,0,1):
            for i in range(-3,11):
                repeated = 0
                for k in range(lag+1):
                    repeated ^= (comb(lag,k)%2)*pulse(k,i+v*k)
                assert repeated == (pulse(lag,i+v*lag) ^ pulse(0,i))
                checks += 1
    print('MC1 PASS:',rows,'ring rows,',frames,'moving-frame cases')
    print('MC2 PASS: derivative-dynamics guard and',checks,'dyadic worldline checks')
    print('Autonomous Rule210-change-field counterfactual REFUTED at sites0,1')
    print('Tracked constant-speed pulse has zero acceleration; fixed-cell second difference1')


if __name__ == '__main__':
    main()
