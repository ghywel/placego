#!/usr/bin/env python3
"""One complete local truth table for continuing808 versus launch4520."""
import argparse
import collections
import json
from pathlib import Path
from image_ancestry_audit import trajectory


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    table, counts = [], collections.Counter()
    for suffix in range(1024):
        row = 72 | (suffix << 7)
        tr = trajectory(row, 113, 16)
        tail = sum((tr[k] >> 7 & 1) << k for k in range(10))
        continuing = row & 2047 == 1096
        launching = row & 4095 == 72
        assert (tail == 50) == continuing
        assert (tail == 282) == launching
        if continuing:
            assert tr[10] & 127 == 64 and tr[16] & 1 == 1
        if launching:
            assert tr[10] & 127 == 56 and tr[16] & 1 == 0
        table.append([row, tail, tr[10] & 127, tr[16] & 1])
        counts[tail] += 1
    assert counts[50] == 64 and counts[282] == 32
    # Earlier-row form: five output whites with the incoming three blacks.
    earlier = []
    for suffix in range(16):
        root = 475 | (suffix << 9)  # row112 low9 = 91 + 128 + 256
        tr = trajectory(root, 112, 1)
        guard = root & 2047 == 2011 and bool(root & (3 << 11))
        assert (tr[1] & 4095 == 72) == guard
        earlier.append([root, tr[1] & 4095, guard])
    result = {'cases': 1024, 'continuing808': 64, 'launch4520': 32,
              'other': 928, 'full_tail_word_counts': dict(sorted(counts.items())),
              'table_columns': ['row113_low17', 'column8_word113_122', 'row123_low7', 'head129'],
              'table': table, 'row112_control': earlier,
              'scalar_and_integer_agree_all_cells': True,
              'scope': 'Local actual-row equivalences only; no prior-first-E feasibility or autonomous return state.'}
    (out / 'selector.json').write_text(json.dumps(result, indent=2) + '\n')
    print('SWITCH_SELECTOR_PASS')
    print(json.dumps({k: v for k, v in result.items() if k not in ('table', 'row112_control')}))


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--out', type=Path, required=True)
    main(p.parse_args().out)
