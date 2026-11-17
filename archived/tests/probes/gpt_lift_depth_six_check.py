#!/usr/bin/env python3
"""Small exact controls for GC2932's depth-six bridge, not a general census."""
import json
import resource
import time


def factorial_cutoff(k):
    r = 0
    valuation = 0
    while valuation < k:
        r += 1
        term = r
        while term % 2 == 0:
            valuation += 1
            term //= 2
    return r


def profile(x, modulus, cutoff):
    product = 1
    total = 1
    for j in range(1, cutoff):
        product = product * (x + j) % modulus
        total = (total + product) % modulus
    return -total % modulus


def truncated_valuation(x, k):
    if x == 0:
        return k
    return min(k, (x & -x).bit_length() - 1)


def diagonal_step(u, modulus):
    following = [2]
    for n in range(1, len(u)):
        older = 1 if n == 1 else u[n - 2]
        following.append((u[n] * u[n - 1] + older - 1) % modulus)
    return following


def main():
    started = time.monotonic()
    # Full spatial rows independently check the coordinate convention.
    row = {0: 1}
    u = [2] + [1] * 6
    for t in range(13):
        assert all(u[n] == 1 + row.get(n - t, 0) for n in range(7))
        if t == 12:
            break
        following = {}
        for j in range(-t - 1, t + 2):
            left, centre, right = (row.get(j - 1, 0), row.get(j, 0), row.get(j + 1, 0))
            following[j] = left + centre + right + centre * right
        row = following
        u = [2] + [u[n] * u[n - 1] + (1 if n == 1 else u[n - 2]) - 1 for n in range(1, 7)]

    results = []
    reversed_phase_rejected = False
    previous_clock = None
    for k in range(1, 13):
        modulus = 1 << k
        cutoff = factorial_cutoff(k)
        onset = k + 2 + 2 * cutoff
        values = [profile(x, modulus, cutoff) for x in range(modulus)]
        assert all(values[(x - 1) % modulus] == (x * values[x] - 1) % modulus for x in range(modulus))
        assert all(truncated_valuation(values[x], k) == truncated_valuation((x + 2) % modulus, k) for x in range(modulus))
        assert [x for x in range(modulus) if values[x] == 0] == [(modulus - 2) % modulus]
        assert any(values[x] != values[(x + modulus // 2) % modulus] for x in range(modulus))
        if k == 2:
            assert values == [2, 3, 0, 3]
        u = [2] + [1] * 6
        clock = None
        for t in range(onset + 2 * modulus + 1):
            if t == k + 1:
                clock = (u[3] + t) % modulus
                if previous_clock is not None:
                    assert clock % (modulus // 2) == previous_clock
            if t >= k + 1:
                assert (u[3] + t) % modulus == clock
            if t >= onset:
                expected = values[(clock - t) % modulus]
                assert u[6] == expected
                assert truncated_valuation(u[6], k) == truncated_valuation((clock + 2 - t) % modulus, k)
                reversed_phase_rejected |= u[6] != values[(clock + t) % modulus]
            u = diagonal_step(u, modulus)
        previous_clock = clock
        results.append({'k': k, 'r_k': cutoff, 'onset': onset, 'clock_residue': clock, 'period': modulus})
        assert time.monotonic() - started < 20
    assert reversed_phase_rejected
    print(json.dumps({'result': 'PASS', 'full_rows_through': 12, 'reversed_phase_control': 'REJECTED',
                      'cases': results, 'cpu_s': resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime}, indent=2))


if __name__ == '__main__':
    main()
