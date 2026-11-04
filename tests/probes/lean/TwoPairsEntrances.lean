import TwoPairs

/-!
# Entrance rows of the eleven-cell robust front

The spatial coordinate `L` is the first cell of the window. Its top wall is at
`L + 9`. We include only `L ≥ 2`, the guard of `TwoPairs.front_back`.
An entrance going backward is the last robust row going forward.
-/

namespace TwoPairs.Entrances

def Robust (x : Row) : Prop := ∃ L, 2 ≤ L ∧ Front x L

def Entrance (x : Row) : Prop := Robust x ∧ ¬Robust (step x)

private theorem xor_twice (a b : Bool) : xor (xor a b) b = a := by
  cases a <;> cases b <;> rfl

/-- Triangular recovery of the entire row, including cells 0 and 1. -/
def previous (x : Row) : Row
  | 0 => x 0
  | 1 => xor (x 1) (x 0)
  | j + 2 => xor (x (j + 2)) (previous x (j + 1) || previous x j)

theorem step_previous (x : Row) : step (previous x) = x := by
  funext j
  cases j with
  | zero => rfl
  | succ k =>
    cases k with
    | zero => exact xor_twice _ _
    | succ i =>
      rw [step_add, previous]
      exact xor_twice _ _

theorem previous_step (x : Row) : previous (step x) = x := by
  have pair : ∀ i, previous (step x) i = x i ∧ previous (step x) (i + 1) = x (i + 1) := by
    intro i
    induction i with
    | zero => exact ⟨rfl, xor_twice _ _⟩
    | succ i ih =>
      refine ⟨ih.2, ?_⟩
      rw [previous, ih.1, ih.2, step_add]
      exact xor_twice _ _
  funext i
  exact (pair i).1

private theorem front_cannot_lie_above {x : Row} {L M : Nat}
    (f : Front x L) (g : Front x M) (lt : L < M) : False := by
  have w := chk_wall _ g.1
  rw [seg_getD x 11 M 9 (by decide), seg_getD x 11 M 10 (by decide)] at w
  have a := f.2 (M + 9) (by omega)
  change x (M + 10) = !x (M + 9) at a
  rw [← w] at a
  cases h : x (M + 10) <;> simp [h] at a

theorem front_level_unique {x : Row} {L M : Nat} (f : Front x L) (g : Front x M) :
    L = M := by
  by_cases h : L < M
  · exact False.elim (front_cannot_lie_above f g h)
  · by_cases k : M < L
    · exact False.elim (front_cannot_lie_above g f k)
    · omega

/-- A robust successor can have only one window location, three below the old one. -/
theorem front_step_level {x : Row} {L M : Nat} (f : Front x L)
    (hM : 2 ≤ M) (g : Front (step x) M) : L = M + 3 :=
  front_level_unique f (front_back hM rfl g)

theorem shallow_entrance {x : Row} {L : Nat} (hL : 2 ≤ L) (low : L < 5)
    (f : Front x L) : Entrance x := by
  refine ⟨⟨L, hL, f⟩, ?_⟩
  intro ⟨M, hM, g⟩
  have := front_step_level f hM g
  omega

/-- At a fixed deep level, test just one possible successor window. -/
theorem entrance_iff {x : Row} {L : Nat} (hL : 2 ≤ L) (f : Front x (L + 3)) :
    Entrance x ↔ ¬Front (step x) L := by
  constructor
  · intro e g
    exact e.2 ⟨L, hL, g⟩
  · intro h
    refine ⟨⟨L + 3, by omega, f⟩, ?_⟩
    intro ⟨M, hM, g⟩
    have eq := front_step_level f hM g
    have : M = L := by omega
    exact h (this ▸ g)

/-- `previous` is a bijection from anchored robust rows at L onto the anchored
non-entrance rows at L+3. The two inverse identities above give its inverse `step`. -/
theorem previous_image {x : Row} {L : Nat} (hL : 2 ≤ L) :
    (x 0 = true ∧ Front x (L + 3) ∧ ¬Entrance x) ↔
      ∃ y : Row, y 0 = true ∧ Front y L ∧ previous y = x := by
  constructor
  · intro ⟨black, f, h⟩
    have g : Front (step x) L := by
      apply Classical.byContradiction
      exact fun ng => h ((entrance_iff hL f).2 ng)
    exact ⟨step x, black, g, previous_step x⟩
  · intro ⟨y, black, g, eq⟩
    subst x
    refine ⟨black, front_back hL (step_previous y) g, ?_⟩
    intro e
    apply e.2
    rw [step_previous]
    exact ⟨L, hL, g⟩

private theorem robust_before_step {x : Row} : Robust (step x) → Robust x := by
  intro ⟨L, hL, f⟩
  exact ⟨L + 3, by omega, front_back hL rfl f⟩

private theorem robust_before_iter {x : Row} (t : Nat) : Robust (iter x t) → Robust x := by
  induction t with
  | zero => exact fun h => h
  | succ t ih => exact fun h => ih (robust_before_step h)

/-- No later iterate of an entrance is robust. -/
theorem after_entrance {x : Row} (h : Entrance x) (t : Nat) : ¬Robust (iter x (1 + t)) := by
  rw [iter_add]
  exact fun g => h.2 (robust_before_iter t g)

/-- Every robust row reaches an entrance in at most (L−2)/3 forward ticks. -/
theorem reaches_entrance {x : Row} {L : Nat} (hL : 2 ≤ L) (f : Front x L) :
    ∃ t, 3 * t + 2 ≤ L ∧ Entrance (iter x t) := by
  induction L using Nat.strongRecOn generalizing x with
  | _ L ih =>
    by_cases h : Robust (step x)
    · obtain ⟨M, hM, g⟩ := h
      have eq := front_step_level f hM g
      obtain ⟨t, bound, e⟩ := ih M (by omega) hM g
      refine ⟨1 + t, by omega, ?_⟩
      rw [iter_add]
      exact e
    · exact ⟨0, by omega, ⟨⟨L, hL, f⟩, h⟩⟩

theorem entrance_time_unique {x : Row} {s t : Nat} (hs : Entrance (iter x s))
    (ht : Entrance (iter x t)) : s = t := by
  have order : ∀ a b : Nat, Entrance (iter x a) → Entrance (iter x b) → a ≤ b := by
    intro a b ea eb
    by_cases le : a ≤ b
    · exact le
    · obtain ⟨d, eq⟩ : ∃ d, a = b + (1 + d) := ⟨a - b - 1, by omega⟩
      rw [eq, iter_add] at ea
      exact False.elim (after_entrance eb d ea.1)
  exact Nat.le_antisymm (order s t hs ht) (order t s ht hs)

end TwoPairs.Entrances
