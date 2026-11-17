#!/usr/bin/env python3
"""GC2206: fixed finite control of a4691a's inverse classes, not a survivor census.

Prediction, counterfactual and resource freeze: rule30-primitive-source-review.md.
One width only, no retries or widening. Forward permutation is an independent
oracle for the serial inverse; scalar gates independently check the packed map.
"""
import hashlib
import json
import os
from collections import Counter
from pathlib import Path

K = 12
k = 8
MASK = (1 << K) - 1


def forward(w, p):
    return (w ^ ((w << 1 | (1 - p)) |
                 (w << 2 | ((1 - p) << 1) | p))) & MASK


def scalar_forward(w, p):
    bits = [(w >> i) & 1 for i in range(K)]
    out = []
    for i in range(K):
        a = bits[i - 1] if i >= 1 else 1 - p
        b = bits[i - 2] if i >= 2 else (p if i == 0 else 1 - p)
        out.append(bits[i] ^ (a | b))
    return sum(bit << i for i, bit in enumerate(out))


def inverse(w, p):
    out = []
    for i in range(K):
        if i == 0:
            gate = 1
        elif i == 1:
            gate = 1 if p == 0 else out[0]
        else:
            gate = out[-1] | out[-2]
        out.append(((w >> i) & 1) ^ gate)
    return sum(bit << i for i, bit in enumerate(out))


def F(w):
    u = w ^ ((w << 1 | 1) | (w << 2 | 2))
    return u ^ ((u << 1) | (u << 2 | 1))


# Exhaustively invert the fixed forward permutations without using inverse().
oracles = []
for p in (0, 1):
    back = {}
    for w in range(1 << K):
        v = forward(w, p)
        assert v == scalar_forward(w, p)
        assert v not in back
        back[v] = w
    assert len(back) == 1 << K
    for w in range(1 << K):
        assert inverse(w, p) == back[w]
    oracles.append(back)

clones = {F(v) for v in range(1 << (k - 4))}
assert len(clones) == 1 << (k - 4)
classes = {}
for w in range(1 << k):
    u = inverse(w, 1)
    v = inverse(u, 0)
    assert v == oracles[0][oracles[1][w]]
    if u < 1 << (k - 2):
        if v < 1 << (k - 4):
            label = 'clone'
            assert F(v) == w
        else:
            label = 'I'
            assert all((v >> i) & 1 for i in range(k - 2, K))
    else:
        label = 'II'
        assert all((u >> i) & 1 for i in range(k, K))
        assert all(((v >> i) & 1) ==
                   (1 ^ (((v >> (i - 1)) & 1) | ((v >> (i - 2)) & 1)))
                   for i in range(k, K))
    assert (label == 'clone') == (w in clones)
    classes[w] = label

all_counts = dict(Counter(classes.values()))
odd_counts = dict(Counter(classes[w] for w in range(1, 1 << k, 2)))
exact_odd_counts = dict(Counter(classes[w] for w in range(129, 256, 2)))
assert all_counts == {'clone': 16, 'I': 48, 'II': 192}
assert odd_counts == {'clone': 8, 'I': 24, 'II': 96}
assert exact_odd_counts == {'clone': 4, 'I': 12, 'II': 48}
named_I = [201, 225, 253]
named_II = [131, 143, 159, 165, 169, 181, 189, 245, 255]
assert classes[223] == 'clone'
assert all(classes[w] == 'I' for w in named_I)
assert all(classes[w] == 'II' for w in named_II)
additional = [w for w in range(129, 256, 2)
              if classes[w] != 'clone' and w not in named_I + named_II]
assert len(additional) == 48

# Unexpected guard: the type-II quantifier is vacuous at K=k, even for a clone.
assert all(True for _ in range(k, k))
assert 223 in clones
# Truncation control: the 7-bit orbit identity does not give equality at width 12.
w = 13
for p in (0, 1, 0, 1):
    w = scalar_forward(w, p)
assert w == F(F(13)) == 3553
assert w % (1 << 7) == 97 and w % (1 << 8) == 225 and w != 97

result = dict(status='PASS', K=K, k=k, forward_cases=2 * (1 << K),
              inverse_cases=2 * (1 << K), all_counts=all_counts,
              odd_counts=odd_counts, exact_8_bit_odd_counts=exact_odd_counts,
              primitive_outside_named_list=additional,
              projective_control={'untruncated': w, 'width7': 97, 'width8': 225},
              source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              scope='Finite implementation/scope control only; no survivor test or mortality claim')
(Path(os.environ['CAPPED_OUT']) / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
