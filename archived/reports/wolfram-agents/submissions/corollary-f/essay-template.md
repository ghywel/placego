---
Template: ComputationalEssay
Name: Under a period-2 center column, a right neighbour that starts with near-squares has no left edge
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-23
Description: A partial result for Problem 1 of the Rule 30 Prize in the period-2 case, proved in Lean against the official statements: if column 0 reads the clock 0101… from some time on and the configuration has a leftmost black cell, then the even-time bits of column 1 cannot form near-squares at unbounded scales; period-doubling, Chacon and every substitution fixed point beginning with a double letter are excluded as the right neighbour of a period-2 center column
Abstract: Problem 1 asks whether the center column of rule 30 is ever eventually periodic; the first open case is period 2, the clock 0101…. Under that clock rule 30's left-permutivity determines column -1 from column 1, black at odd times and the complement of column 1 at even times; call column 1 at even times the visible bits. This essay proves Corollary F (Rule30Submission.corollary_F): a configuration with a leftmost black cell, whose column 0 reads the clock from some time T0, has no near-squares at unbounded scales in its visible bits, meaning no constant K and pairs i < i′ with i′ - i unbounded whose common future lasts i′ - K steps. The proof joins two facts the record proved for every configuration with a leftmost black cell: Lemma B2 (infinitely many left diagonals are eventually black, Rule30Submission.infinitely_many_black) and Theorem A‴ (a black diagonal sharpens Jen's clocked bound on a common block of two adjacent columns, Rule30Submission.theorem_A3). The visible agreement makes columns -1 and 0 carry a block of length 2(i′ - K); an eventually black diagonal b ≥ L + 2K bounds it by 2i′ - 2K - 1. The essay checks the period-doubling word, whose first 2^k bits recur at 2^k for exactly 2^k - 1 bits, and computes its forced left half: black cells at every depth to 2,995 and beyond, as the theorem says. The verifier's replay accepts the module with the three standard axioms only. Nothing here decides Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, period 2, Jen's theorem, left diagonals, near-squares, period-doubling, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entry 11](https://github.com/ghywel/placego/blob/main/PROOFS.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261022-c27323, the white end](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-c27323)"]
---

## The question

Rule 30 updates every cell from itself and its two neighbors: the new color is *left* XOR (*center* OR *right*). From a single black cell it grows a pattern whose center column looks random. Problem 1 of the Rule 30 Prize asks whether that column is ever eventually periodic. The shortest case is period 2: could the center column read the clock `0101…` from some time on? The kit's own open question `Rule30ZeroBoundary.Q01` is that case for the single seed.

The first 60 steps, with the center column in red; its first twenty cells are `11011100110001011001`, not a clock:

```wl
pattern = CellularAutomaton[30, {{1}, 0}, 60];
ArrayPlot[ReplacePart[pattern, {t_, 61} :> 2 pattern[[t, 61]]], ColorRules -> {0 -> White, 1 -> GrayLevel[0.15], 2 -> StandardRed}, ImageSize -> 520]
```

This essay does not decide the period-2 case. It says what the column to the right of a period-2 center column cannot look like, for any configuration that has a leftmost black cell.

## The clock and the visible bits

Rule 30 is left-permutive: a cell's left neighbor is determined by the cell's next value and its two right neighbors, `x(t, j - 1) = x(t + 1, j) XOR (x(t, j) OR x(t, j + 1))`. Under the clock `x(t, 0) = t mod 2`, column `-1` is therefore determined by column `1`: at odd `t` the OR is 1 and the next clock value is 0, so `x(t, -1) = 1`; at even `t`, `x(t, -1) = 1 XOR x(t, 1)`. Only column `1` at even times matters: the *visible bits* `c(i) = x(2i, 1)`. The whole left half is then forced, column by column, by the clock and the visible bits.

**Near-squares.** Say the visible bits have a *near-square* at the pair `i < i′` with slack `K` if they agree for `i′ - K` steps from `i` and from `i′`: `c(i + s) = c(i′ + s)` for all `s < i′ - K`. A square `ww` at the start is the pair `0 < |w|` with slack 0. The period-doubling word, the fixed point of `0 → 01, 1 → 00`, has near-squares at every scale with slack 1: its first `2^k` bits recur at position `2^k` for exactly `2^k - 1` bits:

```wl
pd = Nest[Flatten[# /. {0 -> {0, 1}, 1 -> {0, 0}}] &, {0}, 12];
{StringJoin[ToString /@ Take[pd, 32]], Table[{k, LengthWhile[Range[0, 4095 - 2^k], pd[[# + 1]] == pd[[2^k + # + 1]] &], 2^k - 1}, {k, 1, 11}]}
```

## The forced left half of period-doubling

Take the clock as column 0 and the period-doubling word as the visible bits, and compute the forced left half: column `-1` from the rule above, then each column from the two to its right. The row at time 0 is the configuration's left half. Corollary F says it has no leftmost black cell. Its black cells, by depth, from 3,000 steps of the clock:

```wl
steps = 3000;
col0 = Table[Mod[t, 2], {t, 0, steps - 1}];
col1 = Table[If[EvenQ[t], pd[[t/2 + 1]], 0], {t, 0, steps - 1}];
colm1 = Table[BitXor[col0[[t + 2]], BitOr[col0[[t + 1]], col1[[t + 1]]]], {t, 0, steps - 2}];
row0 = Module[{a = colm1, b = col0, out = {col0[[1]], colm1[[1]]}}, Do[{a, b} = {Table[BitXor[a[[t + 1]], BitOr[a[[t]], b[[t]]]], {t, 1, Length[a] - 1}], a}; AppendTo[out, a[[1]]], {m, 2, steps - 2}]; out];
blacks = Flatten[Position[row0, 1]] - 1;
{Length[row0], Take[blacks, 40], Length[blacks], Last[blacks], Max[Differences[blacks]]}
```

About half the depths are black, the longest white gap is 13 cells, and the last black cell is at the last depth computed. The record's earlier strip search had excluded period-doubling to depth 53,165; the theorem excludes every depth.

## The idea of the proof

Suppose the configuration has a leftmost black cell, `L ≥ 1` cells left of column 0, and the visible bits have near-squares with slack `K` at pairs `i < i′` with `i′ - i` unbounded.

**Lemma B2** (the clock never stops; the record's, filed separately): infinitely many left diagonals `D k t = x(t, -L - t + k)` are eventually black. Take one with `k = b ≥ L + 2K`, black from time `t_b`.

**The block.** Pick a pair with `2(i′ - i) > b` and `2i′ ≥ t_b`. The visible agreement for `i′ - K` steps makes columns `-1` and `0` agree for `2(i′ - K)` steps from the times `2i` and `2i′`: column 0 by the clock, column `-1` at odd times because it is constant and at even times because it is the complement of the visible bits.

**Theorem A‴.** Jen's clocked bound says a common block of two adjacent columns at times `a < a′` has length at most `L′ + a′`, where `L′` is the distance from the left column to the leftmost black cell; the reason is that row `a′` is white at the distances `L′ + a + 1 … n - 1` left of the block. A black diagonal `b < a′ - a` at time `a′` sits in that range unless `n ≤ L′ + a′ - b`. Here `L′ = L - 1`, `a = 2i`, `a′ = 2i′`, so `2(i′ - K) ≤ L - 1 + 2i′ - b ≤ 2i′ - 2K - 1`: a contradiction.

Everything in this section is prose. The proof is the next section.

## The formal proof

The module, as the verifier rebuilds and checks it. The first part is the record's Lemma B2 on the kit's `evol`: `edge`, `D`, `jen_pow2` (the period `2^j`), `lemma_B2_quant`, `no_adjacent_white`, `white_then_black`, `infinitely_many_black`. The second is Theorem A‴: `step_inv`, `agree`, `theorem_A'`, `theorem_A3_white`, `theorem_A3`. The last is Corollary F: `col_m1` (column `-1` under the clock), `blocks_of_visible` (visible agreement to a block on columns `-1` and `0`) and `corollary_F`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["@@LEAN_SOURCE@@", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorem, as Lean prints it. `evol x0 t p` is the kit's evolution of the configuration `x0`; the hypotheses are the leftmost black cell at `-L` with `L ≥ 1`, the clock from `T0`, and the near-squares, as pairs `i < i′` with `i′ - i ≥ N` for every `N`, `T0 ≤ 2i`, and visible agreement for `s + K < i′`:

```wl
opens = {"Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.corollary_F"];
thm["TypeForm", "Open" -> opens]
```

The clock's consequence for column `-1`, and the block it gives:

```wl
{rule30Submission["Rule30Submission.col_m1"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.blocks_of_visible"]["TypeForm", "Open" -> opens]}
```

The two ingredients, Theorem A‴'s corollary and Lemma B2's corollary:

```wl
{rule30Submission["Rule30Submission.theorem_A3"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.infinitely_many_black"]["TypeForm", "Open" -> opens]}
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

- Nothing about the single seed directly: its center column is not known to be eventually a clock, and if it were, the theorem would only constrain column 1's visible bits from that time on.
- The hypothesis `L ≥ 1` excludes a configuration whose leftmost black cell is column 0 itself. With the clock from time 0 that cell is white, so `L ≥ 1` is automatic; with a later `T0` it is a hypothesis.
- The pairs are required to start after the clock begins (`T0 ≤ 2i`). Pairs that start earlier can be shifted: a near-square at `(i, i′)` with slack `K` gives one at `(i + d, i′ + d)` with slack `K + 2d`, so the shift costs a constant and the statement still applies; this shift is not in the module.
- Period-doubling, Chacon and the substitution fixed points with a double letter are excluded as visible bits under the clock; nothing is said about other right neighbours, or about periods other than 2.

## Provenance

Corollary F is RULE30-PRIZE.md section 8.59 and PROOFS.md entry 11 of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT: proved by hand by Local (Claude) on 2026-10-05, with the period-doubling and Chacon examples; machine-checked here for the first time by Cloud (Claude) on 2026-10-23, from Local's Lean for Lemma B2 and Theorem A‴ (2026-10-10). The mechanism is Jen's left-permutivity (1986), as the kit's `window_jen_col` uses it. The companion submissions file Lemmas B1–B3 and Theorem A⁗ separately.

## References

[1] E. Jen, *Global properties of cellular automata*, Journal of Statistical Physics 43 (1986) 219–242.

[2] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[3] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[4] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): PROOFS.md entry 11, `tests/probes/lean/JenPow2.lean` and `tests/probes/lean/TheoremA4.lean`, 2026.
