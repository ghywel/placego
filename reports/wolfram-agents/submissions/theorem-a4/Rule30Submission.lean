import Rule30PrizeKit
import Mathlib

/-!
# Theorem A⁗: a repeat on the center column cannot put its white run inside the settled band of left diagonals

**A partial result for Problem 1.** Jen's theorem with a clock (the kit's `Rule30MaskedJen.window_jen_col`, and
`Rule30FiniteMaskedJen.window_jen_col` for any configuration with a leftmost black cell; the record's Theorem A′) says: if columns `i` and `i + 1` carry equal blocks of length `n` at times `a < a′`, and the leftmost
black cell is `L` cells left of column `i`, then `n ≤ L + a′`. The reason is a white run: row `a′` is white at the
distances `L + a + 1 … n - 1` left of column `i` (`theorem_A3_white`), which, read as left diagonals
`D k t = evol x0 t (e - t + k)` from the moving edge `e`, are the diagonals `L + a′ - n + 1 … a′ - a - 1` at
time `a′`. This module proves that the run cannot lie in the band of diagonals that has settled:

* **Theorem A⁗** (`theorem_A4_sharp`, `theorem_A4`): if, in addition, the diagonals `0 … M` agree at times `a′ - P` and
  `a′` (a common period `P ≥ 1`, `P ≤ a′`) and `M < a′ - a`, then `n ≤ L + a′ - M + 2P - 1`. The gain over Theorem
  A′ is `M - 2P + 1`: the settled band of width `M` pushes a repeat's white run out, up to a margin of `2P - 1`.
* **For the seed** (`center_A4_sharp`, `center_A4`): the same for the center column `cell t 0` and the kit's
  `Rule30Diagonals.D`, with `L = 0`: `n ≤ a′ - M + 2P - 1`.
* **Lemma B3, sharp** (`lemma_B3_sharp`): inside a band of diagonals `0 … M` that has had period `P` for `P` steps,
  a white run of the row bounded on the left by a black diagonal is at most `2P - 1` long. Theorem A⁗ is Lemma B3
  applied to Theorem A‴'s run, whose nearest black diagonal on the left exists because diagonal `0`, the edge, is
  black.

**What is new relative to the kit.** The kit has Jen's theorem with the clock (`window_jen_col`, the bound `n ≤ L + a′`)
and the period-`2^j` upper bound for each left diagonal (`Rule30Diagonals.D_periodic`), but no statement joining the
two: nothing about where a repeat's white run can sit relative to the settled band. Theorem A‴, Lemma B3 and
Theorem A⁗ are the record's. Nothing here decides Problem 1: the diagonals the run reaches have periods up to
`2^(a′ - a)`, far above `a′ - a`, so the hypothesis `hper` is not known to hold for the center column's own repeats.

**Provenance.** PROOFS.md entries 10, 12 and 13 of the Wolfram · Collatz · Mahler record (github.com/ghywel/placego):
Theorem A‴ and A⁗ proved by Local (Claude) on 2026-10-05 and 2026-10-06 (RULE30-PRIZE.md §8.59), second-read by
Cloud and GPT, machine-checked by Local on 2026-10-10 (`tests/probes/lean/TheoremA4.lean`); restated here on the
kit's `evol` and `cell` by Cloud on 2026-10-23, with the bridge to `Rule30Diagonals.D`. Source: E. Jen, J. Stat.
Phys. 43 (1986).
-/

set_option Elab.async false

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30Jen
open Ruliology.CellularAutomata.Rule30Prize
open Ruliology.CellularAutomata.Rule30Realization


lemma evol_succ (x0 : ℤ → Bool) (t : ℕ) (i : ℤ) :
    evol x0 (t + 1) i = xor (evol x0 t (i - 1)) (evol x0 t i || evol x0 t (i + 1)) := rfl

/-- Fact 2 : the leftmost black cell moves left one cell a step. -/
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

/-- Diagonal j at time t. -/
def D (x0 : ℤ → Bool) (e : ℤ) (j : ℤ) (t : ℕ) : Bool := evol x0 t (e - t + j)

lemma D_succ (x0 : ℤ → Bool) (e j : ℤ) (t : ℕ) :
    D x0 e j (t + 1) = xor (D x0 e (j - 2) t) (D x0 e (j - 1) t || D x0 e j t) := by
  unfold D
  rw [evol_succ]
  rw [show e - ((t + 1 : ℕ) : ℤ) + j - 1 = e - t + (j - 2) by push_cast; ring,
    show e - ((t + 1 : ℕ) : ℤ) + j = e - t + (j - 1) by push_cast; ring,
    show e - (t : ℤ) + (j - 1) + 1 = e - t + j by ring]

/-- A white cell at time τ + 1 forces D_(k-2) = D_(k-1) or D_k at time τ. -/
lemma constraint (x0 : ℤ → Bool) (e k : ℤ) (τ : ℕ) (h : D x0 e k (τ + 1) = false) :
    D x0 e (k - 2) τ = (D x0 e (k - 1) τ || D x0 e k τ) := by
  rw [D_succ] at h
  revert h
  cases D x0 e (k - 2) τ <;> cases (D x0 e (k - 1) τ || D x0 e k τ) <;> simp

/-- One step back from a white run bounded by a black cell: older (white two wider, black two further left), or
newborn (black on [g - 1, M' - 2], and black at M' - 1 or M'). -/
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

/-- Forward: a white run only loses cells from its left side, two a step. -/
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

/-- Lemma B3, sharp: the run is at most 2P - 1 long. The newborn case's black cell at M' - 1 or M' stops the
forward white range one cell earlier than entry 12's black range [g - 2s0 - 1, M' - 2] does. -/
theorem lemma_B3_sharp (x0 : ℤ → Bool) (e : ℤ) (t P : ℕ) (g M' M : ℤ) (hP : 1 ≤ P) (htP : P ≤ t) (hgM : g + 1 ≤ M')
    (hM : M' ≤ M) (hper : ∀ k, k ≤ M → D x0 e k (t - P) = D x0 e k t) (hg : D x0 e g t = true)
    (hw : ∀ k, g + 1 ≤ k → k ≤ M' → D x0 e k t = false) : M' - g ≤ 2 * P - 1 := by
  -- the older chain: A s, for s <= P, unless a birth (newborn case) happens first
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
  -- A P contradicts periodicity at the black cell g
  rcases chain P le_rfl with hA | ⟨s0, hs0, hB⟩
  · exfalso
    have := hA.1 g (by omega) (by omega)
    rw [hper g (by omega), hg] at this
    exact absurd this (by decide)
  · -- forward from t - P the run is white on [g + 1 + 2r, M'] at time t - P + r; at the birth time it would
    -- cover both M' - 1 and M', one of which is black
    obtain ⟨-, hBt⟩ := hB
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

/-- Lemma B3 (entry 12's bound 2P), from the sharp form. -/
theorem lemma_B3 (x0 : ℤ → Bool) (e : ℤ) (t P : ℕ) (g M' M : ℤ) (hP : 1 ≤ P) (htP : P ≤ t) (hgM : g + 1 ≤ M')
    (hM : M' ≤ M) (hper : ∀ k, k ≤ M → D x0 e k (t - P) = D x0 e k t) (hg : D x0 e g t = true)
    (hw : ∀ k, g + 1 ≤ k → k ≤ M' → D x0 e k t = false) : M' - g ≤ 2 * P := by
  have := lemma_B3_sharp x0 e t P g M' M hP htP hgM hM hper hg hw
  omega

/-- Theorem A⁗, sharp (from `lemma_B3_sharp`). -/
theorem theorem_A4_sharp (x0 : ℤ → Bool) (i : ℤ) (L : ℕ) (hc : x0 (i - L) = true) (hl : ∀ j < i - L, x0 j = false)
    (n a a' P : ℕ) (M : ℤ) (haa : a < a') (hP : 1 ≤ P) (hPa : P ≤ a') (hMa : M < (a' : ℤ) - a)
    (hblock : ∀ s : ℕ, s < n → evol x0 (a + s) i = evol x0 (a' + s) i ∧ evol x0 (a + s) (i + 1) = evol x0 (a' + s) (i + 1))
    (hper : ∀ k, k ≤ M → D x0 (i - L) k (a' - P) = D x0 (i - L) k a') :
    (n : ℤ) ≤ L + a' - M + 2 * P - 1 := by
  by_contra hlong
  push Not at hlong
  set e : ℤ := i - L with he
  -- A′: n ≤ L + a′, so the run's left end x = L + a′ - n + 1 is at least 1
  have hA' := theorem_A' x0 i L hc hl n a a' haa hblock
  -- the white run of A‴ in diagonal coordinates at time a′: diagonals x .. M
  set x : ℤ := (L : ℤ) + a' - n + 1 with hx
  have white : ∀ k, x ≤ k → k ≤ M → D x0 e k a' = false := by
    intro k h1 h2
    have hk : 0 ≤ (L : ℤ) + a' - k := by omega
    have := theorem_A3_white x0 i L hc hl n a a' hblock ((L : ℤ) + a' - k).toNat (by omega) (by omega)
    unfold D
    rw [show e - (a' : ℤ) + k = i - (((L : ℤ) + a' - k).toNat : ℤ) by rw [he, Int.toNat_of_nonneg hk]; ring]
    exact this
  -- the edge diagonal 0 is black at a′
  have black0 : D x0 e 0 a' = true := by
    unfold D; simpa using (edge x0 e (by rw [he]; exact hc) (by rw [he]; exact hl) a').1
  -- the nearest black diagonal g < x
  have hx1 : 1 ≤ x := by omega
  obtain ⟨g, hg0, hgx, hgb, hgw⟩ : ∃ g : ℤ, 0 ≤ g ∧ g < x ∧ D x0 e g a' = true ∧
      ∀ k, g + 1 ≤ k → k ≤ x - 1 → D x0 e k a' = false := by
    -- search down from x - 1 to 0
    have key : ∀ m : ℕ, ∀ y : ℤ, y = m → y ≤ x - 1 → (∀ k, y + 1 ≤ k → k ≤ x - 1 → D x0 e k a' = false) →
        ∃ g : ℤ, 0 ≤ g ∧ g < x ∧ D x0 e g a' = true ∧ ∀ k, g + 1 ≤ k → k ≤ x - 1 → D x0 e k a' = false := by
      intro m
      induction m with
      | zero =>
        intro y hy hyx hw
        exact ⟨0, le_rfl, by omega, black0, fun k h1 h2 => hw k (by omega) h2⟩
      | succ m ih =>
        intro y hy hyx hw
        by_cases hb : D x0 e y a' = true
        · exact ⟨y, by omega, by omega, hb, hw⟩
        · apply ih (y - 1) (by push_cast at hy; omega) (by omega)
          intro k h1 h2
          rcases (show k = y ∨ y + 1 ≤ k by omega) with h | h
          · subst h; simpa using hb
          · exact hw k h h2
    exact key (x - 1).toNat (x - 1) (by omega) le_rfl (fun k h1 h2 => by omega)
  -- Lemma B3 on the run [g + 1, M]
  have hB3 := lemma_B3_sharp x0 e a' P g M M hP hPa (by omega) le_rfl hper hgb (fun k h1 h2 => by
    rcases (show k ≤ x - 1 ∨ x ≤ k by omega) with h | h
    · exact hgw k h1 h
    · exact white k h h2)
  omega

/-- Theorem A⁗ (entry 13's bound), from the sharp form. -/
theorem theorem_A4 (x0 : ℤ → Bool) (i : ℤ) (L : ℕ) (hc : x0 (i - L) = true) (hl : ∀ j < i - L, x0 j = false)
    (n a a' P : ℕ) (M : ℤ) (haa : a < a') (hP : 1 ≤ P) (hPa : P ≤ a') (hMa : M < (a' : ℤ) - a)
    (hblock : ∀ s : ℕ, s < n → evol x0 (a + s) i = evol x0 (a' + s) i ∧ evol x0 (a + s) (i + 1) = evol x0 (a' + s) (i + 1))
    (hper : ∀ k, k ≤ M → D x0 (i - L) k (a' - P) = D x0 (i - L) k a') :
    (n : ℤ) ≤ L + a' - M + 2 * P := by
  have := theorem_A4_sharp x0 i L hc hl n a a' P M haa hP hPa hMa hblock hper
  omega

/-! ## The bridge to the kit's statements: the center column and `Rule30Diagonals.D` -/

lemma seed_leftmost : seed 0 = true ∧ ∀ p : ℤ, p < 0 → seed p = false := by
  refine ⟨by simp [seed], fun p hp => ?_⟩
  simp only [seed, decide_eq_false_iff_not]; omega

/-- Our diagonal `D seed 0 j t` is the kit's `Rule30Diagonals.D j t = cell t (j - t)`. -/
lemma D_seed (j t : ℕ) : D seed 0 (j : ℤ) t = Rule30Diagonals.D j t := by
  simp only [D, Rule30Diagonals.D, evol_seed]
  congr 1; ring

/-- Left of the edge every diagonal is white. -/
lemma D_seed_neg (k : ℤ) (hk : k < 0) (t : ℕ) : D seed 0 k t = false := by
  unfold D
  exact (edge seed 0 seed_leftmost.1 seed_leftmost.2 t).2 _ (by omega)

/-- The periodicity hypothesis of the kit's diagonals, for `0 ≤ k ≤ M`, gives the module's for every `k ≤ M`. -/
lemma per_seed (P a' : ℕ) (M : ℤ)
    (hper : ∀ k : ℕ, (k : ℤ) ≤ M → Rule30Diagonals.D k (a' - P) = Rule30Diagonals.D k a') :
    ∀ k : ℤ, k ≤ M → D seed 0 k (a' - P) = D seed 0 k a' := by
  intro k hk
  rcases lt_or_ge k 0 with hneg | hnn
  · rw [D_seed_neg k hneg, D_seed_neg k hneg]
  · obtain ⟨m, rfl⟩ : ∃ m : ℕ, k = m := ⟨k.toNat, by omega⟩
    rw [D_seed, D_seed]; exact hper m hk

/-- **Theorem A⁗ for the center column, sharp.** Equal blocks of length `n` on columns `0` and `1` at times
`a < a′`, and the kit's left diagonals `0 … M` agreeing at times `a′ - P` and `a′` with `M < a′ - a`: then
`n ≤ a′ - M + 2P - 1`. -/
theorem center_A4_sharp (n a a' P : ℕ) (M : ℤ) (haa : a < a') (hP : 1 ≤ P) (hPa : P ≤ a') (hMa : M < (a' : ℤ) - a)
    (hblock : ∀ s : ℕ, s < n → cell (a + s) 0 = cell (a' + s) 0 ∧ cell (a + s) 1 = cell (a' + s) 1)
    (hper : ∀ k : ℕ, (k : ℤ) ≤ M → Rule30Diagonals.D k (a' - P) = Rule30Diagonals.D k a') :
    (n : ℤ) ≤ a' - M + 2 * P - 1 := by
  have h := theorem_A4_sharp seed 0 0 (by simpa using seed_leftmost.1) (by simpa using seed_leftmost.2)
    n a a' P M haa hP hPa hMa (fun s hs => by simpa [evol_seed] using hblock s hs)
    (by simpa using per_seed P a' M hper)
  simpa using h

/-- **Theorem A⁗ for the center column** (the record's bound `2P`). -/
theorem center_A4 (n a a' P : ℕ) (M : ℤ) (haa : a < a') (hP : 1 ≤ P) (hPa : P ≤ a') (hMa : M < (a' : ℤ) - a)
    (hblock : ∀ s : ℕ, s < n → cell (a + s) 0 = cell (a' + s) 0 ∧ cell (a + s) 1 = cell (a' + s) 1)
    (hper : ∀ k : ℕ, (k : ℤ) ≤ M → Rule30Diagonals.D k (a' - P) = Rule30Diagonals.D k a') :
    (n : ℤ) ≤ a' - M + 2 * P := by
  have := center_A4_sharp n a a' P M haa hP hPa hMa hblock hper
  omega

end Rule30Submission
