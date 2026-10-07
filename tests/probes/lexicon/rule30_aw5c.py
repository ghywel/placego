#!/usr/bin/env python3
"""rule30_aw5c.py: AW5c, longer-period positive search for AW4's ten P = 10 survivors (Local's run; claimed in
CLOUD-LOCAL.md with these predictions pushed before the script was run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_aw5c.py
COST:       up to 30 minutes; caps 1,800 CPU s in all, 3,000,000 reachable pairs and 5,000,000 stored edges
            per start (memory, about 350 MiB).

AW5 found no 10-periodic right continuation for the ten survivors, and AW5b found their strips alive at width 24 with
millions of states. A continuation of period 10h (h > 1) would still certify them actual. This script repeats AW5's
search (unchanged functions) on the doubled pair at period 20, then on the tripled pair at period 30, for each
survivor in turn until the CPU cap. A surviving start gives a literal witness path into a cycle of 20- or 30-periodic
columns: a real right continuation, so entry 06's actual odd maximum at P = 10 would be exactly 9.

PREDICTIONS, Local's, published before the run:
  A5c-P1 (blind, uncertain): at least one survivor has a 20-periodic right continuation.
  A5c-P2 (blind, uncertain): if none at period 20, at least one has a 30-periodic continuation.
  A5c-C1 (control): AW5's certified P = 5 pair (1, 25), doubled to period 10, is certified again here.
Caps hit leave a pair undecided; a start that dies without a cap has no continuation of that period only.
OUTCOME: not yet run.
"""
import resource
import sys
from collections import deque

CAP_CPU, CAP_NODES, CAP_EDGES = 1800.0, 3_000_000, 5_000_000
SURVIVORS = [(146, 155), (155, 717), (187, 210), (210, 146), (263, 496), (351, 577), (496, 351), (577, 638),
             (717, 884), (884, 263)]


def cpu():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime + r.ru_stime


def succ(u, v, P):
    full = (1 << P) - 1
    need = ((v >> 1) | (v << (P - 1))) & full ^ u          # bit t: v(t + 1) XOR u(t)
    if v & ~need & full:
        return []
    base = need & ~v & full
    out, sub = [], v
    while True:                                            # every subset of v's black bits is free
        out.append(base | sub)
        if sub == 0:
            break
        sub = (sub - 1) & v
    return out


def literal(u, v, w, P):
    bit = lambda x, t: (x >> (t % P)) & 1
    return all(bit(v, t + 1) == bit(u, t) ^ (bit(v, t) | bit(w, t)) for t in range(P))


def search(c0, c1, P):
    start = (c0, c1)
    seen, order, q = {start}, [], deque([start])
    nxt = {}
    edges = 0
    while q:
        if len(seen) > CAP_NODES or edges > CAP_EDGES or cpu() > CAP_CPU:
            return None, len(seen), None
        u, v = q.popleft()
        order.append((u, v))
        nxt[(u, v)] = [(v, w) for w in succ(u, v, P)]
        edges += len(nxt[(u, v)])
        for s in nxt[(u, v)]:
            if s not in seen:
                seen.add(s)
                q.append(s)
    alive = set(order)
    changed = True
    while changed:
        changed = False
        for n in list(alive):
            if not any(m in alive for m in nxt[n]):
                alive.discard(n)
                changed = True
    if start not in alive:
        return False, len(seen), None
    path, cur, steps = [start], start, 0                   # a witness path into a cycle, for the literal check
    visited = {start: 0}
    while True:
        cur = next(m for m in nxt[cur] if m in alive)
        steps += 1
        if cur in visited:
            break
        visited[cur] = steps
        path.append(cur)
    return True, len(seen), (path, cur)


def check_path(path, cyc_start, P):
    cols = [path[0][0]] + [p[1] for p in path] + [cyc_start[1]]
    return all(literal(cols[i], cols[i + 1], cols[i + 2], P) for i in range(len(cols) - 2))



rep = lambda w, P, h: sum(w << (P * i) for i in range(h))
r, n, wit = search(rep(1, 5, 2), rep(25, 5, 2), 10)
c1 = bool(r) and check_path(wit[0], wit[1], 10)
print('A5c-C1', 'PASS' if c1 else 'FAIL')
found = {20: [], 30: []}
for h, P2 in ((2, 20), (3, 30)):
    for c0, c1w in SURVIVORS:
        if cpu() > CAP_CPU:
            print('CPU cap reached; stopping at period %d' % P2)
            break
        r, n, wit = search(rep(c0, 10, h), rep(c1w, 10, h), P2)
        tag = 'CAP' if r is None else ('certified' if r else 'no %d-periodic continuation' % P2)
        if r:
            ok = check_path(wit[0], wit[1], P2)
            tag += ' (witness path %d columns, literal %s)' % (len(wit[0]) + 1, 'PASS' if ok else 'FAIL')
            if ok:
                found[P2].append((c0, c1w))
        print('period %d: pair (%d, %d): reachable pairs %d: %s' % (P2, c0, c1w, n, tag))
        sys.stdout.flush()
    if found[P2]:
        break
print('A5c-P1', 'HELD' if found[20] else 'REFUTED or undecided', found[20])
print('A5c-P2', ('HELD' if found[30] else 'REFUTED or undecided') if not found[20] else 'not reached', found[30])
print('CPU %.1f s, peak RSS %.1f MiB' % (cpu(), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20))
