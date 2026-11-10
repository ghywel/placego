#!/usr/bin/env python3
"""GC2840: independent fixed width-5/6 K-02 relation checks; no census."""
import ast
import hashlib
import itertools
import json
import os
from pathlib import Path

OUT = Path(os.environ['CAPPED_OUT'])
KIT = Path(os.environ['K02_KIT_ROOT'])
ROOT = Path(__file__).resolve().parents[5]
PLAN = ROOT / 'tests/probes/swarm/sw02/carry/gpt_k02_plan.json'
for name, expected in json.loads(PLAN.read_text())['kit_sources_sha256'].items():
    assert hashlib.sha256((KIT / name).read_bytes()).hexdigest() == expected, name


def tick(word, left, right):
    padded = (left,) + word + (right,)
    return tuple((30 >> (4*a + 2*b + c)) & 1
                 for a, b, c in zip(padded, padded[1:], padded[2:]))


def encode(word):
    return sum(bit << i for i, bit in enumerate(word))


def read_list(width):
    source = KIT / ('lean/Ruliology/CellularAutomata/'
                    f'Rule30PeriodTwoWidth{width}.lean')
    line = next(s for s in source.read_text().splitlines()
                if s.startswith('def col1Forbidden :'))
    values = ast.literal_eval(line.split(':=', 1)[1].strip()
                             .replace('true', 'True').replace('false', 'False'))
    result = [''.join(str(int(x)) for x in row) for row in values]
    filed = (ROOT / ('tests/probes/swarm/sw02/carry/'
                     f'cloud_kit_col1Forbidden_width{width}.txt')).read_text().split()
    assert result == filed, 'ACTUAL_KIT_LIST_MISMATCH'
    return result


def graph(width):
    words = tuple(itertools.product((0, 1), repeat=width))
    succ = {}
    for word in words:
        targets = set()
        for r0, r1 in itertools.product((0, 1), repeat=2):
            y = tick(word, 0, r0)
            z = tick(y, 1, r1)
            # Separately written packed arithmetic, used only as an oracle.
            x = encode(word)
            middle = ((x << 1) ^ (x | ((x >> 1) | (r0 << (width-1))))) & ((1 << width)-1)
            packed = (((middle << 1) | 1) ^
                      (middle | ((middle >> 1) | (r1 << (width-1))))) & ((1 << width)-1)
            assert encode(z) == packed, 'SCALAR_PACKED_DISAGREEMENT'
            targets.add(z)
        succ[word] = targets
    return words, succ


def layers(word, start, succ):
    answer = [{x for x in start if x[0] == int(word[0])}]
    for ch in word[1:]:
        answer.append({y for x in answer[-1] for y in succ[x] if y[0] == int(ch)})
    return answer


def reachable(start, succ, allowed):
    seen = {start}
    todo = [start]
    while todo:
        for child in succ[todo.pop()]:
            if child in allowed and child not in seen:
                seen.add(child)
                todo.append(child)
    return seen


def run(width, expected_sizes):
    words, succ = graph(width)
    images = [set(words)]
    for _ in range(4):
        image = {y for x in images[-1] for y in succ[x]}
        if image == images[-1]:
            break
        assert image < images[-1]
        images.append(image)
    sizes = list(map(len, images))
    assert sizes == expected_sizes, ('IMAGE_SIZE', width, sizes)
    limit = images[-1]
    assert all(succ[x] <= limit for x in limit)
    reverse = {x: {y for y in limit if x in succ[y]} for x in limit}
    base = min(limit)
    assert reachable(base, succ, limit) == reachable(base, reverse, limit) == limit
    forbidden = read_list(width)
    if width == 6:
        forbidden += ['101010000']
    checks = {}
    for word in forbidden:
        path_layers = layers(word, limit, succ)
        assert not path_layers[-1], ('FORBIDDEN_WORD_READABLE', width, word)
        checks[word] = {'layers': [sorted(map(encode, x)) for x in path_layers],
                        'first_empty': next(i for i, x in enumerate(path_layers) if not x),
                        'earliest_image_with_no_path': next(i for i, x in enumerate(images)
                                                          if not layers(word, x, succ)[-1])}
    # Positive controls ensure that labels/empty-set rejection are not vacuous.
    assert all(layers(str(bit), limit, succ)[-1] for bit in (0, 1))
    positives = []
    for vertex in sorted(limit)[:4]:
        walk = [vertex]
        for _ in range(15):
            walk.append(min(succ[walk[-1]]))
        word = ''.join(str(x[0]) for x in walk)
        assert layers(word, limit, succ)[-1]
        positives.append(word)
    # Deliberate wrong clock at tick 1 must change at least one transition.
    mutation_differences = sum(tick(tick(x, 0, a), 0, b) != tick(tick(x, 0, a), 1, b)
                               for x in words for a, b in itertools.product((0, 1), repeat=2))
    assert mutation_differences > 0
    return {'width': width, 'image_sizes': sizes, 'limit': sorted(map(encode, limit)),
            'transitions': {str(encode(x)): sorted(map(encode, succ[x])) for x in sorted(limit)},
            'strongly_connected': True, 'forbidden': checks,
            'positive_words': positives, 'wrong_clock_differences': mutation_differences,
            'scalar_packed_cases': 4*len(words)}


answer = {'width5': run(5, [32, 20]), 'width6': run(6, [64, 38, 36])}
# Unexpected test, prediction recorded before execution: projection of the deeper
# stabilized image should be exactly the shallower stabilized image.
projection = sorted({x & 31 for x in answer['width6']['limit']})
answer['unexpected_projection'] = {'equals_width5_limit': projection == answer['width5']['limit'],
                                   'projected_size': len(projection)}
(OUT / 'k02.json').write_text(json.dumps(answer, indent=2) + '\n')
print('K02_FIXED_RELATION_CHECKS_PASS')
print(json.dumps({k: {'sizes': v['image_sizes'], 'scalar_packed_cases': v['scalar_packed_cases'],
                     'earliest_exclusions': {w:c['earliest_image_with_no_path']
                                             for w,c in v['forbidden'].items()}}
                  for k,v in answer.items() if k != 'unexpected_projection'}))
print(json.dumps(answer['unexpected_projection']))
