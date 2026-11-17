#!/usr/bin/env python3
"""G52 preregistered MF1-MF2: phase conversion, not infinite-orbit simulation."""
from itertools import product


def primitive(word):
    p = len(word)
    return all(any(word[i] != word[i % d] for i in range(p))
               for d in range(1, p) if p % d == 0)


def inverse(current, following, right):
    return following ^ (current | right)


def forward(left, centre, right):
    return (30 >> (4 * left + 2 * centre + right)) & 1


def controls():
    walls, samples, transitions = 0, 0, 0
    for p in range(2, 6):
        for wall in product((0, 1), repeat=p):
            if not primitive(wall):
                continue
            walls += 1
            whites = [j for j, b in enumerate(wall) if b == 0]
            for vector in product((0, 1), repeat=len(whites)):
                index = {phase: k for k, phase in enumerate(whites)}
                pairs = [[], []]
                for copy in (0, 1):
                    for t in range(3 * p):
                        phase, block = t % p, t // p
                        centre = wall[phase]
                        following = wall[(phase + 1) % p]
                        # Starts 0 and 4p align; change every invisible bit.
                        right = copy if centre else vector[index[phase]] ^ (block % 2)
                        left = inverse(centre, following, right)
                        assert forward(left, centre, right) == following
                        pairs[copy].append((left, centre))
                        transitions += 1
                assert pairs[0] == pairs[1]
                samples += 1
    # MF2: matching ungrouped visible futures need not align wall phases.
    wall = (0, 0, 1)
    neighbours = tuple(inverse(wall[t], wall[(t + 1) % 3], 0) for t in range(3))
    assert neighbours == (0, 1, 1)
    assert wall[0] == wall[1] == 0 and neighbours[0] != neighbours[1]
    print('MF1 PASS: primitive walls/samples/forward transitions:', walls, samples, transitions)
    print('MF2 PASS: wall001 misaligned white phases have neighbours0 and1.')
    print('Finite boundary conversion only; G52 band argument requires independent reading.')


if __name__ == '__main__':
    controls()
