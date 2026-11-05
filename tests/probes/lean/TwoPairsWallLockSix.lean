import TwoPairsWindowClosed

/-!
# A third lock, with no fixed floor

Forty windows of 175 cells form a closed set under the backward tick for every pair of lower cells, and on them the letters run
`B`, `A`, `A` for ever (`lock_cycle`, `lock_letters`, `lock_forever`). The cells have period six, not three. Unlike the locks of 45 and
136 cells, this one has no reset word at a fixed depth in all its windows: the four lower states merge at sites that move from
window to window. Its top cells lie in the wide clouds too, so a coarse window cannot tell this lock from the rest.
-/

namespace TwoPairs.WallLockSix
open ThreeMoves (wordA wordB)
open WindowClosed

/-- A word of `W` cells from a number, low to high. -/
def dec (W n : Nat) : List Bool := (List.range W).map n.testBit

/-- Phase 0, letter `B`. -/
def P0 : List (List Bool) := [dec 175 37284303768780549450216512176333106322617512176932327, dec 175 37284303768780549450216512176333106322617512176932363, dec 175 37284303768780549450216512176333106322617512176932362, dec 175 37284303768780549450216512176333106322617512176932305, dec 175 37284303768780549450216512176333106322617512176932360]
/-- Phase 1, letter `A`. -/
def P1 : List (List Bool) := [dec 175 37338680436793518946018258025312893609782730154505572, dec 175 37338680436793518946018258025312893609782730154505555, dec 175 37338680436793518946018258025312893609782730154505790, dec 175 37338680436793518946018258025312893609782730154505573, dec 175 37338680436793518946018258025312893609782730154505574, dec 175 37338680436793518946018258025312893609782730154505791]
/-- Phase 2, letter `A`. -/
def P2 : List (List Bool) := [dec 175 37333299180212662931848950068353642697240989240174933, dec 175 37333299180212662931848950068353642697240989240174934, dec 175 37333299180212662931848950068353642697240989240177210, dec 175 37333299180212662931848950068353642697240989240174913, dec 175 37333299180212662931848950068353642697240989240174947, dec 175 37333299180212662931848950068353642697240989240174932, dec 175 37333299180212662931848950068353642697240989240177212]
/-- Phase 3, letter `B`. -/
def P3 : List (List Bool) := [dec 175 37284303528463190167104685405439550272830198693161685, dec 175 37284303528463190167104685405439550272830198693161686, dec 175 37284303528463190167104685405439550272830198693161687, dec 175 37284303528463190167104685405439550272830198693161688, dec 175 37284303528463190167104685405439550272830198693163452, dec 175 37284303528463190167104685405439550272830198693161699, dec 175 37284303528463190167104685405439550272830198693161684, dec 175 37284303528463190167104685405439550272830198693163450]
/-- Phase 4, letter `A`. -/
def P4 : List (List Bool) := [dec 175 37338680284242987720315585462861809216178240387134149, dec 175 37338680284242987720315585462861809216178240387134150, dec 175 37338680284242987720315585462861809216178240387134120, dec 175 37338680284242987720315585462861809216178240387133964, dec 175 37338680284242987720315585462861809216178240387133962, dec 175 37338680284242987720315585462861809216178240387134131, dec 175 37338680284242987720315585462861809216178240387134148]
/-- Phase 5, letter `A`. -/
def P5 : List (List Bool) := [dec 175 37333299375615735401535943766818242528686808079618503, dec 175 37333299375615735401535943766818242528686808079618472, dec 175 37333299375615735401535943766818242528686808079618475, dec 175 37333299375615735401535943766818242528686808079618474, dec 175 37333299375615735401535943766818242528686808079618494, dec 175 37333299375615735401535943766818242528686808079618481, dec 175 37333299375615735401535943766818242528686808079618496]

/-- All forty windows. -/
def L175 : List (List Bool) := P0 ++ P1 ++ P2 ++ P3 ++ P4 ++ P5

theorem chk_mem : ∀ w, w ∈ L175 → ∀ p1 p2 : Bool, next 175 w p1 p2 ∈ L175 := by decide +kernel
theorem chk_a : ∀ w, w ∈ L175 → ∀ p1 p2 : Bool, (back p1 p2 (WindowClosed.inp 175 w)).getD 178 false = !(back p1 p2 (WindowClosed.inp 175 w)).getD 177 false := by decide +kernel
theorem chk_d : ∀ w, w ∈ L175 → ∀ p1 p2 : Bool, (back p1 p2 (WindowClosed.inp 175 w)).getD 179 false = !(back p1 p2 (WindowClosed.inp 175 w)).getD 178 false := by decide +kernel
theorem chk_b : ∀ w, w ∈ L175 → ∀ p1 p2 : Bool, (back p1 p2 (WindowClosed.inp 175 w)).getD 179 false = !(WindowClosed.inp 175 w).getD 179 false := by decide +kernel
theorem chk_c : ∀ w, w ∈ L175 → ∀ p1 p2 : Bool, (back p1 p2 (WindowClosed.inp 175 w)).getD 180 false = !(WindowClosed.inp 175 w).getD 180 false := by decide +kernel

/-- **The lock.** -/
theorem closed : Closed 175 L175 := ⟨by decide, chk_mem, chk_a, chk_d, chk_b, chk_c⟩

theorem chk_0 : ∀ w, w ∈ P0 → ∀ p1 p2 : Bool, next 175 w p1 p2 ∈ P1 := by decide +kernel
theorem chk_1 : ∀ w, w ∈ P1 → ∀ p1 p2 : Bool, next 175 w p1 p2 ∈ P2 := by decide +kernel
theorem chk_2 : ∀ w, w ∈ P2 → ∀ p1 p2 : Bool, next 175 w p1 p2 ∈ P3 := by decide +kernel
theorem chk_3 : ∀ w, w ∈ P3 → ∀ p1 p2 : Bool, next 175 w p1 p2 ∈ P4 := by decide +kernel
theorem chk_4 : ∀ w, w ∈ P4 → ∀ p1 p2 : Bool, next 175 w p1 p2 ∈ P5 := by decide +kernel
theorem chk_5 : ∀ w, w ∈ P5 → ∀ p1 p2 : Bool, next 175 w p1 p2 ∈ P0 := by decide +kernel
theorem let_0 : ∀ w, w ∈ P0 → w.drop 164 = wordB := by decide +kernel
theorem let_1 : ∀ w, w ∈ P1 → w.drop 164 = wordA := by decide +kernel
theorem let_2 : ∀ w, w ∈ P2 → w.drop 164 = wordA := by decide +kernel
theorem let_3 : ∀ w, w ∈ P3 → w.drop 164 = wordB := by decide +kernel
theorem let_4 : ∀ w, w ∈ P4 → w.drop 164 = wordA := by decide +kernel
theorem let_5 : ∀ w, w ∈ P5 → w.drop 164 = wordA := by decide +kernel

theorem seg_top (x : Row) (L : Nat) : (seg x L 175).drop 164 = seg x (L + 164) 11 := by
  have e : seg x L 175 = seg x L 164 ++ seg x (L + 164) 11 := seg_append x 164 11 L
  rw [e, List.drop_left' (seg_length x 164 L)]

/-- **The cycle.** Each phase goes to the next, whatever lies below. -/
theorem lock_cycle {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (hf : Held 175 L175 x L) :
    (seg x L 175 ∈ P0 → seg z (L + 3) 175 ∈ P1) ∧ (seg x L 175 ∈ P1 → seg z (L + 3) 175 ∈ P2) ∧
    (seg x L 175 ∈ P2 → seg z (L + 3) 175 ∈ P3) ∧ (seg x L 175 ∈ P3 → seg z (L + 3) 175 ∈ P4) ∧
    (seg x L 175 ∈ P4 → seg z (L + 3) 175 ∈ P5) ∧ (seg x L 175 ∈ P5 → seg z (L + 3) 175 ∈ P0) := by
  rw [next_seg closed hL hs hf]
  exact ⟨fun h => chk_0 _ h _ _, fun h => chk_1 _ h _ _, fun h => chk_2 _ h _ _, fun h => chk_3 _ h _ _,
    fun h => chk_4 _ h _ _, fun h => chk_5 _ h _ _⟩

/-- **The letters.** -/
theorem lock_letters (x : Row) (L : Nat) :
    (seg x L 175 ∈ P0 → seg x (L + 164) 11 = wordB) ∧
    (seg x L 175 ∈ P1 → seg x (L + 164) 11 = wordA) ∧
    (seg x L 175 ∈ P2 → seg x (L + 164) 11 = wordA) ∧
    (seg x L 175 ∈ P3 → seg x (L + 164) 11 = wordB) ∧
    (seg x L 175 ∈ P4 → seg x (L + 164) 11 = wordA) ∧
    (seg x L 175 ∈ P5 → seg x (L + 164) 11 = wordA) := by
  rw [← seg_top]
  exact ⟨let_0 _, let_1 _, let_2 _, let_3 _, let_4 _, let_5 _⟩

/-- **For ever.** -/
theorem lock_forever {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 175 L175 x L) :
    ∀ n z, iter z n = x → Held 175 L175 z (L + 3 * n) := held_forever closed hL h

/-! ## An anchored row -/

/-- A window of phase 0 on the black edge, with one white cell below it, and rain above. -/
def row (j : Nat) : Bool :=
  if j = 0 then true else if j = 1 then false
  else if j < 177 then (37284303768780549450216512176333106322617512176932327 : Nat).testBit (j - 2)
  else if (j - 177) % 2 = 0 then !(37284303768780549450216512176333106322617512176932327 : Nat).testBit 174 else (37284303768780549450216512176333106322617512176932327 : Nat).testBit 174

theorem row_tail (j : Nat) (hj : 177 ≤ j) : row (j + 1) = !row j := by
  by_cases a : (j - 177) % 2 = 0
  · simp [row, show ¬j = 0 by omega, show ¬j = 1 by omega, show ¬j < 177 by omega, show ¬j + 1 < 177 by omega, a] <;> omega
  · simp [row, show ¬j = 0 by omega, show ¬j = 1 by omega, show ¬j < 177 by omega, show ¬j + 1 < 177 by omega, a] <;> omega

/-- An anchored row in the lock. -/
theorem witness : row 0 = true ∧ Held 175 L175 row 2 := by
  refine ⟨rfl, by decide +kernel, fun j hj => ?_⟩
  by_cases c : 177 ≤ j
  · exact row_tail j c
  · have : j = 176 := by omega
    subst this; decide +kernel

#print axioms closed
#print axioms lock_cycle
#print axioms lock_letters
#print axioms lock_forever
#print axioms witness
end TwoPairs.WallLockSix
