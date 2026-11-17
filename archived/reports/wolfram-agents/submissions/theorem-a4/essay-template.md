---
Template: ComputationalEssay
Name: A repeat on the center column cannot put its white run inside the settled band of left diagonals
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-23
Description: A partial result for Problem 1 of the Rule 30 Prize, proved in Lean against the official statements: Jen's clocked bound n ≤ a′ for a common block of length n on the center column and its right neighbour at times a < a′ improves to n ≤ a′ - M + 2P - 1 when the left diagonals 0 to M agree at times a′ - P and a′ and M < a′ - a
Abstract: Jen's theorem with a clock, the kit's window_jen_col, bounds a common block of length n on columns 0 and 1 at times a < a′ by n ≤ a′. The reason is a white run: row a′ is white at the distances a + 1 … n - 1 left of the center, which are the left diagonals a′ - n + 1 … a′ - a - 1. This essay proves that the run cannot lie in the band of diagonals that has settled. Theorem A⁗ (Rule30Submission.center_A4_sharp, for the kit's cell and Rule30Diagonals.D; theorem_A4_sharp for every configuration with a leftmost black cell L cells left of the column): if the diagonals 0 … M agree at times a′ - P and a′, with P ≥ 1, P ≤ a′ and M < a′ - a, then n ≤ L + a′ - M + 2P - 1. The tool is Lemma B3 (lemma_B3_sharp): inside such a band a white run bounded on the left by a black diagonal is at most 2P - 1 long, and Theorem A‴'s run has a black diagonal on its left because diagonal 0, the edge, is black. The kit has the clocked bound and the period-2^j bound for each left diagonal but no statement joining them. The verifier's replay accepts the module with the three standard axioms only. Nothing here decides Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, Jen's theorem, left diagonals, settled band, white run, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entries 10, 12 and 13](https://github.com/ghywel/placego/blob/main/PROOFS.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261022-c27323, the white end](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-c27323)"]
---

## The question

Rule 30 updates every cell from itself and its two neighbors: the new color is *left* XOR (*center* OR *right*). From a single black cell it grows a pattern whose center column looks random. Problem 1 of the Rule 30 Prize asks whether that column is ever eventually periodic. A periodic column repeats blocks; so the question is about repeats, and the first thing the kit knows about repeats is Jen's theorem with a clock.

The first 60 steps, with the center column in red:

```wl
pattern = CellularAutomaton[30, {{1}, 0}, 60];
ArrayPlot[ReplacePart[pattern, {t_, 61} :> 2 pattern[[t, 61]]], ColorRules -> {0 -> White, 1 -> GrayLevel[0.15], 2 -> StandardRed}, ImageSize -> 520]
```

**Jen's bound.** Suppose columns 0 and 1 (the center and its right neighbor) carry the same block of `n` values at times `a` and `a′`, `a < a′`. Rule 30 is left-permutive: a cell's left neighbor is determined by the cell's next value and its two right neighbors. So the two rows agree one cell further left per step down the block: the cell `m` to the left agrees at times `a + s` and `a′ + s` whenever `s + m < n`. But the pattern's left edge moves one cell left per step, with white beyond it: at distance `a′` left of the center, row `a′` is black and row `a` is white. Hence `n ≤ a′` (the kit's `Rule30MaskedJen.window_jen_col`; `L` more when the edge starts `L` cells left of the column).

**The white run.** The same argument says more: row `a′` is white at every distance `a + 1 … n - 1` left of the center (it agrees with row `a` there, which is beyond row `a`'s edge). In the coordinates of the left diagonals, `D k t = cell t (k - t)`, these cells are the diagonals `a′ - n + 1 … a′ - a - 1` at time `a′`. A long repeat is a long white run near the left edge. This essay shows that the run cannot sit inside the band of diagonals that has settled into a period.

## The repeats and the band, measured

Columns 0 and 1 for 400 steps, and the longest common blocks `{n, a, a′}` of the pair:

```wl
steps = 400;
rows = CellularAutomaton[30, {{1}, 0}, steps];
cell[t_, p_] := rows[[t + 1, steps + 1 + p]];
c0 = Table[cell[t, 0], {t, 0, steps}]; c1 = Table[cell[t, 1], {t, 0, steps}];
block[a_, a2_] := Module[{n = 0}, While[a2 + n <= steps && c0[[a + n + 1]] == c0[[a2 + n + 1]] && c1[[a + n + 1]] == c1[[a2 + n + 1]], n++]; n];
blocks = Reverse[Sort[Flatten[Table[{block[a, a2], a, a2}, {a2, 1, steps}, {a, 0, a2 - 1}], 1]]];
Take[blocks, 8]
```

The settled band: `settled[P, t]` is the largest `M` such that the diagonals `0 … M` agree at times `t - P` and `t` (so `-1` if diagonal 0 does not; it always does, the edge is black). The kit proves that diagonal `k` is eventually periodic with period dividing `2^k`; the measured periods grow slowly, so for small `P` the band has a fixed width and for `P = 8` it covers most of the row (the test is agreement of two rows, not eventual periodicity, so the `P = 16` band comes out narrower than the `P = 8` one):

```wl
diag[k_, t_] := cell[t, k - t];
settled[P_, t_] := Module[{m = -1}, While[m + 1 <= t && diag[m + 1, t - P] == diag[m + 1, t], m++]; m];
Grid[Prepend[Table[Prepend[Table[settled[P, t], {P, {1, 2, 4, 8, 16}}], t], {t, {100, 200, 400}}], {"t, P", 1, 2, 4, 8, 16}], Frame -> All]
```

Theorem A⁗'s bound for the six longest blocks and `P = 1, 2, 4` (the hypothesis `M < a′ - a` holds for these), against Jen's bound `a′`:

```wl
Grid[Prepend[Flatten[Table[With[{n = b[[1]], a = b[[2]], a2 = b[[3]], M = settled[P, b[[3]]]}, If[P <= a2 && M < a2 - a, {{b, P, M, a2 - M + 2 P - 1, a2, n <= a2 - M + 2 P - 1}}, {}]], {b, Take[blocks, 6]}, {P, {1, 2, 4}}], 2], {"{n, a, a′}", "P", "M = settled[P, a′]", "bound a′ - M + 2P - 1", "Jen's bound a′", "holds"}], Frame -> All]
```

Both bounds are far above the blocks actually seen (`n ≤ 12` here): the theorem is structural, about where a repeat's white run can be, not a tight count. Its content is the gain `M - 2P + 1` over Jen: the band of settled diagonals pushes the run out, up to a margin of `2P - 1`.

## The idea of the proof

Write `D k t` for the `k`-th left diagonal at time `t` (the cell `k` places right of the moving edge, so `D 0 t` is the edge, black for ever, and `D k t` is white for `k < 0`).

**Lemma B3 (sharp).** Suppose the diagonals `0 … M` agree at times `t - P` and `t`, and at time `t` the diagonals `g + 1 … M′` are white with `g` black and `M′ ≤ M`. One step back, the run is either older (white two cells wider, its black bound two further left) or newborn (black on `g - 1 … M′ - 2`, and black at `M′ - 1` or `M′`). Following it back `P` steps: if it was older all the way, its black bound has moved to `g - 2P`, and the run at time `t - P` covers `g`, which is black at time `t`, against the agreement; so a birth happened at some step `s0 < P`. Going forward from the birth, a white run only loses cells, two a step from its left, so the white cells of time `t - P` (the same as at time `t`, by the agreement) reach the birth time still covering `M′ - 1` and `M′`, one of which is black there. Hence `M′ - g ≤ 2P - 1`.

**Theorem A⁗.** The white run of the repeat, at time `a′`, is the diagonals `L + a′ - n + 1 … a′ - a - 1`, which contain `L + a′ - n + 1 … M` when `M < a′ - a`. Diagonal 0 is black, so the run has a nearest black diagonal `g` on its left, `g ≤ L + a′ - n`. Lemma B3 bounds the run `g + 1 … M` by `2P - 1`, so `M - (L + a′ - n) ≤ 2P - 1`, which is the claim.

Everything in this section is prose. The proof is the next section.

## The formal proof

The module, as the verifier rebuilds and checks it. `edge` is the moving left edge on the kit's `evol`; `step_inv` is left-permutivity read right to left; `agree` propagates a common block leftward; `theorem_A'` and `theorem_A3_white` are Jen's bound and the white run; `D`, `D_succ`, `constraint`, `back`, `fwd` and `lemma_B3_sharp` are the band argument; `theorem_A4_sharp` assembles them; `D_seed`, `D_seed_neg` and `per_seed` bridge the module's diagonals to the kit's `Rule30Diagonals.D` for the single seed, and `center_A4_sharp` is the headline on the kit's `cell`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["@@LEAN_SOURCE@@", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorem, as Lean prints it: for the center column, with the kit's `cell` and `Rule30Diagonals.D`:

```wl
opens = {"Ruliology.CellularAutomata.Rule30Jen", "Ruliology.CellularAutomata.Rule30Diagonals", "Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.center_A4_sharp"];
thm["TypeForm", "Open" -> opens]
```

The general form, for every configuration with a leftmost black cell `L` cells left of column `i`; the module's `D x0 e k t = evol x0 t (e - t + k)` is the `k`-th left diagonal from the edge `e`:

```wl
rule30Submission["Rule30Submission.theorem_A4_sharp"]["TypeForm", "Open" -> opens]
```

The two ingredients, Lemma B3 in its sharp form and Theorem A‴'s corollary (a black diagonal `b < a′ - a` at time `a′` bounds the block by `L + a′ - b`):

```wl
{rule30Submission["Rule30Submission.lemma_B3_sharp"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.theorem_A3"]["TypeForm", "Open" -> opens]}
```

The axioms of the headline are the three standard ones and nothing else:

```wl
thm["Axioms"]
```

The proof's structure, one level down from the headline:

```wl
thm["CallGraph", "Depth" -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## What is not proved

- The hypothesis `hper` (the diagonals `0 … M` agree at `a′ - P` and `a′`) is not known to hold for the repeats of the center column with `M` large and `P` small together: the diagonals the run reaches have periods up to `2^(a′ - a)`, far above `a′ - a`. The theorem says where a repeat's run cannot be; it does not exclude any period.
- The bound `n ≤ a′ - M + 2P - 1` is far from the observed block lengths, as the table shows; it is a structural statement, not an estimate of repeats.
- This is a partial result about the pattern's left side. It does not touch Problems 2 and 3.

## Provenance

Theorem A‴, Lemma B3 and Theorem A⁗ are RULE30-PRIZE.md section 8.59 and PROOFS.md entries 10, 12 and 13 of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT: proved by Local (Claude) on 2026-10-05 and 2026-10-06, second-read by Cloud (Claude) and GPT, and machine-checked by Local in Lean on 2026-10-10 (`tests/probes/lean/TheoremA4.lean`); Cloud restated them on the kit's definitions and added the bridge to `cell` and `Rule30Diagonals.D` on 2026-10-23. The mechanism is Jen's left-permutivity (1986), as the kit's `window_jen_col` uses it. The companion submission on the band itself (Lemmas B1 and B2, the unbounded periods) is filed separately.

## References

[1] E. Jen, *Global properties of cellular automata*, Journal of Statistical Physics 43 (1986) 219–242.

[2] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[3] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[4] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): PROOFS.md entries 10, 12 and 13 and `tests/probes/lean/TheoremA4.lean`, 2026.
