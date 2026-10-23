import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall
import Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth52

/-!
# The death time of the zero-boundary start at width 52 is exactly 96; witnesses at widths 56 and 60

**Partial result on the kit's `Q01` (the period-2 question, Problem 1 of the Rule 30 Prize), proved against the
kit's own definitions.** The kit's `Rule30ZeroBoundaryWidth52.q01_width_le_52` says that every zero-boundary start
supported at depths at most 52 has a white depth-1 cell at some even time at most 96, and remarks that 96 "is `D(52)`
of the death-time table (its tightness is observed, not proved)". This module proves the tightness: the explicit
start `w52` (bits are depths 1 to 52) has its depth-1 cell black at every even time below 96 and white at 96, by the
kit's packed evaluator `prun` and its bridge `run_toFun`, so the least uniform even death bound at width 52 is exactly
96 (`death_time_52_exact`). Two further explicit starts, `w56` and `w60`, are black at depth 1 at every even time
below 100 and below 114 respectively, so the death time at width 56 is at least 100 and at width 60 at least 114
(`width56_lower`, `width60_lower`). In our record both are exact: complete chunk certificates at K = 101 (width 56)
and K = 115 (width 60), built with the kit's `Rule30ZeroBoundaryLanes` machinery and its `Check.lean`, give the upper
bounds 100 and 114; those certificates (1,024 and 4,096 kernel checks) are not carried in this module.

**What is new.** The kit has no proved exact death time at any width and no bound at widths 56 and 60. The values
D(52) = 96, D(56) = 100, D(60) = 114 are not of the form 2W - c (the differences from 2W are 8, 12, 6), so the kit's
observed "2W + 8" linear bound is loose and the law of D(W) is open.

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
