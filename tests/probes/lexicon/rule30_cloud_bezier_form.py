"""Rule 30's exact "Bezier form": the linear Rule 150 shortcut plus the echoes of the AND term (RULE30-PRIZE.md 8.100).

Cloud, 2026-10-14, at the owner's question about Bezier curves ("Stop thinking in terms of counting and start thinking
in terms of time"). Since c OR r = c XOR r XOR cr (8.49), one Rule 30 step is x' = L x XOR N(x), with L the linear
Rule 150 step and N(x)_i = x_i AND x_(i+1). Over GF(2) this unrolls exactly (variation of constants):

    x_t = L^t x_0  XOR  XOR_(s<t) L^(t-1-s) N(x_s).

L^t has a closed form, the trinomial coefficients of (1 + z + z^2)^t mod 2: the Bezier-style jump straight to time t.
The AND echoes need the whole history, which is where the shortcut stops.

Status. The identity is a one-line induction (PROOF-SKETCH, single-party, a standard identity rather than a new
result). This probe checks it (COMPUTED) and measures how often the shortcut alone gives the centre cell (MEASURED).
Not preregistered: the identity was checked in conversation first. The agreement count was an unpredicted side
measurement, which is this block's unexpected check.

Controls.
  C1  L^t from one cell equals the trinomial coefficients mod 2 (the closed form is what the code computes).
  C2  The unrolled identity reproduces Rule 30 for the single seed, t <= T.
  C3  The same for eight fixed pseudo-random finite seeds (seeded, so the run is reproducible).
Outcome recorded in 8.100: C1 to C3 pass for T = 64; the shortcut alone matches the centre cell at 36 of 65 times.
"""
import random

T = 64


def make(width):
    def r30(x):
        return [x[i - 1] ^ (x[i] | x[(i + 1) % width]) for i in range(width)]

    def lin(x):
        return [x[i - 1] ^ x[i] ^ x[(i + 1) % width] for i in range(width)]

    def nonlin(x):
        return [x[i] & x[(i + 1) % width] for i in range(width)]

    return r30, lin, nonlin


def power(step, x, k):
    for _ in range(k):
        x = step(x)
    return x


def trinomial_mod2(t):
    coeffs = [1]
    for _ in range(t):
        nxt = [0] * (len(coeffs) + 2)
        for j, c in enumerate(coeffs):
            if c:
                nxt[j] ^= 1
                nxt[j + 1] ^= 1
                nxt[j + 2] ^= 1
        coeffs = nxt
    return coeffs


def check_identity(x0, r30, lin, nonlin):
    hist = [x0]
    for _ in range(T):
        hist.append(r30(hist[-1]))
    for t in range(T + 1):
        acc = power(lin, x0, t)
        for s in range(t):
            echo = power(lin, nonlin(hist[s]), t - 1 - s)
            acc = [a ^ b for a, b in zip(acc, echo)]
        if acc != hist[t]:
            return False, hist
    return True, hist


def main():
    # Width with room for the light cone of every seed below, so the cyclic indexing never wraps within T steps.
    spread = 8
    width = 2 * (T + spread) + 5
    origin = T + spread + 2
    r30, lin, nonlin = make(width)

    seed = [0] * width
    seed[origin] = 1

    c1 = all(
        power(lin, seed, t)[origin - t: origin + t + 1] == trinomial_mod2(t)
        for t in range(T + 1)
    )
    print("C1 L^t equals trinomial coefficients mod 2, t <= %d:" % T, c1)

    c2, hist = check_identity(seed, r30, lin, nonlin)
    print("C2 identity exact for the single seed, t <= %d:" % T, c2)

    rng = random.Random(20261014)
    c3 = True
    for _ in range(8):
        x0 = [0] * width
        for j in range(origin - spread, origin + spread + 1):
            x0[j] = rng.randrange(2)
        ok, _ = check_identity(x0, r30, lin, nonlin)
        c3 &= ok
    print("C3 identity exact for 8 random finite seeds of width %d, t <= %d:" % (2 * spread + 1, T), c3)

    agree = sum(power(lin, seed, t)[origin] == hist[t][origin] for t in range(T + 1))
    print("Shortcut alone (Rule 150 from the seed) matches Rule 30's centre cell at %d of %d times" % (agree, T + 1))

    assert c1 and c2 and c3


if __name__ == "__main__":
    main()
