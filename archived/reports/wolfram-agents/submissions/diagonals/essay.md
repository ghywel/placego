---
Template: ComputationalEssay
Name: The left diagonals of rule 30: their periods are unbounded, and the settled band has no long white run
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-23
Description: Partial results for Problem 1 of the Rule 30 Prize about the left diagonals of the pattern, proved in Lean against the official statements: no two adjacent left diagonals are both eventually white, an eventually white one is followed two later by an eventually black one, no single period is eventual for all of them, and inside a band of diagonals that has settled into a common period P no white run is longer than 2P - 1
Abstract: The kit proves that every left diagonal D j t = cell t (j - t) of the rule 30 pattern is eventually periodic with period dividing 2^j (Rule30Diagonals.D_periodic). This essay adds the other direction and the structure beside it, as a partial result for Problem 1. Lemma B1: no two adjacent left diagonals are both eventually white, and an eventually white diagonal is followed two later by an eventually black one (Rule30Submission.seed_no_adjacent_white, seed_white_then_black). Lemma B2: no period P ≥ 1 is an eventual period of every left diagonal, so the eventual periods are unbounded, and among the first 4^P + 2 diagonals one does not have eventual period P (seed_periods_unbounded, seed_periods_unbounded_quant); hence infinitely many diagonals are eventually white and infinitely many eventually black. Lemma B3: if the diagonals 0 to M have had a common period P for P steps, no white run of the row inside them, bounded on the left by a black diagonal, is longer than 2P - 1 (lemma_B3_sharp). All hold for every configuration with a leftmost black cell. The unboundedness is Rowland's (2006); the proofs, the quantitative form and Lemmas B1 and B3 are the record's. The verifier's replay accepts the module with the three standard axioms only. Nothing here decides Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, left diagonals, eventual period, Rowland, period doubling, left-permutive, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entries 8, 9 and 12](https://github.com/ghywel/placego/blob/main/PROOFS.md)", "[E. Rowland, Local Nested Structure in Rule 30, Complex Systems 16 (2006)](https://www.complex-systems.com/abstracts/v16_i03_a03/)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261022-c27323, the white end](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-c27323)"]
---

## The question

Rule 30 updates every cell from itself and its two neighbors: the new color is *left* XOR (*center* OR *right*). From a single black cell it grows a pattern whose center column looks random. Problem 1 of the Rule 30 Prize asks whether that column is ever eventually periodic.

The pattern's left edge is regular: along the diagonals parallel to it the colors settle into periods. The `j`-th left diagonal is `D j t = cell t (j - t)`, the cell `j` places right of the moving left edge. The first 60 steps, with diagonals 0, 4 and 8 marked:

```wl
pattern = CellularAutomaton[30, {{1}, 0}, 60];
marks = Table[{t + 1, j - t + 61}, {t, 0, 60}, {j, {0, 4, 8}}] // Flatten[#, 1] &;
ArrayPlot[ReplacePart[pattern, Thread[marks -> 2]], ColorRules -> {0 -> White, 1 -> GrayLevel[0.15], 2 -> StandardRed}, ImageSize -> 520]
```

The kit's catalog proves that every left diagonal is eventually periodic with period dividing `2^j` (`Rule30Diagonals.D_periodic`; `Rule30FiniteDiagonals.Ld_periodic` for any configuration with a leftmost black cell). The center column is the diagonal of diagonals, `center t = D t t`, but the period bound `2^j` exceeds `j`, so, as the kit says, that theorem says nothing about the center column by itself. This essay proves what the diagonals do beyond that bound: their periods really grow without limit, their colors alternate in a forced pattern, and the band of diagonals that has settled cannot contain a long white run.

## The diagonals, measured

The left diagonals from the first 12,000 rows, and for each the least eventual period found and the color it settles into. `?` marks a period not settled within the sample:

```wl
rowsT = 12000;
rows = CellularAutomaton[30, {{1}, 0}, rowsT];
diag[j_] := Table[rows[[t + 1, j - t + rowsT + 1]], {t, j, rowsT}];
leastPeriod[s_] := Module[{n = Length[s]}, SelectFirst[Range[1, 4096], Function[p, s[[Floor[n/2] ;; n - p]] === s[[Floor[n/2] + p ;; n]]], "?"]];
colour[s_] := With[{tail = s[[-2000 ;;]]}, Which[Max[tail] == 0, "white", Min[tail] == 1, "black", True, "mixed"]];
Grid[Prepend[Table[{j, leastPeriod[diag[j]], colour[diag[j]]}, {j, 0, 12}], {"j", "least eventual period (sample)", "eventually"}], Frame -> All]
```

The periods are powers of two and they double, as Rowland proved; between the doublings sit eventually white and eventually black diagonals, and the white ones never come in adjacent pairs. The theorems below say why, for every `j`, with no sample.

## The idea of the proofs

Write `D j` for the `j`-th left diagonal of a configuration with a leftmost black cell. Rule 30 is left-permutive, and read along diagonals the rule becomes a recurrence that feeds each diagonal from the two before it: `D (j+2) (t+1) = D j t XOR (D (j+1) t OR D (j+2) t)`. Diagonal 0 is the edge, black for ever; diagonal 1 is black from time 1; diagonal 2 is white from time 2.

**Lemma B1.** If `D j` and `D (j+1)` were both eventually white, the recurrence would make `D (j+2)` eventually constant and then, going back up the recurrence, force a contradiction at the edge; and an eventually white `D j` makes `D (j+2)` eventually black because the XOR with a white input leaves the OR, which a black cell keeps black.

**Lemma B2.** Suppose every left diagonal had eventual period `P`. Take a time after which the diagonals `0` to `4^P + 1` are all periodic. The `4^P + 1` windows of two adjacent diagonals over one period take at most `4^P` values, so two windows agree at `k₁ < k₂`, and periodicity extends the agreement to all later times. Left-permutivity then propagates the agreement leftward, diagonal by diagonal, down to the edge: diagonal `k₂ - k₁` would agree with diagonal 0, which is black for ever, so `D (k₂ - k₁)` is eventually black, and the next one down, `D (k₂ - k₁ - 1)`, agrees with `D (-1)`, which is white: it is eventually white, and Lemma B1's "white then black" climbs back up to a contradiction with the recurrence at the top of the window. The period `P` is therefore not shared by all diagonals: the eventual periods are unbounded. The quantitative form keeps the bound `4^P + 1`.

**Lemma B3.** If the diagonals `0 … M` have had a common period `P` for `P` steps, look at a white run of the row at time `t` inside them, bounded on the left by a black diagonal `g`. One step back, the run is either older, white two cells wider with its black bound two further left, or newborn, black on `[g - 1, M' - 2]`. Following it back `P` steps, the run's left end has moved `2P` cells left of `g`, while the periodicity says the row at `t - P` agrees with the row at `t`, which is black at `g`: so the run at time `t` is shorter than `2P`. The sharp bound is `2P - 1`.

Everything in this section is prose. The proofs are the next section.

## The formal proof

The module, as the verifier rebuilds and checks it: the diagonals `D x0 e j t = evol x0 t (e - t + j)` on the kit's `evol` (they are the kit's `Rule30FiniteDiagonals.Ld` and, for the seed, `Rule30Diagonals.D`), the recurrence `D_succ`, the edge lemma, the forced-periodicity transducer lemmas, `jen_pow2` (the period `2^j`), `lemma_B3_sharp`, `lemma_B2_quant`, `lemma_B2`, `infinitely_many_white`, `no_adjacent_white`, `white_then_black`, `infinitely_many_black`, and the bridge lemmas that restate the seed's cases in the kit's `Rule30Diagonals.D`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["import Rule30PrizeKit
import Mathlib

/-!
# The left diagonals of rule 30: white then black, the clock never stops, and the settled band has no long white run

**Partial results for Problem 1** about the left diagonals `D j t = cell t (j - t)` of the single-seed pattern, and
the same diagonals `evol x t (e - t + j)` of every configuration with a leftmost black cell `e`. The kit proves that
each left diagonal is eventually periodic with period dividing `2^j` (`Rule30Diagonals.D_periodic`,
`Rule30FiniteDiagonals.Ld_periodic`). This module adds the other direction and the structure beside it:

* **Lemma B1** (`seed_no_adjacent_white`, `seed_white_then_black`; general: `no_adjacent_white`, `white_then_black`):
  no two adjacent left diagonals are both eventually white, and an eventually white diagonal is followed two later by
  an eventually black one.
* **Lemma B2** (`seed_periods_unbounded`, `seed_periods_unbounded_quant`; general: `lemma_B2`, `lemma_B2_quant`):
  no `P ≥ 1` is an eventual period of every left diagonal, so the eventual periods are unbounded; quantitatively,
  among the first `4^P + 2` diagonals one does not have eventual period `P`. Hence infinitely many diagonals are
  eventually white and infinitely many eventually black (`seed_infinitely_many_white`, `seed_infinitely_many_black`).
* **Lemma B3** (`lemma_B3_sharp`): if the diagonals `0 … M` have had a common period `P` for `P` steps, no white run
  of the row inside them, bounded on the left by a black diagonal, is longer than `2P - 1`.
* `jen_pow2`, `run_bound`, `run_bound_gcd`: the period-`2^j` statement in this module's own vocabulary (the kit's
  `D_periodic`), and the resulting bound `2^(j+1) - 1` on white runs among the first `j + 3` diagonals.

**What is new relative to the kit.** The kit's catalogue has the upper bound `2^j` for left diagonals and lower
bounds only for the right diagonals (`Rule30RightPeriods.period_gt`). The unboundedness of the left periods is
Rowland's (*Local Nested Structure in Rule 30*, Complex Systems 16 (2006)), whom the kit cites without a formal
statement; the proof here is the record's own (a pigeonhole over `4^P + 1` windows of two adjacent diagonals, then
left-permutivity), and the quantitative form, Lemma B1 and Lemma B3 are the record's. Nothing here decides Problem 1:
the period `2^j` exceeds `j`, so, as the kit says, these facts say nothing about the center column directly.

**Provenance.** RULE30-PRIZE.md §8.59 and PROOFS.md entries 8, 9 and 12 of the Wolfram · Collatz · Mahler record
(github.com/ghywel/placego), proved by Local (Claude) on 2026-10-05, second-read by Cloud (CL170–173) and GPT
(GC960–963), machine-checked by Local on 2026-10-10 (`tests/probes/lean/JenPow2.lean`); restated here on the kit's
`evol` and `cell` by Cloud on 2026-10-23, with the bridge to `Rule30Diagonals.D`. Sources: E. Jen, J. Stat. Phys. 43
(1986); E. Rowland, Complex Systems 16 (2006).
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

/-! ## The bridge to the kit's statements: the single-seed pattern's left diagonals -/

lemma seed_leftmost : seed 0 = true ∧ ∀ p : ℤ, p < 0 → seed p = false := by
  refine ⟨by simp [seed], fun p hp => ?_⟩
  simp only [seed, decide_eq_false_iff_not]; omega

/-- Our diagonal `D seed 0 j t` is the kit's `Rule30Diagonals.D j t = cell t (j - t)`. -/
lemma D_seed (j t : ℕ) : D seed 0 (j : ℤ) t = Rule30Diagonals.D j t := by
  simp only [D, Rule30Diagonals.D, evol_seed]
  congr 1; ring

lemma evW_seed (j : ℕ) (h : ∃ T : ℕ, ∀ t, T ≤ t → Rule30Diagonals.D j t = false) : EvW seed 0 (j : ℤ) :=
  let ⟨T, hT⟩ := h; ⟨T, fun t ht => by rw [D_seed]; exact hT t ht⟩

lemma seed_evB (j : ℕ) (h : EvB seed 0 (j : ℤ)) : ∃ T : ℕ, ∀ t, T ≤ t → Rule30Diagonals.D j t = true :=
  let ⟨T, hT⟩ := h; ⟨T, fun t ht => by rw [← D_seed]; exact hT t ht⟩

lemma seed_evW (j : ℕ) (h : EvW seed 0 (j : ℤ)) : ∃ T : ℕ, ∀ t, T ≤ t → Rule30Diagonals.D j t = false :=
  let ⟨T, hT⟩ := h; ⟨T, fun t ht => by rw [← D_seed]; exact hT t ht⟩

/-- **Lemma B1 for the seed:** no two adjacent left diagonals are both eventually white. -/
theorem seed_no_adjacent_white (j : ℕ) (h0 : ∃ T : ℕ, ∀ t, T ≤ t → Rule30Diagonals.D j t = false)
    (h1 : ∃ T : ℕ, ∀ t, T ≤ t → Rule30Diagonals.D (j + 1) t = false) : False := by
  have h1' : EvW seed 0 ((j : ℤ) + 1) := by
    have := evW_seed (j + 1) h1; push_cast at this; exact this
  exact no_adjacent_white seed 0 seed_leftmost.1 seed_leftmost.2 j (by positivity) (evW_seed j h0) h1'

/-- **Lemma B1 for the seed:** an eventually white left diagonal is followed two later by an eventually black one. -/
theorem seed_white_then_black (j : ℕ) (h0 : ∃ T : ℕ, ∀ t, T ≤ t → Rule30Diagonals.D j t = false) :
    ∃ T : ℕ, ∀ t, T ≤ t → Rule30Diagonals.D (j + 2) t = true := by
  apply seed_evB
  have := white_then_black seed 0 seed_leftmost.1 seed_leftmost.2 j (by positivity) (evW_seed j h0)
  push_cast; exact this

/-- **Lemma B2 for the seed:** no `P ≥ 1` is an eventual period of every left diagonal; the kit's `D_periodic`
gives the upper bound `2^j`, this is the matching lower bound: the eventual periods are unbounded. -/
theorem seed_periods_unbounded (P : ℕ) (hP : 1 ≤ P) :
    ¬ ∀ j : ℕ, ∃ T : ℕ, ∀ t, T ≤ t → Rule30Diagonals.D j (t + P) = Rule30Diagonals.D j t := by
  intro h
  apply lemma_B2 seed 0 seed_leftmost.1 seed_leftmost.2 P hP
  intro k
  obtain ⟨T, hT⟩ := h k
  exact ⟨T, fun t ht => by rw [D_seed, D_seed]; exact hT t ht⟩

/-- Quantitative: among the first `4^P + 2` left diagonals, one does not have eventual period `P`. -/
theorem seed_periods_unbounded_quant (P : ℕ) (hP : 1 ≤ P) :
    ¬ ∀ j : ℕ, j ≤ 4 ^ P + 1 → ∃ T : ℕ, ∀ t, T ≤ t → Rule30Diagonals.D j (t + P) = Rule30Diagonals.D j t := by
  intro h
  apply lemma_B2_quant seed 0 seed_leftmost.1 seed_leftmost.2 P hP
  intro k hk
  obtain ⟨T, hT⟩ := h k hk
  exact ⟨T, fun t ht => by rw [D_seed, D_seed]; exact hT t ht⟩

/-- **Lemma B2's corollary for the seed:** infinitely many left diagonals are eventually white, and infinitely
many eventually black. -/
theorem seed_infinitely_many_white (N : ℕ) :
    ∃ k : ℕ, N ≤ k ∧ ∃ T : ℕ, ∀ t, T ≤ t → Rule30Diagonals.D k t = false := by
  obtain ⟨k, hk, hw⟩ := infinitely_many_white seed 0 seed_leftmost.1 seed_leftmost.2 N
  exact ⟨k, hk, seed_evW k hw⟩

theorem seed_infinitely_many_black (N : ℕ) :
    ∃ k : ℕ, N ≤ k ∧ ∃ T : ℕ, ∀ t, T ≤ t → Rule30Diagonals.D k t = true := by
  obtain ⟨k, hk, hb⟩ := infinitely_many_black seed 0 seed_leftmost.1 seed_leftmost.2 N
  exact ⟨k, hk, seed_evB k hb⟩

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorems, as Lean prints them, in the kit's own `Rule30Diagonals.D`. Lemma B1, no two adjacent left diagonals of the seed are both eventually white, and white is followed two later by black:

```wl
opens = {"Ruliology.CellularAutomata.Rule30Diagonals", "Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
{rule30Submission["Rule30Submission.seed_no_adjacent_white"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.seed_white_then_black"]["TypeForm", "Open" -> opens]}
```

Lemma B2, no single period is eventual for every left diagonal, and the quantitative form:

```wl
thm = rule30Submission["Rule30Submission.seed_periods_unbounded"];
{thm["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.seed_periods_unbounded_quant"]["TypeForm", "Open" -> opens]}
```

Its corollary, infinitely many eventually white and infinitely many eventually black diagonals:

```wl
{rule30Submission["Rule30Submission.seed_infinitely_many_white"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.seed_infinitely_many_black"]["TypeForm", "Open" -> opens]}
```

The general statements, for every configuration with a leftmost black cell `e` (`D x0 e j t` is its `j`-th left diagonal): Lemma B2 and Lemma B3:

```wl
{rule30Submission["Rule30Submission.lemma_B2"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.lemma_B3_sharp"]["TypeForm", "Open" -> opens]}
```

The axioms of the headline are the three standard ones and nothing else:

```wl
thm["Axioms"]
```

The proof's structure, one level down from Lemma B2:

```wl
thm["CallGraph", "Depth" -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## What is not proved

- Nothing about the center column directly: the period of diagonal `j` is a power of two above `j`, so the center cell `D t t` is read from a diagonal that has not settled yet. The kit's own remark stands.
- Lemma B2 gives unboundedness and the bound `4^P + 1` on the index of a non-`P`-periodic diagonal; it does not give the exact doubling schedule, which the sample shows and Rowland describes.
- These are partial results about the pattern's left side, not a solution of Problem 1, and nothing about Problems 2 and 3.

## Provenance

Lemmas B1, B2 and B3 are RULE30-PRIZE.md section 8.59 and PROOFS.md entries 8, 9 and 12 of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT: proved by Local (Claude) on 2026-10-05, second-read by Cloud (Claude) and GPT, and machine-checked by Local in Lean on 2026-10-10; Cloud restated them on the kit's definitions and added the bridge to `Rule30Diagonals.D` on 2026-10-23. The unboundedness of the left diagonals' periods is Rowland's theorem (2006); the kit cites it without a formal statement. The mechanism of the proofs is Jen's left-permutivity (1986).

## References

[1] E. Jen, *Global properties of cellular automata*, Journal of Statistical Physics 43 (1986) 219–242.

[2] E. Rowland, *Local Nested Structure in Rule 30*, Complex Systems 16 (2006) 239–258.

[3] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[4] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[5] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): PROOFS.md entries 8, 9 and 12 and `tests/probes/lean/JenPow2.lean`, 2026.
