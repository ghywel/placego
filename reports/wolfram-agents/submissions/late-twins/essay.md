---
Template: ComputationalEssay
Name: From Tick 46 On, Every Row of Rule 30 Beside a Wall Has a Twin
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-08
Description: Core Lean. For every nonzero natural y and every t ≥ 46, the row F^(t-2)(y) beside the wall has a twin of the same width with the same image two ticks later; at even t it inherits immortality and lies off the orbit. Twins share their future. Nothing here proves Q01.
Abstract: In the zero-boundary left half of rule 30, read as natural numbers with one tick F and two ticks G = F∘F, Q01 says that every natural reaches an even value under G. We prove in core Lean that for every nonzero natural y and every t ≥ 46, the row x = F^(t-2)(y) has a twin: a different natural x′ of the same width, with the same cell beside the wall, and with F²(x′) = F²(x). If y never reaches an even value and t is even, the twin never does either and is not on the orbit of y. The top of a row evolves on its own, by an explicit map R, so any twenty-cell band with its top cell black settles on one four-cycle within 26 ticks; the kernel checks this in two stages of 4,096 and 512 cases. Every phase of that cycle carries reset words 0 1 0 or 0 1111 0 of the backward transducer, so inverting twice with one cell flipped returns a finite row. Twins share their future after two ticks. Nothing here decides Q01.
Keywords: [rule 30, Rule 30 Prize, Q01, zero-boundary left half, backward transducer, reset words, left side, twin, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "S. Wolfram, Random sequence generation by cellular automata, Advances in Applied Mathematics 7 (1986) 123-169"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261106-45f6e9: Q01, mortality and repeat budgets](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-45f6e9)", "[R30-20261106-bdd993: the first checks](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-bdd993)"]
---

## 1. The statement

Read a natural number `Y` as a row of rule 30 beside a white wall: bit `k` of `Y` is the cell at depth `k + 1`, and the wall is always white. One tick is `F(Y) = (Y >>> 1) XOR (Y OR (Y <<< 1))`, two ticks are `G = F∘F`, and `iter F t` is `t` ticks. These are the kit's `Rule30ZeroBoundary` definitions. In this frame `Q01` says that every natural reaches an even value under `G`, that is, a white cell beside the wall at some even tick (`Q01_iff_integer`).

**Theorem (`late_twin`).** For every nonzero natural `y` and every `t ≥ 46`, the row `x = iter F (t - 2) y` has a twin: a natural `x′ ≠ x` of the same width, with the same cell beside the wall, and with `F (F x′) = F (F x)`.

**Theorem (`late_twin_immortal`, `late_twin_off_orbit`).** If moreover `y` never reaches an even value under `G` and `t` is even, then `x′` never reaches an even value either, and `x′` is none of the rows `iter G j y`.

So an immortal natural, if one existed, would force another immortal natural of the same width at every even tick from `46` on, off its own orbit. The twin and `x` agree two ticks later, so they have one future: the twins add rows, not futures.

## 2. The top of a row moves on its own

With the cut moving out one cell per tick, the cells retained above it depend only on the cells retained at the preceding tick. In this frame that is one identity (`F_shiftRight`): for every row `Y` and every cut `m`,

`F Y >>> (m + 1) = R (Y >>> m)`, where `R u = (u >>> 2) XOR ((u >>> 1) OR u)`.

The cut moves out by one cell each tick, as the top of the row does. Iterating, `iter F t Y >>> (m + t) = R^t (Y >>> m)` (`iter_F_shiftRight`). Once the row has width at least twenty, take the cut at the bottom of its top twenty cells. This band evolves by `R`, independently of what lies below the moving cut.

## 3. The top twenty cells settle within 26 ticks

From any start whose top cell is the twentieth, `R^t` reaches one four-cycle `C20 = {820683, 822904, 911005, 912610}` by `t = 26` and stays there (`band_settles`). Every nonzero row reaches width `20` by tick `19`, so from tick `45` on every row's top twenty cells lie on `C20` (`band_late`).

The kernel checks this in two stages rather than all `2^19` starts at once. Because `R` commutes with shifting, the top thirteen cells evolve on their own too. All `4,096` starts of the top thirteen cells reach the four-cycle `C13 = {6411, 6428, 7117, 7129}` within `14` ticks (`stage13`). From `C13` with any seven cells below it, `512` states, the top twenty reach `C20` within `12` more (`stage20`). That gives `26`. The earlier exhaustive replay found this band bound sharp: among all `2^19` normalized starts, `40,960` need all `26` ticks (COMPUTED in GC2690). The formal theorem here certifies the upper bound `26`; it does not claim that `46` is the earliest possible uniform twin bound.

## 4. Reset words and the twin

A preimage of a row under `F` is fixed by the row and its cell beside the wall. The kit's backward transducer `back b y` builds it upward one depth at a time (`eq_back`, `zrow_back`). Two runs that read the same inputs forget their starting states once the input contains the word `0 1 0` or `0 1111 0` followed by one more cell (`reset0`, `reset1`, `sync`): from the depth of that extra cell on, the runs agree.

Every phase of `C20` carries such words, and in two consecutive rows they are stacked in the right order. With the band's bits counted upward from the cut, the four phases give:

| Band of `F x` | Band of `F (F x)` | Word in `F (F x)` | Word in `F x` |
|---|---|---|---|
| 820683 | 911005 | `0 1 0` at bit 6 | `0 1 0` at bit 14 |
| 822904 | 912610 | `0 1 0` at bit 0 | `0 1 0` at bit 14 |
| 911005 | 822904 | `0 1111 0` at bit 2 | `0 1111 0` at bit 12 |
| 912610 | 820683 | `0 1 0` at bit 2 | `0 1111 0` at bit 12 |

Now invert `F (F x)` twice, flipping the cell beside the wall at the middle step and keeping it at the first. The flipped run differs from `F x` only below the word in `F (F x)`. The next run reads the word in `F x`, which lies above that, and forgets the difference. So the result agrees with `x` above the second word, and it is a finite row: the twin (`twin_of_factors`). It differs from `x`, because its image one tick on has the other cell beside the wall. Its width is that of `x`, because both reach the same row two ticks later.

At an even tick the twin keeps the cell beside the wall that `x` has, and from two ticks on it is `x`'s future, so immortality passes to it. It is off the orbit because the orbit has exactly one row of each width, and that row is `x`.

## 5. Worked numbers

The cell below recomputes both stage maxima, then takes seven rows, among them the long survivors `1493` and `11083`. For each it checks that the band of `iter F 45 y` is on `C20`, and that `iter F 44 y` has a twin of equal width, the same cell beside the wall and the same image two ticks on, found by inverting `F` twice.

```wl
R[u_] := BitXor[BitShiftRight[u, 2], BitOr[BitShiftRight[u, 1], u]];
F[y_] := BitXor[BitShiftRight[y], BitOr[y, BitShiftLeft[y]]];
c13 = {6411, 6428, 7117, 7129}; c20 = {820683, 822904, 911005, 912610};
entry[v0_, c_] := Module[{v = v0, t = 0}, While[! MemberQ[c, v], v = R[v]; t++]; t];
pre[z_, b_] := Module[{y = {b}}, Do[AppendTo[y, BitXor[BitGet[z, i], BitOr[y[[-1]], If[Length[y] >= 2, y[[-2]], 0]]]], {i, 0, BitLength[z] + 2}];
  If[y[[-1]] == 0 && y[[-2]] == 0, FromDigits[Reverse[y], 2], Missing[]]];
twins[x_] := Select[Table[With[{x1 = pre[F[F[x]], b1]}, If[MissingQ[x1], x1, pre[x1, BitGet[x, 0]]]], {b1, 0, 1}], IntegerQ[#] && # != x &];
check[y_] := With[{x = Nest[F, y, 44]}, With[{x45 = F[x], tw = twins[x]},
  {MemberQ[c20, BitShiftRight[x45, BitLength[x45] - 20]],
   Length[tw] >= 1 && AllTrue[tw, BitLength[#] == BitLength[x] && BitGet[#, 0] == BitGet[x, 0] && F[F[#]] == F[F[x]] &]}]];
{Max[entry[#, c13] & /@ Range[4096, 8191]], Max[Flatten[Table[entry[c 128 + b, c20], {c, c13}, {b, 0, 127}]]], check /@ {1, 3, 5, 7, 331, 1493, 11083}}
```

## 6. Prior art and scope

The reset words come from Feynman's theorem on predecessors: on a cyclic register, a configuration has exactly one predecessor under rule 30 if and only if some run of `1`s between consecutive `0`s has length `1` mod `3` (the kit's `Rule30Predecessors`, `predCount_eq_one_iff`, proved through the transfer map `T`). The words `0 1 0` and `0 1111 0` are such runs, read by the same map. Stacking such words across many rows gives the inverse-cascade staircase of Troy Lowry's kit pull request #60 (`scheduled_cascade_closes`), which assumes recurrent resets. What is new here is that every late row supplies them, from an explicit tick, in its own top. The kit's `Rule30PrefixMerger` gives a fixed seven-cell rewrite beside the wall that merges after two ticks for every tail, a twin for rows with that prefix. The settling of the top is a small explicit case of the left side's settling (`Rule30UniversalLeftSide`, `Rule30FourLeftSides`). The statement was found in the project's swarm and carried by hand in the [project's record](https://github.com/ghywel/placego/blob/main/PROOFS.md); this module is its formal proof.

Not formalized here: the larger family in the hand argument. On the four left strips through `87,866` wheels, checked reset chains reach `7,911` single-tick inverse levels; using `7,910` of them gives `2^3955` finite preimages under the even-time and survival guards in [the GC2690 carrying review](https://github.com/ghywel/placego/blob/main/reports/GPT-SW02-CARRY-REVIEW-20261106.md). Its uniform onset was not computed. The general reset schedule is not formalized either.

The twins have the same future as `x`. They raise the number of immortal rows, not the number of immortal futures, and they bound no death time. Nothing here proves `Q01`, and Problems 1 to 3 stay open.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30ZeroBoundary`, which holds the integer form of the wall dynamics and the backward transducer.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30ZeroBoundary

/-!
# Rule 30 beside a white wall: every late row has a twin

For every nonzero natural `y` and every `t ≥ 46`, the row `x = iter F (t - 2) y` of the
zero-boundary left half (`Rule30ZeroBoundary.IntegerForm`) has a **twin**: a natural `x' ≠ x` of
the same width, with the same cell at depth `1`, and with `F (F x') = F (F x)` (`late_twin`). If
`y` never reaches an even value under `G` and `t` is even, the twin never does either
(`late_twin_immortal`), and it is none of the rows `iter G j y` (`late_twin_off_orbit`). So one
immortal natural would force immortal naturals beyond its own orbit, at every even tick from `46` on.

**The top of a row is autonomous.** For every row `Y` and every cut `m`,
`F Y >>> (m + 1) = R (Y >>> m)` with `R u = (u >>> 2) ^^^ ((u >>> 1) ||| u)` (`F_shiftRight`,
`iter_F_shiftRight`). Rule 30 reads its left neighbour, so nothing below a cut reaches the cells above
it, and the cut moves out one cell per tick with the row's top.

**The top twenty cells settle.** From any start whose top cell is the twentieth, the top twenty cells
lie on one four-cycle `C20` after `26` ticks (`band_settles`); every row reaches width `20` by tick
`19`, so every row from tick `45` on has its band on `C20` (`band_late`). The kernel checks this in
two stages: all `4096` starts of the top thirteen cells reach the four-cycle `C13` in `14` ticks
(`stage13`), and from `C13` with any seven cells below, the top twenty reach `C20` in `12` more
(`stage20`). Some starts need all `26` ticks.

**Reset words.** The backward transducer `Rule30ZeroBoundary.back` forgets its starting state after
reading `0 1 0` or `0 1111 0` and one further bit (`reset0`, `reset1`): two runs reading the same
inputs from the start of such a word agree from the depth of that bit on (`sync`). In each phase of
`C20` the band carries one word in `F x` and one in `F (F x)`, stacked so that inverting twice with
the depth-`1` cell flipped one tick before gives a finitely supported row (`chains`,
`twin_of_factors`). Its width equals that of `x` because both have the same image two ticks later.

Nothing here bounds a death time or decides `Q01`. The immortal statements are conditional on an
immortal natural.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata Rule30ZeroBoundary Rule30ZeroBoundary.IntegerForm

/-! ### The top of a row is autonomous -/

/-- The cells above a cut, one tick later and one cell further out: rule 30 with nothing above. -/
def R (u : Nat) : Nat := (u >>> 2) ^^^ ((u >>> 1) ||| u)

/-- `t` steps of `R`. -/
def iterR : Nat → Nat → Nat
  | 0, u => u
  | n + 1, u => iterR n (R u)

/-- **The top moves out by one and updates by itself.** For every row `Y` and every cut `m`. -/
theorem F_shiftRight (Y m : Nat) : F Y >>> (m + 1) = R (Y >>> m) := by
  apply Nat.eq_of_testBit_eq
  intro i
  simp only [F, R, Nat.testBit_shiftRight, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft]
  rw [show 1 + (m + 1 + i) = m + (2 + i) by omega, show m + 1 + i - 1 = m + i by omega,
    show decide (m + 1 + i ≥ 1) = true from decide_eq_true (by omega),
    show m + 1 + i = m + (1 + i) by omega, Bool.true_and]

theorem R_shiftRight (u s : Nat) : R u >>> s = R (u >>> s) := by
  apply Nat.eq_of_testBit_eq
  intro i
  simp only [R, Nat.testBit_shiftRight, Nat.testBit_xor, Nat.testBit_or]
  have h1 : 2 + (s + i) = s + (2 + i) := by omega
  have h2 : 1 + (s + i) = s + (1 + i) := by omega
  rw [h1, h2]

theorem iterR_succ' (n u : Nat) : iterR (n + 1) u = R (iterR n u) := by
  induction n generalizing u with
  | zero => rfl
  | succ n ih => rw [iterR, ih (R u), iterR]

theorem iterR_add (a b u : Nat) : iterR (a + b) u = iterR b (iterR a u) := by
  induction a generalizing u with
  | zero => rw [Nat.zero_add]; rfl
  | succ a ih => rw [show a + 1 + b = (a + b) + 1 by omega, iterR, iterR, ih]

theorem iterR_shiftRight (n u s : Nat) : iterR n u >>> s = iterR n (u >>> s) := by
  induction n generalizing u with
  | zero => rfl
  | succ n ih => rw [iterR, iterR, ih, R_shiftRight]

/-- `t` ticks of the wall dynamics, read above a cut that moves out one cell per tick. -/
theorem iter_F_shiftRight (Y m : Nat) : ∀ t, iter F t Y >>> (m + t) = iterR t (Y >>> m)
  | 0 => rfl
  | t + 1 => by
      rw [show m + (t + 1) = (m + t) + 1 by omega, iter, F_shiftRight, iter_F_shiftRight Y m t,
        ← iterR_succ']

theorem R_lt {u n : Nat} (h : u < 2 ^ n) : R u < 2 ^ n := by
  apply Nat.lt_pow_two_of_testBit
  intro i hi
  have hb : ∀ j, n ≤ j → u.testBit j = false := fun j hj =>
    Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le h (Nat.pow_le_pow_right (by omega) hj))
  simp only [R, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftRight]
  rw [hb (2 + i) (by omega), hb (1 + i) (by omega), hb i hi]
  rfl

theorem iterR_lt {u n : Nat} (h : u < 2 ^ n) : ∀ t, iterR t u < 2 ^ n := by
  intro t
  induction t generalizing u with
  | zero => exact h
  | succ t ih => rw [iterR]; exact ih (R_lt h)

/-! ### The top twenty cells settle on one four-cycle within 26 ticks -/

/-- The four-cycle of the top thirteen cells. -/
def inC13 (v : Nat) : Bool := v == 6411 || v == 6428 || v == 7117 || v == 7129

/-- The four-cycle of the top twenty cells. -/
def inC20 (v : Nat) : Bool := v == 820683 || v == 822904 || v == 911005 || v == 912610

/-- Binary-split range check, so that the kernel never recurses deeply. -/
def chk (P : Nat → Bool) (lo : Nat) : Nat → Bool
  | 0 => P lo
  | d + 1 => chk P lo d && chk P (lo + 2 ^ d) d

theorem chk_sound (P : Nat → Bool) : ∀ (d lo : Nat), chk P lo d = true → ∀ i, i < 2 ^ d → P (lo + i) = true
  | 0, lo, h, i, hi => by
      have : i = 0 := by omega
      subst this; simpa [chk] using h
  | d + 1, lo, h, i, hi => by
      simp only [chk, Bool.and_eq_true] at h
      by_cases hl : i < 2 ^ d
      · exact chk_sound P d lo h.1 i hl
      · have := chk_sound P d (lo + 2 ^ d) h.2 (i - 2 ^ d) (by rw [Nat.pow_succ] at hi; omega)
        rwa [show lo + 2 ^ d + (i - 2 ^ d) = lo + i by omega] at this

/-- Stage one, exhaustive: every start of the top thirteen cells is on `C13` after 14 ticks. -/
theorem stage13 : chk (fun u => inC13 (iterR 14 u)) 4096 12 = true := by decide +kernel

/-- Stage two: from `C13` with any seven cells below, the top twenty are on `C20` after 12 ticks. -/
theorem stage20 : (chk (fun b => inC20 (iterR 12 (6411 * 128 + b))) 0 7 &&
    chk (fun b => inC20 (iterR 12 (6428 * 128 + b))) 0 7 &&
    chk (fun b => inC20 (iterR 12 (7117 * 128 + b))) 0 7 &&
    chk (fun b => inC20 (iterR 12 (7129 * 128 + b))) 0 7) = true := by decide +kernel

theorem C20_closed (v : Nat) (h : inC20 v = true) : inC20 (R v) = true := by
  simp only [inC20, Bool.or_eq_true, beq_iff_eq] at h
  rcases h with ((rfl | rfl) | rfl) | rfl <;> decide

theorem C20_iterR (v : Nat) (h : inC20 v = true) : ∀ t, inC20 (iterR t v) = true := by
  intro t
  induction t generalizing v with
  | zero => exact h
  | succ t ih => rw [iterR]; exact ih _ (C20_closed v h)

theorem C13_cases (v : Nat) (h : inC13 v = true) : v = 6411 ∨ v = 6428 ∨ v = 7117 ∨ v = 7129 := by
  simp only [inC13, Bool.or_eq_true, beq_iff_eq] at h
  omega

/-- **The top twenty cells settle.** From any start whose top cell is cell 20, after at least 26
ticks the top twenty cells lie on the four-cycle `C20`. -/
theorem band_settles {u : Nat} (h1 : 2 ^ 19 ≤ u) (h2 : u < 2 ^ 20) {t : Nat} (ht : 26 ≤ t) :
    inC20 (iterR t u) = true := by
  have hs13 : inC13 (iterR 14 (u >>> 7)) = true := by
    have hlo : 4096 ≤ u >>> 7 := by rw [Nat.shiftRight_eq_div_pow]; omega
    have hhi : u >>> 7 < 4096 + 2 ^ 12 := by rw [Nat.shiftRight_eq_div_pow]; omega
    have := chk_sound _ 12 4096 stage13 (u >>> 7 - 4096) (by omega)
    rwa [show 4096 + (u >>> 7 - 4096) = u >>> 7 by omega] at this
  obtain ⟨v, hv⟩ : ∃ v, v = iterR 14 u := ⟨_, rfl⟩
  have hvlt : v < 2 ^ 20 := hv ▸ iterR_lt h2 14
  have hc : inC13 (v >>> 7) = true := by rw [hv, iterR_shiftRight]; exact hs13
  have hsplit : v = (v >>> 7) * 128 + v % 128 := by
    rw [Nat.shiftRight_eq_div_pow]; omega
  have hb : v % 128 < 2 ^ 7 := Nat.mod_lt _ (by decide)
  have h26 : inC20 (iterR 12 v) = true := by
    have st := stage20
    simp only [Bool.and_eq_true] at st
    obtain ⟨⟨⟨s1, s2⟩, s3⟩, s4⟩ := st
    rw [hsplit]
    rcases C13_cases _ hc with h | h | h | h <;> rw [h]
    · simpa using chk_sound _ 7 0 s1 (v % 128) hb
    · simpa using chk_sound _ 7 0 s2 (v % 128) hb
    · simpa using chk_sound _ 7 0 s3 (v % 128) hb
    · simpa using chk_sound _ 7 0 s4 (v % 128) hb
  have : iterR t u = iterR (t - 26) (iterR 12 v) := by
    rw [hv, ← iterR_add, ← iterR_add]; congr 1; omega
  rw [this]; exact C20_iterR _ h26 _

/-! ### Widths and the band of a row -/

/-- `m` is the top bit of `Y`: the row has width `m + 1`. -/
def Top (Y m : Nat) : Prop := Y.testBit m = true ∧ ∀ i, m < i → Y.testBit i = false

theorem top_log2 {Y : Nat} (h : Y ≠ 0) : Top Y Y.log2 :=
  ⟨Nat.testBit_log2 h, fun i hi => Nat.testBit_lt_two_pow
    (Nat.lt_of_lt_of_le Nat.lt_log2_self (Nat.pow_le_pow_right (by omega) hi))⟩

theorem Top_F {Y m : Nat} (h : Top Y m) : Top (F Y) (m + 1) := by
  refine ⟨testBit_F_succ_of_top h.1 h.2, fun i hi => ?_⟩
  obtain ⟨j, rfl⟩ : ∃ j, i = j + 1 := ⟨i - 1, by omega⟩
  rw [testBit_F_succ, h.2 (j + 2) (by omega), h.2 (j + 1) (by omega), h.2 j (by omega)]
  rfl

theorem Top_iter {Y m : Nat} (h : Top Y m) : ∀ t, Top (iter F t Y) (m + t)
  | 0 => h
  | t + 1 => by
      rw [iter, show m + (t + 1) = (m + t) + 1 by omega]
      exact Top_F (Top_iter h t)

theorem Top_unique {Y m m' : Nat} (h : Top Y m) (h' : Top Y m') : m = m' := by
  rcases Nat.lt_trichotomy m m' with hl | he | hg
  · have := h.2 m' hl
    rw [h'.1] at this
    exact absurd this (by decide)
  · exact he
  · have := h'.2 m hg
    rw [h.1] at this
    exact absurd this (by decide)

theorem iter_add (f : Nat → Nat) (a b x : Nat) : iter f (a + b) x = iter f b (iter f a x) := by
  induction b with
  | zero => rfl
  | succ b ih => rw [show a + (b + 1) = (a + b) + 1 by omega, iter, iter, ih]

theorem band_bounds {X m : Nat} (h : Top X m) (hm : 19 ≤ m) :
    2 ^ 19 ≤ X >>> (m - 19) ∧ X >>> (m - 19) < 2 ^ 20 := by
  constructor
  · apply Nat.ge_two_pow_of_testBit
    rw [Nat.testBit_shiftRight, show m - 19 + 19 = m by omega]
    exact h.1
  · apply Nat.lt_pow_two_of_testBit
    intro i hi
    rw [Nat.testBit_shiftRight]
    exact h.2 _ (by omega)

/-- **Every late row's band is on `C20`.** For nonzero `y` and `t ≥ 45`, the top twenty cells of
`iter F t y` lie on the four-cycle. -/
theorem band_late {y : Nat} (hy : y ≠ 0) {t : Nat} (ht : 45 ≤ t) :
    inC20 (iter F t y >>> (y.log2 + t - 19)) = true := by
  have hT := top_log2 hy
  have hT0 := Top_iter hT (19 - y.log2)
  have hb := band_bounds hT0 (by omega)
  have hsplit : iter F t y = iter F (t - (19 - y.log2)) (iter F (19 - y.log2) y) := by
    rw [← iter_add]
    congr 1
    omega
  rw [hsplit, show y.log2 + t - 19 = (y.log2 + (19 - y.log2) - 19) + (t - (19 - y.log2)) by omega,
    iter_F_shiftRight]
  exact band_settles hb.1 hb.2 (by omega)

/-! ### Synchronization of the backward transducer (the reset words of G13) -/

theorem back_succ_succ (b : Bool) (y : Nat → Bool) (n : Nat) :
    back b y (n + 2) = xor (y (n + 1)) (back b y (n + 1) || back b y n) := rfl

/-- Two backward runs that agree at two consecutive depths, with equal inputs from there on, agree
from then on. -/
theorem back_agree_from {b b' : Bool} {y y' : Nat → Bool} {N : Nat}
    (hy : ∀ j, N ≤ j → y j = y' j)
    (h0 : back b y N = back b' y' N) (h1 : back b y (N + 1) = back b' y' (N + 1)) :
    ∀ n, N ≤ n → back b y n = back b' y' n := by
  have key : ∀ d, back b y (N + d) = back b' y' (N + d) ∧
      back b y (N + d + 1) = back b' y' (N + d + 1) := by
    intro d
    induction d with
    | zero => exact ⟨h0, h1⟩
    | succ d ih =>
      refine ⟨by rw [show N + (d + 1) = N + d + 1 by omega]; exact ih.2, ?_⟩
      rw [show N + (d + 1) + 1 = (N + d) + 2 by omega, back_succ_succ, back_succ_succ, ih.1, ih.2,
        hy (N + d + 1) (by omega)]
  intro n hn
  obtain ⟨d, rfl⟩ : ∃ d, n = N + d := ⟨n - N, by omega⟩
  exact (key d).1

/-- The reset word `0 1 0 z` read from input `q + 1` fixes the run from depth `q + 4`. -/
theorem reset0 (c : Bool) (z : Nat → Bool) (q : Nat)
    (g0 : z (q + 1) = false) (g1 : z (q + 2) = true) (g2 : z (q + 3) = false) :
    back c z (q + 4) = true ∧ back c z (q + 5) = !z (q + 4) := by
  have e4 : back c z (q + 4) = true := by
    simp only [back_succ_succ, g0, g1, g2]
    cases back c z (q + 1) <;> cases back c z q <;> rfl
  refine ⟨e4, ?_⟩
  rw [show q + 5 = (q + 3) + 2 by omega, back_succ_succ, show q + 3 + 1 = q + 4 from rfl, e4]
  cases z (q + 4) <;> rfl

/-- The reset word `0 1111 0 z` read from input `q + 1` fixes the run from depth `q + 7`. -/
theorem reset1 (c : Bool) (z : Nat → Bool) (q : Nat)
    (g0 : z (q + 1) = false) (g1 : z (q + 2) = true) (g2 : z (q + 3) = true)
    (g3 : z (q + 4) = true) (g4 : z (q + 5) = true) (g5 : z (q + 6) = false) :
    back c z (q + 7) = true ∧ back c z (q + 8) = !z (q + 7) := by
  have e7 : back c z (q + 7) = true := by
    simp only [back_succ_succ, g0, g1, g2, g3, g4, g5]
    cases back c z (q + 1) <;> cases back c z q <;> rfl
  refine ⟨e7, ?_⟩
  rw [show q + 8 = (q + 6) + 2 by omega, back_succ_succ, show q + 6 + 1 = q + 7 from rfl, e7]
  cases z (q + 7) <;> rfl

/-- The reset words: `0 1 0` (`k = 0`) and `0 1111 0` (`k = 1`), followed by a free bit. -/
def pat : Nat → Nat → Bool
  | 0, j => [false, true, false].getD j false
  | _, j => [false, true, true, true, true, false].getD j false

/-- A reset factor of `X` starting at bit `q`. -/
def Fac (X q k : Nat) : Prop := (k = 0 ∨ k = 1) ∧ ∀ j, j < 3 * k + 3 → X.testBit (q + j) = pat k j

/-- **G13's synchronization.** If two backward runs read inputs that agree from `q + 1` on, and
the second run's input carries a reset factor of `X` starting at bit `q`, the runs agree from depth
`q + 3k + 4`. -/
theorem sync {b b' : Bool} {y y' : Nat → Bool} {X q k : Nat} (hX : ∀ j, y' (j + 1) = X.testBit j)
    (hy : ∀ j, q + 1 ≤ j → y j = y' j) (hf : Fac X q k) :
    ∀ n, q + 3 * k + 4 ≤ n → back b y n = back b' y' n := by
  have v : ∀ j, j < 3 * k + 3 → y (q + j + 1) = pat k j ∧ y' (q + j + 1) = pat k j := by
    intro j hj
    have := hf.2 j hj
    rw [← hX] at this
    exact ⟨by rw [hy _ (by omega)]; exact this, this⟩
  rcases hf.1 with rfl | rfl
  · have g := fun j (hj : j < 3) => v j (by omega)
    have a := reset0 b y q (g 0 (by decide)).1 (g 1 (by decide)).1 (g 2 (by decide)).1
    have a' := reset0 b' y' q (g 0 (by decide)).2 (g 1 (by decide)).2 (g 2 (by decide)).2
    exact back_agree_from (N := q + 4) (fun j hj => hy j (by omega)) (by rw [a.1, a'.1])
      (by rw [a.2, a'.2, hy (q + 4) (by omega)])
  · have g := fun j (hj : j < 6) => v j (by omega)
    have a := reset1 b y q (g 0 (by decide)).1 (g 1 (by decide)).1 (g 2 (by decide)).1
      (g 3 (by decide)).1 (g 4 (by decide)).1 (g 5 (by decide)).1
    have a' := reset1 b' y' q (g 0 (by decide)).2 (g 1 (by decide)).2 (g 2 (by decide)).2
      (g 3 (by decide)).2 (g 4 (by decide)).2 (g 5 (by decide)).2
    exact back_agree_from (N := q + 7) (fun j hj => hy j (by omega)) (by rw [a.1, a'.1])
      (by rw [a.2, a'.2, hy (q + 7) (by omega)])

theorem fac_transfer {X C q i k : Nat} (hb : ∀ j, X.testBit (q + j) = C.testBit (i + j))
    (h : Fac C i k) : Fac X q k :=
  ⟨h.1, fun j hj => by rw [hb]; exact h.2 j hj⟩

/-! ### The twin -/

theorem rowOfNat_ext {A B : Nat} (h : ∀ k, rowOfNat A (k + 1) = rowOfNat B (k + 1)) : A = B :=
  Nat.eq_of_testBit_eq fun i => h i

theorem rowOfNat_eq_back (Y : Nat) : ∀ k, rowOfNat Y k = back (rowOfNat Y 1) (rowOfNat (F Y)) k := by
  intro k
  have := eq_back (L := rowOfNat Y) (y := rowOfNat (F Y)) (fun k _ => zrow_rowOfNat_one Y k) k
  rwa [zrow_zero_self (rfl : rowOfNat Y 0 = false)] at this

theorem rowOfNat_F_of_row {A : Nat} {L : Nat → Bool} (h : ∀ k, rowOfNat A k = L k) :
    ∀ k, rowOfNat (F A) k = zrow L 1 k := by
  intro k
  rw [← zrow_rowOfNat_one]
  have : rowOfNat A = L := funext h
  rw [this]

/-- **The twin from two reset factors.** If `F (F x)` has a reset factor at bit `q2` and `F x` one
at bit `q1`, with `q2 + 3 k2 + 4 ≤ q1 + 1`, then there is a natural `x' ≠ x` with the same bit 0
and `F (F x') = F (F x)`. -/
theorem twin_of_factors {x q1 k1 q2 k2 : Nat} (h2 : Fac (F (F x)) q2 k2) (h1 : Fac (F x) q1 k1)
    (hq : q2 + 3 * k2 + 4 ≤ q1 + 1) :
    ∃ x', x' ≠ x ∧ x'.testBit 0 = x.testBit 0 ∧ F (F x') = F (F x) := by
  have hx1 := rowOfNat_eq_back (F x)
  have hx0 := rowOfNat_eq_back x
  have s1 : ∀ n, q2 + 3 * k2 + 4 ≤ n →
      back (!(rowOfNat (F x) 1)) (rowOfNat (F (F x))) n = rowOfNat (F x) n := by
    intro n hn
    rw [hx1 n]
    exact sync (X := F (F x)) (fun _ => rfl) (fun _ _ => rfl) h2 n hn
  have s2 : ∀ n, q1 + 3 * k1 + 4 ≤ n →
      back (rowOfNat x 1) (back (!(rowOfNat (F x) 1)) (rowOfNat (F (F x)))) n = rowOfNat x n := by
    intro n hn
    rw [hx0 n]
    exact sync (X := F x) (fun _ => rfl) (fun j hj => s1 j (by omega)) h1 n hn
  let z0 := back (rowOfNat x 1) (back (!(rowOfNat (F x) 1)) (rowOfNat (F (F x))))
  let N := q1 + 3 * k1 + 4 + x.log2 + 2
  have hW : ∀ k, N < k → z0 k = false := by
    intro k hk
    show back (rowOfNat x 1) (back (!(rowOfNat (F x) 1)) (rowOfNat (F (F x)))) k = false
    rw [s2 k (by omega)]
    obtain ⟨j, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩
    exact Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le Nat.lt_log2_self (Nat.pow_le_pow_right (by omega) (by omega)))
  have hrow : ∀ k, rowOfNat (natOfRow z0 N) k = z0 k := by
    intro k
    rcases Nat.eq_zero_or_pos k with rfl | hk
    · rfl
    · exact rowOfNat_natOfRow hW k hk
  have hF1 : ∀ k, rowOfNat (F (natOfRow z0 N)) k =
      back (!(rowOfNat (F x) 1)) (rowOfNat (F (F x))) k := by
    intro k
    rw [rowOfNat_F_of_row hrow k]
    rcases Nat.eq_zero_or_pos k with rfl | hk
    · rfl
    · exact zrow_back _ _ k hk
  refine ⟨natOfRow z0 N, ?_, ?_, ?_⟩
  · intro he
    have h1 := hF1 1
    rw [he] at h1
    have key : ∀ b : Bool, b ≠ !b := by decide
    exact key _ h1
  · have := hrow 1
    exact this
  · apply rowOfNat_ext
    intro k
    rw [rowOfNat_F_of_row hF1 (k + 1)]
    exact zrow_back _ _ (k + 1) (by omega)

/-! ### Every late row has a twin -/

/-- The chain in each phase of `C20`, as (bit of the factor in `F x`, its word; bit in `F (F x)`,
its word) relative to the band. -/
theorem chains (c : Nat) (hc : inC20 c = true) :
    ∃ i1 k1 i2 k2, Fac c i1 k1 ∧ Fac (R c) i2 k2 ∧ i2 + 3 * k2 + 4 ≤ i1 := by
  simp only [inC20, Bool.or_eq_true, beq_iff_eq] at hc
  rcases hc with ((rfl | rfl) | rfl) | rfl
  · exact ⟨14, 0, 6, 0, ⟨Or.inl rfl, by decide⟩, ⟨Or.inl rfl, by decide⟩, by decide⟩
  · exact ⟨14, 0, 0, 0, ⟨Or.inl rfl, by decide⟩, ⟨Or.inl rfl, by decide⟩, by decide⟩
  · exact ⟨12, 1, 2, 1, ⟨Or.inr rfl, by decide⟩, ⟨Or.inr rfl, by decide⟩, by decide⟩
  · exact ⟨12, 1, 2, 0, ⟨Or.inr rfl, by decide⟩, ⟨Or.inl rfl, by decide⟩, by decide⟩

theorem F_zero : F 0 = 0 := by decide

/-- **Every late row has a twin.** For every nonzero natural `y` and every `t ≥ 46`, the row
`x = iter F (t - 2) y` has a twin `x' ≠ x` of the same width, with the same bit 0 and the same
image two ticks later. -/
theorem late_twin {y : Nat} (hy : y ≠ 0) {t : Nat} (ht : 46 ≤ t) :
    ∃ x', x' ≠ iter F (t - 2) y ∧ x'.testBit 0 = (iter F (t - 2) y).testBit 0 ∧
      F (F x') = iter F t y ∧ Top x' (y.log2 + (t - 2)) := by
  have e1 : iter F (t - 1) y = F (iter F (t - 2) y) := by
    rw [show t - 1 = (t - 2) + 1 by omega]; rfl
  have e2 : iter F t y = F (F (iter F (t - 2) y)) := by
    rw [← e1, show t = (t - 1) + 1 by omega]; rfl
  obtain ⟨c, hc⟩ : ∃ c, iter F (t - 1) y >>> (y.log2 + (t - 1) - 19) = c := ⟨_, rfl⟩
  have hin : inC20 c = true := hc ▸ band_late hy (by omega)
  obtain ⟨i1, k1, i2, k2, f1, f2, hi⟩ := chains c hin
  have b1 : ∀ j, (iter F (t - 1) y).testBit ((y.log2 + (t - 1) - 19) + i1 + j) = c.testBit (i1 + j) := by
    intro j
    rw [← hc, Nat.testBit_shiftRight, Nat.add_assoc]
  have b2 : ∀ j, (F (iter F (t - 1) y)).testBit ((y.log2 + (t - 1) - 19) + 1 + i2 + j) =
      (R c).testBit (i2 + j) := by
    intro j
    rw [← hc, ← F_shiftRight, Nat.testBit_shiftRight, Nat.add_assoc, Nat.add_assoc]
  have g1 := fac_transfer b1 f1
  have g2 := fac_transfer b2 f2
  rw [e1] at g1 g2
  obtain ⟨x', hne, hb0, hF⟩ := twin_of_factors g2 g1 (by omega)
  refine ⟨x', hne, hb0, by rw [hF, e2], ?_⟩
  have hx'0 : x' ≠ 0 := by
    intro h0
    have hT := Top_iter (top_log2 hy) t
    rw [e2, ← hF, h0, F_zero, F_zero] at hT
    exact absurd hT.1 (by rw [Nat.zero_testBit]; decide)
  have hT' := Top_iter (top_log2 hx'0) 2
  have hT2 := Top_iter (top_log2 hy) t
  rw [e2, ← hF] at hT2
  have : x'.log2 + 2 = y.log2 + t := Top_unique hT' hT2
  rw [show y.log2 + (t - 2) = x'.log2 by omega]
  exact top_log2 hx'0

theorem iter_succ' (f : Nat → Nat) (n x : Nat) : iter f (n + 1) x = iter f n (f x) := by
  rw [show n + 1 = 1 + n by omega, iter_add]
  rfl

theorem odd_iff_testBit (x : Nat) : x % 2 = 1 ↔ x.testBit 0 = true := by
  rw [Nat.testBit_zero]
  simp

/-- **Immortality passes to the twin at even ticks.** If `y` never reaches an even value under `G`
and `t ≥ 46` is even, the twin of `iter F (t - 2) y` never does either, and `G x' = iter F t y`. -/
theorem late_twin_immortal {y : Nat} (hy : ∀ s, iter G s y % 2 = 1) {t : Nat} (ht : 46 ≤ t)
    (he : t % 2 = 0) :
    ∃ x', x' ≠ iter F (t - 2) y ∧ (∀ s, iter G s x' % 2 = 1) ∧ G x' = iter F t y ∧
      Top x' (y.log2 + (t - 2)) := by
  have hy0 : y ≠ 0 := by
    intro h
    have := hy 0
    rw [h] at this
    exact absurd this (by decide)
  obtain ⟨x', hne, hb0, hF, hT⟩ := late_twin hy0 ht
  refine ⟨x', hne, ?_, hF, hT⟩
  intro s
  cases s with
  | zero =>
    have h := hy ((t - 2) / 2)
    rw [iter_G_eq_iter_F_two_mul, show 2 * ((t - 2) / 2) = t - 2 by omega] at h
    show x' % 2 = 1
    rw [odd_iff_testBit, hb0, ← odd_iff_testBit]
    exact h
  | succ s =>
    rw [iter_succ']
    have hG : G x' = iter G (t / 2) y := by
      rw [iter_G_eq_iter_F_two_mul, show 2 * (t / 2) = t by omega]
      exact hF
    rw [hG, ← iter_add]
    exact hy _

/-- **The twin is off the orbit.** Under the same hypotheses the twin is none of the rows
`iter G j y`. So one immortal natural forces immortal naturals beyond its own orbit, at every even
tick from 46 on. -/
theorem late_twin_off_orbit {y : Nat} (hy : ∀ s, iter G s y % 2 = 1) {t : Nat} (ht : 46 ≤ t)
    (he : t % 2 = 0) :
    ∃ x', (∀ s, iter G s x' % 2 = 1) ∧ G x' = iter F t y ∧ ∀ j, x' ≠ iter G j y := by
  obtain ⟨x', hne, himm, hG, hT⟩ := late_twin_immortal hy ht he
  refine ⟨x', himm, hG, fun j hj => ?_⟩
  have hy0 : y ≠ 0 := by
    intro h
    have := hy 0
    rw [h] at this
    exact absurd this (by decide)
  have hTj := Top_iter (top_log2 hy0) (2 * j)
  rw [← iter_G_eq_iter_F_two_mul, ← hj] at hTj
  have : y.log2 + (t - 2) = y.log2 + 2 * j := Top_unique hT hTj
  apply hne
  rw [hj, iter_G_eq_iter_F_two_mul, show 2 * j = t - 2 by omega]

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30ZeroBoundary.IntegerForm"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"F_shiftRight", "iter_F_shiftRight", "band_settles", "band_late", "sync", "twin_of_factors", "late_twin", "late_twin_immortal", "late_twin_off_orbit"};
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.late_twin"]["KernelCheck"]
```
