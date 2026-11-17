import SharpAdjacentReturn
import MechanicalCarry

/-!
# Actual carry visits inherit the sharp adjacent-denominator return gap

UNCOMPILED staging component, GC2143. The approximation data remain explicit;
no actual continued fraction is constructed here. Integer phase-floor differences
replace a nearest-integer norm API. Both imported sources must be built first.
-/

namespace CarryReturnSpacing

/-- Two nonzero carries have fractional phases strictly closer than the carry-arc length. -/
theorem phases_close (alpha theta : ℝ) (q : Nat) (p : Int) (h k : Nat)
    (hlo : -1 < (q : ℝ)*alpha-p) (hhi : (q : ℝ)*alpha-p < 1)
    (hne : (q : ℝ)*alpha-p ≠ 0)
    (hh : MechanicalCarry.carry alpha theta q p h ≠ 0)
    (hk : MechanicalCarry.carry alpha theta q p k ≠ 0) :
    |Int.fract (theta+(k : ℝ)*alpha)-Int.fract (theta+(h : ℝ)*alpha)| <
      |(q : ℝ)*alpha-p| := by
  by_cases hpos : 0 < (q : ℝ)*alpha-p
  · have ha := (MechanicalCarry.nonzero_positive alpha theta q p h hpos hhi).mp hh
    have hb := (MechanicalCarry.nonzero_positive alpha theta q p k hpos hhi).mp hk
    rw [abs_of_pos hpos,abs_lt]
    constructor <;> linarith [Int.fract_lt_one (theta+(h : ℝ)*alpha),
      Int.fract_lt_one (theta+(k : ℝ)*alpha)]
  · have hneg : (q : ℝ)*alpha-p < 0 := by
      rcases lt_or_eq_of_le (le_of_not_gt hpos) with h | h
      · exact h
      · exact False.elim (hne h)
    have ha := (MechanicalCarry.nonzero_negative alpha theta q p h hlo hneg).mp hh
    have hb := (MechanicalCarry.nonzero_negative alpha theta q p k hlo hneg).mp hk
    rw [abs_of_neg hneg,abs_lt]
    constructor <;> linarith [Int.fract_nonneg (theta+(h : ℝ)*alpha),
      Int.fract_nonneg (theta+(k : ℝ)*alpha)]

/-- The difference of phase floors is an explicit integer return numerator. -/
theorem phase_difference (alpha theta : ℝ) (h k : Nat) (horder : h ≤ k) :
    ((k-h : Nat) : ℝ)*alpha-
        ((MechanicalCarry.level alpha theta k-MechanicalCarry.level alpha theta h : Int) : ℝ) =
      Int.fract (theta+(k : ℝ)*alpha)-Int.fract (theta+(h : ℝ)*alpha) := by
  unfold MechanicalCarry.level
  rw [Nat.cast_sub horder]
  push_cast
  nlinarith [Int.floor_add_fract (theta+(h : ℝ)*alpha),
    Int.floor_add_fract (theta+(k : ℝ)*alpha)]

/-- Genuine visits to the actual carry arc are separated by at least Q. -/
theorem return_spacing (alpha theta : ℝ) (q Q : Nat) (p P d : Int)
    (hq : 0 < q) (hQ : 0 < Q)
    (hdet : p*(Q : Int)-P*(q : Int) = d) (hd : d*d = 1)
    (hsigns : ((q : ℝ)*alpha-p)*((Q : ℝ)*alpha-P) < 0)
    (hlo : -1 < (q : ℝ)*alpha-p) (hhi : (q : ℝ)*alpha-p < 1)
    (h k : Nat) (hhk : h < k)
    (hh : MechanicalCarry.carry alpha theta q p h ≠ 0)
    (hk : MechanicalCarry.carry alpha theta q p k ≠ 0) : h+Q ≤ k := by
  by_contra hnot
  have hm : 0 < k-h := by omega
  have hmQ : k-h < Q := by omega
  have hne : (q : ℝ)*alpha-p ≠ 0 := by
    intro hz
    rw [hz,zero_mul] at hsigns
    exact (lt_irrefl 0) hsigns
  have hclose := phases_close alpha theta q p h k hlo hhi hne hh hk
  let A : Int := MechanicalCarry.level alpha theta k-MechanicalCarry.level alpha theta h
  have hsharp := SharpAdjacentReturn.sharp_return alpha p (q : Int) P (Q : Int) A
    ((k-h : Nat) : Int) d (by exact_mod_cast hq) (by exact_mod_cast hQ)
    (by exact_mod_cast hm) (by exact_mod_cast hmQ) hdet hd (by exact_mod_cast hsigns)
  push_cast at hsharp
  have heq : ((k-h : Nat) : ℝ)*alpha-(A : ℝ) =
      Int.fract (theta+(k : ℝ)*alpha)-Int.fract (theta+(h : ℝ)*alpha) := by
    exact phase_difference alpha theta h k hhk.le
  rw [heq] at hsharp
  exact (not_lt_of_ge hsharp) hclose

#print axioms CarryReturnSpacing.phases_close
#print axioms CarryReturnSpacing.phase_difference
#print axioms CarryReturnSpacing.return_spacing

end CarryReturnSpacing
