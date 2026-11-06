#!/usr/bin/env python3
"""Independent Boolean-column truth tables for the finite seam relation.

Each integer below is a column of the truth table over all input assignments,
not an encoded spatial row. No imported dynamics implementation.
"""
import argparse
import json
from pathlib import Path


def cone(n, seam, past=None, gap=2):
    count = 1 << n
    mask = (1 << count) - 1
    # Assignment index v has initial cell i equal to bit i of v.
    row = []
    for i in range(n):
        block = 1 << i
        stripes = ((1 << block) - 1) << block
        period = 2 * block
        while period < count:
            stripes |= stripes << period
            period *= 2
        row.append(stripes)
    heads, at_seam = {}, None
    for t in range(seam + 2 * gap + 1):
        heads[t] = row[0]
        if t == seam:
            at_seam = row[:7]
        if t < seam + 2 * gap:
            boundary = mask if t % 2 else 0  # start at odd physical phase
            row = [(boundary if i == 0 else row[i-1]) ^ (row[i] | row[i+1])
                   for i in range(len(row)-1)]
    ok = heads[seam] & heads[seam + 2 * gap]
    for k in range(1, gap):
        ok &= mask ^ heads[seam + 2 * k]
    for t, value in (past or {}).items():
        ok &= heads[t] if value else mask ^ heads[t]
    found = {}
    for prefix in range(128):
        choices = ok
        for i, col in enumerate(at_seam):
            choices &= col if prefix >> i & 1 else mask ^ col
        if choices:
            found[prefix] = {'count': choices.bit_count(),
                             'input_witness': (choices & -choices).bit_length()-1}
    return found


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--prior', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    original = json.loads(a.prior.read_text())
    future = cone(7, 0)
    one_past = cone(9, 2)
    five_past = cone(17, 10, {0: 1, 2: 0, 4: 0, 6: 0, 8: 0})
    gap3_past = cone(9, 2, gap=3)
    assert sorted(set(x & 31 for x in future)) == original['short_cones']['future_only_prefix5']
    assert sorted(set(x & 31 for x in one_past)) == original['short_cones']['with_one_sample_past_prefix5']
    assert sorted(five_past) == original['short_cones']['with_prior_gap5_and_next_gap2_prefix7']
    assert sorted(one_past) == [25, 49, 89]
    assert sorted(one_past) == sorted(five_past)
    assert 9 in future and 9 not in one_past
    assert sorted(set(x & 31 for x in gap3_past)) == [23]
    # Exact Boolean clauses: head=1, cells2,3=0, cell5=1,
    # cell6=NOT(cell4), and cell7 implies cell4.
    def clauses(r):
        c = lambda i: (r >> (i-1)) & 1
        return c(1) and not c(2) and not c(3) and c(5) and c(6) != c(4) and (not c(7) or c(4))
    assert [r for r in range(128) if clauses(r)] == sorted(one_past)
    a.out.mkdir(parents=True, exist_ok=True)
    result = {'future_only': future, 'one_past': one_past, 'five_past': five_past,
              'one_past_gap3': gap3_past,
              'independent_column_truth_table': True, 'clause_equivalence_128_cases': True,
              'dropping_past_guard_admits_9': True}
    (a.out/'column-check.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
