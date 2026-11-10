#!/usr/bin/env python3
"""One fixed period-eight witness for door1; no classification or larger-period search.

Independent scalar Rule30 checks close a spatial lasso beginning with the already
reported columns00010001 and01110000 (time increases from left to right).
Strict cap512 pairs; failure means no carry, never a larger retry.
"""
import json

P = 8
START = (136, 14)
CAP = 512


def ok(a, b, c):
    return all(((b >> ((t + 1) % P)) & 1) ==
               (((a >> t) & 1) ^ (((b >> t) & 1) | ((c >> t) & 1)))
               for t in range(P))


def successors(a, b):
    fixed = 0
    for t in range(P):
        rhs = ((b >> ((t + 1) % P)) & 1) ^ ((a >> t) & 1)
        if (b >> t) & 1:
            if rhs != 1:
                return []
        else:
            fixed |= rhs << t
    return [(b, c) for c in range(256) if c & ~b == fixed]


grey, black, path = {}, set(), []
visited = set()


def dfs(st):
    if st in grey:
        return path[:] + [st], grey[st]
    if st in black:
        return None
    visited.add(st)
    assert len(visited) <= CAP, 'fixed pair cap reached'
    grey[st] = len(path)
    path.append(st)
    for nx in successors(*st):
        assert st[1] == nx[0] and ok(st[0], st[1], nx[1])
        found = dfs(nx)
        if found is not None:
            return found
    path.pop()
    del grey[st]
    black.add(st)
    return None


# Positive control: all seven ether columns, read through two temporal periods.
ether = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1],
         [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
e = [sum(row[t % 4] << t for t in range(8)) for row in ether]
assert all(ok(e[j], e[(j + 1) % 7], e[(j + 2) % 7]) for j in range(7))
assert START[0] == e[5]
assert not any(all(((START[1] >> t) & 1) == ((START[1] >> ((t + q) % 8)) & 1)
                  for t in range(8)) for q in range(1, 8))
found = dfs(START)
assert found is not None, 'no lasso found within fixed search'
states, back = found
assert states[-1] == states[back]
assert all(x[1] == y[0] and ok(*x, y[1]) for x, y in zip(states, states[1:]))
# Negative control: flip the first cell of the proposed third column and keep
# its neighbours. The fixed lasso must cease satisfying the recurrence.
assert not ok(*states[0], states[1][1] ^ 1)
print(json.dumps({'result': 'PASS', 'start': START, 'period': P,
                  'pairs_visited': len(visited), 'cycle_back': back,
                  'cycle_length': len(states) - 1 - back, 'pair_lasso': states,
                  'ether_control': True, 'mutated_cell_rejected': True}))
