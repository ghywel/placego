#!/usr/bin/env python3
"""rule30_local_ring_gaps.py: Local's second check of the ring premises of GC1148 (S, GC686's 84-ring) and GC1151 (L,
the 155-ring of rule30_all_l_slab.py), after CL350 could not reproduce the L ring and GPT's receipt under GC1153 named
the circumference 155 (the integer's bit length is 154; the leading cell is white). L642.

RUN-ON:     cpu (Python 3 standard library; under a second)
COMMAND:    python3 tests/probes/lexicon/rule30_local_ring_gaps.py

For each ring (cyclic row of N cells, Rule 30 on the circle): how it travels (the least tick count with the row back at
some cyclic shift, and the shift), its period at fixed sites (the least with shift 0), columns 0 and 1 over two
periods, and the maximal cyclic white run at every tick of the period with the wall's colour. The L ring at N = its
bit length is run too, as the negative control.

RESULT (2026-10-11 15:57 BST, M5; PASS):
  S ring, N = 84: a travelling wave, 14 sites a tick, period 6 at fixed sites; column 0 = 0101.. (white wall at even
    ticks), column 1 = 110100 (the S trace); maximal white run 5 at every tick (CL348's "shift 14" and "gap 5").
  L ring, N = 155: a travelling wave, 31 sites every two ticks, period 10 at fixed sites; column 0 = 0101.. (white
    wall at even ticks), column 1 = 1101000100 (the L trace; visible word LL); maximal white run 6 at the five
    white-wall ticks and 7 at the five black-wall ticks. GC1151's "spatial white gap 6" holds at every white-wall
    tick, and its anchor is one (a = p + 2s): the white triangle carries a record run of L at time 0 to a run of at
    least L - 2a at the anchor, which must fit in the 6. The 7s sit at black-wall rows, which the bound never uses.
  L ring, N = 154 (the bit length; control): no closure at any shift within 40 ticks, and column 0 is not the wall,
    as CL350 found.
"""


def ring(value, n, ticks):
    row = [(value >> i) & 1 for i in range(n)]
    hist = [row]
    for _ in range(ticks):
        r = hist[-1]
        hist.append([r[(i - 1) % n] ^ (r[i] | r[(i + 1) % n]) for i in range(n)])
    return hist


def closure(hist, n, shifts=None):
    """The least tick count p > 0 with the row back at a cyclic shift (any shift, or one of `shifts`), and the shift."""
    for p in range(1, len(hist)):
        for s in (range(n) if shifts is None else shifts):
            if all(hist[p][i] == hist[0][(i - s) % n] for i in range(n)):
                return p, s
    return None


def max_white(r):
    n, best = len(r), 0
    if not any(r):
        return n
    for s in range(n):
        if r[s] == 0 and r[(s - 1) % n] == 1:
            k = 0
            while r[(s + k) % n] == 0:
                k += 1
            best = max(best, k)
    return best


def report(name, value, n, ticks=40):
    hist = ring(value, n, ticks)
    w, c = closure(hist, n), closure(hist, n, (0,))
    print('%s, N = %d (bit length %d): travels %s; period at fixed sites %s' % (
        name, n, value.bit_length(), w and '%d site(s) in %d tick(s)' % (w[1], w[0]), c and c[0]))
    p = c[0] if c else 10
    print('  column 0 %s  column 1 %s' % (''.join(str(hist[t][0]) for t in range(2 * p)),
                                          ''.join(str(hist[t][1]) for t in range(2 * p))))
    print('  max white run by tick (wall colour): %s' % ' '.join('%d(%s)' % (max_white(hist[t]), 'wb'[hist[t][0]])
                                                              for t in range(p)))
    return c, hist


def main():
    S = 0x688eb74a45efb082671ee
    L = 0x35409b1caa645d715104db5291a2fe8415260ce
    cs, hs = report('S ring', S, 84)
    cl, hl = report('L ring', L, 155)
    c0, h0 = report('L ring control', L, 154)
    assert closure(hs, 84) == (1, 14) and closure(hl, 155) == (2, 31)
    assert cs == (6, 0) and [hs[t][1] for t in range(6)] == [1, 1, 0, 1, 0, 0]
    assert all(max_white(hs[t]) == 5 for t in range(6))
    assert cl == (10, 0) and [hl[t][1] for t in range(10)] == [1, 1, 0, 1, 0, 0, 0, 1, 0, 0]
    assert all(hl[t][0] == t % 2 for t in range(20))
    assert all(max_white(hl[t]) == (6 if t % 2 == 0 else 7) for t in range(10))
    assert c0 is None and any(h0[t][0] != t % 2 for t in range(20))
    print('RING-GAPS PASS')


if __name__ == '__main__':
    main()
