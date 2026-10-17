#!/usr/bin/env python3
"""B156/MI322: ONE complete next-ambient unit-error diagnostic, not automatic widening.
RUN-ON GPT Intel CPU. Compile sibling .cpp to /tmp/math-instinct-b156-descent.
COMMAND python3 tests/probes/instinct/ss3_unit_descent13.py --output /tmp/math-instinct-b156-descent.json
DOMAIN n13 counts3,3,3,4; all SS targets with first3 sorted; all E2 starts.
QUESTION Does the smallest four-token-bin case require 3for3 to release E2?
P1 independent whole coverage map matches all1201200 labelled partitions.
H tentatively expect all E2 starts still release using1/2-token exchanges;
  falsify H with any unreachable state,retaining examples. No uniform bound.
P2 all1/2/3 moves cannot worsen distance; mathematical failures are outcomes.
REFERENCE independent triple-mask enumeration and WHOLE two-mode maps at
  targets(7,23,26,22) and(18,18,18,24); all maximal paths checked literally.
CONTROL padded MI301 has a DIRECT quad escape,distances(1,1):token12 is active.
UNEXPECTED all-state reflected distances with only equal-size labels reversed.
CAPS 80aggregateCPU/120wall/384MiB per process/6M nodes/2B engine moves/16MiB raw;
  engine55wall,80CPU hard,wrapper80CPU hard;130wall watchdog,compile30wall.
ONE run after source/prereg push,no fix/retry/cap rise or further n.
"""
import argparse
from collections import Counter, deque
from itertools import combinations, product
import json
from math import factorial
from pathlib import Path
import resource
import subprocess
import time

FIXTURES = ((7, 23, 26, 22), (18, 18, 18, 24))
SIZES = (3,3,3,4)
START = (1, 1, 3, 3, 3, 2, 1, 0, 0, 0, 2, 2, 3)
BEGAN = time.monotonic()


def budget():
    assert time.monotonic()-BEGAN < 120, 'wall cap'
    # macOS reports bytes. Linux unit adaptation is deliberately not assumed.
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 384*1024**2, 'RSS cap'
    usage = [resource.getrusage(w) for w in (resource.RUSAGE_SELF, resource.RUSAGE_CHILDREN)]
    assert sum(u.ru_utime+u.ru_stime for u in usage) < 80, 'aggregate CPU cap'
    assert usage[1].ru_maxrss < 384*1024**2, 'child RSS cap'


def ss(t):
    if sum(t) != 78:
        return False
    for k in range(1, 4):
        for j in combinations(range(4), k):
            r = sum(SIZES[i] for i in j)
            if not r*(r-1)//2 <= sum(t[i] for i in j) <= r*(25-r)//2:
                return False
    return True


def encode(bins):
    return sum(j << (2*x) for j, b in enumerate(bins) for x in range(13) if b >> x & 1)


def independent_domain():
    weights = [sum(x for x in range(13) if m >> x & 1) for m in range(8192)]
    counts, fixtures = Counter(), {t: {} for t in FIXTURES}
    all_values = set(range(13))
    total = 0
    for aa in combinations(range(13), 3):
        a = sum(1 << x for x in aa)
        rest = all_values-set(aa)
        for bb in combinations(sorted(rest), 3):
            b = sum(1 << x for x in bb)
            tail = rest-set(bb)
            for cc in combinations(sorted(tail), 3):
                c = sum(1 << x for x in cc)
                d = 8191 ^ a ^ b ^ c
                bins = (a, b, c, d)
                q = tuple(weights[m] for m in bins)
                counts[q] += 1
                total += 1
                for t in FIXTURES:
                    e = sum(abs(u-v) for u, v in zip(q, t))
                    if e <= 2:
                        fixtures[t][bins] = e
        budget()
    assert total == 1201200 and sum(counts.values()) == total
    targets = set()
    for a in range(3, 34):
        for b in range(a, 34):
            for c in range(b, 34):
                d = 78-a-b-c
                if 6 <= d <= 42 and ss((a, b, c, d)):
                    targets.add((a, b, c, d))
    coverage = {}
    for t in targets:
        unit = 0
        for a, b in product(range(4), repeat=2):
            if a == b:
                continue
            q = list(t)
            q[a] += 1
            q[b] -= 1
            unit += counts[tuple(q)]
        coverage[t] = (counts[t], unit)
    return coverage, fixtures


def mask_neighbors(bins, mode):
    values = [tuple(x for x in range(13) if m >> x & 1) for m in bins]
    for a, b in combinations(range(4), 2):
        for r in range(1, mode+3):
            for aa in combinations(values[a], r):
                for bb in combinations(values[b], r):
                    flip = sum(1 << x for x in aa+bb)
                    v = list(bins)
                    v[a] ^= flip
                    v[b] ^= flip
                    yield tuple(v)


def reference_maps(fixtures):
    out = {}
    for t, domain in fixtures.items():
        maps = []
        for mode in range(2):
            dist = {b: 0 for b, e in domain.items() if e == 0}
            queue = deque(dist)
            while queue:
                b = queue.popleft()
                for v in mask_neighbors(b, mode):
                    if v in domain and v not in dist:
                        dist[v] = dist[b]+1
                        queue.append(v)
                if len(dist) % 128 == 0:
                    budget()
            maps.append({encode(b): dist.get(b, -1) for b in domain})
        out[t] = {w: tuple(m[w] for m in maps) for w in maps[0]}
    return out


def check_path(t, mode, path):
    words = [tuple(w >> (2*x) & 3 for x in range(13)) for w in path]
    errors = []
    for w in words:
        assert tuple(w.count(j) for j in range(4)) == SIZES
        errors.append(sum(abs(sum(x for x in range(13) if w[x] == j)-t[j]) for j in range(4)))
    assert errors == [2]*(len(words)-1)+[0], errors
    for u, v in zip(words, words[1:]):
        changed = [x for x in range(13) if u[x] != v[x]]
        owners = {u[x] for x in changed}
        assert len(owners) == 2
        a, b = sorted(owners)
        assert all(v[x] == (b if u[x] == a else a) for x in changed)
        assert len(changed) in ((2, 4) if mode == 0 else (2, 4, 6))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU, (80, 81))
    resource.setrlimit(resource.RLIMIT_FSIZE, (16*1024**2, 16*1024**2))
    raw = Path(args.output).with_suffix('.engine.txt')
    subprocess.run(['/tmp/math-instinct-b156-descent', str(raw)], check=True, timeout=65)
    assert raw.stat().st_size <= 16*1024**2
    coverage, maps, hist, paths, total = {}, {t: {} for t in FIXTURES}, {}, [], None
    unreachable = []
    for line in raw.read_text().splitlines():
        fields = line.split()
        if fields[0] == 'TOTAL':
            total = tuple(map(int, fields[1:]))
            continue
        t = tuple(map(int, fields[1:5]))
        assert ss(t) and t[:3] == tuple(sorted(t[:3]))
        if fields[0] == 'C':
            assert t not in coverage
            coverage[t] = tuple(map(int, fields[5:]))
        elif fields[0] == 'D':
            w = int(fields[5]); assert w not in maps[t]
            maps[t][w] = tuple(map(int, fields[6:]))
        elif fields[0] == 'H':
            hist[t, int(fields[5])] = {int(k): int(v) for k, v in (f.split(':') for f in fields[6:])}
        elif fields[0] == 'P':
            mode = int(fields[5]); path = tuple(map(int, fields[6:]))
            check_path(t, mode, path)
            paths.append((t, mode, len(path)-1))
        elif fields[0] == 'U':
            unreachable.append((t, int(fields[5]), int(fields[6])))
        else:
            raise AssertionError(fields[0])
    reference_coverage, fixtures = independent_domain()
    assert coverage == reference_coverage, 'whole-domain coverage mismatch'
    reference = reference_maps(fixtures)
    assert maps == reference, 'whole distance-map mismatch'
    # Padded MI301: triple labels B,A,C then the distinguished four-token D.
    new_label = {1: 0, 0: 1, 2: 2, 3: 3}
    trap_word = sum(new_label[j] << (2*x) for x, j in enumerate(START))
    trap_dist = maps[FIXTURES[0]][trap_word]
    assert trap_dist == (1, 1)
    aggregate = [Counter() for _ in range(2)]
    labelled = [Counter() for _ in range(2)]
    for (t, mode), h in hist.items():
        assert sum(h.values()) == coverage[t][1]
        aggregate[mode].update(h)
        weight = factorial(3)
        for multiplicity in Counter(t[:3]).values():
            weight //= factorial(multiplicity)
        labelled[mode].update({d: n*weight for d, n in h.items()})
    for t, mode, depth in paths:
        assert depth == max((d for d in hist[t, mode] if d >= 0), default=-1)
    assert len(hist) == 2*len(coverage)
    assert total[0] == 1201200 and total[1] == len(coverage)
    assert total[2] == total[4] == sum(sum(x) for x in coverage.values())
    budget()
    report = dict(status='COMPLETE', domain='n13 counts3,3,3,4;first3 SS targets sorted;all E2 labelled starts',
                  total=total, goals=sum(c[0] for c in coverage.values()),
                  unit_starts=sum(c[1] for c in coverage.values()),
                  targets_without_goals=[t for t, c in coverage.items() if not c[0]],
                  histograms=[dict(sorted(h.items())) for h in aggregate], trap_distances=trap_dist,
                  all_labelled_target_histograms=[dict(sorted(h.items())) for h in labelled],
                  quad_all_reachable=aggregate[0].get(-1, 0) == 0,
                  triple_all_reachable=aggregate[1].get(-1, 0) == 0,
                  independent_fixture_nodes={str(t): len(m) for t, m in reference.items()},
                  literal_max_paths=len(paths), controls='PASS',
                  unreachable_examples=unreachable,
                  wall_seconds=time.monotonic()-BEGAN,
                  self_cpu=resource.getrusage(resource.RUSAGE_SELF).ru_utime+resource.getrusage(resource.RUSAGE_SELF).ru_stime,
                  child_usage=list(resource.getrusage(resource.RUSAGE_CHILDREN)))
    Path(args.output).write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, sort_keys=True))


if __name__ == '__main__':
    main()
