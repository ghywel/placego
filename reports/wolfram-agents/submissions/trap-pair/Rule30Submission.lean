import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30PeriodTwoSideways

/-!
# Two explicit instances of `CQ01`, absorbed by the kit's ether-and-wall trap, and a collision outside the moves

The coupled question `CQ01` (Rule30PeriodTwoCoupled) holds iff, for every finite right half `R`, the sideways row `Psi R`
(Rule30PeriodTwoSideways) has infinitely many black cells (`CQ01_iff_Psi`). The kit's absorption route,
`not_finSupp_Psi_of_eventuallyPeriodic`, gives this for `R` whenever column `1` of the driven right half is eventually periodic at
the white steps. This module exhibits two explicit right halves for which that happens:
`R31` (black cells `1..5`) and `R495` (black cells `1..4` and `6..9`; it is the row of `R31` at time `4`).

Both driven right halves enter the kit's ether-and-wall trap (Rule30Ether): column `0`, the alternating column, is the ether
column `B4` (index `3`) at phase `t + 3`; at time `9` (for `R31`) and `5` (for `R495`) columns `1..6` carry the ether at that phase,
column `6` is a `B3`, and columns `7..19` form one of the kit's wall states (decided). The kit's `trap_invariant` then keeps columns
`1..6` in the ether for ever, so column `1` is the ether column `B5` from then on, and with four (resp. two) decided early values the
visible column is the parity of the step: `u R31 q = u R495 q = (q % 2 == 1)` for every `q`.

Consequences: `CQ01` for `R31` and for `R495`; `Psi R31 = Psi R495`; and the two right halves are not related by the right-end moves
(the inverse of the kit's terminal rewrites `011 -> 01`, `101 -> 11`, with the black wall counted as a cell left of cell `1`), so the
moves do not account for every collision of `R -> Psi R`. The move relation is formalized below on reversed cell lists; its chains
have a computable root, invariant under moves, and the two roots differ.
-/

namespace Rule30Submission
open Ruliology.CellularAutomata
open Rule30Jen (EventuallyPeriodic)
open Rule30ZeroBoundary (FinSupp)
open Rule30Ether (ether ether_congr trap_invariant rowOf wallStates drv drv_isR30 drv_col0)
open Rule30PeriodTwoCoupled (altCol)
open Rule30PeriodTwoSideways (u Psi not_finSupp_Psi_of_eventuallyPeriodic)

/-- A finite right half from its cells `1, 2, ...` (column `p` is entry `p - 1`; column `0` is unused). -/
def ofCells (w : List Bool) (p : Nat) : Bool := 1 ≤ p && w.getD (p - 1) false

/-- The cells of the two right halves: black at `1..5`, and black at `1..4, 6..9`. -/
def cells31 : List Bool := [true, true, true, true, true]
def cells495 : List Bool := [true, true, true, true, false, true, true, true, true]

def R31 : Nat → Bool := ofCells cells31
def R495 : Nat → Bool := ofCells cells495

/-- The alternating column is the ether column `B4` (index 3) at phase `t + 3`. -/
theorem altCol_ether (t : Nat) : altCol t = ether 3 (t + 3) := by
  have e : ether 3 (t + 3) = ether 3 (t % 4 + 3) := ether_congr rfl (by omega)
  rw [e]
  rcases (by omega : t % 4 = 0 ∨ t % 4 = 1 ∨ t % 4 = 2 ∨ t % 4 = 3) with h | h | h | h <;>
    · rw [h]; simp [altCol, show t % 2 = t % 4 % 2 by omega, h]; decide

/-- Ether column `B5` (index 4) at phase `2 q + 4` is the parity of `q`. -/
theorem ether4_parity (q : Nat) : ether 4 (2 * q + 4) = (q % 2 == 1) := by
  have e : ether 4 (2 * q + 4) = ether 4 (2 * (q % 2)) := ether_congr rfl (by omega)
  rw [e]
  rcases (by omega : q % 2 = 0 ∨ q % 2 = 1) with h | h <;> · rw [h]; decide

theorem trap31_E : ∀ p, 1 ≤ p → p ≤ 6 → drv altCol R31 9 p = ether (3 + p) (9 + 3) := by
  intro p h1 h2
  rcases (by omega : p = 1 ∨ p = 2 ∨ p = 3 ∨ p = 4 ∨ p = 5 ∨ p = 6) with rfl | rfl | rfl | rfl | rfl | rfl <;> decide

theorem trap31_W : ((9 + 3) % 4, rowOf (drv altCol R31) 9 6 13) ∈ wallStates := by decide

theorem col1_R31 : ∀ t, 9 ≤ t → drv altCol R31 t 1 = ether 4 (t + 3) := by
  have inv := trap_invariant (drv_isR30 altCol R31) 3 3 6 9 (by decide)
    (fun t _ => by rw [drv_col0]; exact altCol_ether t) trap31_E trap31_W
  intro t ht
  have h := (inv (t - 9)).1 1 (by decide)
  rw [show 9 + (t - 9) = t by omega] at h
  rw [h]

theorem u_R31 (q : Nat) : u R31 q = (q % 2 == 1) := by
  show drv altCol R31 (2 * q + 1) 1 = _
  rcases (by omega : q < 4 ∨ 4 ≤ q) with h | h
  · rcases (by omega : q = 0 ∨ q = 1 ∨ q = 2 ∨ q = 3) with rfl | rfl | rfl | rfl <;> decide
  · rw [col1_R31 (2 * q + 1) (by omega), show 2 * q + 1 + 3 = 2 * q + 4 by omega]
    exact ether4_parity q

theorem trap495_E : ∀ p, 1 ≤ p → p ≤ 6 → drv altCol R495 5 p = ether (3 + p) (5 + 3) := by
  intro p h1 h2
  rcases (by omega : p = 1 ∨ p = 2 ∨ p = 3 ∨ p = 4 ∨ p = 5 ∨ p = 6) with rfl | rfl | rfl | rfl | rfl | rfl <;> decide

theorem trap495_W : ((5 + 3) % 4, rowOf (drv altCol R495) 5 6 13) ∈ wallStates := by decide

theorem col1_R495 : ∀ t, 5 ≤ t → drv altCol R495 t 1 = ether 4 (t + 3) := by
  have inv := trap_invariant (drv_isR30 altCol R495) 3 3 6 5 (by decide)
    (fun t _ => by rw [drv_col0]; exact altCol_ether t) trap495_E trap495_W
  intro t ht
  have h := (inv (t - 5)).1 1 (by decide)
  rw [show 5 + (t - 5) = t by omega] at h
  rw [h]

theorem u_R495 (q : Nat) : u R495 q = (q % 2 == 1) := by
  show drv altCol R495 (2 * q + 1) 1 = _
  rcases (by omega : q < 2 ∨ 2 ≤ q) with h | h
  · rcases (by omega : q = 0 ∨ q = 1) with rfl | rfl <;> decide
  · rw [col1_R495 (2 * q + 1) (by omega), show 2 * q + 1 + 3 = 2 * q + 4 by omega]
    exact ether4_parity q

/-- **The two visible columns coincide**: `u R31 = u R495` (both are the parity of the step). -/
theorem u_eq : u R31 = u R495 := funext fun q => by rw [u_R31, u_R495]

/-- **Equal sideways rows** for two different finite right halves. -/
theorem Psi_eq : Psi R31 = Psi R495 := by
  unfold Psi; rw [u_eq]

theorem R31_ne_R495 : R31 ≠ R495 := fun h => by
  have := congrFun h 6; revert this; decide

theorem u_R31_periodic : EventuallyPeriodic (u R31) :=
  ⟨0, 2, by decide, fun t _ => by rw [u_R31, u_R31]; simp⟩

theorem u_R495_periodic : EventuallyPeriodic (u R495) :=
  ⟨0, 2, by decide, fun t _ => by rw [u_R495, u_R495]; simp⟩

/-- **CQ01 for `R31`**: `Psi R31` has infinitely many black cells. -/
theorem CQ01_R31 : ¬ FinSupp (Psi R31) := not_finSupp_Psi_of_eventuallyPeriodic R31 u_R31_periodic

/-- **CQ01 for `R495`**. -/
theorem CQ01_R495 : ¬ FinSupp (Psi R495) := not_finSupp_Psi_of_eventuallyPeriodic R495 u_R495_periodic

/-! ## The two right halves are not related by the right-end moves

The right-end move `S` (the record's L910, the inverse of the kit's terminal rewrites `011 -> 01` and `101 -> 11`, with the black
wall counted as a black cell left of cell `1`) acts on a nonempty right half written from its LAST black cell leftward:
`1 0 r -> 1 1 0 r`, `1 1 r -> 1 0 1 r`, and the single cell `1 -> 1 0` (the wall black at time `0`). Its inverse `P` undoes exactly
these three shapes, so `P (S a) = a`, and the root of the chain through `a` is invariant under moves. -/

/-- The right-end move on a reversed cell list (head = last cell); the identity off its domain. -/
def S : List Bool → List Bool
  | true :: false :: r => true :: true :: false :: r
  | true :: true :: r => true :: false :: true :: r
  | [true] => [true, false]
  | w => w

/-- The inverse of `S` on its image. -/
def P : List Bool → Option (List Bool)
  | true :: true :: false :: r => some (true :: false :: r)
  | true :: false :: true :: r => some (true :: true :: r)
  | [true, false] => some [true]
  | _ => none

/-- A nonempty right half, reversed: its head is its last black cell. -/
def Valid (w : List Bool) : Prop := w.head? = some true

theorem P_S (a : List Bool) (h : Valid a) : P (S a) = some a := by
  match a, h with
  | true :: false :: r, _ => rfl
  | true :: true :: r, _ => rfl
  | [true], _ => rfl

theorem S_length (a : List Bool) (h : Valid a) : (S a).length = a.length + 1 := by
  match a, h with
  | true :: false :: r, _ => rfl
  | true :: true :: r, _ => rfl
  | [true], _ => rfl

/-- The root of the chain: apply `P` while it applies (fuel: the length, which `P` lowers by one). -/
def rootF : Nat → List Bool → List Bool
  | 0, w => w
  | n + 1, w => match P w with
    | some v => rootF n v
    | none => w

def root (w : List Bool) : List Bool := rootF w.length w

theorem root_S (a : List Bool) (h : Valid a) : root (S a) = root a := by
  unfold root; rw [S_length a h]; show (match P (S a) with | some v => rootF a.length v | none => S a) = _
  rw [P_S a h]

/-- One move step: `b = S a` with `a` a nonempty right half. -/
def Move (a b : List Bool) : Prop := Valid a ∧ b = S a

theorem root_of_eqv {a b : List Bool} (h : Relation.EqvGen Move a b) : root a = root b := by
  induction h with
  | rel x y hxy => obtain ⟨hv, rfl⟩ := hxy; exact (root_S x hv).symm
  | refl => rfl
  | symm _ _ _ ih => exact ih.symm
  | trans _ _ _ _ _ ih1 ih2 => exact ih1.trans ih2

/-- **Not move-equivalent**: no chain of right-end moves (either direction) joins the two right halves. -/
theorem not_move_equivalent : ¬ Relation.EqvGen Move cells31.reverse cells495.reverse := fun h => by
  have := root_of_eqv h; revert this; decide

end Rule30Submission
