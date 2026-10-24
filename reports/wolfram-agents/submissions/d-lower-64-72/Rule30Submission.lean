import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall

/-!
# Death-time lower bounds at widths 64, 66, 68, 70, 72: explicit witnesses from a complete GPU census

**Partial result on the kit's `Q01` (the period-2 question, Problem 1 of the Rule 30 Prize), proved against the kit's own
definitions.** Write `D(W)` for the largest, over zero-boundary starts supported at depths at most `W`, of the first even time at
which the depth-1 cell is white. The kit proves `D(52) <= 96` (`Rule30ZeroBoundaryWidth52`) and has no statement at any width
above 52. This module proves the lower bounds `D(64) >= 116`, `D(66) >= 120`, `D(68) >= 122`, `D(70) >= 124`, `D(72) >= 130`: for each width an explicit start,
supported at depths at most `W`, is black at depth 1 at every even time below the bound and white at the bound, by the kit's
packed evaluator `prun` and its bridge `run_toFun` (`width64_lower`, `width66_lower`, `width68_lower`, `width70_lower`, `width72_lower`).

**Where the witnesses come from.** A complete numerical census of every start of each width on a GPU (an exact lane engine in
Metal, validated lane for lane against an independent CPU evaluation of the kit's lane check) found these values to be the
maxima: each witness attains its width's census maximum. The census is numerical; this module proves only the lower bounds.

**The argument** is a kernel computation and the kit's own lemmas: `w < 2 ^ W` by `decide`; `toFun w k = false` beyond the width
by the kit's `testBit_ge_of_lt`; the packed orbit `prun w (2 s)` tested at depth 1 for every `s < D / 2` by `decide +kernel`;
`zrow (toFun w) t 1 = (prun w t).testBit 0` by the kit's `run_toFun`.

**Provenance.** The Wolfram · Collatz · Mahler record (github.com/ghywel/placego, CHAT-LEDGER.md L863 to L868, 2026-10-24).
Nothing is claimed for maximality, for the number of maximizers, or for any upper bound.
-/

set_option Elab.async false

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30ZeroBoundary
open Ruliology.CellularAutomata.Rule30ZeroBoundarySmall

/-- `toFun r` is false beyond the width of `r`. -/
theorem toFun_width {r W : Nat} (h : r < 2 ^ W) (k : Nat) (hk : W < k) : toFun r k = false := by
  unfold toFun
  have h1 : k ≠ 0 := by omega
  simp only [h1, ite_false]
  exact testBit_ge_of_lt h (by omega)

/-- The physical depth-1 cell of the start `toFun r` at time `t` is bit `0` of the packed orbit (the kit's `run_toFun`). -/
theorem zrow_packed (r t : Nat) : zrow (toFun r) t 1 = (prun r t).testBit 0 := by
  rw [run_toFun]; rfl

theorem survives_of_black {r D : Nat} (hb : ∀ s, s < D / 2 → (prun r (2 * s)).testBit 0 = true) (hD : D % 2 = 0) :
    ∀ t, t < D → t % 2 = 0 → zrow (toFun r) t 1 = true := by
  intro t ht he
  rw [zrow_packed]
  obtain ⟨s, rfl⟩ : ∃ s, t = 2 * s := ⟨t / 2, by omega⟩
  exact hb s (by omega)

/-! ## Width 64: `D(64) >= 116` -/

/-- The width-64 witness (64 bits; bits are depths 1 .. 64). -/
def w64 : Nat := 0x88b46d66afc2fbd5

theorem w64_lt : w64 < 2 ^ 64 := by decide

/-- Black at depth 1 at every even time below 116: 58 packed orbits. -/
theorem w64_black : ∀ s, s < 58 → (prun w64 (2 * s)).testBit 0 = true := by decide +kernel

/-- White at 116: the physical death of `w64`. -/
theorem w64_white : (prun w64 116).testBit 0 = false := by decide +kernel

theorem w64_survives : ∀ t, t < 116 → t % 2 = 0 → zrow (toFun w64) t 1 = true :=
  survives_of_black w64_black rfl

theorem w64_dies : zrow (toFun w64) 116 1 = false := by
  rw [zrow_packed]; exact w64_white

/-- **A lower bound at width 64:** a start supported at depths at most 64 with no even white time below 116. -/
theorem width64_lower :
    ∃ x : Nat → Bool, (∀ k, 64 < k → x k = false) ∧ (∀ t, t < 116 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w64, toFun_width w64_lt, w64_survives⟩

/-! ## Width 66: `D(66) >= 120` -/

/-- The width-66 witness (65 bits; bits are depths 1 .. 66). -/
def w66 : Nat := 0x1f2401d1c7d2b42ab

theorem w66_lt : w66 < 2 ^ 66 := by decide

/-- Black at depth 1 at every even time below 120: 60 packed orbits. -/
theorem w66_black : ∀ s, s < 60 → (prun w66 (2 * s)).testBit 0 = true := by decide +kernel

/-- White at 120: the physical death of `w66`. -/
theorem w66_white : (prun w66 120).testBit 0 = false := by decide +kernel

theorem w66_survives : ∀ t, t < 120 → t % 2 = 0 → zrow (toFun w66) t 1 = true :=
  survives_of_black w66_black rfl

theorem w66_dies : zrow (toFun w66) 120 1 = false := by
  rw [zrow_packed]; exact w66_white

/-- **A lower bound at width 66:** a start supported at depths at most 66 with no even white time below 120. -/
theorem width66_lower :
    ∃ x : Nat → Bool, (∀ k, 66 < k → x k = false) ∧ (∀ t, t < 120 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w66, toFun_width w66_lt, w66_survives⟩

/-! ## Width 68: `D(68) >= 122` -/

/-- The width-68 witness (67 bits; bits are depths 1 .. 68). -/
def w68 : Nat := 0x46f44349be325d4ab

theorem w68_lt : w68 < 2 ^ 68 := by decide

/-- Black at depth 1 at every even time below 122: 61 packed orbits. -/
theorem w68_black : ∀ s, s < 61 → (prun w68 (2 * s)).testBit 0 = true := by decide +kernel

/-- White at 122: the physical death of `w68`. -/
theorem w68_white : (prun w68 122).testBit 0 = false := by decide +kernel

theorem w68_survives : ∀ t, t < 122 → t % 2 = 0 → zrow (toFun w68) t 1 = true :=
  survives_of_black w68_black rfl

theorem w68_dies : zrow (toFun w68) 122 1 = false := by
  rw [zrow_packed]; exact w68_white

/-- **A lower bound at width 68:** a start supported at depths at most 68 with no even white time below 122. -/
theorem width68_lower :
    ∃ x : Nat → Bool, (∀ k, 68 < k → x k = false) ∧ (∀ t, t < 122 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w68, toFun_width w68_lt, w68_survives⟩

/-! ## Width 70: `D(70) >= 124` -/

/-- The width-70 witness (70 bits; bits are depths 1 .. 70). -/
def w70 : Nat := 0x3f6591177592c2aaab

theorem w70_lt : w70 < 2 ^ 70 := by decide

/-- Black at depth 1 at every even time below 124: 62 packed orbits. -/
theorem w70_black : ∀ s, s < 62 → (prun w70 (2 * s)).testBit 0 = true := by decide +kernel

/-- White at 124: the physical death of `w70`. -/
theorem w70_white : (prun w70 124).testBit 0 = false := by decide +kernel

theorem w70_survives : ∀ t, t < 124 → t % 2 = 0 → zrow (toFun w70) t 1 = true :=
  survives_of_black w70_black rfl

theorem w70_dies : zrow (toFun w70) 124 1 = false := by
  rw [zrow_packed]; exact w70_white

/-- **A lower bound at width 70:** a start supported at depths at most 70 with no even white time below 124. -/
theorem width70_lower :
    ∃ x : Nat → Bool, (∀ k, 70 < k → x k = false) ∧ (∀ t, t < 124 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w70, toFun_width w70_lt, w70_survives⟩

/-! ## Width 72: `D(72) >= 130` -/

/-- The width-72 witness (72 bits; bits are depths 1 .. 72). -/
def w72 : Nat := 0xd464cc8c0b5f0562ab

theorem w72_lt : w72 < 2 ^ 72 := by decide

/-- Black at depth 1 at every even time below 130: 65 packed orbits. -/
theorem w72_black : ∀ s, s < 65 → (prun w72 (2 * s)).testBit 0 = true := by decide +kernel

/-- White at 130: the physical death of `w72`. -/
theorem w72_white : (prun w72 130).testBit 0 = false := by decide +kernel

theorem w72_survives : ∀ t, t < 130 → t % 2 = 0 → zrow (toFun w72) t 1 = true :=
  survives_of_black w72_black rfl

theorem w72_dies : zrow (toFun w72) 130 1 = false := by
  rw [zrow_packed]; exact w72_white

/-- **A lower bound at width 72:** a start supported at depths at most 72 with no even white time below 130. -/
theorem width72_lower :
    ∃ x : Nat → Bool, (∀ k, 72 < k → x k = false) ∧ (∀ t, t < 130 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w72, toFun_width w72_lt, w72_survives⟩

end Rule30Submission
