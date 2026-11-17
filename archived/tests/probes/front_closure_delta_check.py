#!/usr/bin/env python3
"""GC2386: small transition equivalence test, no phase/trajectory census.

Prediction/counterfactual: GPT-BOUNDARY-LAYER-REVIEW-20261102.md, GC2386.
Extract function definitions without executing either research script's main body.
"""
import ast
import json
from pathlib import Path
import time

import numpy as np


def extract(path, name, namespace):
    tree = ast.parse(path.read_text())
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(path), 'exec'), namespace)
    return namespace[name]


def literal(cl, win, width, bg, nxt):
    edges = set()
    fails = 0
    for unknown in range(4):
        offsets = range(-width - 2, 3)
        base = {j: bg(cl, j) for j in offsets}
        damage = {j: 0 for j in offsets}
        damage[0] = 1
        for j in range(width):
            damage[-1-j] = (win >> j) & 1
        damage[-width-1] = unknown & 1
        damage[-width-2] = unknown >> 1
        altered = {j: base[j] ^ damage[j] for j in offsets}
        step = lambda x, j: x[j] ^ (x[j-1] | x[j-2])
        new = {j: step(base, j) ^ step(altered, j) for j in range(-width, 3)}
        support = [j for j in new if new[j]]
        if not support:
            fails += 1
            continue
        advance = max(support)
        # Enumerate whole candidate windows and filter by every known output.
        for candidate in range(1 << width):
            if all(advance-1-j not in new or ((candidate >> j) & 1) == new[advance-1-j]
                   for j in range(width)):
                edges.add((nxt(cl, advance), candidate, advance))
    return edges, fails


def main():
    start = time.process_time()
    here = Path(__file__).resolve().parent
    bg = lambda cl, offset: (0b1011010010011 >> ((cl + 3 * offset) % 13)) & 1
    nxt = lambda cl, advance: (cl + 1 + 3 * advance) % 8
    successor = extract(here / 'front_closure.py', 'successors', {'bg': bg, 'nxt': nxt})
    builder = extract(here / 'front_cert.py', 'build_generic', {'np': np})
    checked, rows = 0, []
    for width in range(1, 5):
        count, sources, dests, advances, total_fails = builder(8, bg, nxt, width)
        old = [set() for _ in range(count)]
        for source, dest, advance in zip(sources, dests, advances):
            old[int(source)].add((int(dest) >> width, int(dest) % (1 << width), int(advance)))
        failures = 0
        for cl in range(8):
            for win in range(1 << width):
                actual, bad = successor(cl, win, width)
                expected, expected_bad = literal(cl, win, width, bg, nxt)
                assert actual == expected == old[(cl << width) | win]
                assert bad == expected_bad
                failures += bad
                checked += 1
        assert failures == total_fails
        rows.append({'width': width, 'states': count, 'distinct_edges': sum(map(len, old)),
                     'fail_branches': failures})
    # Exact format conversion for all 256 near-front bytes.
    for byte in range(256):
        word = (byte << 24) | 0x543210
        expected = sum(((word >> (31-j)) & 1) << j for j in range(8))
        converted = int(f'{word >> 24:08b}'[::-1], 2)
        assert converted == expected
    print(json.dumps({'status': 'PASS', 'states_checked': checked, 'tables': rows,
                      'byte_order_cases': 256, 'cpu_seconds': time.process_time() - start,
                      'scope': 'transition-function audit; not a reconstruction of the reported W8 closures'}, indent=2))


if __name__ == '__main__':
    main()
