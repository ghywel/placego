#!/usr/bin/env python3
"""GC2396: fixed three-step, actual-phase word screen; no trajectory census.

Read reports/GPT-RESET-PHASE-SCREEN-20261102.md for the frozen prediction/caps.
No subprocesses, threads, solver, random seeds, or horizon parameters.
"""
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = 12
MASK = (1 << 28)-1


def step(x):
    return (x ^ ((x << 1) | (x << 2) | 3)) & MASK


ring = list(map(int, (HERE/'phase1024_ring.txt').read_text().strip()))
row = ring[:]
col0 = []
for t in range(1024):
    col0.append(row[0])
    row = [row[j] ^ (row[j-1] | row[j-2]) for j in range(len(row))]
assert row == ring
assert all(ring[n] == col0[(195*n) % 1024] for n in range(len(ring)))
cols = [int(line.split()[0], 16) for line in (HERE/'phase480_p32.txt').read_text().splitlines()
        if line and not line.startswith('#')]
assert len(cols) == 480
out = {}
for name in ('P1024', '480'):
    states = range(1024) if name == 'P1024' else range(480*32)
    result = {'classes': len(states), 'reset_words': 0, 'next_blocked': 0,
              'same_plus1_different_pair': 0, 'first_witness': None}
    for cls in states:
        if name == 'P1024':
            def bit(n, t=0):
                return col0[(cls+t+195*(n-R)) % 1024]
        else:
            a, q = divmod(cls, 32)
            def bit(n, t=0):
                return (cols[(a+n-R) % 480] >> ((q+t) % 32)) & 1
        # Check the exact word against its own actual next phase, before using it.
        assert all(bit(n, 1) == (bit(n) ^ (bit(n-1) | bit(n-2))) for n in range(2, 28))
        if bit(R) or bit(R+1) or bit(R+2) != bit(R+3):
            continue
        result['reset_words'] += 1
        erow = sum(bit(n) << n for n in range(28))
        e2 = step(step(erow))
        if not ((e2 >> (R+5)) & 1):
            continue
        result['next_blocked'] += 1
        histories = []
        for u in (0, 1):
            e, x = erow, erow ^ (1 << R) ^ (1 << (R-3)) ^ (u << (R-1))
            hist = []
            for t in range(4):
                delta = e ^ x
                front = delta.bit_length()-1
                pair = [(delta >> (front-1)) & 1, (delta >> (front-2)) & 1]
                hist.append({'front': front, 'pair': pair})
                if t < 3:
                    e, x = step(e), step(x)
            assert hist[1]['front'] == R+2 and hist[2]['front'] == R+4
            assert hist[2]['pair'] == [(1-bit(R-1))*(1-bit(R+2)), bit(R-1) | bit(R-2)]
            histories.append(hist)
        if (histories[0][3]['front'] == histories[1][3]['front'] == R+5
                and histories[0][3]['pair'] != histories[1][3]['pair']):
            result['same_plus1_different_pair'] += 1
            if result['first_witness'] is None:
                result['first_witness'] = {'front_class': cls, 'R': R,
                    'alignment': {'theta': (cls-195*R) % 1024} if name == 'P1024' else {'a': (a-R) % 480, 'q': q},
                    'reference_row_hex': hex(erow), 'D_initial_hex': [hex((1 << R) ^ (1 << (R-3)) ^ (u << (R-1))) for u in (0, 1)],
                    'histories': histories}
    out[name] = result
dest = Path(os.environ['CAPPED_OUT'])/'results.json'
dest.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
print('RESET_PHASE_SCREEN_DONE')
