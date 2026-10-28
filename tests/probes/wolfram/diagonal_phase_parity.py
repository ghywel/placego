#!/usr/bin/env python3
"""GC2003: bounded exact phase-parity self-check, fixed scope; no CLI widening."""
import hashlib
import itertools
import json
import os
from pathlib import Path

CAP = 4096
DEPTH = 29

def least(word):
    p = len(word)
    while p > 1 and word[:p // 2] == word[p // 2:p]:
        p //= 2
    return word[:p]

def integrate(g, start=0):
    out, x = [], start
    for bit in g:
        out.append(x)
        x ^= bit
    return out, x

def parity(a):
    return sum(a) % 2

synthetic = 0
for p in (2, 4, 8):
    for g in itertools.product((0, 1), repeat=p):
        if parity(g):
            continue
        for start in (0, 1):
            d, end = integrate(g, start)
            assert end == start
            assert parity(d) == parity(g[::2]) == parity(g[1::2])
            synthetic += 1

# Equal least forcing periods, both closing at period eight, different weights.
examples = []
for g in ([1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0]):
    d, end = integrate(g)
    assert end == 0 and len(least(g)) == len(least(d)) == 8
    examples.append({'g': g, 'D': d, 'weight_parity': parity(d)})
assert [e['weight_parity'] for e in examples] == [1, 0]

diags = [[1]]
rows = []
for k in range(1, DEPTH + 1):
    a, b = diags[k - 1], diags[k - 2] if k > 1 else [0]
    common = max(len(a), len(b))
    g = least([a[t % len(a)] | b[t % len(b)] for t in range(common)])
    q = len(g)
    p = q * (2 if parity(g) else 1)
    assert p <= CAP, 'frozen period cap exceeded'
    d, end = integrate(g * (p // q))
    assert end == 0 and len(least(d)) == p
    if p >= 2:
        fullg = g * (p // q)
        assert parity(d) == parity(fullg[::2]) == parity(fullg[1::2])
    if p == 2 * q:
        assert d[q:] == [1 - v for v in d[:q]]
        assert sum(d) == q
        assert parity(d) == (q % 2)
    diags.append(d)
    rows.append({'d': k, 'period': p, 'forcing_period': q,
                 'weight': sum(d), 'weight_parity': parity(d),
                 'doubled': p == 2 * q})

# Independent bit-parallel forward evolution with literal Rule 30 truth table.
table = [0, 1, 1, 1, 1, 0, 0, 0]  # index 4*l+2*c+r
row = 1
comparisons = 0
for t in range(2 * max(map(len, diags))):
    for k, d in enumerate(diags):
        if t < 2 * len(d):
            index = 2 * t - k
            bit = 0 if index < 0 else (row >> index) & 1
            assert bit == d[t % len(d)], (t, k)
            comparisons += 1
    # Only sites needed for these diagonals: exact boundary 0 outside full cone.
    # Retain the full finite row, not a clamped strip.
    mask = (1 << (2 * t + 3)) - 1
    inputs = (row << 2, row << 1, row)
    nxt = 0
    for code, output in enumerate(table):
        if output:
            term = mask
            for j, bits in enumerate(inputs):
                term &= bits if (code >> (2 - j)) & 1 else (~bits & mask)
            nxt |= term
    row = nxt

result = {'status': 'PASS', 'synthetic_integrals': synthetic,
          'forward_comparisons': comparisons, 'diagonals': rows,
          'same_period_countercontrol': examples,
          'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
dest = Path(os.environ['CAPPED_OUT']) / 'results.json'
dest.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'synthetic_integrals': synthetic,
                  'forward_comparisons': comparisons,
                  'max_period': max(map(len, diags)), 'result_file': dest.name}))
