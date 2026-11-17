import TwoPairsWindowClassification
import TwoPairsFrontPadding

/-! # Ten-cell positive windows, including at the edge

The lower extension of a physical ten-cell suffix is a cell of the current
row, except when the suffix starts at zero. Translating by two white cells
realizes that case as well. The padding commutes with the inverse step.
-/

namespace TwoPairs.ShortPositive

open Entrances FrontPadding WindowExclusions

theorem previous_padTwo (x : Row) : previous (padTwo x) = padTwo (previous x) := by
  calc
    previous (padTwo x) = previous (padTwo (step (previous x))) := by rw [step_previous]
    _ = previous (step (padTwo (previous x))) := by rw [step_padTwo]
    _ = padTwo (previous x) := previous_step _

theorem previousN_padTwo (x : Row) (r : Nat) :
    previousN (padTwo x) r = padTwo (previousN x r) := by
  induction r generalizing x with
  | zero => rfl
  | succ r ih =>
    change previousN (previous (padTwo x)) r = padTwo (previousN (previous x) r)
    rw [previous_padTwo, ih]

theorem top_padTwo (x : Row) (D : Nat) : Top (padTwo x) (D + 2) ↔ Top x D := by
  constructor
  · intro h
    exact ⟨h.1, fun j hj => h.2 (j + 2) (by omega)⟩
  · intro h
    refine ⟨h.1, ?_⟩
    intro j hj
    obtain ⟨i, rfl⟩ : ∃ i, j = i + 2 := ⟨j - 2, by omega⟩
    exact h.2 i (by omega)

private theorem padded_segment (x : Row) (n L : Nat) :
    seg (padTwo x) (L + 2) n = seg x L n := by
  induction n generalizing L with
  | zero => rfl
  | succ n ih =>
    change x L :: seg (padTwo x) (L + 1 + 2) n = x L :: seg x (L + 1) n
    rw [ih]

/-- A ten-cell suffix inherits the physical passage of both its eleven-cell
extensions. Every level is permitted, and the row may have either edge colour. -/
theorem both_extensions (w : List Bool)
    (lo : false :: w ∈ B11 ++ Six.fast ++ Six.slow)
    (hi : true :: w ∈ B11 ++ Six.fast ++ Six.slow)
    (x : Row) (L : Nat) (window : seg x L 10 = w) (wall : Top x (L + 8)) (r : Nat) :
    Top (previousN x r) (L + 8 + 3 * r) := by
  have ext : seg (padTwo x) (L + 1) 11 = padTwo x (L + 1) :: w := by
    change padTwo x (L + 1) :: seg (padTwo x) (L + 2) 10 = padTwo x (L + 1) :: w
    rw [padded_segment, window]
  have mem : seg (padTwo x) (L + 1) 11 ∈ B11 ++ Six.fast ++ Six.slow := by
    rw [ext]
    cases padTwo x (L + 1)
    · exact lo
    · exact hi
  have h := WindowClassification.listed_forever (padTwo x) (L + 1) mem
    ((top_padTwo x (L + 8)).2 wall) r
  rw [previousN_padTwo, show L + 1 + 9 + 3 * r = (L + 8 + 3 * r) + 2 by omega] at h
  exact (top_padTwo _ _).1 h

#print axioms both_extensions
end TwoPairs.ShortPositive
