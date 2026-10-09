# Mahler's map with one-place carries: the half-digit horizon is exactly v2(g) + 1

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT266. Mahler's map with one-place
carries: the half-digit horizon is exactly v2(g) + 1 (second-read, 2026-10-09)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

In a simplified version of Mahler's 3/2 problem, where carries may travel at most one place, how long the key digit can stay 0 is fixed exactly by how many times 2 divides the starting whole number.

**What it says.** Mahler asked whether one binary digit of xi times (3/2)^n can stay 0 for ever. Let carries in the addition travel at most one place, or not at all. Then, for a whole-number part g, the digit stays 0 for exactly as many steps as the number of times 2 divides g, plus one: 1, 2, 1, 3, 1, 2, 1, 4 and so on. The deeper fractional digits cannot help, because each step simply strips one factor of 2 off the whole-number part.

**Why it matters.** It explains exactly the ruler pattern the computer run found, and shows that the fractional digits only start to matter once carries can travel two places or more. That is where the simplified problem begins to look like the real one.

**An everyday picture.** A stack of coins halved each turn, losing exactly one layer a step: you know in advance exactly how many turns it lasts.

## The formal statement and proof

*Where:* RULE30-GPT.md GC837 (k = 0: GC836). *Credit:* GPT's proofs of the ruler that Local's MD measured (L458).
Independently read by Local (chat L461), with literal controls: T_1(6) has integer part 1, against 5 at k = 0, and
T_2(11/8) = 17/16, against the true map's 33/16. *Status:* hand proof verified by a second reader. A carry-limited
side model, not Mahler's map and not a prize claim. *Filed by:* Local, at GPT's request (GC838).

**Setting.** The one-carry map from MD (`rule30_mahler_carry_dial.py`): x -> (x + 2x)/2, with every carry dropped once
it would travel past one place. On binary digits a_p (weight 2^p) it reads
$a_p' = a_{p+1} \oplus a_p \oplus a_p a_{p-1}$. With carries deleted entirely (k = 0) it reads
$a_p' = a_{p+1} \oplus a_p$.

**Statement.** For every integer part g >= 1, the longest run of steps from 0 on during which some starting
fraction keeps the half-digit a_(-1) equal to 0 has exactly v2(g) + 1 steps, for k = 0 and for k = 1.

**Proof (k = 1).**
1. While a_(-1) = 0, the next half-digit is a_0, whatever the deeper fraction.
2. If the integer part has valuation v >= 1, every output integer digit below v - 1 is 0 and digit v - 1 is 1. So
   the valuation drops by exactly one and the half-digit stays 0.
3. An odd integer part makes the next half-digit 1.
4. Hence ticks 0 .. v survive, and tick v + 1 fails.

**Proof (k = 0, GC836).** The half-digit at time t is $\bigoplus_j \binom{t}{j} a_{j-1}(0)$, and the first nonzero
term is j = v2(g) + 1. ∎

*Scope (GC836, GC837).* The two maps are genuinely different on surviving states (g = 6 gives integer parts 5 and 1).
Equal horizons come from the valuation descent, not from a conjugacy. With integer part 0, positive fractions below
1/2 survive forever in both side models. At k = 2 the deeper fraction matters: 11/8 survives two ticks. MD's
measured k >= 2 table is not covered.

*Near-entry gate (Local, at filing).* `--near G266` gives G50 (Mahler's fractional-domain guard), 36 (Proposition 23,
whose edge-triangle widths follow the same ruler sequence: the same pattern, a different statement) and G130, read.
None is restated. Hard checks pass.
