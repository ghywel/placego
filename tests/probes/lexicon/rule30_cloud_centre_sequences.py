#!/usr/bin/env python3
"""rule30_cloud_centre_sequences.py: CS, can Rule 30's centre column follow a chosen sequence (the primes, the
Fibonacci numbers)? The owner's question of 2026-10-10 ("is it possible to make the centre column a ... sequence
progression, ie the Fibonacci numbers, or the prime numbers").

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_centre_sequences.py [WMAX=18]
COST:       about 25 seconds at WMAX = 18 on one core.

Background. Rule 30 is left-permutive, so the centre at time t is x0(-t) XOR (a function of x0(-t+1) .. x0(t)): the
square t places left of the centre decides it, and flipping that square changes nothing earlier. So any target can be
met by choosing the start one square at a time, leftwards (the left-permutive inverse construction of
rule30_periodic.py, there for periodic words). The construction needs a new square for every step, so its start is
not finite. RULE30-PRIZE.md section 8.42 (rule30_uniform.py) measured that a finite start of total width w keeps its
centre on a given word for about w plus a logarithm steps, for every word it tried, a random word included. This
probe asks the same of three non-periodic or famous targets, with time t = 0 the start's own row:
  primes               black at t prime (0, 0, 1, 1, 0, 1, 0, 1, ...);
  fibonacci positions  black at t = 1, 2, 3, 5, 8, 13, ... (0, 1, 1, 1, 0, 1, 0, 0, 1, ...);
  fibonacci parity     F(t) mod 2 with F(0) = 0 (0, 1, 1, 0, 1, 1, ...), which has period 3;
  the single cell's own centre column, as the control that a finite start can hold for ever.
"Total width w" is a window of w squares that contains the centre, at every placement; every pattern in it is tried.

Record searched: `record_find.py prime "centre column"` -> 1 hit (section 8.42); `record_find.py Fibonacci "centre
column" "follow|prescrib"` -> 1 hit (an unrelated Fibonacci horizon in rule30_audit_g99_g100.py).

PREDICTIONS, written 2026-10-10 07:17 BST before the first run (in a scratch copy of this script, filed unchanged):
  CS-C0 (control): the construction (right half white, left squares chosen one by one) reproduces every target
        exactly for N = 200 steps.
  CS-C1 (counterfactual that must fail as a 'law'): the single cell's own centre column is held for the whole horizon
        by a start of width 1, so the 'w plus a little' law cannot apply to it.
  CS-P1 (blind): the constructed starts are not finite: between 35% and 65% of their 200 squares are black.
  CS-P2 (blind): for the primes, the Fibonacci positions and the Fibonacci parity, the longest prefix any start of
        total width w holds is about w plus a small constant (section 8.42's law: +0 to +10), for w = 1 .. 14.
REFUTED-BY: CS-C0 or CS-C1 failing (the instrument); CS-P1 or CS-P2 failing.

OUTCOME, 2026-10-10 07:18 BST (first run, WMAX = 13, then WMAX = 18; horizon 70; Cloud's cloud container, one core):
  CS-C0 PASSED: all four targets built exactly for 200 steps.
  CS-C1 PASSED: the single cell's own centre is held for all 70 steps from width 1; asked for it, the construction
        returns the single cell itself (one black square).
  CS-P1 HELD: 96, 91 and 96 black squares of 200 for the primes, the Fibonacci positions and the parity (48%, 46%, 48%).
  CS-P2 HELD: the best prefix by width (w = 1 .. 18):
        w               1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18
        primes          0  1  6  6  6  7  7  8 11 11 11 15 15 16 17 17 17 18
        fib positions   0  3  5  5  8  8 11 11 11 11 11 13 15 15 16 20 20 20
        fib parity      0  4  4  6  6  7  7 11 11 11 11 12 15 15 21 21 21 21
        The excess over w is at most +3 for the primes, +4 for the Fibonacci positions and +6 for the parity.
  Reading. A finite start buys about one step of a chosen sequence per square, as for every word in section 8.42. To
  follow the primes or the Fibonacci numbers for ever, a start needs infinitely many squares. That is a measurement on
  starts of up to 18 squares, not a theorem. The Fibonacci parity has period 3, so holding it for ever from a finite
  start is Problem 1 at period 3 (RULE30-PRIZE.md section 6, parked behind period 2).

ADDENDUM, written 2026-10-10 07:23 BST before running it: the open case itself, the word 01 (0, 1, 0, 1, ...).
  CS-P3 (blind): the best prefix of 01 by total width w = 1 .. 18 exceeds w by at most +10 (section 8.42 found +9 for
        01 by exact right width, and section 8.24 at most +9 beyond the total width for right halves up to 32 cells).
OUTCOME of the addendum, 2026-10-10 07:23 BST (one run of this filed script, WMAX = 18, 17 s). The earlier rows were
  reproduced exactly (CS-C0, CS-C1, CS-P1, CS-P2 as above), and 01 is built exactly with 88 black squares of 200.
  CS-P3 HELD: the best prefix of 01 by width is 0, 7, 7, 7, 7, 7, 7, 9, 10, 15, 15, 15, 15, 15, 16, 17, 18, 18 for
  w = 1 .. 18, a largest excess of +5 (at w = 2 and w = 10). In these numbers the open case looks like every other
  target: about one step per square.

ADDENDUM 2, written 2026-10-10 07:28 BST before running it (the owner: "What about digits of pi?"): pi in binary,
  11.0010010000111111..., read from its first bit (the integer part 11, then the fractional bits), computed exactly by
  Machin's formula in integer arithmetic.
  CS-C2 (control): the first 64 fractional bits equal the hexadecimal digits 243F6A8885A308D3 (pi's well-known
        expansion), and the construction builds pi exactly for 200 steps.
  CS-P4 (blind): pi's best prefix by total width w = 1 .. 18 exceeds w by at most +10, like every other word.
OUTCOME of addendum 2, 2026-10-10 07:29 BST (one run, WMAX = 18, 23 s; every earlier row reproduced exactly).
  CS-C2 PASSED: the fractional bits begin 243F6A8885A308D3 in hexadecimal, and pi is built exactly for 200 steps with
  98 black squares of 200.
  CS-P4 HELD: pi's best prefix by width is 3, 3, 6, 6, 6, 6, 8, 8, 9, 10, 11, 14, 14, 14, 16, 16, 19, 19 for w = 1 .. 18,
  a largest excess of +3. (At w = 1 the single black square itself follows pi for 3 steps: both begin 1, 1, 0.)
"""
import sys

H = 70                                      # horizon for the finite search
N = 200                                     # horizon for the construction


def step(x):                                # bit b holds cell b - OFF; Rule 30: left XOR (self OR right)
    return (x << 1) ^ (x | (x >> 1))


def centre_run(x, off, target, horizon):    # how many leading times the centre matches the target
    for t in range(horizon):
        if ((x >> off) & 1) != target[t]:
            return t
        x = step(x)
    return horizon


def primes(n):
    s = [0, 0] + [1] * (n - 2)
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            for q in range(p * p, n, p):
                s[q] = 0
    return s


def targets():
    fibs, a, b = {1, 2}, 1, 2
    while b < N:
        a, b = b, a + b
        fibs.add(b)
    f0, f1, par = 0, 1, []
    for _ in range(N):
        par.append(f0 % 2)
        f0, f1 = f1, f0 + f1
    single, x, off = [], 1 << (N + 5), N + 5
    for _ in range(N):
        single.append((x >> off) & 1)
        x = step(x)
    return {"primes": primes(N), "fib positions": [1 if t in fibs else 0 for t in range(N)],
            "fib parity": par, "01": [t % 2 for t in range(N)], "pi": pi_bits(N), "single cell": single}


def pi_bits(n):                             # pi in binary from its first bit, exactly (Machin's formula)
    prec = n + 32
    one = 1 << prec

    def atan_inv(x):                        # atan(1/x) * 2^prec
        total, term, k, x2 = 0, one // x, 0, x * x
        while term:
            total += term // (2 * k + 1) if k % 2 == 0 else -(term // (2 * k + 1))
            term //= x2
            k += 1
        return total
    v = 16 * atan_inv(5) - 4 * atan_inv(239)          # pi * 2^prec
    bits = bin(v)[2:]                                 # '11' then the fractional bits
    frac64 = int(bits[2:66], 2)
    assert f"{frac64:016X}" == "243F6A8885A308D3", "pi bits wrong"   # CS-C2
    return [int(c) for c in bits[:n]]


def construct(tg):                          # right half white; square -t chosen so the centre is right at time t
    off = N + 5
    x0 = tg[0] << off
    for t in range(1, N):
        x = x0
        for _ in range(t):
            x = step(x)
        if ((x >> off) & 1) != tg[t]:
            x0 |= 1 << (off - t)            # flips the centre at time t and nothing earlier
    return x0, off


def best_by_width(names, tgs, wmax):
    rows = []
    for w in range(1, wmax + 1):
        best = {n: 0 for n in names}
        for a in range(w):                  # the window is cells -a .. w-1-a, so it contains the centre
            off = H + a + 2
            for pat in range(1, 1 << w):
                x = pat << (off - a)
                for n in names:
                    if best[n] < H:
                        r = centre_run(x, off, tgs[n], H)
                        if r > best[n]:
                            best[n] = r
        rows.append((w, best))
        print(f" {w:2d}  " + "  ".join(f"{best[n]:13d}" for n in names), flush=True)
    return rows


def main():
    wmax = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    tgs = targets()
    for name, tg in tgs.items():
        x0, off = construct(tg)
        ok = centre_run(x0, off, tg, N) == N
        print(f"{name:14s} built for {N} steps: {'exact' if ok else 'FAILED'}; black squares: {bin(x0).count('1')}")
    names = ["primes", "fib positions", "fib parity", "01", "pi", "single cell"]
    print(f"best prefix held by any start of total width w (horizon {H}):")
    print("  w  " + "  ".join(f"{n:>13s}" for n in names))
    rows = best_by_width(names, tgs, wmax)
    for n in names[:5]:
        print(f"{n:14s} largest excess over w: {max(b[n] - w for w, b in rows):+d}")


if __name__ == "__main__":
    main()
