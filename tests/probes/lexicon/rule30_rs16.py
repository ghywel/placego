#!/usr/bin/env python3
"""rule30_rs16.py: RS16, a census of GPT's named pulse starts (GC326, GC334, GC335) by separation on the actual
rooted tree through period 16 (Local's run, offered in L210; claimed in CLOUD-LOCAL.md with these predictions pushed
before the script was run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_rs16.py
COST:       under a minute; cap 300 CPU s.

A named start is a full pair (e_s + e_(s+r), e_s) up to rotation, 1 <= r <= q - 1, at common period q: a two-black
predecessor over a singleton driver contained in it. Every rooted history is walked at common period 16 in absolute
time from TM5b's root (x, y) = (0, all ones) at depth 0 (rotation children once, genuine branches both ways, to each
history's exit to period 32). At every state the least pair period p is computed and the start test is made on the
p-bit words, so starts at periods 1, 2, 4, 8 and 16 are all seen at their own period. For each start: depth, p, r, and
which histories pass through it.

PREDICTIONS, Local's, published before the run (blind unless marked):
  RS-C0 (control, TM5b): 16 histories, exits as in TM5b.
  RS-C1 (control, G156): on every history each (p, r) class occurs at most once.
  RS-C2 (control): GC326's start, (320, 64) at depth 725,146 with p = 16 and r = 2, is found, on exactly two histories.
  RS-P1 (blind, uncertain): at p = 16 the whole rooted tree has at most 5 distinct start nodes.
  RS-P2 (blind, uncertain): no p = 16 start has r = 1 or r = 13 (the joined q - 3 group is absent at q = 16).
OUTCOME: not yet run.
"""
import os
import resource
import sys

sys.path.insert(0, os.path.dirname(__file__))
import rule30_rq3 as rq3

Q = 16


def cpu():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime + r.ru_stime


def least_pair_period(x, y):
    for p in (1, 2, 4, 8, 16):
        if rq3.rot(x, p, Q) == x and rq3.rot(y, p, Q) == y:
            return p


def start_sep(x, y, p):
    """r if (x, y) restricted to p bits is (e_s + e_(s+r), e_s), else None."""
    m = (1 << p) - 1
    xs, ys = x & m, y & m
    if bin(ys).count('1') != 1 or bin(xs).count('1') != 2 or (xs & ys) != ys:
        return None
    s = ys.bit_length() - 1
    other = (xs ^ ys).bit_length() - 1
    return (other - s) % p


starts = {}                                        # (depth, x, y) -> (p, r, set of history ids)
stack = [(0, (1 << Q) - 1, 0, ())]
paths = []
while stack:
    x, y, d, path = stack.pop()
    path = list(path)
    while True:
        if cpu() > 300:
            print('CAP')
            sys.exit(1)
        if x and y:
            p = least_pair_period(x, y)
            r = start_sep(x, y, p)
            if r is not None:
                path.append((d, x, y, p, r))
        if y == 0:
            kids = rq3.children(x, 0, Q)
            if not kids:
                paths.append((d, path))
                break
            c1, c2 = kids
            if not any(rq3.rot(c1, k, Q) == c2 for k in range(Q)):
                stack.append((0, c2, d + 1, tuple(path)))
            x, y, d = 0, c1, d + 1
            continue
        x, y, d = y, rq3.children(x, y, Q)[0], d + 1

c1 = True
for i, (exitd, path) in enumerate(paths):
    cls = [(p, r) for d, x, y, p, r in path]
    c1 &= len(cls) == len(set(cls))
    for d, x, y, p, r in path:
        starts.setdefault((d, x, y), [p, r, set()])[2].add(i)
print('histories', len(paths), '(TM5b: 16)')
TM5B_N5 = [87867, 183184, 196189, 229338, 253537, 271596, 291257, 527724, 551910, 555813, 575211, 634886, 645655,
           667052, 770532, 894235]
c0 = sorted(d + 1 for d, path in paths) == TM5B_N5
print('RS-C0', 'PASS' if c0 else 'FAIL')
print('RS-C1', 'PASS' if c1 else 'FAIL')
c2 = (725146, 320, 64) in starts and starts[(725146, 320, 64)][:2] == [16, 2] and len(starts[(725146, 320, 64)][2]) == 2
print('RS-C2', 'PASS' if c2 else 'FAIL')
by_p = {}
for (d, x, y), (p, r, hs) in sorted(starts.items()):
    by_p.setdefault(p, []).append((d, r, len(hs)))
for p in sorted(by_p):
    print('p = %d: %d start nodes; (depth, r, histories): %s' % (p, len(by_p[p]), by_p[p]))
s16 = by_p.get(16, [])
print('RS-P1', 'HELD' if len(s16) <= 5 else 'REFUTED', '(%d start nodes at p = 16)' % len(s16))
print('RS-P2', 'HELD' if not any(r in (1, 13) for d, r, n in s16) else 'REFUTED')
print('CPU %.1f s' % cpu())
