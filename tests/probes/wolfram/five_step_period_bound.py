#!/usr/bin/env python3
"""GC2007 fixed exhaustive self-check of the five-step period bound."""
import hashlib
import itertools
import json
import os
from pathlib import Path


def integrate(g, initial=0):
    out, x = [], initial
    for bit in g:
        out.append(x)
        x ^= bit
    return out, x


def least(w):
    p = len(w)
    while p > 1 and w[:p // 2] == w[p // 2:p]:
        p //= 2
    return w[:p]


counts = {}
for q in (2, 4):
    cases = next_doublings = 0
    p = 4 * q
    for ah in itertools.product((0, 1), repeat=2 * q):
        a = list(ah) + [1 ^ x for x in ah]
        for bh in itertools.product((0, 1), repeat=q):
            b = (list(bh) + [1 ^ x for x in bh]) * 2
            g = [x | y for x, y in zip(a, b)]
            assert sum(g) % 2 == 0 and len(least(g)) == p
            for initial in (0, 1):
                c, end = integrate(g, initial)
                assert end == initial and len(least(c)) == p
                profile = [sum(c[r::q]) % 2 for r in range(q)]
                assert all(profile[(r + 1) % q] == (1 ^ profile[r]) for r in range(q))
                assert sum(c) % 2 == (q // 2) % 2
                # Independent weighted prefix count, then modulo two.
                weighted = p * initial + sum((p - 1 - t) * g[t] for t in range(p))
                assert weighted % 2 == sum(c) % 2
                h = [x | y for x, y in zip(c, a)]
                if sum(h) % 2:
                    for start_z in (0, 1):
                        z, end_z = integrate(h * 2, start_z)
                        assert end_z == start_z and len(least(z)) == 2 * p
                        assert z[p:] == [1 ^ x for x in z[:p]]
                        forcing = [z[t] | c[t % p] for t in range(2 * p)]
                        assert sum(forcing) % 2 == (q // 2) % 2
                        next_doublings += 1
                cases += 1
    counts[q] = {'integrals': cases, 'next_doublings_including_both_initial_bits': next_doublings}

# Genuine small-period exception. Exact closed words, then independent spatial check.
diags = [[1]]
for d in range(1, 8):
    a, b = diags[d - 1], diags[d - 2] if d > 1 else [0]
    p = max(len(a), len(b))
    g = [a[t % len(a)] | b[t % len(b)] for t in range(p)]
    c, end = integrate(g * (2 if sum(g) % 2 else 1))
    assert end == 0
    diags.append(least(c))
assert list(map(len, diags[3:])) == [4, 8, 8, 16, 32]
table = (0, 1, 1, 1, 1, 0, 0, 0)
row = {0: 1}
forward = 0
for t in range(64):
    for d, w in enumerate(diags):
        assert row.get(t - d, 0) == w[t % len(w)], (t, d)
        forward += 1
    row = {i: table[4 * row.get(i - 1, 0) + 2 * row.get(i, 0) + row.get(i + 1, 0)]
           for i in range(-t - 1, t + 2)}

# All binary words are covered by last-four-bit DP, not a random word sample.
states = {'': 0}
word_maxima = []
remainders = (0, 1, 2, 2, 3)
for n in range(1, 41):
    nxt = {}
    for suffix, weight in states.items():
        for bit in '01':
            extended = suffix + bit
            if '111' in extended or '11011' in extended:
                continue
            key = extended[-4:]
            nxt[key] = max(nxt.get(key, -1), weight + int(bit))
    states = nxt
    maximum = max(states.values())
    assert maximum <= 3 * (n // 5) + remainders[n % 5]
    word_maxima.append(maximum)
assert '111' not in '11010' * 8 and '11011' not in '11010' * 8

result = {'status': 'PASS', 'counts': counts, 'total_integrals': sum(v['integrals'] for v in counts.values()),
          'forward_comparisons': forward, 'single_seed_periods': list(map(len, diags)),
          'binary_word_maxima_lengths_1_to_40': word_maxima,
          'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(Path(os.environ['CAPPED_OUT']) / 'results.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
