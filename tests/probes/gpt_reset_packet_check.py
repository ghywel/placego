#!/usr/bin/env python3
"""GC2463: tiny 128-parent self-check of the hand reset-packet lemma.

This is a one-update truth-table check, not a trajectory/history search.
The physical row spans old coordinates -8..7. The new thirteen-cell core
after re-origin at -7 spans old coordinates -6..6.
"""
import json

TAB = ((0,0,1,1),(0,1,1,0),(1,1,0,1),(0,1,0,1),
       (0,0,1,1),(0,0,0,1),(0,0,0,1))


def main():
    accepted = []
    for word in range(128):
        before = [TAB[(x+2) % 7][2] if x <= 0 else (word >> (x-1)) & 1
                  for x in range(-8, 8)]
        after = [before[i-1] ^ (before[i] | before[i+1])
                 for i in range(1, len(before)-1)]
        assert len(after) == 14  # old coordinates -7..6
        assert after[0] == TAB[2][3]  # the new anchor remains reference
        fell = after[7] != TAB[2][3]  # old coordinate 0
        core = sum(after[i+1] << i for i in range(13))
        physical = fell and core == 1951
        pattern = (word & 31) == 25 and (word >> 5) != 0
        assert physical == pattern, (word, fell, core)
        if physical:
            accepted.append(word)
    assert accepted == [57, 89, 121]
    print(json.dumps(dict(status='PASS', parents_checked=128,
                          accepted=accepted,
                          scope='one physical update, phase2 ether-left, root-specific core1951; no actual-history existence assertion')))


if __name__ == '__main__':
    main()
