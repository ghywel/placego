---
Template: ComputationalEssay
Name: The Separator Is Q01 for Free Bits Without Two Adjacent Whites, and BWH Is a Death-Time Bound
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-08
Description: Core Lean. The constant-tail separator SEP is Q01 restricted to free bits with no two adjacent whites, and Q01 is SEP plus the free bits that meet two adjacent whites infinitely often; SEP implies Q01Gap and is a width-one-layer statement; BWH is equivalent to exact-width death bounds and gives D(W) ≤ 2W + 4. Nothing here proves SEP, BWH or Q01.
Abstract: In the zero-boundary left half of rule 30, Q01 says that no finitely supported start keeps the cell beside the wall black at every even tick. The kit states two open hypotheses on streams over Fin 4, the constant-tail separator SEP and the binary wedge hypothesis BWH, and records no implication between them and Q01. We prove in core Lean where they sit. A chart sends each constrained start Theta f to an endpoint stream whose inverse cone is the start's own run, and that stream is hard-core exactly when the free bits f have no two adjacent white bits. So SEP is equivalent to Q01 restricted to those free bits, and Q01 is SEP together with the free bits that meet two adjacent whites infinitely often. SEP implies Q01Gap and CQ01Empty. It is also the statement that no width-one layer beside the alternating column, with any input from column 2, has a finite forced left row. BWH is equivalent to exact-width death bounds, so under BWH every start of width at most W ≥ 16 dies by tick 2W + 4, and BWH implies Q01. Kernel-checked controls show that neither guard of those bounds can be dropped. Nothing here proves SEP, BWH or Q01.
Keywords: [rule 30, Rule 30 Prize, Q01, zero-boundary left half, constant-tail separator, binary wedge hypothesis, death time, Q01Gap, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[lhallee/rule30-open, WedgeLadderQ01](https://github.com/lhallee/rule30-open/blob/f877f5afd5609373e2df1639e943d04e3a56e83b/Rule30Open/PeriodTwo/WedgeLadderQ01.lean)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261027-230bc7: the gate trap and Q01Gap](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-230bc7)", "[R30-20261102-f48894: BWH implies the separator](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-f48894)", "[R30-20261106-45f6e9: Q01, mortality and repeat budgets](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-45f6e9)"]
---

## 1. The statements

The kit's zero-boundary left half runs rule 30 on the cells to the left of a white wall: `zrow L t k` is the cell at depth `k` and tick `t`, and the start `L` is read at depths `k ≥ 1`. A start is constrained when depth `1` is black at every even tick. The constrained starts are exactly the rows `Theta f`, where the free bits `f s` are depth `1` at the odd ticks `2 s + 1`. `Q01` says that no constrained start is finitely supported (`Rule30ZeroBoundary.Q01`, `Q01_iff_Theta`).

The kit also states two open hypotheses on streams over `Fin 4` (`Rule30WedgeBridge`). A stream is hard-core when every symbol is `1` or `2` and no two adjacent symbols are both `1`. The constant-tail separator `SEP` says that no hard-core stream has an inverse diagonal that is eventually constant `2` or eventually constant `3` (`ConstantTailSeparator`, equivalent to `OrbitSeparator`). The binary wedge hypothesis `BWH` says that for `n ≥ 7` no stream with a binary prefix of length `2 n + 2` has a constant wedge `2` or `3` of length `n + 2`. The kit proves `BWH ⇒ SEP` and that each excludes period two of the center column. Its docstrings record that no implication is proved, in either direction, between these hypotheses and `Q01`. This module proves where they sit.

Write `N` for the free bits with no two adjacent white bits, and `QN` for `Q01` restricted to them: `Theta f` is not finitely supported when `f` is in `N`.

**Theorem (`sep_iff_QN`).** `SEP` holds if and only if `QN` holds.

**Theorem (`Q01_iff_sep_and`).** `Q01` holds if and only if `SEP` holds and no finitely supported `Theta f` has free bits that meet two adjacent whites infinitely often.

**Theorem (`sep_Q01Gap`, `sep_iff_LR1`).** `SEP` implies the kit's `Q01Gap`, hence `CQ01Empty`. It is equivalent to `LR1`: no width-one layer beside the alternating column, with any start cell and any input from column `2`, has a finitely supported forced left row.

**Theorem (`bwh_iff_deathBounds`, `bwh_death`, `bwh_Q01`).** `BWH` holds if and only if every start of exact even width `W ≥ 16` dies by tick `2 W`, and every start of exact odd width `W ≥ 17` whose top two cells are black dies by tick `2 W - 2`. Under `BWH`, every start supported at depths `≤ W` with `W ≥ 16` dies by tick `2 W + 4`, and `Q01` follows.

Here a start dies at the first even tick at which depth `1` is white.

## 2. The chart

For a start `L`, let `zpair L t k` be the pair of depths `k` and `k + 1` at tick `t`, read as a symbol of `Fin 4` by the kit's `encodePair`. The endpoint stream of `L` is the pair of depths `1, 2` at the odd ticks: `zEnd L j = zpair L (2 j + 1) 1`.

**Chart (`cone_chart`, `peel_chart`).** If depth `1` is black at every even tick up to `2 S`, then for `j + n ≤ S` and `t + d ≤ S`,

`cone (zEnd L) n j = zpair L (2 j + n) (n + 2)`, and `peelPow d (inverse (zEnd L)) t = zpair L t (2 d + t + 2)`.

The inverse cone of the endpoint is the run of the start itself, read diagonally. Two facts carry it. The kit's `phi` steps one pair back in depth, from a pair and the pair below it one tick later (`zpair_back`, from `pair_inverse_table`). At an even tick depth `1` is black, so the boundary of the endpoint is the next pair down (`zEnd_boundary`). This is the kit's `actual_cone_chart` in zero-boundary coordinates. No right half enters, and the finite horizon is what the death bounds of section 5 need.

For a constrained start the endpoint is binary. At the odd tick `2 j + 1` depths `1` and `2` differ, because depth `1` is black one tick later. So `zEnd (Theta f) j` is `2` where `f j` is black and `1` where it is white (`zEnd_Theta`). It is hard-core exactly when `f` has no two adjacent white bits (`hardCore_endOf_iff`), and every hard-core stream arises this way (`hardCore_eq_endOf`).

## 3. SEP is Q01 on one class of free bits

Suppose `f` is in `N` and `Theta f` is white beyond depth `W`. By the chart, the `W`-th peel of the inverse of its endpoint is zero at every tick, because it reads depths beyond `W + t` at tick `t`. The kit's `separator_excludes_finite_peel_rank` says that under `SEP` no hard-core stream has a finite peel rank. So `SEP ⇒ QN`.

Conversely, suppose a hard-core stream has inverse eventually equal to `c ∈ {2, 3}` from index `m` on. The stream is the endpoint of some `Theta f` with `f` in `N`. Since `phi c c = 0` and `phi 0 0 = 0`, every further peel vanishes from `m` on (`peel_tail_zero`). Read through the chart at the even tick `2 m`, the row there is white from depth `2 m + 4` on. That row is `Theta` of the free bits shifted by `m` (`zrow_Theta_even`, from the kit's `two_step_shift`), and the shift stays in `N`. So `QN ⇒ SEP`, and `sep_iff_QN` holds. No rotation of the stream is needed.

The same shift shows that `QN` excludes every finite `Theta f` whose free bits are free of two adjacent whites from some index on (`QN_eventually`). So the only finite constrained starts that `SEP` leaves open have free bits meeting two adjacent whites infinitely often (`Q01_iff_sep_and`). In particular `Q01 ⇒ SEP` (`Q01_sep`). The class of `Q01Gap` gives free bits whose complement has no two adjacent black bits from some step on, so `SEP ⇒ Q01Gap` (`sep_Q01Gap`), and the kit's `CQ01Empty_of_Q01Gap` gives `CQ01Empty`.

## 4. Width-one layers

Put a single column beside the alternating center column, black at the even ticks: `layerCol x0 r` has start cell `x0` and arbitrary input `r t` from column `2`, and steps by rule 30. Its word `layerWord x0 r s` is its value at the white tick `2 s + 1`.

The layer words are exactly the words with no two adjacent black bits. If the column is black at a white tick, it is black at the next black tick, so it is white at the next white tick (`layerWord_no11`). Conversely every such word is a layer word: start white, and feed `r (2 s) = !w s` and `r (2 s + 1) = false` (`layerWord_realizes`). At the black ticks a layer is unconstrained (`black_tick_control`).

So `LR1`, which says that every layer's forced left row `Theta (fun s => !layerWord x0 r s)` is infinite, is `QN` (`LR1_iff_QN`), and `SEP ⇔ LR1`. The column `1` of a right half driven by the alternating column is a layer whose input is the right half's own column `2` (`u_eq_layerWord`). Hence, under `SEP`, the kit's sideways row `Psi R` is infinite for every right half `R` (`LR1_not_finSupp_Psi`), and `CQ01` follows (`sep_CQ01`). The kit already has this conclusion as `constant_separator_excludes_alternating`, in the coordinates of the whole configuration. What the layers add is the converse: `SEP` asks for nothing beyond a single column with free input, and it asks for all of that.

## 5. BWH is a death-time bound

The chart with a finite horizon gives a dictionary. For `n, ℓ ≥ 1` and `c ∈ {2, 3}`, a stream with a binary prefix of length `n + ℓ` and a constant wedge `c` of length `ℓ` at depth `n` exists exactly when some start survives to tick `2 (n + ℓ)` with its last black cell at depth `2 n + 2` (for `c = 2`), or at depth `2 n + 3` with the cell before it black (for `c = 3`).

From a row to a stream (`wedge_of_row_two`, `wedge_of_row_three`): survival makes the endpoint binary, and the top of the row moves out one depth per tick, so the pair the chart reads is the top pair, `2` or `3`. From a stream to a row (`row_of_wedge`): take `Theta f` with the stream's free bits. The constant wedge forces zero pairs from depth `2 n + 4` through depth `2 (n + ℓ) + 1`, because each further peel of a constant is zero. Truncate there; the last check, at tick `2 (n + ℓ)`, reads depths only up to `2 (n + ℓ) + 1`, so the truncation survives.

With `ℓ = n + 2` this turns `BWH` into the exact-width bounds of section 1 (`bwh_iff_deathBounds`). A start of odd width without its top two cells black has them black two ticks later, at width `W + 2`. So it dies by tick `2 + 2 (W + 2) - 2 = 2 W + 4`. Widths up to `16` die by tick `32` (the kit's `q01_width_le_16`). That gives `D(W) ≤ 2 W + 4` for `W ≥ 16` (`bwh_death`), and `BWH ⇒ Q01` (`bwh_Q01`).

Neither guard of the exact-width bounds can be dropped, and the module proves it by kernel checks on natural numbers. The start `272125`, binary `1000010011011111101`, has exact odd width `19`, a white cell at depth `18`, and survives to tick `36 = 2 · 19 - 2` (`odd_guard_control`, `odd_guard_needed`). The start `11083`, of exact width `14 = 2 · 6 + 2`, survives to tick `30`, past `2 · 14` (`even_threshold_control`, `even_threshold_needed`). The kit's `small_bwh_control` is the same threshold in stream form, at `n = 5`.

## 6. Worked numbers

The cell below recomputes the death ticks of the two control starts, checks the peel chart on the start `11083` at all `136` pairs `(d, t)` with `t + d ≤ 15` (the start survives to tick `30`), and counts the distinct layer words of lengths `1` to `6` over every start cell and every input.

```wl
F[y_] := BitXor[BitShiftRight[y], BitOr[y, BitShiftLeft[y]]];
death[y0_] := Module[{y = y0, t = 0}, While[OddQ[y], y = F[F[y]]; t += 2]; t];
phi[a_, b_] := Which[a == 0, {0, 1, 3, 2}[[b + 1]], a == 2, {3, 2, 0, 1}[[b + 1]], True, {3, 2, 1, 0}[[b + 1]]];
rows = NestList[F, 11083, 80];
zrow[t_, k_] := If[k == 0, 0, BitGet[rows[[t + 1]], k - 1]];
zpair[t_, k_] := 2 zrow[t, k] + zrow[t, k + 1];
end[j_] := zpair[2 j + 1, 1];
cone[0, j_] := 3 - end[j];
cone[1, j_] := phi[end[j], 3 - end[j + 1]];
cone[t_, j_] := cone[t, j] = phi[cone[t - 2, j + 1], cone[t - 1, j + 1]];
peel[0, t_] := cone[t, 0];
peel[d_, t_] := peel[d, t] = phi[peel[d - 1, t], peel[d - 1, t + 1]];
pairs = Flatten[Table[{d, t}, {d, 0, 15}, {t, 0, 15 - d}], 1];
layerWord[x0_, r_, k_] := Module[{c = x0, w = {}},
  Do[c = BitXor[Boole[EvenQ[t]], BitOr[c, BitGet[r, t]]]; If[EvenQ[t], AppendTo[w, c]], {t, 0, 2 k - 1}]; w];
layerCount[k_] := Length[Union[Flatten[Table[layerWord[x0, r, k], {x0, 0, 1}, {r, 0, 2^(2 k) - 1}], 1]]];
{death[272125], death[11083], Length[pairs], AllTrue[pairs, peel[#[[1]], #[[2]]] == zpair[#[[2]], 2 #[[1]] + #[[2]] + 2] &], layerCount /@ Range[6]}
```

## 7. Prior art and scope

The chart, `Q01 ⇒ SEP` and `BWH ⇒ Q01` are known. They are in the external Lean development [`lhallee/rule30-open`](https://github.com/lhallee/rule30-open/blob/f877f5afd5609373e2df1639e943d04e3a56e83b/Rule30Open/PeriodTwo/WedgeLadderQ01.lean), whose `zcone_chart` and `zpeel_chart` are the chart for a zero-driven start, and which proves that a binary constant-tail separator is equivalent to `Q01`, that `Q01` implies `ConstantTailSeparator`, and that `BWH` implies `Q01`. They are reproved here in the kit's coordinates. The same development's [`WedgeLadder.md`, section “BWH is the kit's Q01 at a linear horizon (computed)”](https://github.com/lhallee/rule30-open/blob/f877f5afd5609373e2df1639e943d04e3a56e83b/Rule30Open/PeriodTwo/WedgeLadder.md) already states the exact-width interpretation, including the top-two-black guard and the horizons `2 W` and `2 W - 2`, and checks it by simulation through `n = 12`. It explicitly leaves that finite form out of Lean. The dictionary's mathematical interpretation is therefore prior art; this module supplies its formal proof in both directions. The kit's hypotheses and their period-two consequences are David Condrey's (`Rule30WedgeBridge`, `Rule30SeparatorEquivalences`, `Rule30SEPToPeriodTwo`), with additions by G.P.J.W. Quint; `Q01Gap` and `CQ01Empty_of_Q01Gap` are Renaud Bosdure's (`Rule30GateTrap`). The kit's own unconditional bound `q01_width_le_52_linear` gives `2 W + 8` up to width `52`.

The additions are the exact class `N`, so `SEP ⇔ QN` and the description of `Q01` as `SEP` plus one class of free bits; `SEP ⇒ Q01Gap`; the width-one-layer form `LR1`; and a core Lean proof of the known finite-width interpretation, with the at-most-width consequence `2 W + 4` and two kernel-checked guard controls. These statements were developed in the project's swarm and carried by hand in the [project's record](https://github.com/ghywel/placego/blob/main/PROOFS.md), with the prior-art overlap distinguished here; the width-`19` witness is the swarm skeptic's. The record's own version of `LR1` runs its clock from a white tick and needs a one-tick repair. The kit's sideways convention starts black, so it needs none.

Read through the dictionary, the wedge horizons `M(n, c)` of `BWH` are exact-width death times: `M = D / 2 - 1 - n`. An exhaustive search over exact widths reproduces the swarm's table for `n = 5` to `9`: `M(5, 3) = 8` and `M(6, 2) = 9` (why `n ≥ 7` is needed), then `7, 6`, `6, 7` and `5, 8`. That search is in the record, not in this notebook.

Nothing here proves `SEP`, `BWH` or `Q01`, or decides whether `SEP` implies `Q01`: that is exactly the question whether a finite constrained start can have free bits meeting two adjacent whites infinitely often. Problems 1 to 3 stay open.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30SEPToPeriodTwo` (the streams, the separators and `encodePair`), `Rule30GateTrap` (`Q01Gap`) and `Rule30ZeroBoundarySmall` (the bound at width `16`).

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30SEPToPeriodTwo
import Ruliology.CellularAutomata.Rule30GateTrap
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall

/-!
# The constant-tail separator is `Q01` on one class of free bits, and `BWH` is a death-time bound

`ConstantTailSeparator` (`SEP`, equivalent to `OrbitSeparator` by
`Rule30SeparatorEquivalences.separator_equivalence`) and `BWH` are open hypotheses on streams over
`Fin 4` (`Rule30WedgeBridge`). This module places them against `Rule30ZeroBoundary.Q01`.

**The chart.** For a zero-boundary start `L`, `zpair L t k` is the pair of depths `k, k + 1` at tick
`t`, coded by `Rule30SEPToPeriodTwo.encodePair`, and `zEnd L j = zpair L (2 j + 1) 1` is its endpoint
stream. If depth `1` is black at the even ticks, the inverse cone of `zEnd L` is the run of `L`:
`cone (zEnd L) n j = zpair L (2 j + n) (n + 2)` (`cone_chart`) and
`peelPow d (inverse (zEnd L)) t = zpair L t (2 d + t + 2)` (`peel_chart`), with finite-horizon forms
that need depth `1` black only up to a given even tick. This is the zero-boundary form of
`Rule30SEPToPeriodTwo.actual_cone_chart`; no right half enters. `zEnd (Theta f)` is `2` where `f` is
black and `1` where it is white (`zEnd_Theta`), so it is hard-core exactly when `f` has no two
adjacent white bits (`hardCore_endOf_iff`).

**`SEP` is `Q01` on that class.** `NoAdjWhite f`: no two adjacent free bits are white. `QN`: `Theta f`
is not finitely supported whenever `NoAdjWhite f`.
* `sep_iff_QN : ConstantTailSeparator ↔ QN`, `orbitSeparator_iff_QN`.
* `Q01_sep`: `Q01` implies `SEP`.
* `Q01_iff_sep_and`: `Q01` holds iff `SEP` holds and no `Theta f` whose free bits have two adjacent
  white bits infinitely often is finitely supported. So `SEP` is exactly the part of `Q01` for free
  bits that are eventually free of two adjacent whites.
* `sep_Q01Gap`: `SEP` implies `Rule30GateTrap.Q01Gap`, hence `CQ01Empty` (`sep_CQ01Empty`).

**Width-one layers.** `layerCol x0 r` is column `1` beside the alternating center
(`Rule30PeriodTwoCoupled.altCol`, black at the even ticks) with start cell `x0` and an arbitrary
column-`2` input `r`; `layerWord x0 r s` is its value at the white tick `2 s + 1`. Its words are
exactly the words with no two adjacent black bits (`layerWord_no11`, `layerWord_realizes`). `LR1`:
no such layer has a finitely supported forced left row `Theta (fun s => !layerWord x0 r s)`.
`LR1_iff_QN`, so `sep_iff_LR1`: `SEP` is `CQ01` with the right half relaxed to a single column whose
input from column `2` is free. At the black ticks a layer word is unconstrained
(`black_tick_control`). A right half is one such layer (`u_eq_layerWord`), so
`LR1_not_finSupp_Psi` and `sep_CQ01`: under `SEP`, `Rule30PeriodTwoSideways.Psi R` is infinite for
every right half `R`. This is `Rule30SEPToPeriodTwo.constant_separator_excludes_alternating` read in
the sideways coordinates.

**`BWH` is a death-time bound.** `SurvivesTo L N`: depth `1` is black at every even tick `≤ 2 N`.
For `n, ℓ ≥ 1`, a stream with a binary prefix of length `n + ℓ` and a constant wedge `c ∈ {2, 3}` of
length `ℓ` at depth `n` exists exactly when a start survives to tick `2 (n + ℓ)` whose last black cell
is at depth `2 n + 2` (`c = 2`), or at depth `2 n + 3` with the cell before it black (`c = 3`)
(`wedge_of_row_two`, `wedge_of_row_three`, `row_of_wedge`).
* `bwh_iff_deathBounds`: `BWH` holds iff every start of exact even width `W ≥ 16` dies by tick `2 W`
  and every start of exact odd width `W ≥ 17` whose top two cells are black dies by tick `2 W - 2`.
* `bwh_death`: under `BWH`, every start supported at depths `≤ W`, `W ≥ 16`, has a white depth-`1`
  cell at some even tick `≤ 2 W + 4`. Below `17` this is `Rule30ZeroBoundarySmall.q01_width_le_16`.
* `bwh_Q01`: `BWH` implies `Q01`.
* Controls: neither guard of `DeathBounds` can be dropped. The start `272125` has exact odd width
  `19`, a white cell at depth `18`, and survives to tick `36` (`odd_guard_control`,
  `odd_guard_needed`); the start `11083` has exact width `14` and survives to tick `30`
  (`even_threshold_control`, `even_threshold_needed`). Both are kernel checks on natural numbers.

None of `SEP`, `BWH` or `Q01` is proved here, and no prize problem is settled.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata
open Rule30WedgeBridge Rule30SeparatorBridge Rule30SeparatorEquivalences Rule30ZeroBoundary
open Rule30SEPToPeriodTwo (encodePair pair_inverse_table encode_xor_binary)
open Rule30PeriodTwoCoupled (altCol CQ01)

/-! ## The zero-boundary chart -/

/-- The pair of depths `k` and `k + 1` of the run from `L` at tick `t`. -/
def zpair (L : Nat → Bool) (t k : Nat) : Sym := encodePair (zrow L t k) (zrow L t (k + 1))

/-- The endpoint stream of `L`: the pair of depths `1, 2` at the odd tick `2 j + 1`. -/
def zEnd (L : Nat → Bool) (j : Nat) : Sym := zpair L (2 * j + 1) 1

/-- `phi` steps one pair back in depth, two in the run. -/
theorem zpair_back (L : Nat → Bool) (t k : Nat) :
    phi (zpair L t k) (zpair L (t + 1) (k + 1)) = zpair L t (k + 2) := by
  have h1 : zrow L (t + 1) (k + 1) = xor (zrow L t (k + 2)) (zrow L t (k + 1) || zrow L t k) :=
    zrow_succ L t k
  have h2 : zrow L (t + 1) (k + 1 + 1) =
      xor (zrow L t (k + 3)) (zrow L t (k + 2) || zrow L t (k + 1)) := zrow_succ L t (k + 1)
  show phi (encodePair (zrow L t k) (zrow L t (k + 1)))
      (encodePair (zrow L (t + 1) (k + 1)) (zrow L (t + 1) (k + 1 + 1))) =
    encodePair (zrow L t (k + 2)) (zrow L t (k + 2 + 1))
  rw [h1, h2]
  exact pair_inverse_table _ _ _ _

theorem boundary_encode : ∀ x y : Bool, boundary (encodePair (!x) (!y)) = encodePair x y := by
  decide

/-- At a tick where depth `1` is black, the boundary of the endpoint is the next pair down. -/
theorem zEnd_boundary (L : Nat → Bool) (j : Nat) (h : zrow L (2 * j) 1 = true) :
    boundary (zEnd L j) = zpair L (2 * j) 2 := by
  have h1 : zrow L (2 * j + 1) 1 = xor (zrow L (2 * j) 2) (zrow L (2 * j) 1 || zrow L (2 * j) 0) :=
    zrow_succ L (2 * j) 0
  have h2 : zrow L (2 * j + 1) 2 = xor (zrow L (2 * j) 3) (zrow L (2 * j) 2 || zrow L (2 * j) 1) :=
    zrow_succ L (2 * j) 1
  rw [h, Bool.true_or, Bool.xor_true] at h1
  rw [h, Bool.or_true, Bool.xor_true] at h2
  show boundary (encodePair (zrow L (2 * j + 1) 1) (zrow L (2 * j + 1) 2)) =
    encodePair (zrow L (2 * j) 2) (zrow L (2 * j) (2 + 1))
  rw [h1, h2]
  exact boundary_encode _ _

/-- **The cone chart, finite horizon.** -/
theorem cone_chart (L : Nat → Bool) (S : Nat) (hX : ∀ s, s ≤ S → zrow L (2 * s) 1 = true) :
    ∀ n j, j + n ≤ S → cone (zEnd L) n j = zpair L (2 * j + n) (n + 2) := by
  intro n
  induction n using Nat.strongRecOn with
  | ind n ih =>
    intro j hj
    match n with
    | 0 => exact zEnd_boundary L j (hX j (by omega))
    | 1 =>
      show phi (zEnd L j) (boundary (zEnd L (j + 1))) = _
      rw [zEnd_boundary L (j + 1) (hX (j + 1) (by omega))]
      have h := zpair_back L (2 * j + 1) 1
      rw [show 2 * (j + 1) = 2 * j + 1 + 1 by omega]
      exact h
    | n + 2 =>
      show phi (cone (zEnd L) n (j + 1)) (cone (zEnd L) (n + 1) (j + 1)) = _
      rw [ih n (by omega) (j + 1) (by omega), ih (n + 1) (by omega) (j + 1) (by omega)]
      have h := zpair_back L (2 * (j + 1) + n) (n + 2)
      rw [show 2 * (j + 1) + (n + 1) = 2 * (j + 1) + n + 1 by omega,
        show n + 1 + 2 = n + 2 + 1 by omega, h,
        show 2 * (j + 1) + n = 2 * j + (n + 2) by omega]

/-- **The peel chart, finite horizon.** -/
theorem peel_chart (L : Nat → Bool) (S : Nat) (hX : ∀ s, s ≤ S → zrow L (2 * s) 1 = true) :
    ∀ d t, t + d ≤ S → peelPow d (inverse (zEnd L)) t = zpair L t (2 * d + t + 2) := by
  intro d
  induction d with
  | zero =>
    intro t ht
    simpa only [peelPow, inverse, Nat.mul_zero, Nat.zero_add, Nat.add_zero] using
      cone_chart L S hX t 0 (by omega)
  | succ d ih =>
    intro t ht
    show phi (peelPow d (inverse (zEnd L)) t) (peelPow d (inverse (zEnd L)) (t + 1)) = _
    rw [ih t (by omega), ih (t + 1) (by omega)]
    have h := zpair_back L t (2 * d + t + 2)
    rw [show 2 * d + (t + 1) + 2 = 2 * d + t + 2 + 1 by omega, h,
      show 2 * d + t + 2 + 2 = 2 * (d + 1) + t + 2 by omega]

theorem cone_chart_inX {L : Nat → Bool} (hX : InX L) (n j : Nat) :
    cone (zEnd L) n j = zpair L (2 * j + n) (n + 2) :=
  cone_chart L (j + n) (fun s _ => hX s) n j (Nat.le_refl _)

theorem peel_chart_inX {L : Nat → Bool} (hX : InX L) (d t : Nat) :
    peelPow d (inverse (zEnd L)) t = zpair L t (2 * d + t + 2) :=
  peel_chart L (t + d) (fun s _ => hX s) d t (Nat.le_refl _)

/-- The endpoint is binary wherever depth `1` is black at the next even tick. -/
theorem zEnd_binary (L : Nat → Bool) (j : Nat) (h : zrow L (2 * j + 2) 1 = true) :
    binary (zEnd L j) := by
  have e : zrow L (2 * j + 2) 1 =
      xor (zrow L (2 * j + 1) 2) (zrow L (2 * j + 1) 1 || zrow L (2 * j + 1) 0) :=
    zrow_succ L (2 * j + 1) 0
  rw [zrow_wall, Bool.or_false, h] at e
  exact encode_xor_binary _ _ e.symm

/-! ## The endpoint of `Theta f` and hard-core streams -/

/-- The binary stream of free bits `f`: `2` at a black bit, `1` at a white bit. -/
def endOf (f : Nat → Bool) (j : Nat) : Sym := if f j = true then 2 else 1

/-- No two adjacent free bits are white. -/
def NoAdjWhite (f : Nat → Bool) : Prop := ∀ s, f s = true ∨ f (s + 1) = true

theorem zEnd_Theta (f : Nat → Bool) : zEnd (Theta f) = endOf f := by
  funext j
  have e : zrow (Theta f) (2 * j + 2) 1 =
      xor (zrow (Theta f) (2 * j + 1) 2) (zrow (Theta f) (2 * j + 1) 1 ||
        zrow (Theta f) (2 * j + 1) 0) :=
    zrow_succ (Theta f) (2 * j + 1) 0
  have hX : zrow (Theta f) (2 * j + 2) 1 = true := by
    rw [show 2 * j + 2 = 2 * (j + 1) by omega]; exact Theta_inX f (j + 1)
  rw [zrow_wall, Bool.or_false, hX, Theta_free] at e
  show encodePair (zrow (Theta f) (2 * j + 1) 1) (zrow (Theta f) (2 * j + 1) 2) = endOf f j
  rw [Theta_free]
  unfold endOf
  revert e
  cases f j <;> cases zrow (Theta f) (2 * j + 1) 2 <;> decide

theorem hardCore_endOf_iff (f : Nat → Bool) : HardCore (endOf f) ↔ NoAdjWhite f := by
  constructor
  · intro ⟨_, h⟩ s
    have hs := h s
    unfold endOf at hs
    cases h0 : f s <;> cases h1 : f (s + 1) <;> simp_all
  · intro h
    refine ⟨fun i => ?_, fun i => ?_⟩
    · unfold endOf binary; cases f i <;> simp
    · unfold endOf
      rcases h i with h0 | h1
      · simp [h0]
      · simp [h1]

/-- Every hard-core stream is `endOf f` for free bits `f` with no two adjacent whites. -/
theorem hardCore_eq_endOf {e : Nat → Sym} (hh : HardCore e) :
    ∃ f, e = endOf f ∧ NoAdjWhite f := by
  have he : e = endOf (fun j => decide (e j = 2)) := by
    funext j
    unfold endOf
    rcases hh.1 j with h | h <;> simp [h]
  exact ⟨_, he, (hardCore_endOf_iff _).1 (by rw [← he]; exact hh)⟩

/-- Two ZBL steps per free bit: the row at tick `2 m` is `Theta` of the shifted free bits. -/
theorem zrow_Theta_even (f : Nat → Bool) :
    ∀ m, zrow (Theta f) (2 * m) = Theta (fun s => f (s + m)) := by
  intro m
  induction m with
  | zero => rw [Nat.mul_zero, zrow_zero_self (Theta_wall f)]; rfl
  | succ m ih =>
    funext k
    rw [show 2 * (m + 1) = 2 * m + 2 by omega, zrow_shift, ih, two_step_shift]
    show Theta (fun s => f (s + 1 + m)) k = Theta (fun s => f (s + (m + 1))) k
    rw [show (fun s => f (s + 1 + m)) = (fun s => f (s + (m + 1))) from
      funext fun s => by rw [show s + 1 + m = s + (m + 1) by omega]]

/-! ## `SEP` is `Q01` on free bits with no two adjacent whites -/

/-- **`QN`** (open): `Theta f` is not finitely supported when no two adjacent free bits are white. -/
def QN : Prop := ∀ f, NoAdjWhite f → ¬ FinSupp (Theta f)

theorem sep_QN (hs : ConstantTailSeparator) : QN := by
  intro f hf ⟨W, hW⟩
  have hh : HardCore (zEnd (Theta f)) := by
    rw [zEnd_Theta]; exact (hardCore_endOf_iff f).2 hf
  apply separator_excludes_finite_peel_rank hs _ hh W 0
  intro t _
  rw [peel_chart_inX (Theta_inX f)]
  unfold zpair
  rw [zrow_fin hW t (2 * W + t + 2) (by omega), zrow_fin hW t (2 * W + t + 2 + 1) (by omega)]
  rfl

theorem phi_const_tail : ∀ c : Sym, constantTail c → phi c c = 0 := by
  unfold constantTail; decide

theorem phi_zero_zero : phi 0 0 = 0 := by decide

/-- Peels of an eventually constant tail `c ∈ {2, 3}` vanish from the same index on. -/
theorem peel_tail_zero {x : Nat → Sym} {c : Sym} (hc : constantTail c) {N : Nat}
    (hx : ∀ t, N ≤ t → x t = c) : ∀ d t, N ≤ t → peelPow (d + 1) x t = 0 := by
  intro d
  induction d with
  | zero =>
    intro t ht
    show phi (x t) (x (t + 1)) = 0
    rw [hx t ht, hx (t + 1) (by omega)]
    exact phi_const_tail c hc
  | succ d ih =>
    intro t ht
    show phi (peelPow (d + 1) x t) (peelPow (d + 1) x (t + 1)) = 0
    rw [ih t ht, ih (t + 1) (by omega)]
    exact phi_zero_zero

theorem encode_zero : ∀ a b : Bool, encodePair a b = 0 → a = false ∧ b = false := by decide

theorem QN_sep (hq : QN) : ConstantTailSeparator := by
  intro c hc e hh ⟨N, hN⟩
  obtain ⟨f, rfl, hf⟩ := hardCore_eq_endOf hh
  rw [← zEnd_Theta] at hN
  have hz := peel_tail_zero hc hN
  apply hq (fun s => f (s + N)) (fun s => by
    have h := hf (s + N); rwa [show s + N + 1 = s + 1 + N by omega] at h)
  refine ⟨2 * N + 3, fun k hk => ?_⟩
  rw [← zrow_Theta_even f N]
  obtain ⟨d, hd⟩ : ∃ d, k = 2 * (d + 1) + 2 * N + 2 ∨ k = 2 * (d + 1) + 2 * N + 3 :=
    ⟨(k - 2 * N - 4) / 2, by omega⟩
  have hp := hz d (2 * N) (by omega)
  rw [peel_chart_inX (Theta_inX f)] at hp
  have h2 := encode_zero _ _ hp
  rcases hd with rfl | rfl
  · exact h2.1
  · exact h2.2

/-- **`SEP` is `QN`.** -/
theorem sep_iff_QN : ConstantTailSeparator ↔ QN := ⟨sep_QN, QN_sep⟩

theorem orbitSeparator_iff_QN : OrbitSeparator ↔ QN := separator_equivalence.trans sep_iff_QN

/-- `Q01` implies `SEP`. -/
theorem Q01_sep (hQ : Q01) : ConstantTailSeparator :=
  QN_sep fun f _ => Q01_iff_Theta.1 hQ f

/-- `QN` reaches free bits that are free of two adjacent whites from some index on. -/
theorem QN_eventually (hq : QN) (f : Nat → Bool) (s0 : Nat)
    (h : ∀ s, s0 ≤ s → f s = true ∨ f (s + 1) = true) : ¬ FinSupp (Theta f) := by
  rintro ⟨W, hW⟩
  apply hq (fun s => f (s + s0)) (fun s => by
    have h' := h (s + s0) (by omega); rwa [show s + s0 + 1 = s + 1 + s0 by omega] at h')
  refine ⟨W + 2 * s0, fun k hk => ?_⟩
  rw [← zrow_Theta_even f s0]
  exact zrow_fin hW (2 * s0) k (by omega)

/-- The free bits have two adjacent white bits infinitely often. -/
def InfWhitePairs (f : Nat → Bool) : Prop := ∀ s0, ∃ s, s0 ≤ s ∧ f s = false ∧ f (s + 1) = false

/-- **`Q01` is `SEP` together with the free bits that keep meeting two adjacent whites.** -/
theorem Q01_iff_sep_and :
    Q01 ↔ ConstantTailSeparator ∧ ∀ f, InfWhitePairs f → ¬ FinSupp (Theta f) := by
  constructor
  · intro hQ
    exact ⟨Q01_sep hQ, fun f _ => Q01_iff_Theta.1 hQ f⟩
  · rintro ⟨hs, hi⟩
    refine Q01_iff_Theta.2 fun f hfin => ?_
    by_cases hw : InfWhitePairs f
    · exact hi f hw hfin
    · have hex : ∃ s0, ∀ s, s0 ≤ s → ¬ (f s = false ∧ f (s + 1) = false) := by
        apply Classical.byContradiction
        intro hne
        apply hw
        intro s0
        apply Classical.byContradiction
        intro hne2
        exact hne ⟨s0, fun s hs h => hne2 ⟨s, hs, h.1, h.2⟩⟩
      obtain ⟨s0, hs0⟩ := hex
      refine QN_eventually (sep_QN hs) f s0 (fun s hs => ?_) hfin
      cases h : f s
      · cases h' : f (s + 1)
        · exact absurd ⟨h, h'⟩ (hs0 s hs)
        · exact Or.inr rfl
      · exact Or.inl rfl

/-- **`SEP` implies `Q01Gap`.** -/
theorem sep_Q01Gap (hs : ConstantTailSeparator) : Rule30GateTrap.Q01Gap := by
  rintro L ⟨W, hW⟩ hX ⟨s0, hs0⟩
  have hT := Theta_unique hX (f := fun s => zrow L (2 * s + 1) 1) (fun _ => rfl)
  apply QN_eventually (sep_QN hs) (fun s => zrow L (2 * s + 1) 1) s0
  · intro s hs
    show zrow L (2 * s + 1) 1 = true ∨ zrow L (2 * (s + 1) + 1) 1 = true
    cases h : zrow L (2 * s + 1) 1
    · right
      have hg := hs0 s hs
      unfold Rule30GateTrap.GapOK at hg
      have h' : (!zrow L (2 * (s + 1) + 1) 1) = false := by
        rcases hg (by simp [h]) with ⟨h1, _⟩ | ⟨h1, _⟩ <;> exact h1
      simpa using h'
    · exact Or.inl rfl
  · refine ⟨W, fun k hk => ?_⟩
    rw [← hT, zrow_zero_of_pos L (k := k) (by omega)]
    exact hW k hk

theorem sep_CQ01Empty (hs : ConstantTailSeparator) : Rule30PeriodTwoSideways.CQ01Empty :=
  Rule30GateTrap.CQ01Empty_of_Q01Gap (sep_Q01Gap hs)

/-! ## Width-one layers beside the alternating column -/

/-- Column `1` beside the alternating center, with start cell `x0` and column-`2` input `r`. -/
def layerCol (x0 : Bool) (r : Nat → Bool) : Nat → Bool
  | 0 => x0
  | t + 1 => xor (altCol t) (layerCol x0 r t || r t)

/-- Column `1` of the layer at the white tick `2 s + 1`. -/
def layerWord (x0 : Bool) (r : Nat → Bool) (s : Nat) : Bool := layerCol x0 r (2 * s + 1)

theorem layerCol_odd (x0 : Bool) (r : Nat → Bool) (s : Nat) :
    layerCol x0 r (2 * s + 1) = !(layerCol x0 r (2 * s) || r (2 * s)) := by
  show xor (altCol (2 * s)) _ = _
  rw [Rule30PeriodTwoSideways.altCol_even, Bool.true_xor]

theorem layerCol_even (x0 : Bool) (r : Nat → Bool) (s : Nat) :
    layerCol x0 r (2 * s + 2) = (layerCol x0 r (2 * s + 1) || r (2 * s + 1)) := by
  show xor (altCol (2 * s + 1)) _ = _
  rw [Rule30PeriodTwoSideways.altCol_odd, Bool.false_xor]

/-- A layer word has no two adjacent black bits. -/
theorem layerWord_no11 (x0 : Bool) (r : Nat → Bool) (s : Nat) :
    layerWord x0 r s = true → layerWord x0 r (s + 1) = false := by
  intro h
  unfold layerWord at *
  rw [layerCol_odd, show 2 * (s + 1) = 2 * s + 2 by omega, layerCol_even, h]
  rfl

/-- Every word with no two adjacent black bits is a layer word. -/
theorem layerWord_realizes (w : Nat → Bool) (hw : ∀ s, w s = true → w (s + 1) = false) :
    ∃ x0 r, ∀ s, layerWord x0 r s = w s := by
  obtain ⟨r, hr⟩ : ∃ r : Nat → Bool, ∀ t, r t = if t % 2 = 0 then !w (t / 2) else false :=
    ⟨_, fun _ => rfl⟩
  have hr0 (s : Nat) : r (2 * s) = !w s := by
    rw [hr, ite_eq_left (show 2 * s % 2 = 0 by omega), show 2 * s / 2 = s by omega]
  have hr1 (s : Nat) : r (2 * s + 1) = false := by
    rw [hr, ite_eq_right (show ¬ ((2 * s + 1) % 2 = 0) by omega)]
  have key : ∀ s, layerCol false r (2 * s + 1) = w s ∧ layerCol false r (2 * s + 2) = w s := by
    intro s
    induction s with
    | zero =>
      have e0 : r 0 = !w 0 := hr0 0
      have e1 : r 1 = false := hr1 0
      have h1 : layerCol false r 1 = w 0 := by
        show xor (altCol 0) (false || r 0) = w 0
        rw [e0]
        cases w 0 <;> rfl
      refine ⟨h1, ?_⟩
      show xor (altCol 1) (layerCol false r 1 || r 1) = w 0
      rw [h1, e1]
      cases w 0 <;> rfl
    | succ s ih =>
      have h1 : layerCol false r (2 * (s + 1) + 1) = w (s + 1) := by
        rw [layerCol_odd, show 2 * (s + 1) = 2 * s + 2 by omega, ih.2,
          show 2 * s + 2 = 2 * (s + 1) by omega, hr0]
        cases hs : w s
        · cases w (s + 1) <;> rfl
        · rw [hw s hs]; rfl
      refine ⟨h1, ?_⟩
      rw [layerCol_even, hr1, Bool.or_false, h1]
  exact ⟨false, r, fun s => (key s).1⟩

/-- **`LR1`** (open): no width-one layer beside the alternating column, with any start cell and any
column-`2` input, has a finitely supported forced left row. -/
def LR1 : Prop := ∀ x0 r, ¬ FinSupp (Theta fun s => !layerWord x0 r s)

theorem LR1_iff_QN : LR1 ↔ QN := by
  constructor
  · intro hl f hf
    obtain ⟨x0, r, hr⟩ := layerWord_realizes (fun s => !f s) (fun s hs => by
      rcases hf s with h | h
      · simp [h] at hs
      · simp [h])
    have he : (fun s => !layerWord x0 r s) = f := funext fun s => by rw [hr]; simp
    rw [← he]
    exact hl x0 r
  · intro hq x0 r
    apply hq
    intro s
    show (!layerWord x0 r s) = true ∨ (!layerWord x0 r (s + 1)) = true
    cases h : layerWord x0 r s
    · exact Or.inl rfl
    · right
      simp [layerWord_no11 x0 r s h]

theorem sep_iff_LR1 : ConstantTailSeparator ↔ LR1 := sep_iff_QN.trans LR1_iff_QN.symm

/-- **Control: the white ticks matter.** At the black ticks a layer can be black twice running. -/
theorem black_tick_control :
    layerCol false (fun _ => true) 2 = true ∧ layerCol false (fun _ => true) 4 = true := by decide

/-- Column `1` of a right half driven by the alternating center is a width-one layer whose
column-`2` input is the right half's own column `2`. -/
theorem drv_col1_eq_layerCol (R : Nat → Bool) :
    ∀ t, Rule30Ether.drv altCol R t 1 =
      layerCol (R 1) (fun t => Rule30Ether.drv altCol R t 2) t := by
  intro t
  induction t with
  | zero => exact Rule30Ether.drv_init altCol R 1 (by omega)
  | succ t ih =>
    show Rule30Jen.rule (Rule30Ether.drv altCol R t 0) (Rule30Ether.drv altCol R t 1)
        (Rule30Ether.drv altCol R t 2) = _
    rw [Rule30Ether.drv_col0, ih]
    rfl

theorem u_eq_layerWord (R : Nat → Bool) (s : Nat) :
    Rule30PeriodTwoSideways.u R s =
      layerWord (R 1) (fun t => Rule30Ether.drv altCol R t 2) s :=
  drv_col1_eq_layerCol R (2 * s + 1)

/-- Under `LR1`, hence under `SEP`, `Psi R` is infinite for every right half `R`. -/
theorem LR1_not_finSupp_Psi (hl : LR1) (R : Nat → Bool) :
    ¬ FinSupp (Rule30PeriodTwoSideways.Psi R) := by
  have h := hl (R 1) (fun t => Rule30Ether.drv altCol R t 2)
  have he : (fun s => !Rule30PeriodTwoSideways.u R s) =
      (fun s => !layerWord (R 1) (fun t => Rule30Ether.drv altCol R t 2) s) :=
    funext fun s => by rw [u_eq_layerWord]
  unfold Rule30PeriodTwoSideways.Psi
  rw [he]
  exact h

theorem sep_CQ01 (hs : ConstantTailSeparator) : CQ01 :=
  Rule30PeriodTwoSideways.CQ01_iff_Psi.2 fun R _ => LR1_not_finSupp_Psi (sep_iff_LR1.1 hs) R

/-! ## `BWH` is a death-time bound -/

/-- Depth `1` is black at every even tick `≤ 2 N`. -/
def SurvivesTo (L : Nat → Bool) (N : Nat) : Prop := ∀ s, s ≤ N → zrow L (2 * s) 1 = true

/-- The last black cell of `L` is at depth `m`. -/
def ExactWidth (L : Nat → Bool) (m : Nat) : Prop := L m = true ∧ ∀ k, m < k → L k = false

theorem encode_two : ∀ a b : Bool, encodePair a b = 2 → a = true ∧ b = false := by decide
theorem encode_three : ∀ a b : Bool, encodePair a b = 3 → a = true ∧ b = true := by decide

/-- After one tick the cell below the edge is black too. -/
theorem below_edge {L : Nat → Bool} {m : Nat} (hm : 1 ≤ m) (hw : ExactWidth L m) (t : Nat) :
    zrow L (t + 1) (m + t) = true := by
  obtain ⟨j, hj⟩ : ∃ j, m + t = j + 1 := ⟨m + t - 1, by omega⟩
  have he := zrow_edge hm hw.1 hw.2 t
  rw [hj, zrow_succ, he.2 (j + 2) (by omega), ← hj, he.1, Bool.true_or]
  rfl

/-- The binary prefix of the endpoint, from survival. -/
theorem zEnd_binaryPrefix {L : Nat → Bool} {N : Nat} (hS : SurvivesTo L N) :
    BinaryPrefix (zEnd L) N := fun i hi =>
  zEnd_binary L i (by rw [show 2 * i + 2 = 2 * (i + 1) by omega]; exact hS (i + 1) (by omega))

/-- **A surviving start of exact width `2 n + 2` has a constant wedge `2`.** -/
theorem wedge_of_row_two {L : Nat → Bool} {n l : Nat} (hw : ExactWidth L (2 * n + 2))
    (hS : SurvivesTo L (n + l)) :
    BinaryPrefix (zEnd L) (n + l) ∧ ConstantWedge n l 2 (zEnd L) := by
  refine ⟨zEnd_binaryPrefix hS, fun t ht => ?_⟩
  unfold wedge
  rw [peel_chart L (n + l) hS n t (by omega)]
  have he := zrow_edge (by omega) hw.1 hw.2 t
  unfold zpair
  rw [show 2 * n + t + 2 = 2 * n + 2 + t by omega, he.1, he.2 _ (by omega)]
  rfl

/-- **A surviving start of exact width `2 n + 3` with its top two cells black has a constant wedge
`3`.** -/
theorem wedge_of_row_three {L : Nat → Bool} {n l : Nat} (hw : ExactWidth L (2 * n + 3))
    (h2 : L (2 * n + 2) = true) (hS : SurvivesTo L (n + l)) :
    BinaryPrefix (zEnd L) (n + l) ∧ ConstantWedge n l 3 (zEnd L) := by
  refine ⟨zEnd_binaryPrefix hS, fun t ht => ?_⟩
  unfold wedge
  rw [peel_chart L (n + l) hS n t (by omega)]
  have he := zrow_edge (by omega) hw.1 hw.2 t
  have hb : zrow L t (2 * n + t + 2) = true := by
    cases t with
    | zero => rw [zrow_zero_of_pos L (by omega)]; exact h2
    | succ t =>
      rw [show 2 * n + (t + 1) + 2 = 2 * n + 3 + t by omega]
      exact below_edge (by omega) hw t
  unfold zpair
  rw [hb, show 2 * n + t + 2 + 1 = 2 * n + 3 + t by omega, he.1]
  rfl

/-- **The converse dictionary.** A stream with a binary prefix of length `n + l` and a constant
wedge `c ∈ {2, 3}` of length `l ≥ 1` at depth `n` gives a start that survives to tick `2 (n + l)`, of
exact width `2 n + 2` if `c = 2` and of exact width `2 n + 3` with its top two cells black if
`c = 3`. -/
theorem row_of_wedge {e : Nat → Sym} {n l : Nat} {c : Sym} (hl : 1 ≤ l) (hc : constantTail c)
    (hb : BinaryPrefix e (n + l)) (hw : ConstantWedge n l c e) :
    ∃ L, SurvivesTo L (n + l) ∧
      ((c = 2 ∧ ExactWidth L (2 * n + 2)) ∨
        (c = 3 ∧ ExactWidth L (2 * n + 3) ∧ L (2 * n + 2) = true)) := by
  obtain ⟨f, hf⟩ : ∃ f : Nat → Bool, ∀ j, f j = decide (e j = 2) := ⟨_, fun _ => rfl⟩
  have hagree : ∀ i, i < n + l → zEnd (Theta f) i = e i := by
    intro i hi
    rw [zEnd_Theta]
    unfold endOf
    rcases hb i hi with h | h <;> simp [hf, h]
  have hX := Theta_inX f
  -- the wedge of the endpoint of `Theta f` is the wedge of `e`
  have hwc : ∀ t, t < l → zpair (Theta f) t (2 * n + t + 2) = c := by
    intro t ht
    rw [← peel_chart_inX hX n t, ← hw t ht]
    exact wedge_prefix _ _ (n + l) n t hagree (by omega)
  -- the constant wedge forces zero pairs below it, through depth `2 (n + l) + 1`
  have hx : ∀ t, t < l → peelPow n (inverse (zEnd (Theta f))) t = c := by
    intro t ht; rw [peel_chart_inX hX]; exact hwc t ht
  have key : ∀ i t, t + i + 1 < l →
      peelPow (n + 1 + i) (inverse (zEnd (Theta f))) t = 0 := by
    intro i
    induction i with
    | zero =>
      intro t ht
      show phi (peelPow n (inverse (zEnd (Theta f))) t)
        (peelPow n (inverse (zEnd (Theta f))) (t + 1)) = 0
      rw [hx t (by omega), hx (t + 1) (by omega)]
      exact phi_const_tail c hc
    | succ i ih =>
      intro t ht
      show phi (peelPow (n + 1 + i) (inverse (zEnd (Theta f))) t)
        (peelPow (n + 1 + i) (inverse (zEnd (Theta f))) (t + 1)) = 0
      rw [ih t (by omega), ih (t + 1) (by omega)]
      exact phi_zero_zero
  have hz : ∀ d, d + 1 < l → zpair (Theta f) 0 (2 * (n + 1 + d) + 2) = 0 := by
    intro d hd
    have h := key d 0 (by omega)
    rw [peel_chart_inX hX] at h
    exact h
  have hdeep : ∀ k, 2 * n + 4 ≤ k → k ≤ 2 * (n + l) + 1 → Theta f k = false := by
    intro k hk1 hk2
    obtain ⟨d, hd⟩ : ∃ d, k = 2 * (n + 1 + d) + 2 ∨ k = 2 * (n + 1 + d) + 2 + 1 :=
      ⟨(k - 2 * n - 4) / 2, by omega⟩
    have h0 := encode_zero _ _ (hz d (by omega))
    rw [zrow_zero_of_pos (Theta f) (show 1 ≤ 2 * (n + 1 + d) + 2 by omega),
      zrow_zero_of_pos (Theta f) (show 1 ≤ 2 * (n + 1 + d) + 2 + 1 by omega)] at h0
    rcases hd with rfl | rfl
    · exact h0.1
    · exact h0.2
  have htop : encodePair (Theta f (2 * n + 2)) (Theta f (2 * n + 3)) = c := by
    have h : zpair (Theta f) 0 (2 * n + 2) = c := hwc 0 hl
    unfold zpair at h
    rw [zrow_zero_of_pos (Theta f) (show 1 ≤ 2 * n + 2 by omega),
      zrow_zero_of_pos (Theta f) (show 1 ≤ 2 * n + 2 + 1 by omega)] at h
    exact h
  -- a truncation that agrees with `Theta f` through depth `2 (n + l) + 1` survives
  have surv : ∀ D, (∀ k, D < k → k ≤ 2 * (n + l) + 1 → Theta f k = false) →
      SurvivesTo (truncate (Theta f) D) (n + l) := by
    intro D hzD s hs
    have hag : ∀ i, 1 ≤ i → i ≤ 1 + 2 * s → truncate (Theta f) D i = Theta f i := by
      intro i _ h2
      unfold truncate
      by_cases hi : i ≤ D
      · rw [decide_eq_true hi, Bool.and_true]
      · rw [decide_eq_false hi, Bool.and_false]
        exact (hzD i (by omega) (by omega)).symm
    rw [zrow_light_cone (2 * s) 1 hag]
    exact hX s
  rcases (show c = 2 ∨ c = 3 from hc) with rfl | rfl
  · obtain ⟨ht1, ht2⟩ := encode_two _ _ htop
    refine ⟨truncate (Theta f) (2 * n + 2), ?_, Or.inl ⟨rfl, ?_, ?_⟩⟩
    · apply surv
      intro k hk1 hk2
      by_cases hk : k = 2 * n + 3
      · rw [hk]; exact ht2
      · exact hdeep k (by omega) hk2
    · unfold truncate; simp [ht1]
    · intro k hk; unfold truncate; simp [show ¬ k ≤ 2 * n + 2 by omega]
  · obtain ⟨ht1, ht2⟩ := encode_three _ _ htop
    refine ⟨truncate (Theta f) (2 * n + 3), ?_, Or.inr ⟨rfl, ⟨?_, ?_⟩, ?_⟩⟩
    · exact surv _ (fun k hk1 hk2 => hdeep k (by omega) hk2)
    · unfold truncate; simp [ht2]
    · intro k hk; unfold truncate; simp [show ¬ k ≤ 2 * n + 3 by omega]
    · unfold truncate; simp [ht1]

/-- The exact-width death bounds that `BWH` is equivalent to: a start of exact even width
`W = 2 n + 2 ≥ 16` does not survive to tick `2 W`, and a start of exact odd width
`W = 2 n + 3 ≥ 17` whose top two cells are black does not survive to tick `2 W - 2`. -/
def DeathBounds : Prop :=
  (∀ n, 7 ≤ n → ∀ L, ExactWidth L (2 * n + 2) → ¬ SurvivesTo L (2 * n + 2)) ∧
  (∀ n, 7 ≤ n → ∀ L, ExactWidth L (2 * n + 3) → L (2 * n + 2) = true →
    ¬ SurvivesTo L (2 * n + 2))

/-- **`BWH` is a death-time bound.** -/
theorem bwh_iff_deathBounds : BWH ↔ DeathBounds := by
  constructor
  · intro hb
    refine ⟨fun n hn L hw hS => ?_, fun n hn L hw h2 hS => ?_⟩
    · rw [show 2 * n + 2 = n + (n + 2) by omega] at hS
      obtain ⟨h1, h2⟩ := wedge_of_row_two hw hS
      exact hb n hn 2 (Or.inl rfl) (zEnd L) (by rwa [show 2 * n + 2 = n + (n + 2) by omega]) h2
    · rw [show 2 * n + 2 = n + (n + 2) by omega] at hS
      obtain ⟨h1, h3⟩ := wedge_of_row_three hw h2 hS
      exact hb n hn 3 (Or.inr rfl) (zEnd L) (by rwa [show 2 * n + 2 = n + (n + 2) by omega]) h3
  · rintro ⟨hd2, hd3⟩ n hn c hc e hb hw
    obtain ⟨L, hS, hcase⟩ := row_of_wedge (n := n) (l := n + 2) (by omega) hc
      (by rwa [show n + (n + 2) = 2 * n + 2 by omega]) hw
    rw [show n + (n + 2) = 2 * n + 2 by omega] at hS
    rcases hcase with ⟨_, hw2⟩ | ⟨_, hw3, h2⟩
    · exact hd2 n hn L hw2 hS
    · exact hd3 n hn L hw3 h2 hS

/-- **Under `BWH`, `D(W) ≤ 2 W + 4` for `W ≥ 16`**: every start supported at depths `≤ W` has a white
depth-`1` cell at some even tick `≤ 2 W + 4`. -/
theorem bwh_death (hb : BWH) (W : Nat) (hW : 16 ≤ W) (L : Nat → Bool)
    (hL : ∀ k, W < k → L k = false) : ∃ s, s ≤ W + 2 ∧ zrow L (2 * s) 1 = false := by
  obtain ⟨hd2, hd3⟩ := bwh_iff_deathBounds.1 hb
  apply Classical.byContradiction
  intro hno
  have hS : SurvivesTo L (W + 2) := fun s hs => by
    cases h : zrow L (2 * s) 1
    · exact absurd ⟨s, hs, h⟩ hno
    · rfl
  have h1 : L 1 = true := by
    have h := hS 0 (by omega)
    rwa [Nat.mul_zero, zrow_zero_of_pos L (Nat.le_refl 1)] at h
  obtain ⟨m, hm1, hmL, hmfin⟩ := last_black h1 W hL
  have hmW : m ≤ W := by
    apply Classical.byContradiction
    intro h
    rw [hL m (by omega)] at hmL
    exact Bool.noConfusion hmL
  rcases Nat.lt_or_ge m 17 with hsmall | hbig
  · obtain ⟨j, hj, hz⟩ := Rule30ZeroBoundarySmall.q01_width_le_16 L (fun k hk => hmfin k (by omega))
    rw [hS j (by omega)] at hz
    exact Bool.noConfusion hz
  · obtain ⟨n, hn⟩ : ∃ n, m = 2 * n ∨ m = 2 * n + 1 := ⟨m / 2, by omega⟩
    rcases hn with hn | hn
    · -- even width `m = 2 (n - 1) + 2`
      exact hd2 (n - 1) (by omega) L
        ⟨by rw [show 2 * (n - 1) + 2 = m by omega]; exact hmL, fun k hk => hmfin k (by omega)⟩
        (fun s hs => hS s (by omega))
    · -- odd width `m = 2 n + 1`: two ticks later the top two cells are black
      have hw : ExactWidth L m := ⟨hmL, hmfin⟩
      have he := zrow_edge hm1 hmL hmfin 2
      apply hd3 n (by omega) (zrow L 2)
        ⟨by rw [show 2 * n + 3 = m + 2 by omega]; exact he.1, fun k hk => he.2 k (by omega)⟩
        (by rw [show 2 * n + 2 = m + 1 by omega]; exact below_edge hm1 hw 1)
      intro s hs
      rw [← zrow_shift, show 2 + 2 * s = 2 * (s + 1) by omega]
      exact hS (s + 1) (by omega)

/-! ## Controls: the guards of `DeathBounds` cannot be dropped -/

theorem rowOfNat_high {Y W : Nat} (h : Y < 2 ^ W) :
    ∀ k, W < k → IntegerForm.rowOfNat Y k = false := by
  intro k hk
  obtain ⟨i, rfl⟩ : ∃ i, k = i + 1 := ⟨k - 1, by omega⟩
  exact Nat.testBit_lt_two_pow
    (Nat.lt_of_lt_of_le h (Nat.pow_le_pow_right (by omega) (by omega)))

/-- Depth `1` is black at the even ticks `≤ 2 N`, checked on the natural number of the start. -/
def survCheck (Y N : Nat) : Bool :=
  (List.range (N + 1)).all fun s => (IntegerForm.iter IntegerForm.F (2 * s) Y).testBit 0

theorem survCheck_sound {Y N : Nat} (h : survCheck Y N = true) :
    SurvivesTo (IntegerForm.rowOfNat Y) N := by
  intro s hs
  rw [IntegerForm.zrow_rowOfNat_col1]
  unfold survCheck at h
  rw [List.all_eq_true] at h
  exact h s (List.mem_range.2 (by omega))

/-- **Control: the top-two guard.** The start `272125` (binary `1000010011011111101`) has exact odd
width `19 = 2 · 8 + 3`, a white cell at depth `18`, and survives to tick `36 = 2 · 19 - 2`. -/
theorem odd_guard_control :
    ExactWidth (IntegerForm.rowOfNat 272125) 19 ∧ IntegerForm.rowOfNat 272125 18 = false ∧
      SurvivesTo (IntegerForm.rowOfNat 272125) 18 :=
  ⟨⟨by decide, rowOfNat_high (W := 19) (by decide)⟩, by decide,
    survCheck_sound (by decide +kernel)⟩

theorem odd_guard_needed :
    ¬ ∀ n, 7 ≤ n → ∀ L, ExactWidth L (2 * n + 3) → ¬ SurvivesTo L (2 * n + 2) :=
  fun h => h 8 (by omega) _ odd_guard_control.1 odd_guard_control.2.2

/-- **Control: the threshold `n ≥ 7`.** The start `11083` has exact even width `14 = 2 · 6 + 2` and
survives to tick `30`, past `2 · 14`. -/
theorem even_threshold_control :
    ExactWidth (IntegerForm.rowOfNat 11083) 14 ∧ SurvivesTo (IntegerForm.rowOfNat 11083) 15 :=
  ⟨⟨by decide, rowOfNat_high (W := 14) (by decide)⟩, survCheck_sound (by decide +kernel)⟩

theorem even_threshold_needed :
    ¬ ∀ L, ExactWidth L (2 * 6 + 2) → ¬ SurvivesTo L (2 * 6 + 2) :=
  fun h => h _ even_threshold_control.1 fun s hs => even_threshold_control.2 s (by omega)

/-- **`BWH` implies `Q01`.** -/
theorem bwh_Q01 (hb : BWH) : Q01 := by
  rintro L ⟨W, hW⟩ hX
  obtain ⟨s, _, hs⟩ := bwh_death hb (W + 16) (by omega) L (fun k hk => hW k (by omega))
  rw [hX s] at hs
  exact Bool.noConfusion hs

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30WedgeBridge", "Ruliology.CellularAutomata.Rule30SeparatorBridge", "Ruliology.CellularAutomata.Rule30ZeroBoundary"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"cone_chart", "peel_chart", "hardCore_endOf_iff", "sep_iff_QN", "orbitSeparator_iff_QN", "Q01_sep", "Q01_iff_sep_and", "sep_Q01Gap", "sep_CQ01Empty", "sep_iff_LR1", "layerWord_realizes", "sep_CQ01", "bwh_iff_deathBounds", "bwh_death", "bwh_Q01", "odd_guard_needed", "even_threshold_needed"};
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.bwh_Q01"]["KernelCheck"]
```
