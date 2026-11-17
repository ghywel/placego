import MechanicalCarry
import OppositeArcStrip

/-!
# Actual opposite carry arcs give the signed error used by the strip lemma

UNCOMPILED staging component, GC2159. Carries are the actual floor-defined
MechanicalCarry objects. The continued-fraction data and error-size identity
remain explicit caller obligations. This is not the assembled 251 horizon.
-/

namespace OppositeCarryArcs

/-- Coefficient one makes the two opposite arc lengths add to the preceding error. -/
theorem error_sizes (previous current next : ℝ)
    (hrec : next = current+previous)
    (hprev : previous*current < 0) (hnext : current*next < 0) :
    |current|+|next| = |previous| := by
  by_cases hpos : 0 < current
  · have hp : previous < 0 := by
      by_contra hnot
      have h := mul_nonneg (le_of_not_gt hnot) hpos.le
      linarith
    have hn : next < 0 := by
      by_contra hnot
      have h := mul_nonneg hpos.le (le_of_not_gt hnot)
      linarith
    rw [abs_of_pos hpos,abs_of_neg hn,abs_of_neg hp]
    linarith
  · have hneg : current < 0 := by
      rcases lt_or_eq_of_le (le_of_not_gt hpos) with h | h
      · exact h
      · rw [h,mul_zero] at hprev
        exact False.elim ((lt_irrefl 0) hprev)
    have hp : 0 < previous := by
      by_contra hnot
      have h := mul_nonneg_of_nonpos_of_nonpos (le_of_not_gt hnot) hneg.le
      linarith
    have hn : 0 < next := by
      by_contra hnot
      have h := mul_nonneg_of_nonpos_of_nonpos hneg.le (le_of_not_gt hnot)
      linarith
    rw [abs_of_neg hneg,abs_of_pos hn,abs_of_pos hp]
    linarith

/-- Signed time differences do not need a preliminary ordering of the visits. -/
theorem phase_difference (alpha theta : ℝ) (h k : Nat) :
    (((h : Int)-(k : Int) : Int) : ℝ)*alpha-
        ((MechanicalCarry.level alpha theta h-MechanicalCarry.level alpha theta k : Int) : ℝ) =
      Int.fract (theta+(h : ℝ)*alpha)-Int.fract (theta+(k : ℝ)*alpha) := by
  unfold MechanicalCarry.level
  push_cast
  nlinarith [Int.floor_add_fract (theta+(h : ℝ)*alpha),
    Int.floor_add_fract (theta+(k : ℝ)*alpha)]

/-- Opposite actual carry visits straddle zero on the circle. Choosing the
integer lift on the other side of that cut retains a strict signed error. -/
theorem error_witness (alpha theta : ℝ) (q Q : Nat) (p P : Int) (h k : Nat)
    (hlo : -1 < (q : ℝ)*alpha-p) (hhi : (q : ℝ)*alpha-p < 1)
    (Hlo : -1 < (Q : ℝ)*alpha-P) (Hhi : (Q : ℝ)*alpha-P < 1)
    (hsigns : ((q : ℝ)*alpha-p)*((Q : ℝ)*alpha-P) < 0)
    (hh : MechanicalCarry.carry alpha theta q p h ≠ 0)
    (hk : MechanicalCarry.carry alpha theta Q P k ≠ 0) :
    ∃ a : Int,
      ((((h : Int)-(k : Int) : Int) : ℝ)*alpha-a)*((q : ℝ)*alpha-p) < 0 ∧
      |(((h : Int)-(k : Int) : Int) : ℝ)*alpha-a| <
        |(q : ℝ)*alpha-p|+|(Q : ℝ)*alpha-P| := by
  let A : Int := MechanicalCarry.level alpha theta h-MechanicalCarry.level alpha theta k
  have heq := phase_difference alpha theta h k
  change (((h : Int)-(k : Int) : Int) : ℝ)*alpha-(A : ℝ) = _ at heq
  push_cast at heq
  by_cases hpos : 0 < (q : ℝ)*alpha-p
  · have Hneg : (Q : ℝ)*alpha-P < 0 := by
      by_contra hnot
      have h := mul_nonneg hpos.le (le_of_not_gt hnot)
      linarith
    have hx := (MechanicalCarry.nonzero_positive alpha theta q p h hpos hhi).mp hh
    have hy := (MechanicalCarry.nonzero_negative alpha theta Q P k Hlo Hneg).mp hk
    have herror : (((h : Int)-(k : Int) : Int) : ℝ)*alpha-((A+1 : Int) : ℝ) < 0 := by
      push_cast
      linarith [Int.fract_lt_one (theta+(h : ℝ)*alpha),
        Int.fract_nonneg (theta+(k : ℝ)*alpha)]
    refine ⟨A+1,mul_neg_of_neg_of_pos herror hpos,?_⟩
    rw [abs_of_neg herror,abs_of_pos hpos,abs_of_neg Hneg]
    push_cast
    linarith
  · have hneg : (q : ℝ)*alpha-p < 0 := by
      rcases lt_or_eq_of_le (le_of_not_gt hpos) with h | h
      · exact h
      · rw [h,zero_mul] at hsigns
        exact False.elim ((lt_irrefl 0) hsigns)
    have Hpos : 0 < (Q : ℝ)*alpha-P := by
      by_contra hnot
      have h := mul_nonneg_of_nonpos_of_nonpos hneg.le (le_of_not_gt hnot)
      linarith
    have hx := (MechanicalCarry.nonzero_negative alpha theta q p h hlo hneg).mp hh
    have hy := (MechanicalCarry.nonzero_positive alpha theta Q P k Hpos Hhi).mp hk
    have herror : 0 < (((h : Int)-(k : Int) : Int) : ℝ)*alpha-((A-1 : Int) : ℝ) := by
      push_cast
      linarith [Int.fract_nonneg (theta+(h : ℝ)*alpha),
        Int.fract_lt_one (theta+(k : ℝ)*alpha)]
    refine ⟨A-1,mul_neg_of_pos_of_neg herror hneg,?_⟩
    rw [abs_of_pos herror,abs_of_neg hneg,abs_of_pos Hpos]
    push_cast
    linarith

/-- The exact selected-visit shift, with actual carries and no first-visit
operator. The caller supplies the coefficient-one error-size identity. -/
theorem visit_shift (alpha theta : ℝ) (previous q next : Nat) (pPrevious p pNext d D : Int)
    (h k : Nat) (hprevious : 0 < previous) (hq : previous ≤ q) (hD : D < previous)
    (hlow : -(q : Int)-D ≤ (h : Int)-(k : Int))
    (hupp : (h : Int)-(k : Int) ≤ D)
    (hdet : pPrevious*(q : Int)-p*(previous : Int) = d) (hd : d*d = 1)
    (hprevsign : ((previous : ℝ)*alpha-pPrevious)*((q : ℝ)*alpha-p) < 0)
    (hnextsign : ((q : ℝ)*alpha-p)*((next : ℝ)*alpha-pNext) < 0)
    (hsize : |(q : ℝ)*alpha-p|+|(next : ℝ)*alpha-pNext| =
      |(previous : ℝ)*alpha-pPrevious|)
    (hlo : -1 < (q : ℝ)*alpha-p) (hhi : (q : ℝ)*alpha-p < 1)
    (Hlo : -1 < (next : ℝ)*alpha-pNext) (Hhi : (next : ℝ)*alpha-pNext < 1)
    (hh : MechanicalCarry.carry alpha theta q p h ≠ 0)
    (hk : MechanicalCarry.carry alpha theta next pNext k ≠ 0) : k = h+q := by
  obtain ⟨a,hsign,hclose⟩ := error_witness alpha theta q next p pNext h k hlo hhi Hlo Hhi
    hnextsign hh hk
  rw [hsize] at hclose
  have hexact := OppositeArcStrip.exact_negative_return alpha pPrevious (previous : Int)
    p (q : Int) a ((h : Int)-(k : Int)) d D (by exact_mod_cast hprevious)
    (by exact_mod_cast hq) hD hlow hupp hdet hd
    (by exact_mod_cast hprevsign) (by exact_mod_cast hsign) (by exact_mod_cast hclose)
  have hshift := hexact.1
  omega

#print axioms OppositeCarryArcs.error_sizes
#print axioms OppositeCarryArcs.phase_difference
#print axioms OppositeCarryArcs.error_witness
#print axioms OppositeCarryArcs.visit_shift

end OppositeCarryArcs
