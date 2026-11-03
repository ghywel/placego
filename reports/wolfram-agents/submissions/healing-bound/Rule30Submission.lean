import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30Jen

/-!
# Rule 30: the universal healing bound

For any rule-30 evolution `E` of the whole line (a background orbit, periodic or not) and any rule-30 evolution `G` that
agrees with `E` at time 0 on the columns `x ≤ -1`, define the **recruitment frontier** `K t` on diagonals `x + t`:
`K 0 = -1`, and `K (t + 1) = K t + 1` if the background cell `E t (K t - t)` is black, else `K t`.

* `healing_bound`: `G` agrees with `E` at every cell on a diagonal `x + t ≤ K t`. A black centre masks its right
  neighbour, so a diagonal whose newest known cell is black is recruited at the next tick.
* `front_ge`: the leftmost disagreement at time `t` lies at `x ≥ K t - t + 1`, so damage moves left at most at speed one
  minus the frontier's long-run climb rate. For a periodic background that rate is a finite walk on its torus.
* `K_succ_bounds`: the frontier never falls and climbs at most one diagonal per tick.

Scope: any background orbit and any perturbation confined to `x ≥ 0` at time 0. Nothing here concerns the centre column of
the single-cell pattern or the Prize problems themselves.
-/

namespace Rule30Submission
open Ruliology.CellularAutomata
open Rule30Jen

/-- A rule-30 evolution of the whole line. -/
def IsR30Z (G : Nat → Int → Bool) : Prop :=
  ∀ t x, G (t + 1) x = rule (G t (x - 1)) (G t x) (G t (x + 1))

/-- The recruitment frontier of the background `E`, a diagonal index (`x + t`). -/
def K (E : Nat → Int → Bool) : Nat → Int
  | 0 => -1
  | t + 1 => if E t (K E t - t) then K E t + 1 else K E t

/-- **The universal healing bound.** -/
theorem healing_bound {E G : Nat → Int → Bool} (hE : IsR30Z E) (hG : IsR30Z G) (h0 : ∀ x, x ≤ -1 → G 0 x = E 0 x) :
    ∀ t x, x + t ≤ K E t → G t x = E t x := by
  intro t
  induction t with
  | zero => intro x hx; exact h0 x (by simpa [K] using hx)
  | succ t ih =>
    intro x hx
    rw [hG, hE]
    by_cases hin : x + (t : Int) + 1 ≤ K E t
    · rw [ih (x - 1) (by omega), ih x (by omega), ih (x + 1) (by omega)]
    · -- the recruited diagonal: x = K t - t and the background centre is black
      have hK : K E (t + 1) = (if E t (K E t - t) then K E t + 1 else K E t) := rfl
      cases hc : E t (K E t - t) with
      | false =>
        rw [hK, hc] at hx
        simp at hx
        omega
      | true =>
        rw [hK, hc] at hx
        simp at hx
        have hx' : x = K E t - t := by omega
        have hcen : G t x = E t x := ih x (by omega)
        have hcb : E t x = true := by rw [hx']; exact hc
        rw [ih (x - 1) (by omega), hcen, hcb]
        simp [rule]

/-- Hence the leftmost cell where `G` differs from `E` at time `t` lies at `x ≥ K t - t + 1`. -/
theorem front_ge {E G : Nat → Int → Bool} (hE : IsR30Z E) (hG : IsR30Z G) (h0 : ∀ x, x ≤ -1 → G 0 x = E 0 x)
    (t : Nat) (x : Int) (hne : G t x ≠ E t x) : K E t - t + 1 ≤ x := by
  by_cases h : x + (t : Int) ≤ K E t
  · exact absurd (healing_bound hE hG h0 t x h) hne
  · omega

/-- The frontier never falls and climbs at most one diagonal per tick. -/
theorem K_succ_bounds (E : Nat → Int → Bool) (t : Nat) : K E t ≤ K E (t + 1) ∧ K E (t + 1) ≤ K E t + 1 := by
  show K E t ≤ (if E t (K E t - t) then K E t + 1 else K E t) ∧ (if E t (K E t - t) then K E t + 1 else K E t) ≤ K E t + 1
  cases E t (K E t - t) <;> simp <;> omega

end Rule30Submission
