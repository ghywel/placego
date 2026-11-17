#!/usr/bin/env python3
"""GC549 entry-image probe; predictions written before first run, 2026-10-08.
Exact two-step spatial image of CP27's initial cylinder, not a trace census.
C1: 32 five-site bulk windows agree with independent decimal Rule30 updates.
C2: all sixteen initial states admit every output tail (no empty subset).
P1 blind: the CP27 frontier {1000,1001,1010,1011,1100} also admits all tails.
CF: state 1111 admits output 1; must fail (first output is forced zero).
Unexpected: retain a shortest missing tail and its exact subset path, if any.
Stop after 4096 reachable subsets. Failure to exhaust is not a pass.
OUTCOME (GPT, 2026-10-08): C1 PASS, 32 windows; C2 PASS, one closed subset;
P1 REFUTED, shortest missing tail 011 after eight discovered subsets;
CF REFUTED; unexpected subset path retained in GC549 checkpoint 28.
Single-party measurement, with a hand subset certificate below in the record.
REFUTED-BY: truth-table mismatch, empty all-state subset, or a missing P1 tail.
"""
from collections import deque
from itertools import product

STATES = set(product((0, 1), repeat=4))
ENTRY = {(1, 0, u, v) for u, v in product((0, 1), repeat=2)} | {(1, 1, 0, 0)}

def bulk(bits):
    a, b, c, d, e = bits
    return (a ^ (b | c)) ^ ((b ^ (c | d)) | (c ^ (d | e)))

def literal(bits):
    def one(a, b, c):
        return (30 >> (4*a+2*b+c)) & 1
    x = [one(*bits[i:i+3]) for i in range(3)]
    return one(*x)

def image(states, bit):
    return frozenset(s[1:] + (e,) for s in states for e in (0, 1)
                     if bulk(s + (e,)) == bit)

def explore(start):
    start = frozenset(start)
    queue, seen = deque([(start, '')]), {start}
    while queue:
        states, word = queue.popleft()
        for bit in (0, 1):
            after = image(states, bit)
            w = word + str(bit)
            if not after:
                return 'MISSING', w, len(seen)
            if after not in seen:
                if len(seen) == 4096:
                    return 'CAPPED', None, len(seen)
                seen.add(after); queue.append((after, w))
    return 'FULL', None, len(seen)

def labels(states):
    return sorted(''.join(map(str, s)) for s in states)

def main():
    for bits in product((0, 1), repeat=5):
        assert bulk(bits) == literal(bits), bits
    assert not image({(1, 1, 1, 1)}, 1)
    control = explore(STATES)
    assert control[0] == 'FULL', control
    result = explore(ENTRY)
    print('C1 PASS: 32 windows; C2 PASS:', control, '; CF REFUTED')
    print('P1:', result)
    if result[0] == 'MISSING':
        states = frozenset(ENTRY)
        print('unexpected start:', labels(states))
        for bit in result[1]:
            states = image(states, int(bit))
            print(bit, labels(states))
    elif result[0] == 'CAPPED':
        print('Unexpected check incomplete at declared subset cap')

if __name__ == '__main__':
    main()
