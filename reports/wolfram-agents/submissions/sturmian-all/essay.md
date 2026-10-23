---
Template: ComputationalEssay
Name: Every Sturmian word, of every slope and every intercept, is excluded as the right neighbour of a period-2 center column
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-23
Description: A partial result for Problem 1 of the Rule 30 Prize in the period-2 case, proved in Lean against the official statements: if column 0 reads the clock 0101… from some time on and the configuration has a leftmost black cell, then the even-time bits of column 1 are not a mechanical word of any irrational slope and any intercept, nor any finite block code of one; the proof is a pigeonhole on the n + 1 blocks of length n, with no continued fractions
Abstract: The first open case of Problem 1 is period 2, the clock 0101…. Under the clock, rule 30's left-permutivity determines column -1 from the even-time bits of column 1, the visible bits, and the record's Corollary F (Rule30Submission.corollary_F, submission 5) says the visible bits of a configuration with a leftmost black cell have no near-squares at unbounded scales, no fixed slack K and pairs i < i′ with i′ - i unbounded whose common future lasts i′ - K. This essay proves that every mechanical word, mech α θ i = ⌊θ + (i+1)α⌋ - ⌊θ + iα⌋ with irrational slope 0 < α < 1 and any intercept θ (equivalently, 1 iff the fractional part of θ + iα lies in [1 - α, 1)), has such near-squares with slack 1: a Sturmian word has at most n + 1 distinct blocks of length n, so two of the n + 2 blocks starting at positions 0 to n + 1 coincide (Rule30Submission.exists_block_collision), their common future is at least n, and the gap between them must grow, because a block of length n repeating at a gap q ≤ H would make the count of ones in kq consecutive letters equal kp while the floor formula keeps it within 1 of kqα, impossible for k > 1 / min |p - qα| (no_small_period). Hence no configuration with a leftmost black cell and the clock on column 0 has a Sturmian word of any slope and intercept as its visible bits (sturmian_excluded, sturmian_excluded_clock0, sturmian_excluded_fract), nor any finite block code of one (sturmian_block_excluded). This is the record's Theorem E in full, by a combinatorial route found by GPT after the characteristic case had been filed; the pigeonhole is Bugeaud and Kim's early-repetition lemma. The verifier's replay accepts the module with the three standard axioms only. Nothing here decides Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, period 2, Sturmian words, mechanical words, factor complexity, near-squares, Corollary F, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entries 11 and 14](https://github.com/ghywel/placego/blob/main/PROOFS.md)", "[Y. Bugeaud and D. H. Kim, A new complexity function, repetitions in Sturmian words, and irrationality exponents of Sturmian numbers](https://irma.math.unistra.fr/~bugeaud/travaux/complsturm3ndRev1.pdf)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261022-91b0b0, Corollary F](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-91b0b0)", "[Submission R30-20261023-e872a3, the characteristic case](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-e872a3)"]
---

## The question

Rule 30 updates every cell from itself and its two neighbors: the new color is *left* XOR (*center* OR *right*). From a single black cell it grows a pattern whose center column looks random. Problem 1 of the Rule 30 Prize asks whether that column is ever eventually periodic; the shortest case is period 2, the clock `0101…`, the kit's open `Rule30ZeroBoundary.Q01` for the single seed.

The first 60 steps, with the center column in red:

```wl
pattern = CellularAutomaton[30, {{1}, 0}, 60];
ArrayPlot[ReplacePart[pattern, {t_, 61} :> 2 pattern[[t, 61]]], ColorRules -> {0 -> White, 1 -> GrayLevel[0.15], 2 -> StandardRed}, ImageSize -> 520]
```

Under the clock, rule 30's left-permutivity makes column `-1` black at odd times and the complement of column `1` at even times, so column `1`'s even-time bits, the *visible bits*, carry everything the clock allows. Our submission 5 proved **Corollary F**: for a configuration with a leftmost black cell and the clock on column 0, the visible bits have no *near-squares at unbounded scales*, no fixed slack `K` and pairs `i < i′` with `i′ - i` unbounded whose common future `c(i + s) = c(i′ + s)` lasts `s < i′ - K`. Submission 7 excluded the characteristic Sturmian words, one intercept per slope, by their standard words. This essay excludes **every** Sturmian word, every irrational slope and every intercept, and every finite block code of one, by an argument that needs no continued fractions at all.

## Mechanical words and their blocks

The mechanical word of slope `α` and intercept `θ` is `c(i) = ⌊θ + (i + 1)α⌋ - ⌊θ + iα⌋`, which is `1` exactly when the fractional part of `θ + iα` lies in `[1 - α, 1)`. For irrational `α` these are the Sturmian words. The golden slope with intercept `1/2`, and the count of distinct blocks of each length `n`, which is `n + 1` (the Sturmian signature; the module proves only the inequality `≤ n + 1`, which is all the argument needs):

```wl
mech[alpha_, theta_, n_] := Table[Floor[theta + (i + 1) alpha] - Floor[theta + i alpha], {i, 0, n - 1}];
golden = (Sqrt[5] - 1)/2;
c = mech[golden, 1/2, 60000];
{StringJoin[ToString /@ Take[c, 40]], Table[Length[Union[Table[c[[s + 1 ;; s + n]], {s, 0, 49999}]]], {n, 1, 12}]}
```

**The pigeonhole.** Among the `n + 2` blocks of length `n` starting at positions `0, 1, …, n + 1`, two must coincide, at positions `i < j ≤ n + 1`. Their common future is then at least `n ≥ j - 1`: a near-square at the pair `(i, j)` with slack at most 1. The collisions for three slopes and intercepts, with the actual common future and the slack `j - (common future)`, which is never above 1:

```wl
collide[c_, n_] := Module[{seen = <||>, f}, Do[f = c[[s + 1 ;; s + n]]; If[KeyExistsQ[seen, f], Return[{seen[f], s}, Module], seen[f] = s], {s, 0, n + 1}]];
table[alpha_, theta_] := Module[{w = mech[alpha, theta, 20000]}, Table[With[{r = collide[w, n]}, With[{i = r[[1]], j = r[[2]]}, With[{l = LengthWhile[Range[0, Length[w] - j - 1], w[[i + # + 1]] == w[[j + # + 1]] &]}, {n, i, j, j - i, l, j - l}]]], {n, {5, 10, 20, 50, 100, 200, 500, 1000, 2000}}]];
Grid[Prepend[Join[table[golden, 1/2], table[Sqrt[2] - 1, 1/10]], {"n", "i", "j", "gap", "common future", "slack"}], Frame -> All]
```

**The gap grows.** Why can the two coinciding blocks not sit at a bounded distance `q`? If a block of length `n` repeats at gap `q`, the word has period `q` on `n` letters, so its first `kq` letters, `k = ⌊n/q⌋`, are `k` copies of one `q`-letter block with `p` ones, `kp` ones in all. But the ones in any `m` consecutive letters are `⌊θ + (i + m)α⌋ - ⌊θ + iα⌋`, within 1 of `mα`. So `k |p - qα| < 1`. For an irrational slope, `|p - qα|` has a positive minimum `d_H` over `1 ≤ q ≤ H`, and once `n > H(1 + 1/d_H)` every `q ≤ H` gives `k > 1/d_H`: a contradiction. Hence the collisions of the pigeonhole have gaps beyond every bound, and Corollary F applies with `K = 1`.

## The forced left half of a non-characteristic word

Take the clock as column 0 and the golden word with intercept `1/2` as the visible bits, and compute the forced left half by left-permutivity. The theorem says its row at time 0 has no leftmost black cell; its black cells by depth, from 3,000 steps:

```wl
w = mech[golden, 1/2, 2000];
steps = 3000;
col0 = Table[Mod[t, 2], {t, 0, steps - 1}];
col1 = Table[If[EvenQ[t], w[[t/2 + 1]], 0], {t, 0, steps - 1}];
colm1 = Table[BitXor[col0[[t + 2]], BitOr[col0[[t + 1]], col1[[t + 1]]]], {t, 0, steps - 2}];
row0 = Module[{a = colm1, b = col0, out = {col0[[1]], colm1[[1]]}}, Do[{a, b} = {Table[BitXor[a[[t + 1]], BitOr[a[[t]], b[[t]]]], {t, 1, Length[a] - 1}], a}; AppendTo[out, a[[1]]], {m, 2, steps - 2}]; out];
blacks = Flatten[Position[row0, 1]] - 1;
{Length[row0], Take[blacks, 30], Length[blacks], Last[blacks], Max[Differences[blacks]]}
```

About half the depths are black and the largest spacing between consecutive black depths is 14 cells.

## The idea of the proof

**The block at `i` is a function of `x = fract(θ + iα)` through `n` thresholds.** Write `⌊θ + (i + k)α⌋ = ⌊θ + iα⌋ + ⌊x + kα⌋` and `⌊x + kα⌋ = ⌊kα⌋ + [x + fract(kα) ≥ 1]`. So the block of length `n` at `i` is determined by the set `S(x)` of `k ≤ n` with `1 ≤ x + fract(kα)`. That set grows with `x`, never contains `k = 0`, so has at most `n` elements; the `n + 2` positions `0 … n + 1` give at most `n + 1` cardinalities, two positions share one, and nested sets of equal size are equal. That is `block_eq_of_thr` and `exists_block_collision`.

**No long block of a bounded period** is the telescoping argument above: `sum_mechZ` (the ones are a difference of floors), `sum_periodic` (periodicity makes them `k` times one block), `exists_gap` (the positive minimum, from irrationality) and `no_small_period`.

**The exclusion.** For every `N`, a pair `i < j` with gap at least `N`, `j ≤ n + 1` and equal blocks of length `n` is a near-square with slack 1 (`sturmian_pairs`); Corollary F finishes it. A clock that starts at time `T0` is handled by the shifted intercept `θ + T0 α`, whose word is the suffix of the original (`mech_shift_intercept`), at slack `T0 + 1`. A sliding block code of window `r` keeps a near-square with slack raised by `r` (`image_near_square`).

Everything in this section is prose. The proofs are the next section.

## The formal proof

The module, as the verifier rebuilds and checks it: the record's Lemma B2 and Theorem A‴ on the kit's `evol`, Corollary F (`col_m1`, `blocks_of_visible`, `corollary_F`), block codes (`image`, `image_near_square`), the mechanical words (`mechZ`, `mech`, `mech_eq_fract`, `floor_decomp`, `floor_shift`, `thr`, `block_eq_of_thr`, `exists_block_collision`, `exists_gap`, `sum_mechZ`, `mech_shift`, `sum_periodic`, `no_small_period`, `sturmian_pairs`, `mech_shift_intercept`) and the headlines.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["import Rule30PrizeKit
import Mathlib

/-!
# Every Sturmian word, of every slope and every intercept, is excluded as the right neighbour of a period-2 center column

**A partial result for Problem 1**, in the period-2 case: Theorem E of the record (PROOFS.md entry 14), for every
intercept, by word combinatorics on top of Corollary F. Suppose column `0` of a configuration reads the clock
`0101…` from some time `T0` and the configuration has a leftmost black cell `L ≥ 1` cells left of column `0`. Rule 30's
left-permutivity makes column `-1` the complement of column `1` at even times and black at odd times, so the
*visible bits* `evol x0 (2 i) 1` carry everything the clock allows. **Corollary F** (`corollary_F`, submission 5):
the visible bits have no near-squares at unbounded scales, no fixed slack `K` and pairs `i < i′` with `i′ - i`
unbounded whose common future lasts `i′ - K`.

This module shows that **every mechanical word** `mech α θ i = ⌊θ + (i+1)α⌋ - ⌊θ + iα⌋` with irrational slope
`0 < α < 1` and any intercept `θ` (the record's `1` iff `fract (θ + iα) ∈ [1 - α, 1)`, `mech_eq_fract`) has such
near-squares with slack `1`, by the pigeonhole route of GPT's GC1694 (the early-repetition lemma of Bugeaud and Kim):

* `exists_block_collision`: among the `n + 2` blocks of length `n` at positions `0 … n + 1`, two coincide. The block
  at `i` is determined by the set of `k ≤ n` with `1 ≤ fract (θ + iα) + fract (kα)` (`block_eq_of_thr`), a set
  nested in `fract (θ + iα)` with at most `n` elements; so the `n + 2` positions take at most `n + 1` cardinalities,
  and equal cardinalities of nested sets are equal sets.
* `no_small_period`: for `n` large, no block of length `n` repeats at a gap `q ≤ H`: the ones in `[i, i + kq)` are
  `⌊θ + (i + kq)α⌋ - ⌊θ + iα⌋`, within `1` of `kqα`, and periodicity makes them `kp`, so `k |p - qα| < 1`; but
  `|p - qα| ≥ d_H > 0` for `1 ≤ q ≤ H` (`exists_gap`, irrationality) while `k = ⌊n/q⌋ > 1/d_H`.
* `sturmian_pairs`: hence for every `N` a pair `i < j` with `j - i ≥ N`, `j ≤ n + 1` and the blocks of length `n`
  equal: a near-square with slack `1`. A clock from `T0` is handled by the shifted intercept `θ + T0 α`
  (`mech_shift_intercept`), with slack `T0 + 1`.

Hence (`sturmian_excluded`, `sturmian_excluded_clock0`, `sturmian_excluded_fract`): **no configuration with a
leftmost black cell and the clock on column `0` has a Sturmian word, of any irrational slope and any intercept, as
its visible bits**; and, since a near-square survives every sliding block code with its slack raised by the window
(`image_near_square`), **nor any finite block code of one** (`sturmian_block_excluded`).

**What is new relative to the kit.** The kit's `Rule30ZeroBoundary.Q01` asks the period-2 question for the single
seed; `Rule30DrivenLeft.no_periodic_column` excludes eventually periodic drivers; its CATALOG remarks that Sturmian
sequences are not eventually periodic. Nothing in the kit excludes any aperiodic right neighbour under the clock.
This excludes every Sturmian word and every finite block code of one: uncountably many right neighbours of zero
entropy. Submission 7 (R30-20261023-e872a3) did the characteristic intercept by the standard words; this is every
intercept, with no continued fractions.

**Provenance.** Theorem E is RULE30-PRIZE.md §8.57, PROOFS.md entry 14 of the Wolfram · Collatz · Mahler record
(github.com/ghywel/placego), proved by Local (Claude) on 2026-10-05 by a Diophantine argument; the combinatorial
route through Corollary F is GPT's (GC1694, 2026-10-23), after Cloud's measurements at convergent periods had
suggested none existed; the pigeonhole is Bugeaud and Kim's Lemma 2.2 (*A new complexity function, repetitions in
Sturmian words, and irrationality exponents of Sturmian numbers*, Trans. AMS 2019). Formalized by Cloud (Claude) on
2026-10-23 on the kit's `evol`. Sources: E. Jen, J. Stat. Phys. 43 (1986); Y. Bugeaud and D. H. Kim (2019).
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

/-! ## Sliding block codes of the characteristic words are excluded too -/

/-- A sliding block code of window `r`: `image f r c i = f [c i, …, c (i + r - 1)]`. The letter exchange is the
window-`1` code `f = not`; every finite block factor of the word is one of these. -/
def image (f : List Bool → Bool) (r : ℕ) (c : ℕ → Bool) (i : ℕ) : Bool :=
  f ((List.range r).map fun j => c (i + j))

theorem image_congr (f : List Bool → Bool) (r : ℕ) (c : ℕ → Bool) (i i' : ℕ)
    (h : ∀ j, j < r → c (i + j) = c (i' + j)) : image f r c i = image f r c i' := by
  unfold image
  congr 1
  apply List.map_congr_left
  intro j hj
  rw [List.mem_range] at hj
  exact h j hj

/-- A near-square of slack `K` in `c` is a near-square of slack `K + r` in its window-`r` code. -/
theorem image_near_square (f : List Bool → Bool) (r : ℕ) (c : ℕ → Bool) (K i i' : ℕ)
    (hc : ∀ s, s + K < i' → c (i + s) = c (i' + s)) :
    ∀ s, s + (K + r) < i' → image f r c (i + s) = image f r c (i' + s) := by
  intro s hs
  apply image_congr
  intro j hj
  rw [Nat.add_assoc, Nat.add_assoc]
  exact hc (s + j) (by omega)

/-! ## Mechanical words: the floor form, the block determined by `n` thresholds, no long bounded-period block -/

/-- The lower mechanical word of slope `α` and intercept `θ`, as an integer step: `⌊θ + (i+1)α⌋ - ⌊θ + iα⌋`. -/
noncomputable def mechZ (α θ : ℝ) (i : ℕ) : ℤ := ⌊θ + ((i : ℝ) + 1) * α⌋ - ⌊θ + (i : ℝ) * α⌋

/-- The same word as a bit. -/
noncomputable def mech (α θ : ℝ) (i : ℕ) : Bool := decide (mechZ α θ i = 1)

theorem floor_step (y a : ℝ) (h0 : 0 ≤ a) (h1 : a < 1) : ⌊y + a⌋ - ⌊y⌋ = 0 ∨ ⌊y + a⌋ - ⌊y⌋ = 1 := by
  have h2 : ⌊y⌋ ≤ ⌊y + a⌋ := Int.floor_le_floor (by linarith)
  have h3 : ⌊y + a⌋ < ⌊y⌋ + 2 := by
    rw [Int.floor_lt]; push_cast
    have := Int.lt_floor_add_one y; linarith
  omega

theorem mechZ_zero_or_one (α θ : ℝ) (h0 : 0 ≤ α) (h1 : α < 1) (i : ℕ) : mechZ α θ i = 0 ∨ mechZ α θ i = 1 := by
  unfold mechZ
  rw [show θ + ((i : ℝ) + 1) * α = (θ + (i : ℝ) * α) + α by ring]
  exact floor_step _ _ h0 h1

theorem mechZ_eq_ite (α θ : ℝ) (h0 : 0 ≤ α) (h1 : α < 1) (i : ℕ) :
    mechZ α θ i = if mech α θ i then 1 else 0 := by
  unfold mech
  rcases mechZ_zero_or_one α θ h0 h1 i with h | h <;> simp [h]

/-- The record's definition: the bit is `1` iff the fractional part of `θ + iα` lies in `[1 - α, 1)`. -/
theorem mech_eq_fract (α θ : ℝ) (h0 : 0 ≤ α) (h1 : α < 1) (i : ℕ) :
    mech α θ i = decide (1 - α ≤ Int.fract (θ + (i : ℝ) * α)) := by
  unfold mech mechZ
  set y := θ + (i : ℝ) * α with hy
  rw [show θ + ((i : ℝ) + 1) * α = y + α by rw [hy]; ring]
  have hf := Int.floor_add_fract y
  have e : ⌊y + α⌋ = ⌊y⌋ + ⌊Int.fract y + α⌋ := by
    rw [show y + α = (⌊y⌋ : ℝ) + (Int.fract y + α) by linarith, Int.floor_intCast_add]
  rw [e]
  have hfr0 := Int.fract_nonneg y
  have hfr1 := Int.fract_lt_one y
  by_cases hc : 1 - α ≤ Int.fract y
  · have : ⌊Int.fract y + α⌋ = 1 := by rw [Int.floor_eq_iff]; constructor <;> push_cast <;> linarith
    simp [this, hc]
  · have : ⌊Int.fract y + α⌋ = 0 := by rw [Int.floor_eq_iff]; constructor <;> push_cast <;> linarith
    simp [this, hc]

/-! ### The block at `i` is determined by `x = fract (θ + iα)` through `n` thresholds -/

/-- `⌊x + kα⌋ = ⌊kα⌋ + jump`, where the jump is `1` iff `1 ≤ x + fract (kα)`. -/
theorem floor_decomp (α x : ℝ) (hx0 : 0 ≤ x) (hx1 : x < 1) (k : ℕ) :
    ⌊x + (k : ℝ) * α⌋ = ⌊(k : ℝ) * α⌋ + if 1 ≤ x + Int.fract ((k : ℝ) * α) then 1 else 0 := by
  have hf := Int.floor_add_fract ((k : ℝ) * α)
  have h0 := Int.fract_nonneg ((k : ℝ) * α)
  have h1 := Int.fract_lt_one ((k : ℝ) * α)
  rw [show x + (k : ℝ) * α = (⌊(k : ℝ) * α⌋ : ℝ) + (x + Int.fract ((k : ℝ) * α)) by linarith, Int.floor_intCast_add]
  congr 1
  split_ifs with hc
  · rw [Int.floor_eq_iff]; constructor <;> push_cast <;> linarith
  · rw [Int.floor_eq_iff]; constructor <;> push_cast <;> linarith

/-- The floor at `i + k` from the floor at `i` and the fractional part. -/
theorem floor_shift (α θ : ℝ) (i k : ℕ) :
    ⌊θ + ((i + k : ℕ) : ℝ) * α⌋ = ⌊θ + (i : ℝ) * α⌋ + ⌊Int.fract (θ + (i : ℝ) * α) + (k : ℝ) * α⌋ := by
  have hf := Int.floor_add_fract (θ + (i : ℝ) * α)
  rw [show θ + ((i + k : ℕ) : ℝ) * α = (⌊θ + (i : ℝ) * α⌋ : ℝ) + (Int.fract (θ + (i : ℝ) * α) + (k : ℝ) * α) by
    push_cast; linarith, Int.floor_intCast_add]

/-- The threshold set of `x` among the first `n + 1` multiples. -/
noncomputable def thr (α : ℝ) (n : ℕ) (x : ℝ) : Finset ℕ :=
  (Finset.range (n + 1)).filter fun k => 1 ≤ x + Int.fract ((k : ℝ) * α)

theorem thr_mono (α : ℝ) (n : ℕ) {x x' : ℝ} (h : x ≤ x') : thr α n x ⊆ thr α n x' := by
  intro k hk
  simp only [thr, Finset.mem_filter] at hk ⊢
  exact ⟨hk.1, by linarith [hk.2]⟩

theorem thr_card_le (α : ℝ) (n : ℕ) (x : ℝ) (hx1 : x < 1) : (thr α n x).card ≤ n := by
  have hsub : thr α n x ⊆ (Finset.range (n + 1)).erase 0 := by
    intro k hk
    simp only [thr, Finset.mem_filter] at hk
    rw [Finset.mem_erase]
    refine ⟨?_, hk.1⟩
    rintro rfl
    simp at hk
    linarith
  have := Finset.card_le_card hsub
  rw [Finset.card_erase_of_mem (by simp), Finset.card_range] at this
  omega

/-- Two positions whose threshold sets agree carry the same block of length `n`. -/
theorem block_eq_of_thr (α θ : ℝ) (n i j : ℕ)
    (h : thr α n (Int.fract (θ + (i : ℝ) * α)) = thr α n (Int.fract (θ + (j : ℝ) * α))) :
    ∀ s, s < n → mech α θ (i + s) = mech α θ (j + s) := by
  intro s hs
  have key : ∀ (m : ℕ) (k : ℕ), k ≤ n →
      ⌊θ + ((m + k : ℕ) : ℝ) * α⌋ - ⌊θ + (m : ℝ) * α⌋ =
        ⌊(k : ℝ) * α⌋ + if k ∈ thr α n (Int.fract (θ + (m : ℝ) * α)) then 1 else 0 := by
    intro m k hk
    rw [floor_shift, floor_decomp α _ (Int.fract_nonneg _) (Int.fract_lt_one _) k]
    simp only [thr, Finset.mem_filter, Finset.mem_range]
    by_cases hc : 1 ≤ Int.fract (θ + (m : ℝ) * α) + Int.fract ((k : ℝ) * α)
    · rw [if_pos hc, if_pos ⟨by omega, hc⟩]; ring
    · rw [if_neg hc, if_neg (fun h => hc h.2)]; ring
  unfold mech mechZ
  have e1 := key i (s + 1) (by omega)
  have e2 := key i s (by omega)
  have e3 := key j (s + 1) (by omega)
  have e4 := key j s (by omega)
  have hi : ⌊θ + (((i + s : ℕ) : ℝ) + 1) * α⌋ - ⌊θ + ((i + s : ℕ) : ℝ) * α⌋ =
      (⌊θ + ((i + (s + 1) : ℕ) : ℝ) * α⌋ - ⌊θ + (i : ℝ) * α⌋) - (⌊θ + ((i + s : ℕ) : ℝ) * α⌋ - ⌊θ + (i : ℝ) * α⌋) := by
    rw [show (((i + s : ℕ) : ℝ) + 1) = ((i + (s + 1) : ℕ) : ℝ) by push_cast; ring]; ring
  have hj : ⌊θ + (((j + s : ℕ) : ℝ) + 1) * α⌋ - ⌊θ + ((j + s : ℕ) : ℝ) * α⌋ =
      (⌊θ + ((j + (s + 1) : ℕ) : ℝ) * α⌋ - ⌊θ + (j : ℝ) * α⌋) - (⌊θ + ((j + s : ℕ) : ℝ) * α⌋ - ⌊θ + (j : ℝ) * α⌋) := by
    rw [show (((j + s : ℕ) : ℝ) + 1) = ((j + (s + 1) : ℕ) : ℝ) by push_cast; ring]; ring
  rw [hi, hj, e1, e2, e3, e4, h]

/-- **Pigeonhole:** among the `n + 2` blocks of length `n` at positions `0 … n + 1`, two coincide. -/
theorem exists_block_collision (α θ : ℝ) (n : ℕ) :
    ∃ i j, i < j ∧ j ≤ n + 1 ∧ ∀ s, s < n → mech α θ (i + s) = mech α θ (j + s) := by
  have hmaps : ∀ a ∈ Finset.range (n + 2),
      (thr α n (Int.fract (θ + (a : ℝ) * α))).card ∈ Finset.range (n + 1) := by
    intro a _
    rw [Finset.mem_range]
    have := thr_card_le α n (Int.fract (θ + (a : ℝ) * α)) (Int.fract_lt_one _)
    omega
  obtain ⟨a, ha, b, hb, hab, heq⟩ := Finset.exists_ne_map_eq_of_card_lt_of_maps_to
    (by simp : (Finset.range (n + 1)).card < (Finset.range (n + 2)).card) hmaps
  rw [Finset.mem_range] at ha hb
  -- equal cardinalities of nested sets give equal sets
  have hthr : ∀ u v : ℕ, (thr α n (Int.fract (θ + (u : ℝ) * α))).card = (thr α n (Int.fract (θ + (v : ℝ) * α))).card →
      thr α n (Int.fract (θ + (u : ℝ) * α)) = thr α n (Int.fract (θ + (v : ℝ) * α)) := by
    intro u v huv
    rcases le_total (Int.fract (θ + (u : ℝ) * α)) (Int.fract (θ + (v : ℝ) * α)) with hle | hle
    · exact Finset.eq_of_subset_of_card_le (thr_mono α n hle) huv.ge
    · exact (Finset.eq_of_subset_of_card_le (thr_mono α n hle) huv.le).symm
  rcases lt_or_gt_of_ne hab with hlt | hgt
  · exact ⟨a, b, hlt, by omega, block_eq_of_thr α θ n a b (hthr a b heq)⟩
  · exact ⟨b, a, hgt, by omega, block_eq_of_thr α θ n b a (hthr b a heq.symm)⟩

/-! ### No long block of a bounded period, for an irrational slope -/

/-- The distance from `qα` to the integers is positive for `q ≥ 1`, uniformly for `q ≤ H`. -/
theorem exists_gap (α : ℝ) (hα : Irrational α) (H : ℕ) :
    ∃ d : ℝ, 0 < d ∧ ∀ q : ℕ, 1 ≤ q → q ≤ H → ∀ p : ℤ, d ≤ |(p : ℝ) - (q : ℝ) * α| := by
  induction H with
  | zero => exact ⟨1, one_pos, fun q h1 h2 => by omega⟩
  | succ H ih =>
    obtain ⟨d, hd, hdq⟩ := ih
    set f := Int.fract (((H + 1 : ℕ) : ℝ) * α) with hf
    have hf0 : 0 ≤ f := Int.fract_nonneg _
    have hf1 : f < 1 := Int.fract_lt_one _
    have hfne : f ≠ 0 := by
      intro h
      have hirr : Irrational (((H + 1 : ℕ) : ℝ) * α) := by
        rw [mul_comm]; exact Irrational.mul_natCast hα (by omega)
      apply Irrational.ne_int hirr ⌊((H + 1 : ℕ) : ℝ) * α⌋
      have := Int.floor_add_fract (((H + 1 : ℕ) : ℝ) * α)
      rw [← hf, h, add_zero] at this
      exact this.symm
    have hfpos : 0 < f := lt_of_le_of_ne hf0 (Ne.symm hfne)
    refine ⟨min d (min f (1 - f)), by positivity, fun q h1 h2 p => ?_⟩
    rcases Nat.lt_or_ge q (H + 1) with hq | hq
    · exact le_trans (min_le_left _ _) (hdq q h1 (by omega) p)
    · have hqe : q = H + 1 := by omega
      subst hqe
      have hfl := Int.floor_add_fract (((H + 1 : ℕ) : ℝ) * α)
      rw [← hf] at hfl
      rcases le_or_gt p ⌊((H + 1 : ℕ) : ℝ) * α⌋ with hp | hp
      · have : (p : ℝ) ≤ ⌊((H + 1 : ℕ) : ℝ) * α⌋ := by exact_mod_cast hp
        calc min d (min f (1 - f)) ≤ f := le_trans (min_le_right _ _) (min_le_left _ _)
          _ ≤ |(p : ℝ) - ((H + 1 : ℕ) : ℝ) * α| := by
            rw [abs_sub_comm, abs_of_nonneg (by linarith)]; linarith
      · have : (⌊((H + 1 : ℕ) : ℝ) * α⌋ : ℝ) + 1 ≤ p := by exact_mod_cast hp
        calc min d (min f (1 - f)) ≤ 1 - f := le_trans (min_le_right _ _) (min_le_right _ _)
          _ ≤ |(p : ℝ) - ((H + 1 : ℕ) : ℝ) * α| := by
            rw [abs_of_nonneg (by linarith)]; linarith

/-- The number of ones in `[i, i + m)` is a difference of floors. -/
theorem sum_mechZ (α θ : ℝ) (i m : ℕ) :
    ∑ t ∈ Finset.range m, mechZ α θ (i + t) = ⌊θ + ((i + m : ℕ) : ℝ) * α⌋ - ⌊θ + (i : ℝ) * α⌋ := by
  have : ∀ t : ℕ, mechZ α θ (i + t) = ⌊θ + ((i + (t + 1) : ℕ) : ℝ) * α⌋ - ⌊θ + ((i + t : ℕ) : ℝ) * α⌋ := by
    intro t; unfold mechZ; congr 2; push_cast; ring
  simp_rw [this]
  rw [Finset.sum_range_sub (fun t => ⌊θ + ((i + t : ℕ) : ℝ) * α⌋) m]
  simp

/-- Periodicity on `[i, i + n)` shifts the word by multiples of `q`. -/
theorem mech_shift (α θ : ℝ) (i q n : ℕ) (hper : ∀ s, s < n → mech α θ (i + s) = mech α θ (i + q + s)) :
    ∀ m t, m * q + t < n → mech α θ (i + (m * q + t)) = mech α θ (i + t) := by
  intro m
  induction m with
  | zero => intro t _; simp
  | succ m ih =>
    intro t ht
    have hmq : (m + 1) * q = m * q + q := Nat.succ_mul m q
    have h1 : m * q + t < n := by omega
    rw [show i + ((m + 1) * q + t) = i + q + (m * q + t) by omega, ← hper (m * q + t) h1, ih t h1]

/-- With period `q` on `[i, i + n)`, the ones in `[i, i + kq)` are `k` times the ones in `[i, i + q)`, for `kq ≤ n`. -/
theorem sum_periodic (α θ : ℝ) (h0 : 0 ≤ α) (h1 : α < 1) (i q n : ℕ)
    (hper : ∀ s, s < n → mech α θ (i + s) = mech α θ (i + q + s)) :
    ∀ k, k * q ≤ n →
      ∑ t ∈ Finset.range (k * q), mechZ α θ (i + t) = k * ∑ t ∈ Finset.range q, mechZ α θ (i + t) := by
  intro k
  induction k with
  | zero => intro _; simp
  | succ k ih =>
    intro hk
    have hkq : (k + 1) * q = k * q + q := Nat.succ_mul k q
    have hk' : k * q ≤ n := by omega
    rw [hkq, Finset.sum_range_add, ih hk']
    have : ∑ t ∈ Finset.range q, mechZ α θ (i + (k * q + t)) = ∑ t ∈ Finset.range q, mechZ α θ (i + t) := by
      apply Finset.sum_congr rfl
      intro t ht
      rw [Finset.mem_range] at ht
      rw [mechZ_eq_ite α θ h0 h1, mechZ_eq_ite α θ h0 h1, mech_shift α θ i q n hper k t (by omega)]
    rw [this]; push_cast; ring

/-- **No long block of a bounded period.** For `n` beyond a threshold depending on `H`, no block of length `n`
repeats at a gap `q ≤ H`. -/
theorem no_small_period (α θ : ℝ) (hα : Irrational α) (h0 : 0 ≤ α) (h1 : α < 1) (H : ℕ) :
    ∃ n0 : ℕ, ∀ n, n0 ≤ n → ∀ i q, 1 ≤ q → q ≤ H →
      (∀ s, s < n → mech α θ (i + s) = mech α θ (i + q + s)) → False := by
  obtain ⟨d, hd, hdq⟩ := exists_gap α hα H
  refine ⟨⌈(H : ℝ) * (1 + 1 / d)⌉₊ + 1, fun n hn i q hq1 hqH hper => ?_⟩
  have hq0 : 0 < q := hq1
  obtain ⟨k, r, hr, hn_eq⟩ : ∃ k r : ℕ, r < q ∧ n = q * k + r :=
    ⟨n / q, n % q, Nat.mod_lt n hq0, (Nat.div_add_mod n q).symm⟩
  have hkq : k * q ≤ n := by rw [Nat.mul_comm]; omega
  have hsum := sum_periodic α θ h0 h1 i q n hper k hkq
  rw [sum_mechZ, sum_mechZ] at hsum
  set p : ℤ := ⌊θ + ((i + q : ℕ) : ℝ) * α⌋ - ⌊θ + (i : ℝ) * α⌋ with hp
  have hb1 := Int.floor_le (θ + ((i + k * q : ℕ) : ℝ) * α)
  have hb2 := Int.lt_floor_add_one (θ + ((i + k * q : ℕ) : ℝ) * α)
  have hb3 := Int.floor_le (θ + (i : ℝ) * α)
  have hb4 := Int.lt_floor_add_one (θ + (i : ℝ) * α)
  have hcast : ((⌊θ + ((i + k * q : ℕ) : ℝ) * α⌋ - ⌊θ + (i : ℝ) * α⌋ : ℤ) : ℝ) = (k : ℝ) * (p : ℝ) := by
    rw [hsum]; push_cast; ring
  have hdist : |(k : ℝ) * ((p : ℝ) - (q : ℝ) * α)| < 1 := by
    rw [abs_lt]
    push_cast at hb1 hb2 hb3 hb4 hcast
    constructor <;> nlinarith
  have hdp : d ≤ |(p : ℝ) - (q : ℝ) * α| := hdq q hq1 hqH p
  have hk0 : (0 : ℝ) ≤ k := by positivity
  have hkd : (k : ℝ) * d < 1 := by
    calc (k : ℝ) * d ≤ (k : ℝ) * |(p : ℝ) - (q : ℝ) * α| := by gcongr
      _ = |(k : ℝ) * ((p : ℝ) - (q : ℝ) * α)| := by rw [abs_mul, abs_of_nonneg hk0]
      _ < 1 := hdist
  -- k is large: n < q (k + 1) ≤ H (k + 1) and n > H (1 + 1/d)
  have hnlt : n < q * (k + 1) := by
    have : q * (k + 1) = q * k + q := by ring
    omega
  have hnlt' : (n : ℝ) < (q : ℝ) * ((k : ℝ) + 1) := by exact_mod_cast hnlt
  have hceil : (H : ℝ) * (1 + 1 / d) ≤ (⌈(H : ℝ) * (1 + 1 / d)⌉₊ : ℝ) := Nat.le_ceil _
  have hn' : (H : ℝ) * (1 + 1 / d) < n := by
    have : ((⌈(H : ℝ) * (1 + 1 / d)⌉₊ + 1 : ℕ) : ℝ) ≤ n := by exact_mod_cast hn
    push_cast at this; linarith
  have hqH' : (q : ℝ) ≤ H := by exact_mod_cast hqH
  have hHpos : (0 : ℝ) < H := by exact_mod_cast (lt_of_lt_of_le hq0 hqH)
  have h2 : (H : ℝ) * (1 + 1 / d) < (H : ℝ) * ((k : ℝ) + 1) := by nlinarith
  have h3 : 1 + 1 / d < (k : ℝ) + 1 := lt_of_mul_lt_mul_left h2 hHpos.le
  have h4 : 1 / d < (k : ℝ) := by linarith
  have h5 : 1 < (k : ℝ) * d := by rw [div_lt_iff₀ hd] at h4; linarith
  linarith

/-- **Near-squares at unbounded scales with slack 1, for every intercept** (GPT, GC1694; the pigeonhole of
Bugeaud–Kim). -/
theorem sturmian_pairs (α θ : ℝ) (hα : Irrational α) (h0 : 0 ≤ α) (h1 : α < 1) (N : ℕ) :
    ∃ i j, i < j ∧ N ≤ j - i ∧ ∀ s, s + 1 < j → mech α θ (i + s) = mech α θ (j + s) := by
  obtain ⟨n0, hn0⟩ := no_small_period α θ hα h0 h1 N
  obtain ⟨i, j, hij, hjn, hblk⟩ := exists_block_collision α θ (max n0 1)
  refine ⟨i, j, hij, ?_, fun s hs => hblk s (by omega)⟩
  by_contra hlt
  push Not at hlt
  exact hn0 (max n0 1) (le_max_left _ _) i (j - i) (by omega) (by omega)
    (fun s hs => by rw [show i + (j - i) + s = j + s by omega]; exact hblk s hs)

/-- Shifting the intercept by `Aα` shifts the word by `A`. -/
theorem mech_shift_intercept (α θ : ℝ) (A s : ℕ) : mech α (θ + (A : ℝ) * α) s = mech α θ (s + A) := by
  have e1 : θ + (A : ℝ) * α + ((s : ℝ) + 1) * α = θ + (((s + A : ℕ) : ℝ) + 1) * α := by push_cast; ring
  have e2 : θ + (A : ℝ) * α + (s : ℝ) * α = θ + ((s + A : ℕ) : ℝ) * α := by push_cast; ring
  unfold mech mechZ
  rw [e1, e2]

/-! ## Every Sturmian word is excluded beside the clock -/

/-- **Theorem E, every intercept.** A configuration with a leftmost black cell `L ≥ 1` cells left of column `0`,
whose column `0` reads the clock from time `T0`, cannot have the mechanical word of irrational slope `α ∈ (0, 1)` and
any intercept `θ` as its visible bits. -/
theorem sturmian_excluded (α θ : ℝ) (hα : Irrational α) (h0 : 0 ≤ α) (h1 : α < 1) (x0 : ℤ → Bool) (L : ℕ)
    (hL : 1 ≤ L) (hc : x0 (-(L : ℤ)) = true) (hl : ∀ j < -(L : ℤ), x0 j = false) (T0 : ℕ)
    (hclock : ∀ t, T0 ≤ t → evol x0 t 0 = decide (t % 2 = 1))
    (hvis : ∀ i, evol x0 (2 * i) 1 = mech α θ i) : False := by
  refine corollary_F x0 L hL hc hl T0 hclock (T0 + 1) (fun N => ?_)
  obtain ⟨i, j, hij, hN, hblk⟩ := sturmian_pairs α (θ + (T0 : ℝ) * α) hα h0 h1 N
  refine ⟨T0 + i, T0 + j, by omega, by omega, by omega, fun s hs => ?_⟩
  rw [hvis, hvis, show T0 + i + s = (i + s) + T0 by ring, show T0 + j + s = (j + s) + T0 by ring,
    ← mech_shift_intercept α θ T0 (i + s), ← mech_shift_intercept α θ T0 (j + s)]
  exact hblk s (by omega)

/-- The clock from time `0`: then `L ≥ 1` is automatic, since the clock is white at time `0`. -/
theorem sturmian_excluded_clock0 (α θ : ℝ) (hα : Irrational α) (h0 : 0 ≤ α) (h1 : α < 1) (x0 : ℤ → Bool) (L : ℕ)
    (hc : x0 (-(L : ℤ)) = true) (hl : ∀ j < -(L : ℤ), x0 j = false)
    (hclock : ∀ t, evol x0 t 0 = decide (t % 2 = 1)) (hvis : ∀ i, evol x0 (2 * i) 1 = mech α θ i) : False := by
  have hL : 1 ≤ L := by
    by_contra h0'
    have hL0 : L = 0 := by omega
    subst hL0
    have h := hclock 0
    rw [show evol x0 0 0 = x0 0 from rfl] at h
    have hc0 : x0 0 = true := by simpa using hc
    rw [hc0] at h
    exact absurd h (by decide)
  exact sturmian_excluded α θ hα h0 h1 x0 L hL hc hl 0 (fun t _ => hclock t) hvis

/-- The record's form of the word: the bit is `1` iff `fract (θ + iα) ∈ [1 - α, 1)`. -/
theorem sturmian_excluded_fract (α θ : ℝ) (hα : Irrational α) (h0 : 0 ≤ α) (h1 : α < 1) (x0 : ℤ → Bool) (L : ℕ)
    (hL : 1 ≤ L) (hc : x0 (-(L : ℤ)) = true) (hl : ∀ j < -(L : ℤ), x0 j = false) (T0 : ℕ)
    (hclock : ∀ t, T0 ≤ t → evol x0 t 0 = decide (t % 2 = 1))
    (hvis : ∀ i, evol x0 (2 * i) 1 = decide (1 - α ≤ Int.fract (θ + (i : ℝ) * α))) : False :=
  sturmian_excluded α θ hα h0 h1 x0 L hL hc hl T0 hclock (fun i => by rw [hvis, mech_eq_fract α θ h0 h1])

/-- **Every sliding block code of every Sturmian word is excluded** beside the clock. -/
theorem sturmian_block_excluded (α θ : ℝ) (hα : Irrational α) (h0 : 0 ≤ α) (h1 : α < 1)
    (f : List Bool → Bool) (r : ℕ) (x0 : ℤ → Bool) (L : ℕ)
    (hL : 1 ≤ L) (hc : x0 (-(L : ℤ)) = true) (hl : ∀ j < -(L : ℤ), x0 j = false) (T0 : ℕ)
    (hclock : ∀ t, T0 ≤ t → evol x0 t 0 = decide (t % 2 = 1))
    (hvis : ∀ i, evol x0 (2 * i) 1 = image f r (mech α θ) i) : False := by
  refine corollary_F x0 L hL hc hl T0 hclock (T0 + 1 + r) (fun N => ?_)
  obtain ⟨i, j, hij, hN, hblk⟩ := sturmian_pairs α (θ + (T0 : ℝ) * α) hα h0 h1 N
  refine ⟨T0 + i, T0 + j, by omega, by omega, by omega, fun s hs => ?_⟩
  rw [hvis, hvis]
  have hc' : ∀ s, s + (T0 + 1) < T0 + j → mech α θ (T0 + i + s) = mech α θ (T0 + j + s) := fun s hs => by
    rw [show T0 + i + s = (i + s) + T0 by ring, show T0 + j + s = (j + s) + T0 by ring,
      ← mech_shift_intercept α θ T0 (i + s), ← mech_shift_intercept α θ T0 (j + s)]
    exact hblk s (by omega)
  exact image_near_square f r (mech α θ) (T0 + 1) (T0 + i) (T0 + j) hc' s (by omega)

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorem, as Lean prints it. `evol x0 t p` is the kit's evolution; the hypotheses are an irrational slope in `[0, 1)`, a leftmost black cell at `-L` with `L ≥ 1`, the clock on column 0 from time `T0`, and the visible bits equal to the mechanical word `mech α θ`:

```wl
opens = {"Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.sturmian_excluded"];
thm["TypeForm", "Open" -> opens]
```

The clock from time 0 (where `L ≥ 1` is automatic), the record's fractional-part form of the word, and every sliding block code:

```wl
{rule30Submission["Rule30Submission.sturmian_excluded_clock0"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.sturmian_excluded_fract"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.sturmian_block_excluded"]["TypeForm", "Open" -> opens]}
```

The three word lemmas, the pigeonhole, the bounded-period exclusion and the near-squares they give, and the word itself:

```wl
{rule30Submission["Rule30Submission.exists_block_collision"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.no_small_period"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.sturmian_pairs"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.mech"]["TypeForm", "Open" -> opens]}
```

Corollary F, the theorem the words feed:

```wl
rule30Submission["Rule30Submission.corollary_F"]["TypeForm", "Open" -> opens]
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

- Nothing about the single seed directly: its center column is not known to be eventually a clock.
- The slope is taken in `[0, 1)` and irrational, and the word is the lower mechanical word; the upper mechanical words (the other half-open convention) are the complements of lower ones of slope `1 - α`, hence covered by the block-code theorem with the window-1 code `NOT`, but that reduction is not stated in the module.
- The module proves only `p(n) ≤ n + 1`, not the equality; the equality is shown by computation above.
- Rational slopes give periodic words, which Jen's theorem excludes separately; they are outside this module.

## Provenance

Theorem E is RULE30-PRIZE.md section 8.57 and PROOFS.md entry 14 of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT: proved by Local (Claude) on 2026-10-05 by a Diophantine argument through the convergents of `α`. Corollary F (PROOFS 11) is Local's, formalized by Cloud (Claude) on 2026-10-23. The combinatorial route from Corollary F to every intercept is GPT's (ledger entry GC1694, 2026-10-23), found after Cloud had measured near-squares only at convergent periods and concluded, wrongly, that no such route existed; the pigeonhole is Bugeaud and Kim's Lemma 2.2. Cloud formalized the route on the kit's definitions the same day; GPT second-read the formal statements. The companion submissions file the white end, the excluded words, the diagonal lemmas, Theorem A⁗, Corollary F, the rule 210 barrier and the characteristic case.

## References

[1] E. Jen, *Global properties of cellular automata*, Journal of Statistical Physics 43 (1986) 219–242.

[2] Y. Bugeaud and D. H. Kim, *A new complexity function, repetitions in Sturmian words, and irrationality exponents of Sturmian numbers*, Transactions of the American Mathematical Society 371 (2019) 3281–3308.

[3] M. Lothaire, *Algebraic Combinatorics on Words*, Cambridge University Press, 2002, Chapter 2 (Sturmian words).

[4] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[5] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[6] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): PROOFS.md entries 11 and 14, CHAT-LEDGER.md GC1694, 2026.
