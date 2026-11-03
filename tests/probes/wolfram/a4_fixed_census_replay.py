#!/usr/bin/env python3
"""GC2547: fixed independent replay of L1441's retained width12 Ring57 certificate.

No search parameters. A4_DATA and A4_CERT locate the two SHA256-pinned inputs;
CAPPED_OUT is supplied by run_capped.py. Uses literal Rule30 truth table for
graph edges and a separately controlled packed physical-row evolution for entries.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import time

PINS = {'A4_DATA': '24e2f0398331646a289edec5e38fdf167456c3f5121cf6560c99d9f98ed88161',
        'A4_CERT': '63063d70bc9f356d3945eafb9c8da11cff30b93a01d1bceec127506d263f64aa'}
TABLE = (0, 1, 1, 1, 1, 0, 0, 0)
START = time.monotonic()
last_monitor = -10.0
thermal_samples = []


def monitor():
    global last_monitor
    me = resource.getrusage(resource.RUSAGE_SELF)
    kids = resource.getrusage(resource.RUSAGE_CHILDREN)
    assert me.ru_utime + me.ru_stime + kids.ru_utime + kids.ru_stime < 90, 'DRIVER_CPU_STOP'
    assert time.monotonic() - START < 160, 'DRIVER_WALL_STOP'
    if time.monotonic() - last_monitor < 2:
        return
    last_monitor = time.monotonic()
    r = subprocess.run(['pmset', '-g', 'therm'], capture_output=True, text=True, timeout=5)
    assert r.returncode == 0, 'THERMAL_MONITOR_FAILURE'
    found = dict(re.findall(r'(CPU_Scheduler_Limit|CPU_Available_CPUs|CPU_Speed_Limit)\s*=\s*(\d+)', r.stdout))
    assert len(found) == 3, 'THERMAL_MONITOR_PARSE_FAILURE'
    sample = {k: int(v) for k, v in found.items()}
    thermal_samples.append(sample)
    assert sample['CPU_Scheduler_Limit'] == sample['CPU_Speed_Limit'] == 100, 'THERMAL_STOP'
    assert sample['CPU_Available_CPUs'] == 16, 'THERMAL_CPU_STOP'


def rule(a, b, c):
    return TABLE[4 * a + 2 * b + c]


def packed(row, mask):
    return ((row << 1) ^ (row | (row >> 1))) & mask


def expect_rejected(fn):
    try:
        fn()
    except AssertionError:
        return
    raise AssertionError('MUTANT_ACCEPTED')


def run():
    os.nice(10)
    monitor()
    inputs = {}
    for key, pin in PINS.items():
        b = Path(os.environ[key]).read_bytes()
        assert hashlib.sha256(b).hexdigest() == pin, 'INPUT_PIN'
        inputs[key] = json.loads(b)
    data, cert = inputs['A4_DATA'], inputs['A4_CERT']
    assert (data['N'], data['q'], data['W'], data['P'], data['S'], data['r'], data['s']) == (9, 57, 24, 19, 14, 0, 0)
    assert (cert['WP'], cert['TMAX'], cert['W'], cert['P'], cert['S'], cert['r'], cert['s']) == (12, 1200, 24, 19, 14, 0, 0)
    orb = data['orb']
    assert len(orb) == 57 and all(len(row) == 9 and set(row) <= {0, 1} for row in orb)
    # Full cyclic background, checked against literal truth table.
    for t in range(57):
        for j in range(9):
            assert orb[(t + 1) % 57][j] == rule(orb[t][j], orb[t][(j - 1) % 9], orb[t][(j - 2) % 9])
    E = lambda t, x: orb[t % 57][(t - x) % 9]

    # Independent dense literal oracle controls every 8-bit word over four ticks.
    control_cells = 0
    for pat in range(256):
        vec = [0] * 8 + [(pat >> i) & 1 for i in range(8)] + [0] * 8
        row = sum(b << i for i, b in enumerate(vec))
        for tick in range(1, 5):
            vec = [0] + [rule(*vec[i - 1:i + 2]) for i in range(1, 23)] + [0]
            row = packed(row, (1 << 24) - 1)
            for i in range(tick, 24 - tick):
                assert ((row >> i) & 1) == vec[i]
                control_cells += 1
    # A reflected packed update must be distinguished by this oracle.
    v = 3 << 10
    mirrored = ((v >> 1) ^ (v | (v << 1))) & ((1 << 24) - 1)
    expect_rejected(lambda: assert_same(packed(v, (1 << 24) - 1), mirrored))

    def dec(st):
        tq, dq, bits = st
        if isinstance(bits, str):
            assert set(bits) <= {'0', '1'}
            bits = tuple(map(int, bits))
        else:
            bits = tuple(bits)
        assert 0 <= tq < 57 and 0 <= dq < 9 and len(bits) == 24 and set(bits) <= {0, 1}
        return tq, dq, bits

    def successors(st):
        tq, dq, bits = st
        result = []
        for incoming in (0, 1):
            ref = lambda dt, i: orb[(tq + dt) % 57][(dq + dt - i) % 9]
            cell = lambda i: ref(0, i) if i <= 0 else (bits[i - 1] if i <= 24 else incoming)
            new = tuple(rule(cell(i - 1), cell(i), cell(i + 1)) for i in range(25))
            motion = -int(new[0] != ref(1, 0))
            after = new[:24] if motion == -1 else new[1:]
            ndq = (dq + 1 - motion) % 9
            nxt = ((tq + 1) % 57, ndq, after)
            assert any(after[i - 1] != orb[nxt[0]][(ndq - i) % 9] for i in range(1, 25)), 'EMPTY_SUCCESSOR'
            result.append((nxt, motion))
        return result

    graph_counts = []

    def graph_check(raw_states, psi, edges):
        states = [dec(st) for st in raw_states]
        assert len(states) == len(set(states)) == len(psi)
        lookup = {st: p for st, p in zip(states, psi)}
        assert all(type(p) is int for p in psi)
        encoded = {i: es for i, es in edges}
        assert len(encoded) == len(edges) == len(states) and set(encoded) == set(range(len(states)))
        branches = 0
        for i, st in enumerate(states):
            if i % 256 == 0:
                monitor()
            expected = set()
            for nxt, mv in successors(st):
                assert nxt in lookup, 'NOT_CLOSED'
                assert lookup[nxt] - lookup[st] == 19 * mv + 5, 'POTENTIAL'
                expected.add((nxt, mv)); branches += 1
            supplied = set()
            for ni, mv in encoded[i]:
                assert type(ni) is int and 0 <= ni < len(states) and mv in (-1, 0)
                supplied.add((states[ni], mv))
            assert supplied == expected, 'EXPORTED_EDGE_MISMATCH'
        return lookup, branches

    assert data['lo'] == data['hi']
    a4, branches = graph_check(data['states'], data['lo'], data['edges'])
    graph_counts.append({'states': len(a4), 'input_branches': branches})
    # One-potential mutation must be rejected, not merely produce a different band.
    badpsi = data['lo'].copy(); badpsi[0] += 1
    expect_rejected(lambda: graph_check(data['states'], badpsi, data['edges']))
    owns = []
    for own in cert['own_closures']:
        lookup, branches = graph_check(own['states'], own['psi'], own['edges'])
        assert dec(own['start']) in lookup
        owns.append(lookup)
        graph_counts.append({'states': len(lookup), 'input_branches': branches})
    assert [g['states'] for g in graph_counts] == [498, 177, 18595]

    entries = cert['entries']
    assert len(entries) == 4095 and sorted(e[0] for e in entries) == list(range(1, 4096))
    assert all(e[1] in (300, 600, 900, 1200) for e in entries)
    # Whole-row packed simulation in a fixed domain; only its exact interior is read.
    lo, hi = -2410, 1246
    width = hi - lo; mask = (1 << width) - 1
    bg0 = sum(E(0, x) << (x - lo) for x in range(lo, hi))
    background = {0: bg0}; bg = bg0
    exact_masks = {}
    for t in range(1, 1201):
        bg = packed(bg, mask)
        if t in (300, 600, 900, 1200):
            background[t] = bg
            low, high = lo + t + 2, hi - t - 2  # high exclusive, conservative
            exact_masks[t] = ((1 << (high - low)) - 1) << (low - lo)
            reference = sum(E(t, x) << (x - lo) for x in range(low, high))
            assert (bg & exact_masks[t]) == reference, 'BACKGROUND_PHASE'

    entry_hash = hashlib.sha256()
    counts = {'A4': 0, 'own': 0}
    bands = []
    ranges = {id(g): (min(g.values()), max(g.values())) for g in [a4] + owns}
    for n, (pat, tc, raw_st, kind, psi) in enumerate(entries):
        if n % 16 == 0:
            monitor()
        row = bg0 ^ (pat << -lo)
        for _ in range(tc):
            row = packed(row, mask)
        diff = (row ^ background[tc]) & exact_masks[tc]
        assert diff, 'NO_DIFFERENCE_IN_EXACT_RANGE'
        fi = (diff & -diff).bit_length() - 1
        F = fi + lo; A = F - 1
        # Earliest possible initial damage is x=-tc; all x below it agree.
        assert lo + tc + 2 < -tc <= F and F + 24 < hi - tc - 2
        strip = tuple((row >> (fi + i)) & 1 for i in range(24))
        actual = (tc % 57, (tc - A) % 9, strip)
        assert actual == dec(raw_st), 'ENTRY_TRAJECTORY_MISMATCH'
        if kind == 'A4':
            assert actual in a4 and a4[actual] == psi
            chosen = a4
        else:
            assert kind == 'own' and any(actual in own for own in owns)
            chosen = next(own for own in owns if actual in own)
        pmin, pmax = ranges[id(chosen)]
        baseline = 19 * A + 5 * tc - chosen[actual]
        bands.append((baseline + 19 + pmin, baseline + 19 * 24 + pmax))
        counts[kind] += 1
        entry_hash.update(json.dumps([pat, tc, F, ''.join(map(str, strip))], separators=(',', ':')).encode() + b'\n')
        if n == 0:
            mutant = [raw_st[0], raw_st[1], ('1' if raw_st[2][0] == '0' else '0') + raw_st[2][1:]]
            expect_rejected(lambda: assert_same(actual, dec(mutant)))
    assert counts == {'A4': 4056, 'own': 39}
    monitor()
    me = resource.getrusage(resource.RUSAGE_SELF); kids = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = {'status': 'PASS', 'input_sha256': PINS, 'graphs': graph_counts,
              'actual_entry_trajectories': 4095, 'entries': counts,
              'uniform_band_from_t1200': {'expression': '19*F(t)+5*t',
                                          'lower': min(b[0] for b in bands),
                                          'upper': max(b[1] for b in bands)},
              'entry_digest': entry_hash.hexdigest(), 'literal_control_cells': control_cells,
              'negative_controls': ['reflected_rule', 'changed_potential', 'changed_entry_bit'],
              'thermal_samples': thermal_samples, 'wall_s': time.monotonic() - START,
              'driver_and_children_cpu_s': me.ru_utime + me.ru_stime + kids.ru_utime + kids.ru_stime,
              'scope': 'Only retained width12 Ring57 family and its three finite certificates; not arbitrary widths or the Ring63 slow wall.'}
    Path(os.environ['CAPPED_OUT'], 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, sort_keys=True))


def assert_same(a, b):
    assert a == b


if __name__ == '__main__':
    run()
