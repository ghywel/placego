import TwoPairsSixPhysical
import TwoPairsFrontPadding

/-! # Real six-window capture at the shallow boundary and its intermediate wall positions -/

namespace TwoPairs.Six

open FrontPadding

private def Screen (words : List (List Bool)) (x : Row) (L : Nat) : Prop :=
  seg x L 11 ∈ words ∧ ∀ j, L + 10 ≤ j → x (j + 1) = !x j

private theorem pad_seg (x : Row) (n L : Nat) : seg (padTwo x) (L + 2) n = seg x L n := by
  induction n generalizing L with
  | zero => rfl
  | succ n ih =>
    change x L :: seg (padTwo x) (L + 1 + 2) n = x L :: seg x (L + 1) n
    rw [ih]

private theorem lift_screen {words : List (List Bool)} {z : Row} {r L : Nat}
    (h : Screen words (iter z r) L) : Screen words (iter (padTwo z) r) (L + 2) := by
  rw [iter_padTwo]
  refine ⟨by rw [pad_seg]; exact h.1, ?_⟩
  intro j hj
  obtain ⟨i, rfl⟩ : ∃ i, j = i + 2 := ⟨j - 2, by omega⟩
  exact h.2 i (by omega)

theorem fast_all_levels (z : Row) (L : Nat) (screen : seg (iter z 2) L 11 ∈ fast)
    (rain : ∀ j, L + 10 ≤ j → iter z 2 (j + 1) = !iter z 2 j) : Front z (L + 6) := by
  have h : Screen fast (iter z 2) L := ⟨screen, rain⟩
  have hp := lift_screen (lift_screen h)
  have f := fast_physical _ (L + 2 + 2) (by omega) hp.1 hp.2
  exact (front_padTwo z (L + 6)).1 ((front_padTwo _ (L + 6 + 2)).1 f)

theorem slow_all_levels (z : Row) (L : Nat) (screen : seg (iter z 3) L 11 ∈ slow)
    (rain : ∀ j, L + 10 ≤ j → iter z 3 (j + 1) = !iter z 3 j) : Front z (L + 9) := by
  have h : Screen slow (iter z 3) L := ⟨screen, rain⟩
  have hp := lift_screen (lift_screen (lift_screen h))
  have f := slow_physical _ (L + 2 + 2 + 2) (by omega) hp.1 hp.2
  exact (front_padTwo z (L + 9)).1
    ((front_padTwo _ (L + 9 + 2)).1 ((front_padTwo _ (L + 9 + 2 + 2)).1 f))

private theorem top_of_front {x : Row} {L : Nat} (f : Front x L) : Top x (L + 9) := by
  have h := chk_wall _ f.1
  rw [seg_getD x 11 L 9 (by decide), seg_getD x 11 L 10 (by decide)] at h
  exact ⟨h.symm, f.2⟩

/-- Equality in the backward tail bound forces a wall at the other endpoint. -/
private theorem tight_step {z x : Row} {D : Nat} (hD : 2 ≤ D) (s : step z = x)
    (w : Top z (D + 3)) (tail : ∀ j, D + 1 ≤ j → x (j + 1) = !x j) : Top x D := by
  refine ⟨?_, tail⟩
  apply Classical.byContradiction
  intro different
  have full : ∀ j, D ≤ j → x (j + 1) = !x j := by
    intro j hj
    by_cases eq : j = D
    · subst j
      cases a : x D <;> cases b : x (D + 1) <;> simp_all
    · exact tail j (by omega)
  have alt := back_rain_tail hD s full (D + 3) (by omega)
  rw [w.1] at alt
  cases a : z (D + 3) <;> simp_all

/-- The fast screen has exact backward top displacements +3, +3 before the robust regime. -/
theorem fast_passage (z : Row) (L : Nat) (screen : seg (iter z 2) L 11 ∈ fast)
    (rain : ∀ j, L + 10 ≤ j → iter z 2 (j + 1) = !iter z 2 j) :
    Top (iter z 2) (L + 9) ∧ Top (iter z 1) (L + 12) ∧ Front z (L + 6) := by
  have f := fast_all_levels z L screen rain
  have last := top_of_front f
  have mid := back_rain_tail (z := iter z 1) (D := L + 10) (by omega) rfl rain
  have w1 := tight_step (z := z) (x := iter z 1) (D := L + 12) (by omega) rfl last mid
  exact ⟨tight_step (D := L + 9) (by omega) rfl w1 rain, w1, f⟩

/-- The slow screen has three consecutive backward top displacements of +3. -/
theorem slow_passage (z : Row) (L : Nat) (screen : seg (iter z 3) L 11 ∈ slow)
    (rain : ∀ j, L + 10 ≤ j → iter z 3 (j + 1) = !iter z 3 j) :
    Top (iter z 3) (L + 9) ∧ Top (iter z 2) (L + 12) ∧
      Top (iter z 1) (L + 15) ∧ Front z (L + 9) := by
  have f := slow_all_levels z L screen rain
  have last := top_of_front f
  have r2 := back_rain_tail (z := iter z 2) (D := L + 10) (by omega) rfl rain
  have r1 := back_rain_tail (z := iter z 1) (D := L + 13) (by omega) rfl r2
  have w1 := tight_step (z := z) (x := iter z 1) (D := L + 15) (by omega) rfl last r1
  have w2 := tight_step (z := iter z 1) (x := iter z 2) (D := L + 12) (by omega) rfl w1 r2
  exact ⟨tight_step (D := L + 9) (by omega) rfl w2 rain, w2, w1, f⟩

end TwoPairs.Six
