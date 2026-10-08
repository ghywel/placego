#!/usr/bin/env python3
"""rule30_cloud_slant_flips.py: RS, bit flips in windows that descend the single-cell pyramid at an angle

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_slant_flips.py [T=8192]
COST:       seconds.

The owner's follow-up to RW (2026-10-08): the light cone is off centre, so there is no reason to descend vertically.
Descend at an angle instead. For example, take pixels 1, 2, 3 of the 3-wide row, then pixels 1, 2, 3 of the 5-wide
row, of the 7-wide row, and so on: a window that slides one column left per row, along the left edge.

What the record already says (sections 8.27, 8.30). The pyramid has three regions:
- on the left, a band of universal stripes filling the left 38% of each row, with eventually periodic left
  diagonals of tiny period;
- the chaotic core, whose left edge moves left at about 0.25 cells per step, the leftward speed of information;
- on the right, a thin strip of nested period-doubling diagonals (Rowland; RW).
The owner's example runs down the left band.

What a flip means depends on the angle (G97's moving-frame identities, in the Gray split of CL046). Compare cell j of
the window at row s with cell j at row s + 1, where the window has moved by -1, 0 or +1:
    left step:  x(i-2) XOR (x(i-1) AND NOT x(i))   (a Gray step two cells over, plus an edge event)
    stay:       x(i-1) XOR (x(i+1) AND NOT x(i))   (RW's case)
    right step: x(i+1) OR x(i+2)                   (pure OR: the Gray part vanishes)
Under the fair spatial law the first two give uniform flip words (four preimages each), and the third gives the OR
law, with mean 3/4 per cell. So each window is compared with the exact null for its own mix of steps. A window on a
ray of slope v has left end floor(v s) - floor(w / 2) at row s; v = -1 and v = 1 are the edges themselves, so
those windows sit just inside them. Windows on the left edge have left end -s + p.
Controls (should PASS):
  RS-C1: the three flip identities hold exactly at every step of every window.
  RS-C2: left and stay flip words are uniform; the right-step null is the enumerated OR law.
PREDICTIONS (Cloud's, pushed before the first run; T = 8192, widths 3 .. 6):
  RS-P1 (the core): rays of slope v = -1/8, 0, 1/4, 1/2 and 3/4 match their frame's null, with total variation
         below 0.03 at every width. Confidence 0.7.
  RS-P2 (the left band): rays of slope v = -1, -3/4 and -1/2 (through the apex, inside the band) are far from their
         null, with total variation above 0.2 at every width. Confidence 0.75.
  RS-P3 (the band's edge): over the slope scan v = -1, -7/8, .., 3/4 (the right strip at v >= 7/8 is set aside),
         the slopes with total variation above 0.1 at width 4 are exactly those from -1 up to a last one at -1/2,
         -3/8 or -1/4, that is, below the core's edge at -1/4 give or take one step. Confidence 0.5.
UNEXPECTED CHECK (the owner's left-edge windows, positions p .. p + w - 1 of each row, p = 0 .. 20): the ordered
  band is more Gray-like than a coin. At width 4, single-flip steps exceed the null rate (1/4) by a factor of at
  least 2 at most offsets p. Confidence 0.4.
Counterfactual: if the left band's windows match the coin null, its stripes are invisible to flip counts, and the
  flip view adds nothing to the record's diagonal periods there.
"""
import sys
from math import comb
from fractions import Fraction
from itertools import product

T = int(sys.argv[1]) if len(sys.argv) > 1 else 8192
OFF = T + 4
WIDTHS = (3, 4, 5, 6)


def rows():
    row = 1 << OFF
    for _ in range(T + 1):
        yield row
        row = (row << 1) ^ (row | (row >> 1))


def bit(row, i):
    return (row >> (OFF + i)) & 1


def or_null(w):
    h = [0] * (w + 1)
    for y in product((0, 1), repeat=w + 1):
        h[sum(y[j] | y[j + 1] for j in range(w))] += 1
    return [x / 2 ** (w + 1) for x in h]


def uniform_ok(w, step):
    count = {}
    for x in product((0, 1), repeat=w + 2):           # cells a-2 .. a+w-1 (left) or a-1 .. a+w (stay)
        if step == -1:
            f = tuple(x[j] ^ (x[j + 1] & (1 - x[j + 2])) for j in range(w))
        else:
            f = tuple(x[j] ^ (x[j + 2] & (1 - x[j + 1])) for j in range(w))
        count[f] = count.get(f, 0) + 1
    return len(count) == 2 ** w and set(count.values()) == {4}


class Window:
    def __init__(self, w, left_end):
        self.w, self.left_end = w, left_end            # left_end(s) -> column of the window's first cell
        self.hist = [0] * (w + 1)
        self.steps = {-1: 0, 0: 0, 1: 0}
        self.ok = True

    def feed(self, s, prev, row):
        a, b = self.left_end(s), self.left_end(s + 1)
        if a < -s or a + self.w - 1 > s or b < -s - 1 or b + self.w - 1 > s + 1:
            return
        step = b - a
        k = 0
        for j in range(self.w):
            i = a + j
            f = bit(row, b + j) ^ bit(prev, i)
            if step == -1:
                want = bit(prev, i - 2) ^ (bit(prev, i - 1) & (1 - bit(prev, i)))
            elif step == 0:
                want = bit(prev, i - 1) ^ (bit(prev, i + 1) & (1 - bit(prev, i)))
            else:
                want = bit(prev, i + 1) | bit(prev, i + 2)
            self.ok &= f == want
            k += f
        self.hist[k] += 1
        self.steps[step] += 1

    def null(self):
        n = sum(self.steps.values())
        u = [comb(self.w, k) / 2 ** self.w for k in range(self.w + 1)]
        o = or_null(self.w)
        r = self.steps[1] / n
        return [(1 - r) * u[k] + r * o[k] for k in range(self.w + 1)]

    def tv(self):
        n = sum(self.hist)
        if not n:
            return float("nan")
        return 0.5 * sum(abs(h / n - p) for h, p in zip(self.hist, self.null()))

    def gray(self):
        n = sum(self.hist)
        return self.hist[1] / n, self.null()[1]


def ray(v, w):
    return Window(w, lambda s, v=v, w=w: (v * s).__floor__() - w // 2)


def main():
    print("RS-C2", "PASS" if all(uniform_ok(w, st) for w in WIDTHS for st in (-1, 0)) else "FAIL")
    slopes = [Fraction(n, 8) for n in range(-8, 9)]
    rays = {(v, w): ray(v, w) for v in slopes for w in WIDTHS}
    for w in WIDTHS:                                    # v = -1 and v = 1 are the edges: keep the window inside
        rays[(Fraction(-1), w)] = Window(w, lambda s: -s + 1)
        rays[(Fraction(1), w)] = Window(w, lambda s, w=w: s - w + 1)
    edge = {(p, w): Window(w, lambda s, p=p: -s + p) for p in range(21) for w in WIDTHS}
    allw = list(rays.values()) + list(edge.values())
    prev = None
    for s, row in enumerate(rows()):
        if prev is not None:
            for win in allw:
                win.feed(s - 1, prev, row)
        prev = row
    print("RS-C1", "PASS" if all(win.ok for win in allw) else "FAIL")
    print("slope scan: total variation from each frame's null, widths 3 4 5 6")
    tv4 = {}
    for v in slopes:
        tvs = [rays[(v, w)].tv() for w in WIDTHS]
        tv4[v] = tvs[1]
        print(f"  v = {str(v):>5}: {' '.join(f'{x:.3f}' for x in tvs)}")
    p1 = all(rays[(v, w)].tv() < 0.03 for v in (Fraction(-1, 8), 0, Fraction(1, 4), Fraction(1, 2),
                                                 Fraction(3, 4)) for w in WIDTHS)
    p2 = all(rays[(v, w)].tv() > 0.2 for v in (Fraction(-1), Fraction(-3, 4), Fraction(-1, 2)) for w in WIDTHS)
    big = [v for v in slopes if v < Fraction(7, 8) and tv4[v] > 0.1]     # the right strip is set aside
    p3 = bool(big) and big[0] == -1 and big == [v for v in slopes if v <= big[-1]] and \
        big[-1] in (Fraction(-1, 2), Fraction(-3, 8), Fraction(-1, 4))
    print("RS-P1", "HELD" if p1 else "REFUTED")
    print("RS-P2", "HELD" if p2 else "REFUTED")
    print("RS-P3", "HELD" if p3 else "REFUTED", f"(slopes with tv > 0.1 at width 4: {[str(v) for v in big]})")
    print("the owner's left-edge windows (positions p .. p + w - 1 of each row):")
    excess = 0
    for p in range(21):
        tvs = [edge[(p, w)].tv() for w in WIDTHS]
        g, g0 = edge[(p, 4)].gray()
        excess += g >= 2 * g0
        print(f"  p = {p:2d}: tv {' '.join(f'{x:.3f}' for x in tvs)}; width-4 single-flip steps {g:.3f} "
              f"(null {g0:.3f})")
    print("unexpected check", "HELD" if excess >= 11 else "REFUTED", f"({excess} of 21 offsets)")


if __name__ == "__main__":
    main()
