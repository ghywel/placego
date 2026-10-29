import UniformHorizon

/-!
# The uniform horizon for every slope and for every finite recoding (G136, statement 2)

UNCOMPILED draft, Local L1171. Extends `UniformHorizon.uniform_horizon` (irrational slopes) in two steps.

* Every real slope, rational and endpoint slopes included. The prefix through `N` of a mechanical word is also the
  prefix of a mechanical word with an irrational slope: push every sample point up by a small positive amount. The
  floor is right-continuous, so each of the finitely many floors is kept (L1151's simplification of G136).
* Every recoding `c s = F (g s, …, g (s+w))` of width `w+1`, with any `F` and any codomain: no repeat bound with
  constant `C` survives through `251*(C+4)+250*w`. Statement 1 with constant `C+w` supplies a repetition `[a, e]` with
  `e > 2a+q+C+w ≥ a+w`, and `[a, e-w]` is then a forbidden repetition of `c` (GC2133's margin).

The width guard is essential and is kept in the statement: unrestricted widths can fit any finite target prefix (G136).
No physical Rule 30 statement is made here.
-/

namespace RecodedHorizon

open MechanicalCarry

/-- The finite repeat bound sees only the prefix through `N`. -/
theorem repeat_bound_congr {β : Type} (c d : Nat → β) (N C : Nat) (hcd : ∀ s, s ≤ N → c s = d s)
    (h : FiniteHorizonBounds.RepeatBoundThrough c N C) : FiniteHorizonBounds.RepeatBoundThrough d N C := by
  intro q a b hq hab hN heq
  apply h q a b hq hab hN
  intro s hs1 hs2
  rw [hcd (s+q) (by omega), hcd s (by omega)]
  exact heq s hs1 hs2

/-- A positive margin below finitely many positive numbers. -/
theorem finite_margin (f : Nat → ℝ) (hf : ∀ s, 0 < f s) :
    ∀ n, ∃ δ, 0 < δ ∧ ∀ s, s ≤ n → δ ≤ f s
  | 0 => ⟨f 0, hf 0, fun s hs => by
      have hs0 : s = 0 := by omega
      subst hs0
      exact le_refl _⟩
  | n+1 => by
    obtain ⟨δ, hδ, hle⟩ := finite_margin f hf n
    refine ⟨min δ (f (n+1)), lt_min hδ (hf (n+1)), fun s hs => ?_⟩
    by_cases h : s ≤ n
    · exact le_trans (min_le_left _ _) (hle s h)
    · have hsn : s = n+1 := by omega
      subst hsn
      exact min_le_right _ _

/-- Right-continuity of the floor: a small nonnegative push keeps it. -/
theorem floor_stable (x d : ℝ) (h0 : 0 ≤ d) (h1 : d < (⌊x⌋ : ℝ)+1-x) : ⌊x+d⌋ = ⌊x⌋ := by
  rw [Int.floor_eq_iff]
  constructor
  · linarith [Int.floor_le x]
  · linarith

/-- Every finite stretch of floors along a real slope is matched along an irrational slope. -/
theorem exists_irrational_agree (alpha theta : ℝ) (n : Nat) :
    ∃ beta, Irrational beta ∧ ∀ s, s ≤ n → level beta theta s = level alpha theta s := by
  by_cases hα : Irrational alpha
  · exact ⟨alpha, hα, fun _ _ => rfl⟩
  · have hmem : alpha ∈ Set.range ((↑) : ℚ → ℝ) := by
      unfold Irrational at hα
      exact not_not.mp hα
    obtain ⟨r, hr⟩ := hmem
    let f : Nat → ℝ := fun s => (⌊theta+(s : ℝ)*alpha⌋ : ℝ)+1-(theta+(s : ℝ)*alpha)
    have hf : ∀ s, 0 < f s := fun s => by
      have := Int.lt_floor_add_one (theta+(s : ℝ)*alpha)
      show 0 < (⌊theta+(s : ℝ)*alpha⌋ : ℝ)+1-(theta+(s : ℝ)*alpha)
      linarith
    obtain ⟨δ, hδ, hle⟩ := finite_margin f hf n
    have hn : (0 : ℝ) < (n : ℝ)+1 := by positivity
    obtain ⟨ε, hεirr, hε0, hε1⟩ := exists_irrational_btwn (div_pos hδ hn)
    refine ⟨alpha+ε, ?_, fun s hs => ?_⟩
    · rw [← hr, add_comm]
      exact hεirr.add_ratCast r
    · unfold level
      have hsR : (s : ℝ) ≤ (n : ℝ) := by exact_mod_cast hs
      have hpush : (s : ℝ)*ε < f s := by
        have h1 : (s : ℝ)*ε ≤ (n : ℝ)*ε := mul_le_mul_of_nonneg_right hsR hε0.le
        have h2 : ((n : ℝ)+1)*ε < δ := by
          rw [lt_div_iff₀ hn] at hε1
          linarith
        have h3 := hle s hs
        nlinarith
      have hnonneg : (0 : ℝ) ≤ (s : ℝ)*ε := mul_nonneg (Nat.cast_nonneg s) hε0.le
      have hrw : theta+(s : ℝ)*(alpha+ε) = (theta+(s : ℝ)*alpha)+(s : ℝ)*ε := by ring
      rw [hrw]
      exact floor_stable _ _ hnonneg hpush

/-- **Statement 1 for every real slope.** -/
theorem uniform_horizon_all (alpha theta : ℝ) (C : Nat) :
    ¬ FiniteHorizonBounds.RepeatBoundThrough (mech alpha theta) (251*(C+4)) C := by
  obtain ⟨beta, hbeta, hagree⟩ := exists_irrational_agree alpha theta (251*(C+4)+1)
  intro hr
  apply UniformHorizon.uniform_horizon beta theta hbeta C
  apply repeat_bound_congr (mech alpha theta) (mech beta theta) _ _ _ hr
  intro s hs
  unfold mech
  rw [hagree (s+1) (by omega), hagree s (by omega)]

/-- A recoding of width `w+1`: each output reads the `w+1` letters starting at `s`. -/
def recode {β : Type} (w : Nat) (F : (Fin (w+1) → Int) → β) (g : Nat → Int) (s : Nat) : β :=
  F (fun i => g (s+i))

/-- **Statement 2 (G136).** Any recoding of width `w+1` violates the bound through `251*(C+4)+250*w`. -/
theorem recoded_horizon {β : Type} (alpha theta : ℝ) (C w : Nat) (F : (Fin (w+1) → Int) → β) :
    ¬ FiniteHorizonBounds.RepeatBoundThrough (recode w F (mech alpha theta)) (251*(C+4)+250*w) C := by
  intro hr
  apply uniform_horizon_all alpha theta (C+w)
  intro q a e hq _hae hN heq
  apply Classical.byContradiction
  intro hbig
  have hc := hr q a (e-w) hq (by omega) (by omega) (fun s hs1 hs2 => by
    unfold recode
    congr 1
    funext i
    have hi := i.isLt
    rw [show s+q+(i : Nat) = s+(i : Nat)+q by omega]
    exact heq (s+(i : Nat)) (by omega) (by omega))
  omega

#print axioms RecodedHorizon.repeat_bound_congr
#print axioms RecodedHorizon.finite_margin
#print axioms RecodedHorizon.floor_stable
#print axioms RecodedHorizon.exists_irrational_agree
#print axioms RecodedHorizon.uniform_horizon_all
#print axioms RecodedHorizon.recoded_horizon

end RecodedHorizon
