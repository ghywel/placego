---
Template: ComputationalEssay
Name: Rule 210, the two-sided statement: no finite configuration keeps the period-2 clock on its center column
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-23
Description: Barrier material for Problem 1 of the Rule 30 Prize, proved in Lean against the official statements: under rule 210, the one nonlinear left-permutive sibling of rule 30, no finite configuration has a center column reading the clock 0101…, nor one that is eventually alternating in either phase, while the one-sided period-2 question (the kit's Q01) is false for the same rule
Abstract: The kit's Rule30ZeroBoundary.Q01 is the period-2 question for rule 30 in one-sided form, and its barrier Rule30Realization.barrier shows that rules 90, 150 and 210 share left-permutivity and Jen's theorem with rule 30. Our submission R30-20261022-920c1b showed the one-sided period-2 statement false for rule 210: the empty left half keeps the clock. This essay proves the two-sided statement true for rule 210 (Rule30Submission.no_finite_clock): no finite configuration x0 : ℤ → Bool has run210 x0 t 0 = decide (t % 2 = 1) for all t, nor an eventually alternating center column in either phase (no_finite_eventually_alternating; for the kit's seed, seed_not_eventually_alternating through run210_seed). The proof is the record's clearing-front argument: under the clock the whole left half is parity-sparse and evolves as rule 90; every admissible left row has a parity-sparse clock realization built sideways from the clock; rule 90's freshman's dream, run90 x0 (2^n) i = x0 (i - 2^n) xor x0 (i + 2^n), kills any finite parity-sparse clock realization at time 2^n + 1; and a candidate that first leaves the background at e fails the clock on its own diagonal if e is odd, or, if e is even, after a clearing witness and a 01 front propagate through the pairs of diagonals beyond e until the first initially black background gate w, at time e + 2w + 1. So for rule 210 the gap between the one-sided and the two-sided period-2 statements is real, an argument for attacking rule 30's two-sided forms. The verifier's replay accepts the module with the three standard axioms only. Nothing here is about rule 30's center column.
Keywords: [rule 30, rule 210, Rule 30 Prize, Problem 1, period 2, barrier, two-sided, rule 90, clearing front, Lean 4, LeanLink]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entry 32](https://github.com/ghywel/placego/blob/main/PROOFS.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261022-920c1b, the one-sided statement for rule 210](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-920c1b)"]
---

## The question, and the kit's barrier

Problem 1 of the Rule 30 Prize asks whether the center column of rule 30 is ever eventually periodic; its first case is period 2, the clock. The kit states that case one-sidedly, `Rule30ZeroBoundary.Q01`: no finitely supported start of the zero-boundary left half keeps column `-1` black at every even step. It is open. The kit's barrier `Rule30Realization.barrier` shows that left-permutivity, the moving edge and Jen's theorem cannot decide it, because rules 90, 150 and 210 share them.

Rule 210, `left XOR (NOT center AND right)`, is the sibling that is nonlinear and not right-permutive, like rule 30. Our previous submission on it showed the kit's one-sided question **false** there: the empty left half keeps the clock for ever, and beside the clock the left half is parity-sparse and linear. This essay shows the **two-sided** statement **true** for rule 210: no finite configuration keeps the clock. The two answers differ, so the gap between the one-sided and two-sided period-2 statements is real on a rule where it can be studied cheaply.

```wl
Row[{ArrayPlot[CellularAutomaton[30, {{1}, 0}, 40], ImageSize -> 300], ArrayPlot[CellularAutomaton[210, {{1}, 0}, 40], ImageSize -> 300]}]
```

## Finite seeds die quickly

Every finite seed with black cells in `-4 … 8` loses the clock within a dozen steps. `survival` counts the steps for which the center reads `t mod 2`; the longest survivor among all 8,191 nonempty seeds:

```wl
survival[bits_] := Module[{ca = CellularAutomaton[210, {bits, 0}, 199]}, LengthWhile[Range[0, 199], ca[[# + 1, # + 5]] == Mod[#, 2] &]];
best = First[MaximalBy[Rest[Tuples[{0, 1}, 13]], survival]];
{survival[best], StringJoin[ToString /@ best]}
```

## The background: a clock realization built sideways

Under the clock the whole left half is parity-sparse (every black cell `(t, i)` with `i ≤ 0` has `t + i` odd), so rule 210 acts on it as rule 90, `left XOR right`. For any left row that is white at depth 0 and at the even depths, a clock realization can be built *sideways*: the left half evolves by rule 90 with the clock imposed at the wall, and column `j + 1` is read off from columns `j` and `j - 1` by rule 90's right-permutivity, `x(t, j + 1) = x(t + 1, j) XOR x(t, j - 1)`. The construction for the empty left row, its first 64 right sites (the pattern `100010` repeated: black at the odd sites not divisible by 3), and the clock of its truncation at site 160, which holds exactly as long as the light cone from the cut allows:

```wl
bg[L_, w_] := Module[{clk = Mod[#, 2] &, T = w, lft = <||>, cols = <||>}, Do[Do[lft[{t, i}] = If[t == 0, If[i < 0 && -i + 1 <= Length[L], L[[-i + 1]], 0], If[i == 0, clk[t], BitXor[Lookup[lft, Key[{t - 1, i - 1}], 0], Lookup[lft, Key[{t - 1, i + 1}], 0]]]], {i, -w - 1, 0}], {t, 0, T + w + 1}]; cols[0] = Table[clk[t], {t, 0, T + w}]; cols[1] = Table[BitXor[clk[t + 1], lft[{t, -1}]], {t, 0, T + w}]; Do[cols[j] = Table[BitXor[cols[j - 1][[t + 2]], cols[j - 2][[t + 1]]], {t, 0, T + w - j}], {j, 2, w}]; Join[Table[lft[{0, i}], {i, -w, -1}], {0}, Table[cols[j][[1]], {j, 1, w}]]];
survivalList[y0_, w_, T_] := Module[{ca = CellularAutomaton[210, {y0, 0}, T]}, LengthWhile[Range[0, T], ca[[# + 1, # + w + 1]] == Mod[#, 2] &]];
y0 = bg[{0}, 160];
{StringJoin[ToString /@ y0[[161 + 1 ;; 161 + 64]]], survivalList[y0, 160, 400]}
```

The same for the left row with one black cell at depth 3, sites `-4 … 40`:

```wl
y1 = bg[{0, 0, 0, 1}, 160];
{StringJoin[ToString /@ y1[[161 - 4 ;; 161 + 40]]], survivalList[y1, 160, 400]}
```

## A deviation fails at a predictable time

Flip one site `e` of the empty-row background. If `e` is odd the clock fails at time `e`. If `e` is even, the deviation is cleared by the gate left of it, a `01` front propagates through the pairs of diagonals beyond `e`, and the clock fails at time `e + 2w + 1`, where `w` is the index of the first background gate `e + 2w + 1` that is black at time 0:

```wl
flip[y0_, w_, e_] := ReplacePart[y0, w + 1 + e -> 1 - y0[[w + 1 + e]]];
gate[y0_, w_, e_] := LengthWhile[Range[0, 30], y0[[w + 1 + e + 2 # + 1]] == 0 &];
Grid[Prepend[Table[{e, survivalList[flip[y0, 160, e], 160, 200], If[EvenQ[e], gate[y0, 160, e], "-"], If[EvenQ[e], e + 2 gate[y0, 160, e] + 1, e]}, {e, {1, 2, 3, 4, 6, 8}}], {"flipped site e", "clock fails at", "w", "predicted"}], Frame -> All]
```

## The idea of the proof

**Parity.** Under the clock, column `-1` must be white at even times (at an even time the clock is black, so the next clock bit, white, equals the left bit); by left-permutivity read leftward, every black cell `(t, i)` with `i ≤ 0` has `t + i` odd. Two horizontally adjacent cells are then never both black, so the gate `NOT center AND right` is `right` and the left half is rule 90's.

**The background.** Rule 90 is right-permutive, so from the clock and a parity-sparse left half the right columns are forced one by one; the configuration read off at time 0 evolves as built (`run90_bg`), is parity-sparse (`bg_even_white`) and keeps the clock (`clock_bg`).

**The freshman's dream.** Rule 90 is linear and commutes with shifts, so `run90 x0 (2^n) = shift left XOR shift right` by `2^n` (`run90_pow2`). A finite parity-sparse configuration is therefore white at the center at time `2^n + 1` once `2^n` exceeds its support, while the clock is black there (`no_finite_clock90`).

**The deviation.** A clock orbit whose left row is `L` and whose first difference from `bg L` is at `e ≥ 1`. For odd `e`, the diagonal `e` of the two orbits differs for ever, since the diagonal `e - 1` feeding the gate is even and white, so the candidate differs from the clock at time `e` (`odd_impossible`). For even `e`, the deviation's even diagonal is black until the gate `bb = Diag (e - 1)` of the background first fires at `τ ≤ e - 1` and white after; the background's odd gates `Ab j = Diag (e + 2j + 1)` keep their initial values through `τ + j` and flip at `τ + j + 1` (`W1_const`, `W1_flip`); in the candidate a clearing witness and a `01` front propagate pair by pair (`marker`, `propagate`, `front`); after its front each candidate odd diagonal differs from the background's by exactly the background's initial gate value (`identify`); at the first initially black gate `w`, the candidate's clock bit at time `e + 2w + 1` is the complement of the background's, which is the true clock (`even_impossible`). If no gate beyond `e` is black at time 0, the background is finite and the freshman's dream applies to it.

**Phase.** An eventually alternating center in either phase is a clock from time 0 for the configuration at a suitable later time, still finite.

Everything in this section is prose. The proofs are the next section.

## The formal proof

The module, as the verifier rebuilds and checks it: `run210` and the bridge `run210_seed` to the kit's `run g210`; `Clock210`, `Diag210`, `Finite210`; locality (`diag_local`, `run210_cone`); parity (`parity_of_even_white`, `rule90_of_even_white`, `parity_left_of_clock`, `left_row_of_clock`, `left_det`); rule 90 (`run90_xor`, `run90_add`, `run90_shift`, `run90_pow2`, `no_finite_clock90`); the background (`lft`, `colR`, `bg`, `run90_bg`, `lft_parity`, `colR_parity`, `bg_even_white`, `clock_bg`); the deviation (`Dev`, `odd_impossible`, `tau`, `P0_before`, `P0_after`, `W1_const`, `W1_flip`, `marker`, `propagate`, `front`, `identify`, `even_impossible`); and the headlines.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["@@LEAN_SOURCE@@", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline, as Lean prints it: no finite configuration keeps the clock, and no finite configuration has an eventually alternating center column in either phase; `run210` is rule 210 on an arbitrary configuration, with `Finite210` and `Clock210` as defined:

```wl
opens = {"Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.no_finite_clock"];
{thm["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.no_finite_eventually_alternating"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.Clock210"]["TypeForm", "Open" -> opens]}
```

The kit's seed, and the bridge to the kit's `run g210`:

```wl
{rule30Submission["Rule30Submission.seed_not_eventually_alternating"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.run210_seed"]["TypeForm", "Open" -> opens]}
```

The four pillars: the parity of the left half under the clock, the background's clock, the freshman's dream, and the two deviation cases:

```wl
{rule30Submission["Rule30Submission.parity_left_of_clock"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.clock_bg"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.run90_pow2"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.Dev.even_impossible"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.Dev.odd_impossible"]["TypeForm", "Open" -> opens]}
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

- Nothing about rule 30's center column. This is the period-2 question for a sibling rule, in two-sided form, next to the one-sided form filed before: for rule 210 the two statements have opposite answers.
- The background is constructed, not given in closed form; the hand proof's explicit background (black at the odd sites not divisible by 3, with the left row's mirror superposed) is shown by computation above and not identified with the construction in the module.
- `Finite210` is finite support in both directions. A configuration with finite left support and an infinite right half can keep the clock: the backgrounds above are such, and the module's `clock_bg` proves it.

## Provenance

Proposition 19 is PROOFS.md entry 32 of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT: the clearing-front proof is GPT's (ledger entry GC478, 2026-10-08), after Local (Claude) conjectured the exact life law and built the finite instruments (L282); Local second-read it (L285). GPT laid the proof out as a formalization chain with its bounded controls on 2026-10-23 (GC1700). Cloud (Claude) formalized it on the kit's definitions the same day, replacing the chain's residue-class arithmetic by the sideways construction of the background and rule 90's freshman's dream. The companion submission R30-20261022-920c1b files the one-sided statement.

## References

[1] E. Jen, *Global properties of cellular automata*, Journal of Statistical Physics 43 (1986) 219–242.

[2] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[3] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[4] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): PROOFS.md entry 32, CHAT-LEDGER.md GC478 and GC1700, `reports/wolfram-agents/GPT-PROOFS32-CHAIN.md`, 2026.
