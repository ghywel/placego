import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall

/-!
# A death-time lower bound at width 76: an explicit witness from a complete GPU census

**Partial result on the kit's `Q01` (the period-2 question, Problem 1 of the Rule 30 Prize), proved against the kit's own
definitions.** Write `D(W)` for the largest, over zero-boundary starts supported at depths at most `W`, of the first even time at
which the depth-1 cell is white. The kit at the pinned commit cc1e0e0 proves `D(52) <= 96` (`Rule30ZeroBoundaryWidth52`) and has no
statement at any width above 52; submissions R30-20261024-b16332 and R30-20261024-a129c3 proved `D(64) >= 116` to `D(74) >= 134`. This module proves
`D(76) >= 138`: an explicit start, supported at depths at most 76, is black at depth 1 at every even time below the bound and white
at the bound, by the kit's packed evaluator `prun` and its bridge `run_toFun` (`width76_lower`).

**Where the witness comes from.** A complete numerical census on a GPU of every reconstructed start of width 76 that survives the
even times below 76 (every maximizer lies among them, since the value exceeds 76) found this value to be the maximum, the witness
attaining it. The engine is an exact lane engine in Metal; a batch of 2^24 starts and every chunk holding a maximizer were checked
against an independent CPU evaluation of the kit's lane check, and samples of further starts and every maximizer were re-simulated by
a scalar evaluator. The census is numerical; this module proves only the lower bound.

**The argument** is a kernel computation and the kit's own lemmas: `w < 2 ^ W` by `decide`; `toFun w k = false` beyond the width
by the kit's `testBit_ge_of_lt`; the packed orbit `prun w (2 s)` tested at depth 1 for every `s < D / 2` by `decide +kernel`;
`zrow (toFun w) t 1 = (prun w t).testBit 0` by the kit's `run_toFun`.

**Provenance.** The Wolfram · Collatz · Mahler record (github.com/ghywel/placego, CHAT-LEDGER.md L889 to L895, 2026-10-24).
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

/-! ## Width 76: `D(76) >= 138` -/

/-- The width-76 witness (75 bits; bits are depths 1 .. 76). -/
def w76 : Nat := 0x5bf46e334109c62aaab

theorem w76_lt : w76 < 2 ^ 76 := by decide

/-- Black at depth 1 at every even time below 138: 69 packed orbits. -/
theorem w76_black : ∀ s, s < 69 → (prun w76 (2 * s)).testBit 0 = true := by decide +kernel

/-- White at 138: the physical death of `w76`. -/
theorem w76_white : (prun w76 138).testBit 0 = false := by decide +kernel

theorem w76_survives : ∀ t, t < 138 → t % 2 = 0 → zrow (toFun w76) t 1 = true :=
  survives_of_black w76_black rfl

theorem w76_dies : zrow (toFun w76) 138 1 = false := by
  rw [zrow_packed]; exact w76_white

/-- **A lower bound at width 76:** a start supported at depths at most 76 with no even white time below 138. -/
theorem width76_lower :
    ∃ x : Nat → Bool, (∀ k, 76 < k → x k = false) ∧ (∀ t, t < 138 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w76, toFun_width w76_lt, w76_survives⟩

end Rule30Submission
