import Mathlib

/-!
# Theorem B (PROOFS.md entry 6): a zero run cannot outlast two periods (Local, 2026-10-10)

Rule 30 on configurations ℤ → Bool: x'(i) = x(i - 1) xor (x(i) or x(i + 1)).
Theorem B: let columns 0 and 1 be P-periodic from time 0, with P ≥ 2 and column 0 not zero. Then every run of
zeros in row 0 of the left half (columns -d .. -(d + R - 1), d ≥ 1) has length R ≤ 2P - 2.

The proof is entry 6's: every left column is P-periodic (fact 1 of Theorem A, on an unbounded window); a zero run
leaves a white triangle beneath it; if R ≥ 2P - 1, column -(d + P - 1) is white for a whole period, so white for
ever; the column to its right then obeys x' = x or (right neighbour), so it never turns white again once black, and
being periodic and white at time 0 it is white for ever; two adjacent white columns force white columns to their
right, up to column 0, which is not zero.

How to check: as for TheoremA.lean; the `#print axioms` line must list no `sorryAx`.
-/

namespace TheoremB

/-- One Rule 30 step (as in TheoremA.lean). -/
def step (x : ℤ → Bool) : ℤ → Bool := fun i => xor (x (i - 1)) (x i || x (i + 1))

/-- The evolution from `x0` (as in TheoremA.lean). -/
def ev (x0 : ℤ → Bool) : ℕ → ℤ → Bool
  | 0 => x0
  | t + 1 => step (ev x0 t)

lemma ev_succ (x0 : ℤ → Bool) (t : ℕ) (i : ℤ) :
    ev x0 (t + 1) i = xor (ev x0 t (i - 1)) (ev x0 t i || ev x0 t (i + 1)) := rfl

/-- Column k is P-periodic for all times. -/
def PerAll (x0 : ℤ → Bool) (k : ℤ) (P : ℕ) : Prop := ∀ t : ℕ, ev x0 t k = ev x0 (t + P) k

/-- Fact 1 on an unbounded window: periodicity moves left. -/
lemma left_all (x0 : ℤ → Bool) (k : ℤ) (P : ℕ) (h0 : PerAll x0 k P) (h1 : PerAll x0 (k + 1) P) :
    PerAll x0 (k - 1) P := by
  intro t
  have inv : ∀ s : ℕ, ev x0 s (k - 1) = xor (ev x0 (s + 1) k) (ev x0 s k || ev x0 s (k + 1)) := by
    intro s
    rw [ev_succ, show k - 1 = k - 1 by rfl]
    cases ev x0 s (k - 1) <;> cases (ev x0 s k || ev x0 s (k + 1)) <;> rfl
  rw [inv t, inv (t + P), h0 (t + 1), h0 t, h1 t, show t + 1 + P = t + P + 1 by ring]

lemma left_all_iter (x0 : ℤ → Bool) (P : ℕ) (h0 : PerAll x0 0 P) (h1 : PerAll x0 1 P) :
    ∀ j : ℕ, PerAll x0 (-(j : ℤ)) P ∧ PerAll x0 (-(j : ℤ) + 1) P := by
  intro j
  induction j with
  | zero => exact ⟨by simpa using h0, by simpa using h1⟩
  | succ j ih =>
    refine ⟨?_, ?_⟩
    · have := left_all x0 (-(j : ℤ)) P ih.1 ih.2
      rwa [show -(j : ℤ) - 1 = -((j + 1 : ℕ) : ℤ) by push_cast; ring] at this
    · rw [show -((j + 1 : ℕ) : ℤ) + 1 = -(j : ℤ) by push_cast; ring]; exact ih.1

/-- A periodic column is determined by its first period. -/
lemma per_mod (x0 : ℤ → Bool) (k : ℤ) (P : ℕ) (h : PerAll x0 k P) : ∀ m t : ℕ, ev x0 (t + m * P) k = ev x0 t k := by
  intro m
  induction m with
  | zero => intro t; simp
  | succ m ih => intro t; rw [show t + (m + 1) * P = (t + m * P) + P by ring, ← h, ih]

/-- The white triangle under a zero run of row 0 at depths d .. d + R - 1. -/
lemma triangle (x0 : ℤ → Bool) (d R : ℕ) (hrun : ∀ i : ℕ, d ≤ i → i < d + R → x0 (-(i : ℤ)) = false) :
    ∀ t i : ℕ, d + t ≤ i → i + t < d + R → ev x0 t (-(i : ℤ)) = false := by
  intro t
  induction t with
  | zero => intro i h1 h2; exact hrun i (by omega) (by omega)
  | succ t ih =>
    intro i h1 h2
    rw [ev_succ]
    have a : ev x0 t (-(i : ℤ) - 1) = false := by
      have := ih (i + 1) (by omega) (by omega)
      rwa [show -((i + 1 : ℕ) : ℤ) = -(i : ℤ) - 1 by push_cast; ring] at this
    have b : ev x0 t (-(i : ℤ)) = false := ih i (by omega) (by omega)
    have c : ev x0 t (-(i : ℤ) + 1) = false := by
      have := ih (i - 1) (by omega) (by omega)
      rwa [show -((i - 1 : ℕ) : ℤ) = -(i : ℤ) + 1 by push_cast [show 1 ≤ i by omega]; ring] at this
    rw [a, b, c]; rfl

/-- With column k - 1 white for ever, column k never turns from black to white. -/
lemma latch (x0 : ℤ → Bool) (k : ℤ) (hz : ∀ t : ℕ, ev x0 t (k - 1) = false) :
    ∀ t : ℕ, ev x0 t k = true → ∀ s : ℕ, ev x0 (t + s) k = true := by
  intro t ht s
  induction s with
  | zero => simpa using ht
  | succ s ih =>
    rw [show t + (s + 1) = (t + s) + 1 by ring, ev_succ, hz (t + s), ih]; rfl

/-- Two adjacent white columns force white to the right. -/
lemma push_right (x0 : ℤ → Bool) (k : ℤ) (ha : ∀ t : ℕ, ev x0 t (k - 1) = false)
    (hb : ∀ t : ℕ, ev x0 t k = false) : ∀ t : ℕ, ev x0 t (k + 1) = false := by
  intro t
  have := hb (t + 1)
  rw [ev_succ, ha t, hb t] at this
  simpa using this

/-- Theorem B. -/
theorem theorem_B (x0 : ℤ → Bool) (P : ℕ) (hP : 2 ≤ P) (h0 : PerAll x0 0 P) (h1 : PerAll x0 1 P)
    (hnz : ∃ t : ℕ, ev x0 t 0 = true) (d R : ℕ) (hd : 1 ≤ d)
    (hrun : ∀ i : ℕ, d ≤ i → i < d + R → x0 (-(i : ℤ)) = false) : R ≤ 2 * P - 2 := by
  by_contra hR
  push Not at hR
  set k : ℕ := d + P - 1 with hk
  have hper := left_all_iter x0 P h0 h1
  -- column -k is white for the first period, hence for ever
  have white_k : ∀ t : ℕ, ev x0 t (-(k : ℤ)) = false := by
    intro t
    have hfirst : ∀ s : ℕ, s < P → ev x0 s (-(k : ℤ)) = false :=
      fun s hs => triangle x0 d R hrun s k (by omega) (by omega)
    have := per_mod x0 _ P (hper k).1 (t / P) (t % P)
    rw [show t % P + t / P * P = t by rw [Nat.mod_add_div' t P]] at this
    rw [this]; exact hfirst _ (Nat.mod_lt _ (by omega))
  -- column -k + 1 is periodic and latched, and white at time 0, so white for ever
  have white_k1 : ∀ t : ℕ, ev x0 t (-(k : ℤ) + 1) = false := by
    intro t
    by_contra hb
    have hb' : ev x0 t (-(k : ℤ) + 1) = true := by simpa using hb
    have hl := latch x0 (-(k : ℤ) + 1) (by intro s; rw [show -(k : ℤ) + 1 - 1 = -(k : ℤ) by ring]; exact white_k s)
      t hb' (t * P - t)
    rw [show t + (t * P - t) = 0 + t * P by
      have : t ≤ t * P := Nat.le_mul_of_pos_right t (by omega)
      omega] at hl
    rw [per_mod x0 _ P (hper k).2 t 0] at hl
    have h0w : ev x0 0 (-(k : ℤ) + 1) = false := by
      have := hrun (k - 1) (by omega) (by omega)
      rwa [show -((k - 1 : ℕ) : ℤ) = -(k : ℤ) + 1 by push_cast [show 1 ≤ k by omega]; ring] at this
    rw [h0w] at hl; exact absurd hl (by decide)
  -- push the two white columns to the right, up to column 0
  have push : ∀ j : ℕ, j ≤ k → (∀ t : ℕ, ev x0 t (-(k : ℤ) + j) = false) ∧
      (∀ t : ℕ, ev x0 t (-(k : ℤ) + j + 1) = false) := by
    intro j
    induction j with
    | zero =>
      intro _
      refine ⟨fun t => ?_, fun t => ?_⟩
      · rw [show -(k : ℤ) + ((0 : ℕ) : ℤ) = -(k : ℤ) by push_cast; ring]; exact white_k t
      · rw [show -(k : ℤ) + ((0 : ℕ) : ℤ) + 1 = -(k : ℤ) + 1 by push_cast; ring]; exact white_k1 t
    | succ j ih =>
      intro hj
      obtain ⟨a, b⟩ := ih (by omega)
      have a' : ∀ t : ℕ, ev x0 t (-(k : ℤ) + (j : ℤ) + 1 - 1) = false := fun t => by
        rw [show -(k : ℤ) + (j : ℤ) + 1 - 1 = -(k : ℤ) + (j : ℤ) by ring]; exact a t
      have c := push_right x0 (-(k : ℤ) + (j : ℤ) + 1) a' b
      refine ⟨fun t => ?_, fun t => ?_⟩
      · rw [show -(k : ℤ) + ((j + 1 : ℕ) : ℤ) = -(k : ℤ) + (j : ℤ) + 1 by push_cast; ring]; exact b t
      · rw [show -(k : ℤ) + ((j + 1 : ℕ) : ℤ) + 1 = -(k : ℤ) + (j : ℤ) + 1 + 1 by push_cast; ring]; exact c t
  obtain ⟨t, ht⟩ := hnz
  have := (push k le_rfl).1 t
  rw [show -(k : ℤ) + (k : ℤ) = 0 by ring] at this
  rw [this] at ht; exact absurd ht (by decide)

end TheoremB

#print axioms TheoremB.theorem_B
