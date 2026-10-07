#!/usr/bin/env python3
"""Independent second reading of PROOFS C5, not a new triangle census.

Preregistered 2026-10-07 before execution. CPU, standard library, <10 s.
P1: for each L=1..10, exhaustive predecessor blocks give exactly four
    maximal-run outputs, one continuation and three births.
C1: lookup-table Rule 30 and the literal Boolean rule agree on all triples.
C2: every output word of length 1..7 has exactly four predecessor blocks.
CF: Rule 0 must fail C2 and the birth law at L=1.
U (unexpected): on the one-cell periodic ring, uniform input is NOT
    preserved; this prevents conflating infinite iid rows with cyclic rows.
No claim about the single-cell orbit, census accuracy or temporal independence.
"""
from itertools import product
from collections import Counter


def evolve(row, rule):
    return tuple((rule >> (4*l + 2*c + r)) & 1
                 for l, c, r in zip(row, row[1:], row[2:]))


def check_uniform(rule, n):
    counts = Counter(evolve(row, rule) for row in product((0, 1), repeat=n+2))
    return len(counts) == 2**n and set(counts.values()) == {4}


def births(rule, length):
    target = (1,) + (0,)*length + (1,)
    total = continuation = 0
    for row in product((0, 1), repeat=length+4):
        if evolve(row, rule) == target:
            total += 1
            continuation += not any(row[1:-1])
    return total, continuation, total-continuation


def main():
    for l, c, r in product((0, 1), repeat=3):
        assert evolve((l, c, r), 30) == (l ^ (c | r),)
    assert all(check_uniform(30, n) for n in range(1, 8))
    for length in range(1, 11):
        result = births(30, length)
        assert result == (4, 1, 3), (length, result)
        print(f'L={length}: maximal={result[0]} continuation={result[1]} births={result[2]} denominator={2**(length+4)}')
    assert not check_uniform(0, 1)
    assert births(0, 1) != (4, 1, 3)
    ring_outputs = [evolve((bit,)*3, 30)[0] for bit in (0, 1)]
    assert ring_outputs == [0, 0]
    print('C1 C2 P1 CF U PASS; finite-block check only, no orbit census replicated')


if __name__ == '__main__':
    main()
