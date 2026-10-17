#!/usr/bin/env python3
"""MI340/B170: frozen, ONE-RUN audit of MI339's complementary staircases.

RUN-ON: Intel CPU; Python standard library. NOT RUN at registration.
COMMAND: python3 tests/probes/instinct/ss3_staircase_boundary.py
FIXED DOMAIN: equal boundary totals m=n=6..16, every h=0..floor(m*m/4)-1,
all cardinalities r>=3,m-r>=3 with h<r*(m-r). Check BOTH actual boundary
pools. Unequal controls ONLY (m,n,h)=(6,11,5),(7,10,8),(12,6,8),(16,9,19).
PREDICTION: complete combinations spectra equal independent reverse-token
bitset DP, and contain [L(r)+h,L(r)+r*(m-r)] for BOTH pools. Explicit formulas
agree with independent Ferrers row/conjugation construction and the LITERAL
reflected complement. Witnesses, bin-complement spectra and h0 full intervals
are checked. This tests formulas, not all four-bin targets or an infinite claim.
COUNTERFACTUALS: same-moment outlier pool01234,10 misses triple10; rejected
h8 guess013469 differs from the actual complement013568. Neither is repaired
away or treated as the staircase formula.
UNEXPECTED: m4,h2,r2 first pool0125 misses4, contradicting a size2 extension;
compare the entire negative spectrum independently too. No universal size2 claim.
STOPS: one invocation, first disagreement INSTRUMENT-FAILED, first agreed actual
central omission PREDICTION-REFUTED. 15 aggregate CPU seconds,25 internal wall,
128MiB peak RSS,100KiB stdout; external30s watchdog. No patch/retry,cap increase,
new domain,automatic census,raw portal upload. Source committed before execution.
"""
import hashlib
import itertools
import json
import math
import resource
import sys
import time

START_CPU = time.process_time()
START_WALL = time.monotonic()
COUNTS = {"boundaries": 0, "pools": 0, "spectra": 0,
          "literal_subsets": 0, "witnesses": 0, "central_values": 0}
DIGEST = hashlib.sha256()


class Counterexample(Exception):
    pass


def budget():
    if time.process_time() - START_CPU > 15:
        raise RuntimeError("CPU cap")
    if time.monotonic() - START_WALL > 25:
        raise RuntimeError("wall cap")
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        rss *= 1024
    if rss > 128 * 1024 * 1024:
        raise RuntimeError("RSS cap")
    return rss


def low(k):
    return k * (k - 1) // 2


def parameters(h):
    s = 0
    while (s + 1) * (s + 2) // 2 <= h:
        s += 1
    return s, h - s * (s + 1) // 2


def first_pool(m, h):
    if h == 0:
        return tuple(range(m))
    s, t = parameters(h)
    p = m - s
    return tuple(range(p)) + tuple(p + 2*j + 1 + int(j >= s-t)
                                   for j in range(s))


def second_pool(n, h):
    if h == 0:
        return tuple(range(n))
    s, t = parameters(h)
    if t == 0:
        return first_pool(n, h)
    q = n - s - 1
    return tuple(range(q)) + tuple(q + 2*j + 1 - int(j >= t)
                                   for j in range(s+1))


def ferrers_reference(m, n, h):
    # Independent integer square root, explicit rows, then column counts.
    s = (math.isqrt(8*h + 1) - 1) // 2
    t = h - s*(s+1)//2
    rows = [s-i+int(i < t) for i in range(s)]
    assert sum(rows) == h
    columns = [sum(x >= j for x in rows) for j in range(1, max(rows, default=0)+1)]
    assert sum(columns) == h
    p = tuple(i+d for i, d in enumerate([0]*(m-len(rows)) + rows[::-1]))
    q = tuple(i+d for i, d in enumerate([0]*(n-len(columns)) + columns[::-1]))
    return p, q


def dp_spectra(pool):
    bits = [1] + [0] * len(pool)
    count = 0
    for token in reversed(pool):
        count += 1
        for r in range(count, 0, -1):
            bits[r] |= bits[r-1] << token
    out = []
    for word in bits:
        values = set()
        while word:
            one = word & -word
            values.add(one.bit_length()-1)
            word -= one
        out.append(values)
    return out


def combinations_spectrum(pool, r):
    witnesses = {}
    count = 0
    for subset in itertools.combinations(pool, r):
        witnesses.setdefault(sum(subset), subset)
        count += 1
    assert count == math.comb(len(pool), r)
    COUNTS["literal_subsets"] += count
    pset = set(pool)
    for moment, witness in witnesses.items():
        assert len(witness) == len(set(witness)) == r
        assert set(witness) <= pset and sum(witness) == moment
    COUNTS["witnesses"] += len(witnesses)
    return witnesses


def check_pool(label, pool, h):
    m = len(pool)
    assert tuple(sorted(set(pool))) == pool and min(pool) >= 0
    assert sum(pool) == low(m) + h
    independent = dp_spectra(pool)
    maps = {}
    for r in range(3, m-2):
        if h >= r*(m-r):
            continue
        witnesses = combinations_spectrum(pool, r)
        actual = set(witnesses)
        assert actual == independent[r], ("whole-spectrum disagreement", label, m, h, r)
        if h == 0:
            assert actual == set(range(low(r), low(r)+r*(m-r)+1))
        missing = [z for z in range(low(r)+h, low(r)+r*(m-r)+1) if z not in actual]
        if missing:
            raise Counterexample((label, m, h, r, pool, missing))
        COUNTS["central_values"] += r*(m-r)-h+1
        COUNTS["spectra"] += 1
        maps[r] = actual
        DIGEST.update(json.dumps([label, pool, h, r, sorted(actual)], separators=(",", ":")).encode())
        budget()
    assert maps, ("empty registered pool", label, m, h)
    for r, actual in maps.items():
        assert actual == {sum(pool)-z for z in maps[m-r]}
    COUNTS["pools"] += 1


def boundary(m, n, h):
    p, q = first_pool(m, h), second_pool(n, h)
    refp, refq = ferrers_reference(m, n, h)
    assert (p, q) == (refp, refq), ("shape/formula disagreement", m, n, h)
    universe = tuple(range(m+n))
    assert len(p) == len(set(p)) == m and set(p) <= set(universe)
    complement = tuple(v for v in universe if v not in set(p))
    actual_q = tuple(sorted(m+n-1-v for v in complement))
    assert actual_q == q, ("literal complement disagreement", m, n, h, actual_q, q)
    assert len(q) == n and sum(q) == low(n)+h
    check_pool("P", p, h)
    check_pool("Q", q, h)
    COUNTS["boundaries"] += 1


def controls():
    negative = (0, 1, 2, 5)
    primary = combinations_spectrum(negative, 2)
    assert set(primary) == dp_spectra(negative)[2] == {1, 2, 3, 5, 6, 7}
    assert 4 not in primary and first_pool(4, 2) == negative
    bad = (0, 1, 2, 3, 4, 10)
    primary = combinations_spectrum(bad, 3)
    assert set(primary) == dp_spectra(bad)[3] == set(range(3, 10)) | set(range(11, 18))
    assert 10 not in primary
    assert first_pool(6, 8) == (0, 1, 2, 4, 7, 9)
    assert second_pool(6, 8) == (0, 1, 3, 5, 6, 8)
    assert second_pool(6, 8) != (0, 1, 3, 4, 6, 9)
    budget()


def main():
    controls()
    for m in range(6, 17):
        for h in range(m*m//4):
            boundary(m, m, h)
    for case in ((6, 11, 5), (7, 10, 8), (12, 6, 8), (16, 9, 19)):
        boundary(*case)
    result = {"status": "ALL CONTROLS AND FIXED PREDICTIONS PASS", **COUNTS,
              "whole_spectrum_digest": DIGEST.hexdigest(),
              "cpu_seconds": time.process_time()-START_CPU,
              "wall_seconds": time.monotonic()-START_WALL,
              "peak_rss_bytes": budget(), "runs": 1,
              "scope": "finite formula/spectrum audit only; hand theorem and novelty unverified"}
    report = json.dumps(result, sort_keys=True)
    assert len(report.encode()) <= 100*1024
    print(report)


if __name__ == "__main__":
    try:
        main()
    except Counterexample as exc:
        print(json.dumps({"status": "PREDICTION-REFUTED", "detail": str(exc), "counts": COUNTS}), flush=True)
        sys.exit(2)
    except (AssertionError, RuntimeError) as exc:
        print(json.dumps({"status": "INSTRUMENT-FAILED", "detail": str(exc), "counts": COUNTS}), flush=True)
        sys.exit(3)
