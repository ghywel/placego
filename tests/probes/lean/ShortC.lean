import Mathlib

/-!
# PROOFS.md short proofs C.1, C.2, C.3, machine-checked (Local, 2026-10-10)

Rule 30 on configurations ℤ → Bool: x'(i) = x(i - 1) xor (x(i) or x(i + 1)).
- C.2 (the latch): if column 0 is white at time t, then x_(t+1)(1) = x_t(1) or x_t(2).
- C.3 (the shrink theorem): a white run [a, b] with b ≥ a + 1, bounded by black cells, becomes exactly the white run
  [a + 1, b - 1], bounded by the black cells a and b, one step later.
- C.1 (the checkerboard lemma): if column 0 is black at times t .. t + k, then x(-j, t) = (j + 1) mod 2 for
  1 ≤ j ≤ k, whatever the right half.

How to check: as for TheoremA.lean; the `#print axioms` lines must list no `sorryAx`.
-/

namespace ShortC

def step (x : ℤ → Bool) : ℤ → Bool := fun i => xor (x (i - 1)) (x i || x (i + 1))

def ev (x0 : ℤ → Bool) : ℕ → ℤ → Bool
  | 0 => x0
  | t + 1 => step (ev x0 t)

lemma ev_succ (x0 : ℤ → Bool) (t : ℕ) (i : ℤ) :
    ev x0 (t + 1) i = xor (ev x0 t (i - 1)) (ev x0 t i || ev x0 t (i + 1)) := rfl

/-- C.2, the latch. -/
theorem latch (x0 : ℤ → Bool) (t : ℕ) (h : ev x0 t 0 = false) : ev x0 (t + 1) 1 = (ev x0 t 1 || ev x0 t 2) := by
  rw [ev_succ, show (1 : ℤ) - 1 = 0 by ring, h, show (1 : ℤ) + 1 = 2 by ring]; simp

/-- C.3, the shrink theorem: one step of a bounded white run. -/
theorem shrink (x : ℤ → Bool) (a b : ℤ) (hab : a + 1 ≤ b) (hl : x (a - 1) = true) (hr : x (b + 1) = true)
    (hw : ∀ i, a ≤ i → i ≤ b → x i = false) :
    step x a = true ∧ step x b = true ∧ ∀ i, a + 1 ≤ i → i ≤ b - 1 → step x i = false := by
  refine ⟨?_, ?_, ?_⟩
  · show xor (x (a - 1)) (x a || x (a + 1)) = true
    rw [hl, hw a le_rfl (by omega), hw (a + 1) (by omega) (by omega)]; rfl
  · show xor (x (b - 1)) (x b || x (b + 1)) = true
    rw [hw (b - 1) (by omega) (by omega), hw b (by omega) le_rfl, hr]; rfl
  · intro i h1 h2
    show xor (x (i - 1)) (x i || x (i + 1)) = false
    rw [hw (i - 1) (by omega) (by omega), hw i (by omega) (by omega), hw (i + 1) (by omega) (by omega)]; rfl

/-- C.1, the checkerboard lemma (read with the inverse rule): column 0 black at times t .. t + k forces
x(-j, t') = (j + 1) mod 2 at every time t' with column 0 black at t' .. t' + (k - j + 1). -/
theorem checkerboard (x0 : ℤ → Bool) :
    ∀ j : ℕ, 1 ≤ j → ∀ t k : ℕ, j ≤ k → (∀ s, s ≤ k → ev x0 (t + s) 0 = true) →
      ev x0 t (-(j : ℤ)) = decide (j % 2 = 1 → False) := by
  -- inverse rule: x_t(m - 1) = x_(t+1)(m) xor (x_t(m) or x_t(m + 1))
  have inv : ∀ (t : ℕ) (m : ℤ), ev x0 t (m - 1) = xor (ev x0 (t + 1) m) (ev x0 t m || ev x0 t (m + 1)) := by
    intro t m
    rw [ev_succ]
    cases ev x0 t (m - 1) <;> cases (ev x0 t m || ev x0 t (m + 1)) <;> rfl
  intro j
  induction j using Nat.strong_induction_on with
  | _ j ih =>
    intro hj t k hjk hb
    rcases Nat.lt_or_ge j 2 with h | h
    · -- j = 1: x(-1, t) = x(0, t+1) xor (x(0, t) or x(1, t)) = 1 xor 1 = 0
      have hj1 : j = 1 := by omega
      subst hj1
      have := inv t 0
      rw [show (0 : ℤ) - 1 = -((1 : ℕ) : ℤ) by norm_num] at this
      rw [this, show t + 1 = t + 1 by rfl]
      have e1 : ev x0 (t + 1) 0 = true := hb 1 (by omega)
      have e0 : ev x0 t 0 = true := by simpa using hb 0 (by omega)
      rw [e1, e0]; simp
    · -- j ≥ 2: from j - 1 at times t and t + 1, and j - 2 (or column 0) at time t
      have hA : ev x0 (t + 1) (-((j - 1 : ℕ) : ℤ)) = decide ((j - 1) % 2 = 1 → False) :=
        ih (j - 1) (by omega) (by omega) (t + 1) (k - 1) (by omega)
          (fun s hs => by rw [show t + 1 + s = t + (s + 1) by ring]; exact hb (s + 1) (by omega))
      have hB : ev x0 t (-((j - 1 : ℕ) : ℤ)) = decide ((j - 1) % 2 = 1 → False) :=
        ih (j - 1) (by omega) (by omega) t k (by omega) hb
      have hC : ev x0 t (-((j - 1 : ℕ) : ℤ) + 1) = decide (j % 2 = 0) := by
        rcases Nat.lt_or_ge j 3 with h3 | h3
        · have : j = 2 := by omega
          subst this
          simpa using hb 0 (by omega)
        · rw [show -((j - 1 : ℕ) : ℤ) + 1 = -((j - 2 : ℕ) : ℤ) by omega,
            ih (j - 2) (by omega) (by omega) t k (by omega) hb]
          rcases Nat.mod_two_eq_zero_or_one j with hp | hp <;> simp [hp] <;> omega
      have := inv t (-((j - 1 : ℕ) : ℤ))
      rw [show -((j - 1 : ℕ) : ℤ) - 1 = -(j : ℤ) by push_cast [show 1 ≤ j by omega]; ring] at this
      rw [this, hA, hB, hC]
      rcases Nat.mod_two_eq_zero_or_one j with hp | hp
      · have : (j - 1) % 2 = 1 := by omega
        simp [hp, this]
      · have : (j - 1) % 2 = 0 := by omega
        simp [hp, this]

end ShortC

#print axioms ShortC.latch
#print axioms ShortC.shrink
#print axioms ShortC.checkerboard
