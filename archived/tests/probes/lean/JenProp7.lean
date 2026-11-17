import Mathlib

/-!
# Proposition 7 (Jen; PROOFS.md entry 17), machine-checked (Local, 2026-10-10)

Rule 30 on configurations ℤ → Bool. If column 0 is eventually periodic and not eventually zero, and column 1 is
eventually periodic (with any periods), then the left half is never eventually zero: no configuration with a left
bound (white left of some cell) and a black cell has columns 0 and 1 both eventually periodic with column 0 not
eventually white. The proof is Theorem A's corollary with the common period P0 * P1 (TheoremA.lean).

How to check: as for TheoremA.lean; the `#print axioms` line must list no `sorryAx`.
-/

namespace JenProp7

def step (x : ℤ → Bool) : ℤ → Bool := fun i => xor (x (i - 1)) (x i || x (i + 1))

def ev (x0 : ℤ → Bool) : ℕ → ℤ → Bool
  | 0 => x0
  | t + 1 => step (ev x0 t)

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

def Per (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) : Prop :=
  ∀ t : ℕ, a ≤ t → t + P ≤ b → ev x0 t k = ev x0 (t + P) k

lemma left (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 k P a b) (h1 : Per x0 (k + 1) P a b) :
    Per x0 (k - 1) P a (b - 1) := by
  intro t ht htb
  have inv : ∀ s : ℕ, ev x0 s (k - 1) = xor (ev x0 (s + 1) k) (ev x0 s k || ev x0 s (k + 1)) := by
    intro s
    show ev x0 s (k - 1) = xor (xor (ev x0 s (k - 1)) (ev x0 s k || ev x0 s (k + 1))) (ev x0 s k || ev x0 s (k + 1))
    cases ev x0 s (k - 1) <;> cases (ev x0 s k || ev x0 s (k + 1)) <;> rfl
  rw [inv t, inv (t + P)]
  have e1 : ev x0 (t + 1) k = ev x0 (t + 1 + P) k := h0 (t + 1) (by omega) (by omega)
  have e2 : ev x0 t k = ev x0 (t + P) k := h0 t ht (by omega)
  have e3 : ev x0 t (k + 1) = ev x0 (t + P) (k + 1) := h1 t ht (by omega)
  rw [e1, e2, e3, show t + 1 + P = t + P + 1 by ring]

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

theorem theorem_A (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false)
    (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 c P a b) (h1 : Per x0 (c + 1) P a b) :
    b ≤ 2 * a + L + 2 * P - 1 := by
  by_contra hb
  push Not at hb
  set j : ℕ := a + P + L with hj
  have hper := (left_iter x0 c P a b hP h0 h1 j).1
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

theorem no_two_periodic (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false)
    (P a : ℕ) (hP : 1 ≤ P)
    (h0 : ∀ t : ℕ, a ≤ t → ev x0 t c = ev x0 (t + P) c)
    (h1 : ∀ t : ℕ, a ≤ t → ev x0 t (c + 1) = ev x0 (t + P) (c + 1)) : False := by
  have := theorem_A x0 c L hc hl P a (2 * a + L + 2 * P) hP (fun t ht _ => h0 t ht) (fun t ht _ => h1 t ht)
  omega

/-- Periodicity with period P from time a gives periodicity with any multiple of P. -/
lemma per_mul (x0 : ℤ → Bool) (k : ℤ) (P a : ℕ) (h : ∀ t, a ≤ t → ev x0 t k = ev x0 (t + P) k) :
    ∀ m t, a ≤ t → ev x0 t k = ev x0 (t + m * P) k := by
  intro m
  induction m with
  | zero => intro t _; simp
  | succ m ih =>
    intro t ht
    rw [ih t ht, show t + (m + 1) * P = (t + m * P) + P by ring, h (t + m * P) (by omega)]

/-- Proposition 7 (Jen). -/
theorem jen (x0 : ℤ → Bool) (M : ℤ) (hM : ∀ j < M, x0 j = false) (P0 P1 a0 a1 : ℕ) (hP0 : 1 ≤ P0) (hP1 : 1 ≤ P1)
    (h0 : ∀ t, a0 ≤ t → ev x0 t 0 = ev x0 (t + P0) 0) (h1 : ∀ t, a1 ≤ t → ev x0 t 1 = ev x0 (t + P1) 1)
    (hnz : ∀ T, ∃ t, T ≤ t ∧ ev x0 t 0 = true) : False := by
  -- a black cell exists (column 0 is black at some time, so the configuration is not all white)
  have hex : ∃ j, x0 j = true := by
    by_contra hz
    push Not at hz
    obtain ⟨t, _, ht⟩ := hnz 0
    have hzero : ∀ s : ℕ, ∀ j, ev x0 s j = false := by
      intro s
      induction s with
      | zero => intro j; show x0 j = false; simpa using hz j
      | succ s ih => intro j; show xor _ (_ || _) = false; rw [ih, ih, ih]; rfl
    rw [hzero] at ht; exact absurd ht (by decide)
  obtain ⟨e, he, hmin⟩ := Int.exists_least_of_bdd (P := fun j => x0 j = true)
    ⟨M, fun z hz => by by_contra h; push Not at h; rw [hM z h] at hz; exact absurd hz (by decide)⟩ hex
  have hl : ∀ j < e, x0 j = false := fun j hj => by
    by_contra h
    have := hmin j (by simpa using h)
    omega
  -- re-base time so that the edge is at or left of column 0
  set k : ℕ := e.toNat with hk
  have E := edge x0 e he hl k
  have ev_add : ∀ s, ev (ev x0 k) s = ev x0 (k + s) := by
    intro s
    induction s with
    | zero => rfl
    | succ s ih => show step (ev (ev x0 k) s) = step (ev x0 (k + s)); rw [ih]
  set y0 := ev x0 k
  have hy : y0 (e - k) = true := E.1
  have hyl : ∀ j < e - k, y0 j = false := E.2
  have hle : e - (k : ℤ) ≤ 0 := by rw [hk]; omega
  set L : ℕ := (k - e).toNat with hL
  have hc : y0 (0 - L) = true := by rw [show (0 : ℤ) - L = e - k by rw [hL]; omega]; exact hy
  have hcl : ∀ j < 0 - (L : ℤ), y0 j = false := by
    intro j hj; exact hyl j (by rw [hL] at hj; omega)
  apply no_two_periodic y0 0 L hc hcl (P0 * P1) (a0 + a1) (Nat.mul_pos hP0 hP1)
  · intro t ht
    rw [ev_add, ev_add, show k + (t + P0 * P1) = (k + t) + P1 * P0 by ring]
    exact per_mul x0 0 P0 a0 h0 P1 (k + t) (by omega)
  · intro t ht
    rw [show (0 : ℤ) + 1 = 1 by ring, ev_add, ev_add, show k + (t + P0 * P1) = (k + t) + P0 * P1 by ring]
    exact per_mul x0 1 P1 a1 h1 P0 (k + t) (by omega)

end JenProp7

#print axioms JenProp7.jen
