#!/usr/bin/env python3
"""GC2005: exact fixed-size summary collisions in genuine finite-seed worlds."""
import hashlib
import json
import os
from pathlib import Path

DEPTH = 8
PERIOD_CAP = 256
RESOLUTIONS = (1, 2, 4, 8)


def least(w):
    n = len(w)
    while n > 1 and w[:n // 2] == w[n // 2:n]:
        n //= 2
    return w[:n]


def integral(g, initial):
    w, x = [], initial
    for z in g:
        w.append(x)
        x ^= z
    return w, x


def phase_parities(w, m):
    assert len(w) % m == 0
    return tuple(sum(w[r::m]) % 2 for r in range(m))


def summary(a, b, m, p):
    bins = [[0] * 4 for _ in range(m)]
    for t in range(p):
        bins[t % m][2 * a[t % len(a)] + b[t % len(b)]] += 1
    return tuple(tuple(h) for h in bins)


def compatible(a, b):
    p = max(len(a), len(b))
    return all(b[t % len(b)] <= (a[t % len(a)] ^ a[(t + 1) % len(a)])
               <= (b[t % len(b)] | b[(t + 1) % len(b)]) for t in range(p))


def word(w):
    return ''.join(map(str, w))


seen = {m: {} for m in RESOLUTIONS}
collisions = {}
comparisons = hierarchy_checks = pairs = 0
eligible = dict.fromkeys(RESOLUTIONS, 0)
max_period = 1
table = (0, 1, 1, 1, 1, 0, 0, 0)

# The generic histogram collision is a negative compatibility control.
for m in RESOLUTIONS:
    p = 8 * m
    a1 = [int(t in (0, m)) for t in range(p)]
    a2 = [int(t in (0, 2 * m)) for t in range(p)]
    assert summary(a1, [0], m, p) == summary(a2, [0], m, p)
    assert not compatible(a1, [0]) and not compatible(a2, [0])
    c1, end1 = integral(a1, 0)
    c2, end2 = integral(a2, 0)
    assert end1 == end2 == 0
    assert phase_parities(c1, m) == (1,) * m
    assert phase_parities(c2, m) == (0,) * m

for seed in range(128):
    initial = [1] + [(seed >> j) & 1 for j in range(7)] + [0]
    diags = [[1]]
    for d in range(1, DEPTH + 1):
        a = diags[d - 1]
        b = diags[d - 2] if d >= 2 else [0]
        p = max(len(a), len(b))
        g = least([a[t % len(a)] | b[t % len(b)] for t in range(p)])
        q = len(g)
        period = q * (2 if sum(g) % 2 else 1)
        assert period <= PERIOD_CAP, 'frozen period cap exceeded'
        c, end = integral(g * (period // q), initial[d])
        c = least(c)
        assert end == initial[d]
        # Constant forcing zero may yield constant zero or one, both period one.
        assert len(c) == period
        diags.append(c)
        max_period = max(max_period, len(c))
        if d < 2:
            continue
        assert compatible(a, b), (seed, d, 'adjacency')
        pairs += 1
        for m in RESOLUTIONS:
            if len(c) % (2 * m) == 0:
                pc = len(c)
                fullg = [g[t % q] for t in range(pc)]
                fine = phase_parities(fullg, 2 * m)
                derived = tuple(sum(fine[(r + u) % (2 * m)]
                                    for u in range(m)) % 2 for r in range(m))
                assert phase_parities(c, m) == derived, (seed, d, m)
                hierarchy_checks += 1
            if p % m:
                continue
            eligible[m] += 1
            signature = (d, p, len(a), len(b), q, a[0], b[0], c[0],
                         summary(a, b, m, p))
            first = [c[t % len(c)] for t in range(p)]
            twice = [c[t % len(c)] for t in range(2 * p)]
            output = (len(c), phase_parities(first, m), phase_parities(twice, m))
            evidence = {'seed_code': seed, 'seed_left_to_right': word(initial[7::-1]),
                        'target_depth': d, 'M': m, 'P': p, 'a': word(a), 'b': word(b),
                        'c': word(c), 'signature': signature, 'output': output}
            old = seen[m].get(signature)
            if old is None:
                seen[m][signature] = evidence
            else:
                # Period is already fixed by q and the input histogram's OR parity.
                assert old['output'][0] == output[0]
                if old['output'] != output and m not in collisions:
                    collisions[m] = [old, evidence]

    # Independent spatial evolution: literal table, full finite cone, no clamps.
    row = sum(initial[d] << (7 - d) for d in range(8))
    for t in range(2 * max(map(len, diags))):
        for d, c in enumerate(diags):
            if t < 2 * len(c):
                pos = 2 * t + 7 - d
                value = 0 if pos < 0 else (row >> pos) & 1
                assert value == c[t % len(c)], (seed, t, d)
                comparisons += 1
        mask = (1 << (10 + 2 * t)) - 1
        inputs = (row << 2, row << 1, row)
        nxt = 0
        for code, result in enumerate(table):
            if result:
                term = mask
                for j, bits in enumerate(inputs):
                    term &= bits if (code >> (2 - j)) & 1 else (~bits & mask)
                nxt |= term
        row = nxt

result = {'status': 'PASS', 'seed_count': 128, 'max_depth': DEPTH,
          'max_period': max_period, 'adjacent_pairs_checked': pairs,
          'forward_comparisons': comparisons, 'hierarchy_checks': hierarchy_checks,
          'eligible': eligible, 'distinct_input_summaries': {m: len(s) for m, s in seen.items()},
          'prediction_met': bool(set(collisions) & {1, 2}), 'collisions': collisions,
          'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out = Path(os.environ['CAPPED_OUT']) / 'results.json'
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'collisions'}))
print('collision_resolutions', sorted(collisions))
