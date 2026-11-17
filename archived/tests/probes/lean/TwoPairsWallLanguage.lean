import TwoPairsThreeMoves
import TwoPairsWindowExclusions

/-!
# The settled wall has more memory than one letter

GPT's `no_BB` excludes the word `B` twice in succession at the top of a wall that advances three places
backward. Here the word `A` cannot occur three times in succession (`no_AAA`), for a row at any depth, with
the same kind of proof: nine cells force a contradiction in the forward rule. So a settled wall reads `B`
every second or third tick. The pairs `AA`, `AB`, `BA` and the word `ABA` occur on anchored rows, with an
explicit row for each, so the first gap GPT asked about is closed.

Letters are read in backward time: the deepest row carries the last letter.
-/

namespace TwoPairs.WallLanguage
open ThreeMoves (wordA wordB)
open WindowExclusions (source)

private theorem read {x : Row} {L : Nat} {w : List Bool} (h : seg x L 11 = w) (i : Nat) (hi : i < 11) :
    x (L + i) = w.getD i false := by
  rw [← h, seg_getD _ _ _ _ hi]

private theorem or_false' {a b : Bool} (h : (a || b) = false) : a = false ∧ b = false := by
  cases a <;> cases b <;> simp_all

/-- **`A` cannot occur three times in succession.** The deepest window is on the row `z`, and the two later
windows are on its forward images, three cells lower each. -/
theorem no_AAA (z : Row) (L : Nat) (deep : seg z (L + 6) 11 = wordA)
    (mid : seg (step z) (L + 3) 11 = wordA) (top : seg (step (step z)) L 11 = wordA) : False := by
  -- the window on the top row against the middle row
  have v2 : step (step z) (L + 2) = true := read top 2 (by decide)
  have v4 : step (step z) (L + 4) = true := read top 4 (by decide)
  have u3 : step z (L + 3) = false := read mid 0 (by decide)
  have u4 : step z (L + 4) = false := read mid 1 (by decide)
  have u5 : step z (L + 5) = true := read mid 2 (by decide)
  have u7 : step z (L + 7) = true := read mid 4 (by decide)
  have z6 : z (L + 6) = false := read deep 0 (by decide)
  have z7 : z (L + 7) = false := read deep 1 (by decide)
  change xor (step z (L + 4)) (step z (L + 3) || step z (L + 2)) = true at v4
  rw [u4, u3] at v4
  have u2 : step z (L + 2) = true := by simpa using v4
  change xor (step z (L + 2)) (step z (L + 1) || step z L) = true at v2
  rw [u2] at v2
  have w1 : (step z (L + 1) || step z L) = false := by simpa using v2
  have u1 : step z (L + 1) = false := (or_false' w1).1
  -- the same two steps one row deeper
  change xor (z (L + 7)) (z (L + 6) || z (L + 5)) = true at u7
  rw [z7, z6] at u7
  have z5 : z (L + 5) = true := by simpa using u7
  change xor (z (L + 5)) (z (L + 4) || z (L + 3)) = true at u5
  rw [z5] at u5
  have w2 : (z (L + 4) || z (L + 3)) = false := by simpa using u5
  obtain ⟨z4, z3⟩ := or_false' w2
  change xor (z (L + 4)) (z (L + 3) || z (L + 2)) = false at u4
  rw [z4, z3] at u4
  have z2 : z (L + 2) = false := by simpa using u4
  change xor (z (L + 3)) (z (L + 2) || z (L + 1)) = false at u3
  rw [z3, z2] at u3
  have z1 : z (L + 1) = false := by simpa using u3
  change xor (z (L + 2)) (z (L + 1) || z L) = true at u2
  rw [z2, z1] at u2
  have z0 : z L = true := by simpa using u2
  -- wheel L + 1 of the middle row cannot be white
  cases L with
  | zero =>
    have e : step z 1 = xor (z 1) (z 0) := rfl
    simp only [Nat.zero_add] at u1 z1 z0
    rw [e, z1, z0] at u1
    cases u1
  | succ k =>
    have e : step z (k + 1 + 1) = xor (z (k + 1 + 1)) (z (k + 1) || z k) := rfl
    rw [e, z1, z0] at u1
    cases u1

/-! ## Witnesses on anchored rows -/

/-- The row `x` shows the word `w` from cell `L`, with rain above it. -/
def Shows (x : Row) (L : Nat) (w : List Bool) : Prop :=
  seg x L 11 = w ∧ ∀ j, L + 10 ≤ j → x (j + 1) = !x j

theorem source_tail (w low L j : Nat) (hj : L + 10 ≤ j) :
    source w low L (j + 1) = !source w low L j := by
  by_cases a : (j - (L + 10)) % 2 = 0
  · simp [source, show ¬j < L by omega, show ¬j + 1 < L by omega,
      show ¬j < L + 10 by omega, show ¬j + 1 < L + 10 by omega, a] <;> omega
  · simp [source, show ¬j < L by omega, show ¬j + 1 < L by omega,
      show ¬j < L + 10 by omega, show ¬j + 1 < L + 10 by omega, a] <;> omega

/-- A forward image keeps the rain, given the few cells that the general lemma does not reach. -/
private theorem step_shows {x : Row} {L P : Nat} {w : List Bool} (h : ∀ j, L ≤ j → x (j + 1) = !x j)
    (hw : seg (step x) P 11 = w)
    (near : ∀ j : Fin (L + 2), P + 10 ≤ j.val → step x (j.val + 1) = !step x j.val) :
    Shows (step x) P w := by
  refine ⟨hw, fun j hj => ?_⟩
  by_cases c : j < L + 2
  · exact near ⟨j, c⟩ hj
  · exact step_rain_tail h j (by omega)

/-- `AA`: the row with low bits 33 below `A`. -/
theorem witness_AA :
    source 1596 33 6 0 = true ∧ Shows (source 1596 33 6) 6 wordA ∧ Shows (step (source 1596 33 6)) 3 wordA := by
  have t := source_tail 1596 33 6
  refine ⟨by decide, ⟨by decide +kernel, t⟩, ?_⟩
  exact step_shows (L := 16) t (by decide +kernel) (by decide +kernel)

/-- `AB` in backward order: `B` on the deeper row. The low bits are 7. -/
theorem witness_AB :
    source 1594 7 4 0 = true ∧ Shows (source 1594 7 4) 4 wordB ∧ Shows (step (source 1594 7 4)) 1 wordA := by
  have t := source_tail 1594 7 4
  refine ⟨by decide, ⟨by decide +kernel, t⟩, ?_⟩
  exact step_shows (L := 14) t (by decide +kernel) (by decide +kernel)

/-- `BA` in backward order: `A` on the deeper row. The low bits are 11. -/
theorem witness_BA :
    source 1596 11 4 0 = true ∧ Shows (source 1596 11 4) 4 wordA ∧ Shows (step (source 1596 11 4)) 1 wordB := by
  have t := source_tail 1596 11 4
  refine ⟨by decide, ⟨by decide +kernel, t⟩, ?_⟩
  exact step_shows (L := 14) t (by decide +kernel) (by decide +kernel)

/-- `ABA` on one row: both ends of the pair of pairs share one shallow history. The low bits are 97. -/
theorem witness_ABA :
    source 1596 97 7 0 = true ∧ Shows (source 1596 97 7) 7 wordA ∧ Shows (step (source 1596 97 7)) 4 wordB ∧
      Shows (step (step (source 1596 97 7))) 1 wordA := by
  have t := source_tail 1596 97 7
  have s1 : Shows (step (source 1596 97 7)) 4 wordB := step_shows (L := 17) t (by decide +kernel) (by decide +kernel)
  refine ⟨by decide, ⟨by decide +kernel, t⟩, s1, ?_⟩
  exact step_shows (L := 19) (fun j hj => s1.2 j (by omega)) (by decide +kernel) (by decide +kernel)

#print axioms no_AAA
#print axioms witness_AA
#print axioms witness_AB
#print axioms witness_BA
#print axioms witness_ABA
end TwoPairs.WallLanguage
