import TwoPairsThreeMoves
import TwoPairsShortPositive

/-! # Three exact backward top-wall advances force all subsequent advances

This includes top index zero. Six white cells translate the four observed
rows together across the shallow boundary without changing their dynamics.
-/

namespace TwoPairs.ThreeLock

open Entrances FrontPadding ShortPositive WindowExclusions

private def six (z : Row) : Row := padTwo (padTwo (padTwo z))

private theorem lift_top (z : Row) (r D : Nat) (h : Top (iter z r) D) :
    Top (iter (six z) r) (D + 6) := by
  simp only [six, iter_padTwo]
  exact (top_padTwo _ (D + 4)).2 ((top_padTwo _ (D + 2)).2 ((top_padTwo _ D).2 h))

private theorem six_seg (x : Row) (n L : Nat) : seg (six x) (L + 6) n = seg x L n := by
  induction n generalizing L with
  | zero => rfl
  | succ n ih =>
    change x L :: seg (six x) (L + 1 + 6) n = x L :: seg x (L + 1) n
    rw [ih]

theorem lock (z : Row) (D : Nat)
    (t0 : Top z (D + 9)) (t1 : Top (iter z 1) (D + 6))
    (t2 : Top (iter z 2) (D + 3)) (t3 : Top (iter z 3) D) : Front z D := by
  have f := ThreeMoves.deep (six z) (D + 6) (by omega)
    (lift_top z 0 _ t0) (lift_top z 1 _ t1) (lift_top z 2 _ t2) (lift_top z 3 _ t3)
  exact (front_padTwo z D).1 ((front_padTwo _ (D + 2)).1 ((front_padTwo _ (D + 4)).1 f))

theorem two_words (z : Row) (D : Nat)
    (t0 : Top z (D + 9)) (t1 : Top (iter z 1) (D + 6))
    (t2 : Top (iter z 2) (D + 3)) (t3 : Top (iter z 3) D) :
    seg z D 11 = ThreeMoves.wordA ∨ seg z D 11 = ThreeMoves.wordB := by
  have h := ThreeMoves.deep_words (six z) (D + 6) (by omega)
    (lift_top z 0 _ t0) (lift_top z 1 _ t1) (lift_top z 2 _ t2) (lift_top z 3 _ t3)
  simpa only [six_seg] using h

theorem locked_tops (z : Row) (D : Nat)
    (t0 : Top z (D + 9)) (t1 : Top (iter z 1) (D + 6))
    (t2 : Top (iter z 2) (D + 3)) (t3 : Top (iter z 3) D) (r : Nat) :
    Top (previousN z r) (D + 9 + 3 * r) := by
  have f := lock z D t0 t1 t2 t3
  refine WindowClassification.listed_forever z D ?_ t0 r
  simp only [List.mem_append, or_assoc]
  exact Or.inl f.1

/-- In the original backward clock, the third maximal step lands in the robust set. -/
theorem front_after_three (x : Row) (D : Nat)
    (h0 : Top x D) (h1 : Top (previousN x 1) (D + 3))
    (h2 : Top (previousN x 2) (D + 6)) (h3 : Top (previousN x 3) (D + 9)) :
    Front (previousN x 3) D := by
  apply lock _ _ h3
  · simpa [previousN, iter, step_previous] using h2
  · simpa [previousN, iter, step_previous] using h1
  · simpa [previousN, iter, step_previous] using h0

/-- Three observed advances suffice for an infinite statement about this same row,
without quantifying over other rows that share its window. -/
theorem passage_forever (x : Row) (D : Nat)
    (h0 : Top x D) (h1 : Top (previousN x 1) (D + 3))
    (h2 : Top (previousN x 2) (D + 6)) (h3 : Top (previousN x 3) (D + 9)) (r : Nat) :
    Top (previousN x r) (D + 3 * r) := by
  cases r with
  | zero => simpa [previousN] using h0
  | succ r =>
    cases r with
    | zero => exact h1
    | succ r =>
      cases r with
      | zero => exact h2
      | succ s =>
        have f := front_after_three x D h0 h1 h2 h3
        have mem : seg (previousN x 3) D 11 ∈ B11 ++ Six.fast ++ Six.slow := by
          simp only [List.mem_append, or_assoc]
          exact Or.inl f.1
        have h := WindowClassification.listed_forever (previousN x 3) D mem h3 s
        rw [show D + 3 * (s + 1 + 1 + 1) = D + 9 + 3 * s by omega]
        exact h

#print axioms two_words
#print axioms passage_forever
end TwoPairs.ThreeLock
