#!/usr/bin/env python3
"""GC1277/G303: unit-preserving digit-count reduction controls.

Registered at e8f615c7 before execution. No automaton enumeration.
Record searched: digit counts/Parikh/commutative with Erd/ternary/K2/x4;
only G302's countercontrol was relevant. Bounded primary search found no
relevant result; no novelty claim. All formulas are proved by carries.
C1: 288 feasible triples a=0..6,b=1..6,c=0..6 reach ternary01 within16 steps;
every rearrangement stays canonical, ends1 and preserves the counts.
C2: literal multiplication agrees with a separate LSD carry transducer
and the proposed count formulas. Counterfactual omitted flush fails at21_3.
Unexpected: the path from19 must differ from its literal powers-of4 orbit.
c=0 requires no step. REFUTED-BY: any failed assertion; stop and retain it.
OUTCOME GC1278: all288 feasible triples pass,582 multiplications,max4 steps,
36 zero-step cases; flush omission refuted;19/550 path distinction passes.
"""

from collections import Counter
import json


def digits(n):
    out = []
    while n:
        n, d = divmod(n, 3)
        out.append(d)
    return out


def counts(word):
    c = Counter(word)
    return tuple(c[d] for d in range(3))


def value(word):
    return sum(d * 3 ** j for j, d in enumerate(word))


def carry_four(word, flush=True):
    out, carry = [], 0
    for digit in word:
        v = 4 * digit + carry
        carry, digit_out = divmod(v, 3)
        out.append(digit_out)
    if flush:
        while carry:
            carry, digit_out = divmod(carry, 3)
            out.append(digit_out)
    return out


def step_pattern(a, b, c):
    assert c > 0 and b > 0
    if b == 2 and a >= c:
        w = [1] + [0] * (a - c + 1) + [1, 2] + [0, 2] * (c - 1)
        return 'H2', w, (a + c, 4, 0)
    if b == 4 and c >= 2 and a >= c:
        w = ([1] + [0] * (a - c + 2) + [1, 2]
             + [1] * (b - 2) + [2] + [0, 2] * (c - 2))
        return 'H4', w, None  # finisher: verify absence of2 independently
    if a < c:
        w = [1] * b + [2] * (c - a) + [0, 2] * a
        return 'A', w, (2 * a + 2, 2, b + c - a - 2)
    w = [1] * b + [0] * a + [2] * c
    target = (a - 1, 2, b + 1) if c == 1 else (a, 4, b + c - 2)
    return 'B1' if c == 1 else 'B2', w, target


def reduce(a, b, c, initial=None):
    path, kinds = [], []
    n = initial
    while c:
        assert len(path) < 16
        kind, word, target = step_pattern(a, b, c)
        assert word[0] == 1 and word[-1] != 0
        assert counts(word) == (a, b, c)
        x = value(word)
        if n is not None:
            assert counts(digits(n)) == counts(word)
            assert n % 3 == 1
        y = 4 * x
        literal = digits(y)
        assert literal == carry_four(word)
        assert y % 3 == 1 and literal[-1] != 0
        actual = counts(literal)
        if target is not None:
            assert actual == target, (kind, (a, b, c), actual, target)
        if kind.startswith('H'):
            assert actual[2] == 0
        path.append((x, y))
        kinds.append(kind)
        a, b, c = actual
        n = y
    return path, kinds


def main():
    triples = skipped = total_steps = max_steps = zero_cases = 0
    types = Counter()
    for a in range(7):
        for b in range(1, 7):
            for c in range(7):
                if a > 0 and b == 1 and c == 0:
                    skipped += 1
                    continue
                path, kinds = reduce(a, b, c)
                total_steps += len(path)
                max_steps = max(max_steps, len(path))
                zero_cases += not path
                types.update(kinds)
                triples += 1
    assert (triples, skipped) == (288, 6)
    assert zero_cases == 36
    assert value(carry_four([1, 2], flush=False)) != 4 * value([1, 2])
    path, kinds = reduce(1, 1, 1, initial=19)
    assert path == [(19, 76), (76, 304), (550, 2200)]
    assert path[-1][1] != 19 * 4 ** len(path)
    assert set(digits(path[-1][1])) <= {0, 1}
    print(json.dumps(dict(feasible_triples=triples, skipped_noncanonical=skipped,
                          multiplications=total_steps, max_steps=max_steps,
                          zero_step_cases=zero_cases, gadgets=dict(types),
                          omitted_flush='REFUTED', unexpected_19_path=path,
                          verdict='ALL CONTROLS PASS')))


if __name__ == '__main__':
    main()
