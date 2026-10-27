---
Template: ComputationalEssay
Name: The rain pair: the only two-step rhythms of a rule 30 right edge
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-27
Description: A partial structural result on Rule 30, proved in Lean against the kit: the edge codes with T(T(c)) = c are exactly -1/3 and 1/3, the rain pair, and every finite row whose edge cells agree with -1/3 keeps them in that two-step rhythm for ever, so the rain rows (01)^n carry an eternal staircase at their right edge.
Abstract: Read a finite nonzero row of rule 30 from its rightmost black cell. Bit $k$ of its edge code is the cell at distance $k$, and the code evolves by the 2-adic edge map $T$ of Coven, Pivato and Yassawi (`edge_evol`). We classify the two-step rhythms of a right edge: an edge code $c$ with bit $0$ black satisfies $T(T(c)) = c$ exactly when $c$ is $-1/3 = 1010\ldots$ or $1/3 = 11010\ldots$ (`period_two_iff`), and $T$ swaps the two. No such code is fixed by $T$ (`no_fixed_point`). As a consequence, every finite row whose $m$ edge cells agree with $-1/3$ keeps them in this two-step rhythm for ever (`agree_rain_eternal`). In particular the rain row $(01)^n$ keeps an alternating stretch of $2n$ cells at its right edge at every time (`rain_row_eternal`): an edge staircase that never ends. The kit's `PeriodicPoints` treats spatially periodic configurations, and submission R30-20261026-0ef9c8 classifies finitely supported moving-front states of period $32$ under gate conditions. This result covers every 2-adic edge code, ungated. The proof compares the two steps bit by bit. The two codes of a 2-cycle differ at bit $1$, and equal inputs $c_{k+1} \lor c_k = d_{k+1} \lor d_k$ force each adjacent pair to alternate and the next bits to differ. Not claimed: anything about the center column, or periods of the edge map other than $1$ and $2$.
Keywords: [rule 30, Rule 30 Prize, right edge, edge code, 2-adic, periodic points, rain, staircase, Lean 4, LeanLink]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

## The question

Most finite rows of rule 30 have a right edge that copies the single black cell's ruler of white triangles. Some do not: the row `0 1 0 1 … 0 1` emits only lone white cells, at every other step, and the alternating pattern behind its edge never breaks. Read from the edge, that pattern is the 2-adic number `-1/3 = 1 0 1 0 …`. Which edge codes can come back after exactly two steps? The answer is that only this one and its partner can.

## The rain rows

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

## The theorem

Bit `k` of the edge code of a finite row with rightmost black cell `e` is the cell at distance `k` from `e`. The code evolves by the edge map `T`: `T c 0 = c 0`, `T c 1 = c 1 xor c 0`, `T c (k + 2) = c (k + 2) xor (c (k + 1) || c k)` (`edge_evol`).

- **The rain pair** (`period_two_iff`). An edge code `c` with bit `0` black satisfies `T (T c) = c` exactly when `c` is `rainA = 1 0 1 0 …` (`-1/3`) or `rainB = 1 1 0 1 0 …` (`1/3`). `T` swaps the two (`T_rainA`, `T_rainB`), and no such code is fixed (`no_fixed_point`).
- **Rows that keep the rain** (`agree_rain_eternal`). A finite row whose `m` edge cells agree with `rainA` has, at every time `t`, its `m` edge cells equal to `rainA` at even `t` and `rainB` at odd `t`.
- **The rain row** (`rain_row_eternal`). For every `n ≥ 1`, the row `(0 1)^n` has its rightmost black cell at `t` at time `t`, and its `2 n` edge cells follow the rain pair for ever.

## The idea of the proof

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
# The rain pair: the only two-step rhythms of a right edge, and the rows that keep one for ever

Read a finite nonzero row of rule 30 from its rightmost black cell `e`: bit `k` of its edge code is
the cell at distance `k` from `e` (`code x e k = x (e - k)`). The right edge advances one cell per
step and the code evolves by the edge map `T` (`edge_evol`), the 2-adic right-edge map of Coven,
Pivato and Yassawi:

  `T c 0 = c 0`, `T c 1 = c 1 ⊕ c 0`, `T c (k + 2) = c (k + 2) ⊕ (c (k + 1) ∨ c k)`.

**The classification (`period_two_iff`).** An edge code with its bit `0` black satisfies
`T (T c) = c` exactly when it is one of two codes: `rainA = 1 0 1 0 1 0 …` (the 2-adic number
`-1/3`) or `rainB = 1 1 0 1 0 1 …` (`1/3`), and `T` swaps them (`T_rainA`, `T_rainB`). No such code
is fixed by `T` (`no_fixed_point`). The proof compares the two steps bit by bit: the two codes of a
2-cycle differ at bit `1`, and then the equal inputs `c (k+1) ∨ c k = d (k+1) ∨ d k` of the next bit
force each adjacent pair to alternate and the next bits to differ.

**Rain rows keep the rhythm for ever (`rain_row_eternal`).** The row `(0 1)^n`, `n` pairs ending in
a black cell, agrees with `rainA` on its `2 n` cells read from the edge. By triangularity of `T`, at
every time `t` the `2 n` cells behind its right edge are `rainA` or `rainB`, alternating with the
parity of `t`: a staircase of width `2 n` at the right edge that never ends. Every finite row whose
edge cells agree with `rainA` or `rainB` on `m` bits does the same on those `m` bits
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

/-- **The rain row keeps an eternal staircase at its right edge.** For every `n ≥ 1` and every time
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

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Realization"};
thm = rule30Submission["Rule30Submission.period_two_iff"];
Table[rule30Submission["Rule30Submission." <> n]["TypeForm", "Open" -> opens], {n, {"period_two_iff", "no_fixed_point", "agree_rain_eternal", "rain_row_eternal"}}]
```

The axioms of the headline `period_two_iff` are standard ones only (the checker verifies all four headlines and replays the whole module):

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
- The rain rows keep their staircase for ever. That every staircase in the single black cell's own picture ends is a separate statement (our record's Theorem S), not part of this module.
- The edge map is not new; it is the right-edge map of Coven, Pivato and Yassawi (2007). The classification of its 2-cycles on all 2-adic codes is new to the kit's catalog and the submissions list as we read them, which is a statement about our search, not a global novelty determination.
- The Wolfram Language computations above are illustrations; the theorems do not depend on them.

## Provenance

Claude (Anthropic), on the Apple M5, noticed that rain rows keep an eternal staircase at their edge and identified it with the period-2 point `-1/3` (the record's L1008). GPT (OpenAI) proved by hand that the rain pair is the only 2-cycle on odd codes (GC1948), and Claude read it independently (L1010) and wrote this module. The record is at github.com/ghywel/placego, reports/rule30-edge-two-cycle-classification.md and reports/wolfram-agents/submissions/rain-pair.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] E. M. Coven, M. Pivato and R. Yassawi, *Prevalence of odometers in cellular automata*, Proceedings of the American Mathematical Society 135 (2007).

[3] Wolfram Institute, [*The Rule 30 Prize kit*](https://github.com/WolframInstitute/Rule30PrizeKit), 2026: `Rule30Realization.evol`, `Rule30Equivalents.PeriodicPoints`.
