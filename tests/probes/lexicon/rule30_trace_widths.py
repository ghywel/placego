#!/usr/bin/env python3
"""rule30_trace_widths.py: TW, exact trace-language counts of Rule 30 at widths 1 and 2, in the physical frame and in
the G frame (Cloud's CL085 survey, next step 4: "Resolve Guillon's width convention against the column-pair counts: do
they grow like 2^n or faster?"). Local's run (chat L427).

RUN-ON:     cpu (Python 3, numpy); about two minutes
COMMAND:    python3 tests/probes/lexicon/rule30_trace_widths.py [NMAX=14]

A width-w trace word of length n is the n x w block of columns 0 .. w - 1 over times 0 .. n - 1. Every one is read off
the light cone that determines it, and the cone's cells are enumerated exhaustively, so the counts are exact.
  F, the physical frame: x'(i) = x(i - 1) xor (x(i) or x(i + 1)); cone cells -(n - 1) .. (w - 1) + (n - 1).
  G, the frame moving right at light speed: y'(i) = y(i) xor (y(i + 1) or y(i + 2)), so G = shift o F and a G column
     is an F light-speed diagonal; cone cells 0 .. (w - 1) + 2(n - 1).
Why both frames: topological entropy is not invariant under composing with a shift, so a theorem relating entropy to
a trace's entropy (Guillon 2008, Proposition 4.8.5) names a frame as well as a width. Guillon's thesis could not be read
here (HAL's bot protection refused the fetch, 2026-10-09, and was not bypassed), so the convention itself is open.

PREDICTION (Cloud's, CL085's report table, pushed before this run): "Expect growth faster than 2^n, which would make the
convention r = 2 and refute the naive reading of Remark 4.6.9" (for the column-pair counts). The width-2 counts in the
physical frame were first computed to n = 12 in an exploratory look minutes before this probe was written; n = 13, 14
and the G frame came after.
OUTCOME, 2026-10-09 15:52 BST (M5; exact, every cone enumerated):
  F width 1: exactly 2^n (the centre column is a full shift, as left permutivity says).
  F width 2: 4, 12, 32, 80, 200, 496, 1208, 2916, 6964, 16476, 38616, 89844, 207544, 476596 (n = 1 .. 14); successive
    ratios 3.000, 2.667, 2.500, 2.500, 2.480, 2.435, 2.414, 2.388, 2.366, 2.344, 2.327, 2.310, 2.296, falling by about
    0.015 a step; N/2^n rises from 2 to 29.1.
  G width 1 (L426's language): 2, 4, 8, 16, 30, 54, 96, 170, 302, 536, 924, 1576, 2670 (n = 1 .. 13); ratios about
    1.78 falling to 1.69.
  G width 2: 4, 10, 22, 50, 104, 208, 406, 774, 1466, 2728, 4994, 9038, 16174 (n = 1 .. 13); ratios falling to 1.79.
  Reading: Cloud's prediction HELD as a statement about counts (the physical width-2 language exceeds 2^n at every n
  and is not determined by width 1). As a statement about entropy it is NOT decided: the ratio is still falling at
  n = 14, and these n do not tell a limit above 2 from one equal to 2. Submultiplicativity gives only upper bounds
  (h <= log2(N(n)) / n, e.g. 1.347 bits at n = 14 for F width 2). The G-frame traces grow more slowly than 2^n, so
  which frame and width Guillon's Remark 4.6.9 and Proposition 4.8.5 mean changes the answer.
"""
import sys
import numpy as np


def count(n, frame, width):
    if frame == 'F':
        lo, hi = -(n - 1), (width - 1) + (n - 1)
    else:
        lo, hi = 0, (width - 1) + 2 * (n - 1)
    m = hi - lo + 1
    seen = set()
    chunk = 1 << min(m, 22)
    for base in range(0, 1 << m, chunk):
        w = np.arange(base, base + chunk, dtype=np.int64)
        y = [((w >> i) & 1).astype(np.uint8) for i in range(m)]
        off = -lo
        code = np.zeros(chunk, dtype=np.int64)
        for t in range(n):
            for c in range(width):
                code = (code << 1) | y[off + c]
            if t < n - 1:
                if frame == 'F':
                    y = [y[i - 1] ^ (y[i] | y[i + 1]) for i in range(1, len(y) - 1)]
                    off -= 1
                else:
                    y = [y[i] ^ (y[i + 1] | y[i + 2]) for i in range(len(y) - 2)]
        seen.update(np.unique(code).tolist())
    return len(seen)


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    for frame, width in (('F', 1), ('F', 2), ('G', 1), ('G', 2)):
        top = min(nmax, 12 if width == 1 and frame == 'F' else 13 if frame == 'G' else nmax)
        cs = [count(n, frame, width) for n in range(1, top + 1)]
        print('%s width %d: %s' % (frame, width, ' '.join(map(str, cs))))
        print('   ratios: %s' % ' '.join('%.3f' % (b / a) for a, b in zip(cs, cs[1:])), flush=True)
    print('COMPLETE')


if __name__ == '__main__':
    main()
