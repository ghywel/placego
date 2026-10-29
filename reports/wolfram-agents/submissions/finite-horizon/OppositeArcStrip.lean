import SharpAdjacentReturn

/-!
# A signed adjacent-basis strip forces the exact negative return

UNCOMPILED staging component, GC2159. This is the opposite-arc separation
interface for the existing G134/G135 hand proof, not the final finite horizon.
Actual floor-carry arcs and actual continuants are separate callers. No build,
new computation, current-toolchain acceptance or additional submission follows.
-/

namespace OppositeArcStrip

/-- The finite visit bounds themselves give the exact signed spatial strip.
The two recurrences are the coefficient-one conclusions of the caller. -/
theorem visit_difference_bounds (C previous q next after h k : Nat)
    (hnext : next = q+previous) (hafter : after = next+q)
    (hlow : next ≤ h+q+C+4) (hupp : h ≤ q+C+2)
    (klow : after ≤ k+next+C+4) (kupp : k ≤ next+C+2) :
    -(q : Int)-(2*(C : Int)+6) ≤ (h : Int)-(k : Int) ∧
      (h : Int)-(k : Int) ≤ 2*(C : Int)+6 := by
  omega

/-- With negative first error and positive second error, the spatial strip
and the open error strip force the basis coordinates (0,-1). -/
theorem negative_error_coordinates (q Q D u v : Int) (epsilon eta : ℝ)
    (hq : 0 < q) (hqQ : q ≤ Q) (hD : D < q)
    (hlow : -Q-D ≤ u*q+v*Q) (hupp : u*q+v*Q ≤ D)
    (hepsilon : epsilon < 0) (heta : 0 < eta)
    (herrlow : epsilon < (u : ℝ)*epsilon+(v : ℝ)*eta)
    (herrupp : (u : ℝ)*epsilon+(v : ℝ)*eta < 0) :
    u = 0 ∧ v = -1 := by
  have hQ : 0 < Q := lt_of_lt_of_le hq hqQ
  by_cases hu : 0 < u
  · have huone : 1 ≤ u := by omega
    by_cases hv : 0 ≤ v
    · have hleft := mul_le_mul_of_nonneg_right huone hq.le
      have hright := mul_nonneg hv hQ.le
      nlinarith
    · have hvone : v ≤ -1 := by omega
      have huR : (1 : ℝ) ≤ u := by exact_mod_cast huone
      have hvR : (v : ℝ) ≤ -1 := by exact_mod_cast hvone
      have hleft := mul_le_mul_of_nonpos_right huR hepsilon.le
      have hright := mul_le_mul_of_nonneg_right hvR heta.le
      nlinarith
  · by_cases huneg : u < 0
    · have huone : u ≤ -1 := by omega
      by_cases hv : v ≤ -1
      · have hleft := mul_le_mul_of_nonneg_right huone hq.le
        have hright := mul_le_mul_of_nonneg_right hv hQ.le
        nlinarith
      · have hvzero : 0 ≤ v := by omega
        have huR : (u : ℝ) ≤ -1 := by exact_mod_cast huone
        have hvR : (0 : ℝ) ≤ v := by exact_mod_cast hvzero
        have hleft := mul_le_mul_of_nonpos_right huR hepsilon.le
        have hright := mul_nonneg hvR heta.le
        nlinarith
    · have huzero : u = 0 := by omega
      have hvneg : v < 0 := by
        by_contra hnot
        have hvzero : (0 : ℝ) ≤ v := by exact_mod_cast (le_of_not_gt hnot)
        have hright := mul_nonneg hvzero heta.le
        rw [huzero,Int.cast_zero,zero_mul,zero_add] at herrupp
        linarith
      have hvone : v = -1 := by
        by_contra hnot
        have hvtwo : v ≤ -2 := by omega
        have hright := mul_le_mul_of_nonneg_right hvtwo hQ.le
        rw [huzero,zero_mul,zero_add] at hlow
        nlinarith
      exact ⟨huzero,hvone⟩

/-- Orientation-independent version: the return error has the opposite sign
to the second basis error and is strictly smaller than the first error. -/
theorem signed_coordinates (q Q D u v : Int) (epsilon eta : ℝ)
    (hq : 0 < q) (hqQ : q ≤ Q) (hD : D < q)
    (hlow : -Q-D ≤ u*q+v*Q) (hupp : u*q+v*Q ≤ D)
    (hsigns : epsilon*eta < 0)
    (hreturn : ((u : ℝ)*epsilon+(v : ℝ)*eta)*eta < 0)
    (hclose : |(u : ℝ)*epsilon+(v : ℝ)*eta| < |epsilon|) :
    u = 0 ∧ v = -1 := by
  by_cases heta : 0 < eta
  · have hepsilon : epsilon < 0 := by
      by_contra hnot
      have h := mul_nonneg (le_of_not_gt hnot) heta.le
      linarith
    have herr : (u : ℝ)*epsilon+(v : ℝ)*eta < 0 := by
      by_contra hnot
      have h := mul_nonneg (le_of_not_gt hnot) heta.le
      linarith
    rw [abs_of_neg herr,abs_of_neg hepsilon] at hclose
    exact negative_error_coordinates q Q D u v epsilon eta hq hqQ hD hlow hupp
      hepsilon heta (by linarith) herr
  · have hetaNeg : eta < 0 := by
      rcases lt_or_eq_of_le (le_of_not_gt heta) with h | h
      · exact h
      · rw [h,mul_zero] at hsigns
        exact False.elim ((lt_irrefl 0) hsigns)
    have hepsilon : 0 < epsilon := by
      by_contra hnot
      have h := mul_nonneg_of_nonpos_of_nonpos (le_of_not_gt hnot) hetaNeg.le
      linarith
    have herr : 0 < (u : ℝ)*epsilon+(v : ℝ)*eta := by
      by_contra hnot
      have h := mul_nonneg_of_nonpos_of_nonpos (le_of_not_gt hnot) hetaNeg.le
      linarith
    rw [abs_of_pos herr,abs_of_pos hepsilon] at hclose
    have heq : (u : ℝ)*(-epsilon)+(v : ℝ)*(-eta) =
        -((u : ℝ)*epsilon+(v : ℝ)*eta) := by ring
    apply negative_error_coordinates q Q D u v (-epsilon) (-eta) hq hqQ hD hlow hupp
      (by linarith) (by linarith)
    · rw [heq]
      linarith
    · rw [heq]
      linarith

/-- Adjacent integer data convert the coordinate conclusion to an exact
signed denominator and numerator, with no circle-norm API or offset search. -/
theorem exact_negative_return (alpha : ℝ) (p q P Q a m d D : Int)
    (hq : 0 < q) (hqQ : q ≤ Q) (hD : D < q)
    (hlow : -Q-D ≤ m) (hupp : m ≤ D)
    (hdet : p*Q-P*q = d) (hd : d*d = 1)
    (hsigns : ((q : ℝ)*alpha-p)*((Q : ℝ)*alpha-P) < 0)
    (hreturn : ((m : ℝ)*alpha-a)*((Q : ℝ)*alpha-P) < 0)
    (hclose : |(m : ℝ)*alpha-a| < |(q : ℝ)*alpha-p|) :
    m = -Q ∧ a = -P := by
  let u := d*(a*Q-P*m)
  let v := d*(p*m-a*q)
  obtain ⟨hnum,hden⟩ := SharpAdjacentReturn.basis_coordinates p q P Q a m d hdet hd
  change u*p+v*P = a at hnum
  change u*q+v*Q = m at hden
  have herr : (m : ℝ)*alpha-a =
      (u : ℝ)*((q : ℝ)*alpha-p)+(v : ℝ)*((Q : ℝ)*alpha-P) := by
    rw [← hden,← hnum]
    push_cast
    ring
  have hlo : -Q-D ≤ u*q+v*Q := by rw [hden]; exact hlow
  have hhi : u*q+v*Q ≤ D := by rw [hden]; exact hupp
  rw [herr] at hreturn hclose
  obtain ⟨hu,hv⟩ := signed_coordinates q Q D u v
    ((q : ℝ)*alpha-p) ((Q : ℝ)*alpha-P) hq hqQ hD hlo hhi hsigns hreturn hclose
  constructor
  · rw [← hden,hu,hv]
    ring
  · rw [← hnum,hu,hv]
    ring

/-- The width guard cannot be replaced by D<=q in this general interface. -/
theorem width_endpoint_control :
    let alpha : ℝ := 7/10
    let p : Int := 1
    let q : Int := 1
    let P : Int := 1
    let Q : Int := 2
    let D : Int := 1
    let m : Int := -3
    let a : Int := -2
    p*Q-P*q = 1 ∧ 0 < q ∧ q ≤ Q ∧ D = q ∧
      -Q-D ≤ m ∧ m ≤ D ∧
      ((q : ℝ)*alpha-p)*((Q : ℝ)*alpha-P) < 0 ∧
      ((m : ℝ)*alpha-a)*((Q : ℝ)*alpha-P) < 0 ∧
      |(m : ℝ)*alpha-a| < |(q : ℝ)*alpha-p| ∧ m ≠ -Q := by
  norm_num

#print axioms OppositeArcStrip.visit_difference_bounds
#print axioms OppositeArcStrip.negative_error_coordinates
#print axioms OppositeArcStrip.signed_coordinates
#print axioms OppositeArcStrip.exact_negative_return
#print axioms OppositeArcStrip.width_endpoint_control

end OppositeArcStrip
