import Mathlib

/-!
# The left diagonals' periods are powers of 2 (Local, 2026-10-10)

Rule 30 on configurations ℤ → Bool with a leftmost black cell e at time 0; diagonal k at time t is the cell e - t + k
(as in LemmaB1.lean). The record credits this to Jen (1986, Theorem 4) and Rowland (§5); this file proves it.

`jen_pow2`: for every j there is a time T after which every diagonal k ≤ j + 2 has period 2^j.

The proof. D_0 is black, D_1 is black from t = 1 and D_2 white from t = 2, so every k ≤ 2 has period 1 from t = 2.
Diagonal k obeys x(t + 1) = a(t) xor (b(t) or x(t)) with a = D_(k-2), b = D_(k-1). If a and b have period p from T,
two of the bits x(T), x(T + p), x(T + 2p) are equal, and equal states with equal inputs have equal futures; in each
case x(T + 3p) = x(T + p), so x has period 2p from T + p (`forced_periodic`).

`run_bound` combines it with Lemma B3's sharp form (`lemma_B3_sharp`, LemmaB3.lean, repeated here): from some time on,
every white run [g + 1, M'] in the diagonals up to j + 2, bounded by a black diagonal g, has M' - g ≤ 2^(j+1) - 1.

How to check: as for TheoremA.lean; the `#print axioms` lines must list no `sorryAx`.
-/

set_option Elab.async false

namespace JenPow2

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

/-- Diagonal k at time t. -/
def D (x0 : ℤ → Bool) (e : ℤ) (k : ℤ) (t : ℕ) : Bool := ev x0 t (e - t + k)

lemma D_succ (x0 : ℤ → Bool) (e j : ℤ) (t : ℕ) :
    D x0 e j (t + 1) = xor (D x0 e (j - 2) t) (D x0 e (j - 1) t || D x0 e j t) := by
  unfold D
  rw [ev_succ]
  rw [show e - ((t + 1 : ℕ) : ℤ) + j - 1 = e - t + (j - 2) by push_cast; ring,
    show e - ((t + 1 : ℕ) : ℤ) + j = e - t + (j - 1) by push_cast; ring,
    show e - (t : ℤ) + (j - 1) + 1 = e - t + j by ring]

/-! ### One bit forced by periodic inputs -/

section forced
variable (a b x : ℕ → Bool) (T p : ℕ) (ha : ∀ t, T ≤ t → a (t + p) = a t) (hb : ∀ t, T ≤ t → b (t + p) = b t)
  (hx : ∀ t, x (t + 1) = xor (a t) (b t || x t))

include ha in
lemma per_iter : ∀ m t, T ≤ t → a (t + m * p) = a t := by
  intro m
  induction m with
  | zero => intro t _; simp
  | succ m ih =>
    intro t ht
    rw [show t + (m + 1) * p = (t + m * p) + p by ring, ha _ (le_trans ht (Nat.le_add_right _ _)), ih t ht]

include ha hb hx in
/-- Equal states with equal (periodic) inputs have equal futures. -/
lemma det (m : ℕ) (s : ℕ) (hs : T ≤ s) (h0 : x s = x (s + m * p)) : ∀ k, x (s + k) = x (s + m * p + k) := by
  intro k
  induction k with
  | zero => simpa using h0
  | succ k ih =>
    rw [show s + (k + 1) = (s + k) + 1 by ring, show s + m * p + (k + 1) = (s + m * p + k) + 1 by ring, hx, hx,
      ← ih, show s + m * p + k = (s + k) + m * p by ring, per_iter a T p ha m (s + k) (by omega),
      per_iter b T p hb m (s + k) (by omega)]

lemma pigeon (u v w : Bool) : u = v ∨ u = w ∨ v = w := by
  cases u <;> cases v <;> cases w <;> simp

include ha hb hx in
/-- Period 2p from T + p. -/
lemma forced_periodic : ∀ t, T + p ≤ t → x (t + 2 * p) = x t := by
  have key : x (T + p) = x (T + p + 2 * p) := by
    rcases pigeon (x T) (x (T + p)) (x (T + 2 * p)) with h | h | h
    · -- x T = x (T + p)
      have d := det a b x T p ha hb hx 1 T le_rfl (by simpa using h)
      have e1 := d p
      have e2 := d (2 * p)
      rw [show T + 1 * p + p = T + 2 * p by ring] at e1
      rw [show T + 1 * p + 2 * p = T + p + 2 * p by ring] at e2
      rw [e1, e2]
    · -- x T = x (T + 2p)
      have d := det a b x T p ha hb hx 2 T le_rfl (by simpa using h)
      have e1 := d p
      rw [show T + 2 * p + p = T + p + 2 * p by ring] at e1
      exact e1
    · -- x (T + p) = x (T + 2p)
      have d := det a b x T p ha hb hx 1 (T + p) (Nat.le_add_right _ _) (by
        rw [show T + p + 1 * p = T + 2 * p by ring]; exact h)
      have e1 := d p
      rw [show T + p + p = T + 2 * p by ring, show T + p + 1 * p + p = T + p + 2 * p by ring] at e1
      rw [h, e1]
  have d := det a b x T p ha hb hx 2 (T + p) (Nat.le_add_right _ _) key
  intro t ht
  have := d (t - (T + p))
  rw [show T + p + (t - (T + p)) = t by omega, show T + p + 2 * p + (t - (T + p)) = t + 2 * p by omega] at this
  exact this.symm

end forced

/-! ### The diagonals -/

section diagonals
variable (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false)
include he hl

lemma D0 (t : ℕ) : D x0 e 0 t = true := by
  unfold D; simpa using (edge x0 e he hl t).1

lemma Dneg (k : ℤ) (hk : k < 0) (t : ℕ) : D x0 e k t = false := by
  unfold D; exact (edge x0 e he hl t).2 _ (by omega)

lemma D1 (t : ℕ) (ht : 1 ≤ t) : D x0 e 1 t = true := by
  obtain ⟨s, rfl⟩ : ∃ s, t = s + 1 := ⟨t - 1, by omega⟩
  rw [D_succ, Dneg x0 e he hl _ (by norm_num), show (1 : ℤ) - 1 = 0 by norm_num, D0 x0 e he hl]; rfl

lemma D2 (t : ℕ) (ht : 2 ≤ t) : D x0 e 2 t = false := by
  obtain ⟨s, rfl⟩ : ∃ s, t = s + 1 := ⟨t - 1, by omega⟩
  rw [D_succ, show (2 : ℤ) - 2 = 0 by norm_num, show (2 : ℤ) - 1 = 1 by norm_num, D0 x0 e he hl,
    D1 x0 e he hl s (by omega)]; rfl

/-- The left diagonals' periods: every diagonal k ≤ j + 2 has period 2^j from some time on. -/
theorem jen_pow2 : ∀ j : ℕ, ∃ T : ℕ, ∀ k : ℤ, k ≤ j + 2 → ∀ t, T ≤ t → D x0 e k (t + 2 ^ j) = D x0 e k t := by
  intro j
  induction j with
  | zero =>
    refine ⟨2, fun k hk t ht => ?_⟩
    simp only [pow_zero]
    rcases (show k < 0 ∨ k = 0 ∨ k = 1 ∨ k = 2 by push_cast at hk; omega) with h | h | h | h
    · rw [Dneg x0 e he hl k h, Dneg x0 e he hl k h]
    · subst h; rw [D0 x0 e he hl, D0 x0 e he hl]
    · subst h; rw [D1 x0 e he hl _ (by omega), D1 x0 e he hl _ (by omega)]
    · subst h; rw [D2 x0 e he hl _ (by omega), D2 x0 e he hl _ (by omega)]
  | succ j ih =>
    obtain ⟨T, hT⟩ := ih
    have hp : 1 ≤ 2 ^ j := Nat.one_le_two_pow
    refine ⟨T + 2 ^ j, fun k hk t ht => ?_⟩
    rw [pow_succ]
    rcases (show k ≤ (j : ℤ) + 2 ∨ k = (j : ℤ) + 3 by push_cast at hk; omega) with h | h
    · -- already periodic with 2^j, hence with 2 · 2^j
      rw [show t + 2 ^ j * 2 = (t + 2 ^ j) + 2 ^ j by ring, hT k h (t + 2 ^ j) (by omega), hT k h t (by omega)]
    · -- the new diagonal, forced by two periodic ones
      have F := forced_periodic (fun t => D x0 e (k - 2) t) (fun t => D x0 e (k - 1) t) (fun t => D x0 e k t)
        T (2 ^ j) (fun t ht => hT (k - 2) (by omega) t ht) (fun t ht => hT (k - 1) (by omega) t ht)
        (fun t => D_succ x0 e k t) t ht
      rw [show 2 ^ j * 2 = 2 * 2 ^ j by ring]
      exact F

end diagonals

/-! ### Lemma B3's sharp form (as in LemmaB3.lean) and the run bound -/

lemma constraint (x0 : ℤ → Bool) (e k : ℤ) (τ : ℕ) (h : D x0 e k (τ + 1) = false) :
    D x0 e (k - 2) τ = (D x0 e (k - 1) τ || D x0 e k τ) := by
  rw [D_succ] at h
  revert h
  cases D x0 e (k - 2) τ <;> cases (D x0 e (k - 1) τ || D x0 e k τ) <;> simp

lemma back (x0 : ℤ → Bool) (e g M' : ℤ) (τ : ℕ) (hgM : g + 1 ≤ M') (hg : D x0 e g (τ + 1) = true)
    (hw : ∀ k, g + 1 ≤ k → k ≤ M' → D x0 e k (τ + 1) = false) :
    ((∀ k, g - 1 ≤ k → k ≤ M' → D x0 e k τ = false) ∧ D x0 e (g - 2) τ = true) ∨
    ((∀ k, g - 1 ≤ k → k ≤ M' - 2 → D x0 e k τ = true) ∧ (D x0 e (M' - 1) τ = true ∨ D x0 e M' τ = true)) := by
  by_cases hall : ∀ k, g - 1 ≤ k → k ≤ M' → D x0 e k τ = false
  · left
    refine ⟨hall, ?_⟩
    have := hg
    rw [D_succ, hall (g - 1) le_rfl (by omega), hall g (by omega) (by omega)] at this
    simpa using this
  · right
    push Not at hall
    obtain ⟨k0, hk0a, hk0b, hk0⟩ := hall
    have hk0' : D x0 e k0 τ = true := by simpa using hk0
    have top : D x0 e (M' - 1) τ = true ∨ D x0 e M' τ = true := by
      by_contra hn
      push Not at hn
      have h1 : D x0 e (M' - 1) τ = false := by simpa using hn.1
      have h2 : D x0 e M' τ = false := by simpa using hn.2
      have down : ∀ n : ℕ, ∀ k, k = M' - n → g - 1 ≤ k → D x0 e k τ = false := by
        intro n
        induction n using Nat.strong_induction_on with
        | _ n ih =>
          intro k hk hkg
          rcases n with _ | _ | n
          · rw [hk]; simpa using h2
          · rw [hk]; simpa using h1
          · have c := constraint x0 e (k + 2) τ (hw (k + 2) (by omega) (by omega))
            rw [show k + 2 - 2 = k by ring, show k + 2 - 1 = k + 1 by ring,
              ih (n + 1) (by omega) (k + 1) (by push_cast at hk ⊢; omega) (by omega),
              ih n (by omega) (k + 2) (by push_cast at hk ⊢; omega) (by omega)] at c
            simpa using c
      have := down (M' - k0).toNat k0 (by omega) hk0a
      rw [hk0'] at this; exact absurd this (by decide)
    have downB : ∀ n : ℕ, ∀ k, k = M' - 2 - n → g - 1 ≤ k → D x0 e k τ = true := by
      intro n
      induction n with
      | zero =>
        intro k hk hkg
        have c := constraint x0 e (k + 2) τ (hw (k + 2) (by omega) (by omega))
        rw [show k + 2 - 2 = k by ring, show k + 2 - 1 = k + 1 by ring] at c
        rw [c]
        rcases top with h | h
        · rw [show k + 1 = M' - 1 by push_cast at hk; omega, h]; rfl
        · rw [show k + 2 = M' by push_cast at hk; omega, h]; simp
      | succ n ih =>
        intro k hk hkg
        have c := constraint x0 e (k + 2) τ (hw (k + 2) (by omega) (by push_cast at hk; omega))
        rw [show k + 2 - 2 = k by ring, show k + 2 - 1 = k + 1 by ring] at c
        rw [c, ih (k + 1) (by push_cast at hk ⊢; omega) (by omega)]; rfl
    exact ⟨fun k hk1 hk2 => downB (M' - 2 - k).toNat k (by omega) hk1, top⟩

lemma fwd (x0 : ℤ → Bool) (e g M' : ℤ) (τ0 : ℕ) (hw : ∀ k, g + 1 ≤ k → k ≤ M' → D x0 e k τ0 = false) :
    ∀ r : ℕ, ∀ k, g + 1 + 2 * r ≤ k → k ≤ M' → D x0 e k (τ0 + r) = false := by
  intro r
  induction r with
  | zero => intro k h1 h2; simpa using hw k (by simpa using h1) h2
  | succ r ih =>
    intro k h1 h2
    rw [show τ0 + (r + 1) = (τ0 + r) + 1 by ring, D_succ, ih (k - 2) (by push_cast at h1; omega) (by omega),
      ih (k - 1) (by push_cast at h1; omega) (by omega), ih k (by push_cast at h1; omega) h2]
    rfl

theorem lemma_B3_sharp (x0 : ℤ → Bool) (e : ℤ) (t P : ℕ) (g M' M : ℤ) (hP : 1 ≤ P) (htP : P ≤ t)
    (hgM : g + 1 ≤ M') (hM : M' ≤ M) (hper : ∀ k, k ≤ M → D x0 e k (t - P) = D x0 e k t)
    (hg : D x0 e g t = true) (hw : ∀ k, g + 1 ≤ k → k ≤ M' → D x0 e k t = false) : M' - g ≤ 2 * P - 1 := by
  let A : ℕ → Prop := fun s => (∀ k, g - 2 * s + 1 ≤ k → k ≤ M' → D x0 e k (t - s) = false) ∧
    D x0 e (g - 2 * s) (t - s) = true
  let B : ℕ → Prop := fun s0 => (∀ k, g - 2 * s0 - 1 ≤ k → k ≤ M' - 2 → D x0 e k (t - s0 - 1) = true) ∧
    (D x0 e (M' - 1) (t - s0 - 1) = true ∨ D x0 e M' (t - s0 - 1) = true)
  have chain : ∀ s : ℕ, s ≤ P → A s ∨ ∃ s0, s0 < s ∧ B s0 := by
    intro s
    induction s with
    | zero => intro _; left; exact ⟨fun k h1 h2 => by simpa using hw k (by simpa using h1) h2, by simpa using hg⟩
    | succ s ih =>
      intro hs
      rcases ih (by omega) with hA | ⟨s0, hs0, hB⟩
      · obtain ⟨hAw, hAb⟩ := hA
        have ht : t - s = (t - s - 1) + 1 := by omega
        rw [ht] at hAw hAb
        rcases back x0 e (g - 2 * s) M' (t - s - 1) (by omega) hAb hAw with ⟨hw2, hb2⟩ | ⟨hB, htop⟩
        · left
          refine ⟨fun k h1 h2 => ?_, ?_⟩
          · rw [show t - (s + 1) = t - s - 1 by omega]; exact hw2 k (by push_cast at h1; omega) h2
          · rw [show t - (s + 1) = t - s - 1 by omega, show g - 2 * ((s + 1 : ℕ) : ℤ) = g - 2 * s - 2 by
              push_cast; ring]; exact hb2
        · right
          exact ⟨s, by omega, fun k h1 h2 => hB k (by omega) h2, htop⟩
      · right; exact ⟨s0, by omega, hB⟩
  rcases chain P le_rfl with hA | ⟨s0, hs0, hB⟩
  · exfalso
    have := hA.1 g (by omega) (by omega)
    rw [hper g (by omega), hg] at this
    exact absurd this (by decide)
  · obtain ⟨-, hBt⟩ := hB
    have hw0 : ∀ k, g + 1 ≤ k → k ≤ M' → D x0 e k (t - P) = false := fun k h1 h2 => by
      rw [hper k (by omega)]; exact hw k h1 h2
    have F := fwd x0 e g M' (t - P) hw0 (P - s0 - 1)
    rw [show t - P + (P - s0 - 1) = t - s0 - 1 by omega] at F
    by_contra hlong
    push Not at hlong
    rcases hBt with h | h
    · rw [F (M' - 1) (by omega) (by omega)] at h
      exact absurd h (by decide)
    · rw [F M' (by omega) le_rfl] at h
      exact absurd h (by decide)

/-- From some time on, every white run in the diagonals up to j + 2 is at most 2^(j+1) - 1 long. -/
theorem run_bound (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (j : ℕ) :
    ∃ T : ℕ, ∀ t, T ≤ t → ∀ g M' : ℤ, g + 1 ≤ M' → M' ≤ j + 2 → D x0 e g t = true →
      (∀ k, g + 1 ≤ k → k ≤ M' → D x0 e k t = false) → M' - g ≤ 2 ^ (j + 1) - 1 := by
  obtain ⟨T, hT⟩ := jen_pow2 x0 e he hl j
  refine ⟨T + 2 ^ j, fun t ht g M' hgM hM hg hw => ?_⟩
  have hp : 1 ≤ 2 ^ j := Nat.one_le_two_pow
  have := lemma_B3_sharp x0 e t (2 ^ j) g M' ((j : ℤ) + 2) hp (by omega) hgM hM (fun k hk => by
    have := hT k hk (t - 2 ^ j) (by omega)
    rw [show t - 2 ^ j + 2 ^ j = t by omega] at this
    exact this.symm) hg hw
  rw [pow_succ]
  push_cast at this ⊢
  linarith

end JenPow2

#print axioms JenPow2.forced_periodic
#print axioms JenPow2.jen_pow2
#print axioms JenPow2.run_bound
