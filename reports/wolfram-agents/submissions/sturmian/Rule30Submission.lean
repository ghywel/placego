import Rule30PrizeKit
import Mathlib

/-!
# Every characteristic Sturmian word is excluded as the right neighbour of a period-2 center column

**A partial result for Problem 1**, in the period-2 case, by word combinatorics on top of Corollary F. Suppose
column `0` of a configuration reads the clock `0101…` from time `0` and the configuration has a leftmost black cell.
Rule 30's left-permutivity makes column `-1` the complement of column `1` at even times and black at odd times, so
the *visible bits* `c i = evol x0 (2 i) 1` carry everything the clock allows. **Corollary F** (`corollary_F`, the
record's PROOFS.md entry 11, formalized in the previous submission): the visible bits have no near-squares at
unbounded scales, no fixed slack `K` and pairs `i < i′` with `i′ - i` unbounded whose common future lasts `i′ - K`.

This module adds the words. For a directive sequence `d` with every `d n ≥ 1`, the **standard words** are
`std d 0 = [1]`, `std d 1 = [0]`, `std d (n+2) = (std d (n+1))^(d n) ++ std d n`; each is a prefix of the next, and
their common limit `cw d` is the characteristic Sturmian word of slope `[0; d 0 + 1, d 1, d 2, …]` (exchanging the
letters gives the slopes above `1/2`). Two facts about them, proved by induction on lists:

* `std_near_comm`: `std (n+1) ++ std n` and `std n ++ std (n+1)` agree except on their last two letters;
* `cw_near_square`: for every `n`, `cw d` agrees with its shift by `|std d (n+1)|` on the first `|std d (n+1)| - 2`
  positions. So the pairs `(0, |std d (n+1)|)` are near-squares with slack `2` at every scale.

Hence (`characteristic_excluded`, `characteristic_excluded_compl`, `fibonacci_excluded`): **no configuration with a
leftmost black cell and the clock on column `0` has a characteristic Sturmian word, or its letter exchange, as its
visible bits**, for every directive sequence, so for every irrational slope. The Fibonacci word (`d n = 1`) is the
first example.

**What is new relative to the kit.** The kit's `Rule30ZeroBoundary.Q01` asks the period-2 question for the single
seed; `Rule30DrivenLeft.no_periodic_column` excludes eventually periodic drivers; its CATALOG remarks that Sturmian
sequences are not eventually periodic. Nothing in the kit excludes any aperiodic right neighbour under the clock.
This excludes uncountably many of zero entropy, the characteristic words of every slope. The record's Theorem E
(PROOFS.md entry 14) excludes every Sturmian word, every slope *and every intercept*, by a Diophantine argument;
the characteristic case is what word combinatorics gives without real analysis, and the general intercept is not
formalized here.

**Provenance.** Corollary F and Theorem E are RULE30-PRIZE.md §8.57 and §8.59, PROOFS.md entries 11 and 14, of the
Wolfram · Collatz · Mahler record (github.com/ghywel/placego), proved by hand by Local (Claude) on 2026-10-05; the
near-commutation of standard words is classical (Lothaire, *Algebraic Combinatorics on Words*, Chapter 2). Formalized
by Cloud (Claude) on 2026-10-23 on the kit's `evol`, from the record's Lean for Lemma B2 and Theorem A‴ (Local,
2026-10-10). Sources: E. Jen, J. Stat. Phys. 43 (1986); M. Lothaire (2002).
-/

set_option Elab.async false

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30Jen
open Ruliology.CellularAutomata.Rule30Prize
open Ruliology.CellularAutomata.Rule30Realization

lemma evol_succ (x0 : ℤ → Bool) (t : ℕ) (i : ℤ) :
    evol x0 (t + 1) i = xor (evol x0 t (i - 1)) (evol x0 t i || evol x0 t (i + 1)) := rfl

lemma edge (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (t : ℕ) :
    evol x0 t (e - t) = true ∧ ∀ j < e - t, evol x0 t j = false := by
  induction t with
  | zero => simpa using ⟨he, hl⟩
  | succ t ih =>
    obtain ⟨h1, h2⟩ := ih
    constructor
    · rw [evol_succ]
      have a1 : evol x0 t (e - ↑(t + 1) - 1) = false := h2 _ (by push_cast; omega)
      have a2 : evol x0 t (e - ↑(t + 1)) = false := h2 _ (by push_cast; omega)
      have a3 : e - ↑(t + 1) + 1 = e - ↑t := by push_cast; ring
      rw [a1, a2, a3, h1]; rfl
    · intro j hj
      rw [evol_succ]
      have b1 : evol x0 t (j - 1) = false := h2 _ (by push_cast at hj; omega)
      have b2 : evol x0 t j = false := h2 _ (by push_cast at hj; omega)
      have b3 : evol x0 t (j + 1) = false := h2 _ (by push_cast at hj; omega)
      rw [b1, b2, b3]; rfl

/-- Diagonal k at time t. -/
def D (x0 : ℤ → Bool) (e : ℤ) (k : ℤ) (t : ℕ) : Bool := evol x0 t (e - t + k)

lemma D_succ (x0 : ℤ → Bool) (e j : ℤ) (t : ℕ) :
    D x0 e j (t + 1) = xor (D x0 e (j - 2) t) (D x0 e (j - 1) t || D x0 e j t) := by
  unfold D
  rw [evol_succ]
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

/-- Lemma B2, quantitative: some diagonal k ≤ 4^P + 1 does not have eventual period P (the form of Nersissian's
m + 2 ≤ 4^(Q_m), here for every configuration with a leftmost black cell). -/
theorem lemma_B2_quant (P : ℕ) (hP : 1 ≤ P) :
    ¬ ∀ k : ℕ, k ≤ 4 ^ P + 1 → ∃ T : ℕ, ∀ t, T ≤ t → D x0 e k (t + P) = D x0 e k t := by
  intro h
  have common : ∀ n : ℕ, n ≤ 4 ^ P + 1 →
      ∃ Ts, ∀ k : ℕ, k ≤ n → ∀ t, Ts ≤ t → D x0 e k (t + P) = D x0 e k t := by
    intro n
    induction n with
    | zero =>
      intro hn
      obtain ⟨T, hT⟩ := h 0 (by omega)
      exact ⟨T, fun k hk t ht => by
        have : k = 0 := by omega
        subst this; exact hT t ht⟩
    | succ n ih =>
      intro hn
      obtain ⟨T1, h1⟩ := ih (by omega)
      obtain ⟨T2, h2⟩ := h (n + 1) hn
      exact ⟨T1 + T2, fun k hk t ht => by
        rcases (show k ≤ n ∨ k = n + 1 by omega) with hk' | hk'
        · exact h1 k hk' t (by omega)
        · subst hk'; exact h2 t (by omega)⟩
  obtain ⟨Ts, hper⟩ := common (4 ^ P + 1) le_rfl
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

/-- Lemma B2: no P ≥ 1 is an eventual period of every diagonal. -/
theorem lemma_B2 (P : ℕ) (hP : 1 ≤ P) :
    ¬ ∀ k : ℕ, ∃ T : ℕ, ∀ t, T ≤ t → D x0 e k (t + P) = D x0 e k t :=
  fun h => lemma_B2_quant x0 e he hl P hP (fun k _ => h k)

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

/-- Read right to left: x_t(j - 1) from x_(t+1)(j), x_t(j) and x_t(j + 1). -/
lemma step_inv (x0 : ℤ → Bool) (t : ℕ) (j : ℤ) :
    evol x0 t (j - 1) = xor (evol x0 (t + 1) j) (evol x0 t j || evol x0 t (j + 1)) := by
  rw [evol_succ]
  cases evol x0 t (j - 1) <;> cases (evol x0 t j || evol x0 t (j + 1)) <;> rfl

/-- Equal blocks on columns i and i + 1 at times a .. a + n - 1 and a′ .. a′ + n - 1 make the rows agree: the cell
m to the left of column i agrees at times a + s and a′ + s whenever s + m < n. -/
lemma agree (x0 : ℤ → Bool) (i : ℤ) (n a a' : ℕ)
    (hblock : ∀ s : ℕ, s < n → evol x0 (a + s) i = evol x0 (a' + s) i ∧ evol x0 (a + s) (i + 1) = evol x0 (a' + s) (i + 1)) :
    ∀ m s : ℕ, s + m < n → evol x0 (a + s) (i - m) = evol x0 (a' + s) (i - m) := by
  intro m
  induction m using Nat.strong_induction_on with
  | _ m ih =>
    intro s hs
    rcases m with _ | m
    · simpa using (hblock s (by omega)).1
    · -- the cell m + 1 to the left from the cells m and m - 1 to the left (or column i + 1 when m = 0)
      have h1 : evol x0 (a + s + 1) (i - m) = evol x0 (a' + s + 1) (i - m) := by
        have := ih m (by omega) (s + 1) (by omega)
        rwa [show a + (s + 1) = a + s + 1 by ring, show a' + (s + 1) = a' + s + 1 by ring] at this
      have h2 : evol x0 (a + s) (i - m) = evol x0 (a' + s) (i - m) := ih m (by omega) s (by omega)
      have h3 : evol x0 (a + s) (i - m + 1) = evol x0 (a' + s) (i - m + 1) := by
        rcases m with _ | m
        · simpa using (hblock s (by omega)).2
        · have := ih m (by omega) s (by omega)
          rwa [show i - ((m : ℕ) : ℤ) = i - ((m + 1 : ℕ) : ℤ) + 1 by push_cast; ring] at this
      rw [show i - ((m + 1 : ℕ) : ℤ) = (i - m) - 1 by push_cast; ring, step_inv x0 (a + s), step_inv x0 (a' + s), h1, h2, h3]

/-- Theorem A′. -/
theorem theorem_A' (x0 : ℤ → Bool) (i : ℤ) (L : ℕ) (hc : x0 (i - L) = true) (hl : ∀ j < i - L, x0 j = false)
    (n a a' : ℕ) (haa : a < a')
    (hblock : ∀ s : ℕ, s < n → evol x0 (a + s) i = evol x0 (a' + s) i ∧ evol x0 (a + s) (i + 1) = evol x0 (a' + s) (i + 1)) :
    n ≤ L + a' := by
  by_contra h
  push Not at h
  have hag := agree x0 i n a a' hblock (L + a') 0 (by omega)
  simp only [add_zero] at hag
  have E := edge x0 (i - L) hc hl
  have black : evol x0 a' (i - ((L + a' : ℕ) : ℤ)) = true := by
    have := (E a').1
    rwa [show i - (L : ℤ) - (a' : ℤ) = i - ((L + a' : ℕ) : ℤ) by push_cast; ring] at this
  have white : evol x0 a (i - ((L + a' : ℕ) : ℤ)) = false :=
    (E a).2 _ (by push_cast; omega)
  rw [white, black] at hag
  exact absurd hag (by decide)

/-- Theorem A‴ (entry 10): row a′ is white at the distances L + a + 1 .. n - 1 left of column i, which are its
diagonals L + a′ - n + 1 .. a′ - a - 1. -/
theorem theorem_A3_white (x0 : ℤ → Bool) (i : ℤ) (L : ℕ) (hc : x0 (i - L) = true) (hl : ∀ j < i - L, x0 j = false)
    (n a a' : ℕ)
    (hblock : ∀ s : ℕ, s < n → evol x0 (a + s) i = evol x0 (a' + s) i ∧ evol x0 (a + s) (i + 1) = evol x0 (a' + s) (i + 1)) :
    ∀ δ : ℕ, L + a + 1 ≤ δ → δ + 1 ≤ n → evol x0 a' (i - δ) = false := by
  intro δ h1 h2
  have hag := agree x0 i n a a' hblock δ 0 (by omega)
  simp only [add_zero] at hag
  rw [← hag]
  exact (edge x0 (i - L) hc hl a).2 _ (by omega)

/-- Theorem A‴'s corollary: if diagonal b (the cell b right of the moving left edge) is black at time a′ and
b < a′ - a, then n ≤ L + a′ - b. -/
theorem theorem_A3 (x0 : ℤ → Bool) (i : ℤ) (L : ℕ) (hc : x0 (i - L) = true) (hl : ∀ j < i - L, x0 j = false)
    (n a a' b : ℕ) (hb : b + a < a') (hblack : evol x0 a' (i - L - a' + b) = true)
    (hblock : ∀ s : ℕ, s < n → evol x0 (a + s) i = evol x0 (a' + s) i ∧ evol x0 (a + s) (i + 1) = evol x0 (a' + s) (i + 1)) :
    n ≤ L + a' - b := by
  by_contra h
  push Not at h
  have hw := theorem_A3_white x0 i L hc hl n a a' hblock (L + a' - b) (by omega) (by omega)
  rw [show i - ((L + a' - b : ℕ) : ℤ) = i - L - a' + b by push_cast [show b ≤ L + a' by omega]; ring] at hw
  rw [hw] at hblack
  exact absurd hblack (by decide)

/-! ## Corollary F: near-squares at the start are fatal -/

/-- Column `-1` under the clock: black at odd times, the complement of column `1` at even times. -/
lemma col_m1 (x0 : ℤ → Bool) (T0 : ℕ) (hclock : ∀ t, T0 ≤ t → evol x0 t 0 = decide (t % 2 = 1)) (t : ℕ)
    (ht : T0 ≤ t) :
    (t % 2 = 1 → evol x0 t (-1) = true) ∧ (t % 2 = 0 → evol x0 t (-1) = !(evol x0 t 1)) := by
  have h := evol_succ x0 t 0
  simp only [zero_sub, zero_add] at h
  constructor
  · intro ho
    have hA : evol x0 t 0 = true := by rw [hclock t ht]; simp only [decide_eq_true_eq]; omega
    have hB : evol x0 (t + 1) 0 = false := by rw [hclock (t + 1) (by omega)]; simp only [decide_eq_false_iff_not]; omega
    rw [hA, hB] at h
    revert h; cases evol x0 t (-1) <;> simp
  · intro he
    have hA : evol x0 t 0 = false := by rw [hclock t ht]; simp only [decide_eq_false_iff_not]; omega
    have hB : evol x0 (t + 1) 0 = true := by rw [hclock (t + 1) (by omega)]; simp only [decide_eq_true_eq]; omega
    rw [hA, hB] at h
    revert h; cases evol x0 t (-1) <;> cases evol x0 t 1 <;> simp

/-- Visible bits agreeing for `l` steps make columns `-1` and `0` agree for `2l` steps. -/
lemma blocks_of_visible (x0 : ℤ → Bool) (T0 : ℕ) (hclock : ∀ t, T0 ≤ t → evol x0 t 0 = decide (t % 2 = 1))
    (i i' l : ℕ) (hi : T0 ≤ 2 * i) (hii : i ≤ i')
    (hvis : ∀ s, s < l → evol x0 (2 * (i + s)) 1 = evol x0 (2 * (i' + s)) 1) :
    ∀ u : ℕ, u < 2 * l → evol x0 (2 * i + u) (-1) = evol x0 (2 * i' + u) (-1) ∧
      evol x0 (2 * i + u) 0 = evol x0 (2 * i' + u) 0 := by
  intro u hu
  have h1 : T0 ≤ 2 * i + u := by omega
  have h2 : T0 ≤ 2 * i' + u := by omega
  constructor
  · rcases Nat.mod_two_eq_zero_or_one u with he | ho
    · obtain ⟨s, rfl⟩ : ∃ s, u = 2 * s := ⟨u / 2, by omega⟩
      have e1 := (col_m1 x0 T0 hclock (2 * i + 2 * s) h1).2 (by omega)
      have e2 := (col_m1 x0 T0 hclock (2 * i' + 2 * s) h2).2 (by omega)
      rw [e1, e2, show 2 * i + 2 * s = 2 * (i + s) by ring, show 2 * i' + 2 * s = 2 * (i' + s) by ring,
        hvis s (by omega)]
    · rw [(col_m1 x0 T0 hclock _ h1).1 (by omega), (col_m1 x0 T0 hclock _ h2).1 (by omega)]
  · rw [hclock _ h1, hclock _ h2, show (2 * i + u) % 2 = (2 * i' + u) % 2 by omega]

/-- **Corollary F.** A configuration with a leftmost black cell `L ≥ 1` cells left of column `0`, whose column `0`
reads the clock `0101…` from time `T0`, has no near-squares at unbounded scales in its visible bits
`evol x0 (2 i) 1`: there are no `K` and pairs `i < i′` with `i′ - i` unbounded, `T0 ≤ 2 i`, and
`evol x0 (2 (i + s)) 1 = evol x0 (2 (i′ + s)) 1` for all `s + K < i′`. -/
theorem corollary_F (x0 : ℤ → Bool) (L : ℕ) (hL : 1 ≤ L) (hc : x0 (-(L : ℤ)) = true)
    (hl : ∀ j < -(L : ℤ), x0 j = false)
    (T0 : ℕ) (hclock : ∀ t, T0 ≤ t → evol x0 t 0 = decide (t % 2 = 1)) (K : ℕ)
    (hpairs : ∀ N : ℕ, ∃ i i' : ℕ, i < i' ∧ N ≤ i' - i ∧ T0 ≤ 2 * i ∧
      ∀ s, s + K < i' → evol x0 (2 * (i + s)) 1 = evol x0 (2 * (i' + s)) 1) : False := by
  obtain ⟨b, hb, tb, htb⟩ := infinitely_many_black x0 (-(L : ℤ)) hc hl (L + 2 * K)
  obtain ⟨i, i', hii, hN, hT0, hvis⟩ := hpairs (b + tb + 1)
  have hK : K < i' := by omega
  have hblock := blocks_of_visible x0 T0 hclock i i' (i' - K) hT0 hii.le (fun s hs => hvis s (by omega))
  have hblack : evol x0 (2 * i') ((-1 : ℤ) - ((L - 1 : ℕ) : ℤ) - ((2 * i' : ℕ) : ℤ) + ((b : ℕ) : ℤ)) = true := by
    have h := htb (2 * i') (by omega)
    unfold D at h
    have e : (-1 : ℤ) - ((L - 1 : ℕ) : ℤ) - ((2 * i' : ℕ) : ℤ) + ((b : ℕ) : ℤ) =
        -(L : ℤ) - ((2 * i' : ℕ) : ℤ) + ((b : ℕ) : ℤ) := by omega
    rw [e]; exact h
  have hA3 := theorem_A3 x0 (-1) (L - 1)
    (by rw [show (-1 : ℤ) - ((L - 1 : ℕ) : ℤ) = -(L : ℤ) by omega]; exact hc)
    (fun j hj => hl j (by omega)) (2 * (i' - K)) (2 * i) (2 * i') b (by omega) hblack
    (fun s hs => by simpa using hblock s hs)
  omega

/-! ## Standard words and the characteristic Sturmian words -/

/-- `w` repeated `a` times. -/
def wpow (w : List Bool) : ℕ → List Bool
  | 0 => []
  | a + 1 => w ++ wpow w a

theorem wpow_succ (w : List Bool) (a : ℕ) : wpow w (a + 1) = w ++ wpow w a := rfl

theorem wpow_length (w : List Bool) : ∀ a, (wpow w a).length = a * w.length
  | 0 => by simp [wpow]
  | a + 1 => by rw [wpow_succ, List.length_append, wpow_length w a, Nat.succ_mul, Nat.add_comm]

theorem wpow_comm (w : List Bool) : ∀ a, w ++ wpow w a = wpow w a ++ w
  | 0 => by simp [wpow]
  | a + 1 => by rw [wpow_succ, List.append_assoc, wpow_comm w a]

/-- The standard words of the directive sequence `d`: `std d 0 = [1]`, `std d 1 = [0]`,
`std d (n + 2) = (std d (n + 1))^(d n) ++ std d n`. With every `d n ≥ 1` these are the standard words of the
characteristic Sturmian word of slope `[0; d 0 + 1, d 1, d 2, …]`; exchanging the letters gives the other slopes. -/
def std (d : ℕ → ℕ) : ℕ → List Bool
  | 0 => [true]
  | 1 => [false]
  | n + 2 => wpow (std d (n + 1)) (d n) ++ std d n

theorem std_succ_succ (d : ℕ → ℕ) (n : ℕ) : std d (n + 2) = wpow (std d (n + 1)) (d n) ++ std d n := rfl

theorem std_length_pos (d : ℕ → ℕ) : ∀ n, 1 ≤ (std d n).length
  | 0 => by simp [std]
  | 1 => by simp [std]
  | n + 2 => by rw [std_succ_succ, List.length_append]; have := std_length_pos d n; omega

/-- With `d n ≥ 1`, `std d (n + 2)` begins with `std d (n + 1)`. -/
theorem std_prefix (d : ℕ → ℕ) (hd : ∀ n, 1 ≤ d n) (n : ℕ) : std d (n + 1) <+: std d (n + 2) := by
  rw [std_succ_succ]
  obtain ⟨a, ha⟩ : ∃ a, d n = a + 1 := ⟨d n - 1, by have := hd n; omega⟩
  rw [ha, wpow_succ, List.append_assoc]
  exact List.prefix_append _ _

theorem std_prefix_le (d : ℕ → ℕ) (hd : ∀ n, 1 ≤ d n) (n : ℕ) : ∀ m, std d (n + 1) <+: std d (n + 1 + m)
  | 0 => List.prefix_rfl
  | m + 1 => by
    have h := std_prefix d hd (n + m)
    rw [show n + m + 1 = n + 1 + m by ring, show n + m + 2 = n + 1 + (m + 1) by ring] at h
    exact (std_prefix_le d hd n m).trans h

theorem std_length_ge (d : ℕ → ℕ) (hd : ∀ n, 1 ≤ d n) : ∀ n, n + 1 ≤ (std d (n + 1)).length
  | 0 => by simp [std]
  | n + 1 => by
    have h1 := std_length_ge d hd n
    have h2 := std_length_pos d n
    have h3 : (std d (n + 2)).length = d n * (std d (n + 1)).length + (std d n).length := by
      rw [std_succ_succ, List.length_append, wpow_length]
    have h4 : (std d (n + 1)).length ≤ d n * (std d (n + 1)).length := Nat.le_mul_of_pos_left _ (hd n)
    rw [show n + 1 + 1 = n + 2 by ring, h3]
    omega

/-- The characteristic word: position `i` read in `std d (i + 2)`, which is long enough. -/
def cw (d : ℕ → ℕ) (i : ℕ) : Bool := (std d (i + 2)).getD i false

theorem getD_of_prefix {u v : List Bool} (h : u <+: v) (i : ℕ) (hi : i < u.length) :
    v.getD i false = u.getD i false := by
  obtain ⟨t, rfl⟩ := h
  exact List.getD_append u t false i hi

/-- The characteristic word agrees with every standard word `std d (n + 1)` on its length. -/
theorem cw_eq (d : ℕ → ℕ) (hd : ∀ n, 1 ≤ d n) (n i : ℕ) (hi : i < (std d (n + 1)).length) :
    cw d i = (std d (n + 1)).getD i false := by
  unfold cw
  rcases le_or_gt (n + 1) (i + 2) with h | h
  · obtain ⟨m, hm⟩ : ∃ m, i + 2 = n + 1 + m := ⟨i + 2 - (n + 1), by omega⟩
    rw [hm]; exact getD_of_prefix (std_prefix_le d hd n m) i hi
  · obtain ⟨m, hm⟩ : ∃ m, n + 1 = i + 2 + m := ⟨n + 1 - (i + 2), by omega⟩
    have hi2 : i < (std d (i + 2)).length := by
      have := std_length_ge d hd (i + 1)
      rw [show i + 1 + 1 = i + 2 by ring] at this
      omega
    rw [hm, getD_of_prefix (std_prefix_le d hd (i + 1) m) i hi2]

/-- Agreement of two words on the first `m` positions. -/
def Agree (u v : List Bool) (m : ℕ) : Prop := ∀ i, i < m → u.getD i false = v.getD i false

theorem agree_append_left (p u v : List Bool) (m : ℕ) (h : Agree u v m) :
    Agree (p ++ u) (p ++ v) (p.length + m) := by
  intro i hi
  rcases lt_or_ge i p.length with hp | hp
  · rw [List.getD_append _ _ _ _ hp, List.getD_append _ _ _ _ hp]
  · rw [List.getD_append_right _ _ _ _ hp, List.getD_append_right _ _ _ _ hp]
    exact h _ (by omega)

theorem agree_symm (u v : List Bool) (m : ℕ) (h : Agree u v m) : Agree v u m :=
  fun i hi => (h i hi).symm

/-- **Near-commutation of standard words**: `std (n+1) ++ std n` and `std n ++ std (n+1)` agree except on their
last two letters. -/
theorem std_near_comm (d : ℕ → ℕ) : ∀ n,
    Agree (std d (n + 1) ++ std d n) (std d n ++ std d (n + 1)) ((std d (n + 1)).length + (std d n).length - 2)
  | 0 => by intro i hi; simp [std] at hi
  | n + 1 => by
    rw [show n + 1 + 1 = n + 2 by ring, std_succ_succ]
    -- (wpow s (d n) ++ std n) ++ s  vs  s ++ (wpow s (d n) ++ std n), where s = std (n+1)
    have e1 : wpow (std d (n + 1)) (d n) ++ std d n ++ std d (n + 1) =
        wpow (std d (n + 1)) (d n) ++ (std d n ++ std d (n + 1)) := by rw [List.append_assoc]
    have e2 : std d (n + 1) ++ (wpow (std d (n + 1)) (d n) ++ std d n) =
        wpow (std d (n + 1)) (d n) ++ (std d (n + 1) ++ std d n) := by
      rw [← List.append_assoc, wpow_comm, List.append_assoc]
    rw [e1, e2]
    have ih := agree_symm _ _ _ (std_near_comm d n)
    have h := agree_append_left (wpow (std d (n + 1)) (d n)) _ _ _ ih
    have hl : (wpow (std d (n + 1)) (d n) ++ std d n).length + (std d (n + 1)).length - 2 =
        (wpow (std d (n + 1)) (d n)).length + ((std d (n + 1)).length + (std d n).length - 2) := by
      rw [List.length_append]
      have := std_length_pos d n; have := std_length_pos d (n + 1); omega
    rw [hl]; exact h

theorem prefix_agree (B A W : List Bool) (h : A <+: W) : Agree (B ++ A) (B ++ W) (B.length + A.length) := by
  apply agree_append_left
  intro i hi
  exact (getD_of_prefix h i hi).symm

/-- **The near-square at the start.** For every `n`, the characteristic word agrees with its shift by
`|std d (n + 1)|` on the first `|std d (n + 1)| - 2` positions: a near-square at the pair `(0, |std d (n + 1)|)`
with slack `2`. -/
theorem cw_near_square (d : ℕ → ℕ) (hd : ∀ n, 1 ≤ d n) (n s : ℕ) (hs : s + 2 < (std d (n + 1)).length) :
    cw d s = cw d ((std d (n + 1)).length + s) := by
  have hBpos := std_length_pos d n
  have hleft : cw d s = (std d (n + 1)).getD s false := cw_eq d hd n s (by omega)
  obtain ⟨a, ha⟩ : ∃ a, d n = a + 1 := ⟨d n - 1, by have := hd n; omega⟩
  rcases a with _ | a
  · -- `d n = 1`: `std d (n + 2) = A ++ B`; read the shifted position inside `(A ++ B) ++ W` with `A <+: W`
    have h2 : std d (n + 2) = std d (n + 1) ++ std d n := by
      rw [std_succ_succ, ha, wpow_succ]; simp [wpow]
    obtain ⟨b, hb⟩ : ∃ b, d (n + 1) = b + 1 := ⟨d (n + 1) - 1, by have := hd (n + 1); omega⟩
    have hW : std d (n + 1) <+: wpow (std d (n + 2)) b ++ std d (n + 1) := by
      rcases b with _ | b
      · simp [wpow]
      · rw [wpow_succ, List.append_assoc]
        exact (std_prefix d hd n).trans (List.prefix_append _ _)
    have h3 : std d (n + 3) = (std d (n + 1) ++ std d n) ++ (wpow (std d (n + 2)) b ++ std d (n + 1)) := by
      rw [show n + 3 = (n + 1) + 2 by ring, std_succ_succ, show n + 1 + 1 = n + 2 by ring, hb, wpow_succ,
        List.append_assoc]
      nth_rewrite 1 [h2]; rfl
    have hlen : (std d (n + 1)).length + s < (std d (n + 3)).length := by
      rw [h3, List.length_append, List.length_append]
      have := hW.length_le; omega
    rw [cw_eq d hd (n + 2) _ hlen, h3, List.append_assoc,
      List.getD_append_right _ _ _ _ (by omega), Nat.add_sub_cancel_left,
      ← prefix_agree (std d n) (std d (n + 1)) _ hW s (by omega),
      ← (std_near_comm d n) s (by omega), List.getD_append _ _ _ _ (by omega), hleft]
  · -- `d n ≥ 2`: `std d (n + 2) = A ++ (A ++ …)`, the shifted position is in the second copy of `A`
    have h2 : std d (n + 2) = std d (n + 1) ++ (std d (n + 1) ++ (wpow (std d (n + 1)) a ++ std d n)) := by
      rw [std_succ_succ, ha, wpow_succ, wpow_succ]; simp only [List.append_assoc]
    have hlen : (std d (n + 1)).length + s < (std d (n + 2)).length := by
      rw [h2, List.length_append, List.length_append]; omega
    rw [cw_eq d hd (n + 1) _ hlen, h2, List.getD_append_right _ _ _ _ (by omega), Nat.add_sub_cancel_left,
      List.getD_append _ _ _ _ (by omega), hleft]

/-! ## Every characteristic Sturmian word is excluded beside the clock -/

/-- **Every characteristic Sturmian word is excluded.** A configuration with a leftmost black cell, whose column
`0` reads the clock from time `0`, cannot have the characteristic word of any directive sequence `d` (every
`d n ≥ 1`) as its visible bits `evol x0 (2 i) 1`. -/
theorem characteristic_excluded (d : ℕ → ℕ) (hd : ∀ n, 1 ≤ d n) (x0 : ℤ → Bool) (L : ℕ)
    (hc : x0 (-(L : ℤ)) = true) (hl : ∀ j < -(L : ℤ), x0 j = false)
    (hclock : ∀ t, evol x0 t 0 = decide (t % 2 = 1)) (hvis : ∀ i, evol x0 (2 * i) 1 = cw d i) : False := by
  have hL : 1 ≤ L := by
    by_contra h0
    have hL0 : L = 0 := by omega
    subst hL0
    have h := hclock 0
    rw [show evol x0 0 0 = x0 0 from rfl] at h
    have hc0 : x0 0 = true := by simpa using hc
    rw [hc0] at h
    exact absurd h (by decide)
  refine corollary_F x0 L hL hc hl 0 (fun t _ => hclock t) 2 (fun N => ?_)
  refine ⟨0, (std d (N + 1)).length, std_length_pos d (N + 1), by have := std_length_ge d hd N; omega,
    by omega, fun s hs => ?_⟩
  rw [hvis, hvis, Nat.zero_add]
  exact cw_near_square d hd N s hs

/-- The same with the letters exchanged (the characteristic words of the other slopes). -/
theorem characteristic_excluded_compl (d : ℕ → ℕ) (hd : ∀ n, 1 ≤ d n) (x0 : ℤ → Bool) (L : ℕ)
    (hc : x0 (-(L : ℤ)) = true) (hl : ∀ j < -(L : ℤ), x0 j = false)
    (hclock : ∀ t, evol x0 t 0 = decide (t % 2 = 1)) (hvis : ∀ i, evol x0 (2 * i) 1 = !cw d i) : False := by
  have hL : 1 ≤ L := by
    by_contra h0
    have hL0 : L = 0 := by omega
    subst hL0
    have h := hclock 0
    rw [show evol x0 0 0 = x0 0 from rfl] at h
    have hc0 : x0 0 = true := by simpa using hc
    rw [hc0] at h
    exact absurd h (by decide)
  refine corollary_F x0 L hL hc hl 0 (fun t _ => hclock t) 2 (fun N => ?_)
  refine ⟨0, (std d (N + 1)).length, std_length_pos d (N + 1), by have := std_length_ge d hd N; omega,
    by omega, fun s hs => ?_⟩
  rw [hvis, hvis, Nat.zero_add, cw_near_square d hd N s hs]

/-- The Fibonacci word, `d n = 1` for every `n`, as the first example. -/
theorem fibonacci_excluded (x0 : ℤ → Bool) (L : ℕ) (hc : x0 (-(L : ℤ)) = true) (hl : ∀ j < -(L : ℤ), x0 j = false)
    (hclock : ∀ t, evol x0 t 0 = decide (t % 2 = 1)) (hvis : ∀ i, evol x0 (2 * i) 1 = cw (fun _ => 1) i) :
    False :=
  characteristic_excluded (fun _ => 1) (fun _ => le_rfl) x0 L hc hl hclock hvis

end Rule30Submission
