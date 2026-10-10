#!/usr/bin/env python3
"""rule30_cloud_junctions.py: JN, where do white runs come from? The forced left half of piecewise-periodic visible
words (free model: the inverse recurrence from the clock and a visible word, no realizability), measuring the longest
white run in the time-0 row as the periodic pieces grow. (row Q6; CL200's anatomy question.)

RUN-ON:     cpu (Python 3, seconds)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_junctions.py pure | one | two | all

Why. Every record witness seen today is piecewise periodic in its visible code: the d = 152 witness (L596) is a 2-gap
train of 11 cars, the exit 4, 5, a train of 5, the exit 4, 5, then 3, 3, 3, 5, 5, 5, 5, 2; the d = 107 relaxed code
(L584) is a 4-gap train then an S/L mix. A pure periodic visible word has a forced left half that is spatially periodic
when a ring realizes it (S: 84 cells, L: 155, the 2-gap train: GC1013's seven-ring), so its white runs are bounded. If
white runs are created only at the junctions between periodic pieces, each adding a bounded amount, then
R_real(d) <= c * (junctions in the cone) <= c' * d, a linear bound, which is finiteness at every depth and period 2.
This probe tests the first half of that sentence in the free model, where it must hold for any such argument to start.

Record searched: `record_find.py template|templates` -> the free-record templates (§8.38 lineage); `junction|piecewise`
-> no hit; the forced-walk description (§8.37). The forced left half here reproduces L596's band (18 white cells at
depths 152 .. 169 from its 85-symbol code), checked before registration.

PREDICTIONS (2026-10-10 16:15 BST, written before any run):
  JN-P1 (0.7): for each pure word w in {10, 1000, 001, 00001}, the longest white run beyond depth 10 in the forced row
    of w^n is bounded as n grows to 120 (it stops changing by n = 60).
  JN-P2 (0.6): one junction, (10)^n then 0001 00001 then (001)^m: the longest white run is bounded in n and m (n, m up
    to 80), i.e. the junction's contribution saturates. Counterfactual: it grows with n or m, and junction counting fails.
  JN-P3 (0.5): two junctions, the L596 shape (10)^n 4,5 (10)^m 4,5 3,3,3,5,5,5,5,2: the longest white run stays <= 20
    for all n, m <= 40 while its depth moves with n + m. Counterfactual: a longer run appears for some n, m.
  These are free-model facts; realizability of the varied words is not claimed ((1000)^n is not actual for large n,
  L563/GC987).
"""
import sys


def left_row(vis):
    """Time-0 cells x_0(-1), x_0(-2), .. of the forced left half, as far as the visible word determines them. Column 0
    is the clock t mod 2; column -1 is 1 at odd t and NOT v at even t; x_t(k-1) = x_{t+1}(k) XOR (x_t(k) OR x_t(k+1))."""
    T = 2 * len(vis) - 1
    cols = {0: [t % 2 for t in range(T + 1)], -1: [1 if t % 2 else 1 - int(vis[t // 2]) for t in range(T + 1)]}
    k = -1
    while len(cols[k]) > 1:
        c, r = cols[k], cols[k + 1]
        cols[k - 1] = [c[t + 1] ^ (c[t] | r[t]) for t in range(len(c) - 1)]
        k -= 1
    return ''.join(str(cols[j][0]) for j in range(-1, k, -1))


def longest_white(row, dmin=10):
    """(length, start depth) of the longest white run starting at depth >= dmin (depth 1 is cell -1)."""
    best = (0, 0)
    d = 1
    for run in row.split('1'):
        if d >= dmin and len(run) > best[0]:
            best = (len(run), d)
        d += len(run) + 1
    return best


def word(gaps, lead='0'):
    return lead + '1' + ''.join('0' * (g - 1) + '1' for g in gaps)


def pure():
    for w in ('10', '1000', '001', '00001'):
        print('pure %-6s longest white run beyond depth 10, by n:' % w,
              ' '.join('%d:%s' % (n, longest_white(left_row(w * n))) for n in (15, 30, 60, 90, 120)))


def one():
    print('one junction, (10)^n then 4, 5 then (001)^m: longest white run (length, depth):')
    for n in (10, 20, 40, 80):
        runs = ['m=%2d:%s' % (m, longest_white(left_row(word([2] * (n - 1) + [4, 5] + [3] * m)))) for m in (10, 20, 40, 80)]
        print('  n = %2d:' % n, ' '.join(runs))


def two():
    tail = [4, 5, 3, 3, 3, 5, 5, 5, 5, 2]
    print('two junctions, (10)^n 4,5 (10)^m 4,5 3,3,3,5,5,5,5,2: longest white run (length, depth):')
    for n in (5, 11, 20, 40):
        runs = ['m=%2d:%s' % (m, longest_white(left_row(word([4] + [2] * (n - 1) + [4, 5] + [2] * (m - 1) + tail))))
                for m in (5, 11, 20, 40)]
        print('  n = %2d:' % n, ' '.join(runs))
    l596 = word([4] + [2] * 10 + [4, 5] + [2] * 4 + tail)
    print('  check, the L596 code itself (n = 11, m = 5):', longest_white(left_row(l596)))


if __name__ == '__main__':
    cmd = sys.argv[1]
    for name, fn in (('pure', pure), ('one', one), ('two', two)):
        if cmd in (name, 'all'):
            fn()
