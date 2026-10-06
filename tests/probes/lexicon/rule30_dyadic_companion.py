#!/usr/bin/env python3
"""rule30_dyadic_companion.py: GPT's G137 leaves open whether the dyadic word d (visible bit 1 exactly at indices that
are powers of two) can be column 1 beside the 0101 wall with a finite left half. It passes every repeat test of
Theorem E Step 0. This measures its forced left half directly (Local, 2026-10-06; PROOFS.md G137 note; chat).

RUN-ON:     cpu (pure Python 3, standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_dyadic_companion.py [K=4000]
COST:       about a minute at K = 4000.

Method (RULE30-PRIZE.md section 8.39, rule30_wall.py's forced_half): column 0 is t mod 2; column 1 carries the
visible bit c_s at time 2s and is invisible at odd times; the forced cells x_0(-j) of row 0 come from the sideways
inverse rule x_t(-j) = x_(t+1)(-j+1) XOR (x_t(-j+1) OR x_t(-j+2)), column by column, depth j needing times 0 .. j.
Finite left support would make row 0 zero from some depth on.

PREDICTIONS, written 2026-10-06 before this script's first run:
  DY0 (control): for 50 random visible words the bit-packed sideways computation equals rule30_wall.py's
      forced_half cell by cell on row 0 to depth 200.
  DY1 (blind): the forced row 0 for d has ones at depths beyond K/2 (no sign of a finite left half to depth K), for d
      and for its complement.
  DY2 (blind; the doubling law of section 8.36): every zero run of row 0 for d that starts at depth j >= 4 ends by
      depth 2j + 4.
"""
import random
import sys

sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from rule30_wall import forced_half  # noqa: E402


def row0(vis, K):
    """Forced row 0 cells x_0(-j), j = 1..K, from visible bits vis[s] (time 2s); bit-packed over time."""
    T = K + 2
    right = 0           # column 0 as a time bitmask: bit t = t mod 2
    for t in range(T + 1):
        if t % 2:
            right |= 1 << t
    far = 0             # column 1: bit 2s = vis[s], odd times 0 (invisible; Lemma 1 makes them irrelevant)
    for s_ in range(T // 2 + 1):
        if s_ < len(vis) and vis[s_]:
            far |= 1 << (2 * s_)
    out = []
    mask = (1 << (T + 1)) - 1
    for j in range(1, K + 1):
        # col_t = right_(t+1) XOR (right_t OR far_t), for t = 0 .. T-1
        col = ((right >> 1) ^ (right | far)) & (mask >> j)
        out.append(col & 1)
        far, right = right, col
    return out


def main():
    K = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    rng = random.Random(137)
    ok0 = True
    for trial in range(50):
        vis = [rng.randint(0, 1) for _ in range(150)]
        c = {2 * s_: vis[s_] for s_ in range(150)}
        cells = forced_half(c, 0, 200)
        mine = row0(vis, 200)
        ok0 &= all(cells[(0, j)] == mine[j - 1] for j in range(1, 201))
    print('DY0', 'PASS' if ok0 else 'FAIL', '(bit-packed row 0 = forced_half, 50 random words, depth 200)')
    for name, flip in (('d', 0), ('complement', 1)):
        vis = [(1 if s_ >= 1 and (s_ & (s_ - 1)) == 0 else 0) ^ flip for s_ in range(K // 2 + 3)]
        r = row0(vis, K)
        ones = [j + 1 for j, b in enumerate(r) if b]
        last = ones[-1] if ones else None
        dy1 = last is not None and last > K // 2
        runs_ok = True
        worst = None
        for a_, b_ in zip(ones, ones[1:]):
            start = a_ + 1
            if start >= 4 and b_ - 1 >= start:
                if b_ - 1 > 2 * start + 4:
                    runs_ok = False
                    worst = (start, b_ - 1) if worst is None else worst
        print('%s: ones to depth %d: %d, last at %s, largest gap %d' % (name, K, len(ones), last,
                                                                     max(b - a for a, b in zip(ones, ones[1:]))))
        print('  DY1', 'HELD' if dy1 else 'REFUTED', ' DY2', 'HELD' if runs_ok else 'REFUTED', worst or '')


if __name__ == '__main__':
    main()
