/-!
Uncompiled source fragment, GPT GC1840, 2026-10-25.
Append after the existing Rule30Submission.lean (27f799f4...) for Local's elaboration.
This fragment is not a standalone module and has not been built on GPT's host.
No new axioms or admitted proofs. The kernel-checked pair module remains unchanged.
-/
namespace Rule30Submission

open Ruliology.CellularAutomata
open Rule30ZeroBoundary (FinSupp)
open Rule30Ether (drv drv_init drv_col0 drv_isR30 ether rowOf wallStates seg_congr trap_invariant)
open Rule30PeriodTwoCoupled (altCol)
open Rule30PeriodTwoSideways (u Psi not_finSupp_Psi_of_eventuallyPeriodic)

/-- Agreement at the positive initial cells; column zero belongs to the common driver. -/
def AgreesPrefix (M : Nat) (R S : Nat → Bool) : Prop :=
  ∀ p, 1 ≤ p → p ≤ M → R p = S p

/-- Common-driver radius-one light cone, with an inclusive right endpoint. -/
theorem drv_prefix_agree (c R S : Nat → Bool) (M : Nat) (h : AgreesPrefix M R S) :
    ∀ t p, p + t ≤ M → drv c R t p = drv c S t p := by
  intro t
  induction t with
  | zero =>
    intro p hp
    cases p with
    | zero => rfl
    | succ p =>
      rw [drv_init c R (p + 1) (by omega), drv_init c S (p + 1) (by omega)]
      exact h (p + 1) (by omega) (by omega)
  | succ t ih =>
    intro p hp
    cases p with
    | zero => rfl
    | succ p =>
      change Rule30Jen.rule (drv c R t p) (drv c R t (p + 1)) (drv c R t (p + 2)) =
        Rule30Jen.rule (drv c S t p) (drv c S t (p + 1)) (drv c S t (p + 2))
      rw [ih p (by omega), ih (p + 1) (by omega), ih (p + 2) (by omega)]

/-- Transfer a finite entry witness; the trap then allows the actual arbitrary later right input. -/
theorem col1_ether_of_prefix_entry (R S : Nat → Bool) (t1 : Nat)
    (h : AgreesPrefix (19 + t1) R S)
    (hE : ∀ p, 1 ≤ p → p ≤ 6 → drv altCol S t1 p = ether (3 + p) (t1 + 3))
    (hW : ((t1 + 3) % 4, rowOf (drv altCol S) t1 6 13) ∈ wallStates) :
    ∀ t, t1 ≤ t → drv altCol R t 1 = ether 4 (t + 3) := by
  have hER : ∀ p, 1 ≤ p → p ≤ 6 → drv altCol R t1 p = ether (3 + p) (t1 + 3) := by
    intro p hp1 hp6
    rw [drv_prefix_agree altCol R S (19 + t1) h t1 p (by omega)]
    exact hE p hp1 hp6
  have hrow : rowOf (drv altCol R) t1 6 13 = rowOf (drv altCol S) t1 6 13 := by
    unfold rowOf
    apply seg_congr
    intro i hi
    exact drv_prefix_agree altCol R S (19 + t1) h t1 (6 + i + 1) (by omega)
  have hWR : ((t1 + 3) % 4, rowOf (drv altCol R) t1 6 13) ∈ wallStates := by
    rw [hrow]; exact hW
  have inv := trap_invariant (drv_isR30 altCol R) 3 3 6 t1 (by decide)
    (fun t _ => by rw [drv_col0]; exact altCol_ether t) hER hWR
  intro t ht
  have hh := (inv (t - t1)).1 1 (by decide)
  rw [show t1 + (t - t1) = t by omega] at hh
  exact hh

/-- Locality handles the finitely many early samples; the trap handles all subsequent samples. -/
theorem u_parity_of_prefix_entry (R S : Nat → Bool) (t1 : Nat)
    (h : AgreesPrefix (19 + t1) R S)
    (hE : ∀ p, 1 ≤ p → p ≤ 6 → drv altCol S t1 p = ether (3 + p) (t1 + 3))
    (hW : ((t1 + 3) % 4, rowOf (drv altCol S) t1 6 13) ∈ wallStates)
    (huS : ∀ q, u S q = (q % 2 == 1)) : ∀ q, u R q = (q % 2 == 1) := by
  intro q
  change drv altCol R (2 * q + 1) 1 = _
  by_cases ht : t1 ≤ 2 * q + 1
  · rw [col1_ether_of_prefix_entry R S t1 h hE hW (2 * q + 1) ht,
      show 2 * q + 1 + 3 = 2 * q + 4 by omega]
    exact ether4_parity q
  · rw [drv_prefix_agree altCol R S (19 + t1) h (2 * q + 1) 1 (by omega)]
    exact huS q

theorem u_prefix31 (R : Nat → Bool) (h : AgreesPrefix 28 R R31) :
    ∀ q, u R q = (q % 2 == 1) :=
  u_parity_of_prefix_entry R R31 9 h trap31_E trap31_W u_R31

theorem u_prefix495 (R : Nat → Bool) (h : AgreesPrefix 24 R R495) :
    ∀ q, u R q = (q % 2 == 1) :=
  u_parity_of_prefix_entry R R495 5 h trap495_E trap495_W u_R495

/-- Infinite family: no finite left partner, for every right half with this prefix, even with infinite tail. -/
theorem CQ01_prefix31 (R : Nat → Bool) (h : AgreesPrefix 28 R R31) : ¬ FinSupp (Psi R) := by
  apply not_finSupp_Psi_of_eventuallyPeriodic R
  exact ⟨0, 2, by decide, fun t _ => by rw [u_prefix31 R h, u_prefix31 R h]; simp⟩

theorem CQ01_prefix495 (R : Nat → Bool) (h : AgreesPrefix 24 R R495) : ¬ FinSupp (Psi R) := by
  apply not_finSupp_Psi_of_eventuallyPeriodic R
  exact ⟨0, 2, by decide, fun t _ => by rw [u_prefix495 R h, u_prefix495 R h]; simp⟩

theorem Psi_prefix31 (R : Nat → Bool) (h : AgreesPrefix 28 R R31) : Psi R = Psi R31 := by
  have hu : u R = u R31 := funext fun q => by rw [u_prefix31 R h, u_R31]
  unfold Psi; rw [hu]

theorem Psi_prefix495 (R : Nat → Bool) (h : AgreesPrefix 24 R R495) : Psi R = Psi R495 := by
  have hu : u R = u R495 := funext fun q => by rw [u_prefix495 R h, u_R495]
  unfold Psi; rw [hu]

end Rule30Submission
