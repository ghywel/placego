#!/usr/bin/env python3
"""GC1025: bounded early-perturbation diagnostic on the retained L596 witness.

Predictions in RULE30-GPT.md before execution. Exactly45 single/pair flips
in sites1..9, fixed remaining right half and clock. All break the visible
train; no carrier isolated and no expansion of the mutation search.
Literal shrinking cones independently check every packed trajectory.
The separate CL193 retained model is replayed as the requested positive
membership gate for GC1024, with its site21 negative control.
"""
import itertools
import re
from pathlib import Path


def evidence(heading):
    root = Path(__file__).resolve().parents[3]
    for p in sorted(root.glob('CHAT-LEDGER*.md')):
        s = p.read_text()
        m = re.search(r'^## ' + heading + r'\b.*?(?=^## |\Z)', s, re.M | re.S)
        if m:
            return re.findall(r'`([01]{80,})`', m.group())
    raise RuntimeError('missing public evidence ' + heading)


def packed(seed, steps):
    out = []
    for t in range(steps+1):
        if t % 2 == 0:
            out.append(str(seed & 1))
        seed = ((seed << 1) | (t % 2)) ^ (seed | (seed >> 1))
    return ''.join(out)


def literal(seed, steps):
    row = [(seed >> i) & 1 for i in range(steps+1)]
    out = []
    for t in range(steps+1):
        if t % 2 == 0:
            out.append(str(row[0]))
        p = [t % 2] + row
        row = [(30 >> (4*p[j]+2*p[j+1]+p[j+2])) & 1
               for j in range(len(row)-1)]
    return ''.join(out)


def encode(s):
    return sum(int(b) << i for i, b in enumerate(s))


def main():
    _, right, visible = evidence('L596')[:3]
    seed = encode(right)
    assert packed(seed, 168) == literal(seed, 168) == visible
    assert visible[5:27] == '10'*11
    kept, first_fail = [], []
    for k in (1, 2):
        for flip in itertools.combinations(range(9), k):
            r = seed
            for i in flip:
                r ^= 1 << i
            v = packed(r, 168)
            assert v == literal(r, 168)
            if v[5:27] == visible[5:27]:
                kept.append(flip)
            else:
                first_fail.append(next(i for i in range(5, 27) if v[i] != visible[i]))
    assert len(first_fail) == 45 and not kept
    assert packed(seed ^ (1 << 169), 168) == visible
    print('45/45 early perturbations break train; first differing visible indices',
          sorted(set(first_fail)), '; no surviving carrier selected')
    right = evidence('CL193')[0]
    target = '000010001010000' + '10'*13 + '0010000101'
    seed = encode(right)
    assert len(right) == 101 and len(target) == 51
    assert packed(seed, 100) == literal(seed, 100) == target
    assert literal(seed ^ (1 << 20), 100) != target
    print('CL193 positive model and site21 negative control PASS')


if __name__ == '__main__':
    main()
