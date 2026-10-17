#!/usr/bin/env python3
"""MI309/B148 prereg: ONE fixed audit of MI308 after source/prediction push.

h2..4,m2(h+1)..16,all r=h+1..m-h-1,both X/Y:54 pools/278 FULL spectra.
Independent set-DP vs combinations; exact Y holes, literal band joins, reflected
complements. n12/slack5:225 independently generated targets,195 X-first,
26 Y-second,4 forced repairs. Exceptional h2..5,b/d in k,k+1,k+3:36 witnesses.
Retain h1 missing sums/negative complete n8 oracle and signed-map controls.
Predict all comparisons pass. 10CPU/20wall/128MiB/2M subsets/2MiB raw,
25wall external watchdog. First failure/cap stops; no repair/retry/expansion.
Finite checks do not prove MI308. Raw outside git; only outcome header after.
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
SUBSETS = 0
ORACLE_STATES = 0


def limits():
    assert time.process_time() - START_CPU < 10, 'CPU cap'
    assert time.monotonic() - START_WALL < 20, 'wall cap'
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 128 * 1024**2, 'RSS cap (macOS bytes)'
    assert SUBSETS <= 2_000_000, 'subset cap'
    assert ORACLE_STATES <= 1000, 'negative-oracle state cap'


def low(r):
    return r * (r - 1) // 2


def high(m, r):
    return r * (2 * m - r - 1) // 2


def shapes(h, m):
    x = tuple(range(m - h)) + tuple(range(m, m + h - 1)) + (m + h,)
    y = tuple(range(m - h - 1)) + (m - h,) + tuple(range(m, m + h))
    assert len(x) == len(set(x)) == m and len(y) == len(set(y)) == m
    return {'X': x, 'Y': y}


def set_dp(values, r):
    # No band, extremum or hole formulas; signed values work directly.
    acc = [{0}] + [set() for _ in range(r)]
    for seen, v in enumerate(reversed(values)):
        for k in range(min(r, seen + 1), 0, -1):
            acc[k].update(s + v for s in tuple(acc[k - 1]))
    return acc[r]


def literal(values, r, upper=()):
    global SUBSETS
    upper = frozenset(upper)
    witnesses, bands = {}, {}
    for chosen in itertools.combinations(values, r):
        SUBSETS += 1
        s = sum(chosen)
        witnesses.setdefault(s, chosen)
        j = sum(v in upper for v in chosen)
        bands.setdefault(j, set()).add(s)
    limits()
    return witnesses, bands


def check_partition(bins, sizes, targets):
    assert tuple(map(len, bins)) == tuple(sizes)
    assert tuple(map(sum, bins)) == tuple(targets)
    assert sorted(x for bucket in bins for x in bucket) == list(range(sum(sizes)))


def exceptional(h, b, d):
    k = h + 1
    n, m, ell = b + d + 2 * k, b + k, d + k
    targets = (high(m, k) + h * h, low(b) + 1,
               (n - 1) * k - high(ell, k) - h * h, high(n, d) - 1)
    bb = tuple(range(b - 1)) + (b,)
    dd = (n - d - 1,) + tuple(range(n - d + 1, n))
    rest = tuple(x for x in range(n) if x not in bb and x not in dd)
    w = (0,) + tuple(range(2, 2 * k)) + (2 * k + 1,)
    assert tuple(x - (b - 1) for x in rest) == w
    smallest = (0,) + tuple(range(2, k + 1))
    assert k >= 3 and 2 != k
    cp = tuple(sorted(x for x in smallest if x not in (2, k))) + (k + 1, 2 * k + 1)
    ap = tuple(x for x in w if x not in cp)
    assert len(cp) == len(ap) == k
    assert sum(ap) == 3 * low(k) + 1
    assert sum(cp) == low(k + 1) - 1 + 2 * k
    aa = tuple(x + b - 1 for x in ap)
    cc = tuple(x + b - 1 for x in cp)
    bins = (aa, bb, cc, dd)
    check_partition(bins, (k, b, k, d), targets)
    return dict(h=h, b=b, d=d, targets=targets, bins=bins, residue=w)


def exact_oracle(values, sizes, targets):
    global ORACLE_STATES, SUBSETS
    ORACLE_STATES += 1
    limits()
    if len(sizes) == 1:
        return len(values) == sizes[0] and sum(values) == targets[0]
    for chosen in itertools.combinations(values, sizes[0]):
        SUBSETS += 1
        if sum(chosen) == targets[0]:
            rest = tuple(v for v in values if v not in chosen)
            if exact_oracle(rest, sizes[1:], targets[1:]):
                return True
    return False


def audit(report_path):
    rows, cache = [], {}
    pool_count = 0
    for h in (2, 3, 4):
        k = h + 1
        for m in range(2 * k, 17):
            pair = shapes(h, m)
            for name, pool in pair.items():
                pool_count += 1
                assert sum(pool) == low(m) + h * h + 1
                reflected = tuple(sorted(2 * m - 1 - v for v in range(2 * m) if v not in pool))
                assert reflected == pair['Y' if name == 'X' else 'X']
                for r in range(k, m - k + 1):
                    q = m - r
                    w, bands = literal(pool, r, range(m, m + h))
                    direct = set(w)
                    assert direct == set_dp(pool, r)
                    expected = set(range(low(r), sum(pool) - low(q) + 1))
                    holes = set()
                    if name == 'Y':
                        if r == k:
                            holes.add(high(m, k) + h * h)
                        if q == k:
                            holes.add(sum(pool) - high(m, k) - h * h)
                    assert expected - direct == holes and direct == expected - holes
                    joins = []
                    if name == 'Y' and r == k:
                        assert set(bands) == set(range(h + 1))
                        for j in range(h):
                            actual = max(bands[j]) + 1 - min(bands[j + 1])
                            g = h * (q - h - 1) + 1 + j * (3 * h - q - 1) - 2 * j * j
                            assert actual == g and actual >= 1
                            joins.append(actual)
                    cache[h, m, name, r] = w
                    rows.append(dict(h=h, m=m, name=name, r=r, sums=sorted(direct),
                                     holes=sorted(holes), joins=joins))
    assert pool_count == 54 and len(rows) == 278

    # Original-target loop, independent of pool spectra and failure formulas.
    domain = set()
    for a, b, c in itertools.product(range(3, 31), repeat=3):
        d = 66 - a - b - c
        if 3 <= d <= 30 and a + b == 20:
            domain.add((a, b, c, d))
    assert len(domain) == 225
    branches = {'X': 0, 'Y': 0, 'repair': 0}
    certificates = []
    for targets in sorted(domain):
        chosen_bins, branch = None, None
        for name, partner in (('X', 'Y'), ('Y', 'X')):
            left, right = cache[2, 6, name, 3], cache[2, 6, partner, 3]
            if targets[0] not in left or 33 - targets[2] not in right:
                continue
            pool = shapes(2, 6)[name]
            aa = left[targets[0]]
            bb = tuple(x for x in pool if x not in aa)
            cc = tuple(sorted(11 - x for x in right[33 - targets[2]]))
            dd = tuple(x for x in range(12) if x not in pool and x not in cc)
            chosen_bins, branch = (aa, bb, cc, dd), name
            break
        if chosen_bins is None:
            ex = exceptional(2, 3, 3)
            ia = next(i for i in (0, 1) if targets[i] == 16)
            ic = next(i for i in (2, 3) if targets[i] == 17)
            ib, idd = 1 - ia, 5 - ic
            result = [None] * 4
            for index, bucket in zip((ia, ib, ic, idd), ex['bins']):
                result[index] = bucket
            chosen_bins, branch = tuple(result), 'repair'
        check_partition(chosen_bins, (3, 3, 3, 3), targets)
        branches[branch] += 1
        certificates.append(dict(targets=targets, branch=branch, bins=chosen_bins))
    assert branches == {'X': 195, 'Y': 26, 'repair': 4}
    assert {tuple(x['targets']) for x in certificates} == domain

    repairs = []
    for h in (2, 3, 4, 5):
        k = h + 1
        for b, d in itertools.product((k, k + 1, k + 3), repeat=2):
            repairs.append(exceptional(h, b, d))
    assert len(repairs) == 36
    controls = []
    for values, r in [(shapes(1, 4)['X'], 2), (shapes(2, 6)['Y'], 3), (shapes(3, 8)['X'], 4)]:
        w, _ = literal(values, r)
        moved = tuple(v - 17 for v in values)
        wm, _ = literal(moved, r)
        assert set(w) == set_dp(values, r)
        assert set(wm) == set_dp(moved, r) == {s - 17 * r for s in w}
        controls.append(dict(values=values, r=r, sums=sorted(w), shifted=sorted(wm)))
    assert 4 not in controls[0]['sums']  # h1 X is not claimed complete.
    residual, _ = literal((0, 2, 3, 5), 2)
    assert 4 not in residual and 6 not in residual
    assert set(residual) == set_dp((0, 2, 3, 5), 2)
    assert not exact_oracle(tuple(range(8)), (2, 2, 2, 2), (6, 2, 8, 12))
    limits()
    report = dict(status='PASS', pools=pool_count, spectra=rows, target_domain=sorted(domain),
                  certificates=certificates, branches=branches, repairs=repairs, controls=controls,
                  pair_residue_sums=sorted(residual), oracle_states=ORACLE_STATES,
                  literal_subsets=SUBSETS, cpu_seconds=time.process_time() - START_CPU,
                  wall_seconds=time.monotonic() - START_WALL,
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    encoded = json.dumps(report, sort_keys=True, separators=(",", ":")).encode()
    assert len(encoded) <= 2 * 1024**2 and not report_path.exists()
    report_path.write_bytes(encoded)
    summary = {k: report[k] for k in ('status', 'pools', 'branches', 'oracle_states', 'literal_subsets',
                                    'cpu_seconds', 'wall_seconds', 'peak_rss_bytes')}
    summary.update(spectra=len(rows), target_vectors=len(domain), repairs=len(repairs),
                   report_bytes=len(encoded), report_sha256=hashlib.sha256(encoded).hexdigest())
    print(json.dumps(summary, sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', type=Path, required=True)
    audit(parser.parse_args().report)
