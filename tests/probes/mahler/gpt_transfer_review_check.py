#!/usr/bin/env python3
"""GC2935: small exact self-checks of the Mahler carrying review, not a census."""
from collections import Counter
from fractions import Fraction
import json
import time


def step(n):
    return (3 * n + 1) // 2


def orbit(n, length):
    bits = []
    for _ in range(length):
        bits.append(n % 2)
        n = step(n)
    return bits, n


def valid(bits):
    """Direct rational tail sums, independent of Cloud's integer-slack update."""
    u = Fraction(0)
    for b in reversed(bits):
        u = (b + 2 * u) / 3
        if u >= Fraction(1, 2):
            return False
    return True


def tau(n, cap=100):
    bits = []
    for length in range(1, cap + 1):
        bits.append(n % 2)
        n = step(n)
        if not valid(bits):
            return length
    raise AssertionError('fixed horizon cap reached')


def psi(x, L):
    out = x
    k = 0
    while True:
        match = (x >> k) % 2 == (k % 2 == 0)
        if k >= 2 * L and k % 2 == 0:
            out ^= 1 << k
        if not match:
            return out
        k += 1


def inverse(y, L):
    tL = (4**L - 1) // 3
    if y % 4**L != tL:
        return y
    assert y != tL
    x, matching, k = 0, True, 0
    while k <= y.bit_length() + 1:
        bit = (y >> k) % 2
        if matching and k >= 2 * L and k % 2 == 0:
            bit ^= 1
        x |= bit << k
        matching &= bit == (k % 2 == 0)
        k += 1
    assert not matching
    return x


def main():
    start = time.monotonic()
    rows, previous, A = [], None, {0: 1}
    for w in range(1, 11):
        N = 1 << (w - 1)
        data = [orbit(n, w) for n in range(2 * N)]
        chi = [x % 2 for _, x in data]
        alive = [valid(b) for b, _ in data]
        boundary = [a and not valid(b + [1]) for a, (b, _) in zip(alive, data)]
        deaths = sum(b and c for b, c in zip(boundary, chi))
        A[w] = sum(alive)
        assert all(chi[n] == chi[2 * N - 1 - n] for n in range(2 * N))
        prev = previous if previous is not None else [0]
        for n in range(2 * N):
            q, r = divmod(step(n), N)
            assert q <= 2 and chi[n] == (prev[r] ^ (q % 2))
            bits, x = data[n]
            C = sum(b * 2**j * 3**(w - 1 - j) for j, b in enumerate(bits))
            assert x == C * pow(2**w, -1, 3**w) % 3**w
        assert all(chi[r] ^ chi[r + N] == (prev[r] ^ (w % 2 == 0)) for r in range(N))
        d = (2**w + 2 * (-1)**w) // 3
        assert sum(chi) == d + 2 * sum(prev[r] for r in range(N) if r % 3 == (1 - N) % 3)
        if w >= 2:
            assert d <= sum(chi) <= 2**w - d
            assert 2**w <= 4 * sum(chi) <= 3 * 2**w
        # Conditional pairing: suffix starts with 00, is boundary, and avoids one residue.
        R = []
        if w >= 4:
            for r in range(N):
                p, _ = orbit(r, w - 1)
                if p[:2] == [0, 0] and valid(p) and not valid(p + [1]) and r % 3 != (1 - N) % 3:
                    pair = [n for n in range(2 * N) if step(n) % N == r]
                    assert len(pair) == 2
                    assert all(boundary[n] for n in pair)
                    assert chi[pair[0]] != chi[pair[1]]
                    R.append(r)
            assert min(deaths, sum(boundary) - deaths) >= len(R)
        rows.append({'w': w, 'A': A[w], 'O': sum(chi), 'B': sum(boundary), 'D': deaths,
                     'pass1': A[w] - deaths, 'paired_00_suffixes': len(R)})
        previous = chi
    assert [A[w] for w in range(1, 11)] == [2, 3, 5, 8, 12, 18, 27, 40, 60, 90]
    assert all(row['pass1'] >= A[row['w'] + 1] - row['A'] for row in rows[:-1])
    assert rows[0]['D'] == 0 and rows[1]['D'] == rows[1]['B']  # no onset-free conditional bound
    assert orbit(8, 4) == ([0, 0, 0, 1], 41) and orbit(13, 4) == ([1, 0, 0, 1], 68)

    for L in range(1, 4):
        tL = (4**L - 1) // 3
        assert tau(tL) == 2 * L + 2
        Tp = lambda n: 0 if n == tL else psi(step(inverse(n, L)), L)
        for n in range(1 << 9):
            assert inverse(psi(n, L), L) == n
            if n != tL:
                assert psi(inverse(n, L), L) == n
            C = n % 4**L == tL
            preC = step(n) % 4**L == tL
            assert (Tp(n) != step(n)) == (C or preC)
        for W in range(1, 9):
            image = [inverse(n, L) for n in range(1, 2**W) if n != tL]
            expected = set(range(1, 2**W))
            if W >= 2 * L - 1:
                expected.remove((4**((W + 1) // 2) - 1) // 3)
            assert len(set(image)) == len(image) and set(image) == expected
    assert psi(step(inverse(3, 2)), 2) == 21 != step(3)  # claimed one-class support rejected

    witnesses = []
    for k in range(3, 10):
        L = next(L for L in range(2, 2 + 2**(k - 3)) if (7 * pow(9, L, 2**k) + 1) % 2**k == 0)
        n = (7 * 4**L - 1) // 3
        bits, _ = orbit(n, 2 * L + k)
        assert bits == [1] + [0] * (2 * L - 1) + [1] + [0] * (k - 1)
        assert valid(bits) and n.bit_length() == 2 * L + 2
        M = next(M for M in range(1, 1 + 2**(k - 1)) if (27 * pow(9, M, 2**(k + 2)) + 13) % 2**(k + 2) == 0)
        bits2, _ = orbit(9**M, k + 2)
        assert bits2 == [1, 0, 1] + [0] * (k - 1) and valid(bits2)
        witnesses.append({'k': k, 'stripe_L': L, 'power_L': M})
    for L in range(2, 7):
        for v in range(4):
            a = ((3 * v + 1) & -(3 * v + 1)).bit_length() - 1
            K = 2 * L + a
            n = (4**L - 1) // 3 + 4**L * v
            m = 3**(K - 1) * ((3 * v + 1) >> a)
            assert orbit(n, K)[1] == m and tau(n) == K + tau(m)
    assert tau(4) == 12 and tau(9) == 10
    assert time.monotonic() - start < 20
    print(json.dumps({'result': 'PASS', 'first_checks': rows, 'recharge_witnesses': witnesses,
                      'negative_controls': ['one-residue conjugacy support', 'onset-free boundary balance'],
                      'wall_s': time.monotonic() - start}, indent=2))


if __name__ == '__main__':
    main()
