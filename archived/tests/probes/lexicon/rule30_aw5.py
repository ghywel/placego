#!/usr/bin/env python3
"""rule30_aw5.py: AW5, a positive search for AW4's ten undecided pairs at P = 10 (Local's run; claimed in CLOUD-LOCAL.md
with these predictions pushed before the script was run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_aw5.py
COST:       minutes; caps 1,800 CPU s, 2,000,000 reachable pairs per start.

AW4 left ten pairs of 10-periodic columns 0, 1 undecided at strip width 18, each with an odd row-0 run of 9 in its
forced left half. A strip test can only refute. This script searches for a POSITIVE certificate: a right continuation
whose columns are all 10-periodic. From the pair (c0, c1), the next column w must satisfy c1(t + 1) = c0(t) XOR
(c1(t) OR w(t)) for every t; where c1(t) = 1 this needs c1(t + 1) = c0(t) XOR 1 and leaves w(t) free, and where
c1(t) = 0 it fixes w(t). Explore every pair reachable from the start (breadth first, capped), prune to the states
with an infinite path, and report whether the start survives. A surviving start has a real right continuation (a
path into a cycle of 10-periodic columns), so its odd run of 9 occurs on an actual wall and entry 06's actual odd
maximum at P = 10 is exactly 9. A start that dies has no 10-periodic continuation, which is not a refutation (AW's
lesson: periods 10h, h > 1, are not searched).

PREDICTIONS, Local's, published before the run:
  A5-P1 (blind, uncertain): at least one of the ten pairs has a 10-periodic right continuation (actual odd 9 at P = 10).
  A5-C1 (control): the same search certifies a pair AW found admissible at P = 5 and rejects GPT's 01/11 at P = 2.
  A5-C2 (control): every certified continuation is checked column by column against the literal equation along an
        explicit path into its cycle.
FIRST RUN (18:22, at 087935c) CRASHED on a print-format error in the A5-C1 line (a 2-tuple passed to a single %s),
before any prediction was evaluated or printed; that line was fixed and the script rerun once.
OUTCOME, 2026-10-07 18:22 (M5, the rerun; CPU 0.1 s, no cap). A5-C1 PASS (01/11 rejected; the AW-admissible P = 5
pair (1, 25) certified with a literal witness path). A5-C2 PASS. A5-P1 REFUTED: none of the ten P = 10 survivors has a
10-periodic right continuation; every reachable graph was explored completely (4,023 to 9,208 pairs) and pruned to
nothing. This does not refute them: a continuation of period 10h, h > 1, or a non-periodic one, is not searched here.
"""
import resource
import sys
from collections import deque

CAP_CPU, CAP_NODES = 1800.0, 2_000_000
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
    while q:
        if len(seen) > CAP_NODES or cpu() > CAP_CPU:
            return None, len(seen), None
        u, v = q.popleft()
        order.append((u, v))
        nxt[(u, v)] = [(v, w) for w in succ(u, v, P)]
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


c1ok = True
r, n, wit = search(0b10, 0b11, 2)
c1ok &= r is False
adm5 = None
for a in range(1, 32):                                     # a P = 5 pair that AW counted admissible
    for b in range(32):
        rr, nn, ww = search(a, b, 5)
        if rr:
            adm5 = (a, b, ww)
            break
    if adm5:
        break
c1ok &= adm5 is not None and check_path(adm5[2][0], adm5[2][1], 5)
print('A5-C1', 'PASS' if c1ok else 'FAIL', '(01/11 rejected; P = 5 pair %s certified)' % (str(adm5[:2]) if adm5 else 'none'))
certified, c2ok = [], True
for c0, c1 in SURVIVORS:
    r, n, wit = search(c0, c1, 10)
    tag = 'CAP' if r is None else ('certified' if r else 'no 10-periodic continuation')
    if r:
        ok = check_path(wit[0], wit[1], 10)
        c2ok &= ok
        certified.append((c0, c1, len(wit[0])))
        tag += ' (path %d columns, literal %s)' % (len(wit[0]) + 1, 'PASS' if ok else 'FAIL')
    print('P = 10 pair (%d, %d): reachable pairs %d: %s' % (c0, c1, n, tag))
print('A5-C2', 'PASS' if c2ok else 'FAIL')
print('A5-P1', 'HELD' if certified else 'REFUTED', '(%d of 10 certified)' % len(certified))
print('CPU %.1f s, peak RSS %.1f MiB' % (cpu(), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20))
