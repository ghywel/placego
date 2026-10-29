import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Lean.Elab.Tactic.NormCast

/-!
# Sharp return exclusion from adjacent integer approximations

UNCOMPILED staging source, GC2138. Classical best approximation reconstructed
from the adjacent-basis argument carried in L1153, not an additional submission.
No actual continuants, rotation arcs or Rule30 orbit are constructed here.
-/

namespace SharpAdjacentReturn

/-- Coordinates in an integer basis of determinant d with d^2=1. -/
theorem basis_coordinates (p q P Q a m d : Int)
    (hdet : p*Q-P*q = d) (hd : d*d = 1) :
    let u := d*(a*Q-P*m)
    let v := d*(p*m-a*q)
    u*p+v*P = a ∧ u*q+v*Q = m := by
  dsimp only
  constructor
  · calc
      d*(a*Q-P*m)*p+d*(p*m-a*q)*P = d*a*(p*Q-P*q) := by ring
      _ = a := by
        rw [hdet]
        calc d*a*d = a*(d*d) := by ring
             _ = a := by rw [hd]; ring
  · calc
      d*(a*Q-P*m)*q+d*(p*m-a*q)*Q = d*m*(p*Q-P*q) := by ring
      _ = m := by
        rw [hdet]
        calc d*m*d = m*(d*d) := by ring
             _ = m := by rw [hd]; ring

/-- Opposite signed errors cannot cancel at a positive coordinate smaller than Q. -/
theorem positive_error_bound (q Q u v : Int) (epsilon eta : ℝ)
    (hq : 0 < q) (hQ : 0 < Q)
    (hm : 0 < u*q+v*Q) (hmQ : u*q+v*Q < Q)
    (hepsilon : 0 < epsilon) (heta : eta < 0) :
    epsilon ≤ |(u : ℝ)*epsilon+(v : ℝ)*eta| := by
  by_cases hu : u ≤ 0
  · have hv : 0 < v := by
      by_contra hnot
      have hvle : v ≤ 0 := le_of_not_gt hnot
      have huq := mul_nonpos_of_nonpos_of_nonneg hu hq.le
      have hvQ := mul_nonpos_of_nonpos_of_nonneg hvle hQ.le
      omega
    have huone : u ≤ -1 := by
      by_contra hnot
      have hu0 : u = 0 := by omega
      have hvone : 1 ≤ v := by omega
      have hb := mul_le_mul_of_nonneg_right hvone hQ.le
      rw [hu0] at hmQ
      nlinarith
    have huR : (u : ℝ) ≤ -1 := by exact_mod_cast huone
    have hvR : (0 : ℝ) ≤ v := by exact_mod_cast hv.le
    have hleft := mul_le_mul_of_nonneg_right huR hepsilon.le
    have hright := mul_nonpos_of_nonneg_of_nonpos hvR heta.le
    have hsum : (u : ℝ)*epsilon+(v : ℝ)*eta ≤ -epsilon := by nlinarith
    rw [abs_of_nonpos (show (u : ℝ)*epsilon+(v : ℝ)*eta ≤ 0 by linarith)]
    linarith
  · have huone : 1 ≤ u := by omega
    have hv : v ≤ 0 := by
      by_contra hnot
      have hvone : 1 ≤ v := by omega
      have huq := mul_nonneg (by omega : 0 ≤ u) hq.le
      have hb := mul_le_mul_of_nonneg_right hvone hQ.le
      nlinarith
    have huR : (1 : ℝ) ≤ u := by exact_mod_cast huone
    have hvR : (v : ℝ) ≤ 0 := by exact_mod_cast hv
    have hleft := mul_le_mul_of_nonneg_right huR hepsilon.le
    have hright := mul_nonneg_of_nonpos_of_nonpos hvR heta.le
    have hsum : epsilon ≤ (u : ℝ)*epsilon+(v : ℝ)*eta := by nlinarith
    exact le_trans hsum (le_abs_self _)

/-- Sharp adjacent-convergent form, with determinant and error signs explicit. -/
theorem sharp_return (alpha : ℝ) (p q P Q a m d : Int)
    (hq : 0 < q) (hQ : 0 < Q) (hm : 0 < m) (hmQ : m < Q)
    (hdet : p*Q-P*q = d) (hd : d*d = 1)
    (hsigns : ((q : ℝ)*alpha-p)*((Q : ℝ)*alpha-P) < 0) :
    |(q : ℝ)*alpha-p| ≤ |(m : ℝ)*alpha-a| := by
  let u := d*(a*Q-P*m)
  let v := d*(p*m-a*q)
  obtain ⟨ha,hcoord⟩ := basis_coordinates p q P Q a m d hdet hd
  change u*p+v*P = a at ha
  change u*q+v*Q = m at hcoord
  have hm' : 0 < u*q+v*Q := by rw [hcoord]; exact hm
  have hmQ' : u*q+v*Q < Q := by rw [hcoord]; exact hmQ
  let epsilon := (q : ℝ)*alpha-p
  let eta := (Q : ℝ)*alpha-P
  have herr : (m : ℝ)*alpha-a = (u : ℝ)*epsilon+(v : ℝ)*eta := by
    rw [← hcoord,← ha]
    dsimp [epsilon,eta]
    push_cast
    ring
  change epsilon*eta < 0 at hsigns
  change |epsilon| ≤ |(m : ℝ)*alpha-a|
  rw [herr]
  by_cases hepsilon : 0 < epsilon
  · have heta : eta < 0 := by
      by_contra hnot
      have hp := mul_nonneg hepsilon.le (le_of_not_gt hnot)
      linarith
    rw [abs_of_pos hepsilon]
    exact positive_error_bound q Q u v epsilon eta hq hQ hm' hmQ' hepsilon heta
  · have hepsilonNeg : epsilon < 0 := by
      have hle : epsilon ≤ 0 := le_of_not_gt hepsilon
      by_contra hnot
      have hz : epsilon = 0 := by linarith
      rw [hz,zero_mul] at hsigns
      exact (lt_irrefl 0) hsigns
    have heta : 0 < eta := by
      by_contra hnot
      have hp := mul_nonneg_of_nonpos_of_nonpos hepsilonNeg.le (le_of_not_gt hnot)
      linarith
    have h := positive_error_bound q Q u v (-epsilon) (-eta) hq hQ hm' hmQ'
      (by linarith) (by linarith)
    have heq : (u : ℝ)*(-epsilon)+(v : ℝ)*(-eta) = -((u : ℝ)*epsilon+(v : ℝ)*eta) := by ring
    rw [heq,abs_neg] at h
    rw [abs_of_neg hepsilonNeg]
    exact h

/-- Independent guard control: without opposite errors, the claimed lower bound fails. -/
theorem same_sign_control :
    ((0 : Int)*2-1*1)^2 = 1 ∧
    0 < ((1 : ℝ)*(3/5)-0)*((2 : ℝ)*(3/5)-1) ∧
    |(1 : ℝ)*(3/5)-1| < |(1 : ℝ)*(3/5)-0| := by
  norm_num

/-- Independent endpoint control: m=Q must be excluded, even with opposite errors. -/
theorem endpoint_control :
    ((1 : Int)*3-2*2)^2 = 1 ∧
    ((2 : ℝ)*(5/8)-1)*((3 : ℝ)*(5/8)-2) < 0 ∧
    |(3 : ℝ)*(5/8)-2| < |(2 : ℝ)*(5/8)-1| := by
  norm_num

#print axioms SharpAdjacentReturn.basis_coordinates
#print axioms SharpAdjacentReturn.positive_error_bound
#print axioms SharpAdjacentReturn.sharp_return
#print axioms SharpAdjacentReturn.same_sign_control
#print axioms SharpAdjacentReturn.endpoint_control

end SharpAdjacentReturn
