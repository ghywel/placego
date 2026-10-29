import ActualCarrySpacing
import ActualOppositeCarry
import DenominatorBootstrap
import FiniteHorizonSelection
import ContinuantSequence

/-!
# The uniform finite horizon for irrational mechanical words (G135, statement 1)

UNCOMPILED assembly draft, Local L1170. For every irrational `alpha`, every phase `theta` and every `C`, the
standard half-open mechanical word `mech alpha theta s = ⌊θ+(s+1)α⌋ − ⌊θ+sα⌋` violates the finite repeat bound
through the inclusive index `N = 251*(C+4)`: some repetition of positive lag `q` on `[a, b]`, with `b+q ≤ N`, has
`b > 2a+q+C`. No bound on partial quotients is assumed, and `alpha` need not lie in `(0, 1)`.

This assembles components carried two-party (G135/L088, L1151, L1153, L1164, L1166, L1168): the crossing
`q_r ≤ T < q_(r+1)` with `T = 2C+8`, five guarded growth steps (four for the budget and a fifth at `q_(r+4)`, GC2159's
guard), coefficient forcing at three scales, three selected carry visits, two exact opposite-arc shifts and the final
contradiction. Every finite-prefix fact is literal; nothing is assumed about the continued fraction.

Scope: the qualitative existence of SOME uniform deadline is known (Bugeaud–Kim with compactness, GC2134); only the
explicit constant is a candidate contribution, subject to prior-art review. Rational and endpoint slopes, recodings
(G136) and the physical Rule 30 restart are separate statements, not made here.
-/

namespace UniformHorizon

open FiniteHorizonContinuants
open Rule30Equivalents.Lagrange

/-- Coefficient forcing: the growth bound at scale `m+1` and a large denominator at scale `m` give `digit (m+2) = 1`. -/
theorem digit_eq_one {alpha : ℝ} (ha : Irrational alpha) (C m : Nat)
    (hgrowth : ArcRotation.denominator alpha (m+2) ≤ 2*ArcRotation.denominator alpha (m+1)+2*C+6)
    (hprev : 2*C+6 < ArcRotation.denominator alpha m) :
    digit alpha (m+2) = 1 := by
  have hpos : 1 ≤ digit alpha (m+2) := one_le_digit ha (m+1)
  have hnat : (digit alpha (m+2)).toNat = 1 :=
    FiniteHorizonSelection.coefficient_one C (digit alpha (m+2)).toNat
      (ArcRotation.denominator alpha (m+1)) (ArcRotation.denominator alpha m)
      (ArcRotation.denominator alpha (m+2))
      (by omega) (FiniteHorizonContinuantSequence.denominator_recurrence ha m) hgrowth hprev
  omega

/-- A unit coefficient makes the next denominator the sum of the previous two. -/
theorem recurrence_one {alpha : ℝ} (ha : Irrational alpha) (m : Nat) (hone : digit alpha (m+2) = 1) :
    ArcRotation.denominator alpha (m+2) =
      ArcRotation.denominator alpha (m+1)+ArcRotation.denominator alpha m := by
  rw [FiniteHorizonContinuantSequence.denominator_recurrence ha m, hone]
  simp

/-- **G135, statement 1.** No finite repeat bound with constant `C` survives through `251*(C+4)`. -/
theorem uniform_horizon (alpha theta : ℝ) (ha : Irrational alpha) (C : Nat) :
    ¬ FiniteHorizonBounds.RepeatBoundThrough (MechanicalCarry.mech alpha theta) (251*(C+4)) C := by
  intro hr
  -- the initial crossing q_r ≤ T < q_(r+1), T = 2C+8
  obtain ⟨r, hr0, hr1⟩ := FiniteHorizonContinuantSequence.threshold_crossing ha C
  -- every growth step whose input deadline fits
  have hg : ∀ n, DenominatorBootstrap.GrowthAt (251*(C+4)) C (ArcRotation.denominator alpha n)
      (ArcRotation.denominator alpha (n+1)) := by
    intro n hdl
    obtain ⟨_, _, _, _, h⟩ := FiniteHorizonActualCarry.denominator_growth alpha theta ha (251*(C+4)) C n hr hdl
    exact h
  -- the four-step budget, from q_r ≤ T
  have hb := DenominatorBootstrap.four_steps C (ArcRotation.denominator alpha r)
    (ArcRotation.denominator alpha (r+1)) (ArcRotation.denominator alpha (r+2))
    (ArcRotation.denominator alpha (r+3)) (ArcRotation.denominator alpha (r+4)) hr0
    (hg r) (hg (r+1)) (hg (r+2)) (hg (r+3))
  obtain ⟨_, hb2, hb3, hb4, _⟩ := hb
  -- monotone denominators, restated with canonical indices
  have hm1 : ArcRotation.denominator alpha (r+1) ≤ ArcRotation.denominator alpha (r+2) :=
    FiniteHorizonContinuantSequence.denominator_successive ha (r+1)
  have hm2 : ArcRotation.denominator alpha (r+2) ≤ ArcRotation.denominator alpha (r+3) :=
    FiniteHorizonContinuantSequence.denominator_successive ha (r+2)
  -- three selected visits, at the scales r+2, r+3 and r+4 (the third is the fifth growth call)
  obtain ⟨h2, hz2, hu2, hl2, hgr2⟩ := FiniteHorizonActualCarry.denominator_growth alpha theta ha
    (251*(C+4)) C (r+2) hr (by omega)
  obtain ⟨h3, hz3, hu3, hl3, hgr3⟩ := FiniteHorizonActualCarry.denominator_growth alpha theta ha
    (251*(C+4)) C (r+3) hr (by omega)
  obtain ⟨h4, hz4, hu4, hl4, hgr4⟩ := FiniteHorizonActualCarry.denominator_growth alpha theta ha
    (251*(C+4)) C (r+4) hr (by omega)
  have hl2' : ArcRotation.denominator alpha (r+3) ≤ h2+ArcRotation.denominator alpha (r+2)+C+4 := hl2
  have hl3' : ArcRotation.denominator alpha (r+4) ≤ h3+ArcRotation.denominator alpha (r+3)+C+4 := hl3
  have hl4' : ArcRotation.denominator alpha (r+5) ≤ h4+ArcRotation.denominator alpha (r+4)+C+4 := hl4
  have hgr2' : ArcRotation.denominator alpha (r+3) ≤ 2*ArcRotation.denominator alpha (r+2)+2*C+6 := hgr2
  have hgr3' : ArcRotation.denominator alpha (r+4) ≤ 2*ArcRotation.denominator alpha (r+3)+2*C+6 := hgr3
  have hgr4' : ArcRotation.denominator alpha (r+5) ≤ 2*ArcRotation.denominator alpha (r+4)+2*C+6 := hgr4
  -- coefficient forcing at the three scales
  have hd3 : digit alpha (r+3) = 1 := digit_eq_one ha C (r+1) hgr2' (by omega)
  have hd4 : digit alpha (r+4) = 1 := digit_eq_one ha C (r+2) hgr3' (by omega)
  have hd5 : digit alpha (r+5) = 1 := digit_eq_one ha C (r+3) hgr4' (by omega)
  have hrec3 : ArcRotation.denominator alpha (r+3) =
      ArcRotation.denominator alpha (r+2)+ArcRotation.denominator alpha (r+1) := recurrence_one ha (r+1) hd3
  have hrec4 : ArcRotation.denominator alpha (r+4) =
      ArcRotation.denominator alpha (r+3)+ArcRotation.denominator alpha (r+2) := recurrence_one ha (r+2) hd4
  -- the two exact opposite-arc shifts
  have hs1 : h3 = h2+ArcRotation.denominator alpha (r+2) :=
    FiniteHorizonActualOpposite.visit_shift alpha theta ha (r+1) C h2 h3 hd3 hd4 (by omega)
      hl2' hu2 hl3' hu3 hz2 hz3
  have hs2 : h4 = h3+ArcRotation.denominator alpha (r+3) :=
    FiniteHorizonActualOpposite.visit_shift alpha theta ha (r+2) C h3 h4 hd4 hd5 (by omega)
      hl3' hu3 hl4' hu4 hz3 hz4
  -- the final contradiction: q_(r+1) ≤ 2C+6, against q_(r+1) > 2C+8
  exact DenominatorBootstrap.final_visit_contradiction C (ArcRotation.denominator alpha (r+1))
    (ArcRotation.denominator alpha (r+2)) (ArcRotation.denominator alpha (r+3))
    (ArcRotation.denominator alpha (r+4)) h2 h3 h4 hr1 hrec4 (by omega) hu4 hs1 hs2

/-- **G135, statement 1, as an explicit witness** (the GC2133 form). -/
theorem uniform_horizon_witness (alpha theta : ℝ) (ha : Irrational alpha) (C : Nat) :
    ∃ q a b, 0 < q ∧ a ≤ b ∧ b+q ≤ 251*(C+4) ∧
      (∀ s, a ≤ s → s ≤ b → MechanicalCarry.mech alpha theta (s+q) = MechanicalCarry.mech alpha theta s) ∧
      2*a+q+C < b := by
  by_contra hno
  apply uniform_horizon alpha theta ha C
  intro q a b hq hab hN heq
  by_contra hbig
  exact hno ⟨q, a, b, hq, hab, hN, heq, by omega⟩

#print axioms UniformHorizon.digit_eq_one
#print axioms UniformHorizon.recurrence_one
#print axioms UniformHorizon.uniform_horizon
#print axioms UniformHorizon.uniform_horizon_witness

end UniformHorizon
