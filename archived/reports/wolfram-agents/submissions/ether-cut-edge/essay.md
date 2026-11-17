---
Template: ComputationalEssay
Name: The Cut Ether Is Off the Single Cell's Edge Cycle: Depth 8 with Phase 16, and No Flush Thirteen-Cell Ether Word on the Single Cell
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. The kit's cut ether c7cut N has edge-code depth 8 with phase 16 for every N, never agrees on nine edge bits with any phase of the single cell, and so is never a translate of a single-cell row; conversely no single-cell row shows thirteen ether cells flush with its rightmost black cell, and twelve is sharp.
Abstract: In core Lean 4.35.0 we locate the kit's cut ether on the edge dynamics of rule 30. The kit's two-sided barrier uses the truncations c7cut N of the period-4 ether c7, black exactly at the positions 6 mod 7. Read from its rightmost black cell, a finite row has an edge code that evolves by the 2-adic right-edge map, and the kit's frozen ruler says that a code of depth k with phase s0 follows the single cell's code at time s0 + t below bit k and differs from it at bit k for ever. We prove that every c7cut N has depth 8 with phase 16, so its edge never has a white run of eight cells or more behind its edge cell. More: at no time does its edge code agree on nine bits with the single cell's code at any time, so no row of its evolution is a translate of a row of the single cell. Conversely, no row of the single cell shows thirteen ether cells flush with its rightmost black cell, at any phase or position. Twelve occur at time 55, and thirteen at an offset at time 204. The finite facts are a 32-state and a 64-state cycle of the edge map, checked by the kernel.
Keywords: [rule 30, Rule 30 Prize, edge code, frozen ruler, ether, c7cut, single cell, 2-adic edge map, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[lhallee/rule30-open](https://github.com/lhallee/rule30-open)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[rule30-open: SeedPastPeriods](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Frames/SeedPastPeriods.lean)"]
---

## 1. The statement

The kit's `Rule30ZeroBoundaryBarriers` builds its two-sided barrier from the ether `c7`, the row black exactly at the positions `p ≡ 6 (mod 7)`. It is a rule 30 orbit of period `4`, and its truncations `c7cut N` keep the cells of `[-(7N + 1), 7N + 6]`. The kit's `Rule30FrozenRuler` reads a finite row from its rightmost black cell `e`: bit `k` of its *edge code* is the cell at distance `k` from `e`. The code evolves by the 2-adic right-edge map `T` of Coven, Pivato and Yassawi, with the edge moving one cell per step. A code has *depth `k`* with phase `s₀` when it agrees with the single cell's code at time `s₀` below bit `k`, and no code of the single cell's orbit agrees with it below bit `k + 1`. Then, by `frozen_ruler`, it follows the single cell's code at time `s₀ + t` below bit `k`, and differs from it at bit `k`, for ever.

This module places the cut ether in that picture.

- `cut_code_prefix`, `c7cut_depth`: for every `N`, the edge code of `c7cut N` begins `1 0 0 0 0 0 0 1 0`, and it has depth `8` with phase `16`.
- `c7cut_frozen`: at every time `t`, the code of `c7cut N` agrees with the single cell's code at time `16 + t` below bit `8` and differs from it at bit `8`. The white run behind its edge cell is never `8` or longer.
- `c7cut_off_seed`: more, at no time does it agree below bit `9` with the single cell's code at *any* time.
- `c7cut_not_seed_row`: so no row of the evolution of `c7cut N` is a translate of a row of the single cell.
- `seed_no_flush_ether`: conversely, at every time `s`, phase `a` and position `p`, one of the first thirteen cells of the single cell's row, counted from its rightmost black cell, differs from the ether.
- `seed_flush_ether_sharp`: the bound is sharp. At time `55`, twelve cells agree with the ether at phase `3`.
- `seed_offset_ether_204`: the flush condition is needed. At time `204`, the cells at distances `7` to `19` are the ether at phase `2`.

## 2. Codes as numbers

On the first `k` bits, the edge map is a map of numbers:

`T c = (c xor ((c << 1) or (c << 2))) mod 2^k` (`enc_T`).

Bit `k` of `T c` reads only bits `k - 2` to `k` of `c`, so the first `k` bits of a code evolve by themselves. The single cell starts at the code `1`. Its first nine bits run through a cycle of `32` distinct values that misses `129` (`cycle9`), and its first thirteen bits through a cycle of `64` distinct values (`cycle13`). Every time of the single cell lands on these cycles (`orbit9_mem`, `orbit13_mem`), by induction from the kernel-checked closure of each list under the map.

## 3. The proofs

- **The cut's code.** The edge code of `c7cut N` has bit `k` black exactly when `k` is a multiple of `7` and `k ≤ 14N + 7` (`code_cut`). Its first nine bits are therefore `129`, for every `N`, including `N = 0`, where bit `8` lies outside the cut.
- **Depth.** The single cell's code at time `16` has the same first eight bits (`c7cut_depth`), and no code of the single cell has first nine bits `129`. That is depth `8` with phase `16`, and the kit's `frozen_ruler` gives `c7cut_frozen`.
- **Off the cycle.** The edge map sends every odd nine-bit code off the cycle to an odd code off the cycle (`off9_closed`, checked over all `512` codes); it permutes the odd codes, so the cycle and its complement are both closed. The cut's code starts off the cycle and stays off it, whatever the time, which gives `c7cut_off_seed`.
- **Translates.** If a row of the cut were a translate of a row of the single cell, their rightmost black cells would correspond and their codes would be equal (`c7cut_not_seed_row`).
- **Flush ether words.** The ether has `4` phases and `7` positions. None of its `28` thirteen-cell words, read leftward from a position, lies on the thirteen-bit cycle (`ether_off_cycle13`). Since every flush window of the single cell does lie on it, `seed_no_flush_ether` follows. The white-ended words are excluded by the black edge cell itself.

## 4. Scope

- **The flush condition is part of the theorem.** At time `204`, the single cell does have thirteen ether cells at distances `7` to `19`, a black-ended window behind its edge.
- **The cheap version is weaker.** Whole-row non-equality for the unmodified cuts already follows from span parity: a cut's width stays even, while the single cell's rows have odd width. The depth and the flush exclusion say more. Removing the last black cell of `c7cut 1` gives an odd span with the same forbidden nine-bit prefix.
- **What it does not show.** The single cell's nonfinite past is known (below). Nothing here concerns the center column, the kit's ranking barrier for other finite rows, or Problem 1.

## 5. Worked numbers

The cell below replays the finite facts on actual rule 30 rows, not on the edge map:
- the lengths of the nine-bit and thirteen-bit cycles, and whether `129` is on the first;
- the first nine bits of the codes of `c7cut N` for `N = 0..5`;
- for `N = 0, 1, 2` and `t ≤ 32`, whether the edge code of the cut agrees with the single cell's at time `16 + t` below bit `8` and differs at bit `8`;
- over the single cell's rows up to time `300`, the longest flush agreement with the ether at any phase and position, and its first time;
- whether row `204` carries the ether at distances `7` to `19`.

```wl
tm[c_, nb_] := Mod[BitXor[c, BitOr[BitShiftLeft[c, 1], BitShiftLeft[c, 2]]], 2^nb];
cycle[nb_] := Most[NestWhileList[tm[#, nb] &, 1, # != 1 &, {2, 1}]];
c9 = cycle[9]; c13 = cycle[13];
step[row_Association] := With[{ps = Union[Flatten[{# - 1, #, # + 1} & /@ Keys[row]]], g = Lookup[row, #, 0] &}, Association[(# -> 1) & /@ Select[ps, BitXor[g[# - 1], BitOr[g[#], g[# + 1]]] == 1 &]]];
c7[p_] := Boole[Mod[p + 1, 7] == 0];
cut[n_] := Association[(# -> 1) & /@ Select[Range[-(7 n + 1), 7 n + 6], c7[#] == 1 &]];
code[row_, e_, n_] := Sum[Lookup[row, e - k, 0] 2^k, {k, 0, n - 1}];
prefixes = Table[code[cut[n], 7 n + 6, 9], {n, 0, 5}];
seeds = NestList[step, <|0 -> 1|>, 320];
frozen = And @@ Flatten[Table[With[{rows = NestList[step, cut[n], 32]}, Table[With[{a = code[rows[[t + 1]], 7 n + 6 + t, 9], b = code[seeds[[17 + t]], 16 + t, 9]}, Mod[a, 256] == Mod[b, 256] && BitGet[a, 8] != BitGet[b, 8]], {t, 0, 32}]], {n, 0, 2}]];
ether = NestList[Function[r, Table[BitXor[r[[Mod[p - 1, 7] + 1]], BitOr[r[[p + 1]], r[[Mod[p + 1, 7] + 1]]]], {p, 0, 6}]], Table[c7[p], {p, 0, 6}], 3];
flush = Table[With[{cs = Table[Lookup[seeds[[s + 1]], s - j, 0], {j, 0, 12}]}, Max[Table[LengthWhile[Range[0, 12], cs[[# + 1]] == ether[[a + 1, Mod[p - #, 7] + 1]] &], {a, 0, 3}, {p, 0, 6}]]], {s, 0, 300}];
row204 = And @@ Table[Lookup[seeds[[205]], 204 - 7 - j, 0] == ether[[3, Mod[1 - j, 7] + 1]], {j, 0, 12}];
{Length[c9], MemberQ[c9, 129], Length[c13], prefixes, frozen, Max[flush], First[FirstPosition[flush, Max[flush]]] - 1, row204}
```

## 6. Prior art and scope

- **The kit's machinery.** The edge code, its map, depth and the frozen ruler are the kit's `Rule30FrozenRuler`. The 2-adic right-edge map is that of E. Coven, M. Pivato and R. Yassawi, Proc. Amer. Math. Soc. 135 (2007). The cut ether and its period are the kit's `Rule30ZeroBoundaryBarriers`.
- **The single cell's past.** [`lhallee/rule30-open`'s `SeedPastPeriods`](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Frames/SeedPastPeriods.lean) proves that the single cell has no finite past; we do not claim it.
- **What is new.** The depth and phase of the cut ether, its separation from every phase of the single cell's cycle, and the sharp flush ether exclusion, in Lean.
- **History.** These came from a sub-agent run of our programme. A skeptic's run corrected them to the flush form, and GPT carried the result with an independent finite replay.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30FrozenRuler` and `Rule30ZeroBoundaryBarriers`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30FrozenRuler
import Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers
/-!
# Rule 30: the cut ether is off the single cell's edge cycle

`Rule30ZeroBoundaryBarriers` uses the truncations `c7cut N` of the period-4 configuration `c7`
(black exactly at `p ≡ 6 mod 7`) as witnesses of its two-sided barrier. `Rule30FrozenRuler` reads a
finite row from its rightmost black cell: its edge code evolves by the edge map `T`, and a code of
depth `k` with phase `s₀` follows the single cell's code at time `s₀ + t` below bit `k` and differs
from it at bit `k`, for ever (`frozen_ruler`). This module computes where the cut ether sits.

* `cut_code_prefix`, `c7cut_depth`: for every `N`, the edge code of `c7cut N`, read from its
  rightmost black cell `7 N + 6`, begins `1 0 0 0 0 0 0 1 0` (bits `0` and `7` black), and it has
  depth `8` with phase `16`.
* `c7cut_frozen`: so by the frozen ruler, at every time `t` its code agrees with the single cell's
  at time `16 + t` below bit `8` and differs at bit `8`, and the white run behind its edge cell is
  never `8` or longer.
* `c7cut_off_seed`: more: at no time does its code agree below bit `9` with the single cell's code
  at any time. The first nine bits of the single cell's code run through a cycle of `32` values
  (`cycle9`), which `129` misses, and the edge map permutes the odd nine-bit codes, so the
  complement of that cycle is closed too (`off9_closed`). Hence no row of the evolution of
  `c7cut N` is a translate of a row of the single cell (`c7cut_not_seed_row`).
* `seed_no_flush_ether`: no row of the single cell shows, flush with its rightmost black cell,
  thirteen consecutive cells of the ether `c7` at any phase and position: the first thirteen bits
  of its code run through a cycle of `64` values (`cycle13`), none of them a thirteen-cell word of
  `c7`. The bound is sharp: at time `55` the first twelve cells agree with the ether at phase `3`
  (`seed_flush_ether_sharp`).

The computations are on `k`-bit codes, where the edge map is `c xor ((c << 1) or (c << 2))`
modulo `2 ^ k` (`enc_T`). The flush condition matters: without it the statement is false, since
the single cell's row at time `204` has thirteen ether cells at distances `7..19` behind its edge
(`seed_offset_ether_204`).
The single cell's nonfinite past is known (`lhallee/rule30-open`, `SeedPastPeriods`); nothing here
concerns the center column.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

open Rule30Jen Rule30Realization Rule30FrozenRuler
open Rule30ZeroBoundaryBarriers (c7 c7cut c7cut_eq c7cut_hi c7cut_above evol_c7_shift evol_c7_period_mul)

/-! ### The edge map on `k`-bit codes -/

/-- The edge map on the first `k` bits of a code, as a number. -/
def Tm (k c : Nat) : Nat := (c ^^^ ((c <<< 1) ||| (c <<< 2))) % 2 ^ k

/-- `itN f n x`: `n` applications of `f`. -/
def itN (f : Nat → Nat) : Nat → Nat → Nat
  | 0, x => x
  | n + 1, x => f (itN f n x)

/-- The first `k` bits of a code, as a number (bit `i` is `c i`). -/
def enc : Nat → (Nat → Bool) → Nat
  | 0, _ => 0
  | k + 1, c => (if c 0 then 1 else 0) + 2 * enc k (fun i => c (i + 1))

theorem testBit_enc : ∀ k (c : Nat → Bool) i, (enc k c).testBit i = (decide (i < k) && c i)
  | 0, c, i => by simp [enc]
  | k + 1, c, 0 => by
    rw [Nat.testBit_zero]
    simp only [enc]
    by_cases h : c 0 <;> simp [h] <;> omega
  | k + 1, c, i + 1 => by
    rw [Nat.testBit_succ]
    simp only [enc]
    have : ((if c 0 then 1 else 0) + 2 * enc k (fun i => c (i + 1))) / 2 = enc k (fun i => c (i + 1)) := by
      by_cases h : c 0 <;> simp [h] <;> omega
    rw [this, testBit_enc k (fun i => c (i + 1)) i]
    simp

theorem enc_ext {k : Nat} {c d : Nat → Bool} : enc k c = enc k d ↔ AgreeBelow k c d := by
  constructor
  · intro h i hi
    have := congrArg (fun n => n.testBit i) h
    simpa [testBit_enc, hi] using this
  · intro h
    apply Nat.eq_of_testBit_eq
    intro i
    rw [testBit_enc, testBit_enc]
    by_cases hi : i < k
    · simp [hi, h i hi]
    · simp [hi]

theorem enc_T (k : Nat) (c : Nat → Bool) : enc k (T c) = Tm k (enc k c) := by
  apply Nat.eq_of_testBit_eq
  intro i
  unfold Tm
  rw [testBit_enc, Nat.testBit_mod_two_pow, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft,
    Nat.testBit_shiftLeft, testBit_enc, testBit_enc, testBit_enc]
  by_cases hi : i < k
  · simp only [hi, decide_true, Bool.true_and]
    match i, hi with
    | 0, _ => simp [T]
    | 1, _ => simp [T, show 0 < k by omega]
    | j + 2, _ =>
      simp [T, show j + 1 < k by omega, show j < k by omega]
  · simp [hi]

theorem enc_iter (k : Nat) (c : Nat → Bool) : ∀ n, enc k (Rule30FrozenRuler.iter n c) = itN (Tm k) n (enc k c)
  | 0 => rfl
  | n + 1 => by
    show enc k (T (Rule30FrozenRuler.iter n c)) = Tm k (itN (Tm k) n (enc k c))
    rw [enc_T, enc_iter k c n]

theorem enc_one : ∀ k, 1 ≤ k → enc k one = 1
  | 0, h => absurd h (by omega)
  | k + 1, _ => by
    simp only [enc]
    have : enc k (fun i => one (i + 1)) = 0 := by
      have hz : ∀ m (c : Nat → Bool), (∀ i, c i = false) → enc m c = 0 := by
        intro m
        induction m with
        | zero => intro c _; rfl
        | succ m ih => intro c hc; simp only [enc, hc 0]; rw [ih _ (fun i => hc (i + 1))]; rfl
      exact hz k _ (fun i => by simp [one])
    rw [this]
    simp [one]

theorem enc_orbit (k : Nat) (hk : 1 ≤ k) (s : Nat) : enc k (orbit s) = itN (Tm k) s 1 := by
  rw [orbit, enc_iter, enc_one k hk]

/-! ### The single cell's cycles of nine and of thirteen bits -/

/-- The first nine bits of the single cell's code at the times `0 .. 31`. -/
def C9 : List Nat := (List.range 32).map fun s => itN (Tm 9) s 1

/-- The first thirteen bits of the single cell's code at the times `0 .. 63`. -/
def C13 : List Nat := (List.range 64).map fun s => itN (Tm 13) s 1

/-- **The nine-bit cycle**: the first nine bits of the single cell's code return to `1` after `32`
steps, take `32` distinct values before, are closed under the edge map, and never equal `129`. -/
theorem cycle9 : itN (Tm 9) 32 1 = 1 ∧
    (∀ i, i < 32 → ∀ j, j < 32 → itN (Tm 9) i 1 = itN (Tm 9) j 1 → i = j) ∧
    C9.all (fun x => C9.contains (Tm 9 x)) = true ∧ C9.contains 129 = false := by decide +kernel

/-- **The thirteen-bit cycle**: `64` distinct values, closed under the edge map. -/
theorem cycle13 : itN (Tm 13) 64 1 = 1 ∧
    (∀ i, i < 64 → ∀ j, j < 64 → itN (Tm 13) i 1 = itN (Tm 13) j 1 → i = j) ∧
    C13.all (fun x => C13.contains (Tm 13 x)) = true := by decide +kernel

theorem orbit_mem (k : Nat) (C : List Nat) (h1 : C.contains 1 = true)
    (hC : C.all (fun x => C.contains (Tm k x)) = true) : ∀ s, C.contains (itN (Tm k) s 1) = true
  | 0 => h1
  | s + 1 => by
    have hm := orbit_mem k C h1 hC s
    exact List.all_eq_true.1 hC _ (List.contains_iff_mem.1 hm)

theorem orbit9_mem (s : Nat) : C9.contains (enc 9 (orbit s)) = true := by
  rw [enc_orbit 9 (by omega)]
  exact orbit_mem 9 C9 (by decide) cycle9.2.2.1 s

theorem orbit13_mem (s : Nat) : C13.contains (enc 13 (orbit s)) = true := by
  rw [enc_orbit 13 (by omega)]
  exact orbit_mem 13 C13 (by decide) cycle13.2.2 s

/-- **The odd nine-bit codes off the cycle stay off it.** -/
theorem off9_closed : ∀ x, x < 512 → x % 2 = 1 → C9.contains x = false →
    Tm 9 x < 512 ∧ (Tm 9 x) % 2 = 1 ∧ C9.contains (Tm 9 x) = false := by decide +kernel

/-! ### The cut ether -/

theorem code_cut (N k : Nat) : code (c7cut N) (7 * (N : Int) + 6) k =
    (decide (k ≤ 14 * N + 7) && decide (k % 7 = 0)) := by
  unfold code
  rw [c7cut_eq]
  by_cases hk : k ≤ 14 * N + 7
  · rw [ite_eq_left (by omega)]
    unfold c7
    simp only [hk, decide_true, Bool.true_and]
    have : (7 * (N : Int) + 6 - (k : Int) + 1) % 7 = 0 ↔ k % 7 = 0 := by omega
    exact decide_eq_decide.2 this
  · rw [ite_eq_right (by omega)]
    simp [hk]

/-- **The cut's code begins `1 0 0 0 0 0 0 1 0`**, for every `N`. -/
theorem cut_code_prefix (N : Nat) : ∀ i, i < 9 →
    code (c7cut N) (7 * (N : Int) + 6) i = decide (i = 0 ∨ i = 7) := by
  intro i hi
  rw [code_cut]
  have : (decide (i ≤ 14 * N + 7) && decide (i % 7 = 0)) = decide (i = 0 ∨ i = 7) := by
    by_cases h0 : i = 0
    · subst h0; simp
    · by_cases h7 : i = 7
      · subst h7; simp
      · have : ¬ (i % 7 = 0) := by omega
        simp [this, h0, h7]
  exact this

theorem enc9_cut (N : Nat) : enc 9 (code (c7cut N) (7 * (N : Int) + 6)) = 129 := by
  have h : enc 9 (fun i => decide (i = 0 ∨ i = 7)) = 129 := by decide +kernel
  rw [← h, enc_ext]
  intro i hi
  exact cut_code_prefix N i hi

/-- **Depth `8`, phase `16`**, for every cut. -/
theorem c7cut_depth (N : Nat) : HasDepth (code (c7cut N) (7 * (N : Int) + 6)) 8 16 := by
  refine ⟨?_, fun s hs => ?_⟩
  · rw [← enc_ext, enc_orbit 8 (by omega)]
    have h8 : enc 8 (code (c7cut N) (7 * (N : Int) + 6)) = 129 := by
      have h : enc 8 (fun i => decide (i = 0 ∨ i = 7)) = 129 := by decide +kernel
      rw [← h, enc_ext]
      intro i hi
      exact cut_code_prefix N i (by omega)
    rw [h8]
    decide +kernel
  · have h := enc_ext.2 (show AgreeBelow 9 (orbit s) (code (c7cut N) (7 * (N : Int) + 6)) from
      fun i hi => hs i (by omega))
    rw [enc9_cut] at h
    have := orbit9_mem s
    rw [h, cycle9.2.2.2] at this
    exact Bool.noConfusion this

/-- **The frozen ruler for the cut ether.** -/
theorem c7cut_frozen (N t : Nat) :
    AgreeBelow 8 (code (cell (16 + t)) ((16 + t : Nat) : Int))
        (code (evol (c7cut N) t) (7 * (N : Int) + 6 + t)) ∧
      code (cell (16 + t)) ((16 + t : Nat) : Int) 8 ≠ code (evol (c7cut N) t) (7 * (N : Int) + 6 + t) 8 ∧
      ∀ w, 8 ≤ w → ¬ Width (code (evol (c7cut N) t) (7 * (N : Int) + 6 + t)) w := by
  have h := frozen_ruler (c7cut N) (7 * (N : Int) + 6) (c7cut_hi N)
    (fun p hp => c7cut_above N p hp) 8 16 (by omega) (c7cut_depth N) t
  exact ⟨h.2.2.1, h.2.2.2.1, h.2.2.2.2.2.2⟩

/-- **At no time does the cut's code agree with any of the single cell's codes below bit `9`.** -/
theorem c7cut_off_seed (N t s : Nat) :
    ¬ AgreeBelow 9 (orbit s) (code (evol (c7cut N) t) (7 * (N : Int) + 6 + t)) := by
  intro hs
  have he := (edge_evol (c7cut N) (7 * (N : Int) + 6) (c7cut_hi N) (fun p hp => c7cut_above N p hp) t).2.2
  rw [he, ← enc_ext, enc_iter, enc9_cut] at hs
  have hinv : ∀ n, itN (Tm 9) n 129 < 512 ∧ (itN (Tm 9) n 129) % 2 = 1 ∧
      C9.contains (itN (Tm 9) n 129) = false := by
    intro n
    induction n with
    | zero => exact ⟨by decide, by decide, cycle9.2.2.2⟩
    | succ n ih => exact off9_closed _ ih.1 ih.2.1 ih.2.2
  have hm := orbit9_mem s
  rw [hs, (hinv t).2.2] at hm
  exact Bool.noConfusion hm

theorem seed_edge (s : Nat) : cell s s = true ∧ ∀ p, (s : Int) < p → cell s p = false := by
  have h := edge_evol seed 0 (by simp [seed]) (fun p hp => by simp [seed]; omega) s
  refine ⟨?_, fun p hp => ?_⟩
  · rw [← evol_seed]; simpa using h.1
  · rw [← evol_seed]; exact h.2.1 p (by omega)

/-- **No row of the evolution of a cut is a translate of a row of the single cell.** -/
theorem c7cut_not_seed_row (N t s : Nat) (d : Int) :
    ¬ ∀ q, evol (c7cut N) t q = cell s (q + d) := by
  intro h
  obtain ⟨h1, h2, -⟩ := edge_evol (c7cut N) (7 * (N : Int) + 6) (c7cut_hi N)
    (fun p hp => c7cut_above N p hp) t
  obtain ⟨s1, s2⟩ := seed_edge s
  have hpos : 7 * (N : Int) + 6 + t + d = s := by
    rcases Int.lt_trichotomy (7 * (N : Int) + 6 + t + d) s with hlt | heq | hgt
    · have h3 := h2 ((s : Int) - d) (by omega)
      rw [h, show (s : Int) - d + d = s by omega, s1] at h3
      exact absurd h3 (by decide)
    · exact heq
    · have h3 := h1
      rw [h, s2 _ hgt] at h3
      exact absurd h3 (by decide)
  apply c7cut_off_seed N t s
  intro i _
  rw [← seed_code]
  unfold code
  rw [h, show 7 * (N : Int) + 6 + t - (i : Int) + d = (s : Int) - i by omega]

/-! ### Flush ether words -/

/-- The first `13` cells of the ether `c7` at phase `a`, read leftward from position `p`. -/
def ew (a : Nat) (p : Int) : Nat := enc 13 (fun j => evol c7 a (p - j))

/-- **No thirteen-cell word of the ether is a code of the single cell.** -/
theorem ether_off_cycle13 : ∀ a, a < 4 → ∀ p : Nat, p < 7 → C13.contains (ew a p) = false := by
  decide +kernel

theorem ew_reduce (a : Nat) (p : Int) : ew a p = ew (a % 4) ((p % 7 : Int).toNat) := by
  unfold ew
  congr 1
  funext j
  have e1 : evol c7 a (p - j) = evol c7 (a % 4) (p - j) := by
    have := evol_c7_period_mul (a % 4) (a / 4) (p - j)
    rw [show a % 4 + 4 * (a / 4) = a by omega] at this
    exact this
  have e2 : evol c7 (a % 4) (p - j) = evol c7 (a % 4) (((p % 7 : Int).toNat : Int) - j) := by
    have := evol_c7_shift (a % 4) (((p % 7 : Int).toNat : Int) - j) (p / 7)
    rw [show ((p % 7 : Int).toNat : Int) - j + 7 * (p / 7) = p - j by
      have := Int.emod_nonneg p (by decide : (7 : Int) ≠ 0); omega] at this
    exact this
  rw [e1, e2]

/-- **No flush ether word on the single cell.** At every time `s`, for every phase `a` and
position `p` of the ether, one of the first thirteen cells behind and including the single cell's
rightmost black cell differs from the ether. -/
theorem seed_no_flush_ether (s a : Nat) (p : Int) :
    ∃ j, j < 13 ∧ code (cell s) s j ≠ evol c7 a (p - j) := by
  refine Classical.byContradiction fun hne => ?_
  have hag : AgreeBelow 13 (orbit s) (fun j => evol c7 a (p - j)) := by
    intro j hj
    rw [← seed_code]
    exact Classical.byContradiction fun h => hne ⟨j, hj, h⟩
  have h := enc_ext.2 hag
  have hm := orbit13_mem s
  rw [h, show enc 13 (fun j => evol c7 a (p - j)) = ew a p from rfl, ew_reduce,
    ether_off_cycle13 (a % 4) (by omega) ((p % 7 : Int).toNat)
      (by have := Int.emod_nonneg p (by decide : (7 : Int) ≠ 0); omega)] at hm
  exact Bool.noConfusion hm

/-- **Sharpness**: at time `55` the first twelve cells of the single cell's code agree with the
ether at phase `3`, position `4`. -/
theorem seed_flush_ether_sharp :
    ∀ j, j < 12 → code (cell 55) ((55 : Nat) : Int) j = evol c7 3 (4 - j) := by
  intro j hj
  have h : itN (Tm 12) 55 1 = enc 12 (fun j => evol c7 3 (4 - j)) := by decide +kernel
  rw [← enc_orbit 12 (by omega), enc_ext] at h
  rw [seed_code]
  exact h j hj

/-- **The flush condition is needed.** At time `204` the thirteen cells at distances `7 .. 19`
behind the single cell's rightmost black cell are the ether at phase `2`, position `1`. -/
theorem seed_offset_ether_204 :
    ∀ j, j < 13 → code (cell 204) ((204 : Nat) : Int) (7 + j) = evol c7 2 (1 - j) := by
  intro j hj
  have h : ∀ j, j < 13 → (itN (Tm 20) 204 1).testBit (7 + j) = evol c7 2 (1 - j) := by
    decide +kernel
  have e := testBit_enc 20 (orbit 204) (7 + j)
  rw [enc_orbit 20 (by omega)] at e
  rw [seed_code, ← h j hj, e]
  simp [show 7 + j < 20 by omega]

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30FrozenRuler", "Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers", "Ruliology.CellularAutomata.Rule30Realization", "Ruliology.CellularAutomata.Rule30Jen"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"cycle9", "cycle13", "off9_closed", "cut_code_prefix", "c7cut_depth", "c7cut_frozen", "c7cut_off_seed", "c7cut_not_seed_row", "seed_no_flush_ether", "seed_flush_ether_sharp", "seed_offset_ether_204"};
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.seed_offset_ether_204"]["KernelCheck"]
```
