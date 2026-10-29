import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Lean.Elab.Tactic.NormCast

/-!
# Elementary spacing from a rational approximation

Uncompiled draft. This is the number-theoretic component of the arc argument, not a Rule30 theorem.
The integer Bezout identity is explicit so the kit's continuant determinant can instantiate it directly.
-/

namespace ArcDeterminant

/-- The unit determinant of consecutive continuants gives an explicit Bezout identity. -/
theorem bezout_of_unit_determinant (p q previousP previousQ sign : ℤ)
    (hsign : sign*sign = 1) (hdet : p*previousQ-previousP*q = sign) :
    (sign*previousQ)*p+(-sign*previousP)*q = 1 := by
  calc
    (sign*previousQ)*p+(-sign*previousP)*q = sign*(p*previousQ-previousP*q) := by ring
    _ = 1 := by rw [hdet]; exact hsign

/-- A return closer than the error of a reduced approximation must have `(m+q)*error > 1`. -/
theorem spacing_of_bezout (alpha : ℝ) (p q m a u v : ℤ)
    (hq : 0 < q) (hm : 0 < m) (hbezout : u*p+v*q = 1)
    (hepsilon : 0 < |(q : ℝ)*alpha-p|)
    (hclose : |(m : ℝ)*alpha-a| < |(q : ℝ)*alpha-p|) :
    1 < ((m : ℝ)+q)*|(q : ℝ)*alpha-p| := by
  by_contra hnot
  have hupper : ((m : ℝ)+q)*|(q : ℝ)*alpha-p| ≤ 1 := le_of_not_gt hnot
  have hqR : (0 : ℝ) < q := by exact_mod_cast hq
  have hmR : (0 : ℝ) < m := by exact_mod_cast hm
  let D : ℤ := q*a-m*p
  have hDsmall : |(D : ℝ)| < 1 := by
    calc
      |(D : ℝ)| = |(m : ℝ)*((q : ℝ)*alpha-p)-(q : ℝ)*((m : ℝ)*alpha-a)| := by
        dsimp [D]
        push_cast
        congr 1
        ring
      _ ≤ |(m : ℝ)*((q : ℝ)*alpha-p)|+|(q : ℝ)*((m : ℝ)*alpha-a)| := abs_sub _ _
      _ = (m : ℝ)*|(q : ℝ)*alpha-p|+(q : ℝ)*|(m : ℝ)*alpha-a| := by
        rw [abs_mul,abs_mul,abs_of_pos hmR,abs_of_pos hqR]
      _ < ((m : ℝ)+q)*|(q : ℝ)*alpha-p| := by
        have h := mul_lt_mul_of_pos_left hclose hqR
        nlinarith
      _ ≤ 1 := hupper
  have hDint : |D| < 1 := by exact_mod_cast hDsmall
  have hDzero : D = 0 := by
    have h := abs_lt.mp hDint
    omega
  let k : ℤ := u*a+v*m
  have hmk : m = q*k := by
    dsimp [k,D] at *
    linear_combination (-m) * hbezout - u * hDzero
  have hak : a = p*k := by
    dsimp [k,D] at *
    linear_combination (-a) * hbezout + v * hDzero
  have hkpos : 0 < k := by
    by_contra hh
    have hkle : k ≤ 0 := le_of_not_gt hh
    have hprod : q*k ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hq.le hkle
    rw [← hmk] at hprod
    omega
  have hkone : (1 : ℝ) ≤ k := by exact_mod_cast (show 1 ≤ k by omega)
  have herror : |(m : ℝ)*alpha-a| = (k : ℝ)*|(q : ℝ)*alpha-p| := by
    calc
      |(m : ℝ)*alpha-a| = |(k : ℝ)*((q : ℝ)*alpha-p)| := by
        rw [hmk,hak]
        push_cast
        congr 1
        ring
      _ = (k : ℝ)*|(q : ℝ)*alpha-p| := by
        rw [abs_mul,abs_of_pos (by exact_mod_cast hkpos)]
  rw [herror] at hclose
  nlinarith

/-- One-scale contradiction in the form used after finite-colour break counting. -/
theorem no_short_return (alpha : ℝ) (p q m a u v : ℤ) (B : ℝ)
    (hq : 0 < q) (hm : 0 < m) (hbezout : u*p+v*q = 1)
    (hepsilon : 0 < |(q : ℝ)*alpha-p|) (hmB : (m : ℝ) < B)
    (hscale : (B+q)*|(q : ℝ)*alpha-p| ≤ 1) :
    ¬ |(m : ℝ)*alpha-a| < |(q : ℝ)*alpha-p| := by
  intro hclose
  have h := spacing_of_bezout alpha p q m a u v hq hm hbezout hepsilon hclose
  have hlt := mul_lt_mul_of_pos_right (add_lt_add_right hmB (q : ℝ)) hepsilon
  linarith

#print axioms ArcDeterminant.spacing_of_bezout
#print axioms ArcDeterminant.no_short_return

end ArcDeterminant
