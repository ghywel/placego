#!/usr/bin/env python3
"""GC1020: finite certificate for the eternal Q2 train, beside a clamped clock.

Preregistered in RULE30-GPT.md, following GC1019. This applies Local's
P8Lock.lean (GC878 source audit); it does not search for a new lock.
Prediction: the fourteen-cell band closes by a causal sixteen-tick lock.
Controls: literal shrinking cone versus packed rule; independently encoded
five-cell image sets; wrong white-phase input must break the band; one
macro alone must not force white. Unexpected check: arbitrary tails after
site 46 cannot change the finite warmup. The induction is in GC1020;
this program checks its finite premises, not an indefinitely long orbit.
Run: python3 tests/probes/lexicon/rule30_train_p8_closure.py
Outcome: all checks PASS, sixteen-tick lock image has ten states.
"""
from itertools import product

PATTERNS = tuple(tuple(map(int, s)) for s in (
    '10011000100101',
    '11110101111101',
    '00000101000001',
    '00001101100011',
    '10011001010110',
    '11110111010101',
    '00000100010101',
    '00001110110101',
))
LOCK_IMAGE = {
    tuple(map(int, s)) for s in (
        '00000', '00001', '01000', '01001', '01010',
        '01011', '01100', '01101', '01110', '01111',
    )
}


def literal(row, wall, exterior):
    p = (wall,) + row + (exterior,)
    return tuple((30 >> (4*p[i] + 2*p[i+1] + p[i+2])) & 1
                 for i in range(len(row)))


def packed(row, wall):
    return ((row << 1) | wall) ^ (row | (row >> 1))


def encode(row):
    return sum(v << i for i, v in enumerate(row))


def main():
    # Exact cone: after 32 ticks, 46 supplied sites still determine 14 sites.
    row = (1, 0, 0, 1) + (0,)*42
    r = 9
    padded = 9 | (((1 << 16)-1) << 46)
    for t in range(33):
        assert row[:14] == tuple((r >> i) & 1 for i in range(14))
        assert (r & ((1 << 14)-1)) == (padded & ((1 << 14)-1))
        assert row[0] == int(t % 4 < 2)
        if t >= 16:
            assert row[:14] == PATTERNS[t % 8]
        if t < 32:
            row = literal(row, t % 2, 0)[:-1]
            r = packed(r, t % 2)
            padded = packed(padded, t % 2)
    assert len(row) == 14

    # The only exterior-sensitive band update is the white phase of site 14.
    for phase, row in enumerate(PATTERNS):
        assert row[0] == int(phase % 4 < 2)
        assert row[-1] == int(phase != 4)
        for u in (0, 1):
            nxt = literal(row, phase % 2, u)
            assert (nxt == PATTERNS[(phase+1) % 8]) == (phase != 4 or u == 0)
            assert encode(nxt) == (packed(encode(row) | (u << 14), phase % 2) & 16383)

    # Exact all-state, all-input image recurrence for the existing P8 lock.
    states = set(product((0, 1), repeat=5))
    packed_states = set(range(32))
    counts = []
    for t in range(16):
        wall = int(t % 8 != 0)
        states = {literal(s, wall, u) for s in states for u in (0, 1)}
        packed_states = {packed(s | (u << 5), wall) & 31
                         for s in packed_states for u in (0, 1)}
        assert {encode(s) for s in states} == packed_states
        counts.append(len(states))
        if t == 7:
            assert any(s[0] for s in states)  # One macro is insufficient.
    assert states == LOCK_IMAGE
    assert all(s[0] == 0 for s in states)
    assert counts == [25, 20, 22, 20, 20, 18, 16, 13,
                      11, 11, 15, 17, 17, 15, 14, 10]
    print('PASS: 32-tick warmup, eight band transitions, 16-tick causal lock,')
    print('literal/packed controls, wrong-gate and one-macro countercontrols, tail check')


if __name__ == '__main__':
    main()
