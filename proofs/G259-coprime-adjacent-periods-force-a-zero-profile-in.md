# Coprime adjacent periods force a zero profile in a right tail

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT259. Coprime adjacent periods force
a zero profile in a right tail (second-read, 2026-10-09)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Two neighbouring columns that repeat on unrelated odd and coprime cycles cannot both be alive in Rule 30's right half: one goes blank and the other freezes.

**What it says.** Picture each column of a Rule 30 history as a strip of tape repeating in time. Suppose one column repeats every m steps, with m odd, and its right-hand neighbour repeats every n steps, with n sharing no factor with m. Then the neighbour must be all white, and the first column must never change. The neighbour's black ticks, stepping n at a time, would land on every phase of the first column's cycle, including a phase where the first column cannot accept one.

**Why it matters.** It rules out one way a hypothetical period-310 pattern might be built from smaller pieces: columns repeating every 5 steps cannot sit next to columns repeating every 31. At least every other column must carry the full 155-step cycle.

**An everyday picture.** Two gears with coprime numbers of teeth: a mark on one eventually meets every tooth of the other. If even one tooth cannot take the mark, the mark cannot be there at all.

## The formal statement and proof

*Where:* RULE30-GPT.md GC820. *Credit:* GPT's lemma and consequence. Independently read by Local (chat L441), with an
exhaustive literal check: odd m in {1, 3, 5, 7, 9, 15}, coprime n <= 8, every D and U, using GC798's exact two-equation
projection. 78 admissible pairs, all with U = 0 and D constant. The even-m control D = 01, U = 1 is admissible, as the
lemma's scope says. *Status:* hand proof verified by a second reader. Not a prize claim.
*Filed by:* Local, at GPT's request (GC820). The G number is assigned here at filing; GC820 has no other.

**Lemma.** Let D, U, W, X be consecutive temporal profiles of a G orbit (G(y)(i) = y(i) xor (y(i+1) OR y(i+2))), so
$\Delta D = U \lor W$ and $\Delta U = W \lor X$. If D has an odd period m and U has a period n with gcd(m, n) = 1, then U
is identically 0 and D is constant.

**Proof.**
1. Summed over one period, $\Delta D$ is even. An all-one $\Delta D$ would have m ones, which is odd, so $\Delta D$
   has a zero at some residue r mod m.
2. If U(s) = 1, then U(s + kn) = 1 for every k. These ticks meet every residue mod m, since gcd(n, m) = 1, so one of
   them falls at r. But $U \le \Delta D$ from the first equation, a contradiction. Hence U = 0.
3. Then $\Delta U = 0$ forces W = X = 0, and $\Delta D = U \lor W = 0$ makes D constant. ∎

**Consequence (GC820).** Take the period-310 critical candidate after its rightmost complement (GC769, GC785), where
every profile's period divides 155 and GC760 makes every adjacent joint period 155.
- No profile is constant:
  - a constant profile forces the next two to 0;
  - a 0 to the right of a profile makes it constant;
  - a 1 to the right forces an all-one difference of odd period.
- Two adjacent proper-period profiles could reach joint period 155 only as 5 beside 31. The lemma excludes this in
  either order.
- So every adjacent pair contains a profile of least period 155. Any N consecutive profiles include at least
  floor(N/2) of them, and an eventual spatial cycle of length d includes at least ceil(d/2).
- This says nothing about E parity, black density in time, or whether such a background exists.

*Controls (GC820).*
- Stepping by 31 visits every residue mod 5, and stepping by 5 visits every residue mod 31.
- GC817's genuine q5 tail is not a counterexample: its adjacent periods share the factor 5.

*Near-entry gate (Local, at filing).* `proof_dupes.py --near G259` gives G207 (three boundary beats repeat the
neighbouring bit), 34 (Proposition 21) and C.1 (the checkerboard lemma), with scores of 0.03 or less on the formal
text. Read: none states or uses a coprime-period argument, so none is restated. The hard checks pass (273 entries).
