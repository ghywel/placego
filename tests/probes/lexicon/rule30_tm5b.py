#!/usr/bin/env python3
"""rule30_tm5b.py: TM5b, N_5 on every rooted history to depth 1,000,000 (Local's run, the next item after TM5;
claimed in CLOUD-LOCAL.md, with these predictions pushed before the script was run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_tm5b.py
COST:       a minute or two expected; caps 900 CPU s, 512 MiB peak RSS, 60,000,000 walk steps, 256 histories. The
            first cap hit stops the run, which is then partial.

Domain and walk exactly as rule30_tm5.py (common period Q = 16, the literal equation checked on every retained
transition, rotation children followed once, genuine branches followed both ways), with the bound raised from
87,866 to 1,000,000. Each history ends at its first odd zero at depth d (period 32 from N_5 = d + 1) or is alive at
the bound. For each history the run reports its zeros above 399 with their kinds, its N_5, its period-16 excursion
lengths (the gaps between successive zeros from 399 to its exit) and lambda_4 = (N_5 - 400)/16.

What is already known, and so is a control here, not a prediction. TM5 found four histories to 87,866 (branches at
53,207, 58,286, 72,575; the single cell's exit at 87,866). rule30_leftside_million.py's "sides" run (2026-10-06)
realised four sides, which are these four histories, by flipping diagonals 53,208, 58,287 and 72,576. Their
eventually white diagonals above 60,000: generic 87,866 (doubling); flip 53,208: 72,575 (branch), 165,748 (branch),
183,183 (doubling); flip 58,287: 229,337 (doubling); flip 53,208 and 72,576: 291,256 (doubling). The sibling at
165,748 was never realised, so its history is new.

PREDICTIONS, Local's, published before the run:
  B-C1 (control, from TM5): the literal equation on every transition; the branches 53,207, 58,286, 72,575 and the
        single cell's exit at 87,866 recur.
  B-C2 (control, a second code against the million run): histories exit at 183,183 (after branches 53,207,
        72,575, 165,748), 229,337 (after 53,207, 58,286) and 291,256 (after 53,207, 72,575), and the branch at
        165,748 occurs, each on exactly one history.
  B-P1 (blind, uncertain): the history through the unrealised sibling at 165,748 reaches period 32 below 1,000,000.
  B-P2 (blind): at most 8 histories are explored in all (the five above, plus at most three from new branches on the
        unrealised side).
  B-U (the unexpected check): every history's excursion lengths sum to its own N_5 - 400 (G200's telescoping, read
        on actual data), and each odd exit's driver has odd parity over 16 bits while every branch driver's is even.
Transcripts: none; the outcome is written into this docstring by hand after the single run.

OUTCOME, 2026-10-07 14:50 (M5, one run at commit 0006978; CPU 22.3 s, wall 22.3 s, peak RSS 10.3 MiB, 2,159,010
walk steps, no cap hit). Literal equation PASS on every retained transition. B-C1 PASS (TM5's branches and the single
cell's exit at 87,866 recur). B-C2 PASS: the million run's three flipped sides are reproduced by this second code,
exits 183,183, 229,337 and 291,256 and the branch at 165,748, each on exactly one history. B-U PASS (every history's
excursions sum to its N_5 - 400; branch drivers even, exit drivers odd over 16 bits). B-P1 HELD: the unrealised side
at 165,748 reaches period 32 below a million, on every one of its histories. B-P2 REFUTED: 16 histories, not at most
8; the unrealised side branches again and again (174,449, 179,399, 243,767, 350,243, 445,474, 482,608, 485,619,
537,692, 563,842, 603,582, 760,454), giving 12 histories of its own. None is alive at the bound, so the rooted
period-16 stage is finite and complete: 15 genuine branch nodes, 16 histories up to rotation, every one entering
period 32 by depth 894,235. N_5 over the histories: 87,867, 183,184, 196,189, 229,338, 253,537, 271,596, 291,257,
527,724, 551,910, 555,813, 575,211, 634,886, 645,655, 667,052, 770,532, 894,235. So R_5 = N_5/32 runs from 2,745.8 (the
single cell's, the whole-tree minimum, as TM5 found) to 27,944.8; lambda_4 = (N_5 - 400)/16 from 5,466.7 to 55,864.7;
the excursion counts k from 3 to 12; the longest single excursion is 218,681 (on the history exiting at 291,256).
Per-history excursion lists are printed by the script.
"""
import resource
import sys
import time

sys.path.insert(0, __import__('os').path.dirname(__file__))
import rule30_rq3 as rq3

Q, FULL, BOUND = 16, (1 << 16) - 1, 1000000
CAP_CPU, CAP_RSS, CAP_STEPS, CAP_HIST = 900.0, 512 * 2 ** 20, 60_000_000, 256
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
rows = []
for h in sorted(histories, key=lambda h: (h['end'][0] != 'exit', h['end'][1])):
    zs = [e for e in h['events'] if e[0] >= 399]
    br = [e[0] for e in zs if e[1] == 'branch']
    exc = [b[0] - a[0] for a, b in zip(zs, zs[1:])]
    n5 = h['end'][1] + 1 if h['end'][0] == 'exit' else None
    rows.append((h, br, exc, n5))
    print('  %s: branches %s; excursions %s; %s' % (
        'exit at %d, N_5 = %d, lambda_4 = %.2f, R_5 = %.2f' % (h['end'][1], n5, (n5 - 400) / 16, n5 / 32) if n5
        else 'alive at %d' % h['end'][1], br, exc, 'k = %d' % len(exc)))
if stopped is None:
    sigs = [(tuple(r[1]), r[3]) for r in rows]
    c1 = literal_ok and sum(s == ((53207, 58286), 87867) for s in sigs) == 1
    c1 &= any(53207 in r[1] and 58286 in r[1] for r in rows) and any(72575 in r[1] for r in rows)
    print('B-C1', 'PASS' if c1 else 'FAIL')
    c2 = (sum(s == ((53207, 72575, 165748), 183184) for s in sigs) == 1
          and sum(s == ((53207, 58286), 229338) for s in sigs) == 1
          and sum(s == ((53207, 72575), 291257) for s in sigs) == 1)
    print('B-C2', 'PASS' if c2 else 'FAIL')
    new = [r for r in rows if 165748 in r[1] and r[3] != 183184]
    p1 = bool(new) and all(r[3] is not None for r in new)
    print('B-P1', 'HELD' if p1 else 'REFUTED', [r[3] for r in new])
    print('B-P2', 'HELD' if len(histories) <= 8 else 'REFUTED', '(%d histories)' % len(histories))
    bu = all(sum(r[2]) == r[3] - 400 for r in rows if r[3])
    for h in histories:
        for e in h['events']:
            if e[1] == 'branch':
                bu &= par(e[2]) == 0
    bu &= all(par(h['end'][2]) == 1 for h in histories if h['end'][0] == 'exit')
    print('B-U', 'PASS' if bu else 'FAIL')
    if c1 and c2:
        ns = sorted(r[3] for r in rows if r[3])
        print('N_5 over the explored histories:', ns, '(alive at the bound: %d)' % sum(1 for r in rows if not r[3]))
