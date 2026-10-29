/-!
# Finite threshold selection and coefficient forcing

UNCOMPILED staging component, GC2148. Pure Nat adapters for the G135 argument;
no continued fraction is replaced by an abstract model or constructed here.
The actual caller must supply its denominator sequence, recurrence and growth.
-/

namespace FiniteHorizonSelection

/-- A coefficient at least two would consume more than the allowed denominator growth. -/
theorem coefficient_one (C a q previous next : Nat)
    (ha : 1 ≤ a) (hrec : next = a*q+previous)
    (hgrowth : next ≤ 2*q+2*C+6) (hprevious : 2*C+6 < previous) : a = 1 := by
  by_contra hnot
  have ha2 : 2 ≤ a := by omega
  have hprod := Nat.mul_le_mul_right q ha2
  omega

/-- A supplied finite witness above the threshold gives a crossing before it, without a least-index operator. -/
theorem crossing_before (q : Nat → Nat) (T : Nat) (h0 : q 0 ≤ T) (n : Nat) :
    T < q n → ∃ r, r < n ∧ q r ≤ T ∧ T < q (r+1) := by
  induction n with
  | zero => intro hn; omega
  | succ n ih =>
    intro hn
    by_cases h : T < q n
    · obtain ⟨r,hr,hlo,hhi⟩ := ih h
      exact ⟨r,by omega,hlo,hhi⟩
    · exact ⟨n,by omega,le_of_not_gt h,hn⟩

/-- Only unboundedness and q0=1 are needed to select the initial usable scale. -/
theorem crossing_scale (q : Nat → Nat) (T : Nat) (hT : 1 ≤ T)
    (h0 : q 0 = 1) (hunbounded : ∀ B, ∃ n, B < q n) :
    ∃ r, q r ≤ T ∧ T < q (r+1) := by
  obtain ⟨n,hn⟩ := hunbounded T
  obtain ⟨r,_,hlo,hhi⟩ := crossing_before q T (by omega) n hn
  exact ⟨r,hlo,hhi⟩

/-- Positive recurrence coefficients make all successive denominators nondecreasing. -/
theorem successive_ge (q a : Nat → Nat)
    (h0 : q 0 ≤ q 1) (ha : ∀ n, 1 ≤ a (n+2))
    (hrec : ∀ n, q (n+2) = a (n+2)*q (n+1)+q n) :
    ∀ n, q n ≤ q (n+1) := by
  intro n
  cases n with
  | zero => exact h0
  | succ n =>
    have hprod := Nat.mul_le_mul_right (q (n+1)) (ha n)
    have hr := hrec n
    omega

#print axioms FiniteHorizonSelection.coefficient_one
#print axioms FiniteHorizonSelection.crossing_before
#print axioms FiniteHorizonSelection.crossing_scale
#print axioms FiniteHorizonSelection.successive_ge

end FiniteHorizonSelection
