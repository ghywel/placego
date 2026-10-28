#!/usr/bin/env python3
"""GC2016: exact B-ancestry with U(-k,-k)=1-(k mod 2), to depth 512.

Complete periodic-right-ray inverse construction, then filtering; never clamp a
display boundary. If the constraint dies, retain every rejected parent and
continue one explicitly unconstrained history for the context visualisation.
Controls and bounds are frozen in reports/rule30-backward-diagonal-b.md.
"""
import base64
import hashlib
import json
import os
from pathlib import Path

DEPTH, LO, HI, FUTURE = 512, -1600, 320, 64
TRUTH = (0, 1, 1, 1, 1, 0, 0, 0)
STATES = ((0, 0), (0, 1), (1, 0), (1, 1))
checks = 0


class Row:
    def __init__(self, win, tail):
        self.win, self.tail = bytes(win), tuple(tail)
        assert len(self.win) == 1 - LO

    def at(self, i):
        assert i >= LO
        return self.win[i - LO] if i <= 0 else self.tail[(i - 1) % len(self.tail)]


class FiniteRow:
    def __init__(self, cells):
        self.cells = cells

    def at(self, i):
        return self.cells.get(i, 0)


def G(b, s):
    c, r = s
    return b ^ (c | r), c


def least_block(v):
    for p in range(1, len(v) + 1):
        if len(v) % p == 0 and all(v[i] == v[i % p] for i in range(len(v))):
            return tuple(v[:p])
    raise AssertionError


def parents(y):
    global checks
    p = len(y.tail)
    assert p <= 4096, 'tail-period cap'
    def M(s):
        for i in range(1 + p, 1, -1):
            s = G(y.at(i), s)
        return s
    maps = {s: M(s) for s in STATES}
    cycles = set()
    for s in STATES:
        seen = []
        while s not in seen:
            seen.append(s)
            s = maps[s]
        cycles.update(seen[seen.index(s):])
    previous = {maps[s]: s for s in cycles}
    assert len(previous) == len(cycles)
    out = []
    for s in sorted(cycles):
        orbit = [s]
        while previous[orbit[-1]] != s:
            orbit.append(previous[orbit[-1]])
        q = p * len(orbit)
        assert q <= 4096, 'parent tail-period cap'
        x = {}
        for k in range(1, len(orbit) + 1):
            v, pos = orbit[k % len(orbit)], 1 + k * p
            x[pos], x[pos + 1] = v
            for i in range(pos, pos - p, -1):
                v = G(y.at(i), v)
                x[i - 1] = v[0]
        x[1], x[2] = s
        tail = least_block([x[1 + j] for j in range(q)])
        for i in range(0, LO - 1, -1):
            x[i] = y.at(i + 1) ^ (x[i + 1] | x[i + 2])
        r = Row([x[i] for i in range(LO, 1)], tail)
        for i in range(LO + 1, 2 + 3 * q):
            assert y.at(i) == TRUTH[4*r.at(i-1) + 2*r.at(i) + r.at(i+1)]
            checks += 1
        out.append(r)
    assert len({(r.win, r.tail) for r in out}) == len(out)
    return sorted(out, key=lambda r: (len(r.tail), r.tail, r.win))


def pack_rows(rows):
    raw = bytearray()
    for r in rows:
        bits = [r.at(i) for i in range(LO, HI + 1)]
        for j in range(0, len(bits), 8):
            value = 0
            for k in range(8):
                value = (value << 1) | (bits[j+k] if j+k < len(bits) else 0)
            raw.append(value)
    return base64.b64encode(raw).decode()


def main():
    out = Path(os.environ['CAPPED_OUT'])
    seed = Row([0] * (-LO) + [1], [0])
    control = [seed]
    counts = [1]
    for _ in range(3):
        control = [p for y in control for p in parents(y)]
        counts.append(len(control))
    assert counts == [1, 2, 5, 8]
    a, b = parents(seed)
    assert all(a.at(i) == int(i < 0) for i in range(-20, 21))
    assert all(b.at(i) == int(i != -1) for i in range(-20, 21))
    bp = parents(b)
    assert sorted(r.at(-1) for r in bp) == [0, 0, 1]
    b1 = next(r for r in bp if r.at(-1))
    assert all(r.at(-1) == 1 for r in parents(b1))

    nodes = [(seed, None)]
    live = [0]
    summary, rejection, failure = [], [], None
    for d in range(1, DEPTH + 1):
        nxt, candidates = [], []
        for parent_id in live:
            for r in parents(nodes[parent_id][0]):
                node_id = len(nodes)
                nodes.append((r, parent_id))
                assert len(nodes) <= 20000, 'total-node cap'
                actual, required = r.at(-d), 1 - d % 2
                candidates.append(node_id)
                if actual == required:
                    nxt.append(node_id)
        summary.append({'depth':d, 'parents_examined':len(candidates), 'survivors':len(nxt)})
        print(json.dumps(summary[-1]), flush=True)
        if not nxt:
            failure = d
            for i in candidates:
                r, parent_id = nodes[i]
                rejection.append({'node':i, 'child':parent_id, 'actual':r.at(-d),
                                  'required':1-d%2, 'tail_from_x1':''.join(map(str,r.tail)),
                                  'window_x0':-24, 'window':''.join(str(r.at(x)) for x in range(-24,25)),
                                  'row_sha256':hashlib.sha256(r.win + bytes(r.tail)).hexdigest()})
            chosen = min(candidates, key=lambda i:(len(nodes[i][0].tail),nodes[i][0].tail,nodes[i][0].win))
            break
        assert len(nxt) <= 2000, 'live-branch cap'
        live = nxt
    else:
        chosen = min(live, key=lambda i:(len(nodes[i][0].tail),nodes[i][0].tail,nodes[i][0].win))
    chain = []
    while chosen is not None:
        r, chosen = nodes[chosen]
        chain.append(r)
    chain.reverse()
    # Explicitly unconstrained context, only if strict alternation was disproved.
    while len(chain) <= DEPTH:
        chain.append(parents(chain[-1])[0])

    white = [seed]
    for d in range(1, DEPTH+1):
        x = bytearray(1-LO)
        for i in range(0, LO-1, -1):
            c = x[i+1-LO] if i+1<=0 else 0
            r = x[i+2-LO] if i+2<=0 else 0
            x[i-LO] = white[-1].at(i+1) ^ (c|r)
        row = Row(x, [0])
        assert row.at(-d) == 1
        for i in range(LO+1, HI):
            assert white[-1].at(i) == TRUTH[4*row.at(i-1)+2*row.at(i)+row.at(i+1)]
        white.append(row)

    future = []
    row = {i:int(i==0) for i in range(LO-FUTURE, HI+FUTURE+1)}
    for t in range(1,FUTURE+1):
        row = {i:TRUTH[4*row[i-1]+2*row[i]+row[i+1]]
               for i in range(LO-FUTURE+t,HI+FUTURE-t+1)}
        future.append(FiniteRow(row))
    result = {'depth_limit':DEPTH, 'first_impossible_depth':failure,
              'max_alternating_steps':failure-1 if failure else DEPTH,
              'controls_counts':counts, 'levels':summary,'rejected':rejection,
              'scalar_inverse_checks':checks, 'x0':LO,'x1':HI,'t0':-DEPTH,'t1':FUTURE,
              'diagonal_bits_backward':''.join(str(r.at(-d)) for d,r in enumerate(chain)),
              'selected_tail_periods':[len(r.tail) for r in chain],
              'selection_after_failure':'shortest tail period, then lexicographic right tail and stored left window',
              'continued_after_failure':failure is not None}
    (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    view = {'x0':LO,'w':HI-LO+1,'t0':-DEPTH,'h':DEPTH+FUTURE+1,
            'stride':(HI-LO+8)//8,'failure':failure,
            'b':pack_rows(list(reversed(chain))+future),
            'a':pack_rows(list(reversed(white))+future)}
    (out/'view.json').write_text(json.dumps(view,separators=(',',':')))
    print('RESULT',json.dumps({k:result[k] for k in ('first_impossible_depth','max_alternating_steps','scalar_inverse_checks')}))


if __name__ == '__main__':
    main()
