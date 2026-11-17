---
Template: ComputationalEssay
Name: A repeat on the center column cannot put its white run inside the settled band of left diagonals
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-23
Description: A partial result for Problem 1 of the Rule 30 Prize, proved in Lean against the official statements: Jen's clocked bound n ≤ a′ for a common block of length n on the center column and its right neighbour at times a < a′ improves to n ≤ a′ - M + 2P - 1 when the left diagonals 0 to M agree at times a′ - P and a′ and M < a′ - a
Abstract: Jen's theorem with a clock, the kit's window_jen_col, bounds a common block of length n on columns 0 and 1 at times a < a′ by n ≤ a′. The reason is a white run: row a′ is white at the distances a + 1 … n - 1 left of the center, which are the left diagonals a′ - n + 1 … a′ - a - 1. This essay proves that the run cannot lie in the band of diagonals that has settled. Theorem A⁗ (Rule30Submission.center_A4_sharp, for the kit's cell and Rule30Diagonals.D; theorem_A4_sharp for every configuration with a leftmost black cell L cells left of the column): if the diagonals 0 … M agree at times a′ - P and a′, with P ≥ 1, P ≤ a′ and M < a′ - a, then n ≤ L + a′ - M + 2P - 1. The tool is Lemma B3 (lemma_B3_sharp): inside such a band a white run bounded on the left by a black diagonal is at most 2P - 1 long, and Theorem A‴'s run has a black diagonal on its left because diagonal 0, the edge, is black. The kit has the clocked bound and the period-2^j bound for each left diagonal but no statement joining them. The verifier's replay accepts the module with the three standard axioms only. Nothing here decides Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, Jen's theorem, left diagonals, settled band, white run, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entries 10, 12 and 13](https://github.com/ghywel/placego/blob/main/PROOFS.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261022-c27323, the white end](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-c27323)"]
---

## The question

Rule 30 updates every cell from itself and its two neighbors: the new color is *left* XOR (*center* OR *right*). From a single black cell it grows a pattern whose center column looks random. Problem 1 of the Rule 30 Prize asks whether that column is ever eventually periodic. A periodic column repeats blocks; so the question is about repeats, and the first thing the kit knows about repeats is Jen's theorem with a clock.

The first 60 steps, with the center column in red:

```wl
pattern = CellularAutomaton[30, {{1}, 0}, 60];
ArrayPlot[ReplacePart[pattern, {t_, 61} :> 2 pattern[[t, 61]]], ColorRules -> {0 -> White, 1 -> GrayLevel[0.15], 2 -> StandardRed}, ImageSize -> 520]
```

**Jen's bound.** Suppose columns 0 and 1 (the center and its right neighbor) carry the same block of `n` values at times `a` and `a′`, `a < a′`. Rule 30 is left-permutive: a cell's left neighbor is determined by the cell's next value and its two right neighbors. So the two rows agree one cell further left per step down the block: the cell `m` to the left agrees at times `a + s` and `a′ + s` whenever `s + m < n`. But the pattern's left edge moves one cell left per step, with white beyond it: at distance `a′` left of the center, row `a′` is black and row `a` is white. Hence `n ≤ a′` (the kit's `Rule30MaskedJen.window_jen_col`; `L` more when the edge starts `L` cells left of the column).

**The white run.** The same argument says more: row `a′` is white at every distance `a + 1 … n - 1` left of the center (it agrees with row `a` there, which is beyond row `a`'s edge). In the coordinates of the left diagonals, `D k t = cell t (k - t)`, these cells are the diagonals `a′ - n + 1 … a′ - a - 1` at time `a′`. A long repeat is a long white run near the left edge. This essay shows that the run cannot sit inside the band of diagonals that has settled into a period.

## The repeats and the band, measured

Columns 0 and 1 for 400 steps, and the longest common blocks `{n, a, a′}` of the pair:

```wl
steps = 400;
rows = CellularAutomaton[30, {{1}, 0}, steps];
cell[t_, p_] := rows[[t + 1, steps + 1 + p]];
c0 = Table[cell[t, 0], {t, 0, steps}]; c1 = Table[cell[t, 1], {t, 0, steps}];
block[a_, a2_] := Module[{n = 0}, While[a2 + n <= steps && c0[[a + n + 1]] == c0[[a2 + n + 1]] && c1[[a + n + 1]] == c1[[a2 + n + 1]], n++]; n];
blocks = Reverse[Sort[Flatten[Table[{block[a, a2], a, a2}, {a2, 1, steps}, {a, 0, a2 - 1}], 1]]];
Take[blocks, 8]
```

The settled band: `settled[P, t]` is the largest `M` such that the diagonals `0 … M` agree at times `t - P` and `t` (so `-1` if diagonal 0 does not; it always does, the edge is black). The kit proves that diagonal `k` is eventually periodic with period dividing `2^k`; the measured periods grow slowly, so for small `P` the band has a fixed width and for `P = 8` it covers most of the row (the test is agreement of two rows, not eventual periodicity, so the `P = 16` band comes out narrower than the `P = 8` one):

```wl
diag[k_, t_] := cell[t, k - t];
settled[P_, t_] := Module[{m = -1}, While[m + 1 <= t && diag[m + 1, t - P] == diag[m + 1, t], m++]; m];
Grid[Prepend[Table[Prepend[Table[settled[P, t], {P, {1, 2, 4, 8, 16}}], t], {t, {100, 200, 400}}], {"t, P", 1, 2, 4, 8, 16}], Frame -> All]
```

Theorem A⁗'s bound for the six longest blocks and `P = 1, 2, 4` (the hypothesis `M < a′ - a` holds for these), against Jen's bound `a′`:

```wl
Grid[Prepend[Flatten[Table[With[{n = b[[1]], a = b[[2]], a2 = b[[3]], M = settled[P, b[[3]]]}, If[P <= a2 && M < a2 - a, {{b, P, M, a2 - M + 2 P - 1, a2, n <= a2 - M + 2 P - 1}}, {}]], {b, Take[blocks, 6]}, {P, {1, 2, 4}}], 2], {"{n, a, a′}", "P", "M = settled[P, a′]", "bound a′ - M + 2P - 1", "Jen's bound a′", "holds"}], Frame -> All]
```

Both bounds are far above the blocks actually seen (`n ≤ 12` here): the theorem is structural, about where a repeat's white run can be, not a tight count. Its content is the gain `M - 2P + 1` over Jen: the band of settled diagonals pushes the run out, up to a margin of `2P - 1`.

## The idea of the proof

Write `D k t` for the `k`-th left diagonal at time `t` (the cell `k` places right of the moving edge, so `D 0 t` is the edge, black for ever, and `D k t` is white for `k < 0`).

**Lemma B3 (sharp).** Suppose the diagonals `0 … M` agree at times `t - P` and `t`, and at time `t` the diagonals `g + 1 … M′` are white with `g` black and `M′ ≤ M`. One step back, the run is either older (white two cells wider, its black bound two further left) or newborn (black on `g - 1 … M′ - 2`, and black at `M′ - 1` or `M′`). Following it back `P` steps: if it was older all the way, its black bound has moved to `g - 2P`, and the run at time `t - P` covers `g`, which is black at time `t`, against the agreement; so a birth happened at some step `s0 < P`. Going forward from the birth, a white run only loses cells, two a step from its left, so the white cells of time `t - P` (the same as at time `t`, by the agreement) reach the birth time still covering `M′ - 1` and `M′`, one of which is black there. Hence `M′ - g ≤ 2P - 1`.

**Theorem A⁗.** The white run of the repeat, at time `a′`, is the diagonals `L + a′ - n + 1 … a′ - a - 1`, which contain `L + a′ - n + 1 … M` when `M < a′ - a`. Diagonal 0 is black, so the run has a nearest black diagonal `g` on its left, `g ≤ L + a′ - n`. Lemma B3 bounds the run `g + 1 … M` by `2P - 1`, so `M - (L + a′ - n) ≤ 2P - 1`, which is the claim.

Everything in this section is prose. The proof is the next section.

## The formal proof

The module, as the verifier rebuilds and checks it. `edge` is the moving left edge on the kit's `evol`; `step_inv` is left-permutivity read right to left; `agree` propagates a common block leftward; `theorem_A'` and `theorem_A3_white` are Jen's bound and the white run; `D`, `D_succ`, `constraint`, `back`, `fwd` and `lemma_B3_sharp` are the band argument; `theorem_A4_sharp` assembles them; `D_seed`, `D_seed_neg` and `per_seed` bridge the module's diagonals to the kit's `Rule30Diagonals.D` for the single seed, and `center_A4_sharp` is the headline on the kit's `cell`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["import Rule30PrizeKit
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
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorem, as Lean prints it: for the center column, with the kit's `cell` and `Rule30Diagonals.D`:

```wl
opens = {"Ruliology.CellularAutomata.Rule30Jen", "Ruliology.CellularAutomata.Rule30Diagonals", "Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.center_A4_sharp"];
thm["TypeForm", "Open" -> opens]
```

The general form, for every configuration with a leftmost black cell `L` cells left of column `i`; the module's `D x0 e k t = evol x0 t (e - t + k)` is the `k`-th left diagonal from the edge `e`:

```wl
rule30Submission["Rule30Submission.theorem_A4_sharp"]["TypeForm", "Open" -> opens]
```

The two ingredients, Lemma B3 in its sharp form and Theorem A‴'s corollary (a black diagonal `b < a′ - a` at time `a′` bounds the block by `L + a′ - b`):

```wl
{rule30Submission["Rule30Submission.lemma_B3_sharp"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.theorem_A3"]["TypeForm", "Open" -> opens]}
```

The axioms of the headline are the three standard ones and nothing else:

```wl
thm["Axioms"]
```

The proof's structure, one level down from the headline:

```wl
thm["CallGraph", "Depth" -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## What is not proved

- The hypothesis `hper` (the diagonals `0 … M` agree at `a′ - P` and `a′`) is not known to hold for the repeats of the center column with `M` large and `P` small together: the diagonals the run reaches have periods up to `2^(a′ - a)`, far above `a′ - a`. The theorem says where a repeat's run cannot be; it does not exclude any period.
- The bound `n ≤ a′ - M + 2P - 1` is far from the observed block lengths, as the table shows; it is a structural statement, not an estimate of repeats.
- This is a partial result about the pattern's left side. It does not touch Problems 2 and 3.

## Provenance

Theorem A‴, Lemma B3 and Theorem A⁗ are RULE30-PRIZE.md section 8.59 and PROOFS.md entries 10, 12 and 13 of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT: proved by Local (Claude) on 2026-10-05 and 2026-10-06, second-read by Cloud (Claude) and GPT, and machine-checked by Local in Lean on 2026-10-10 (`tests/probes/lean/TheoremA4.lean`); Cloud restated them on the kit's definitions and added the bridge to `cell` and `Rule30Diagonals.D` on 2026-10-23. The mechanism is Jen's left-permutivity (1986), as the kit's `window_jen_col` uses it. The companion submission on the band itself (Lemmas B1 and B2, the unbounded periods) is filed separately.

## References

[1] E. Jen, *Global properties of cellular automata*, Journal of Statistical Physics 43 (1986) 219–242.

[2] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[3] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[4] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): PROOFS.md entries 10, 12 and 13 and `tests/probes/lean/TheoremA4.lean`, 2026.
