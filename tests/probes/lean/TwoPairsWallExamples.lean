import TwoPairsWindowClassification

/-! Two consecutive maximal backward moves can be followed by a retreat.
The same wall and eleven visible cells also admit a permanently advancing row. -/
namespace TwoPairs.WallExamples
open Entrances WindowExclusions

def row (low : Nat) : Row := source 1595 low 6

private theorem tail (low j : Nat) (hj : 16 ≤ j) :
    row low (j+1) = !row low j := by
  by_cases a : (j-16) % 2 = 0
  · simp [row, source, show ¬j < 6 by omega, show ¬j+1 < 6 by omega,
      show ¬j < 16 by omega, show ¬j+1 < 16 by omega, a] <;> omega
  · simp [row, source, show ¬j < 6 by omega, show ¬j+1 < 6 by omega,
      show ¬j < 16 by omega, show ¬j+1 < 16 by omega, a] <;> omega

private theorem top (low : Nat) : Top (row low) 15 :=
  ⟨by rfl, tail low⟩

private theorem back_tail (low : Nat) : ∀ j, 19 ≤ j →
    previous (row low) (j+1) = !previous (row low) j :=
  back_rain_tail (D := 16) (by decide) (step_previous _) (tail low)

/-- In backward chronological order the four wall depths are 9, 12, 15, 13. -/
theorem two_then_retreat :
    Top (step (step (row 39))) 9 ∧ Top (step (row 39)) 12 ∧
      Top (row 39) 15 ∧ Top (previous (row 39)) 13 := by
  have one := (top_minus_three (k := 10) (top 39) (by decide) (by decide) (by decide)
    (by decide) (by decide)).1
  have two := (top_minus_three (k := 7) one (by decide) (by decide) (by decide)
    (by decide) (by decide)).1
  refine ⟨two, one, top 39, by decide, ?_⟩
  intro j hj
  by_cases high : 19 ≤ j
  · exact back_tail _ _ high
  · have finite : ∀ j : Fin 19, 14 ≤ j.val →
       previous (row 39) (j.val+1) = !previous (row 39) j.val := by decide +kernel
    exact finite ⟨j, by omega⟩ hj

theorem same_window_different_future :
    row 39 0 = true ∧ row 41 0 = true ∧ seg (row 39) 6 11 = seg (row 41) 6 11 ∧
      Top (row 41) 15 ∧ Front (previous (row 41)) 9 := by
  exact ⟨rfl, rfl, by decide, top 41, by decide +kernel, back_tail 41⟩

#print axioms two_then_retreat
#print axioms same_window_different_future
end TwoPairs.WallExamples
