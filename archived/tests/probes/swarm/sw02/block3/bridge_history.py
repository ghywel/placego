#!/usr/bin/env python3
"""Fixed DFA comparisons and two genuine finite-history bridge queries.

The DFA conclusions concern the supplied finite automata, not collision-free
reconstruction of Local's window subsets. SAT witnesses are checked by a
separate scalar-cell simulator. UNSAT is reported as uncertified, never as a
word exclusion. No horizon, seed census or width grows in response to a result.
"""
import argparse
import collections
import hashlib
import itertools
import json
import struct
from pathlib import Path


def read_dfa(path):
    rows = {}
    for line in Path(path).read_text().splitlines():
        p = line.split()
        s = int(p[0])
        assert s not in rows
        rows[s] = {int(g): int(t) for g, t in (x.split(':') for x in p[2:])}
    assert 0 in rows and all(t in rows for r in rows.values() for t in r.values())
    return rows


def word(T, s, w):
    for g in w:
        s = T.get(s, {}).get(int(g), -1)
    return s


def compare(A, B, start_a=0, start_b=0):
    """All nondead states accept. BFS returns a shortest separating word."""
    q = collections.deque([(start_a, start_b, '')])
    seen = {(start_a, start_b)}
    while q:
        a, b, w = q.popleft()
        if (a == -1) != (b == -1):
            return {'equal': False, 'word': w, 'left_accepts': a != -1,
                    'product_states': len(seen)}
        for g in sorted(set(A.get(a, {})) | set(B.get(b, {}))):
            k = (A.get(a, {}).get(g, -1), B.get(b, {}).get(g, -1))
            if k not in seen:
                assert len(seen) < 500000, 'product-state stop'
                seen.add(k)
                q.append((*k, w + str(g)))
    return {'equal': True, 'product_states': len(seen)}


def x_grammar():
    """Factor language of A=25, E=33535555, with 4 or >=6 A's per E."""
    N = collections.defaultdict(lambda: collections.defaultdict(set))
    for n in range(7):
        N[('b', n)][2].add(('a', n))
        N[('a', n)][5].add(('b', min(6, n + 1)))
        if n in (4, 6):
            N[('b', n)][3].add(('e', 1))
    E = '33535555'
    for k in range(1, len(E)):
        N[('e', k)][int(E[k])].add(('e', k + 1) if k + 1 < len(E) else ('b', 0))
    all_states = frozenset(N)
    sets = {all_states: 0}
    todo = collections.deque([all_states])
    T = {}
    while todo:
        S = todo.popleft()
        row = {}
        for g in (2, 3, 5):
            V = frozenset(t for s in S for t in N[s].get(g, ()))
            if V:
                if V not in sets:
                    sets[V] = len(sets)
                    todo.append(V)
                row[g] = sets[V]
        T[sets[S]] = row
    return T


def unary_orbit(T, initial_word, loop, final_word):
    """Exact ultimately periodic set of accepted exponents, with no n cutoff."""
    seen, accepted = {}, []
    s = word(T, 0, initial_word)
    while s not in seen:
        seen[s] = len(accepted)
        accepted.append(word(T, s, final_word) != -1)
        s = word(T, s, loop)
    mu, period = seen[s], len(accepted) - seen[s]
    return {'preperiod': mu, 'period': period,
            'accepted_before': [n for n in range(mu) if accepted[n]],
            'accepted_cycle_offsets': [n for n in range(period) if accepted[mu + n]]}


def dfa_checks(root):
    A = x_grammar()
    # Known equal and unequal controls for the all-length comparison.
    assert compare({0: {2: 0}}, {0: {2: 1}, 1: {2: 1}})['equal']
    assert compare({0: {2: 0}}, {0: {2: 1}, 1: {}})['word'] == '22'
    results = {'x_grammar_states': len(A), 'x': {}, 'y': {}}
    previous = None
    for width in (38, 39, 40, 41):
        T = read_dfa(root / 'dfa2' / f'dfa_xx_W{width}_c0.txt')
        r = {'states': len(T), 'grammar': compare(T, A),
             'E_A_n_E': unary_orbit(T, '33535555', '25', '33535555'),
             'periodic_A4E': unary_orbit(T, '', '25' * 4 + '33535555', ''),
             'periodic_A6E': unary_orbit(T, '', '25' * 6 + '33535555', '')}
        if previous is not None:
            r['previous_width'] = compare(previous, T)
        results['x'][width] = r
        previous = T
    T = read_dfa(root / 'y' / 'dfa_xx_W60_c0.txt')
    for a in ('45', '4525'):
        for b in ('45', '4525'):
            results['y'][a + '_to_' + b] = unary_orbit(T, a, '2', b)
    results['y']['pure_2'] = unary_orbit(T, '', '2', '')
    return results


def scalar_trace(R, horizon, width):
    """Literal cells; the center is black at even times, white at odd times."""
    row = [False] + [bool((R >> (j - 1)) & 1) for j in range(1, width + horizon + 3)]
    trace = []
    for t in range(horizon + 1):
        trace.append(row[1])
        center = t % 2 == 0
        row = [False] + [((center if j == 1 else row[j - 1]) !=
                         (row[j] or (row[j + 1] if j + 1 < len(row) else False)))
                        for j in range(1, len(row))]
    return trace


def bit_trace(R, horizon):
    trace = []
    for t in range(horizon + 1):
        trace.append(bool(R & 1))
        R = ((R << 1) | (t % 2 == 0)) ^ (R | (R >> 1))
    return trace


def solve_trace(wanted, fixed_root=None, conflict_budget=60000):
    from pysat.solvers import Cadical195
    H = max(wanted)
    width = H + 1
    offsets = [0]
    for t in range(H + 1):
        offsets.append(offsets[-1] + width - t)

    def vid(t, x):
        return offsets[t] + x

    digest = hashlib.sha256()
    count = 0
    with Cadical195() as S:
        def add(c):
            nonlocal count
            count += 1
            digest.update(struct.pack('<' + 'i' * (len(c) + 1), *c, 0))
            S.add_clause(c)

        for t in range(H):
            for x in range(1, width - t):
                ins = [vid(t, x - 1) if x > 1 else None, vid(t, x), vid(t, x + 1)]
                out = vid(t + 1, x)
                for a, b, c in itertools.product((False, True), repeat=3):
                    if x == 1 and a != (t % 2 == 0):
                        continue
                    values = (a, b, c)
                    clause = [-v if z else v for v, z in zip(ins, values) if v is not None]
                    clause.append(out if a != (b or c) else -out)
                    add(clause)
        for t, value in sorted(wanted.items()):
            add([vid(t, 1) if value else -vid(t, 1)])
        if fixed_root is not None:
            for x in range(1, width + 1):
                add([vid(0, x) if (fixed_root >> (x - 1)) & 1 else -vid(0, x)])
        S.conf_budget(conflict_budget)
        answer = S.solve_limited()
        result = {'horizon': H, 'root_width_bound': width, 'variables': offsets[-1],
                  'clauses': count, 'cnf_sha256': digest.hexdigest(),
                  'answer': 'SAT' if answer is True else 'UNSAT_UNCERTIFIED' if answer is False else 'UNKNOWN',
                  'solver_stats': S.accum_stats()}
        if answer is True:
            model = set(S.get_model())
            R = sum(1 << (x - 1) for x in range(1, width + 1) if vid(0, x) in model)
            trace = scalar_trace(R, H, width)
            assert trace == bit_trace(R, H)
            assert all(trace[t] == b for t, b in wanted.items()), 'SAT witness failed scalar replay'
            mutant = dict(wanted)
            first = min(wanted)
            mutant[first] = not mutant[first]
            assert not all(trace[t] == b for t, b in mutant.items()), 'bad-target control failed'
            result.update(root_hex=hex(R), root_bits=R.bit_length(),
                          scalar_replay=True, bit_replay=True,
                          sampled_trace=''.join(str(int(trace[t])) for t in sorted(wanted)))
        return result


def sat_checks():
    R, H = 19, 17
    trace = scalar_trace(R, H, H + 1)
    wanted = dict(enumerate(trace))
    good = solve_trace(wanted, fixed_root=R)
    assert good['answer'] == 'SAT'
    wanted[1] = not wanted[1]
    bad = solve_trace(wanted, fixed_root=R)
    assert bad['answer'] == 'UNSAT_UNCERTIFIED'
    controls = {'fixed_root_good': good, 'wrong_tick_rejected': bad}
    print(json.dumps({'controls': controls}), flush=True)
    results = {}
    E = '33535555'
    for n in (4, 6):
        gaps = '25' * 2 + ('25' * n + E) * 3 + '25' * 2
        black = {0}
        for g in gaps:
            black.add(max(black) + int(g))
        target = {1 + 2 * s: s in black for s in range(max(black) + 1)}
        r = solve_trace(target)
        r.update(gap_word=gaps, A_per_excursion=n, E_count=3)
        results[n] = r
        print(json.dumps({'three_crossing_query': n, 'result': r}), flush=True)
    return results


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--packet', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    D = dfa_checks(args.packet)
    (args.out / 'dfa.json').write_text(json.dumps(D, indent=2) + '\n')
    print(json.dumps({'dfa_checks': D}), flush=True)
    A = sat_checks()
    (args.out / 'history.json').write_text(json.dumps(A, indent=2) + '\n')


if __name__ == '__main__':
    main()
