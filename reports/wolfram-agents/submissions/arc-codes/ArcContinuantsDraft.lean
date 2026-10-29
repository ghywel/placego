import Rule30Equivalents.Lagrange
import ArcDeterminantDraft

/-!
# Continuant inputs for the elementary spacing bound

UNCOMPILED draft. Requires the existing equivalents project and a compiled ArcDeterminantDraft on LEAN_PATH.
No dependency build or validation is implied by this source. The approximation facts are classical; these
lemmas expose the kit's exact definitions and indexing for the later rotation-code application.
-/

namespace ArcDeterminant

/-- The kit's consecutive continuants give the concrete coefficients for `spacing_of_bezout`. -/
theorem continuant_bezout (alpha : ℝ) (n : ℕ) :
    let sign : ℤ := (-1)^(n+1)
    let previousP := Rule30Equivalents.Lagrange.contP (Rule30Equivalents.Lagrange.digit alpha) (n+1)
    let previousQ := Rule30Equivalents.Lagrange.contQ (Rule30Equivalents.Lagrange.digit alpha) (n+1)
    let p := Rule30Equivalents.Lagrange.contP (Rule30Equivalents.Lagrange.digit alpha) (n+2)
    let q := Rule30Equivalents.Lagrange.contQ (Rule30Equivalents.Lagrange.digit alpha) (n+2)
    (sign*previousQ)*p+(-sign*previousP)*q = 1 := by
  dsimp only
  apply bezout_of_unit_determinant
  · rw [← mul_pow]
    norm_num
  · simpa [Nat.add_assoc] using
      Rule30Equivalents.Lagrange.cont_det (Rule30Equivalents.Lagrange.digit alpha) (n+1)

/-- The kit's exact error identity implies the strict next-denominator approximation bound. -/
theorem continuant_error_lt_next {alpha : ℝ} (halpha : Irrational alpha) (n : ℕ) :
    let a := Rule30Equivalents.Lagrange.digit alpha
    0 < |alpha*(Rule30Equivalents.Lagrange.contQ a (n+2) : ℝ)-Rule30Equivalents.Lagrange.contP a (n+2)| ∧
    |alpha*(Rule30Equivalents.Lagrange.contQ a (n+2) : ℝ)-Rule30Equivalents.Lagrange.contP a (n+2)| <
      1/(Rule30Equivalents.Lagrange.contQ a (n+3) : ℝ) := by
  dsimp only
  let a := Rule30Equivalents.Lagrange.digit alpha
  have ha : ∀ k, 1 ≤ a (k+1) := Rule30Equivalents.Lagrange.one_le_digit halpha
  have hqone : (1 : ℝ) ≤ Rule30Equivalents.Lagrange.contQ a (n+2) := by
    exact_mod_cast Rule30Equivalents.Lagrange.one_le_contQ ha n
  have hnxtone : (1 : ℝ) ≤ Rule30Equivalents.Lagrange.contQ a (n+3) := by
    exact_mod_cast Rule30Equivalents.Lagrange.one_le_contQ ha (n+1)
  have hqpos : (0 : ℝ) < Rule30Equivalents.Lagrange.contQ a (n+2) := by linarith
  have hnxtpos : (0 : ℝ) < Rule30Equivalents.Lagrange.contQ a (n+3) := by linarith
  have htailpos : 0 < (Rule30Equivalents.Lagrange.cq alpha (n+2))⁻¹ := by
    apply inv_pos.2
    have h := Rule30Equivalents.Lagrange.one_lt_cq halpha (n+1)
    linarith
  have hquot : (a (n+1) : ℝ) < Rule30Equivalents.Lagrange.cq alpha (n+1) := by
    have h := Rule30Equivalents.Lagrange.cq_eq_digit_add alpha (n+1)
    change Rule30Equivalents.Lagrange.cq alpha (n+1) =
      (a (n+1) : ℝ)+(Rule30Equivalents.Lagrange.cq alpha (n+2))⁻¹ at h
    linarith
  have hnxt : (Rule30Equivalents.Lagrange.contQ a (n+3) : ℝ) =
      (a (n+1) : ℝ)*Rule30Equivalents.Lagrange.contQ a (n+2)+
        Rule30Equivalents.Lagrange.contQ a (n+1) := by
    rw [show n+3 = (n+1)+2 by omega, Rule30Equivalents.Lagrange.contQ]
    push_cast
    rfl
  have hden : (Rule30Equivalents.Lagrange.contQ a (n+3) : ℝ) <
      Rule30Equivalents.Lagrange.cq alpha (n+1)*Rule30Equivalents.Lagrange.contQ a (n+2)+
        Rule30Equivalents.Lagrange.contQ a (n+1) := by
    have h := mul_pos (sub_pos.2 hquot) hqpos
    rw [hnxt]
    nlinarith
  have hdenpos : (0 : ℝ) <
      Rule30Equivalents.Lagrange.cq alpha (n+1)*Rule30Equivalents.Lagrange.contQ a (n+2)+
        Rule30Equivalents.Lagrange.contQ a (n+1) := lt_trans hnxtpos hden
  have he := congrArg abs (Rule30Equivalents.Lagrange.error_mul halpha n)
  rw [abs_mul,abs_pow,abs_neg,abs_one,one_pow,abs_of_pos hdenpos] at he
  have hepos : 0 < |alpha*(Rule30Equivalents.Lagrange.contQ a (n+2) : ℝ)-
      Rule30Equivalents.Lagrange.contP a (n+2)| := by
    have hn := abs_nonneg (alpha*(Rule30Equivalents.Lagrange.contQ a (n+2) : ℝ)-
      Rule30Equivalents.Lagrange.contP a (n+2))
    by_contra hnot
    have hzero := le_antisymm (le_of_not_gt hnot) hn
    change |alpha*(Rule30Equivalents.Lagrange.contQ a (n+2) : ℝ)-
      Rule30Equivalents.Lagrange.contP a (n+2)| * _ = 1 at he
    rw [hzero,zero_mul] at he
    norm_num at he
  refine ⟨hepos, (lt_div_iff₀ hnxtpos).2 ?_⟩
  have hprod := mul_lt_mul_of_pos_left hden hepos
  change |alpha*(Rule30Equivalents.Lagrange.contQ a (n+2) : ℝ)-
    Rule30Equivalents.Lagrange.contP a (n+2)| * _ = 1 at he
  linarith

#print axioms ArcDeterminant.continuant_bezout
#print axioms ArcDeterminant.continuant_error_lt_next

end ArcDeterminant
