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
`run_bound_gcd` (settled form of L539's v2 pattern): if those diagonals have period P from some time, the bound is
2 gcd(P, 2^j) - 1; `per_gcd` combines two periods by Euclid.

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

/-! ### Periods combine by gcd, and the v2 run bound (settled form) -/

section gcdper
variable (x : ℕ → Bool) (T : ℕ)

lemma per_mul (p : ℕ) (hp : ∀ t, T ≤ t → x (t + p) = x t) : ∀ m t, T ≤ t → x (t + m * p) = x t := by
  intro m
  induction m with
  | zero => intro t _; simp
  | succ m ih =>
    intro t ht
    rw [show t + (m + 1) * p = (t + m * p) + p by ring, hp _ (le_trans ht (Nat.le_add_right _ _)), ih t ht]

lemma per_sub (p q : ℕ) (hp : ∀ t, T ≤ t → x (t + p) = x t) (hq : ∀ t, T ≤ t → x (t + q) = x t) (hqp : q ≤ p) :
    ∀ t, T ≤ t → x (t + (p - q)) = x t := by
  intro t ht
  rw [← hq (t + (p - q)) (by omega), show t + (p - q) + q = t + p by omega, hp t ht]

/-- Two periods give their gcd (Euclid on periods). -/
lemma per_gcd : ∀ m n : ℕ, (∀ t, T ≤ t → x (t + m) = x t) → (∀ t, T ≤ t → x (t + n) = x t) →
    ∀ t, T ≤ t → x (t + Nat.gcd m n) = x t := by
  intro m n
  induction m, n using Nat.gcd.induction with
  | H0 n => intro _ hn; simpa using hn
  | H1 m n _ ih =>
    intro hm hn
    rw [Nat.gcd_rec]
    apply ih _ hm
    have hmod : n % m = n - m * (n / m) := Nat.eq_sub_of_add_eq (Nat.mod_add_div n m)
    rw [hmod]
    exact per_sub x T n (m * (n / m)) hn
      (fun t ht => by rw [mul_comm]; exact per_mul x T m hm (n / m) t ht) (Nat.mul_div_le n m)

end gcdper

/-- The v2 bound, settled form: if the diagonals up to j + 2 have period P from some time, then from some later time
every white run there is at most 2 gcd(P, 2^j) - 1 long (so at most 1 for odd P). -/
theorem run_bound_gcd (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (j P T0 : ℕ)
    (hset : ∀ k : ℤ, k ≤ j + 2 → ∀ t, T0 ≤ t → D x0 e k (t + P) = D x0 e k t) :
    ∃ T : ℕ, ∀ t, T ≤ t → ∀ g M' : ℤ, g + 1 ≤ M' → M' ≤ j + 2 → D x0 e g t = true →
      (∀ k, g + 1 ≤ k → k ≤ M' → D x0 e k t = false) → M' - g ≤ 2 * (Nat.gcd P (2 ^ j) : ℤ) - 1 := by
  obtain ⟨T1, hT1⟩ := jen_pow2 x0 e he hl j
  set c := Nat.gcd P (2 ^ j) with hc
  have hc1 : 1 ≤ c := Nat.gcd_pos_of_pos_right _ (Nat.two_pow_pos j)
  have hper : ∀ k : ℤ, k ≤ j + 2 → ∀ t, T0 + T1 ≤ t → D x0 e k (t + c) = D x0 e k t := by
    intro k hk
    exact per_gcd (fun t => D x0 e k t) (T0 + T1) P (2 ^ j)
      (fun t ht => hset k hk t (by omega)) (fun t ht => hT1 k hk t (by omega))
  refine ⟨T0 + T1 + c, fun t ht g M' hgM hM hg hw => ?_⟩
  exact lemma_B3_sharp x0 e t c g M' ((j : ℤ) + 2) hc1 (by omega) hgM hM (fun k hk => by
    have := hper k hk (t - c) (by omega)
    rw [show t - c + c = t by omega] at this
    exact this.symm) hg hw

/-! ### Lemma B2 and entry 9's corollary: infinitely many eventually white and eventually black diagonals -/

/-- The recurrence read backwards. -/
lemma D_back (x0 : ℤ → Bool) (e m : ℤ) (t : ℕ) :
    D x0 e (m - 2) t = xor (D x0 e m (t + 1)) (D x0 e (m - 1) t || D x0 e m t) := by
  rw [D_succ]
  cases D x0 e (m - 2) t <;> cases (D x0 e (m - 1) t || D x0 e m t) <;> rfl

/-- Two sequences with period P from T that agree on [T, T + P) agree from T on. -/
lemma ext_window (u v : ℕ → Bool) (T P : ℕ) (hP : 1 ≤ P) (hu : ∀ t, T ≤ t → u (t + P) = u t)
    (hv : ∀ t, T ≤ t → v (t + P) = v t) (hw : ∀ s, s < P → u (T + s) = v (T + s)) :
    ∀ t, T ≤ t → u t = v t := by
  intro t
  induction t using Nat.strong_induction_on with
  | _ t ih =>
    intro ht
    by_cases h : t < T + P
    · have := hw (t - T) (by omega)
      rwa [show T + (t - T) = t by omega] at this
    · have e1 := hu (t - P) (by omega)
      have e2 := hv (t - P) (by omega)
      rw [show t - P + P = t by omega] at e1 e2
      rw [e1, e2, ih (t - P) (by omega) (by omega)]

/-- A black input resets: once D_(k-1) is black at a time t0 ≥ T, D_k inherits its inputs' period p. -/
lemma reset (a b x : ℕ → Bool) (T p : ℕ) (ha : ∀ t, T ≤ t → a (t + p) = a t) (hb : ∀ t, T ≤ t → b (t + p) = b t)
    (hx : ∀ t, x (t + 1) = xor (a t) (b t || x t)) (t0 : ℕ) (ht0 : T ≤ t0) (hb1 : b t0 = true) :
    ∀ t, t0 + 1 ≤ t → x (t + p) = x t := by
  have h1 : x (t0 + 1 + 1 * p) = x (t0 + 1) := by
    simp only [show t0 + 1 + 1 * p = (t0 + p) + 1 by ring, hx, ha t0 ht0, hb t0 ht0, hb1, Bool.true_or]
  have d := det a b x T p ha hb hx 1 (t0 + 1) (by omega) h1.symm
  intro t ht
  have := d (t - (t0 + 1))
  rw [show t0 + 1 + (t - (t0 + 1)) = t by omega, show t0 + 1 + 1 * p + (t - (t0 + 1)) = t + p by omega] at this
  exact this.symm

/-- Eventually white / eventually black (as in LemmaB1.lean). -/
def EvW (x0 : ℤ → Bool) (e j : ℤ) : Prop := ∃ T : ℕ, ∀ t, T ≤ t → D x0 e j t = false
def EvB (x0 : ℤ → Bool) (e j : ℤ) : Prop := ∃ T : ℕ, ∀ t, T ≤ t → D x0 e j t = true

section band
variable (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false)
include he hl

/-- Lemma B2: no P ≥ 1 is an eventual period of every diagonal. -/
theorem lemma_B2 (P : ℕ) (hP : 1 ≤ P) :
    ¬ ∀ k : ℕ, ∃ T : ℕ, ∀ t, T ≤ t → D x0 e k (t + P) = D x0 e k t := by
  intro h
  choose T hT using h
  obtain ⟨Ts, hTk⟩ : ∃ Ts, ∀ k, k ≤ 4 ^ P + 1 → T k ≤ Ts :=
    ⟨(Finset.range (4 ^ P + 2)).sup T, fun k hk => Finset.le_sup (Finset.mem_range.mpr (by omega))⟩
  have hper : ∀ k : ℕ, k ≤ 4 ^ P + 1 → ∀ t, Ts ≤ t → D x0 e k (t + P) = D x0 e k t :=
    fun k hk t ht => hT k t (le_trans (hTk k hk) ht)
  have hper1 : ∀ k : ℕ, k ≤ 4 ^ P → ∀ t, Ts ≤ t → D x0 e ((k : ℤ) + 1) (t + P) = D x0 e ((k : ℤ) + 1) t := by
    intro k hk t ht
    have := hper (k + 1) (by omega) t ht
    push_cast at this
    exact this
  -- the windows (D_k, D_(k+1)) on [Ts, Ts + P)
  let f : Fin (4 ^ P + 1) → (Fin P → Bool) × (Fin P → Bool) :=
    fun k => (fun s => D x0 e ((k : ℕ) : ℤ) (Ts + s), fun s => D x0 e (((k : ℕ) : ℤ) + 1) (Ts + s))
  have hcard : Fintype.card ((Fin P → Bool) × (Fin P → Bool)) < Fintype.card (Fin (4 ^ P + 1)) := by
    simp only [Fintype.card_prod, Fintype.card_fun, Fintype.card_bool, Fintype.card_fin]
    rw [← mul_pow]
    norm_num
  obtain ⟨a, b, hab, hfab⟩ := Fintype.exists_ne_map_eq_of_card_lt f hcard
  -- two equal windows at k1 < k2 give a contradiction
  have key : ∀ k1 k2 : ℕ, k1 < k2 → k2 ≤ 4 ^ P →
      (∀ s, s < P → D x0 e (k1 : ℤ) (Ts + s) = D x0 e (k2 : ℤ) (Ts + s)) →
      (∀ s, s < P → D x0 e ((k1 : ℤ) + 1) (Ts + s) = D x0 e ((k2 : ℤ) + 1) (Ts + s)) → False := by
    intro k1 k2 hlt hk2 w0 w1
    have E0 := ext_window (fun t => D x0 e (k1 : ℤ) t) (fun t => D x0 e (k2 : ℤ) t) Ts P hP
      (hper k1 (by omega)) (hper k2 (by omega)) w0
    have E1 := ext_window (fun t => D x0 e ((k1 : ℤ) + 1) t) (fun t => D x0 e ((k2 : ℤ) + 1) t) Ts P hP
      (hper1 k1 (by omega)) (hper1 k2 hk2) w1
    have Q : ∀ j : ℕ, ∀ t, Ts ≤ t → D x0 e ((k1 : ℤ) + 1 - j) t = D x0 e ((k2 : ℤ) + 1 - j) t ∧
        D x0 e ((k1 : ℤ) - j) t = D x0 e ((k2 : ℤ) - j) t := by
      intro j
      induction j with
      | zero => intro t ht; simpa using And.intro (E1 t ht) (E0 t ht)
      | succ j ih =>
        intro t ht
        obtain ⟨h1, h0⟩ := ih t ht
        obtain ⟨h1', -⟩ := ih (t + 1) (by omega)
        refine ⟨?_, ?_⟩
        · rw [show (k1 : ℤ) + 1 - ((j + 1 : ℕ) : ℤ) = k1 - j by push_cast; ring,
            show (k2 : ℤ) + 1 - ((j + 1 : ℕ) : ℤ) = k2 - j by push_cast; ring]
          exact h0
        · have b1 := D_back x0 e ((k1 : ℤ) + 1 - j) t
          have b2 := D_back x0 e ((k2 : ℤ) + 1 - j) t
          rw [show (k1 : ℤ) + 1 - j - 2 = k1 - ((j + 1 : ℕ) : ℤ) by push_cast; ring,
            show (k1 : ℤ) + 1 - j - 1 = k1 - j by ring] at b1
          rw [show (k2 : ℤ) + 1 - j - 2 = k2 - ((j + 1 : ℕ) : ℤ) by push_cast; ring,
            show (k2 : ℤ) + 1 - j - 1 = k2 - j by ring] at b2
          rw [b1, b2, h1', h0, h1]
    have := (Q k2 Ts le_rfl).2
    rw [Dneg x0 e he hl ((k1 : ℤ) - k2) (by omega), sub_self, D0 x0 e he hl] at this
    exact absurd this (by decide)
  have hv : (a : ℕ) ≠ (b : ℕ) := fun h => hab (Fin.ext h)
  have w0 : ∀ s, s < P → D x0 e ((a : ℕ) : ℤ) (Ts + s) = D x0 e ((b : ℕ) : ℤ) (Ts + s) :=
    fun s hs => congrFun (congrArg Prod.fst hfab) ⟨s, hs⟩
  have w1 : ∀ s, s < P → D x0 e (((a : ℕ) : ℤ) + 1) (Ts + s) = D x0 e (((b : ℕ) : ℤ) + 1) (Ts + s) :=
    fun s hs => congrFun (congrArg Prod.snd hfab) ⟨s, hs⟩
  rcases Nat.lt_or_gt_of_ne hv with hlt | hlt
  · exact key a b hlt (by omega) w0 w1
  · exact key b a hlt (by omega) (fun s hs => (w0 s hs).symm) (fun s hs => (w1 s hs).symm)

/-- Entry 9's corollary: for every N some diagonal k ≥ N is eventually white. -/
theorem infinitely_many_white (N : ℕ) : ∃ k : ℕ, N ≤ k ∧ EvW x0 e k := by
  by_contra hno
  push Not at hno
  have hinf : ∀ k : ℕ, N ≤ k → ∀ T, ∃ t, T ≤ t ∧ D x0 e k t = true := by
    intro k hk T
    by_contra hc
    push Not at hc
    exact hno k hk ⟨T, fun t ht => by simpa using hc t ht⟩
  obtain ⟨T0, hT0⟩ := jen_pow2 x0 e he hl N
  have grow : ∀ m : ℕ, ∃ T, ∀ k : ℤ, k ≤ (N : ℤ) + 2 + m → ∀ t, T ≤ t → D x0 e k (t + 2 ^ N) = D x0 e k t := by
    intro m
    induction m with
    | zero => exact ⟨T0, fun k hk t ht => hT0 k (by simpa using hk) t ht⟩
    | succ m ih =>
      obtain ⟨T, hT⟩ := ih
      obtain ⟨t0, ht0, hb1⟩ := hinf (N + 2 + m) (by omega) T
      refine ⟨t0 + 1, fun k hk t ht => ?_⟩
      rcases (show k ≤ (N : ℤ) + 2 + m ∨ k = (N : ℤ) + 2 + m + 1 by push_cast at hk; omega) with h | h
      · exact hT k h t (by omega)
      · exact reset (fun t => D x0 e (k - 2) t) (fun t => D x0 e (k - 1) t) (fun t => D x0 e k t) T (2 ^ N)
          (fun t ht => hT (k - 2) (by omega) t ht) (fun t ht => hT (k - 1) (by omega) t ht)
          (fun t => D_succ x0 e k t) t0 ht0 (by
            show D x0 e (k - 1) t0 = true
            rw [show k - 1 = ((N + 2 + m : ℕ) : ℤ) by push_cast; omega]
            exact hb1) t ht
  exact lemma_B2 x0 e he hl (2 ^ N) Nat.one_le_two_pow (fun k => by
    obtain ⟨T, hT⟩ := grow k
    exact ⟨T, fun t ht => hT k (by omega) t ht⟩)

omit he hl in
lemma down (j : ℤ) (h0 : EvW x0 e j) (h1 : EvW x0 e (j + 1)) : EvW x0 e (j - 1) := by
  obtain ⟨T0, h0⟩ := h0
  obtain ⟨T1, h1⟩ := h1
  refine ⟨T0 + T1, fun t ht => ?_⟩
  have := h1 (t + 1) (by omega)
  rw [D_succ, show j + 1 - 2 = j - 1 by ring, show j + 1 - 1 = j by ring, h0 t (by omega), h1 t (by omega)] at this
  simpa using this

/-- B1 (1), as in LemmaB1.lean. -/
theorem no_adjacent_white (j : ℤ) (hj : 0 ≤ j) (h0 : EvW x0 e j) (h1 : EvW x0 e (j + 1)) : False := by
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

/-- B1 (2), as in LemmaB1.lean. -/
theorem white_then_black (j : ℤ) (hj : 0 ≤ j) (h0 : EvW x0 e j) : EvB x0 e (j + 2) := by
  obtain ⟨T, hT⟩ := h0
  have hm : ∀ t, T ≤ t → D x0 e (j + 2) t = true → D x0 e (j + 2) (t + 1) = true := by
    intro t ht hb
    rw [D_succ, show j + 2 - 2 = j by ring, hT t ht, hb]; simp
  rcases mono_eventually x0 e (j + 2) T hm with hw | hb
  · exfalso
    obtain ⟨T2, h2⟩ := hw
    have h1 : EvW x0 e (j + 1) := ⟨T + T2, fun t ht => by
      have := h2 (t + 1) (by omega)
      rw [D_succ, show j + 2 - 2 = j by ring, show j + 2 - 1 = j + 1 by ring, hT t (by omega)] at this
      simp at this
      exact this.1⟩
    exact no_adjacent_white x0 e he hl j hj ⟨T, hT⟩ h1
  · exact hb

/-- Entry 9's corollary: for every N some diagonal k ≥ N is eventually black. -/
theorem infinitely_many_black (N : ℕ) : ∃ k : ℕ, N ≤ k ∧ EvB x0 e k := by
  obtain ⟨k, hk, hw⟩ := infinitely_many_white x0 e he hl N
  refine ⟨k + 2, by omega, ?_⟩
  have := white_then_black x0 e he hl k (by omega) hw
  push_cast
  exact this

end band

end JenPow2

#print axioms JenPow2.forced_periodic
#print axioms JenPow2.jen_pow2
#print axioms JenPow2.run_bound
#print axioms JenPow2.per_gcd
#print axioms JenPow2.run_bound_gcd
#print axioms JenPow2.lemma_B2
#print axioms JenPow2.infinitely_many_white
#print axioms JenPow2.infinitely_many_black
