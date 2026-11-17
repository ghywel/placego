import ArcRotationDraft

/-!
# Actual continuant determinant and signed-error inputs

UNCOMPILED staging source, GC2144. Reuses the actual continuants and natural
denominator adapters of the already delivered arc development. It does not
replace the continued fraction by an abstract sequence. Existing ArcRotationDraft
and its dependencies must be available as exact compiled modules before checking.
No library build, new validation run or complete horizon theorem follows here.
-/

namespace FiniteHorizonContinuants

open Rule30Equivalents.Lagrange

noncomputable def numerator (alpha : ℝ) (n : Nat) : Int :=
  contP (digit alpha) (n+2)

noncomputable def error (alpha : ℝ) (n : Nat) : ℝ :=
  (ArcRotation.denominator alpha n : ℝ)*alpha-numerator alpha n

noncomputable def multiplier (alpha : ℝ) (n : Nat) : ℝ :=
  cq alpha (n+1)*(ArcRotation.denominator alpha n : ℝ)+
    (contQ (digit alpha) (n+1) : ℝ)

/-- The same positive multiplier as the kit's exact error_mul identity. -/
theorem multiplier_pos {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    0 < multiplier alpha n := by
  have hq : (0 : ℝ) < ArcRotation.denominator alpha n := by
    exact_mod_cast ArcRotation.denominator_pos ha n
  have hc : 0 < cq alpha (n+1) := lt_trans (by norm_num) (one_lt_cq ha n)
  have hp : (0 : ℝ) ≤ contQ (digit alpha) (n+1) := by
    exact_mod_cast contQ_nonneg (fun k => one_le_digit ha k) (n+1)
  have hprod := mul_pos hc hq
  unfold multiplier
  linarith

/-- The concrete signed error identity, with the public kit's index shift+2. -/
theorem error_identity {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    error alpha n*multiplier alpha n = (-1 : ℝ)^n := by
  dsimp only [error,multiplier,numerator]
  rw [ArcRotation.denominator_real ha n]
  simpa only [mul_comm] using error_mul ha n

/-- Adjacent errors of the ACTUAL continuants have opposite strict signs. -/
theorem adjacent_errors_opposite {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    error alpha n*error alpha (n+1) < 0 := by
  have h0 := error_identity ha n
  have h1 := error_identity ha (n+1)
  rw [pow_succ] at h1
  have hsquare : ((-1 : ℝ)^n)*((-1 : ℝ)^n) = 1 := by
    rw [← mul_pow]
    norm_num
  have hprod : (error alpha n*error alpha (n+1))*
      (multiplier alpha n*multiplier alpha (n+1)) = -1 := by
    calc
      _ = (error alpha n*multiplier alpha n)*
          (error alpha (n+1)*multiplier alpha (n+1)) := by ring
      _ = ((-1 : ℝ)^n)*(((-1 : ℝ)^n)*(-1)) := by rw [h0,h1]
      _ = -1 := by nlinarith [hsquare]
  have hpositive := mul_pos (multiplier_pos ha n) (multiplier_pos ha (n+1))
  by_contra hnot
  have hnonneg := mul_nonneg (le_of_not_gt hnot) hpositive.le
  linarith

/-- The adjacent integer determinant has square one, in sharp_return's orientation. -/
theorem adjacent_determinant_unit {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    let d := numerator alpha n*(ArcRotation.denominator alpha (n+1) : Int)-
      numerator alpha (n+1)*(ArcRotation.denominator alpha n : Int)
    d*d = 1 := by
  dsimp only
  rw [ArcRotation.denominator_cast ha (n+1),ArcRotation.denominator_cast ha n]
  unfold numerator
  have hdet := cont_det (digit alpha) (n+2)
  have hd : contP (digit alpha) (n+2)*contQ (digit alpha) (n+1+2)-
      contP (digit alpha) (n+1+2)*contQ (digit alpha) (n+2) = -((-1 : Int)^(n+2)) := by
    have heq : n+1+2 = n+2+1 := by omega
    rw [heq]
    linear_combination -hdet
  have hprod := congrArg (fun x : Int => x*x) hd
  rw [neg_mul_neg,← mul_pow] at hprod
  norm_num at hprod
  exact hprod

/-- The next-denominator approximation bound already proved in the arc development implies |error|<1. -/
theorem error_abs_lt_one {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    |error alpha n| < 1 := by
  have he := ArcDeterminant.continuant_error_lt_next ha n
  dsimp only at he
  have hbound : |error alpha n| < 1/(ArcRotation.denominator alpha (n+1) : ℝ) := by
    dsimp only [error,numerator]
    rw [ArcRotation.denominator_real ha n,ArcRotation.denominator_real ha (n+1)]
    simpa only [mul_comm,Nat.add_assoc] using he.2
  have hQ : (1 : ℝ) ≤ ArcRotation.denominator alpha (n+1) := by
    exact_mod_cast (show 1 ≤ ArcRotation.denominator alpha (n+1) from
      ArcRotation.denominator_pos ha (n+1))
  have hQpos : (0 : ℝ) < ArcRotation.denominator alpha (n+1) := by linarith
  have hrecip : 1/(ArcRotation.denominator alpha (n+1) : ℝ) ≤ 1 := by
    apply (div_le_iff₀ hQpos).2
    linarith
  exact lt_of_lt_of_le hbound hrecip

#print axioms FiniteHorizonContinuants.multiplier_pos
#print axioms FiniteHorizonContinuants.error_identity
#print axioms FiniteHorizonContinuants.adjacent_errors_opposite
#print axioms FiniteHorizonContinuants.adjacent_determinant_unit
#print axioms FiniteHorizonContinuants.error_abs_lt_one

end FiniteHorizonContinuants
