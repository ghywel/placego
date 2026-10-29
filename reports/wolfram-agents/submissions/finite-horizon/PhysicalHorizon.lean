import RecodedHorizon
import ArcRule30BridgeDraft
import Ruliology.CellularAutomata.Rule30WhiteEnd
import Ruliology.CellularAutomata.Rule30FiniteConfigs

/-!
# Matching pieces beside a Rule 30 clock (G135/G136, statement 3)

UNCOMPILED draft, Local L1172. Let a configuration `x` have every cell left of `-L` white and its column `0` a clock
(white at even times, black at odd times) from time `0`. Its visible companion is `visible x s = evol x (2s) 1`.

* `piece_bound`: if the companion agrees with ANY recoding of width `w+1` of ANY mechanical word on `[a, b]`, read from
  `a`, then `b - a < 251*(L+2a+4)+250*w`. The proof restarts the evolution at the even time `2a`: the clock keeps its
  phase, the companion shifts by `a`, every cell left of `-(L+2a)` is still white, and the clock itself forces a
  leftmost black cell at some `-L'` with `1 ≤ L' ≤ L+2a`. The delivered arc theorem `ArcRule30Bridge.repeat_bound`
  then bounds the restarted companion's repetitions with constant `L'`, which `RecodedHorizon.recoded_horizon` forbids
  through the horizon.
* `reset_step`, `first_disagreement`, `disagreement_step`: the reset and disagreement recursions (L1151).

No leftmost-black hypothesis on `x` is needed, only the white left tail and the clock. Slopes, phases and the recoding
may change from piece to piece in `reset_step`; the disagreement bounds are against one fixed recoded word. No density,
entropy, realizability or prize claim follows.
-/

namespace PhysicalHorizon

open Ruliology.CellularAutomata Rule30Realization Rule30Jen

/-- Restarting at the even time `2a` shifts the visible companion by `a`. -/
theorem restart_visible (x : Int → Bool) (a s : Nat) :
    ArcRule30Bridge.visible (evol x (2*a)) s = ArcRule30Bridge.visible x (a+s) := by
  unfold ArcRule30Bridge.visible
  rw [Rule30WhiteEnd.evol_add, show 2*a+2*s = 2*(a+s) by omega]

/-- An even restart keeps the clock's phase. -/
theorem restart_clock (x : Int → Bool) (a : Nat)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1)) :
    ∀ t : Nat, evol (evol x (2*a)) t 0 = decide (t % 2 = 1) := by
  intro t
  rw [Rule30WhiteEnd.evol_add, hclock, show (2*a+t) % 2 = t % 2 by omega]

/-- The white left tail moves left by at most one cell per step. -/
theorem restart_left_zero (x : Int → Bool) (L a : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false) :
    ∀ i : Int, i < -((L+2*a : Nat) : Int) → evol x (2*a) i = false := by
  intro i hi
  exact Rule30FiniteConfigs.evol_eq_false_of_lt hzero (2*a) i (by push_cast at hi ⊢; omega)

/-- The clock forces a black cell in `[-(L+2a), -1]` at the restart time: a row white at every cell `≤ 0` would make
column `0` black at the restarted time `2`, against the clock. -/
theorem restart_has_black (x : Int → Bool) (L a : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1)) :
    ∃ k : Nat, k < L+2*a ∧ evol x (2*a) (-((L+2*a : Nat) : Int)+k) = true := by
  apply Classical.byContradiction
  intro hno
  have hno' : ∀ k : Nat, k < L+2*a → evol x (2*a) (-((L+2*a : Nat) : Int)+k) = false := by
    intro k hk
    have h := fun h' => hno ⟨k, hk, h'⟩
    simpa using h
  have hc := restart_clock x a hclock
  have hy : ∀ i : Int, i ≤ 0 → evol x (2*a) i = false := by
    intro i hi
    by_cases hlow : i < -((L+2*a : Nat) : Int)
    · exact restart_left_zero x L a hzero i hlow
    · by_cases hz : i = 0
      · subst hz
        exact hc 0
      · have hk := hno' (Int.toNat (i+((L+2*a : Nat) : Int))) (by omega)
        rw [show -((L+2*a : Nat) : Int)+((Int.toNat (i+((L+2*a : Nat) : Int)) : Nat) : Int) = i by omega] at hk
        exact hk
  have hm1 : evol x (2*a) (-1) = false := hy (-1) (by norm_num)
  have hm2 : evol x (2*a) (-2) = false := hy (-2) (by norm_num)
  have h00 : evol x (2*a) 0 = false := hy 0 le_rfl
  have he1 : evol (evol x (2*a)) 1 (-1) = false := by
    show rule (evol x (2*a) (-1-1)) (evol x (2*a) (-1)) (evol x (2*a) (-1+1)) = false
    rw [show (-1 : Int)-1 = -2 by norm_num, show (-1 : Int)+1 = 0 by norm_num, hm2, hm1, h00]
    rfl
  have he0 : evol (evol x (2*a)) 1 0 = true := hc 1
  have he2 : evol (evol x (2*a)) 2 0 = true := by
    show rule (evol (evol x (2*a)) 1 (0-1)) (evol (evol x (2*a)) 1 0) (evol (evol x (2*a)) 1 (0+1)) = true
    rw [show (0 : Int)-1 = -1 by norm_num, he1, he0]
    simp [rule]
  have hc2 := hc 2
  rw [he2] at hc2
  exact absurd hc2 (by decide)

/-- The restarted row has a leftmost black cell at some `-L'` with `1 ≤ L' ≤ L+2a`. -/
theorem restart_leftmost (x : Int → Bool) (L a : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1)) :
    ∃ L' : Nat, 1 ≤ L' ∧ L' ≤ L+2*a ∧ evol x (2*a) (-(L' : Int)) = true ∧
      ∀ i : Int, i < -(L' : Int) → evol x (2*a) i = false := by
  classical
  have hex := restart_has_black x L a hzero hclock
  have hk := Nat.find_spec hex
  refine ⟨L+2*a-Nat.find hex, by omega, by omega, ?_, ?_⟩
  · rw [show -(((L+2*a-Nat.find hex : Nat) : Int)) = -((L+2*a : Nat) : Int)+((Nat.find hex : Nat) : Int) by
      have := hk.1
      omega]
    exact hk.2
  · intro i hi
    by_cases hlow : i < -((L+2*a : Nat) : Int)
    · exact restart_left_zero x L a hzero i hlow
    · have hlt : Int.toNat (i+((L+2*a : Nat) : Int)) < Nat.find hex := by omega
      have hm := Nat.find_min hex hlt
      rw [show -((L+2*a : Nat) : Int)+((Int.toNat (i+((L+2*a : Nat) : Int)) : Nat) : Int) = i by omega] at hm
      have hbound : Int.toNat (i+((L+2*a : Nat) : Int)) < L+2*a := by
        have := hk.1
        omega
      simpa [hbound] using hm

/-- **Statement 3, one matching piece.** -/
theorem piece_bound (x : Int → Bool) (L : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1))
    (alpha theta : ℝ) (w : Nat) (F : (Fin (w+1) → Int) → Bool) (a b : Nat)
    (hmatch : ∀ i, i ≤ b-a → ArcRule30Bridge.visible x (a+i) =
      RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) i) :
    b-a < 251*(L+2*a+4)+250*w := by
  apply Classical.byContradiction
  intro hbig
  obtain ⟨L', _, hL', hl, hz⟩ := restart_leftmost x L a hzero hclock
  apply RecodedHorizon.recoded_horizon alpha theta (L+2*a) w F
  intro q c d hq hcd hN heq
  have hv : ∀ i, i ≤ 251*(L+2*a+4)+250*w →
      RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) i =
        ArcRule30Bridge.visible (evol x (2*a)) i := by
    intro i hi
    rw [restart_visible, hmatch i (by omega)]
  have hrb := ArcRule30Bridge.repeat_bound (evol x (2*a)) L' hl hz (restart_clock x a hclock) q hq c d hcd
    (fun s hs1 hs2 => by
      rw [← hv (s+q) (by omega), ← hv s (by omega)]
      exact heq s hs1 hs2)
  omega

/-- A mechanical word read from `m` is the mechanical word of the shifted phase. -/
theorem mech_shift (alpha theta : ℝ) (m s : Nat) :
    MechanicalCarry.mech alpha theta (m+s) = MechanicalCarry.mech alpha (theta+(m : ℝ)*alpha) s := by
  unfold MechanicalCarry.mech MechanicalCarry.level
  congr 1 <;> (congr 1; push_cast; ring)

/-- **The reset recursion.** A piece `[t, t'-1]` matching a recoded mechanical word gives the next reset bound. -/
theorem reset_step (x : Int → Bool) (L : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1))
    (alpha theta : ℝ) (w : Nat) (F : (Fin (w+1) → Int) → Bool) (t t' : Nat)
    (hmatch : ∀ i, i ≤ t'-1-t → ArcRule30Bridge.visible x (t+i) =
      RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) i) :
    t' ≤ 503*t+251*L+1004+250*w := by
  have h := piece_bound x L hzero hclock alpha theta w F t (t'-1) hmatch
  omega

/-- **The first disagreement** against one fixed recoded mechanical word. -/
theorem first_disagreement (x : Int → Bool) (L : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1))
    (alpha theta : ℝ) (w : Nat) (F : (Fin (w+1) → Int) → Bool) (k : Nat)
    (hagree : ∀ s, s < k → ArcRule30Bridge.visible x s =
      RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) s) :
    k ≤ 251*(L+4)+250*w := by
  by_cases hk : k = 0
  · omega
  · have h := piece_bound x L hzero hclock alpha theta w F 0 (k-1)
      (fun i hi => by rw [Nat.zero_add]; exact hagree i (by omega))
    omega

/-- **The disagreement recursion** against one fixed recoded mechanical word. -/
theorem disagreement_step (x : Int → Bool) (L : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1))
    (alpha theta : ℝ) (w : Nat) (F : (Fin (w+1) → Int) → Bool) (k k' : Nat)
    (hagree : ∀ s, k < s → s < k' → ArcRule30Bridge.visible x s =
      RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) s) :
    k' ≤ 503*k+251*L+1507+250*w := by
  by_cases hkk : k' ≤ k+1
  · omega
  · have h := piece_bound x L hzero hclock alpha (theta+((k+1 : Nat) : ℝ)*alpha) w F (k+1) (k'-1)
      (fun i hi => by
        rw [hagree (k+1+i) (by omega) (by omega)]
        unfold RecodedHorizon.recode
        congr 1
        funext j
        rw [show k+1+i+(j : Nat) = (k+1)+(i+(j : Nat)) by omega, mech_shift])
    omega

#print axioms PhysicalHorizon.restart_visible
#print axioms PhysicalHorizon.restart_clock
#print axioms PhysicalHorizon.restart_left_zero
#print axioms PhysicalHorizon.restart_has_black
#print axioms PhysicalHorizon.restart_leftmost
#print axioms PhysicalHorizon.piece_bound
#print axioms PhysicalHorizon.mech_shift
#print axioms PhysicalHorizon.reset_step
#print axioms PhysicalHorizon.first_disagreement
#print axioms PhysicalHorizon.disagreement_step

end PhysicalHorizon
