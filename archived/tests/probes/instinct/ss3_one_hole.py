#!/usr/bin/env python3
r"""MI331/B162 preregistration: exact spectra versus three-bin compatibility.

NOT RUN at registration. This is a new one-hole question, NOT a repair or
retry of MI327, an extension of MI319/323, or a universal SS3 experiment.
RUN-ON: Intel CPU, Python standard library.
COMMAND: python3 tests/probes/instinct/ss3_one_hole.py

Fixed domains: P={0,...,M}\{q}, all q=0,...,M, sizes (3,3,3) at M=9
and (3,3,4) at M=10. No larger domain or second invocation authorized by
this registration. Exact rank bounds alone already fail at q=3,M=9,
targets (4,18,20), since no triple of sum4 omits3.

PREDICTION: if every individual requested sum is attained by a subset of
the required size AND all rank bounds hold, the three bins can be realized
simultaneously throughout these two fixed domains. A pass is finite evidence
only; arbitrary sizes/holes remain OPEN. A counterexample ends this route.
COUNTERFACTUAL: rank-only (4,18,20) above is accepted by rank bounds but
rejected by the singleton-spectrum filter and by actual partitions.
INDEPENDENT: combinations/complements versus token-by-token owner recursion,
whole sum-vector sets and multinomial counts; every retained witness checked
literally for disjointness, exact pool coverage, sizes and sums. Endpoint holes
are full intervals, so verified MI295 predicts rank-only completeness there.
UNEXPECTED: sizes2 on P={0,1,2,3,4,6}, targets(2,6,8), obey every rank bound
and individual spectrum condition but have no partition. Thus the new filter
must NOT accidentally claim a theorem without the minimum-size hypothesis.
REFLECTION: q -> M-q, s_i -> M*c_i-s_i, preserving bin labels.
STOP: ONE invocation; first failed control stops as INSTRUMENT-FAILED; first
counterexample to the prediction stops the question as REFUTED. 3 aggregate
process CPU seconds, 5 wall seconds, 64MiB peak RSS, 100KiB output, external
10s watchdog. No patch/retry, automatic larger n or cap increase. Local output
only; no raw portal upload. No experiment has run merely by saving this file.

OUTCOME MI332/B163: ONE unchanged-source run completes21 domains.
8229 rank-and-singleton-spectrum vectors all realized (3184 at333,
5045 at334);8373 rank-only vectors,144 excluded by spectra. Whole
independent maps/counts/literals/reflections/endpoints and both negative
controls PASS.0.447717CPU,0.451051311wall,15,597,568B peakRSS,2087B
stdout,empty stderr,exit0. Finite only;general criterion OPEN. No retry
or larger domain. Original source hash and raw receipt in MI332.

"""

import itertools
import json
import math
import resource
import sys
import time

START_CPU = time.process_time()
START_WALL = time.monotonic()


def budget():
    assert time.process_time() - START_CPU <= 3, "CPU cap"
    assert time.monotonic() - START_WALL <= 5, "wall cap"
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        peak *= 1024
    assert peak <= 64 * 1024 * 1024, "RSS cap"


def combinations_map(pool, sizes):
    witnesses = {}
    count = 0
    for a in itertools.combinations(pool, sizes[0]):
        remainder = tuple(x for x in pool if x not in a)
        for b in itertools.combinations(remainder, sizes[1]):
            c = tuple(x for x in remainder if x not in b)
            bins = (a, b, c)
            sums = tuple(map(sum, bins))
            # Check EVERY generated partition, not only one witness per sum.
            assert tuple(map(len, bins)) == sizes
            assert len(set(a) | set(b) | set(c)) == len(pool)
            assert sorted(a + b + c) == list(pool)
            witnesses.setdefault(sums, bins)
            count += 1
        budget()
    return witnesses, count


def owner_map(pool, sizes):
    """Independent enumeration: choose each token's owner, not bin subsets."""
    reachable = set()
    count = 0
    remaining = list(sizes)
    sums = [0, 0, 0]

    def visit(at):
        nonlocal count
        if at == len(pool):
            assert remaining == [0, 0, 0]
            reachable.add(tuple(sums))
            count += 1
            return
        value = pool[at]
        for owner in range(3):
            if remaining[owner]:
                remaining[owner] -= 1
                sums[owner] += value
                visit(at + 1)
                sums[owner] -= value
                remaining[owner] += 1

    visit(0)
    budget()
    return reachable, count


def spectra(pool, sizes):
    return tuple({sum(t) for t in itertools.combinations(pool, c)} for c in sizes)


def rank_ok(pool, sizes, sums):
    if sum(sums) != sum(pool):
        return False
    # All six proper subsets, not just singletons. Explicitly avoid relying
    # on the three-bin complement simplification in this checker.
    for mask in range(1, 7):
        c = sum(sizes[i] for i in range(3) if mask & (1 << i))
        s = sum(sums[i] for i in range(3) if mask & (1 << i))
        if not sum(pool[:c]) <= s <= sum(pool[-c:]):
            return False
    return True


def candidates(pool, sizes):
    total = sum(pool)
    bounds = [(sum(pool[:c]), sum(pool[-c:])) for c in sizes]
    for a in range(bounds[0][0], bounds[0][1] + 1):
        for b in range(bounds[1][0], bounds[1][1] + 1):
            s = (a, b, total - a - b)
            if rank_ok(pool, sizes, s):
                yield s


def run():
    maps = {}
    rows = []
    for sizes in ((3, 3, 3), (3, 3, 4)):
        m = sum(sizes)
        for hole in range(m + 1):
            pool = tuple(x for x in range(m + 1) if x != hole)
            witnesses, count = combinations_map(pool, sizes)
            independent, independent_count = owner_map(pool, sizes)
            expected = math.factorial(m) // math.prod(math.factorial(c) for c in sizes)
            assert count == independent_count == expected
            assert set(witnesses) == independent
            maps[sizes, hole] = (pool, witnesses)
    for (sizes, hole), (pool, witnesses) in maps.items():
        m = sum(sizes)
        reflected = maps[sizes, m - hole][1]
        assert {tuple(m*c-s for c, s in zip(sizes, t)) for t in witnesses} == set(reflected)
        if hole in (0, m):
            assert set(candidates(pool, sizes)) == set(witnesses)
        budget()

    pool, witnesses = maps[(3, 3, 3), 3]
    control = (4, 18, 20)
    assert rank_ok(pool, (3, 3, 3), control)
    assert 4 not in spectra(pool, (3, 3, 3))[0]
    assert control not in witnesses
    small_pool = (0, 1, 2, 3, 4, 6)
    small_sizes, small_target = (2, 2, 2), (2, 6, 8)
    small_map, small_count = combinations_map(small_pool, small_sizes)
    small_ref, small_ref_count = owner_map(small_pool, small_sizes)
    assert set(small_map) == small_ref and small_count == small_ref_count == 90
    assert rank_ok(small_pool, small_sizes, small_target)
    assert all(t in sp for t, sp in zip(small_target, spectra(small_pool, small_sizes)))
    assert small_target not in small_map

    for (sizes, hole), (pool, witnesses) in maps.items():
        sp = spectra(pool, sizes)
        rank_count = eligible = 0
        for target in candidates(pool, sizes):
            rank_count += 1
            if not all(t in s for t, s in zip(target, sp)):
                continue
            eligible += 1
            if target not in witnesses:
                return {"status": "REFUTED", "sizes": sizes, "hole": hole,
                        "target": target, "pool": pool,
                        "controls": "all passed", "completed_domains": rows}
            bins = witnesses[target]
            assert tuple(map(sum, bins)) == target
            assert tuple(map(len, bins)) == sizes
            assert sorted(sum(bins, ())) == list(pool)
        rows.append({"sizes": sizes, "hole": hole, "rank": rank_count,
                     "singleton_feasible": eligible, "realized": len(witnesses)})
        assert eligible == len(witnesses)
        budget()
    return {"status": "FINITE-PASS", "controls": "all passed", "domains": rows,
            "universal_statement": "OPEN"}


if __name__ == "__main__":
    result = run()
    budget()
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result.update(cpu_seconds=time.process_time() - START_CPU,
                  wall_seconds=time.monotonic() - START_WALL,
                  peak_rss_bytes=peak if sys.platform == "darwin" else peak * 1024)
    output = json.dumps(result, sort_keys=True)
    assert len(output.encode()) <= 100 * 1024
    print(output)
