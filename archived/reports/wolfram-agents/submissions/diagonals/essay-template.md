---
Template: ComputationalEssay
Name: The left diagonals of rule 30: their periods are unbounded, and the settled band has no long white run
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-23
Description: Partial results for Problem 1 of the Rule 30 Prize about the left diagonals of the pattern, proved in Lean against the official statements: no two adjacent left diagonals are both eventually white, an eventually white one is followed two later by an eventually black one, no single period is eventual for all of them, and inside a band of diagonals that has settled into a common period P no white run is longer than 2P - 1
Abstract: The kit proves that every left diagonal D j t = cell t (j - t) of the rule 30 pattern is eventually periodic with period dividing 2^j (Rule30Diagonals.D_periodic). This essay adds the other direction and the structure beside it, as a partial result for Problem 1. Lemma B1: no two adjacent left diagonals are both eventually white, and an eventually white diagonal is followed two later by an eventually black one (Rule30Submission.seed_no_adjacent_white, seed_white_then_black). Lemma B2: no period P ≥ 1 is an eventual period of every left diagonal, so the eventual periods are unbounded, and among the first 4^P + 2 diagonals one does not have eventual period P (seed_periods_unbounded, seed_periods_unbounded_quant); hence infinitely many diagonals are eventually white and infinitely many eventually black. Lemma B3: if the diagonals 0 to M have had a common period P for P steps, no white run of the row inside them, bounded on the left by a black diagonal, is longer than 2P - 1 (lemma_B3_sharp). All hold for every configuration with a leftmost black cell. The unboundedness is Rowland's (2006); the proofs, the quantitative form and Lemmas B1 and B3 are the record's. The verifier's replay accepts the module with the three standard axioms only. Nothing here decides Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, left diagonals, eventual period, Rowland, period doubling, left-permutive, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entries 8, 9 and 12](https://github.com/ghywel/placego/blob/main/PROOFS.md)", "[E. Rowland, Local Nested Structure in Rule 30, Complex Systems 16 (2006)](https://www.complex-systems.com/abstracts/v16_i03_a03/)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261022-c27323, the white end](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-c27323)"]
---

## The question

Rule 30 updates every cell from itself and its two neighbors: the new color is *left* XOR (*center* OR *right*). From a single black cell it grows a pattern whose center column looks random. Problem 1 of the Rule 30 Prize asks whether that column is ever eventually periodic.

The pattern's left edge is regular: along the diagonals parallel to it the colors settle into periods. The `j`-th left diagonal is `D j t = cell t (j - t)`, the cell `j` places right of the moving left edge. The first 60 steps, with diagonals 0, 4 and 8 marked:

```wl
pattern = CellularAutomaton[30, {{1}, 0}, 60];
marks = Table[{t + 1, j - t + 61}, {t, 0, 60}, {j, {0, 4, 8}}] // Flatten[#, 1] &;
ArrayPlot[ReplacePart[pattern, Thread[marks -> 2]], ColorRules -> {0 -> White, 1 -> GrayLevel[0.15], 2 -> StandardRed}, ImageSize -> 520]
```

The kit's catalog proves that every left diagonal is eventually periodic with period dividing `2^j` (`Rule30Diagonals.D_periodic`; `Rule30FiniteDiagonals.Ld_periodic` for any configuration with a leftmost black cell). The center column is the diagonal of diagonals, `center t = D t t`, but the period bound `2^j` exceeds `j`, so, as the kit says, that theorem says nothing about the center column by itself. This essay proves what the diagonals do beyond that bound: their periods really grow without limit, their colors alternate in a forced pattern, and the band of diagonals that has settled cannot contain a long white run.

## The diagonals, measured

The left diagonals from the first 12,000 rows, and for each the least eventual period found and the color it settles into. `?` marks a period not settled within the sample:

```wl
rowsT = 12000;
rows = CellularAutomaton[30, {{1}, 0}, rowsT];
diag[j_] := Table[rows[[t + 1, j - t + rowsT + 1]], {t, j, rowsT}];
leastPeriod[s_] := Module[{n = Length[s]}, SelectFirst[Range[1, 4096], Function[p, s[[Floor[n/2] ;; n - p]] === s[[Floor[n/2] + p ;; n]]], "?"]];
colour[s_] := With[{tail = s[[-2000 ;;]]}, Which[Max[tail] == 0, "white", Min[tail] == 1, "black", True, "mixed"]];
Grid[Prepend[Table[{j, leastPeriod[diag[j]], colour[diag[j]]}, {j, 0, 12}], {"j", "least eventual period (sample)", "eventually"}], Frame -> All]
```

The periods are powers of two and they double, as Rowland proved; between the doublings sit eventually white and eventually black diagonals, and the white ones never come in adjacent pairs. The theorems below say why, for every `j`, with no sample.

## The idea of the proofs

Write `D j` for the `j`-th left diagonal of a configuration with a leftmost black cell. Rule 30 is left-permutive, and read along diagonals the rule becomes a recurrence that feeds each diagonal from the two before it: `D (j+2) (t+1) = D j t XOR (D (j+1) t OR D (j+2) t)`. Diagonal 0 is the edge, black for ever; diagonal 1 is black from time 1; diagonal 2 is white from time 2.

**Lemma B1.** If `D j` and `D (j+1)` were both eventually white, the recurrence would make `D (j+2)` eventually constant and then, going back up the recurrence, force a contradiction at the edge; and an eventually white `D j` makes `D (j+2)` eventually black because the XOR with a white input leaves the OR, which a black cell keeps black.

**Lemma B2.** Suppose every left diagonal had eventual period `P`. Take a time after which the diagonals `0` to `4^P + 1` are all periodic. The `4^P + 1` windows of two adjacent diagonals over one period take at most `4^P` values, so two windows agree at `k₁ < k₂`, and periodicity extends the agreement to all later times. Left-permutivity then propagates the agreement leftward, diagonal by diagonal, down to the edge: diagonal `k₂ - k₁` would agree with diagonal 0, which is black for ever, so `D (k₂ - k₁)` is eventually black, and the next one down, `D (k₂ - k₁ - 1)`, agrees with `D (-1)`, which is white: it is eventually white, and Lemma B1's "white then black" climbs back up to a contradiction with the recurrence at the top of the window. The period `P` is therefore not shared by all diagonals: the eventual periods are unbounded. The quantitative form keeps the bound `4^P + 1`.

**Lemma B3.** If the diagonals `0 … M` have had a common period `P` for `P` steps, look at a white run of the row at time `t` inside them, bounded on the left by a black diagonal `g`. One step back, the run is either older, white two cells wider with its black bound two further left, or newborn, black on `[g - 1, M' - 2]`. Following it back `P` steps, the run's left end has moved `2P` cells left of `g`, while the periodicity says the row at `t - P` agrees with the row at `t`, which is black at `g`: so the run at time `t` is shorter than `2P`. The sharp bound is `2P - 1`.

Everything in this section is prose. The proofs are the next section.

## The formal proof

The module, as the verifier rebuilds and checks it: the diagonals `D x0 e j t = evol x0 t (e - t + j)` on the kit's `evol` (they are the kit's `Rule30FiniteDiagonals.Ld` and, for the seed, `Rule30Diagonals.D`), the recurrence `D_succ`, the edge lemma, the forced-periodicity transducer lemmas, `jen_pow2` (the period `2^j`), `lemma_B3_sharp`, `lemma_B2_quant`, `lemma_B2`, `infinitely_many_white`, `no_adjacent_white`, `white_then_black`, `infinitely_many_black`, and the bridge lemmas that restate the seed's cases in the kit's `Rule30Diagonals.D`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["@@LEAN_SOURCE@@", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorems, as Lean prints them, in the kit's own `Rule30Diagonals.D`. Lemma B1, no two adjacent left diagonals of the seed are both eventually white, and white is followed two later by black:

```wl
opens = {"Ruliology.CellularAutomata.Rule30Diagonals", "Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
{rule30Submission["Rule30Submission.seed_no_adjacent_white"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.seed_white_then_black"]["TypeForm", "Open" -> opens]}
```

Lemma B2, no single period is eventual for every left diagonal, and the quantitative form:

```wl
thm = rule30Submission["Rule30Submission.seed_periods_unbounded"];
{thm["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.seed_periods_unbounded_quant"]["TypeForm", "Open" -> opens]}
```

Its corollary, infinitely many eventually white and infinitely many eventually black diagonals:

```wl
{rule30Submission["Rule30Submission.seed_infinitely_many_white"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.seed_infinitely_many_black"]["TypeForm", "Open" -> opens]}
```

The general statements, for every configuration with a leftmost black cell `e` (`D x0 e j t` is its `j`-th left diagonal): Lemma B2 and Lemma B3:

```wl
{rule30Submission["Rule30Submission.lemma_B2"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.lemma_B3_sharp"]["TypeForm", "Open" -> opens]}
```

The axioms of the headline are the three standard ones and nothing else:

```wl
thm["Axioms"]
```

The proof's structure, one level down from Lemma B2:

```wl
thm["CallGraph", "Depth" -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## What is not proved

- Nothing about the center column directly: the period of diagonal `j` is a power of two above `j`, so the center cell `D t t` is read from a diagonal that has not settled yet. The kit's own remark stands.
- Lemma B2 gives unboundedness and the bound `4^P + 1` on the index of a non-`P`-periodic diagonal; it does not give the exact doubling schedule, which the sample shows and Rowland describes.
- These are partial results about the pattern's left side, not a solution of Problem 1, and nothing about Problems 2 and 3.

## Provenance

Lemmas B1, B2 and B3 are RULE30-PRIZE.md section 8.59 and PROOFS.md entries 8, 9 and 12 of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT: proved by Local (Claude) on 2026-10-05, second-read by Cloud (Claude) and GPT, and machine-checked by Local in Lean on 2026-10-10; Cloud restated them on the kit's definitions and added the bridge to `Rule30Diagonals.D` on 2026-10-23. The unboundedness of the left diagonals' periods is Rowland's theorem (2006); the kit cites it without a formal statement. The mechanism of the proofs is Jen's left-permutivity (1986).

## References

[1] E. Jen, *Global properties of cellular automata*, Journal of Statistical Physics 43 (1986) 219–242.

[2] E. Rowland, *Local Nested Structure in Rule 30*, Complex Systems 16 (2006) 239–258.

[3] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[4] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[5] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): PROOFS.md entries 8, 9 and 12 and `tests/probes/lean/JenPow2.lean`, 2026.
