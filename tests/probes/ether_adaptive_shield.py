#!/usr/bin/env python3
"""GC2420 frozen adaptive shield pilot; fixed28 entry times and b0..198.

Prediction: the maximum of the28 least A2-certified cutoffs is <198.
Counterfactual:198 remains necessary for this certificate/table, or controls fail.
No new trajectory horizon, alignment family, wall census, solver or Lean build.
"""
import hashlib
import json
import os
import re
from pathlib import Path

ENTRY_HASH = '4787092702a8744f3376c0fa074991f641df98fd3cf3ab7885536e508fd53773'
ETHER_HASH = '9413bfbf7b8d53f8320160d28b1c8ec7644a12369bcc224be9405415c27e282d'
TABLE = [[0,0,1,1],[0,1,1,0],[1,1,0,1],[0,1,0,1],[0,0,1,1],[0,0,0,1],[0,0,0,1]]
LO, HI, HORIZON = -446, 422, 222


def lit_step(w):
    return [a ^ (b | c) for a, b, c in zip(w, w[1:], w[2:])]


def packed_step(z, n):
    return (((z << 1) ^ (z | (z >> 1))) >> 1) & ((1 << (n-2))-1)


def walk(rows, b, T):
    p = b
    trace = []
    for t in range(T):
        row = rows[t]
        i = p-(LO+t)
        assert 0 <= i < len(row)
        bit = row[i]
        trace.append([t, p, bit])
        p -= 1-bit
    return p, trace


def word_check(initial, rows, b, T, endpoint):
    # Independent adaptive finite-word certificate, no frontier oracle queries.
    w = initial[:b-LO+1]
    left = LO
    for t in range(T+1):
        assert w
        reference = rows[t]
        assert w == reference[:len(w)]
        if t == T:
            assert left+len(w)-1 == endpoint
            break
        if len(w) < 2:
            w = []
        else:
            tail = [1-w[-2]] if w[-1] else []
            w = lit_step(w)+tail
        left += 1


def main():
    out = Path(os.environ['CAPPED_OUT'])
    raw = Path('tests/probes/lean/EtherEdgeZero.lean').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == ENTRY_HASH
    ether = Path(os.environ['ETHER_KIT_SOURCE']).read_bytes()
    assert hashlib.sha256(ether).hexdigest() == ETHER_HASH
    entries = []
    for c0, c1, T, xB in re.findall(r'theorem entry_[0-6]_[0-3] : checkEntry (\d) (\d) (\d+) (\(?-?\d+\)?) = true', raw.decode()):
        entries.append((int(c0), int(c1), int(T), int(xB.strip('()'))))
    assert len(entries) == 28 and len({(a,b) for a,b,_,_ in entries}) == 28
    assert max(t for _,_,t,_ in entries) == HORIZON
    text = ether.decode().split('def wallStates :', 1)[1].split('theorem', 1)[0]
    walls = set()
    for phase, bits in re.findall(r'\((\d), \[([a-z, ]+)\]\)', text):
        w = tuple(int(s.strip() == 'true') for s in bits.split(','))
        assert len(w) == 13
        walls.add((int(phase), w))
    assert len(walls) == 109
    # Literal rule30 truth table in lexicographic parent order.
    assert [lit_step([a,b,c])[0] for a in [0,1] for b in [0,1] for c in [0,1]] == [0,1,1,1,1,0,0,0]
    # Walker branch controls on artificial constant reference fields; these are
    # controls of the recursion, not claims that all-black is a Rule30 orbit.
    fake0 = [[0]*(HI-LO+1-2*t) for t in range(11)]
    fake1 = [[1]*(HI-LO+1-2*t) for t in range(11)]
    assert walk(fake0, 20, 10)[0] == 10
    assert walk(fake1, 20, 10)[0] == 20
    results = []
    grid_hash = hashlib.sha256()
    for c0, c1, T, xB in entries:
        initial = [TABLE[(x+c0)%7][c1] if x < 0 else int(x == 0) for x in range(LO,HI+1)]
        rows = [initial]
        z = sum(v << i for i,v in enumerate(initial))
        n = len(initial)
        for t in range(T+1):
            assert rows[t] == [(z >> i) & 1 for i in range(n)]
            grid_hash.update(bytes(rows[t]))
            if t < T:
                rows.append(lit_step(rows[t]))
                z = packed_step(z,n)
                n -= 2
        # Replay the existing entry's finite strip using the pinned kit wall.
        final = rows[T]
        def at(x):
            i = x-(LO+T)
            assert 0 <= i < len(final)
            return final[i]
        assert (xB+c0)%7 == 2
        assert all(at(x) == TABLE[(x+c0)%7][(T+c1)%4] for x in range(-T,xB+1))
        wall = tuple(at(xB+i+1) for i in range(13))
        assert ((T+c1)%4,wall) in walls
        assert wall != tuple(TABLE[(xB+i+1+c0)%7][(T+c1)%4] for i in range(13))
        endpoints = [walk(rows,b,T)[0] for b in range(199)]
        # Noncrossing walkers on the same field give monotonicity, not a fit.
        assert all(a <= b for a,b in zip(endpoints,endpoints[1:]))
        assert all(b-T <= p <= b for b,p in enumerate(endpoints))
        assert endpoints[198] >= xB+13
        eligible = [b for b,p in enumerate(endpoints) if p >= xB+13]
        minimum = min(eligible)
        assert minimum == 0 or endpoints[minimum-1] < xB+13
        first_difference = next(x for x in range(8) if int(x == 0) != TABLE[(x+c0)%7][c1])
        # A smaller cutoff admits pure ether as a completion: no permanent
        # mismatch can then be guaranteed. Independent negative scope control.
        assert minimum >= first_difference
        p, trace = walk(rows,minimum,T)
        word_check(initial,rows,minimum,T,p)
        word_check(initial,rows,198,T,endpoints[198])
        results.append({'c0':c0,'c1':c1,'T':T,'xB':xB,'target':xB+13,
                        'minimum_cutoff':minimum,'endpoint':p,'first_initial_difference':first_difference,
                        'endpoints_0_to_198':endpoints,'minimum_trace':trace})
    B = max(r['minimum_cutoff'] for r in results)
    summary = {'status':'PASS','maximum_cutoff':B,'prediction':'HELD' if B < 198 else 'REFUTED',
               'alignments':28,'candidate_cutoffs':199,'horizon_max':HORIZON,
               'source_sha256':ENTRY_HASH,'ether_sha256':ETHER_HASH,
               'grid_sha256':grid_hash.hexdigest(),'scope':'A2 certificate at retained entry times, not globally optimal shielding or a new Lean proof'}
    (out/'adaptive-shield.json').write_text(json.dumps({'summary':summary,'results':results},indent=2)+'\n')
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
