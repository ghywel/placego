#!/usr/bin/env python3
"""GC2606: one hand-constructed dropped-p1 case; no search or census.

Check the two existing observer variants, one proposed retreat refinement,
and all eight exterior assignments in the single target's backward cone.
"""
import ast
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource

BG_SHA = '528b5760a6d9c4b9d709512b6ba1e45ffecfe57a3ea987cc447ca69c9a94075b'
OBS_SHA = '1895a76fe6b418816f707e5ec31f8b675dcc01dcf046e087fb5be8a73c2f145e'
ROOT = '1000000001111011'
START = (59, 5, tuple(map(int, ROOT)))
OUT = Path(os.environ['CAPPED_OUT'])


def pinned(path, sha):
    raw = Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == sha
    return raw


data = json.loads(pinned(os.environ['OBS_DROP_INPUT'], BG_SHA))
orb = [tuple(r) for r in data['orb']]
q, N, r0, s0 = len(orb), data['N'], data['r'], data['s']
assert (q, N, r0, s0) == (63, 7, 0, 4)
assert orb[0] == (1, 0, 1, 0, 0, 0, 0)
rule = lambda a, b, c: a ^ (b | c)
raw = pinned(Path(__file__).with_name('a4_observer_compare.py'), OBS_SHA)
nodes = [n for n in ast.parse(raw).body if isinstance(n, ast.FunctionDef)
         and n.name in {'step1', 'join', 'new_step'}]
assert len(nodes) == 3
exec(compile(ast.Module(body=nodes, type_ignores=[]), 'pinned-observer', 'exec'))


def refined(flags, strip, nxt_strip, mv, active, label):
    old = new_step(flags, strip, mv, active, label)
    if old is None or mv == 0 or old[0] is not None:
        return old
    p0, p1, c = old
    bnext = nxt_strip[-1]
    extra = 1 - bnext if c == 1 else (
        bnext ^ flags[1] if c == 0 and flags[1] is not None else None)
    p1, ok = join(p1, extra)
    return (p0, p1, c) if ok else None


def run(labels, literal, repair):
    global LITERAL
    LITERAL = literal
    state, flags, B = START, (None, None, None), 16
    trace = []
    for t, label in enumerate(labels):
        n0, m0, alive0 = step1(state, 0)
        n1, m1, alive1 = step1(state, 1)
        assert m0 == m1
        active = n0 != n1
        nxt, mv, alive = (n1, m1, alive1) if label else (n0, m0, alive0)
        nf = (refined(flags, state[2], nxt[2], mv, active, label) if repair
              else new_step(flags, state[2], mv, active, label))
        trace.append({'t': t, 'B': B, 'strip': ''.join(map(str, state[2])),
                      'memory': flags, 'active': active, 'label': label,
                      'motion': mv, 'next_memory': nf, 'alive': alive})
        assert alive
        if nf is None:
            return t, trace
        state, flags, B = nxt, nf, B + mv
    return None, trace


# Independent scalar oracle uses the literal eight-entry rule table.
TABLE = (0, 1, 1, 1, 1, 0, 0, 0)
def scalar(row):
    return {j: TABLE[4*row[j-1]+2*row[j]+row[j+1]]
            for j in range(min(row)+1, max(row))}


def background(t, j):
    return orb[(59+t+4) % 63][(5+t-j) % 7]


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (3, 3))
    results = {}
    for literal in (True, False):
        name = 'literal' if literal else 'enriched'
        reject, trace = run([0]*5, literal, False)
        assert reject is None, ('OLD_REJECTED', name, reject)
        assert [r['motion'] for r in trace] == [-1, 0, -1, 0, 0]
        assert [r['active'] for r in trace] == [False]*4+[True]
        rr, rt = run([0]*5, literal, True)
        assert rr == 4, ('REPAIR_NOT_AT_4', name, rr)
        results[name] = {'original': trace, 'refined': rt}
    targets = []
    for suffix in itertools.product((0, 1), repeat=3):
        row = {j: (background(0, j) if j <= 0 else
                   int(ROOT[j-1]) if j <= 16 else
                   suffix[j-17] if j <= 19 else 0)
               for j in range(-8, 25)}
        state, B, labels = START, 16, []
        for t in range(5):
            assert state[2] == tuple(row[j] for j in range(B-15, B+1))
            label = row[B+1]
            labels.append(label)
            if t == 4:
                assert B+1 == 15
                targets.append(label)
                assert (row[13], row[14], row[15]) == (0, 0, 1)
            state, mv, alive = step1(state, label)
            B += mv
            row = scalar(row)
        assert labels[-1] == 1
        for literal in (True, False):
            for repair in (False, True):
                assert run(labels, literal, repair)[0] is None
    assert targets == [1]*8
    # Exact target cone [11,19]; only [17,19] are outside the root.
    for suffix in itertools.product((0, 1), repeat=3):
        cone = dict(zip(range(11, 20), map(int, ROOT[10:]+''.join(map(str, suffix)))))
        assert len(cone) == 9
        for _ in range(4):
            cone = scalar(cone)
        assert cone == {15: 1}
    empty = dict.fromkeys(range(11, 20), 0)
    for _ in range(4):
        empty = scalar(empty)
    assert empty == {15: 0}, 'ALL_WHITE_COUNTERCONTROL'
    results.update({'status': 'PASS', 'root': ROOT, 'start_phase': [59, 5],
                    'target': [4, 15], 'free_exterior': [17, 18, 19],
                    'all_8_target_values': targets, 'physical_controls': 32,
                    'all_white_control': 0, 'scope': 'one constructed root; not the saved t3000 root',
                    'cpu_self_s': resource.getrusage(resource.RUSAGE_SELF).ru_utime+
                                  resource.getrusage(resource.RUSAGE_SELF).ru_stime})
    (OUT/'result.json').write_text(json.dumps(results, indent=2)+'\n')
    print('PASS: old variants accept zero at4; proposed refinement rejects; 8 cones black; 32 physical controls pass')


if __name__ == '__main__':
    main()
