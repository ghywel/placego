#!/usr/bin/env python3
"""GC852 one-sided 56-row wheel audit, width-four relaxation only.
Predictions and controls were registered in CLOUD-LOCAL.md before the scratch
calculation: start forcing need not follow from centred forcing; white visible
bits fix column2; reversed word is an unexpected orientation check.
OUTCOME: column2 ambiguous at phases9,19,29,39,55; all forward phases viable.
Reversed 56-words have no path at any aligned phase. Positive relaxed paths are
not claimed full right-half realizations. No source shared with core probes.
"""
from itertools import product
U = '00010011010001001101000100110100010011010001001101001101'
A = set(product((0, 1), repeat=4))
F = dict(zip(product((1, 0), repeat=3), (0, 0, 0, 1, 1, 1, 1, 0)))

def step(x, w, u):
    return tuple(F[(w if j == 0 else x[j-1], x[j],
                    u if j == 3 else x[j+1])] for j in range(4))

def backward(word, phase):
    S = {x for x in A if x[0] == int(word[-1])}
    for t in range(len(word)-2, -1, -1):
        S = {x for x in A if x[0] == int(word[t]) and
             any(step(x, (phase+t) % 2, u) in S for u in (0, 1))}
    return S

def forward(word, phase):
    paths = {(x, x) for x in A if x[0] == int(word[0])}
    for t in range(len(word)-1):
        paths = {(start, y) for start, x in paths for u in (0, 1)
                 for y in [step(x, (phase+t) % 2, u)]
                 if y[0] == int(word[t+1])}
    return {start for start, end in paths}

def check():
    ambiguous = {j: [] for j in (1, 2, 3)}
    for p in range(56):
        word = ''.join(U[(p+t) % 56] for t in range(56))
        S = backward(word, p)
        assert S and S == forward(word, p)
        for j in ambiguous:
            if len({x[j] for x in S}) > 1:
                ambiguous[j].append(p)
        if U[p] == '0':
            assert {x[1] for x in S} == {int(U[(p+1) % 56]) ^ (p % 2)}
        assert not backward(word[::-1], p)
        assert not forward(word[::-1], p)
    assert ambiguous[1] == [9, 19, 29, 39, 55]
    assert [len(ambiguous[j]) for j in (1, 2, 3)] == [5, 27, 44]
    print('GC852 PASS: backward and forward paths agree; ambiguities 5,27,44; reversed words empty')

if __name__ == '__main__':
    check()
