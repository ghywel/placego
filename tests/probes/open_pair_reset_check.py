#!/usr/bin/env python3
"""GC2393: 64 literal two-row controls; no trajectory census or symbolic engine.

Prediction and scope: reports/GPT-OPEN-STRETCH-REVIEW-20261102.md.
Also reproduces T45's unresolved-scan sentinel bug without running its driver.
"""
import ast
import itertools
from pathlib import Path

R = 12
MASK = (1 << 24) - 1


def step(x):
    return (x ^ ((x << 1) | (x << 2) | 3)) & MASK


images = {}
for b, c, d, z, u, v in itertools.product((0, 1), repeat=6):
    e = (d << (R-2)) | (c << (R-1)) | (b << R) | (z << (R+2)) | (z << (R+3))
    x = e ^ (1 << R) ^ (u << (R-1)) ^ (v << (R-2))
    e1, x1 = step(e), step(x)
    m1 = e1 ^ x1
    assert m1.bit_length()-1 == R+2
    pair1 = ((m1 >> (R+1)) & 1, (m1 >> R) & 1)
    assert pair1 == ((1-c) ^ (b*u), 1 ^ ((1-d)*u) ^ ((1-c)*v) ^ (u*v))
    m2 = step(e1) ^ step(x1)
    assert m2.bit_length()-1 == R+4
    pair2 = ((m2 >> (R+3)) & 1, (m2 >> (R+2)) & 1)
    images.setdefault((b, c, d, z), set()).add(pair2)
    if b == 0:
        assert pair2 == ((1-c)*(1-z), c | d)
for (b, c, d, z), pairs in images.items():
    assert len(pairs) == (1 if b == 0 else (2 if z == 1 else 3))
print('PASS: 64 literal controls; two-step reset iff b=0; b=1 countercontrols retained')

# Extract only the two pure scan functions, never execute the trajectory driver.
source = Path(__file__).with_name('blocked_reading.py').read_text()
nodes = [n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)
         and n.name in ('new_front', 'reading_depth')]
ns = {'NB': 10}
exec(compile(ast.Module(body=nodes, type_ignores=[]), 'blocked_reading_scan', 'exec'), ns)
eb = list(map(int, '01010010010'))
xb = list(map(int, '10001001001'))
eo = {-j: val for j, val in enumerate(eb)}
eo.update({1: 1, 2: 0})
dfull = [None] + [eb[j] ^ xb[j] for j in range(1, 11)]
erow = (1 << (R+1)) | sum(val << (R-j) for j, val in enumerate(eb))
xrow = (1 << (R+1)) | sum(val << (R-j) for j, val in enumerate(xb))
assert (step(erow) ^ step(xrow)).bit_length()-1 == R-10
assert ns['new_front'](eo, dfull) is None
observed = ns['reading_depth'](eo, dfull)
assert observed == (10, None), ('Sentinel behavior changed; review the fix', observed)
print('CONFIRMED existing sentinel bug: unresolved local scan is labelled (10, None)')
