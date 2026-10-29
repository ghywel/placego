import ArcContinuantsDraft
import ArcStepCodeDraft

/-!
# Large continued-fraction digits violate a uniform repeat bound for finite-step rotation codes

UNCOMPILED assembly draft. Uses the kit's actual Lagrange continuants, not a substitute continued-fraction
sequence. StepCode's constancy interface is explicit. No Rule30 physical repeat bridge or arbitrary-endpoint
restart is proved here. A dependency lookup/install/compiler run is not authorized by writing this source.
-/

namespace ArcRotation

open Rule30Equivalents.Lagrange

/-- Natural form of the actual denominator continuant; positivity below requires irrational input. -/
noncomputable def denominator (alpha : ℝ) (n : Nat) : Nat := (contQ (digit alpha) (n+2)).toNat

theorem denominator_cast {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    (denominator alpha n : ℤ) = contQ (digit alpha) (n+2) := by
  exact Int.toNat_of_nonneg (contQ_nonneg (fun k => one_le_digit ha k) (n+2))

theorem denominator_real {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    (denominator alpha n : ℝ) = (contQ (digit alpha) (n+2) : ℝ) := by
  exact_mod_cast denominator_cast ha n

theorem denominator_pos {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    0 < denominator alpha n := by
  have h : (1 : ℤ) ≤ (denominator alpha n : ℤ) := by
    rw [denominator_cast ha n]
    exact one_le_contQ (fun k => one_le_digit ha k) n
  omega

/-- The integer recurrence has no truncation loss when converted to natural denominators/digits. -/
theorem denominator_next {alpha : ℝ} (ha : Irrational alpha) (n : Nat) (hn : 1 ≤ n) :
    denominator alpha (n+1) = (digit alpha (n+1)).toNat*denominator alpha n+denominator alpha (n-1) := by
  have hdnonneg : (0 : ℤ) ≤ digit alpha (n+1) := le_trans (by decide) (one_le_digit ha n)
  have hi : (denominator alpha (n+1) : ℤ) =
      ((digit alpha (n+1)).toNat : ℤ)*(denominator alpha n : ℤ)+(denominator alpha (n-1) : ℤ) := by
    rw [denominator_cast ha (n+1),denominator_cast ha n,denominator_cast ha (n-1),
      Int.toNat_of_nonneg hdnonneg,show n-1+2 = n+1 by omega]
    rfl
  exact_mod_cast hi

/-- A large enough index makes the previous denominator pay any fixed break-window margin. -/
theorem previous_margin {alpha : ℝ} (ha : Irrational alpha) (K C n : Nat)
    (hn : K*(C+2)+2 ≤ n) : K*(C+2) ≤ denominator alpha (n-1) := by
  have hn2 : 2 ≤ n := by omega
  have hg := contQ_ge (fun k => one_le_digit ha k) (n-2)
  rw [show n-2+3 = (n-1)+2 by omega,← denominator_cast ha (n-1)] at hg
  have hb : K*(C+2) ≤ (n-2)+1 := by omega
  have hbInt : ((K*(C+2) : Nat) : ℤ) ≤ ((n-2 : Nat) : ℤ)+1 := by exact_mod_cast hb
  have h := le_trans hbInt hg
  exact_mod_cast h

/-- At the original digit threshold, the next denominator covers the entire counting window plus q. -/
theorem next_covers_window {alpha : ℝ} (ha : Irrational alpha) (K C n : Nat)
    (hn : K*(C+2)+2 ≤ n) (hdigit : (K : ℤ) < digit alpha (n+1)) :
    K*(denominator alpha n+C+2)+denominator alpha n ≤ denominator alpha (n+1) := by
  have hdnonneg : (0 : ℤ) ≤ digit alpha (n+1) := le_trans (by decide) (one_le_digit ha n)
  have hdcast : ((digit alpha (n+1)).toNat : ℤ) = digit alpha (n+1) := Int.toNat_of_nonneg hdnonneg
  have hdNat : K < (digit alpha (n+1)).toNat := by
    have h : (K : ℤ) < ((digit alpha (n+1)).toNat : ℤ) := by rw [hdcast]; exact hdigit
    exact_mod_cast h
  exact ArcBreakBounds.next_denominator_covers_window K (denominator alpha n) C
    (denominator alpha (n-1)) ((digit alpha (n+1)).toNat) (denominator alpha (n+1))
    hdNat (previous_margin ha K C n hn) (denominator_next ha n (by omega))

/-- One sufficiently late large digit supplies every approximation premise of the finite-step exclusion. -/
theorem no_repeat_at_large_digit {r : Nat} (S : ArcStepCode.StepCode r) (alpha theta : ℝ)
    (ha : Irrational alpha) (C n : Nat)
    (hn : 2^(r+1)*(C+2)+2 ≤ n) (hdigit : ((2^(r+1) : Nat) : ℤ) < digit alpha (n+1)) :
    ¬ ArcBreakSequence.RepeatBound (ArcStepCode.orbit S alpha theta) (denominator alpha n) C := by
  let p : ℤ := contP (digit alpha) (n+2)
  let u : ℤ := (-1)^(n+1)*contQ (digit alpha) (n+1)
  let v : ℤ := -((-1)^(n+1))*contP (digit alpha) (n+1)
  have hbez : u*p+v*(denominator alpha n : ℤ) = 1 := by
    rw [denominator_cast ha n]
    exact ArcDeterminant.continuant_bezout alpha n
  have he := ArcDeterminant.continuant_error_lt_next ha n
  dsimp only at he
  have hepos : 0 < |(denominator alpha n : ℝ)*alpha-p| := by
    rw [denominator_real ha n]
    simpa only [mul_comm] using he.1
  have heupper : |(denominator alpha n : ℝ)*alpha-p| < 1/(denominator alpha (n+1) : ℝ) := by
    rw [denominator_real ha n,denominator_real ha (n+1)]
    simpa only [mul_comm,Nat.add_assoc] using he.2
  have hnpos : (0 : ℝ) < denominator alpha (n+1) := by exact_mod_cast denominator_pos ha (n+1)
  have hprod : |(denominator alpha n : ℝ)*alpha-p| * (denominator alpha (n+1) : ℝ) < 1 :=
    (lt_div_iff₀ hnpos).1 heupper
  have hmargin := next_covers_window ha (2^(r+1)) C n hn hdigit
  have hmarginR : (((2^(r+1)*(denominator alpha n+C+2) : Nat) : ℝ)+(denominator alpha n : ℝ)) ≤
      (denominator alpha (n+1) : ℝ) := by exact_mod_cast hmargin
  have hscale : (((2^(r+1)*(denominator alpha n+C+2) : Nat) : ℝ)+(denominator alpha n : ℝ))*
      |(denominator alpha n : ℝ)*alpha-p| ≤ 1 := by
    have hmul := mul_le_mul_of_nonneg_right hmarginR hepos.le
    nlinarith
  exact ArcStepCode.no_repeat_bound S alpha theta (denominator alpha n) C p u v
    (denominator_pos ha n) hbez hepos hscale

/-- Infinitely late digits above the original threshold contradict every fixed repeat obstruction constant. -/
theorem repeat_bound_fails {r : Nat} (S : ArcStepCode.StepCode r) (alpha theta : ℝ)
    (ha : Irrational alpha)
    (hlarge : ∀ N : Nat, ∃ n : Nat, N ≤ n ∧ ((2^(r+1) : Nat) : ℤ) < digit alpha (n+1)) (C : Nat) :
    ∃ q : Nat, 0 < q ∧ ¬ ArcBreakSequence.RepeatBound (ArcStepCode.orbit S alpha theta) q C := by
  obtain ⟨n,hn,hdigit⟩ := hlarge (2^(r+1)*(C+2)+2)
  exact ⟨denominator alpha n,denominator_pos ha n,no_repeat_at_large_digit S alpha theta ha C n hn hdigit⟩

/-- Abstract rotation-code exclusion; the physical Rule30 bridge must still supply the uniform bound. -/
theorem no_uniform_repeat_bound {r : Nat} (S : ArcStepCode.StepCode r) (alpha theta : ℝ)
    (ha : Irrational alpha)
    (hlarge : ∀ N : Nat, ∃ n : Nat, N ≤ n ∧ ((2^(r+1) : Nat) : ℤ) < digit alpha (n+1)) :
    ¬ ∃ C : Nat, ∀ q : Nat, 0 < q → ArcBreakSequence.RepeatBound (ArcStepCode.orbit S alpha theta) q C := by
  rintro ⟨C,hC⟩
  obtain ⟨q,hq,hnot⟩ := repeat_bound_fails S alpha theta ha hlarge C
  exact hnot (hC q hq)

#print axioms ArcRotation.denominator_next
#print axioms ArcRotation.previous_margin
#print axioms ArcRotation.next_covers_window
#print axioms ArcRotation.no_repeat_at_large_digit
#print axioms ArcRotation.repeat_bound_fails
#print axioms ArcRotation.no_uniform_repeat_bound

end ArcRotation
