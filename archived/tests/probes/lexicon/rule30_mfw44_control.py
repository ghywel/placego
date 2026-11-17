"""rule30_mfw44_control.py: checks of rule30_local_mfw44.txt (L641), the certified minimal forbidden words of the real
visible language to length 44 in both phases.

1. Format and minimality: no duplicates, and no listed word has a proper factor in its phase's list.
2. Negative control: a random right half beside the clamped wall gives a REAL visible word (the left half is forced by
   the clamp), so no listed word of the phase may occur in it; phase 0's words may not occur in phase 1's words either
   (L1 c L). A word planted into a real word must be found, so the scan can fail.
The certificates themselves are cake_lpr's (rule30_mfw_certify.py); this is an independent sanity check, not a proof.
Usage: python3 rule30_mfw44_control.py [N=3000] [T=500]. L641's run: N = 3000, T = 500, PASS, 8 s.
"""
import os
import re
import sys

import numpy as np

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rule30_local_mfw44.txt')


def lists():
    txt = open(P).read()
    out = {}
    for m in re.finditer(r'^## phase (\d): (\d+) words.*\n((?:[01]+\n?)+)', txt, re.M):
        out[int(m.group(1))] = m.group(3).split()
        assert len(out[int(m.group(1))]) == int(m.group(2))
    return out


def minimal(ws):
    s = set(ws)
    assert len(s) == len(ws), 'duplicates'
    for w in ws:
        for k in range(1, len(w)):
            for i in range(len(w) - k + 1):
                assert w[i:i + k] not in s, (w, w[i:i + k])


def real_visible(ph, N, T, rng):
    """N real visible words: column 1 at the white-wall times t <= T, (t + phase) even."""
    row = rng.integers(0, 2, size=(N, T + 6), dtype=np.uint8)
    row[:, -2:] = 0
    vis = []
    for t in range(T + 1):
        wall = (t + ph) % 2
        if wall == 0:
            vis.append(row[:, 0].copy())
        left = np.concatenate([np.full((N, 1), wall, np.uint8), row[:, :-1]], axis=1)
        right = np.concatenate([row[:, 1:], np.zeros((N, 1), np.uint8)], axis=1)
        row = left ^ (row | right)
    return [''.join(map(str, r)) for r in np.stack(vis, axis=1)]


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    T = int(sys.argv[2]) if len(sys.argv) > 2 else 500
    ls = lists()
    assert sorted(ls) == [0, 1]
    for ph in (0, 1):
        minimal(ls[ph])
    rng = np.random.default_rng(20261011)
    for ph in (0, 1):
        words = real_visible(ph, N, T, rng)
        hits = sum(1 for v in words for w in ls[ph] if w in v)
        cross = sum(1 for v in words for w in ls[0] if w in v) if ph == 1 else 0
        planted = words[0][:50] + ls[ph][-1] + words[0][50:]
        assert any(w in planted for w in ls[ph])
        print('phase %d: %d words, minimal; %d real visible words of length %d: %d list hits, %d phase-0 hits; planted '
              'word found' % (ph, len(ls[ph]), N, len(words[0]), hits, cross), flush=True)
        assert hits == 0 and cross == 0
    print('MFW44-CONTROL PASS')


if __name__ == '__main__':
    main()
