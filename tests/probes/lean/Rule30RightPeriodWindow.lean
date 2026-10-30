module
public import Ruliology.CellularAutomata.Rule30RightPeriods
public import Rule30RecordChargeWindow

/-!
GC2227: UNCOMPILED actual-single-seed wrapper for GC2220.
Imports the official pairPath and leastExp without replacing their definitions.
No density limit, sharpness, metric or Assouad formalization is asserted here.
-/
@[expose] public section
namespace Ruliology.CellularAutomata.Rule30RightPeriodWindow
open Rule30RecordCharge Rule30RightPeriods Rule30RecordChargeWindow

theorem leastExp_le_add (a d : Nat) : leastExp a ≤ leastExp (a + d) := by
  induction d with
  | zero => simp
  | succ d ih =>
      have hs := leastExp_succ_cases (a + d)
      rw [show a + (d + 1) = a + d + 1 by omega]
      rcases hs with hs | hs <;> omega

theorem leastExp_mono {a b : Nat} (h : a ≤ b) : leastExp a ≤ leastExp b := by
  have hb := leastExp_le_add a (b - a)
  simpa only [Nat.add_sub_of_le h] using hb

theorem pair_window (a d : Nat) :
    leastExp (2 * (a + d)) - leastExp (2 * a) ≤ d + Q (leastExp (2 * a)) d := by
  simpa only [pairPath, Nat.zero_add] using exponent_window pairPath a d

theorem pair_window_uniform (a d : Nat) :
    leastExp (2 * (a + d)) - leastExp (2 * a) ≤ d + Q 0 d := by
  exact exponent_window_uniform pairPath a d

/-- Includes N=0; for positive N this is the even-endpoint enclosure used in GC2220. -/
theorem arbitrary_window (j N : Nat) :
    leastExp (j + N) - leastExp j ≤ N / 2 + 1 + Q 0 (N / 2 + 1) := by
  let a := j / 2
  let b := (j + N + 1) / 2
  let M := N / 2 + 1
  have hab : a ≤ b := by dsimp [a, b]; omega
  have hd : b - a ≤ M := by dsimp [a, b, M]; omega
  have hlo : 2 * a ≤ j := by dsimp [a]; omega
  have hhi : j + N ≤ 2 * b := by dsimp [b]; omega
  have lower := leastExp_mono hlo
  have upper := leastExp_mono hhi
  have hb := exponent_window_up_to pairPath a (b - a) M hd
  change leastExp (2 * (a + (b - a))) - leastExp (2 * a) ≤ M + Q 0 M at hb
  rw [Nat.add_sub_of_le hab] at hb
  change leastExp (j + N) - leastExp j ≤ M + Q 0 M
  omega

end Ruliology.CellularAutomata.Rule30RightPeriodWindow
