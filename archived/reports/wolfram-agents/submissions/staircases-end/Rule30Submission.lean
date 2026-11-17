import Rule30PrizeKit

/-!
# Every staircase near the single cell's right edge ends, by a period of the right diagonals

In the picture of rule 30 grown from one black cell (`cell t p`), a *staircase* is a maximal
alternating stretch of a row, `… x x̄ x x̄ …`, of length at least `3`. Its interior cells keep their
colors from row to row (`interior_kept`): beside an alternating pair the black OR always fires, so
the cell becomes the complement of its left neighbour, which is its own color. Its left end, the
*front*, is eaten one cell per row: if `f` is the front at time `t` (the cell left of it has the
same color, and `f, f+1, f+2` alternate), then at time `t + 1` the cells `f` and `f + 1` have the
same color (`front_step`), so the stretch continues from `f + 1` or not at all. The right edge of
the picture advances one cell per row as well, so a living staircase keeps its front at a fixed
distance `W` from the edge.

**The headline (`staircase_ends`).** Say the staircase *lives through* time `t` from time `t₀`
with front `a` (`Lives`) if at every time `t'` between `t₀` and `t`, the three cells from
`a + (t' - t₀)` alternate. If its front is at distance `W = t₀ - a ≥ 2` from the edge, and the
right diagonal `W + 1` has period `H` (`Rule30RightPeriods.Per (W + 1) H`, as in the kit), then the
staircase does not live through any time `H n ≥ t₀`. At such a time the diagonals `0 .. W + 1`
are back at their time-0 values, so the cells at distances `1 .. W + 1` from the edge are white,
and the front pair is white-white.

With the kit's `R_periodic`, `H = 2 ^ (W + 1)` always works (`staircase_ends_pow`): every staircase
whose front is `W ≥ 2` cells from the edge dies within `2 ^ (W + 1)` rows. The least common period
of the diagonals `0 .. W + 1` gives the sharpest bound. Nothing here concerns staircases deep in
the picture's chaotic core, rows of other seeds, or the center column.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30Jen (cell rule)
open Ruliology.CellularAutomata.Rule30Diagonals (R R_periodic)
open Ruliology.CellularAutomata.Rule30RightPeriods (Per per_mono_all R_init)

/-- Three cells from `f` at time `t` alternate. -/
def Alt3 (t : Nat) (f : Int) : Prop := cell t f ≠ cell t (f + 1) ∧ cell t (f + 1) ≠ cell t (f + 2)

/-- `f` is the front (left end) of a maximal alternating stretch of length at least `3`. -/
def Front (t : Nat) (f : Int) : Prop := cell t (f - 1) = cell t f ∧ Alt3 t f

theorem cell_succ (t : Nat) (p : Int) :
    cell (t + 1) p = rule (cell t (p - 1)) (cell t p) (cell t (p + 1)) := rfl

/-- Interior cells of an alternating stretch keep their colors. -/
theorem interior_kept (t : Nat) (p : Int) (h1 : cell t (p - 1) ≠ cell t p)
    (h2 : cell t p ≠ cell t (p + 1)) : cell (t + 1) p = cell t p := by
  rw [cell_succ]
  revert h1 h2
  cases cell t (p - 1) <;> cases cell t p <;> cases cell t (p + 1) <;> decide

/-- The front is eaten one cell per row: after one step, the old front and the next cell agree. -/
theorem front_step (t : Nat) (f : Int) (h : Front t f) :
    cell (t + 1) f = cell (t + 1) (f + 1) := by
  obtain ⟨hl, ha, hb⟩ := h
  rw [cell_succ t f, cell_succ t (f + 1)]
  have e1 : f + 1 - 1 = f := by ring
  rw [e1, hl, show f + 1 + 1 = f + 2 by ring]
  revert ha hb
  cases cell t f <;> cases cell t (f + 1) <;> cases cell t (f + 2) <;> decide

/-- The stretch lives through `t`, from `t₀` with front `a`, its front moving one cell per row. -/
def Lives (t₀ : Nat) (a : Int) (t : Nat) : Prop :=
  ∀ t', t₀ ≤ t' → t' ≤ t → Alt3 t' (a + ((t' - t₀ : Nat) : Int))

/-- A living stretch's front stays at its distance from the edge: at time `t ≥ t₀` its front is at
`t - W` when `t₀ - a = W`. -/
theorem front_distance (t₀ t : Nat) (a : Int) (W : Nat) (hW : (t₀ : Int) - a = W) (ht : t₀ ≤ t) :
    a + ((t - t₀ : Nat) : Int) = (t : Int) - W := by
  have : ((t - t₀ : Nat) : Int) = (t : Int) - t₀ := by push_cast [Nat.cast_sub ht]; ring
  rw [this]; omega

/-- At a time that is a multiple of a period of diagonal `W + 1`, the cells at distances
`1 .. W + 1` behind the right edge are white. -/
theorem white_behind_edge {W H : Nat} (hP : Per (W + 1) H) (n : Nat) (j : Nat) (hj1 : 1 ≤ j)
    (hj : j ≤ W + 1) : cell (H * n) ((H * n : Nat) - (j : Int)) = false := by
  have hPj : Per j H := by
    rcases Nat.lt_or_eq_of_le hj with h | h
    · exact per_mono_all hP j (by omega)
    · rw [h]; exact hP
  have h1 := hPj.at_mul n
  rw [R_init hj1] at h1
  exact h1

/-- **Every staircase ends.** A staircase living from `t₀` with front `a` at distance
`W = t₀ - a ≥ 2` from the right edge does not live through any multiple `H n ≥ t₀` of a period `H`
of the right diagonal `W + 1`. -/
theorem staircase_ends (t₀ : Nat) (a : Int) (W H : Nat) (hW2 : 2 ≤ W)
    (hW : (t₀ : Int) - a = W) (hP : Per (W + 1) H) (n : Nat) (hn : t₀ ≤ H * n) :
    ¬ Lives t₀ a (H * n) := by
  intro hl
  have h := hl (H * n) hn le_rfl
  rw [front_distance t₀ (H * n) a W hW hn] at h
  have c0 := white_behind_edge hP n W (by omega) (by omega)
  have c1 := white_behind_edge hP n (W - 1) (by omega) (by omega)
  have e : (((H * n : Nat) : Int) - (W : Int)) + 1 = ((H * n : Nat) : Int) - ((W - 1 : Nat) : Int) := by
    push_cast [Nat.cast_sub (show 1 ≤ W by omega)]; ring
  apply h.1
  rw [e, c0, c1]

/-- With the kit's `R_periodic`: every staircase whose front is `W ≥ 2` cells from the right edge
dies by the first multiple of `2 ^ (W + 1)` after it is seen. -/
theorem staircase_ends_pow (t₀ : Nat) (a : Int) (W : Nat) (hW2 : 2 ≤ W)
    (hW : (t₀ : Int) - a = W) (n : Nat) (hn : t₀ ≤ 2 ^ (W + 1) * n) :
    ¬ Lives t₀ a (2 ^ (W + 1) * n) :=
  staircase_ends t₀ a W (2 ^ (W + 1)) hW2 hW (R_periodic (W + 1)) n hn

end Rule30Submission
