import RightRayLanguage
import Ruliology.CellularAutomata.Rule30ControlledResponse

/-! The half-speed follower and the kit's externally driven column have the
same equivalence relation on their initial states. The controls and the
observations in the two experiments differ. This bridge uses the kit's
`sameResponse_iff_diagonal` on the low part of the cut, in reverse order. -/

namespace RightRayControlledBridge

open RightRayWhiteCone RightRayProbe RightRayLanguage
open Ruliology.CellularAutomata.Rule30ControlledResponse

/-- Read the low part from the cut toward the right exterior. -/
def lower (x : Row) (d : Int) : State := fun k => x (d-1-(k : Int))

theorem lower_iterate (x : Row) (d : Int) : ∀ (t k : Nat),
    iterate (lower x d) t k = orbit x t (d-1-(k : Int)) := by
  intro t
  induction t with
  | zero => intro k; simp only [iterate, orbit, lower]
  | succ t ih =>
    intro k
    simp only [iterate, diagonal, orbit, ih,
      show d-1-((k+1 : Nat) : Int) = d-1-(k : Int)-1 by omega,
      show d-1-((k+2 : Nat) : Int) = d-1-(k : Int)-2 by omega]

private theorem observe_iff (x z : Row) (d e : Int) (t : Nat) :
    ObserveEq (iterate (lower x d) t) (iterate (lower z e) t) ↔
      band x d 1 t = band z e 1 t ∧ band x d 2 t = band z e 2 t := by
  have head (y : Row) (c : Int) : iterate (lower y c) t 0 = orbit y t (c-1) := by
    simpa using lower_iterate y c t 0
  have nextBit (y : Row) (c : Int) : iterate (lower y c) t 1 = orbit y t (c-2) := by
    rw [lower_iterate, show c-1-((1 : Nat) : Int) = c-2 by omega]
  simp [ObserveEq, head, nextBit, band]

/-- A cut has exactly the same finite half-speed futures as a second cut iff
all controlled-column responses of their reversed low rows agree. -/
theorem followers_iff_controlled (x z : Row) (d e : Int)
    (hx : ∀ i : Int, i < 0 → x i = false) (hz : ∀ i : Int, i < 0 → z i = false) :
    Same x d z e ↔ SameResponse (lower x d) (lower z e) := by
  rw [same_iff_movies x z d e hx hz, sameResponse_iff_diagonal]
  constructor
  · intro h t
    exact (observe_iff x z d e t).mpr ⟨h 1 (Or.inl rfl) t, h 2 (Or.inr rfl) t⟩
  · intro h k hk t
    have e' := (observe_iff x z d e t).mp (h t)
    rcases hk with rfl | rfl
    · exact e'.1
    · exact e'.2

#print axioms followers_iff_controlled
end RightRayControlledBridge
