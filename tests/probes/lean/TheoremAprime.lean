import Mathlib

/-!
# Theorem A′ (PROOFS.md entry 7): a block recurs only if it is no longer than the edge is far (Local, 2026-10-10)

Rule 30 on configurations ℤ → Bool: x'(i) = x(i - 1) xor (x(i) or x(i + 1)).
Theorem A′: if the leftmost black cell at time 0 is L ≥ 0 cells left of column i, and the pair of columns (i, i + 1)
shows the same block of n consecutive values starting at times a and a′ > a, then n ≤ L + a′.

The proof is entry 7's: read right to left, x_t(j - 1) = x_(t+1)(j) xor (x_t(j) or x_t(j + 1)), so the two columns
at times t .. t + m fix the cell m to their left at time t (`agree`); equal blocks make the rows at a and a′ agree
for n - 1 cells left of column i; the later row is black L + a′ cells out (the edge lemma), where the earlier row is
still white.

How to check: as for TheoremA.lean; the `#print axioms` line must list no `sorryAx`.
-/

namespace TheoremAprime

/-- One Rule 30 step (as in TheoremA.lean). -/
def step (x : ℤ → Bool) : ℤ → Bool := fun i => xor (x (i - 1)) (x i || x (i + 1))

/-- The evolution from `x0` (as in TheoremA.lean). -/
def ev (x0 : ℤ → Bool) : ℕ → ℤ → Bool
  | 0 => x0
  | t + 1 => step (ev x0 t)

lemma ev_succ (x0 : ℤ → Bool) (t : ℕ) (i : ℤ) :
    ev x0 (t + 1) i = xor (ev x0 t (i - 1)) (ev x0 t i || ev x0 t (i + 1)) := rfl

/-- Fact 2 (as in TheoremA.lean): the leftmost black cell moves left one cell a step. -/
lemma edge (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (t : ℕ) :
    ev x0 t (e - t) = true ∧ ∀ j < e - t, ev x0 t j = false := by
  induction t with
  | zero => simpa using ⟨he, hl⟩
  | succ t ih =>
    obtain ⟨h1, h2⟩ := ih
    constructor
    · rw [ev_succ]
      have a1 : ev x0 t (e - ↑(t + 1) - 1) = false := h2 _ (by push_cast; omega)
      have a2 : ev x0 t (e - ↑(t + 1)) = false := h2 _ (by push_cast; omega)
      have a3 : e - ↑(t + 1) + 1 = e - ↑t := by push_cast; ring
      rw [a1, a2, a3, h1]; rfl
    · intro j hj
      rw [ev_succ]
      have b1 : ev x0 t (j - 1) = false := h2 _ (by push_cast at hj; omega)
      have b2 : ev x0 t j = false := h2 _ (by push_cast at hj; omega)
      have b3 : ev x0 t (j + 1) = false := h2 _ (by push_cast at hj; omega)
      rw [b1, b2, b3]; rfl

/-- Read right to left: x_t(j - 1) from x_(t+1)(j), x_t(j) and x_t(j + 1). -/
lemma inv (x0 : ℤ → Bool) (t : ℕ) (j : ℤ) :
    ev x0 t (j - 1) = xor (ev x0 (t + 1) j) (ev x0 t j || ev x0 t (j + 1)) := by
  rw [ev_succ]
  cases ev x0 t (j - 1) <;> cases (ev x0 t j || ev x0 t (j + 1)) <;> rfl

/-- Equal blocks on columns i and i + 1 at times a .. a + n - 1 and a′ .. a′ + n - 1 make the rows agree: the cell
m to the left of column i agrees at times a + s and a′ + s whenever s + m < n. -/
lemma agree (x0 : ℤ → Bool) (i : ℤ) (n a a' : ℕ)
    (hblock : ∀ s : ℕ, s < n → ev x0 (a + s) i = ev x0 (a' + s) i ∧ ev x0 (a + s) (i + 1) = ev x0 (a' + s) (i + 1)) :
    ∀ m s : ℕ, s + m < n → ev x0 (a + s) (i - m) = ev x0 (a' + s) (i - m) := by
  intro m
  induction m using Nat.strong_induction_on with
  | _ m ih =>
    intro s hs
    rcases m with _ | m
    · simpa using (hblock s (by omega)).1
    · -- the cell m + 1 to the left from the cells m and m - 1 to the left (or column i + 1 when m = 0)
      have h1 : ev x0 (a + s + 1) (i - m) = ev x0 (a' + s + 1) (i - m) := by
        have := ih m (by omega) (s + 1) (by omega)
        rwa [show a + (s + 1) = a + s + 1 by ring, show a' + (s + 1) = a' + s + 1 by ring] at this
      have h2 : ev x0 (a + s) (i - m) = ev x0 (a' + s) (i - m) := ih m (by omega) s (by omega)
      have h3 : ev x0 (a + s) (i - m + 1) = ev x0 (a' + s) (i - m + 1) := by
        rcases m with _ | m
        · simpa using (hblock s (by omega)).2
        · have := ih m (by omega) s (by omega)
          rwa [show i - ((m : ℕ) : ℤ) = i - ((m + 1 : ℕ) : ℤ) + 1 by push_cast; ring] at this
      rw [show i - ((m + 1 : ℕ) : ℤ) = (i - m) - 1 by push_cast; ring, inv x0 (a + s), inv x0 (a' + s), h1, h2, h3]

/-- Theorem A′. -/
theorem theorem_A' (x0 : ℤ → Bool) (i : ℤ) (L : ℕ) (hc : x0 (i - L) = true) (hl : ∀ j < i - L, x0 j = false)
    (n a a' : ℕ) (haa : a < a')
    (hblock : ∀ s : ℕ, s < n → ev x0 (a + s) i = ev x0 (a' + s) i ∧ ev x0 (a + s) (i + 1) = ev x0 (a' + s) (i + 1)) :
    n ≤ L + a' := by
  by_contra h
  push Not at h
  have hag := agree x0 i n a a' hblock (L + a') 0 (by omega)
  simp only [add_zero] at hag
  have E := edge x0 (i - L) hc hl
  have black : ev x0 a' (i - ((L + a' : ℕ) : ℤ)) = true := by
    have := (E a').1
    rwa [show i - (L : ℤ) - (a' : ℤ) = i - ((L + a' : ℕ) : ℤ) by push_cast; ring] at this
  have white : ev x0 a (i - ((L + a' : ℕ) : ℤ)) = false :=
    (E a).2 _ (by push_cast; omega)
  rw [white, black] at hag
  exact absurd hag (by decide)

/-- Theorem A‴ (entry 10): row a′ is white at the distances L + a + 1 .. n - 1 left of column i, which are its
diagonals L + a′ - n + 1 .. a′ - a - 1. -/
theorem theorem_A3_white (x0 : ℤ → Bool) (i : ℤ) (L : ℕ) (hc : x0 (i - L) = true) (hl : ∀ j < i - L, x0 j = false)
    (n a a' : ℕ)
    (hblock : ∀ s : ℕ, s < n → ev x0 (a + s) i = ev x0 (a' + s) i ∧ ev x0 (a + s) (i + 1) = ev x0 (a' + s) (i + 1)) :
    ∀ δ : ℕ, L + a + 1 ≤ δ → δ + 1 ≤ n → ev x0 a' (i - δ) = false := by
  intro δ h1 h2
  have hag := agree x0 i n a a' hblock δ 0 (by omega)
  simp only [add_zero] at hag
  rw [← hag]
  exact (edge x0 (i - L) hc hl a).2 _ (by omega)

/-- Theorem A‴'s corollary: if diagonal b (the cell b right of the moving left edge) is black at time a′ and
b < a′ - a, then n ≤ L + a′ - b. -/
theorem theorem_A3 (x0 : ℤ → Bool) (i : ℤ) (L : ℕ) (hc : x0 (i - L) = true) (hl : ∀ j < i - L, x0 j = false)
    (n a a' b : ℕ) (hb : b + a < a') (hblack : ev x0 a' (i - L - a' + b) = true)
    (hblock : ∀ s : ℕ, s < n → ev x0 (a + s) i = ev x0 (a' + s) i ∧ ev x0 (a + s) (i + 1) = ev x0 (a' + s) (i + 1)) :
    n ≤ L + a' - b := by
  by_contra h
  push Not at h
  have hw := theorem_A3_white x0 i L hc hl n a a' hblock (L + a' - b) (by omega) (by omega)
  rw [show i - ((L + a' - b : ℕ) : ℤ) = i - L - a' + b by push_cast [show b ≤ L + a' by omega]; ring] at hw
  rw [hw] at hblack
  exact absurd hblack (by decide)

end TheoremAprime

#print axioms TheoremAprime.theorem_A'
#print axioms TheoremAprime.theorem_A3
