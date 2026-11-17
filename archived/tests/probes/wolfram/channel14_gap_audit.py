#!/usr/bin/env python3
"""GC2208: fixed source-bound graph audit, not a language or SAT census.

Read the existing 919-state certificate; no state regeneration or Lean build.
Find the shortest rejected rooted S/L word by number of complete gap blocks,
and compare the two old L590 exclusions with the certificate. Independent
oracle: all 14-bit windows, literal Rule30 truth table, arbitrary right inputs.
This oracle is the same finite-width relaxation, not full CA realizability.
Predictions/stops are frozen in reports/rule30-clocked-gap-interface.md.
"""
import ast
from collections import deque
import hashlib
import json
from pathlib import Path
import time

START = time.monotonic()
ROOT = Path(__file__).resolve().parents[3]
REL = 'reports/wolfram-agents/submissions/channel-14/Rule30Submission.lean'
EXPECTED = '7559970244b025c1733a9fc98f1f16a2583366ff8d70edb5cfda50bd71f42fd7'
BLOCK = {'S': '001', 'L': '00001'}
DEAD = 1000000
M, MASK = 14, (1 << 14) - 1
F1 = '010010010000100001001001000010000100001001'
F2 = '001001000010000100001000010010000100001001'


def guard():
    assert time.monotonic() - START < 240, 'internal wall stop'


data = (ROOT / REL).read_bytes()
assert len(data) < 8 * 1024**2
assert hashlib.sha256(data).hexdigest() == EXPECTED
line = next(s for s in data.decode().splitlines() if s.startswith('def succ14 :'))
succ = ast.literal_eval(line.split(':=', 1)[1].strip())
assert len(succ) == 919
assert all(len(pair) == 2 and all(0 <= x < 919 or x == DEAD for x in pair) for pair in succ)


def trace(word, initial=0):
    q, path = initial, [initial]
    for b in word:
        q = DEAD if q == DEAD else succ[q][int(b)]
        path.append(q)
    return q, path


def spell(macro):
    return '1' + ''.join(BLOCK[b] for b in macro)


# BFS on gap-boundary states. First rejected edge gives minimum macro length.
q1, _ = trace('1')
todo, seen = deque([(q1, '')]), {q1}
shortest = None
while todo and shortest is None:
    q, macro = todo.popleft()
    for b, bits in BLOCK.items():
        r, _ = trace(bits, q)
        if r == DEAD:
            shortest = macro + b
            break
        if r not in seen:
            seen.add(r)
            todo.append((r, macro + b))
    guard()
assert shortest is not None, 'certificate unexpectedly admits every gap word'
assert len(spell(shortest)) <= 256, 'oracle horizon stop; do not widen'

# Fixed offered <=8-block question. Counts are in the relaxation only.
counts, live = [], {q1: 1}
for n in range(1, 9):
    nxt = {}
    for q, count in live.items():
        for bits in BLOCK.values():
            r, _ = trace(bits, q)
            if r != DEAD:
                nxt[r] = nxt.get(r, 0) + count
    live = nxt
    counts.append({'gaps': n, 'accepted': sum(live.values()), 'total': 2**n})

# Literal rule table is independent of the packed formula used by the source.
RULE = (0, 1, 1, 1, 1, 0, 0, 0)  # index 4*left+2*centre+right


def literal(s, wall, right):
    out = 0
    for p in range(M):
        left = wall if p == 0 else (s >> (p - 1)) & 1
        centre = (s >> p) & 1
        rr = right if p == M - 1 else (s >> (p + 1)) & 1
        out |= RULE[4 * left + 2 * centre + rr] << p
    return out


def packed(s, wall, right):
    return (((s << 1) | wall) ^ (s | (s >> 1) | (right << (M - 1)))) & MASK


images, comparisons = [], 0
for s in range(1 << M):
    row = []
    for u in range(2):
        a = literal(s, 0, u)
        assert a == packed(s, 0, u)
        for v in range(2):
            b = literal(a, 1, v)
            assert b == packed(packed(s, 0, u), 1, v)
            row.append(b)
            comparisons += 1
    images.append(tuple(row))
    if s % 256 == 0:
        guard()


def oracle(word):
    state, sizes = set(range(1 << M)), []
    for b in word:
        state = {r for s in state if (s & 1) == int(b) for r in images[s]}
        sizes.append(len(state))
        guard()
    return bool(state), sizes


cases = {
    'empty': '', 'negative_11': '11', 'negative_00000': '00000',
    'pure_S': spell('S' * 8), 'pure_L': spell('L' * 8),
    'old_f1': F1, 'old_f2': F2,
    'startup_u': F1[1:], 'startup_0v': F2[1:], 'startup_v': F2[2:],
    'shortest': spell(shortest),
}
results = {}
for name, word in cases.items():
    q, path = trace(word)
    actual, sizes = oracle(word)
    assert actual == (q != DEAD), ('graph/oracle mismatch', name)
    results[name] = {'word': word, 'accepted': actual, 'final_state': q,
                     'first_dead_symbol': next((i for i, x in enumerate(path) if x == DEAD), None),
                     'oracle_sizes': sizes, 'path': path}
assert not results['negative_11']['accepted'] and not results['negative_00000']['accepted']
assert all(results[k]['accepted'] for k in ('empty', 'pure_S', 'pure_L', 'startup_u', 'startup_0v', 'startup_v'))
assert not results['shortest']['accepted']
print(json.dumps({
    'status': 'PASS', 'scope': 'existing width14 relaxation only',
    'lean_source_sha256': EXPECTED,
    'probe_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'shortest_macro': shortest, 'shortest_gap_count': len(shortest),
    'bfs_seen_before_first_rejection': len(seen),
    'counts_through_8': counts, 'literal_packed_comparisons': comparisons,
    'predictions': {'P1_rejection_by_8': len(shortest) <= 8,
                    'P2_old_f1_f2_both_missed': results['old_f1']['accepted'] and results['old_f2']['accepted']},
    'cases': results, 'elapsed_seconds': time.monotonic() - START,
}, indent=2))
