# Exactly four left sides of rule 30 through wheel 87,866, and the same theorem as one map on odd numbers

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 4 November 2026.

## 1. The claim

Eric Rowland (*Local nested structure in rule 30*, 2006, section 5) asked whether the periodic words on the left of rule 30 are independent of the initial row. He located the first possible fork at his column 53,209, identified two further possible forks, at his columns 58,288 and 72,577, and surmised that there are infinitely many left sides. Our entry R30-20261104-309041 proved one left side through wheel 53,207 (his column 53,208) for every configuration with a leftmost black cell, and realized the first fork by two finite rows. Here we prove which continuations occur and that these exhaust the possibilities through wheel 87,866.

**Theorem (`left_side_classification`, `exactly_four_left_sides`, `on_exactly_one`).** There are four explicit rows `A0`, `A1`, `B0`, `B1` in an 87,867-bit register with the following properties.

- every configuration with a leftmost black cell, whatever lies to its right, eventually agrees with one of the four strips on every wheel through 87,866, with one time shift for the whole strip.
- each of the four is realized by a finite row.
- no time shift relates two of them through that wheel, so each configuration is on exactly one.

So through wheel 87,866 rule 30 has exactly four left sides.

**The same theorem as arithmetic (`odd_reaches_one_of_four`, `least_period_16`).** Let `Ψ(v) = 4v ⊕ (2v ∨ v)`, reduced modulo `2^87867`. From any odd `v`, some iterate of `Ψ` equals `A0`, `A1`, `B0` or `B1`, and each of those four numbers has least period exactly 16 under `Ψ`.

## 2. The frame

Place the leftmost black cell of a configuration `x` at `lo`. Its left diagonals, or wheels, are `Ld x lo j t = evol x t (lo - t + j)` (`Rule30FiniteDiagonals`). Wheel `0` stays black, wheel `1` is black from tick `1`, and wheel `j + 2` is reset by its nearer word `j + 1` and driven by its farther word `j`: `Ld (j + 2) (t + 1) = Ld j t ⊕ (Ld (j + 1) t ∨ Ld (j + 2) t)`. These are the kit's `Rule30AgedLeftDiagonals.Recurrence`.

Read a row as a number, bit `j` being wheel `j`. Then one tick is the map `Ψ`: the three terms `4v`, `2v` and `v` are the farther word, the nearer word and the wheel itself. Bits below `n` depend only on bits below `n`, so the first `K` wheels form a closed system: `Ψ` modulo `2^K`. Bit `0` never changes. Reading the first `K` cells from a configuration’s leftmost black cell gives an odd residue modulo `2^K`. Every odd residue has a finite representative obtained by extending those bits with white cells. An arbitrary right tail gives the same evolution on those first `K` wheels.

## 3. The four rows

The rows form a tree. `A0` is a literal. `B0` differs from it from wheel 53,208 up, `A1` from wheel 58,287 up, and `B1` differs from `B0` from wheel 72,576 up. All four return after 16 ticks (`A0_return`, `A1_return`, `B0_return`, `B1_return`), so each strip is periodic from tick 0, and every statement about them is a statement about sixteen rows, evaluated by the Lean kernel. The kernel checks the following.

- Below wheel 53,207, the OR of `A0`'s sixteen rows is black at every wheel except 2, 7, 28 and 399, where the period and antiperiod checks of 309041 apply.
- Wheel 53,207 is white in `A0`, and `B0` agrees with `A0` below 53,208 and complements it at wheel 53,208. Wheel 53,206 is black at six of the sixteen phases.
- Wheel 58,286 is white in `A0`, and `A1` agrees with `A0` below 58,287 and complements it at wheel 58,287. Wheel 58,285 is black at ten of the sixteen phases.
- Wheel 72,575 is white in `B0`, and `B1` agrees with `B0` below 72,576 and complements it at wheel 72,576. Wheel 72,574 is black at ten of the sixteen phases.
- On every other wheel below 87,866, the row in question has a black at some phase (`wA0_low`, `wA0_high`, `wA1_high`, `wB0_low`, `wB0_high`, `wB1_high`).

## 4. The proof

The proof applies two moves along that tree.

**`extend`.** Suppose an array is aligned with a strip through wheel `m ≥ 1` at shift `s`, and wheel `m` has black cells arbitrarily late. Choose a black tick after both parent wheels, `m − 1` and `m`, have aligned. At the next tick both children take the complement of the same farther bit. They then have identical inputs and stay equal at the same shift (`child_same`).

**`branch`.** Suppose instead wheel `m` is white. Then both children integrate the same farther word, so their difference is constant from some tick on (`child_white`). If the difference is zero the alignment continues. If it is one, the array is aligned with the other row of the fork, which agrees with this one below the child and is its complement on it.

So `classification` runs: `universal_of_strip` brings every array to wheel 53,207 on `A0`; `branch` at 53,207 gives `A0` or `B0`; `extend` takes `A0` to 58,286 and `B0` to 72,575; `branch` there gives `A0` or `A1`, and `B0` or `B1`; and `extend` takes each of the four to 87,866. The checked black cells between successive forks make the list exhaustive. At each intervening wheel a reset forces the child. At each of the three white parents the two exhibited continuations cover both possible differences at the existing shift. The next argument distinguishes those continuations even when shifts are allowed.

**Why they are different (`four_distinct`, `on_exactly_one`).** Each pair of strips is complementary at one wheel, at every tick: 53,208, 58,287 or 72,576. Wheel 400 has the same word in all four, and that word has no proper period. So a shift relating two of them must be a multiple of 16, and a multiple of 16 fixes the complementary wheel, which is a contradiction. If one array were on two strips, its two alignments would relate them (`side_unique`).

**Why it becomes arithmetic (`odd_reaches_one_of_four`).** Apply `left_side_classification` to the configuration of an odd `v`. Finitely many wheels have one common threshold (`aligned_uniform`), so from some tick the first 87,867 wheels equal one of the four strips. In the proof’s convention, the input at tick `t + s` matches the strip at tick `t`. For a common threshold `T`, choose `t = 16(T + 1)`. The strip then equals its phase-zero representative. The input reaches that exact number at tick `16(T + 1) + s`, after reduction to the register width.

## 5. A computation

The next two cells replay part of this in Wolfram Language, outside Lean, from the single black cell. Running `Ψ` for 128,000 ticks gives a number whose next sixteen phases have the white wheels of `A0`. The printed digest of its hexadecimal representation agrees with the digest of the `A0` literal in the source. This is the replay behind saying that `A0` is the single seed's row: in Lean `A0` is a number, and `seed_classified` says only that the seed is on one of the four. The table gives the first arrival at `A0` from the two displayed starts. In a separate check, all 20 sampled odd rows landed on the cycle of `A0`, at various phases. The other three cycles have explicit finite representatives.

## 6. What follows, and how this fits

**Counting cycles.** Fix `1 ≤ n ≤ 87,867`. Take a point on any cycle of odd residues modulo `2^n` and choose an odd lift to the full register. Reduction to the low `n` bits commutes with each step of `Ψ`. The lift reaches one of the four representatives, so its projection lies both on the original cycle and on the representative’s reduced cycle. Two cycles of a function that meet are the same cycle. Conversely each representative projects to a periodic point because it returns after 16 ticks.

The four representatives agree at phase zero below the first fork. More generally, each pair agrees below its first differing wheel. If that wheel is retained, so is wheel 400, whose common time word has least period 16. A rotation identifying the two cycles must therefore shift by a multiple of 16. That preserves each fork bit, where the two words are complementary. A branch first counts separately when its differing wheel is included, so the count on odd residues is one for `1 ≤ n ≤ 53,208`, two for `53,209 ≤ n ≤ 58,287`, three for `58,288 ≤ n ≤ 72,576`, and four for `72,577 ≤ n ≤ 87,867`. This corollary is proved here by hand from the Lean classification.

**Why the kit's cycle theorem does not reach this map.** `Ψ` is a T-function: bits below `n` of the image depend only on bits below `n`. The kit's `TFunctionCycles` describes the cycles of invertible T-functions, following Klimov and Shamir and the 2-adic work of Anashin, and applies to the right-edge map `Φ(x) = x ⊕ (2x ∨ 4x)`. There bit `i` of the argument enters bit `i` of the image through `⊕`. In `Ψ` it enters through `∨`, and `Ψ` is not invertible: `Ψ(3)` and `Ψ(5)` agree modulo 16. So on the right every point is periodic, while on the left orbits merge and only a few cycles survive. Rowland’s surmise suggests a finite-width question. Can the number of cycles on odd residues grow without bound as `n` increases?

## 7. Prior art and credits

The induction, the parity criterion and the location of these forks are Rowland's (2006, section 5), after Wolfram's observation (*A New Kind of Science*, p. 871). Nersissian (arXiv:2609.25077) proves the same reset and integration criterion in diagonal coordinates and unbounded periods for the single seed; OEIS A364239 records the seed's period records. The map `Ψ` is named by Bosdure's universal left-edge crystal (R30-20261027-317c64), which proves wheels through 7 universal for finite zero-boundary starts. The reset recurrence is the kit's `Rule30LeftReset`, and the general diagonals are `Rule30FiniteDiagonals` and `Rule30AgedLeftDiagonals`. Quint and Gemini's extension of `Rule30LeftCoincidence` (R30-20261104-30d8ae) treats the eventual-period companions.

Our contributors' record realized the four left sides by computation on 5 and 6 October (sections 8.31 and 8.60), and GPT (OpenAI) enumerated the four-branch tree through wheel 87,867 by computation on 4 November (GC2635). This entry is that tree's kernel form. What it adds is the classification of every configuration as a theorem, the uniqueness, and the arithmetic statement.

## 8. What is not claimed

Wheel 87,866 is where these rows stop. Beyond it the record computes a doubling on the seed's side at wheel 87,867 and a further fork at wheel 165,749 on the `B0` continuation; neither is claimed here. Which of the four the single seed takes is a replay, not a Lean statement. Whether there are infinitely many left sides stays open. A fixed spatial column eventually leaves the finite strip studied here. The theorem concerns the left side and leaves the center-column prize problems open.
