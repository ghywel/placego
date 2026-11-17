import Rule30PrizeKit
import Mathlib

/-!
# Rule 210 beside the period-2 clock: the one-sided question is false, and the left half is linear

**Barrier material for Problem 1.** The kit's `Rule30ZeroBoundary.Q01` is the period-2 question for rule 30 in its
one-sided form: no finitely supported start of the zero-boundary left half keeps column `-1` black at every even
step. It is open. The kit's `Rule30Realization.barrier` shows that left-permutivity, the moving edge and Jen's theorem
cannot decide Problem 1, because rules 90, 150 and 210 share them and have eventually constant center columns. This
module sharpens the barrier at period 2 with the one sibling that is nonlinear and not right-permutive, rule 210
(`left xor (!center && right)`, the kit's `g210`):

* `zrow210 L t k`: rule 210's left half with the period-2 clock at the wall, in the kit's ZBL encoding (depth `k` is
  position `-k`, depth `0` is the wall, black at the even steps as in the kit's `InX`; the start `L` is read at
  depths `k ≥ 1`). Under the clock, column `0` constrains the left half only through column `-1`: it must be white at
  every even step (`InX210`), and column `1`'s bits at the odd steps are then determined. `Q01_210` is the kit's
  `Q01` with these replacements.
* **`not_Q01_210`: the one-sided period-2 statement is false for rule 210.** The empty start keeps the clock for
  ever (`white_start_inX`), because from a white start every black cell `(t, k)` has `t + k` even
  (`white_start_parity`), so column `-1` is black only at odd steps.
* **The parity invariant** (`parity_invariant`): for *every* start consistent with the clock, every black cell has
  `t + k` even; hence two horizontally adjacent cells are never both black, the `!center && right` gate reduces to
  `right`, and **the left half is rule 90's** (`linear`: `zrow210 L (t+1) (k+1) = xor (zrow210 L t (k+2))
  (zrow210 L t k)`).

**What is new relative to the kit.** The kit's barrier is about the seed's center column (eventually constant for
rules 90, 150, 210). This is about the period-2 question itself: the exact analogue of the kit's open `Q01` is false
for rule 210, from the very first start, while the record's hand proof (PROOFS.md entry 32, not formalized here)
shows that the two-sided statement, no finite configuration keeps the clock, is true for rule 210. So the gap between
the one-sided and the two-sided period-2 statements is real on a sibling rule, which argues for attacking the
two-sided form (`Rule30PeriodTwo.Q01`'s finite-configuration cousins) rather than `Q01` alone.

**Provenance.** RULE30-PRIZE.md §8.65 and PROOFS.md entry 18 of the Wolfram · Collatz · Mahler record
(github.com/ghywel/placego): the witness (the empty left half with its doubling-runs column 1) found by Local (Claude)
on 2026-10-06 and proved by GPT (§G26); the parity invariant proved by Local the same day; formalized here for the
first time by Cloud (Claude) on 2026-10-23 in the kit's ZBL encoding.
-/

set_option Elab.async false

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30ZeroBoundary

/-- Rule 210's left half with the period-2 clock at the wall: depth `k` is position `-k`; depth `0` is the wall,
black at the even steps; the start `L` is read at depths `k ≥ 1`. The step at depth `k + 1` is rule 210 read
leftward: `left xor (!center && right)` with the left neighbour at depth `k + 2` and the right one at depth `k`. -/
def zrow210 (L : ℕ → Bool) : ℕ → ℕ → Bool
  | 0, 0 => true
  | 0, k + 1 => L (k + 1)
  | t + 1, 0 => decide ((t + 1) % 2 = 0)
  | t + 1, k + 1 => xor (zrow210 L t (k + 2)) (!zrow210 L t (k + 1) && zrow210 L t k)

theorem zrow210_wall (L : ℕ → Bool) : ∀ t, zrow210 L t 0 = decide (t % 2 = 0)
  | 0 => rfl
  | _ + 1 => rfl

theorem zrow210_start (L : ℕ → Bool) (k : ℕ) : zrow210 L 0 (k + 1) = L (k + 1) := rfl

theorem zrow210_succ (L : ℕ → Bool) (t k : ℕ) :
    zrow210 L (t + 1) (k + 1) = xor (zrow210 L t (k + 2)) (!zrow210 L t (k + 1) && zrow210 L t k) := rfl

/-- Left permutivity: the cell at depth `k + 2` from the next cell at depth `k + 1` and the cells at depths
`k + 1` and `k`. -/
theorem zrow210_inv (L : ℕ → Bool) (t k : ℕ) :
    zrow210 L t (k + 2) = xor (zrow210 L (t + 1) (k + 1)) (!zrow210 L t (k + 1) && zrow210 L t k) := by
  rw [zrow210_succ]
  cases zrow210 L t (k + 2) <;> cases (!zrow210 L t (k + 1) && zrow210 L t k) <;> rfl

/-- Starts consistent with the clock: column `-1` is white at every even step. (Under the clock, black at the even
steps at the wall, rule 210 at position `0` reads `clock (t + 1) = xor (col (-1) t) (!clock t && col 1 t)`: at even
`t` this forces column `-1` white, at odd `t` it determines column `1`.) -/
def InX210 (L : ℕ → Bool) : Prop := ∀ s, zrow210 L (2 * s) 1 = false

/-- The kit's `Q01` for rule 210: no finitely supported start keeps the clock. -/
def Q01_210 : Prop := ∀ L : ℕ → Bool, FinSupp L → ¬ InX210 L

/-- From a white start every black cell `(t, k)` has `t + k` even. -/
theorem white_start_parity (L : ℕ → Bool) (hL : ∀ k, L k = false) :
    ∀ t k, zrow210 L t k = true → (t + k) % 2 = 0 := by
  intro t
  induction t with
  | zero =>
    intro k h
    rcases k with _ | k
    · rfl
    · rw [zrow210_start, hL] at h; exact absurd h (by decide)
  | succ t ih =>
    intro k h
    rcases k with _ | k
    · rw [zrow210_wall] at h; simp only [decide_eq_true_eq] at h; omega
    · rw [zrow210_succ] at h
      by_cases h1 : zrow210 L t (k + 2) = true
      · have := ih (k + 2) h1; omega
      · have h1' : zrow210 L t (k + 2) = false := by simpa using h1
        rw [h1'] at h
        have hk : zrow210 L t k = true := by
          revert h; cases zrow210 L t (k + 1) <;> cases zrow210 L t k <;> simp
        have := ih k hk; omega

/-- The white start keeps the clock for ever. -/
theorem white_start_inX (L : ℕ → Bool) (hL : ∀ k, L k = false) : InX210 L := by
  intro s
  by_contra hne
  have h : zrow210 L (2 * s) 1 = true := by simpa using hne
  have := white_start_parity L hL (2 * s) 1 h
  omega

/-- **The one-sided period-2 statement is false for rule 210**: the empty start is finitely supported and keeps the
clock. -/
theorem not_Q01_210 : ¬ Q01_210 :=
  fun hQ => hQ (fun _ => false) ⟨0, fun _ _ => rfl⟩ (white_start_inX _ (fun _ => rfl))

/-- **The parity invariant.** For every start consistent with the clock, every black cell `(t, k)` has `t + k`
even. By induction on the depth, with left permutivity. -/
theorem parity_invariant (L : ℕ → Bool) (hX : InX210 L) :
    ∀ k t, zrow210 L t k = true → (t + k) % 2 = 0 := by
  intro k
  induction k using Nat.strong_induction_on with
  | _ k ih =>
    intro t h
    rcases k with _ | _ | k
    · rw [zrow210_wall] at h; simp only [decide_eq_true_eq] at h; omega
    · rcases Nat.even_or_odd t with ⟨s, hs⟩ | ⟨s, hs⟩
      · exfalso
        have := hX s
        rw [show 2 * s = t by omega, h] at this
        exact absurd this (by decide)
      · omega
    · rw [zrow210_inv] at h
      by_cases h1 : zrow210 L (t + 1) (k + 1) = true
      · have := ih (k + 1) (by omega) (t + 1) h1; omega
      · have h1' : zrow210 L (t + 1) (k + 1) = false := by simpa using h1
        rw [h1'] at h
        have hk : zrow210 L t k = true := by
          revert h; cases zrow210 L t (k + 1) <;> cases zrow210 L t k <;> simp
        have := ih k (by omega) t hk; omega

/-- **Beside the clock, rule 210's left half is rule 90's.** Two horizontally adjacent cells are never both black,
so the gate `!center && right` is `right`. -/
theorem linear (L : ℕ → Bool) (hX : InX210 L) (t k : ℕ) :
    zrow210 L (t + 1) (k + 1) = xor (zrow210 L t (k + 2)) (zrow210 L t k) := by
  rw [zrow210_succ]
  have : (!zrow210 L t (k + 1) && zrow210 L t k) = zrow210 L t k := by
    by_cases hk : zrow210 L t k = true
    · have hk1 : zrow210 L t (k + 1) = false := by
        by_contra hne
        have h1 := parity_invariant L hX (k + 1) t (by simpa using hne)
        have h0 := parity_invariant L hX k t hk
        omega
      rw [hk, hk1]; rfl
    · have hk' : zrow210 L t k = false := by simpa using hk
      rw [hk']; simp
  rw [this]

/-- No two horizontally adjacent black cells, for every start consistent with the clock. -/
theorem no_adjacent (L : ℕ → Bool) (hX : InX210 L) (t k : ℕ) :
    ¬ (zrow210 L t k = true ∧ zrow210 L t (k + 1) = true) := by
  rintro ⟨h0, h1⟩
  have := parity_invariant L hX k t h0
  have := parity_invariant L hX (k + 1) t h1
  omega

end Rule30Submission
