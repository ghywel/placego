---
Template: ComputationalEssay
Name: Every configuration of rule 30 with a leftmost black cell is on its strip by tick 177,575, through wheel 87,866
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-04
Description: An explicit tick in core Lean. Every configuration with a leftmost black cell carries one of four explicit strips on every left diagonal through wheel 87,866 from tick 177,560 + s of its own clock, with s at most 15, and the time of each wheel is given by a settling recursion evaluated by the kernel.
Abstract: Our entry R30-20261104-458f3b proved that every configuration of rule 30 with a leftmost black cell eventually agrees with one of four explicit strips on all left diagonals through wheel 87,866, after one time shift, but it gave no time. Here the time is explicit. Every such configuration carries its strip through wheel 87,866 from tick 177,560 + s of its own clock, with s at most 15, and through wheel 53,207 from tick 107,310 + s (forced_front_four_left_side, forced_front_low_left_side). forced_front_four gives the time wheel by wheel, as the settling recursion of the kit's Rule30FrontLaw run on each strip's sixteen-row cycle and carried through the classification. The time shift of 458f3b is now bounded by 15 (classification_bounded). The recursion is evaluated as a walk. From wheel j at tick t, move to wheel j + 1 if the strip's cell is black and stay if it is white. That is one addition, one shift and one mask per tick, and the kernel runs all four strips in seconds. The bound is not sharp, since the single black cell reaches its strip's exact row at tick 117,328. It is about an eighth of the linear bound 1 + 16 j at period 16, the form of the kit's frontBound_le_linear, which is 1,405,857 at that wheel. Nothing here concerns the center column or the Prize problems, and 87,866 is where these rows stop, not a claim about what happens beyond it.
Keywords: [rule 30, Rule 30 Prize, left diagonals, left side, settling time, forced front, Rowland, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "[Rowland, Local nested structure in rule 30](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261104-458f3b: exactly four left sides through wheel 87,866](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-458f3b)", "[R30-20261104-309041: one left side through wheel 53,207](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-309041)", "[R30-20261103-1c93e6: exact bounded whiteCount witnesses](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-1c93e6)"]
---

## 1. The claim

Our entry R30-20261104-458f3b proved that every configuration of rule 30 with a leftmost black cell, whatever lies to its right, eventually agrees with one of four explicit strips on all left diagonals through wheel 87,866, after one time shift. It gave no time. Here the time is explicit.

**Theorem (`forced_front_four_left_side`).** Let `x` be a configuration with a leftmost black cell. There are a shift `s ≤ 15` and a strip `v` among `A0`, `A1`, `B0`, `B1` such that wheel `j` of `x` at tick `t + s` equals wheel `j` of `v` at tick `t`, for every wheel `j ≤ 87,866` and every tick `t ≥ 177,560`.

So from tick 177,575 of its own clock at the latest, every such configuration carries one of the four strips on all of its first 87,867 wheels.

**Below the first fork (`forced_front_low_left_side`).** The same holds with wheel 53,207 and tick 107,310 in place of 87,866 and 177,560. The strip there is `A0`, because the four strips agree below wheel 53,208.

**Wheel by wheel (`forced_front_four`).** Each wheel has its own time. Wheel `j` is on the strip `v` from strip tick `F_v(j)`, the settling recursion of section 2, and this holds for every array with the left-diagonal recurrence and a black start. At wheel 87,866 the four fronts are as follows.

| strip | `F_v(87,866)` | Lean |
|---|---|---|
| `A0` | 176,968 | `FA0_87866` |
| `A1` | 177,229 | `FA1_87866` |
| `B0` | 177,170 | `FB0_87866` |
| `B1` | 177,560 | `FB1_87866` |

`forced_front_four_seed` is the single black cell. `classification_bounded` is the classification of 458f3b with its time shift bounded by 15, which 458f3b did not bound.

## 2. The settling recursion

The wheels are those of 458f3b. `Ld x lo j t` is the left diagonal `j` from the leftmost black cell `lo`, and the recurrence is `Ld (j + 2) (t + 1) = Ld j t ⊕ (Ld (j + 1) t ∨ Ld (j + 2) t)`. Each strip returns after 16 ticks, so wheel `j` of a strip is a word of sixteen bits.

Put `F_v(0) = 0` and `F_v(1) = 1`. Then `F_v(j + 2)` is defined from `m = max(F_v(j), F_v(j + 1))`.

- If wheel `j + 1` is white on the strip, `F_v(j + 2) = m`.
- Otherwise `F_v(j + 2)` is one more than the first tick at or after `m` at which wheel `j + 1` is black on the strip.

This is the recursion `frontBound` of the kit's `Rule30FrontLaw`, read on a strip's cycle instead of on the seed's history. It is non-decreasing (`F_mono`).

## 3. Why it bounds every configuration

The two moves of 458f3b, with the time carried.

**A black nearer wheel (`step_black`).** Suppose wheels `j` and `j + 1` of an array are aligned with the strip from strip tick `m`, and wheel `j + 1` is black at a tick `u ≥ m`. At the next tick both children take the complement of the same farther bit (`child_same`). They then have identical inputs, so the child is aligned from tick `u + 1`.

**A white nearer wheel (`step_white`).** If wheel `j + 1` is white on the strip, both children integrate the same farther word from tick `m` on, so their difference is constant from `m` (`child_white`). If it is zero, the child is aligned from `m`. If it is one, the array carries the complement of the strip's word. At a doubling wheel the complement is a time shift by the lower period (`white_shift`). At a fork it is the other strip's word (`white_fork`).

Below the first fork there are four doubling wheels, at 2, 7, 28 and 399, with shifts of 1, 2, 4 and 8, so the total shift is at most 15 (`low_from`). The white wheels 53,207, 58,286 and 72,575 are the forks, and they change the strip and not the shift. Two strips agree below their fork, so their recursions agree through it (`F_congr`). That is the proof of `forced_front_four`. The uniform statements follow because `F_v` is monotone and its largest value at wheel 87,866 is 177,560.

## 4. The recursion as a walk

A strip has 87,867 wheels, and the recursion has to be evaluated on all of them. Because `F_v` is monotone, it can be read another way. Put a pointer on a wheel `j` at a tick `t`. At each tick, move the pointer to the next wheel if the strip's cell at wheel `j` and tick `t` is black, and leave it if the cell is white. With `R_0, …, R_15` the strip's rows, that is

`j ← j + ((R_(t mod 16) >> j) & 1)`.

On a run of black wheels the pointer reaches wheel `j + 1` exactly at tick `F_v(j + 1)` (`run_arrival`). A wheel is reached at one tick only (`arrival_unique`), and a wheel the pointer has passed is black (`walk_black`). So four facts about the walk fix the recursion's state after a run of wheels (`frun_of_walk`). There are no branches in this step, and since the tick advances every time, sixteen ticks are one fixed expression in the sixteen rows (`st16`, `w16`).

A white wheel would hold the pointer for ever. Each strip has at most seven of them. The four lowest lie in the first 400 wheels, which the kernel evaluates directly, and the others are stepped over one at a time (`frun_white`). The strips share their wheels below the forks, so the four runs together take about 338,000 ticks.

The whole module, including the part repeated from 458f3b, builds in about seven seconds on a laptop. We first evaluated the same recursion wheel by wheel, on sixteen literal rows per strip, in four kernel modules of about seventy seconds each. Both evaluations give the four numbers of section 1.

## 5. A computation

The next two cells replay this in Wolfram Language, outside Lean, on the seed's row `A0`. The first runs the recursion and prints `F(53,207)` and `F(87,866)`. Its running value `t` stands for `max(F(j − 1), F(j))`, because `F` is monotone (`F_mono`), so the cell is the walk. It also prints the digest of the computed row, which should be that of the literal `A0` in the source, `0dc9e1db3e968ceb8e12cac61d61ca1f7fd6b749422681ae53d5f842b64d1e3c`. The second cell sets the bound beside what the single black cell actually does.

```wl
K = 87867; mask = 2^K - 1;
step[v_] := BitAnd[BitXor[BitShiftLeft[v, 2], BitOr[BitShiftLeft[v, 1], v]], mask];
A = Nest[step, 1, 128000];
bits = Reverse[IntegerDigits[#, 2, K]] & /@ NestList[step, A, 15];
black = Total[bits];
t = 1;
F = Join[{0, 1}, Table[If[black[[j + 1]] > 0, While[bits[[Mod[t, 16] + 1, j + 1]] == 0, t++]; t++]; t, {j, 1, 87865}]];
{Nest[step, A, 16] == A, F[[53208]], F[[87867]], Hash[IntegerString[A, 16], "SHA256", "HexString"]}
```

```wl
reach[v_] := Module[{x = v, n = 0}, While[x != A && n < 128000, x = step[x]; n++]; n];
Grid[{{"F(87,866) on A0", F[[87867]]}, {"first tick at which the single black cell equals A0", reach[1]}}, Frame -> All]
```

## 6. What this does and does not say

**The bound is not sharp.** The single black cell reaches the exact row `A0` at tick 117,328, and the bound for its strip is 176,968. The recursion grows by about two ticks per wheel, while the seed's actual front grows by about four ticks per three wheels. The recursion counts only the resets the proof can see, and a wheel can fall into its cycle earlier by coincidence. These growth rates are computed, not proved.

**Against the general bound.** Each wheel waits at most sixteen ticks, so the same recursion has the linear bound `1 + 16 j`. That is the form of the kit's `frontBound_le_linear` at period 16, a lemma about the recursion on the seed's own history. At wheel 87,866 it is 1,405,857, about eight times the evaluated front.

**Beyond the cut.** 87,866 is where these rows stop. The moves take any strip given by a row with a 16-tick return, so the next fork would need new rows and no new proof.

**Scope.** Nothing here concerns the center column or the Prize problems.

## 7. Credits

The recursion and the linear bound are the kit's `Rule30FrontLaw`, contributed by @AIOvernight with OpenAI Codex and Claude, and R30-20261103-1c93e6 (Quint and Gemini). R30-20261103-050b68 (Quint and Gemini) evaluates the same recursion at small depths on the seed, and R30-20261027-e324b6 (@AIOvernight, with Claude and OpenAI Codex) uses settling times as barriers for center runs. The induction is Rowland's (2006, section 5), and the strips are those of R30-20261104-309041 and R30-20261104-458f3b.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30AgedLeftDiagonals`, which brings `Rule30FiniteDiagonals`, `Rule30Diagonals` and `Rule30Realization`. Its first part repeats the module of R30-20261104-458f3b, because the verifier's kit does not hold that module. The rest is the recursion, the moves with the time carried, the walk and the numbers. Every number in sections 1 and 4 is checked by the kernel, and nothing is taken from the computation above.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30AgedLeftDiagonals

/-!
# The forced front of rule 30 on the four left strips: an explicit tick for every configuration with a leftmost black cell

R30-20261104-458f3b placed every configuration with a leftmost black cell on one of four strips through wheel 87,866, after a time
shift and from some time on. Here the time is explicit. Every such configuration is on its strip through wheel 87,866 from tick
177,560 + s of its own clock, with s at most 15 (`forced_front_four_left_side`), and through wheel 53,207 from tick 107,310 + s
(`forced_front_low_left_side`). `forced_front_four` gives the time wheel by wheel: the settling recursion of the kit's `Rule30FrontLaw`,
run on each strip's sixteen-row cycle. `classification_bounded` is the classification of 458f3b with its shift bounded by 15.

The recursion is evaluated as a walk. From wheel `j` at tick `t`, move to wheel `j + 1` if the strip's cell is black and stay if it is
white, the tick moving on either way (`walk`, `frun_of_walk`). That is one addition, one shift and one mask per tick, so the kernel
runs all four strips in seconds. The first part of this module repeats 458f3b, because the verifier's kit does not hold it. Nothing
here concerns the center column or the Prize problems, and 87,866 is where these rows stop, not a claim about what happens beyond it.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

set_option autoImplicit false

open Rule30AgedLeftDiagonals Rule30FiniteDiagonals Rule30Diagonals Rule30Realization

/-! ### The induction on the wheel -/

theorem rec_zero {a : Nat → Nat → Bool} (ha : Recurrence a) (h : a 0 0 = true) : ∀ t, a 0 t = true := by
  intro t
  induction t with
  | zero => exact h
  | succ t ih => rw [ha.1, ih]

theorem rec_one {a : Nat → Nat → Bool} (ha : Recurrence a) (h : a 0 0 = true) (t : Nat) : a 1 (t + 1) = true := by
  rw [ha.2.1, rec_zero ha h t]
  rfl

theorem child_same {a C : Nat → Nat → Bool} {k s T r : Nat} (ha : Recurrence a)
    (hC : ∀ t, C (k + 2) (t + 1) = xor (C k t) (C (k + 1) t || C (k + 2) t))
    (hk : ∀ t, T ≤ t → a k (t + s) = C k t) (hk1 : ∀ t, T ≤ t → a (k + 1) (t + s) = C (k + 1) t)
    (hr : T ≤ r) (hb : C (k + 1) r = true) :
    ∀ t, r + 1 ≤ t → a (k + 2) (t + s) = C (k + 2) t := by
  intro t ht
  obtain ⟨n, rfl⟩ : ∃ n, t = r + 1 + n := ⟨t - (r + 1), by omega⟩
  clear ht
  induction n with
  | zero =>
    have e : r + 1 + 0 + s = (r + s) + 1 := by omega
    rw [e, ha.2.2, hk r hr, hk1 r hr, hb, show r + 1 + 0 = r + 1 from rfl, hC, hb]
    rfl
  | succ n ih =>
    have e : r + 1 + (n + 1) + s = (r + 1 + n + s) + 1 := by omega
    have e2 : r + 1 + (n + 1) = (r + 1 + n) + 1 := by omega
    rw [e, ha.2.2, hk _ (by omega), hk1 _ (by omega), ih, e2, hC]

theorem child_white {a C : Nat → Nat → Bool} {k s T : Nat} (ha : Recurrence a)
    (hC : ∀ t, C (k + 2) (t + 1) = xor (C k t) (C (k + 1) t || C (k + 2) t))
    (hk : ∀ t, T ≤ t → a k (t + s) = C k t) (hk1 : ∀ t, T ≤ t → a (k + 1) (t + s) = C (k + 1) t)
    (hw : ∀ t, T ≤ t → C (k + 1) t = false) :
    (∀ t, T ≤ t → a (k + 2) (t + s) = C (k + 2) t) ∨
      (∀ t, T ≤ t → a (k + 2) (t + s) = !C (k + 2) t) := by
  have hstep : ∀ t, T ≤ t →
      xor (a (k + 2) (t + 1 + s)) (C (k + 2) (t + 1)) = xor (a (k + 2) (t + s)) (C (k + 2) t) := by
    intro t ht
    rw [show t + 1 + s = (t + s) + 1 by omega, ha.2.2, hk t ht, hk1 t ht, hC, hw t ht]
    cases C k t <;> cases a (k + 2) (t + s) <;> cases C (k + 2) t <;> rfl
  have hconst : ∀ n, xor (a (k + 2) (T + n + s)) (C (k + 2) (T + n)) =
      xor (a (k + 2) (T + s)) (C (k + 2) T) := by
    intro n
    induction n with
    | zero => rfl
    | succ n ih => rw [← ih, ← hstep (T + n) (by omega)]; rfl
  cases hT : xor (a (k + 2) (T + s)) (C (k + 2) T) with
  | false =>
    left
    intro t ht
    obtain ⟨n, rfl⟩ : ∃ n, t = T + n := ⟨t - T, by omega⟩
    have := hconst n
    rw [hT] at this
    cases h1 : a (k + 2) (T + n + s) <;> cases h2 : C (k + 2) (T + n) <;> simp_all
  | true =>
    right
    intro t ht
    obtain ⟨n, rfl⟩ : ∃ n, t = T + n := ⟨t - T, by omega⟩
    have := hconst n
    rw [hT] at this
    cases h1 : a (k + 2) (T + n + s) <;> cases h2 : C (k + 2) (T + n) <;> simp_all

theorem universal_of_strip {a C : Nat → Nat → Bool} {J : Nat} (hJ : 1 ≤ J) (ha : Recurrence a)
    (ha0 : a 0 0 = true) (h0 : ∀ t, C 0 t = true) (h1 : ∀ t, C 1 t = true)
    (hC : ∀ j t, j + 2 ≤ J → C (j + 2) (t + 1) = xor (C j t) (C (j + 1) t || C (j + 2) t))
    (hstep : ∀ m, m + 1 ≤ J → (∀ T, ∃ t, T ≤ t ∧ C m t = true) ∨
      ∃ L, (∀ j, j ≤ m → ∀ t, C j (t + L) = C j t) ∧ ∀ t, C (m + 1) (t + L) = !C (m + 1) t) :
    ∃ s, ∀ j, j ≤ J → ∃ T, ∀ t, T ≤ t → a j (t + s) = C j t := by
  have hmain : ∀ m, m + 1 ≤ J → ∃ s, ∀ j, j ≤ m + 1 → ∃ T, ∀ t, T ≤ t → a j (t + s) = C j t := by
    intro m
    induction m with
    | zero =>
      intro _
      refine ⟨0, fun j hj => ⟨1, fun t ht => ?_⟩⟩
      have hj' : j = 0 ∨ j = 1 := by omega
      rcases hj' with rfl | rfl
      · rw [rec_zero ha ha0, h0]
      · obtain ⟨u, rfl⟩ : ∃ u, t = u + 1 := ⟨t - 1, by omega⟩
        rw [Nat.add_zero, rec_one ha ha0, h1]
    | succ m ih =>
      intro hm
      obtain ⟨s, hs⟩ := ih (by omega)
      obtain ⟨T1, hT1⟩ := hs m (by omega)
      obtain ⟨T2, hT2⟩ := hs (m + 1) (by omega)
      have hCm : ∀ t, C (m + 2) (t + 1) = xor (C m t) (C (m + 1) t || C (m + 2) t) :=
        fun t => hC m t (by omega)
      by_cases hb : ∀ T, ∃ t, T ≤ t ∧ C (m + 1) t = true
      · obtain ⟨r, hr, hbr⟩ := hb (max T1 T2)
        have hnew := child_same (s := s) (T := max T1 T2) ha hCm
          (fun t ht => hT1 t (by omega)) (fun t ht => hT2 t (by omega)) hr hbr
        refine ⟨s, fun j hj => ?_⟩
        by_cases hjm : j ≤ m + 1
        · exact hs j hjm
        · have e : j = m + 2 := by omega
          subst e
          exact ⟨r + 1, hnew⟩
      · obtain ⟨T0, hT0⟩ := Classical.not_forall.mp hb
        have hw : ∀ t, T0 ≤ t → C (m + 1) t = false := by
          intro t ht
          cases e : C (m + 1) t with
          | false => rfl
          | true => exact absurd ⟨t, ht, e⟩ hT0
        rcases hstep (m + 1) hm with hb' | ⟨L, hper, hanti⟩
        · exact absurd hb' hb
        · have hT : ∀ t, max (max T1 T2) T0 ≤ t → T1 ≤ t ∧ T2 ≤ t ∧ T0 ≤ t := by
            intro t ht
            omega
          rcases child_white (s := s) (T := max (max T1 T2) T0) ha hCm
            (fun t ht => hT1 t (hT t ht).1) (fun t ht => hT2 t (hT t ht).2.1)
            (fun t ht => hw t (hT t ht).2.2) with same | flip
          · refine ⟨s, fun j hj => ?_⟩
            by_cases hjm : j ≤ m + 1
            · exact hs j hjm
            · have e : j = m + 2 := by omega
              subst e
              exact ⟨_, same⟩
          · refine ⟨s + L, fun j hj => ?_⟩
            by_cases hjm : j ≤ m + 1
            · obtain ⟨T, hT'⟩ := hs j hjm
              refine ⟨T, fun t ht => ?_⟩
              rw [show t + (s + L) = (t + L) + s by omega, hT' (t + L) (by omega), hper j hjm]
            · have e : j = m + 2 := by omega
              subst e
              refine ⟨max (max T1 T2) T0, fun t ht => ?_⟩
              rw [show t + (s + L) = (t + L) + s by omega, flip (t + L) (by omega), hanti]
              cases C (m + 1 + 1) t <;> rfl
  obtain ⟨s, hs⟩ := hmain (J - 1) (by omega)
  exact ⟨s, fun j hj => hs j (by omega)⟩

/-! ### Rows as numbers -/

/-- One update of the first `K` left diagonals, as a `K`-bit number (`v`'s bit `j` is diagonal `j`). -/
def stepK (K v : Nat) : Nat := ((v <<< 2) ^^^ ((v <<< 1) ||| v)) % 2 ^ K

/-- The row `t` ticks after `v`. -/
def rowAt (K v : Nat) : Nat → Nat
  | 0 => v
  | t + 1 => stepK K (rowAt K v t)

theorem stepK_bit_zero {K : Nat} (hK : 0 < K) (v : Nat) : (stepK K v).testBit 0 = v.testBit 0 := by
  simp [stepK, hK]

theorem stepK_bit_one {K : Nat} (hK : 1 < K) (v : Nat) :
    (stepK K v).testBit 1 = (v.testBit 0 || v.testBit 1) := by
  simp [stepK, Nat.testBit_mod_two_pow, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft, hK]

theorem stepK_bit_step {K j : Nat} (hj : j + 2 < K) (v : Nat) :
    (stepK K v).testBit (j + 2) = xor (v.testBit j) (v.testBit (j + 1) || v.testBit (j + 2)) := by
  simp [stepK, Nat.testBit_mod_two_pow, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft, hj]

theorem rowAt_add_period {K v P : Nat} (hP : rowAt K v P = v) (t : Nat) :
    rowAt K v (t + P) = rowAt K v t := by
  induction t with
  | zero => simpa [rowAt] using hP
  | succ t ih =>
    rw [show t + 1 + P = (t + P) + 1 by omega]
    simp only [rowAt]
    rw [ih]

theorem rowAt_add_mul {K v P : Nat} (hP : rowAt K v P = v) (t q : Nat) :
    rowAt K v (t + q * P) = rowAt K v t := by
  induction q with
  | zero => simp
  | succ q ih =>
    rw [Nat.succ_mul, show t + (q * P + P) = (t + q * P) + P by omega, rowAt_add_period hP, ih]

/-- The configuration of a row: bit `p` at position `p ≥ 0`, white on the left. -/
def ofRow (v : Nat) (p : Int) : Bool := if p < 0 then false else v.testBit p.toNat

theorem ofRow_left (v : Nat) : ∀ p, p < 0 → ofRow v p = false := by
  intro p hp
  simp [ofRow, hp]

/-- The left diagonals of a row, read off the number. -/
theorem Ld_ofRow {K : Nat} (hK : 1 < K) (v : Nat) (t : Nat) :
    ∀ j, j < K → Ld (ofRow v) 0 j t = (rowAt K v t).testBit j := by
  have hrec := Ld_recurrence (x := ofRow v) (anchor := 0) (ofRow_left v)
  induction t with
  | zero =>
    intro j _
    simp [Ld, evol, ofRow, rowAt]
  | succ t ih =>
    intro j hj
    cases j with
    | zero =>
      rw [hrec.1, ih 0 (by omega)]
      simp only [rowAt]
      rw [stepK_bit_zero (by omega)]
    | succ j =>
      cases j with
      | zero =>
        rw [hrec.2.1, ih 0 (by omega), ih 1 (by omega)]
        simp only [rowAt]
        rw [stepK_bit_one (by omega)]
      | succ j =>
        rw [hrec.2.2, ih j (by omega), ih (j + 1) (by omega), ih (j + 2) (by omega)]
        simp only [rowAt]
        rw [stepK_bit_step (by omega)]

/-! ### Strips of rows -/

/-- Wheel `j` of the row `v` at tick `t`, on 87,867 wheels. -/
def Sp (v j t : Nat) : Bool := (rowAt 87867 v t).testBit j

theorem Sp_add_mul {v : Nat} (hv : rowAt 87867 v 16 = v) (j t q : Nat) : Sp v j (t + q * 16) = Sp v j t := by
  simp only [Sp]
  rw [rowAt_add_mul hv]

theorem Sp_mod {v : Nat} (hv : rowAt 87867 v 16 = v) (j t : Nat) : Sp v j t = Sp v j (t % 16) := by
  have h := Sp_add_mul hv j (t % 16) (t / 16)
  rw [show t % 16 + t / 16 * 16 = t by omega] at h
  exact h

theorem Sp_rec (v j t : Nat) (hj : j + 2 < 87867) :
    Sp v (j + 2) (t + 1) = xor (Sp v j t) (Sp v (j + 1) t || Sp v (j + 2) t) := by
  simp only [Sp, rowAt]
  rw [stepK_bit_step hj]

/-- The OR of the first `n` rows of `v`'s cycle. -/
def orRows (v : Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => orRows v n ||| rowAt 87867 v n

theorem orRows_black {v n m : Nat} (h : (orRows v n).testBit m = true) : ∃ r, r < n ∧ Sp v m r = true := by
  induction n with
  | zero => simp [orRows] at h
  | succ n ih =>
    simp only [orRows, Nat.testBit_or, Bool.or_eq_true] at h
    rcases h with h | h
    · obtain ⟨r, hr, hc⟩ := ih h
      exact ⟨r, by omega, hc⟩
    · exact ⟨n, by omega, h⟩

theorem blacks_late {v m r : Nat} (hv : rowAt 87867 v 16 = v) (hc : Sp v m r = true) (T : Nat) :
    ∃ t, T ≤ t ∧ Sp v m t = true :=
  ⟨r + T * 16, by omega, by rw [Sp_add_mul hv]; exact hc⟩

/-- Every wheel in a window has a black at some phase, from one kernel evaluation. -/
theorem black_window {v lo n m : Nat} (hv : rowAt 87867 v 16 = v)
    (h : (orRows v 16 >>> lo) % 2 ^ n = 2 ^ n - 1) (h1 : lo ≤ m) (h2 : m < lo + n) (T : Nat) :
    ∃ t, T ≤ t ∧ Sp v m t = true := by
  have hl : m - lo < n := by omega
  have e := congrArg (fun y => y.testBit (m - lo)) h
  simp only [Nat.testBit_mod_two_pow, Nat.testBit_two_pow_sub_one, Nat.testBit_shiftRight, hl,
    decide_true, Bool.true_and, show lo + (m - lo) = m by omega] at e
  obtain ⟨r, _, hc⟩ := orRows_black e
  exact blacks_late hv hc T

theorem low_of_phase {v v' n : Nat} (hv : rowAt 87867 v 16 = v) (hv' : rowAt 87867 v' 16 = v')
    (h : ∀ r, r < 16 → rowAt 87867 v' r % 2 ^ n = rowAt 87867 v r % 2 ^ n) (j t : Nat) (hj : j < n) :
    Sp v' j t = Sp v j t := by
  have e := congrArg (fun y => y.testBit j) (h (t % 16) (Nat.mod_lt _ (by omega)))
  simp only [Nat.testBit_mod_two_pow, hj, decide_true, Bool.true_and] at e
  rw [Sp_mod hv', Sp_mod hv j t]
  exact e

theorem comp_of_phase {v v' w : Nat} (hv : rowAt 87867 v 16 = v) (hv' : rowAt 87867 v' 16 = v')
    (h : ∀ r, r < 16 → Sp v' w r = !Sp v w r) (t : Nat) : Sp v' w t = !Sp v w t := by
  rw [Sp_mod hv', Sp_mod hv w t]
  exact h _ (Nat.mod_lt _ (by omega))

theorem white_of_phase {v w : Nat} (hv : rowAt 87867 v 16 = v) (h : ∀ r, r < 16 → Sp v w r = false)
    (t : Nat) : Sp v w t = false := by
  rw [Sp_mod hv]
  exact h _ (Nat.mod_lt _ (by omega))

/-! ### Alignment, and the two moves up the tree -/

/-- The array `a` carries the strip of `v` on every wheel through `J`, after the shift `s`. -/
def Aligned (a : Nat → Nat → Bool) (v s J : Nat) : Prop :=
  ∀ j, j ≤ J → ∃ T, ∀ t, T ≤ t → a j (t + s) = Sp v j t

/-- **Going up without a fork.** While each nearer wheel has blacks arbitrarily late, the alignment extends with the same shift. -/
theorem extend {a : Nat → Nat → Bool} {v s j0 J : Nat} (ha : Recurrence a) (h1 : 1 ≤ j0) (hJ : J ≤ 87866)
    (hal : Aligned a v s j0) (hj : j0 ≤ J)
    (hb : ∀ m, j0 ≤ m → m < J → ∀ T, ∃ t, T ≤ t ∧ Sp v m t = true) : Aligned a v s J := by
  have aux : ∀ n, j0 + n ≤ J → Aligned a v s (j0 + n) := by
    intro n
    induction n with
    | zero => intro _; exact hal
    | succ n ih =>
      intro hn
      have hp := ih (by omega)
      obtain ⟨k, hk⟩ : ∃ k, j0 + n = k + 1 := ⟨j0 + n - 1, by omega⟩
      rw [hk] at hp
      obtain ⟨T1, hT1⟩ := hp k (by omega)
      obtain ⟨T2, hT2⟩ := hp (k + 1) (by omega)
      obtain ⟨r, hr, hbr⟩ := hb (k + 1) (by omega) (by omega) (max T1 T2)
      have hnew := child_same (k := k) (s := s) (T := max T1 T2) ha
        (fun t => Sp_rec v k t (by omega)) (fun t ht => hT1 t (by omega))
        (fun t ht => hT2 t (by omega)) hr hbr
      intro j hj'
      by_cases hc : j ≤ k + 1
      · exact hp j hc
      · have e : j = k + 2 := by omega
        subst e
        exact ⟨r + 1, hnew⟩
  have h := aux (J - j0) (by omega)
  rwa [show j0 + (J - j0) = J by omega] at h

/-- **A fork.** At a white wheel `w`, the child is either `v`'s word or the word of `v'`, which agrees with `v` below it and
is `v`'s complement on the child. -/
theorem branch {a : Nat → Nat → Bool} {v v' s w : Nat} (ha : Recurrence a) (h1 : 1 ≤ w) (hw : w + 1 ≤ 87866)
    (hal : Aligned a v s w) (hwhite : ∀ t, Sp v w t = false)
    (hlow : ∀ j t, j ≤ w → Sp v' j t = Sp v j t) (hcomp : ∀ t, Sp v' (w + 1) t = !Sp v (w + 1) t) :
    Aligned a v s (w + 1) ∨ Aligned a v' s (w + 1) := by
  obtain ⟨k, rfl⟩ : ∃ k, w = k + 1 := ⟨w - 1, by omega⟩
  obtain ⟨T1, hT1⟩ := hal k (by omega)
  obtain ⟨T2, hT2⟩ := hal (k + 1) (by omega)
  rcases child_white (k := k) (s := s) (T := max T1 T2) ha (fun t => Sp_rec v k t (by omega))
    (fun t ht => hT1 t (by omega)) (fun t ht => hT2 t (by omega)) (fun t _ => hwhite t) with h | h
  · left
    intro j hj
    by_cases hc : j ≤ k + 1
    · exact hal j hc
    · have e : j = k + 2 := by omega
      subst e
      exact ⟨_, h⟩
  · right
    intro j hj
    by_cases hc : j ≤ k + 1
    · obtain ⟨T, hT⟩ := hal j hc
      exact ⟨T, fun t ht => by rw [hT t ht, hlow j t hc]⟩
    · have e : j = k + 2 := by omega
      subst e
      exact ⟨max T1 T2, fun t ht => by rw [h t ht, hcomp t]⟩

/-! ### The four rows -/

/-- The first row: 87,867 wheels at one phase. -/
def A0 : Nat := 0x800a82a6f08458c8c868ca181267587ba5ff3988b87f3dbe1fd3d51de78808f997681801fa91b0aaf8ab9ce6d487db0e21de08b33f384a82c363b12ec3d791bba8400838c1a5495001ffea3fa497ff00efdd0735a1b3a6e55a1c2ba3213992952479f5fe1688ca6fa7b4fbd9abeaf9269f1ba089d9faf2624751e6e2d37c5c4b9bc3b23498f4736e0feef8cb157e3d4fadb4025d489aca0a635a8885526a6345fcf0fdf46d576f4b8b7ca025afeb2577c6c28260dc597f55ce7af207b0181e0ae87401359ded7a831262d9a89c9e220dc1b8f38fbc9af19e9baf3b2bfc1876963b1e4632d4807a406f457dc087c53b2e8db39efb2201b142b90e4dd6c0e4dec7bc881272b168da76b508c6d0e161af21e08a6747dbba98638b398d4346f9369abaa78b1c1c2c6b10ccac0387db9213b8b011da96cd4032b63e59c076aedf89e91efc6644bcb1dec085d437070ba112764121a1b867c8ab8ad9cd5284b23b347012c279bf5187d30c178e7523f3c2816030362c6af2f03f0441d9e8c7778fc4c15120f902d4a16870dbf07410e98e861902fe222c7f366684caffe9142cc86e5fc10383f6d1e0418c6e06691e53c34e15a8eeec51fbcc91a0c0d3fa4f61b6050726dcab921c1fab9f66902f8ebcade72117527d051513eef19a5c06064e5db7fe74829fc06d3095c21d27daa801d95ec73464dd58a110cfeb85f1a5f76da52f78acc5feebecef93dfafb7eea1ead130c737bbc88c8a6a70f266e888a385865743c1fa52cccf9924b0ed81579ae8a8debfa529775cc9b1df6d473fa3a205c0f3ee08fc7dec003d7e11fab5da903af869f9139ce8f3a0e59fe5805340882c612243b3d97dd0fb1d9ecb506b3a9d1399a54fe5928c83e7a8f118f987b43ca6a3ca301c206f3a60ebaabab6a9e599252c4aa93d53f93cffefcafdab38ec620b337c4010b0e61b2041596718a86af95e276a2f416dc742550f682218652e4012310be73d73c3f9be30712fe90cc9382e602f29e2aff2b7aaafca613041479e7461a6da3009c1963b07c4f99aee5c546d9d7611ef445d3789c1fd68ca23ace8c3fe007e336f76ddeef713e6b92ba524fdf259e49b34cec86def6f40d5e89f288f8ee4b9e0864617933c0d27117126bd47aa872121c686ab4d33d21354527b99927a20dfd24303511b6bdc10da8fbac6aa8e4df8bdfde016d90781441fada06fb72504ecf099d53c8a9b5f0a1b797f803faf2f64c26de7be094b45ddcf3e7b7da2f18b5e91f3aa3372cb07de25533104ae8335c75f85f9dbf4294132e4e79501a49019ee7073c6ec447d05c62aad3678f34ca973c2276a4604305fa258a8bb9834bf7a73dbedc67794a121e33ed9c290f7de5af8224f23b03868ecb12700b47a23b900501bb181c5792f350d6f72479e7df48ae158f687ae95fb7dc884eb8dcecdc97cc1176c8dcfad92f5f691e5a4e76bad20e9f5aa7a1a876a7ea9d4891a581e862309451724290fc92a2c1878adca38a2309dbd064e467354d3ed3f7142a58a60e885359c7bc01c91a032298530da74fb8200b8417122c251fda947286facecdf0d0abd657d9aa72e83b9b8f1f32637d8e30398b106280fa94cc15bd9f470ac10e0e7d39a5450fbb6c27d918ea37f30e1447ff776a40fa305699e2dc9fed7ed1f907977fd83d60f46c115857b9f77a8d962489a4a35d8da3cb8d8ac82d8751c8c172016826f3b0f14c83f7c39211735d664bf807195cd06fea94d0d6a5890415931341711b7499e4c0a67ca311b50c59d8d50f712723e48d88dd1bcf8c2c508995c8d5cf609fab4275c7a5716977e2768b6e91763bac52a11860053cc5cfac7ccdc5df8655999829c78d2afc42b854ebe502510d3d2f8b4995ceb86d310324b88932f819c6123ca1900571c16d0d1cd776ad27e3a477c4b7b32eb75b3087c70deef5f78d447495ffe97a03ba427d0660e6d5fd2c302721c73af625d9faf51ebb77e08ca722c82e201c2d9da2e2cecb4794c30038420c3ccb57366be03a47bf1af83ca16fc35814693638a193646aa1f45d21220a1b598b34ee40dd700b3c0720c80c3ffc2794e947b85e3001e9ce75e76670bb71fd7e4a4b40fd150d3e5fdfb385cf83370ee192fd6ba256241c82b08e127e1f9ec84562aacbd77c0b84a693e426fe200bea2afda7a5c0d504df64ddebf2eee2478c809be6e9992ba94d31aba70a4bef2e8a6b931964f8e719f2ee5f7785fd09339cb1517e0b2e315f617979eb62fccdbcf9be779dc4dc45912ba1e62a7f5ebd16c1136a3d194602de27fea4a0a7b65680c573d79b2e091e376be3ee1f7629111ce9cdabe16920abebb1a0dea2dfc9ee3989f8c3bf131dd761b04dc8a470dab170112fdbb280977bf0b72170af24ea7d0ed4e3094fac9af366e056f3bb9be293b3d871361eb036d42b1c915191671e00c66d3e1f081742e524186e28589a75fd0de97d4cf335eb2e09e8db7f5f3c02323182eadbc7b6c122e8f96b91b3b728d18d0b78a9fac2daedb02d066e6e27326989ff619f73516438a8949e6f6e69719616298faeb75c36f8f530dee1a699dd48eaca5280ca6ae2c4a1081b5015889eb5558f6bdd5b59b4875d432602f5670b266e3bf5ac9c1a29b9fc559c2d6f677ccb629cf8bcfc42c9716a20fc87692c382774cc4f35de8e0bbcffbda145553ff0ff202517969e4a7f7d1dbbfe2f8476bba820ea222987ef4ba93eeb0ed588ce595c2a2fe81a36c063e5b1c2c8c835d288e6608a7ceae2e58bde138a057ab2217a6ab2dac11178e7d9ba97acb37daf67d18075d86e9c0bc6f02e4da08224f97acee8b553c989cc7878565a904c4eb0f38f6cd984ae27122ff76f09bbd7b8daa56d03e4074d07e2dfb3d9d3b1f1ebe71661a60c52abce9310878441b5477b1bd6b3314e76bfa0f49925255909a4dc3ea1c7a1b99744828c63483d054bf56dbf39bf008f9025315196df766fe35f2ef6b41b1edb1db04884d5b20eb8c94d0b9eb7ea05057a08ca5d9a547bacb3733341af730c920c0226364c69e8f1df80e6c1a9bca10d6d0b1d87ea4d0d3b5944978d903b109dd6761b703baffbbdb5fae4c015fd5dd5c11972541d73cf468333dd1f160a7aad3bb44f83c659e6d2112bce050d9c45bf083b13558fd4dce900f6f9fc84e52adeaec77936936d5dba080533caff738201994ea093770ba5f1788f06a022476ebb67d2e9b80ac39cbd9e3599760e6deb95fcd31b9af1152955295f749bb88eca25f6b108517b086c406432ee6d1b0c803a6829bc1824940ea386a6fbf7affe6c36c740fcce32ff9d2a8a2395a3b713467d3dc284c8616b976ba0c83377d0fbe2961f6700bdf710992fad18ce05a2c8d6d6241f62b21314f9eec65575599ad6a03df2462fcff8b4b60ed3a433bb37c7eddeee4f89ab5f374738897bee3e85db17b344842fb3d7208228966e74566d285d081fec48f8a1ffbc7677970209e4492942c8d201bd99da625ab7379ea501ecae7c2b015756f04428066b170b7ac3b1236fa8ee3358933ad889ef24eeb7c473d13996b875f0b6357454753c364c38ffabceb6bedf61532b67a4c7e61ede999a79b161fd780c3d141eb972b142865e30384f2f1636d685e81666e99688de4cacb113a744fb6839052d96194ebe6bf560d8aff3c61ef498f334c43e41f58dda1245c4bbd9802f9a361a6f9ee4eb2cd768ce01061dcf90814c4f5a4a2368a49cca2cbbf559495bf7f43082eacc5cd86957f23e7ab9a28716980c4df112e4b0b3f80365423c8d7a3932a14c7fed8ea00cf74b886bb67718724e365775f456b5f2f01a6209a8a35a6ecad640d6589aa8c90184d962c32d3fae49be29a8f6335d69a2ee70c2ef122d5cfe7165a460b00569dd4c46ecaca87470cdb45cb4a1129102dec413a3d84f24a6b6c0b39367d82c36b749a29059dd74d90954a5faa62d73a1138040c7248e6020e5f2a9bca31943d61195e092aded1d486aef752064d80e2de7cbd8aad10cdcb647d9e6c89c3ede6736811d1ffd551ee73ee08cfa372c357bdd7d17c6ee18a95d74860cc994a586148399e7cac9d490adf2b4f8a3529cb3c6142849e9c5bda52b88064962550536f55506ad092e7861878438e0e2a38b3a2915f55a53d56d6217a5a4dafc85af632d2f8b2ad5496d3c37a2e83cb2a4e74d573e0e6dc63991355e7a6dfc8b6c2fb68d6fd5ae9d23304765657defa7ff50e7216c88b3cea2e075c206379a294ab0c1ef7ee793961cebd0b4ba831ad7cce40d7fa07eff44e717f485193c3eaf3bb588817c6d9d8a3d041f94af6c436f2963d9d6ebdb89f898bd51c6fee90a8774f266782faf564e7dbd28e1b4761807721691cf1a10ae9737fde9df8162ca643321505396a31e40c471b674eff6720b6e1f601cd894b7df385eb8b7163b62db78ac54e9dbec643fe42284e1c1223a3568fc107276cb0807fa4f324074b3be0d1381aa0b0471218a99ca2ebf79a923f7c2a34cb350a40d3230920d56fa23220043bb2fd210938f6c08e9a6f9ce7225ed82d74ce006ed8b9cd1fda7f60e85617ca1e3d1fcb9bc2258e820b376485d9bc0e9c6b9becfd53bb4fea7374d3655ad0c45eca94c9198dd3fd9adea3853a9facbcabb9935e6fd1d84345a121ab4aed2b6d4e638c336d9938bf5d6ee0c2e9386c3318200e197a37c65ee44e816cdfb6ba5c7d6832c58cff1276891403c70ce2f4b7da06f14e7afb72df70a7f1204d412392767d29e603bdf977d183a9f508d97d246adb873eacc2648f2499354fb85728df79454fe077b5b2c92cb6b8705b38a183a43374e8b2bf4ca4f0c1f7411175f139a32b3857e02b52928555d40cd74cdffb6c3fc0804cd066e8ba5fe9e27182ee65cb60d56411df16aab91e5b2fa3e1bc5093636abcafbe4438fe6807b1aa6f0da242ebe33eb7ee97163a14ba10f6ae8eb2cb501ab2353a0172692647be27324b6e6dd174b3add8342632f50926ba23b28919c2eff05ec854613a2d73aa98d905cd1d245b8f99a6ac24e913701b8067fa17c23a686557a7489ba360505d339ae290e39e30a6dc284a7d2ec590e265ec6a44a366aef683df637dab44528b4ad77be63373888d62ad329b7fbb94d57e6d824da35e6a89d9a5eaeaf9192172c86a8e9816ca34966e145b122bae3b5e29ba154eb8a9c05edbfa8317e5d0ab11b99a5324acbd71a4c5229ecd86fa6de72a772ced6ad1b5d8f11838acd7905ea7570090ffaf5483164cd926d1884ed0a51aaef6869eaabe143d4718c3e8b6d83733397824665644f479c6d38f0dd8d3a828bc809ef507c7229974e56c2b6ee7d970e7a10840bcf7db1ed886702089fe487a5f94d31379aca81fc8817294504185875a731cae55fa50cbc4351e9a8fcb031b2ea2e9552c4d6e352ebbb14a38357c573cb4b9dd94bb7d02e0ac2610bba629307bcf192cba4797e0369c436e55d23d45d9bdd2ef214a103a2c323e8dd7d2067747e8f9a0f21e0981e6f390d6a95c8729cf615e10733d4849c1d0e1cb715372eb7d5342c01a58067274da657b221e893c38e0eb7356e61536060f199cbd4b673c61276d2f3cbcb89dcb6641a54abb19bb885d04bbf56d0c92e091aca2aee4a1e0b07b0045d99482f552bb9bf76b9e7675838af9fbd0c1692548e8ef32eaf49a00c7f6b9869a862ce1a91d1c9c0e10faa6fb3159c929069a88bf6fa634b4c8b8f1d53dc5b70774ac217c48c84a3697448cc5adc965118fc9e0a58a930458d64ac380c147306717f01aa75fbd00c44519efc7e0f6088827b9628af4b9f14a66657c33ec13107196ed95d0c045fd5edfa34a4be928b68ae4281c3206b0e750aa5f9e5ebf71ec7bf0987d04f9bace0c51ba10d22966959271dbe964e4d7b173f4d8699a696fe546a9791688fa137924829283a5b7b126a5ee5e00130f4f6cfd4af69f6f5d91357660c528cf42c03398a2868a062db689be6b935df9f5d48f20ba652930dd22b6f55d4e3a2a9506b330e28406a6824ec0b100c57417402744efdba5bf7af7a436ca7104977f984c996f28b708d42580370f69e146eef780b62ccc2a0105faf714613d0fd46e0784df0c95f5e8e186cf78033b700cb5a8b26eec8f5d7442805e66497a92b8f14b7ac41ec8a22250fb68f5beaf5ddb3d5fd0ea31c7c6bff5291b5dbd937c37381dcf8444f16061122123e4c583ebe11c15ed63ab03499503bfc003bb184041a4323c495519e75aa757678cad0dc78784fd512f0b3089b31ef8432b25ca7da87698865d4a5195f23366c233de80292eb6bb2a9206743aca18e1fb4ffe46af75caa0ba3fd0c6f56efa611c9178e1b10b3492e4dd2719b1d3dd24bd3d01da37ada9e27ccd501a7869baac52f7cd7d2042c5c7fca540dc77456af306d1b9854716344eac2af78737472ccac796bfdf1d2b9e0cdc302ad4bfea4c46f4142067ae9f77aa1cce243d7ab7c96c1779bbda180d2d33b7531cec2e7e77a20d27d6c912ced316df811cbb790477259c6fe080edf8933e0937a4e208b595e2628f183ab813119011f387484c0c4b18570475916be457b02bfb354b974a7711c0500c13e4ce89344987f6d599ed2e359c6efd6b236cc2f2b4d8914dc5f9ce393c1d779c6d606c2252a5030c2590a3cf0222663129ed69ac993794d51ae14118f7253895e318d358d60ece9a9b2db6bca44ec97c288589ce633c269abdd470192224b5ff521f89ab4ff832d265ea7305643ea6e1b1c1044a095aed8dadf613024c55f430908075873bb526886e3525492fb2e349eed14cf4239ccbab00e137b023a4adc1c1385cf320bc716f3a11bf69076cff6f81bd0842e2ac3f73354943743d04d06a348f5e06b2a3cab350c49043fc03bcba8baa45f75c1c65a8751b1ada5958fe8541d32f00e7ac9f6f93be98ea9e829ec4c83d18cbb56c6f73f2f08766047752a996ee69c628972d1e0e92b4aad6d64a2e22c5544fe9cf6aed410d9f83c84305c33fc70c4b6ea3fe4f2a0d0164a2768cf30c4aacd6f7369c855a87c35329584477c259acbcc08a19a80e8c29506694477cc2bf90a1062c21ad8fd5a7438358b393efbf767c8188df71f1091f4866b2d1657ee49e9f75ab1a0c8b082ce0523e69f6011b0c7422cd4e56e41427a929b6cf72b7ec284754fd4da90c422842f78b574225be6111e9e8ce479b49f53005fbf71696c23062ae93d3ff201748f63024c0e23982c2533c723a6ed6ead720717fbc5a183061a580f584371cd3d96a44fca448202268d3a1efd165da2725359015fe08083646a4605815223ce46721d9bdf7eb38a6a394dd2c3c4d9d2cc0fed52e3bc537e91468b5d73b410958edc8bee033471d8667505771f92e87d06230147d6eee2e5f6326f12fc20340e61b3406e58bf7161fe5a837020b246e5b04dfc2f0c5674c39b1096039f73a436b6376751f3a3c0dca0d872814d1b6074053997074393a17c7100125c71fc7759878020c9abee42de82dfb58321b74391040a6893d1d635d52dc8d8dfd7fdef771208ddd4b8e56f335d712951ab1ec8ef06631f124ed68289202fa6b38655dc9347aa6e1d3b5e9b4e0f2bd6e7dd973b6b76a53b87bd49312f2e2404c454298dd81d7a43508cbfd3c529c88dbceebf15da68b9a2e22ba07b04d0fb8bcd9a97733e53223c8c4d90890bf58f28a0727f81ba2973e5d763b586d4730bff13e9f659897c19ca201b3dbfbb20ac101b2e826933dc00143f2de435a5cb06c6d94f808c76b275c29bee379555e903dbdc6248784a48d0ea472efa4c9811423ede7cee36cd572416d8d73ee69a32e098b7d75eb49f608716bd180116df3d2dde297862fce7f39376bb62506382a21da7b890ffbde81d102bbc484a8cefdbc68d05d1a9b3a0ed74d36f9c41e1d7ab82d2610704d9f521bd4d95ac37641a0f5a57c1c46e2dcf88baf17e3b5ec538e0e967e6db9f076c941079d541e0cfbef1582d982133831beb522c5245511e5fced58f973e1de63d5273195fcf7a62d28365434c7b527589cd606feb762f496673fbecc91ead7a44bcfbf45645d8982a84460841a28b8bbd0cc5d1e09e9396d4f37c481d3305d87649a4660a4ffa6af8f47b90083688b11b431601b4bd1fcdb5a33d18ca5acd344c75ddc02333b19182883cfd31474cfd6365b92f806a5ce36849d73cd3fde7d60039ac1b8f4269cc7ef2951e05187fe42f92a56fb7eff538f513cfccdc80db851b20234f88560d657dfdc8c8c70d8022eb156229a4b8e3d4acb3fdab6a955f6260dffb084171cae8b124e30ab5ff098805cdf8f68f0bac8616953e4f446e22c95a9f41ba77609390a51306ba91c8e255a72c5b4528c5b7ccbcf86da8eaefad83ef7048b828703cb8f91fed39a1401b92e85473296ebfb839965b4337135285740a5923bba5caac619ea32b2ef11d3637600c803e0f6de53efdacbf052bce5be1977e2c7df8973ddec633d9b4f67fe22c962b4a25e490de1e216f73f0d7977ee85c1a5a9f0bb8dd939e40a9770db36c979067b684c2fbbe8572cb15012df2d0e32f2efa45ac728084faf873fc7210858975e84ac7e36b69d1efffc846c8a5f0fde48857c524841e916ea2c3f28f73254088f6b3d15556a310aedb0bd8091b02c2724c22dfe0e3cd5a5ff033ea65d9b8a9c9f641b54905366facbca5d9aa03d029c526e179491694188f7aa6e5cd81a052c2828ebbf87fa04518677cfdd9df972ff487d4873303cd185955907662559762b55ec6d1ace2bc9bc4a9efbd22639388ed1463f6a1142adbd759de772cf2edebc895b71f71b31a8a4369795b7c7b245c9abb91ba3e55e23638ce8e356909c22728ed56ec4d86d55444ef37ae3b4a044295187e8c61f335d599bb1d91877507a6545b82d605ad189ac68b791a0dd2f6e701d12285b6c74f69ccc539ea5cc0e89e29cb3ee27e79e1c7e64302423835fe3ccda13c003de3bc3878104485d0a6e761c5c8a07b1ba6b3e1422d09fc88fc2def3381a61d44374b7843192a5bbe6c9946b50ea9e87509ac3f5fef674104a3dc93e3105cf86f71e29cee4409a5dc1061617ba3ead7317a55efceb5e80acd0812efe591b7c7fdac21885c29e57803b649cee577eafdefb5faa9fc63721e4840d4694a6a6d018c9a89558bfb1e072110f77b93825fbf900081aececdae9ebd19c1e37022f757d63d0109aac62aa9b669dc9fe546d82644d2489e53fcc61237caf2b58680d29df9e4673a7c3b6595e7b9bb6a2d2568fc091670e05abb80f861c74c6c5afed8709f3629c6ed12334abc7c43754189bd7ac879a44cc48c27bb4a0304cd16db11c3d30f239471ef390780850f1c91fd11d5c015136114c8a65b111227bd5510009d0a5c688d954f121242fddce72029ea5cebc9e31f140a935aaf04bb631b71bbe7b82bd3c7b0f2c2be938a999262d3f3b09d7f75c7572ea767d53ede43868dd3cdfc543e9865760465bad8d46ac08357fb75aeae08749f859f2212d8fea75b44601391df497819ab47ae70b8928331e1173c513da3b0d5187b818b4afd32005e82e70b1a830901102e771b9c095bfd6ff84efcd55802832cad332508c34da599a4343d3c9d5f5c624379e770432feb437fd23d7b895c32a993bb6a66bd04bd3ad12672ef3b6e76679da70bc6bd723b9a4627d4829994011f53c148b77dee47bfe9692fa5642eeb7b8c40798bcc6593ced7f715b2d35e36a1a0d0d1ebfea0b0f00be4df86eeb3ae3e9ab30321fad0c41f8aa5f54b3fc86a6d1048b9bedecc286d20cfb64fb72f81079ac70fc6817c09f715999f277c7334b907a9216edaf562da99ca600e9575432a5eeacdf124542054d777c7df89801c35cf769241a453fea7acbeb710168a121b311273fb839140cebc4a6f88f888cbf5935be25f707299bb15e57eeb33f8374585d43a086000e365970b82dce6267fb64e21328526a77254f108b8d4f80ec72003b5aa7abed6573330415e76f8e6d74ecf9efe8d63ee9284f0e7c56ae76364ca1405e0a65e38fef02db963f9a7051ba1a18ac413483e9ad22ba86937632aa22eee194baf2e798e9d34da3f4c48b44bdd3e674d7970ed811c569ddc88c746dd008fc889baa94ac882c86a3f657dd679fe0274cfeb2526a5f7c8c132e7285180ece1c16f0ec8197c7f8bc14fc3a1ed03e69ce119983872d5e90625b5b44a0ba1b40b01b7f3dd093fd67855bfc587dffdcfdb80562a70499fa5ea324bcb41a61bc2892e8f36a52457ac176739aaa72ce835ada34d9522c040a1caff89fe1006e976daf2f8aa7d15b2fb41938d5b1ff098a7c2d2d2c61b93a8e95488e2239f2fb0b7e8fdfed8bfbedcb83103704865baa672af7ad20630ac6eb9e40bcbd1aa0c62eb39619103a933c4a932518d9c91e396446316fc260f7e8b9440c9cbaa145572287d40a1803c33dab0913aa92c4fcca5af6d1046d53a09472e5800989c3802396fbf690455b45a7980d453d8bc5541b2a8ebdba2c38927cdd6216b346f3c2548d72720687bc7b53a466900936cb393728e5717ffcac038c2153eec787cf79bab6afa9a33a1147441cbe8d6749cc7df7a629da2e4870f40f8773522291b3c9be3eb17a907f811ea674c137b99477f90affa7b2992d42377488ff2510a1956da4d14242428f277a2db988910f7148c1fbbc139eaddb58ed1ba74a44623d5150636713bbb68205271e1a2be8e0da512010530dd2822d1f27d3e2090bddbf78d55df8b55d903e5fe419cac18d3947a51311ec86929b9b2ad8212d4c08f2bd7f05962a746aee964bac4b1c76d189bbff150415f8737f20b39497174cd1b88b4bc1641ae682bae4bbf1395fa78142c9f16629a727d98ff5ba6347039f96f5e0e24788c9b0fb61da0d27ec1ccd9bfa604e15a9958d3ff909da98e825620ece4c5cecb127323fcf38d93b507c0f6bdf83ce6118649283f3b627fe740b05b9f3f0fd7c8db1174db74f3ad2652e19105b71101367993866eea516d4f34a42d738481e210f5b9185cf6e60e16de311b28fce9edad83ed9d6cc9900f44de8eae0943000a4923615a85f1031d8701159c0f6cec18a18beaa8b7924851288b6d215ba98ffa675efc346f9c333e9df27907416399da333d8b846f40fde5e36063cb6c9e0b16c464afa950fd3ff9c95d85c3f94fcb2d819b18f2190ae291b1f39c83d773d840bf249ea9826934c608724df602efadc90ad84f7ceefcffb311b6a55da356b7fd4bef4d773cf9a0d88edad3af8371d0f165ae544516ac5b7509066c0d3c5bf17195157631a9af32edfd0616ea4e92011f6d0f60ff285d02ee229a8a3a61d711bb1e9e6500b72f488f6f6013c7e49ccc7560eacecb645e4e5bbeb6f2cb574ccb21f3e6d7cd0cfc7ef8768689a86eb10bb26a0b16028a056b31cfe064e838e376b611c19422e6fc4e4b2a2e618e896badb65a2f7b53593d4a5d37536d2df3d70fca33f1e8a62d2005e66d7581c6cd008d1d0db93dfc9381b06b9e6ce0eb93caa4c2df59ed5a934710201e921786b6c611c97eb4ffb81eb59136170d168f6ce3e0f1dec4eff6279048de644afb2f1b55a663189338aa24330378f8ef0ca0dcd5e2f1df7b6508c89b793212774e6dfe3ca5875ecc37aa6a6903f954d39f7d03f5ae00a38ad5fbef251bef2ea8431ded48c3d3ae913aa04981736582d9f55f54d5782f15e901a80b0169ab376cbe60e6caee93831fe1af2200a1c83e791ac1e8793c67a497d745dfef33468cdbdea7affb71a7e293ce17ed94af0b19357e9b0f0dda4c706dc64b46bfd01b48b606339a20658fcf1972280df4a27b0e21f5a7dea0a9b8ec81d1b621d88d806fc756a28aea1a55b4b29d9de7b8b44338e3322df587d7eff0a7a33da748d624e8ea57215330baa13c8d0096583cf91378a3b3c87b0b79942aa603a1b541519cc0f0e8c70c50361a9d731b3addc2c3698aa99806c42015168650f6dd5550c48dfb293bbe4febcb2769fa72b27371bf77a637a15f24d1de8699138287130f1890a46d20f9b52c25b321c2fcf39293c8fd424b77a0550868d14a7170dc2033807a665121d694e8c8b7ae9a396c2adbcb2f0d92f1acb38f51c27852756e049d5dcf1fe35d8923628f43302ff039ef59197625b78d563b25fd1f74ca05466e91d9a18b8ae61fcce389cc24cfd259e64214e5a40cdd5ee4978128d990bec1646eef3298b36b45961511cf0280b1d0c56f2339fa0d15c7f0d62f190717b08dded2118d1aa75895d38475abcb9c65456c3f4c36c8a5773547d63ff9bf0e885b09762053a2f97fa6490ab73103d5bbb018eb2b32a2162af6ab7d7329dcfd72f0a023902f1cef57ab0d850b056c99c31d4dbc889a04e6d5e42c37a222262c4655167e2f77451b21d0b30b4775e505843fb1e566a49045dfa9b5bc24e4d5ba259568252d6d5aab41d11926801fd310f310de5314cc32f59d46b8e56fed2361cb95d6ddce3d15d8362e81a62ea605329095084fd6e30b7df62396c4f1e8c8207f92bfa5fba2fe97e9858353eecfc0aea374ed7c7b632eeabbe78c431874d1cf77be986846da75d31b30abded309fa6959c28d7a25b39c3649e9d7550aa59c5a3f7cbda13dbf610dbf408caf3520f21dd03fdbfb33da6218fd9adcf17f3e11018ece2596f4b51b02e309e644a10a4be8741158435110b20aca030eae261af28ad7bb4d0c9e1df2db0304afa4d2c0f9e23da3a12567d8370c8470bb22e0e7cc34fbb358c0c1c3f5a6b7d6600daae5df933884d9057dae47057cfa060d594cf43bbe1e0dc550d5599949f7ea98aac4e14c40007f0676f7d7bbfdeea55af39713068508372dbce22b5b21e195cb607e9fa36ef12caef6972869a95d9ffa62c9ba58c07d9fb66bee30511a4d2c13c0cd3dc22989a7ecd98ff51d24a78364aee077447d464b99575808a513f932fb35a6b571a1c441daa63c3aa9f4cbb086e5d436cda63c9dba3fb5b6e508fb5f7f24af6b64e5c0dee70e86c5f50db5cf8eae277234fd40a19283ce2b90c414a00da2dbbccb6260268238894c73101dd64c9fef016d602ca72523a88db051d4af3a19e2645eba1567fbdedc02abd13d22acf5d838295b60c31fb7d543d10f4bbd79bef9a3821c6d8d018916496e07961514f7c968e165a640f32697a9e7bbf5d8ed2d8638f56d0ffec8dd8171482d5b43512245b17b689cbcd8acc784620fb738014c75f300e575da39d7d78b6f83c70e4b13bda17b1123714a4b56c12fa7929ac6774c92586fa44be2c8c3103be5ba1647da1ff89065ac20a1059cad488da9b6c5284e79e121615bd00b99c70d2e7dbb31ca196bbddc3668c282d405e4501753b749d2483a00fc486aa09146be106ef056997019bed9f6e59eae532abc16e51607c1523a468fb044b22af5d6a484961f548914306a4bcef32d0292664063f413a7519ffe79982375a9dd006bca067d5b60a377db2728d8ad63940bf0e8cd685271f401e1e99c3dfe4407475fb3466e17b60f677507ca2ed4d8342818117a223dbde3bf3a84137dbc6667fba6c4d702f14304561dcb2f6a04a256f63594588c0946d8aaed85f26aef9175cb068da02ffa8c46e4eded57b00b36be934ec7b439be04b1219f0a3f0ed0534be3488f5d2c4d8fb9d58e7cd6e48afa10dd2196ddd4239fb33f5aa1bbed7107077d1c64308a6f45b50eb78317d04126cdd5db384dd442cee46cc4c3c8f8843bce5a7d267a646d1c737519332bbd8c7af23b0f6eed0a8fa70154d2b2f5d2e2ad50d19215b1a1f502c2210bc82cc630117b33ad5d0850c9c12e75494e9390745c4925df21cc46f5289988340104fcaf86da46027adab8d04d785fe8e34dbbcb8af24598a74bdae54c3e4cce394c9452bb79816d4442725ef2161a9688c249780e8350158ff0d850282e70e132f02d2342398b98d8e261902fef3b89d458ca51348d4aec8551947bd70b3b36c73eff8d66425ad29d638f1037dcb816cd210bd0a1e27ca1e66ffd6e53034ca0d83bc6e9eaa51758ae7c3aeeb79c8441b8dce6fbdb53c998125ec5dc09dc4099df738577660b8e715ab1f8d1870d4c8abaf29f52e5de2de179e55aaf7e17efd1bd72bcb9d9d9003532a55e85a6388a5363dd78af922146e0b97d36f7c26112790408c8ed0c40ecbb27b77d1163abe0ff876df6e382adc9879ed9bc727abe7b7ec34aad9800ac5b2e53d9b2ba56e871f09d9e4c61f734f0031efc00f353933f85edebb3f26ddc6c4155d8323f0ea51f1632fb3f7514e0fa198992bdb98c8b7e0094d8b57fc5b6bf3490304b5d34060cba6391a28f516ffddf5149555f1784484e7b948092bb40c48b5c4a14327b7e9fb5beee87a83378e404389d5d3b4395c4576c8fffc86e20eec725527dcc392bee5018a4b17bc7971d56a8245a7b01d360b7d47c9a300f6e256908320c469c2491928bc4fe71ddf37c909017cc625515dabcdd6162bb62db61cf76d698fe046ee0e8b9a195e12f8629b2bbb8f8aeba957cc965de93f89c68fc12f89b18c0bc7582451d83c2906007b681fc21ef02f60e9557ee9de6a5f30bdbc222d1ef1b3369611feab9825450a6678c5bae1974b8ce94a88ee18ba282d20cb8962100ebde5c5e20e87e964910807c84d9c34a5ca7a9bd67a16a8251f2abdc1058800255f085245294a1a26692ed0619ae56aca33e18c180310d0f8834276e4c94d5d0a295d45b2a5775844f9e7c0f29053c7fe91e38492af88de2fafa7e3e77fe3b585205987e07c3557f9dcd0816741ab78971b266af70f3bf5ff4fae676434caba40ba5b67b09e3b23fb60b93a8a020350b8adf82c2c6dc2f247122f85fe9c32aa396fb79438857560df83d61e3fe43787d1f1a2034687fb2ccb44647e6edb6f33d735bb3ce6187c49b0edcede555cb91f8667a142cbadaf4b55ca22a328e51ee18bd73b70b68cbc9a616d345bcc26ecf18dc1f19f1cbc23fac2fbc0b4f2a256614d33b869a706ab625ee74edd0ddaddbe64026d3661d06fd60878be47274e28442cab040e5a43514c338eba1f0c805f461b739a8adcc7b787aca1f3a73c7dee92348aa8fda6f9e52ca8c3f05759c5233d3dd95c5bbedcbc8bfc8c1fa441a730f55fe11aa503cdc15ab747f100a2910d9790f98e9a09ea18729f0d1541185644b5420f6f4ac8e461e895d36894a4886392842a81695bbd79dd1000d46a06a0b5778da869b6948ab69de79177973d59d5d73589c26c12427b1a93c9806ed3953aeb957097e77e9e8717076b49dca3085676b59aa5a9d1b1537c65cb44dccf2e693d309a7e8ec5cafbdf400cc79cf3bc9f4fe19d974cad683715d34a38dd6c97fe84f9233a87ebff7c45a35ffa45cdc94e27f27a8c3088dcc01a2bc2666c085305d304f460c22b9024926199afa1211c614eeced2a141b0e7a4d68cd50779989d4b6ebdd90cf5e5db465cad7778e3eb0df9ed347ce63314ad81f1735ea988d3c38230ba31c434895b82ad3e12007e5ee291e772c08e3811b931c63e4023be658e57fe944a96853a314f81afeaafaaafd974d21462e2bd062e7e17e2f1e713

/-- The row differing from `A0` from wheel 58,287 up. -/
def A1 : Nat := A0 ^^^ (0x166d7b1929fb6cbc8c730c60a39744f05c3e1f8261175543515c208310a7f3d9b8554c6b7da1fe8a5483f2f65d4296c505582ba51c800d41966972b65012580cef3fb16bb3c8486b8c3248f1fbeb5ec6418be028d88fb803e5a4f2bf5de04a734c9b558a80e76ae9a28d92212d42a540836923f07901afb1e4a53f6780ff98bdd8f48d0e47b2e56931fb61289a97c895d7039ca7c9b1ca1c021ef57f1acd98aabf12c6b1df80aab8263ad75016e8fd94ac036135d8caa7715a921225dfb09116f827d19b7e76d3b5f1066f51c4f720df7dd581a173f92e7b54374c2d8ff369c8bcf62d89f209b43883dac505d8f496601b21fd64753c73ba75dd49279519e0ae0128b92acc0e04b9f0b24f8e022732b954aba5e62059c51579e6780549175109b5658b49dfba2e812c9e198fecc9f068b19b078f3562e4104e213654cd9050eff75308ee1c8e5bc4c32bf8a9fe377b386eeb4ba56bb6a36d441dac53771f8b878ba923404b545a80412107c21653681171ae460008e543fa990a6ad51b0d672350fa0db5e6dbf90fc157f48ddffa2363a2d961e20a4d9cbcde50fac82a2101d01bf6791abc33d6f9a85cc0c2135b7eec1140df144563df1e5048d55e0ecd77328ce38e2ccbc0bc628b1a6ad36e3f3f9bdb025224adb89bf0bac737a6bda823e08a3d32f27f06de1d8cb8f046c3b20dafeb8f6f96a434e40516c3c66b8273162830c8da08472969720bfcd8cd398f45eae625fe3a7aa79284f6582fb0dcfc6364f440fe941ce4e7e4375e335db5186f10f5ecf417740c9171507d2bf3180183a244b6162d5edfa30042b55e7b71d5ab6f57b39dda7115f75c24c2bc5466baca7ca6cb92e3bc033879ef39a6e7c365e786d19a76741203e49e6b060f72e24303b7c0be236f3358ba00320e40664ac919bf4b5eaa5d271843e30bb304c84ca3168bf936d98e774bb7d26f5c91ec10bef618e88a02e7942d1cebff8a4945f976124d3a79402bdc092a17882b85149dd09efdc34ce8f0875e4edbae8bf1023b65db1be179640b444cad59af02016b9b393131d00f049276654caf0065092d69319a77073f4a080b92814743010cc9382b907f091f24632209d57a4f6e359ed89dd83a64c851a6262250d13841223b67b8125efad51f1a6581106c6c8fb3546a63ced11ace38399582e59431df20e2255cb33ed2b4a4950de3a65340b0f44ec73d97678ad2b15807e141de9be61669d7d57c808ec575b97208fd3a40cdd73bfdcceaf26e8e1e202ae934ce43f214febfd148d73409de9e707b6211beb949262e46d5b35c99471b21fcb4960733863fe1498858335d848e9866c22463eb6c5877a38f046ef813348892805a60f4eae11b5e8696a622bf756399c7e713fad9e2740806daa05450224f48b8427db9e5274232fc93ec0ab1bb4334e8716419114be0368d6e7cd2f2839caff3b9d6a1a2ad32707a350e2cbad7eed88e5c920a952f1e789b4eafe8a0edcdc5e62019830fcae29b85306991a909fab6c5cbeac5d7271a7bc8e6787aec6a8b613111397e6450c40ca52ee2182ed046676efef9f345b2224d907355006a7e4cd4c4ffaca3b3b812726dd9717bf5ef373e7c7a2b76256d286a6149971d293881a57d029c26704977c03ccdcba41808e2cff46f870b94884f4fba29dd1cf546609744f5bbc9a79ed08e26548d8320f8b906eb3530424a24ce9dc0d5627206c23ff7cb77e7ec3265f84ee11ba8275bbbf22b57c342de49661701d6af0db032d294da8da032e04ce25560a4947da70a91a40d48e06f33adb835ca7180510aa5c26c3284ddc64f29959f36ab480b709f61f4b85e815a1916d7babf4f2208739c30e25096614158bf1b2ad4dad68da9d53c4a971559d1767a3c029778ab385b7919fb68eb3872afad7f10f8b1d0248cc693eab7878b938b1dd29afe9f5bfec27820800e5597c505c24ea950fdc0b79db4bc7102c022840e131f41bfb99ca7e019ab4fff3eeeaa11ba37996ce3f8944e0cdb5954b0c7623c9ee00706eeaf7b0c70d5caef3a15b0eb103197862371fbb04e9ded485a7c573536b469d01a73695c01ed0e47a63ed7308cd1c57f24c348c93f8893ae19996b1f1a8117d17cc95812f69fcf24b4f20b8b8e972a00a5275f708ff42ab894fe13d09bd0b3e4ff021ac5c507d758ed84d75d3a80bd1b95e171769810560d30d7ff8f7cc66c6d9a56fd4322932f8bb7aa08aa286595f7f83ead320c7f3c4b3a978de29d9da5d4ab10f81039bf2194bf64a5843f61eab2389f44099c6065c43374c375b15049db6c3ffd84867338d0740d63b7352bab722010234ac26cb724e28f0fbf0a79ba477605198e3082d8efb6a4780c8c72dc9880f0324216c76e74720e24dc654d8341bd76fb9ee5af21f165004eaf0601c13d0a71d86a121986b9019790abd723fc1842331bf4b779a95df9d8d6d6276b3963a3725ee839b1c812d5368d58ff5448ad60fb4924363cbf49a03bc594592a495a4e8568ea543c57dfd80aea790e56a15d4f0564692b888580199a2d7d7a85d904e6d8148f40eb2187fa36272508e126ba837be4539a2b0a9b902695b066d7e725a7a9dfc20b20752e7ff509012ac10671552d3471e51cbd3e545a46ad51c1b69aea4dff79f942bd8c85d75171dd67eb3418cf798847ee2226daccffd2c35db1d2bb32ba1a9e7505806a1114cfd45c9edf7784e48d82d1a3f24efe0bea36e8c0b31f2f552f44e17e28f6e5fcb6894d1f36c4edaa5495a86a8ffb552f8a16d9c5bfdcb034073f608784f7a38bfc16b8203661248d4e18e3b5dd309a8067a144cc84707ac64c6c7a4bcfff2009de2b9cdfd0a02313a5e6f252412797075ed05d7c2f4231f554f4eac87017c43a3510ab6388c943af2eae3c15ad80ce7bea2d75fb88aa5d835fcb61fe322c4bb268b3b80959e92435b7083a94bc49deca9d32521d59aee25b5604d549e29fefd8e2b48e11aef8b8dd308da1a3abdc6eb28d61f135ee6000cd030829dbd0e2616678360dc24bd7295a87dbf199f60b0ee367a919a597e7022b43e9a19ad4a2757019850655586433a84e15506a395b81b4daa04e06fd38cdbfc4f550b3562aaf78d240d63a04ed73fc0b7909a2d262ec77db678f3f03d853505bbcc0b0cd52e8b8cfeeb92f2d403ed21a52bc889d5b97651ecb9c0cd0ce73fb6e7f14b4c761f32b1fe9467a458382a7c81aa7abfb19a34b7e6ecaa6a08519c73843c58ed14b1e3e4a764b24af9840341059e97a505944e5451b073bb3571502f4eb13c42559dd6b9b467a61626623eda232fe5a1a3cb062bf6c57452fc33f08f84bab578afcfb2b814f28543d2c2b7292c7866f28f65b68d1ac85db804b16fefa745ae00cb714e5787f66ddf309135124e4769a67e9dcb7d0aaa1ea167200b711cff51ee3438debf550267fcebe44e147e458b4ffcd0bc1b6e7b9ba8486a1cec293e48cb9bbd9decf74e042a8683ad7b66da23da52f6bfe7f0885f0a7cae8eee19ee87de9df201f7d5febed1a8180432f7bfe5655def1e0db80515cae04d48363f5ccd4becc97b02733b8d8dde6004eb8476e3eaa9d9efa8751dc7339387a1f83887e3cb7faafa16a7ad5f06f9f48503b80bc11d8e45edb176a3efd06bb51b24f2ca6621cef04483afdd58850963685ae39f7df7d5cdbba03090865365e653353809e83b63f2eb104b098b5746a0a80f9469a784b72507a296bd619da3ec39be21c87dc4cff3529d92ee7c48f4c97309f03bc11784283961ff4563cb951bc91bcd3674fa9993a92269d7a2b41bd052f8041176e8ae9a1382c54c7fdc7b1888cbe0ba2e5d9c6ac1e27f5426ca0bb22ed7f1cee0a868f272f5840db5938368e2920e829e815a1b2bc53c6b909828301d9bbac0e68fc8cf1b06ea5d4bfc2fe1d65d3000a2279548c26a0e0707be1413494ee14cd4c94aecdc25dad4f84ff498e9aff37baded2934cf35211b193a1e5328eed7329294099e13ba66c4eb98ea3922b7c0c6f3e4c62923880999b0886c36189db4ceb7b283c26f81a79d61896d216b69aa4cc211d2b8f14262c4279ee1a44978dbab4f09e3dfa2fbfbc372236a54ff5d883bf8279ab3955fb71b5de11d3e9c73f574290ce3b0858ba74a4b067dab59b10db7f68c8a2ddd3484a5c3e4c7ac4ac6055f33e4675a4f9aaee88475cba651c27d1eccb0c241db9b91f40eeeedf0cc91f15525cc11023e8127a21e11a2d1d9c135b86735cdcc5b303b60ccea56d3babd205fd7a3c5a9e810c80c106721b1f4ea04122a7c7c1f1726cdf7be25483c5d28f49b2cb366b97a98f2a1068d5fe264b09e5b691f1af352a7a4e5b004705fc9bd8b3d768e1cfdad43f4bfb8621611a1f5c2962edf68d8474bd7fdb0a39fb8a186460818e304b4379fc39e00da8d34e3778e85d599c50dac595678ec89e6f8612706efea9f6f0c50c049428af637c926eebc407f4873f4f9f00018c13d9b89afb2da32913f30894fda573333acd9a4dd04ca1c3c3709f1e644de4a9ab800aa9010aa690d2f12ebd971429a71e735de91646aa3e2662df8b4bf14fc6ae263977f56c7c98b568b59ee3a488c09d86803eb89fbb055696bba50207d7ddfa593e9544fa3e544d40d34ae46a34089f0f59c08dda1ee60aae56cfc8ecd08a30d58b84c750b25790ef94774503f419bf22af594859fded6f38cb2694de27ddeabf93a8da5c3c256b7a4089619cb92073c40f93adc10b38c99813c725f773bee52f142965e5d9f08009a8f945abf720aec33fdd4ed2b8b3f1c0f5b9707862ca19295054c0508caec9722a1e7ff2bf4f85f711013a09eb2dbe5af9e966620c09e2ff9d4f35449f8bab74b6052ecafe1f858eb0bb2140ce0ce9c3e0413a06f53b3153f377be1c0447758be706e3b4c8e18926bcdd30ae06a8667a804359ad68a82cd6590be8303c19501d5ab21c80809bdb79417200dd615b427673c279de704628524eeba12b92cd59ac4fe6c311d26bcebc27cb27a7f8aa1d89b178dfaf2a1f734f43ff43c20bf801d50d5eebaed2e0048a703fce98ba033bb5adf45aafb2c37f13e069a74f747bb2cd813d8cbb8440965cbd452734a4fcc22a0aca83cc582e8f6fa8a71cdb323d2cf6bce2448edbd31cdab05ff0dd7cb408fe593dbe36527673cd4d476222a8635192ff68c7cb37c085e735fd5e420bd8d50384b02adffe391fde1f3f45babc4ade410aef4d98eea620b9ec5261d <<< 58287)

/-- The row differing from `A0` from wheel 53,208 up. -/
def B0 : Nat := A0 ^^^ (0x529b4841c6d6a5af107a600fbdbffa16f83f1ab92502e1426890ebc36ccde71f6b244379f692ad88cae94923753b01fb9c28bb8489b4337629ed80edfdb8b96d891127d5ceaa5818150c78207bd7d10129b27b293fa659efb1d0b30c0c83c1047168fd7519117decc293d4cd6170cd3554f96af927ef4b97375a3205869d6e254323463cdebb843dc00deafc95b68179aef8cad09e2fa80c011b44e35ef2d0165856b745389a6532a0a95c35f4d441eabbd0e4fa8dc64fe5a76b83a251c3560e170808bb6294c322e91c2e3590613eb1139c7dfd2542b28f99e1e6045951b9cfa4b8fcb0837f6926f6eb174104eca8d4c617f41007a0ff28790e41d075a0faade42ba74a3ed52a638d5d98cbdef768b218f3a10ba43e425bae47e91ba9d0f8950f4aa628f14c235f47a72232ae7e688de311e2d6138c6878ff1e5ee55f986634f699e3d82aa41fa3fa671813c5ffc59e465f25a13a3747888f1a13abff303fb2f1dae3bdc22ae4877e9840a85c5e4677509ff93750d3aea93550806bcfa90818606407cb05118a704345e8727fc8d690c362ba8c4f87089158d1b13858073afa0a5b6fa3f9a3dac5b8a06e8e33f7b47ede0d200bb13b4c363f1be6bf003d2075d0db7ca048e42e69773b4665c2542ee5959e8e19d0da3a307108e4b0a6520b826959f6dc7542a8347d1435f8ba7d30ee6686470b24fbce912fdab134d269de69ddf23633303ba4a5f5bbaa5528c74ba7b753503f42a05f4246d3d59feae415f888288d7a9d215000832c65059e37e4381cc13c84aeadc8fc516cada6e6a18b49acf6903652338defe72a554d9592da844a5a93bdde1c00df9282f1cfc21954e17e25bd16e48830c415f33df03a24222d0e841913bda85a9a2e0df091ed3a590b2274a2ac64a4e7c79fb1e68d9896420f8dd724e0b627e470bcc03b88686ce858682b0a7298e011ae12fbc979dd6f2974d0ec54daa1b04dbe386cf24caed90ac1f5972db861713ea05bc7660367374a95a0a7ca2573290eab4235e8d3516dd59ddaa53bae02fb9a0132ab2002ddf2d8cc054f5d97082addd092b4e30161f8bfa598292e0a28fd6baf469a283fc0bbb71d30d7c7b44f149a0e20255e349298b15446c2caa55e74e2780aaa7ceb524c274d72c0bb2f12f47a69d178629156f0268c90a3f7505d88b31b809e453ee96006532010b7efc9e266d8d137b59f24a4a1719deb08338e98029891eb937f74f7914b89b91496513c9caefb35dacdab4711443cc7868a9921b17458b9fdcf8657e4ea7923f8fe6113bed634d5a90f55323fc803d9078dfa84eeaa1450346ef555dadc53f475570b545b7905435fc09702aaf84c60146f875b4fd41108215b75674a851b6a358d7185f16486cc7b6066d52eac9e1a79126076d0e68bbed3381066b1a0d8dcb32db1a43f3233a7bfca12199a9b6daee8e7d1427a024f1ca5b34277f35075ff741bf7d9db23aec23aea897d47806c36199757aa8c35a49aecf4fae14ce9878c754d167c9125fc375cefc7a99c3b18d521170f2438f755e6f8f23adc38aa24c613fc0af8130cfeb601ae46cacf99520d73d3497137d699fb496a418409a90d34d2051ba9f93fc3c18f2a92830ba5fdf8fc51b5579762cefda02ea813c8e86ad7f1c84f79cc27a67ea4a4660a238c6464ed74b826db5eff85d62a59379ff52a97d37e9e188ad585c169e538567f98e3815807cf427d1a68c4b573e1745ca458ceccb5a02471b7740949d2d7cef98c61de29a8cb19f7a4505b64250d86670911b42e2a0c4d1dc8d1ed02a952f3d19294378a99e74e9fd0ff5f43cf879e71c1a0ffe5b01e69b0ad47a77aa4eee68fb9946fcf67a7790b8677dcdd0e00c4740e5ca556262d92120c29d583487a98e313aa60a133a235f1cf44bd3165824c6f165627a8076ed337e8147379224b9933b12ecc8659fe0f07581cfcf2d6959301a093d71ad66c1325a86eada4522f6e9aca732d7398167b1c56069dcd6b6d5373022fef30b84886cc41b6ed2f8e38c9c8cbd5e60fbd38159364db180372c8b870db47568eee02bc9434c27e03c59af0ecc2810160ad3d2008144a2a68ad7085605866ecfd553a72a118ab28c48956bd32362f7d5ff3f7de3a32afdb73f6aceff46f1f8a3d51ec080935788f394d05dfb236512ae80f04f045d69c14529e8f06eb91de745e27ef51fcdffa30ce3cce9dd4cb56326170556f7a20d5b105e6e7c8032d0330327f1c577a4cb3e4335cb3be6c252bef702c41bc797768b6d5b502a66c80dde99cb3cdcfd8ab24eef57f9d3fb7618a550da17dad9fa5b8a362523f6eb31d67fc0b3bf2fe771279e741fa31ffb7f2b2e12388b814e073d70ddcdcdf5b5fa08b61b421f0bb7b9ff91227fbf90b0e530da5fdb8562d731dad807e5b92d8d80df5fb49a77c5bd5eac6ef73e526370df3f5a5b474d1094ed74efb9f386dd3e351fb6b0a8c5cc13c981684fb101fa4405998564b9737dc7930f506f96b6c62212e96444910af937dc53d05a4955be4ff706b8472c1420d37200748d2e2f949faf953d57142a3d30f93c4fe52fc5d00f9aa2d0d381d867032823b80a4923032e7dd30218e751e8fa98c2d915b469710d1de968fa6397c3e65bfec726e95d4e21418c66c62a7e454e32dbbf8f2bdcb3fc2b182a7cbee9e55ab20f8524016364a7f56f24a6ad1a1c6d351a7aed57e443d7f367b40b7fd677afe9f0aa53af892a96b8ee166f26d4d5c1424edea25aaa2d1307cac8281a9d087d13bf9d3fe7f84846bee744a02580380b2c53cd26efbc44a9df5aa1931e83941766815a9ef9d35b6ff60a07692231b71c101b77e7302edb13494badb1682505246ce32a509b3685df82bf24d5994571f0d1a5c9124e6dae0ba42b7a60df0eb5ffa6c5e4763ac8c225137d54f306d3443b38ba932a50fe9e6c083a3b246c8c1a98e3dd0f12ec1cb28568badac22ac9b62e0adc39de0da6e973fb3e5d76469e65e02b8f67dce2a0060c7d84a3d8eda79a51dcb0625f571b35f103b887b5594918aea0998c19dd38322180e6faa5eeec275f7f9886b517bba46dfbb5a36b994c4ca9d94368e3d4898c4b28ce280a9c41330c093eda78b54fd6502de9164be7c7a9f029bc50f5a0ebe2546a9020e98d8e7f5c3d37b1e892c65a2919af298b36ed7c82006ef63c9514e83a74bb6fa29f4b8a585fb33ddd25a66c23d85a48bf6468ff890b313144b8b1472914e8823d2473c34187975514f011bf59dea5c57238acfc3139bc74ded36b29c60e88e42369691f45a31d853c5bdcbc6521d3c284836a2d66b5a1cae41be8587a7ed483425141d1415f69e28a7b509c622b4f6dd679343ee32548e058953ce3489b2cb2ecf9aba6d0c0cd0d8be998f55db3aeef9a2e979500f41194bc2a282c7d56aa0157a85567c6b5ef0bc413a186fbdae04805a53f8770156e8b9e820dbf41d0d93e42f72c86077a1bb18dfe9432c4528a25ca6ff87b89c297be587518e4c7984f88219a2bb2baa2bf3e2629853b908bd70ab2193571a6026416d9899710fc806a47949e6570a9cc8d16f5e1a6429d993666bdc4563d3d62dc333aa734952feb4a3f5360a4312adc33fc38521218e352c8a97692dd6f7948ebf854c812dc5f804f8231fbc922782733225c737f647ac743a072a7841e3498dfdf4a2b0de47c5049738b02136f800f80dfe22e09053488bc3d9ef93c869e80e85f8cacbb603684f6bc96149367b5e4cc9bf4c891b37dc885c844b541c718b7abd1ad3caadd9098aad42ea8588c9bcf6c22480d5fa1000e1a3d368f0717e0b0e2d6719aabd6ae84692c043dbc687cff769952447b0c873a8776ee22e7beb0f5b8fa4f6d5cebc4573123266bfd7ce0f07592adf4118e7d02ec473269fd8e389601a20b10b31cf70c9d419b997bb1415477420253683ba5e8d576443d1be3d35d9ff835d3de8de85002c1c8dabbd612144fc260a49188578a1a3ae629e48ddfac9a8e565f618a16af73eb459140b14ccc6e6ddba9912341f5d8b817d539efe95aecc685c47640cf34de3cb5420e38f0afd1ae744782b43d80efacf0b9fdf5a8c540fadd0e687a5837d79507a403ed21d2eb66a9eff5996cce684a2de028a105fbc4b22afa794cd154f11b907438486f8131b2c9e7f6d6afa284e7fd910d94360d6c895812002b25e1cf3cf7fea96d794721ef05baea79f9fa3999b0c3ea95851129176c0fe88c0465effb21918536c4f2943bc19059899de07fbd9185d2bba1ecd69a63c57fc0cc9c86379727e7c20a8a2f94724a0cc561d26b435b696a37cd238e557a6521b45f7077dd997765b8017ad93e43d1e8c72ffc2e998e79e7357c54caa81f98482e16da5ad69e990efbc3896ecec7e490257ee42b3e70aabc57252b6761bb81d1f13764be7372f56f7d7720f248c99dee030eb4090a35daf3d6ed48d6e35531bcfe94ffb60c823cd90d9b7f5955a0035c2c1e3715202b2859e8ac1dfec3a0830afd7c02c8961800f8dcc912ea5653640bc782646b089680470ddcf5aa670d74273ba9de0d3457e85aa89bdd590cf8ce0ad7a930e0709d6646a5670ecac92d5e42d4b5a012e72122f18eb8df52b8d323cb2767a3e18919771cec0f469837a103547d8a66b4621d8c6bedd58de8df2896cb91c64806495b940f478679f6efc0af26a56c7055f22a91bfcc378f0d110b6c00630ec821dceca5b1ce516e84ae7b73d40196b4aa865940d6443061e9dca9648f7720a63fe57e6950e9737454b02aa00e13674fbcd0b056c442e3f0ceceb34cf35069427a598a02b44ddd02e1d5f289f4e01a71e261ee8f30a296d1d2da6edb32a8a1233b310ac0ff46b94f77d183b1bbc14fac8bf9a85631b73135e7daf427d101de90cd48a288d0078cab961c5af3f77d0c6e86279b85a3a9fdb884e58880558b1b70d922f8f0802d05eef9a3b24a552ed2405abacdb430eab1dffa8404d956619b344ef4ad5ca1de19a3d744efb04572d896bb91caa0d3d7e6521d3b18616cb934a3ad575434cbaa618f57ad23d0fbc295ea8cbc73266243540fdc0d4b6a9b463265cafc287bf057ff3e64ffcf0d0a9d08bc8e6c826bf2a059364085b0265bba0dee93fd846d30e6c1fc4788676b0db51319ade2ccd82d7d6c7d8e22b35316923bf1b1039f8410266d597fecbe890343fce6d701589c80bd29ab2dc715dc27683e7c24a1b6f2e693d13ad6cb34545a3192aca0793b861641a40171e8c4160879cbca9e74539b96c4d231c4f4c7803160707ff14162d2e2abb0e545888987cc9f9c0b05ec65204f6dcdb1e081490612ff28ca5e8c96e2da6fc6d0abe126482c040eac9694836a42a215f20fa8ebfd29212167c79916a4f1ebdd1a226a974f2a929e07206e74ed9c5f018e06f758192956ffb8bd3f2a2d80a9b68a6b5d89e01896db6c47f6f52d15aaa6f264fa9df140db8d56fd4877385eb43938458d57036185fe1dcb54768e5b3215eecc2a80e646d310d9a5de4455704fa33f6fec6e05c04074d5c8d55520677ae65cc76a7788cc82f763648bc6ac716fb802294975bde5e4b9b5cda4a513d12ea17da8cb396d041b64edfbec8f8dd5f5d7645281934eebe2549cf0dc0110880e6ce05acf6bacbeac7d301df53d0de316cb4211f479081a69984f4c1074651d5875dba88ea741976e31fbfff2a59e603d11de50a04bf3bdfca8e85e2fcd33b727f20e5b3a1ef190d22c6f1dbbe2b1c1c0aaae1becf392ff9af529c4c2764b3fae74864cfb889311a4e6f2b8c1f40cd9d071ea021613c4f2216c5dd219c24dce3f106d66d020692d4e8857769fff3fcfd5beffa39a79ba356abc379fd27275809ef09fa51d025392d687011d672c3d407a9e80624c4fcd04555171d5f2d430e418414b749dcd7cd9bc32516dcd9471e0b25a610f557ab6d6bf9fdd19b0697af9f35bcd42d7110d351460c55cf79d5b6e24a7d8c53a048d98186c597dc5d76a3b09c34a04887a0d3ba630df06682c473c9b2b899bf37420de14a51d7539bdc7424022c31339eb7a5d291216ce89e9603b9c398aca778abf421afeebd3c30e222312abd1167205c77a74d9d373472020a592a769abbf9243dc9b3c5be7097561776ef63c96120e7add <<< 53208)

/-- The row differing from `B0` from wheel 72,576 up. -/
def B1 : Nat := B0 ^^^ (0x1fa839468cc7c7b58481761d18eb75a8a6dcfb69dde1d505f90b57ff3ca208850435cc691d91cb5b75fbab412f1453f40ad612d500e13ca43cd9bb47b7234a8baea3809cf1410561330f83acb065e17fa30b4661b4e2d64da86c3d67c11bf9999837cdcccb53728dbee0a98f7ee8b7fe9347c852d3dfdba4eac4718e68dcbfc35d8cd0ec69d2e8d1ab64f253508efa4ae34f7613b4f25bc5248aeccd803ffeb1b56a66c3d18586b782f5bfdf5360d55d5a39d014ce2cfc6a092502586eed56087e26f150a61b2858510b7bc75eb63d76d46b42754dd1ad07d18c168a614e87e093fc5639c9826ca55f44ee1e85fd2604bf533f1dd94a6b85c75feed24eb1f0c3a2817167421c0ea8d6b2110c1c6315a1badff6be227f6f763067c2417f95438140e4a5166ed5da4cd4b201a916810a2b582cf414b8728fcfffce74209bfd63abdcf88e58ef9659fed6faf16233724383d21de3b99f031e7ba24ba811550cd55bfb62f3adbddebfbb0a2bae51b1f4afdfe50c0fd843b1b7057fe8ea23fa8fb27a20ae13a581df7a2e7d2f3a321e7e55930475b0318f6513f270bd3f9557b9aef0228e8c9276e2746272ba0bf76b25e143d144018ea6fdec0e3408fa19d02f8ac1a7724426c84b5e1a566c64386980a81fe216344f4d3776f2decc4957ef412873d56f270a2341b85bb7053e246ea197a49486044f4e5f6d8f58ee6e300e97ab38878c04d98883ff8b894c86d91a05e4827eed9e07aa53a93ca1ad1c01b0ce163bd7f8e935428184f459116788cd4f1173852a2c9bbb3cb48e9debda8693ebb029eaffab3bd820f47ca7abac77b31f17e1b8d5a52a908dc3faa2dfb92fe1626a2173a48c9626f3ed427ded05c544a6b382b663c4dd1b0d6001176950f8b0852b8cb27ba68b2f56fe6384f2cac1d4628006a93c19a43e470ffe64c7bcb8b2ab9b34707ee40ef82cae6f7bbae0edb78fc715d558ea48a9a5e91bd9bbc9efe1ae66f3d3f3e02980b1172a57577d9c3c2b6219df6aa99314cae7d30ecc6ff05cc55eaefb1a435d887cf087cde8d8d1f38c9881149e6bdbd6f20576bf8f5920cc4f7bc0b1248fb835114833e31b455b091e4ac2b9c427a3f1b8d3345366331a1fdf7f4164770cf10d76a4c260a002c24f52453f81ca43a2a0f9bc849cbe310c8de16d539141599c2d5e69005751790e5ceca1c58bb55b2065b0001124aa70856084cade46f1923a3be18a37c5f23dc496354d9614964a63f1585ffa8c9186b4e19cc00b683713d3ba1eed35e65a261db2fa4b4fee4b2ed521ff149d5b2e1d23624a27a05bf1819356e3c1a508451add7a1a2f2e941eade686ee59bd3b1149c27cc1738474bf05e5055bdb8a062ab1a4726bb3e3a5b42702a78bd9db0e0c1d1302715b4df6344eb6e8c1bdec8160762ac95bb092fe3a40c07c9bc3648c83a93d17a46e907ff96e4fb3e35a53fce40fd480c82f2a53a9f3c3a82daedbdc03d733eca71f1f2d280dc1c73702d0cd384d1056c36f287d42c1bd0b78b99c8bc4e891250c6fed9897f464b2689209b91e8b49db040ad698d91c735c0eb6946f498064bedf1f9f85f2959d1fb95f6b73ef70d3c9b92aa0a082d325d106d43f7c6d452e42416b98119c53b6a1ca6a61e095b752235513c089f333664e56c88272de9776336b369e82b720bda9d82d433e94e927ccdb5b42f95d955dd300efaf73b7ff46a3b0e173dd7d8ae62ac70c131251f2d1a3dd59d61f0f15c8d160b41befa7b77cb9d58c06019a91389919f9a62012f8d4cbb822b2300e40d3efafbd584b2f0d344406ec3467dec97dfbbed729e965aae3a69b858b91b4c5e6bf18f291faf55f63d0c33b2b5170578d975f720339d99911f6465be3dcd84d9e4ff0bd7fc12642cde4291b1766ebce3f989b61346e2b3815947880ac70052e0e3082137c7eecca1605bc1e0328e3f8f09cf9ab50941d7846a8d90f52d0120cc8c7211f5badc5b79c7170ad6d0521a703a3a180743397a353645ec48b1577f13700309b37d7fc122d70c820c9e3f0a6aa1481003f4976ff69164b6fc696d48087c25ff44fff24d57e49603ab8f9b1e9f5043b247a0fa570f772badbae68fe8af6c5afd59792eaa30dc4c2be2907bbbbaaf4070d9c8e9179b28fdac2c8af1917fed1944269fdf6008334729475692015e54fae7f1394ffb2bf82c0512a572fc7779d05711a4cd5312c046c7c1f03c1044dc65c3c7f47dcefc069183ad0cad354b9aba7388e530101d21ec650491feb53b3bb544ec6eb6e73ee7455e60f79cb1142cd0827a028cf485886c96a7899783f20d3e0750c3924a6562de6c42e34a34ceaffe43238e2976a4477e67778e152be60f0bf3f579bb9a960116d12f5f61be47077ba09f2178b30c5524c58dc0bf5e6c968748be947a90755f20bba4b7a025128c88e52bcebe632fd226da3c26d0bfad40da95067927e08695f03fbfb493f9a895111232ec21b48d6e94af26ab2a6e55301bc46bf65b517c84bff8147fd9142031976d760a2a5280da5d4ca6b19d6d2653bc7619fd11bc4e353f37ef6a90a3ed9a21afb485b349ea4244bfde2ee6f63d682b17e642ec11825979ec67ca02ae8926fe1edaa4ddb1898b7eb9f0bc7fc32cdf5692504205110b2e1e92b10ff2e70c6a7acffce2004ca9f3967e3ec9a9ec90b7ca057a8caadf2e726494c02f0de967d4378edd <<< 72576)

theorem A0_return : rowAt 87867 A0 16 = A0 := by decide +kernel
theorem A1_return : rowAt 87867 A1 16 = A1 := by decide +kernel
theorem B0_return : rowAt 87867 B0 16 = B0 := by decide +kernel
theorem B1_return : rowAt 87867 B1 16 = B1 := by decide +kernel

/-- All four rows are finite, with their leftmost black cell at position 0. -/
theorem rows_finite : A0 < 2 ^ 87867 ∧ A1 < 2 ^ 87867 ∧ B0 < 2 ^ 87867 ∧ B1 < 2 ^ 87867 ∧
    A0.testBit 0 = true ∧ A1.testBit 0 = true ∧ B0.testBit 0 = true ∧ B1.testBit 0 = true := by decide +kernel

/-! ### Below the first fork -/

theorem A0_zero_phase : ∀ r, r < 16 → Sp A0 0 r = true := by decide +kernel
theorem A0_one_phase : ∀ r, r < 16 → Sp A0 1 r = true := by decide +kernel

theorem A0_zero (t : Nat) : Sp A0 0 t = true := by
  rw [Sp_mod A0_return]; exact A0_zero_phase _ (Nat.mod_lt _ (by omega))

theorem A0_one (t : Nat) : Sp A0 1 t = true := by
  rw [Sp_mod A0_return]; exact A0_one_phase _ (Nat.mod_lt _ (by omega))

/-- The white wheels below 53,207. -/
def whiteMask : Nat := 2 ^ 2 ||| 2 ^ 7 ||| 2 ^ 28 ||| 2 ^ 399

theorem black_mask : (orRows A0 16 ||| whiteMask) % 2 ^ 53207 = 2 ^ 53207 - 1 := by decide +kernel

theorem black_or_white {m : Nat} (hm : m < 53207) :
    (∃ r, r < 16 ∧ Sp A0 m r = true) ∨ m = 2 ∨ m = 7 ∨ m = 28 ∨ m = 399 := by
  have h := congrArg (fun n => n.testBit m) black_mask
  simp only [Nat.testBit_mod_two_pow, Nat.testBit_two_pow_sub_one, Nat.testBit_or, whiteMask,
    Nat.testBit_two_pow, hm, decide_true, Bool.true_and, Bool.or_eq_true, decide_eq_true_eq] at h
  rcases h with h | h
  · exact Or.inl (orRows_black h)
  · right
    omega

theorem strip_shift {m L : Nat}
    (h1 : ∀ r, r < 16 → rowAt 87867 A0 (r + L) % 2 ^ (m + 1) = rowAt 87867 A0 r % 2 ^ (m + 1))
    (h2 : ∀ r, r < 16 → Sp A0 (m + 1) (r + L) = !Sp A0 (m + 1) r) :
    (∀ j, j ≤ m → ∀ t, Sp A0 j (t + L) = Sp A0 j t) ∧ ∀ t, Sp A0 (m + 1) (t + L) = !Sp A0 (m + 1) t := by
  have ht : ∀ t, t + L = (t % 16 + L) + t / 16 * 16 := by intro t; omega
  constructor
  · intro j hj t
    have e := congrArg (fun n => n.testBit j) (h1 (t % 16) (Nat.mod_lt _ (by omega)))
    simp only [Nat.testBit_mod_two_pow, show j < m + 1 by omega, decide_true, Bool.true_and] at e
    rw [ht t, Sp_add_mul A0_return, Sp_mod A0_return j t]
    exact e
  · intro t
    rw [ht t, Sp_add_mul A0_return, Sp_mod A0_return (m + 1) t]
    exact h2 _ (Nat.mod_lt _ (by omega))

theorem per2 : ∀ r, r < 16 → rowAt 87867 A0 (r + 1) % 2 ^ (2 + 1) = rowAt 87867 A0 r % 2 ^ (2 + 1) := by decide +kernel
theorem anti2 : ∀ r, r < 16 → Sp A0 (2 + 1) (r + 1) = !Sp A0 (2 + 1) r := by decide +kernel
theorem per7 : ∀ r, r < 16 → rowAt 87867 A0 (r + 2) % 2 ^ (7 + 1) = rowAt 87867 A0 r % 2 ^ (7 + 1) := by decide +kernel
theorem anti7 : ∀ r, r < 16 → Sp A0 (7 + 1) (r + 2) = !Sp A0 (7 + 1) r := by decide +kernel
theorem per28 : ∀ r, r < 16 → rowAt 87867 A0 (r + 4) % 2 ^ (28 + 1) = rowAt 87867 A0 r % 2 ^ (28 + 1) := by decide +kernel
theorem anti28 : ∀ r, r < 16 → Sp A0 (28 + 1) (r + 4) = !Sp A0 (28 + 1) r := by decide +kernel
theorem per399 : ∀ r, r < 16 → rowAt 87867 A0 (r + 8) % 2 ^ (399 + 1) = rowAt 87867 A0 r % 2 ^ (399 + 1) := by decide +kernel
theorem anti399 : ∀ r, r < 16 → Sp A0 (399 + 1) (r + 8) = !Sp A0 (399 + 1) r := by decide +kernel

theorem strip_step (m : Nat) (hm : m + 1 ≤ 53207) : (∀ T, ∃ t, T ≤ t ∧ Sp A0 m t = true) ∨
    ∃ L, (∀ j, j ≤ m → ∀ t, Sp A0 j (t + L) = Sp A0 j t) ∧ ∀ t, Sp A0 (m + 1) (t + L) = !Sp A0 (m + 1) t := by
  rcases black_or_white (m := m) (by omega) with ⟨r, _, hc⟩ | rfl | rfl | rfl | rfl
  · exact Or.inl (blacks_late A0_return hc)
  · exact Or.inr ⟨1, strip_shift (m := 2) per2 anti2⟩
  · exact Or.inr ⟨2, strip_shift (m := 7) per7 anti7⟩
  · exact Or.inr ⟨4, strip_shift (m := 28) per28 anti28⟩
  · exact Or.inr ⟨8, strip_shift (m := 399) per399 anti399⟩

/-! ### The tree -/

theorem white_53207 : ∀ r, r < 16 → Sp A0 53207 r = false := by decide +kernel
theorem white_58286 : ∀ r, r < 16 → Sp A0 58286 r = false := by decide +kernel
theorem white_72575 : ∀ r, r < 16 → Sp B0 72575 r = false := by decide +kernel

theorem low_B0 : ∀ r, r < 16 → rowAt 87867 B0 r % 2 ^ 53208 = rowAt 87867 A0 r % 2 ^ 53208 := by decide +kernel
theorem low_A1 : ∀ r, r < 16 → rowAt 87867 A1 r % 2 ^ 58287 = rowAt 87867 A0 r % 2 ^ 58287 := by decide +kernel
theorem low_B1 : ∀ r, r < 16 → rowAt 87867 B1 r % 2 ^ 72576 = rowAt 87867 B0 r % 2 ^ 72576 := by decide +kernel
theorem top_B0 : ∀ r, r < 16 → Sp B0 53208 r = !Sp A0 53208 r := by decide +kernel
theorem top_A1 : ∀ r, r < 16 → Sp A1 58287 r = !Sp A0 58287 r := by decide +kernel
theorem top_B1 : ∀ r, r < 16 → Sp B1 72576 r = !Sp B0 72576 r := by decide +kernel

theorem wA0_low : (orRows A0 16 >>> 53208) % 2 ^ (58286 - 53208) = 2 ^ (58286 - 53208) - 1 := by decide +kernel
theorem wA0_high : (orRows A0 16 >>> 58287) % 2 ^ (87866 - 58287) = 2 ^ (87866 - 58287) - 1 := by decide +kernel
theorem wA1_high : (orRows A1 16 >>> 58287) % 2 ^ (87866 - 58287) = 2 ^ (87866 - 58287) - 1 := by decide +kernel
theorem wB0_low : (orRows B0 16 >>> 53208) % 2 ^ (72575 - 53208) = 2 ^ (72575 - 53208) - 1 := by decide +kernel
theorem wB0_high : (orRows B0 16 >>> 72576) % 2 ^ (87866 - 72576) = 2 ^ (87866 - 72576) - 1 := by decide +kernel
theorem wB1_high : (orRows B1 16 >>> 72576) % 2 ^ (87866 - 72576) = 2 ^ (87866 - 72576) - 1 := by decide +kernel

set_option exponentiation.threshold 90000 in
/-- **The classification.** Every array with the left-diagonal recurrence and a black wheel 0 carries, after one time shift,
one of the four strips on every wheel through 87,866. -/
theorem classification {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, Aligned a A0 s 87866 ∨ Aligned a A1 s 87866 ∨ Aligned a B0 s 87866 ∨ Aligned a B1 s 87866 := by
  obtain ⟨s, hs⟩ := universal_of_strip (J := 53207) (by omega) ha ha0 A0_zero A0_one
    (fun j t hj => Sp_rec A0 j t (by omega)) strip_step
  refine ⟨s, ?_⟩
  rcases branch (v' := B0) ha (by omega) (by omega) hs (white_of_phase A0_return white_53207)
    (fun j t hj => low_of_phase A0_return B0_return low_B0 j t (by omega))
    (comp_of_phase A0_return B0_return top_B0) with h | h
  · have h2 : Aligned a A0 s 58286 := extend ha (by omega) (by omega) h (by omega)
      (fun m h1 h2 T => black_window A0_return wA0_low h1 (by omega) T)
    rcases branch (v' := A1) ha (by omega) (by omega) h2 (white_of_phase A0_return white_58286)
      (fun j t hj => low_of_phase A0_return A1_return low_A1 j t (by omega))
      (comp_of_phase A0_return A1_return top_A1) with h3 | h3
    · exact Or.inl (extend ha (by omega) (by omega) h3 (by omega)
        (fun m h1 h2 T => black_window A0_return wA0_high h1 (by omega) T))
    · exact Or.inr (Or.inl (extend ha (by omega) (by omega) h3 (by omega)
        (fun m h1 h2 T => black_window A1_return wA1_high h1 (by omega) T)))
  · have h2 : Aligned a B0 s 72575 := extend ha (by omega) (by omega) h (by omega)
      (fun m h1 h2 T => black_window B0_return wB0_low h1 (by omega) T)
    rcases branch (v' := B1) ha (by omega) (by omega) h2 (white_of_phase B0_return white_72575)
      (fun j t hj => low_of_phase B0_return B1_return low_B1 j t (by omega))
      (comp_of_phase B0_return B1_return top_B1) with h3 | h3
    · exact Or.inr (Or.inr (Or.inl (extend ha (by omega) (by omega) h3 (by omega)
        (fun m h1 h2 T => black_window B0_return wB0_high h1 (by omega) T))))
    · exact Or.inr (Or.inr (Or.inr (extend ha (by omega) (by omega) h3 (by omega)
        (fun m h1 h2 T => black_window B1_return wB1_high h1 (by omega) T))))

/-! ### The four are different, and every row is on exactly one -/

/-- Two strips related by a time shift through wheel 87,866. -/
def Related (v v' : Nat) : Prop := ∃ s, ∀ j, j ≤ 87866 → ∃ T, ∀ t, T ≤ t → Sp v j (t + s) = Sp v' j t

theorem not_related {v v' w : Nat} (hv : rowAt 87867 v 16 = v) (hv' : rowAt 87867 v' 16 = v') (hw : w ≤ 87866)
    (hc : ∀ r, r < 16 → Sp v w r = !Sp v' w r) (h4 : ∀ r, r < 16 → Sp v 400 r = Sp v' 400 r)
    (hp : ∀ d, d < 16 → d ≠ 0 → ∃ p, p < 16 ∧ Sp v 400 (p + d) ≠ Sp v 400 p) : ¬ Related v v' := by
  rintro ⟨s, hs⟩
  obtain ⟨T1, h400⟩ := hs 400 (by omega)
  obtain ⟨T2, htop⟩ := hs w hw
  by_cases hd : s % 16 = 0
  · have e := htop T2 (Nat.le_refl _)
    have p : Sp v w (T2 + s) = Sp v w T2 := by
      have h := Sp_add_mul hv w T2 (s / 16)
      rwa [show T2 + s / 16 * 16 = T2 + s by omega] at h
    rw [p, comp_of_phase hv' hv hc T2] at e
    cases h : Sp v' w T2 <;> simp [h] at e
  · obtain ⟨p, hp', hne⟩ := hp (s % 16) (Nat.mod_lt _ (by omega)) hd
    have e := h400 (p + T1 * 16) (by omega)
    have e1 : Sp v 400 (p + T1 * 16 + s) = Sp v 400 (p + s % 16) := by
      have h := Sp_add_mul hv 400 (p + s % 16) (T1 + s / 16)
      rwa [show p + s % 16 + (T1 + s / 16) * 16 = p + T1 * 16 + s by omega] at h
    rw [e1, Sp_add_mul hv', ← h4 p hp'] at e
    exact hne e

theorem prim_A0 : ∀ d, d < 16 → d ≠ 0 → ∃ p, p < 16 ∧ Sp A0 400 (p + d) ≠ Sp A0 400 p := by decide +kernel
theorem prim_A1 : ∀ d, d < 16 → d ≠ 0 → ∃ p, p < 16 ∧ Sp A1 400 (p + d) ≠ Sp A1 400 p := by decide +kernel
theorem prim_B0 : ∀ d, d < 16 → d ≠ 0 → ∃ p, p < 16 ∧ Sp B0 400 (p + d) ≠ Sp B0 400 p := by decide +kernel

theorem pair_A0_A1 : (∀ r, r < 16 → Sp A0 58287 r = !Sp A1 58287 r) ∧ ∀ r, r < 16 → Sp A0 400 r = Sp A1 400 r := by decide +kernel
theorem pair_B0_B1 : (∀ r, r < 16 → Sp B0 72576 r = !Sp B1 72576 r) ∧ ∀ r, r < 16 → Sp B0 400 r = Sp B1 400 r := by decide +kernel
theorem pair_A0_B0 : (∀ r, r < 16 → Sp A0 53208 r = !Sp B0 53208 r) ∧ ∀ r, r < 16 → Sp A0 400 r = Sp B0 400 r := by decide +kernel
theorem pair_A0_B1 : (∀ r, r < 16 → Sp A0 53208 r = !Sp B1 53208 r) ∧ ∀ r, r < 16 → Sp A0 400 r = Sp B1 400 r := by decide +kernel
theorem pair_A1_B0 : (∀ r, r < 16 → Sp A1 53208 r = !Sp B0 53208 r) ∧ ∀ r, r < 16 → Sp A1 400 r = Sp B0 400 r := by decide +kernel
theorem pair_A1_B1 : (∀ r, r < 16 → Sp A1 53208 r = !Sp B1 53208 r) ∧ ∀ r, r < 16 → Sp A1 400 r = Sp B1 400 r := by decide +kernel

/-- **The four strips are pairwise unrelated** through wheel 87,866. -/
theorem four_distinct : ¬ Related A0 A1 ∧ ¬ Related A0 B0 ∧ ¬ Related A0 B1 ∧ ¬ Related A1 B0 ∧
    ¬ Related A1 B1 ∧ ¬ Related B0 B1 :=
  ⟨not_related A0_return A1_return (by omega) pair_A0_A1.1 pair_A0_A1.2 prim_A0,
   not_related A0_return B0_return (by omega) pair_A0_B0.1 pair_A0_B0.2 prim_A0,
   not_related A0_return B1_return (by omega) pair_A0_B1.1 pair_A0_B1.2 prim_A0,
   not_related A1_return B0_return (by omega) pair_A1_B0.1 pair_A1_B0.2 prim_A1,
   not_related A1_return B1_return (by omega) pair_A1_B1.1 pair_A1_B1.2 prim_A1,
   not_related B0_return B1_return (by omega) pair_B0_B1.1 pair_B0_B1.2 prim_B0⟩

/-- An array cannot be on two unrelated sides: two alignments of one array relate their strips. -/
theorem side_unique {a : Nat → Nat → Bool} {v v' s s' : Nat} (hv' : rowAt 87867 v' 16 = v')
    (h : Aligned a v s 87866) (h' : Aligned a v' s' 87866) : Related v v' := by
  refine ⟨s' + 15 * s, fun j hj => ?_⟩
  obtain ⟨T, hT⟩ := h j hj
  obtain ⟨T', hT'⟩ := h' j hj
  refine ⟨T + T', fun t ht => ?_⟩
  have a1 := hT (t + (s' + 15 * s)) (by omega)
  have a2 := hT' (t + 16 * s) (by omega)
  rw [← a1, show t + (s' + 15 * s) + s = t + 16 * s + s' by omega, a2,
    show t + 16 * s = t + s * 16 by omega, Sp_add_mul hv']

/-! ### The theorems for configurations -/

/-- **Every configuration with a leftmost black cell is on one of the four sides**, whatever lies to its right. -/
theorem left_side_classification {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false)
    (hlo : x lo = true) :
    ∃ s, Aligned (Ld x lo) A0 s 87866 ∨ Aligned (Ld x lo) A1 s 87866 ∨ Aligned (Ld x lo) B0 s 87866 ∨
      Aligned (Ld x lo) B1 s 87866 :=
  classification (Ld_recurrence hleft) (by simpa [Ld, evol] using hlo)

theorem D_recurrence : Recurrence D :=
  ⟨fun t => by rw [D_zero, D_zero], fun t => by rw [D_one, D_zero]; rfl, D_step⟩

/-- The single black cell is on one of the four. The proof does not say which. -/
theorem seed_classified :
    ∃ s, Aligned D A0 s 87866 ∨ Aligned D A1 s 87866 ∨ Aligned D B0 s 87866 ∨ Aligned D B1 s 87866 :=
  classification D_recurrence (D_zero 0)

theorem Ld_row (v : Nat) {j : Nat} (hj : j ≤ 87866) (t : Nat) : Ld (ofRow v) 0 j t = Sp v j t :=
  Ld_ofRow (K := 87867) (by omega) v t j (by omega)

/-- **All four occur.** Each strip is carried from tick 0 by a finite row with its leftmost black cell at position 0. -/
theorem four_realized (v : Nat) : Aligned (Ld (ofRow v) 0) v 0 87866 :=
  fun _ hj => ⟨0, fun t _ => Ld_row v hj (t + 0)⟩

/-- **Exactly four left sides through wheel 87,866.** Every configuration with a leftmost black cell is on one of the four
strips; the four rows `A0`, `A1`, `B0`, `B1` are finite and realize them; and no time shift relates two of them. -/
theorem exactly_four_left_sides :
    (∀ {x : Int → Bool} {lo : Int}, (∀ p, p < lo → x p = false) → x lo = true →
      ∃ s, Aligned (Ld x lo) A0 s 87866 ∨ Aligned (Ld x lo) A1 s 87866 ∨ Aligned (Ld x lo) B0 s 87866 ∨
        Aligned (Ld x lo) B1 s 87866) ∧
    (A0 < 2 ^ 87867 ∧ A1 < 2 ^ 87867 ∧ B0 < 2 ^ 87867 ∧ B1 < 2 ^ 87867 ∧
      A0.testBit 0 = true ∧ A1.testBit 0 = true ∧ B0.testBit 0 = true ∧ B1.testBit 0 = true) ∧
    (∀ v, Aligned (Ld (ofRow v) 0) v 0 87866) ∧
    (¬ Related A0 A1 ∧ ¬ Related A0 B0 ∧ ¬ Related A0 B1 ∧ ¬ Related A1 B0 ∧ ¬ Related A1 B1 ∧ ¬ Related B0 B1) :=
  ⟨fun hl h0 => left_side_classification hl h0, rows_finite, four_realized, four_distinct⟩

/-- The number of blacks of wheel `m` of `v` over the sixteen phases. -/
def weight16 (v m : Nat) : Nat → Nat
  | 0 => 0
  | L + 1 => weight16 v m L + (Sp v m L).toNat

/-- The farther words at the three forks have even weight over 16: 6, 10, 10. -/
theorem fork_weights : weight16 A0 53206 16 = 6 ∧ weight16 A0 58285 16 = 10 ∧ weight16 B0 72574 16 = 10 := by
  decide +kernel

/-- **Each array is on exactly one side.** Two different strips cannot both carry it, at any shifts. -/
theorem on_exactly_one {a : Nat → Nat → Bool} {s s' : Nat} :
    ¬ (Aligned a A0 s 87866 ∧ Aligned a A1 s' 87866) ∧ ¬ (Aligned a A0 s 87866 ∧ Aligned a B0 s' 87866) ∧
    ¬ (Aligned a A0 s 87866 ∧ Aligned a B1 s' 87866) ∧ ¬ (Aligned a A1 s 87866 ∧ Aligned a B0 s' 87866) ∧
    ¬ (Aligned a A1 s 87866 ∧ Aligned a B1 s' 87866) ∧ ¬ (Aligned a B0 s 87866 ∧ Aligned a B1 s' 87866) :=
  ⟨fun h => four_distinct.1 (side_unique A1_return h.1 h.2),
   fun h => four_distinct.2.1 (side_unique B0_return h.1 h.2),
   fun h => four_distinct.2.2.1 (side_unique B1_return h.1 h.2),
   fun h => four_distinct.2.2.2.1 (side_unique B0_return h.1 h.2),
   fun h => four_distinct.2.2.2.2.1 (side_unique B1_return h.1 h.2),
   fun h => four_distinct.2.2.2.2.2 (side_unique B1_return h.1 h.2)⟩

/-! ### The same theorem as arithmetic -/

/-- Each wheel's threshold can be replaced by one. -/
theorem aligned_uniform {a : Nat → Nat → Bool} {u s : Nat} : ∀ J, Aligned a u s J →
    ∃ T, ∀ j, j ≤ J → ∀ t, T ≤ t → a j (t + s) = Sp u j t := by
  intro J
  induction J with
  | zero =>
    intro h
    obtain ⟨T, hT⟩ := h 0 (Nat.le_refl _)
    exact ⟨T, fun j hj t ht => by
      have e : j = 0 := by omega
      subst e
      exact hT t ht⟩
  | succ J ih =>
    intro h
    obtain ⟨T1, h1⟩ := ih (fun j hj => h j (by omega))
    obtain ⟨T2, h2⟩ := h (J + 1) (Nat.le_refl _)
    refine ⟨max T1 T2, fun j hj t ht => ?_⟩
    by_cases hc : j ≤ J
    · exact h1 j hc t (by omega)
    · have e : j = J + 1 := by omega
      subst e
      exact h2 t (by omega)

set_option exponentiation.threshold 90000 in
theorem rowAt_succ_lt (v n : Nat) : rowAt 87867 v (n + 1) < 2 ^ 87867 := by
  simp only [rowAt, stepK]
  exact Nat.mod_lt _ (Nat.pow_pos (by omega))

set_option exponentiation.threshold 90000 in
theorem eq_of_low_bits {x y : Nat} (hx : x < 2 ^ 87867) (hy : y < 2 ^ 87867)
    (h : ∀ j, j < 87867 → x.testBit j = y.testBit j) : x = y := by
  apply Nat.eq_of_testBit_eq
  intro j
  by_cases hj : j < 87867
  · exact h j hj
  · have hp : 2 ^ 87867 ≤ 2 ^ j := Nat.pow_le_pow_right (by omega) (by omega)
    rw [Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hx hp), Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hy hp)]

/-- If a row's strip is aligned with `u`'s, the row reaches the number `u`. -/
theorem reaches {v u s : Nat} (hu : rowAt 87867 u 16 = u) (hlt : u < 2 ^ 87867)
    (h : Aligned (Ld (ofRow v) 0) u s 87866) : ∃ n, rowAt 87867 v n = u := by
  obtain ⟨T, hT⟩ := aligned_uniform 87866 h
  obtain ⟨n, hn⟩ : ∃ n, (T + 1) * 16 + s = n + 1 := ⟨(T + 1) * 16 + s - 1, by omega⟩
  refine ⟨n + 1, eq_of_low_bits (rowAt_succ_lt v n) hlt fun j hj => ?_⟩
  have e := hT j (by omega) ((T + 1) * 16) (by omega)
  rw [hn, Ld_row v (by omega)] at e
  have base : rowAt 87867 u (0 + (T + 1) * 16) = u := by
    rw [rowAt_add_mul hu]
    rfl
  rw [Nat.zero_add] at base
  simp only [Sp] at e
  rw [base] at e
  exact e

/-- **Every odd number reaches one of four.** Iterate `v ↦ 4 v ⊕ (2 v ∨ v)` modulo `2 ^ 87867` from any odd `v`: the orbit
reaches `A0`, `A1`, `B0` or `B1`. -/
theorem odd_reaches_one_of_four (v : Nat) (hv : v.testBit 0 = true) :
    ∃ n, rowAt 87867 v n = A0 ∨ rowAt 87867 v n = A1 ∨ rowAt 87867 v n = B0 ∨ rowAt 87867 v n = B1 := by
  have h0 : ofRow v 0 = true := by simpa [ofRow] using hv
  obtain ⟨s, h⟩ := left_side_classification (ofRow_left v) h0
  rcases h with h | h | h | h
  · obtain ⟨n, e⟩ := reaches A0_return rows_finite.1 h
    exact ⟨n, Or.inl e⟩
  · obtain ⟨n, e⟩ := reaches A1_return rows_finite.2.1 h
    exact ⟨n, Or.inr (Or.inl e)⟩
  · obtain ⟨n, e⟩ := reaches B0_return rows_finite.2.2.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inl e))⟩
  · obtain ⟨n, e⟩ := reaches B1_return rows_finite.2.2.2.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr e))⟩

/-- Each of the four numbers has least period exactly 16. -/
theorem least_period_16 : ∀ d, d < 16 → d ≠ 0 →
    rowAt 87867 A0 d ≠ A0 ∧ rowAt 87867 A1 d ≠ A1 ∧ rowAt 87867 B0 d ≠ B0 ∧ rowAt 87867 B1 d ≠ B1 := by
  decide +kernel

/-! ## The forced front -/

/-! ### Sixteen-bit words -/

/-- The word with bits `f 0, …, f 15`. -/
def word16 (f : Nat → Bool) : Nat :=
  (f 0).toNat + 2 * ((f 1).toNat + 2 * ((f 2).toNat + 2 * ((f 3).toNat + 2 * ((f 4).toNat + 2 * ((f 5).toNat + 2 * ((f 6).toNat + 2 * ((f 7).toNat + 2 * ((f 8).toNat + 2 * ((f 9).toNat + 2 * ((f 10).toNat + 2 * ((f 11).toNat + 2 * ((f 12).toNat + 2 * ((f 13).toNat + 2 * ((f 14).toNat + 2 * (f 15).toNat))))))))))))))

theorem horner_zero (b : Bool) (n : Nat) : (b.toNat + 2 * n).testBit 0 = b := by
  cases b <;> simp only [Nat.testBit_zero, Bool.toNat_true, Bool.toNat_false, decide_eq_true_eq,
    decide_eq_false_iff_not] <;> omega

theorem horner_div (b : Bool) (n : Nat) : (b.toNat + 2 * n) / 2 = n := by
  cases b <;> simp only [Bool.toNat_true, Bool.toNat_false] <;> omega

theorem horner_last (b : Bool) : b.toNat.testBit 0 = b := by
  cases b <;> rfl

theorem word16_bit (f : Nat → Bool) : ∀ r, r < 16 → (word16 f).testBit r = f r
  | 0, _ => by unfold word16; rw [horner_zero]
  | 1, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, horner_zero]
  | 2, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 3, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 4, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 5, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 6, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 7, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 8, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 9, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 10, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 11, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 12, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 13, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 14, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
  | 15, _ => by unfold word16; rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_last]
  | n + 16, h => absurd h (by omega)

theorem word16_lt (f : Nat → Bool) : word16 f < 2 ^ 16 := by
  unfold word16
  have h0 := Bool.toNat_le (f 0)
  have h1 := Bool.toNat_le (f 1)
  have h2 := Bool.toNat_le (f 2)
  have h3 := Bool.toNat_le (f 3)
  have h4 := Bool.toNat_le (f 4)
  have h5 := Bool.toNat_le (f 5)
  have h6 := Bool.toNat_le (f 6)
  have h7 := Bool.toNat_le (f 7)
  have h8 := Bool.toNat_le (f 8)
  have h9 := Bool.toNat_le (f 9)
  have h10 := Bool.toNat_le (f 10)
  have h11 := Bool.toNat_le (f 11)
  have h12 := Bool.toNat_le (f 12)
  have h13 := Bool.toNat_le (f 13)
  have h14 := Bool.toNat_le (f 14)
  have h15 := Bool.toNat_le (f 15)
  omega

/-- A word below `2 ^ 16` is its sixteen bits. -/
theorem word_eq {x y : Nat} (hx : x < 2 ^ 16) (hy : y < 2 ^ 16)
    (h : ∀ r, r < 16 → x.testBit r = y.testBit r) : x = y := by
  apply Nat.eq_of_testBit_eq
  intro r
  rcases Nat.lt_or_ge r 16 with hr | hr
  · exact h r hr
  · have hp : 2 ^ 16 ≤ 2 ^ r := Nat.pow_le_pow_right (by decide) hr
    rw [Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hx hp), Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hy hp)]

theorem word_zero {x : Nat} (hx : x < 2 ^ 16) (h : ∀ r, r < 16 → x.testBit r = false) : x = 0 :=
  word_eq hx (by decide) (fun r hr => by rw [h r hr, Nat.zero_testBit])

theorem bit_of_ne {x : Nat} (hx : x < 2 ^ 16) (h : x ≠ 0) : ∃ r, r < 16 ∧ x.testBit r = true := by
  apply Classical.byContradiction
  intro hno
  apply h
  apply word_zero hx
  intro r hr
  cases hb : x.testBit r
  · rfl
  · exact absurd ⟨r, hr, hb⟩ hno

/-! ### The words of a strip -/

/-- `w j` is the sixteen-bit word of wheel `j` of the strip of `v`: bit `r` is the wheel at phase `r`. -/
def Words (v : Nat) (w : Nat → Nat) : Prop :=
  (∀ j, w j < 2 ^ 16) ∧ ∀ j r, r < 16 → (w j).testBit r = Sp v j r

theorem white_of_word {v : Nat} {w : Nat → Nat} (hv : rowAt 87867 v 16 = v) (hw : Words v w) {m : Nat}
    (h : w m = 0) (t : Nat) : Sp v m t = false := by
  rw [Sp_mod hv, ← hw.2 m (t % 16) (Nat.mod_lt _ (by decide)), h, Nat.zero_testBit]

theorem word_ne_of_black {v : Nat} {w : Nat → Nat} (hw : Words v w) {m r : Nat} (hr : r < 16)
    (hb : Sp v m r = true) : w m ≠ 0 := by
  intro h0
  have e := hw.2 m r hr
  rw [h0, Nat.zero_testBit, hb] at e
  exact Bool.false_ne_true e

theorem word_zero_of_white {v : Nat} {w : Nat → Nat} (hw : Words v w) {m : Nat}
    (h : ∀ r, r < 16 → Sp v m r = false) : w m = 0 :=
  word_zero (hw.1 m) (fun r hr => by rw [hw.2 m r hr, h r hr])

theorem word_eq_of_low {v v' : Nat} {w w' : Nat → Nat} (hw : Words v w) (hw' : Words v' w') {j : Nat}
    (h : ∀ r, r < 16 → Sp v' j r = Sp v j r) : w' j = w j :=
  word_eq (hw'.1 j) (hw.1 j) (fun r hr => by rw [hw'.2 j r hr, hw.2 j r hr, h r hr])

/-- Every wheel in a window has a black at some phase, from one kernel evaluation (`black_window`,
stopped at the phase). -/
theorem black_window_phase {v lo n m : Nat} (h : (orRows v 16 >>> lo) % 2 ^ n = 2 ^ n - 1) (h1 : lo ≤ m)
    (h2 : m < lo + n) : ∃ r, r < 16 ∧ Sp v m r = true := by
  have hl : m - lo < n := by omega
  have e := congrArg (fun y => y.testBit (m - lo)) h
  simp only [Nat.testBit_mod_two_pow, Nat.testBit_two_pow_sub_one, Nat.testBit_shiftRight, hl,
    decide_true, Bool.true_and, show lo + (m - lo) = m by omega] at e
  exact orRows_black e

/-! ### The settling recursion as a state machine -/

/-- The wait from phase `m` to the next black of the word `w`, searching the offsets `16 - fuel, …, 15`; `16` if none. -/
def srch (w m : Nat) : Nat → Nat
  | 0 => 16
  | fuel + 1 => if w.testBit ((m + (16 - (fuel + 1))) % 16) then 16 - (fuel + 1) else srch w m fuel

/-- One wheel: from `(F j, F (j + 1))` to `(F (j + 1), F (j + 2))`, reading the word of wheel `j + 1`. -/
def fstep (w : Nat → Nat) (j : Nat) (st : Nat × Nat) : Nat × Nat :=
  if w (j + 1) = 0 then (st.2, max st.1 st.2)
  else (st.2, max st.1 st.2 + srch (w (j + 1)) (max st.1 st.2) 16 + 1)

/-- `n` wheels from wheel `j`. -/
def frun (w : Nat → Nat) (j : Nat) : Nat → Nat × Nat → Nat × Nat
  | 0, st => st
  | n + 1, st => frun w (j + 1) n (fstep w j st)

/-- The state after `j` wheels: `(F j, F (j + 1))`. -/
def S (w : Nat → Nat) (j : Nat) : Nat × Nat := frun w 0 j (0, 1)

/-- The forced settling tick of wheel `j`, in strip time. -/
def F (w : Nat → Nat) (j : Nat) : Nat := (S w j).1

theorem srch_spec (w m : Nat) : ∀ fuel, fuel ≤ 16 →
    (∃ k, 16 - fuel ≤ k ∧ k < 16 ∧ w.testBit ((m + k) % 16) = true) →
    w.testBit ((m + srch w m fuel) % 16) = true
  | 0, _, ⟨k, hk1, hk2, _⟩ => absurd hk2 (by omega)
  | fuel + 1, hf, ⟨k, hk1, hk2, hk⟩ => by
    simp only [srch]
    split
    · assumption
    · rename_i hw
      apply srch_spec w m fuel (by omega)
      refine ⟨k, ?_, hk2, hk⟩
      rcases Nat.lt_or_ge k (16 - fuel) with hlt | hge
      · have e : k = 16 - (fuel + 1) := by omega
        subst e
        exact absurd hk hw
      · exact hge

theorem srch_black (w m : Nat) (hw : ∃ r, r < 16 ∧ w.testBit r = true) :
    w.testBit ((m + srch w m 16) % 16) = true := by
  obtain ⟨r, hr, hb⟩ := hw
  refine srch_spec w m 16 (Nat.le_refl _) ⟨(r + 16 - m % 16) % 16, by omega, Nat.mod_lt _ (by decide), ?_⟩
  rw [show (m + (r + 16 - m % 16) % 16) % 16 = r by omega]
  exact hb

theorem frun_add (w : Nat → Nat) (i a b : Nat) (st : Nat × Nat) :
    frun w i (a + b) st = frun w (i + a) b (frun w i a st) := by
  induction a generalizing i st with
  | zero => rw [Nat.zero_add]; rfl
  | succ a ih =>
    rw [show i + (a + 1) = (i + 1) + a by omega, show a + 1 + b = (a + b) + 1 by omega]
    rw [frun, frun]
    exact ih (i + 1) (fstep w i st)

theorem frun_chain (w : Nat → Nat) (i a b : Nat) (st st' st'' : Nat × Nat) (h1 : frun w i a st = st')
    (h2 : frun w (i + a) b st' = st'') : frun w i (a + b) st = st'' := by
  rw [frun_add, h1, h2]

/-- Two word functions that agree on the wheels read give the same run. -/
theorem frun_congr {w w' : Nat → Nat} : ∀ (n j : Nat) (st : Nat × Nat),
    (∀ i, i < n → w (j + i + 1) = w' (j + i + 1)) → frun w j n st = frun w' j n st
  | 0, _, _, _ => rfl
  | n + 1, j, st, h => by
    have h0 : w (j + 1) = w' (j + 1) := h 0 (by omega)
    have e : fstep w j st = fstep w' j st := by
      unfold fstep
      rw [h0]
    simp only [frun]
    rw [e]
    exact frun_congr n (j + 1) _ (fun i hi => by
      have := h (i + 1) (by omega)
      rwa [show j + (i + 1) + 1 = j + 1 + i + 1 by omega] at this)

theorem S_succ (w : Nat → Nat) (j : Nat) : S w (j + 1) = fstep w j (S w j) := by
  unfold S
  rw [frun_add w 0 j 1 (0, 1), Nat.zero_add]
  rfl

theorem fstep_fst (w : Nat → Nat) (j : Nat) (st : Nat × Nat) : (fstep w j st).1 = st.2 := by
  unfold fstep
  split <;> rfl

theorem fstep_snd (w : Nat → Nat) (j : Nat) (st : Nat × Nat) : (fstep w j st).2 =
    if w (j + 1) = 0 then max st.1 st.2 else max st.1 st.2 + srch (w (j + 1)) (max st.1 st.2) 16 + 1 := by
  unfold fstep
  split <;> rfl

theorem S_snd (w : Nat → Nat) (j : Nat) : (S w j).2 = F w (j + 1) := by
  show (S w j).2 = (S w (j + 1)).1
  rw [S_succ, fstep_fst]

theorem F_zero (w : Nat → Nat) : F w 0 = 0 := rfl

theorem F_one (w : Nat → Nat) : F w 1 = 1 := by
  show (fstep w 0 (0, 1)).1 = 1
  rw [fstep_fst]

theorem F_succ_succ (w : Nat → Nat) (j : Nat) : F w (j + 2) =
    if w (j + 1) = 0 then max (F w j) (F w (j + 1))
    else max (F w j) (F w (j + 1)) + srch (w (j + 1)) (max (F w j) (F w (j + 1))) 16 + 1 := by
  have h : F w (j + 2) = (fstep w j (S w j)).2 := by
    show (S w (j + 2)).1 = _
    rw [S_succ, fstep_fst, S_succ]
  rw [h, fstep_snd, S_snd]
  rfl

theorem F_white (w : Nat → Nat) (j : Nat) (hb : w (j + 1) = 0) : F w (j + 2) = max (F w j) (F w (j + 1)) := by
  simp [F_succ_succ, hb]

theorem F_black (w : Nat → Nat) (j : Nat) (hb : w (j + 1) ≠ 0) :
    F w (j + 2) = max (F w j) (F w (j + 1)) + srch (w (j + 1)) (max (F w j) (F w (j + 1))) 16 + 1 := by
  have hb' : ¬ w (j + 1) = 0 := hb
  simp [F_succ_succ, hb']

theorem F_step_le (w : Nat → Nat) (j : Nat) : F w (j + 1) ≤ F w (j + 2) := by
  rw [F_succ_succ]
  split <;> omega

theorem F_mono (w : Nat → Nat) {j k : Nat} (h : j ≤ k) : F w j ≤ F w k := by
  induction k with
  | zero =>
    have e : j = 0 := by omega
    subst e
    exact Nat.le_refl _
  | succ k ih =>
    rcases Nat.lt_or_ge j (k + 1) with hlt | hge
    · have hk := ih (by omega)
      cases k with
      | zero => exact Nat.le_trans hk (by rw [F_zero, F_one]; omega)
      | succ k => exact Nat.le_trans hk (F_step_le w k)
    · have e : j = k + 1 := by omega
      subst e
      exact Nat.le_refl _

/-- Read the front off a computed pair; stated with variables, so that an instance asks the kernel for no unfolding. -/
theorem F_of_S {w : Nat → Nat} {j a b : Nat} (h : S w j = (a, b)) : F w j = a := by
  show (S w j).1 = a
  rw [h]

/-- The front through wheel `j` reads only the words of wheels `1, …, j - 1`. -/
theorem F_congr {w w' : Nat → Nat} : ∀ j, (∀ i, i + 2 ≤ j → w (i + 1) = w' (i + 1)) → F w j = F w' j
  | 0, _ => rfl
  | 1, _ => by rw [F_one, F_one]
  | j + 2, h => by
    rw [F_succ_succ w j, F_succ_succ w' j, h j (by omega), F_congr j (fun i hi => h i (by omega)),
      F_congr (j + 1) (fun i hi => h i (by omega))]

/-! ### Alignment with the time carried -/

/-- `a` carries the strip of `v` on every wheel through `J` from strip tick `T` on, at the shift `s`. -/
def OnStrip (a : Nat → Nat → Bool) (v s T J : Nat) : Prop :=
  ∀ j, j ≤ J → ∀ t, T ≤ t → a j (t + s) = Sp v j t

/-- The same with a time for each wheel. -/
def AlignedFrom (a : Nat → Nat → Bool) (v s : Nat) (F : Nat → Nat) (J : Nat) : Prop :=
  ∀ j, j ≤ J → ∀ t, F j ≤ t → a j (t + s) = Sp v j t

theorem aligned_of_alignedFrom {a : Nat → Nat → Bool} {v s J : Nat} {F : Nat → Nat} (h : AlignedFrom a v s F J) :
    Aligned a v s J :=
  fun j hj => ⟨F j, h j hj⟩

theorem onStrip_of_alignedFrom {a : Nat → Nat → Bool} {v s T J : Nat} {F : Nat → Nat} (hT : ∀ j, j ≤ J → F j ≤ T)
    (h : AlignedFrom a v s F J) : OnStrip a v s T J :=
  fun j hj t ht => h j hj t (Nat.le_trans (hT j hj) ht)

theorem alignedFrom_congr {a : Nat → Nat → Bool} {v s J : Nat} {F F' : Nat → Nat} (hF : ∀ j, j ≤ J → F j = F' j)
    (h : AlignedFrom a v s F J) : AlignedFrom a v s F' J :=
  fun j hj t ht => h j hj t (by rw [hF j hj]; exact ht)

/-- Wheels `0` and `1`: black from ticks `0` and `1`. -/
theorem base_from {a : Nat → Nat → Bool} {v : Nat} {w : Nat → Nat} (ha : Recurrence a) (ha0 : a 0 0 = true)
    (h0 : ∀ t, Sp v 0 t = true) (h1 : ∀ t, Sp v 1 t = true) : AlignedFrom a v 0 (F w) 1 := by
  intro j hj t ht
  rcases Nat.lt_or_ge j 1 with hlt | hge
  · have e : j = 0 := by omega
    subst e
    show a 0 t = Sp v 0 t
    rw [rec_zero ha ha0, h0]
  · have e : j = 1 := by omega
    subst e
    rw [F_one] at ht
    obtain ⟨u, rfl⟩ : ∃ u, t = u + 1 := ⟨t - 1, by omega⟩
    show a 1 (u + 1) = Sp v 1 (u + 1)
    rw [rec_one ha ha0 u, h1]

/-- **The forced child.** At a nearer word with a black, wheel `k + 2` carries the strip from `F (k + 2)` on. -/
theorem step_black {a : Nat → Nat → Bool} {v s k : Nat} {w : Nat → Nat} (ha : Recurrence a)
    (hv : rowAt 87867 v 16 = v) (hw : Words v w) (hk : k + 2 < 87867)
    (ih : AlignedFrom a v s (F w) (k + 1)) (hb : w (k + 1) ≠ 0) : AlignedFrom a v s (F w) (k + 2) := by
  have hF := F_black w k hb
  have hblack : Sp v (k + 1) (max (F w k) (F w (k + 1)) + srch (w (k + 1)) (max (F w k) (F w (k + 1))) 16) = true := by
    rw [Sp_mod hv, ← hw.2 (k + 1) _ (Nat.mod_lt _ (by decide))]
    exact srch_black (w (k + 1)) _ (bit_of_ne (hw.1 (k + 1)) hb)
  have hnew := child_same (k := k) (s := s) (T := max (F w k) (F w (k + 1))) ha (fun t => Sp_rec v k t hk)
    (fun t ht => ih k (by omega) t (by omega)) (fun t ht => ih (k + 1) (by omega) t (by omega))
    (Nat.le_add_right _ _) hblack
  intro j hj t ht
  rcases Nat.lt_or_ge j (k + 2) with hlt | hge
  · exact ih j (by omega) t ht
  · have e : j = k + 2 := by omega
    subst e
    exact hnew t (by omega)

/-- **A white nearer word.** From the parents' time, which is `F (k + 2)`, the child is the strip's word or its
complement. -/
theorem step_white {a : Nat → Nat → Bool} {v s k : Nat} {w : Nat → Nat} (ha : Recurrence a)
    (hv : rowAt 87867 v 16 = v) (hw : Words v w) (hk : k + 2 < 87867)
    (ih : AlignedFrom a v s (F w) (k + 1)) (hb : w (k + 1) = 0) :
    AlignedFrom a v s (F w) (k + 2) ∨ ∀ t, F w (k + 2) ≤ t → a (k + 2) (t + s) = !Sp v (k + 2) t := by
  have hF := F_white w k hb
  rcases child_white (k := k) (s := s) (T := max (F w k) (F w (k + 1))) ha (fun t => Sp_rec v k t hk)
    (fun t ht => ih k (by omega) t (by omega)) (fun t ht => ih (k + 1) (by omega) t (by omega))
    (fun t _ => white_of_word hv hw hb t) with h | h
  · left
    intro j hj t ht
    rcases Nat.lt_or_ge j (k + 2) with hlt | hge
    · exact ih j (by omega) t ht
    · have e : j = k + 2 := by omega
      subst e
      exact h t (by omega)
  · right
    intro t ht
    exact h t (by omega)

/-- **A doubling wheel.** The complement is a shift by the lower strip's period `L`, which the lower wheels do not see. -/
theorem white_shift {a : Nat → Nat → Bool} {v s k L : Nat} {w : Nat → Nat}
    (ih : AlignedFrom a v s (F w) (k + 1))
    (h : ∀ t, F w (k + 2) ≤ t → a (k + 2) (t + s) = !Sp v (k + 2) t)
    (hper : ∀ j, j ≤ k + 1 → ∀ t, Sp v j (t + L) = Sp v j t)
    (hanti : ∀ t, Sp v (k + 2) (t + L) = !Sp v (k + 2) t) :
    AlignedFrom a v (s + L) (F w) (k + 2) := by
  intro j hj t ht
  rcases Nat.lt_or_ge j (k + 2) with hlt | hge
  · rw [show t + (s + L) = (t + L) + s by omega, ih j (by omega) (t + L) (by omega), hper j (by omega) t]
  · have e : j = k + 2 := by omega
    subst e
    rw [show t + (s + L) = (t + L) + s by omega, h (t + L) (by omega), hanti t]
    cases Sp v (k + 2) t <;> rfl

/-- **A fork.** The complement is the other strip's word, and that strip agrees with `v` below. -/
theorem white_fork {a : Nat → Nat → Bool} {v v' s k : Nat} {w : Nat → Nat}
    (ih : AlignedFrom a v s (F w) (k + 1))
    (h : ∀ t, F w (k + 2) ≤ t → a (k + 2) (t + s) = !Sp v (k + 2) t)
    (hlow : ∀ j t, j ≤ k + 1 → Sp v' j t = Sp v j t) (hcomp : ∀ t, Sp v' (k + 2) t = !Sp v (k + 2) t) :
    AlignedFrom a v' s (F w) (k + 2) := by
  intro j hj t ht
  rcases Nat.lt_or_ge j (k + 2) with hlt | hge
  · rw [ih j (by omega) t ht, hlow j t (by omega)]
  · have e : j = k + 2 := by omega
    subst e
    rw [h t ht, hcomp t]

/-- **Going up without a fork**, with the time carried: while every nearer word has a black, the same shift. -/
theorem extend_from {a : Nat → Nat → Bool} {v s j0 J : Nat} {w : Nat → Nat} (ha : Recurrence a)
    (hv : rowAt 87867 v 16 = v) (hw : Words v w) (h1 : 1 ≤ j0) (hJ : J ≤ 87866) (hj : j0 ≤ J)
    (hal : AlignedFrom a v s (F w) j0) (hb : ∀ m, j0 ≤ m → m < J → w m ≠ 0) :
    AlignedFrom a v s (F w) J := by
  have aux : ∀ n, j0 + n ≤ J → AlignedFrom a v s (F w) (j0 + n) := by
    intro n
    induction n with
    | zero => intro _; exact hal
    | succ n ih =>
      intro hn
      have hp := ih (by omega)
      obtain ⟨k, hk⟩ : ∃ k, j0 + n = k + 1 := ⟨j0 + n - 1, by omega⟩
      rw [hk] at hp
      rw [show j0 + (n + 1) = k + 2 by omega]
      exact step_black ha hv hw (by omega) hp (hb (k + 1) (by omega) (by omega))
  have h := aux (J - j0) (by omega)
  rwa [show j0 + (J - j0) = J by omega] at h

/-! ### Below the first fork: the shift budget -/

/-- The shift budget through wheel `n`: `1, 2, 4, 8` become available at wheels `3, 8, 29, 400`. -/
def lsum (n : Nat) : Nat := min 1 (n / 3) + 2 * min 1 (n / 8) + 4 * min 1 (n / 29) + 8 * min 1 (n / 400)

theorem lsum_53207 : lsum 53207 = 15 := by decide

/-- **Through wheel 53,207**, for a strip whose white wheels there are the four doubling wheels, with the time carried:
the shift stays within the budget. -/
theorem low_from {a : Nat → Nat → Bool} {v : Nat} {w : Nat → Nat} (ha : Recurrence a) (ha0 : a 0 0 = true)
    (hv : rowAt 87867 v 16 = v) (hw : Words v w) (h0 : ∀ t, Sp v 0 t = true) (h1 : ∀ t, Sp v 1 t = true)
    (hbw : ∀ m, m < 53207 → w m ≠ 0 ∨ m = 2 ∨ m = 7 ∨ m = 28 ∨ m = 399)
    (hs2 : (∀ j, j ≤ 2 → ∀ t, Sp v j (t + 1) = Sp v j t) ∧ ∀ t, Sp v (2 + 1) (t + 1) = !Sp v (2 + 1) t)
    (hs7 : (∀ j, j ≤ 7 → ∀ t, Sp v j (t + 2) = Sp v j t) ∧ ∀ t, Sp v (7 + 1) (t + 2) = !Sp v (7 + 1) t)
    (hs28 : (∀ j, j ≤ 28 → ∀ t, Sp v j (t + 4) = Sp v j t) ∧ ∀ t, Sp v (28 + 1) (t + 4) = !Sp v (28 + 1) t)
    (hs399 : (∀ j, j ≤ 399 → ∀ t, Sp v j (t + 8) = Sp v j t) ∧ ∀ t, Sp v (399 + 1) (t + 8) = !Sp v (399 + 1) t) :
    ∀ n, n ≤ 53207 → ∃ s, s ≤ lsum n ∧ AlignedFrom a v s (F w) n
  | 0, _ => ⟨0, by simp [lsum], fun j hj t _ => by
      have e : j = 0 := by omega
      subst e
      show a 0 t = Sp v 0 t
      rw [rec_zero ha ha0, h0]⟩
  | 1, _ => ⟨0, by simp [lsum], base_from ha ha0 h0 h1⟩
  | n + 2, hn => by
    obtain ⟨s, hs, ih⟩ := low_from ha ha0 hv hw h0 h1 hbw hs2 hs7 hs28 hs399 (n + 1) (by omega)
    have hlsum : lsum (n + 1) ≤ lsum (n + 2) := by simp only [lsum]; omega
    by_cases hb : w (n + 1) = 0
    · rcases step_white ha hv hw (by omega) ih hb with h | h
      · exact ⟨s, Nat.le_trans hs hlsum, h⟩
      · rcases hbw (n + 1) (by omega) with hne | h2 | h7 | h28 | h399
        · exact absurd hb hne
        · have e : n = 1 := by omega
          subst e
          exact ⟨s + 1, by simp only [lsum] at hs ⊢; omega, white_shift ih h hs2.1 hs2.2⟩
        · have e : n = 6 := by omega
          subst e
          exact ⟨s + 2, by simp only [lsum] at hs ⊢; omega, white_shift ih h hs7.1 hs7.2⟩
        · have e : n = 27 := by omega
          subst e
          exact ⟨s + 4, by simp only [lsum] at hs ⊢; omega, white_shift ih h hs28.1 hs28.2⟩
        · have e : n = 398 := by omega
          subst e
          exact ⟨s + 8, by simp only [lsum] at hs ⊢; omega, white_shift ih h hs399.1 hs399.2⟩
    · exact ⟨s, Nat.le_trans hs hlsum, step_black ha hv hw (by omega) ih hb⟩

/-! ### The walk: the recursion as one arithmetic step per tick -/

/-- The cell of wheel `j` at tick `t` of the sixteen-row cycle `R`, as a number. -/
def tb (R : Nat → Nat) (t j : Nat) : Nat := Nat.land (Nat.shiftRight (R (t % 16)) j) 1

/-- From wheel `j` at tick `t`, `n` ticks: a black cell moves on to the next wheel, a white one waits. -/
def walk (R : Nat → Nat) : Nat → Nat → Nat → Nat
  | 0, _, j => j
  | n + 1, t, j => walk R n (t + 1) (j + tb R t j)

theorem tb_eq (R : Nat → Nat) (t j : Nat) : tb R t j = ((R (t % 16)).testBit j).toNat := by
  show (R (t % 16) >>> j) &&& 1 = _
  rw [Nat.and_one_is_mod, Nat.shiftRight_eq_div_pow, Nat.testBit_eq_decide_div_mod_eq]
  rcases Nat.mod_two_eq_zero_or_one (R (t % 16) / 2 ^ j) with h | h <;> simp [h]

theorem tb_le (R : Nat → Nat) (t j : Nat) : tb R t j ≤ 1 := by
  rw [tb_eq]; exact Bool.toNat_le _

theorem walk_add (R : Nat → Nat) (x y : Nat) : ∀ t j, walk R (x + y) t j = walk R y (t + x) (walk R x t j) := by
  induction x with
  | zero => intro t j; simp [walk]
  | succ x ih =>
    intro t j
    have e : x + 1 + y = (x + y) + 1 := by omega
    rw [e]
    show walk R (x + y) (t + 1) (j + tb R t j) = walk R y (t + (x + 1)) (walk R x (t + 1) (j + tb R t j))
    rw [ih]
    have e2 : t + 1 + x = t + (x + 1) := by omega
    rw [e2]

theorem walk_one (R : Nat → Nat) (t j : Nat) : walk R 1 t j = j + tb R t j := rfl

theorem walk_end (R : Nat → Nat) (n t j : Nat) :
    walk R (n + 1) t j = walk R n t j + tb R (t + n) (walk R n t j) := by
  rw [walk_add, walk_one]

theorem walk_le_succ (R : Nat → Nat) (n t j : Nat) : walk R n t j ≤ walk R (n + 1) t j := by
  rw [walk_end]; omega

theorem walk_mono (R : Nat → Nat) (t j : Nat) {n m : Nat} (h : n ≤ m) : walk R n t j ≤ walk R m t j := by
  induction m with
  | zero => have : n = 0 := by omega
            rw [this]; exact Nat.le_refl _
  | succ m ih =>
    rcases Nat.lt_or_ge n (m + 1) with h1 | h1
    · exact Nat.le_trans (ih (by omega)) (walk_le_succ R m t j)
    · have : n = m + 1 := by omega
      rw [this]; exact Nat.le_refl _

theorem le_walk (R : Nat → Nat) (n t j : Nat) : j ≤ walk R n t j :=
  walk_mono R t j (Nat.zero_le n)

/-- A wheel is reached at one tick only. -/
theorem arrival_unique (R : Nat → Nat) (t j : Nat) {n1 n2 J : Nat} (h1 : 1 ≤ n1) (h2 : 1 ≤ n2)
    (a1 : walk R n1 t j = J) (b1 : walk R (n1 - 1) t j + 1 = J)
    (a2 : walk R n2 t j = J) (b2 : walk R (n2 - 1) t j + 1 = J) : n1 = n2 := by
  rcases Nat.lt_trichotomy n1 n2 with h | h | h
  · have := walk_mono R t j (show n1 ≤ n2 - 1 by omega)
    omega
  · exact h
  · have := walk_mono R t j (show n2 ≤ n1 - 1 by omega)
    omega

section words

variable {R w : Nat → Nat}

theorem tb_word (hR : ∀ j r, r < 16 → (w j).testBit r = (R r).testBit j) (t j : Nat) :
    tb R t j = ((w j).testBit (t % 16)).toNat := by
  rw [tb_eq, hR j (t % 16) (Nat.mod_lt _ (by decide))]

/-- A wheel with no black cell at the next `n` ticks waits. -/
theorem walk_stay (hR : ∀ j r, r < 16 → (w j).testBit r = (R r).testBit j) {j : Nat} :
    ∀ n t, (∀ i, i < n → (w j).testBit ((t + i) % 16) = false) → walk R n t j = j := by
  intro n
  induction n with
  | zero => intro t _; rfl
  | succ n ih =>
    intro t h
    have h0 := h 0 (by omega)
    have e : tb R t j = 0 := by
      rw [tb_word hR]; rw [Nat.add_zero] at h0; rw [h0]; rfl
    show walk R n (t + 1) (j + tb R t j) = j
    rw [e, Nat.add_zero]
    apply ih
    intro i hi
    have := h (i + 1) (by omega)
    have e2 : t + (i + 1) = t + 1 + i := by omega
    rw [e2] at this
    exact this

theorem srch_min (x m : Nat) : ∀ fuel, fuel ≤ 16 → ∀ i, 16 - fuel ≤ i → i < srch x m fuel →
    x.testBit ((m + i) % 16) = false
  | 0, _, i, _, h => by
    have : srch x m 0 = 16 := rfl
    omega
  | fuel + 1, hf, i, h1, h2 => by
    simp only [srch] at h2
    split at h2
    · omega
    · rename_i hb
      rcases Nat.lt_or_ge i (16 - fuel) with hlt | hge
      · have e : i = 16 - (fuel + 1) := by omega
        subst e
        simpa using hb
      · exact srch_min x m fuel (by omega) i hge h2

/-- At a black wheel the wait of `srch` is the walk. -/
theorem walk_srch (hR : ∀ j r, r < 16 → (w j).testBit r = (R r).testBit j) (hw : ∀ j, w j < 2 ^ 16) {j : Nat}
    (hb : w j ≠ 0) (m : Nat) :
    walk R (srch (w j) m 16) m j = j ∧ walk R (srch (w j) m 16 + 1) m j = j + 1 := by
  have h1 : walk R (srch (w j) m 16) m j = j :=
    walk_stay hR _ m (fun i hi => srch_min (w j) m 16 (Nat.le_refl _) i (Nat.zero_le _) hi)
  refine ⟨h1, ?_⟩
  rw [walk_end, h1, tb_word hR, srch_black (w j) m (bit_of_ne (hw j) hb)]
  rfl

/-- A wheel the walk has passed is black. -/
theorem walk_black (hR : ∀ j r, r < 16 → (w j).testBit r = (R r).testBit j) :
    ∀ n t j j', j ≤ j' → j' < walk R n t j → w j' ≠ 0 := by
  intro n
  induction n with
  | zero => intro t j j' h1 h2; exact absurd h2 (by show ¬ j' < j; omega)
  | succ n ih =>
    intro t j j' h1 h2
    have e : walk R (n + 1) t j = walk R n (t + 1) (j + tb R t j) := rfl
    rw [e] at h2
    by_cases hb : (w j).testBit (t % 16) = true
    · have t1 : tb R t j = 1 := by rw [tb_word hR, hb]; rfl
      rw [t1] at h2
      rcases Nat.lt_or_ge j j' with hlt | hge
      · exact ih (t + 1) (j + 1) j' (by omega) h2
      · have : j' = j := by omega
        subst this
        intro h0
        rw [h0, Nat.zero_testBit] at hb
        cases hb
    · have t0 : tb R t j = 0 := by
        rw [tb_word hR]
        cases hc : (w j).testBit (t % 16)
        · rfl
        · exact absurd hc hb
      rw [t0, Nat.add_zero] at h2
      exact ih (t + 1) j j' h1 h2

theorem frun_last (v : Nat → Nat) (i n : Nat) (st : Nat × Nat) :
    frun v i (n + 1) st = fstep v (i + n) (frun v i n st) := by
  rw [frun_add]; rfl

/-- The recursion from a state `(a, b)` with `a ≤ b` is the walk from wheel `j0 + 1` at tick `b`: the second front after `n` black
wheels is the tick at which the walk reaches wheel `j0 + 1 + n`. -/
theorem run_arrival (hR : ∀ j r, r < 16 → (w j).testBit r = (R r).testBit j) (hw : ∀ j, w j < 2 ^ 16)
    {j0 a b : Nat} (hab : a ≤ b) : ∀ n, (∀ i, i < n → w (j0 + 1 + i) ≠ 0) →
    (frun w j0 n (a, b)).1 ≤ (frun w j0 n (a, b)).2 ∧ b ≤ (frun w j0 n (a, b)).2 ∧
    walk R ((frun w j0 n (a, b)).2 - b) b (j0 + 1) = j0 + 1 + n ∧
    (1 ≤ n → b + 1 ≤ (frun w j0 n (a, b)).2 ∧
      walk R ((frun w j0 n (a, b)).2 - b - 1) b (j0 + 1) + 1 = j0 + 1 + n) := by
  intro n
  induction n with
  | zero =>
    intro _
    refine ⟨hab, Nat.le_refl _, ?_, fun h => absurd h (by omega)⟩
    show walk R (b - b) b (j0 + 1) = j0 + 1 + 0
    rw [Nat.sub_self]; rfl
  | succ n ih =>
    intro hbl
    obtain ⟨c1, c2, c3, _⟩ := ih (fun i hi => hbl i (by omega))
    rw [frun_last]
    generalize hst : frun w j0 n (a, b) = st at c1 c2 c3 ⊢
    obtain ⟨x, y⟩ := st
    simp only at c1 c2 c3
    have hb : w (j0 + n + 1) ≠ 0 := by
      have := hbl n (by omega)
      have e : j0 + 1 + n = j0 + n + 1 := by omega
      rw [e] at this
      exact this
    have hmax : max x y = y := Nat.max_eq_right c1
    have hf : fstep w (j0 + n) (x, y) = (y, y + srch (w (j0 + n + 1)) y 16 + 1) := by
      simp only [fstep, hb, ite_false, hmax]
    rw [hf]
    obtain ⟨k1, k2⟩ := walk_srch hR hw hb y
    generalize srch (w (j0 + n + 1)) y 16 = k at k1 k2
    simp only
    have e0 : b + (y - b) = y := by omega
    have e1 : y + k + 1 - b = (y - b) + (k + 1) := by omega
    have e2 : y + k + 1 - b - 1 = (y - b) + k := by omega
    have e3 : j0 + 1 + n = j0 + n + 1 := by omega
    refine ⟨by omega, by omega, ?_, fun _ => ⟨by omega, ?_⟩⟩
    · rw [e1, walk_add, c3, e0, e3, k2]; omega
    · rw [e2, walk_add, c3, e0, e3, k1]; omega

/-- **A block of black wheels by the walk.** Four facts about the walk fix the state after `n ≥ 2` wheels; the wheels need not be known
to be black, since the walk passes them. -/
theorem frun_of_walk (hR : ∀ j r, r < 16 → (w j).testBit r = (R r).testBit j) (hw : ∀ j, w j < 2 ^ 16)
    {j0 n a b A B : Nat} (hab : a ≤ b) (hn : 2 ≤ n) (hA : b < A) (hB : A < B)
    (f1 : walk R (A - 1 - b) b (j0 + 1) = j0 + n - 1) (f2 : tb R (A - 1) (j0 + n - 1) = 1)
    (f3 : walk R (B - 1 - A) A (j0 + n) = j0 + n) (f4 : tb R (B - 1) (j0 + n) = 1) :
    frun w j0 n (a, b) = (A, B) := by
  -- the walk from the start at the four ticks
  have eA : A - b = (A - 1 - b) + 1 := by omega
  have eB1 : B - 1 - b = (A - b) + (B - 1 - A) := by omega
  have eB : B - b = (B - 1 - b) + 1 := by omega
  have wA1 : walk R (A - 1 - b) b (j0 + 1) = j0 + n - 1 := f1
  have wA : walk R (A - b) b (j0 + 1) = j0 + n := by
    rw [eA, walk_end, wA1]
    have e : b + (A - 1 - b) = A - 1 := by omega
    rw [e, f2]; omega
  have wB1 : walk R (B - 1 - b) b (j0 + 1) = j0 + n := by
    rw [eB1, walk_add, wA]
    have e : b + (A - b) = A := by omega
    rw [e, f3]
  have wB : walk R (B - b) b (j0 + 1) = j0 + 1 + n := by
    rw [eB, walk_end, wB1]
    have e : b + (B - 1 - b) = B - 1 := by omega
    rw [e, f4]; omega
  -- every wheel of the block is black
  have hbl : ∀ i, i < n → w (j0 + 1 + i) ≠ 0 := fun i hi =>
    walk_black hR (B - b) b (j0 + 1) (j0 + 1 + i) (by omega) (by rw [wB]; omega)
  obtain ⟨c1, c2, c3, c4⟩ := run_arrival hR hw hab n hbl
  obtain ⟨d1, d2, d3, d4⟩ := run_arrival hR hw hab (n - 1) (fun i hi => hbl i (by omega))
  obtain ⟨c5, c6⟩ := c4 (by omega)
  obtain ⟨d5, d6⟩ := d4 (by omega)
  -- the two fronts are the two arrivals
  have hy : (frun w j0 n (a, b)).2 - b = B - b :=
    arrival_unique R b (j0 + 1) (J := j0 + 1 + n) (by omega) (by omega) c3 c6 wB (by rw [show B - b - 1 = B - 1 - b by omega, wB1]; omega)
  have hy' : (frun w j0 (n - 1) (a, b)).2 - b = A - b := by
    have e : j0 + 1 + (n - 1) = j0 + n := by omega
    rw [e] at d3 d6
    exact arrival_unique R b (j0 + 1) (J := j0 + n) (by omega) (by omega) d3 d6 wA
      (by rw [show A - b - 1 = A - 1 - b by omega, wA1]; omega)
  have hlast : frun w j0 n (a, b) = fstep w (j0 + (n - 1)) (frun w j0 (n - 1) (a, b)) := by
    have e : n = (n - 1) + 1 := by omega
    conv => lhs; rw [e]
    rw [frun_last]
  have h1 : (frun w j0 n (a, b)).1 = A := by
    rw [hlast, fstep_fst]; omega
  have h2 : (frun w j0 n (a, b)).2 = B := by omega
  exact Prod.ext h1 h2

/-- A white wheel leaves the second front where it is. -/
theorem frun_white {j a b : Nat} (hab : a ≤ b) (h0 : w (j + 1) = 0) : frun w j 1 (a, b) = (b, b) := by
  show fstep w j (a, b) = (b, b)
  simp only [fstep, h0, ite_true, Nat.max_eq_right hab]

end words

/-! ### Sixteen ticks at a time -/

/-- One tick of a row `x`. -/
def s (x j : Nat) : Nat := Nat.add j (Nat.land (Nat.shiftRight x j) 1)

/-- Sixteen ticks from a tick that is a multiple of sixteen. -/
def st16 (R : Nat → Nat) (j : Nat) : Nat :=
  s (R 15) (s (R 14) (s (R 13) (s (R 12) (s (R 11) (s (R 10) (s (R 9) (s (R 8) (s (R 7) (s (R 6) (s (R 5) (s (R 4)
    (s (R 3) (s (R 2) (s (R 1) (s (R 0) j)))))))))))))))

/-- `16 g` ticks. The test forces the value at each round, so the kernel's recursion stays shallow; it is never true. -/
def w16 (R : Nat → Nat) : Nat → Nat → Nat
  | 0, j => j
  | g + 1, j => cond (Nat.beq (st16 R j) 0) 0 (w16 R g (st16 R j))

theorem s_eq (R : Nat → Nat) {t i : Nat} (h : t % 16 = i) (j : Nat) : s (R i) j = j + tb R t j := by
  show Nat.add j (Nat.land (Nat.shiftRight (R i) j) 1) = j + Nat.land (Nat.shiftRight (R (t % 16)) j) 1
  rw [h]; rfl

theorem st16_walk (R : Nat → Nat) {t : Nat} (ht : t % 16 = 0) (j : Nat) : st16 R j = walk R 16 t j := by
  have wk : ∀ i, i < 16 → walk R (i + 1) t j = s (R i) (walk R i t j) := fun i hi => by
    rw [walk_end, s_eq R (t := t + i) (i := i) (by omega) (walk R i t j)]
  have e1 : walk R 1 t j = s (R 0) j := wk 0 (by omega)
  have e2 : walk R 2 t j = s (R 1) (walk R 1 t j) := wk 1 (by omega)
  have e3 : walk R 3 t j = s (R 2) (walk R 2 t j) := wk 2 (by omega)
  have e4 : walk R 4 t j = s (R 3) (walk R 3 t j) := wk 3 (by omega)
  have e5 : walk R 5 t j = s (R 4) (walk R 4 t j) := wk 4 (by omega)
  have e6 : walk R 6 t j = s (R 5) (walk R 5 t j) := wk 5 (by omega)
  have e7 : walk R 7 t j = s (R 6) (walk R 6 t j) := wk 6 (by omega)
  have e8 : walk R 8 t j = s (R 7) (walk R 7 t j) := wk 7 (by omega)
  have e9 : walk R 9 t j = s (R 8) (walk R 8 t j) := wk 8 (by omega)
  have e10 : walk R 10 t j = s (R 9) (walk R 9 t j) := wk 9 (by omega)
  have e11 : walk R 11 t j = s (R 10) (walk R 10 t j) := wk 10 (by omega)
  have e12 : walk R 12 t j = s (R 11) (walk R 11 t j) := wk 11 (by omega)
  have e13 : walk R 13 t j = s (R 12) (walk R 12 t j) := wk 12 (by omega)
  have e14 : walk R 14 t j = s (R 13) (walk R 13 t j) := wk 13 (by omega)
  have e15 : walk R 15 t j = s (R 14) (walk R 14 t j) := wk 14 (by omega)
  have e16 : walk R 16 t j = s (R 15) (walk R 15 t j) := wk 15 (by omega)
  rw [e16, e15, e14, e13, e12, e11, e10, e9, e8, e7, e6, e5, e4, e3, e2, e1]
  rfl

theorem w16_walk (R : Nat → Nat) : ∀ g t j, t % 16 = 0 → 1 ≤ j → w16 R g j = walk R (16 * g) t j := by
  intro g
  induction g with
  | zero => intro t j _ _; rfl
  | succ g ih =>
    intro t j ht hj
    have e := st16_walk R ht j
    have hp : 1 ≤ st16 R j := by
      rw [e]; exact Nat.le_trans hj (le_walk R 16 t j)
    have hb : Nat.beq (st16 R j) 0 = false := by
      cases h : st16 R j with
      | zero => omega
      | succ q => rfl
    show cond (Nat.beq (st16 R j) 0) 0 (w16 R g (st16 R j)) = _
    rw [hb]
    show w16 R g (st16 R j) = _
    rw [ih (t + 16) (st16 R j) (by omega) hp, e, ← walk_add]
    have : 16 + 16 * g = 16 * (g + 1) := by omega
    rw [this]

/-- A head of `h` ticks up to a multiple of sixteen, `16 g` ticks, and a tail of `d` ticks. -/
def fastWalk (R : Nat → Nat) (h g d t j : Nat) : Nat :=
  walk R d (t + h + 16 * g) (w16 R g (walk R h t j))

theorem fastWalk_eq (R : Nat → Nat) {h g d t j : Nat} (ht : (t + h) % 16 = 0) (hj : 1 ≤ j) :
    fastWalk R h g d t j = walk R (h + (16 * g + d)) t j := by
  show walk R d (t + h + 16 * g) (w16 R g (walk R h t j)) = _
  rw [w16_walk R g (t + h) _ ht (Nat.le_trans hj (le_walk R h t j)), ← walk_add, ← walk_add]

/-! ### The words of the four strips -/

/-- The sixteen-bit word of wheel `j` of the strip of `v`: bit `r` is the wheel at phase `r`. -/
def wd (v j : Nat) : Nat := word16 (fun r => (rowAt 87867 v r).testBit j)

abbrev wdA0 : Nat → Nat := wd A0
abbrev wdA1 : Nat → Nat := wd A1
abbrev wdB0 : Nat → Nat := wd B0
abbrev wdB1 : Nat → Nat := wd B1

theorem wd_row (v : Nat) : ∀ j r, r < 16 → (wd v j).testBit r = (rowAt 87867 v r).testBit j := fun _ r hr =>
  word16_bit _ r hr

theorem wd_lt (v j : Nat) : wd v j < 2 ^ 16 := word16_lt _

theorem words (v : Nat) : Words v (wd v) := ⟨wd_lt v, fun j r hr => wd_row v j r hr⟩

theorem wordsA0 : Words A0 wdA0 := words A0
theorem wordsA1 : Words A1 wdA1 := words A1
theorem wordsB0 : Words B0 wdB0 := words B0
theorem wordsB1 : Words B1 wdB1 := words B1

/-! ### White wheels, black windows and the agreement below the forks -/

theorem wdA0_53207 : wdA0 53207 = 0 := word_zero_of_white wordsA0 white_53207
theorem wdA0_58286 : wdA0 58286 = 0 := word_zero_of_white wordsA0 white_58286
theorem wdB0_72575 : wdB0 72575 = 0 := word_zero_of_white wordsB0 white_72575

theorem hbwA0 : ∀ m, m < 53207 → wdA0 m ≠ 0 ∨ m = 2 ∨ m = 7 ∨ m = 28 ∨ m = 399 := fun m hm => by
  rcases black_or_white hm with ⟨r, hr, hb⟩ | h
  · exact Or.inl (word_ne_of_black wordsA0 hr hb)
  · exact Or.inr h

set_option exponentiation.threshold 90000 in
theorem bA0_low : ∀ m, 53208 ≤ m → m < 58286 → wdA0 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wA0_low h1 (by omega)
  exact word_ne_of_black wordsA0 hr hb
set_option exponentiation.threshold 90000 in
theorem bA0_high : ∀ m, 58287 ≤ m → m < 87866 → wdA0 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wA0_high h1 (by omega)
  exact word_ne_of_black wordsA0 hr hb
set_option exponentiation.threshold 90000 in
theorem bA1_high : ∀ m, 58287 ≤ m → m < 87866 → wdA1 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wA1_high h1 (by omega)
  exact word_ne_of_black wordsA1 hr hb
set_option exponentiation.threshold 90000 in
theorem bB0_low : ∀ m, 53208 ≤ m → m < 72575 → wdB0 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wB0_low h1 (by omega)
  exact word_ne_of_black wordsB0 hr hb
set_option exponentiation.threshold 90000 in
theorem bB0_high : ∀ m, 72576 ≤ m → m < 87866 → wdB0 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wB0_high h1 (by omega)
  exact word_ne_of_black wordsB0 hr hb
set_option exponentiation.threshold 90000 in
theorem bB1_high : ∀ m, 72576 ≤ m → m < 87866 → wdB1 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wB1_high h1 (by omega)
  exact word_ne_of_black wordsB1 hr hb

/-- Below a fork the two strips have the same words, so the same fronts. -/
theorem wB0_eq_A0 : ∀ i, i + 2 ≤ 53208 → wdA0 (i + 1) = wdB0 (i + 1) := fun i hi =>
  (word_eq_of_low wordsA0 wordsB0 (fun r _ => low_of_phase A0_return B0_return low_B0 (i + 1) r (by omega))).symm
theorem wA1_eq_A0 : ∀ i, i + 2 ≤ 58287 → wdA0 (i + 1) = wdA1 (i + 1) := fun i hi =>
  (word_eq_of_low wordsA0 wordsA1 (fun r _ => low_of_phase A0_return A1_return low_A1 (i + 1) r (by omega))).symm
theorem wB1_eq_B0 : ∀ i, i + 2 ≤ 72576 → wdB0 (i + 1) = wdB1 (i + 1) := fun i hi =>
  (word_eq_of_low wordsB0 wordsB1 (fun r _ => low_of_phase B0_return B1_return low_B1 (i + 1) r (by omega))).symm

/-! ### The tree, with the time carried -/

/-- **The forced front on the four strips.** Every array with the left-diagonal recurrence and a black wheel 0 carries one of
the four strips on every wheel `j ≤ 87,866` from strip tick `F j` on, at a shift of at most `15`. -/
theorem forced_front_four {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ (AlignedFrom a A0 s (F wdA0) 87866 ∨ AlignedFrom a A1 s (F wdA1) 87866 ∨
      AlignedFrom a B0 s (F wdB0) 87866 ∨ AlignedFrom a B1 s (F wdB1) 87866) := by
  obtain ⟨s, hs, h⟩ := low_from ha ha0 A0_return wordsA0 A0_zero A0_one hbwA0
    (strip_shift (m := 2) per2 anti2) (strip_shift (m := 7) per7 anti7) (strip_shift (m := 28) per28 anti28)
    (strip_shift (m := 399) per399 anti399) 53207 (Nat.le_refl _)
  refine ⟨s, by rw [lsum_53207] at hs; exact hs, ?_⟩
  rcases step_white ha A0_return wordsA0 (by omega) h wdA0_53207 with hA | hB
  · -- the A side: on A0 through the first fork
    have h2 : AlignedFrom a A0 s (F wdA0) 58286 :=
      extend_from ha A0_return wordsA0 (by omega) (by omega) (by omega) hA bA0_low
    rcases step_white ha A0_return wordsA0 (by omega) h2 wdA0_58286 with hA0 | hA1
    · exact Or.inl (extend_from ha A0_return wordsA0 (by omega) (by omega) (by omega) hA0 bA0_high)
    · have h3 : AlignedFrom a A1 s (F wdA0) 58287 := white_fork h2 hA1
        (fun j t hj => low_of_phase A0_return A1_return low_A1 j t (by omega))
        (comp_of_phase A0_return A1_return top_A1)
      have h4 : AlignedFrom a A1 s (F wdA1) 58287 :=
        alignedFrom_congr (fun j hj => F_congr j (fun i hi => wA1_eq_A0 i (by omega))) h3
      exact Or.inr (Or.inl (extend_from ha A1_return wordsA1 (by omega) (by omega) (by omega) h4 bA1_high))
  · -- the B side: the complement at 53,208 is B0's word
    have h3 : AlignedFrom a B0 s (F wdA0) 53208 := white_fork h hB
      (fun j t hj => low_of_phase A0_return B0_return low_B0 j t (by omega))
      (comp_of_phase A0_return B0_return top_B0)
    have h4 : AlignedFrom a B0 s (F wdB0) 53208 :=
      alignedFrom_congr (fun j hj => F_congr j (fun i hi => wB0_eq_A0 i (by omega))) h3
    have h5 : AlignedFrom a B0 s (F wdB0) 72575 :=
      extend_from ha B0_return wordsB0 (by omega) (by omega) (by omega) h4 bB0_low
    rcases step_white ha B0_return wordsB0 (by omega) h5 wdB0_72575 with hB0 | hB1
    · exact Or.inr (Or.inr (Or.inl (extend_from ha B0_return wordsB0 (by omega) (by omega) (by omega) hB0 bB0_high)))
    · have h6 : AlignedFrom a B1 s (F wdB0) 72576 := white_fork h5 hB1
        (fun j t hj => low_of_phase B0_return B1_return low_B1 j t (by omega))
        (comp_of_phase B0_return B1_return top_B1)
      have h7 : AlignedFrom a B1 s (F wdB1) 72576 :=
        alignedFrom_congr (fun j hj => F_congr j (fun i hi => wB1_eq_B0 i (by omega))) h6
      exact Or.inr (Or.inr (Or.inr (extend_from ha B1_return wordsB1 (by omega) (by omega) (by omega) h7 bB1_high)))

/-- The classification of `Rule30FourLeftSides`, recovered with its shift bounded by `15`. -/
theorem classification_bounded {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ (Aligned a A0 s 87866 ∨ Aligned a A1 s 87866 ∨ Aligned a B0 s 87866 ∨ Aligned a B1 s 87866) := by
  obtain ⟨s, hs, h⟩ := forced_front_four ha ha0
  refine ⟨s, hs, ?_⟩
  rcases h with h | h | h | h
  · exact Or.inl (aligned_of_alignedFrom h)
  · exact Or.inr (Or.inl (aligned_of_alignedFrom h))
  · exact Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h)))
  · exact Or.inr (Or.inr (Or.inr (aligned_of_alignedFrom h)))

/-! ### The numbers, by the walk -/

/-- A black run of a strip by the walk, with the long stretch sixteen ticks at a time. -/
theorem seg_black {v j0 n a b A B h g d : Nat} (hab : a ≤ b) (hn : 2 ≤ n) (hA : b < A) (hB : A < B)
    (e : A - 1 - b = h + (16 * g + d)) (ht : (b + h) % 16 = 0)
    (k1 : fastWalk (rowAt 87867 v) h g d b (j0 + 1) = j0 + n - 1)
    (f2 : tb (rowAt 87867 v) (A - 1) (j0 + n - 1) = 1)
    (f3 : walk (rowAt 87867 v) (B - 1 - A) A (j0 + n) = j0 + n)
    (f4 : tb (rowAt 87867 v) (B - 1) (j0 + n) = 1) : frun (wd v) j0 n (a, b) = (A, B) :=
  frun_of_walk (wd_row v) (wd_lt v) hab hn hA hB
    (by rw [e, ← fastWalk_eq _ ht (by omega)]; exact k1) f2 f3 f4

theorem low_congr {w w' : Nat → Nat} {n : Nat} {st : Nat × Nat} (h : ∀ i, i < n → w (i + 1) = w' (i + 1)) :
    frun w 0 n st = frun w' 0 n st :=
  frun_congr n 0 st (fun i hi => by rw [Nat.zero_add]; exact h i hi)

theorem a_low : frun wdA0 0 400 (0, 1) = (783, 784) := by decide +kernel

theorem a_1 : frun wdA0 400 52806 (783, 784) = (107308, 107310) :=
  seg_black (v := A0) (h := 0) (g := 6657) (d := 11) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem a_2 : frun wdA0 53206 1 (107308, 107310) = (107310, 107310) := frun_white (by decide) wdA0_53207

theorem a_53207 : frun wdA0 0 53207 (0, 1) = (107310, 107310) :=
  (frun_chain _ 0 400 52807 _ _ _ a_low
    (frun_chain _ 400 52806 1 _ _ _ a_1
    a_2))

theorem a_3 : frun wdA0 53207 5078 (107310, 107310) = (117438, 117439) :=
  seg_black (v := A0) (h := 2) (g := 632) (d := 13) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem a_4 : frun wdA0 58285 1 (117438, 117439) = (117439, 117439) := frun_white (by decide) wdA0_58286

theorem a_58286 : frun wdA0 0 58286 (0, 1) = (117439, 117439) :=
  (frun_chain _ 0 53207 5079 _ _ _ a_53207
    (frun_chain _ 53207 5078 1 _ _ _ a_3
    a_4))

theorem a_5 : frun wdA0 58286 29579 (117439, 117439) = (176966, 176968) :=
  seg_black (v := A0) (h := 1) (g := 3720) (d := 5) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem a_6 : frun wdA0 87865 1 (176966, 176968) = (176968, 176968) := frun_white (by decide) (by decide +kernel)

theorem SA0 : S wdA0 87866 = (176968, 176968) :=
  frun_chain _ 0 58286 29580 _ _ _ a_58286 (frun_chain _ 58286 29579 1 _ _ _ a_5 a_6)

theorem b_53207 : frun wdB0 0 53207 (0, 1) = (107310, 107310) :=
  (low_congr (fun i hi => (wB0_eq_A0 i (by omega)).symm)).trans a_53207

theorem b_1 : frun wdB0 53207 19367 (107310, 107310) = (146462, 146463) :=
  seg_black (v := B0) (h := 2) (g := 2446) (d := 13) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem b_2 : frun wdB0 72574 1 (146462, 146463) = (146463, 146463) := frun_white (by decide) wdB0_72575

theorem b_72575 : frun wdB0 0 72575 (0, 1) = (146463, 146463) :=
  (frun_chain _ 0 53207 19368 _ _ _ b_53207
    (frun_chain _ 53207 19367 1 _ _ _ b_1
    b_2))

theorem b_3 : frun wdB0 72575 15291 (146463, 146463) = (177170, 177173) :=
  seg_black (v := B0) (h := 1) (g := 1919) (d := 1) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem SB0 : S wdB0 87866 = (177170, 177173) := frun_chain _ 0 72575 15291 _ _ _ b_72575 b_3

theorem a1_58286 : frun wdA1 0 58286 (0, 1) = (117439, 117439) :=
  (low_congr (fun i hi => (wA1_eq_A0 i (by omega)).symm)).trans a_58286

theorem a1_1 : frun wdA1 58286 29580 (117439, 117439) = (177229, 177232) :=
  seg_black (v := A1) (h := 1) (g := 3736) (d := 12) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem SA1 : S wdA1 87866 = (177229, 177232) := frun_chain _ 0 58286 29580 _ _ _ a1_58286 a1_1

theorem b1_72575 : frun wdB1 0 72575 (0, 1) = (146463, 146463) :=
  (low_congr (fun i hi => (wB1_eq_B0 i (by omega)).symm)).trans b_72575

theorem b1_1 : frun wdB1 72575 15291 (146463, 146463) = (177560, 177563) :=
  seg_black (v := B1) (h := 1) (g := 1943) (d := 7) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)
    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)

theorem SB1 : S wdB1 87866 = (177560, 177563) := frun_chain _ 0 72575 15291 _ _ _ b1_72575 b1_1

theorem FA0_87866 : F wdA0 87866 = 176968 := F_of_S SA0

theorem FA1_87866 : F wdA1 87866 = 177229 := F_of_S SA1

theorem FB0_87866 : F wdB0 87866 = 177170 := F_of_S SB0

theorem FB1_87866 : F wdB1 87866 = 177560 := F_of_S SB1

/-- Every front through wheel 87,866 is at most 177,560, the B1 front there. -/
theorem fronts_le : (∀ j, j ≤ 87866 → F wdA0 j ≤ 177560) ∧ (∀ j, j ≤ 87866 → F wdA1 j ≤ 177560) ∧
    (∀ j, j ≤ 87866 → F wdB0 j ≤ 177560) ∧ ∀ j, j ≤ 87866 → F wdB1 j ≤ 177560 :=
  ⟨fun j hj => Nat.le_trans (F_mono wdA0 hj) (by rw [FA0_87866]; omega),
   fun j hj => Nat.le_trans (F_mono wdA1 hj) (by rw [FA1_87866]; omega),
   fun j hj => Nat.le_trans (F_mono wdB0 hj) (by rw [FB0_87866]; omega),
   fun j hj => Nat.le_trans (F_mono wdB1 hj) (by rw [FB1_87866]; omega)⟩

/-! ### The headlines -/

/-- **From strip tick 177,560**, that is from tick at most 177,575 of its own clock, every array with the recurrence and a
black start carries the whole of one of the four strips through wheel 87,866. -/
theorem forced_front_four_uniform {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ (OnStrip a A0 s 177560 87866 ∨ OnStrip a A1 s 177560 87866 ∨
      OnStrip a B0 s 177560 87866 ∨ OnStrip a B1 s 177560 87866) := by
  obtain ⟨s, hs, h⟩ := forced_front_four ha ha0
  refine ⟨s, hs, ?_⟩
  rcases h with h | h | h | h
  · exact Or.inl (onStrip_of_alignedFrom fronts_le.1 h)
  · exact Or.inr (Or.inl (onStrip_of_alignedFrom fronts_le.2.1 h))
  · exact Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom fronts_le.2.2.1 h)))
  · exact Or.inr (Or.inr (Or.inr (onStrip_of_alignedFrom fronts_le.2.2.2 h)))

/-- **Every configuration with a leftmost black cell**, whatever lies to its right: on one of the four strips through wheel
87,866 from tick 177,560 + s of its own clock, s ≤ 15. -/
theorem forced_front_four_left_side {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false)
    (hlo : x lo = true) :
    ∃ s, s ≤ 15 ∧ (OnStrip (Ld x lo) A0 s 177560 87866 ∨ OnStrip (Ld x lo) A1 s 177560 87866 ∨
      OnStrip (Ld x lo) B0 s 177560 87866 ∨ OnStrip (Ld x lo) B1 s 177560 87866) :=
  forced_front_four_uniform (Ld_recurrence hleft) (by simpa [Ld, evol] using hlo)

/-- The single black cell. The proof does not say which strip. -/
theorem forced_front_four_seed :
    ∃ s, s ≤ 15 ∧ (OnStrip D A0 s 177560 87866 ∨ OnStrip D A1 s 177560 87866 ∨
      OnStrip D B0 s 177560 87866 ∨ OnStrip D B1 s 177560 87866) :=
  forced_front_four_uniform D_recurrence (D_zero 0)

/-- Below the first fork the four strips are one, so the front there comes sooner: `107,310`, the value `F 53207` of `Rule30ForcedFront`. -/
theorem F_low : F wdA0 53207 = 107310 ∧ F wdA1 53207 = 107310 ∧ F wdB0 53207 = 107310 ∧ F wdB1 53207 = 107310 := by
  have h0 : F wdA0 53207 = 107310 := F_of_S a_53207
  have h2 : F wdB0 53207 = 107310 := F_of_S b_53207
  exact ⟨h0, by rw [← h0]; exact (F_congr 53207 (fun i hi => wA1_eq_A0 i (by omega))).symm, h2,
    by rw [← h2]; exact (F_congr 53207 (fun i hi => wB1_eq_B0 i (by omega))).symm⟩

theorem low_front {a : Nat → Nat → Bool} {v s : Nat} {w : Nat → Nat} (hF : F w 53207 = 107310)
    (hs : ∀ j t, j ≤ 53207 → Sp v j t = Sp A0 j t) (h : AlignedFrom a v s (F w) 87866) : OnStrip a A0 s 107310 53207 :=
  fun j hj t ht => by
    rw [h j (by omega) t (Nat.le_trans (by rw [← hF]; exact F_mono w hj) ht)]
    exact hs j t hj

/-- **Through the first fork's wheel**: every array with the recurrence and a black start carries the strip of `A0` through wheel 53,207
from strip tick 107,310, that is from tick at most 107,325 of its own clock. -/
theorem forced_front_low {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ OnStrip a A0 s 107310 53207 := by
  obtain ⟨s, hs, h⟩ := forced_front_four ha ha0
  obtain ⟨f0, f1, f2, f3⟩ := F_low
  have eB0 : ∀ j t, j ≤ 53207 → Sp B0 j t = Sp A0 j t := fun j t hj =>
    low_of_phase A0_return B0_return low_B0 j t (by omega)
  refine ⟨s, hs, ?_⟩
  rcases h with h | h | h | h
  · exact low_front f0 (fun _ _ _ => rfl) h
  · exact low_front f1 (fun j t hj => low_of_phase A0_return A1_return low_A1 j t (by omega)) h
  · exact low_front f2 eB0 h
  · exact low_front f3 (fun j t hj => by
      rw [low_of_phase B0_return B1_return low_B1 j t (by omega)]; exact eB0 j t hj) h

/-- Every configuration with a leftmost black cell, through wheel 53,207 from tick 107,310 + s of its own clock, s ≤ 15. -/
theorem forced_front_low_left_side {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false)
    (hlo : x lo = true) : ∃ s, s ≤ 15 ∧ OnStrip (Ld x lo) A0 s 107310 53207 :=
  forced_front_low (Ld_recurrence hleft) (by simpa [Ld, evol] using hlo)

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30AgedLeftDiagonals", "Ruliology.CellularAutomata.Rule30FiniteDiagonals", "Ruliology.CellularAutomata.Rule30Diagonals"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"forced_front_four", "forced_front_four_uniform", "forced_front_four_left_side", "forced_front_four_seed", "classification_bounded",
   "forced_front_low", "forced_front_low_left_side", "FA0_87866", "FA1_87866", "FB0_87866", "FB1_87866"};
show[Take[heads, 5], "TypeForm"]
```

The statement below the first fork, and the four fronts:

```wl
show[Take[heads, -6], "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.forced_front_four_left_side"]["KernelCheck"]
```
