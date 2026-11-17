---
Template: ComputationalEssay
Name: Rule 210 beside the period-2 clock: the one-sided question is false and the left half is linear
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-23
Description: Barrier material for Problem 1 of the Rule 30 Prize, proved in Lean against the official statements: the exact analogue of the kit's open period-2 question Q01 for rule 210, the one nonlinear left-permutive sibling, is false from the very first start, while every start consistent with the clock makes rule 210's left half linear (rule 90's)
Abstract: The kit's Rule30ZeroBoundary.Q01 is the period-2 question for rule 30 in one-sided form: no finitely supported start of the zero-boundary left half keeps column -1 black at every even step. The kit's barrier (Rule30Realization.barrier) shows that left-permutivity, the moving edge and Jen's theorem do not decide Problem 1, since rules 90, 150 and 210 share them. This essay takes rule 210 (left XOR (NOT center AND right)), the sibling that is nonlinear and not right-permutive like rule 30, and asks the kit's question of it. Rule30Submission.not_Q01_210: the one-sided period-2 statement is false for rule 210, because the empty start keeps the clock for ever. The reason is a parity invariant (parity_invariant): for every start consistent with the clock, every black cell at time t and depth k has t + k even, so two horizontally adjacent cells are never both black, the AND-NOT gate reduces to its right input, and the left half is rule 90's (linear). The record's hand proof that no finite configuration keeps rule 210's clock (the two-sided statement) is not formalized here. The essay computes the empty start's run, its parity, the column-1 bits it forces (runs of doubling lengths), and the count of starts of width W that survive W steps: 2^floor(W/2), the same count as the kit's count_constrained for rule 30. The verifier's replay accepts the module with the three standard axioms only. Nothing here decides Problem 1.
Keywords: [rule 30, rule 210, Rule 30 Prize, Problem 1, period 2, zero-boundary left half, Q01, barrier, rule 90, Lean 4, LeanLink]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entry 18](https://github.com/ghywel/placego/blob/main/PROOFS.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261022-c27323, the white end](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-c27323)"]
---

## The question, and the kit's barrier

Problem 1 of the Rule 30 Prize asks whether the center column of rule 30 is ever eventually periodic. Its first case is period 2, the clock. The kit states that case in one-sided form, `Rule30ZeroBoundary.Q01`: if the center column alternates, the left half sees it only as a white wall and evolves on its own; `Q01` says no finitely supported start of that *zero-boundary left half* keeps column `-1` black at every even step. It is open.

The kit also records a barrier, `Rule30Realization.barrier`: rule 30 is `left XOR g(center, right)` with `g = OR`, and every rule of that shape with `g(0,0) = 0`, `g(0,1) = 1` is left-permutive with an edge moving one cell per step, so Jen's theorem holds for all of them; yet for `g = right` (rule 90), `g = XOR` (rule 150) and `g = NOT center AND right` (rule 210) the single seed's center column is eventually constant. A proof of Problem 1 must use something specific to `OR`.

Rule 210 is the interesting sibling: like rule 30 it is nonlinear and not right-permutive. This essay asks the kit's period-2 question of rule 210 and answers it.

```wl
Row[{ArrayPlot[CellularAutomaton[30, {{1}, 0}, 40], ImageSize -> 300], ArrayPlot[CellularAutomaton[210, {{1}, 0}, 40], ImageSize -> 300]}]
```

## Rule 210's left half beside the clock

Hold the center column to the clock, black at the even steps as in the kit's `InX`. Rule 210 at position 0 reads `clock(t + 1) = x(t, -1) XOR (NOT clock(t) AND x(t, 1))`. At even `t` the clock is black and the next value white, so column `-1` must be white; at odd `t` the clock is white and the next value black, so column `1` is determined by column `-1`. The left half itself evolves on its own with the clock at the wall: in depth coordinates (`k` is position `-k`, depth 0 the wall), `z(t + 1, k + 1) = z(t, k + 2) XOR (NOT z(t, k + 1) AND z(t, k))`. So the kit's question for rule 210 is: does any finitely supported start keep column `-1` white at every even step?

The empty start does. Its run, 12 steps and 12 depths, the wall at the right:

```wl
z210[L_, T_, D_] := Module[{row = Prepend[Table[L[k], {k, 1, D - 1}], 1], out}, out = {row}; Do[row = Prepend[Table[BitXor[row[[k + 2]], BitAnd[1 - row[[k + 1]], row[[k]]]], {k, 1, D - 2}] ~Join~ {0}, If[EvenQ[t], 1, 0]]; AppendTo[out, row], {t, 1, T - 1}]; out];
Z = z210[0 &, 300, 600];
ArrayPlot[Reverse /@ Z[[1 ;; 12, 1 ;; 13]], Mesh -> True, ImageSize -> 400]
```

Every black cell sits at a time and depth of even sum, so column `-1` (depth 1) is black only at odd steps, and the clock is kept. The parity check over 300 steps inside the light cone, and the count of black cells:

```wl
{Length[Select[Flatten[Table[{t, k}, {t, 0, 299}, {k, 0, t}], 1], Z[[#[[1]] + 1, #[[2]] + 1]] == 1 && OddQ[#[[1]] + #[[2]]] &]], Total[Table[Z[[t + 1, k + 1]], {t, 0, 299}, {k, 0, t}], 2]}
```

The column-1 bits that the clock then forces at the odd steps, `1 - z(t, 1)`, come in runs of doubling lengths (the record's doubling-runs sequence, proved by its formula in the record; here only computed):

```wl
sigma = Table[1 - Z[[t + 1, 2]], {t, 1, 299, 2}];
{StringJoin[ToString /@ Take[sigma, 64]], Length /@ Split[sigma]}
```

How many starts of width `W` keep the clock through time `W - 1`? For rule 30 the kit's `count_constrained` says exactly `2^⌊W/2⌋` of them satisfy its constraint up to time `W - 1`. Rule 210 gives the same count, with the empty start among them at every width:

```wl
keeps[bits_, W_] := Module[{R = z210[If[# <= W, bits[[#]], 0] &, W, 2 W + 2]}, AllTrue[Range[0, W - 1, 2], R[[# + 1, 2]] == 0 &]];
Table[{W, Count[Tuples[{0, 1}, W], b_ /; keeps[b, W]], 2^Floor[W/2]}, {W, 1, 12}]
```

## The idea of the proofs

**The empty start keeps the clock.** Induction on time: from a white start every black cell `(t, k)` has `t + k` even. The wall is black at even times. A cell at depth `k + 1` and time `t + 1` is `z(t, k + 2) XOR (NOT z(t, k + 1) AND z(t, k))`; if it is black, exactly one of the two terms is, and either `(t, k + 2)` or `(t, k)` is black, both of parity `t + k`, so `t + 1 + k + 1` is even.

**The parity invariant for every consistent start.** Induction on depth, with left-permutivity read leftward: `z(t, k + 2) = z(t + 1, k + 1) XOR (NOT z(t, k + 1) AND z(t, k))`. Depth 0 is the wall; depth 1 is white at even times by the constraint, so black only at odd times; and a black cell at depth `k + 2` needs `(t + 1, k + 1)` or `(t, k)` black, both of parity `t + k`.

**Linearity.** Two cells at depths `k` and `k + 1` have parities `t + k` and `t + k + 1`, so by the invariant they are never both black; when `z(t, k)` is black, `NOT z(t, k + 1)` is true and the gate is `z(t, k)`; when it is white the gate is 0. So the step is `z(t, k + 2) XOR z(t, k)`: rule 90.

Everything in this section is prose. The proofs are the next section.

## The formal proof

The module, as the verifier rebuilds and checks it: `zrow210` (the left half in the kit's ZBL encoding), `zrow210_inv` (left permutivity), `InX210` and `Q01_210` (the kit's `InX` and `Q01` with column `-1` white at the even steps), `white_start_parity`, `white_start_inX`, `not_Q01_210`, `parity_invariant`, `linear`, `no_adjacent`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["@@LEAN_SOURCE@@", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline, as Lean prints it, and the definition it negates beside the kit's own `Q01`:

```wl
opens = {"Ruliology.CellularAutomata.Rule30ZeroBoundary", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.not_Q01_210"];
{thm["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.Q01_210"]["TypeForm", "Open" -> opens], rule30Submission["Ruliology.CellularAutomata.Rule30ZeroBoundary.Q01"]["TypeForm", "Open" -> opens]}
```

The parity invariant and the linear step:

```wl
{rule30Submission["Rule30Submission.parity_invariant"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.linear"]["TypeForm", "Open" -> opens]}
```

The system itself and the constraint:

```wl
{rule30Submission["Rule30Submission.zrow210_succ"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.InX210"]["TypeForm", "Open" -> opens]}
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

- Nothing about rule 30. The kit's `Q01` stays open; this is its analogue for a sibling rule, and the answer there is no.
- The two-sided statement for rule 210, that no finite configuration keeps the clock, is proved by hand in the record (PROOFS.md entry 32) and not formalized here. With this module it says: for rule 210 the one-sided period-2 statement is false and the two-sided one is true, so the gap between them is real on a rule where it can be studied cheaply.
- The doubling-runs formula for the forced column-1 bits is the record's (GPT, §G26); here it is only computed.
- The count `2^⌊W/2⌋` for rule 210 is a computation to width 12, not a theorem.

## Provenance

The witness and the parity invariant are RULE30-PRIZE.md section 8.65 and PROOFS.md entry 18 of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT: the empty left half and its doubling-runs column 1 found by Local (Claude) on 2026-10-06 and proved by GPT (§G26), the parity invariant proved by Local the same day; formalized here for the first time by Cloud (Claude) on 2026-10-23, in the kit's zero-boundary encoding. The companion submissions file the record's rule 30 results (the white end, the excluded words, the diagonal lemmas, Theorem A⁗, Corollary F).

## References

[1] E. Jen, *Global properties of cellular automata*, Journal of Statistical Physics 43 (1986) 219–242.

[2] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[3] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[4] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): PROOFS.md entries 18 and 32, RULE30-PRIZE.md §8.65, 2026.
