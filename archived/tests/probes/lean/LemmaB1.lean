import Mathlib

/-!
# Lemma B1 (PROOFS.md entry 8): white, then black (Local, 2026-10-10)

Rule 30 on configurations ℤ → Bool with a leftmost black cell e at time 0. Diagonal j at time t is the cell
e - t + j: diagonal 0 is the moving left edge (always black), diagonals j < 0 are white.
Lemma B1: (1) no two adjacent diagonals are both eventually white; (2) if diagonal j is eventually white, diagonal
j + 2 is eventually black; (3) if diagonal k >= 2 is eventually black, diagonal k - 2 is eventually white.

The proof is entry 8's, from the diagonal recurrence D_j(t+1) = D_(j-2)(t) xor (D_(j-1)(t) or D_j(t)).

How to check: as for TheoremA.lean; the `#print axioms` line must list no `sorryAx`.
-/

namespace LemmaB1

def step (x : ℤ → Bool) : ℤ → Bool := fun i => xor (x (i - 1)) (x i || x (i + 1))

def ev (x0 : ℤ → Bool) : ℕ → ℤ → Bool
  | 0 => x0
  | t + 1 => step (ev x0 t)

lemma ev_succ (x0 : ℤ → Bool) (t : ℕ) (i : ℤ) :
    ev x0 (t + 1) i = xor (ev x0 t (i - 1)) (ev x0 t i || ev x0 t (i + 1)) := rfl

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

/-- Diagonal j at time t. -/
def D (x0 : ℤ → Bool) (e : ℤ) (j : ℤ) (t : ℕ) : Bool := ev x0 t (e - t + j)

/-- The diagonal recurrence. -/
lemma D_succ (x0 : ℤ → Bool) (e j : ℤ) (t : ℕ) :
    D x0 e j (t + 1) = xor (D x0 e (j - 2) t) (D x0 e (j - 1) t || D x0 e j t) := by
  unfold D
  rw [ev_succ]
  rw [show e - ((t + 1 : ℕ) : ℤ) + j - 1 = e - t + (j - 2) by push_cast; ring,
    show e - ((t + 1 : ℕ) : ℤ) + j = e - t + (j - 1) by push_cast; ring,
    show e - (t : ℤ) + (j - 1) + 1 = e - t + j by ring]

/-- Eventually white / eventually black. -/
def EvW (x0 : ℤ → Bool) (e j : ℤ) : Prop := ∃ T : ℕ, ∀ t, T ≤ t → D x0 e j t = false
def EvB (x0 : ℤ → Bool) (e j : ℤ) : Prop := ∃ T : ℕ, ∀ t, T ≤ t → D x0 e j t = true

section
variable (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false)
include he hl

lemma D0 (t : ℕ) : D x0 e 0 t = true := by
  unfold D; simpa using (edge x0 e he hl t).1

lemma Dneg (j : ℤ) (hj : j < 0) (t : ℕ) : D x0 e j t = false := by
  unfold D; exact (edge x0 e he hl t).2 _ (by omega)

omit he hl in
/-- Two adjacent eventually white diagonals force the one before them eventually white. -/
lemma down (j : ℤ) (h0 : EvW x0 e j) (h1 : EvW x0 e (j + 1)) : EvW x0 e (j - 1) := by
  obtain ⟨T0, h0⟩ := h0
  obtain ⟨T1, h1⟩ := h1
  refine ⟨T0 + T1, fun t ht => ?_⟩
  have := h1 (t + 1) (by omega)
  rw [D_succ, show j + 1 - 2 = j - 1 by ring, show j + 1 - 1 = j by ring, h0 t (by omega), h1 t (by omega)] at this
  simpa using this

/-- (1) No two adjacent diagonals are both eventually white. -/
theorem no_adjacent_white (j : ℤ) (hj : 0 ≤ j) (h0 : EvW x0 e j) (h1 : EvW x0 e (j + 1)) : False := by
  -- walk down to the pair (0, 1)
  have key : ∀ n : ℕ, ∀ j : ℤ, j = n → EvW x0 e j → EvW x0 e (j + 1) → False := by
    intro n
    induction n with
    | zero =>
      intro j hjn hw _
      obtain ⟨T, hT⟩ := hw
      have := hT T le_rfl
      rw [hjn, show ((0 : ℕ) : ℤ) = 0 by simp, D0 x0 e he hl] at this
      exact absurd this (by decide)
    | succ n ih =>
      intro j hjn hw hw1
      exact ih (j - 1) (by rw [hjn]; push_cast; ring) (down x0 e j hw hw1) (by simpa using hw)
  exact key j.toNat j (by omega) h0 h1

omit he hl in
/-- A monotone diagonal is eventually constant. -/
lemma mono_eventually (j : ℤ) (T : ℕ) (hm : ∀ t, T ≤ t → D x0 e j t = true → D x0 e j (t + 1) = true) :
    EvW x0 e j ∨ EvB x0 e j := by
  by_cases h : ∃ t, T ≤ t ∧ D x0 e j t = true
  · obtain ⟨t0, ht0, hb⟩ := h
    right
    refine ⟨t0, fun t ht => ?_⟩
    induction t, ht using Nat.le_induction with
    | base => exact hb
    | succ t ht ih => exact hm t (by omega) ih
  · push Not at h
    left
    exact ⟨T, fun t ht => by simpa using h t ht⟩

/-- (2) If diagonal j >= 0 is eventually white, diagonal j + 2 is eventually black. -/
theorem white_then_black (j : ℤ) (hj : 0 ≤ j) (h0 : EvW x0 e j) : EvB x0 e (j + 2) := by
  obtain ⟨T, hT⟩ := h0
  have hm : ∀ t, T ≤ t → D x0 e (j + 2) t = true → D x0 e (j + 2) (t + 1) = true := by
    intro t ht hb
    rw [D_succ, show j + 2 - 2 = j by ring, hT t ht, hb]; simp
  rcases mono_eventually x0 e (j + 2) T hm with hw | hb
  · -- then diagonal j + 1 is eventually white too, contradicting (1)
    exfalso
    obtain ⟨T2, h2⟩ := hw
    have h1 : EvW x0 e (j + 1) := ⟨T + T2, fun t ht => by
      have := h2 (t + 1) (by omega)
      rw [D_succ, show j + 2 - 2 = j by ring, show j + 2 - 1 = j + 1 by ring, hT t (by omega)] at this
      simp at this
      exact this.1⟩
    exact no_adjacent_white x0 e he hl j hj ⟨T, hT⟩ h1
  · exact hb

omit he hl in
/-- (3) If diagonal k is eventually black, diagonal k - 2 is eventually white. -/
theorem black_needs_white (k : ℤ) (hb : EvB x0 e k) : EvW x0 e (k - 2) := by
  obtain ⟨T, hT⟩ := hb
  refine ⟨T, fun t ht => ?_⟩
  have := hT (t + 1) (by omega)
  rw [D_succ, hT t ht] at this
  simpa using this

end

end LemmaB1

#print axioms LemmaB1.no_adjacent_white
#print axioms LemmaB1.white_then_black
#print axioms LemmaB1.black_needs_white
