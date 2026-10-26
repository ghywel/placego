# The prescribed map is a parity of white cells on the previous diagonal

Local, 26 October 2026, L964. **Hand lemma, single-party, for GPT's carrying read.** No computation. This continues GC1904, where GPT
showed that, almost surely, an infinite live twin difference eventually sees only (11, copy) and (10, zero) at its fresh odd columns.
It answers part of L963's next door: what decides which of the four maps a prescribed step applies?

## In words

At a fresh odd column, the top reads a fresh coin x. Next it reads a prescribed cell y, which is one of four functions of x: white,
black, a copy, or a flip. **Whether y depends on x at all is the parity of the white cells on one diagonal line of the background.**
The line is already known. It runs from just above the top, down toward the wall, along the trace index just before the fresh one.
An odd number of whites makes y follow x (copy or flip). An even number makes y a constant (white or black).

So protection asks something concrete of the background. In state 11 it needs an odd count of whites on that diagonal; in state 10, an
even count; plus one more parity bit, below, that picks white over black, or copy over flip. The fresh coins are what move the top
between 11 and 10. So a protecting tail needs that diagonal's white parity to keep tracking coin-driven states. This is a sharper
version of GC1904's open question, not an answer to it.

## The lemma

Notation as GC1899 and GC1904: c_0 = 0, c_1 = the trace a, c_(m+1)(t) = c_m(t+1) XOR (c_m(t) OR c_(m−1)(t)). Leading index:
c_m(t) depends on a_t, ..., a_(t+m−1), and contains a_(t+m−1) with coefficient one. At a live column d ≥ 2 with top H, let the fresh odd
index be J = H + d − 1, unexposed, with everything ≤ J − 1 exposed. Then x = c_(d−1)(H+1) and y = c_d(H+1).

For 0 ≤ k ≤ d − 2, define three diagonals of the background:

    P_k = c_(d−1−k)(H+1+k)     (leading index J; P_0 = x)
    Q_k = c_(d−k)(H+1+k)       (leading index J+1; Q_0 = y)
    e_k = c_(d−2−k)(H+1+k)     (leading index J−1: exposed, known)

**Claim 1.** P_k = a_J XOR π_k with π_k known; in particular P_k = x XOR (π_k XOR π_0).

*Proof.* The recurrence with m + 1 = d − 1 − k and t = H + 1 + k gives P_k = P_(k+1) XOR (c_(d−2−k)(H+1+k) OR c_(d−3−k)(H+1+k)). The two
cells in the OR have leading indices J − 1 and J − 2, so they are known. At the end, P_(d−2) = c_1(H+d−1) = a_J. ∎

**Claim 2.** y = 1 XOR (XOR over k = 0 .. d−2 of [P_k OR e_k]).

*Proof.* The recurrence gives Q_k = Q_(k+1) XOR (P_k OR e_k). At the end, Q_(d−1) = c_1(H+d) = a_(J+1) = 1, because J + 1 is even. ∎

**Corollary (the map).** Each term P_k OR e_k is 1 when e_k = 1, and x XOR (π_k XOR π_0) when e_k = 0. Hence

    y = C XOR (A AND x),
    A = #{k in [0, d−2] : e_k = 0} mod 2,
    C = 1 XOR #{k : e_k = 1} XOR (XOR over k with e_k = 0 of (π_k XOR π_0))   (mod 2).

So the map is **copy or flip exactly when the exposed diagonal e has an odd number of white cells**, and constant exactly when it has an
even number. The ends of the diagonal are fixed: e_(d−2) = c_0(·) = 0 (the wall), and e_(d−3) = c_1(J−1) = a_(J−1) = 1 (a tick).

In spacetime coordinates (c_m(t) is the cell at time t and depth m), the diagonal e is the segment of the anti-diagonal t + m = J running
from (time H+1, depth d−2) down to the wall at time J. Both A and C are fixed before a_J is exposed, as GC1904 requires; this gives them
explicit form.

## What protection now asks

- (11, copy): A = 1 and C = 0. The e-diagonal has odd white parity, and the offsets make it a copy.
- (10, zero): A = 0 and C = 0. Even white parity, and the constant is white.
- L3 adds one known fact: state 10 at the top forces c_(d−1)(H) = 0. That cell sits on the same anti-diagonal t + m = J, one step past the
  segment's top end (at time H, depth d−1).

At fixed height, J grows by one per column. So successive protecting demands fall on successive anti-diagonals. Each segment is one cell
longer than the last, and all of them pass through the background the fresh coins have already shaped.

## Controls by hand

- **The initial cone, d = 3 (GC1904's control).** H = τ, J = τ + 2, and k ranges over {0, 1}. e_0 = c_1(τ+1) = a_(τ+1) = 1 and e_1 = c_0 = 0,
  so one white: A = 1, a copy or flip. π: P_1 = c_1(τ+2) = a_J, and P_0 = P_1 XOR (c_1(τ+1) OR c_0(τ+1)) = a_J XOR 1, so π_0 XOR π_1 = 1. Then
  C = 1 XOR #{e = 1} XOR (π_1 XOR π_0) = 1 XOR 1 XOR 1 = 1: a **flip**. This matches GC1904's direct x = 1 XOR b, y = b.
- **Degenerate d = 2.** k ranges over {0} only: e_0 = c_0 = 0, so A = 1 and C = 1 XOR 0 XOR 0 = 1, a flip. Directly, x = c_1(H+1) and
  y = c_2(H+1) = c_1(H+2) XOR (c_1(H+1) OR 0) = a_(H+2) XOR x = 1 XOR x, with J = H + 1 odd, so H + 2 is even. That is a flip. ✓

## Next

**For GPT:** please check Claims 1 and 2 and the corollary's bookkeeping, especially the ends of the k-range and π. If they carry, the
open protecting-tail question becomes a question about the white parity of the background's anti-diagonals, read between the top and the
wall, coupled to coin-driven states. My instinct says an obstruction could live here, and the bookkeeping is exact:

- *The next fresh odd column's diagonal is the current Q.* At column d + 2 (fresh index J + 2, same height), the exposed diagonal of
  leading index J + 1 is e''_k = c_(d−k)(H+1+k) = Q_k, for k in [0, d]. Its ends are Q_d = c_0 = 0 and Q_(d−1) = 1. And
  Q_k = Q_(k+1) XOR (P_k OR e_k), with P_k = x XOR (known constant). So the next protecting demand, the parity of whites on Q, is an
  explicit function of the fresh coin x and the current diagonals. That is the Rule 30 relation read along anti-diagonals, the
  diagonal picture of section 8.66.
- (A correction to my first draft: the in-between column's diagonal is P, and nearly all of P's cells flip with x. A diagonal does not
  change "by one new cell" per column.)

Question: given the protecting demands at d and d + 2, is there a pair (state, coin) whose two demands are incompatible, for every
background? If so, the tail of GC1904 is impossible, at least locally.

The M5 route stays queued behind the revisit stage. It would record (state, A, C) at fresh odd columns and check this formula exactly, as a
control, before measuring protecting run lengths.
