import TwoPairsThreeMoves

/-!
# The reset word

Ten cells, low to high, `0, b, !b, 1, u, 1, 0, v, 0, 1`. On a backward tick this word stops everything that comes up from below. Whatever
the two cells under it, the new row has a word of the same shape three cells higher, and the two new cells at the top of the word
are always `1` then `0` (`reset`). So the new row above the word depends only on the old row above the word. The two wall letters are
such words. Only one bit of the new word, `b'`, feels the lower cells, and only through whether both are white (`reset_bit`).
-/

namespace TwoPairs.Reset

/-- The reset word. -/
def F (b u v : Bool) : List Bool := [false, b, !b, true, u, true, false, v, false, true]

/-- The first seven cells of the word. -/
def W (b u : Bool) : List Bool := [false, b, !b, true, u, true, false]

/-- The bit of the new word. -/
def newbit (b u p1 p2 : Bool) : Bool := if b || (!p1 && !p2) then !u else u

/-- **The reset.** Under any two lower cells the output on cells 3 to 9 of the word is the shape `W` with the new bit. -/
theorem reset : ∀ b u v p1 p2 : Bool, ((back p1 p2 (F b u v)).drop 3).take 7 = W (newbit b u p1 p2) (!v) := by decide

/-- **Nothing passes.** Above the word the output is the same function of the input, whatever the bits of the word and the cells below it. -/
theorem above (b u v p1 p2 : Bool) (r : List Bool) : (back p1 p2 (F b u v ++ r)).drop 10 = back false true r := by
  cases b <;> cases u <;> cases v <;> cases p1 <;> cases p2 <;> rfl

/-- **Again.** If the old row reads `s, !s, s` above the word, the new word is a reset word again, three cells higher. -/
theorem again : ∀ b u v s p1 p2 : Bool,
    ((back p1 p2 (F b u v ++ [s, !s, s])).drop 3).take 10 = F (newbit b u p1 p2) (!v) (!s) := by decide

/-- The wall letters are reset words, with `u` black and `v` white, under one black cell. -/
theorem letters : ThreeMoves.wordA = F false true false ++ [true] ∧ ThreeMoves.wordB = F true true false ++ [true] := by decide

#print axioms reset
#print axioms above
#print axioms again
#print axioms letters
end TwoPairs.Reset
