import TwoPairsThreeMoves

/-!
# The alternating wall is locked

A settled wall reads `A` and `B`. Most rows sit in `AAB` repeated for long stretches and leave it, but a few sit in `AB`
repeated and never leave. This module says why. Four windows of 45 cells form a closed set under the backward tick, for every
pair of lower cells (`lock_back`), and on them the letters alternate (`lock_alternates`). So a row showing one of these windows
at its top, with rain above, has wall letters `ABAB…` at every backward tick for ever, whatever lies below the window
(`lock_forever`). Such rows exist on anchored rows (`witness`). The cells below the window never reach the letters.
-/

namespace TwoPairs.WallLock
open ThreeMoves (wordA wordB)

/-- The four windows, low to high; the wall is their last two cells. -/
def L45 : List (List Bool) := [
  [false, false, true, true, false, true, false, false, false, true, false, true, false, false, true, false, false, true, false, false, false, false, false, false, false, false, true, true, false, false, false, false, true, true, false, false, true, true, true, true, false, false, false, true, true],
  [false, false, true, true, true, true, false, true, false, true, true, false, true, true, false, true, true, true, true, true, true, true, true, false, false, false, false, false, false, true, false, true, true, false, false, true, false, true, true, true, false, false, false, true, true],
  [false, true, false, true, false, true, false, false, false, true, false, true, false, false, true, false, false, true, false, false, false, false, false, false, false, false, true, true, false, false, false, false, true, true, false, false, true, true, true, true, false, false, false, true, true],
  [false, true, false, true, true, true, false, true, false, true, true, false, true, true, false, true, true, true, true, true, true, true, true, false, false, false, false, false, false, true, false, true, true, false, false, true, false, true, true, true, false, false, false, true, true]]

/-- A row with its window of 45 cells from `L` in `L45` and rain above it. -/
def Lock (x : Row) (L : Nat) : Prop :=
  seg x L 45 ∈ L45 ∧ ∀ j, L + 44 ≤ j → x (j + 1) = !x j

/-- A window with seven cells of rain over its last. -/
def inp (w : List Bool) : List Bool := w.take 44 ++ alt (w.getD 44 false) 7

theorem chk_mem : ∀ w, w ∈ L45 → ∀ p1 p2 : Bool, ((back p1 p2 (inp w)).drop 3).take 45 ∈ L45 := by decide +kernel
theorem chk_a : ∀ w, w ∈ L45 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 48 false = !(back p1 p2 (inp w)).getD 47 false := by decide +kernel
theorem chk_b : ∀ w, w ∈ L45 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 49 false = !(inp w).getD 49 false := by decide +kernel
theorem chk_c : ∀ w, w ∈ L45 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 50 false = !(inp w).getD 50 false := by decide +kernel
theorem chk_d : ∀ w, w ∈ L45 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 49 false = !(back p1 p2 (inp w)).getD 48 false := by decide +kernel
theorem chk_letter : ∀ w, w ∈ L45 → ∀ p1 p2 : Bool,
    (w.drop 34 = wordA ∧ (((back p1 p2 (inp w)).drop 3).take 45).drop 34 = wordB) ∨
    (w.drop 34 = wordB ∧ (((back p1 p2 (inp w)).drop 3).take 45).drop 34 = wordA) := by decide +kernel
theorem chk_top : ∀ w, w ∈ L45 → w.drop 34 = wordA ∨ w.drop 34 = wordB := by decide +kernel

theorem seg_inp {x : Row} {L : Nat} (h : ∀ j, L + 44 ≤ j → x (j + 1) = !x j) : seg x L 51 = inp (seg x L 45) := by
  have e1 : seg x L 45 = seg x L 44 ++ seg x (L + 44) 1 := seg_append x 44 1 L
  have e2 : (seg x L 45).take 44 = seg x L 44 := by
    rw [e1]; exact List.take_left' (seg_length x 44 L)
  have e3 : (seg x L 45).getD 44 false = x (L + 44) := seg_getD x 45 L 44 (by omega)
  show seg x L 51 = (seg x L 45).take 44 ++ alt ((seg x L 45).getD 44 false) 7
  rw [e2, e3, ← seg_alt h 7 (L + 44) (Nat.le_refl _)]
  exact seg_append x 44 7 L

theorem seg_top (x : Row) (L : Nat) : (seg x L 45).drop 34 = seg x (L + 34) 11 := by
  have e : seg x L 45 = seg x L 34 ++ seg x (L + 34) 11 := seg_append x 34 11 L
  rw [e, List.drop_left' (seg_length x 34 L)]

/-- The image window, as the list the checks speak about. -/
private theorem seg_next {z : Row} {L : Nat} :
    seg z (L + 3) 45 = ((seg z L 51).drop 3).take 45 := by
  have e1 : seg z L 51 = seg z L 3 ++ seg z (L + 3) 48 := seg_append z 3 48 L
  have e2 : seg z (L + 3) 48 = seg z (L + 3) 45 ++ seg z (L + 3 + 45) 3 := seg_append z 45 3 (L + 3)
  rw [e1, List.drop_left' (seg_length z 3 L), e2]
  exact (List.take_left' (seg_length z 45 (L + 3))).symm

/-- **The lock.** Every predecessor of a locked row is locked three cells higher, whatever lies below the window. -/
theorem lock_back {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (hf : Lock x L) : Lock z (L + 3) := by
  obtain ⟨hw, hr⟩ := hf
  have e : seg z L 51 = back (z (L - 1)) (z (L - 2)) (inp (seg x L 45)) := by
    rw [back_seg hs 51 L hL, seg_inp hr]
  have ha := chk_a _ hw (z (L - 1)) (z (L - 2))
  have hb := chk_b _ hw (z (L - 1)) (z (L - 2))
  have hc := chk_c _ hw (z (L - 1)) (z (L - 2))
  have hd := chk_d _ hw (z (L - 1)) (z (L - 2))
  have hm := chk_mem _ hw (z (L - 1)) (z (L - 2))
  rw [← e] at ha hb hc hd hm
  have g : ∀ i, i < 51 → (seg z L 51).getD i false = z (L + i) := fun i h => seg_getD z 51 L i h
  rw [g 47 (by omega), g 48 (by omega)] at ha
  rw [g 48 (by omega), g 49 (by omega)] at hd
  rw [g 49 (by omega)] at hb
  rw [g 50 (by omega)] at hc
  have q : ∀ i, i < 51 → (inp (seg x L 45)).getD i false = x (L + i) := by
    intro i h; rw [← seg_inp hr]; exact seg_getD x 51 L i h
  rw [q 49 (by omega)] at hb
  rw [q 50 (by omega)] at hc
  refine ⟨by rw [seg_next]; exact hm, ?_⟩
  have htail := tail_of_compl hs (J := L + 49) (fun j hj => hr j (by omega)) hb hc
  intro j hj
  by_cases c1 : j = L + 47
  · subst c1; exact ha
  · by_cases c2 : j = L + 48
    · subst c2; exact hd
    · exact htail j (by omega)

/-- On a locked row the wall reads `A` or `B`. -/
theorem lock_letter {x : Row} {L : Nat} (h : Lock x L) :
    seg x (L + 34) 11 = wordA ∨ seg x (L + 34) 11 = wordB := by
  have := chk_top _ h.1
  rwa [seg_top] at this

/-- **The letters alternate.** The word at the wall of a predecessor is the other word. -/
theorem lock_alternates {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (hf : Lock x L) :
    (seg x (L + 34) 11 = wordA ∧ seg z (L + 37) 11 = wordB) ∨
    (seg x (L + 34) 11 = wordB ∧ seg z (L + 37) 11 = wordA) := by
  obtain ⟨hw, hr⟩ := hf
  have e : seg z L 51 = back (z (L - 1)) (z (L - 2)) (inp (seg x L 45)) := by
    rw [back_seg hs 51 L hL, seg_inp hr]
  have hl := chk_letter _ hw (z (L - 1)) (z (L - 2))
  rw [← e, ← seg_next, seg_top, seg_top] at hl
  exact hl

/-- **For ever.** Every row `n` ticks before a locked row is locked `3 n` cells higher. -/
theorem lock_forever {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Lock x L) :
    ∀ n z, iter z n = x → Lock z (L + 3 * n) := by
  intro n
  induction n with
  | zero => intro z hz; rw [show iter z 0 = z from rfl] at hz; subst hz; exact h
  | succ n ih =>
    intro z hz
    have e : iter z (1 + n) = iter (iter z 1) n := iter_add z 1 n
    rw [Nat.add_comm n 1, e] at hz
    have := lock_back (by omega) (show step z = iter z 1 from rfl) (ih (iter z 1) hz)
    have e2 : L + 3 * n + 3 = L + 3 * (n + 1) := by omega
    rw [e2] at this
    exact this

/-! ## An anchored row -/

/-- The first window of `L45` on the black edge, with one white cell below it, and rain above. -/
def row (j : Nat) : Bool :=
  if j = 0 then true else if j = 1 then false
  else if j < 47 then (27432157596204 : Nat).testBit (j - 2)
  else if (j - 47) % 2 = 0 then !(27432157596204 : Nat).testBit 44 else (27432157596204 : Nat).testBit 44

theorem row_tail (j : Nat) (hj : 47 ≤ j) : row (j + 1) = !row j := by
  by_cases a : (j - 47) % 2 = 0
  · simp [row, show ¬j = 0 by omega, show ¬j = 1 by omega, show ¬j < 47 by omega, show ¬j + 1 < 47 by omega, a] <;> omega
  · simp [row, show ¬j = 0 by omega, show ¬j = 1 by omega, show ¬j < 47 by omega, show ¬j + 1 < 47 by omega, a] <;> omega

/-- An anchored row in the lock. -/
theorem witness : row 0 = true ∧ Lock row 2 := by
  refine ⟨rfl, by decide +kernel, fun j hj => ?_⟩
  by_cases c : 47 ≤ j
  · exact row_tail j c
  · have : j = 46 := by omega
    subst this; decide +kernel

#print axioms lock_back
#print axioms lock_alternates
#print axioms lock_forever
#print axioms witness
end TwoPairs.WallLock
