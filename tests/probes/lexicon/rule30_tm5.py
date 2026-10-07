#!/usr/bin/env python3
"""rule30_tm5.py: TM5, the whole-tree minimum of N_5 over all rooted histories (Local's run, on the quantifier
question of G184's continuation and GC233/L150; claimed in CLOUD-LOCAL.md, with these predictions pushed before the
script was run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_tm5.py
COST:       seconds expected; caps 300 CPU s, 512 MiB peak RSS, 5,000,000 walk steps, 256 histories. The first cap
            hit stops the run, which is then partial and certifies nothing about the minimum.

Domain. Temporal words of period Q = 16 (bit t is time t; S c means c(t + 1)). The root (0, 1^16) is at depth 0 and
the state at depth d is the pair (w_(d-1), w_d). A child of (a, b) is a Q-periodic c with S c = a XOR (b OR c): one
child when b is nonzero; when b = 0 the integration c(t + 1) = c(t) XOR a(t) closes, with two children c and c + 1,
exactly when a has even parity over the 16 bits, and otherwise there is no Q-periodic child: the history's period
doubles to 32 and N_5 = d + 1 (as N_4 = 400 follows the zero at 399). At a zero with two children: if they are
rotations of each other (a doubling from a shorter period), one is followed, since the other history is its temporal
rotation with the same depths; if not (a genuine branch), both are followed. Every history is explored to its first
odd zero or to the bound depth 87,866, whichever comes first: rule30_leftside_million.py found the actual single
cell's left side doubling from 16 to 32 at diagonal 87,866, so the tree minimum is at most 87,867. Every retained
transition is checked by the literal equation at all 16 times, separately from the constructor (rule30_rq3.children).

PREDICTIONS, Local's, published before the run (blind unless marked):
  TM-P1 (blind, uncertain): the tree minimum of N_5 is strictly below 87,867: some history other than the single
        cell's reaches period 32 first, so R_5's tree minimum is below 87,867/32 (about 2,746).
  TM-P2 (blind): at most 8 distinct histories (up to temporal rotation) are explored, counting those that exit
        before the bound and those alive at it.
  TM-C1 (control): the zeros at depths 2, 7, 28, 399 have rotation children (doublings), and the first genuine
        branch is at depth 53,207 with driver a rotation of 0000110001010011 (FBR16 and G2.3).
  TM-C2 (control, a second code): exactly one explored history has the events 53,207 (branch), 58,286 (branch),
        87,866 (odd zero, the doubling to 32), as rule30_leftside_million.py found for the single cell.
  TM-U (the unexpected check): at every genuine branch the two children are not rotations of each other, and the
        two histories they start differ at the next zero (depth or driver), so following both is not redundant.
Transcripts: none; the outcome is written into this docstring by hand after the single run.

OUTCOME: not yet run.
"""
import resource
import sys
import time

sys.path.insert(0, __import__('os').path.dirname(__file__))
import rule30_rq3 as rq3

Q, FULL, BOUND = 16, (1 << 16) - 1, 87866
CAP_CPU, CAP_RSS, CAP_STEPS, CAP_HIST = 300.0, 512 * 2 ** 20, 5_000_000, 256
W = lambda s: sum(int(ch) << t for t, ch in enumerate(s))
par = lambda u: bin(u).count('1') & 1


def literal(a, b, c):
    return all(((c >> ((t + 1) % Q)) & 1) == ((a >> t) & 1) ^ (((b >> t) | (c >> t)) & 1) for t in range(Q))


def is_rot(u, v):
    return any(rq3.rot(u, k, Q) == v for k in range(Q))


def cpu():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime + r.ru_stime


def rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss      # bytes on macOS


stopped = None
steps = 0
literal_ok = True
histories = []                    # each: dict(events=[(depth, kind[, driver])], end=(kind, depth, x, y))
stack = [((), (), 0, 0, FULL)]    # (event prefix, branch choices, depth, x, y): the state (x, y) at depth
t0 = time.time()
while stack and stopped is None:
    events, path, d, x, y = stack.pop()
    events = list(events)
    while True:
        if steps >= CAP_STEPS or cpu() > CAP_CPU or rss() > CAP_RSS:
            stopped = 'cap at %d steps, %.1f CPU s' % (steps, cpu())
            break
        if y == 0:
            kids = rq3.children(x, 0, Q)
            if not kids:
                ok_odd = par(x) == 1
                histories.append(dict(events=events + [(d, 'exit' if ok_odd else 'BAD')], end=('exit', d, x, y), path=path))
                break
            c1, c2 = kids
            literal_ok &= literal(x, 0, c1) and literal(x, 0, c2) and c2 == c1 ^ FULL and par(x) == 0
            if is_rot(c1, c2):
                events.append((d, 'doubling'))
                if d + 1 > BOUND:
                    histories.append(dict(events=events, end=('alive', d, x, y), path=path))
                    break
                x, y, d = 0, c1, d + 1
            else:
                events.append((d, 'branch', x))
                if len(histories) + len(stack) + 2 > CAP_HIST:
                    stopped = 'history cap'
                    break
                if d + 1 <= BOUND:
                    stack.append((tuple(events), path + (1,), d + 1, 0, c2))
                    x, y, d, path = 0, c1, d + 1, path + (0,)
                else:
                    histories.append(dict(events=events, end=('alive', d, x, y), path=path))
                    break
            steps += 1
            continue
        if d >= BOUND:
            histories.append(dict(events=events, end=('alive', d, x, y), path=path))
            break
        kids = rq3.children(x, y, Q)
        if len(kids) != 1:
            literal_ok = False
            stopped = 'nonzero driver without a unique child at depth %d' % d
            break
        c = kids[0]
        literal_ok &= literal(x, y, c)
        x, y, d = y, c, d + 1
        steps += 1

wall = time.time() - t0
print('steps %d, histories %d, CPU %.2f s, wall %.2f s, peak RSS %.1f MiB, stopped: %s'
      % (steps, len(histories), cpu(), wall, rss() / 2 ** 20, stopped))
print('literal equation on every retained transition:', 'PASS' if literal_ok else 'FAIL')
exits = sorted(h['end'][1] for h in histories if h['end'][0] == 'exit')
for i, h in enumerate(sorted(histories, key=lambda h: (h['end'][1], h['end'][0]))):
    ev = ', '.join('%d %s' % (e[0], e[1]) for e in h['events'] if e[0] > 399 or e[1] != 'doubling')
    print('  history %d: %s; ends %s at %d' % (i + 1, ev, h['end'][0], h['end'][1]))
if stopped is None:
    m = exits[0] + 1 if exits else None
    zero_low = [e for e in histories[0]['events'] if e[0] <= 399]
    c1 = [e[0] for e in zero_low] == [2, 7, 28, 399] and all(e[1] == 'doubling' for e in zero_low)
    first = [e for h in histories for e in h['events'] if e[1] == 'branch']
    c1 &= min((e[0] for e in first), default=None) == 53207
    c1 &= all(is_rot(e[2], W('0000110001010011')) for e in first if e[0] == 53207)
    print('TM-C1', 'PASS' if c1 else 'FAIL')
    sig = [[(e[0], e[1]) for e in h['events'] if e[0] > 399] for h in histories]
    c2 = sum(s_ == [(53207, 'branch'), (58286, 'branch'), (87866, 'exit')] for s_ in sig) == 1
    print('TM-C2', 'PASS' if c2 else 'FAIL')
    bad = any(e[1] == 'BAD' for h in histories for e in h['events'])
    certified = literal_ok and c1 and c2 and not bad
    print('tree minimum N_5 within the bound:', m, '(R_5 = %.2f)' % (m / 32) if m else '',
          'CERTIFIED (all controls pass)' if certified else 'PROVISIONAL (a control failed; certifies nothing)')
    if certified:
        print('TM-P1', 'HELD' if m is not None and m < 87867 else 'REFUTED')
        print('TM-P2', 'HELD' if len(histories) <= 8 else 'REFUTED', '(%d histories)' % len(histories))

    # TM-U: each genuine branch node is identified by its branch path (the choices before it); below it, the two
    # sibling subtrees (choice 0 and 1) differ at their next record: the next zero (depth, kind, driver up to
    # rotation) or, with no zero before the bound, the end state up to a common rotation
    def nxt(h, i):
        if i + 1 < len(h['events']):
            e = h['events'][i + 1]
            return (e[0], e[1], min(rq3.rot(e[2], k, Q) for k in range(Q)) if len(e) > 2 else None)
        kind, dd, xx, yy = h['end']
        return (kind, dd, min((rq3.rot(xx, k, Q), rq3.rot(yy, k, Q)) for k in range(Q)))
    sides = {}
    for h in histories:
        k = 0
        for i, e in enumerate(h['events']):
            if e[1] == 'branch':
                if e[0] < BOUND:
                    sides.setdefault(h['path'][:k], {}).setdefault(h['path'][k], set()).add(nxt(h, i))
                k += 1
    tu = bool(sides) and all(set(v) == {0, 1} and all(len(r) == 1 for r in v.values()) and v[0] != v[1]
                            for v in sides.values())
    print('TM-U', 'PASS' if tu else 'FAIL', '(%d genuine branch nodes)' % len(sides))
