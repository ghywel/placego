import TwoPairsInterfaces
import CanonicalDecoration

/-!
Lowry's definitions are from the PR61 research archive at commit
`30b7cfb980efadd1809bb9aff4039815e218efad`, directory
`research/period-reflection-20261030T190801Z/proofs`. The five-layer
statement is written out in the archive's `NEXT-CLAIM.txt`.
-/

namespace TwoPairsLowry

open Ruliology.CellularAutomata.Rule30FrozenRuler
open CanonicalDecoration

theorem iter_eq (x : Code) (t : Nat) : TwoPairs.iter x t = iter t x := by
  induction t with
  | zero => rfl
  | succ t ih =>
    change TwoPairs.step (TwoPairs.iter x t) = T (iter t x)
    rw [ih]
    funext j
    cases j with
    | zero => rfl
    | succ j => cases j <;> rfl

/-- A law at width k+2 resolves a confined band whose last digit is k+1. -/
theorem confined_at_band (k : Nat) (law : TwoPairs.Law k) (x y : Code)
    (hx : x 0 = true) (hy : y 0 = true) (hc : Confined (k+1) 0 x y) :
    x = y := by
  have movie (j : Nat) (hj : k+2 ≤ j) (t : Nat) :
      TwoPairs.iter x t j = TwoPairs.iter y t j := by
    rw [iter_eq, iter_eq]
    exact (hc t j hj).symm
  have below := TwoPairsInterfaces.recover k law hx hy
    (movie (k+2) (by omega)) (movie (k+3) (by omega))
  funext j
  by_cases hj : j < k+2
  · exact below j hj
  · exact (hc 0 j (by omega)).symm

theorem same_edge_rigidity (laws : ∀ k, TwoPairs.Law k) : SameEdgeRigidity := by
  intro K x y hx hy hc
  cases K with
  | zero =>
    funext j
    cases j with
    | zero => exact hx.trans hy.symm
    | succ j => exact (hc 0 (j+1) (by omega)).symm
  | succ k => exact confined_at_band k (laws k) x y hx hy hc

/-- The law at width j+6 implies the archive's five-layer escape at depth j.
Only lower-prefix agreement and the first difference are imposed at time zero. -/
theorem five_layer_escape (j : Nat) (law : TwoPairs.Law (j+4)) (x y : Code)
    (hx : x 0 = true) (low : ∀ i, i < j+1 → x i = y i)
    (different : x (j+1) ≠ y (j+1)) :
    ∃ t, iter t x (j+6) ≠ iter t y (j+6) ∨ iter t x (j+7) ≠ iter t y (j+7) := by
  classical
  apply Classical.byContradiction
  intro no
  have first (t : Nat) : TwoPairs.iter x t (j+6) = TwoPairs.iter y t (j+6) := by
    rw [iter_eq, iter_eq]
    exact Classical.byContradiction (fun h => no ⟨t, Or.inl h⟩)
  have second (t : Nat) : TwoPairs.iter x t (j+7) = TwoPairs.iter y t (j+7) := by
    rw [iter_eq, iter_eq]
    exact Classical.byContradiction (fun h => no ⟨t, Or.inr h⟩)
  have hy : y 0 = true := (low 0 (by omega)).symm.trans hx
  have below := TwoPairsInterfaces.recover (j+4) law hx hy first second
  exact different (below (j+1) (by omega))

end TwoPairsLowry
