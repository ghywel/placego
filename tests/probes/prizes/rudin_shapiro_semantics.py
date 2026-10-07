#!/usr/bin/env python3
"""Independent LSD repeat-language reconstruction; RSP-S preregistration.

Bulk results belong outside Git. No Walnut or Java is used by this checker.
"""
import argparse
from collections import deque
from itertools import product
import json
from pathlib import Path
import resource
from rudin_shapiro_repeat import read_machine

DIGITS = tuple(product((0, 1), repeat=3))
START = (0, 0, 0, 0, 0, 0)


def compare(old, left, right):
    return (left > right) - (left < right) if left != right else old


def advance(state, digits, s):
    h, k, parity, carry, lower, upper = state
    a, b, q = digits
    total = s + q + carry
    t, carry = total % 2, total // 2
    return (s, t, parity ^ (h*s) ^ (k*t), carry,
            compare(lower, a, s), compare(upper, s, b))


def accepts(state):
    # s<=b fits in the input width; s+q can need one further binary digit.
    h, k, parity, carry, lower, upper = advance(state, (0, 0, 0), 0)
    return carry == 0 and lower <= 0 and upper <= 0 and parity == 1


def literal(a, b, q):
    return q >= 1 and b >= a and all(
        bin(s & (s>>1)).count('1') % 2 == bin((s+q) & ((s+q)>>1)).count('1') % 2
        for s in range(a, b+1))


def lsd_repeat(a, b, q):
    states = frozenset((START,))
    width = max(1, max(a, b, q).bit_length())
    for i in range(width):
        digits = tuple((v >> i) & 1 for v in (a, b, q))
        states = frozenset(advance(st, digits, s) for st in states for s in (0, 1))
    return q >= 1 and b >= a and not any(accepts(st) for st in states)


def equivalence(machine):
    _, outputs, transitions = machine
    incoming = {}
    for (source, symbol), target in transitions.items():
        incoming.setdefault((target, symbol), set()).add(source)
    # Reversing MSD language: original accepting states become NFA starts.
    start = (frozenset(st for st, out in outputs.items() if out),
             frozenset((START,)), False, 0, False)
    parents, queue = {start: None}, deque((start,))
    while queue:
        node = queue.popleft()
        reverse, mismatch, positive_q, order, nonempty = node
        expected = positive_q and order <= 0 and not any(accepts(st) for st in mismatch)
        if nonempty and ((0 in reverse) != expected):
            word, at = [], node
            while parents[at] is not None:
                at, digits = parents[at]
                word.append(digits)
            word.reverse()
            values = tuple(sum(d[k] << i for i, d in enumerate(word)) for k in range(3))
            return dict(equivalent=False, states=len(parents), witness=values,
                        literal=literal(*values), reconstructed=expected,
                        exported=(0 in reverse))
        for digits in DIGITS:
            rev = frozenset(source for st in reverse
                            for source in incoming.get((st, digits), ()))
            bad = frozenset(advance(st, digits, s) for st in mismatch for s in (0, 1))
            a, b, q = digits
            target = (rev, bad, positive_q or bool(q), compare(order, a, b), True)
            if target not in parents:
                parents[target] = (node, digits)
                if len(parents) > 100000:
                    return dict(equivalent=None, states=len(parents), stopped='state limit')
                queue.append(target)
    return dict(equivalent=True, states=len(parents))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate', type=Path)
    args = parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    machine = read_machine(args.certificate)
    for values in product(range(16), repeat=3):
        assert lsd_repeat(*values) == literal(*values), values
    assert lsd_repeat(0, 1, 1) and not lsd_repeat(0, 2, 1)
    # Independently control digit recurrence through carry boundaries.
    for a, b in product(range(32), repeat=2):
        cmp = 0
        for i in range(6):
            cmp = compare(cmp, (a>>i)&1, (b>>i)&1)
        assert cmp == (a>b)-(a<b)
        st = START
        for i in range(6):
            st = advance(st, (0, 31, (b>>i)&1), (a>>i)&1)
        st = advance(st, (0, 0, 0), 0)
        assert st[2] == ((bin(a & (a>>1)).count('1') ^
                          bin((a+b) & ((a+b)>>1)).count('1')) % 2)
        assert st[3] == 0
    result = equivalence(machine)
    # Mutating acceptance at the initial state must expose the q=0 guard.
    tracks, outputs, transitions = machine
    changed = dict(outputs)
    changed[0] = 1 - changed[0]
    mutation = equivalence((tracks, changed, transitions))
    assert mutation['equivalent'] is False, mutation
    print(json.dumps(dict(result=result, mutation=mutation, literal_controls=4096,
                          arithmetic_controls=1024), indent=2))


if __name__ == '__main__':
    main()
