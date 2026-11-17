#!/usr/bin/env python3
"""rule30_witness_check.py: re-simulate a record witness from its written bits, independently of the RLK code.

RUN-ON:     cpu (Python 3, no solver); under a second
COMMAND:    python3 tests/probes/lexicon/rule30_witness_check.py D L PHASE LEFT RIGHT [VISIBLE]
            LEFT is cells -T .. 0 at time 0 (T = D + L - 1, so LEFT has T + 1 bits), RIGHT is sites 1 .. n; cells
            outside are 0 (outside column 0's light cone through T, so their values do not matter)
Checks, with a plain Rule 30 loop (new = left XOR (centre OR right)) on one row:
  - the band: cells -D .. -(D + L - 1) are white at time 0;
  - the clock: column 0 equals (t + PHASE) mod 2 at every t = 0 .. T;
  - optionally, column 1 at the times t < T with (t + PHASE) even spells VISIBLE.
All three passing means R_real(D) >= L in that phase, by an explicit finite configuration (L596).
"""
import sys


def check(d, L, ph, left, right, vis=None):
    T = d + L - 1
    assert len(left) == T + 1, 'LEFT must be cells -T .. 0'
    off = T + 4                                     # index of cell 0 in the row
    row = [0] * (off + len(right) + T + 4)
    for j, b in enumerate(left):
        row[off - T + j] = int(b)
    for j, b in enumerate(right):
        row[off + 1 + j] = int(b)
    band = all(row[off - j] == 0 for j in range(d, d + L))
    clock, seen = True, []
    for t in range(T + 1):
        clock &= row[off] == (t + ph) % 2
        if t < T and (t + ph) % 2 == 0:
            seen.append(str(row[off + 1]))
        row = [0] + [row[i - 1] ^ (row[i] | row[i + 1]) for i in range(1, len(row) - 1)] + [0]
    return band, clock, (None if vis is None else ''.join(seen) == vis)


if __name__ == '__main__':
    d, L, ph = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    band, clock, v = check(d, L, ph, sys.argv[4], sys.argv[5], sys.argv[6] if len(sys.argv) > 6 else None)
    print('band white: %s; clock through T = %d: %s; visible matches: %s' % (band, d + L - 1, clock, v))
    print('WITNESS VALID: R_real(%d) >= %d (phase %d)' % (d, L, ph) if band and clock and v is not False else 'NOT VALID')
