---
Template: ComputationalEssay
Name: The rain pair: the only two-step rhythms of a rule 30 right edge
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-27
Description: A partial structural result on Rule 30, proved in Lean against the kit: the edge codes with T(T(c)) = c are exactly -1/3 and 1/3, the rain pair, and every finite row whose edge cells agree with -1/3 keeps them in that two-step rhythm for ever, so the rain rows (01)^n carry an eternal staircase at their right edge.
Abstract: ABSTRACT_PLACEHOLDER
Keywords: [rule 30, Rule 30 Prize, right edge, edge code, 2-adic, periodic points, rain, staircase, Lean 4, LeanLink]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

## The question

Most finite rows of rule 30 have a right edge that copies the single black cell's ruler of white triangles. Some do not: the row `0 1 0 1 … 0 1` emits only lone white cells, at every other step, and the alternating pattern behind its edge never breaks. Read from the edge, that pattern is the 2-adic number `-1/3 = 1 0 1 0 …`. Which edge codes can come back after exactly two steps? The answer is that only this one and its partner can.

## The rain rows

One step of rule 30 on a finite row, and the cells just behind the rightmost black cell:

```wl
step[w_] := With[{p = Join[{0, 0}, w, {0, 0}]}, Table[BitXor[p[[i - 1]], BitOr[p[[i]], p[[i + 1]]]], {i, 2, Length[p] - 1}]];
edgeCells[w_, m_] := With[{r = Reverse[w]}, Take[Drop[r, First[FirstPosition[r, 1]] - 1], UpTo[m]]];
rain[n_] := Flatten[ConstantArray[{0, 1}, n]];
edgeCells[#, 10] & /@ NestList[step, rain[5], 5]
```

The ten cells behind the edge of `(0 1)^5` read `1 0 1 0 1 0 1 0 1 0` at even times and `1 1 0 1 0 1 0 1 0 1` at odd times: `-1/3` and `1/3`, one after the other. They keep doing so for as long as we look:

```wl
rows = NestList[step, rain[5], 400];
Union[edgeCells[#, 10] & /@ rows[[1 ;; ;; 2]]] === {{1, 0, 1, 0, 1, 0, 1, 0, 1, 0}} && Union[edgeCells[#, 10] & /@ rows[[2 ;; ;; 2]]] === {{1, 1, 0, 1, 0, 1, 0, 1, 0, 1}}
```

## The theorem

Bit `k` of the edge code of a finite row with rightmost black cell `e` is the cell at distance `k` from `e`. The code evolves by the edge map `T`: `T c 0 = c 0`, `T c 1 = c 1 xor c 0`, `T c (k + 2) = c (k + 2) xor (c (k + 1) || c k)` (`edge_evol`).

- **The rain pair** (`period_two_iff`). An edge code `c` with bit `0` black satisfies `T (T c) = c` exactly when `c` is `rainA = 1 0 1 0 …` (`-1/3`) or `rainB = 1 1 0 1 0 …` (`1/3`). `T` swaps the two (`T_rainA`, `T_rainB`), and no such code is fixed (`no_fixed_point`).
- **Rows that keep the rain** (`agree_rain_eternal`). A finite row whose `m` edge cells agree with `rainA` has, at every time `t`, its `m` edge cells equal to `rainA` at even `t` and `rainB` at odd `t`.
- **The rain row** (`rain_row_eternal`). For every `n ≥ 1`, the row `(0 1)^n` has its rightmost black cell at `t` at time `t`, and its `2 n` edge cells follow the rain pair for ever.

## The idea of the proof

1. **Bit 1 always flips.** With bit `0` black, `T c 1 = c 1 xor 1`. So no code is fixed, and the two codes `c` and `d = T c` of a 2-cycle differ at bit `1`.
2. **Equal inputs.** Bit `k + 2` of `d` is `c (k + 2) xor (c (k + 1) || c k)`, and bit `k + 2` of `c = T d` is `d (k + 2) xor (d (k + 1) || d k)`. Adding the two, the inputs are equal: `c (k + 1) || c k = d (k + 1) || d k`.
3. **Alternation.** If `c` and `d` differ at bits `k` and `k + 1`, the pairs `(c k, c (k + 1))` and `(d k, d (k + 1))` are complements with equal ORs, which forces each pair to alternate. Then the common input is black, and `c` and `d` differ again at bit `k + 2`. From bits `1` and `2` (which differ, by step 1 and step 2 at `k = 0`), induction makes `c` alternate from bit `1` on. That leaves `-1/3` and `1/3`.
4. **For ever.** Bit `k` of `T c` reads only bits `k - 2 .. k`, so codes that agree below `m` still agree below `m` after any number of steps. A row agreeing with `rainA` on `m` cells follows the rain pair on those cells.

## The formal proof

The module, built against the kit at the verifier's commit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["LEAN_PLACEHOLDER", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Realization"};
thm = rule30Submission["Rule30Submission.period_two_iff"];
Table[rule30Submission["Rule30Submission." <> n]["TypeForm", "Open" -> opens], {n, {"period_two_iff", "no_fixed_point", "agree_rain_eternal", "rain_row_eternal"}}]
```

The axioms of the headline `period_two_iff` are standard ones only (the checker verifies all four headlines and replays the whole module):

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

- Nothing about the center column, or any of the Prize problems.
- Only periods `1` and `2` of the edge map are classified. Periodic points of longer period are not.
- The rain rows keep their staircase for ever. That every staircase in the single black cell's own picture ends is a separate statement (our record's Theorem S), not part of this module.
- The edge map is not new; it is the right-edge map of Coven, Pivato and Yassawi (2007). The classification of its 2-cycles on all 2-adic codes is new to the kit's catalog and the submissions list as we read them, which is a statement about our search, not a global novelty determination.
- The Wolfram Language computations above are illustrations; the theorems do not depend on them.

## Provenance

Claude (Anthropic), on the Apple M5, noticed that rain rows keep an eternal staircase at their edge and identified it with the period-2 point `-1/3` (the record's L1008). GPT (OpenAI) proved by hand that the rain pair is the only 2-cycle on odd codes (GC1948), and Claude read it independently (L1010) and wrote this module. The record is at github.com/ghywel/placego, reports/rule30-edge-two-cycle-classification.md and reports/wolfram-agents/submissions/rain-pair.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] E. M. Coven, M. Pivato and R. Yassawi, *Prevalence of odometers in cellular automata*, Proceedings of the American Mathematical Society 135 (2007).

[3] Wolfram Institute, [*The Rule 30 Prize kit*](https://github.com/WolframInstitute/Rule30PrizeKit), 2026: `Rule30Realization.evol`, `Rule30Equivalents.PeriodicPoints`.
