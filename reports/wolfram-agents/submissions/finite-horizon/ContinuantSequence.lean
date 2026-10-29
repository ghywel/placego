import ActualContinuants
import FiniteHorizonSelection

/-!
# The actual denominator sequence supplies finite threshold selection

UNCOMPILED staging component, GC2148. The public Lagrange recurrence/growth
supply q0=1, positive coefficients, successive monotonicity and unboundedness.
No assumed abstract denominator sequence or least-index operator is needed.
No validation stage is launched or widened by this source.
-/

namespace FiniteHorizonContinuantSequence

open Rule30Equivalents.Lagrange

/-- The first standard denominator is1, independently of the integer part of alpha. -/
theorem denominator_zero (alpha : ℝ) : ArcRotation.denominator alpha 0 = 1 := by
  simp [ArcRotation.denominator,contQ]

/-- Offset indexing avoids truncated subtraction in the actual recurrence. -/
theorem denominator_recurrence {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    ArcRotation.denominator alpha (n+2) = (digit alpha (n+2)).toNat*
      ArcRotation.denominator alpha (n+1)+ArcRotation.denominator alpha n := by
  exact ArcRotation.denominator_next ha (n+1) (by omega)

/-- A concrete witness B+1 suffices; no asymptotic numerical estimate enters. -/
theorem denominator_unbounded {alpha : ℝ} (ha : Irrational alpha) :
    ∀ B : Nat, ∃ n : Nat, B < ArcRotation.denominator alpha n := by
  intro B
  have h := contQ_ge (fun k => one_le_digit ha k) B
  rw [show B+3 = (B+1)+2 by omega,← ArcRotation.denominator_cast ha (B+1)] at h
  have hb : B+1 ≤ ArcRotation.denominator alpha (B+1) := by exact_mod_cast h
  exact ⟨B+1,by omega⟩

/-- Successive denominators may be equal initially, but never decrease. -/
theorem denominator_successive {alpha : ℝ} (ha : Irrational alpha) :
    ∀ n, ArcRotation.denominator alpha n ≤ ArcRotation.denominator alpha (n+1) := by
  apply FiniteHorizonSelection.successive_ge (ArcRotation.denominator alpha)
    (fun n => (digit alpha n).toNat)
  · rw [denominator_zero]
    have h := ArcRotation.denominator_pos ha 1
    omega
  · intro n
    have h := one_le_digit ha (n+1)
    have hnonneg : 0 ≤ digit alpha (n+2) := by omega
    have ht : (1 : Int) ≤ ((digit alpha (n+2)).toNat : Int) := by
      rw [Int.toNat_of_nonneg hnonneg]
      exact h
    exact_mod_cast ht
  · exact denominator_recurrence ha

/-- The exact initial scale used in the four-step finite budget exists for every irrational slope. -/
theorem threshold_crossing {alpha : ℝ} (ha : Irrational alpha) (C : Nat) :
    ∃ r, ArcRotation.denominator alpha r ≤ 2*C+8 ∧
      2*C+8 < ArcRotation.denominator alpha (r+1) := by
  exact FiniteHorizonSelection.crossing_scale (ArcRotation.denominator alpha) (2*C+8)
    (by omega) (denominator_zero alpha) (denominator_unbounded ha)

#print axioms FiniteHorizonContinuantSequence.denominator_zero
#print axioms FiniteHorizonContinuantSequence.denominator_recurrence
#print axioms FiniteHorizonContinuantSequence.denominator_unbounded
#print axioms FiniteHorizonContinuantSequence.denominator_successive
#print axioms FiniteHorizonContinuantSequence.threshold_crossing

end FiniteHorizonContinuantSequence
