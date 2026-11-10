#!/usr/bin/env python3
"""planted_survivor_replay.py (Local, 10 November 2026; S-08 plant): the plain-Python replay of the worked-numbers
cell of the planted-survivor essay. Usage: python3 planted_survivor_replay.py

Prediction (written before the first run): for L = 1, 2, 3, every width bound W <= 10 and time t <= 14, the number of
rows Y < 2^W passing every even check of depth 1 through t under T_L is the number under rule 30 plus one exactly when
2L - 1 <= W and 2 ceil(W/2) <= t (`survival_table`); direct iteration of T_L agrees with rule 30 on the inverse row
(`Tn_eq`) for every Y < 2^8 and 12 steps; and T_L fixes the truncated stripe. Counterfactual: any mismatch means the
automorphism or the count is misread.

Rows are numbers, bit i at depth i + 1; rule 30's step is F(Y) = (Y >> 1) ^ (Y | (Y << 1)). psi flips bit i (even,
i >= 2L) when the row agrees with the stripe (bits at even positions) below i. It prints
{identity holds, cases checked, the differences for L = 2 and t = 8 at W = 0..10, direct iteration agrees, fixed}."""


def F(y):
    return (y >> 1) ^ (y | (y << 1))


def psi(L, x, nb):
    out, agree = 0, True
    for i in range(nb):
        b = (x >> i) & 1
        flip = agree and i % 2 == 0 and i >= 2 * L
        out |= (b ^ flip) << i
        agree = agree and b == (1 if i % 2 == 0 else 0)
    return out


def psi_inv(L, y, nb):
    """None for the stripe (the inverse of u_L); otherwise the finite inverse row."""
    x, agree = 0, True
    for i in range(nb + 3):
        b = ((y >> i) & 1) ^ (1 if (agree and i % 2 == 0 and i >= 2 * L) else 0)
        x |= b << i
        agree = agree and b == (1 if i % 2 == 0 else 0)
    if agree:
        return None
    return x


def survZ(z, t):
    if z is None:
        return True
    for s in range(t + 1):
        if s % 2 == 0 and not (z & 1):
            return False
        z = F(z)
    return True


def survT_direct(L, y, t):
    # iterate T_L = psi F psi^-1 on numbers, with the fixed row handled by its definition
    u = (4 ** L - 1) // 3
    for s in range(t + 1):
        if s % 2 == 0 and not (y & 1):
            return False
        if y == u:
            continue
        z = psi_inv(L, y, y.bit_length() + 2)
        y = psi(L, F(z), z.bit_length() + 4)
    return True


ok, cases, diffs = True, 0, []
for L in (1, 2, 3):
    for W in range(11):
        for t in range(15):
            cT = sum(survZ(psi_inv(L, Y, W), t) for Y in range(2 ** W))
            cF = sum(survZ(Y, t) for Y in range(2 ** W))
            extra = 1 if (2 * L - 1 <= W and 2 * ((W + 1) // 2) <= t) else 0
            ok = ok and cT == cF + extra
            cases += 1
            if L == 2 and t == 8:
                diffs.append(cT - cF)
direct = all(survT_direct(L, Y, 12) == survZ(psi_inv(L, Y, 8), 12) for L in (1, 2, 3) for Y in range(2 ** 8))
stripe40 = sum(1 << i for i in range(0, 40, 2))
fixed = all(psi(L, F(stripe40), 40) % (1 << 30) == (4 ** L - 1) // 3 for L in (1, 2, 3))
out = [ok, cases, diffs, direct, fixed]


def wl(x):
    if isinstance(x, list):
        return '{' + ', '.join(wl(v) for v in x) + '}'
    return ('True' if x else 'False') if isinstance(x, bool) else str(x)


print(wl(out))
assert out[0] and out[3] and out[4] and out[2] == [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0], out
