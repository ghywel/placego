#!/usr/bin/env python3
"""Fixed real-history diagnostic and exhaustive short-cone seam checks.

No seed census, SAT call, graph lift, or adaptive horizon. Prefix integers
store physical cell 1 in bit 0. An odd-time sample advances with B1 o B0.
"""
import argparse
import json
from pathlib import Path

from physical_ancestry import (A, E, complete_tail, drive, rows, scalar_heads,
                               step, word_heads)


def sample(x):
    return step(step(x, 0), 1)


def gap2(x):
    return (x & 1) == 1 and (sample(x) & 1) == 0 and (sample(sample(x)) & 1) == 1


def short_checks():
    # Four ticks to the final head use exactly five initial cells.
    future = [r for r in range(32) if gap2(r)]
    assert future == [9, 17, 25]
    # Two preceding ticks plus those five cells use seven predecessor cells.
    past = sorted({sample(s) & 31 for s in range(128)
                   if gap2(sample(s))})
    assert past == [17, 25]
    assert all(not (sample(s) & 31 == 9) for s in range(128))
    # Independent scalar update for every seven-cell predecessor cone.
    for s in range(128):
        hs = scalar_heads(s, 1, 6)
        assert hs[2::2] == [sample(s) & 1, sample(sample(s)) & 1,
                            sample(sample(sample(s))) & 1]
    # Unexpected check: retain the preceding complete gap5, not just one row.
    # A seven-cell seam prefix after ten ticks has a 17-cell input cone.
    after5 = set()
    witnesses = {}
    for s in range(1, 1 << 17, 2):
        y = s
        for k in range(1, 6):
            y = sample(y)
            if bool(y & 1) != (k == 5):
                break
        else:
            if gap2(y):
                v = y & 127
                after5.add(v)
                witnesses.setdefault(v, s)
    return {'future_only_prefix5': future, 'with_one_sample_past_prefix5': past,
            'with_prior_gap5_and_next_gap2_prefix7': sorted(after5),
            'gap5_witnesses': witnesses,
            'scalar_predecessor_cones': 128, 'gap5_input_cones': 1 << 17}


def fixed_trace(out):
    seed, horizon = 2135555, 6000
    trajectory = rows(seed, horizon)
    # Distinct cell-array oracle and an initial-phase mutant on a short cone.
    assert scalar_heads(seed, 0, 700) == [x & 1 for x in trajectory[:701]]
    mutant = [seed]
    for t in range(100):
        mutant.append(step(mutant[-1], 1 - drive(t)))
    assert [x & 1 for x in mutant] != [x & 1 for x in trajectory[:101]]
    black = [t for t in range(1, horizon + 1, 2) if trajectory[t] & 1]
    gaps = [(b - a) // 2 for a, b in zip(black, black[1:])]
    starts = [i for i in range(len(gaps) - len(E) + 1)
              if gaps[i:i + len(E)] == list(map(int, E))]
    crossings = []
    for i in starts:
        anchor = black[i + len(E)]
        n = 0
        while gaps[i + len(E) + 2*n:i + len(E) + 2*n + 2] == [2, 5]:
            n += 1
        before = 0
        while i - 2 * before >= 2 and gaps[i-2*before-2:i-2*before] == [2, 5]:
            before += 1
        seam = trajectory[anchor]
        q = seam >> anchor
        root, reconstructed = complete_tail(q, anchor)
        assert root == seed and reconstructed == seam
        checks = []
        for shortened in (4, 7):
            expected = word_heads(A * shortened + E, anchor)
            failures = [t for t, b in expected.items()
                        if (trajectory[t] & 1) != b]
            branch = anchor + 14 * shortened
            r = trajectory[branch]
            checks.append({'A_blocks': shortened, 'first_head_failure_tick':
                           min(failures) if failures else None,
                           'first_failure_sample_offset':
                           (min(failures)-anchor)//2 if failures else None,
                           'branch_tick': branch, 'branch_prefix5': r & 31,
                           'branch_prefix7': r & 127,
                           'branch_has_gap2': gap2(r),
                           'expected_at_first_failure':
                           expected[min(failures)] if failures else None,
                           'actual_at_first_failure':
                           trajectory[min(failures)] & 1 if failures else None})
        crossings.append({'E_gap_index': i, 'E_start_tick': black[i],
                          'E_end_tick': anchor, 'A_before': before,
                          'A_after': n, 'next_gaps': gaps[i+len(E)+2*n:i+len(E)+2*n+8],
                          'seam_width': seam.bit_length(), 'q': q,
                          'q_width': q.bit_length(), 'seam_prefix7': seam & 127,
                          'shortened': checks})
    assert len(crossings) >= 2, 'fixed fixture has fewer than two E words'
    (out / 'fixed-gap-trace.json').write_text(json.dumps(
        {'seed': seed, 'horizon': horizon, 'black_ticks': black, 'gaps': gaps}, indent=2)+'\n')
    return {'seed': seed, 'horizon': horizon, 'E_crossings': crossings,
            'cell_oracle_ticks': 700, 'wrong_phase_mutant_rejected': True}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    result = {'short_cones': short_checks(), 'fixed_trace': fixed_trace(args.out)}
    (args.out / 'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
