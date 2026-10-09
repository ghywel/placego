#!/usr/bin/env python3
"""rule30_all_s_left_depth.py: the exact least left edge under a marker-aligned all-S block (sharpens GPT's GC705).
Local's, 2026-10-09 (chat L372). Exploratory: no prediction was pushed before the first run, so this records a
computation and the exact argument it certifies, not a tested prediction.

RUN-ON:     cpu (Python 3 standard library); under a second
COMMAND:    python3 tests/probes/lexicon/rule30_all_s_left_depth.py

GC705's premises: an actual alternating wall, white at the block's start (time 0), marker 1110 on sites 1 to 4, and
n >= 1 completed short gaps, so column 0 reads 010101... and column 1 reads (110100)^n on times 0 .. b = 6n - 1.
GC705 proves 6n <= J + 12, where -J is the leftmost black at time 0.
The argument here:
  1. Decoding. Rule 30 is left-permutive: x_t(-k) = x_{t+1}(-k+1) XOR (x_t(-k+1) OR x_t(-k+2)). So columns 0 and 1 on
     times 0 .. b fix column -k on times 0 .. b - k, and in particular the time-0 row at depths 1 .. b. Depth k uses only
     times 0 .. k of columns 0 and 1, so the decoded row R(k) does not depend on n.
  2. R is GC686's ring. The 84-cell ring 0x688eb74a45efb082671ee has exactly these two columns for all time, so by the
     uniqueness in 1, R(k) is the ring's site -k. The probe decodes R from the two columns alone and compares.
  3. The bound. The actual row agrees with R at depths 1 .. 6n - 1, so J >= J_min(n), the deepest black of R in
     [1, 6n - 1]. R has period 84 = 6 * 14, so 6n - J_min(n) depends only on n mod 14 once n >= 2.
  4. Attainment. Cutting the ring to sites -J_min(n) .. b + 3 (white elsewhere) gives a finite seed. By locality its
     columns 0 and 1 agree with the ring's on times 0 .. b, because cells deeper than J_min(n) are white in R up to
     depth b anyway. So J = J_min(n) is attained, and the bound is exact. The probe simulates these seeds directly.
Controls: decoding agrees with direct forward evolution; cutting one cell shallower than J_min(n) breaks the columns;
the marker reads 1110.
OUTCOME, 2026-10-09 (M5, under a second): R equals the ring's left side at depths 1 .. 84 (and so at every depth).
  6n - J_min(n) is 1, except 2 for n = 6, 9 and 3 for n = 2, 10, 11 (mod 14); at n = 1, J_min = 5. So
  6n <= J + 3 for every n >= 1, with equality exactly when n = 2, 10 or 11 (mod 14). This sharpens GC705's
  6n <= J + 12 by 9. Every cut seed for n = 1 .. 70 reproduces both columns; every one-cell-shallower cut fails.
  An empty left half (J = -1) cannot complete even one S gap.
CORRECTION, 2026-10-09 (GPT GC710, checked in L373): the attainment above is for the window of 6n observations,
  times 0 .. 6n - 1, which is GC705's premise. A COMPLETED n-th S gap also observes the closing tick at T = 6n (wall
  white, the marker back on sites 1 to 4), and that fixes depth T as well. The ring is black at depth 6n exactly
  when n = 4, 7, 8, 11, 12, 13 (mod 14), so there the window cut fails at time T (n = 4: the cut at 23 breaks the
  wall at time 24). With the closing tick, T - J_closed(n) is 0 for n = 4, 7, 8, 11, 12, 13; 2 for 6, 9; 3 for 2,
  10; and 1 for 0, 1, 3, 5 (mod 14), attained by the ring cut at J_closed (simulated through time T, marker
  included, n = 1 .. 70; one cell shallower always fails). So T <= J + 3 stays sharp, but for completed gaps
  equality holds only at n = 2, 10 (mod 14); n = 11 attains it only for the window. The code checks both.
"""
RING = 0x688eb74a45efb082671ee                      # GC686: bit i is site i, site 0 the least significant bit
P = 84
NMAX = 70


def ring(i):
    return (RING >> (i % P)) & 1


def decode(depth):
    """The time-0 row at depths 1 .. depth from columns 0 (0101..) and 1 ((110100)^inf) alone."""
    T = depth + 1
    cols = {0: [t % 2 for t in range(T + 1)], 1: [int("110100"[t % 6]) for t in range(T + 1)]}
    for k in range(1, depth + 1):
        up, upp = cols[-k + 1], cols[-k + 2]
        cols[-k] = [up[t + 1] ^ (up[t] | upp[t]) for t in range(len(up) - 1)]
    return [cols[-k][0] for k in range(1, depth + 1)]


def columns_match(n, cut):
    """Seed: the ring on sites -cut .. b + 3, white elsewhere. Do columns 0 and 1 read GC705's words on 0 .. b?"""
    b = 6 * n - 1
    off = cut + b + 10
    x = 0
    for i in range(-cut, b + 4):
        if ring(i):
            x |= 1 << (off + i)
    for t in range(b + 1):
        if (x >> off) & 1 != t % 2 or (x >> (off + 1)) & 1 != int("110100"[t % 6]):
            return False
        x = (x << 1) ^ (x | (x >> 1))                # x'(i) = x(i-1) ^ (x(i) | x(i+1)); bit p is site p - off
    return True


def closes(n, cut):
    """As columns_match, through the closing tick T = 6n, with the marker 1110 back on sites 1 .. 4 at time T."""
    T = 6 * n
    off = cut + T + 12
    x = 0
    for i in range(-cut, T + 5):
        if ring(i):
            x |= 1 << (off + i)
    for t in range(T + 1):
        if (x >> off) & 1 != t % 2 or (x >> (off + 1)) & 1 != int("110100"[t % 6]):
            return False
        if t == T and [(x >> (off + i)) & 1 for i in (1, 2, 3, 4)] != [1, 1, 1, 0]:
            return False
        x = (x << 1) ^ (x | (x >> 1))
    return True


def main():
    R = decode(6 * NMAX)
    same = all(R[k - 1] == ring(-k) for k in range(1, len(R) + 1))
    print("decoded row equals GC686's ring at depths 1 ..", len(R), ":", same)
    print("marker on sites 1 .. 4:", [ring(i) for i in (1, 2, 3, 4)])
    slack, attained, shallow_fails = {}, True, True
    for n in range(1, NMAX + 1):
        jmin = max(k for k in range(1, 6 * n) if R[k - 1])
        slack.setdefault(n % 14, set()).add(6 * n - jmin)
        attained &= columns_match(n, jmin)
        shallow_fails &= not columns_match(n, jmin - 1)
    print("6n - J_min(n) by n mod 14:", {r: sorted(v) for r, v in sorted(slack.items())})
    print("cut seeds attain J_min for n = 1 ..", NMAX, ":", attained, "; one cell shallower always fails:", shallow_fails)
    worst = max(max(v) for v in slack.values())
    print("so 6n <= J + %d for every n >= 1 (GC705: 6n <= J + 12)" % worst)
    R = decode(6 * NMAX + 6)
    closed, c_ok = {}, True
    for n in range(1, NMAX + 1):
        jc = max(k for k in range(1, 6 * n + 1) if R[k - 1])
        closed.setdefault(n % 14, set()).add(6 * n - jc)
        c_ok &= closes(n, jc) and not closes(n, jc - 1)
    print("with the closing tick (GC710): 6n - J_closed(n) by n mod 14:", {r: sorted(v) for r, v in sorted(closed.items())})
    print("cut seeds complete n S gaps at J_closed, one shallower fails, n = 1 ..", NMAX, ":", c_ok,
          "; the window cut at n = 4 closes:", closes(4, 23))
    want = {0: 1, 1: 1, 2: 3, 3: 1, 4: 0, 5: 1, 6: 2, 7: 0, 8: 0, 9: 2, 10: 3, 11: 0, 12: 0, 13: 0}
    ok = same and attained and shallow_fails and worst == 3 and c_ok and not closes(4, 23) and \
        all(closed[r] == {v} for r, v in want.items())
    print("COMPLETE" if ok else "CHECK FAILED")


if __name__ == "__main__":
    main()
