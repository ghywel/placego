import Rule30PrizeKit
import Mathlib

/-!
# Rule 210: no finite configuration keeps the period-2 clock on its center column

**Barrier material for Problem 1, the two-sided statement for rule 210.** Submission 6 (R30-20261022-920c1b) showed
that the kit's one-sided period-2 question `Q01` is *false* for rule 210, the one nonlinear left-permutive sibling of
rule 30 (`left xor (!center && right)`, the kit's `g210`): the empty left half keeps the clock. This module proves
the two-sided statement *true* for rule 210: **no finite configuration `x0 : ℤ → Bool` has a center column reading
the clock `0101…`** (`no_finite_clock`), nor one that is eventually alternating in either phase
(`no_finite_eventually_alternating`); for the kit's single seed, `seed_not_eventually_alternating` through the bridge
`run210_seed : run210 seed = run g210`. So for rule 210 the gap between the one-sided and the two-sided period-2
statements is real, which is an argument for attacking rule 30's two-sided forms (`Rule30PeriodTwo`,
`Rule30PeriodTwoSideways`) rather than `Q01` alone.

**The proof** (the record's Proposition 19, PROOFS.md entry 32: GPT's clearing-front argument GC478, second-read by
Local L285, laid out for formalization in GPT's chain GC1700):
* **Parity (P1, P2).** On a configuration white at the even sites every black cell `(t, i)` has `t + i` odd and the
  gate `!center && right` is `right`: rule 210 is rule 90 there (`parity_of_even_white`, `rule90_of_even_white`).
  Under the clock the whole left half is parity-sparse whatever the right half (`parity_left_of_clock`, by strong
  induction on the depth with left-permutivity), so the left row is white at `0` and at the even depths.
* **The background (B).** For every admissible left row `L` a parity-sparse clock realization `bg L` is built
  sideways from the clock: the left half by the Dirichlet evolution with the clock at the wall (`lft`), the right
  columns by rule 90's right-permutivity (`colR`); `run90_bg` shows it evolves as built, `bg_even_white` its parity,
  `clock_bg` its clock. This replaces the explicit residue-class background of the hand proof.
* **The freshman's dream.** Rule 90 is linear and `run90 x0 (2^n) i = x0 (i - 2^n) xor x0 (i + 2^n)`
  (`run90_pow2`), so a finite parity-sparse configuration is white at the center at time `2^n + 1` beyond its support,
  while the clock is black there (`no_finite_clock90`).
* **The deviation (F, W, C).** A clock orbit with left row `L` that first differs from `bg L` at `e ≥ 1`: if `e` is odd
  the two orbits differ on the diagonal `e` for ever and so at its clock time (`Dev.odd_impossible`); if `e` is even,
  the deviation's even diagonal is black until the gate `bb` left of it first fires at `τ ≤ e - 1` and white after
  (`P0_before`, `P0_after`), the background's odd gates `Ab j` beyond `e` keep their initial values through `τ + j`
  and flip at `τ + j + 1` (`W1_const`, `W1_flip`), a clearing witness and a `01` front propagate pair by pair
  (`marker`, `propagate`, `front`), the candidate's odd diagonals then differ from the background's by exactly the
  background's initial gate values (`identify`), and at the first initially black gate `w` the candidate's clock
  fails at time `e + 2w + 1` (`Dev.even_impossible`). If no gate beyond `e` is black, the background is finite and
  the freshman's dream applies to it.
* **Phase.** A clock from time `T` in either phase is a clock from time `0` for the configuration at an even or odd
  later time, which is still finite (`run210_add`, `finite_run210`).

**What is new relative to the kit.** The kit's `Rule30Realization.barrier` is about the seed's center column of rules
90, 150 and 210 being eventually constant. This is the period-2 question itself for rule 210 in its two-sided form,
answered yes, next to submission 6's one-sided no. Nothing here is about rule 30's center column.

**Provenance.** PROOFS.md entry 32 of the Wolfram · Collatz · Mahler record (github.com/ghywel/placego): the
clearing-front proof is GPT's (GC478, 2026-10-08), the conjectured life law and the finite instruments Local's (L282,
L285); GPT's formalization chain GC1700 (reports/wolfram-agents/GPT-PROOFS32-CHAIN.md, 2026-10-23) with its bounded
controls (10,880 abstract cases, 3,136 actual-orbit tails, 8,192 seeds). Formalized by Cloud (Claude) on 2026-10-23,
with the sideways background and the freshman's dream in place of the chain's residue-class arithmetic. Source:
E. Jen, J. Stat. Phys. 43 (1986), for left-permutivity.
-/

set_option Elab.async false

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30Realization

/-! ## Rule 210 on a general configuration -/

/-- Rule 210, `left xor (!center && right)`, from any configuration. The kit's `run g210` is the single seed. -/
def run210 (x0 : ℤ → Bool) : ℕ → ℤ → Bool
  | 0, i => x0 i
  | t + 1, i => xor (run210 x0 t (i - 1)) (!(run210 x0 t i) && run210 x0 t (i + 1))

theorem run210_succ (x0 : ℤ → Bool) (t : ℕ) (i : ℤ) :
    run210 x0 (t + 1) i = xor (run210 x0 t (i - 1)) (!(run210 x0 t i) && run210 x0 t (i + 1)) := rfl

/-- The kit's single-seed `run g210` is `run210` from the seed. -/
theorem run210_seed : ∀ t p, run210 (fun p => decide (p = 0)) t p = run g210 t p
  | 0, p => rfl
  | t + 1, p => by
    rw [run210_succ]
    show _ = xor (run g210 t (p - 1)) (g210 (run g210 t p) (run g210 t (p + 1)))
    rw [run210_seed t (p - 1), run210_seed t p, run210_seed t (p + 1)]; rfl

/-- The center column reads the clock, white at even times. -/
def Clock210 (x0 : ℤ → Bool) : Prop := ∀ t : ℕ, run210 x0 t 0 = decide (t % 2 = 1)

/-- The left diagonal `c`: the cell `c - s` at time `s`. -/
def Diag210 (x0 : ℤ → Bool) (c : ℤ) (s : ℕ) : Bool := run210 x0 s (c - (s : ℤ))

def FinLeft210 (x0 : ℤ → Bool) : Prop := ∃ R : ℕ, ∀ i : ℤ, i < -(R : ℤ) → x0 i = false

def Finite210 (x0 : ℤ → Bool) : Prop := ∃ R : ℕ, ∀ i : ℤ, (R : ℤ) < |i| → x0 i = false

/-- **D1.** The diagonal recursion. -/
theorem diag_succ (x0 : ℤ → Bool) (c : ℤ) (s : ℕ) :
    Diag210 x0 c (s + 1) = xor (Diag210 x0 (c - 2) s) (!(Diag210 x0 (c - 1) s) && Diag210 x0 c s) := by
  unfold Diag210
  rw [run210_succ]
  have e1 : c - ((s + 1 : ℕ) : ℤ) - 1 = (c - 2) - (s : ℤ) := by push_cast; ring
  have e2 : c - ((s + 1 : ℕ) : ℤ) = (c - 1) - (s : ℤ) := by push_cast; ring
  have e3 : c - ((s + 1 : ℕ) : ℤ) + 1 = c - (s : ℤ) := by push_cast; ring
  rw [e1, e3, e2]

theorem diag_zero (x0 : ℤ → Bool) (c : ℤ) : Diag210 x0 c 0 = x0 c := by simp [Diag210, run210]

/-- **D2.** Left locality: agreement of the initial rows left of `e` gives agreement of every diagonal left of `e`. -/
theorem diag_local (x0 y0 : ℤ → Bool) (e : ℤ) (h : ∀ i, i < e → x0 i = y0 i) :
    ∀ s, ∀ c, c < e → Diag210 x0 c s = Diag210 y0 c s := by
  intro s
  induction s with
  | zero => intro c hc; rw [diag_zero, diag_zero]; exact h c hc
  | succ s ih =>
    intro c hc
    rw [diag_succ, diag_succ, ih (c - 2) (by omega), ih (c - 1) (by omega), ih c hc]

/-- The light cone: the cell `i` at time `t` depends on the initial sites in `[i - t, i + t]`. -/
theorem run210_cone (x0 y0 : ℤ → Bool) : ∀ t : ℕ, ∀ i : ℤ,
    (∀ j, i - t ≤ j → j ≤ i + t → x0 j = y0 j) → run210 x0 t i = run210 y0 t i := by
  intro t
  induction t with
  | zero => intro i h; simpa [run210] using h i (by simp) (by simp)
  | succ t ih =>
    intro i h
    rw [run210_succ, run210_succ,
      ih (i - 1) (fun j h1 h2 => h j (by push_cast at h1 ⊢; omega) (by push_cast at h2 ⊢; omega)),
      ih i (fun j h1 h2 => h j (by push_cast at h1 ⊢; omega) (by push_cast at h2 ⊢; omega)),
      ih (i + 1) (fun j h1 h2 => h j (by push_cast at h1 ⊢; omega) (by push_cast at h2 ⊢; omega))]

/-! ## Parity: the forced left half -/

/-- **P1.** From a configuration white on the even sites, every black cell `(t, i)` has `t + i` odd. -/
theorem parity_of_even_white (x0 : ℤ → Bool) (h : ∀ i, i % 2 = 0 → x0 i = false) :
    ∀ t : ℕ, ∀ i : ℤ, run210 x0 t i = true → ((t : ℤ) + i) % 2 = 1 := by
  intro t
  induction t with
  | zero =>
    intro i hi
    by_contra hne
    have : i % 2 = 0 := by omega
    have := h i this
    simp [run210] at hi
    rw [hi] at this; exact absurd this (by decide)
  | succ t ih =>
    intro i hi
    rw [run210_succ] at hi
    by_cases hl : run210 x0 t (i - 1) = true
    · have := ih (i - 1) hl; push_cast; omega
    · have hl' : run210 x0 t (i - 1) = false := by simpa using hl
      rw [hl'] at hi
      have hr : run210 x0 t (i + 1) = true := by
        revert hi; cases run210 x0 t i <;> cases run210 x0 t (i + 1) <;> simp
      have := ih (i + 1) hr; push_cast; omega

/-- **P1′.** On such an orbit the gate is rule 90's: `left xor right`. -/
theorem rule90_of_even_white (x0 : ℤ → Bool) (h : ∀ i, i % 2 = 0 → x0 i = false) (t : ℕ) (i : ℤ) :
    run210 x0 (t + 1) i = xor (run210 x0 t (i - 1)) (run210 x0 t (i + 1)) := by
  rw [run210_succ]
  have : (!(run210 x0 t i) && run210 x0 t (i + 1)) = run210 x0 t (i + 1) := by
    by_cases hr : run210 x0 t (i + 1) = true
    · have hc : run210 x0 t i = false := by
        by_contra hne
        have h1 := parity_of_even_white x0 h t i (by simpa using hne)
        have h2 := parity_of_even_white x0 h t (i + 1) hr
        omega
      rw [hc, hr]; rfl
    · have hr' : run210 x0 t (i + 1) = false := by simpa using hr
      rw [hr']; simp
  rw [this]

/-- **P2.** Under the clock, every black cell `(t, i)` with `i ≤ 0` has `t + i` odd: the left half is parity-sparse,
whatever the right half. By strong induction on the depth `-i`, with left-permutivity. -/
theorem parity_left_of_clock (x0 : ℤ → Bool) (hc : Clock210 x0) :
    ∀ k : ℕ, ∀ t : ℕ, run210 x0 t (-(k : ℤ)) = true → ((t : ℤ) - k) % 2 = 1 := by
  intro k
  induction k using Nat.strong_induction_on with
  | _ k ih =>
    intro t h
    rcases k with _ | _ | k
    · -- depth 0: the clock
      have := hc t
      simp only [Nat.cast_zero, neg_zero] at h
      rw [this] at h
      simp only [decide_eq_true_eq] at h
      omega
    · -- depth 1: at odd `t` the clock is black and the next clock bit white forces column `-1` white
      by_contra hpar
      have hodd : t % 2 = 1 := by omega
      have h0 : run210 x0 t 0 = true := by rw [hc t]; simp [hodd]
      have h1 : run210 x0 (t + 1) 0 = false := by rw [hc (t + 1)]; simp; omega
      rw [run210_succ, h0] at h1
      simp only [zero_sub, zero_add] at h1
      rw [show (-((0 + 1 : ℕ) : ℤ)) = -1 by norm_num] at h
      rw [h] at h1
      simp at h1
    · -- depth k + 2: left-permutivity at column -(k+1)
      have hinv := run210_succ x0 t (-((k + 1 : ℕ) : ℤ))
      -- hinv : run (t+1) (-(k+1)) = xor (run t (-(k+1) - 1)) (!(run t (-(k+1))) && run t (-(k+1) + 1))
      have e1 : (-((k + 1 : ℕ) : ℤ)) - 1 = -((k + 1 + 1 : ℕ) : ℤ) := by push_cast; ring
      have e2 : (-((k + 1 : ℕ) : ℤ)) + 1 = -((k : ℕ) : ℤ) := by push_cast; ring
      rw [e1, e2] at hinv
      rw [h] at hinv
      -- hinv : run (t+1) (-(k+1)) = xor true (!(run t (-(k+1))) && run t (-k))
      by_cases hmid : run210 x0 t (-((k + 1 : ℕ) : ℤ)) = true
      · -- then run (t+1) (-(k+1)) = true, and parity at depth k+1, time t+1
        rw [hmid] at hinv
        have hinv' : run210 x0 (t + 1) (-((k + 1 : ℕ) : ℤ)) = true := by rw [hinv]; rfl
        have := ih (k + 1) (by omega) (t + 1) hinv'
        push_cast at this ⊢; omega
      · have hmid' : run210 x0 t (-((k + 1 : ℕ) : ℤ)) = false := by simpa using hmid
        rw [hmid'] at hinv
        by_cases hr : run210 x0 t (-((k : ℕ) : ℤ)) = true
        · have := ih k (by omega) t hr; push_cast at this ⊢; omega
        · have hr' : run210 x0 t (-((k : ℕ) : ℤ)) = false := by simpa using hr
          rw [hr'] at hinv
          have hinv' : run210 x0 (t + 1) (-((k + 1 : ℕ) : ℤ)) = true := by rw [hinv]; rfl
          have := ih (k + 1) (by omega) (t + 1) hinv'
          push_cast at this ⊢; omega

/-- **P2′.** Under the clock, the initial row is white at `0` and at every even negative site. -/
theorem left_row_of_clock (x0 : ℤ → Bool) (hc : Clock210 x0) (i : ℤ) (hi : i ≤ 0) (he : i % 2 = 0) :
    x0 i = false := by
  by_contra hne
  have hb : run210 x0 0 (-((-i).toNat : ℤ)) = true := by
    rw [show (-((-i).toNat : ℤ)) = i by omega]; simpa [run210] using hne
  have := parity_left_of_clock x0 hc (-i).toNat 0 hb
  omega

/-- **P3.** Two clock orbits with the same initial row on `i ≤ 0` agree on `i ≤ 0` for ever. -/
theorem left_det (x0 y0 : ℤ → Bool) (hx : Clock210 x0) (hy : Clock210 y0) (h : ∀ i, i ≤ 0 → x0 i = y0 i) :
    ∀ t : ℕ, ∀ i, i ≤ 0 → run210 x0 t i = run210 y0 t i := by
  intro t
  induction t with
  | zero => intro i hi; simpa [run210] using h i hi
  | succ t ih =>
    intro i hi
    rcases lt_or_eq_of_le hi with hlt | heq
    · rw [run210_succ, run210_succ, ih (i - 1) (by omega), ih i hi, ih (i + 1) (by omega)]
    · subst heq; rw [hx, hy]


/-! ## Rule 90: linearity, the semigroup, and the freshman's dream -/

def run90 (x0 : ℤ → Bool) : ℕ → ℤ → Bool
  | 0, i => x0 i
  | t + 1, i => xor (run90 x0 t (i - 1)) (run90 x0 t (i + 1))

theorem run90_succ (x0 : ℤ → Bool) (t : ℕ) (i : ℤ) :
    run90 x0 (t + 1) i = xor (run90 x0 t (i - 1)) (run90 x0 t (i + 1)) := rfl

theorem run90_zero (x0 : ℤ → Bool) (i : ℤ) : run90 x0 0 i = x0 i := rfl

theorem run90_one (x0 : ℤ → Bool) (i : ℤ) : run90 x0 1 i = xor (x0 (i - 1)) (x0 (i + 1)) := rfl

/-- On a configuration white at the even sites, rule 210 is rule 90. -/
theorem run210_eq_run90 (x0 : ℤ → Bool) (h : ∀ i, i % 2 = 0 → x0 i = false) :
    ∀ t i, run210 x0 t i = run90 x0 t i := by
  intro t
  induction t with
  | zero => intro i; rfl
  | succ t ih => intro i; rw [rule90_of_even_white x0 h, run90_succ, ih, ih]

/-- Linearity. -/
theorem run90_xor (x0 y0 : ℤ → Bool) : ∀ t i, run90 (fun j => xor (x0 j) (y0 j)) t i = xor (run90 x0 t i) (run90 y0 t i) := by
  intro t
  induction t with
  | zero => intro i; rfl
  | succ t ih =>
    intro i
    rw [run90_succ, run90_succ, run90_succ, ih, ih]
    cases run90 x0 t (i - 1) <;> cases run90 y0 t (i - 1) <;> cases run90 x0 t (i + 1) <;> cases run90 y0 t (i + 1) <;> rfl

/-- The semigroup property. -/
theorem run90_add (x0 : ℤ → Bool) (a : ℕ) : ∀ b i, run90 (run90 x0 a) b i = run90 x0 (a + b) i := by
  intro b
  induction b with
  | zero => intro i; rfl
  | succ b ih => intro i; rw [run90_succ, ih, ih, show a + (b + 1) = (a + b) + 1 by ring, run90_succ]

/-- Shifts commute with the rule. -/
theorem run90_shift (x0 : ℤ → Bool) (d : ℤ) : ∀ t i, run90 (fun j => x0 (j + d)) t i = run90 x0 t (i + d) := by
  intro t
  induction t with
  | zero => intro i; rfl
  | succ t ih =>
    intro i
    rw [run90_succ, run90_succ, ih, ih, show i - 1 + d = i + d - 1 by ring, show i + 1 + d = i + d + 1 by ring]

/-- **The freshman's dream:** at time `2^n` rule 90 is the sum of the two shifts by `2^n`. -/
theorem run90_pow2 (x0 : ℤ → Bool) : ∀ n : ℕ, ∀ i, run90 x0 (2 ^ n) i = xor (x0 (i - 2 ^ n)) (x0 (i + 2 ^ n)) := by
  intro n
  induction n with
  | zero => intro i; rw [pow_zero, run90_one]; simp
  | succ n ih =>
    intro i
    have e5 : (2 : ℤ) ^ (n + 1) = 2 ^ n + 2 ^ n := by ring
    rw [e5, pow_succ, show 2 ^ n * 2 = 2 ^ n + 2 ^ n by ring, ← run90_add]
    -- run90 (run90 x0 (2^n)) (2^n) i
    have hf : run90 x0 (2 ^ n) = fun j => xor (x0 (j - 2 ^ n)) (x0 (j + 2 ^ n)) := funext (ih)
    rw [hf]
    have hl : (fun j => xor (x0 (j - 2 ^ n)) (x0 (j + 2 ^ n))) =
        fun j => xor ((fun j => x0 (j + (-(2 ^ n : ℤ)))) j) ((fun j => x0 (j + (2 ^ n : ℤ))) j) := by
      funext j; simp [sub_eq_add_neg]
    rw [hl, run90_xor, run90_shift, run90_shift, ih, ih]
    push_cast
    have e1 : i + -(2 ^ n : ℤ) - 2 ^ n = i - (2 ^ n + 2 ^ n) := by ring
    have e2 : i + -(2 ^ n : ℤ) + 2 ^ n = i := by ring
    have e3 : i + (2 ^ n : ℤ) - 2 ^ n = i := by ring
    have e4 : i + (2 ^ n : ℤ) + 2 ^ n = i + (2 ^ n + 2 ^ n) := by ring
    rw [e1, e2, e3, e4]
    cases x0 (i - (2 ^ n + 2 ^ n)) <;> cases x0 i <;> cases x0 (i + (2 ^ n + 2 ^ n)) <;> rfl

/-- **No finite configuration keeps the clock under rule 90**: at time `2^n + 1` beyond the support, the center is
white, but the clock is black there. -/
theorem no_finite_clock90 (x0 : ℤ → Bool) (R : ℕ) (hR : ∀ i : ℤ, (R : ℤ) < |i| → x0 i = false)
    (hc : ∀ t : ℕ, run90 x0 t 0 = decide (t % 2 = 1)) : False := by
  obtain ⟨n, hn⟩ : ∃ n : ℕ, (R : ℤ) + 1 < 2 ^ n := by
    refine ⟨R + 1, ?_⟩
    have := Nat.lt_two_pow_self (n := R + 1)
    exact_mod_cast this
  have h := hc (2 ^ n + 1)
  have hodd : (2 ^ n + 1) % 2 = 1 := by
    have : 2 ^ n % 2 = 0 := by
      rcases n with _ | n
      · exact absurd hn (by norm_num)
      · rw [pow_succ]; simp
    omega
  rw [show 2 ^ n + 1 = 1 + 2 ^ n by ring, ← run90_add, run90_pow2] at h
  have hodd' : (1 + 2 ^ n) % 2 = 1 := by omega
  simp only [hodd', decide_true] at h
  rw [run90_one, run90_one] at h
  rw [hR _ (by rw [lt_abs]; right; push_cast; omega), hR _ (by rw [lt_abs]; right; push_cast; omega),
    hR _ (by rw [lt_abs]; left; push_cast; omega), hR _ (by rw [lt_abs]; left; push_cast; omega)] at h
  exact absurd h (by decide)


/-! ## The background: the parity realization of a left row, built sideways from the clock -/

/-- The clock, white at even times. -/
def clk (t : ℕ) : Bool := decide (t % 2 = 1)

/-- The left half driven by the clock at column `0`, from the left row `L` (depth `k` is position `-k`). -/
def lft (L : ℕ → Bool) : ℕ → ℤ → Bool
  | 0, i => if i < 0 then L (-i).toNat else false
  | t + 1, i => if i = 0 then clk (t + 1) else xor (lft L t (i - 1)) (lft L t (i + 1))

theorem lft_zero_pos (L : ℕ → Bool) (t : ℕ) : lft L t 0 = clk t := by
  cases t with
  | zero => simp [lft, clk]
  | succ t => simp [lft]

theorem lft_succ_neg (L : ℕ → Bool) (t : ℕ) (i : ℤ) (hi : i ≠ 0) :
    lft L (t + 1) i = xor (lft L t (i - 1)) (lft L t (i + 1)) := by
  simp [lft, hi]

/-- The columns to the right, by right-permutivity of rule 90: `colR (j+2) t = colR (j+1) (t+1) xor colR j t`. -/
def colR (L : ℕ → Bool) : ℕ → ℕ → Bool
  | 0, t => clk t
  | 1, t => xor (clk (t + 1)) (lft L t (-1))
  | j + 2, t => xor (colR L (j + 1) (t + 1)) (colR L j t)

/-- The background configuration and its intended space-time diagram. -/
def bgCol (L : ℕ → Bool) (t : ℕ) (i : ℤ) : Bool := if i ≤ 0 then lft L t i else colR L i.toNat t

def bg (L : ℕ → Bool) : ℤ → Bool := bgCol L 0

theorem bgCol_zero (L : ℕ → Bool) (t : ℕ) : bgCol L t 0 = clk t := by simp [bgCol, lft_zero_pos]

theorem bgCol_pos (L : ℕ → Bool) (t : ℕ) (j : ℕ) : bgCol L t ((j : ℤ) + 1) = colR L (j + 1) t := by
  simp [bgCol]

/-- **The background evolves as built**: rule 90 from `bg L` is `bgCol L`. -/
theorem run90_bg (L : ℕ → Bool) : ∀ t i, run90 (bg L) t i = bgCol L t i := by
  intro t
  induction t with
  | zero => intro i; rfl
  | succ t ih =>
    intro i
    rw [run90_succ, ih, ih]
    rcases lt_trichotomy i 0 with hneg | hzero | hpos
    · -- left of the center: the Dirichlet evolution
      have h1 : i - 1 ≤ 0 := by omega
      have h2 : i + 1 ≤ 0 := by omega
      simp only [bgCol, if_pos h1, if_pos h2, if_pos hneg.le]
      try rw [lft_succ_neg L t i hneg.ne]
    · subst hzero
      rw [bgCol_zero, show (0 : ℤ) - 1 = -1 by norm_num, show (0 : ℤ) + 1 = (0 : ℕ) + 1 by norm_num, bgCol_pos]
      simp only [bgCol, if_pos (by norm_num : (-1 : ℤ) ≤ 0)]
      show xor (lft L t (-1)) (xor (clk (t + 1)) (lft L t (-1))) = clk (t + 1)
      cases lft L t (-1) <;> cases clk (t + 1) <;> rfl
    · obtain ⟨j, rfl⟩ : ∃ j : ℕ, i = (j : ℤ) + 1 := ⟨(i - 1).toNat, by omega⟩
      rw [bgCol_pos, show (j : ℤ) + 1 + 1 = ((j + 1 : ℕ) : ℤ) + 1 by push_cast; ring, bgCol_pos,
        show (j : ℤ) + 1 - 1 = (j : ℤ) by ring]
      rcases j with _ | j
      · rw [Nat.cast_zero, bgCol_zero]
        show xor (clk t) (xor (colR L 1 (t + 1)) (clk t)) = colR L 1 (t + 1)
        cases clk t <;> cases colR L 1 (t + 1) <;> rfl
      · rw [show ((j + 1 : ℕ) : ℤ) = (j : ℤ) + 1 by push_cast; ring, bgCol_pos]
        show xor (colR L (j + 1) t) (xor (colR L (j + 2) (t + 1)) (colR L (j + 1) t)) = colR L (j + 2) (t + 1)
        cases colR L (j + 1) t <;> cases colR L (j + 2) (t + 1) <;> rfl

/-- An admissible left row: white at depth `0` and at every even depth. -/
def Admissible (L : ℕ → Bool) : Prop := ∀ k, k % 2 = 0 → L k = false

theorem lft_parity (L : ℕ → Bool) (hL : Admissible L) :
    ∀ t : ℕ, ∀ i : ℤ, i ≤ 0 → lft L t i = true → ((t : ℤ) + i) % 2 = 1 := by
  intro t
  induction t with
  | zero =>
    intro i hi h
    simp only [lft] at h
    split_ifs at h with hneg
    by_contra hpar
    have hk : (-i).toNat % 2 = 0 := by omega
    rw [hL _ hk] at h; exact absurd h (by decide)
  | succ t ih =>
    intro i hi h
    by_cases h0 : i = 0
    · subst h0; simp only [lft, if_true, clk, decide_eq_true_eq] at h; push_cast; omega
    · rw [lft_succ_neg L t i h0] at h
      by_cases hl : lft L t (i - 1) = true
      · have := ih (i - 1) (by omega) hl; push_cast; omega
      · have hl' : lft L t (i - 1) = false := by simpa using hl
        rw [hl'] at h
        have hr : lft L t (i + 1) = true := by revert h; cases lft L t (i + 1) <;> simp
        have := ih (i + 1) (by omega) hr; push_cast; omega

theorem colR_parity (L : ℕ → Bool) (hL : Admissible L) :
    ∀ j t : ℕ, colR L j t = true → (t + j) % 2 = 1 := by
  intro j
  induction j using Nat.strong_induction_on with
  | _ j ih =>
    intro t h
    rcases j with _ | _ | j
    · simp only [colR, clk, decide_eq_true_eq] at h; omega
    · simp only [colR] at h
      by_cases hc : clk (t + 1) = true
      · simp only [clk, decide_eq_true_eq] at hc; omega
      · have hc' : clk (t + 1) = false := by simpa using hc
        rw [hc'] at h
        have hl : lft L t (-1) = true := by revert h; cases lft L t (-1) <;> simp
        have := lft_parity L hL t (-1) (by norm_num) hl
        omega
    · simp only [colR] at h
      by_cases h1 : colR L (j + 1) (t + 1) = true
      · have := ih (j + 1) (by omega) (t + 1) h1; omega
      · have h1' : colR L (j + 1) (t + 1) = false := by simpa using h1
        rw [h1'] at h
        have h2 : colR L j t = true := by revert h; cases colR L j t <;> simp
        have := ih j (by omega) t h2; omega

/-- The background is white at the even sites. -/
theorem bg_even_white (L : ℕ → Bool) (hL : Admissible L) : ∀ i, i % 2 = 0 → bg L i = false := by
  intro i hi
  by_contra hne
  have hb : bg L i = true := by simpa using hne
  simp only [bg, bgCol] at hb
  split_ifs at hb with hle
  · have := lft_parity L hL 0 i hle hb; omega
  · have := colR_parity L hL i.toNat 0 hb; omega

/-- **The background keeps the clock**, under rule 210. -/
theorem clock_bg (L : ℕ → Bool) (hL : Admissible L) : Clock210 (bg L) := by
  intro t
  rw [run210_eq_run90 (bg L) (bg_even_white L hL), run90_bg, bgCol_zero]; rfl

/-- The background's left row is `L`. -/
theorem bg_left (L : ℕ → Bool) (i : ℤ) (hi : i < 0) : bg L i = L (-i).toNat := by
  simp [bg, bgCol, lft, hi, hi.le]

theorem bg_zero (L : ℕ → Bool) : bg L 0 = false := by simp [bg, bgCol, lft]


/-! ## The deviation argument: a candidate that leaves the background fails the clock -/

/-- The background's even diagonals are white. -/
theorem bg_diag_even (L : ℕ → Bool) (hL : Admissible L) (c : ℤ) (hc : c % 2 = 0) (s : ℕ) :
    Diag210 (bg L) c s = false := by
  by_contra hne
  have hb : run210 (bg L) s (c - s) = true := by simpa [Diag210] using hne
  have := parity_of_even_white (bg L) (bg_even_white L hL) s (c - s) hb
  omega

/-- The background's diagonal recursion is rule 90's. -/
theorem bg_diag_succ (L : ℕ → Bool) (hL : Admissible L) (c : ℤ) (s : ℕ) :
    Diag210 (bg L) c (s + 1) = xor (Diag210 (bg L) (c - 2) s) (Diag210 (bg L) c s) := by
  rw [diag_succ]
  have : (!(Diag210 (bg L) (c - 1) s) && Diag210 (bg L) c s) = Diag210 (bg L) c s := by
    by_cases h : Diag210 (bg L) c s = true
    · have h1 : Diag210 (bg L) (c - 1) s = false := by
        by_contra hne
        have hb1 : run210 (bg L) s (c - 1 - s) = true := by simpa [Diag210] using hne
        have hb2 : run210 (bg L) s (c - s) = true := by simpa [Diag210] using h
        have := parity_of_even_white (bg L) (bg_even_white L hL) s _ hb1
        have := parity_of_even_white (bg L) (bg_even_white L hL) s _ hb2
        omega
      rw [h1, h]; rfl
    · have h' : Diag210 (bg L) c s = false := by simpa using h
      rw [h']; simp
  rw [this]

/-- The clock on a diagonal: the cell at the center at time `c`. -/
theorem diag_clock (x0 : ℤ → Bool) (hx : Clock210 x0) (c : ℕ) : Diag210 x0 c c = decide (c % 2 = 1) := by
  unfold Diag210; rw [sub_self]; exact hx c

/-- The setting of the deviation argument: a clock orbit `x0` whose left row is the admissible `L`, agreeing with the
background `bg L` left of `e ≥ 1` and differing at `e`. -/
structure Dev (x0 : ℤ → Bool) (L : ℕ → Bool) (e : ℕ) : Prop where
  hx : Clock210 x0
  hL : Admissible L
  he : 1 ≤ e
  hfirst : ∀ i : ℤ, i < e → x0 i = bg L i
  hdev : x0 e ≠ bg L e

namespace Dev

variable {x0 : ℤ → Bool} {L : ℕ → Bool} {e : ℕ}

theorem local_diag (h : Dev x0 L e) (c : ℤ) (hc : c < e) (s : ℕ) : Diag210 x0 c s = Diag210 (bg L) c s :=
  diag_local x0 (bg L) e h.hfirst s c hc

/-- **F1.** An odd first deviation differs on its diagonal for ever, and so at its own clock time. -/
theorem odd_impossible (h : Dev x0 L e) (hodd : e % 2 = 1) : False := by
  have key : ∀ s, Diag210 x0 e s ≠ Diag210 (bg L) e s := by
    intro s
    induction s with
    | zero => rw [diag_zero, diag_zero]; exact h.hdev
    | succ s ih =>
      rw [diag_succ, diag_succ, h.local_diag (e - 2) (by omega), h.local_diag (e - 1) (by omega),
        bg_diag_even L h.hL (e - 1) (by omega)]
      intro heq
      apply ih
      revert heq
      cases Diag210 (bg L) (↑e - 2) s <;> cases Diag210 x0 ↑e s <;> cases Diag210 (bg L) ↑e s <;> simp
  apply key e
  rw [diag_clock x0 h.hx e, diag_clock (bg L) (clock_bg L h.hL) e]

/-- The gate: the background's odd diagonal just left of the deviation. -/
def bb (L : ℕ → Bool) (e : ℕ) (s : ℕ) : Bool := Diag210 (bg L) ((e : ℤ) - 1) s

theorem bb_exists (h : Dev x0 L e) (heven : e % 2 = 0) : ∃ s, bb L e s = true := by
  have he := h.he
  refine ⟨e - 1, ?_⟩
  unfold bb
  rw [show (e : ℤ) - 1 = ((e - 1 : ℕ) : ℤ) by omega, diag_clock (bg L) (clock_bg L h.hL)]
  simp; omega

/-- The first black time of the gate. -/
noncomputable def tau (h : Dev x0 L e) (heven : e % 2 = 0) : ℕ := Nat.find (h.bb_exists heven)

theorem bb_tau (h : Dev x0 L e) (heven : e % 2 = 0) : bb L e (h.tau heven) = true := Nat.find_spec (h.bb_exists heven)

theorem bb_before_tau (h : Dev x0 L e) (heven : e % 2 = 0) (s : ℕ) (hs : s < h.tau heven) : bb L e s = false := by
  have := Nat.find_min (h.bb_exists heven) hs
  simpa using this

theorem tau_le (h : Dev x0 L e) (heven : e % 2 = 0) : h.tau heven ≤ e - 1 := by
  have he := h.he
  apply Nat.find_min'
  unfold bb
  rw [show (e : ℤ) - 1 = ((e - 1 : ℕ) : ℤ) by omega, diag_clock (bg L) (clock_bg L h.hL)]
  simp; omega

/-- The candidate's pairs: even and odd diagonals right of the deviation. -/
def P (x0 : ℤ → Bool) (e : ℕ) (j s : ℕ) : Bool := Diag210 x0 ((e : ℤ) + 2 * j) s
def Q (x0 : ℤ → Bool) (e : ℕ) (j s : ℕ) : Bool := Diag210 x0 ((e : ℤ) + 2 * j + 1) s
/-- The background's gates. -/
def Ab (L : ℕ → Bool) (e : ℕ) (j s : ℕ) : Bool := Diag210 (bg L) ((e : ℤ) + 2 * j + 1) s

theorem P_zero (h : Dev x0 L e) (heven : e % 2 = 0) : P x0 e 0 0 = true := by
  unfold P; rw [Nat.cast_zero, mul_zero, add_zero, diag_zero]
  have hb : bg L e = false := by
    have := bg_even_white L h.hL e (by omega); exact this
  have := h.hdev; rw [hb] at this; simpa using this

/-- **F2.** The deviation's even diagonal is black until the gate fires and white afterwards. -/
theorem P0_succ (h : Dev x0 L e) (heven : e % 2 = 0) (s : ℕ) : P x0 e 0 (s + 1) = (!(bb L e s) && P x0 e 0 s) := by
  unfold P bb
  rw [Nat.cast_zero, mul_zero, add_zero, diag_succ, h.local_diag (e - 2) (by omega), bg_diag_even L h.hL (e - 2) (by omega)]
  rw [h.local_diag (e - 1) (by omega)]
  simp

theorem P0_before (h : Dev x0 L e) (heven : e % 2 = 0) : ∀ s, s ≤ h.tau heven → P x0 e 0 s = true := by
  intro s
  induction s with
  | zero => intro _; exact h.P_zero heven
  | succ s ih =>
    intro hs
    rw [h.P0_succ heven, h.bb_before_tau heven s (by omega), ih (by omega)]; rfl

theorem P0_after (h : Dev x0 L e) (heven : e % 2 = 0) : ∀ s, h.tau heven + 1 ≤ s → P x0 e 0 s = false := by
  intro s hs
  obtain ⟨m, rfl⟩ : ∃ m, s = m + 1 := ⟨s - 1, by omega⟩
  induction m with
  | zero =>
    rw [h.P0_succ heven]
    have ht : h.tau heven = 0 := by omega
    have hb : bb L e 0 = true := by rw [← ht]; exact h.bb_tau heven
    rw [hb]; rfl
  | succ m ih =>
    rw [h.P0_succ heven]
    rcases Nat.lt_or_ge (h.tau heven) (m + 1) with hlt | hge
    · rw [ih (by omega)]; simp
    · have ht : h.tau heven = m + 1 := by omega
      have hb : bb L e (m + 1) = true := by rw [← ht]; exact h.bb_tau heven
      rw [hb]; rfl

/-- The candidate's recursions, from the diagonal recursion. -/
theorem P_succ (x0 : ℤ → Bool) (e j s : ℕ) :
    P x0 e (j + 1) (s + 1) = xor (P x0 e j s) (!(Q x0 e j s) && P x0 e (j + 1) s) := by
  unfold P Q; rw [diag_succ]
  rw [show (e : ℤ) + 2 * ((j + 1 : ℕ) : ℤ) - 2 = (e : ℤ) + 2 * j by push_cast; ring,
    show (e : ℤ) + 2 * ((j + 1 : ℕ) : ℤ) - 1 = (e : ℤ) + 2 * j + 1 by push_cast; ring]

theorem Q_succ (x0 : ℤ → Bool) (e j s : ℕ) :
    Q x0 e j (s + 1) = xor (Diag210 x0 ((e : ℤ) + 2 * j - 1) s) (!(P x0 e j s) && Q x0 e j s) := by
  unfold P Q; rw [diag_succ]
  rw [show (e : ℤ) + 2 * (j : ℤ) + 1 - 2 = (e : ℤ) + 2 * j - 1 by ring,
    show (e : ℤ) + 2 * (j : ℤ) + 1 - 1 = (e : ℤ) + 2 * j by ring]

theorem Q_succ' (x0 : ℤ → Bool) (e j s : ℕ) :
    Q x0 e (j + 1) (s + 1) = xor (Q x0 e j s) (!(P x0 e (j + 1) s) && Q x0 e (j + 1) s) := by
  rw [Q_succ]; unfold Q
  rw [show (e : ℤ) + 2 * ((j + 1 : ℕ) : ℤ) - 1 = (e : ℤ) + 2 * j + 1 by push_cast; ring]

theorem Q0_succ (h : Dev x0 L e) (s : ℕ) :
    Q x0 e 0 (s + 1) = xor (bb L e s) (!(P x0 e 0 s) && Q x0 e 0 s) := by
  have he := h.he
  rw [Q_succ]; unfold bb
  rw [show (e : ℤ) + 2 * ((0 : ℕ) : ℤ) - 1 = (e : ℤ) - 1 by push_cast; ring, h.local_diag (e - 1) (by omega)]

/-- The background gates' recursions (rule 90). -/
theorem Ab_succ (L : ℕ → Bool) (hL : Admissible L) (e j s : ℕ) :
    Ab L e (j + 1) (s + 1) = xor (Ab L e j s) (Ab L e (j + 1) s) := by
  unfold Ab; rw [bg_diag_succ L hL]
  rw [show (e : ℤ) + 2 * ((j + 1 : ℕ) : ℤ) + 1 - 2 = (e : ℤ) + 2 * j + 1 by push_cast; ring]

theorem Ab0_succ (L : ℕ → Bool) (hL : Admissible L) (e s : ℕ) :
    Ab L e 0 (s + 1) = xor (bb L e s) (Ab L e 0 s) := by
  unfold Ab bb; rw [bg_diag_succ L hL]
  rw [show (e : ℤ) + 2 * ((0 : ℕ) : ℤ) + 1 - 2 = (e : ℤ) - 1 by push_cast; ring]


/-! ### W1: the gate wave in the background -/

theorem W1_const (h : Dev x0 L e) (heven : e % 2 = 0) (w : ℕ) (hw : ∀ j, j < w → Ab L e j 0 = false) :
    ∀ j, j ≤ w → ∀ s, s ≤ h.tau heven + j → Ab L e j s = Ab L e j 0 := by
  intro j
  induction j with
  | zero =>
    intro _ s hs
    induction s with
    | zero => rfl
    | succ s ih =>
      rw [Ab0_succ L h.hL, h.bb_before_tau heven s (by omega), ih (by omega)]; simp
  | succ j ih =>
    intro hj s hs
    induction s with
    | zero => rfl
    | succ s ihs =>
      rw [Ab_succ L h.hL, ih (by omega) s (by omega), hw j (by omega), ihs (by omega)]; simp

theorem W1_flip (h : Dev x0 L e) (heven : e % 2 = 0) (w : ℕ) (hw : ∀ j, j < w → Ab L e j 0 = false) :
    ∀ j, j ≤ w → Ab L e j (h.tau heven + j + 1) = !(Ab L e j 0) := by
  intro j
  induction j with
  | zero =>
    intro _
    rw [show h.tau heven + 0 + 1 = h.tau heven + 1 by ring, Ab0_succ L h.hL, h.bb_tau heven,
      h.W1_const heven w hw 0 (by omega) (h.tau heven) (by omega)]
    cases Ab L e 0 0 <;> rfl
  | succ j ih =>
    intro hj
    rw [show h.tau heven + (j + 1) + 1 = (h.tau heven + j + 1) + 1 by ring, Ab_succ L h.hL, ih (by omega),
      hw j (by omega), h.W1_const heven w hw (j + 1) hj (h.tau heven + j + 1) (by omega)]
    cases Ab L e (j + 1) 0 <;> rfl

/-! ### The abstract clearing front -/

/-- **C1.** The marker identity, for any streams obeying the pair update. -/
theorem marker (U B Pp Qq : ℕ → Bool) (hP : ∀ s, Pp (s + 1) = xor (U s) (!(B s) && Pp s))
    (hQ : ∀ s, Qq (s + 1) = xor (B s) (!(Pp s) && Qq s)) (s : ℕ) :
    (!(Pp (s + 1)) && Qq (s + 1)) = xor (!(U s) && B s) (!(U s) && (!(Pp s) && Qq s)) := by
  rw [hP, hQ]; cases U s <;> cases B s <;> cases Pp s <;> cases Qq s <;> rfl

/-- **C2.** Propagation of a clearing witness and a `01` front from the input pair to the output pair. -/
theorem propagate (U B Pp Qq : ℕ → Bool) (hP : ∀ s, Pp (s + 1) = xor (U s) (!(B s) && Pp s))
    (hQ : ∀ s, Qq (s + 1) = xor (B s) (!(Pp s) && Qq s)) (t T : ℕ) (htT : t < T) (hUt : U t = true)
    (hM : ∀ s, t ≤ s → s < T → (!(U s) && B s) = false) (hUT : U T = false) (hBT : B T = true) :
    ∃ t', (t' = t ∨ t' = t + 1) ∧ Pp t' = true ∧ (∀ s, t' ≤ s → s ≤ T → (!(Pp s) && Qq s) = false) ∧
      Pp (T + 1) = false ∧ Qq (T + 1) = true := by
  have hM1 : ∀ n, t + 1 + n ≤ T → (!(Pp (t + 1 + n)) && Qq (t + 1 + n)) = false := by
    intro n
    induction n with
    | zero =>
      intro _
      rw [show t + 1 + 0 = t + 1 by ring, marker U B Pp Qq hP hQ t, hM t le_rfl htT, hUt]; rfl
    | succ n ih =>
      intro hn
      rw [show t + 1 + (n + 1) = (t + 1 + n) + 1 by ring, marker U B Pp Qq hP hQ, ih (by omega),
        hM (t + 1 + n) (by omega) (by omega)]
      cases U (t + 1 + n) <;> rfl
  have hMT : (!(Pp T) && Qq T) = false := by
    have := hM1 (T - t - 1) (by omega)
    rwa [show t + 1 + (T - t - 1) = T by omega] at this
  have hPT1 : Pp (T + 1) = false := by rw [hP, hUT, hBT]; cases Pp T <;> rfl
  have hQT1 : Qq (T + 1) = true := by
    rw [hQ, hBT]
    have : (!(Pp T) && Qq T) = false := hMT
    rw [this]; rfl
  by_cases hPt : Pp t = true
  · refine ⟨t, Or.inl rfl, hPt, fun s hs1 hs2 => ?_, hPT1, hQT1⟩
    rcases Nat.eq_or_lt_of_le hs1 with heq | hlt
    · subst heq; rw [hPt]; rfl
    · have := hM1 (s - t - 1) (by omega)
      rwa [show t + 1 + (s - t - 1) = s by omega] at this
  · have hPt' : Pp t = false := by simpa using hPt
    refine ⟨t + 1, Or.inr rfl, ?_, fun s hs1 hs2 => ?_, hPT1, hQT1⟩
    · rw [hP, hUt, hPt']; cases B t <;> rfl
    · have := hM1 (s - t - 1) (by omega)
      rwa [show t + 1 + (s - t - 1) = s by omega] at this

/-- **C3.** Every candidate pair has a clearing witness no later than `τ + j` and the `01` front at `τ + j + 1`. -/
theorem front (h : Dev x0 L e) (heven : e % 2 = 0) : ∀ j, ∃ tj, tj ≤ h.tau heven + j ∧ P x0 e j tj = true ∧
    (∀ s, tj ≤ s → s ≤ h.tau heven + j → (!(P x0 e j s) && Q x0 e j s) = false) ∧
    P x0 e j (h.tau heven + j + 1) = false ∧ Q x0 e j (h.tau heven + j + 1) = true := by
  intro j
  induction j with
  | zero =>
    refine ⟨h.tau heven, by omega, h.P0_before heven _ le_rfl, fun s hs1 hs2 => ?_, ?_, ?_⟩
    · have hs : s = h.tau heven := by omega
      subst hs; rw [h.P0_before heven _ le_rfl]; rfl
    · rw [show h.tau heven + 0 + 1 = h.tau heven + 1 by ring]; exact h.P0_after heven _ le_rfl
    · rw [show h.tau heven + 0 + 1 = h.tau heven + 1 by ring, h.Q0_succ, h.bb_tau heven, h.P0_before heven _ le_rfl]; rfl
  | succ j ih =>
    obtain ⟨tj, htj, hPtj, hMj, hPT, hQT⟩ := ih
    obtain ⟨t', ht', hPt', hM', hP1, hQ1⟩ := propagate (P x0 e j) (Q x0 e j) (P x0 e (j + 1)) (Q x0 e (j + 1))
      (P_succ x0 e j) (Q_succ' x0 e j) tj (h.tau heven + j + 1) (by omega) hPtj
      (fun s hs1 hs2 => hMj s hs1 (by omega)) hPT hQT
    refine ⟨t', by omega, hPt', fun s hs1 hs2 => hM' s hs1 (by omega), ?_, ?_⟩
    · rw [show h.tau heven + (j + 1) + 1 = (h.tau heven + j + 1) + 1 by ring]; exact hP1
    · rw [show h.tau heven + (j + 1) + 1 = (h.tau heven + j + 1) + 1 by ring]; exact hQ1

/-! ### C4: identification with the background after the front -/

theorem identify (h : Dev x0 L e) (heven : e % 2 = 0) (w : ℕ) (hw : ∀ j, j < w → Ab L e j 0 = false) :
    ∀ j, j ≤ w → ∀ s, h.tau heven + j + 1 ≤ s →
      P x0 e j s = false ∧ xor (Q x0 e j s) (Ab L e j s) = Ab L e j 0 := by
  intro j
  induction j with
  | zero =>
    intro _ s hs
    obtain ⟨n, rfl⟩ : ∃ n, s = h.tau heven + 0 + 1 + n := ⟨s - (h.tau heven + 0 + 1), by omega⟩
    induction n with
    | zero =>
      obtain ⟨_, _, _, _, _, hQT⟩ := h.front heven 0
      refine ⟨h.P0_after heven _ (by omega), ?_⟩
      rw [hQT, h.W1_flip heven w hw 0 (by omega)]
      cases Ab L e 0 0 <;> rfl
    | succ n ihn =>
      obtain ⟨hPn, hQn⟩ := ihn (by omega)
      refine ⟨h.P0_after heven _ (by omega), ?_⟩
      rw [show h.tau heven + 0 + 1 + (n + 1) = (h.tau heven + 0 + 1 + n) + 1 by ring, h.Q0_succ, Ab0_succ L h.hL, hPn]
      rw [← hQn]
      cases bb L e (h.tau heven + 0 + 1 + n) <;> cases Q x0 e 0 (h.tau heven + 0 + 1 + n) <;>
        cases Ab L e 0 (h.tau heven + 0 + 1 + n) <;> rfl
  | succ j ih =>
    intro hj s hs
    obtain ⟨n, rfl⟩ : ∃ n, s = h.tau heven + (j + 1) + 1 + n := ⟨s - (h.tau heven + (j + 1) + 1), by omega⟩
    induction n with
    | zero =>
      obtain ⟨_, _, _, _, hPT, hQT⟩ := h.front heven (j + 1)
      refine ⟨hPT, ?_⟩
      rw [hQT, h.W1_flip heven w hw (j + 1) hj]
      cases Ab L e (j + 1) 0 <;> rfl
    | succ n ihn =>
      obtain ⟨hPn, hQn⟩ := ihn (by omega)
      have hprev := ih (by omega) (h.tau heven + (j + 1) + 1 + n) (by omega)
      obtain ⟨hPj, hQj⟩ := hprev
      have hQjeq : Q x0 e j (h.tau heven + (j + 1) + 1 + n) = Ab L e j (h.tau heven + (j + 1) + 1 + n) := by
        rw [hw j (by omega)] at hQj
        revert hQj; cases Q x0 e j (h.tau heven + (j + 1) + 1 + n) <;> cases Ab L e j (h.tau heven + (j + 1) + 1 + n) <;> simp
      rw [show h.tau heven + (j + 1) + 1 + (n + 1) = (h.tau heven + (j + 1) + 1 + n) + 1 by ring]
      constructor
      · rw [P_succ, hPj, hPn]; cases Q x0 e j (h.tau heven + (j + 1) + 1 + n) <;> rfl
      · rw [Q_succ', Ab_succ L h.hL, hPn, hQjeq, ← hQn]
        cases Ab L e j (h.tau heven + (j + 1) + 1 + n) <;> cases Q x0 e (j + 1) (h.tau heven + (j + 1) + 1 + n) <;>
          cases Ab L e (j + 1) (h.tau heven + (j + 1) + 1 + n) <;> rfl

/-- **C5.** With a black background gate beyond the deviation, the candidate fails the clock at `e + 2w + 1`. -/
theorem even_impossible (h : Dev x0 L e) (heven : e % 2 = 0) (hwex : ∃ j, Ab L e j 0 = true) : False := by
  have he := h.he
  have htau := h.tau_le heven
  set w := Nat.find hwex with hw_def
  have hw : ∀ j, j < w → Ab L e j 0 = false := fun j hj => by
    have := Nat.find_min hwex hj; simpa using this
  have hAw : Ab L e w 0 = true := Nat.find_spec hwex
  obtain ⟨-, hid⟩ := h.identify heven w hw w le_rfl (e + 2 * w + 1) (by omega)
  rw [hAw] at hid
  have hQ : Q x0 e w (e + 2 * w + 1) = true := by
    unfold Q
    rw [show (e : ℤ) + 2 * (w : ℤ) + 1 = ((e + 2 * w + 1 : ℕ) : ℤ) by push_cast; ring, diag_clock x0 h.hx]
    simp; omega
  have hA : Ab L e w (e + 2 * w + 1) = true := by
    unfold Ab
    rw [show (e : ℤ) + 2 * (w : ℤ) + 1 = ((e + 2 * w + 1 : ℕ) : ℤ) by push_cast; ring, diag_clock (bg L) (clock_bg L h.hL)]
    simp; omega
  rw [hQ, hA] at hid
  exact absurd hid (by decide)

end Dev


/-! ## The theorem: no finite configuration keeps the clock -/

theorem run210_zero_config : ∀ t i, run210 (fun _ => false) t i = false
  | 0, _ => rfl
  | t + 1, i => by rw [run210_succ, run210_zero_config t, run210_zero_config t, run210_zero_config t]; rfl

/-- **No finite configuration has the clock `0101…` on its center column under rule 210** (the record's
Proposition 19, PROOFS.md entry 32; GPT's clearing-front proof). -/
theorem no_finite_clock (x0 : ℤ → Bool) (hfin : Finite210 x0) (hx : Clock210 x0) : False := by
  obtain ⟨R, hR⟩ := hfin
  set L : ℕ → Bool := fun k => x0 (-(k : ℤ)) with hL_def
  have hL : Admissible L := fun k hk => left_row_of_clock x0 hx (-(k : ℤ)) (by omega) (by omega)
  have hleft : ∀ i : ℤ, i ≤ 0 → x0 i = bg L i := by
    intro i hi
    rcases lt_or_eq_of_le hi with hlt | heq
    · rw [bg_left L i hlt, hL_def]; simp only; congr 1; omega
    · subst heq; rw [bg_zero]; exact left_row_of_clock x0 hx 0 le_rfl (by norm_num)
  have hclock90 : ∀ t, run90 (bg L) t 0 = decide (t % 2 = 1) := fun t => by
    rw [← run210_eq_run90 (bg L) (bg_even_white L hL)]; exact clock_bg L hL t
  by_cases hall : ∀ i : ℤ, x0 i = bg L i
  · exact no_finite_clock90 (bg L) R (fun i hi => by rw [← hall i]; exact hR i hi) hclock90
  · push Not at hall
    have hex : ∃ n : ℕ, x0 n ≠ bg L n := by
      obtain ⟨i, hi⟩ := hall
      have hpos : 0 < i := by
        by_contra hle; push Not at hle; exact hi (hleft i hle)
      exact ⟨i.toNat, by rw [Int.toNat_of_nonneg hpos.le]; exact hi⟩
    set e := Nat.find hex with he_def
    have hdev : x0 e ≠ bg L e := Nat.find_spec hex
    have he : 1 ≤ e := by
      by_contra h0; push Not at h0
      have h00 : e = 0 := by omega
      apply hdev; rw [h00, Nat.cast_zero]; exact hleft 0 le_rfl
    have hfirst : ∀ i : ℤ, i < e → x0 i = bg L i := by
      intro i hi
      rcases le_or_gt i 0 with hle | hpos
      · exact hleft i hle
      · have hmin := Nat.find_min hex (m := i.toNat) (by omega)
        push Not at hmin
        rwa [Int.toNat_of_nonneg hpos.le] at hmin
    have hD : Dev x0 L e := ⟨hx, hL, he, hfirst, hdev⟩
    rcases Nat.even_or_odd e with ⟨k, hk⟩ | ⟨k, hk⟩
    · have heven : e % 2 = 0 := by omega
      by_cases hwex : ∃ j, Dev.Ab L e j 0 = true
      · exact hD.even_impossible heven hwex
      · push Not at hwex
        have hbgfin : ∀ i : ℤ, ((max R e : ℕ) : ℤ) < |i| → bg L i = false := by
          intro i hi
          rcases lt_or_ge i 0 with hneg | hnn
          · rw [← hleft i hneg.le]
            apply hR
            rw [lt_abs] at hi ⊢
            push_cast at hi
            rcases hi with h1 | h1
            · left; have := le_max_left R e; omega
            · right; have := le_max_left R e; omega
          · rcases Int.emod_two_eq_zero_or_one i with hev | hod
            · exact bg_even_white L hL i hev
            · have hgt : (e : ℤ) < i := by
                rw [lt_abs] at hi; push_cast at hi
                rcases hi with h1 | h1
                · have := le_max_right R e; omega
                · have := le_max_right R e; omega
              obtain ⟨j, hj⟩ : ∃ j : ℕ, i = (e : ℤ) + 2 * j + 1 := ⟨((i - e - 1) / 2).toNat, by omega⟩
              have := hwex j
              simp only [Dev.Ab, diag_zero] at this
              rw [hj]; simpa using this
        exact no_finite_clock90 (bg L) (max R e) hbgfin hclock90
    · exact hD.odd_impossible (by omega)

/-- The semigroup property of `run210`. -/
theorem run210_add (x0 : ℤ → Bool) (a : ℕ) : ∀ b i, run210 (run210 x0 a) b i = run210 x0 (a + b) i := by
  intro b
  induction b with
  | zero => intro i; rfl
  | succ b ih => intro i; rw [run210_succ, ih, ih, ih, show a + (b + 1) = (a + b) + 1 by ring, run210_succ]

/-- A finite configuration stays finite: its support at time `T` lies within `R + T`. -/
theorem finite_run210 (x0 : ℤ → Bool) (R : ℕ) (hR : ∀ i : ℤ, (R : ℤ) < |i| → x0 i = false) (T : ℕ) :
    ∀ i : ℤ, ((R + T : ℕ) : ℤ) < |i| → run210 x0 T i = false := by
  intro i hi
  rw [run210_cone x0 (fun _ => false) T i (fun j h1 h2 => hR j (by
    rw [lt_abs] at hi ⊢; push_cast at hi; rcases hi with h | h
    · left; omega
    · right; omega)), run210_zero_config]

/-- **Phase and eventual clocks.** No finite configuration has a center column that is eventually alternating, in
either phase. -/
theorem no_finite_eventually_alternating (x0 : ℤ → Bool) (hfin : Finite210 x0) (T φ : ℕ)
    (h : ∀ t, T ≤ t → run210 x0 t 0 = decide ((t + φ) % 2 = 1)) : False := by
  obtain ⟨R, hR⟩ := hfin
  set T' := T + (T + φ) % 2 with hT'
  apply no_finite_clock (run210 x0 T') ⟨R + T', finite_run210 x0 R hR T'⟩
  intro t
  rw [run210_add, h (T' + t) (by omega)]
  congr 1
  apply propext
  constructor <;> intro hh <;> omega

/-- For the kit's single seed, the same statement in the kit's `run g210`: its center column is not eventually
alternating (the kit's `center210` already makes it eventually constant; this is the general finite case). -/
theorem seed_not_eventually_alternating (T φ : ℕ)
    (h : ∀ t, T ≤ t → run g210 t 0 = decide ((t + φ) % 2 = 1)) : False :=
  no_finite_eventually_alternating (fun p => decide (p = 0)) ⟨0, fun i hi => by
    rw [lt_abs] at hi; simp only [decide_eq_false_iff_not]; omega⟩ T φ
    (fun t ht => by rw [run210_seed]; exact h t ht)

end Rule30Submission
