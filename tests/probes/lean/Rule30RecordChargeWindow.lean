module
public import Ruliology.CellularAutomata.Rule30RecordCharge

/-!
GC2227: UNCOMPILED source draft for the arithmetic part of GC2220.
Uses the kit's exact Path, threshold and Q; no replacement definitions.
Kit source pin: 932cf8dde039b89b1dcbe9636867bb1b2057fef0.
The hand deduction is still awaiting an independent carrying read.
This file does not formalize a metric, an Assouad dimension, or a density limit.
-/
@[expose] public section
namespace Ruliology.CellularAutomata.Rule30RecordChargeWindow
open Rule30RecordCharge

theorem exponent_le_add {nu : Nat} (p : Path nu) (a d : Nat) :
    p.exponent a ≤ p.exponent (a + d) := by
  induction d with
  | zero => simp
  | succ d ih =>
      have hs := p.exponent_step (a + d)
      rw [show a + (d + 1) = a + d + 1 by omega]
      omega

/-- Restart at any index, retaining the actual resource, even when it is nonzero. -/
def shift {nu : Nat} (p : Path nu) (a : Nat) : Path (nu + p.exponent a) where
  weight i := p.weight (a + i)
  exponent i := p.exponent (a + i) - p.exponent a
  resource i := p.resource (a + i)
  exponent_zero := by simp
  exponent_step i := by
    have hm := exponent_le_add p a i
    have hs := p.exponent_step (a + i)
    rw [show a + (i + 1) = a + i + 1 by omega]
    omega
  weight_le_two i := p.weight_le_two (a + i)
  reset_before i h := p.reset_before (a + i) h
  reset_after i h := by
    have hr := p.reset_after (a + i) h
    have hm := exponent_le_add p a (i + 1)
    have he : (nu + p.exponent a) +
        (p.exponent (a + (i + 1)) - p.exponent a) - 1 =
        nu + p.exponent (a + (i + 1)) - 1 := by omega
    rw [he]
    simpa only [Nat.add_assoc] using hr
  countdown i h := by
    simpa only [Nat.add_assoc] using p.countdown (a + i) h

theorem threshold_parameter_mono {nu mu : Nat} (h : nu ≤ mu) :
    ∀ q, threshold nu q ≤ threshold mu q := by
  intro q
  induction q with
  | zero => exact Nat.le_refl _
  | succ q ih =>
      have hp := Nat.pow_le_pow_right (n := 2) (by decide)
        (show nu + threshold nu q + q ≤ mu + threshold mu q + q by omega)
      simp only [threshold]
      omega

theorem Q_parameter_antitone {nu mu : Nat} (h : nu ≤ mu) (d : Nat) :
    Q mu d ≤ Q nu d := by
  apply (Q_le_iff mu d (Q nu d)).mpr
  exact Nat.lt_of_lt_of_le (Q_spec nu d)
    (threshold_parameter_mono h (Q nu d))

theorem exponent_le_Q_any {nu : Nat} (p : Path nu) (d : Nat) :
    p.exponent d ≤ d + Q nu d :=
  exponent_bound_before_threshold p d (Q nu d) (Q_spec nu d)

/-- The sharper, starting-index-dependent window estimate. -/
theorem exponent_window {nu : Nat} (p : Path nu) (a d : Nat) :
    p.exponent (a + d) - p.exponent a ≤ d + Q (nu + p.exponent a) d :=
  exponent_le_Q_any (shift p a) d

/-- A bound uniform over the starting index. -/
theorem exponent_window_uniform {nu : Nat} (p : Path nu) (a d : Nat) :
    p.exponent (a + d) - p.exponent a ≤ d + Q 0 d := by
  exact Nat.le_trans (exponent_window p a d)
    (Nat.add_le_add_left (Q_parameter_antitone (Nat.zero_le _) d) d)

/-- A larger declared horizon can also be used without a separate Q-monotonicity lemma. -/
theorem exponent_window_up_to {nu : Nat} (p : Path nu) (a d M : Nat) (hd : d ≤ M) :
    p.exponent (a + d) - p.exponent a ≤ M + Q 0 M := by
  have hsmall : d < threshold (nu + p.exponent a) (Q 0 M) :=
    Nat.lt_of_le_of_lt hd (Nat.lt_of_lt_of_le (Q_spec 0 M)
      (threshold_parameter_mono (Nat.zero_le _) (Q 0 M)))
  have hb := exponent_bound_before_threshold (shift p a) d (Q 0 M) hsmall
  change p.exponent (a + d) - p.exponent a ≤ d + Q 0 M at hb
  omega

end Ruliology.CellularAutomata.Rule30RecordChargeWindow
