#!/usr/bin/env python3
"""Independent finite counting check for SC2's second reading, not another simulation.
Prediction/claim: CLOUD-LOCAL.md at 731df08, before this script was run.
Enumerate loss subsets and unordered morning pairs for n=1..6 with exact fractions.
The morning mean requires independent draws from the replenished full drawer.
"""
from fractions import Fraction
from itertools import combinations

cases = subsets = morning_pairs = 0
for n in range(1, 7):
    universe = tuple(range(2*n))
    pairs = tuple((2*i, 2*i+1) for i in range(n))
    for k in range(2*n+1):
        total = count = 0
        for lost_tuple in combinations(universe, k):
            lost = set(lost_tuple)
            # Count partially lost pairs, independent of the surviving-sock loop.
            total += sum(len(lost.intersection(pair)) == 1 for pair in pairs)
            count += 1
        assert Fraction(total, count) == Fraction(k*(2*n-k), 2*n-1)
        cases += 1
        subsets += count
    draws = tuple(combinations(universe, 2))
    matches = sum(draw in pairs for draw in draws)
    p = Fraction(matches, len(draws))
    assert p == Fraction(1, 2*n-1)
    assert 1/p == 2*n-1  # geometric mean with independent full-drawer draws
    morning_pairs += len(draws)

# Boundary and model controls: symmetry after k versus 2n-k losses is exact;
# all interchangeable socks have a possible partner for at least two survivors.
for left in range(7):
    partnerless = sum(not any(t != s for t in range(left)) for s in range(left))
    assert partnerless == (left if left < 2 else 0)
assert 3 % 2 == 1  # one unmatched sock in a maximum simultaneous pairing

# Without replenishment, n=2: a nonmatching first pair leaves another nonmatch.
full = set(range(4))
draws = tuple(combinations(range(4), 2))
matched = {(0, 1), (2, 3)}
success = sum(d in matched or tuple(sorted(full-set(d))) in matched for d in draws)
assert Fraction(success, len(draws)) == Fraction(1, 3)
print(f'PASS: {cases} loss-count cases, {subsets} subsets, {morning_pairs} unordered morning draws')
print('Model guard: without replenishment, n=2 has only probability 1/3 of any match before empty')
print('Parity guard: 3 interchangeable socks have 0 partnerless socks but 1 simultaneously unmatched sock')
