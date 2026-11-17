#!/usr/bin/env python3
"""MI495: one first-gap test of ALL-pair H2 support, old counts233/234 only.

PREDICTIONS (written before first run): for internal q and 3<=u<=2M-1-q,
the union of b-subset spectra after EVERY legal sum-u pair deletion is an
integer interval. Blind stronger assertion, not an assumed H2 lemma.
Independent direct subsets, F-H coefficients, and pair-deletion spectra agree.
COUNTERFACTUAL: M8,q5,u1 has an interior triple gap10; outside H2 range.
UNEXPECTED: entire physical-reflection coefficient vector; midpoint deletion;
distinct good subsets versus pair-incidence multiplicities.
STOP: first gap or20s/500 domains. No retry, repair or domain expansion.
REFUTED-BY: any admitted domain with an internal support gap.
Raw JSONL outside git; no infinite theorem follows from a pass.

OUTCOME (2026-10-20, MI496): controls PASS; FIRST GAP at domain18,
M8,q2,u8,counts233,gap6. Complete union {5}+[7,19]+{21}; gap6 is NOT
H2-protected. Remaining domains NOT run. 0.013039325014688075 seconds.
No retry or larger run. This outcome paragraph was appended after execution.
"""
from collections import Counter
from itertools import combinations
import json
import time


def edges(pool, u):
    return tuple(a for a in combinations(pool, 2) if sum(a) == u)


def product(factors, size):
    """Exact truncated bivariate polynomial, keys (cardinality, sum)."""
    out = {(0, 0): 1}
    for factor in factors:
        nxt = Counter()
        for (k, v), count in out.items():
            for dk, dv in factor:
                if k + dk <= size:
                    nxt[k + dk, v + dv] += count
        out = nxt
    return Counter({v: n for (k, v), n in out.items() if k == size})


def audit(pool, u, size):
    ee = edges(pool, u)
    direct = Counter()
    witnesses = {}
    for b in combinations(pool, size):
        bs = set(b)
        if any(bs.isdisjoint(a) for a in ee):
            direct[sum(b)] += 1
            witnesses.setdefault(sum(b), b)
    all_counts = product([((0, 0), (1, x)) for x in pool], size)
    paired = {x for a in ee for x in a}
    factors = [((1, a), (1, b), (2, u)) for a, b in ee]
    factors += [((0, 0), (1, x)) for x in pool if x not in paired]
    hit_counts = product(factors, size)
    difference = {v: all_counts[v] - hit_counts[v]
                  for v in set(all_counts) | set(hit_counts)}
    assert all(n >= 0 for n in difference.values())
    assert {v: n for v, n in difference.items() if n} == dict(direct)
    per_pair = {}
    for a in ee:
        remainder = tuple(x for x in pool if x not in a)
        per_pair[a] = sorted({sum(b) for b in combinations(remainder, size)})
    union = {v for spectrum in per_pair.values() for v in spectrum}
    assert union == set(direct)
    return direct, per_pair, witnesses


def physical_reflection(pool, u, size, counts):
    m = max(pool)
    reflected_pool = tuple(sorted(m-x for x in pool))
    other, _, _ = audit(reflected_pool, 2*m-u, size)
    assert dict(other) == {size*m-v: n for v, n in counts.items()}


def protected(m, q, u, v, b, c):
    targets = (u, v, m*(m+1)//2-q-u-v)
    counts = (2, b, c)
    return all(sum(targets[i] for i in range(3) if mask >> i & 1) >=
               (r := sum(counts[i] for i in range(3) if mask >> i & 1))
               * (r+1)//2 for mask in range(1, 7))


def emit(value):
    print(json.dumps(value), flush=True)


def main():
    start = time.monotonic()
    pool = tuple(x for x in range(9) if x != 3)
    counts, per_pair, _ = audit(pool, 8, 3)
    assert 7 in counts and 7 not in per_pair[(2, 6)]
    pool = tuple(x for x in range(9) if x != 5)
    counts, per_pair, _ = audit(pool, 1, 3)
    assert min(counts) == 9 and max(counts) == 21 and 10 not in counts
    physical_reflection(pool, 1, 3, counts)
    pool = tuple(x for x in range(9) if x != 4)
    assert len(edges(pool, 8)) == 4
    pool = tuple(x for x in range(9) if x != 1)
    ee = edges(pool, 8)
    assert sum(set((0, 4, 7)).isdisjoint(a) for a in ee) == 2
    counts, _, _ = audit(pool, 8, 3)
    incidence = sum(sum(b) == 11 for a in ee
                    for b in combinations(tuple(x for x in pool if x not in a), 3))
    assert incidence > counts[11]
    emit({'controls': 'PASS', 'negative_gap': 10,
          'distinct_B_at_11': counts[11], 'pair_incidence_at_11': incidence})
    domains = coefficients = protected_targets = 0
    for b, c in ((3, 3), (3, 4)):
        m = 2+b+c
        for q in range(1, m):
            pool = tuple(x for x in range(m+1) if x != q)
            for u in range(3, 2*m-q):
                assert domains < 500 and time.monotonic()-start < 20, 'CAP'
                counts, per_pair, witnesses = audit(pool, u, b)
                physical_reflection(pool, u, b, counts)
                domains += 1
                coefficients += len(counts)
                assert counts, 'empty union in claimed domain'
                gaps = [v for v in range(min(counts), max(counts)+1) if v not in counts]
                if gaps:
                    v = gaps[0]
                    emit({'result': 'FIRST GAP', 'M': m, 'q': q, 'u': u,
                          'counts': [2, b, c], 'gap': v,
                          'protected': protected(m, q, u, v, b, c),
                          'per_pair': [{'pair': a, 'support': ss}
                                       for a, ss in per_pair.items()],
                          'union_support': sorted(counts),
                          'neighbour_witnesses': {str(w): witnesses[w]
                              for w in (v-1, v+1) if w in witnesses},
                          'domains': domains, 'seconds': time.monotonic()-start})
                    return
                total = sum(pool)
                for v in range(total+1):
                    if protected(m, q, u, v, b, c):
                        protected_targets += 1
                        assert v in counts, 'H2 failure'
    emit({'result': 'FIXED DOMAIN PASS', 'domains': domains,
          'support_coefficients': coefficients,
          'protected_targets': protected_targets,
          'seconds': time.monotonic()-start})


if __name__ == '__main__':
    main()
