#!/usr/bin/env python3
"""MI306/B146 preregistration: audit MI305, not an SS3 existence census.

ONE run after source/predictions push. h=1..3, m=2h+2..14, every h-of-2h
window, every r=h+1..m-h-1: 216 pools, 962 complete spectra. Independent
bitset DP versus literal combinations; literal j-bands audit the join bound.
All 6 h2,m6 selections construct 874 partitions on an independently generated
730-target n12 domain. Three fixed witnesses, signed translations, the old
slack3 failure, invalid-cardinality counterfactual and 3 touching controls.
Predict all asserted comparisons pass; never infer the infinite theorem from
this finite audit. Stop first assertion/cap: 10CPU/20wall/128MiB/2M literal
subsets/2MiB report, external 25wall watchdog. No retry, repair, or expansion.
Raw report outside git; only an outcome header may be added after the run.
"""

import argparse
import hashlib
import itertools
import json
import resource
import time
from pathlib import Path


START_CPU = time.process_time()
START_WALL = time.monotonic()
LITERAL_SUBSETS = 0


def limits():
    assert time.process_time() - START_CPU < 10, "CPU cap"
    assert time.monotonic() - START_WALL < 20, "wall cap"
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 128 * 1024**2, "RSS cap (macOS bytes)"
    assert LITERAL_SUBSETS <= 2_000_000, "literal-subset cap"


def low(r):
    return r * (r - 1) // 2


def high(n, r):
    return r * (2 * n - r - 1) // 2


def dp(values, r):
    """Exact cardinality bitsets; normalize signed inputs before shifting."""
    assert len(values) == len(set(values))
    offset = min(values)
    bits = [1] + [0] * r
    for seen, v in enumerate(values):
        for k in range(min(r, seen + 1), 0, -1):
            bits[k] |= bits[k - 1] << (v - offset)
    return {s + r * offset for s in range(bits[r].bit_length()) if (bits[r] >> s) & 1}


def literal(values, r, upper=()):
    """Whole sum-to-witness map and j-bands, with no interval formulas."""
    global LITERAL_SUBSETS
    up = frozenset(upper)
    witnesses, bands = {}, {}
    for chosen in itertools.combinations(values, r):
        LITERAL_SUBSETS += 1
        s = sum(chosen)
        witnesses.setdefault(s, chosen)
        j = sum(v in up for v in chosen)
        bands.setdefault(j, set()).add(s)
    limits()
    return witnesses, bands


def digest(value):
    return hashlib.sha256(json.dumps(value, separators=(",", ":"), sort_keys=True).encode()).hexdigest()


def check_partition(bins, sizes, targets):
    n = sum(sizes)
    assert tuple(map(len, bins)) == tuple(sizes)
    assert tuple(map(sum, bins)) == tuple(targets)
    # Independent coverage: sort actual original tokens, no index-mask allocator.
    assert sorted(v for bucket in bins for v in bucket) == list(range(n))


def audit(report_path):
    spectra, pool_rows, cache = [], [], {}
    touching = []
    for h in (1, 2, 3):
        for m in range(2 * h + 2, 15):
            ell = m - h
            for offsets in itertools.combinations(range(2 * h), h):
                upper = tuple(ell + x for x in offsets)
                pool = tuple(range(ell)) + upper
                delta = sum(pool) - low(m)
                assert 0 <= delta <= h * h
                reflected = tuple(sorted(2 * m - 1 - x for x in range(2 * m) if x not in pool))
                assert reflected[:ell] == tuple(range(ell))
                assert len(reflected[ell:]) == h
                assert all(ell <= x < ell + 2 * h for x in reflected[ell:])
                assert sum(reflected) == sum(pool)
                pool_rows.append(dict(h=h, m=m, upper=upper, delta=delta, reflected=reflected))
                for r in range(h + 1, m - h):
                    q = m - r
                    witnesses, bands = literal(pool, r, upper)
                    direct = set(witnesses)
                    dynamic = dp(tuple(reversed(pool)), r)
                    expected = set(range(low(r), sum(pool) - low(q) + 1))
                    assert direct == dynamic == expected
                    assert set(bands) == set(range(h + 1))
                    joins = []
                    for j in range(h + 1):
                        b = bands[j]
                        assert b == set(range(min(b), max(b) + 1))
                        if j < h:
                            actual = max(b) + 1 - min(bands[j + 1])
                            f = r * (q - h) - q + j * (r - q + 2 * h - 2) - 2 * j * j
                            expression = (r - j) * (ell - (r - j) + 1) + sum(upper[h - j:]) - sum(upper[:j + 1])
                            assert actual == expression and actual >= f >= 0
                            joins.append(actual)
                    alpha, beta = r - h - 1, q - h - 1
                    f0 = r * (q - h) - q
                    fh = f0 + (h - 1) * (r - q + 2 * h - 2) - 2 * (h - 1)**2
                    assert f0 == alpha + h * beta + alpha * beta
                    assert fh == h * alpha + beta + alpha * beta
                    if m == 2 * h + 2 and upper == tuple(range(ell + h, ell + 2 * h)):
                        assert r == h + 1 and joins[0] == joins[-1] == 0
                        touching.append((h, m, r))
                    cache[h, m, upper, r] = witnesses
                    spectra.append(dict(h=h, m=m, r=r, upper=upper, sums=sorted(direct), joins=joins))
                    limits()
    assert len(pool_rows) == 216 and len(spectra) == 962
    assert touching == [(1, 4, 2), (2, 6, 3), (3, 8, 4)]

    # Domain generation is independent of the window/subset instruments.
    domain = set()
    for a, b, c in itertools.product(range(3, 31), repeat=3):
        d = 66 - a - b - c
        if 3 <= d <= 30 and 0 <= a + b - 15 <= 4:
            domain.add((a, b, c, d))
    assert len(domain) == 730
    certificates, covered = [], set()
    for offsets in itertools.combinations(range(4), 2):
        upper = tuple(4 + x for x in offsets)
        pool = tuple(range(4)) + upper
        reflected = tuple(sorted(11 - x for x in range(12) if x not in pool))
        left_map = cache[2, 6, upper, 3]
        right_map = cache[2, 6, reflected[4:], 3]
        delta = sum(pool) - 15
        for targets in sorted(domain):
            a, b, c, d = targets
            if a + b != 15 + delta:
                continue
            aa = left_map[a]
            bb = tuple(x for x in pool if x not in aa)
            reflected_c = right_map[33 - c]
            cc = tuple(sorted(11 - x for x in reflected_c))
            dd = tuple(x for x in range(12) if x not in pool and x not in cc)
            bins = (aa, bb, cc, dd)
            check_partition(bins, (3, 3, 3, 3), targets)
            certificates.append(dict(upper=upper, targets=targets, bins=bins))
            covered.add(targets)
    assert len(certificates) == 874 and covered == domain

    controls = []
    for values, r in [((0, 1, 2, 5, 6), 2), ((0, 1, 2, 4, 5, 6), 3), ((0, 1, 2, 4), 2)]:
        w, _ = literal(values, r)
        assert set(w) == dp(values, r)
        moved = tuple(v - 11 for v in values)
        shifted, _ = literal(moved, r)
        assert set(shifted) == dp(moved, r) == {s - 11 * r for s in w}
        controls.append(dict(values=values, r=r, sums=sorted(w), shifted=sorted(shifted)))
    assert 4 not in controls[0]['sums'] and 1 in controls[0]['sums'] and 11 in controls[0]['sums']
    assert 4 not in controls[1]['sums']  # Old canonical slack3 complement really fails.

    fixtures = [
        ((3, 3, 3, 3), (3, 15, 19, 29), ((0, 1, 2), (3, 5, 7), (4, 6, 9), (8, 10, 11))),
        ((3, 3, 3, 3), (8, 11, 25, 22), ((0, 1, 7), (2, 3, 6), (4, 10, 11), (5, 8, 9))),
        ((4, 5, 4, 5), (14, 29, 46, 64), ((0, 1, 2, 11), (3, 4, 5, 8, 9), (6, 7, 16, 17), (10, 12, 13, 14, 15))),
    ]
    for sizes, targets, bins in fixtures:
        check_partition(bins, sizes, targets)
    limits()
    report = dict(status='PASS', pools=pool_rows, spectra=spectra, touching=touching,
                  target_domain=sorted(domain), certificates=certificates, controls=controls,
                  fixtures=fixtures, literal_subsets=LITERAL_SUBSETS,
                  cpu_seconds=time.process_time() - START_CPU,
                  wall_seconds=time.monotonic() - START_WALL,
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    encoded = json.dumps(report, sort_keys=True, separators=(",", ":")).encode()
    assert len(encoded) <= 2 * 1024**2, 'report cap'
    assert not report_path.exists(), 'report must be new'
    report_path.write_bytes(encoded)
    print(json.dumps(dict(status='PASS', pools=len(pool_rows), spectra=len(spectra),
                          target_vectors=len(domain), certificates=len(certificates), touching=touching,
                          literal_subsets=LITERAL_SUBSETS, cpu_seconds=report['cpu_seconds'],
                          wall_seconds=report['wall_seconds'], peak_rss_bytes=report['peak_rss_bytes'],
                          report_bytes=len(encoded), report_sha256=hashlib.sha256(encoded).hexdigest()),
                     sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', type=Path, required=True)
    audit(parser.parse_args().report)
