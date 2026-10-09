import FormalConjectures.Other.Rule30

/-!
# Period 1 for Rule 30's single seed (Local's formalization, 2026-10-09)

Against Google DeepMind's `FormalConjectures/Other/Rule30.lean` definitions (`step`, `state`, `centerColumn`):
the center column is not eventually constant, i.e. Problem 1 holds for period 1. This is the single-seed case of
Condrey's theorem (PROOFS.md entry 37 in the placego record), by a route that avoids the leftmost-black-cell walk:
an eventually constant column 0 that is never white together with column 1 forces a checkerboard left half, which
finite support forbids; the white-wall case reaches that situation through the latch, or else every column to the
right of the wall stays white, which the right edge forbids.

How to check (Local, 2026-10-09; Lean 4 v4.33.1 via elan; google-deepmind/formal-conjectures at b3f2641 with its
Mathlib cache): copy this file into that checkout (here, `LocalScratch/Rule30Period1.lean`) and run
`lake env lean LocalScratch/Rule30Period1.lean`. It compiles with no errors or warnings, and the two `#print axioms`
lines at the end report only `propext`, `Classical.choice` and `Quot.sound` (no `sorryAx`).
-/

namespace Rule30Local

open Rule30

lemma state_succ_apply (t : ℕ) (i : ℤ) :
    state (t + 1) i = xor (state t (i - 1)) (state t i || state t (i + 1)) := rfl

/-- Rule 30 read for its left input (left permutivity). -/
lemma state_inv (t : ℕ) (i : ℤ) :
    state t (i - 1) = xor (state (t + 1) i) (state t i || state t (i + 1)) := by
  rw [state_succ_apply]
  generalize state t (i - 1) = a
  generalize (state t i || state t (i + 1)) = b
  cases a <;> cases b <;> rfl

/-- Nothing is black to the right of the light cone. -/
lemma support_right : ∀ (t : ℕ) (i : ℤ), (t : ℤ) < i → state t i = false := by
  intro t
  induction t with
  | zero =>
    intro i hi
    simp only [state_zero, decide_eq_false_iff_not]
    push_cast at hi
    omega
  | succ n ih =>
    intro i hi
    push_cast at hi
    rw [state_succ_apply, ih (i - 1) (by omega), ih i (by omega), ih (i + 1) (by omega)]
    rfl

/-- Nothing is black to the left of the light cone. -/
lemma support_left : ∀ (t : ℕ) (i : ℤ), i < -(t : ℤ) → state t i = false := by
  intro t
  induction t with
  | zero =>
    intro i hi
    simp only [state_zero, decide_eq_false_iff_not]
    push_cast at hi
    omega
  | succ n ih =>
    intro i hi
    push_cast at hi
    rw [state_succ_apply, ih (i - 1) (by omega), ih i (by omega), ih (i + 1) (by omega)]
    rfl

/-- The right edge of the light cone is black at every time. -/
lemma right_edge : ∀ t : ℕ, state t (t : ℤ) = true := by
  intro t
  induction t with
  | zero => simp [state_zero]
  | succ n ih =>
    rw [state_succ_apply]
    have e1 : ((n + 1 : ℕ) : ℤ) - 1 = (n : ℤ) := by push_cast; ring
    rw [e1, ih, support_right n _ (by push_cast; omega), support_right n _ (by push_cast; omega)]
    rfl

/-- If column 0 is constant `c0` from time `T` on and columns 0 and 1 are never both white, the left half is the
checkerboard `c0 xor (d odd)` at every depth `d`, at every time from `T` on. -/
lemma checkerboard (T : ℕ) (c0 : Bool) (h0 : ∀ t, T ≤ t → state t 0 = c0)
    (h01 : ∀ t, T ≤ t → (state t 0 || state t 1) = true) :
    ∀ d : ℕ, ∀ t, T ≤ t → state t (-(d : ℤ)) = xor c0 (d % 2 == 1) ∧
      state t (-((d + 1 : ℕ) : ℤ)) = xor c0 ((d + 1) % 2 == 1) := by
  intro d
  induction d with
  | zero =>
    intro t ht
    refine ⟨by simpa using h0 t ht, ?_⟩
    have := state_inv t 0
    simp only [zero_sub] at this
    have e : (-((0 + 1 : ℕ) : ℤ)) = -1 := by norm_num
    rw [e, this, h0 (t + 1) (by omega), show (0 : ℤ) + 1 = 1 by norm_num, h01 t ht]
    cases c0 <;> rfl
  | succ n ih =>
    intro t ht
    refine ⟨(ih t ht).2, ?_⟩
    have hinv := state_inv t (-((n + 1 : ℕ) : ℤ))
    have e1 : -((n + 1 : ℕ) : ℤ) - 1 = -((n + 1 + 1 : ℕ) : ℤ) := by push_cast; ring
    have e2 : -((n + 1 : ℕ) : ℤ) + 1 = -(n : ℤ) := by push_cast; ring
    rw [e1] at hinv
    rw [hinv, (ih (t + 1) (by omega)).2, (ih t ht).2, e2, (ih t ht).1]
    have hpar : ((n + 1) % 2 == 1) = !(n % 2 == 1) := by
      rcases Nat.mod_two_eq_zero_or_one n with h | h <;> simp [h, Nat.add_mod]
    have hpar2 : ((n + 1 + 1) % 2 == 1) = (n % 2 == 1) := by
      rcases Nat.mod_two_eq_zero_or_one n with h | h <;> simp [h, Nat.add_mod]
    rw [hpar2, hpar]
    cases c0 <;> cases (n % 2 == 1) <;> rfl

/-- A checkerboard left half contradicts finite support. -/
lemma no_checkerboard (T : ℕ) (c0 : Bool) (h0 : ∀ t, T ≤ t → state t 0 = c0)
    (h01 : ∀ t, T ≤ t → (state t 0 || state t 1) = true) : False := by
  have hc := checkerboard T c0 h0 h01
  cases c0 with
  | true =>
    have h := (hc (2 * T + 2) T le_rfl).1
    rw [support_left T _ (by push_cast; omega)] at h
    have : (2 * T + 2) % 2 = 0 := by omega
    simp [this] at h
  | false =>
    have h := (hc (2 * T + 1) T le_rfl).1
    rw [support_left T _ (by push_cast; omega)] at h
    have : (2 * T + 1) % 2 = 1 := by omega
    simp [this] at h

/-- **Period 1 (the single seed).** The center column of Rule 30 is not eventually constant. -/
theorem centerColumn_not_eventually_constant :
    ¬ ∃ N : ℕ, ∃ c : Bool, ∀ t, N ≤ t → centerColumn t = c := by
  rintro ⟨N, c, hN⟩
  have h0 : ∀ t, N ≤ t → state t 0 = c := hN
  cases c with
  | true => exact no_checkerboard N true h0 (fun t ht => by simp [h0 t ht])
  | false =>
    by_cases hex : ∃ t1, N ≤ t1 ∧ state t1 1 = true
    · obtain ⟨t1, ht1, h1⟩ := hex
      -- the latch: with column 0 white, column 1 never turns white again
      have latch : ∀ k : ℕ, state (t1 + k) 1 = true := by
        intro k
        induction k with
        | zero => simpa using h1
        | succ k ih =>
          rw [show t1 + (k + 1) = (t1 + k) + 1 by omega, state_succ_apply,
            show (1 : ℤ) - 1 = 0 by norm_num, h0 (t1 + k) (by omega), ih]
          rfl
      refine no_checkerboard t1 false (fun t ht => h0 t (by omega)) (fun t ht => ?_)
      obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le ht
      simp [latch k]
    · push Not at hex
      have hw1 : ∀ t, N ≤ t → state t 1 = false := by
        intro t ht
        cases h : state t 1 with
        | false => rfl
        | true => exact absurd h (hex t ht)
      -- every column to the right of the wall stays white
      have white : ∀ j : ℕ, ∀ t, N ≤ t → state t (j : ℤ) = false ∧ state t ((j + 1 : ℕ) : ℤ) = false := by
        intro j
        induction j with
        | zero => intro t ht; exact ⟨by simpa using h0 t ht, by simpa using hw1 t ht⟩
        | succ m ih =>
          intro t ht
          refine ⟨(ih t ht).2, ?_⟩
          have hs := state_succ_apply t ((m + 1 : ℕ) : ℤ)
          have e1 : ((m + 1 : ℕ) : ℤ) - 1 = (m : ℤ) := by push_cast; ring
          have e2 : ((m + 1 : ℕ) : ℤ) + 1 = ((m + 1 + 1 : ℕ) : ℤ) := by push_cast; ring
          rw [e1, e2, (ih t ht).1, (ih t ht).2, (ih (t + 1) (by omega)).2] at hs
          cases h : state t ((m + 1 + 1 : ℕ) : ℤ) with
          | false => rfl
          | true => rw [h] at hs; simp at hs
      have := (white N N le_rfl).1
      rw [right_edge N] at this
      exact Bool.noConfusion this

/-- The period-1 instance of Problem 1, in `Rule30.lean`'s own form. -/
theorem centerColumn_not_eventually_period_one :
    ¬ ∃ N : ℕ, ∀ t : ℕ, N ≤ t → centerColumn (t + 1) = centerColumn t := by
  rintro ⟨N, hN⟩
  apply centerColumn_not_eventually_constant
  refine ⟨N, centerColumn N, fun t ht => ?_⟩
  induction t, ht using Nat.le_induction with
  | base => rfl
  | succ n hn ih => rw [hN n hn, ih]

end Rule30Local

#print axioms Rule30Local.centerColumn_not_eventually_constant
#print axioms Rule30Local.centerColumn_not_eventually_period_one
