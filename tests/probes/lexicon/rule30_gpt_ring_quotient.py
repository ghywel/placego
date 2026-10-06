#!/usr/bin/env python3
"""G55 published RQ1-RQ3. Small independent quotient/direct controls.
No output data files. Does not extend the large ring census.
"""
from collections import Counter


def rotate(x, p):
    mask = (1 << p) - 1
    return ((x << 1) & mask) | (x >> (p - 1))


def rotations(x, p):
    out = []
    for _ in range(p):
        out.append(x)
        x = rotate(x, p)
    return out


def scalar(x, p):
    out = 0
    for i in range(p):
        left = (x >> ((i - 1) % p)) & 1
        centre = (x >> i) & 1
        right = (x >> ((i + 1) % p)) & 1
        out |= ((30 >> (4 * left + 2 * centre + right)) & 1) << i
    return out


def vector(x, p):
    right = (x >> 1) | ((x & 1) << (p - 1))
    return rotate(x, p) ^ (x | right)


def cycles(states, step):
    done, result = set(), []
    for start in states:
        positions, path = {}, []
        x = start
        while x not in done and x not in positions:
            positions[x] = len(path)
            path.append(x)
            x = step(x)
        if x in positions:
            result.append(path[positions[x]:])
        done.update(path)
    return result


def audit(p):
    states = range(1 << p)
    canonical = {x: min(rotations(x, p)) for x in states}
    for x in states:
        assert scalar(x, p) == vector(x, p)
        assert vector(rotate(x, p), p) == rotate(vector(x, p), p)
    direct = cycles(states, lambda x: scalar(x, p))
    quotient = cycles(sorted(set(canonical.values())), lambda x: canonical[vector(x, p)])
    expected, lift_data = Counter({1: 1}), []
    for cycle in quotient:
        x, q = cycle[0], len(cycle)
        if x == 0:
            assert cycle == [0]
            continue
        assert x != (1 << p) - 1
        assert len(set(rotations(x, p))) == p
        terminal = x
        for _ in range(q):
            terminal = vector(terminal, p)
        b = rotations(x, p).index(terminal)
        expected[q if b == 0 else p * q] += p if b == 0 else 1
        lift_data.append((q, b))
    actual = Counter(map(len, direct))
    assert actual == expected
    gliders = sum(rotate(cycle[0], p) in set(cycle) for cycle in direct)
    assert gliders == 1 + sum(b != 0 for q, b in lift_data)
    if p == 7:
        assert (4, 0) in lift_data and actual[4] == 7
    if p == 11:
        assert (17, 0) in lift_data and actual[17] == 11
    print('RQ1/RQ2 PASS:', p, 'quotient(q,displacement)=', sorted(lift_data), 'cycles=', dict(actual))
    return (1 << p)


if __name__ == '__main__':
    count = sum(audit(p) for p in (3, 5, 7, 11, 13))
    shifted = cycles(range(8), lambda x: rotate(x, 3))
    assert Counter(map(len, shifted)) == Counter({1: 2, 3: 2})
    assert all(rotate(c[0], 3) in set(c) for c in shifted)
    print('RQ3 PASS: shift CA has two travelling cycles of length3.')
    print('Exact scalar/vector state controls:', count)
    print('Small finite controls only; prime-size pattern remains unexplained.')
