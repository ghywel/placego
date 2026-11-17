#!/usr/bin/env python3
"""SW-02 reference library (Local, 5 November 2026). One copy of the conventions, so that no agent re-derives them.

Run `python3 ref.py` for the self-test, which prints the smallest cases (guards G1, G11). Import it with
`sys.path.insert(0, DIR); import ref`. Standard library only; numpy is used by S_table when available.

Conventions, as in the kit (`Rule30ZeroBoundary`, `Rule30Ether`, `Rule30PeriodTwoSideways`, `Rule30FrozenRuler`):
  rule(a, b, c) = a xor (b or c), with a the LEFT neighbour.
  ZERO-BOUNDARY HALF-ROW. A natural Y is a row: bit i is the cell at depth i + 1, depth k is position -k, depth 0 is a white
  wall for ever. F(Y) = (Y >> 1) xor (Y or (Y << 1)) is one physical tick, G = F o F. Time t is the physical tick.
  WHOLE LINE. `line_rows` keeps the row as an int whose bit t is position 0 at tick t, and steps with fw.
  EDGE CODE. Bit k = cell k behind the rightmost black cell; one tick is T = fw (Rule30FrozenRuler.T).
  DRIVEN RIGHT HALF. drv(col, R, t) gives columns p >= 1 with column 0 prescribed by col; bit p - 1 of the int is column p.
"""
import random, sys


def rule(a, b, c):
    return a ^ (b | c)


def F(y):
    return (y >> 1) ^ (y | (y << 1))


def G(y):
    return F(F(y))


def Fpow(y, t):
    for _ in range(t):
        y = F(y)
    return y


def width(y):
    return y.bit_length()


def col1(y, n):
    """bit0 of F^t(y) for t < n: the column at depth 1."""
    out = []
    for _ in range(n):
        out.append(y & 1)
        y = F(y)
    return out


def first_even_white(y, cap=None):
    """Least even tick t with bit0(F^t(y)) = 0; None if none is met up to cap (a None is not immortality)."""
    t = 0
    cap = cap if cap is not None else 4 * width(y) + 64
    while t <= cap:
        if y & 1 == 0:
            return t
        y = G(y)
        t += 2
    return None


def survives_through(y, t):
    """bit0(F^(2s)(y)) = 1 for every even 2s <= t (t a physical tick, inclusive)."""
    s = 0
    while s <= t:
        if y & 1 == 0:
            return False
        y = G(y)
        s += 2
    return True


def S(W, t):
    """S_W(t) = #{0 <= Y < 2^W : bit0(F^(2s)(Y)) = 1 for every 2s <= t}. Exhaustive; for small W."""
    return sum(1 for y in range(1 << W) if survives_through(y, t))


def S_table(W, T):
    """[S_W(t) for even t = 0, 2, ..., T], one pass; numpy if present (W <= 28 or so)."""
    try:
        import numpy as np
    except ImportError:
        return [S(W, t) for t in range(0, T + 1, 2)]
    if W + T // 1 > 62:
        return [S(W, t) for t in range(0, T + 1, 2)]
    ys = np.arange(1 << W, dtype=np.uint64)
    alive = np.ones(1 << W, dtype=bool)
    out = []
    one = np.uint64(1)
    for t in range(T + 1):
        if t % 2 == 0:
            alive &= (ys & one).astype(bool)
            out.append(int(alive.sum()))
        ys = (ys >> one) ^ (ys | (ys << one))
    return out


def D(W, cap=None):
    """D(W): maximum over 0 <= Y < 2^W of the first even white tick. Exhaustive; small W only."""
    cap = cap if cap is not None else 4 * W + 64
    best = 0
    for y in range(1 << W):
        d = first_even_white(y, cap)
        if d is None:
            raise RuntimeError(f"no death by tick {cap} at Y={y}")
        best = max(best, d)
    return best


def alt(f, t):
    """kit `alt`: black at even t, free bit f(t // 2) at odd t."""
    return 1 if t % 2 == 0 else f(t // 2)


def theta(f, n):
    """First n depths of kit `Theta f`, as a natural Y: bit k - 1 is depth k, read from the sideways recursion
    C_(k+1)(t) = C_k(t + 1) xor (C_k(t) or C_(k-1)(t)), C_0 = 0, C_1 = alt f. Bit t of an int is tick t."""
    c_prev, c = 0, 0
    for t in range(n):
        c |= alt(f, t) << t
    y = 0
    for k in range(1, n + 1):
        y |= (c & 1) << (k - 1)
        c, c_prev = (c >> 1) ^ (c | c_prev), c
        c &= (1 << (n - k)) - 1 if n - k > 0 else 0
        c_prev &= (1 << (n - k + 1)) - 1
    return y


def alt_col(t):
    """kit `altCol`: black at the even steps."""
    return 1 if t % 2 == 0 else 0


def drv(col, R, T):
    """Rows of the driven right half, ticks 0..T: list of ints, bit p - 1 is column p. R is the initial right half."""
    rows = [R]
    x = R
    for t in range(T):
        x = ((x << 1) | col(t)) ^ (x | (x >> 1))
        rows.append(x)
    return rows


def u(R, n):
    """kit `u R s` for s < n: column 1 of the driven right half at the odd tick 2s + 1, under the alternating column."""
    rows = drv(alt_col, R, 2 * n + 1)
    return [rows[2 * s + 1] & 1 for s in range(n)]


def psi(R, n):
    """First n depths of kit `Psi R` = Theta (not u R), as a natural: bit k - 1 is depth k."""
    us = u(R, n // 2 + 2)
    return theta(lambda s: 1 - us[s], n)


def fw(y):
    """One tick of the whole line in the frame that moves one cell a tick; also the edge map T (Rule30FrozenRuler.T)."""
    return y ^ ((y << 1) | (y << 2))


T_edge = fw


def center(n):
    """The first n cells of the prize's centre column from the single black cell."""
    x, out = 1, []
    for t in range(n):
        out.append((x >> t) & 1)
        x = fw(x)
    return out


def row_bit_tables(m):
    """Exact truth tables over the m free bits f_0..f_(m-1), as big ints: depth -> table (bit a is the value on assignment a).
    Depth d <= 2m + 1. Depth 2n + 1 depends only on f_0..f_(n-1): that is the check. (tests/probes/stepback/checks.py.)"""
    N = 1 << m
    ones = (1 << N) - 1

    def var(i):
        blk = 1 << i
        v, w = ((1 << blk) - 1) << blk, 2 * blk
        while w < N:
            v |= v << w
            w *= 2
        return v & ones

    T = 2 * m + 1
    a = [ones if s % 2 == 0 else var((s - 1) // 2) for s in range(T)]
    prev, cur = [0] * (T + 1), a + [None]
    bits = {1: cur[0]}
    for k in range(1, T):
        nxt = [None] * (T + 1)
        for t in range(T - k):
            nxt[t] = cur[t + 1] ^ (cur[t] | prev[t])
        prev, cur = cur, nxt
        bits[k + 1] = cur[0]
    return bits


def check_sum(n, m=None):
    """Sum over f_0..f_(n-1) of (-1)^(row bit at depth 2n + 1), exact."""
    m = n if m is None else m
    tb = row_bit_tables(max(m, n))[2 * n + 1]
    total_vars = max(m, n)
    ones = bin(tb).count("1") >> (total_vars - n)
    return (1 << n) - 2 * ones


def selftest():
    # width law
    assert all(width(F(y)) == width(y) + 1 for y in range(1, 1 << 12))
    print("F adds one to width: ok for 0 < Y < 2^12")
    # smallest cases of F
    print("F(1), F(2), F(3), F(5) =", F(1), F(2), F(3), F(5))
    # exact range, inclusive physical ticks, W >= 1, 0 <= t < W
    for W in range(1, 11):
        for t in range(W):
            assert S(W, t) == 2 ** (W - t // 2 - 1), (W, t)
    assert S(10, 9) == 2 ** 5
    print("S_W(t) = 2^(W - floor(t/2) - 1) for 1 <= W <= 10, 0 <= t < W: ok; S_0(0) =", S(0, 0))
    # the table in the design
    tab = {12: (64, 38, 9, 3, 2, 2, 2), 14: (128, 57, 26, 15, 14, 7, 7), 16: (256, 112, 63, 34, 19, 16, 13), 18: (512, 251, 147, 72, 43, 33, 22)}
    for W, row in tab.items():
        got = S_table(W, W + 10)
        assert tuple(got[(W - 2) // 2:]) == row, (W, got)
    print("design table rows W = 12..18: ok")
    print("D(W), W = 1..14:", [D(W) for W in range(1, 15)])
    # Theta: the constrained start keeps column -1 at alt f
    rnd = random.Random(30)
    for _ in range(50):
        fb = [rnd.getrandbits(1) for _ in range(40)]
        y = theta(lambda s: fb[s], 70)
        c = col1(y, 60)
        assert all(c[t] == alt(lambda s: fb[s], t) for t in range(60)), fb
    print("theta: column at depth 1 reproduces alt f for 60 ticks on 50 random words of 70 depths: ok")
    # the trunc stripe: the all-ones free word? kit trunc_survives: depth 1 black for t <= n, white at n + 1
    # centre column
    want = "1101110011000101100100111010111001110101"
    assert "".join(map(str, center(40))) == want
    print("centre column, first 40 cells: ok")
    # u and Psi of the empty right half
    us = u(0, 400)
    blacks = [s for s in range(146, 400) if us[s]]
    gaps = sorted(set(b - a for a, b in zip(blacks, blacks[1:])))
    print("u(empty): black gaps from s = 146 to 399:", gaps)
    assert set(gaps) <= {3, 5}
    p = psi(0, 401)
    dens = bin(p).count("1")
    print("Psi(empty), depths 1..401: black count", dens, "share", round(dens / 401, 4))
    # right-edge map
    assert T_edge(1) == 7 and T_edge(0b101) == 0b101 ^ ((0b1010) | (0b10100))
    print("T(1) =", T_edge(1))
    print("check sums n = 1..14:", [check_sum(n) for n in range(1, 15)])
    print("SELFTEST PASS")


if __name__ == "__main__":
    selftest()
