#!/usr/bin/env python3
"""rule30_r88_census.py: RC88, how many q = 8 rooted walks first return to zero at r = 88, and with which return
words (Q7's "other r88 / r52808 components"; PERIOD-TWO.md §6). Drawn by Local under draw-and-work (seed 1791575358,
chat L482); predictions pushed before the run.

RUN-ON:     cpu (Python 3); seconds
COMMAND:    python3 tests/probes/lexicon/rule30_r88_census.py

The walk is S84's (rule30_pr195_d0.py): q-periodic profiles, (x, y) -> (y, c) for each child c of (x, y) by the
descending recursion. A rooted walk starts at (a, 0), with a = blk | blk << 4 for an odd 4-bit block, and first returns
to zero when a child is 0. S84's witness takes the first child at every step and returns at r = 88, with return word
w = 00111101 (time order) and prof[r - 1] = prof[r - 2] = w.
Instead of following one child, this tracks the set of pair states reachable at each depth with no zero profile yet,
over every source and every child choice. That is exact over all walks, because the state space has 2^16 pairs. A
first return at depth r is a reachable state (x, y) at depth r - 1 with 0 among its children. Its return word is
y = prof[r - 1]. The D0 shape needs prof[r - 2] = prof[r - 1] = w, that is the state (w, w).

PREDICTIONS (Local's, published before the run):
  RC-C1 (control): the census contains S84's witness: from a = 17, a first return at r = 88 through the state (w, w)
        with w = 00111101.
  RC-P1 (blind, confidence 0.6): at r = 88 there is more than one return word, up to rotation, in the D0 shape
        (state (w, w)).
  RC-P2 (blind, confidence 0.5): first returns occur at more than 20 distinct depths r <= 400.
  RC-D1 (descriptive): the first-return depths r <= 400 with their counts of return words. At r = 88: every return
        word, its rotation class, and whether it has the D0 shape.
"""
import sys

Q = 8


def children(a, b, q=Q):
    out = []
    bit = lambda w, t: (w >> (t % q)) & 1
    for c0 in (0, 1):
        c = [c0]
        for t in range(q - 1):
            c.append(bit(a, t) ^ (bit(b, t) | c[t]))
        if bit(a, q - 1) ^ (bit(b, q - 1) | c[q - 1]) == c0:
            out.append(sum(v << t for t, v in enumerate(c)))
    return out


def rotclass(w, q=Q):
    return min(((w >> d) | (w << (q - d))) & ((1 << q) - 1) for d in range(q))


def tstr(w, q=Q):
    return ''.join(str((w >> t) & 1) for t in range(q))


def main(RMAX=400):
    CH = {(x, y): children(x, y) for x in range(1 << Q) for y in range(1 << Q)}
    roots = [blk | (blk << 4) for blk in range(16) if bin(blk).count('1') % 2]
    # depth 1: the first child step from (a, 0) gives (0, c); a walk's profiles are 0, c, ...; depth = number of steps
    layer = {}
    for a in roots:
        for c in CH[(a, 0)]:
            if c:
                layer.setdefault((0, c), set()).add(a)
    returns = {}
    depth = 1
    witness_ok = False
    while layer and depth < RMAX:
        nxt = {}
        for (x, y), srcs in layer.items():
            for c in CH[(x, y)]:
                if c == 0:
                    r = depth + 1
                    returns.setdefault(r, set()).add((x, y, frozenset(srcs)))
                    if r == 88 and 17 in srcs and x == y == int('00111101'[::-1], 2):
                        witness_ok = True
                else:
                    nxt.setdefault((y, c), set()).update(srcs)
        layer = nxt
        depth += 1
    print('RC-C1', 'PASS' if witness_ok else 'FAIL', flush=True)
    rs = sorted(returns)
    print('first-return depths r <= %d (%d distinct): %s' % (RMAX, len(rs), ' '.join(
        '%d:%d' % (r, len({y for x, y, s in returns[r]})) for r in rs)))
    r88 = returns.get(88, set())
    shapes = {}
    for x, y, srcs in r88:
        shapes.setdefault(rotclass(y), set()).add((tstr(x), tstr(y), x == y, tuple(sorted(srcs))))
    print('r = 88: %d return states, %d return words up to rotation' % (len(r88), len(shapes)))
    for cls, items in sorted(shapes.items()):
        for xs, ys, d0, srcs in sorted(items):
            print('  class %s: prof[r-2] = %s, prof[r-1] = %s, D0 shape %s, sources %s' % (tstr(cls), xs, ys, d0, list(srcs)))
    d0classes = {cls for cls, items in shapes.items() if any(d0 for _, _, d0, _ in items)}
    print('RC-P1', 'HELD' if len(d0classes) > 1 else 'REFUTED', '(%d D0-shape classes at r = 88)' % len(d0classes))
    print('RC-P2', 'HELD' if len(rs) > 20 else 'REFUTED', '(%d distinct depths)' % len(rs))
    print('COMPLETE')


if __name__ == '__main__':
    main()
