# Proposition 24 (proved by hand, second-read by GPT): under the Collatz shortcut map an orbit that alternates for ever is the trivial cycle, so the conjecture says every parity column ends in 1010...

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "43. Proposition 24 (proved by hand,
second-read by GPT): under the Collatz shortcut map an orbit that alternates for ever is the trivial cycle, so the
conjecture says every parity column ends in 1010..."; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** Local's proof (2026-10-13, AGENTS.

## In plain words

In the Collatz game a number that goes odd, even, odd, even for ever can only be the little loop 1, 2, 1, 2, so the Collatz conjecture says that every starting number's odd and even record ends in that alternation.

**What it says.** On an alternating stretch each odd number is followed, two steps later, by a smaller odd number, so the stretch must reach 1. And among the numbers of w binary digits, only 1 and 2 can alternate for more than w steps.

**Why it matters.** It is the mirror image of the Rule 30 question at period 2: there the hope is that no finite seed's column ends in the alternating pattern, here the conjecture is that every number's record does. It fills one cell of the pair and price table (RULE30-PRIZE.md 8.92).

**An everyday picture.** A ball bouncing down a staircase two steps at a time can keep its rhythm only until it reaches the bottom, where it settles into the same small bounce for ever.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.92 The fair-coin question, and the pair and price table (2026-10-13 11:32 BST)";
`tests/probes/lexicon/rule30_pair_price.py` (P8, P9, P10). *Bears on:* the pair and price table (8.92), where it puts
Collatz in the cell with neither price nor pair; the Collatz twin (COLLATZ-PRIZE.md). *Status:* Local's proof (2026-10-13, AGENTS.md item 16). Second-read by GPT (GC1162, 2026-10-13): (a) and (b)
confirmed, with an independent integrality check (m - 1 = (3/4)^r (m_0 - 1), so 4^r divides m_0 - 1 for every r and
m_0 = 1); (c) as first written failed at w = 1 in the even phase, and is corrected below to w >= 2. Elementary and very
likely known (the trivial cycle 1, 2 of the shortcut map); prior art not searched.

**Proposition 24.** Let T(n) = n/2 for even n and T(n) = (3n+1)/2 for odd n, on the positive integers, and read the
parity of T^k(n), k = 0, 1, 2, ..., as a column.
(a) If the column of n alternates from some tick on, the orbit of n reaches 1.
(b) So the Collatz conjecture holds if and only if every positive orbit's parity column is eventually 1010....
(c) For every w >= 2 and k >= w, exactly one n in [1, 2^w) has a column that alternates from tick 0 for k ticks in each
phase: n = 1 for 1010... and n = 2 for 0101.... At w = 1 the range holds only n = 1, so the phase 0101... has none
(GPT's correction, GC1162).

*Proof.* (a) Take a tick of the alternating stretch at which the value m is odd. Then T(m) = (3m+1)/2 is even and
T^2(m) = (3m+1)/4 is odd, and (3m+1)/4 < m whenever m > 1. So the odd values along the stretch decrease strictly while
they exceed 1; they cannot decrease for ever, so one of them is 1. (b) An orbit that reaches 1 continues 1, 2, 1, 2, ...,
whose column is 1010...; the converse is (a). (c) By Terras's bijection a parity word of length k fixes n modulo 2^k,
and when k >= w a residue class modulo 2^k holds at most one n in [1, 2^w). The columns of 1 and 2 alternate for ever,
in the two phases, so for w >= 2 each phase has exactly that one n; at w = 1 the number 2 lies outside [1, 2). $\square$
