---
Template: ComputationalEssay
Name: White runs beside two periodic columns of rule 30 are at most two periods long
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-29
Description: A partial result about rule 30 from arbitrary configurations, proved in Lean: if columns 0 and 1 share a period P ≥ 2 from time 0 and column 0 is black at some time, every white run of row 0 to their left has length at most 2P − 2, and an odd black-bounded white run at most 2P − 5; the bound is attained by the period-3 and period-4 ethers
Abstract: For every configuration $x : \mathbb{Z} \to \{0,1\}$ of rule 30 whose columns $0$ and $1$ are periodic with a common period $P \ge 2$ from time $0$, and whose column $0$ is black at some time, every run of white cells in row $0$ to the left of column $0$ has length at most $2P-2$ (`Rule30Submission.zero_run_le`); a white run of odd length $2m+1 \ge 3$ with black cells at both ends needs $P \ge m+3$, so it has length at most $2P-5$ (`Rule30Submission.odd_zero_run_le`). The kit propagates periodicity to the left (`Rule30Jen.periodic_left`) and, by Jen's theorem (`Rule30FiniteConfigs.jen`), the hypotheses never hold in a configuration with a leftmost black cell; we found no bound on white runs beside two periodic columns in the catalog or among the listed submissions. The proof: periodicity moves left; a long white run leaves a white triangle that makes the column at depth $d+P-1$ white for a whole period, hence for ever; the column to its right then only latches black, so being periodic and white at time $0$ it is white for ever; two adjacent white columns force white columns to their right up to column $0$. The bound is attained: on rings of up to 18 cells, the period-3 ether $(000010011111)^\infty$ has white runs of $4$ and $(0000001)^\infty$, of period $4$, has runs of $6$. The statement is vacuous for configurations with a leftmost black cell, and nothing here concerns the single-seed centre column or decides Problem 1.
Keywords: [rule 30, Rule 30 Prize, periodic columns, Jen's theorem, white runs, ether, spatially periodic configurations, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entry 6](https://github.com/ghywel/placego/blob/main/PROOFS.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Rule30Jen in the kit](https://github.com/WolframInstitute/Rule30PrizeKit/blob/main/lean/Ruliology/CellularAutomata/Rule30Jen.lean)"]
---

## The question

Rule 30 updates every cell from itself and its two neighbours: the new colour is *left* XOR (*centre* OR *right*). Problem 1 asks whether the centre column of the single-seed pattern is ever eventually periodic. Jen showed in 1986 that no two columns of a configuration with a leftmost black cell are both eventually periodic (the kit's `Rule30Jen.jen`, `Rule30FiniteConfigs.jen`). Her argument starts from a local fact: if two adjacent columns share a period, every column to their left does too (`Rule30Jen.periodic_left`), because rule 30 is left-permutive.

Without a left edge, two adjacent periodic columns are possible: spatially periodic configurations that repeat in time are examples. This essay asks what such columns force on the row they start from, and proves that they bound the white runs to their left by two periods.

## The theorems

Write $x_t(i)$ for the cell at position $i$ and time $t$, from an arbitrary start $x_0 : \mathbb{Z} \to \{0,1\}$ (the kit's `Rule30Realization.evol`).

- **White runs** (`zero_run_le`). If columns $0$ and $1$ are $P$-periodic from time $0$, $P \ge 2$, and $x_t(0) = 1$ for some $t$, then every white run of row $0$ at positions $-d, \dots, -(d+R-1)$, $d \ge 1$, has $R \le 2P - 2$.
- **Odd white runs** (`odd_zero_run_le`). Under the same hypotheses with $P \ge 1$, a white run of odd length $2m+1 \ge 3$ with black cells at both ends needs $P \ge m + 3$, so its length is at most $2P - 5$.

## The idea of the proof

1. **Periodicity moves left.** By left-permutivity, $x_t(k-1) = x_{t+1}(k) \oplus (x_t(k) \lor x_t(k+1))$, so two $P$-periodic columns $k, k+1$ make column $k-1$ $P$-periodic (`left_periodic`). Every column left of $0$ is $P$-periodic.
2. **A white triangle.** A white run of row $0$ stays white in a triangle beneath it, losing a cell at each end per step (`triangle`).
3. **A column white for ever.** If $R \ge 2P - 1$, the column at depth $d + P - 1$ lies in the triangle for the first $P$ steps, so it is white for a whole period, hence for ever (`per_first`).
4. **A latch.** Beside a column that is always white, the next column follows $x' = x \lor (\text{right neighbour})$, so once black it stays black (`latch`). Being periodic and white at time $0$, it is white for ever (`white_of_latch`).
5. **Pushing right.** Two adjacent always-white columns force the column to their right to be always white (`push_right`), and so on up to column $0$ (`push_to_zero`), which is black at some time: a contradiction.

For odd runs the run shrinks by exactly one cell at each end per step while its ends are black (`shrink`); its apex column stays white for $m + 2$ steps, a whole period when $P \le m + 2$, and steps 4 and 5 apply.

## The bound is attained

On a ring of $n$ cells, every column of a periodic point with least period $P$ repeats with period $P$ (a single column's own least period may be smaller), so the theorems apply to every maximal white run of every row. The census below stores cell $i$ in bit $i$ of an integer; white-run lengths do not depend on the reading direction. A census of all periodic points on rings of $3$ to $14$ cells (the same holds up to $18$ cells, computed separately):

```wl
ringStep[n_][x_] := BitXor[BitAnd[BitOr[BitShiftLeft[x, 1], BitShiftRight[x, n - 1]], 2^n - 1], BitOr[x, BitAnd[BitOr[BitShiftRight[x, 1], BitShiftLeft[BitAnd[x, 1], n - 1]], 2^n - 1]]];
whiteRuns[x_, n_] := Module[{d = IntegerDigits[x, 2, n], k}, k = First[FirstPosition[d, 1]]; Length /@ Select[Split[RotateLeft[d, k - 1]], First[#] == 0 &]];
ringCensus[n_] := Module[{nxt = ringStep[n][Range[0, 2^n - 1]], s, t, per}, s = Range[0, 2^n - 1]; While[(t = Union[nxt[[s + 1]]]) =!= s, s = t]; s = DeleteCases[s, 0]; per = Table[Module[{y = nxt[[x + 1]], p = 1}, While[y != x, y = nxt[[y + 1]]; p++]; p], {x, s}]; GroupBy[Transpose[{per, Max[Append[whiteRuns[#, n], 0]] & /@ s}], First -> Last, Max]];
census = KeySort[Merge[Table[ringCensus[n], {n, 3, 14}], Max]];
Grid[Prepend[KeyValueMap[{#1, #2, 2 #1 - 2} &, KeySelect[census, 2 <= # <= 40 &]], {"least period P", "longest white run", "2P - 2"}], Frame -> All]
```

No periodic point exceeds the bound, and it is reached at $P = 3$ and $P = 4$. (The fixed points, $P = 1$, are the two phases of $(01)^\infty$; they are also $2$-periodic, and their white runs of length $1$ are within the bound $2$ for $P = 2$.) The two extremes are ethers: the period-3 ether $(000010011111)^\infty$ and the configuration $(0000001)^\infty$, read left to right. Their least periods under rule 30 itself are $3$ and $4$:

```wl
leastPeriod[w_] := SelectFirst[Range[64], Last[CellularAutomaton[30, w, #]] == w &];
{leastPeriod[{0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1}], leastPeriod[{0, 0, 0, 0, 0, 0, 1}]}
```

```wl
GraphicsRow[{ArrayPlot[CellularAutomaton[30, Flatten[ConstantArray[{0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1}, 4]], 12]], ArrayPlot[CellularAutomaton[30, Flatten[ConstantArray[{0, 0, 0, 0, 0, 0, 1}, 7]], 12]]}, ImageSize -> 520]
```

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
# Rule 30 beside two periodic columns: white runs to their left are at most two periods long

Run rule 30 from an arbitrary configuration `x : Int → Bool` (`Rule30Realization.evol`). Suppose
columns `0` and `1` are both periodic with period `P` from time `0`, and column `0` is black at some
time. Then:

* `zero_run_le`: **every run of white cells of row `0` to the left of column `0`** (the cells
  `-d, …, -(d + R - 1)`, `d ≥ 1`) **has length `R ≤ 2P - 2`**, for `P ≥ 2`.
* `odd_zero_run_le`: a white run of row `0` of odd length `2m + 1 ≥ 3`, with black cells at both
  ends, needs `P ≥ m + 3`; so its length is at most `2P - 5`.

The argument. Left-permutivity moves periodicity left: if columns `k` and `k + 1` have period `P`,
so has column `k - 1` (`left_periodic`, the arbitrary-configuration form of `Rule30Jen.periodic_left`),
so every column left of `0` has period `P`. A white run of
row `0` leaves a white triangle beneath it (`triangle`). If `R ≥ 2P - 1`, the column at depth
`d + P - 1` is white for a whole period, hence for ever. The column to its right then follows
`x' = x ∨ (right neighbour)`, so once black it stays black (`latch`); being periodic and white at
time `0`, it is white for ever. Two adjacent white columns force the column to their right to be
white (`push_right`), and so on up to column `0`, which is not white for ever. For the odd run, the
run shrinks by one cell at each end per step (`shrink`), and its apex column is white for `m + 2`
steps, which covers a period when `P ≤ m + 2`.

**Scope.** For a configuration with a leftmost black cell, two adjacent columns are never both
eventually periodic (Jen's theorem, `Rule30FiniteConfigs.jen`), so the hypotheses cannot hold
there. The theorems are about configurations without a left edge, such as spatially periodic ones.
Nothing here concerns the single-seed center column or decides Problem 1.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata Rule30Jen Rule30Realization

theorem evol_succ' (x : Int → Bool) (t : Nat) (i : Int) :
    evol x (t + 1) i = xor (evol x t (i - 1)) (evol x t i || evol x t (i + 1)) := rfl

/-- Column `k` repeats with period `P` from time `0`. -/
def PerAll (x : Int → Bool) (k : Int) (P : Nat) : Prop := ∀ t : Nat, evol x t k = evol x (t + P) k

/-- **Periodicity moves left**: two adjacent `P`-periodic columns make the column to their left
`P`-periodic. -/
theorem left_periodic (x : Int → Bool) (k : Int) (P : Nat) (h0 : PerAll x k P)
    (h1 : PerAll x (k + 1) P) : PerAll x (k - 1) P := by
  intro t
  have inv : ∀ s : Nat, evol x s (k - 1) = xor (evol x (s + 1) k) (evol x s k || evol x s (k + 1)) := by
    intro s
    rw [evol_succ' x s k]
    cases evol x s (k - 1) <;> cases (evol x s k || evol x s (k + 1)) <;> rfl
  rw [inv t, inv (t + P), h0 (t + 1), h0 t, h1 t, show t + 1 + P = t + P + 1 by omega]

/-- Every column left of `0` is `P`-periodic. -/
theorem left_periodic_iter (x : Int → Bool) (P : Nat) (h0 : PerAll x 0 P) (h1 : PerAll x 1 P) :
    ∀ j : Nat, PerAll x (-(j : Int)) P ∧ PerAll x (-(j : Int) + 1) P := by
  intro j
  induction j with
  | zero => exact ⟨by simpa using h0, by simpa using h1⟩
  | succ j ih =>
    refine ⟨?_, ?_⟩
    · have := left_periodic x (-(j : Int)) P ih.1 ih.2
      rwa [show -(j : Int) - 1 = -((j + 1 : Nat) : Int) by omega] at this
    · rw [show -((j + 1 : Nat) : Int) + 1 = -(j : Int) by omega]; exact ih.1

/-- A periodic column is determined by its first period. -/
theorem per_mod (x : Int → Bool) (k : Int) (P : Nat) (h : PerAll x k P) :
    ∀ m t : Nat, evol x (t + m * P) k = evol x t k := by
  intro m
  induction m with
  | zero => intro t; simp
  | succ m ih => intro t; rw [Nat.succ_mul, ← Nat.add_assoc, ← h, ih]

theorem per_first (x : Int → Bool) (k : Int) (P : Nat) (h : PerAll x k P) (t : Nat) :
    evol x t k = evol x (t % P) k := by
  have := per_mod x k P h (t / P) (t % P)
  rw [Nat.mul_comm, Nat.mod_add_div] at this
  exact this

/-- **The white triangle** under a white run of row `0` at depths `d, …, d + R - 1`. -/
theorem triangle (x : Int → Bool) (d R : Nat)
    (hrun : ∀ i : Nat, d ≤ i → i < d + R → x (-(i : Int)) = false) :
    ∀ t i : Nat, d + t ≤ i → i + t < d + R → evol x t (-(i : Int)) = false := by
  intro t
  induction t with
  | zero => intro i h1 h2; exact hrun i (by omega) (by omega)
  | succ t ih =>
    intro i h1 h2
    rw [evol_succ']
    have a : evol x t (-(i : Int) - 1) = false := by
      have := ih (i + 1) (by omega) (by omega)
      rwa [show -((i + 1 : Nat) : Int) = -(i : Int) - 1 by omega] at this
    have b : evol x t (-(i : Int)) = false := ih i (by omega) (by omega)
    have c : evol x t (-(i : Int) + 1) = false := by
      have := ih (i - 1) (by omega) (by omega)
      rwa [show -((i - 1 : Nat) : Int) = -(i : Int) + 1 by omega] at this
    rw [a, b, c]; rfl

/-- **Latch**: with column `k - 1` white for ever, column `k` never turns from black to white. -/
theorem latch (x : Int → Bool) (k : Int) (hz : ∀ t : Nat, evol x t (k - 1) = false) :
    ∀ t : Nat, evol x t k = true → ∀ s : Nat, evol x (t + s) k = true := by
  intro t ht s
  induction s with
  | zero => simpa using ht
  | succ s ih =>
    rw [show t + (s + 1) = (t + s) + 1 by omega, evol_succ', hz (t + s), ih]; rfl

/-- Two adjacent white columns force white to their right. -/
theorem push_right (x : Int → Bool) (k : Int) (ha : ∀ t : Nat, evol x t (k - 1) = false)
    (hb : ∀ t : Nat, evol x t k = false) : ∀ t : Nat, evol x t (k + 1) = false := by
  intro t
  have := hb (t + 1)
  rw [evol_succ', ha t, hb t] at this
  simpa using this

/-- Two white columns at `-k` and `-k + 1` force column `0` white. -/
theorem push_to_zero (x : Int → Bool) (k : Nat) (a0 : ∀ t : Nat, evol x t (-(k : Int)) = false)
    (b0 : ∀ t : Nat, evol x t (-(k : Int) + 1) = false) : ∀ t : Nat, evol x t 0 = false := by
  have push : ∀ j : Nat, j ≤ k → (∀ t : Nat, evol x t (-(k : Int) + j) = false) ∧
      (∀ t : Nat, evol x t (-(k : Int) + j + 1) = false) := by
    intro j
    induction j with
    | zero =>
      intro _
      refine ⟨fun t => ?_, fun t => ?_⟩
      · rw [show -(k : Int) + ((0 : Nat) : Int) = -(k : Int) by omega]; exact a0 t
      · rw [show -(k : Int) + ((0 : Nat) : Int) + 1 = -(k : Int) + 1 by omega]; exact b0 t
    | succ j ih =>
      intro hj
      obtain ⟨a, b⟩ := ih (by omega)
      have a' : ∀ t : Nat, evol x t (-(k : Int) + (j : Int) + 1 - 1) = false := fun t => by
        rw [show -(k : Int) + (j : Int) + 1 - 1 = -(k : Int) + (j : Int) by omega]; exact a t
      have c := push_right x (-(k : Int) + (j : Int) + 1) a' b
      refine ⟨fun t => ?_, fun t => ?_⟩
      · rw [show -(k : Int) + ((j + 1 : Nat) : Int) = -(k : Int) + (j : Int) + 1 by omega]; exact b t
      · rw [show -(k : Int) + ((j + 1 : Nat) : Int) + 1 = -(k : Int) + (j : Int) + 1 + 1 by omega]
        exact c t
  intro t
  have := (push k (Nat.le_refl k)).1 t
  rwa [show -(k : Int) + (k : Int) = 0 by omega] at this

/-- A periodic column that is white at time `0`, beside a column that is white for ever, is white
for ever. -/
theorem white_of_latch (x : Int → Bool) (k : Int) (P : Nat) (hP : 1 ≤ P) (hper : PerAll x k P)
    (hz : ∀ t : Nat, evol x t (k - 1) = false) (h0 : evol x 0 k = false) :
    ∀ t : Nat, evol x t k = false := by
  intro t
  cases hb : evol x t k with
  | false => rfl
  | true =>
    have hl := latch x k hz t hb (t * P - t)
    have : t ≤ t * P := Nat.le_mul_of_pos_right t (by omega)
    rw [show t + (t * P - t) = 0 + t * P by omega, per_mod x k P hper t 0, h0] at hl
    exact absurd hl (by decide)

/-- **White runs beside two periodic columns.** If columns `0` and `1` are `P`-periodic from time
`0`, `P ≥ 2`, and column `0` is black at some time, every white run of row `0` at depths
`d, …, d + R - 1` (`d ≥ 1`) has `R ≤ 2P - 2`. -/
theorem zero_run_le (x : Int → Bool) (P : Nat) (hP : 2 ≤ P) (h0 : PerAll x 0 P) (h1 : PerAll x 1 P)
    (hnz : ∃ t : Nat, evol x t 0 = true) (d R : Nat) (hd : 1 ≤ d)
    (hrun : ∀ i : Nat, d ≤ i → i < d + R → x (-(i : Int)) = false) : R ≤ 2 * P - 2 := by
  by_cases hR : R ≤ 2 * P - 2
  · exact hR
  · exfalso
    obtain ⟨k, hk⟩ : ∃ k : Nat, k = d + P - 1 := ⟨_, rfl⟩
    have hper := left_periodic_iter x P h0 h1
    -- column -k is white for the first period, hence for ever
    have white_k : ∀ t : Nat, evol x t (-(k : Int)) = false := by
      intro t
      rw [per_first x _ P (hper k).1 t]
      exact triangle x d R hrun (t % P) k (by have := Nat.mod_lt t (show 0 < P by omega); omega)
        (by have := Nat.mod_lt t (show 0 < P by omega); omega)
    -- column -k + 1 is periodic and latched, and white at time 0, so white for ever
    have white_k1 : ∀ t : Nat, evol x t (-(k : Int) + 1) = false := by
      refine white_of_latch x _ P (by omega) (hper k).2
        (fun s => by rw [show -(k : Int) + 1 - 1 = -(k : Int) by omega]; exact white_k s) ?_
      have := hrun (k - 1) (by omega) (by omega)
      rwa [show -((k - 1 : Nat) : Int) = -(k : Int) + 1 by omega] at this
    obtain ⟨t, ht⟩ := hnz
    rw [push_to_zero x k white_k white_k1 t] at ht
    exact absurd ht (by decide)

/-- A white run of row `0` bounded by black cells shrinks by one cell at each end per step. -/
theorem shrink (x : Int → Bool) (d m : Nat) (hd : 1 ≤ d)
    (hrun : ∀ i : Nat, d ≤ i → i ≤ d + 2 * m → x (-(i : Int)) = false)
    (hL : x (-((d - 1 : Nat) : Int)) = true) (hR : x (-((d + 2 * m + 1 : Nat) : Int)) = true) :
    ∀ t : Nat, t ≤ m → (∀ i : Nat, d + t ≤ i → i ≤ d + 2 * m - t → evol x t (-(i : Int)) = false) ∧
      evol x t (-((d + t - 1 : Nat) : Int)) = true ∧
      evol x t (-((d + 2 * m - t + 1 : Nat) : Int)) = true := by
  intro t
  induction t with
  | zero =>
    intro _
    refine ⟨fun i h1 h2 => hrun i (by omega) (by omega), ?_, ?_⟩
    · rw [show d + 0 - 1 = d - 1 by omega]; exact hL
    · rw [show d + 2 * m - 0 + 1 = d + 2 * m + 1 by omega]; exact hR
  | succ t ih =>
    intro ht
    obtain ⟨W, hl, hr⟩ := ih (by omega)
    refine ⟨fun i h1 h2 => ?_, ?_, ?_⟩
    · rw [evol_succ']
      have e1 : evol x t (-(i : Int) - 1) = false := by
        have := W (i + 1) (by omega) (by omega)
        rwa [show -((i + 1 : Nat) : Int) = -(i : Int) - 1 by omega] at this
      have e2 : evol x t (-(i : Int)) = false := W i (by omega) (by omega)
      have e3 : evol x t (-(i : Int) + 1) = false := by
        have := W (i - 1) (by omega) (by omega)
        rwa [show -((i - 1 : Nat) : Int) = -(i : Int) + 1 by omega] at this
      rw [e1, e2, e3]; rfl
    · rw [show d + (t + 1) - 1 = d + t by omega, evol_succ']
      have e1 : evol x t (-((d + t : Nat) : Int) - 1) = false := by
        have := W (d + t + 1) (by omega) (by omega)
        rwa [show -((d + t + 1 : Nat) : Int) = -((d + t : Nat) : Int) - 1 by omega] at this
      have e2 : evol x t (-((d + t : Nat) : Int)) = false := W (d + t) (by omega) (by omega)
      have e3 : evol x t (-((d + t : Nat) : Int) + 1) = true := by
        rwa [show -((d + t : Nat) : Int) + 1 = -((d + t - 1 : Nat) : Int) by omega]
      rw [e1, e2, e3]; rfl
    · rw [show d + 2 * m - (t + 1) + 1 = d + 2 * m - t by omega, evol_succ']
      have e1 : evol x t (-((d + 2 * m - t : Nat) : Int) - 1) = true := by
        rwa [show -((d + 2 * m - t : Nat) : Int) - 1 = -((d + 2 * m - t + 1 : Nat) : Int) by omega]
      have e2 : evol x t (-((d + 2 * m - t : Nat) : Int)) = false := W (d + 2 * m - t) (by omega) (by omega)
      have e3 : evol x t (-((d + 2 * m - t : Nat) : Int) + 1) = false := by
        have := W (d + 2 * m - t - 1) (by omega) (by omega)
        rwa [show -((d + 2 * m - t - 1 : Nat) : Int) = -((d + 2 * m - t : Nat) : Int) + 1 by omega] at this
      rw [e1, e2, e3]; rfl

/-- **Odd white runs.** If columns `0` and `1` are `P`-periodic from time `0` and column `0` is black
at some time, a white run of row `0` of odd length `2m + 1 ≥ 3` (depths `d, …, d + 2m`, `d ≥ 1`) with
black cells at depths `d - 1` and `d + 2m + 1` needs `P ≥ m + 3`: its length is at most `2P - 5`. -/
theorem odd_zero_run_le (x : Int → Bool) (P : Nat) (hP : 1 ≤ P) (h0 : PerAll x 0 P)
    (h1 : PerAll x 1 P) (hnz : ∃ t : Nat, evol x t 0 = true) (d m : Nat) (hd : 1 ≤ d) (hm : 1 ≤ m)
    (hrun : ∀ i : Nat, d ≤ i → i ≤ d + 2 * m → x (-(i : Int)) = false)
    (hL : x (-((d - 1 : Nat) : Int)) = true) (hR : x (-((d + 2 * m + 1 : Nat) : Int)) = true) :
    m + 3 ≤ P := by
  by_cases hP' : m + 3 ≤ P
  · exact hP'
  · exfalso
    have hper := left_periodic_iter x P h0 h1
    have S := shrink x d m hd hrun hL hR
    obtain ⟨c, hc⟩ : ∃ c : Nat, c = d + m := ⟨_, rfl⟩
    -- the apex column -c is white at times 0 .. m + 1, which covers a period
    have apex : ∀ s : Nat, s ≤ m + 1 → evol x s (-(c : Int)) = false := by
      intro s hs
      by_cases h : s < m + 1
      · exact (S s (by omega)).1 c (by omega) (by omega)
      · have hs' : s = m + 1 := by omega
        subst hs'
        obtain ⟨hw, hl, hr⟩ := S m (Nat.le_refl m)
        rw [evol_succ']
        have e1 : evol x m (-(c : Int) - 1) = true := by
          rwa [show -(c : Int) - 1 = -((d + 2 * m - m + 1 : Nat) : Int) by omega]
        have e2 : evol x m (-(c : Int)) = false := hw c (by omega) (by omega)
        have e3 : evol x m (-(c : Int) + 1) = true := by
          rwa [show -(c : Int) + 1 = -((d + m - 1 : Nat) : Int) by omega]
        rw [e1, e2, e3]; rfl
    have white_c : ∀ t : Nat, evol x t (-(c : Int)) = false := by
      intro t
      rw [per_first x _ P (hper c).1 t]
      exact apex _ (by have := Nat.mod_lt t (show 0 < P by omega); omega)
    -- its right neighbour is latched, periodic and white at time 0
    have white_c1 : ∀ t : Nat, evol x t (-(c : Int) + 1) = false := by
      refine white_of_latch x _ P hP (hper c).2
        (fun s => by rw [show -(c : Int) + 1 - 1 = -(c : Int) by omega]; exact white_c s) ?_
      have := hrun (c - 1) (by omega) (by omega)
      rwa [show -((c - 1 : Nat) : Int) = -(c : Int) + 1 by omega] at this
    obtain ⟨t, ht⟩ := hnz
    rw [push_to_zero x c white_c white_c1 t] at ht
    exact absurd ht (by decide)

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The two headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Realization"};
Table[rule30Submission["Rule30Submission." <> n]["TypeForm", "Open" -> opens], {n, {"zero_run_le", "odd_zero_run_le"}}]
```

Their axioms are standard ones only:

```wl
thm = rule30Submission["Rule30Submission.zero_run_le"];
{thm["Axioms"], rule30Submission["Rule30Submission.odd_zero_run_le"]["Axioms"]}
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

- For a configuration with a leftmost black cell, two adjacent columns are never both periodic (Jen), so the hypotheses cannot hold there and the theorems say nothing about the single-seed pattern or its centre column. Nothing here decides Problem 1.
- The hypotheses ask for periodicity from time $0$. Periodicity from a later time $T$ gives the same bound for row $T$, by restarting the evolution there; that corollary is not stated separately.
- `left_periodic` is the arbitrary-configuration form of the kit's `Rule30Jen.periodic_left`; the new content is the bound on white runs and its sharpness.
- The bound is attained at $P = 3$ and $P = 4$ by the census above; for larger $P$ the longest white runs found on small rings are far below $2P - 2$, and no sharper general bound is claimed.
- We found no such bound in the kit's catalog or the submissions list as we read them, which is a statement about our search, not a global novelty determination.
- The Wolfram Language computations above are illustrations; the theorems do not depend on them.

## Provenance

Theorem B of the Wolfram · Collatz · Mahler record (PROOFS.md entry 6, 2026-10-05) was proved by hand by Claude (Anthropic) and second-read by GPT (OpenAI); the odd-run refinement is GPT's (GC307). Claude formalized both in Lean against Mathlib on 2026-10-10, and ported them to the kit's core Lean, on the kit's `evol`, on 2026-10-29. The ring census was computed on the Apple M5.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] E. Jen, *Global properties of cellular automata*, J. Stat. Phys. 43 (1986) 219–242.

[3] Wolfram Institute, [*The Rule 30 Prize kit*](https://github.com/WolframInstitute/Rule30PrizeKit), 2026: `Rule30Realization.evol`, `Rule30Jen.periodic_left`, `Rule30Jen.jen`, `Rule30FiniteConfigs.jen`.
