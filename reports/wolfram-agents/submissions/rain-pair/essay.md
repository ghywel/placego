---
Template: ComputationalEssay
Name: Staircases near the single cell's right edge end; the rain rows keep a two-step edge patch for ever
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-27
Description: A partial structural result on Rule 30, proved in Lean against the kit: every alternating stretch (staircase) near the single black cell's right edge ends, within 2^(W+1) rows when its front is W cells from the edge; and the odd edge codes (bit 0 black) with T(T(c)) = c are exactly -1/3 and 1/3, so the rain rows (01)^n keep a moving 2n-cell patch at their right edge that alternates between the two prefixes for ever.
Abstract: In rule 30 grown from one black cell, call a maximal alternating stretch of length at least $3$ a staircase. Its interior keeps its colors, and its front is eaten one cell per row (`front_step`), so a living staircase keeps its distance $W$ from the advancing right edge. We prove that every staircase with $W \ge 2$ ends: it does not survive to any multiple of a period $H$ of the right diagonal $W+1$ (`staircase_ends`), so it dies within $2^{W+1}$ rows by the kit's `R_periodic` (`staircase_ends_pow`). The reason is that at such times the cells at distances $1,\dots,W+1$ behind the edge are white. The bound concerns the single cell: other rows keep a two-step patch at their edge for ever. Bit $k$ of a finite row's edge code is the cell at distance $k$ from its rightmost black cell, and the code evolves by the 2-adic edge map $T$ of Coven, Pivato and Yassawi (`edge_evol`). An odd edge code $c$ (bit $0$ black) satisfies $T(T(c)) = c$ exactly when $c$ is $-1/3 = 1010\ldots$ or $1/3 = 11010\ldots$ (`period_two_iff`), and none is fixed (`no_fixed_point`). Every row agreeing with $-1/3$ on $m$ edge cells keeps them in that rhythm for ever (`agree_rain_eternal`), so the rain row $(01)^n$ keeps a moving $2n$-cell patch that alternates between the two prefixes for ever (`rain_row_eternal`). Unlike R30-20261026-0ef9c8 (gated, finitely supported, period $32$), this covers every odd 2-adic code at period $2$, with no gate hypothesis. Not claimed: the center column, staircases of other seeds, or longer periods of $T$.
Keywords: [rule 30, Rule 30 Prize, right edge, edge code, 2-adic, periodic points, rain, staircase, Lean 4, LeanLink]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

## The question

Rule 30's picture is full of *staircases*: stretches of a row that alternate black, white, black, white, and stay put from row to row while their left end is eaten away. Near the right edge of the single black cell's picture they are everywhere. Do they all end? This essay proves that they do, with an explicit bound, and shows that the bound is about the single cell: the rain rows `0 1 0 1 … 0 1` keep a moving patch at their edge in a two-step rhythm for ever. The only odd edge codes with a two-step rhythm are a pair of 2-adic numbers, `-1/3` and `1/3`.

## Part 1: staircases near the single cell's edge end

A staircase's interior cells keep their colors, because beside an alternating pair the black OR always fires and each cell becomes the complement of its left neighbour. Its left end, the front, is eaten one cell per row. The right edge also advances one cell per row, so a living staircase keeps its front at a fixed distance `W` from the edge. The proof's key fact: at every multiple of `2^(W + 1)`, the cells at distances `1 .. W + 1` behind the single cell's edge are all white, so no staircase with its front there can be alive. In the computed picture:

```wl
ca = CellularAutomaton[30, {{1}, 0}, 512];
edgeWhite[t_, m_] := With[{row = ca[[t + 1]], e = 513 + t}, AllTrue[Range[1, m], row[[e - #]] == 0 &]];
And @@ Flatten[Table[edgeWhite[2^(W + 1) n, W + 1], {W, 2, 7}, {n, 1, Floor[512/2^(W + 1)]}]]
```

## Part 2: the rain rows keep theirs

One step of rule 30 on a finite row, and the cells just behind the rightmost black cell:

```wl
step[w_] := With[{p = Join[{0, 0}, w, {0, 0}]}, Table[BitXor[p[[i - 1]], BitOr[p[[i]], p[[i + 1]]]], {i, 2, Length[p] - 1}]];
edgeCells[w_, m_] := With[{r = Reverse[w]}, Take[Drop[r, First[FirstPosition[r, 1]] - 1], UpTo[m]]];
rain[n_] := Flatten[ConstantArray[{0, 1}, n]];
edgeCells[#, 10] & /@ NestList[step, rain[5], 5]
```

The ten cells behind the edge of `(0 1)^5` read `1 0 1 0 1 0 1 0 1 0` at even times and `1 1 0 1 0 1 0 1 0 1` at odd times: `-1/3` and `1/3`, one after the other. They keep doing so for as long as we look:

```wl
rows = NestList[step, rain[5], 400];
Union[edgeCells[#, 10] & /@ rows[[1 ;; ;; 2]]] === {{1, 0, 1, 0, 1, 0, 1, 0, 1, 0}} && Union[edgeCells[#, 10] & /@ rows[[2 ;; ;; 2]]] === {{1, 1, 0, 1, 0, 1, 0, 1, 0, 1}}
```

## The theorems

**Part 1.** In the single cell's picture (`cell t p`):
- **Interior and front** (`interior_kept`, `front_step`). An interior cell of an alternating stretch keeps its color. If `f` is the front of a maximal alternating stretch of length at least `3` at time `t`, the cells `f` and `f + 1` agree at time `t + 1`, so the stretch continues from `f + 1` or ends.
- **Every staircase ends** (`staircase_ends`, `staircase_ends_pow`). Say a staircase *lives through* `t` from `t₀` with front `a` if at every time `t'` from `t₀` to `t`, the three cells from `a + (t' - t₀)` alternate. If `W = t₀ - a ≥ 2` and the kit's right diagonal `W + 1` has period `H` (`Rule30RightPeriods.Per (W + 1) H`), the staircase does not live through any multiple `H n ≥ t₀`. With `H = 2^(W + 1)` (the kit's `R_periodic`) it dies within `2^(W + 1)` rows.

**Part 2.** Bit `k` of the edge code of a finite row with rightmost black cell `e` is the cell at distance `k` from `e`. The code evolves by the edge map `T`: `T c 0 = c 0`, `T c 1 = c 1 xor c 0`, `T c (k + 2) = c (k + 2) xor (c (k + 1) || c k)` (`edge_evol`).
- **The rain pair** (`period_two_iff`). An odd edge code `c` (bit `0` black) satisfies `T (T c) = c` exactly when `c` is `rainA = 1 0 1 0 …` (`-1/3`) or `rainB = 1 1 0 1 0 …` (`1/3`). `T` swaps the two (`T_rainA`, `T_rainB`), and no such code is fixed (`no_fixed_point`).
- **Rows that keep the rain** (`agree_rain_eternal`). A finite row whose `m` edge cells agree with `rainA` has, at every time `t`, its `m` edge cells equal to `rainA` at even `t` and `rainB` at odd `t`.
- **The rain row** (`rain_row_eternal`). For every `n ≥ 1`, the row `(0 1)^n` has its rightmost black cell at `t` at time `t`, and its `2 n` edge cells follow the rain pair for ever: the first `2 n` bits of `rainA` at even times and of `rainB` at odd times. Since `rainB` begins `1 1`, the patch is not a spatially alternating word at odd times; for `n = 1` the two phases are `1 0` and `1 1`.

## The idea of the proof

**Part 1.** At a multiple `H n` of a period of diagonal `W + 1`, the kit's monotonicity (`per_mono_all`) makes every diagonal `0 .. W + 1` periodic with period `H`, so each is back at its time-0 value (`Per.at_mul`): white for `1 ≤ j` (`R_init`). The front of a living staircase sits at distance `W`, and the next cell at distance `W - 1 ≥ 1`. Both are white, so they do not alternate.

**Part 2.**

1. **Bit 1 always flips.** With bit `0` black, `T c 1 = c 1 xor 1`. So no code is fixed, and the two codes `c` and `d = T c` of a 2-cycle differ at bit `1`.
2. **Equal inputs.** Bit `k + 2` of `d` is `c (k + 2) xor (c (k + 1) || c k)`, and bit `k + 2` of `c = T d` is `d (k + 2) xor (d (k + 1) || d k)`. Adding the two, the inputs are equal: `c (k + 1) || c k = d (k + 1) || d k`.
3. **Alternation.** If `c` and `d` differ at bits `k` and `k + 1`, the pairs `(c k, c (k + 1))` and `(d k, d (k + 1))` are complements with equal ORs, which forces each pair to alternate. Then the common input is black, and `c` and `d` differ again at bit `k + 2`. From bits `1` and `2` (which differ, by step 1 and step 2 at `k = 0`), induction makes `c` alternate from bit `1` on. That leaves `-1/3` and `1/3`.
4. **For ever.** Bit `k` of `T c` reads only bits `k - 2 .. k`, so codes that agree below `m` still agree below `m` after any number of steps. A row agreeing with `rainA` on `m` cells follows the rain pair on those cells.

## The formal proof

The module, built against the kit at the verifier's commit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["import Rule30PrizeKit

/-!
# Staircases at the right edge: the single cell's all end, and the rain rows' never do

## Part 1. Every staircase near the single cell's right edge ends

In the picture of rule 30 grown from one black cell (`cell t p`), a *staircase* is a maximal
alternating stretch of a row, `… x x̄ x x̄ …`, of length at least `3`. Its interior cells keep their
colors from row to row (`interior_kept`): beside an alternating pair the black OR always fires, so
the cell becomes the complement of its left neighbour, which is its own color. Its left end, the
*front*, is eaten one cell per row: if `f` is the front at time `t` (the cell left of it has the
same color, and `f, f+1, f+2` alternate), then at time `t + 1` the cells `f` and `f + 1` have the
same color (`front_step`), so the stretch continues from `f + 1` or not at all. The right edge of
the picture advances one cell per row as well, so a living staircase keeps its front at a fixed
distance `W` from the edge.

**The headline (`staircase_ends`).** Say the staircase *lives through* time `t` from time `t₀`
with front `a` (`Lives`) if at every time `t'` between `t₀` and `t`, the three cells from
`a + (t' - t₀)` alternate. If its front is at distance `W = t₀ - a ≥ 2` from the edge, and the
right diagonal `W + 1` has period `H` (`Rule30RightPeriods.Per (W + 1) H`, as in the kit), then the
staircase does not live through any time `H n ≥ t₀`. At such a time the diagonals `0 .. W + 1`
are back at their time-0 values, so the cells at distances `1 .. W + 1` from the edge are white,
and the front pair is white-white.

With the kit's `R_periodic`, `H = 2 ^ (W + 1)` always works (`staircase_ends_pow`): every staircase
whose front is `W ≥ 2` cells from the edge dies within `2 ^ (W + 1)` rows. The least common period
of the diagonals `0 .. W + 1` gives the sharpest bound. Nothing here concerns staircases deep in
the picture's chaotic core, rows of other seeds, or the center column.

## Part 2. The rain pair: the only two-step rhythms of a right edge

Read a finite nonzero row of rule 30 from its rightmost black cell `e`: bit `k` of its edge code is
the cell at distance `k` from `e` (`code x e k = x (e - k)`). The right edge advances one cell per
step and the code evolves by the edge map `T` (`edge_evol`), the 2-adic right-edge map of Coven,
Pivato and Yassawi:

  `T c 0 = c 0`, `T c 1 = c 1 ⊕ c 0`, `T c (k + 2) = c (k + 2) ⊕ (c (k + 1) ∨ c k)`.

**The classification (`period_two_iff`).** An odd edge code (bit `0` black) satisfies
`T (T c) = c` exactly when it is one of two codes: `rainA = 1 0 1 0 1 0 …` (the 2-adic number
`-1/3`) or `rainB = 1 1 0 1 0 1 …` (`1/3`), and `T` swaps them (`T_rainA`, `T_rainB`). No such code
is fixed by `T` (`no_fixed_point`). The proof compares the two steps bit by bit: the two codes of a
2-cycle differ at bit `1`, and then the equal inputs `c (k+1) ∨ c k = d (k+1) ∨ d k` of the next bit
force each adjacent pair to alternate and the next bits to differ.

**Rain rows keep the rhythm for ever (`rain_row_eternal`).** The row `(0 1)^n`, `n` pairs ending in
a black cell, agrees with `rainA` on its `2 n` cells read from the edge. By triangularity of `T`, at
every time `t` the `2 n` cells read from its right edge are the first `2 n` bits of `rainA` at even
`t` and of `rainB` at odd `t`: a moving patch that keeps this two-step rhythm for ever (`rainB`
begins `1 1`, so the patch is not a spatially alternating word at odd times). Every finite row
whose edge cells agree with `rainA` on `m` bits does the same on those `m` bits
(`agree_rain_eternal`).

Nothing here concerns the center column.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30Jen (rule)
open Ruliology.CellularAutomata.Rule30Realization (evol)

/-! ### The edge map (as in the companion submission on the frozen ruler) -/

def T (c : Nat → Bool) : Nat → Bool
  | 0 => c 0
  | 1 => xor (c 1) (c 0)
  | k + 2 => xor (c (k + 2)) (c (k + 1) || c k)

def AgreeBelow (k : Nat) (c d : Nat → Bool) : Prop := ∀ i, i < k → c i = d i

theorem T_agree {k : Nat} {c d : Nat → Bool} (h : AgreeBelow k c d) :
    AgreeBelow k (T c) (T d) := by
  intro i hi
  match i, hi with
  | 0, hi => simp [T, h 0 hi]
  | 1, hi => simp [T, h 1 hi, h 0 (by omega)]
  | j + 2, hi => simp [T, h (j + 2) hi, h (j + 1) (by omega), h j (by omega)]

theorem iter_agree {k : Nat} {c d : Nat → Bool} (h : AgreeBelow k c d) :
    ∀ t, AgreeBelow k (T^[t] c) (T^[t] d)
  | 0 => h
  | t + 1 => by
    rw [Function.iterate_succ_apply', Function.iterate_succ_apply']
    exact T_agree (iter_agree h t)

/-- The edge code of a row whose rightmost black cell is `e`. -/
def code (x : Int → Bool) (e : Int) : Nat → Bool := fun k => x (e - k)

theorem edge_evol (x : Int → Bool) (e : Int) (he : x e = true)
    (hr : ∀ p, e < p → x p = false) :
    ∀ t : Nat, evol x t (e + t) = true ∧ (∀ p, e + t < p → evol x t p = false) ∧
      code (evol x t) (e + t) = T^[t] (code x e)
  | 0 => by
    refine ⟨by simpa [evol] using he, fun p hp => by simpa [evol] using hr p (by omega), ?_⟩
    funext k; simp [code, evol]
  | t + 1 => by
    obtain ⟨h1, h2, h3⟩ := edge_evol x e he hr t
    have hz : ∀ p, e + (t : Int) < p → evol x t p = false := h2
    refine ⟨?_, ?_, ?_⟩
    · show rule (evol x t (e + (t + 1 : Nat) - 1)) (evol x t (e + (t + 1 : Nat)))
        (evol x t (e + (t + 1 : Nat) + 1)) = true
      have a : e + ((t + 1 : Nat) : Int) - 1 = e + t := by push_cast; ring
      have b : e + ((t + 1 : Nat) : Int) = e + t + 1 := by push_cast; ring
      have c : e + ((t + 1 : Nat) : Int) + 1 = e + t + 2 := by push_cast; ring
      rw [a, c, b, h1, hz (e + t + 1) (by omega), hz (e + t + 2) (by omega)]
      rfl
    · intro p hp
      show rule (evol x t (p - 1)) (evol x t p) (evol x t (p + 1)) = false
      push_cast at hp
      rw [hz (p - 1) (by omega), hz p (by omega), hz (p + 1) (by omega)]
      rfl
    · rw [Function.iterate_succ_apply', ← h3]
      funext k
      have hm : e + ((t + 1 : Nat) : Int) = (e + t) + 1 := by push_cast; ring
      show rule (evol x t (e + ((t + 1 : Nat) : Int) - k - 1)) (evol x t (e + ((t + 1 : Nat) : Int) - k))
        (evol x t (e + ((t + 1 : Nat) : Int) - k + 1)) = T (code (evol x t) (e + t)) k
      rw [hm]
      match k with
      | 0 =>
        have a1 : e + (t : Int) + 1 - ((0 : Nat) : Int) - 1 = e + t := by push_cast; ring
        have a2 : e + (t : Int) + 1 - ((0 : Nat) : Int) + 1 = e + t + 2 := by push_cast; ring
        have a3 : e + (t : Int) + 1 - ((0 : Nat) : Int) = e + t + 1 := by push_cast; ring
        rw [a1, a2, a3, hz (e + t + 1) (by omega), hz (e + t + 2) (by omega)]
        simp [T, code, rule]
      | 1 =>
        have a1 : e + (t : Int) + 1 - ((1 : Nat) : Int) - 1 = e + t - ((1 : Nat) : Int) := by
          push_cast; ring
        have a2 : e + (t : Int) + 1 - ((1 : Nat) : Int) + 1 = e + t + 1 := by push_cast; ring
        have a3 : e + (t : Int) + 1 - ((1 : Nat) : Int) = e + t - ((0 : Nat) : Int) := by
          push_cast; ring
        rw [a1, a2, a3, hz (e + t + 1) (by omega)]
        simp [T, code, rule]
      | j + 2 =>
        have a1 : e + (t : Int) + 1 - ((j + 2 : Nat) : Int) - 1 = e + t - ((j + 2 : Nat) : Int) := by
          push_cast; ring
        have a2 : e + (t : Int) + 1 - ((j + 2 : Nat) : Int) + 1 = e + t - ((j : Nat) : Int) := by
          push_cast; ring
        have a3 : e + (t : Int) + 1 - ((j + 2 : Nat) : Int) = e + t - ((j + 1 : Nat) : Int) := by
          push_cast; ring
        rw [a1, a2, a3]
        simp [T, code, rule]

/-! ### The rain pair -/

/-- `1 0 1 0 …`: the 2-adic number `-1/3`, an edge emitting a lone white cell at every other step. -/
def rainA : Nat → Bool := fun k => k % 2 == 0

/-- `1 1 0 1 0 …`: the 2-adic number `1/3`. -/
def rainB : Nat → Bool := fun k => k == 0 || k % 2 == 1

theorem T_rainA : T rainA = rainB := by
  funext k
  match k with
  | 0 => rfl
  | 1 => rfl
  | j + 2 =>
    simp only [T, rainA, rainB]
    rcases Nat.mod_two_eq_zero_or_one j with h | h
    · have h1 : (j + 1) % 2 = 1 := by omega
      have h2 : (j + 2) % 2 = 0 := by omega
      simp [h, h1, h2]
    · have h1 : (j + 1) % 2 = 0 := by omega
      have h2 : (j + 2) % 2 = 1 := by omega
      simp [h, h1, h2]

theorem T_rainB : T rainB = rainA := by
  funext k
  match k with
  | 0 => rfl
  | 1 => rfl
  | 2 => rfl
  | j + 3 =>
    show xor (rainB (j + 3)) (rainB (j + 2) || rainB (j + 1)) = rainA (j + 3)
    simp only [rainA, rainB]
    rcases Nat.mod_two_eq_zero_or_one j with h | h
    · have h1 : (j + 1) % 2 = 1 := by omega
      have h2 : (j + 2) % 2 = 0 := by omega
      have h3 : (j + 3) % 2 = 1 := by omega
      simp [h1, h2, h3]
    · have h1 : (j + 1) % 2 = 0 := by omega
      have h2 : (j + 2) % 2 = 1 := by omega
      have h3 : (j + 3) % 2 = 0 := by omega
      simp [h1, h2, h3]

theorem rainA_ne_rainB : rainA ≠ rainB := by
  intro h
  have := congrFun h 1
  simp [rainA, rainB] at this

/-- No edge code with bit `0` black is fixed by `T`: bit `1` always flips. -/
theorem no_fixed_point (c : Nat → Bool) (h0 : c 0 = true) : T c ≠ c := by
  intro h
  have := congrFun h 1
  simp [T, h0] at this

/-- The two codes of a 2-cycle differ at every bit from `1` on, and each alternates from bit `1`. -/
theorem cycle_bits (c : Nat → Bool) (h0 : c 0 = true) (h2 : T (T c) = c) :
    ∀ k, 1 ≤ k → T c k ≠ c k ∧ T c (k + 1) ≠ c (k + 1) ∧ c k ≠ c (k + 1) := by
  set d := T c with hd
  have hc : ∀ k, T d k = c k := fun k => congrFun h2 k
  have dk0 : d 0 = true := by simp [hd, T, h0]
  -- the step relations
  have rel_d : ∀ k, d (k + 2) = xor (c (k + 2)) (c (k + 1) || c k) := fun k => rfl
  have rel_c : ∀ k, c (k + 2) = xor (d (k + 2)) (d (k + 1) || d k) := fun k => (hc (k + 2)).symm
  have or_eq : ∀ k, (c (k + 1) || c k) = (d (k + 1) || d k) := by
    intro k
    have a := rel_d k; have b := rel_c k
    revert a b
    cases c (k + 2) <;> cases d (k + 2) <;> cases (c (k + 1) || c k) <;>
      cases (d (k + 1) || d k) <;> simp
  have d1 : d 1 ≠ c 1 := by
    show xor (c 1) (c 0) ≠ c 1
    rw [h0]; cases c 1 <;> simp
  have d2 : d 2 ≠ c 2 := by
    have := rel_d 0
    rw [h0] at this
    simp at this
    rw [this]; cases c 2 <;> simp
  -- induction on k ≥ 1
  have step : ∀ k, d (k + 1) ≠ c (k + 1) → d (k + 2) ≠ c (k + 2) →
      c (k + 1) ≠ c (k + 2) ∧ d (k + 3) ≠ c (k + 3) := by
    intro k ha hb
    have ho := or_eq (k + 1)
    have hne : c (k + 2) ≠ c (k + 1) := by
      intro heq
      revert ha hb ho heq
      cases c (k + 1) <;> cases c (k + 2) <;> cases d (k + 1) <;> cases d (k + 2) <;> simp
    have hor : (c (k + 2) || c (k + 1)) = true := by
      revert hne; cases c (k + 1) <;> cases c (k + 2) <;> simp
    refine ⟨fun h => hne h.symm, ?_⟩
    have := rel_d (k + 1)
    rw [hor] at this
    rw [this]; cases c (k + 3) <;> simp
  have main : ∀ k, d (k + 1) ≠ c (k + 1) ∧ d (k + 2) ≠ c (k + 2) := by
    intro k
    induction k with
    | zero => exact ⟨d1, d2⟩
    | succ n ih => exact ⟨ih.2, (step n ih.1 ih.2).2⟩
  intro k hk
  obtain ⟨n, rfl⟩ : ∃ n, k = n + 1 := ⟨k - 1, by omega⟩
  exact ⟨(main n).1, (main n).2, (step n (main n).1 (main n).2).1⟩

/-- **The rain pair.** An edge code with bit `0` black is a point of period dividing `2` of the edge
map exactly when it is `rainA` (`-1/3`) or `rainB` (`1/3`). -/
theorem period_two_iff (c : Nat → Bool) (h0 : c 0 = true) :
    T (T c) = c ↔ (c = rainA ∨ c = rainB) := by
  constructor
  · intro h2
    have hb := cycle_bits c h0 h2
    -- c alternates from bit 1 on
    have alt : ∀ n, c (n + 1) = (if n % 2 = 0 then c 1 else !c 1) := by
      intro n
      induction n with
      | zero => simp
      | succ m ih =>
        have := (hb (m + 1) (by omega)).2.2
        rw [ih] at this
        split at this <;> rename_i hm
        · have : c (m + 2) = !c 1 := by revert this; cases c 1 <;> cases c (m + 2) <;> simp
          rw [show m + 1 + 1 = m + 2 by omega, this]
          simp [show (m + 1) % 2 ≠ 0 by omega]
        · have : c (m + 2) = c 1 := by revert this; cases c 1 <;> cases c (m + 2) <;> simp
          rw [show m + 1 + 1 = m + 2 by omega, this]
          simp [show (m + 1) % 2 = 0 by omega]
    cases h1 : c 1
    · left; funext k
      match k with
      | 0 => simp [rainA, h0]
      | n + 1 =>
        rw [alt n, h1]
        simp only [rainA]
        split <;> rename_i hn <;> simp <;> omega
    · right; funext k
      match k with
      | 0 => simp [rainB, h0]
      | n + 1 =>
        rw [alt n, h1]
        simp only [rainB]
        split <;> rename_i hn <;> simp <;> omega
  · rintro (rfl | rfl)
    · rw [T_rainA, T_rainB]
    · rw [T_rainB, T_rainA]

/-! ### Rows that keep the rain for ever -/

theorem iter_rainA : ∀ t, T^[t] rainA = (if t % 2 = 0 then rainA else rainB)
  | 0 => rfl
  | t + 1 => by
    rw [Function.iterate_succ_apply', iter_rainA t]
    by_cases h : t % 2 = 0
    · simp [h, T_rainA, show (t + 1) % 2 ≠ 0 by omega]
    · simp [h, T_rainB, show (t + 1) % 2 = 0 by omega]

/-- A finite row whose `m` edge cells agree with `rainA` keeps them `rainA` at even times and
`rainB` at odd times, for ever. -/
theorem agree_rain_eternal (x : Int → Bool) (e : Int) (he : x e = true)
    (hr : ∀ p, e < p → x p = false) (m : Nat) (hag : AgreeBelow m (code x e) rainA) (t : Nat) :
    AgreeBelow m (code (evol x t) (e + t)) (if t % 2 = 0 then rainA else rainB) := by
  rw [(edge_evol x e he hr t).2.2, ← iter_rainA t]
  exact iter_agree hag t

/-- The rain row `(0 1)^n`: black exactly at the cells `-2 i`, `0 ≤ i < n`. -/
def rainRow (n : Nat) (p : Int) : Bool := decide (p ≤ 0 ∧ -(2 * (n : Int)) < p ∧ p % 2 = 0)

theorem rainRow_code (n : Nat) : AgreeBelow (2 * n) (code (rainRow n) 0) rainA := by
  intro i hi
  simp only [code, rainRow, rainA]
  rcases Nat.mod_two_eq_zero_or_one i with h | h
  · simp [h]; first | omega | (intro _; omega)
  · simp [h]; first | omega | (intro _; omega)

/-- **The rain row keeps a two-step patch at its right edge for ever.** For every `n ≥ 1` and every time
`t`, the rightmost black cell of the row `(0 1)^n` after `t` steps is at `t`, and the `2 n` cells
behind it read `rainA` at even times and `rainB` at odd times. -/
theorem rain_row_eternal (n : Nat) (hn : 1 ≤ n) (t : Nat) :
    evol (rainRow n) t t = true ∧ (∀ p, (t : Int) < p → evol (rainRow n) t p = false) ∧
    AgreeBelow (2 * n) (code (evol (rainRow n) t) t) (if t % 2 = 0 then rainA else rainB) := by
  have he : rainRow n 0 = true := by simp [rainRow]; omega
  have hr : ∀ p, (0 : Int) < p → rainRow n p = false := by
    intro p hp; simp [rainRow]; omega
  have h := edge_evol (rainRow n) 0 he hr t
  simp only [zero_add] at h
  refine ⟨h.1, h.2.1, ?_⟩
  have := agree_rain_eternal (rainRow n) 0 he hr (2 * n) (rainRow_code n) t
  simpa using this

/-! ### Part 1: staircases in the single cell's picture end -/

open Ruliology.CellularAutomata.Rule30Jen (cell)
open Ruliology.CellularAutomata.Rule30Diagonals (R R_periodic)
open Ruliology.CellularAutomata.Rule30RightPeriods (Per per_mono_all R_init)

/-- Three cells from `f` at time `t` alternate. -/
def Alt3 (t : Nat) (f : Int) : Prop := cell t f ≠ cell t (f + 1) ∧ cell t (f + 1) ≠ cell t (f + 2)

/-- `f` is the front (left end) of a maximal alternating stretch of length at least `3`. -/
def Front (t : Nat) (f : Int) : Prop := cell t (f - 1) = cell t f ∧ Alt3 t f

theorem cell_succ (t : Nat) (p : Int) :
    cell (t + 1) p = rule (cell t (p - 1)) (cell t p) (cell t (p + 1)) := rfl

/-- Interior cells of an alternating stretch keep their colors. -/
theorem interior_kept (t : Nat) (p : Int) (h1 : cell t (p - 1) ≠ cell t p)
    (h2 : cell t p ≠ cell t (p + 1)) : cell (t + 1) p = cell t p := by
  rw [cell_succ]
  revert h1 h2
  cases cell t (p - 1) <;> cases cell t p <;> cases cell t (p + 1) <;> decide

/-- The front is eaten one cell per row: after one step, the old front and the next cell agree. -/
theorem front_step (t : Nat) (f : Int) (h : Front t f) :
    cell (t + 1) f = cell (t + 1) (f + 1) := by
  obtain ⟨hl, ha, hb⟩ := h
  rw [cell_succ t f, cell_succ t (f + 1)]
  have e1 : f + 1 - 1 = f := by ring
  rw [e1, hl, show f + 1 + 1 = f + 2 by ring]
  revert ha hb
  cases cell t f <;> cases cell t (f + 1) <;> cases cell t (f + 2) <;> decide

/-- The stretch lives through `t`, from `t₀` with front `a`, its front moving one cell per row. -/
def Lives (t₀ : Nat) (a : Int) (t : Nat) : Prop :=
  ∀ t', t₀ ≤ t' → t' ≤ t → Alt3 t' (a + ((t' - t₀ : Nat) : Int))

/-- A living stretch's front stays at its distance from the edge: at time `t ≥ t₀` its front is at
`t - W` when `t₀ - a = W`. -/
theorem front_distance (t₀ t : Nat) (a : Int) (W : Nat) (hW : (t₀ : Int) - a = W) (ht : t₀ ≤ t) :
    a + ((t - t₀ : Nat) : Int) = (t : Int) - W := by
  have : ((t - t₀ : Nat) : Int) = (t : Int) - t₀ := by push_cast [Nat.cast_sub ht]; ring
  rw [this]; omega

/-- At a time that is a multiple of a period of diagonal `W + 1`, the cells at distances
`1 .. W + 1` behind the right edge are white. -/
theorem white_behind_edge {W H : Nat} (hP : Per (W + 1) H) (n : Nat) (j : Nat) (hj1 : 1 ≤ j)
    (hj : j ≤ W + 1) : cell (H * n) ((H * n : Nat) - (j : Int)) = false := by
  have hPj : Per j H := by
    rcases Nat.lt_or_eq_of_le hj with h | h
    · exact per_mono_all hP j (by omega)
    · rw [h]; exact hP
  have h1 := hPj.at_mul n
  rw [R_init hj1] at h1
  exact h1

/-- **Every staircase ends.** A staircase living from `t₀` with front `a` at distance
`W = t₀ - a ≥ 2` from the right edge does not live through any multiple `H n ≥ t₀` of a period `H`
of the right diagonal `W + 1`. -/
theorem staircase_ends (t₀ : Nat) (a : Int) (W H : Nat) (hW2 : 2 ≤ W)
    (hW : (t₀ : Int) - a = W) (hP : Per (W + 1) H) (n : Nat) (hn : t₀ ≤ H * n) :
    ¬ Lives t₀ a (H * n) := by
  intro hl
  have h := hl (H * n) hn le_rfl
  rw [front_distance t₀ (H * n) a W hW hn] at h
  have c0 := white_behind_edge hP n W (by omega) (by omega)
  have c1 := white_behind_edge hP n (W - 1) (by omega) (by omega)
  have e : (((H * n : Nat) : Int) - (W : Int)) + 1 = ((H * n : Nat) : Int) - ((W - 1 : Nat) : Int) := by
    push_cast [Nat.cast_sub (show 1 ≤ W by omega)]; ring
  apply h.1
  rw [e, c0, c1]

/-- With the kit's `R_periodic`: every staircase whose front is `W ≥ 2` cells from the right edge
dies by the first multiple of `2 ^ (W + 1)` after it is seen. -/
theorem staircase_ends_pow (t₀ : Nat) (a : Int) (W : Nat) (hW2 : 2 ≤ W)
    (hW : (t₀ : Int) - a = W) (n : Nat) (hn : t₀ ≤ 2 ^ (W + 1) * n) :
    ¬ Lives t₀ a (2 ^ (W + 1) * n) :=
  staircase_ends t₀ a W (2 ^ (W + 1)) hW2 hW (R_periodic (W + 1)) n hn

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Realization", "Ruliology.CellularAutomata.Rule30Jen", "Ruliology.CellularAutomata.Rule30RightPeriods"};
thm = rule30Submission["Rule30Submission.staircase_ends"];
Table[rule30Submission["Rule30Submission." <> n]["TypeForm", "Open" -> opens], {n, {"staircase_ends", "staircase_ends_pow", "front_step", "period_two_iff", "no_fixed_point", "agree_rain_eternal", "rain_row_eternal"}}]
```

The axioms of the headline `staircase_ends` are standard ones only (the checker verifies all seven headlines and replays the whole module):

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

- Nothing about the center column, or any of the Prize problems.
- Only periods `1` and `2` of the edge map are classified. Periodic points of longer period are not.
- Part 1 concerns staircases whose front is within a fixed distance `W ≥ 2` of the single cell's right edge, with a bound exponential in `W`; it says nothing about staircases deep in the chaotic core in practice, nor about other seeds. The front at distance `W ≤ 1` (the pattern `0 1 0` around the edge cell) is not treated.
- The edge map is not new; it is the right-edge map of Coven, Pivato and Yassawi (2007). The staircase bound and the classification of the map's 2-cycles on all odd 2-adic codes are new to the kit's catalog and the submissions list as we read them, which is a statement about our search, not a global novelty determination.
- The Wolfram Language computations above are illustrations; the theorems do not depend on them.

## Provenance

Claude (Anthropic), on the Apple M5, proved by hand that every staircase near the single cell's edge ends (the record's Theorem S, L1007, read by GPT in GC1947), noticed that rain rows keep a two-step patch at their edge for ever and identified it with the period-2 point `-1/3` (the record's L1008). GPT (OpenAI) proved by hand that the rain pair is the only 2-cycle on odd codes (GC1948), and Claude read it independently (L1010) and wrote this module. The record is at github.com/ghywel/placego, reports/rule30-staircases-end.md, reports/rule30-edge-two-cycle-classification.md and reports/wolfram-agents/submissions/rain-pair.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] E. M. Coven, M. Pivato and R. Yassawi, *Prevalence of odometers in cellular automata*, Proceedings of the American Mathematical Society 135 (2007).

[3] Wolfram Institute, [*The Rule 30 Prize kit*](https://github.com/WolframInstitute/Rule30PrizeKit), 2026: `Rule30RightPeriods.Per`, `per_mono_all`, `Per.at_mul`, `R_init`, `Rule30Diagonals.R_periodic`, `Rule30Realization.evol`, `Rule30Equivalents.PeriodicPoints`.
