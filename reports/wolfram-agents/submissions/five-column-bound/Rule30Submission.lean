import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30Realization
/-!
# A sharp black-count ceiling on five adjacent Rule 30 columns

For every Rule 30 trajectory, five adjacent physical columns contain at most `3 * T + 2` black
cells in any interval of `T` ticks, counting its first row and not its endpoint.

The proof uses the potential `H(u) = max(0, 2 - pop(right four cells of u))`, with values in
`0..2` (`potential_bounds`). On seven Boolean input cells, `pop(u) - 3 ≤ H(v) - H(u)`, where `u`
is the middle five cells and `v` their update, with both exterior cells free (`local_potential`).
Summing along a trajectory telescopes it (`telescope`, `five_column_bound`), and the window has at
least `2 * T - 2` white cells (`white_column_bound`). `evol_five_column_bound` covers every
initial configuration and starting time, and `cell_five_column_bound` the official singleton
diagram. The constant `2` is needed at `T = 1` (`sharp_constant`), and the fixed alternating
configuration has exactly `3 * T` black cells in a window at every horizon (`sharp_rate`).

Summing local inequalities and telescoping a bounded potential is a standard method. Nothing here
bounds the density of a single column or gives a positive lower density, and Problems 1 to 3 stay
open.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

open Rule30Jen Rule30Realization

def bit (b : Bool) : Int := if b then 1 else 0

def pop5 (a b c d e : Bool) : Int := bit a + bit b + bit c + bit d + bit e

def potential (_a b c d e : Bool) : Int := max 0 (2 - (bit b + bit c + bit d + bit e))

theorem potential_bounds (a b c d e : Bool) :
    0 ≤ potential a b c d e ∧ potential a b c d e ≤ 2 := by
  cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> decide

/-- Both exterior cells are free; windows read from left to right in physical coordinates. -/
theorem local_potential (l a b c d e r : Bool) :
    pop5 a b c d e - 3 ≤
      potential (rule l a b) (rule a b c) (rule b c d) (rule c d e) (rule d e r) -
      potential a b c d e := by
  cases l <;> cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases r <;> decide

def weight (x : Int → Bool) (p : Int) : Int := pop5 (x p) (x (p+1)) (x (p+2)) (x (p+3)) (x (p+4))

def pot (x : Int → Bool) (p : Int) : Int := potential (x p) (x (p+1)) (x (p+2)) (x (p+3)) (x (p+4))

def count (x : Nat → Int → Bool) (p : Int) : Nat → Int
  | 0 => 0
  | t+1 => count x p t + weight (x t) p

def whiteCount (x : Nat → Int → Bool) (p : Int) : Nat → Int
  | 0 => 0
  | t+1 => whiteCount x p t + (5 - weight (x t) p)

theorem pot_bounds (x : Int → Bool) (p : Int) : 0 ≤ pot x p ∧ pot x p ≤ 2 :=
  potential_bounds _ _ _ _ _

theorem step_potential (x : Nat → Int → Bool)
    (hx : ∀ t i, x (t+1) i = rule (x t (i-1)) (x t i) (x t (i+1))) (t : Nat) (p : Int) :
    weight (x t) p - 3 ≤ pot (x (t+1)) p - pot (x t) p := by
  have h0 := hx t p
  have h1 : x (t+1) (p+1) = rule (x t p) (x t (p+1)) (x t (p+2)) := by
    rw [hx t (p+1), show p+1-1=p by omega, show p+1+1=p+2 by omega]
  have h2 : x (t+1) (p+2) = rule (x t (p+1)) (x t (p+2)) (x t (p+3)) := by
    rw [hx t (p+2), show p+2-1=p+1 by omega, show p+2+1=p+3 by omega]
  have h3 : x (t+1) (p+3) = rule (x t (p+2)) (x t (p+3)) (x t (p+4)) := by
    rw [hx t (p+3), show p+3-1=p+2 by omega, show p+3+1=p+4 by omega]
  have h4 : x (t+1) (p+4) = rule (x t (p+3)) (x t (p+4)) (x t (p+5)) := by
    rw [hx t (p+4), show p+4-1=p+3 by omega, show p+4+1=p+5 by omega]
  simpa only [weight, pot, h0, h1, h2, h3, h4] using
    local_potential (x t (p-1)) (x t p) (x t (p+1)) (x t (p+2)) (x t (p+3)) (x t (p+4)) (x t (p+5))

/-- The count includes time `0` and excludes time `T`; the exact endpoint potential is kept. -/
theorem telescope (x : Nat → Int → Bool)
    (hx : ∀ t i, x (t+1) i = rule (x t (i-1)) (x t i) (x t (i+1))) (p : Int) (T : Nat) :
    count x p T ≤ 3 * (T : Int) + pot (x T) p - pot (x 0) p := by
  induction T with
  | zero => simp [count]
  | succ t ih =>
    have h := step_potential x hx t p
    simp only [count]
    omega

theorem five_column_bound (x : Nat → Int → Bool)
    (hx : ∀ t i, x (t+1) i = rule (x t (i-1)) (x t i) (x t (i+1))) (p : Int) (T : Nat) :
    count x p T ≤ 3 * (T : Int) + 2 := by
  have h := telescope x hx p T
  have h0 := pot_bounds (x 0) p
  have hT := pot_bounds (x T) p
  omega

theorem count_partition (x : Nat → Int → Bool) (p : Int) (T : Nat) :
    whiteCount x p T + count x p T = 5 * (T : Int) := by
  induction T with
  | zero => rfl
  | succ t ih => simp only [whiteCount, count]; omega

theorem white_column_bound (x : Nat → Int → Bool)
    (hx : ∀ t i, x (t+1) i = rule (x t (i-1)) (x t i) (x t (i+1))) (p : Int) (T : Nat) :
    2 * (T : Int) - 2 ≤ whiteCount x p T := by
  have h := five_column_bound x hx p T
  have hp := count_partition x p T
  omega

/-- Every initial row, every physical window and every starting time. -/
theorem evol_five_column_bound (y : Int → Bool) (A : Nat) (p : Int) (T : Nat) :
    count (fun t => evol y (A+t)) p T ≤ 3 * (T : Int) + 2 := by
  apply five_column_bound
  intro t i
  rw [show A+(t+1)=(A+t)+1 by omega]
  rfl

/-- The official singleton diagram, without a stronger seed-specific conclusion. -/
theorem cell_five_column_bound (A : Nat) (p : Int) (T : Nat) :
    count (fun t => cell (A+t)) p T ≤ 3 * (T : Int) + 2 := by
  apply five_column_bound
  intro t i
  rw [show A+(t+1)=(A+t)+1 by omega]
  rfl

def alternating (p : Int) : Bool := decide (p % 2 = 0)

theorem rule_alternating (p : Int) :
    rule (alternating (p-1)) (alternating p) (alternating (p+1)) = alternating p := by
  by_cases h : p % 2 = 0
  · have hm : (p-1) % 2 = 1 := by omega
    have hp : (p+1) % 2 = 1 := by omega
    simp [alternating, h, hm, hp, rule]
  · have hm : (p-1) % 2 = 0 := by omega
    have hp : (p+1) % 2 = 0 := by omega
    simp [alternating, h, hm, hp, rule]

theorem evol_alternating : ∀ t p, evol alternating t p = alternating p
  | 0, p => rfl
  | t+1, p => by rw [evol, evol_alternating t (p-1), evol_alternating t p, evol_alternating t (p+1)]; exact rule_alternating p

/-- The rate `3` is attained on an actual fixed row at every horizon. -/
theorem sharp_rate (T : Nat) : count (evol alternating) 0 T = 3 * (T : Int) := by
  have he : evol alternating = fun _ => alternating := funext fun t => funext fun p => evol_alternating t p
  rw [he]
  have hw : weight alternating 0 = 3 := by decide
  induction T with
  | zero => rfl
  | succ t ih => simp only [count, hw]; omega

/-- The additive constant `2` is needed already at horizon `1`, on an actual row. -/
theorem sharp_constant : count (evol (fun _ => true)) 0 1 = 5 := by decide

end Rule30Submission
