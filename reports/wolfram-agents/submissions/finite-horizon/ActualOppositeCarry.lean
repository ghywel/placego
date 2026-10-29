import ActualCarrySpacing
import ContinuantSequence
import OppositeCarryArcs

/-!
# Exact opposite-scale shift for actual continued-fraction carries

UNCOMPILED staging component, GC2159. No abstract replacement denominator
sequence: all data are the actual kit continuants. Selected visits need not
be first visits. The caller still supplies finite visit bounds and the two
coefficient-one conclusions. The complete 251 theorem remains unfinished.
-/

namespace FiniteHorizonActualOpposite

open FiniteHorizonContinuants
open Rule30Equivalents.Lagrange

/-- Numerator recurrence in the same offset convention as the actual denominators. -/
theorem numerator_recurrence (alpha : ℝ) (n : Nat) :
    numerator alpha (n+2) = digit alpha (n+2)*numerator alpha (n+1)+numerator alpha n := by
  rfl

/-- Coefficient one gives an exact signed-error sum, rather than an assumed arc-size relation. -/
theorem error_recurrence {alpha : ℝ} (ha : Irrational alpha) (n : Nat)
    (hone : digit alpha (n+2) = 1) :
    error alpha (n+2) = error alpha (n+1)+error alpha n := by
  have hnum : numerator alpha (n+2) = numerator alpha (n+1)+numerator alpha n := by
    rw [numerator_recurrence,hone]
    ring
  have hden : ArcRotation.denominator alpha (n+2) =
      ArcRotation.denominator alpha (n+1)+ArcRotation.denominator alpha n := by
    rw [FiniteHorizonContinuantSequence.denominator_recurrence ha n,hone]
    simp
  unfold error
  rw [hnum,hden]
  push_cast
  ring

/-- The opposite carry-arc lengths add to the actual preceding error. -/
theorem error_sizes {alpha : ℝ} (ha : Irrational alpha) (n : Nat)
    (hone : digit alpha (n+2) = 1) :
    |error alpha (n+1)|+|error alpha (n+2)| = |error alpha n| := by
  exact OppositeCarryArcs.error_sizes (error alpha n) (error alpha (n+1))
    (error alpha (n+2)) (error_recurrence ha n hone)
    (adjacent_errors_opposite ha n) (by simpa only [Nat.add_assoc] using adjacent_errors_opposite ha (n+1))

/-- Actual selected carries at successive usable scales differ by the current denominator.
The two finite recurrence conclusions derive both spatial strip bounds. -/
theorem visit_shift (alpha theta : ℝ) (ha : Irrational alpha) (n C h k : Nat)
    (hone : digit alpha (n+2) = 1) (hnextone : digit alpha (n+3) = 1)
    (hlarge : 2*C+6 < ArcRotation.denominator alpha n)
    (hlow : ArcRotation.denominator alpha (n+2) ≤
      h+ArcRotation.denominator alpha (n+1)+C+4)
    (hupp : h ≤ ArcRotation.denominator alpha (n+1)+C+2)
    (klow : ArcRotation.denominator alpha (n+3) ≤
      k+ArcRotation.denominator alpha (n+2)+C+4)
    (kupp : k ≤ ArcRotation.denominator alpha (n+2)+C+2)
    (hh : MechanicalCarry.carry alpha theta (ArcRotation.denominator alpha (n+1))
      (numerator alpha (n+1)) h ≠ 0)
    (hk : MechanicalCarry.carry alpha theta (ArcRotation.denominator alpha (n+2))
      (numerator alpha (n+2)) k ≠ 0) :
    k = h+ArcRotation.denominator alpha (n+1) := by
  have hrec : ArcRotation.denominator alpha (n+2) =
      ArcRotation.denominator alpha (n+1)+ArcRotation.denominator alpha n := by
    rw [FiniteHorizonContinuantSequence.denominator_recurrence ha n,hone]
    simp
  have hnextrec : ArcRotation.denominator alpha (n+3) =
      ArcRotation.denominator alpha (n+2)+ArcRotation.denominator alpha (n+1) := by
    have hr := FiniteHorizonContinuantSequence.denominator_recurrence ha (n+1)
    rw [show n+1+2 = n+3 by omega,hnextone] at hr
    simpa only [Int.toNat_one,one_mul] using hr
  obtain ⟨hstriplo,hstriphi⟩ := OppositeArcStrip.visit_difference_bounds C
    (ArcRotation.denominator alpha n) (ArcRotation.denominator alpha (n+1))
    (ArcRotation.denominator alpha (n+2)) (ArcRotation.denominator alpha (n+3))
    h k hrec hnextrec hlow hupp klow kupp
  let d := numerator alpha n*(ArcRotation.denominator alpha (n+1) : Int)-
    numerator alpha (n+1)*(ArcRotation.denominator alpha n : Int)
  have hd : d*d = 1 := adjacent_determinant_unit ha n
  have hc := abs_lt.mp (error_abs_lt_one ha (n+1))
  have hn := abs_lt.mp (error_abs_lt_one ha (n+2))
  apply OppositeCarryArcs.visit_shift alpha theta (ArcRotation.denominator alpha n)
    (ArcRotation.denominator alpha (n+1)) (ArcRotation.denominator alpha (n+2))
    (numerator alpha n) (numerator alpha (n+1)) (numerator alpha (n+2)) d (2*(C : Int)+6)
    h k (ArcRotation.denominator_pos ha n)
    (FiniteHorizonContinuantSequence.denominator_successive ha n)
    (by exact_mod_cast hlarge) hstriplo hstriphi rfl hd
  · simpa only [error] using adjacent_errors_opposite ha n
  · simpa only [error,Nat.add_assoc] using adjacent_errors_opposite ha (n+1)
  · simpa only [error] using error_sizes ha n hone
  · exact hc.1
  · exact hc.2
  · exact hn.1
  · exact hn.2
  · exact hh
  · exact hk

#print axioms FiniteHorizonActualOpposite.numerator_recurrence
#print axioms FiniteHorizonActualOpposite.error_recurrence
#print axioms FiniteHorizonActualOpposite.error_sizes
#print axioms FiniteHorizonActualOpposite.visit_shift

end FiniteHorizonActualOpposite
