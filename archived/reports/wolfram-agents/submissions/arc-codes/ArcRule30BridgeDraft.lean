import Ruliology.CellularAutomata.Rule30FiniteMaskedJen
import ArcBreakSequence

/-!
# The physical Rule30 repeat bound from the kit's window-Jen theorem

UNCOMPILED draft. The clock is already normalized to white at even times, black at odd times, at column0.
The start has a leftmost black cell at-L. No eventual-clock or endpoint-value restart is silently assumed.
-/

namespace ArcRule30Bridge

open Ruliology.CellularAutomata Rule30Realization

/-- The neighbour on the clock's white (even) physical times. -/
def visible (x : Int → Bool) (s : Nat) : Bool := evol x (2*s) 1

/-- The current kit's window reconstruction supplies the uniform constant C=L at every positive lag. -/
theorem repeat_bound (x : Int → Bool) (L : Nat)
    (hleft : x (-(L : Int)) = true) (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1)) (q : Nat) (hq : 0 < q) :
    ArcBreakSequence.RepeatBound (visible x) q L := by
  intro a b hab hmatch
  by_cases hbound : b ≤ 2*a+q+L
  · exact hbound
  · have hbad : 2*a+q+L < b := by omega
    let m := L+2*(a+q)
    have hc : ∀ s : Nat, s ≤ m → evol x (2*a+s) 0 = evol x (2*(a+q)+s) 0 := by
      intro s _
      have hp : (2*a+s) % 2 = (2*(a+q)+s) % 2 := by omega
      rw [hclock,hclock,hp]
    have he : ∀ s : Nat, s < m →
        Rule30FiniteMaskedJen.orCol x 0 (2*a+s) = Rule30FiniteMaskedJen.orCol x 0 (2*(a+q)+s) := by
      intro s hs
      by_cases hseven : s % 2 = 0
      · let k := s/2
        have hsk : 2*k = s := by dsimp [k]; omega
        have haTime : 2*a+s = 2*(a+k) := by omega
        have hbTime : 2*(a+q)+s = 2*((a+k)+q) := by omega
        have hkbound : a+k ≤ b := by
          have hs' : s < L+2*(a+q) := hs
          omega
        have hv := hmatch (a+k) (by omega) hkbound
        have heva : evol x (2*a+s) 0 = false := by
          rw [hclock]
          have hp : (2*a+s) % 2 = 0 := by omega
          simp [hp]
        have hevb : evol x (2*(a+q)+s) 0 = false := by
          rw [hclock]
          have hp : (2*(a+q)+s) % 2 = 0 := by omega
          simp [hp]
        unfold Rule30FiniteMaskedJen.orCol
        rw [heva,hevb]
        change evol x (2*a+s) 1 = evol x (2*(a+q)+s) 1
        rw [haTime,hbTime]
        exact hv.symm
      · have hsodd : s % 2 = 1 := by omega
        have heva : evol x (2*a+s) 0 = true := by
          rw [hclock]
          have hp : (2*a+s) % 2 = 1 := by omega
          simp [hp]
        have hevb : evol x (2*(a+q)+s) 0 = true := by
          rw [hclock]
          have hp : (2*(a+q)+s) % 2 = 1 := by omega
          simp [hp]
        simp only [Rule30FiniteMaskedJen.orCol,heva,hevb,Bool.true_or]
    exact False.elim (Rule30FiniteMaskedJen.window_jen_col hleft hzero
      (t₁ := 2*a) (t₂ := 2*(a+q)) (i := 0) m (by omega) (by dsimp [m]; omega) hc he)

#print axioms ArcRule30Bridge.repeat_bound

end ArcRule30Bridge
