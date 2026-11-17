import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.Archimedean.Real.Basic
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Lean.Elab.Tactic.NormCast

/-!
# Actual mechanical derivatives and their signed carry arcs

UNCOMPILED staging component, GC2142. The floor-shift argument is the known
helper in R30-20261023-8084e6, reconstructed with an arbitrary integer p and
signed error. This supplies the actual carry, not a hypothesis of arc membership.
No continuant, return spacing, finite horizon or Rule30 theorem is asserted.
-/

namespace MechanicalCarry

noncomputable def level (alpha theta : ℝ) (s : Nat) : Int :=
  ⌊theta+(s : ℝ)*alpha⌋

noncomputable def mech (alpha theta : ℝ) (s : Nat) : Int :=
  level alpha theta (s+1)-level alpha theta s

noncomputable def carry (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat) : Int :=
  level alpha theta (s+q)-level alpha theta s-p

/-- Cancellation, with all Nat-index shifts made explicit. -/
theorem difference_identity (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat) :
    mech alpha theta (s+q)-mech alpha theta s =
      carry alpha theta q p (s+1)-carry alpha theta q p s := by
  unfold mech carry
  rw [show s+q+1 = s+1+q by omega]
  omega

/-- An arbitrary integer approximation p leaves the floor of fractional phase plus signed error. -/
theorem carry_as_floor (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat) :
    carry alpha theta q p s =
      ⌊Int.fract (theta+(s : ℝ)*alpha)+((q : ℝ)*alpha-p)⌋ := by
  have hf := Int.floor_add_fract (theta+(s : ℝ)*alpha)
  have e : theta+((s+q : Nat) : ℝ)*alpha =
      ((⌊theta+(s : ℝ)*alpha⌋+p : Int) : ℝ)+
        (Int.fract (theta+(s : ℝ)*alpha)+((q : ℝ)*alpha-p)) := by
    calc
      theta+((s+q : Nat) : ℝ)*alpha = (theta+(s : ℝ)*alpha)+(q : ℝ)*alpha := by
        push_cast
        ring
      _ = _ := by push_cast; linarith
  unfold carry level
  rw [e,Int.floor_intCast_add]
  omega

/-- Positive error gives a left-closed upper carry arc. -/
theorem carry_positive (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat)
    (h0 : 0 < (q : ℝ)*alpha-p) (h1 : (q : ℝ)*alpha-p < 1) :
    carry alpha theta q p s =
      if 1-((q : ℝ)*alpha-p) ≤ Int.fract (theta+(s : ℝ)*alpha) then 1 else 0 := by
  rw [carry_as_floor]
  by_cases h : 1-((q : ℝ)*alpha-p) ≤ Int.fract (theta+(s : ℝ)*alpha)
  · rw [ite_eq_left h,Int.floor_eq_iff]
    constructor <;> push_cast <;> linarith [Int.fract_nonneg (theta+(s : ℝ)*alpha),
      Int.fract_lt_one (theta+(s : ℝ)*alpha)]
  · rw [ite_eq_right h,Int.floor_eq_iff]
    constructor <;> push_cast <;> linarith [Int.fract_nonneg (theta+(s : ℝ)*alpha),
      Int.fract_lt_one (theta+(s : ℝ)*alpha)]

/-- Negative error gives a right-open lower carry arc and carry value -1. -/
theorem carry_negative (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat)
    (h0 : -1 < (q : ℝ)*alpha-p) (h1 : (q : ℝ)*alpha-p < 0) :
    carry alpha theta q p s =
      if Int.fract (theta+(s : ℝ)*alpha) < -((q : ℝ)*alpha-p) then -1 else 0 := by
  rw [carry_as_floor]
  by_cases h : Int.fract (theta+(s : ℝ)*alpha) < -((q : ℝ)*alpha-p)
  · rw [ite_eq_left h,Int.floor_eq_iff]
    constructor <;> push_cast <;> linarith [Int.fract_nonneg (theta+(s : ℝ)*alpha),
      Int.fract_lt_one (theta+(s : ℝ)*alpha)]
  · rw [ite_eq_right h,Int.floor_eq_iff]
    constructor <;> push_cast <;> linarith [Int.fract_nonneg (theta+(s : ℝ)*alpha),
      Int.fract_lt_one (theta+(s : ℝ)*alpha)]

theorem nonzero_positive (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat)
    (h0 : 0 < (q : ℝ)*alpha-p) (h1 : (q : ℝ)*alpha-p < 1) :
    carry alpha theta q p s ≠ 0 ↔
      1-((q : ℝ)*alpha-p) ≤ Int.fract (theta+(s : ℝ)*alpha) := by
  rw [carry_positive alpha theta q p s h0 h1]
  by_cases h : 1-((q : ℝ)*alpha-p) ≤ Int.fract (theta+(s : ℝ)*alpha)
  · rw [ite_eq_left h]
    exact ⟨fun _ => h, fun _ => by decide⟩
  · rw [ite_eq_right h]
    exact ⟨fun hne => absurd rfl hne, fun hh => absurd hh h⟩

theorem nonzero_negative (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat)
    (h0 : -1 < (q : ℝ)*alpha-p) (h1 : (q : ℝ)*alpha-p < 0) :
    carry alpha theta q p s ≠ 0 ↔
      Int.fract (theta+(s : ℝ)*alpha) < -((q : ℝ)*alpha-p) := by
  rw [carry_negative alpha theta q p s h0 h1]
  by_cases h : Int.fract (theta+(s : ℝ)*alpha) < -((q : ℝ)*alpha-p)
  · rw [ite_eq_left h]
    exact ⟨fun _ => h, fun _ => by decide⟩
  · rw [ite_eq_right h]
    exact ⟨fun hne => absurd rfl hne, fun hh => absurd hh h⟩

/-- Endpoint controls: the positive arc includes its threshold; the negative arc excludes its threshold. -/
theorem half_open_endpoint_controls :
    carry (1/4) (3/4) 1 0 0 = 1 ∧ carry (3/4) (1/4) 1 1 0 = 0 := by
  norm_num [carry,level]

#print axioms MechanicalCarry.difference_identity
#print axioms MechanicalCarry.carry_as_floor
#print axioms MechanicalCarry.carry_positive
#print axioms MechanicalCarry.carry_negative
#print axioms MechanicalCarry.nonzero_positive
#print axioms MechanicalCarry.nonzero_negative
#print axioms MechanicalCarry.half_open_endpoint_controls

end MechanicalCarry
