import Mathlib

/-!
# Theorem A (PROOFS.md entry 5, Jen's theorem with a clock), machine-checked (Local, 2026-10-09)

Rule 30 on configurations ℤ → Bool: x'(i) = x(i - 1) xor (x(i) or x(i + 1)).
Theorem A: if the leftmost black cell at time 0 is L cells left of column c, and columns c and c + 1 are P-periodic on
the time window [a, b], then b ≤ 2a + L + 2P - 1. Corollary: two adjacent columns that are P-periodic from some time on
(P ≥ 1) are impossible in a configuration with a leftmost black cell; this is the finish of entries 38 and 40.

How to check: as for RootedReturn.lean; the `#print axioms` lines must list no `sorryAx`.
-/

namespace TheoremA

/-- One Rule 30 step. -/
def step (x : ℤ → Bool) : ℤ → Bool := fun i => xor (x (i - 1)) (x i || x (i + 1))

/-- The evolution from `x0`. -/
def ev (x0 : ℤ → Bool) : ℕ → ℤ → Bool
  | 0 => x0
  | t + 1 => step (ev x0 t)

/-- Fact 2: the leftmost black cell moves left one cell a step. -/
lemma edge (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (t : ℕ) :
    ev x0 t (e - t) = true ∧ ∀ j < e - t, ev x0 t j = false := by
  induction t with
  | zero => simpa using ⟨he, hl⟩
  | succ t ih =>
    obtain ⟨h1, h2⟩ := ih
    constructor
    · show xor (ev x0 t (e - ↑(t + 1) - 1)) (ev x0 t (e - ↑(t + 1)) || ev x0 t (e - ↑(t + 1) + 1)) = true
      have a1 : ev x0 t (e - ↑(t + 1) - 1) = false := h2 _ (by push_cast; omega)
      have a2 : ev x0 t (e - ↑(t + 1)) = false := h2 _ (by push_cast; omega)
      have a3 : e - ↑(t + 1) + 1 = e - ↑t := by push_cast; ring
      rw [a1, a2, a3, h1]; rfl
    · intro j hj
      show xor (ev x0 t (j - 1)) (ev x0 t j || ev x0 t (j + 1)) = false
      have b1 : ev x0 t (j - 1) = false := h2 _ (by push_cast at hj; omega)
      have b2 : ev x0 t j = false := h2 _ (by push_cast at hj; omega)
      have b3 : ev x0 t (j + 1) = false := h2 _ (by push_cast at hj; omega)
      rw [b1, b2, b3]; rfl

/-- Column `k` is `P`-periodic on the window `[a, b]`. -/
def Per (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) : Prop :=
  ∀ t : ℕ, a ≤ t → t + P ≤ b → ev x0 t k = ev x0 (t + P) k

/-- Fact 1: periodicity of columns k and k + 1 moves left to column k - 1, losing one step. -/
lemma left (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 k P a b) (h1 : Per x0 (k + 1) P a b) :
    Per x0 (k - 1) P a (b - 1) := by
  intro t ht htb
  -- x_t(k - 1) = x_(t+1)(k) xor (x_t(k) or x_t(k + 1))
  have inv : ∀ s : ℕ, ev x0 s (k - 1) = xor (ev x0 (s + 1) k) (ev x0 s k || ev x0 s (k + 1)) := by
    intro s
    show ev x0 s (k - 1) = xor (xor (ev x0 s (k - 1)) (ev x0 s k || ev x0 s (k + 1))) (ev x0 s k || ev x0 s (k + 1))
    cases ev x0 s (k - 1) <;> cases (ev x0 s k || ev x0 s (k + 1)) <;> rfl
  rw [inv t, inv (t + P)]
  have e1 : ev x0 (t + 1) k = ev x0 (t + 1 + P) k := h0 (t + 1) (by omega) (by omega)
  have e2 : ev x0 t k = ev x0 (t + P) k := h0 t ht (by omega)
  have e3 : ev x0 t (k + 1) = ev x0 (t + P) (k + 1) := h1 t ht (by omega)
  rw [e1, e2, e3, show t + 1 + P = t + P + 1 by ring]

/-- Iterated: columns k - j and k - j + 1 are P-periodic on [a, b - j]. -/
lemma left_iter (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 k P a b) (h1 : Per x0 (k + 1) P a b) :
    ∀ j : ℕ, Per x0 (k - j) P a (b - j) ∧ Per x0 (k - j + 1) P a (b - j) := by
  intro j
  induction j with
  | zero => simpa using ⟨h0, h1⟩
  | succ j ih =>
    obtain ⟨g0, g1⟩ := ih
    have g := left x0 (k - j) P a (b - j) hP g0 (by simpa using g1)
    refine ⟨?_, ?_⟩
    · have : (k - ↑(j + 1)) = k - ↑j - 1 := by push_cast; ring
      rw [this, show b - (j + 1) = b - j - 1 by omega]; exact g
    · have e : (k - ↑(j + 1) + 1) = k - ↑j := by push_cast; ring
      rw [e, show b - (j + 1) = b - j - 1 by omega]
      intro t ht htb
      exact g0 t ht (by omega)

/-- Theorem A. -/
theorem theorem_A (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false)
    (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 c P a b) (h1 : Per x0 (c + 1) P a b) :
    b ≤ 2 * a + L + 2 * P - 1 := by
  by_contra hb
  push Not at hb
  -- go j = a + P + L columns left
  set j : ℕ := a + P + L with hj
  have hper := (left_iter x0 c P a b hP h0 h1 j).1
  -- the edge reaches column c - j at time a + P (black there); at time a it is P cells right of c - j (white there)
  have E := edge x0 (c - L) hc hl
  have black : ev x0 (a + P) (c - j) = true := by
    have := (E (a + P)).1
    have e : c - ↑L - ↑(a + P) = c - ↑j := by rw [hj]; push_cast; ring
    rwa [e] at this
  have white : ev x0 a (c - j) = false := by
    have := (E a).2 (c - j) (by rw [hj]; push_cast; omega)
    exact this
  have := hper a le_rfl (by omega)
  rw [white, black] at this
  exact absurd this (by decide)

/-- Corollary: no configuration with a leftmost black cell has two adjacent columns P-periodic from time a on. -/
theorem no_two_periodic (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false)
    (P a : ℕ) (hP : 1 ≤ P)
    (h0 : ∀ t : ℕ, a ≤ t → ev x0 t c = ev x0 (t + P) c)
    (h1 : ∀ t : ℕ, a ≤ t → ev x0 t (c + 1) = ev x0 (t + P) (c + 1)) : False := by
  have := theorem_A x0 c L hc hl P a (2 * a + L + 2 * P) hP (fun t ht _ => h0 t ht) (fun t ht _ => h1 t ht)
  omega

end TheoremA

#print axioms TheoremA.theorem_A
#print axioms TheoremA.no_two_periodic
