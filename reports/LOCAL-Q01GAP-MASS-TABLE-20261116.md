# The exact mass table of the Q01Gap language, to popcount 90

Local, L1675, 16 November 2026, at the owner's word ("Yes, run it"). It follows
[the 16 November portal update](LOCAL-PORTAL-KIT-UPDATE-20261116.md), section 2.1, and
[the frontier report](LOCAL-Q01CORE-FRONTIER-20261114.md) (L1673).

**Status.**
- The remark in section 2 is a hand argument of two lines: PROOF-SKETCH, Local.
- The tables are COMPUTED: exhaustive enumeration with exact integers, replayed in Wolfram by different code at
  the sizes section 7 names.
- The comparisons with a branching random walk are MEASURED.
- Nothing here proves `MassDiverges` or `Q01Gap`. The kit's rung is known (Emerson Villafuerte, Codex and
  Antigravity, R30-20261115-fdf6a3, Lean); it is reproduced here and shown to be sharp.

## 1. Summary

1. **The kit's rung is reproduced exactly and is sharp.**
   - The least popcount of a seed surviving 102 ticks is 38, and the survivors of popcount 38 are exactly the
     submission's eight seeds.
   - `NoMass 37 H` first holds at H = 102 and `NoMass 38 H` first holds at H = 111, so both of the
     submission's horizons are the least possible.
2. **The table now runs to popcount 90.** No seed of popcount at most 50, 60, 70, 80, 90 survives to tick
   148, 182, 212, 244, 278, and each of these horizons is the least. The submission had the rung at 37 and 38.
3. **The law behind the table is statistical.**
   - Over all accepted traces the row bits are fair coins: the popcount of an H-bit prefix has mean 0.5005·H and
     variance 0.256·H.
   - The least popcount sits where a branching random walk of fair coins would put it: 3 to 8 above the
     first-moment line, growing at 0.307 per tick.
   - Extrapolating that law from H ≤ 162 predicts the horizons at M = 60 to 90 to within 2.2%.
4. **No structured family of sparse rows appears to H = 277.** For the larger G language the kit's
   `sharp_86` family beats the coins. Here nothing does.
5. **Support and popcount pick different rows.** At H = 162 the sparsest prefixes have full support (161 or
   162), and the shortest prefixes (support 142) have popcount 78 or more, against the least popcount 55.
6. **Consequence.** `MassDiverges` holds on all the data at a linear rate, about three ticks per unit of mass. A
   proof would need an exact large-deviation bound for the popcount over the language. That is a weighted count
   over all words, not a single-orbit statement, and it is the form in which this conjecture looks most like the
   Mahler lemma of L1670.

## 2. The objects and one remark

All definitions are from kit main `8b397bde`, module `Rule30ZeroCoastBridge`.
- **Seeds.** A seed y is a left row read as an integer (bit i is depth i + 1), and F y = (y >> 1) xor
  (y or (y << 1)).
- **`SurvivesTo y H`.** The depth-1 trace of y at ticks 0 to H − 1 is white at tick 0, black at odd ticks, and
  at even ticks follows the gap clock: a white cell is allowed 6 ticks after the last one and forced after 10.
  These are the gaps 3 and 5 of `Q01Gap`, read from a white time.
- **`NoMass M H`.** No y of popcount at most M survives to H. `MassDiverges` says every M has such an H, and
  `massDiverges_iff_Q01Gap` proves it equivalent to `Q01Gap`.

**Remark.** Depth 1 at tick t depends on depths 1 to t + 1, so `SurvivesTo y H` reads only bits 0 to H − 1 of y.
Hence `NoMass M H` holds exactly when M < μ(H), where μ(H) is the least popcount of an H-bit prefix whose trace is
accepted for H ticks. μ is non-decreasing, and `Q01Gap` says that μ is unbounded. The whole mass table is the
function μ, and a depth-first search over accepted traces, cut off when the popcount passes M, computes it
exactly up to the horizon of M.

## 3. The kit's rung (known; reproduced and sharpened)

- **The count.** At H = 102 there are 6,654 accepted prefixes. The least popcount is 38, and exactly eight
  prefixes have it.
- **The seeds.** As a set they are the submission's `c37Roots`. Their bit lengths are 95 to 102.
- **Their survival as finite seeds.** They survive to 102, 102, 102, 103, 103, 103, 107 and 110 ticks. The last
  is the submission's y* = 343533199256979670105602359638.
- **Sharpness (COMPUTED).** A prefix of popcount 37 survives to 101, and y* survives to 110. So 102 and 111 are
  the least horizons for M = 37 and M = 38.

## 4. The table (COMPUTED)

Least H with `NoMass M H`:

| M | 10 | 20 | 30 | 37 | 38 | 40 | 50 | 60 | 70 | 80 | 90 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H | 29 | 50 | 83 | 102 | 111 | 116 | 148 | 182 | 212 | 244 | 278 |
| H/M | 2.90 | 2.50 | 2.77 | 2.76 | 2.92 | 2.90 | 2.96 | 3.03 | 3.03 | 3.05 | 3.09 |

The least popcount μ(H):

| H | 20 | 40 | 60 | 80 | 100 | 120 | 140 | 160 | 180 | 200 | 220 | 240 | 260 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| μ(H) | 7 | 16 | 23 | 29 | 37 | 43 | 49 | 54 | 59 | 67 | 74 | 79 | 85 |

- μ is exact for every H up to 277.
- A least-squares line through the even H from 60 to 276 is μ = 0.3071·H + 5.3.
- The search for M = 90 visited 1.07·10^8 nodes; at its widest, 4,562,344 prefixes of popcount at most 90 were
  alive at one depth.
- A search for M = 100 was not started: the time guard predicted 20 minutes.

## 5. The law (MEASURED on exhaustive counts)

Phase 1 enumerated every accepted trace to H = 162 (1,355,842 of them at the end).

| H | B(H) | mean popcount | variance | μ(H) | first-moment line x1 | μ − x1 |
|---|---|---|---|---|---|---|
| 62 | 195 | 30.91 | 12.05 | 23 | 19.63 | +3.4 |
| 102 | 6,654 | 50.95 | 22.68 | 38 | 30.97 | +7.0 |
| 142 | 230,552 | 70.94 | 33.01 | 49 | 42.39 | +6.6 |
| 162 | 1,355,842 | 80.94 | 37.98 | 55 | 48.19 | +6.8 |

- **Fair coins.** Fits over 80 ≤ H ≤ 162 give mean = 0.5005·H − 0.13 and variance = 0.2563·H − 3.4. The count
  grows as ln B = 0.08860·H, against the language's exact 0.08858.
- **The first-moment line** is x1 = mean − sd·√(2 ln B): the popcount below which the expected number of words
  is about one. Its slope is 0.287. Exactly fair coins with this entropy would give 0.293.
- **The minimum sits above it**, by 3.1 to 7.8 for 60 ≤ H ≤ 162. That is the behaviour of the minimum of a
  branching random walk, whose minimum lies above its first-moment line by a term of order log H, because words
  that share a prefix share its popcount. (The standard theory is Hammersley, Kingman and Biggins for the speed
  and Bramson for the logarithm; cited from memory, not opened.)
- **The lower tail is depleted in the same way.** At H = 162, two words have popcount 55 where a Gaussian with
  the measured mean and variance would have 12.5; then 5 against 24.5, and 7 against 46.5.
- **Out of sample.** I fitted the mean, the variance and ln B by lines over 80 ≤ H ≤ 162, and added the median
  in-sample offset (+6.9). That predicts horizons 180, 215, 249, 284 for M = 60, 70, 80, 90. The exact horizons
  are 182, 212, 244, 278. Without the offset the prediction is 22 to 30 ticks too long.
- **The deep minimisers are not one row.** The deepest survivor of popcount at most 90 (H = 276) has prefixes
  that exceed μ(H) by up to 6, and equal it at 33 of 129 even depths. The number of minimisers stays small:
  1 to 9 at the depths sampled.

## 6. The two coordinates

L1673 measured survival by support in two thinner languages. In this language, at H = 162:
- **Support.** The least support is 142, so the longest white tail is 20. The white-tail counts halve
  (677,783, 338,090, 169,300, 85,050, …), as L1673 found. A seed of support W survives about W/0.87 ticks.
- **Popcount.** The least popcount is 55. A seed of popcount M survives about 3M ticks.
- **Different rows.** The sparsest prefixes have support 161 or 162. The shortest have popcount 78, 81, 82 or
  87.
- **The frontier** (support W: least popcount among prefixes of support at most W) is 142: 78, 146: 65,
  149: 64, 150: 56, 161: 55. At H = 102 it is 89: 50, 93: 49, 94: 41, 95: 38.

So the mass bound is the binding one only for seeds of density below about 0.37. For a typical seed, of
density one half, the support bound is stronger.

## 7. Controls, predictions and receipts

**Controls**, all PASS.
- **C0.** The anti-diagonal recursion inverts 300 random columns.
- **C1.** For 3 ≤ H ≤ 18 the accepted prefixes are exactly the z below 2^H that survive to H under a literal
  simulation of the kit's acceptor.
- **C2.** Forty sampled prefixes of 30 to 100 free steps survive to their H when run forward.
- **C3.** 7μ(H) ≥ H + 4 for H ≤ 90, as the kit's `S_upto_90` requires of a sublanguage of the G words.
- **C4.** The popcount-bounded search reproduces the exhaustive μ(H) at every H ≤ 162.

**Predictions** (L1675 and its first addendum, pushed before the run).

| | Prediction | Outcome |
|---|---|---|
| K1 (0.9) | μ(102) = 38; minimisers = `c37Roots`; none survives to 111; y* survives to 110 | **HELD** |
| K2 (0.65) | 2.4 ≤ H_M/M ≤ 3.3 for 40 ≤ M ≤ the largest completed | **HELD**: 2.82 to 3.14 |
| K3 (0.5) | μ − x1 within −2 to +12 for 60 ≤ H ≤ 162; horizons beyond 162 within 10% of the extrapolation | **HELD**: +3.1 to +7.8; within 2.2% |
| K4 (0.5) | at H = 162, min-popcount prefixes have support ≥ 154; min-support prefixes have popcount ≥ 1.2μ | **HELD**: 161; 78 against 66 |
| K5 (0.6) | white-tail ratios within 0.03 of 1/2; longest white tail 14 to 26 | **HELD**: 0.487 to 0.510; 20 |

All five held. K3's extrapolation needed a definition (which offset), which I fixed in the first addendum
before any output existed.

**Receipts.**
- **Probe:** [`local_q01gap_mass_table.py`](../tests/probes/sepgap/local_q01gap_mass_table.py), SHA256
  `8bb02cf3…`, frozen at `7208b9900` after the predictions (`34b78e1e1`).
- **Run 15:** COMPLETED in 228 s on Local's M5, peak RSS 21 MiB. Caps: CPU 600 s, wall 900 s, RSS 4096 MiB;
  one Python process.
- **Output:** [`local_q01gap_mass_table.out`](../tests/probes/sepgap/local_q01gap_mass_table.out), `1dc3668c…`.
- **Wolfram replay:** [`q01gap_mass_table_replay.wl`](../tests/probes/wolfram/q01gap_mass_table_replay.wl),
  `1ad25c82…`, 31 s. It uses explicit anti-diagonal lists and its own acceptor. Equal to Python:
  - the horizons 102, 111, 148 and 182 for M = 37, 38, 50 and 60;
  - μ(102) = 38 with eight survivors equal to `c37Roots`, and their eight survival lengths;
  - μ(H) at H = 20 to 180;
  - the node counts 63,489 and 407,950, and the largest box 20,411 at M = 60.
- **Python only:** M = 70, 80, 90; the popcount statistics of phase 1; sections 5 and 6.

**Record searched:** as in L1675. Our record had no mass table for the gap language. The kit has Conjecture S
for the G language (`Rule30PeriodTwoMass`) and the single rung of fdf6a3. No novelty is claimed for the
branching-walk reading, which is standard.

## 8. What next

- **A proof target, stated exactly.** `MassDiverges` follows if, for one z below 1, the sum of
  z^popcount(prefix) over the accepted traces of H ticks tends to 0. For fair independent bits that sum is
  (1.0926·(1 + z)/2)^H, which decays for every z below 0.83. So the conjecture is a decay statement for a
  weighted count over a language, like the lemma that settled the Mahler limit in L1670. The difference is that
  there the weight was a character of a linear map. Here the row is a non-linear function of the free bits, and
  I see no toggle that preserves the future.
- **The table as a contribution (the owner's call).** The table extends the submission's rung from 38 to 90.
  A Lean rung at M = 50 needs 63,489 nodes by the submission's own method. Whether to offer the table to its
  author, for example in a comment on kit PR #350, is an outward step I have not taken.
- **The G language.** The kit's author computed its least weight to H = 300 and found a sharp periodic family.
  The same statistics there (mean, variance, the first-moment line) would show how far below the coins that
  family sits. Not run.
