import TwoPairsWindowClosed
/-!
# The wall with period three is locked too

Most rows sit in the letters `AAB` for long stretches and leave them. This module gives rows that never leave: six windows of 136
cells form a closed set under the backward tick, for every pair of lower cells, and on them the letters run `A`, `A`, `B` for ever
(`lock_cycle`, `lock_letters`), whatever lies below the window. The set is two windows in each of three phases. The two windows of
a phase differ only in cells 1 and 2, and each window starts with a reset word, so whatever comes up from below stops there.
-/

namespace TwoPairs.WallLockAAB
open ThreeMoves (wordA wordB)
open WindowClosed

/-- A word of `W` cells from a number, low to high. -/
def dec (W n : Nat) : List Bool := (List.range W).map n.testBit

/-- Phase 0. -/
def P0 : List (List Bool) := [dec 136 67918664933144423441542139865466147588794, dec 136 67918664933144423441542139865466147588796]
/-- Phase 1. -/
def P1 : List (List Bool) := [dec 136 67908875212190969569599336687020282132138, dec 136 67908875212190969569599336687020282132140]
/-- Phase 2. -/
def P2 : List (List Bool) := [dec 136 67819754217029842684664044888796937824810, dec 136 67819754217029842684664044888796937824812]

/-- All six windows. -/
def L136 : List (List Bool) := P0 ++ P1 ++ P2

theorem chk_len : ∀ w, w ∈ L136 → w.length = 136 := by decide +kernel
theorem chk_mem : ∀ w, w ∈ L136 → ∀ p1 p2 : Bool, next 136 w p1 p2 ∈ L136 := by decide +kernel
theorem chk_a : ∀ w, w ∈ L136 → ∀ p1 p2 : Bool, (back p1 p2 (WindowClosed.inp 136 w)).getD 139 false = !(back p1 p2 (WindowClosed.inp 136 w)).getD 138 false := by decide +kernel
theorem chk_d : ∀ w, w ∈ L136 → ∀ p1 p2 : Bool, (back p1 p2 (WindowClosed.inp 136 w)).getD 140 false = !(back p1 p2 (WindowClosed.inp 136 w)).getD 139 false := by decide +kernel
theorem chk_b : ∀ w, w ∈ L136 → ∀ p1 p2 : Bool, (back p1 p2 (WindowClosed.inp 136 w)).getD 140 false = !(WindowClosed.inp 136 w).getD 140 false := by decide +kernel
theorem chk_c : ∀ w, w ∈ L136 → ∀ p1 p2 : Bool, (back p1 p2 (WindowClosed.inp 136 w)).getD 141 false = !(WindowClosed.inp 136 w).getD 141 false := by decide +kernel

/-- **The lock.** -/
theorem closed : Closed 136 L136 := ⟨by decide, chk_mem, chk_a, chk_d, chk_b, chk_c⟩

theorem chk_01 : ∀ w, w ∈ P0 → ∀ p1 p2 : Bool, next 136 w p1 p2 ∈ P1 := by decide +kernel
theorem chk_12 : ∀ w, w ∈ P1 → ∀ p1 p2 : Bool, next 136 w p1 p2 ∈ P2 := by decide +kernel
theorem chk_20 : ∀ w, w ∈ P2 → ∀ p1 p2 : Bool, next 136 w p1 p2 ∈ P0 := by decide +kernel
theorem chk_l0 : ∀ w, w ∈ P0 → w.drop 125 = wordA := by decide +kernel
theorem chk_l1 : ∀ w, w ∈ P1 → w.drop 125 = wordA := by decide +kernel
theorem chk_l2 : ∀ w, w ∈ P2 → w.drop 125 = wordB := by decide +kernel

theorem seg_top (x : Row) (L : Nat) : (seg x L 136).drop 125 = seg x (L + 125) 11 := by
  have e : seg x L 136 = seg x L 125 ++ seg x (L + 125) 11 := seg_append x 125 11 L
  rw [e, List.drop_left' (seg_length x 125 L)]

/-- **The cycle.** Each phase goes to the next, whatever lies below. -/
theorem lock_cycle {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (hf : Held 136 L136 x L) :
    (seg x L 136 ∈ P0 → seg z (L + 3) 136 ∈ P1) ∧ (seg x L 136 ∈ P1 → seg z (L + 3) 136 ∈ P2) ∧
    (seg x L 136 ∈ P2 → seg z (L + 3) 136 ∈ P0) := by
  rw [next_seg closed hL hs hf]
  exact ⟨fun h => chk_01 _ h _ _, fun h => chk_12 _ h _ _, fun h => chk_20 _ h _ _⟩

/-- **The letters.** Phases 0 and 1 read `A` at the wall and phase 2 reads `B`. -/
theorem lock_letters (x : Row) (L : Nat) :
    (seg x L 136 ∈ P0 → seg x (L + 125) 11 = wordA) ∧ (seg x L 136 ∈ P1 → seg x (L + 125) 11 = wordA) ∧
    (seg x L 136 ∈ P2 → seg x (L + 125) 11 = wordB) := by
  rw [← seg_top]
  exact ⟨chk_l0 _, chk_l1 _, chk_l2 _⟩

/-- A held row is in one of the three phases. -/
theorem lock_phase {x : Row} {L : Nat} (h : Held 136 L136 x L) :
    seg x L 136 ∈ P0 ∨ seg x L 136 ∈ P1 ∨ seg x L 136 ∈ P2 := by
  have := h.1
  simp only [L136, List.mem_append] at this
  rcases this with (h | h) | h
  · exact Or.inl h
  · exact Or.inr (Or.inl h)
  · exact Or.inr (Or.inr h)

/-- **For ever.** Every row `n` ticks before a held row is held `3 n` cells higher, so its wall reads the cycle. -/
theorem lock_forever {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 136 L136 x L) :
    ∀ n z, iter z n = x → Held 136 L136 z (L + 3 * n) := held_forever closed hL h

/-! ## An anchored row -/

/-- The first window of phase 0 on the black edge, with one white cell below it, and rain above. -/
def row (j : Nat) : Bool :=
  if j = 0 then true else if j = 1 then false
  else if j < 138 then (67918664933144423441542139865466147588794 : Nat).testBit (j - 2)
  else if (j - 138) % 2 = 0 then !(67918664933144423441542139865466147588794 : Nat).testBit 135 else (67918664933144423441542139865466147588794 : Nat).testBit 135

theorem row_tail (j : Nat) (hj : 138 ≤ j) : row (j + 1) = !row j := by
  by_cases a : (j - 138) % 2 = 0
  · simp [row, show ¬j = 0 by omega, show ¬j = 1 by omega, show ¬j < 138 by omega, show ¬j + 1 < 138 by omega, a] <;> omega
  · simp [row, show ¬j = 0 by omega, show ¬j = 1 by omega, show ¬j < 138 by omega, show ¬j + 1 < 138 by omega, a] <;> omega

/-- An anchored row in the lock. -/
theorem witness : row 0 = true ∧ Held 136 L136 row 2 := by
  refine ⟨rfl, by decide +kernel, fun j hj => ?_⟩
  by_cases c : 138 ≤ j
  · exact row_tail j c
  · have : j = 137 := by omega
    subst this; decide +kernel

#print axioms closed
#print axioms lock_cycle
#print axioms lock_letters
#print axioms lock_phase
#print axioms lock_forever
#print axioms witness
end TwoPairs.WallLockAAB
