#!/usr/bin/env python3
"""Exact finite ancestry and its diagonal cut; no candidate or SAT search.

Rule30Predecessors.T/back/eq_back already give the inverse transfer.
This specializes it to white tails and a prescribed alternating center,
then exposes the state at the physical 4-to-7 seam's 167-cell cut.
"""
import argparse
import json
from pathlib import Path

A, E = '25', '33535555'


def step(x, b):
    return ((x << 1) | b) ^ (x | (x >> 1))


def drive(t):
    return int(t % 2 == 0)


def tail_step(x):
    return x ^ ((x >> 1) | (x >> 2))


def tail_inverse(y):
    x = 0
    for i in range(y.bit_length() - 1, -1, -1):
        value = ((y >> i) & 1) ^ (((x >> (i + 1)) | (x >> (i + 2))) & 1)
        x |= value << i
    return x


def complete_tail(q, m):
    """Unique m-step driven image with high tail q above its first m cells."""
    root = q
    for _ in range(m):
        root = tail_inverse(root)
    return root, rows(root, m)[-1]


def rows(x, n):
    out = [x]
    for t in range(n):
        x = step(x, drive(t))
        out.append(x)
    return out


def inverse(y, b):
    # Cell indices are 1-based; finite predecessor has width at most N-1.
    x = 0
    for i in range(y.bit_length(), 1, -1):
        bit = ((y >> (i - 1)) & 1) ^ (((x >> (i - 1)) | (x >> i)) & 1)
        x |= bit << (i - 2)
    return x if (y & 1) == (b ^ ((x | (x >> 1)) & 1)) else None


def ancestry(y, m):
    out = [y]
    for t in range(m - 1, -1, -1):
        y = inverse(y, drive(t))
        if y is None:
            return {'accepted': False, 'failed_boundary_time': t}
        out.append(y)
    return {'accepted': True, 'rows': list(reversed(out))}


def diagonal(y, m, wanted=None, cut=None, pad=0):
    """Sweep v_t(k)=x^t_(k+t) from right to left, reconstructing all rows.

    At the cut retain two diagonals of each live predecessor row. Earlier
    boundary/head constraints are checked before discarding their rows.
    Returned rows are diagnostic; the accepting scan needs only the pairs.
    """
    wanted = wanted or {}
    near, far = [0] * m, [0] * m
    reconstructed = [0] * m + [y]
    heads, bad_boundary, bad_head = {}, [], []
    interface = None
    for j in range(max(y.bit_length(), m + 1) + pad, 0, -1):
        k = j - m
        value = (y >> (j - 1)) & 1
        if j == 1:
            heads[m] = value
        current = [0] * m
        for s in range(m - 1, -1, -1):
            position = k + s
            if position < 0:
                break
            value ^= near[s] | far[s]
            current[s] = value
            if position == 0:
                if value != drive(s):
                    bad_boundary.append(s)
            else:
                reconstructed[s] |= value << (position - 1)
                if position == 1:
                    heads[s] = value
        far, near = near, current
        if cut is not None and j == cut + 1:
            first = max(0, m - cut)
            interface = {
                'prefix_cells': cut, 'first_live_time': first,
                'live_pair_bits': 2 * (m - first),
                'near': ''.join(map(str, near[first:])),
                'far': ''.join(map(str, far[first:])),
                'boundary_failures_so_far': bad_boundary.copy(),
                'checked_head_times': sorted(t for t in heads if t in wanted),
                'head_failures_so_far': sorted(t for t in heads
                                              if t in wanted and heads[t] != wanted[t]),
            }
    bad_head = sorted(t for t, value in wanted.items() if heads[t] != value)
    return {'accepted': not bad_boundary and not bad_head,
            'boundary_failures': bad_boundary, 'head_failures': bad_head,
            'rows': reconstructed, 'heads': heads, 'interface': interface}


def word_heads(word, start):
    ones = {0}
    end = 0
    for c in word:
        end += int(c)
        ones.add(end)
    return {start + 2 * s: int(s in ones) for s in range(end + 1)}


def accepts_physical_47(y):
    # Full white-tail seam row at physical time193, not a truncated row.
    # Original root width<=360 gives seam width<=553 (b_0=1 also
    # starts the zero root's edge). This keeps the original finite query.
    if y < 0 or y.bit_length() > 553:
        return False
    past = diagonal(y, 193, word_heads(E + A * 4 + E, 1), cut=167)
    if not past['accepted']:
        return False
    value = y & ((1 << 167) - 1)
    expected = word_heads(A * 7 + E, 193)
    for t in range(193, 360):
        if t in expected and (value & 1) != expected[t]:
            return False
        value = step(value, drive(t))
    return True


def scalar_heads(x, start, duration):
    width = x.bit_length() + duration + 3
    cell = [(x >> i) & 1 for i in range(width)]
    out = []
    for t in range(start, start + duration + 1):
        out.append(cell[0])
        cell = [(drive(t) if i == 0 else cell[i - 1]) ^
                (cell[i] | (cell[i + 1] if i + 1 < width else 0))
                for i in range(width)]
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    # Complete one-step oracle: all outputs of width<=13 have predecessors
    # of width<=12. Exhaustive lookup is independent of inverse transfer.
    checked = 0
    for b in (0, 1):
        lookup = {step(x, b): x for x in range(1 << 12)}
        assert len(lookup) == 1 << 12
        for y in range(1 << 13):
            assert inverse(y, b) == lookup.get(y)
            checked += 1
    # Both accepted and rejected finite histories, including short/zero rows.
    for m in (1, 2, 5):
        for y in range(256):
            ref, scan = ancestry(y, m), diagonal(y, m)
            assert ref['accepted'] == scan['accepted']
            if ref['accepted']:
                assert ref['rows'] == scan['rows']
            else:
                assert ref['failed_boundary_time'] == max(scan['boundary_failures'])
    for root in range(32):
        expected = rows(root, 7)
        heads = {t: x & 1 for t, x in enumerate(expected)}
        scan = diagonal(expected[-1], 7, heads)
        assert scan['accepted'] and scan['rows'] == expected
        assert diagonal(expected[-1], 7, heads, pad=4)['rows'] == expected
        mutant = heads.copy()
        mutant[3] ^= 1
        assert diagonal(expected[-1], 7, mutant)['head_failures'] == [3]
    # Independent forward lookup of every 8-bit tail at four depths.
    # This tests both surjectivity and the inverse-based completion, not
    # merely whether the completion function agrees with its own scanner.
    for depth in (1, 2, 5, 7):
        lookup = {}
        for root in range(256):
            image = rows(root, depth)[-1]
            q = image >> depth
            assert q not in lookup
            lookup[q] = (root, image)
            d = root
            for _ in range(depth):
                d = tail_step(d)
            assert d == q
        assert len(lookup) == 256
        for q in range(256):
            assert complete_tail(q, depth) == lookup[q]
    # One frozen causal-versus-ancestry control; it is not a bridge witness.
    root, m, cut = 19, 193, 167
    full = rows(root, m)
    y = full[-1]
    changed = y ^ (1 << cut)  # physical cell168, beyond the future cone.
    wanted = {t: full[t] & 1 for t in range(1, m + 1, 2)}
    good = diagonal(y, m, wanted, cut)
    bad = diagonal(changed, m, wanted, cut)
    assert good['accepted'] and good['rows'] == full
    assert ancestry(y, m)['rows'] == full
    assert complete_tail(y >> m, m) == (root, y)
    reference_bad = ancestry(changed, m)
    assert reference_bad['accepted'] == (not bad['boundary_failures'])
    if reference_bad['accepted']:
        assert reference_bad['rows'] == bad['rows']
    else:
        assert reference_bad['failed_boundary_time'] == max(bad['boundary_failures'])
    assert (y ^ changed) & ((1 << cut) - 1) == 0
    future = scalar_heads(y, m, 166)
    assert future == scalar_heads(changed, m, 166)
    # Minimal retained snapshot: both full rows remain in output for replay.
    for scan in (good, bad):
        scan.pop('rows')
        scan.pop('heads')
    result = {
        'controls': {'one_step_exhaustive_cases': checked,
                     'small_ancestry_cases': 768, 'seven_step_seeds': 32,
                     'tail_completion_cases': 1024,
                     'seam_tail_completion': True,
                     'wrong_head_rejected': True, 'zero_padding_invariant': True},
        'control_not_bridge_witness': True,
        'seed': root, 'seam_tick': m, 'seam_hex': hex(y),
        'changed_cell': 168, 'changed_seam_hex': hex(changed),
        'future_column1_equal_ticks_including_seam': 167,
        'original': good, 'changed': bad,
        'changed_sequential_ancestry': {k: v for k, v in reference_bad.items() if k != 'rows'},
        'physical47_accepts_control': accepts_physical_47(y),
    }
    (args.out / 'ancestry.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('original', 'changed')}, indent=2))


if __name__ == '__main__':
    main()
