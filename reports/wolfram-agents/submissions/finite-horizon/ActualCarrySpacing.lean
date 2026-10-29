import ActualContinuants
import CarryReturnSpacing
import FiniteHorizonBounds

/-!
# The actual continued-fraction carry gap and finite-prefix growth bound

UNCOMPILED assembly component, GC2144. It instantiates determinant/sign/range
premises with the actual kit continuants; no abstract substitute sequence remains.
This is not the completed 251(C+4) theorem. Imported staging modules must be built
in a separately frozen validation stage; this file launches no build.
-/

namespace FiniteHorizonActualCarry

open FiniteHorizonContinuants

/-- Actual nonzero carry visits at a convergent are separated by its next denominator. -/
theorem return_spacing (alpha theta : ℝ) (ha : Irrational alpha) (n h k : Nat)
    (hhk : h < k)
    (hh : MechanicalCarry.carry alpha theta (ArcRotation.denominator alpha n) (numerator alpha n) h ≠ 0)
    (hk : MechanicalCarry.carry alpha theta (ArcRotation.denominator alpha n) (numerator alpha n) k ≠ 0) :
    h+ArcRotation.denominator alpha (n+1) ≤ k := by
  let q := ArcRotation.denominator alpha n
  let Q := ArcRotation.denominator alpha (n+1)
  let p := numerator alpha n
  let P := numerator alpha (n+1)
  let d := p*(Q : Int)-P*(q : Int)
  have hd : d*d = 1 := adjacent_determinant_unit ha n
  have hsigns : ((q : ℝ)*alpha-p)*((Q : ℝ)*alpha-P) < 0 := adjacent_errors_opposite ha n
  have herror : |(q : ℝ)*alpha-p| < 1 := error_abs_lt_one ha n
  have hrange := abs_lt.mp herror
  exact CarryReturnSpacing.return_spacing alpha theta q Q p P d
    (ArcRotation.denominator_pos ha n) (ArcRotation.denominator_pos ha (n+1))
    rfl hd hsigns hrange.1 hrange.2 h k hhk hh hk

/-- Finite comparison deadlines bound actual adjacent denominators, with a genuine bounded carry witness. -/
theorem denominator_growth (alpha theta : ℝ) (ha : Irrational alpha) (N C n : Nat)
    (hr : FiniteHorizonBounds.RepeatBoundThrough (MechanicalCarry.mech alpha theta) N C)
    (hdeadline : 4*ArcRotation.denominator alpha n+3*C+8 ≤ N) :
    ∃ h, MechanicalCarry.carry alpha theta (ArcRotation.denominator alpha n) (numerator alpha n) h ≠ 0 ∧
      h ≤ ArcRotation.denominator alpha n+C+2 ∧
      ArcRotation.denominator alpha (n+1) ≤ h+ArcRotation.denominator alpha n+C+4 ∧
      ArcRotation.denominator alpha (n+1) ≤ 2*ArcRotation.denominator alpha n+2*C+6 := by
  apply FiniteHorizonBounds.denominator_growth
    (MechanicalCarry.mech alpha theta)
    (MechanicalCarry.carry alpha theta (ArcRotation.denominator alpha n) (numerator alpha n))
    N C (ArcRotation.denominator alpha n) (ArcRotation.denominator alpha (n+1)) hr
    (ArcRotation.denominator_pos ha n)
    (fun s => MechanicalCarry.difference_identity alpha theta (ArcRotation.denominator alpha n) (numerator alpha n) s)
    hdeadline
  intro h k hhk hh hk
  exact return_spacing alpha theta ha n h k hhk hh hk

#print axioms FiniteHorizonActualCarry.return_spacing
#print axioms FiniteHorizonActualCarry.denominator_growth

end FiniteHorizonActualCarry
