"""GC651: fixed L224 witness scope check, preregistered in CLOUD-LOCAL.

No census or ancestry replay. Uses published literal words, including the
endpoint solely to validate the last edge. Works across ledger rotations.
"""
import json
import re
from pathlib import Path

from rule30_hw32_literal_audit import reset, scalar_edge


def main():
    blocks = []
    for path in Path('.').glob('CHAT-LEDGER*.md'):
        text = path.read_text()
        if '\n## L224 ' in '\n' + text:
            blocks.append(('\n' + text).split('\n## L224 ', 1)[1]
                          .split('\n## ', 1)[0])
    assert len(blocks) == 1, 'Require exactly one authoritative L224'
    matches = re.findall(
        r'^    (\d+) ([0-9a-f]{8}) ([0-9a-f]{8}) (\d+) (\d+) (-?\d+)$',
        blocks[0], re.M)
    rows = [(int(d), int(a, 16), int(b, 16), int(pc), int(dl), int(z))
            for d, a, b, pc, dl, z in matches]
    assert len(rows) == 40
    clocks = []
    for d, a, b, pc, delay, z in rows:
        assert (z + 5*d) % 2 == 0
        t = (z + 5*d)//2
        clocks.append(t)
        assert b.bit_count() == pc and reset(b, t) == delay
    for i, (left, right) in enumerate(zip(rows, rows[1:])):
        assert right[0] == left[0]+1 and right[1] == left[2]
        assert scalar_edge(left[1], left[2], right[2])
        assert clocks[i+1]-clocks[i] == left[4]
        assert right[5]-left[5] == 2*left[4]-5
    delays = [r[4] for r in rows[:-1]]
    pairs = [a+b for a, b in zip(delays, delays[1:])]
    assert len(delays) == 39 and sum(delays) == 176
    assert rows[-1][5]-rows[0][5] == 2*176-5*39 == 157
    assert not scalar_edge(rows[0][1], rows[0][2], rows[1][2] ^ 1)
    assert reset(rows[0][2], clocks[0]+1) != delays[0]
    # Unexpected endpoint check: its own delay is outside the witness.
    assert 2*sum(delays+[rows[-1][4]])-5*40 == 156
    out = dict(edges=39, adjacent_pairs=len(pairs), elapsed=176,
               doubled_debt=157, max_delay=max(delays),
               max_pair_sum=max(pairs), long_pair_triggers=sum(s>32 for s in pairs),
               endpoint_included_doubled_debt=156, controls='PASS',
               scope='literal segment only; no ancestry or census replay')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
