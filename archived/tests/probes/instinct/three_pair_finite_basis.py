#!/usr/bin/env python3
"""MI547: ONE fixed-basis check for full-interval counts (2,2,2,c).

Predictions/domain/controls/caps are preregistered in GPT-MATH-INSTINCT.md MI547.
Main: M=8..16, endpoint target bands, ALL original rank cuts; low basis 1..8.
Blind: only (2,6,8) and its reflection fail. Stop on a new miss or mismatch.
Independent engines: target-edge selection / six-token-first perfect pairings.
Can-fail: token reuse falsely admits 2/6/8. Old negatives and two-hole AP hole.
Caps: 60 wall / 30 CPU seconds; 1M secondary leaves; 10K candidate triples.
No expanded run, random sample, external libraries, network or data in git.
"""
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import time


WALL = time.monotonic()
CPU = time.process_time()
LEAVES = 0
QUERIES = 0
CANDIDATES = 0
CACHE = {}


def cap():
    assert time.monotonic() - WALL < 60, 'wall cap'
    assert time.process_time() - CPU < 30, 'CPU cap'
    assert LEAVES <= 1_000_000, 'secondary terminal cap'
    assert QUERIES <= 10_000, 'candidate cap'
    assert CANDIDATES <= 10_000, 'all candidate cap'


def primary(pool, targets):
    """Three labelled target edge lists; literal vertex-disjoint selection."""
    edges = [[(x, y) for x, y in it.combinations(pool, 2) if x+y == s]
             for s in targets]
    for a in edges[0]:
        for b in edges[1]:
            if set(a).intersection(b):
                continue
            used = set(a+b)
            for c in edges[2]:
                if not used.intersection(c):
                    return (a, b, c)
    return None


def secondary(pool):
    """No target lists: choose six tokens and all 15 perfect pairings."""
    global LEAVES
    pool = tuple(pool)
    if pool in CACHE:
        return CACHE[pool]
    support = {}
    terminals = 0
    for six in it.combinations(pool, 6):
        x = six[0]
        for j in range(1, 6):
            four = six[1:j] + six[j+1:]
            y = four[0]
            for k in range(1, 4):
                last = four[1:k] + four[k+1:]
                pairs = ((x, six[j]), (y, four[k]), last)
                target = tuple(sorted(sum(pair) for pair in pairs))
                if target not in support:
                    support[target] = tuple(sorted(pairs, key=lambda p: (sum(p), p)))
                terminals += 1
                LEAVES += 1
        if terminals % 1500 == 0:
            cap()
    assert terminals == 15*math.comb(len(pool), 6), 'secondary complete count'
    cap()
    CACHE[pool] = (support, terminals)
    return CACHE[pool]


def literal(pool, targets, witness):
    assert len(witness) == 3
    assert all(len(pair) == 2 for pair in witness)
    tokens = tuple(x for pair in witness for x in pair)
    assert len(set(tokens)) == 6 and set(tokens) <= set(pool)
    assert tuple(map(sum, witness)) == targets
    filler = tuple(x for x in pool if x not in tokens)
    assert len(filler) == len(pool)-6
    assert sum(filler) == sum(pool)-sum(targets)


def query(pool, targets, actual):
    global QUERIES
    QUERIES += 1
    cap()
    got = primary(pool, targets)
    want = actual.get(targets)
    assert (got is None) == (want is None), ('oracle mismatch', pool, targets)
    if got is not None:
        literal(pool, targets, got)
        literal(pool, targets, want)
    return got is not None


def original_rank(m, target):
    counts = (2, 2, 2, m-5)
    values = target + (m*(m+1)//2-sum(target),)
    for mask in range(1, 15):
        r = sum(counts[j] for j in range(4) if mask >> j & 1)
        value = sum(values[j] for j in range(4) if mask >> j & 1)
        if not r*(r-1)//2 <= value <= r*(2*(m+1)-r-1)//2:
            return False
    return True


def pair_rank(m, target):
    """Independent cut reduction: equal-size pair groups and complements."""
    for j in (1, 2, 3):
        r = 2*j
        if sum(target[:j]) < r*(r-1)//2:
            return False
        if sum(target[-j:]) > r*(2*m+1-r)//2:
            return False
    return True


def controls():
    rows = []
    for m, targets, expected in (
            (7, (2, 6, 8), False), (7, (4, 4, 10), False),
            (7, (4, 4, 9), True), (9, (1, 5, 9), True),
            (9, (9, 9, 9), True)):
        pool = tuple(range(m+1))
        actual, _ = secondary(pool)
        assert original_rank(m, targets), ('control rank', m, targets)
        assert query(pool, targets, actual) == expected
        rows.append([m, targets, expected])
    # A genuinely weaker method accepts the old forced negative by reuse.
    reuse = ((0, 2), (0, 6), (0, 8))
    assert tuple(map(sum, reuse)) == (2, 6, 8)
    try:
        literal(tuple(range(9)), (2, 6, 8), reuse)
    except AssertionError:
        pass
    else:
        raise AssertionError('can-fail reuse witness escaped the literal checker')
    for pool, expected in (((0, 2, 3, 4, 5, 6, 8), False),
                           ((1, 2, 3, 4, 5, 6, 8), True)):
        actual, _ = secondary(pool)
        assert query(pool, (8, 9, 10), actual) == expected
        rows.append([pool, (8, 9, 10), expected])
    return rows


def main():
    global CANDIDATES
    out = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'controls': controls(), 'intervals': [], 'low_basis': None}
    for m in range(8, 17):
        pool = tuple(range(m+1))
        actual, terminals = secondary(pool)
        reflect = lambda t: tuple(sorted(2*m-u for u in t))
        assert {reflect(t) for t in actual} == set(actual), 'full support reflection'
        assert all(original_rank(m, t) for t in actual), 'actual support outside cuts'
        bands = sorted(set(range(1, 9)) | set(range(2*m-8, 2*m)))
        candidates = list(it.combinations_with_replacement(bands, 3))
        eligible = []
        missing = []
        expected = {(2, 6, 8), reflect((2, 6, 8))}
        for target in candidates:
            CANDIDATES += 1
            cap()
            assert original_rank(m, target) == pair_rank(m, target), 'rank mismatch'
            if not original_rank(m, target):
                continue
            eligible.append(target)
            if not query(pool, target, actual):
                missing.append(target)
                if target not in expected:
                    out.update(status='BLIND-REFUTED-FIRST-NEW-MISS',
                               first_new_miss={'M': m, 'target': target},
                               secondary_leaves=LEAVES, queried=QUERIES)
                    print(json.dumps(out, sort_keys=True))
                    return
        assert set(missing) == expected, 'predicted obstruction absent'
        assert {reflect(t) for t in eligible} == set(eligible), 'rank domain reflection'
        out['intervals'].append(dict(M=m, candidates=len(candidates),
                                    eligible=len(eligible), missing=missing,
                                    secondary_support=len(actual),
                                    secondary_terminal_matchings=terminals))
    pool = tuple(range(9))
    actual, _ = secondary(pool)
    low = [t for t in it.combinations_with_replacement(range(1, 9), 3)
           if t[0]+t[1] >= 6 and sum(t) >= 15]
    missing = []
    for target in low:
        CANDIDATES += 1
        cap()
        assert original_rank(8, target), 'low basis reference cuts'
        if not query(pool, target, actual):
            missing.append(target)
            if target != (2, 6, 8):
                out.update(status='BLIND-REFUTED-FIRST-NEW-LOW-MISS', target=target)
                print(json.dumps(out, sort_keys=True))
                return
    assert missing == [(2, 6, 8)]
    out.update(status='COMPLETE', low_basis={'eligible': len(low), 'missing': missing},
               secondary_leaves=LEAVES, queried=QUERIES,
               candidate_triples=CANDIDATES,
               cpu_seconds=time.process_time()-CPU, wall_seconds=time.monotonic()-WALL)
    cap()
    print(json.dumps(out, sort_keys=True))


if __name__ == '__main__':
    main()
