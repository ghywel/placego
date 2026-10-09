"""GC684: one fixed L224 continuation, at most256 edges; stop at a zero driver."""
import json
import re
from pathlib import Path

LIMIT = 256


def bit(w, t):
    return (w >> (t % 32)) & 1


def reset_child(a, b):
    t0 = next(t for t in range(32) if bit(b, t))
    t = (t0 + 1) % 32
    value = 1 ^ bit(a, t0)
    out = 0
    for _ in range(32):
        out |= value << t
        value = bit(a, t) ^ (bit(b, t) | value)
        t = (t + 1) % 32
    assert value == bit(out, t)
    return out


def scalar_children(a, b):
    # Independent time-zero closure, with a literal truth table.
    table = (0, 1, 1, 1, 1, 0, 0, 0)
    valid = []
    for initial in (0, 1):
        values = [initial]
        for t in range(32):
            values.append(table[4 * bit(a, t) + 2 * bit(b, t) + values[-1]])
        if values[-1] == initial:
            valid.append(sum(v << t for t, v in enumerate(values[:-1])))
    return valid


def main():
    blocks = []
    for path in Path('.').glob('CHAT-LEDGER*.md'):
        source = '\n' + path.read_text()
        if '\n## L224 ' in source:
            blocks.append(source.split('\n## L224 ', 1)[1].split('\n## ', 1)[0])
    assert len(blocks) == 1
    rows = [tuple(int(x, 16) if j in (1, 2) else int(x)
                  for j, x in enumerate(parts))
            for parts in re.findall(
                r'^    (\d+) ([0-9a-f]{8}) ([0-9a-f]{8}) (\d+) (\d+) (-?\d+)$',
                blocks[0], re.M)]
    assert len(rows) == 40
    clocks = [(r[5] + 5 * r[0]) // 2 for r in rows]
    assert 2 * (clocks[-1] - clocks[0]) - 5 * 39 == 157
    for left, right in zip(rows, rows[1:]):
        assert scalar_children(left[1], left[2]) == [right[2]]
        assert reset_child(left[1], left[2]) == right[2]
    depth, a, b, _, endpoint_delay, _ = rows[-1]
    clock = clocks[-1]
    initial_clock = clock
    debt2 = 157
    peak2 = debt2
    first_repayment = None
    repayment_elapsed = None
    repayment_debt2 = None
    post_repayment_peak2 = None
    first_delay = None
    steps = 0
    pulse_drivers = 0
    fast = mismatch_sum = 0
    repayment_account = None
    stopped = 'limit'
    for j in range(LIMIT):
        if b == 0:
            stopped = 'zero-driver branch; no choice made'
            break
        pulse_drivers += any(all(bit(b, t) == int(t % period == residue)
                                 for t in range(32))
                             for period in (1, 2, 4, 8, 16, 32)
                             for residue in range(period))
        delay = next(k + 1 for k in range(32) if bit(b, clock + k))
        grandparent = sum((bit(b, t + 1) ^ (bit(a, t) | bit(b, t))) << t
                          for t in range(32))
        if j == 0:
            assert grandparent == rows[-2][1]
        assert bit(a, clock - 1) == 1
        if bit(grandparent, clock - 1) == 0:
            assert delay == 1
            fast += 1
        else:
            assert grandparent != a
            distance = next(k for k in range(32)
                            if bit(grandparent ^ a, clock + k))
            assert delay == distance + 2
            mismatch_sum += distance
        child = reset_child(a, b)
        assert scalar_children(a, b) == [child]
        if first_delay is None:
            first_delay = delay
            assert delay == endpoint_delay == 2
        clock += delay
        debt2 += 2 * delay - 5
        peak2 = max(peak2, debt2)
        steps += 1
        if debt2 <= 0 and first_repayment is None:
            first_repayment = steps
            repayment_elapsed = clock - initial_clock
            repayment_debt2 = debt2
            repayment_account = dict(edges=steps, fast=fast, mismatch_sum=mismatch_sum)
        if first_repayment is not None:
            post_repayment_peak2 = (debt2 if post_repayment_peak2 is None
                                     else max(post_repayment_peak2, debt2))
        assert debt2 - 157 == 2 * mismatch_sum - steps - 2 * fast
        a, b = b, child
    print(json.dumps(dict(limit=LIMIT, steps=steps, stopped=stopped,
                          first_extension_delay=first_delay,
                          first_repayment_edges=first_repayment,
                          first_repayment_elapsed=repayment_elapsed,
                          first_repayment_doubled_debt=repayment_debt2,
                          later_peak_doubled_debt=post_repayment_peak2,
                          initial_doubled_debt=157, peak_doubled_debt=peak2,
                          final_doubled_debt=debt2,
                          extension_elapsed=clock - initial_clock,
                          independent_child_controls=39 + steps,
                          first_extension_depth=depth,
                          pulse_drivers=pulse_drivers,
                          fast_branches=fast, selected_mismatch_sum=mismatch_sum,
                          first_repayment_account=repayment_account), sort_keys=True))


if __name__ == '__main__':
    main()
