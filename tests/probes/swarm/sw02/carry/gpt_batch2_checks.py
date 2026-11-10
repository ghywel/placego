#!/usr/bin/env python3
"""Fixed Phase C batch-2 controls; see GPT-SW02-CARRY-BATCH2-20261110.md.

No census, seed enlargement, solver or Wolfram call. The raw source is verified
before replay. Output belongs outside git. Scalar controls are independently
written; the long prefix replay is explicitly a replay of the original Python.
"""
import argparse
import contextlib
import hashlib
import io
import itertools
import json
from pathlib import Path
import re
import runpy


def wheel_step(bits):
    return [bits[j - 2] ^ (bits[j - 1] | bits[j]) for j in range(2, len(bits))]


def local_controls():
    # Known three cells a,b,c followed by free u,v. After two updates,
    # output indices 3,4 of the original row are the last two outputs.
    got = set()
    for u, v in itertools.product(range(2), repeat=2):
        got.add(tuple(wheel_step(wheel_step([0, 0, 0, 1, 0, u, v]))[-2:]))
    assert len(got) == 1, got
    mutant = {
        tuple(wheel_step(wheel_step([0, 0, 0, 0, 0, u, v]))[-2:])
        for u, v in itertools.product(range(2), repeat=2)
    }
    assert len(mutant) > 1  # 000 cannot replace the guarded 010 pattern.
    # One-wheel healing is uniform over both unseen cells when the last
    # known wheel is black. This is a recurrence check, not a trajectory.
    for a, b in itertools.product(range(2), repeat=2):
        assert len({wheel_step([a, b, 1, u, v])[-2]
                    for u, v in itertools.product(range(2), repeat=2)}) == 1
    # At the wall: F(a)_1 = a_2 xor a_1. A depth-1 discrepancy can cancel.
    row_step = lambda y: (y >> 1) ^ (y | (y << 1))
    assert ((row_step(0) ^ row_step(3)) & 1) == 0
    assert ((row_step(0) ^ row_step(1)) & 1) == 1
    print(json.dumps({'local_controls': 'PASS', '010_outputs': sorted(got),
                      '000_mutant_outputs': sorted(mutant),
                      'depth1_cancellation_pair': [0, 3]}), flush=True)


def pulse_controls():
    cases = 0
    for h in range(1, 9):
        m = 8 ** h
        assert 2 * h < 7 * m - 7
        assert 4 * m - 4 - h >= 3 * m
        assert 11 * m + 3 + h < 12 * m
        # Parent M-1: Lucas gives one 1..7 pulse every 7M ticks.
        def parent(t, a):
            p, r = divmod(t - a + 3 * (m - 1), 7)
            return r + 1 if p >= 0 and ((m - 1) & p) == m - 1 else 0
        ts = set()
        for a in range(-h, h + 1):
            for q in (0, 1):
                start = a + 4 * m - 4 + 7 * q * m
                ts.update(range(start - 1, start + 8))
        for t in ts:
            vals = {a: parent(t, a) for a in range(-h, h + 1)}
            for a, b in itertools.product(vals, repeat=2):
                if vals[a] and vals[b] == vals[a]:
                    assert a == b
                cases += 1
        for a in range(-h, h + 1):
            for q in (0, 1):
                start = a + 4 * m - 4 + 7 * q * m
                assert [parent(start + k, a) for k in range(7)] == list(range(1, 8))
                assert parent(start - 1, a) == parent(start + 7, a) == 0
    print(json.dumps({'RS1_pulse_controls': 'PASS', 'heights': 'h=1..8, |a|<=h',
                      'equal_support_comparisons': cases}), flush=True)


def strip_controls(kit):
    src = (kit / 'lean/Ruliology/CellularAutomata/Rule30FourLeftSides.lean').read_text()
    lines = {name: re.search(r'^def ' + name + r' : Nat := (.*)$', src, re.M)[1]
             for name in ('A0', 'A1', 'B0', 'B1')}
    a0 = int(re.search(r'0x[0-9a-f]+', lines['A0'])[0], 16)
    def delta(name):
        return (int(re.findall(r'0x[0-9a-f]+', lines[name])[-1], 16)
                << int(re.search(r'<<< (\d+)', lines[name])[1]))
    a1, b0 = a0 ^ delta('A1'), a0 ^ delta('B0')
    values = {'A0': a0, 'A1': a1, 'B0': b0, 'B1': b0 ^ delta('B1')}
    k = 87867
    mask = (1 << k) - 1
    result = {}
    for name, v in values.items():
        rows, x = [], v
        for _ in range(16):
            rows.append(format(x, '0' + str(k) + 'b')[::-1])
            x = ((x << 2) ^ ((x << 1) | x)) & mask
        assert x == v
        w = [sum((rows[r][j] == '1') << r for r in range(16)) for j in range(k)]
        f = [0, 1]
        for j in range(2, k):
            t = max(f[j - 2], f[j - 1])
            if w[j - 1]:
                delay = next(d for d in range(16) if (w[j - 1] >> ((t + d) % 16)) & 1)
                f.append(t + delay + 1)
            else:
                f.append(t)
        black = min((f[j] - j, j) for j in range(2, k) if w[j - 1])
        white = min((f[j] - (j - 1), j) for j in range(2, k) if not w[j - 1])
        assert black[0] >= 0 and white[0] >= 0
        result[name] = {'black_W1_slack': black, 'white_W1_slack': white,
                        'F3': f[3], 'F87866': f[-1]}
    print(json.dumps({'half_row_birth_guards': 'PASS', 'strips': result}), flush=True)


def original_guard(raw):
    p = raw / 'R-04/k_guard3.py'
    expected = 'db4bd5ccd897071ac660251274caee3926c0cf4f9889ba216633465c16da3ce7'
    assert hashlib.sha256(p.read_bytes()).hexdigest() == expected
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        runpy.run_path(str(p), run_name='__main__')
    expected_lines = [
        'control 116976 117702',
        'least P, two rules: 19197 {71115: 54472, 77909: 58354} P-1: {71115: 54273, 77909: 58180}',
        'at 19,656: {71115: 54841, 77909: 58753} True',
    ]
    assert out.getvalue().splitlines() == expected_lines, out.getvalue()
    print(json.dumps({'original_k_guard3_replay': 'PASS', 'source_sha256': expected,
                      'lines': expected_lines}), flush=True)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--raw-root', type=Path, required=True)
    ap.add_argument('--kit-root', type=Path, required=True)
    args = ap.parse_args()
    local_controls()
    pulse_controls()
    strip_controls(args.kit_root)
    original_guard(args.raw_root)
    print(json.dumps({'result': 'PASS'}), flush=True)
