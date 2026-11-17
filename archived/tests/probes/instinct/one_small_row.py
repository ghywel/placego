#!/usr/bin/env python3
"""B236 / MI451: one fixed full-interval row diagnostic. Predictions in notebook.
Cases: (2,3,3,3), N11; negative control (2,2,2,2), N8. No expansion.
Independent whole maps: bin-combinations versus token-owner recursion.
Stop per case: 2,000,000 recursion nodes / 20 seconds. Raw output outside git.
"""
import itertools, json, math, time


def case(counts):
    n = sum(counts)
    start = time.monotonic()
    universe = tuple(range(n))
    primary = set()
    leaves = 0
    for a in itertools.combinations(universe, counts[0]):
        ra = tuple(x for x in universe if x not in a)
        for b in itertools.combinations(ra, counts[1]):
            rb = tuple(x for x in ra if x not in b)
            for c in itertools.combinations(rb, counts[2]):
                d = tuple(x for x in rb if x not in c)
                assert len(d) == counts[3]
                assert sorted(a+b+c+d) == list(universe)
                primary.add(tuple(map(sum, (a,b,c,d))))
                leaves += 1
        assert time.monotonic()-start < 20, 'primary time cap'
    expected = math.factorial(n)//math.prod(math.factorial(c) for c in counts)
    assert leaves == expected
    independent = set()
    rem = list(counts)
    sums = [0]*4
    nodes = 0
    independent_leaves = 0
    def owner(x):
        nonlocal nodes, independent_leaves
        nodes += 1
        assert nodes <= 2000000, 'node cap'
        if nodes % 10000 == 0:
            assert time.monotonic()-start < 20, 'owner time cap'
        if x == n:
            assert rem == [0]*4
            independent.add(tuple(sums))
            independent_leaves += 1
            return
        for j in range(4):
            if rem[j]:
                rem[j] -= 1
                sums[j] += x
                owner(x+1)
                sums[j] -= x
                rem[j] += 1
    owner(0)
    assert independent_leaves == expected
    assert independent == primary, 'independent map mismatch'
    groups = [tuple(j for j in range(4) if mask>>j & 1) for mask in range(1,15)]
    def rank(v):
        for g in groups:
            r = sum(counts[j] for j in g)
            val = sum(v[j] for j in g)
            if not r*(r-1)//2 <= val <= r*(2*n-r-1)//2:
                return False
        return True
    ranges = [range(c*(c-1)//2,c*(2*n-c-1)//2+1) for c in counts]
    admitted = set()
    for v3 in itertools.product(*ranges[:3]):
        v = v3+(n*(n-1)//2-sum(v3),)
        if v[3] in ranges[3] and rank(v): admitted.add(v)
    assert primary <= admitted
    reflect = lambda v: tuple(c*(n-1)-x for c,x in zip(counts,v))
    assert {reflect(v) for v in primary} == primary
    assert {reflect(v) for v in admitted} == admitted
    assert time.monotonic()-start < 20, 'total time cap'
    missing = sorted(admitted-primary)
    if counts == (2,3,3,3):
        assert (1,9,18,27) in primary
    else:
        assert (4,4,10,10) in admitted and (4,4,10,10) not in primary
    return dict(counts=counts, partitions=leaves, owner_nodes=nodes,
                attained=len(primary), admitted=len(admitted), missing=len(missing),
                first_missing=missing[:5], seconds=time.monotonic()-start,
                controls='complete map, multinomial, literal coverage, full reflection PASS')

if __name__ == '__main__':
    for c in ((2,2,2,2),(2,3,3,3)):
        print(json.dumps(case(c),sort_keys=True),flush=True)
