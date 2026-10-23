---
Template: ComputationalEssay
Name: The death time at width 52 is exactly 96, with witnesses at widths 56 and 60
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-23
Description: A partial result on the kit's Q01 (the period-2 question, Problem 1 of the Rule 30 Prize), proved in Lean against the kit's own definitions: the kit's certified bound 96 at width 52 is attained by an explicit start, so the death time at width 52 is exactly 96; explicit starts at widths 56 and 60 survive to 100 and 114.
Abstract: The kit's Rule30ZeroBoundaryWidth52 proves that every zero-boundary start supported at depths at most 52 has a white depth-1 cell at some even time at most 96, and says of 96 that its tightness is observed, not proved. This essay proves the tightness: the explicit start 0x7dc2ff6fcc4fd is black at depth 1 at every even time below 96 and white at 96, by the kit's packed evaluator prun and its bridge run_toFun, so the death time at width 52 is exactly 96 (the headline theorem Rule30Submission.death_time_52_exact). Two further explicit starts give the lower bounds 100 at width 56 and 114 at width 60 (width56_lower, width60_lower); in our record both are exact by complete chunk certificates at K = 101 and K = 115, which are not carried here. The values 96, 100, 114 are not of the form 2W - c, so the observed linear law is loose and the law of D(W) is open.
Keywords: [rule 30, Rule 30 Prize, Problem 1, Q01, zero boundary, death time, exact bound, witness, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, CHAT-LEDGER.md L805 to L820](https://github.com/ghywel/placego/blob/main/CHAT-LEDGER.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)"]
---

## The question

The kit reduces the period-2 question of Problem 1 to `Q01`: every finite start of the zero-boundary left half, driven by the clock at column 0, has a white cell at depth 1 at some even time. The kit proves `Q01` for every start of width at most 52 by 256 kernel-checked chunk computations (`Rule30ZeroBoundaryWidth52`), with the bound: a white depth-1 cell at an even time at most 96. Its docstring calls 96 "`D(52)` of the death-time table (its tightness is observed, not proved)". This essay proves it.

Write `D(W)` for the largest, over starts supported at depths 1 to `W`, of the first even time at which the depth-1 cell is white. The kit gives `D(52) ≤ 96`. Here: `D(52) = 96`, and `D(56) ≥ 100`, `D(60) ≥ 114`.

## The zero-boundary half-line

A start is a row of cells at depths `1, 2, 3, …`, the wall at depth 0 always white, evolved by rule 30 with the wall as the left neighbour. The kit's `Rule30ZeroBoundarySmall` packs a row into a natural number (bit `j` is depth `j + 1`) and steps it by `pstep r = (r >>> 1) xor (r ||| (r <<< 1))`; its theorem `run_toFun` says this packed orbit is the physical evolution `zrow`. The same step in the Wolfram Language:

```wl
pstep[r_] := BitXor[BitShiftRight[r, 1], BitOr[r, BitShiftLeft[r, 1]]];
orbit[r_, n_] := NestList[pstep, r, n];
depth1[r_, n_] := BitAnd[#, 1] & /@ orbit[r, n];
```

The three witnesses, as numbers whose bits are the depths:

```wl
w52 = 16^^7dc2ff6fcc4fd; w56 = 16^^93d4b223f5b9b5; w60 = 16^^e77a4e77b8f99b5;
{BitLength[w52], BitLength[w56], BitLength[w60]}
```

The first even time at which depth 1 is white, for each:

```wl
firstEvenWhite[r_, n_] := First[Select[Range[0, n, 2], depth1[r, n][[# + 1]] == 0 &]];
{firstEvenWhite[w52, 120], firstEvenWhite[w56, 120], firstEvenWhite[w60, 130]}
```

The orbit of `w52` for 100 steps, depth 1 at the left, with the even times at which depth 1 is black marked:

```wl
rows = Reverse[IntegerDigits[#, 2, 170]] & /@ orbit[w52, 100];
ArrayPlot[rows, ImageSize -> 600, Frame -> False]
```

## The Lean module

LeanLink and the kit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

The module imports the kit, defines the three witnesses, proves they are below `2^W` (so supported at depths at most `W`), evaluates their packed orbits at every even time below the bound by `decide +kernel`, bridges to `zrow` by the kit's `run_toFun`, and composes the width-52 case with the kit's theorem:

```wl
rule30Submission = LeanImportString["import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall
import Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth52

/-!
# The death time of the zero-boundary start at width 52 is exactly 96; witnesses at widths 56 and 60

**Partial result on the kit's `Q01` (the period-2 question, Problem 1 of the Rule 30 Prize), proved against the
kit's own definitions.** The kit's `Rule30ZeroBoundaryWidth52.q01_width_le_52` says that every zero-boundary start
supported at depths at most 52 has a white depth-1 cell at some even time at most 96, and remarks that 96 \"is `D(52)`
of the death-time table (its tightness is observed, not proved)\". This module proves the tightness: the explicit
start `w52` (bits are depths 1 to 52) has its depth-1 cell black at every even time below 96 and white at 96, by the
kit's packed evaluator `prun` and its bridge `run_toFun`, so the least uniform even death bound at width 52 is exactly
96 (`death_time_52_exact`). Two further explicit starts, `w56` and `w60`, are black at depth 1 at every even time
below 100 and below 114 respectively, so the death time at width 56 is at least 100 and at width 60 at least 114
(`width56_lower`, `width60_lower`). In our record both are exact: complete chunk certificates at K = 101 (width 56)
and K = 115 (width 60), built with the kit's `Rule30ZeroBoundaryLanes` machinery and its `Check.lean`, give the upper
bounds 100 and 114; those certificates (1,024 and 4,096 kernel checks) are not carried in this module.

**What is new.** The kit has no proved exact death time at any width and no bound at widths 56 and 60. The values
D(52) = 96, D(56) = 100, D(60) = 114 are not of the form 2W - c (the differences from 2W are 8, 12, 6), so the kit's
observed \"2W + 8\" linear bound is loose and the law of D(W) is open.

**The argument** is a kernel computation and the kit's own lemmas: `w < 2 ^ W` by `decide`; `toFun w k = false` beyond
the width by the kit's `testBit_ge_of_lt`; the packed orbit `prun w (2 s)` tested at depth 1 for every `s < D / 2` by
`decide +kernel` (48, 50 and 57 orbits of at most 112 steps); `zrow (toFun w) t 1 = (prun w t).testBit 0` by the kit's
`run_toFun`; the exactness statement is the conjunction of the kit's theorem with the witness's survival.

**Provenance.** Lane D-exact of the Wolfram · Collatz · Mahler record (github.com/ghywel/placego, CHAT-LEDGER.md
L805 to L820, 2026-10-23): a Python word engine exact to the kit's `check` found the witnesses (the lane's maximum
over all 2^(W/2 - 18) chunks of 2^18 lanes), two independent physical engines validated them, GPT (OpenAI) read every
design and audited every receipt, and the three exactness certificates were kernel-checked on the kit's commit
cc1e0e0 with Lean v4.35.0. Nothing is claimed for any other width; nothing here touches `Q01` for every width.
-/

set_option Elab.async false

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30ZeroBoundary
open Ruliology.CellularAutomata.Rule30ZeroBoundarySmall

/-! ## The witnesses (bits are depths `1 .. W`; the wall at depth `0` is white) -/

/-- The width-52 witness: 51 bits, so supported at depths at most 52. -/
def w52 : Nat := 0x7dc2ff6fcc4fd

/-- The width-56 witness: 56 bits. -/
def w56 : Nat := 0x93d4b223f5b9b5

/-- The width-60 witness: 60 bits. -/
def w60 : Nat := 0xe77a4e77b8f99b5

theorem w52_lt : w52 < 2 ^ 52 := by decide
theorem w56_lt : w56 < 2 ^ 56 := by decide
theorem w60_lt : w60 < 2 ^ 60 := by decide

/-- `toFun r` is false beyond the width of `r`. -/
theorem toFun_width {r W : Nat} (h : r < 2 ^ W) (k : Nat) (hk : W < k) : toFun r k = false := by
  unfold toFun
  have h1 : k ≠ 0 := by omega
  simp only [h1, ite_false]
  exact testBit_ge_of_lt h (by omega)

/-- The physical depth-1 cell of the start `toFun r` at time `t` is bit `0` of the packed orbit (the kit's
`run_toFun`). -/
theorem zrow_packed (r t : Nat) : zrow (toFun r) t 1 = (prun r t).testBit 0 := by
  rw [run_toFun]; rfl

/-! ## The packed orbits, kernel-evaluated -/

/-- Black at depth 1 at every even time below 96: 48 packed orbits. -/
theorem w52_black : ∀ s, s < 48 → (prun w52 (2 * s)).testBit 0 = true := by decide +kernel

/-- White at 96: the physical death of `w52`. -/
theorem w52_white : (prun w52 96).testBit 0 = false := by decide +kernel

/-- Black at depth 1 at every even time below 100: 50 packed orbits. -/
theorem w56_black : ∀ s, s < 50 → (prun w56 (2 * s)).testBit 0 = true := by decide +kernel

theorem w56_white : (prun w56 100).testBit 0 = false := by decide +kernel

/-- Black at depth 1 at every even time below 114: 57 packed orbits. -/
theorem w60_black : ∀ s, s < 57 → (prun w60 (2 * s)).testBit 0 = true := by decide +kernel

theorem w60_white : (prun w60 114).testBit 0 = false := by decide +kernel

/-! ## Survival below the bound, in the kit's physical vocabulary -/

theorem survives_of_black {r D : Nat} (hb : ∀ s, s < D / 2 → (prun r (2 * s)).testBit 0 = true) (hD : D % 2 = 0) :
    ∀ t, t < D → t % 2 = 0 → zrow (toFun r) t 1 = true := by
  intro t ht he
  rw [zrow_packed]
  obtain ⟨s, rfl⟩ : ∃ s, t = 2 * s := ⟨t / 2, by omega⟩
  exact hb s (by omega)

theorem w52_survives : ∀ t, t < 96 → t % 2 = 0 → zrow (toFun w52) t 1 = true :=
  survives_of_black w52_black rfl

theorem w52_dies : zrow (toFun w52) 96 1 = false := by
  rw [zrow_packed]; exact w52_white

theorem w56_survives : ∀ t, t < 100 → t % 2 = 0 → zrow (toFun w56) t 1 = true :=
  survives_of_black w56_black rfl

theorem w56_dies : zrow (toFun w56) 100 1 = false := by
  rw [zrow_packed]; exact w56_white

theorem w60_survives : ∀ t, t < 114 → t % 2 = 0 → zrow (toFun w60) t 1 = true :=
  survives_of_black w60_black rfl

theorem w60_dies : zrow (toFun w60) 114 1 = false := by
  rw [zrow_packed]; exact w60_white

/-! ## The headline statements -/

/-- **The death time at width 52 is exactly 96.** Every start supported at depths at most 52 has a white depth-1 cell
at some even time at most 96 (the kit's `q01_width_le_52`), and the start `w52`, supported at depths at most 52, has
none below 96. -/
theorem death_time_52_exact :
    (∀ x : Nat → Bool, (∀ k, 52 < k → x k = false) → ∃ t, t ≤ 96 ∧ t % 2 = 0 ∧ zrow x t 1 = false) ∧
    (∃ x : Nat → Bool, (∀ k, 52 < k → x k = false) ∧ (∀ t, t < 96 → t % 2 = 0 → zrow x t 1 = true)) :=
  ⟨Rule30ZeroBoundaryWidth52.q01_width_le_52, ⟨toFun w52, toFun_width w52_lt, w52_survives⟩⟩

/-- **A lower bound at width 56:** a start supported at depths at most 56 with no even white time below 100. -/
theorem width56_lower :
    ∃ x : Nat → Bool, (∀ k, 56 < k → x k = false) ∧ (∀ t, t < 100 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w56, toFun_width w56_lt, w56_survives⟩

/-- **A lower bound at width 60:** a start supported at depths at most 60 with no even white time below 114. -/
theorem width60_lower :
    ∃ x : Nat → Bool, (∀ k, 60 < k → x k = false) ∧ (∀ t, t < 114 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w60, toFun_width w60_lt, w60_survives⟩

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

The environment loads:

```wl
Head[rule30Submission]
```

## The headline theorems

The exact value at width 52: the kit's upper bound and the witness's survival, in one statement.

```wl
opens = {"Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30ZeroBoundarySmall", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.death_time_52_exact"];
thm["TypeForm", "Open" -> opens]
```

The lower bounds at widths 56 and 60:

```wl
{rule30Submission["Rule30Submission.width56_lower"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.width60_lower"]["TypeForm", "Open" -> opens]}
```

The axioms behind the headline, which must be the standard three:

```wl
thm["Axioms"]
```

The witnesses' survival and death, as the kernel evaluated them (black at every even time below the bound; white at the bound):

```wl
{rule30Submission["Rule30Submission.w52_survives"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.w52_dies"]["TypeForm", "Open" -> opens]}
```

The module's two bridge lemmas, from the kit's `run_toFun` (the packed orbit is the physical evolution) and `testBit_ge_of_lt` (a number below `2^W` has no bit at or beyond `W`):

```wl
{rule30Submission["Rule30Submission.zrow_packed"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.toFun_width"]["TypeForm", "Open" -> opens]}
```

The proof's structure, one level down from the headline:

```wl
thm["CallGraph", "Depth" -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## The table so far

| width W | D(W) | status |
|---|---|---|
| 52 | 96 | exact, kernel-checked here (the kit's bound, attained) |
| 56 | 100 | ≥ 100 here; exact in our record (certificate at K = 101, 1,024 chunk checks) |
| 60 | 114 | ≥ 114 here; exact in our record (certificate at K = 115, 4,096 chunk checks) |
| 64 | 116 | a numerical candidate in our record (a census over all 16,384 chunks), not certified |

The differences from `2W` are 8, 12, 6, 12: the observed "`2W + 8`" bound of the kit is loose, and no fit of the form `2W - c` holds. The small widths are rougher still: `D(2 .. 24)` is 6, 6, 6, 8, 10, 12, 12, 18, 18, 30, 30, 30, 32, 32, 32, 32, 32, 38, 38, 38, 40, 40, 42 (exhaustive over all starts at each width), with plateaus where one short start is the record-holder for several widths.

## What is not proved

- Nothing about any width other than those named; `Q01` for every width is untouched.
- The upper bounds at widths 56 and 60 are not in this module. They are complete chunk certificates in our record, built with the kit's `Rule30ZeroBoundaryLanes` and checked by the kit's `Check.lean` on commit cc1e0e0; carrying 5,120 kernel checks in one submission is a separate step.
- No law of `D(W)` is claimed; the points above refute one fit, not the existence of a formula.

## Provenance

Lane D-exact of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT (CHAT-LEDGER.md L805 to L820, 2026-10-23). A Python word engine exact to the kit's `check` found each witness as the maximum of its width's lane computation over every chunk; two independent physical engines validated each witness; GPT (OpenAI) read every design before it ran and audited every receipt; the three exactness certificates were kernel-checked on the M5 against the kit at cc1e0e0 with Lean v4.35.0, the kit's `Check.lean` passing with standard axioms and no new axioms.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026: `Rule30ZeroBoundary`, `Rule30ZeroBoundarySmall`, `Rule30ZeroBoundaryLanes`, `Rule30ZeroBoundaryWidth52`.

[3] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): `tests/probes/wolfram/d1_engine.py`, `d2_witness.py`, `w5_harness.py` and CHAT-LEDGER.md L805 to L820, 2026.
