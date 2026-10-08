#!/usr/bin/env python3
"""rule30_cloud_review_gc483.py: Cloud's independent replay of the finite claims in GPT's GC483 to GC496 (CL034).

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_review_gc483.py
COST:       a few seconds.

The hand arguments of GC483 to GC496 were read line by line in CL034. This script checks only their finite claims,
in Cloud's own coding (a row is a set of black sites, or a Python integer), sharing no code with GPT's probes.
Each check is GPT's stated value, so each line is a control: it should PASS.
  R483: the seven-cell ring cycle 1, 67, 100, 63 (G4), its centre bits 1, 1, 0, 1, and the truncated full-line seeds
        on [-T, T] reproducing spin sums -T/2 for T = 4, 8, 16, 32 (GC483).
  R484: the singleton's rows 0 .. 4 are {0}, {-1,0,1}, {-2,-1,2}, {-3,-2,0,1,2,3}, {-4,-3,0,4}; rows 0 and 4 agree
        on [-2, 2]; rewards g_0 = -1, g_2 = 0 (GC484).
  R485: on the singleton orbit, row 192 on [-5, 5] reads 01010101000, the radius 3 windows at 192, 193, 194 read
        0101010, 0101011, 0101010, and the centre is black at all three (GC485).
  R486: the two-step centre polynomial a+d+e+bd+cd+be+ce+de+bde+cde; ANF degrees 2, 3, 7 and term counts 4, 10, 122
        at times 1, 2, 4; the dilation F(a, c, e) differs on 16 of 32 inputs (GC486).
  R487: the 31 decimations a(2^d n + r), d <= 4, are pairwise distinct on n = 1 .. 32, every pair differing at some
        n <= 9; Thue-Morse gives 2 signatures (GC487).
  R491: the velocity v = u XOR F(u) equals Rule 210 of u, and GPT's coupled law for v_next holds on all 32 inputs
        (u_c, u_r, v_l, v_c, v_r) that occur, checked against real consecutive rows (GC491).
  R492: on every finite row u of width up to 12, GPT's three-state machine accepts G(u); on every velocity word of
        length up to 12, it accepts exactly the words with a finite preimage (by brute force over rows) (GC492).
Unexpected check (Cloud's, predicted before the run, confidence 0.9): by GC491's injectivity, and because a finite
  row whose black cells run from L to R has velocity running exactly from L - 1 to R + 1, the machine accepts
  exactly 2^(n-4) velocity words of length n with both ends black for n >= 4, one at n = 3 and none below. So among
  words with black ends only a quarter are admissible, at every length from 4 on.
"""
from itertools import product


def step(black):
    """One Rule 30 update of a finite set of black sites."""
    lo, hi = min(black, default=0) - 1, max(black, default=0) + 1
    return {i for i in range(lo, hi + 1) if ((i - 1) in black) ^ ((i in black) or ((i + 1) in black))}


def orbit(seed, n):
    rows, row = [], set(seed)
    for _ in range(n):
        rows.append(row)
        row = step(row)
    return rows


def report(name, ok, detail=""):
    print(name, "PASS" if ok else "FAIL", detail)


def r483():
    def ring(row, n=7):                                  # site s is bit s mod 7; the left neighbour of bit i is i - 1
        bits = [(row >> i) & 1 for i in range(n)]
        new = [bits[(i - 1) % n] ^ (bits[i] | bits[(i + 1) % n]) for i in range(n)]
        return sum(b << i for i, b in enumerate(new))
    seen, row = [], 1
    for _ in range(5):
        seen.append(row)
        row = ring(row)
    centre = [r & 1 for r in seen[:4]]
    sums = []
    for T in (4, 8, 16, 32):                             # ring row 1 repeated on the line: black at multiples of 7
        rows = orbit({x for x in range(-T, T + 1) if x % 7 == 0}, T)
        sums.append(sum(1 - 2 * (0 in r) for r in rows))
    report("R483", seen == [1, 67, 100, 63, 1] and centre == [1, 1, 0, 1] and sums == [-2, -4, -8, -16],
           f"cycle {seen}, centre {centre}, spin sums {sums}")


def r484():
    rows = orbit({0}, 6)
    want = [{0}, {-1, 0, 1}, {-2, -1, 2}, {-3, -2, 0, 1, 2, 3}, {-4, -3, 0, 4}]
    same = all((i in rows[0]) == (i in rows[4]) for i in range(-2, 3))
    c = [int(0 in r) for r in rows]
    g = [(1 - 2 * c[t]) * (c[t] == c[t + 1]) for t in (0, 2)]
    report("R484", rows[:5] == want and same and g == [-1, 0], f"rewards {g}")


def r485():
    rows = orbit({0}, 196)
    w = lambda t, r: "".join(str(int(i in rows[t])) for i in range(-r, r + 1))
    ok = w(192, 5) == "01010101000" and [w(t, 3) for t in (192, 193, 194)] == ["0101010", "0101011", "0101010"]
    report("R485", ok and all(0 in rows[t] for t in (192, 193, 194)), w(192, 5))


def anf(f, n):
    """Algebraic normal form (Moebius transform) of a Boolean function given as a truth table list."""
    a = list(f)
    for i in range(n):
        for m in range(1 << n):
            if m >> i & 1:
                a[m] ^= a[m ^ (1 << i)]
    return [m for m in range(1 << n) if a[m]]


def r486():
    F = lambda l, c, r: l ^ (c | r)
    two = [F(F(a, b, c), F(b, c, d), F(c, d, e)) for a, b, c, d, e in
           ((m >> 4 & 1, m >> 3 & 1, m >> 2 & 1, m >> 1 & 1, m & 1) for m in range(32))]
    poly = lambda a, b, c, d, e: (a + d + e + b*d + c*d + b*e + c*e + d*e + b*d*e + c*d*e) % 2
    ok_poly = all(two[m] == poly(m >> 4 & 1, m >> 3 & 1, m >> 2 & 1, m >> 1 & 1, m & 1) for m in range(32))
    dil = sum(two[m] != F(m >> 4 & 1, m >> 2 & 1, m & 1) for m in range(32))
    profile = []
    for t in (1, 2, 4):
        n = 2 * t + 1
        table = []
        for m in range(1 << n):
            row = {i - t for i in range(n) if m >> (n - 1 - i) & 1}
            table.append(int(0 in orbit(row, t + 1)[t]))
        terms = anf(table, n)
        profile.append((max(bin(x).count("1") for x in terms), len(terms)))
    report("R486", ok_poly and dil == 16 and profile == [(2, 4), (3, 10), (7, 122)], f"profile {profile}, "
           f"dilation mismatches {dil}")


def r487():
    rows = orbit({0}, 530)
    a = [int(0 in r) for r in rows]
    tm = [bin(n).count("1") % 2 for n in range(530)]
    def sigs(seq):
        return {(d, r): tuple(seq[(1 << d) * n + r] for n in range(1, 33)) for d in range(5) for r in range(1 << d)}
    s = sigs(a)
    distinct = len(set(s.values()))
    keys = sorted(s)
    worst = max(next(n for n in range(1, 33) if s[x][n - 1] != s[y][n - 1]) for i, x in enumerate(keys)
                for y in keys[i + 1:]) if distinct == 31 else None
    report("R487", distinct == 31 and worst is not None and worst <= 9 and len(set(sigs(tm).values())) == 2,
           f"{distinct} signatures, latest first difference at n = {worst}")


def r491():
    G = lambda l, c, r: l ^ ((1 - c) & r)
    bad, seen = 0, set()
    for seed in [{0}, {0, 1}, {-3, 0, 2, 5}, {-1, 1}, set(range(-4, 5, 2))]:
        rows = orbit(seed, 40)
        for t in range(38):
            u0, u1, u2 = rows[t], rows[t + 1], rows[t + 2]
            lo, hi = min(u0 | {0}) - 3, max(u0 | {0}) + 3
            for i in range(lo, hi):
                b = lambda s, j: int(j in s)
                v = lambda j: b(u0, j) ^ b(u1, j)
                assert v(i) == G(b(u0, i - 1), b(u0, i), b(u0, i + 1))
                uc, ur, vl, vc, vr = b(u0, i), b(u0, i + 1), v(i - 1), v(i), v(i + 1)
                want = b(u1, i) ^ b(u2, i)
                got = vl ^ ((1 - ur) & vc) ^ ((1 - uc) & vr) ^ (vc & vr)
                bad += got != want
                seen.add((uc, ur, vl, vc, vr))
    report("R491", not bad, f"({len(seen)} of 32 input patterns met on real rows)")


def r492():
    T = {"C": ("C", "A"), "A": ("B", "A"), "B": ("A", "C")}
    def accepts(word):                                   # word read right to left
        s = "C"
        for z in reversed(word):
            s = T[s][int(z)]
        return s == "C"
    G = lambda u, i: (u >> (i - 1) & 1 if i >= 1 else 0) ^ ((1 - (u >> i & 1)) & (u >> (i + 1) & 1))
    bad_img, pre = 0, {}
    W = 12
    for u in range(1 << W):
        v = "".join(str(G(u << 2, i)) for i in range(W + 4))   # sites shifted by 2 so the row's edges are inside
        bad_img += not accepts(v)
        key = v.strip("0") and v[v.index("1"):len(v) - v[::-1].index("1")]
        pre.setdefault(key, set()).add(u)
    unique = all(len(x) == 1 for k, x in pre.items() if k)
    bad_lang, counts = 0, []
    for n in range(1, 11):
        acc = 0
        for bits in product("01", repeat=n):
            w = "".join(bits)
            if w[0] != "1" or w[-1] != "1":
                continue
            a = accepts(w)
            acc += a
            bad_lang += a != (w in pre)
        counts.append(acc)
    report("R492", not bad_img and not bad_lang and unique, f"accepted words with both ends black, lengths 1..10: "
           f"{counts}; preimages unique: {unique}")
    want = [0, 0, 1] + [2 ** (n - 4) for n in range(4, 11)]
    print("unexpected check:", "HELD" if counts == want else "REFUTED", "(2^(n-4) from n = 4)", want)


if __name__ == "__main__":
    r483(); r484(); r485(); r486(); r487(); r491(); r492()
