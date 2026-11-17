import ArcStepCodeDraft

/-!
# A concrete finite-union-of-intervals instance of the finite-step interface

UNCOMPILED/PROOF-SKETCH. Membership is in finitely many half-open real intervals and ALL their integer
translates. This describes circular arcs using real lifts; wrapped arcs need no special seam case.
There are 2*k SUPPLIED endpoint labels, not necessarily distinct or actual jumps. No disjointness,
endpoint sorting, nonemptiness or interval-length premise is needed. Empty/full/overlapping cases are
allowed. This is classical representation plumbing, not a new novelty claim.
-/

namespace ArcIntervalCode

def Member (k : Nat) (a b : Nat → ℝ) (x : ℝ) : Prop :=
  ∃ i : Nat, i < k ∧ ∃ z : ℤ, a i+z ≤ x ∧ x < b i+z

noncomputable def value (k : Nat) (a b : Nat → ℝ) (x : ℝ) : Bool := by
  classical
  exact decide (Member k a b x)

def endpoint (a b : Nat → ℝ) (j : Nat) : ℝ :=
  if j % 2 = 0 then a (j/2) else b (j/2)

theorem endpoint_even (a b : Nat → ℝ) (i : Nat) : endpoint a b (2*i) = a i := by
  have hd : (2*i)/2 = i := by omega
  have hm : (2*i)%2 = 0 := by omega
  simp [endpoint,hd,hm]

theorem endpoint_odd (a b : Nat → ℝ) (i : Nat) : endpoint a b (2*i+1) = b i := by
  have hd : (2*i+1)/2 = i := by omega
  have hm : (2*i+1)%2 = 1 := by omega
  simp [endpoint,hd,hm]

/-- Periodicity by reindexing the integer lift, without a circle quotient API. -/
theorem member_shift (k : Nat) (a b : Nat → ℝ) (x : ℝ) (w : ℤ) :
    Member k a b (x+w) ↔ Member k a b x := by
  constructor
  · rintro ⟨i,hi,z,hlo,hhi⟩
    refine ⟨i,hi,z-w,?_,?_⟩ <;> push_cast <;> linarith
  · rintro ⟨i,hi,z,hlo,hhi⟩
    refine ⟨i,hi,z+w,?_,?_⟩ <;> push_cast <;> linarith

theorem value_eq_of_member_iff (k : Nat) (a b : Nat → ℝ) (x y : ℝ)
    (h : Member k a b x ↔ Member k a b y) : value k a b x = value k a b y := by
  classical
  by_cases hx : Member k a b x
  · have hy := h.mp hx
    simp [value,hx,hy]
  · have hy : ¬ Member k a b y := fun hy => hx (h.mpr hy)
    simp [value,hx,hy]

/-- In a jump-free (x,y] window, the same lifted interval witness works in both directions. -/
theorem member_constant (k : Nat) (a b : Nat → ℝ) (x y : ℝ) (hxy : x ≤ y)
    (hnone : ∀ j : Nat, j < 2*k → ∀ z : ℤ, ¬ (x < endpoint a b j+z ∧ endpoint a b j+z ≤ y)) :
    Member k a b x ↔ Member k a b y := by
  constructor
  · rintro ⟨i,hi,z,hlo,hhi⟩
    have hyhi : y < b i+z := by
      by_contra hnot
      apply hnone (2*i+1) (by omega) z
      simpa only [endpoint_odd] using And.intro hhi (le_of_not_gt hnot)
    exact ⟨i,hi,z,le_trans hlo hxy,hyhi⟩
  · rintro ⟨i,hi,z,hlo,hhi⟩
    have hxlo : a i+z ≤ x := by
      by_contra hnot
      apply hnone (2*i) (by omega) z
      simpa only [endpoint_even] using And.intro (lt_of_not_ge hnot) hlo
    exact ⟨i,hi,z,hxlo,lt_of_le_of_lt hxy hhi⟩

/-- A conventional periodic finite union of half-open intervals satisfies the explicit StepCode interface. -/
noncomputable def code (k : Nat) (a b : Nat → ℝ) : ArcStepCode.StepCode (2*k) where
  value := value k a b
  endpoint := endpoint a b
  periodic := by
    intro x w
    apply value_eq_of_member_iff
    exact member_shift k a b x w
  constant_between := by
    intro x y hxy hnone
    apply value_eq_of_member_iff
    exact member_constant k a b x y hxy hnone

#print axioms ArcIntervalCode.member_shift
#print axioms ArcIntervalCode.member_constant
#print axioms ArcIntervalCode.code

end ArcIntervalCode
