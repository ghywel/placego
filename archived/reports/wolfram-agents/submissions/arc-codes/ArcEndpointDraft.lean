import ArcStepCodeDraft
import ArcTailBounds
import Mathlib.NumberTheory.Real.Irrational

/-!
# Finite endpoint changes along an irrational rotation

UNCOMPILED integration of the known G131/G132 endpoint argument. Actual finite-step constancy is supplied
by StepCode; this file does not infer it from a picture or a generic function's name. Only endpoint values
may differ from that supplied code. Each integer-translate endpoint class is hit at most once, so the
core finite-exception transfer applies. No effective last-visit deadline follows from endpoint count.
-/

namespace ArcEndpoint

def Hit (endpoint : Nat → ℝ) (alpha theta : ℝ) (i n : Nat) : Prop :=
  ∃ z : ℤ, theta+(n : ℝ)*alpha = endpoint i+z

/-- Two visits to one endpoint class would make alpha a ratio of integers. -/
theorem hit_unique {alpha : ℝ} (ha : Irrational alpha) (endpoint : Nat → ℝ) (theta : ℝ)
    (i s t : Nat) (hs : Hit endpoint alpha theta i s) (ht : Hit endpoint alpha theta i t) : s = t := by
  obtain ⟨z,hz⟩ := hs
  obtain ⟨w,hw⟩ := ht
  by_contra hst
  have hstInt : (s : ℤ) ≠ (t : ℤ) := by exact_mod_cast hst
  have hn : (s : ℤ)-(t : ℤ) ≠ 0 := sub_ne_zero.mpr hstInt
  have hden : (((s : ℤ)-(t : ℤ) : ℤ) : ℝ) ≠ 0 := by exact_mod_cast hn
  apply ha.ne_rational (z-w) ((s : ℤ)-(t : ℤ))
  apply (eq_div_iff hden).2
  push_cast
  nlinarith [hz,hw]

/-- Any colouring which differs only at the listed endpoint translates eventually has the same sampled code.
    No periodicity is needed for its exceptional values at different integer translates. -/
theorem eventual_agreement {r : Nat} (S : ArcStepCode.StepCode r) (g : ℝ → Bool) (alpha theta : ℝ)
    (ha : Irrational alpha)
    (hoff : ∀ x : ℝ, (∀ i : Nat, i < r → ∀ z : ℤ, x ≠ S.endpoint i+z) → g x = S.value x) :
    ∃ N : Nat, ∀ n : Nat, N ≤ n →
      g (theta+(n : ℝ)*alpha) = ArcStepCode.orbit S alpha theta n := by
  apply ArcTailBounds.finite_single_hits_eventual
    (fun n => g (theta+(n : ℝ)*alpha)) (ArcStepCode.orbit S alpha theta) r
    (Hit S.endpoint alpha theta)
  · intro i _ s t hs ht
    exact hit_unique ha S.endpoint theta i s t hs ht
  · intro n hbad
    apply Classical.byContradiction
    intro hno
    apply hbad
    apply hoff
    intro i hi z hz
    exact hno ⟨i,hi,z,hz⟩

#print axioms ArcEndpoint.hit_unique
#print axioms ArcEndpoint.eventual_agreement

end ArcEndpoint
