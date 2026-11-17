import TwoPairsThreeMoves

/-! The settled word B cannot occur twice in succession at the top of a
wall that advances three places backward. Only five specified bits enter
the obstruction, so it applies at the edge as well. -/
namespace TwoPairs.Settled
open ThreeMoves (wordB)

private theorem incompatible (a b c : Bool) :
    ¬(xor c (b || a) = false ∧ xor false (c || b) = true ∧ xor true (false || c) = true) := by
  cases a <;> cases b <;> cases c <;> decide

private theorem readB {x : Row} {L : Nat} (w : seg x L 11 = wordB) (i : Nat) (hi : i < 11) :
    x (L+i) = wordB.getD i false := by rw [←w,seg_getD _ _ _ _ hi]

/-- The deeper B is on the predecessor row `z`. If its successor had B
three cells lower, the successor bits at offsets 2,3,4 would be 0,1,1,
while the input bits at offsets 3,4 would be 0,1. No choice of the other
three inputs is consistent with that update. -/
theorem no_BB (z : Row) (L : Nat) (deep : seg z (L+3) 11 = wordB) :
    seg (step z) L 11 ≠ wordB := by
  intro shallow
  have s2 : step z (L+2) = false := readB shallow 2 (by decide)
  have s3 : step z (L+3) = true := readB shallow 3 (by decide)
  have s4 : step z (L+4) = true := readB shallow 4 (by decide)
  have b3 : z (L+3) = false := readB deep 0 (by decide)
  have b4 : z (L+4) = true := readB deep 1 (by decide)
  change xor (z (L+2)) (z (L+1) || z L) = false at s2
  change xor (z (L+3)) (z (L+2) || z (L+1)) = true at s3
  change xor (z (L+4)) (z (L+3) || z (L+2)) = true at s4
  rw [b3] at s3
  rw [b4,b3] at s4
  exact incompatible (z L) (z (L+1)) (z (L+2)) ⟨s2,s3,s4⟩

#print axioms no_BB
end TwoPairs.Settled
