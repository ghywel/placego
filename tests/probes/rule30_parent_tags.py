#!/usr/bin/env python3
"""GC2351: tiny exhaustive controls for the owner's 1..8 parent labels.

Run: python3 tests/probes/rule30_parent_tags.py
32 binary windows, 512 tag triples and eight a10 completions; no solver or files.
This is a self-check, not an independent carrying read.
"""
from itertools import product


def rule(a, b, c):
    return a ^ (b | c)


def tag(a, b, c):
    return 1 + 4 * a + 2 * b + c


def bits(q):
    n = q - 1
    return n >> 2, (n >> 1) & 1, n & 1


def colour(q):
    # Independent literal Rule 30 lookup in ascending parent order.
    return (0, 1, 1, 1, 1, 0, 0, 0)[q - 1]


def compatible(p, q):
    return (p - 1) % 4 == (q - 1) // 2


def lift(qs):
    return tag(*(colour(q) for q in qs))


def first_tags(word):
    return tuple(tag(*word[i:i + 3]) for i in range(3))


for abc in product(range(2), repeat=3):
    assert bits(tag(*abc)) == abc
    assert colour(tag(*abc)) == rule(*abc)

valid = {qs for qs in product(range(1, 9), repeat=3)
         if compatible(qs[0], qs[1]) and compatible(qs[1], qs[2])}
windows = list(product(range(2), repeat=5))
assert valid == {first_tags(w) for w in windows}
assert len(valid) == 32
for w in windows:
    children = tuple(rule(*w[i:i + 3]) for i in range(3))
    assert colour(lift(first_tags(w))) == rule(*children)

for a, expected in [(0, {6, 7, 8}), (1, {2, 3, 4})]:
    rows = [first_tags((a, 1, 0, r, s)) for r, s in product(range(2), repeat=2)]
    assert {lift(qs) for qs in rows} == expected
    assert {colour(lift(qs)) for qs in rows} == {a}
    independent = product(*({qs[i] for qs in rows} for i in range(3)))
    assert {colour(lift(qs)) for qs in independent} == {0, 1}
    print(f'a={a}: exact second tags={sorted(expected)}, colour={a}; independent sets lose certainty')

zero, one = first_tags((0,) * 5), first_tags((1,) * 5)
assert (zero[1], one[1]) == (1, 8)
assert lift(zero) == lift(one) == 1
print('PASS: 8 table entries, 32/512 compatible tag triples, 32 two-step controls, 8 a10 completions')
print('PASS: 00000 and 11111 give distinct first centre tags 1/8, identical second centre tag 1')
