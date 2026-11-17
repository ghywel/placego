#!/usr/bin/env python3
"""expected_numbers.py: the expected outputs of the essay's Wolfram cells, computed independently in plain Python (no shared code with
the cells or the Lean module). The driven right half: cells 1..N, column 0 black at even times and white at odd times, rule 30
new(p) = old(p - 1) xor (old(p) or old(p + 1)). Run: python3 expected_numbers.py"""
def drive(cells, T):
    w = list(cells) + [0] * (T + 3); rows = [list(w)]
    for t in range(T):
        col0 = 1 if t % 2 == 0 else 0
        w = [(col0 if p == 0 else w[p - 1]) ^ (w[p] | (w[p + 1] if p + 1 < len(w) else 0)) for p in range(len(w))]
        rows.append(list(w))
    return rows
r31, r495 = drive([1, 1, 1, 1, 1], 30), drive([1, 1, 1, 1, 0, 1, 1, 1, 1], 30)
u31 = [r31[2 * s + 1][0] for s in range(12)]; u495 = [r495[2 * s + 1][0] for s in range(12)]
print('Cell 1 (visible columns, row of R31 at time 4):', [u31, u495, r31[4][:9]])
print('Cell 2 (rows at the trap entries, columns 1..19):', [r31[9][:19], r495[5][:19]])
ETHER = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
print('Cell 2 (ether columns 1..6 at phase 12):', [ETHER[(3 + p) % 7][12 % 4] for p in range(1, 7)])
def S(w):
    if w[:2] == [1, 0]: return [1, 1] + w[1:]
    if w[:2] == [1, 1]: return [1, 0] + w[1:]
    if w == [1]: return [1, 0]
    return w
chain = [[1]]
for _ in range(4): chain.append(S(chain[-1]))
def P(w):
    if w[:3] == [1, 1, 0]: return [1] + w[2:]
    if w[:3] == [1, 0, 1]: return [1, 1] + w[3:]
    if w == [1, 0]: return [1]
    return None
def root(w):
    while P(w) is not None: w = P(w)
    return w
print('Cell 3 (S-chain from [1], and the two roots):', [chain, root([1, 1, 1, 1, 1]), root([1, 1, 1, 1, 0, 1, 1, 1, 1][::-1])])
