import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Lean.Elab.Tactic.NormCast
/-! L1168 probe (Local): the `error_witness` pattern in OppositeCarryArcs (GC2159). After `push_cast` on the goal only,
does `linarith` still use a hypothesis whose cast of a difference was left unpushed? Prediction: the first example
FAILS (`↑(↑h - ↑k) * α` and `(↑h - ↑k) * α` are different atoms) and the second, `push_cast at heq ⊢`, PASSES. -/
example (h k : ℕ) (α A f g : ℝ) (heq : (((h : ℤ) - (k : ℤ) : ℤ) : ℝ) * α - A = f - g) (hf : f < 1) (hg : 0 ≤ g) :
    (((h : ℤ) - (k : ℤ) : ℤ) : ℝ) * α - (A + 1) < 0 := by
  push_cast
  linarith
example (h k : ℕ) (α A f g : ℝ) (heq : (((h : ℤ) - (k : ℤ) : ℤ) : ℝ) * α - A = f - g) (hf : f < 1) (hg : 0 ≤ g) :
    (((h : ℤ) - (k : ℤ) : ℤ) : ℝ) * α - (A + 1) < 0 := by
  push_cast at heq ⊢
  linarith
