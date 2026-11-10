---
Template: ComputationalEssay
Name: If a Finite Row Survives, Its Free Word Is Not Sturmian-Like: Zero-Wall Diagonals, Bounded Lag and Rising Factor Complexity
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. Zero-wall left diagonals of rule 30 obey their recurrence from entry time, giving eventually black diagonals of every large index; hence a surviving finite row would have a free word with bounded-lag repeats and unbounded factor-complexity excess. Conditional on Q01 failing.
Abstract: In core Lean 4.35.0 we prove what a counterexample to the kit question Q01 would have to look like. A finite start of the zero-boundary left half of rule 30 that survives every even check is a finitely supported constrained row, and its values at the odd steps form its free word f. For such a row, for every K, the number of distinct length-n factors of f exceeds n + K for all large n; f cannot have the bounded complexity excess of Sturmian words. The route is unconditional up to its last step. For every finite row with last black cell at depth m, the diagonals measured from the moving edge obey the left-diagonal recurrence exactly from their entry time, when j + 2 <= m + t, equality included. From this we port the kit single-seed diagonal theory with entry-time guards: eventual periods 2 to the power j, a finite profile bound, and eventually black diagonals of arbitrarily large index. These force bounded lag for bounded-slack repeats of the free word. A word argument with explicit right-special witnesses then turns bounded lag into unbounded complexity excess. The free-word theorems are conditional: such rows exist only if Q01 fails. Nothing here decides Q01.
Keywords: [rule 30, Rule 30 Prize, period two, Q01, zero-boundary left half, left diagonals, factor complexity, right-special factors, Sturmian words, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

## 1. The statement

The kit's `Q01` asks whether every finite start of the zero-boundary left half of rule 30 eventually turns depth `1` white at an even time. A start that never does is a finite constrained row: it is black at depth `1` at every even step, and its values at the odd steps form its free word `f` (`freeWord`). If `Q01` holds there are no such rows. This module proves what any such row would have to satisfy.

- `freeWord_complexity`: the free word `f` of a finitely supported constrained row satisfies, for every `K`, `n + K < p_f(n)` for all large `n`. Here `p_f(n)` is the number of distinct length-`n` factors (`factorCount`). So `p_f(n) - n` tends to infinity; such a word cannot have the bounded excess of Sturmian or quasi-Sturmian words.
- `freeWord_bounded_lag`, `freeWord_bounded_lag_of_finSupp`: for every slack `K` there is a bound `B` with the following property. Whenever the length-`n` blocks of `f` at `i < j` agree and `j ≤ n + K`, the lag `j - i` is at most `B`.

These are conditional theorems. They say something only if `Q01` fails, and nothing here proves or refutes `Q01`.

The route has two parts that hold unconditionally.
- **Zero-wall diagonals.** For any finite row with last black cell at depth `m ≥ 1`, measure diagonals from the moving edge: `E j t = zrow L t (m + t - j)`.
  - `E_entry`: the left-diagonal recurrence holds exactly from the time the diagonal enters the half-line, `j + 2 ≤ m + t`, equality included.
  - `E_tailLeft` packages the edge-measured diagonals as an array whose recurrence holds at each index from some time on (`TailLeft`).
  - For every such array: each coordinate is eventually periodic with period `2^j` (`tail_periodic`); finitely many `Q`-periodic coordinates obey `M + 3 ≤ 4^Q` (`tail_profile_bound`); eventually white coordinates are unbounded, never adjacent, and followed two later by an eventually black one (`tail_white_unbounded`, `tail_no_two_white`, `tail_black_after_white`).
  - So eventually black diagonals occur at arbitrarily large index (`tail_black_unbounded`, `E_black_unbounded`).
- **Words.**
  - `factorCount_succ`: the factor count rises by the number of right-special factors.
  - `rightSpecialCount_pos`: there is at least one right-special factor of every length unless the word is eventually periodic.
  - `two_run`: two long maximal runs of one period force two distinct right-special factors of one length.
  - `complexity_of_bounded_lag`: an aperiodic word whose bounded-slack repeats have bounded lag has `p(n) - n → ∞`.

## 2. Zero-wall diagonals

The recurrence `E (j+2) (t+1) = E j t xor (E (j+1) t or E (j+2) t)` is rule 30 solved for its left input, read along the diagonal at fixed distance `j` from the edge. It is the kit's `zrow_succ` at depth `m + t - (j + 2)`. At equality the right input is the wall at depth `0`, which is white, so the recurrence still holds there. One step earlier the updated cell would be the wall itself, and the recurrence fails. The worked numbers show both.

So a diagonal obeys the recurrence only from its entry time. The kit's single-seed left-diagonal theory (`Rule30Diagonals`, `Rule30LeftReset`, `Rule30LeftUnbounded`) assumes the recurrence from time `0`. Here every argument takes the maximum of finitely many entry and period thresholds, and never one threshold for infinitely many indices. The periodic-profile bound reuses the kit's array-free inverse map and its pigeonhole: the `M + 3` profile pairs, the ghost pairs before the edge included, are pairwise distinct, so `M + 3 ≤ 4^Q`.

## 3. From black diagonals to bounded lag, and from bounded lag to complexity

Two steps of the constrained row shift its free word by one place (`row_eq_Theta`). With the kit's `Theta_dep`, two equal length-`n` blocks of `f` at `i` and `j` make the rows at times `2i` and `2j` agree through depth `2n + 1` (`rows_agree`).

Take an eventually black diagonal `b ≥ m + 2K - 1` with black onset `T`, and suppose the lag `j - i` exceeds `max(b/2, (T+1)/2)`. Then the later row has a black cell at depth `m + 2j - b`. That depth lies beyond the earlier row's support but inside the agreed range, which is a contradiction (`lag_le_of_black`). This gives `freeWord_bounded_lag`.

For the words, suppose `p(n) ≤ n + K` for arbitrarily large `n`. The excess `p(n) - n` never decreases, so it is eventually constant, and then there is exactly one right-special factor per length. By `two_run`, the `q`-periodic factors then have bounded length for each `q` (`perRun_bounded`). But two equal windows among the first `n + K + 1` positions have lag at most `B`, and their union is a periodic factor longer than any of those bounds. So `p(n) - n → ∞`.

## 4. Scope

- **Conditional.** The free-word theorems apply to finitely supported constrained rows, which exist only if `Q01` fails. If `Q01` holds they are vacuous. The diagonal theorems hold for every finite row.
- **No rate.** `p(n) - n → ∞` is qualitative. No rate is claimed.
- **Excluded.** The queue's separate near-square claim is not part of this module.
- **The count.** `factorCount` counts factor codes below `2^n`. `le_factorCount` and `factorCount_le` show it is exactly the number of distinct factors.

## 5. Worked numbers

The cell below runs the zero-boundary left half from the single black cell at depth `1` for 600 steps. It reports:
- whether the edge-diagonal recurrence holds at every point inside the guard `j + 2 ≤ m + t`, for `j ≤ 12`;
- whether it fails somewhere just outside the guard;
- whether each of `E_0, …, E_10` is periodic on the window `400 ≤ t < 600` with a period dividing `2^j`, and those minimal periods;
- whether the Fibonacci word, the standard Sturmian word, has exactly `n + 1` factors and one right-special factor of every length `n ≤ 12`.

That last line shows the boundary case `freeWord_complexity` excludes for free words.

```wl
T = 600; m = 1; width = m + T + 4;
rows = NestList[Function[r, Join[{0}, Table[BitXor[r[[k + 2]], BitOr[r[[k + 1]], r[[k]]]], {k, 1, width}], {0}]], Join[{0}, Table[If[k == m, 1, 0], {k, 1, width}], {0}], T + 1];
EE[j_, t_] := If[m + t - j >= 0, rows[[t + 1, m + t - j + 1]], 0];
inside = AllTrue[Flatten[Table[If[j + 2 <= m + t, EE[j + 2, t + 1] == BitXor[EE[j, t], BitOr[EE[j + 1, t], EE[j + 2, t]]], True], {t, 0, T - 1}, {j, 0, 12}]], TrueQ];
outside = AnyTrue[Flatten[Table[If[j + 2 == m + t + 1, EE[j + 2, t + 1] != BitXor[EE[j, t], BitOr[EE[j + 1, t], EE[j + 2, t]]], False], {t, 0, T - 1}, {j, 0, 12}]], TrueQ];
latePeriod[j_] := With[{s = Table[EE[j, t], {t, 400, 599}]}, SelectFirst[Range[200], Function[p, AllTrue[Range[Length[s] - p], s[[#]] == s[[# + p]] &]]]];
periods = latePeriod /@ Range[0, 10];
divides = AllTrue[Range[0, 10], Divisible[2^#, periods[[# + 1]]] &];
fibw = Take[Nest[{#[[2]], Join[#[[2]], #[[1]]]} &, {{0}, {0, 1}}, 25][[2]], 20000];
fibcounts = Table[With[{f = Union[Partition[Most[fibw], n, 1]], g = Union[Partition[Most[fibw], n + 1, 1]]}, {Length[f], Count[f, u_ /; MemberQ[g, Append[u, 0]] && MemberQ[g, Append[u, 1]]]}], {n, 1, 12}];
{inside, outside, divides, periods, fibcounts === Table[{n + 1, 1}, {n, 1, 12}]}
```

## 6. Prior art and scope

- **Words.** Morse and Hedlund (1938) show that an aperiodic word has at least `n + 1` factors of each length, and the identity `p(n+1) - p(n) =` (number of right-special factors) for binary words is classical (Cassaigne, *Complexité et facteurs spéciaux*, 1997). Both are reproved here in core Lean. The kit's `ShiftOrbit` and `WordsAutomata` contain the Morse–Hedlund equivalences in Mathlib form. Repetitions in low-complexity words are studied by Bugeaud and Kim (Trans. AMS 371, 2019). We claim no priority for the abstract implication `complexity_of_bounded_lag`.
- **Diagonals.** The left-diagonal theory and the profile bound are the kit's `Rule30Diagonals`, `Rule30LeftReset` and `Rule30LeftUnbounded`, for the single seed. This module ports them to the zero wall with entry-time guards. `Theta`, `Theta_dep` and `free_not_eventuallyPeriodic` are the kit's `Rule30ZeroBoundary`.
- **What is new.** The guarded zero-wall diagonal package, and the conclusion that the free word of any surviving finite row has unbounded complexity excess.
- **History.** The statement came from a sub-agent run of our programme and was carried by GPT. GPT then proposed this tail-recurrence route and the explicit word witnesses, and Local carried both. A Local sub-agent formalized it; Local read and checked it.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30LeftUnbounded` and `Rule30ZeroBoundary`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30LeftUnbounded
import Ruliology.CellularAutomata.Rule30ZeroBoundary
/-!
# Left diagonals of the zero-boundary left half, and bounded lag of the free word

Take a row `L` of the zero-boundary left half (`Rule30ZeroBoundary.zrow`) whose last black cell
is at depth `m ≥ 1`. Its edge moves out one depth per step (`zrow_edge`). Measure diagonals from
that moving edge: `E L m j t = zrow L t (m + t - j)`, with natural subtraction.

**The entry guard.**
* `E_entry`: for `j + 2 ≤ m + t`,
  `E (j + 2) (t + 1) = xor (E j t) (E (j + 1) t || E (j + 2) t)`. This is `zrow_succ` at depth
  `m + t - (j + 2)`; equality is allowed, where the right input is the white wall at depth `0`.
* `E_zero`, `E_one`: the diagonal `E 0` is always black, and `E 1` is black from time `1`.

So the left-diagonal recurrence holds at each index from some time on, but not from time `0`.
`TailLeft X` records exactly this for an arbitrary array `X j t`: the coordinates `0` and `1` are
eventually black, and the recurrence for `X (j + 2)` holds from a threshold depending on `j`.
`E_tailLeft` shows that `E L m` is such an array. No common threshold for infinitely many
indices is used; every argument takes the maximum of finitely many thresholds (`common_time`).

**The tail-left package** (each statement for every array with `TailLeft X`).
* `tail_periodic`: `EvPer (X j) (2 ^ j)` for every `j`, from the kit's `transducer_periodic`.
* `tail_profile_bound`: if `X 0, …, X (M + 1)` are all eventually `Q`-periodic with `Q > 0`, then
  `M + 3 ≤ 2 ^ (2 * Q)`. The profile pairs `prof` are inverted by the kit's array-free map
  `Rule30LeftUnbounded.B`, and are pairwise distinct.
* `tail_white_unbounded`: eventually white coordinates occur at arbitrarily large index.
* `tail_no_two_white`: no two consecutive coordinates are eventually white.
* `tail_black_after_white`: two steps after an eventually white coordinate comes an eventually
  black one.
* `tail_black_unbounded`: eventually black coordinates occur at arbitrarily large index.

The instances for the zero-wall diagonals are `E_periodic`, `E_profile_bound`,
`E_white_unbounded`, `E_no_two_white`, `E_black_after_white` and `E_black_unbounded`.

**Bounded lag of the free word.** The free word of a row is `freeWord L s = zrow L (2 s + 1) 1`,
column `-1` at the odd steps. For a constrained row (`InX L`) it is the unique `f` with
`zrow L 0 = Theta f` (`Theta_unique`), and `row_eq_Theta` shows the row at time `2 i` is `Theta`
of the shifted free word. With `Theta_dep`, two length-`n` blocks of the free word that agree
force the rows at times `2 i` and `2 j` to agree through depth `2 n + 1` (`rows_agree`).
* `freeWord_bounded_lag`: for a constrained row with last black cell at depth `m ≥ 1`, for every
  slack `K` there is a bound `B` such that whenever the length-`n` blocks of the free word at
  `i < j` agree and `j ≤ n + K`, the lag `j - i` is at most `B`.
* `freeWord_bounded_lag_of_finSupp` and `Theta_bounded_lag`: the same for every finitely
  supported constrained row, and for every `f` with `Theta f` finitely supported. Such rows exist
  only if the open question `Rule30ZeroBoundary.Q01` fails; these are conditional statements.

**Factor complexity.** `factorCount f n` is the number of distinct length-`n` blocks of a
one-sided Boolean word `f`, counted by their codes below `2 ^ n` (the kit's `code`).
`le_factorCount` and `factorCount_le` pin it down: it is at least the size of any family of
positions with pairwise distinct blocks, and at most the size of any family covering all blocks.
* `factorCount_succ`: `factorCount f (n + 1) = factorCount f n + rightSpecialCount f n`, the
  binary special-factor count (known; Cassaigne, *Complexité et facteurs spéciaux*, 1997).
* `rightSpecialCount_pos`: a word that is not eventually periodic has a right-special factor of
  every length (the step behind Morse and Hedlund's theorem; known).
* `two_run`: two maximal `q`-periodic runs with the same first `q` cells, of lengths `L` and
  `M ≥ L + q + 1`, give two distinct right-special factors of length `L + 1`.
* `perRun_bounded`: if eventually there is at most one right-special factor per length, the
  `q`-periodic factors have bounded length, for each `q ≥ 1`.
* `complexity_of_bounded_lag`: a word that is not eventually periodic and whose bounded-slack
  repeats have bounded lag satisfies, for every `K`, eventually `n + K < factorCount f n`.
* `freeWord_complexity` and `Theta_complexity`: hence the free word of a finitely supported
  constrained row, and every `f` with `Theta f` finitely supported, has `factorCount f n - n`
  tending to infinity.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

open Rule30Diagonals (transducer_periodic)
open Rule30LeftReset (EvPer EvWhite period_or_white white_forces_eq)
open Rule30Jen (EventuallyPeriodic)
open Rule30LeftUnbounded (B Bpow Bpow_zero win zero Trunc win_trunc zero_trunc xor_cancel
  pairCode pairCode_lt pairCode_inj pigeonhole code code_lt code_inj)
open Rule30ZeroBoundary

/-! ### The tail-left interface -/

/-- An array of left diagonals `X j t` (index `j`, time `t`) whose coordinates `0` and `1` are
eventually black, and whose left-diagonal recurrence for index `j + 2` holds from some time on,
the threshold depending on `j`. -/
structure TailLeft (X : Nat → Nat → Bool) : Prop where
  zero_black : ∃ T, ∀ t, T ≤ t → X 0 t = true
  one_black : ∃ T, ∀ t, T ≤ t → X 1 t = true
  step : ∀ j, ∃ S, ∀ t, S ≤ t → X (j + 2) (t + 1) = xor (X j t) (X (j + 1) t || X (j + 2) t)

/-- **Finitely many thresholds have a common bound.** -/
theorem common_time (P : Nat → Nat → Prop) (hmono : ∀ j S S', S ≤ S' → P j S → P j S') :
    ∀ n, (∀ j, j ≤ n → ∃ S, P j S) → ∃ S, ∀ j, j ≤ n → P j S := by
  intro n
  induction n with
  | zero =>
    intro h
    obtain ⟨S, hS⟩ := h 0 (Nat.le_refl 0)
    refine ⟨S, fun j hj => ?_⟩
    obtain rfl : j = 0 := by omega
    exact hS
  | succ n ih =>
    intro h
    obtain ⟨S, hS⟩ := ih (fun j hj => h j (by omega))
    obtain ⟨S', hS'⟩ := h (n + 1) (Nat.le_refl _)
    refine ⟨S + S', fun j hj => ?_⟩
    rcases Nat.lt_or_ge j (n + 1) with hlt | hge
    · exact hmono j S _ (by omega) (hS j (by omega))
    · obtain rfl : j = n + 1 := by omega
      exact hmono _ S' _ (by omega) hS'

/-- After a start `s` past the threshold, the recurrence holds at every shifted time. -/
theorem shift_step {X : Nat → Nat → Bool} {j S s : Nat}
    (hS : ∀ t, S ≤ t → X (j + 2) (t + 1) = xor (X j t) (X (j + 1) t || X (j + 2) t))
    (hs : S ≤ s) (t : Nat) :
    X (j + 2) (s + (t + 1)) = xor (X j (s + t)) (X (j + 1) (s + t) || X (j + 2) (s + t)) :=
  hS (s + t) (by omega)

/-! ### Lemma 1: each coordinate is eventually periodic with period `2 ^ j` -/

/-- **Every coordinate of a tail-left array is eventually periodic, with period `2 ^ j`.** -/
theorem tail_periodic {X : Nat → Nat → Bool} (hX : TailLeft X) : ∀ j, EvPer (X j) (2 ^ j) := by
  have pair : ∀ j, EvPer (X j) (2 ^ j) ∧ EvPer (X (j + 1)) (2 ^ (j + 1)) := by
    intro j
    induction j with
    | zero =>
      obtain ⟨T0, h0⟩ := hX.zero_black
      obtain ⟨T1, h1⟩ := hX.one_black
      exact ⟨⟨T0, fun t ht => by rw [h0 t ht, h0 _ (by omega)]⟩,
        ⟨T1, fun t ht => by rw [h1 t ht, h1 _ (by omega)]⟩⟩
    | succ j ih =>
      refine ⟨ih.2, ?_⟩
      obtain ⟨⟨Ta, ha⟩, ⟨Tb, hb⟩⟩ := ih
      obtain ⟨S, hS⟩ := hX.step j
      have hp := Nat.two_pow_pos j
      have ha2 : ∀ t, Ta ≤ t → X j (t + 2 ^ (j + 1)) = X j t := by
        intro t ht
        rw [show t + 2 ^ (j + 1) = (t + 2 ^ j) + 2 ^ j by rw [Nat.pow_succ]; omega,
          ha _ (by omega), ha t ht]
      refine ⟨Ta + Tb + S + 2 ^ (j + 1), fun t ht => ?_⟩
      have := transducer_periodic (x := X (j + 2))
        (F := fun t b => xor (X j t) (X (j + 1) t || b)) (T := Ta + Tb + S) (L := 2 ^ (j + 1))
        (fun t ht => hS t (by omega))
        (fun t ht => by
          funext b
          rw [ha2 t (by omega), hb t (by omega)])
        t (by omega)
      rw [show 2 ^ (j + 1 + 1) = 2 * 2 ^ (j + 1) by rw [Nat.pow_succ]; omega]
      exact this
  exact fun j => (pair j).1

/-! ### Lemma 2: the finite-profile bound -/

/-- The profile pairs of an array over the time window `[S, S + Q)`: two ghost pairs, then the
windows of consecutive coordinates. -/
def prof (X : Nat → Nat → Bool) (Q S : Nat) : Nat → (Nat → Bool) × (Nat → Bool)
  | 0 => (zero, zero)
  | 1 => (zero, win (X 0) Q S)
  | i + 2 => (win (X i) Q S, win (X (i + 1)) Q S)

theorem prof_trunc (X : Nat → Nat → Bool) (Q S : Nat) :
    ∀ i, Trunc Q (prof X Q S i).1 ∧ Trunc Q (prof X Q S i).2
  | 0 => ⟨zero_trunc Q, zero_trunc Q⟩
  | 1 => ⟨zero_trunc Q, win_trunc _ Q S⟩
  | _ + 2 => ⟨win_trunc _ Q S, win_trunc _ Q S⟩

/-- **The inverse update steps the profile back by one index.** It uses black coordinates `0`
and `1` on the window, the recurrence on the window for the indices `i + 2 ≤ m + 1`, and the
single wrap value `X j (S + Q) = X j S` for `j ≤ m + 1`. -/
theorem B_prof_succ {X : Nat → Nat → Bool} {m Q S : Nat} (hQ : 0 < Q)
    (h0 : ∀ t, S ≤ t → X 0 t = true) (h1 : ∀ t, S ≤ t → X 1 t = true)
    (hs : ∀ i, i + 2 ≤ m + 1 → ∀ t, S ≤ t →
      X (i + 2) (t + 1) = xor (X i t) (X (i + 1) t || X (i + 2) t))
    (hwrap : ∀ j, j ≤ m + 1 → X j (S + Q) = X j S) :
    ∀ i, i ≤ m + 1 → B Q (prof X Q S (i + 1)) = prof X Q S i := by
  have h0' : ∀ r, X 0 (S + r) = true := fun r => h0 _ (by omega)
  have h1' : ∀ r, X 1 (S + r) = true := fun r => h1 _ (by omega)
  intro i hi
  match i, hi with
  | 0, _ =>
    show B Q (zero, win (X 0) Q S) = (zero, zero)
    unfold B
    rw [Prod.mk.injEq]
    refine ⟨funext fun r => ?_, rfl⟩
    simp only [win, zero, h0']
    by_cases hr : r < Q
    · by_cases hr1 : r + 1 < Q <;> simp [hr, hr1, hQ]
    · simp [hr]
  | 1, _ =>
    show B Q (win (X 0) Q S, win (X 1) Q S) = (zero, win (X 0) Q S)
    unfold B
    rw [Prod.mk.injEq]
    refine ⟨funext fun r => ?_, rfl⟩
    simp only [win, zero, h0', h1']
    by_cases hr : r < Q
    · by_cases hr1 : r + 1 < Q <;> simp [hr, hr1, hQ]
    · simp [hr]
  | i + 2, hi =>
    show B Q (win (X (i + 1)) Q S, win (X (i + 2)) Q S) = (win (X i) Q S, win (X (i + 1)) Q S)
    unfold B
    rw [Prod.mk.injEq]
    refine ⟨funext fun r => ?_, rfl⟩
    have hstep := hs i (by omega) (S + r) (by omega)
    by_cases hr : r < Q
    · by_cases hr1 : r + 1 < Q
      · simp only [win, hr, hr1, ↓reduceIte]
        rw [show S + (r + 1) = S + r + 1 by omega, hstep, xor_cancel]
      · have hrq : Q = r + 1 := by omega
        simp only [win, hr, hr1, hQ, ↓reduceIte, Nat.add_zero]
        rw [← hwrap (i + 2) (by omega), hrq,
          show S + (r + 1) = S + r + 1 by omega, hstep, xor_cancel]
    · simp only [win, hr, ↓reduceIte]

theorem Bpow_prof {X : Nat → Nat → Bool} {m Q S : Nat} (hQ : 0 < Q)
    (h0 : ∀ t, S ≤ t → X 0 t = true) (h1 : ∀ t, S ≤ t → X 1 t = true)
    (hs : ∀ i, i + 2 ≤ m + 1 → ∀ t, S ≤ t →
      X (i + 2) (t + 1) = xor (X i t) (X (i + 1) t || X (i + 2) t))
    (hwrap : ∀ j, j ≤ m + 1 → X j (S + Q) = X j S) :
    ∀ k i, k ≤ i → i ≤ m + 2 → Bpow Q k (prof X Q S i) = prof X Q S (i - k) := by
  intro k
  induction k with
  | zero => intro i _ _; simp [Bpow]
  | succ k ih =>
    intro i hk hi
    simp only [Bpow]
    rw [ih i (by omega) hi, show i - k = (i - (k + 1)) + 1 by omega,
      B_prof_succ hQ h0 h1 hs hwrap (i - (k + 1)) (by omega)]

/-- The profile pairs with index at most `m + 2` are pairwise distinct. A repeat would send the
pair `(0, X 0)` to the fixed pair `(0, 0)`, against the black coordinate `0`. -/
theorem prof_ne {X : Nat → Nat → Bool} {m Q S : Nat} (hQ : 0 < Q)
    (h0 : ∀ t, S ≤ t → X 0 t = true) (h1 : ∀ t, S ≤ t → X 1 t = true)
    (hs : ∀ i, i + 2 ≤ m + 1 → ∀ t, S ≤ t →
      X (i + 2) (t + 1) = xor (X i t) (X (i + 1) t || X (i + 2) t))
    (hwrap : ∀ j, j ≤ m + 1 → X j (S + Q) = X j S) :
    ∀ a b, a < b → b ≤ m + 2 → prof X Q S a ≠ prof X Q S b := by
  intro a b hab hb heq
  have h1' : prof X Q S 0 = prof X Q S (b - a) := by
    have e1 := Bpow_prof hQ h0 h1 hs hwrap a a (Nat.le_refl _) (by omega)
    have e2 := Bpow_prof hQ h0 h1 hs hwrap a b (by omega) hb
    rw [Nat.sub_self] at e1
    rw [← e1, heq, e2]
  have h2 : prof X Q S 1 = (zero, zero) := by
    have e3 := Bpow_prof hQ h0 h1 hs hwrap (b - a - 1) (b - a) (by omega) (by omega)
    rw [show b - a - (b - a - 1) = 1 by omega] at e3
    rw [← e3, ← h1']
    exact Bpow_zero Q _
  have hS0 : X 0 S = true := h0 S (Nat.le_refl S)
  have := congrArg (fun p => p.2 0) h2
  simp [prof, win, zero, hQ, hS0] at this

/-- The profile bound on one window `[S, S + Q)`. -/
theorem prof_bound {X : Nat → Nat → Bool} {m Q S : Nat} (hQ : 0 < Q)
    (h0 : ∀ t, S ≤ t → X 0 t = true) (h1 : ∀ t, S ≤ t → X 1 t = true)
    (hs : ∀ i, i + 2 ≤ m + 1 → ∀ t, S ≤ t →
      X (i + 2) (t + 1) = xor (X i t) (X (i + 1) t || X (i + 2) t))
    (hwrap : ∀ j, j ≤ m + 1 → X j (S + Q) = X j S) : m + 3 ≤ 2 ^ (2 * Q) := by
  apply pigeonhole (2 ^ (2 * Q)) (m + 3) (fun i => pairCode Q (prof X Q S i))
  · intro i _; exact pairCode_lt Q _
  · intro i j hi hj hij
    have hij' : prof X Q S i = prof X Q S j :=
      pairCode_inj (prof_trunc X Q S i).1 (prof_trunc X Q S i).2 (prof_trunc X Q S j).1
        (prof_trunc X Q S j).2 hij
    rcases Nat.lt_trichotomy i j with h | h | h
    · exact absurd hij' (prof_ne hQ h0 h1 hs hwrap i j h (by omega))
    · exact h
    · exact absurd hij'.symm (prof_ne hQ h0 h1 hs hwrap j i h (by omega))

/-- **The finite-profile bound for a tail-left array.** If the coordinates `0, …, M + 1` are all
eventually `Q`-periodic, `Q > 0`, then `M + 3 ≤ 2 ^ (2 * Q)`. The window start is the maximum of
finitely many thresholds: the two black onsets, the periods through `M + 1`, and the recurrence
thresholds through `M + 1`. -/
theorem tail_profile_bound {X : Nat → Nat → Bool} (hX : TailLeft X) {M Q : Nat} (hQ : 0 < Q)
    (h : ∀ j, j ≤ M + 1 → EvPer (X j) Q) : M + 3 ≤ 2 ^ (2 * Q) := by
  obtain ⟨T0, h0⟩ := hX.zero_black
  obtain ⟨T1, h1⟩ := hX.one_black
  obtain ⟨Sp, hp⟩ := common_time (fun j S => ∀ t, S ≤ t → X j (t + Q) = X j t)
    (fun _ _ _ hle hP t ht => hP t (by omega)) (M + 1) (fun j hj => h j hj)
  obtain ⟨Ss, hss⟩ := common_time
    (fun i S => ∀ t, S ≤ t → X (i + 2) (t + 1) = xor (X i t) (X (i + 1) t || X (i + 2) t))
    (fun _ _ _ hle hP t ht => hP t (by omega)) (M + 1) (fun i _ => hX.step i)
  exact prof_bound (m := M) (S := T0 + T1 + Sp + Ss) hQ (fun t ht => h0 t (by omega))
    (fun t ht => h1 t (by omega)) (fun i hi t ht => hss i (by omega) t (by omega))
    (fun j hj => hp j hj _ (by omega))

/-! ### Lemma 3: eventually white coordinates are unbounded -/

/-- **Period or white, for a tail-left array.** If two consecutive coordinates are eventually
`Q`-periodic, then the next one is too, unless the nearer parent is eventually white. This is
the kit's `period_or_white` applied to the three sequences shifted past their thresholds. -/
theorem tail_evper_or_white {X : Nat → Nat → Bool} (hX : TailLeft X) {j Q : Nat}
    (ha : EvPer (X j) Q) (hb : EvPer (X (j + 1)) Q) :
    EvPer (X (j + 2)) Q ∨ EvWhite (X (j + 1)) := by
  obtain ⟨Ta, ha⟩ := ha
  obtain ⟨Tb, hb⟩ := hb
  obtain ⟨S, hS⟩ := hX.step j
  obtain ⟨s, hsa, hsb, hsS⟩ : ∃ s, Ta ≤ s ∧ Tb ≤ s ∧ S ≤ s :=
    ⟨Ta + Tb + S, by omega, by omega, by omega⟩
  rcases period_or_white (x := fun t => X (j + 2) (s + t)) (a := fun t => X j (s + t))
      (b := fun t => X (j + 1) (s + t)) (s := 0) (L := Q)
      (shift_step hS hsS)
      (fun t _ => by
        show X j (s + (t + Q)) = X j (s + t)
        rw [← Nat.add_assoc]; exact ha _ (by omega))
      (fun t _ => by
        show X (j + 1) (s + (t + Q)) = X (j + 1) (s + t)
        rw [← Nat.add_assoc]; exact hb _ (by omega)) with h | h
  · refine Or.inl ⟨s + Q, fun t ht => ?_⟩
    obtain ⟨u, rfl⟩ : ∃ u, t = s + u := ⟨t - s, by omega⟩
    have e : X (j + 2) (s + (u + Q)) = X (j + 2) (s + u) := h u (by omega)
    rw [Nat.add_assoc]; exact e
  · refine Or.inr ⟨s, fun t ht => ?_⟩
    have e : X (j + 1) (s + (t - s)) = false := h (t - s) (Nat.zero_le _)
    rwa [show s + (t - s) = t by omega] at e

/-- **Eventually white coordinates of a tail-left array occur at arbitrarily large index.** If
none occurs above `N`, every coordinate has the common eventual period `2 ^ (N + 1)`, and the
finite-profile bound fails for a long enough prefix. -/
theorem tail_white_unbounded {X : Nat → Nat → Bool} (hX : TailLeft X) (N : Nat) :
    ∃ j, N < j ∧ EvWhite (X j) := by
  refine Classical.byContradiction fun hne => ?_
  have hN : ∀ j, N < j → ¬ EvWhite (X j) := fun j hj hw => hne ⟨j, hj, hw⟩
  have hQ : 0 < 2 ^ (N + 1) := Nat.two_pow_pos _
  have low : ∀ j, j ≤ N + 1 → EvPer (X j) (2 ^ (N + 1)) := fun j hj =>
    Rule30LeftUnbounded.EvPer.of_dvd (tail_periodic hX j) (Nat.pow_dvd_pow 2 hj)
  have pair : ∀ j, EvPer (X j) (2 ^ (N + 1)) ∧ EvPer (X (j + 1)) (2 ^ (N + 1)) := by
    intro j
    induction j with
    | zero => exact ⟨low 0 (by omega), low 1 (by omega)⟩
    | succ j ih =>
      refine ⟨ih.2, ?_⟩
      by_cases hj : j + 2 ≤ N + 1
      · exact low _ hj
      · rcases tail_evper_or_white hX ih.1 ih.2 with h | h
        · exact h
        · exact absurd h (hN (j + 1) (by omega))
  have := tail_profile_bound hX hQ (M := 2 ^ (2 * 2 ^ (N + 1))) (fun j _ => (pair j).1)
  omega

/-! ### Lemma 4: no two consecutive eventually white coordinates -/

/-- **No two consecutive coordinates of a tail-left array are eventually white.** Two white
children force their parents equal (the kit's `white_forces_eq`, past the threshold), which
propagates back to the eventually black coordinate `0`. -/
theorem tail_no_two_white {X : Nat → Nat → Bool} (hX : TailLeft X) :
    ∀ j, ¬ (EvWhite (X j) ∧ EvWhite (X (j + 1))) := by
  intro j
  induction j with
  | zero =>
    rintro ⟨⟨T, hT⟩, _⟩
    obtain ⟨T0, h0⟩ := hX.zero_black
    have e := hT (T + T0) (by omega)
    rw [h0 _ (by omega)] at e
    exact Bool.noConfusion e
  | succ j ih =>
    rintro ⟨⟨T1, h1⟩, ⟨T2, h2⟩⟩
    obtain ⟨S, hS⟩ := hX.step j
    apply ih
    refine ⟨⟨T1 + T2 + S, fun t ht => ?_⟩, ⟨T1, h1⟩⟩
    have hs : S ≤ T1 + T2 + S := by omega
    have heq := white_forces_eq (x := fun u => X (j + 2) (T1 + T2 + S + u))
      (a := fun u => X j (T1 + T2 + S + u)) (b := fun u => X (j + 1) (T1 + T2 + S + u))
      (s := 0) (shift_step hS hs) (fun u _ => h2 _ (by omega)) (t - (T1 + T2 + S))
      (Nat.zero_le _)
    have e : X j (T1 + T2 + S + (t - (T1 + T2 + S))) =
        X (j + 1) (T1 + T2 + S + (t - (T1 + T2 + S))) := heq
    rw [show T1 + T2 + S + (t - (T1 + T2 + S)) = t by omega] at e
    rw [e]
    exact h1 t (by omega)

/-! ### Lemma 5: two steps after an eventually white coordinate, an eventually black one -/

/-- **Two steps after an eventually white coordinate of a tail-left array comes an eventually
black one.** The middle coordinate is black at some time past the white onset and the
threshold; that sets the coordinate two steps on to black, and the recurrence then keeps it
black. -/
theorem tail_black_after_white {X : Nat → Nat → Bool} (hX : TailLeft X) {j : Nat}
    (hw : EvWhite (X j)) : ∃ T, ∀ t, T ≤ t → X (j + 2) t = true := by
  obtain ⟨T, hT⟩ := hw
  obtain ⟨S, hS⟩ := hX.step j
  have hnw : ¬ EvWhite (X (j + 1)) := fun h => tail_no_two_white hX j ⟨⟨T, hT⟩, h⟩
  have hex : ∃ t0, T + S ≤ t0 ∧ X (j + 1) t0 = true := by
    refine Classical.byContradiction fun h => hnw ⟨T + S, fun t ht => ?_⟩
    cases hb : X (j + 1) t
    · rfl
    · exact absurd ⟨t, ht, hb⟩ h
  obtain ⟨t0, ht0, hb⟩ := hex
  refine ⟨t0 + 1, fun t ht => ?_⟩
  obtain ⟨n, rfl⟩ : ∃ n, t = t0 + 1 + n := ⟨t - (t0 + 1), by omega⟩
  induction n with
  | zero =>
    rw [Nat.add_zero, hS t0 (by omega), hT t0 (by omega), hb]
    rfl
  | succ n ih =>
    rw [show t0 + 1 + (n + 1) = (t0 + 1 + n) + 1 by omega, hS _ (by omega), hT _ (by omega),
      ih (by omega)]
    simp

/-- **Eventually black coordinates of a tail-left array occur at arbitrarily large index.** -/
theorem tail_black_unbounded {X : Nat → Nat → Bool} (hX : TailLeft X) (N : Nat) :
    ∃ b, N < b ∧ ∃ T, ∀ t, T ≤ t → X b t = true := by
  obtain ⟨j, hj, hw⟩ := tail_white_unbounded hX N
  exact ⟨j + 2, by omega, tail_black_after_white hX hw⟩

/-! ### The zero-wall diagonals -/

/-- The edge-measured left diagonals of a run: `E L m j t` is the cell at time `t` that lies `j`
depths inside the depth `m + t` (natural subtraction). When the last black cell of `L` is at
depth `m`, the depth `m + t` is the edge at time `t`. -/
def E (L : Nat → Bool) (m j t : Nat) : Bool := zrow L t (m + t - j)

/-- **The zero-wall entry guard.** For `j + 2 ≤ m + t`, equality included, the edge-measured
diagonals obey the left-diagonal recurrence. It is `zrow_succ` at depth `m + t - (j + 2)`; at
equality the right input is the white wall at depth `0`, and the updated cell is at depth `1`. -/
theorem E_entry (L : Nat → Bool) (m j t : Nat) (h : j + 2 ≤ m + t) :
    E L m (j + 2) (t + 1) = xor (E L m j t) (E L m (j + 1) t || E L m (j + 2) t) := by
  obtain ⟨k, hk⟩ : ∃ k, m + t = j + 2 + k := ⟨m + t - (j + 2), by omega⟩
  unfold E
  rw [show m + (t + 1) - (j + 2) = k + 1 by omega, show m + t - j = k + 2 by omega,
    show m + t - (j + 1) = k + 1 by omega, show m + t - (j + 2) = k by omega]
  exact zrow_succ L t k

/-- **The edge diagonal is always black.** -/
theorem E_zero {L : Nat → Bool} {m : Nat} (hm : 1 ≤ m) (hedge : L m = true)
    (hfin : ∀ k, m < k → L k = false) (t : Nat) : E L m 0 t = true := by
  unfold E
  rw [Nat.sub_zero]
  exact (zrow_edge hm hedge hfin t).1

/-- **The diagonal next to the edge is black from time `1`.** -/
theorem E_one {L : Nat → Bool} {m : Nat} (hm : 1 ≤ m) (hedge : L m = true)
    (hfin : ∀ k, m < k → L k = false) (t : Nat) : E L m 1 (t + 1) = true := by
  have hE := zrow_edge hm hedge hfin t
  obtain ⟨k, hk⟩ : ∃ k, m + t = k + 1 := ⟨m + t - 1, by omega⟩
  unfold E
  rw [show m + (t + 1) - 1 = k + 1 by omega, zrow_succ, hE.2 (k + 2) (by omega),
    show k + 1 = m + t by omega, hE.1]
  rfl

/-- **The zero-wall diagonals form a tail-left array.** The recurrence for index `j + 2` holds
from time `(j + 2) - m` (natural subtraction). -/
theorem E_tailLeft {L : Nat → Bool} {m : Nat} (hm : 1 ≤ m) (hedge : L m = true)
    (hfin : ∀ k, m < k → L k = false) : TailLeft (E L m) where
  zero_black := ⟨0, fun t _ => E_zero hm hedge hfin t⟩
  one_black := ⟨1, fun t ht => by
    obtain ⟨s, rfl⟩ : ∃ s, t = s + 1 := ⟨t - 1, by omega⟩
    exact E_one hm hedge hfin s⟩
  step j := ⟨j + 2 - m, fun t ht => E_entry L m j t (by omega)⟩

theorem E_periodic {L : Nat → Bool} {m : Nat} (hm : 1 ≤ m) (hedge : L m = true)
    (hfin : ∀ k, m < k → L k = false) : ∀ j, EvPer (E L m j) (2 ^ j) :=
  tail_periodic (E_tailLeft hm hedge hfin)

theorem E_profile_bound {L : Nat → Bool} {m : Nat} (hm : 1 ≤ m) (hedge : L m = true)
    (hfin : ∀ k, m < k → L k = false) {M Q : Nat} (hQ : 0 < Q)
    (h : ∀ j, j ≤ M + 1 → EvPer (E L m j) Q) : M + 3 ≤ 2 ^ (2 * Q) :=
  tail_profile_bound (E_tailLeft hm hedge hfin) hQ h

theorem E_white_unbounded {L : Nat → Bool} {m : Nat} (hm : 1 ≤ m) (hedge : L m = true)
    (hfin : ∀ k, m < k → L k = false) (N : Nat) : ∃ j, N < j ∧ EvWhite (E L m j) :=
  tail_white_unbounded (E_tailLeft hm hedge hfin) N

theorem E_no_two_white {L : Nat → Bool} {m : Nat} (hm : 1 ≤ m) (hedge : L m = true)
    (hfin : ∀ k, m < k → L k = false) : ∀ j, ¬ (EvWhite (E L m j) ∧ EvWhite (E L m (j + 1))) :=
  tail_no_two_white (E_tailLeft hm hedge hfin)

theorem E_black_after_white {L : Nat → Bool} {m : Nat} (hm : 1 ≤ m) (hedge : L m = true)
    (hfin : ∀ k, m < k → L k = false) {j : Nat} (hw : EvWhite (E L m j)) :
    ∃ T, ∀ t, T ≤ t → E L m (j + 2) t = true :=
  tail_black_after_white (E_tailLeft hm hedge hfin) hw

/-- **Eventually black zero-wall diagonals occur at arbitrarily large index**: for every `N`
there is `b > N` and a time `T` with `zrow L t (m + t - b)` black for all `t ≥ T`. -/
theorem E_black_unbounded {L : Nat → Bool} {m : Nat} (hm : 1 ≤ m) (hedge : L m = true)
    (hfin : ∀ k, m < k → L k = false) (N : Nat) :
    ∃ b, N < b ∧ ∃ T, ∀ t, T ≤ t → zrow L t (m + t - b) = true :=
  tail_black_unbounded (E_tailLeft hm hedge hfin) N

/-! ### Bounded lag of the free word -/

/-- The free word of a row: column `-1` at the odd steps. For a constrained row `L` it is the
unique `f` with `zrow L 0 = Theta f` (`Theta_unique`). -/
def freeWord (L : Nat → Bool) (s : Nat) : Bool := zrow L (2 * s + 1) 1

theorem freeWord_Theta (L : Nat → Bool) (hX : InX L) : zrow L 0 = Theta (freeWord L) :=
  Theta_unique hX fun _ => rfl

/-- **The row at an even time is `Theta` of the shifted free word.** -/
theorem row_eq_Theta {L : Nat → Bool} (hX : InX L) (i : Nat) :
    zrow L (2 * i) = Theta (fun s => freeWord L (s + i)) := by
  have hX' : InX (zrow L (2 * i)) := by
    intro s
    rw [← zrow_shift, show 2 * i + 2 * s = 2 * (i + s) by omega]
    exact hX (i + s)
  have e := Theta_unique hX' (f := fun s => freeWord L (s + i)) (fun s => by
    rw [← zrow_shift, show 2 * i + (2 * s + 1) = 2 * (s + i) + 1 by omega]
    rfl)
  rwa [zrow_zero_self (zrow_wall L (2 * i))] at e

/-- **Agreeing blocks give agreeing rows.** If the length-`n` blocks of the free word at `i` and
`j` agree, the rows at times `2 i` and `2 j` agree through depth `2 n + 1`. -/
theorem rows_agree {L : Nat → Bool} (hX : InX L) {i j n : Nat}
    (h : ∀ r, r < n → freeWord L (i + r) = freeWord L (j + r)) :
    ∀ k, k ≤ 2 * n + 1 → zrow L (2 * i) k = zrow L (2 * j) k := by
  intro k hk
  rw [row_eq_Theta hX i, row_eq_Theta hX j]
  apply Theta_dep
  intro s hs
  show freeWord L (s + i) = freeWord L (s + j)
  rw [Nat.add_comm s i, Nat.add_comm s j]
  exact h s (by omega)

/-- **An eventually black diagonal bounds the lag.** Let the zero-wall diagonal `b` be black
from time `T`, with `m + 2 K ≤ b + 1`. If the length-`n` blocks of the free word at `i < j`
agree and `j ≤ n + K`, then `j - i ≤ max (b / 2) ((T + 1) / 2)`. Otherwise the black cell of
row `2 j` at depth `m + 2 j - b` lies beyond the edge of row `2 i`, within the depth where the
two rows agree. -/
theorem lag_le_of_black {L : Nat → Bool} {m : Nat} (hm : 1 ≤ m) (hedge : L m = true)
    (hfin : ∀ k, m < k → L k = false) (hX : InX L) {K b T : Nat} (hb : m + 2 * K ≤ b + 1)
    (hT : ∀ t, T ≤ t → zrow L t (m + t - b) = true) {i j n : Nat} (hij : i < j)
    (hjn : j ≤ n + K) (h : ∀ r, r < n → freeWord L (i + r) = freeWord L (j + r)) :
    j - i ≤ max (b / 2) ((T + 1) / 2) := by
  refine Nat.le_of_not_lt fun hlag => ?_
  have hm1 := Nat.le_max_left (b / 2) ((T + 1) / 2)
  have hm2 := Nat.le_max_right (b / 2) ((T + 1) / 2)
  have hblack := hT (2 * j) (by omega)
  have hwhite := (zrow_edge hm hedge hfin (2 * i)).2 (m + 2 * j - b) (by omega)
  rw [rows_agree hX h (m + 2 * j - b) (by omega), hblack] at hwhite
  exact Bool.noConfusion hwhite

/-- **Bounded lag of the free word of a finite constrained row.** Let `L` be constrained, with
last black cell at depth `m ≥ 1`. For every slack `K` there is `B` such that whenever the
length-`n` blocks of the free word at `i < j` agree and `j ≤ n + K`, the lag `j - i` is at
most `B`. -/
theorem freeWord_bounded_lag {L : Nat → Bool} {m : Nat} (hm : 1 ≤ m) (hedge : L m = true)
    (hfin : ∀ k, m < k → L k = false) (hX : InX L) :
    ∀ K, ∃ B, ∀ i j n, i < j → j ≤ n + K →
      (∀ r, r < n → freeWord L (i + r) = freeWord L (j + r)) → j - i ≤ B := by
  intro K
  obtain ⟨b, hb, T, hT⟩ := E_black_unbounded hm hedge hfin (m + 2 * K)
  exact ⟨max (b / 2) ((T + 1) / 2), fun i j n hij hjn h =>
    lag_le_of_black hm hedge hfin hX (by omega) hT hij hjn h⟩

/-- **Bounded lag for every finitely supported constrained row.** -/
theorem freeWord_bounded_lag_of_finSupp {L : Nat → Bool} (hfin : FinSupp L) (hX : InX L) :
    ∀ K, ∃ B, ∀ i j n, i < j → j ≤ n + K →
      (∀ r, r < n → freeWord L (i + r) = freeWord L (j + r)) → j - i ≤ B := by
  obtain ⟨W, hW⟩ := hfin
  obtain ⟨m, hm, hedge, hz⟩ := last_black (show L 1 = true from hX 0) W hW
  exact freeWord_bounded_lag hm hedge hz hX

/-- **Bounded lag for free bits with a finitely supported constrained start.** If `Theta f` is
finitely supported, then for every slack `K` there is `B` such that whenever the length-`n`
blocks of `f` at `i < j` agree and `j ≤ n + K`, the lag `j - i` is at most `B`. -/
theorem Theta_bounded_lag (f : Nat → Bool) (hfin : FinSupp (Theta f)) :
    ∀ K, ∃ B, ∀ i j n, i < j → j ≤ n + K →
      (∀ r, r < n → f (i + r) = f (j + r)) → j - i ≤ B := by
  intro K
  obtain ⟨B, hB⟩ := freeWord_bounded_lag_of_finSupp hfin (Theta_inX f) K
  have hf : ∀ s, freeWord (Theta f) s = f s := Theta_free f
  exact ⟨B, fun i j n hij hjn hr => hB i j n hij hjn (fun r hr' => by
    rw [hf, hf]; exact hr r hr')⟩

/-! ### Factor complexity of a one-sided word -/

theorem code_congr {g h : Nat → Bool} : ∀ n, (∀ r, r < n → g r = h r) → code g n = code h n
  | 0, _ => rfl
  | n + 1, hgh => by
    show code g n + (if g n then 2 ^ n else 0) = code h n + (if h n then 2 ^ n else 0)
    rw [code_congr n (fun r hr => hgh r (by omega)), hgh n (by omega)]

/-- The code of the length-`n` block of `f` at position `i` (the kit's `code`). -/
def blk (f : Nat → Bool) (i n : Nat) : Nat := code (fun r => f (i + r)) n

theorem blk_lt (f : Nat → Bool) (i n : Nat) : blk f i n < 2 ^ n := code_lt _ n

theorem blk_succ (f : Nat → Bool) (i n : Nat) :
    blk f i (n + 1) = blk f i n + (if f (i + n) then 2 ^ n else 0) := rfl

theorem blk_succ_false {f : Nat → Bool} {i n : Nat} (h : f (i + n) = false) :
    blk f i (n + 1) = blk f i n := by
  have e := blk_succ f i n
  rw [h] at e
  exact e

theorem blk_succ_true {f : Nat → Bool} {i n : Nat} (h : f (i + n) = true) :
    blk f i (n + 1) = blk f i n + 2 ^ n := by
  have e := blk_succ f i n
  rw [h] at e
  exact e

/-- Two blocks have the same code exactly when they agree cell by cell. -/
theorem blk_eq_iff (f : Nat → Bool) (i j n : Nat) :
    blk f i n = blk f j n ↔ ∀ r, r < n → f (i + r) = f (j + r) :=
  ⟨fun h => code_inj _ _ n h, fun h => code_congr n h⟩

open Classical in
/-- The number of `c < N` with `P c`. -/
noncomputable def countBelow (P : Nat → Prop) : Nat → Nat
  | 0 => 0
  | N + 1 => countBelow P N + if P N then 1 else 0

theorem countBelow_succ_pos {P : Nat → Prop} {N : Nat} (h : P N) :
    countBelow P (N + 1) = countBelow P N + 1 := by
  simp only [countBelow, h, ↓reduceIte]

theorem countBelow_succ_neg {P : Nat → Prop} {N : Nat} (h : ¬ P N) :
    countBelow P (N + 1) = countBelow P N := by
  simp only [countBelow, h, ↓reduceIte, Nat.add_zero]

theorem countBelow_le_succ (P : Nat → Prop) (N : Nat) :
    countBelow P N ≤ countBelow P (N + 1) := by
  by_cases h : P N
  · have := countBelow_succ_pos h; omega
  · have := countBelow_succ_neg h; omega

theorem countBelow_mono (P : Nat → Prop) {N M : Nat} (h : N ≤ M) :
    countBelow P N ≤ countBelow P M := by
  obtain ⟨d, rfl⟩ : ∃ d, M = N + d := ⟨M - N, by omega⟩
  induction d with
  | zero => exact Nat.le_refl _
  | succ d ih => exact Nat.le_trans (ih (by omega)) (countBelow_le_succ P _)

theorem countBelow_lt_of {P : Nat → Prop} {c M : Nat} (hc : c < M) (h : P c) :
    countBelow P c < countBelow P M := by
  have e1 := countBelow_succ_pos h
  have e2 := countBelow_mono P (show c + 1 ≤ M by omega)
  omega

theorem countBelow_congr {P Q : Nat → Prop} :
    ∀ N, (∀ c, c < N → (P c ↔ Q c)) → countBelow P N = countBelow Q N
  | 0, _ => rfl
  | N + 1, h => by
    have ih := countBelow_congr N (fun c hc => h c (by omega))
    by_cases hp : P N
    · have e1 := countBelow_succ_pos hp
      have e2 := countBelow_succ_pos ((h N (by omega)).1 hp)
      omega
    · have e1 := countBelow_succ_neg hp
      have e2 := countBelow_succ_neg (fun hq => hp ((h N (by omega)).2 hq))
      omega

theorem countBelow_add (P : Nat → Prop) (A : Nat) : ∀ B,
    countBelow P (A + B) = countBelow P A + countBelow (fun c => P (A + c)) B
  | 0 => rfl
  | B + 1 => by
    have ih := countBelow_add P A B
    rw [show A + (B + 1) = (A + B) + 1 by omega]
    by_cases hp : P (A + B)
    · have e1 := countBelow_succ_pos (N := A + B) hp
      have e2 := countBelow_succ_pos (P := fun c => P (A + c)) (N := B) hp
      omega
    · have e1 := countBelow_succ_neg (N := A + B) hp
      have e2 := countBelow_succ_neg (P := fun c => P (A + c)) (N := B) hp
      omega

theorem countBelow_or_and (P Q : Nat → Prop) : ∀ N,
    countBelow P N + countBelow Q N =
      countBelow (fun c => P c ∨ Q c) N + countBelow (fun c => P c ∧ Q c) N
  | 0 => rfl
  | N + 1 => by
    have ih := countBelow_or_and P Q N
    by_cases hp : P N <;> by_cases hq : Q N
    · have e1 := countBelow_succ_pos hp
      have e2 := countBelow_succ_pos hq
      have e3 := countBelow_succ_pos (P := fun c => P c ∨ Q c) (Or.inl hp)
      have e4 := countBelow_succ_pos (P := fun c => P c ∧ Q c) ⟨hp, hq⟩
      omega
    · have e1 := countBelow_succ_pos hp
      have e2 := countBelow_succ_neg hq
      have e3 := countBelow_succ_pos (P := fun c => P c ∨ Q c) (Or.inl hp)
      have e4 := countBelow_succ_neg (P := fun c => P c ∧ Q c) (fun h => hq h.2)
      omega
    · have e1 := countBelow_succ_neg hp
      have e2 := countBelow_succ_pos hq
      have e3 := countBelow_succ_pos (P := fun c => P c ∨ Q c) (Or.inr hq)
      have e4 := countBelow_succ_neg (P := fun c => P c ∧ Q c) (fun h => hp h.1)
      omega
    · have e1 := countBelow_succ_neg hp
      have e2 := countBelow_succ_neg hq
      have e3 := countBelow_succ_neg (P := fun c => P c ∨ Q c) (fun h => h.elim hp hq)
      have e4 := countBelow_succ_neg (P := fun c => P c ∧ Q c) (fun h => hp h.1)
      omega

/-- An injection of `N` positions into the codes below `M` satisfying `P` gives `N` such codes.
The rank `countBelow P c` of each code is injective on `P`, so the kit's `pigeonhole` applies. -/
theorem le_countBelow {P : Nat → Prop} {M N : Nat} (g : Nat → Nat)
    (hg : ∀ i, i < N → g i < M ∧ P (g i))
    (hinj : ∀ i j, i < N → j < N → g i = g j → i = j) : N ≤ countBelow P M := by
  apply pigeonhole (countBelow P M) N (fun i => countBelow P (g i))
  · intro i hi; exact countBelow_lt_of (hg i hi).1 (hg i hi).2
  · intro i j hi hj hij
    apply hinj i j hi hj
    rcases Nat.lt_trichotomy (g i) (g j) with h | h | h
    · exact absurd hij (Nat.ne_of_lt (countBelow_lt_of h (hg i hi).2))
    · exact h
    · exact absurd hij.symm (Nat.ne_of_lt (countBelow_lt_of h (hg j hj).2))

theorem two_le_countBelow {P : Nat → Prop} {c d M : Nat} (hcd : c < d) (hd : d < M)
    (h1 : P c) (h2 : P d) : 2 ≤ countBelow P M := by
  have e1 := countBelow_lt_of hcd h1
  have e2 := countBelow_lt_of hd h2
  omega

/-- `c` is the code of a length-`n` factor of `f`. -/
def Occurs (f : Nat → Bool) (n c : Nat) : Prop := ∃ i, blk f i n = c

/-- `c` is the code of a right-special length-`n` factor of `f`: an occurrence followed by a
white cell, and one followed by a black cell. -/
def RightSpecial (f : Nat → Bool) (n c : Nat) : Prop :=
  (∃ i, blk f i n = c ∧ f (i + n) = false) ∧ (∃ i, blk f i n = c ∧ f (i + n) = true)

/-- The factor complexity of `f`: the number of distinct length-`n` blocks, counted by their
codes below `2 ^ n`. -/
noncomputable def factorCount (f : Nat → Bool) (n : Nat) : Nat := countBelow (Occurs f n) (2 ^ n)

/-- The number of right-special length-`n` factors of `f`. -/
noncomputable def rightSpecialCount (f : Nat → Bool) (n : Nat) : Nat :=
  countBelow (RightSpecial f n) (2 ^ n)

theorem countBelow_false : ∀ M, countBelow (fun _ => False) M = 0
  | 0 => rfl
  | M + 1 => (countBelow_succ_neg (P := fun _ => False) (N := M) id).trans (countBelow_false M)

theorem countBelow_le_of_imp {P Q : Nat → Prop} :
    ∀ M, (∀ c, c < M → P c → Q c) → countBelow P M ≤ countBelow Q M
  | 0, _ => Nat.le_refl 0
  | M + 1, h => by
    have ih := countBelow_le_of_imp M (fun c hc => h c (by omega))
    by_cases hp : P M
    · have e1 := countBelow_succ_pos hp
      have e2 := countBelow_succ_pos (h M (by omega) hp)
      omega
    · have e1 := countBelow_succ_neg hp
      have e2 := countBelow_le_succ Q M
      omega

theorem countBelow_eq_le_one (x : Nat) : ∀ M, countBelow (fun c => c = x) M ≤ 1 := by
  intro M
  induction M with
  | zero => exact Nat.zero_le 1
  | succ M ih =>
    by_cases hx : M = x
    · have h0 := countBelow_le_of_imp (P := fun c => c = x) (Q := fun _ => False) M
        (fun c hc hcx => absurd (show c = x from hcx) (by omega))
      have hF := countBelow_false M
      have e := countBelow_succ_pos (P := fun c => c = x) hx
      omega
    · have e := countBelow_succ_neg (P := fun c => c = x) hx
      omega

/-- If the codes below `M` satisfying `P` are all among `h 0, …, h (N - 1)`, at most `N` of them
satisfy `P`. -/
theorem countBelow_le_of_cover (h : Nat → Nat) : ∀ N (P : Nat → Prop) M,
    (∀ c, c < M → P c → ∃ k, k < N ∧ h k = c) → countBelow P M ≤ N := by
  intro N
  induction N with
  | zero =>
    intro P M hcov
    have e1 := countBelow_le_of_imp (P := P) (Q := fun _ => False) M (fun c hc hp => by
      obtain ⟨k, hk, _⟩ := hcov c hc hp
      omega)
    have e2 := countBelow_false M
    omega
  | succ N ih =>
    intro P M hcov
    have e1 := countBelow_le_of_imp (P := P)
      (Q := fun c => (∃ k, k < N ∧ h k = c) ∨ c = h N) M (fun c hc hp => by
        obtain ⟨k, hk, hkc⟩ := hcov c hc hp
        by_cases hkN : k < N
        · exact Or.inl ⟨k, hkN, hkc⟩
        · exact Or.inr (by rw [← hkc, show k = N by omega]))
    have e2 := countBelow_or_and (fun c => ∃ k, k < N ∧ h k = c) (fun c => c = h N) M
    have e3 := ih (fun c => ∃ k, k < N ∧ h k = c) M (fun c _ hc => hc)
    have e4 := countBelow_eq_le_one (h N) M
    omega

/-- **`factorCount` is at least the size of every family of positions with pairwise distinct
length-`n` blocks.** -/
theorem le_factorCount (f : Nat → Bool) (n N : Nat) (g : Nat → Nat)
    (hg : ∀ k l, k < N → l < N → (∀ r, r < n → f (g k + r) = f (g l + r)) → k = l) :
    N ≤ factorCount f n :=
  le_countBelow (fun k => blk f (g k) n) (fun k _ => ⟨blk_lt f _ n, g k, rfl⟩)
    (fun k l hk hl hkl => hg k l hk hl ((blk_eq_iff f _ _ n).1 hkl))

/-- **`factorCount` is at most the size of every family of positions whose length-`n` blocks
include every length-`n` block.** With `le_factorCount`, it is the number of distinct
length-`n` factors. -/
theorem factorCount_le (f : Nat → Bool) (n N : Nat) (g : Nat → Nat)
    (hcov : ∀ i, ∃ k, k < N ∧ ∀ r, r < n → f (g k + r) = f (i + r)) : factorCount f n ≤ N :=
  countBelow_le_of_cover (fun k => blk f (g k) n) N (Occurs f n) (2 ^ n) (fun c _ hc => by
    obtain ⟨i, hi⟩ := hc
    obtain ⟨k, hk, hki⟩ := hcov i
    exact ⟨k, hk, ((blk_eq_iff f _ _ n).2 hki).trans hi⟩)

theorem occurs_succ_low (f : Nat → Bool) (n c : Nat) (hc : c < 2 ^ n) :
    Occurs f (n + 1) c ↔ ∃ i, blk f i n = c ∧ f (i + n) = false := by
  constructor
  · rintro ⟨i, hi⟩
    have hl := blk_lt f i n
    cases h : f (i + n)
    · exact ⟨i, by rw [← blk_succ_false h]; exact hi, h⟩
    · rw [blk_succ_true h] at hi; omega
  · rintro ⟨i, hi, h⟩
    exact ⟨i, by rw [blk_succ_false h]; exact hi⟩

theorem occurs_succ_high (f : Nat → Bool) (n c : Nat) :
    Occurs f (n + 1) (2 ^ n + c) ↔ ∃ i, blk f i n = c ∧ f (i + n) = true := by
  constructor
  · rintro ⟨i, hi⟩
    have hl := blk_lt f i n
    cases h : f (i + n)
    · rw [blk_succ_false h] at hi; omega
    · rw [blk_succ_true h] at hi; exact ⟨i, by omega, h⟩
  · rintro ⟨i, hi, h⟩
    exact ⟨i, by rw [blk_succ_true h]; omega⟩

theorem factorCount_zero (f : Nat → Bool) : factorCount f 0 = 1 :=
  (countBelow_succ_pos (P := Occurs f 0) (N := 0) ⟨0, rfl⟩).trans rfl

/-- **The binary special-factor count.** Each length-`n` factor has one or two right
extensions, and two exactly when it is right special. -/
theorem factorCount_succ (f : Nat → Bool) (n : Nat) :
    factorCount f (n + 1) = factorCount f n + rightSpecialCount f n := by
  have e1 := countBelow_add (Occurs f (n + 1)) (2 ^ n) (2 ^ n)
  have e2 := countBelow_congr (P := Occurs f (n + 1))
    (Q := fun c => ∃ i, blk f i n = c ∧ f (i + n) = false) (2 ^ n)
    (fun c hc => occurs_succ_low f n c hc)
  have e3 := countBelow_congr (P := fun c => Occurs f (n + 1) (2 ^ n + c))
    (Q := fun c => ∃ i, blk f i n = c ∧ f (i + n) = true) (2 ^ n)
    (fun c _ => occurs_succ_high f n c)
  have e4 := countBelow_or_and (fun c => ∃ i, blk f i n = c ∧ f (i + n) = false)
    (fun c => ∃ i, blk f i n = c ∧ f (i + n) = true) (2 ^ n)
  have e5 : countBelow (fun c => (∃ i, blk f i n = c ∧ f (i + n) = false) ∨
      (∃ i, blk f i n = c ∧ f (i + n) = true)) (2 ^ n) = countBelow (Occurs f n) (2 ^ n) := by
    apply countBelow_congr
    intro c _
    constructor
    · rintro (⟨i, hi, _⟩ | ⟨i, hi, _⟩) <;> exact ⟨i, hi⟩
    · rintro ⟨i, hi⟩
      cases h : f (i + n)
      · exact Or.inl ⟨i, hi, h⟩
      · exact Or.inr ⟨i, hi, h⟩
  have e6 : countBelow (fun c => (∃ i, blk f i n = c ∧ f (i + n) = false) ∧
      (∃ i, blk f i n = c ∧ f (i + n) = true)) (2 ^ n) =
      countBelow (RightSpecial f n) (2 ^ n) := rfl
  have e7 : 2 ^ (n + 1) = 2 ^ n + 2 ^ n := by rw [Nat.pow_succ]; omega
  show countBelow (Occurs f (n + 1)) (2 ^ (n + 1)) =
    countBelow (Occurs f n) (2 ^ n) + countBelow (RightSpecial f n) (2 ^ n)
  rw [e7]
  omega

theorem rightSpecial_lt {f : Nat → Bool} {n c : Nat} (h : RightSpecial f n c) : c < 2 ^ n := by
  obtain ⟨i, hi, _⟩ := h.1
  rw [← hi]
  exact blk_lt f i n

/-- **Morse and Hedlund, one step.** A word that is not eventually periodic has a
right-special factor of every length. Otherwise each length-`n` block determines the next cell,
two of the first `2 ^ n + 1` blocks agree, and the word is periodic from there on. -/
theorem rightSpecialCount_pos {f : Nat → Bool} (hnp : ¬ EventuallyPeriodic f) (n : Nat) :
    1 ≤ rightSpecialCount f n := by
  refine Nat.pos_of_ne_zero fun h0 => hnp ?_
  have hno : ∀ c, ¬ RightSpecial f n c := by
    intro c hc
    have := countBelow_lt_of (rightSpecial_lt hc) hc
    unfold rightSpecialCount at h0
    omega
  have hdet : ∀ i j, blk f i n = blk f j n → f (i + n) = f (j + n) := by
    intro i j hij
    cases hi : f (i + n) <;> cases hj : f (j + n)
    · rfl
    · exact absurd ⟨⟨i, rfl, hi⟩, ⟨j, hij.symm, hj⟩⟩ (hno _)
    · exact absurd ⟨⟨j, hij.symm, hj⟩, ⟨i, rfl, hi⟩⟩ (hno _)
    · rfl
  obtain ⟨i, j, hij, heq⟩ : ∃ i j, i < j ∧ blk f i n = blk f j n := by
    refine Classical.byContradiction fun hne => ?_
    have := pigeonhole (2 ^ n) (2 ^ n + 1) (fun i => blk f i n) (fun i _ => blk_lt f i n)
      (fun i j _ _ hij => by
        rcases Nat.lt_trichotomy i j with h | h | h
        · exact absurd ⟨i, j, h, hij⟩ hne
        · exact h
        · exact absurd ⟨j, i, h, hij.symm⟩ hne)
    omega
  have hprop : ∀ s, blk f (i + s) n = blk f (j + s) n := by
    intro s
    induction s with
    | zero => exact heq
    | succ s ih =>
      have hr := (blk_eq_iff f _ _ n).1 ih
      have hn := hdet _ _ ih
      refine (blk_eq_iff f _ _ n).2 fun r hr' => ?_
      by_cases hrn : r + 1 < n
      · have := hr (r + 1) hrn
        rw [show i + (s + 1) + r = i + s + (r + 1) by omega,
          show j + (s + 1) + r = j + s + (r + 1) by omega]
        exact this
      · rw [show i + (s + 1) + r = i + s + n by omega, show j + (s + 1) + r = j + s + n by omega]
        exact hn
  refine ⟨i + n, j - i, by omega, fun t ht => ?_⟩
  have := hdet _ _ (hprop (t - (i + n)))
  rw [show i + (t - (i + n)) + n = t by omega,
    show j + (t - (i + n)) + n = t + (j - i) by omega] at this
  exact this.symm

/-- **Two fibres.** Two distinct right-special factors of length `n` give two of them. -/
theorem rightSpecialCount_two {f : Nat → Bool} {n c d : Nat} (hne : c ≠ d)
    (hc : RightSpecial f n c) (hd : RightSpecial f n d) : 2 ≤ rightSpecialCount f n := by
  unfold rightSpecialCount
  rcases Nat.lt_or_gt_of_ne hne with h | h
  · exact two_le_countBelow h (rightSpecial_lt hd) hc hd
  · exact two_le_countBelow h (rightSpecial_lt hc) hd hc

theorem rightSpecial_of_two {f : Nat → Bool} {i j n : Nat} (h : blk f i n = blk f j n)
    (hne : f (i + n) ≠ f (j + n)) : RightSpecial f n (blk f i n) := by
  cases hi : f (i + n) <;> cases hj : f (j + n)
  · exact absurd (hi.trans hj.symm) hne
  · exact ⟨⟨i, rfl, hi⟩, ⟨j, h.symm, hj⟩⟩
  · exact ⟨⟨j, h.symm, hj⟩, ⟨i, rfl, hi⟩⟩
  · exact absurd (hi.trans hj.symm) hne

/-- A nondecreasing bounded sequence of naturals is eventually constant. -/
theorem eventually_const {g : Nat → Nat} (hmono : ∀ n, g n ≤ g (n + 1)) {K : Nat}
    (hK : ∀ n, g n ≤ K) : ∃ N, ∀ n, N ≤ n → g n = g N := by
  have mono : ∀ a b, a ≤ b → g a ≤ g b := by
    intro a b hab
    obtain ⟨d, rfl⟩ : ∃ d, b = a + d := ⟨b - a, by omega⟩
    induction d with
    | zero => exact Nat.le_refl _
    | succ d ih => exact Nat.le_trans (ih (by omega)) (hmono (a + d))
  have key : ∀ d n0, K - g n0 ≤ d → ∃ N, ∀ n, N ≤ n → g n = g N := by
    intro d
    induction d with
    | zero =>
      intro n0 h
      exact ⟨n0, fun n hn => by have := mono n0 n hn; have := hK n; omega⟩
    | succ d ih =>
      intro n0 h
      by_cases hc : ∀ n, n0 ≤ n → g n = g n0
      · exact ⟨n0, hc⟩
      · obtain ⟨n1, hn1, hne⟩ : ∃ n1, n0 ≤ n1 ∧ g n1 ≠ g n0 :=
          Classical.byContradiction fun hno => hc fun n hn =>
            Classical.byContradiction fun hne => hno ⟨n, hn, hne⟩
        have := mono n0 n1 hn1
        exact ih n1 (by have := hK n1; omega)
  exact key K 0 (by omega)

/-! ### Periodic runs and the two-run lemma -/

/-- `f` is `q`-periodic on the `L` cells from position `a`. -/
def PerRun (f : Nat → Bool) (q a L : Nat) : Prop := ∀ r, r + q < L → f (a + r + q) = f (a + r)

/-- A maximal `q`-run: periodic on `L ≥ q` cells from `a > 0`, and broken by one cell on each
side. -/
def MaxRun (f : Nat → Bool) (q a L : Nat) : Prop :=
  q ≤ L ∧ 0 < a ∧ PerRun f q a L ∧ f (a - 1) ≠ f (a - 1 + q) ∧ f (a + L) ≠ f (a + L - q)

theorem perRun_reduce {f : Nat → Bool} {q a L : Nat} (hq : 0 < q) (h : PerRun f q a L) :
    ∀ s, s < L → f (a + s) = f (a + s % q) := by
  have key : ∀ k r, r < q → r + q * k < L → f (a + (r + q * k)) = f (a + r) := by
    intro k
    induction k with
    | zero => intro r _ _; rfl
    | succ k ih =>
      intro r hr hL
      rw [Nat.mul_succ] at hL
      rw [show a + (r + q * (k + 1)) = a + (r + q * k) + q by rw [Nat.mul_succ]; omega,
        h (r + q * k) (by omega)]
      exact ih r hr (by omega)
  intro s hs
  have hd := Nat.mod_add_div s q
  have := key (s / q) (s % q) (Nat.mod_lt s hq) (by omega)
  rw [hd] at this
  exact this

/-- **The two-run lemma.** Two maximal `q`-runs with the same first `q` cells, of lengths `L` and
`M ≥ L + q + 1`, give two distinct right-special factors of length `L + 1`: the factor starting one
cell before the first run, and the factor ending one cell before the end of the second. -/
theorem two_run {f : Nat → Bool} {q a b L M : Nat} (hq : 0 < q) (hM : L + q + 1 ≤ M)
    (hA : MaxRun f q a L) (hB : MaxRun f q b M) (hfirst : ∀ r, r < q → f (a + r) = f (b + r)) :
    ∃ c d, c ≠ d ∧ RightSpecial f (L + 1) c ∧ RightSpecial f (L + 1) d := by
  obtain ⟨hL, ha, hpA, hAl, hAr⟩ := hA
  obtain ⟨_, hb, hpB, hBl, hBr⟩ := hB
  have hagree : ∀ s, s < L → f (a + s) = f (b + s) := by
    intro s hs
    rw [perRun_reduce hq hpA s hs, perRun_reduce hq hpB s (by omega)]
    exact hfirst _ (Nat.mod_lt s hq)
  have hU : ∀ r, r < L + 1 → f (a - 1 + r) = f (b - 1 + r) := by
    intro r hr
    cases r with
    | zero =>
      show f (a - 1) = f (b - 1)
      have e := hagree (q - 1) (by omega)
      rw [show a + (q - 1) = a - 1 + q by omega, show b + (q - 1) = b - 1 + q by omega] at e
      revert hAl hBl e
      generalize f (a - 1) = x
      generalize f (b - 1) = y
      generalize f (a - 1 + q) = z
      generalize f (b - 1 + q) = w
      cases x <;> cases y <;> cases z <;> cases w <;> decide
    | succ s =>
      rw [show a - 1 + (s + 1) = a + s by omega, show b - 1 + (s + 1) = b + s by omega]
      exact hagree s (by omega)
  have hUr : f (a - 1 + (L + 1)) ≠ f (b - 1 + (L + 1)) := by
    rw [show a - 1 + (L + 1) = a + L by omega, show b - 1 + (L + 1) = b + L by omega]
    have e1 : f (b + L) = f (b + (L - q)) := by
      have := hpB (L - q) (by omega)
      rw [show b + (L - q) + q = b + L by omega] at this
      exact this
    have e2 := hagree (L - q) (by omega)
    rw [e1, ← e2, show a + (L - q) = a + L - q by omega]
    exact hAr
  have hV : ∀ r, r < L + 1 → f (b + (M - L - 1) + r) = f (b + (M - L - 1 - q) + r) := by
    intro r hr
    have := hpB (M - L - 1 - q + r) (by omega)
    rw [show b + (M - L - 1 - q + r) + q = b + (M - L - 1) + r by omega,
      show b + (M - L - 1 - q + r) = b + (M - L - 1 - q) + r by omega] at this
    exact this
  have hVr : f (b + (M - L - 1) + (L + 1)) ≠ f (b + (M - L - 1 - q) + (L + 1)) := by
    rw [show b + (M - L - 1) + (L + 1) = b + M by omega,
      show b + (M - L - 1 - q) + (L + 1) = b + M - q by omega]
    exact hBr
  have hD : blk f (a - 1) (L + 1) ≠ blk f (b + (M - L - 1)) (L + 1) := by
    intro h
    have hh := (blk_eq_iff f _ _ _).1 h
    have h0 := hh 0 (by omega)
    have hqq := hh q (by omega)
    have hper := hpB (M - L - 1) (by omega)
    apply hAl
    calc f (a - 1) = f (b + (M - L - 1)) := h0
      _ = f (b + (M - L - 1) + q) := hper.symm
      _ = f (a - 1 + q) := hqq.symm
  refine ⟨blk f (a - 1) (L + 1), blk f (b + (M - L - 1)) (L + 1), hD, ?_, ?_⟩
  · exact rightSpecial_of_two ((blk_eq_iff f _ _ _).2 hU) hUr
  · exact rightSpecial_of_two ((blk_eq_iff f _ _ _).2 hV) hVr

/-- Without an eventual period, a `q`-periodic run is broken somewhere on the right. -/
theorem perRun_break {f : Nat → Bool} {q : Nat} (hnp : ¬ EventuallyPeriodic f) (hq : 0 < q)
    {i ℓ : Nat} (hℓ : q ≤ ℓ) (h : PerRun f q i ℓ) :
    ∃ L, ℓ ≤ L ∧ PerRun f q i L ∧ f (i + L) ≠ f (i + L - q) := by
  refine Classical.byContradiction fun hne => hnp ?_
  have hall : ∀ d, PerRun f q i (ℓ + d) := by
    intro d
    induction d with
    | zero => exact h
    | succ d ih =>
      intro r hr
      by_cases hr' : r + q < ℓ + d
      · exact ih r hr'
      · have hbr : f (i + (ℓ + d)) = f (i + (ℓ + d) - q) :=
          Classical.byContradiction fun hb => hne ⟨ℓ + d, by omega, ih, hb⟩
        rw [show i + r + q = i + (ℓ + d) by omega, show i + r = i + (ℓ + d) - q by omega]
        exact hbr
  refine ⟨i, q, hq, fun t ht => ?_⟩
  have := hall (t - i + 1) (t - i) (by omega)
  rw [show i + (t - i) + q = t + q by omega, show i + (t - i) = t by omega] at this
  exact this

/-- A `q`-periodic run extends to the left until a breaker or position `0`. -/
theorem perRun_left {f : Nat → Bool} {q : Nat} : ∀ i L, PerRun f q i L →
    ∃ a, a ≤ i ∧ PerRun f q a (i + L - a) ∧ (a = 0 ∨ (0 < a ∧ f (a - 1) ≠ f (a - 1 + q))) := by
  intro i
  induction i with
  | zero => intro L h; exact ⟨0, Nat.le_refl 0, by rw [show 0 + L - 0 = L by omega]; exact h,
      Or.inl rfl⟩
  | succ i ih =>
    intro L h
    by_cases hb : f i = f (i + q)
    · have h' : PerRun f q i (L + 1) := by
        intro r hr
        cases r with
        | zero => exact hb.symm
        | succ r =>
          have := h r (by omega)
          rw [show i + (r + 1) + q = i + 1 + r + q by omega, show i + (r + 1) = i + 1 + r by omega]
          exact this
      obtain ⟨a, ha, hp, hl⟩ := ih (L + 1) h'
      exact ⟨a, by omega, by rw [show i + 1 + L - a = i + (L + 1) - a by omega]; exact hp, hl⟩
    · exact ⟨i + 1, Nat.le_refl _, by rw [show i + 1 + L - (i + 1) = L by omega]; exact h,
        Or.inr ⟨by omega, by rw [show i + 1 - 1 = i by omega]; exact hb⟩⟩

/-- **Long periodic factors give long maximal runs with a positive start.** The maximal
`q`-periodic prefix has one finite length, so long enough runs start after position `0`. -/
theorem long_runs {f : Nat → Bool} {q : Nat} (hnp : ¬ EventuallyPeriodic f) (hq : 0 < q)
    (hunb : ∀ T, ∃ i ℓ, T ≤ ℓ ∧ PerRun f q i ℓ) : ∀ T, ∃ a L, T ≤ L ∧ MaxRun f q a L := by
  obtain ⟨L0, hL0, hp0, hb0⟩ :=
    perRun_break hnp hq (i := 0) (ℓ := q) (Nat.le_refl q) (fun r hr => by omega)
  intro T
  obtain ⟨i, ℓ, hℓ, hp⟩ := hunb (T + L0 + q + 1)
  obtain ⟨L, hL, hpL, hbL⟩ := perRun_break hnp hq (i := i) (ℓ := ℓ) (by omega) hp
  obtain ⟨a, hai, hpa, hla⟩ := perRun_left i L hpL
  rcases hla with h0 | ⟨hapos, hla⟩
  · exfalso
    subst h0
    rcases Nat.lt_trichotomy (i + L - 0) L0 with h | h | h
    · have := hp0 (i + L - 0 - q) (by omega)
      rw [show 0 + (i + L - 0 - q) + q = i + L by omega,
        show 0 + (i + L - 0 - q) = i + L - q by omega] at this
      exact hbL this
    · omega
    · have := hpa (L0 - q) (by omega)
      rw [show 0 + (L0 - q) + q = 0 + L0 by omega, show 0 + (L0 - q) = 0 + L0 - q by omega] at this
      exact hb0 this
  · refine ⟨a, i + L - a, by omega, by omega, hapos, hpa, hla, ?_⟩
    rw [show a + (i + L - a) = i + L by omega]
    exact hbL

/-- **Bounded periodic factors.** If from some length on there is at most one right-special
factor per length, then for each `q ≥ 1` the `q`-periodic factors have bounded length. Among
maximal `q`-runs of unbounded length one first `q`-block recurs (a finite maximum over the
`2 ^ q` blocks), and the two-run lemma then gives two right-special factors of one length. -/
theorem perRun_bounded {f : Nat → Bool} (hnp : ¬ EventuallyPeriodic f) {N0 : Nat}
    (hrs : ∀ n, N0 ≤ n → rightSpecialCount f n ≤ 1) {q : Nat} (hq : 0 < q) :
    ∃ R, ∀ i ℓ, PerRun f q i ℓ → ℓ ≤ R := by
  refine Classical.byContradiction fun hno => ?_
  have hunb : ∀ T, ∃ i ℓ, T ≤ ℓ ∧ PerRun f q i ℓ := by
    intro T
    refine Classical.byContradiction fun hT => hno ⟨T, fun i ℓ hp => ?_⟩
    exact Nat.le_of_not_lt fun hlt => hT ⟨i, ℓ, by omega, hp⟩
  have hruns := long_runs hnp hq hunb
  obtain ⟨c, hc⟩ : ∃ c, ∀ T, ∃ a L, T ≤ L ∧ MaxRun f q a L ∧ blk f a q = c := by
    refine Classical.byContradiction fun hnc => ?_
    have hbd : ∀ c, c ≤ 2 ^ q → ∃ T, ∀ a L, MaxRun f q a L → blk f a q = c → L < T := by
      intro c _
      refine Classical.byContradiction fun hT => hnc ⟨c, fun T => ?_⟩
      refine Classical.byContradiction fun hT' => hT ⟨T, fun a L h1 h2 => ?_⟩
      exact Nat.lt_of_not_le fun hle => hT' ⟨a, L, hle, h1, h2⟩
    obtain ⟨T, hT⟩ := common_time (fun c T => ∀ a L, MaxRun f q a L → blk f a q = c → L < T)
      (fun _ _ _ hle hP a L h1 h2 => Nat.lt_of_lt_of_le (hP a L h1 h2) hle) (2 ^ q) hbd
    obtain ⟨a, L, hTL, h1⟩ := hruns T
    have := hT (blk f a q) (Nat.le_of_lt (blk_lt f a q)) a L h1 rfl
    omega
  obtain ⟨a, L, hL1, hA, hca⟩ := hc (N0 + q)
  obtain ⟨b, M, hM1, hB, hcb⟩ := hc (L + q + 1)
  obtain ⟨c1, c2, hne, h1, h2⟩ := two_run hq hM1 hA hB
    (fun r hr => (blk_eq_iff f a b q).1 (hca.trans hcb.symm) r hr)
  have h2le := rightSpecialCount_two hne h1 h2
  have := hrs (L + 1) (by omega)
  omega

/-- **Bounded lag forces superlinear-plus-slack complexity.** Let `f` be not eventually periodic,
and let bounded-slack repeats of `f` have bounded lag. Then for every `K`, eventually
`n + K < factorCount f n`. If not, the excess `factorCount f n - n` is bounded and nondecreasing,
hence eventually constant; then there is eventually one right-special factor per length, so
`q`-periodic factors are bounded for each `q`; but among the first `n + K + 1` blocks of a long
length `n` two agree, with lag `q` at most the bound, and their union is a long `q`-periodic
factor. -/
theorem complexity_of_bounded_lag {f : Nat → Bool} (hnp : ¬ EventuallyPeriodic f)
    (hbl : ∀ K, ∃ B, ∀ i j n, i < j → j ≤ n + K →
      (∀ r, r < n → f (i + r) = f (j + r)) → j - i ≤ B) :
    ∀ K, ∃ N, ∀ n, N ≤ n → n + K < factorCount f n := by
  intro K
  refine Classical.byContradiction fun hno => ?_
  have hinf : ∀ N, ∃ n, N ≤ n ∧ factorCount f n ≤ n + K := by
    intro N
    refine Classical.byContradiction fun hN => hno ⟨N, fun n hn => ?_⟩
    exact Nat.lt_of_not_le fun hle => hN ⟨n, hn, hle⟩
  have hgrow : ∀ n d, factorCount f n + d ≤ factorCount f (n + d) := by
    intro n d
    induction d with
    | zero => exact Nat.le_refl _
    | succ d ih =>
      have e1 := factorCount_succ f (n + d)
      have e2 := rightSpecialCount_pos hnp (n + d)
      rw [show n + (d + 1) = n + d + 1 by omega]
      omega
  have hall : ∀ n, factorCount f n ≤ n + K := by
    intro n
    obtain ⟨n', hn', hle⟩ := hinf n
    have e := hgrow n (n' - n)
    rw [show n + (n' - n) = n' by omega] at e
    omega
  have hpos : ∀ n, n + 1 ≤ factorCount f n := by
    intro n
    have e := hgrow 0 n
    rw [factorCount_zero, Nat.zero_add] at e
    omega
  obtain ⟨N0, hN0⟩ := eventually_const (g := fun n => factorCount f n - n) (K := K)
    (fun n => by
      show factorCount f n - n ≤ factorCount f (n + 1) - (n + 1)
      have e1 := factorCount_succ f n
      have e2 := rightSpecialCount_pos hnp n
      omega)
    (fun n => by
      show factorCount f n - n ≤ K
      have e := hall n
      omega)
  have hrs : ∀ n, N0 ≤ n → rightSpecialCount f n ≤ 1 := by
    intro n hn
    have e1 : factorCount f n - n = factorCount f N0 - N0 := hN0 n hn
    have e2 : factorCount f (n + 1) - (n + 1) = factorCount f N0 - N0 := hN0 (n + 1) (by omega)
    have e3 := factorCount_succ f n
    have e4 := hpos n
    omega
  obtain ⟨B, hB⟩ := hbl K
  obtain ⟨R, hR⟩ := common_time (fun q R => 0 < q → ∀ i ℓ, PerRun f q i ℓ → ℓ ≤ R)
    (fun _ _ _ hle hP hq i ℓ hp => Nat.le_trans (hP hq i ℓ hp) hle) B
    (fun q _ => by
      by_cases hq : 0 < q
      · obtain ⟨R, hR⟩ := perRun_bounded hnp hrs hq
        exact ⟨R, fun _ => hR⟩
      · exact ⟨0, fun h => absurd h hq⟩)
  obtain ⟨i, j, hij, hjn, heq⟩ :
      ∃ i j, i < j ∧ j ≤ R + 1 + K ∧ blk f i (R + 1) = blk f j (R + 1) := by
    refine Classical.byContradiction fun hne => ?_
    have hcount := le_countBelow (P := Occurs f (R + 1)) (M := 2 ^ (R + 1)) (N := R + 1 + K + 1)
      (fun i => blk f i (R + 1)) (fun i _ => ⟨blk_lt f i _, i, rfl⟩)
      (fun i j hi hj hij => by
        rcases Nat.lt_trichotomy i j with h | h | h
        · exact absurd ⟨i, j, h, by omega, hij⟩ hne
        · exact h
        · exact absurd ⟨j, i, h, by omega, hij.symm⟩ hne)
    have e := hall (R + 1)
    unfold factorCount at e
    omega
  have hlag := hB i j (R + 1) hij (by omega) ((blk_eq_iff f i j _).1 heq)
  have hrun : PerRun f (j - i) i (R + 1 + (j - i)) := by
    intro r hr
    have e := (blk_eq_iff f i j _).1 heq r (by omega)
    rw [show i + r + (j - i) = j + r by omega]
    exact e.symm
  have e := hR (j - i) hlag (by omega) i _ hrun
  omega

/-- **The complexity of the free word of a finitely supported constrained row.** For every `K`,
eventually more than `n + K` distinct length-`n` blocks occur in the free word. -/
theorem freeWord_complexity {L : Nat → Bool} (hfin : FinSupp L) (hX : InX L) :
    ∀ K, ∃ N, ∀ n, N ≤ n → n + K < factorCount (freeWord L) n :=
  complexity_of_bounded_lag (free_not_eventuallyPeriodic hfin hX)
    (freeWord_bounded_lag_of_finSupp hfin hX)

/-- **The same for free bits with a finitely supported constrained start `Theta f`.** -/
theorem Theta_complexity (f : Nat → Bool) (hfin : FinSupp (Theta f)) :
    ∀ K, ∃ N, ∀ n, N ≤ n → n + K < factorCount f n := by
  have hf : (fun s => zrow (Theta f) (2 * s + 1) 1) = f := funext (Theta_free f)
  have hnp := free_not_eventuallyPeriodic hfin (Theta_inX f)
  rw [hf] at hnp
  exact complexity_of_bounded_lag hnp (Theta_bounded_lag f hfin)

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30LeftReset"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"E_entry", "E_tailLeft", "tail_periodic", "tail_profile_bound", "tail_white_unbounded", "tail_no_two_white", "tail_black_after_white", "tail_black_unbounded", "E_black_unbounded", "row_eq_Theta", "rows_agree", "freeWord_bounded_lag", "freeWord_bounded_lag_of_finSupp", "le_factorCount", "factorCount_le", "factorCount_succ", "rightSpecialCount_pos", "two_run", "complexity_of_bounded_lag", "freeWord_complexity"};
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.freeWord_complexity"]["KernelCheck"]
```
