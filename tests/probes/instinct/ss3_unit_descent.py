#!/usr/bin/env python3
"""B153/MI318 preregistered COMPLETE n12,3^4,E2 move-set diagnostic.

RUN-ON: GPT Intel CPU, one process plus one sequential C++ engine.
COMMAND: python3 tests/probes/instinct/ss3_unit_descent.py --output /tmp/math-instinct-b153-descent.json
Requires a precompiled /tmp/math-instinct-b153-descent binary from sibling .cpp.
P1: independent combination enumeration and engine coverage agree for EVERY
    sorted SS target (including targets with no goals, if any), all369600 words.
P2: exact shortest descent maps obey adjacent >= single >= single+two-for-two
    (infinity allowed); expect two-for-two to reach every E2 state, falsifiable.
P3: MI301 canonical trap remains unreachable under all single swaps, but is
    reachable under single+two-for-two. No prediction of a uniform depth bound.
REFERENCE: independent ordered triple-mask enumeration, all target coverage
    counts from sum-vector multiplicities, WHOLE distance maps on trap and
    central(16,16,17,17) targets using literal mask exchanges (not engine code).
UNEXPECTED: engine compares EVERY state's exact three distances with its
    value-reflected/bin-reversed counterpart, not merely histograms.
COUNTERFACTUAL: target existence need not imply single-swap reachability;
    omitting unreachable nodes, equal-target labels or SS targets fails controls.
    Finite success cannot certify SS3, higher error levels, other sizes or n.
CAPS: one invocation,60CPU/90wall seconds,256MiB per process,2M engine nodes,
    200M generated engine moves,8MiB raw engine output,100wall watchdog.
    Stop first instrument failure/cap;retain mathematical negative results;
    no repair/retry/extension. Compile only after source/prediction push.
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

FIXTURES = ((7, 10, 23, 26), (16, 16, 17, 17))
START = (1, 1, 3, 3, 3, 2, 1, 0, 0, 0, 2, 2)
BEGAN = time.monotonic()


def budget():
    assert time.monotonic()-BEGAN < 90, 'wall cap'
    # macOS reports bytes. Linux unit adaptation is deliberately not assumed.
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 256*1024**2, 'RSS cap'
    usage = [resource.getrusage(w) for w in (resource.RUSAGE_SELF, resource.RUSAGE_CHILDREN)]
    assert sum(u.ru_utime+u.ru_stime for u in usage) < 60, 'aggregate CPU cap'
    assert usage[1].ru_maxrss < 256*1024**2, 'child RSS cap'


def ss(t):
    if sum(t) != 66:
        return False
    for k in range(1, 4):
        for j in combinations(range(4), k):
            r = 3*k
            if not r*(r-1)//2 <= sum(t[i] for i in j) <= r*(23-r)//2:
                return False
    return True


def encode(bins):
    return sum(j << (2*x) for j, b in enumerate(bins) for x in range(12) if b >> x & 1)


def independent_domain():
    weights = [sum(x for x in range(12) if m >> x & 1) for m in range(4096)]
    counts, fixtures = Counter(), {t: {} for t in FIXTURES}
    all_values = set(range(12))
    total = 0
    for aa in combinations(range(12), 3):
        a = sum(1 << x for x in aa)
        rest = all_values-set(aa)
        for bb in combinations(sorted(rest), 3):
            b = sum(1 << x for x in bb)
            tail = rest-set(bb)
            for cc in combinations(sorted(tail), 3):
                c = sum(1 << x for x in cc)
                d = 4095 ^ a ^ b ^ c
                bins = (a, b, c, d)
                q = tuple(weights[m] for m in bins)
                counts[q] += 1
                total += 1
                for t in FIXTURES:
                    e = sum(abs(u-v) for u, v in zip(q, t))
                    if e <= 2:
                        fixtures[t][bins] = e
        budget()
    assert total == 369600 and sum(counts.values()) == total
    targets = set()
    for a in range(3, 31):
        for b in range(a, 31):
            for c in range(b, 31):
                d = 66-a-b-c
                if c <= d <= 30 and ss((a, b, c, d)):
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
    values = [tuple(x for x in range(12) if m >> x & 1) for m in bins]
    for a, b in combinations(range(4), 2):
        for r in ((1, 2) if mode == 2 else (1,)):
            for aa in combinations(values[a], r):
                for bb in combinations(values[b], r):
                    if mode == 0 and abs(aa[0]-bb[0]) != 1:
                        continue
                    flip = sum(1 << x for x in aa+bb)
                    v = list(bins)
                    v[a] ^= flip
                    v[b] ^= flip
                    yield tuple(v)


def reference_maps(fixtures):
    out = {}
    for t, domain in fixtures.items():
        maps = []
        for mode in range(3):
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
    words = [tuple(w >> (2*x) & 3 for x in range(12)) for w in path]
    errors = []
    for w in words:
        assert tuple(w.count(j) for j in range(4)) == (3,)*4
        errors.append(sum(abs(sum(x for x in range(12) if w[x] == j)-t[j]) for j in range(4)))
    assert errors == [2]*(len(words)-1)+[0], errors
    for u, v in zip(words, words[1:]):
        changed = [x for x in range(12) if u[x] != v[x]]
        owners = {u[x] for x in changed}
        assert len(owners) == 2
        a, b = sorted(owners)
        assert all(v[x] == (b if u[x] == a else a) for x in changed)
        assert len(changed) in ((2, 4) if mode == 2 else (2,))
        if mode == 0:
            assert abs(changed[0]-changed[1]) == 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU, (60, 61))
    resource.setrlimit(resource.RLIMIT_FSIZE, (8*1024**2, 8*1024**2))
    raw = Path(args.output).with_suffix('.engine.txt')
    subprocess.run(['/tmp/math-instinct-b153-descent', str(raw)], check=True, timeout=60)
    assert raw.stat().st_size <= 8*1024**2
    coverage, maps, hist, paths, total = {}, {t: {} for t in FIXTURES}, {}, [], None
    unreachable = []
    for line in raw.read_text().splitlines():
        fields = line.split()
        if fields[0] == 'TOTAL':
            total = tuple(map(int, fields[1:]))
            continue
        t = tuple(map(int, fields[1:5]))
        assert ss(t) and t == tuple(sorted(t))
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
    # MI301 target sorting uses labels B,D,A,C; tied-target labels elsewhere
    # are NOT quotiented, all assignments are retained in their whole maps.
    new_label = {1: 0, 3: 1, 0: 2, 2: 3}
    trap_word = sum(new_label[j] << (2*x) for x, j in enumerate(START))
    trap_dist = maps[FIXTURES[0]][trap_word]
    assert trap_dist[0] == trap_dist[1] == -1 and trap_dist[2] > 0
    aggregate = [Counter() for _ in range(3)]
    labelled = [Counter() for _ in range(3)]
    for (t, mode), h in hist.items():
        assert sum(h.values()) == coverage[t][1]
        aggregate[mode].update(h)
        weight = factorial(4)
        for multiplicity in Counter(t).values():
            weight //= factorial(multiplicity)
        labelled[mode].update({d: n*weight for d, n in h.items()})
    for t, mode, depth in paths:
        assert depth == max((d for d in hist[t, mode] if d >= 0), default=-1)
    assert len(hist) == 3*len(coverage)
    assert total[0] == 369600 and total[1] == len(coverage)
    assert total[2] == total[4] == sum(sum(x) for x in coverage.values())
    budget()
    report = dict(status='COMPLETE', domain='n12 sizes3^4 sorted SS targets;all E2 labelled starts',
                  total=total, goals=sum(c[0] for c in coverage.values()),
                  unit_starts=sum(c[1] for c in coverage.values()),
                  targets_without_goals=[t for t, c in coverage.items() if not c[0]],
                  histograms=[dict(sorted(h.items())) for h in aggregate], trap_distances=trap_dist,
                  all_labelled_target_histograms=[dict(sorted(h.items())) for h in labelled],
                  quad_all_reachable=aggregate[2].get(-1, 0) == 0,
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
