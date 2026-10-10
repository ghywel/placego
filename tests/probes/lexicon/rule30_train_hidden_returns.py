#!/usr/bin/env python3
"""GC1022: recurrent five-cell ambiguity and its lost exterior compatibility.

Predictions and record search in RULE30-GPT.md. The two artificial returns
are paths of the free-exterior relaxation, not actual half-line witnesses.
Both fail the exterior cell's own temporal rule. The seven-ring control
realizes the same output as one failed path, so output deletion is unsound.
No solver, strip-width sweep, or claim that every realization of B fails.
"""
from itertools import product

START = (0, 1, 0, 0, 1)


def step(s, w, u):
    p = (w,) + s + (u,)
    return tuple((30 >> (4*p[i]+2*p[i+1]+p[i+2])) & 1 for i in range(5))


def packed(r, w, u):
    r |= u << 5
    return (((r << 1) | w) ^ (r | (r >> 1))) & 31


def trajectory(us):
    states, s = [], START
    for t, u in enumerate(map(int, us)):
        states.append(s)
        s = step(s, int(t % 4 != 0), u)
    return states, s


def main():
    # Independent encodings on the entire four-tick relation, including failures.
    for s in product((0, 1), repeat=5):
        for us in product((0, 1), repeat=4):
            x, r = s, sum(v << i for i, v in enumerate(s))
            for w, u in zip((0, 1, 1, 1), us):
                x, r = step(x, w, u), packed(r, w, u)
                assert x == tuple((r >> i) & 1 for i in range(5))
            if s == (0, 0, 0, 1, 0):
                assert x[0] == 1  # GC1018 failing gate, regardless of input.

    cases = (
        ('A', '000100010001', '010101010101', [3, 7, 11]),
        ('B', '000000000110', '010101010000', [10]),
        ('ring', '100110011001', '010101010101', []),
    )
    for name, us, trace, expected_bad in cases:
        states, end = trajectory(us)
        assert end == START
        assert ''.join(str(s[0]) for s in states) == trace
        assert all(states[t][0] == 0 for t in (0, 4, 8))
        bad = []
        for t, s in enumerate(states):
            u, nxt = int(us[t]), int(us[(t+1) % 12])
            possible = {s[-1] ^ (u | v) for v in (0, 1)}
            if nxt not in possible:
                bad.append(t)
        assert bad == expected_bad
        print(name, 'trace', trace, 'exterior-incompatible ticks', bad)

    # Every concatenation returns to the same state; visible blocks really differ.
    for a, b in product(('000100010001', '000000000110'), repeat=2):
        states, end = trajectory(a+b)
        assert end == START and all(states[t][0] == 0 for t in range(0, 24, 4))
    # The actual periodic control includes one extra site and its own right input.
    ring = ('0100110', '1111101', '0000001', '1000011')
    states, _ = trajectory('100110011001')
    for t, s in enumerate(states):
        assert s == tuple(int(ring[t % 4][i % 7]) for i in range(7, 12))
        u, v = int(ring[t % 4][12 % 7]), int(ring[t % 4][13 % 7])
        assert int(ring[(t+1) % 4][12 % 7]) == s[-1] ^ (u | v)
    r, seed_states = 9, []
    for t in range(29):
        seed_states.append(r)
        r = ((r << 1) | (t % 2)) ^ (r | (r >> 1))
    for t0 in range(4, 25, 4):
        s = tuple((seed_states[t0] >> i) & 1 for i in range(6, 11))
        assert s[0] == 0
        for t in range(t0, t0+4):
            s = step(s, int((t-t0) % 4 != 0), (seed_states[t] >> 11) & 1)
        assert s[0] == 0
        assert s == tuple((seed_states[t0+4] >> i) & 1 for i in range(6, 11))
    print('PASS: complete macro encoding, return words, compatibility and actual control')


if __name__ == '__main__':
    main()
