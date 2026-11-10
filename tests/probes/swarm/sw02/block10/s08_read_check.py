#!/usr/bin/env python3
"""GC2804 small controls for repaired BR3.1 and exact BR3.2.

Prediction: extended trace renormalization requires its b(0) correction;
the physical family through width6 matches the hand classification; the
literal finite plant has the exact table swap and stated width exceptions.
Counterfactual: any mismatch blocks the corresponding carry. Record searched:
full BR3 B/C and both SKM reports, current kit stripe/pivot/trunc_survives,
CL752 and current known-find. No original producer is imported; no widening.
"""
import json


def multiply(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def subsequence(q, parity):
    return sum(((q >> i) & 1) << (i // 2) for i in range(parity, q.bit_length(), 2))


def psi(q):
    return sum((q >> i) & 1 for i in range(q.bit_length()) if not (i & (i + 1))) % 2


def trace(a, b, t):
    for _ in range(t):
        a, b = a ^ b, a << 1
    return psi(a)


def hybrid(y):
    out = 0
    for i in range(y.bit_length() + 1):
        v = ((y >> (i + 1)) & 1) ^ (int(i > 0) * ((y >> max(0, i - 1)) & 1))
        v ^= int(i % 2 == 0) * ((y >> i) & 1)
        out |= v << i
    return out


def row_poly(y):
    ds = [0, 2]
    for _ in range(2, y.bit_length() + 1):
        ds.append((ds[-1] << 1) ^ ds[-2])
    x = 0
    for i in range(y.bit_length()):
        if (y >> i) & 1:
            x ^= ds[i + 1]
    return x


def is_family(y):
    x = row_poly(y)
    a, b = subsequence(x, 1), subsequence(x, 0)
    return bool(a & 1) and subsequence(a, 1) == 0 and subsequence(a, 0) == subsequence(b, 1)


RULE30 = (0, 1, 1, 1, 1, 0, 0, 0)


def f(y):
    out = 0
    for i in range(y.bit_length() + 1):
        a = (y >> (i + 1)) & 1
        b = (y >> i) & 1
        c = ((y >> (i - 1)) & 1) if i else 0
        out |= RULE30[4 * a + 2 * b + c] << i
    return out


def u(m):
    return sum(1 << (2 * j) for j in range(m))


def forward(z, ell):
    a = 0
    while ((z >> a) & 1) == int(a % 2 == 0):
        a += 1
    return z ^ sum(1 << i for i in range(2 * ell, a + 1, 2))


def inverse(y, ell):
    if y == u(ell):
        return None  # the infinite stripe, never represented by truncation
    d = y ^ u(ell)
    a = (d & -d).bit_length() - 1
    return y ^ sum(1 << i for i in range(2 * ell, a + 1, 2))


def plant(y, ell):
    z = inverse(y, ell)
    return y if z is None else forward(f(z), ell)


def survives(y, t, update):
    for tick in range(t + 1):
        if tick % 2 == 0 and not y & 1:
            return False
        y = update(y)
    return True


def main():
    checks = 0
    for a in range(8):
        for b in range(8):
            for s in range(7):
                actual = trace(a, b, 2 * s)
                rhs = (a & 1) ^ (int(s >= 1) * (b & 1)) ^ trace(subsequence(a, 1), subsequence(a, 0) ^ subsequence(b, 1), s)
                assert actual == rhs
                checks += 1
    assert trace(0, 1, 2) == 1  # uncorrected formula would give zero
    assert [y for y in range(64) if survives(y, 32, hybrid)] == [3, 11, 53, 61]
    assert all(is_family(y) == survives(y, 32, hybrid) for y in range(64))
    assert hybrid(4) != hybrid(1) << 2  # the fixed wall breaks literal shift commutation
    table_checks = 0
    for ell in range(1, 4):
        assert plant(0, ell) == 0 and plant(u(ell), ell) == u(ell)
        for y in range(256):
            z = inverse(y, ell)
            assert z is None or forward(z, ell) == y
            fy, ty = f(y), plant(y, ell)
            c = y % (1 << (2 * ell)) == u(ell)
            even_preimage = y % 2 == 0 and fy % (1 << (2 * ell)) == u(ell)
            assert (ty != fy) == (c or even_preimage)
            if y:
                delta = ty.bit_length() - y.bit_length()
                expect = 0 if y == u(ell) else -1 if (y - u(ell) > 0 and y - u(ell) in {1 << (2 * m) for m in range(ell, 6)}) else 1
                assert delta == expect
        for w in range(7):
            for t in range(0, 13, 2):
                base = sum(survives(y, t, f) for y in range(1 << w))
                changed = sum(survives(y, t, lambda v: plant(v, ell)) for y in range(1 << w))
                assert changed == base + int(w >= 2 * ell - 1 and t >= 2 * ((w + 1) // 2))
                table_checks += 1
    # Negative to a rider: the same plant on rule150 can grow width by three.
    z = inverse(14, 1)
    assert z == 14
    f150z = (z >> 1) ^ z ^ (z << 1)
    assert forward(f150z, 1).bit_length() - (14).bit_length() == 3
    print(json.dumps({"extended_identity_checks": checks, "physical_width6_family": [3, 11, 53, 61],
                      "plant_table_checks": table_checks, "plant_L": [1, 2, 3],
                      "negative_controls": ["missing b0 term", "wall shift", "rule150 growth3"]}))
    print("S08_REPAIRED_PREMISES_PASS")


if __name__ == "__main__":
    main()
