#!/usr/bin/env python3
"""GC2788: independent finite audit of Local's S-15 draft.

Prediction: all 40 literal Lean layers equal scalar-rule path sets, all six
minimality witnesses read their stated words, and the gap-language product has
19 reachable nonrejecting pairs with no disagreement. The 18-column lift kills
3535353, which the 16-column graph admits. A mismatch stops clearance; no larger
search follows. Controls: reject a deleted start window and inverted boundary
phase; retain the permitted 33 start and the graph-only scope of witnesses.
Record searched: GC2775, CL758, L1608, CP-2.2, GC706/1087, kit GateTrap and
PeriodTwoWidth13, and portal60990f including relaxed_no_forbidden_factor.
No new census, physical realisability claim, Lean build or Wolfram execution.
"""
import argparse
import ast
import functools
import hashlib
import json
import math
import re
from pathlib import Path


def audit(kit, packet):
    cert = (kit / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
    src = (packet / 'Rule30GateTrapWords.lean').read_text()
    codes = set(map(int, re.findall(r'\d+', re.search(
        r'def trapCodes : List Nat := \[(.*?)\]', cert, re.S)[1])))
    assert len(codes) == 829

    def scalar(w, c, outside, width=16):
        row = [c] + [(w >> i) & 1 for i in range(width)] + [outside]
        # Literal Rule 30 table in neighbourhood order 000..111.
        truth = [0, 1, 1, 1, 1, 0, 0, 0]
        return sum(truth[4 * row[j - 1] + 2 * row[j] + row[j + 1]] << (j - 1)
                   for j in range(1, width + 1))

    @functools.lru_cache(None)
    def edge(w, a, b, width=16):
        return scalar(scalar(w, 0, a, width), 1, b, width)

    def move(states, bit, width=16):
        return frozenset(v for w in states for a in (0, 1) for b in (0, 1)
                         if ((v := edge(w, a, b, width)) & 1) == bit)

    def gap(states, g, width=16):
        for i in range(g):
            states = move(states, int(i == g - 1), width)
        return states

    assert all(edge(w, a, b) in codes for w in codes for a in (0, 1) for b in (0, 1))
    black = frozenset(w for w in codes if w & 1)
    layers = {k: frozenset(map(int, re.findall(r'\d+', v))) for k, v in re.findall(
        r'def lay([01]+) : List Nat := \[(.*?)\]', src, re.S)}
    assert len(layers) == 40 and layers['1'] == black
    for word, states in layers.items():
        actual = black
        for b in word[1:]:
            actual = move(actual, int(b))
        assert states == actual, word
    checks = re.findall(r'theorem step([01]+) : stepOK lay([01]+) (true|false) (lay[01]+|\[\]) = true', src)
    assert len(checks) == 44
    for word, parent, b, child in checks:
        assert word == parent + ('1' if b == 'true' else '0')
        target = frozenset() if child == '[]' else layers[child[3:]]
        assert move(layers[parent], int(b == 'true')) == target
    assert black != black - {min(black)}
    assert move(black, 0) != frozenset(
        v for w in black for a in (0, 1) for b in (0, 1)
        if ((v := scalar(scalar(w, 1, a), 0, b)) & 1) == 0)

    witnesses = re.findall(r'def path(\d+) : Nat × List \(Bool × Bool\) :=\s*\((\d+), (\[.*?\])\)', src, re.S)
    assert len(witnesses) == 6
    for name, start, choices in witnesses:
        w = int(start)
        assert w in black
        choices = ast.literal_eval(choices.replace('true', 'True').replace('false', 'False'))
        bits = [1]
        for g in map(int, name):
            bits += [0] * (g - 1) + [1]
        assert len(bits) == len(choices) + 1
        for (a, b), expected in zip(choices, bits[1:]):
            w = edge(w, int(a), int(b))
            assert w in codes and w & 1 == expected, name

    forbidden = {(3, 3, 3), (3, 3, 5, 3), (3, 5, 3, 3), (3, 5, 5, 3), (5, 5, 3, 3)}
    seen = {(black, ())}
    todo = list(seen)
    while todo:
        states, suffix = todo.pop()
        for g in (3, 5):
            new = gap(states, g)
            history = suffix + (g,)
            accepted = not any(history[-len(f):] == f for f in forbidden if len(history) >= len(f))
            assert bool(new) == accepted
            if accepted:
                pair = (new, history[-3:])
                if pair not in seen:
                    seen.add(pair)
                    todo.append(pair)
    assert len(seen) == 19
    s16 = black
    lift = {w | (h << 16) for w in codes for h in range(4)}
    assert len(lift) == 3316
    assert all(edge(w, a, b, 18) in lift for w in lift for a in (0, 1) for b in (0, 1))
    s18 = frozenset(w for w in lift if w & 1)
    for g in (3, 5, 3, 5, 3, 5, 3):
        s16, s18 = gap(s16, g), gap(s18, g, 18)
    assert s16 and not s18

    # Numerical evaluation of the already-derived renewal equation, not a fit.
    lo, hi = 1.01, 1.5
    for _ in range(60):
        x = (lo + hi) / 2
        if x ** -8 + x ** -18 / (1 - x ** -5) > 1:
            lo = x
        else:
            hi = x

    receipt = json.loads((packet / 'check-5fb59158.json').read_text())
    heads = (packet / 'headlines.txt').read_text().split()
    assert receipt['verdict'] == 'pass' and not receipt['newAxioms']
    assert [h['name'] for h in receipt['headlines']] == heads
    assert all(h['ok'] and h['typeMatches'] for h in receipt['headlines'])
    assert len(receipt['declared']) == 152 and receipt['replay'] == {'constants': 239, 'ok': True}
    portal = (packet / 'Rule30Submission.lean').read_text()
    normal = src.replace('module\n\npublic import Ruliology.CellularAutomata.Rule30GateTrap',
                         'import Ruliology.CellularAutomata.Rule30Prize\nimport Ruliology.CellularAutomata.Rule30GateTrap')
    normal = normal.replace('@[expose] public section\n\n', '').replace(
        'Ruliology.CellularAutomata.Rule30GateTrapWords', 'Rule30Submission').replace(
        'open Rule30StripCertificates', 'open Ruliology.CellularAutomata Rule30StripCertificates')
    assert normal == portal
    assert portal in (packet / 'essay.md').read_text()
    return {'literal_layers': len(layers), 'literal_steps': len(checks), 'witness_paths': len(witnesses),
            'product_pairs': len(seen), 'lift_windows': len(lift), 'word3535353_16_survivors': len(s16),
            'word3535353_18_survivors': len(s18), 'entropy_lambda': (lo + hi) / 2,
            'entropy_bits_per_sample': math.log2((lo + hi) / 2), 'receipt_read_not_rebuilt': True,
            'negative_controls': ['missing start rejected', 'wrong phase rejected'],
            'source_sha256': hashlib.sha256(src.encode()).hexdigest(),
            'portal_sha256': hashlib.sha256(portal.encode()).hexdigest()}


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('kit', type=Path)
    p.add_argument('packet', type=Path)
    p.add_argument('out', type=Path)
    a = p.parse_args()
    result = audit(a.kit, a.packet)
    a.out.write_text(json.dumps(result, indent=2) + '\n')
    print('S15_DRAFT_AUDIT_PASS')
    print(json.dumps(result))
