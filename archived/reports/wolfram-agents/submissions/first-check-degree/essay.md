---
Template: ComputationalEssay
Name: The First Check of the Zero-Boundary Left Half: Its Weight Is n mod 2, Its Degree Is n or n - 1, and the Other Clock Phase Is Always Odd
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. For every n the first check of the zero-boundary left half has top ANF coefficient n mod 2 and degree n or n - 1, so its weight and the number of first-check survivors are congruent to n mod 2; in the other clock phase the weight is always odd. Nothing about the single seed.
Abstract: In Lean 4.35.0 we prove two ANF coefficient laws and the exact degree of the first check of the zero-boundary left half of rule 30. Keep column -1 black at every even step and let its values at the odd steps be n free bits. The first check past the free range is the cell at depth 2n + 1, the kit's Rule30FirstChecks.check. For n >= 1 its top coefficient is n mod 2, and for n >= 2 the coefficient of the monomial without the second free bit is n + 1 mod 2, so the check has degree n for odd n and n - 1 for even n. With the kit's first_check_count, the number of rows of width at most 2n that are black at column -1 at every even tick through 2n is congruent to n modulo 2. The Walsh sum is 2 mod 4 exactly at odd n >= 2, and 0 at n = 1. In the other clock phase, with the free bits at the even steps, the check has odd weight for every n. The proof is a derivative along the anti-diagonals of the reconstruction. Nothing here bears on the single seed.
Keywords: [rule 30, Rule 30 Prize, period two, zero-boundary left half, first check, algebraic normal form, degree, parity, Moebius transform, Walsh sum, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

## 1. The statement

In the zero-boundary left half, keep column `-1` black at every even step and let its values at the odd steps be free bits `f 0, f 1, …`. The kit reconstructs the whole row from that column (`Rule30ZeroBoundary.Theta`). The first cell past `n` free bits is the cell at depth `2n + 1`, the kit's first check `Rule30FirstChecks.check n`, a Boolean function of `f 0, …, f (n - 1)`.

This module proves two coefficient laws in its algebraic normal form over `GF(2)`, and its exact degree for every positive `n`. The coefficient of a monomial is the exclusive-or of the function over the points below its mask (`coeff`), and every function is the exclusive-or of the coefficients below its argument (`anf_expansion`).
- `top_coefficient`: for `n ≥ 1`, the coefficient of `f 0 ⋯ f (n - 1)` is `n mod 2`.
- `omit_coefficient`: for `n ≥ 2`, the coefficient of the monomial of every free bit except `f 1` is `n + 1 mod 2`.
- `check_degree`: so the check has degree `n` for odd `n` and `n - 1` for even `n`. At even `n` the top coefficient only bounds the degree; the second coefficient fixes it.
- `ones_parity`: for `n ≥ 1`, the number of words on which the check is black is congruent to `n` modulo `2`.
- `first_check_parity`: for `n ≥ 1`, the number of rows of width at most `2n` that are black at column `-1` at every even tick through `2n` is congruent to `n` modulo `2`. This uses the kit's count `first_check_count` and is a congruence, not a count.
- `walsh_mod_four`, `walsh_one`: the Walsh sum `2^n - 2 ones(n)` is `2` mod `4` exactly at odd `n ≥ 2`. At `n = 1` it is `0`, so the guard `n ≥ 2` is needed.
- `other_phase_odd`: in the other clock phase, with the free bits at the even steps and column `-1` black at the odd ones, the check at depth `2n` has top coefficient `1` for every `n ≥ 1`. Its weight is always odd, so the two phases differ at every even `n`.

## 2. The derivative along an anti-diagonal

The cell at depth `k` and time `t` reads column `-1` at times `t, …, t + k - 1`. Call `t + k - 1` its anti-diagonal. The kit's `recon_aff` says that the cell depends affinely on its newest entry, with coefficient `1`.

Flip one entry of column `-1`, at time `d - 1`, and keep the rest.
- Every cell on anti-diagonal `d - 1` flips.
- Cells on earlier anti-diagonals are unchanged.
- Each cell on anti-diagonal `d` is the cell one depth shallower and one step later, on the same anti-diagonal, exclusive-or `(y OR z)`, where `y` is on anti-diagonal `d - 1` and `z` on `d - 2`. Flipping `y` changes `y OR z` by `NOT z`.

So the top cell changes by the exclusive-or of the negated cells two anti-diagonals back (`diag`, with the sum `zs`).

## 3. The two recurrences

For the check, the newest entry, at time `2n`, is a fixed black cell, and the entry before it is the newest free bit `f (n - 1)`. Summing over `f (n - 1)` therefore leaves the derivative, and the remaining sum runs over `f 0, …, f (n - 2)`.

Every derivative cell at a time `≥ 2` does not read `f 0`, which sits at time `1`. Summing over `f 0` kills it, and so do the negations, which are constants summed over at least two points. Two cells survive:
- the previous check, at time `0`;
- the cell `bcell` at depth `2(n - 1)` and time `1`.

So the top sum changes by the top sum of `bcell` (`top_succ`). The same argument for `bcell` leaves only the previous `bcell` at time `1` (`bsum`), so that sum is `1` at every step. The top coefficient is `1` at `n = 1`, where the check is `f 0`, and it changes at every step after that.

For the coefficient without `f 1`, fix `f 1 = 0` before summing (`ins`). The same two cells survive, and the base cases move to `n = 2` and, for `bcell`, `n = 3` (`rsum_succ`, `tsum_succ`).

In the other phase, `g 0` sits at time `0`. So only the cell at time `0`, the previous check, survives (`other_flip`), and the top coefficient keeps its initial value `1`. This pinpoints the difference between the phases: two surviving time slices against one.

## 4. Scope

These are exact statements about one Boolean function for every `n`. They do not say how often a long run of checks passes, and nothing here bears on the single seed. The survivor statement is a congruence modulo `2`, not a count.

## 5. Worked numbers

The cell below computes, for the words of length `n`:
- whether `ones(n) ≡ n mod 2` for `n = 1, …, 12`, and whether the words with `f 1 = 0` give `n + 1 mod 2` for `n = 2, …, 12`;
- the algebraic degree of the check for `n = 1, …, 10`, by the Möbius transform of its truth table;
- the rows of width at most `2n` that pass every even check through `2n`, by direct simulation, for `n = 1, …, 6`;
- the Walsh sum modulo `4` for `n = 1, …, 12`;
- whether the other phase has odd weight for `n = 1, …, 12`.

```wl
recCell[col_, k_] := Module[{prev = ConstantArray[0, Length[col] + 1], cur = col, nxt}, Do[nxt = Table[BitXor[cur[[t + 2]], BitOr[cur[[t + 1]], prev[[t + 1]]]], {t, 0, Length[cur] - 2}]; prev = cur; cur = nxt, {k - 1}]; First[cur]];
bit[w_, s_] := If[s < Length[w], w[[s + 1]], 0];
check[n_, w_] := recCell[Table[If[EvenQ[t], 1, bit[w, Quotient[t, 2]]], {t, 0, 2 n}], 2 n + 1];
other[n_, w_] := recCell[Table[If[EvenQ[t], bit[w, Quotient[t, 2]], 1], {t, 0, 2 n - 1}], 2 n];
cube[n_] := Tuples[{0, 1}, n];
ones = Association[Table[n -> Total[check[n, #] & /@ cube[n]], {n, 1, 12}]];
kit = AllTrue[Range[12], Mod[ones[#], 2] == Mod[#, 2] &];
omit = AllTrue[Range[2, 12], Function[n, Mod[Total[If[#[[2]] == 0, check[n, #], 0] & /@ cube[n]], 2] == Mod[n + 1, 2]]];
degree[n_] := Module[{tt = ConstantArray[0, 2^n]}, Do[tt[[FromDigits[Reverse[w], 2] + 1]] = check[n, w], {w, cube[n]}]; Do[If[BitGet[x, i] == 1, tt[[x + 1]] = BitXor[tt[[x + 1]], tt[[x - 2^i + 1]]]], {i, 0, n - 1}, {x, 0, 2^n - 1}]; Max[DigitCount[#, 2, 1] & /@ (Flatten[Position[tt, 1]] - 1)]];
step[row_] := With[{r = Join[{0}, row, {0, 0}]}, Table[BitXor[r[[i + 2]], BitOr[r[[i + 1]], r[[i]]]], {i, 1, Length[row] + 1}]];
surv[n_] := Count[cube[2 n], row_ /; Module[{cur = row, ok = True}, Do[If[EvenQ[t] && cur[[1]] == 0, ok = False; Break[]]; cur = step[cur], {t, 0, 2 n}]; ok]];
odd = AllTrue[Range[12], Function[n, OddQ[Total[other[n, #] & /@ cube[n]]]]];
{kit, omit, degree /@ Range[10], surv /@ Range[6], Table[Mod[2^n - 2 ones[n], 4], {n, 1, 12}], odd}
```

## 6. Prior art and scope

- **The kit's inputs.** The reconstruction, `recon_aff` and `Theta` are the kit's (`Rule30ZeroBoundary`). The check, its weight `ones` and the count `first_check_count` are the kit's `Rule30FirstChecks`, which is reused, not reproved.
- **The method.** Differentiating along the newest variable, which left permutivity makes enter linearly, is the method of the kit's [`AlgebraicDegree`](https://github.com/WolframInstitute/Rule30PrizeKit/blob/03a19bf6240b63c6d15894c5f7552f3a6091d937/equivalents/Rule30Equivalents/AlgebraicDegree.lean), which finds the degree of the unconstrained `t`-step map. Summing out a variable after a triangular substitution is the method of the kit's `Rule30WedgeParity` and `Rule30TopCoefficient`. Those modules treat different functions, on free initial cells or free diagonals, and this module does not rely on them.
- **The other phase.**
  - N. Berzai's paper ([rule30-left-edge](https://github.com/nateberzai-svg/rule30-left-edge/tree/d9cb3d57b28f5a713a4ac28c11f5723cbe14d6a4), 8 October 2026), in the subsection on the left machine for the tail `01`, works in the other phase. It states that the weights of its checks are odd, labelled proved, without a parity proof in that subsection.
  - The code it cites ([rule30-prize](https://github.com/cochon123/rule30-prize/tree/0ff6930488bfa5e9c244b2caa05835907217077f)) computes the same reconstruction in that phase.
  - [`forced-bits-dense`](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/negative-results/period-two/forced-bits-dense.md) in `rule30-open` computes the forced bits of that phase as polynomials of full degree for twelve widths, in row coordinates. Full degree is odd weight, which the triangular change between row bits and free bits keeps, so that table agrees with `other_phase_odd` up to `n = 12`.
  - Berzai's centre alternates rather than staying white. At the odd times, when it is black, the cell next to it is forced black, so its OR with the centre is unchanged if the centre is replaced by white. That comparison argument is ours and is not formalized here.
- **What is new.** The all-`n` law in the kit phase (top coefficient `n mod 2`, degree `n` or `n - 1`), its corollary for the survivors, the Walsh exception at `n = 1`, and an all-`n` formal proof of the odd weight in the other phase.
- **History.** It came from a sub-agent run of our programme. GPT carried the hand proof with its repairs: the guard `n ≥ 2` on the Walsh sum, and the second coefficient needed for the degree at even `n`. GPT also made the phase comparison. Local formalized it, adding the other phase.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30ZeroBoundary`. The verifier's kit predates the kit module `Rule30FirstChecks`, so the source carries a byte copy of that module's body in the namespace `Rule30Submission.Rule30FirstChecks`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30ZeroBoundary
/-!
# The degree of the first check

`Rule30FirstChecks.check n l = Theta (word l) (2 n + 1)` is the first check past the free range: the
cell at depth `2 n + 1` of the constrained row whose free bits are the `n` bits of `l`. As a Boolean
function of `f 0, …, f (n - 1)` over `𝔽₂`, we prove two algebraic normal form coefficient laws
and its exact degree here for every positive `n`.

The coefficient of the monomial of a mask `S` is the exclusive-or of the function over the points
below `S` (`coeff`), and every function is the exclusive-or of the coefficients below its argument
(`anf_expansion`).

* `top_coefficient`: for `n ≥ 1` the coefficient of `f 0 ⋯ f (n - 1)` is `n mod 2`.
* `omit_coefficient`: for `n ≥ 2` the coefficient of the monomial without `f 1` is `n + 1 mod 2`.
* `check_degree`: so the degree of the check is `n` for odd `n` and `n - 1` for even `n`. At even `n`
  the top coefficient alone would only bound the degree; the second coefficient is what fixes it.
* `ones_parity`: for `n ≥ 1` the number of words on which the check is black is congruent to `n`
  modulo `2`.
* `first_check_parity`: with `Rule30FirstChecks.first_check_count`, for `n ≥ 1` the number of rows of
  width at most `2 n` that are black at column `-1` at every even tick through `2 n` is congruent to
  `n` modulo `2`. This is a congruence, not a count.
* `walsh_mod_four`, `walsh_one`: the Walsh sum `2 ^ n - 2 * ones n` is `2 mod 4` exactly at odd
  `n ≥ 2`; at `n = 1` it is `0`.
* `other_phase_odd`: in the other clock phase, with the free bits at the even steps and column `-1`
  black at the odd ones, the check at depth `2 n` (`otherCheck`) has top coefficient `1` for every
  `n ≥ 1`. So its weight is always odd, and the two phases differ at every even `n`.

The proof is a derivative along the anti-diagonals of the reconstruction. Flipping the newest free
bit flips every cell on the anti-diagonal before the top one (`Rule30ZeroBoundary.recon_aff`), so
the change of the top cell is the exclusive-or of the negated cells two anti-diagonals back (`diag`).
Summing out the first free bit `f 0` kills every one of those cells at a time `≥ 2`, and only two
survive: the previous check and the cell `bcell` at depth `2 m` and time `1` (`top_succ`). The same
derivative for `bcell` leaves only the previous `bcell` (`bsum`), so the top coefficient changes at
every step. Fixing `f 1 = 0` before summing gives the second recurrence (`rsum_succ`, `tsum_succ`).
In the other phase the first free bit sits at time `0`, so only the cell at time `0`, the previous
check, survives (`other_flip`), and the top coefficient never changes.

Nothing here bears on the single seed, and Problems 1 to 3 stay open.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

/-! ### A copy of the kit module `Rule30FirstChecks`, which the verifier kit does not have -/

namespace Rule30FirstChecks

open Rule30ZeroBoundary

/-! ### Sums over the cube -/

/-- The free word of a bit list, white past its end. -/
def word (l : List Bool) (s : Nat) : Bool := l.getD s false

/-- The sum of `F` over all bit lists of length `n`. -/
def cubeSum : Nat → (List Bool → Nat) → Nat
  | 0, F => F []
  | n + 1, F => cubeSum n (fun l => F (false :: l)) + cubeSum n (fun l => F (true :: l))

theorem cubeSum_congr {n : Nat} {F G : List Bool → Nat} (h : ∀ l, l.length = n → F l = G l) :
    cubeSum n F = cubeSum n G := by
  induction n generalizing F G with
  | zero => exact h [] rfl
  | succ n ih =>
    show cubeSum n _ + cubeSum n _ = cubeSum n _ + cubeSum n _
    rw [ih (fun l hl => h (false :: l) (by simp [hl])), ih (fun l hl => h (true :: l) (by simp [hl]))]

theorem cubeSum_le {n : Nat} {F G : List Bool → Nat} (h : ∀ l, F l ≤ G l) :
    cubeSum n F ≤ cubeSum n G := by
  induction n generalizing F G with
  | zero => exact h []
  | succ n ih =>
    show cubeSum n _ + cubeSum n _ ≤ cubeSum n _ + cubeSum n _
    exact Nat.add_le_add (ih fun l => h _) (ih fun l => h _)

theorem cubeSum_add (n : Nat) (F G : List Bool → Nat) :
    cubeSum n (fun l => F l + G l) = cubeSum n F + cubeSum n G := by
  induction n generalizing F G with
  | zero => rfl
  | succ n ih =>
    show cubeSum n _ + cubeSum n _ = (cubeSum n _ + cubeSum n _) + (cubeSum n _ + cubeSum n _)
    rw [ih, ih]
    omega

theorem cubeSum_const (n c : Nat) : cubeSum n (fun _ => c) = 2 ^ n * c := by
  induction n with
  | zero => show c = 2 ^ 0 * c; omega
  | succ n ih =>
    show cubeSum n _ + cubeSum n _ = _
    rw [ih, Nat.pow_succ]
    generalize 2 ^ n = N
    rw [Nat.mul_comm N 2, Nat.mul_assoc]
    omega

theorem cubeSum_snoc (n : Nat) (F : List Bool → Nat) :
    cubeSum (n + 1) F = cubeSum n (fun l => F (l ++ [false]) + F (l ++ [true])) := by
  induction n generalizing F with
  | zero => rfl
  | succ n ih =>
    show cubeSum (n + 1) _ + cubeSum (n + 1) _ = cubeSum (n + 1) _
    rw [ih, ih]
    rfl

/-! ### The checks -/

/-- The first check past the free range of a word of length `n`. -/
def check (n : Nat) (l : List Bool) : Bool := Theta (word l) (2 * n + 1)

/-- The number of words of length `n` on which the check is black. -/
def ones (n : Nat) : Nat := cubeSum n (fun l => (check n l).toNat)

/-- The number of words of length `n + 1` on which the check differs from the check of the shift. -/
def flips (n : Nat) : Nat :=
  cubeSum (n + 1) (fun l => (xor (check (n + 1) l) (check n l.tail)).toNat)

/-- The smaller of the two sides of the check. -/
def gap (n : Nat) : Nat := min (ones n) (2 ^ n - ones n)

theorem ones_le (n : Nat) : ones n ≤ 2 ^ n := by
  have h : cubeSum n (fun l => (check n l).toNat) ≤ cubeSum n (fun _ => 1) :=
    cubeSum_le fun l => by cases check n l <;> decide
  rw [cubeSum_const] at h
  simpa [ones] using h

theorem shifted_sum (n : Nat) :
    cubeSum (n + 1) (fun l => (check n l.tail).toNat) = 2 * ones n := by
  show cubeSum n _ + cubeSum n _ = _
  simp only [List.tail_cons]
  unfold ones
  omega

/-- Two sets inside the cube, and their symmetric difference. -/
theorem overlap (n : Nat) :
    ones (n + 1) ≤ 2 * ones n + flips n ∧ 2 * ones n ≤ ones (n + 1) + flips n ∧
      flips n ≤ ones (n + 1) + 2 * ones n ∧
      flips n + (ones (n + 1) + 2 * ones n) ≤ 2 ^ (n + 1) * 2 := by
  have hs := shifted_sum n
  let X : List Bool → Nat := fun l => (check (n + 1) l).toNat
  let Y : List Bool → Nat := fun l => (check n l.tail).toNat
  let D : List Bool → Nat := fun l => (xor (check (n + 1) l) (check n l.tail)).toNat
  have hX : cubeSum (n + 1) X = ones (n + 1) := rfl
  have hY : cubeSum (n + 1) Y = 2 * ones n := hs
  have hD : cubeSum (n + 1) D = flips n := rfl
  have h1 : cubeSum (n + 1) X ≤ cubeSum (n + 1) (fun l => Y l + D l) :=
    cubeSum_le fun l => by
      show (check (n + 1) l).toNat ≤ (check n l.tail).toNat + (xor (check (n + 1) l) (check n l.tail)).toNat
      cases check (n + 1) l <;> cases check n l.tail <;> decide
  have h2 : cubeSum (n + 1) Y ≤ cubeSum (n + 1) (fun l => X l + D l) :=
    cubeSum_le fun l => by
      show (check n l.tail).toNat ≤ (check (n + 1) l).toNat + (xor (check (n + 1) l) (check n l.tail)).toNat
      cases check (n + 1) l <;> cases check n l.tail <;> decide
  have h3 : cubeSum (n + 1) D ≤ cubeSum (n + 1) (fun l => X l + Y l) :=
    cubeSum_le fun l => by
      show (xor (check (n + 1) l) (check n l.tail)).toNat ≤ (check (n + 1) l).toNat + (check n l.tail).toNat
      cases check (n + 1) l <;> cases check n l.tail <;> decide
  have h4 : cubeSum (n + 1) (fun l => D l + (X l + Y l)) ≤ cubeSum (n + 1) (fun _ => 2) :=
    cubeSum_le fun l => by
      show (xor (check (n + 1) l) (check n l.tail)).toNat + ((check (n + 1) l).toNat + (check n l.tail).toNat) ≤ 2
      cases check (n + 1) l <;> cases check n l.tail <;> decide
  rw [cubeSum_add] at h1 h2 h3
  rw [cubeSum_add, cubeSum_add, cubeSum_const] at h4
  omega

/-! ### Two ticks -/

/-- **Two ticks of a row with a white wall.** -/
theorem two_tick (L : Nat → Bool) (j : Nat) :
    zrow L 2 (j + 2) = xor (zrow L 0 (j + 4))
      ((zrow L 0 (j + 1) || zrow L 0 j) && !(xor (zrow L 0 (j + 3)) (zrow L 0 (j + 2)))) := by
  have h : zrow L 2 (j + 2) = xor (zrow L 1 (j + 3)) (zrow L 1 (j + 2) || zrow L 1 (j + 1)) :=
    zrow_succ L 1 (j + 1)
  have h1 : zrow L 1 (j + 1) = xor (zrow L 0 (j + 2)) (zrow L 0 (j + 1) || zrow L 0 j) :=
    zrow_succ L 0 j
  have h2 : zrow L 1 (j + 2) = xor (zrow L 0 (j + 3)) (zrow L 0 (j + 2) || zrow L 0 (j + 1)) :=
    zrow_succ L 0 (j + 1)
  have h3 : zrow L 1 (j + 3) = xor (zrow L 0 (j + 4)) (zrow L 0 (j + 3) || zrow L 0 (j + 2)) :=
    zrow_succ L 0 (j + 2)
  rw [h, h1, h2, h3]
  generalize zrow L 0 j = a
  generalize zrow L 0 (j + 1) = b
  generalize zrow L 0 (j + 2) = c
  generalize zrow L 0 (j + 3) = d
  generalize zrow L 0 (j + 4) = e
  revert a b c d e
  decide

/-- The check of a shifted word, against the check of the word. -/
theorem check_xor (m : Nat) (f : Nat → Bool) :
    Theta (fun s => f (s + 1)) (2 * m + 3) = xor (Theta f (2 * m + 5))
      ((Theta f (2 * m + 2) || Theta f (2 * m + 1)) &&
        !(xor (Theta f (2 * m + 4)) (Theta f (2 * m + 3)))) := by
  have h := two_tick (Theta f) (2 * m + 1)
  rw [two_step_shift f, zrow_zero_self (Theta_wall f)] at h
  exact h

/-! ### The pair law -/

theorem word_tail (l : List Bool) : word l.tail = fun s => word l (s + 1) := by
  funext s
  cases l with
  | nil => rfl
  | cons b l => rfl

theorem word_lt (p q : List Bool) {s : Nat} (hs : s < p.length) : word (p ++ q) s = word p s := by
  unfold word
  rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD, List.getElem?_append_left hs]

theorem word_ge (p q : List Bool) (s : Nat) : word (p ++ q) (p.length + s) = word q s := by
  unfold word
  rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD,
    List.getElem?_append_right (by omega), show p.length + s - p.length = s by omega]

theorem four_bools (c u v0 v1 w0 w1 : Bool) :
    ((u || c) && !(xor w0 v0)).toNat + ((u || c) && !(xor (!w0) v0)).toNat +
      ((((!u) || c) && !(xor w1 v1)).toNat + (((!u) || c) && !(xor (!w1) v1)).toNat) =
      1 + c.toNat := by
  revert c u v0 v1 w0 w1
  decide

theorem not_of_xor {a b : Bool} (h : xor a b = true) : b = !a := by
  revert h
  cases a <;> cases b <;> decide

/-- The four completions of a prefix by two bits. -/
theorem four_sum (p : List Bool) :
    (xor (check (p.length + 2) (p ++ [false] ++ [false])) (check (p.length + 1) (p ++ [false] ++ [false]).tail)).toNat +
      (xor (check (p.length + 2) (p ++ [false] ++ [true])) (check (p.length + 1) (p ++ [false] ++ [true]).tail)).toNat +
      ((xor (check (p.length + 2) (p ++ [true] ++ [false])) (check (p.length + 1) (p ++ [true] ++ [false]).tail)).toNat +
       (xor (check (p.length + 2) (p ++ [true] ++ [true])) (check (p.length + 1) (p ++ [true] ++ [true]).tail)).toNat) =
      1 + (check p.length p).toNat := by
  have key : ∀ x y : Bool,
      xor (check (p.length + 2) (p ++ [x] ++ [y])) (check (p.length + 1) (p ++ [x] ++ [y]).tail) =
        ((Theta (word (p ++ [x] ++ [y])) (2 * p.length + 2) ||
            Theta (word (p ++ [x] ++ [y])) (2 * p.length + 1)) &&
          !(xor (Theta (word (p ++ [x] ++ [y])) (2 * p.length + 4))
            (Theta (word (p ++ [x] ++ [y])) (2 * p.length + 3)))) := by
    intro x y
    have h := check_xor p.length (word (p ++ [x] ++ [y]))
    show xor (Theta (word (p ++ [x] ++ [y])) (2 * p.length + 5))
      (Theta (word (p ++ [x] ++ [y]).tail) (2 * p.length + 3)) = _
    rw [word_tail, h]
    cases Theta (word (p ++ [x] ++ [y])) (2 * p.length + 5) <;> simp
  have agree : ∀ x y : Bool, ∀ s, s < p.length → word (p ++ [x] ++ [y]) s = word p s := by
    intro x y s hs
    rw [List.append_assoc]
    exact word_lt p _ hs
  have agree1 : ∀ x y y' : Bool, ∀ s, s ≤ p.length →
      word (p ++ [x] ++ [y]) s = word (p ++ [x] ++ [y']) s := by
    intro x y y' s hs
    have hl : (p ++ [x]).length = p.length + 1 := by simp
    rw [word_lt (p ++ [x]) [y] (by omega), word_lt (p ++ [x]) [y'] (by omega)]
  have atx : ∀ x y : Bool, word (p ++ [x] ++ [y]) p.length = x := by
    intro x y
    rw [List.append_assoc]
    exact word_ge p ([x] ++ [y]) 0
  have aty : ∀ x y : Bool, word (p ++ [x] ++ [y]) (p.length + 1) = y := by
    intro x y
    have h := word_ge (p ++ [x]) [y] 0
    have hl : (p ++ [x]).length = p.length + 1 := by simp
    rw [hl] at h
    exact h
  have b2 : ∀ x y : Bool, Theta (word (p ++ [x] ++ [y])) (2 * p.length + 1) = check p.length p := by
    intro x y
    exact tri_odd _ _ p.length (agree x y)
  have u0 : ∀ x y : Bool, Theta (word (p ++ [x] ++ [y])) (2 * p.length + 2) =
      Theta (word (p ++ [x] ++ [false])) (2 * p.length + 2) := by
    intro x y
    exact Theta_dep _ _ _ (fun s hs => agree1 x y false s (by omega))
  have v0 : ∀ x y : Bool, Theta (word (p ++ [x] ++ [y])) (2 * p.length + 3) =
      Theta (word (p ++ [x] ++ [false])) (2 * p.length + 3) := by
    intro x y
    exact Theta_dep _ _ _ (fun s hs => agree1 x y false s (by omega))
  have flipU : Theta (word (p ++ [true] ++ [false])) (2 * p.length + 2) =
      !Theta (word (p ++ [false] ++ [false])) (2 * p.length + 2) := by
    apply not_of_xor
    rw [tri_even _ _ p.length (fun s hs => by rw [agree _ _ s hs, agree _ _ s hs]), atx, atx]
    rfl
  have flipW : ∀ x : Bool, Theta (word (p ++ [x] ++ [true])) (2 * p.length + 4) =
      !Theta (word (p ++ [x] ++ [false])) (2 * p.length + 4) := by
    intro x
    apply not_of_xor
    rw [show 2 * p.length + 4 = 2 * (p.length + 1) + 2 by omega,
      tri_even _ _ (p.length + 1) (fun s hs => agree1 x false true s (by omega)), aty, aty]
    rfl
  rw [key, key, key, key, b2, b2, b2, b2, u0 false true, u0 true false, u0 true true, flipU,
    v0 false true, v0 true true, flipW false, flipW true]
  exact four_bools _ _ _ _ _ _

/-- **The pair law.** The check differs from the check of the shift on exactly `2 ^ m + ones m`
of the words of length `m + 2`. -/
theorem pair_count (m : Nat) : flips (m + 1) = 2 ^ m + ones m := by
  unfold flips
  rw [cubeSum_snoc, cubeSum_snoc]
  have h : cubeSum m (fun l =>
      (xor (check (m + 1 + 1) (l ++ [false] ++ [false])) (check (m + 1) (l ++ [false] ++ [false]).tail)).toNat +
      (xor (check (m + 1 + 1) (l ++ [false] ++ [true])) (check (m + 1) (l ++ [false] ++ [true]).tail)).toNat +
      ((xor (check (m + 1 + 1) (l ++ [true] ++ [false])) (check (m + 1) (l ++ [true] ++ [false]).tail)).toNat +
       (xor (check (m + 1 + 1) (l ++ [true] ++ [true])) (check (m + 1) (l ++ [true] ++ [true]).tail)).toNat)) =
      cubeSum m (fun l => 1 + (check m l).toNat) := by
    apply cubeSum_congr
    intro l hl
    subst hl
    exact four_sum l
  refine h.trans ?_
  rw [cubeSum_add, cubeSum_const, Nat.mul_one]
  rfl

/-! ### The inequalities -/

theorem pow_one_more (m : Nat) : 2 ^ (m + 1) = 2 * 2 ^ m := Nat.pow_succ'

theorem pow_two_more (m : Nat) : 2 ^ (m + 2) = 4 * 2 ^ m := by
  rw [pow_one_more (m + 1), pow_one_more m]; omega

theorem pow_three_more (m : Nat) : 2 ^ (m + 3) = 8 * 2 ^ m := by
  rw [pow_one_more (m + 2), pow_two_more m]; omega

theorem pow_four_more (m : Nat) : 2 ^ (m + 4) = 16 * 2 ^ m := by
  rw [pow_one_more (m + 3), pow_three_more m]; omega

/-- `overlap` with the pair law substituted, at indices `k + 1` and `k + 2`. -/
theorem overlap_pair (k : Nat) :
    ones (k + 2) ≤ 2 * ones (k + 1) + (2 ^ k + ones k) ∧
      2 * ones (k + 1) ≤ ones (k + 2) + (2 ^ k + ones k) ∧
      2 ^ k + ones k ≤ ones (k + 2) + 2 * ones (k + 1) ∧
      2 ^ k + ones k + (ones (k + 2) + 2 * ones (k + 1)) ≤ 8 * 2 ^ k := by
  have h := overlap (k + 1)
  rw [pair_count k, show 2 ^ (k + 1 + 1) * 2 = 8 * 2 ^ k by rw [pow_two_more k]; omega] at h
  exact h

theorem adjacent (m : Nat) : 2 ^ m + ones m ≤ gap (m + 2) + 2 * gap (m + 1) := by
  obtain ⟨a1, a2, a3, a4⟩ := overlap_pair m
  have b0 := ones_le m
  have b1 := ones_le (m + 1)
  have b2 := ones_le (m + 2)
  unfold gap
  rw [pow_one_more m] at b1 ⊢
  rw [pow_two_more m] at b2 ⊢
  generalize 2 ^ m = N at *
  omega

/-- **The distance-two inequality.** -/
theorem distance_two (m : Nat) : 2 ^ (m + 2) ≤ 4 * gap (m + 4) + 24 * gap (m + 2) := by
  obtain ⟨a1, a2, a3, a4⟩ : ones (m + 4) ≤ 2 * ones (m + 3) + (2 ^ (m + 2) + ones (m + 2)) ∧
      2 * ones (m + 3) ≤ ones (m + 4) + (2 ^ (m + 2) + ones (m + 2)) ∧
      2 ^ (m + 2) + ones (m + 2) ≤ ones (m + 4) + 2 * ones (m + 3) ∧
      2 ^ (m + 2) + ones (m + 2) + (ones (m + 4) + 2 * ones (m + 3)) ≤ 8 * 2 ^ (m + 2) :=
    overlap_pair (m + 2)
  obtain ⟨c1, c2, c3, c4⟩ : ones (m + 3) ≤ 2 * ones (m + 2) + (2 ^ (m + 1) + ones (m + 1)) ∧
      2 * ones (m + 2) ≤ ones (m + 3) + (2 ^ (m + 1) + ones (m + 1)) ∧
      2 ^ (m + 1) + ones (m + 1) ≤ ones (m + 3) + 2 * ones (m + 2) ∧
      2 ^ (m + 1) + ones (m + 1) + (ones (m + 3) + 2 * ones (m + 2)) ≤ 8 * 2 ^ (m + 1) :=
    overlap_pair (m + 1)
  obtain ⟨d1, d2, d3, d4⟩ := overlap_pair m
  have b0 := ones_le m
  have b1 := ones_le (m + 1)
  have b2 := ones_le (m + 2)
  have b3 := ones_le (m + 3)
  have b4 := ones_le (m + 4)
  unfold gap
  rw [pow_one_more m] at b1 c1 c2 c3 c4
  rw [pow_two_more m] at b2 a1 a2 a3 a4 ⊢
  rw [pow_three_more m] at b3
  rw [pow_four_more m] at b4 ⊢
  generalize 2 ^ m = N at *
  omega

/-- A check is *near constant* when its smaller side is under one fortieth. -/
def Bad (n : Nat) : Prop := 40 * gap n < 2 ^ n

/-- Two adjacent checks are not both near constant. -/
theorem not_both_bad_adjacent (m : Nat) : ¬ (Bad (m + 2) ∧ Bad (m + 3)) := by
  rintro ⟨h1, h2⟩
  have h : 2 ^ (m + 1) + ones (m + 1) ≤ gap (m + 3) + 2 * gap (m + 2) := adjacent (m + 1)
  unfold Bad at h1 h2
  rw [pow_one_more m] at h
  rw [pow_two_more m] at h1
  rw [pow_three_more m] at h2
  generalize 2 ^ m = N at *
  omega

/-- Two checks at distance two are not both near constant. -/
theorem not_both_bad_two (m : Nat) : ¬ (Bad (m + 2) ∧ Bad (m + 4)) := by
  rintro ⟨h1, h2⟩
  have h := distance_two m
  unfold Bad at h1 h2
  rw [pow_two_more m] at h h1
  rw [pow_four_more m] at h2
  generalize 2 ^ m = N at *
  omega

/-- **At most one of any three consecutive checks from `2` on is near constant.** -/
theorem two_of_three (m : Nat) :
    ¬ (Bad (m + 2) ∧ Bad (m + 3)) ∧ ¬ (Bad (m + 3) ∧ Bad (m + 4)) ∧ ¬ (Bad (m + 2) ∧ Bad (m + 4)) :=
  ⟨not_both_bad_adjacent m, not_both_bad_adjacent (m + 1), not_both_bad_two m⟩

/-! ### The survivor count -/

/-- The rows given by bit lists of length `n` beyond `l` whose last extension by a white cell passes
every even check. -/
def lastWhite : Nat → List Bool → Nat
  | 0, l => if ok (l ++ [false]) then 1 else 0
  | n + 1, l => lastWhite n (l ++ [false]) + lastWhite n (l ++ [true])

/-- The rows of width at most `2 n` black at column `-1` at every even tick through `2 n`. -/
def firstCheck (n : Nat) : Nat := lastWhite (2 * n) []

/-- The first `k` cells of a row, as a list. -/
def rowList (f : Nat → Bool) : Nat → List Bool
  | 0 => []
  | k + 1 => rowList f k ++ [Theta f (k + 1)]

theorem rowList_length (f : Nat → Bool) (k : Nat) : (rowList f k).length = k := by
  induction k with
  | zero => rfl
  | succ k ih => simp [rowList, ih]

theorem toRow_rowList (f : Nat → Bool) (k i : Nat) (hi : 1 ≤ i) (hk : i ≤ k) :
    toRow (rowList f k) i = Theta f i := by
  induction k with
  | zero => omega
  | succ k ih =>
    show toRow (rowList f k ++ [Theta f (k + 1)]) i = _
    by_cases h : i ≤ k
    · rw [toRow_snoc_le _ _ i (by rw [rowList_length]; exact h)]
      exact ih h
    · have e : i = (rowList f k).length + 1 := by rw [rowList_length]; omega
      rw [e, toRow_snoc_last, rowList_length]

theorem ok_rowList (f : Nat → Bool) (k : Nat) : ok (rowList f k) := by
  intro t ht he
  rw [rowList_length] at ht
  rw [zrow_light_cone (L' := Theta f) t 1 (fun i h1 h2 => toRow_rowList f k i h1 (by omega))]
  have := Theta_inX f (t / 2)
  rwa [show 2 * (t / 2) = t by omega] at this

theorem rowList_congr (f g : Nat → Bool) (k : Nat) (h : ∀ i, 1 ≤ i → i ≤ k → Theta f i = Theta g i) :
    rowList f k = rowList g k := by
  induction k with
  | zero => rfl
  | succ k ih =>
    show rowList f k ++ _ = rowList g k ++ _
    rw [ih (fun i h1 h2 => h i h1 (by omega)), h (k + 1) (by omega) (by omega)]

theorem lastWhite_of_not_ok {l : List Bool} (h : ¬ ok l) : ∀ n, lastWhite n l = 0 := by
  intro n
  induction n generalizing l with
  | zero =>
    show (if ok (l ++ [false]) then 1 else 0) = 0
    rw [ite_eq_right (fun hk => h (ok_of_snoc l false hk))]
  | succ n ih =>
    show lastWhite n _ + lastWhite n _ = 0
    rw [ih (fun hk => h (ok_of_snoc l false hk)), ih (fun hk => h (ok_of_snoc l true hk))]

/-- At an even length, exactly one of the two next cells keeps the row alive, and it is the row's own. -/
theorem wrong_cell_dead (f : Nat → Bool) (j : Nat) :
    ¬ ok (rowList f (2 * j) ++ [!Theta f (2 * j + 1)]) := by
  intro h
  have hl : (rowList f (2 * j)).length = 2 * j := rowList_length f (2 * j)
  have hb := ((ok_snoc _ _).mp h).2 (by rw [hl]; omega)
  have hg := ((ok_snoc (rowList f (2 * j)) (Theta f (2 * j + 1))).mp (ok_rowList f (2 * j + 1))).2
    (by rw [hl]; omega)
  have hp := snoc_pivot (rowList f (2 * j))
  cases hc : Theta f (2 * j + 1) with
  | false =>
    rw [hc] at hb hg
    have hb' : zrow (toRow (rowList f (2 * j) ++ [true])) (rowList f (2 * j)).length 1 = true := hb
    rw [hp, hg] at hb'
    exact absurd hb' (by decide)
  | true =>
    rw [hc] at hb hg
    have hb' : zrow (toRow (rowList f (2 * j) ++ [false])) (rowList f (2 * j)).length 1 = true := hb
    rw [hp, hb'] at hg
    exact absurd hg (by decide)

theorem rowList_cell (f : Nat → Bool) (j : Nat) :
    rowList f (2 * j) ++ [Theta f (2 * j + 1)] = rowList f (2 * j + 1) := rfl

theorem lastWhite_row (r : Nat) : ∀ p : List Bool,
    lastWhite (2 * r) (rowList (word p) (2 * p.length)) =
      cubeSum r (fun q => (!check (p.length + r) (p ++ q)).toNat) := by
  induction r with
  | zero =>
    intro p
    show (if ok (rowList (word p) (2 * p.length) ++ [false]) then 1 else 0) =
      (!check (p.length + 0) (p ++ [])).toNat
    have hc : check (p.length + 0) (p ++ []) = Theta (word p) (2 * p.length + 1) := by
      rw [List.append_nil]; rfl
    rw [hc]
    cases hb : Theta (word p) (2 * p.length + 1) with
    | false =>
      have h : ok (rowList (word p) (2 * p.length) ++ [false]) := by
        have := ok_rowList (word p) (2 * p.length + 1)
        rwa [← rowList_cell, hb] at this
      rw [ite_eq_left h]
      rfl
    | true =>
      have h := wrong_cell_dead (word p) p.length
      rw [hb] at h
      have h' : ¬ ok (rowList (word p) (2 * p.length) ++ [false]) := h
      rw [ite_eq_right h']
      rfl
  | succ r ih =>
    intro p
    have hstep : lastWhite (2 * (r + 1)) (rowList (word p) (2 * p.length)) =
        lastWhite (2 * r + 1) (rowList (word p) (2 * p.length) ++ [false]) +
          lastWhite (2 * r + 1) (rowList (word p) (2 * p.length) ++ [true]) := rfl
    have hext : ∀ x : Bool, rowList (word p) (2 * p.length + 1) =
        rowList (word (p ++ [x])) (2 * p.length + 1) := by
      intro x
      apply rowList_congr
      intro i _ hi
      exact Theta_dep _ _ _ (fun s hs => (word_lt p [x] (by omega)).symm)
    have hflip : Theta (word (p ++ [true])) (2 * p.length + 2) =
        !Theta (word (p ++ [false])) (2 * p.length + 2) := by
      apply not_of_xor
      rw [tri_even _ _ p.length (fun s hs => by rw [word_lt p _ hs, word_lt p _ hs])]
      have e : ∀ x : Bool, word (p ++ [x]) p.length = x := fun x => word_ge p [x] 0
      rw [e, e]
      rfl
    have hsucc : ∀ x : Bool, rowList (word (p ++ [x])) (2 * (p ++ [x]).length) =
        rowList (word p) (2 * p.length + 1) ++ [Theta (word (p ++ [x])) (2 * p.length + 2)] := by
      intro x
      have hl : 2 * (p ++ [x]).length = 2 * p.length + 1 + 1 := by simp; omega
      rw [hl, hext x]
      rfl
    have hih : ∀ x : Bool,
        lastWhite (2 * r) (rowList (word p) (2 * p.length + 1) ++ [Theta (word (p ++ [x])) (2 * p.length + 2)]) =
          cubeSum r (fun q => (!check (p.length + (r + 1)) (p ++ x :: q)).toNat) := by
      intro x
      rw [← hsucc x, ih (p ++ [x])]
      apply cubeSum_congr
      intro q _
      have hlen : (p ++ [x]).length + r = p.length + (r + 1) := by simp; omega
      rw [hlen, List.append_assoc]
      rfl
    have hright : lastWhite (2 * r + 1) (rowList (word p) (2 * p.length + 1)) =
        cubeSum (r + 1) (fun q => (!check (p.length + (r + 1)) (p ++ q)).toNat) := by
      show lastWhite (2 * r) (rowList (word p) (2 * p.length + 1) ++ [false]) +
          lastWhite (2 * r) (rowList (word p) (2 * p.length + 1) ++ [true]) =
        cubeSum r _ + cubeSum r _
      have h0 := hih false
      have h1 := hih true
      rw [hflip] at h1
      cases hb : Theta (word (p ++ [false])) (2 * p.length + 2) with
      | false =>
        rw [hb] at h0 h1
        have h1' : lastWhite (2 * r) (rowList (word p) (2 * p.length + 1) ++ [true]) = _ := h1
        rw [h0, h1']
      | true =>
        rw [hb] at h0 h1
        have h1' : lastWhite (2 * r) (rowList (word p) (2 * p.length + 1) ++ [false]) = _ := h1
        rw [h0, h1', Nat.add_comm]
    have hdead := wrong_cell_dead (word p) p.length
    cases hb : Theta (word p) (2 * p.length + 1) with
    | false =>
      rw [hb] at hdead
      have hd : ¬ ok (rowList (word p) (2 * p.length) ++ [true]) := hdead
      have e : rowList (word p) (2 * p.length + 1) = rowList (word p) (2 * p.length) ++ [false] := by
        rw [← rowList_cell, hb]
      rw [hstep, lastWhite_of_not_ok hd, Nat.add_zero]
      rw [e] at hright
      exact hright
    | true =>
      rw [hb] at hdead
      have hd : ¬ ok (rowList (word p) (2 * p.length) ++ [false]) := hdead
      have e : rowList (word p) (2 * p.length + 1) = rowList (word p) (2 * p.length) ++ [true] := by
        rw [← rowList_cell, hb]
      rw [hstep, lastWhite_of_not_ok hd, Nat.zero_add]
      rw [e] at hright
      exact hright

/-- **The first check, counted.** -/
theorem first_check_count (n : Nat) : firstCheck n + ones n = 2 ^ n := by
  have h := lastWhite_row n []
  have e : firstCheck n = cubeSum n (fun q => (!check n q).toNat) := by
    have h' : lastWhite (2 * n) (rowList (word []) (2 * ([] : List Bool).length)) =
        cubeSum n (fun q => (!check (([] : List Bool).length + n) ([] ++ q)).toNat) := h
    simp only [List.length_nil, Nat.mul_zero, Nat.zero_add, List.nil_append] at h'
    exact h'
  have s : cubeSum n (fun q => (!check n q).toNat + (check n q).toNat) = cubeSum n (fun _ => 1) :=
    cubeSum_congr fun l _ => by cases check n l <;> rfl
  rw [cubeSum_add, cubeSum_const] at s
  rw [e]
  unfold ones
  simpa using s

/-- **Balance.** A check that is not near constant passes between one fortieth and thirty-nine
fortieths of the rows. -/
theorem first_check_balanced {n : Nat} (h : ¬ Bad n) :
    2 ^ n ≤ 40 * firstCheck n ∧ 40 * firstCheck n ≤ 39 * 2 ^ n := by
  have hc := first_check_count n
  have hb := ones_le n
  unfold Bad gap at h
  generalize 2 ^ n = N at *
  omega

end Rule30FirstChecks

open Rule30ZeroBoundary Rule30FirstChecks

/-! ### Exclusive-or sums over the cube -/

/-- The exclusive-or of `F` over all bit lists of length `n`. -/
def xs : Nat → (List Bool → Bool) → Bool
  | 0, F => F []
  | n + 1, F => xor (xs n (fun l => F (false :: l))) (xs n (fun l => F (true :: l)))

theorem xs_congr {n : Nat} {F G : List Bool → Bool} (h : ∀ l, l.length = n → F l = G l) :
    xs n F = xs n G := by
  induction n generalizing F G with
  | zero => exact h [] rfl
  | succ n ih =>
    show xor (xs n _) (xs n _) = xor (xs n _) (xs n _)
    rw [ih (fun l hl => h (false :: l) (by simp [hl])), ih (fun l hl => h (true :: l) (by simp [hl]))]

theorem xs_xor (n : Nat) (F G : List Bool → Bool) :
    xs n (fun l => xor (F l) (G l)) = xor (xs n F) (xs n G) := by
  induction n generalizing F G with
  | zero => rfl
  | succ n ih =>
    show xor (xs n fun l => xor (F (false :: l)) (G (false :: l)))
        (xs n fun l => xor (F (true :: l)) (G (true :: l))) =
      xor (xor (xs n fun l => F (false :: l)) (xs n fun l => F (true :: l)))
        (xor (xs n fun l => G (false :: l)) (xs n fun l => G (true :: l)))
    rw [ih (fun l => F (false :: l)) (fun l => G (false :: l)),
      ih (fun l => F (true :: l)) (fun l => G (true :: l))]
    generalize xs n (fun l => F (false :: l)) = a
    generalize xs n (fun l => G (false :: l)) = b
    generalize xs n (fun l => F (true :: l)) = c
    generalize xs n (fun l => G (true :: l)) = d
    cases a <;> cases b <;> cases c <;> cases d <;> rfl

theorem xs_const (n : Nat) (c : Bool) : xs (n + 1) (fun _ => c) = false := by
  show xor (xs n fun _ => c) (xs n fun _ => c) = false
  generalize xs n (fun _ => c) = a
  cases a <;> rfl

theorem xs_not (n : Nat) (F : List Bool → Bool) : xs (n + 1) (fun l => !F l) = xs (n + 1) F := by
  have h := xs_xor (n + 1) F (fun _ => true)
  rw [xs_const] at h
  have e : xs (n + 1) (fun l => !F l) = xs (n + 1) (fun l => xor (F l) true) :=
    xs_congr fun l _ => by cases F l <;> rfl
  rw [e, h]
  generalize xs (n + 1) F = a
  cases a <;> rfl

/-- A function that does not read the first bit sums to `false`. -/
theorem xs_head {n : Nat} {F : List Bool → Bool} (h : ∀ l, F (false :: l) = F (true :: l)) :
    xs (n + 1) F = false := by
  show xor (xs n fun l => F (false :: l)) (xs n fun l => F (true :: l)) = false
  rw [show (fun l => F (false :: l)) = (fun l => F (true :: l)) from funext h]
  generalize xs n (fun l => F (true :: l)) = a
  cases a <;> rfl

/-- Summing the last bit first. -/
theorem xs_snoc (n : Nat) (F : List Bool → Bool) :
    xs (n + 1) F = xs n (fun l => xor (F (l ++ [false])) (F (l ++ [true]))) := by
  induction n generalizing F with
  | zero => rfl
  | succ n ih =>
    show xor (xs (n + 1) _) (xs (n + 1) _) = xs (n + 1) _
    rw [ih, ih]
    rfl

theorem toNat_xor (a b : Bool) : (xor a b).toNat = (a.toNat + b.toNat) % 2 := by
  cases a <;> cases b <;> rfl

/-- The parity of a count over the cube is the exclusive-or sum. -/
theorem cubeSum_parity (n : Nat) (F : List Bool → Bool) :
    cubeSum n (fun l => (F l).toNat) % 2 = (xs n F).toNat := by
  induction n generalizing F with
  | zero =>
    show (F []).toNat % 2 = (F []).toNat
    generalize F [] = a
    cases a <;> rfl
  | succ n ih =>
    have h1 : cubeSum n (fun l => (F (false :: l)).toNat) % 2 = (xs n fun l => F (false :: l)).toNat :=
      ih _
    have h2 : cubeSum n (fun l => (F (true :: l)).toNat) % 2 = (xs n fun l => F (true :: l)).toNat :=
      ih _
    show (cubeSum n (fun l => (F (false :: l)).toNat) + cubeSum n (fun l => (F (true :: l)).toNat)) % 2 =
      (xor (xs n fun l => F (false :: l)) (xs n fun l => F (true :: l))).toNat
    rw [toNat_xor]
    omega

/-! ### The derivative along an anti-diagonal -/

/-- `zs a (k + 1) t` is the exclusive-or of the negated cells `recon a i (t + k - 1 - i)` for
`i < k`: the anti-diagonal two steps behind the one through depth `k + 1` and time `t`. -/
def zs (a : Nat → Bool) : Nat → Nat → Bool
  | 0, _ => false
  | 1, _ => false
  | k + 2, t => xor (zs a (k + 1) (t + 1)) (!recon a k t)

theorem zs_two (a : Nat → Bool) (k t : Nat) :
    zs a (k + 2) t = xor (zs a (k + 1) (t + 1)) (!recon a k t) := rfl

/-- `zs a k t` only reads `a` at times `≥ t`. -/
theorem zs_local {a b : Nat → Bool} {t : Nat} (h : ∀ s, t ≤ s → a s = b s) :
    ∀ k, zs a k t = zs b k t := by
  have key : ∀ k, (∀ t, (∀ s, t ≤ s → a s = b s) → zs a k t = zs b k t) ∧
      (∀ t, (∀ s, t ≤ s → a s = b s) → zs a (k + 1) t = zs b (k + 1) t) := by
    intro k
    induction k with
    | zero => exact ⟨fun _ _ => rfl, fun _ _ => rfl⟩
    | succ k ih =>
      refine ⟨ih.2, fun t h => ?_⟩
      show zs a (k + 2) t = zs b (k + 2) t
      rw [zs_two, zs_two, ih.2 (t + 1) (fun s hs => h s (by omega)),
        recon_local k t (fun j _ => h (t + j) (by omega))]
  exact fun k => (key k).1 t h

/-- **The derivative in the second newest entry.** If `a` and `b` differ only at time `d - 1`, then
along the anti-diagonal of time `d` the cells differ by `zs`. -/
theorem diag (a b : Nat → Bool) (d : Nat) (hd : 1 ≤ d) (hab : ∀ s, s ≠ d - 1 → a s = b s)
    (hflip : xor (a (d - 1)) (b (d - 1)) = true) :
    ∀ k t, t + (k + 1) = d + 1 → xor (recon a (k + 1) t) (recon b (k + 1) t) = zs a (k + 1) t := by
  intro k
  induction k with
  | zero =>
    intro t ht
    show xor (a t) (b t) = false
    rw [hab t (by omega)]
    generalize b t = x
    cases x <;> rfl
  | succ k ih =>
    intro t ht
    have e1 := ih (t + 1) (by omega)
    have e2 : xor (recon a (k + 1) t) (recon b (k + 1) t) = true := by
      rw [recon_aff k a b t (fun j hj => hab (t + j) (by omega)), show t + k = d - 1 by omega]
      exact hflip
    have e3 : recon a k t = recon b k t := recon_local k t (fun j hj => hab (t + j) (by omega))
    show xor (recon a (k + 2) t) (recon b (k + 2) t) = xor (zs a (k + 1) (t + 1)) (!recon a k t)
    rw [recon_two, recon_two, ← e1, ← e3]
    revert e2
    generalize recon a (k + 1) (t + 1) = p
    generalize recon b (k + 1) (t + 1) = q
    generalize recon a (k + 1) t = y
    generalize recon b (k + 1) t = y'
    generalize recon a k t = z
    cases p <;> cases q <;> cases y <;> cases y' <;> cases z <;> decide

/-! ### Column `-1` of a word with one more bit -/

theorem alt_snoc_ne (l : List Bool) (s : Nat) (hs : s ≠ 2 * l.length + 1) :
    alt (word (l ++ [false])) s = alt (word (l ++ [true])) s := by
  unfold alt
  by_cases h2 : s % 2 = 0
  · rw [ite_eq_left h2, ite_eq_left h2]
  · rw [ite_eq_right h2, ite_eq_right h2]
    rcases Nat.lt_or_gt_of_ne (show s / 2 ≠ l.length by omega) with hlt | hgt
    · rw [word_lt l [false] hlt, word_lt l [true] hlt]
    · obtain ⟨j, hj⟩ : ∃ j, s / 2 = l.length + (j + 1) := ⟨s / 2 - l.length - 1, by omega⟩
      rw [hj, word_ge, word_ge]
      rfl

theorem alt_snoc_top (l : List Bool) (b : Bool) : alt (word (l ++ [b])) (2 * l.length + 1) = b := by
  unfold alt
  rw [ite_eq_right (by omega), show (2 * l.length + 1) / 2 = l.length + 0 by omega, word_ge]
  rfl

theorem alt_snoc_low (l : List Bool) (b : Bool) (s : Nat) (hs : s < 2 * l.length + 1) :
    alt (word (l ++ [b])) s = alt (word l) s := by
  unfold alt
  by_cases h2 : s % 2 = 0
  · rw [ite_eq_left h2, ite_eq_left h2]
  · rw [ite_eq_right h2, ite_eq_right h2, word_lt l [b] (by omega)]

theorem alt_cons (b c : Bool) (l : List Bool) (s : Nat) (hs : 2 ≤ s) :
    alt (word (b :: l)) s = alt (word (c :: l)) s := by
  unfold alt
  by_cases h2 : s % 2 = 0
  · rw [ite_eq_left h2, ite_eq_left h2]
  · rw [ite_eq_right h2, ite_eq_right h2]
    obtain ⟨j, hj⟩ : ∃ j, s / 2 = j + 1 := ⟨s / 2 - 1, by omega⟩
    rw [hj]
    rfl

theorem snoc_hab (p : List Bool) :
    ∀ s, s ≠ 2 * p.length + 2 - 1 → alt (word (p ++ [false])) s = alt (word (p ++ [true])) s :=
  fun s hs => alt_snoc_ne p s (by omega)

theorem snoc_flip (p : List Bool) :
    xor (alt (word (p ++ [false])) (2 * p.length + 2 - 1))
      (alt (word (p ++ [true])) (2 * p.length + 2 - 1)) = true := by
  rw [show 2 * p.length + 2 - 1 = 2 * p.length + 1 by omega, alt_snoc_top, alt_snoc_top]
  rfl

/-! ### The two recurrences for the top coefficient -/

/-- The cell at depth `2 m` and time `1` of the constrained history with free bits `l`. -/
def bcell (m : Nat) (l : List Bool) : Bool := recon (alt (word l)) (2 * m) 1

/-- The part of the derivative at times `≥ 2`, which does not read the first free bit. -/
def hc (m : Nat) (l : List Bool) : Bool := zs (alt (word (l ++ [false]))) (2 * m + 1) 2

theorem hc_cons (m : Nat) (b c : Bool) (l : List Bool) : hc m (b :: l) = hc m (c :: l) :=
  zs_local (t := 2) (fun s hs => alt_cons b c (l ++ [false]) s hs) (2 * m + 1)

/-- **The derivative of the check in its newest free bit.** -/
theorem check_flip (m : Nat) (p : List Bool) (hp : p.length = m) :
    xor (check (m + 1) (p ++ [false])) (check (m + 1) (p ++ [true])) =
      xor (xor (hc m p) (!bcell m p)) (!check m p) := by
  subst hp
  have hd := diag (alt (word (p ++ [false]))) (alt (word (p ++ [true]))) (2 * p.length + 2)
    (by omega) (snoc_hab p) (snoc_flip p) (2 * p.length + 2) 0 (by omega)
  have e1 : recon (alt (word (p ++ [false]))) (2 * p.length) 1 = bcell p.length p :=
    recon_local _ 1 (fun j hj => alt_snoc_low p false (1 + j) (by omega))
  have e2 : recon (alt (word (p ++ [false]))) (2 * p.length + 1) 0 = check p.length p :=
    recon_local _ 0 (fun j hj => alt_snoc_low p false (0 + j) (by omega))
  show xor (recon (alt (word (p ++ [false]))) (2 * (p.length + 1) + 1) 0)
      (recon (alt (word (p ++ [true]))) (2 * (p.length + 1) + 1) 0) = _
  rw [show 2 * (p.length + 1) + 1 = 2 * p.length + 2 + 1 by omega, hd,
    show 2 * p.length + 2 + 1 = 2 * p.length + 1 + 2 by omega, zs_two,
    show 2 * p.length + 1 + 1 = 2 * p.length + 2 by omega, zs_two, e1, e2]
  rfl

/-- **The derivative of `bcell` in its newest free bit.** -/
theorem bcell_flip (m : Nat) (p : List Bool) (hp : p.length = m) :
    xor (bcell (m + 1) (p ++ [false])) (bcell (m + 1) (p ++ [true])) =
      xor (hc m p) (!bcell m p) := by
  subst hp
  have hd := diag (alt (word (p ++ [false]))) (alt (word (p ++ [true]))) (2 * p.length + 2)
    (by omega) (snoc_hab p) (snoc_flip p) (2 * p.length + 1) 1 (by omega)
  have e1 : recon (alt (word (p ++ [false]))) (2 * p.length) 1 = bcell p.length p :=
    recon_local _ 1 (fun j hj => alt_snoc_low p false (1 + j) (by omega))
  show xor (recon (alt (word (p ++ [false]))) (2 * (p.length + 1)) 1)
      (recon (alt (word (p ++ [true]))) (2 * (p.length + 1)) 1) = _
  rw [show 2 * (p.length + 1) = 2 * p.length + 1 + 1 by omega, hd,
    show 2 * p.length + 1 + 1 = 2 * p.length + 2 by omega, zs_two, e1]
  rfl

theorem bsum (m : Nat) : xs (m + 1) (bcell (m + 1)) = true := by
  induction m with
  | zero => decide
  | succ m ih =>
    have h1 : xs (m + 1 + 1) (bcell (m + 1 + 1)) =
        xs (m + 1) (fun l => xor (hc (m + 1) l) (!bcell (m + 1) l)) := by
      rw [xs_snoc]
      exact xs_congr fun l hl => bcell_flip (m + 1) l hl
    rw [h1, xs_xor, xs_head (F := hc (m + 1)) (fun l => hc_cons (m + 1) false true l), xs_not, ih]
    rfl

/-- **The first recurrence.** The top sum of the check is the previous one plus the top sum of
`bcell`. -/
theorem top_succ (m : Nat) :
    xs (m + 2) (check (m + 2)) = xor (xs (m + 1) (check (m + 1))) (xs (m + 1) (bcell (m + 1))) := by
  have h1 : xs (m + 1 + 1) (check (m + 1 + 1)) =
      xs (m + 1) (fun l => xor (xor (hc (m + 1) l) (!bcell (m + 1) l)) (!check (m + 1) l)) := by
    rw [xs_snoc]
    exact xs_congr fun l hl => check_flip (m + 1) l hl
  rw [h1, xs_xor, xs_xor, xs_head (F := hc (m + 1)) (fun l => hc_cons (m + 1) false true l),
    xs_not, xs_not]
  generalize xs (m + 1) (check (m + 1)) = x
  generalize xs (m + 1) (bcell (m + 1)) = y
  cases x <;> cases y <;> rfl

/-- The exclusive-or of the check over all words is `n mod 2`. -/
theorem top_sum (n : Nat) (hn : 1 ≤ n) : xs n (check n) = decide (n % 2 = 1) := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  induction m with
  | zero => decide
  | succ m ih =>
    rw [top_succ, ih (by omega), bsum]
    by_cases h : (m + 1) % 2 = 1
    · rw [decide_eq_true h, decide_eq_false (by omega)]
      rfl
    · rw [decide_eq_false h, decide_eq_true (by omega)]
      rfl

/-! ### The coefficient without `f 1` -/

/-- Insert a white bit at position `1`. -/
def ins : List Bool → List Bool
  | [] => [false]
  | x :: l => x :: false :: l

/-- The sum over the words with `f 1 = 0`, for checks of `m + 2` bits. -/
def rsum (m : Nat) : Bool := xs (m + 1) (fun l => check (m + 2) (ins l))

/-- The same sum for `bcell` of `m + 2` bits. -/
def tsum (m : Nat) : Bool := xs (m + 1) (fun l => bcell (m + 2) (ins l))

theorem ins_cons_length (x : Bool) (l : List Bool) : (ins (x :: l)).length = l.length + 2 := rfl

theorem tsum_succ (m : Nat) : tsum (m + 1) = tsum m := by
  have h1 : xs (m + 1 + 1) (fun l => bcell (m + 1 + 2) (ins l)) =
      xs (m + 1) (fun l => xor (hc (m + 2) (ins l)) (!bcell (m + 2) (ins l))) := by
    rw [xs_snoc]
    apply xs_congr
    intro l hl
    cases l with
    | nil => simp at hl
    | cons x l' =>
      exact bcell_flip (m + 2) (ins (x :: l')) (by rw [ins_cons_length]; simp at hl; omega)
  show xs (m + 1 + 1) (fun l => bcell (m + 1 + 2) (ins l)) = tsum m
  rw [h1, xs_xor, xs_head (F := fun l => hc (m + 2) (ins l))
    (fun l => hc_cons (m + 2) false true (false :: l)), xs_not]
  show xor false (tsum m) = tsum m
  generalize tsum m = a
  cases a <;> rfl

theorem rsum_succ (m : Nat) : rsum (m + 1) = xor (rsum m) (tsum m) := by
  have h1 : xs (m + 1 + 1) (fun l => check (m + 1 + 2) (ins l)) =
      xs (m + 1) (fun l =>
        xor (xor (hc (m + 2) (ins l)) (!bcell (m + 2) (ins l))) (!check (m + 2) (ins l))) := by
    rw [xs_snoc]
    apply xs_congr
    intro l hl
    cases l with
    | nil => simp at hl
    | cons x l' =>
      exact check_flip (m + 2) (ins (x :: l')) (by rw [ins_cons_length]; simp at hl; omega)
  show xs (m + 1 + 1) (fun l => check (m + 1 + 2) (ins l)) = xor (rsum m) (tsum m)
  rw [h1, xs_xor, xs_xor, xs_head (F := fun l => hc (m + 2) (ins l))
    (fun l => hc_cons (m + 2) false true (false :: l)), xs_not, xs_not]
  show xor (xor false (tsum m)) (rsum m) = xor (rsum m) (tsum m)
  generalize tsum m = a
  generalize rsum m = b
  cases a <;> cases b <;> rfl

theorem tsum_all (m : Nat) : tsum m = true := by
  induction m with
  | zero => decide
  | succ m ih => rw [tsum_succ, ih]

theorem rsum_all (m : Nat) : rsum m = decide (m % 2 = 0) := by
  induction m with
  | zero => decide
  | succ m ih =>
    rw [rsum_succ, ih, tsum_all]
    by_cases h : m % 2 = 0
    · rw [decide_eq_true h, decide_eq_false (by omega)]
      rfl
    · rw [decide_eq_false h, decide_eq_true (by omega)]
      rfl

/-! ### Algebraic normal form -/

/-- The coefficient of the monomial of the mask `S` in the algebraic normal form of `F`: the
exclusive-or of `F` over the bit lists below `S`. -/
def coeff : List Bool → (List Bool → Bool) → Bool
  | [], F => F []
  | false :: S, F => coeff S (fun l => F (false :: l))
  | true :: S, F => xor (coeff S (fun l => F (false :: l))) (coeff S (fun l => F (true :: l)))

theorem coeff_xor : ∀ (S : List Bool) (F G : List Bool → Bool),
    coeff S (fun l => xor (F l) (G l)) = xor (coeff S F) (coeff S G)
  | [], _, _ => rfl
  | false :: S, F, G => coeff_xor S (fun l => F (false :: l)) (fun l => G (false :: l))
  | true :: S, F, G => by
    show xor (coeff S fun l => xor (F (false :: l)) (G (false :: l)))
        (coeff S fun l => xor (F (true :: l)) (G (true :: l))) =
      xor (xor (coeff S fun l => F (false :: l)) (coeff S fun l => F (true :: l)))
        (xor (coeff S fun l => G (false :: l)) (coeff S fun l => G (true :: l)))
    rw [coeff_xor S (fun l => F (false :: l)) (fun l => G (false :: l)),
      coeff_xor S (fun l => F (true :: l)) (fun l => G (true :: l))]
    generalize coeff S (fun l => F (false :: l)) = a
    generalize coeff S (fun l => G (false :: l)) = b
    generalize coeff S (fun l => F (true :: l)) = c
    generalize coeff S (fun l => G (true :: l)) = d
    cases a <;> cases b <;> cases c <;> cases d <;> rfl

/-- **Möbius expansion.** `F x` is the exclusive-or of the coefficients of the masks below `x`, so
`coeff` is the algebraic normal form of `F`. -/
theorem anf_expansion : ∀ (x : List Bool) (F : List Bool → Bool), F x = coeff x (fun S => coeff S F)
  | [], _ => rfl
  | false :: x, F => anf_expansion x (fun l => F (false :: l))
  | true :: x, F => by
    have e : F (true :: x) = coeff x (fun S => coeff S fun l => F (true :: l)) :=
      anf_expansion x (fun l => F (true :: l))
    show F (true :: x) = xor (coeff x fun S => coeff S fun l => F (false :: l))
      (coeff x fun S => xor (coeff S fun l => F (false :: l)) (coeff S fun l => F (true :: l)))
    rw [coeff_xor x (fun S => coeff S fun l => F (false :: l)) (fun S => coeff S fun l => F (true :: l)),
      ← e]
    generalize coeff x (fun S => coeff S fun l => F (false :: l)) = a
    generalize F (true :: x) = c
    cases a <;> cases c <;> rfl

theorem coeff_replicate (n : Nat) (F : List Bool → Bool) : coeff (List.replicate n true) F = xs n F := by
  induction n generalizing F with
  | zero => rfl
  | succ n ih =>
    show xor (coeff (List.replicate n true) _) (coeff (List.replicate n true) _) = xor (xs n _) (xs n _)
    rw [ih, ih]

theorem coeff_omit (m : Nat) (F : List Bool → Bool) :
    coeff (true :: false :: List.replicate m true) F = xs (m + 1) (fun l => F (ins l)) := by
  show xor (coeff (List.replicate m true) fun l => F (false :: false :: l))
      (coeff (List.replicate m true) fun l => F (true :: false :: l)) =
    xor (xs m fun l => F (false :: false :: l)) (xs m fun l => F (true :: false :: l))
  rw [coeff_replicate, coeff_replicate]

/-! ### The coefficients and the degree of the check -/

/-- **The top coefficient.** For `n ≥ 1`, the coefficient of `f 0 ⋯ f (n - 1)` in the check is
`n mod 2`. -/
theorem top_coefficient (n : Nat) (hn : 1 ≤ n) :
    coeff (List.replicate n true) (check n) = decide (n % 2 = 1) := by
  rw [coeff_replicate]
  exact top_sum n hn

/-- **The coefficient without `f 1`.** For `n ≥ 2`, the coefficient of the monomial of every free
bit but `f 1` is `n + 1 mod 2`. -/
theorem omit_coefficient (n : Nat) (hn : 2 ≤ n) :
    coeff (true :: false :: List.replicate (n - 2) true) (check n) = decide (n % 2 = 0) := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 2 := ⟨n - 2, by omega⟩
  rw [show m + 2 - 2 = m by omega, coeff_omit]
  have h := rsum_all m
  unfold rsum at h
  rw [h]
  exact decide_eq_decide.mpr (by omega)

/-- `F` on bit lists of length `n` has degree `d`: no mask with more than `d` ones has a nonzero
coefficient, and one with exactly `d` ones has. -/
def IsDegree (n : Nat) (F : List Bool → Bool) (d : Nat) : Prop :=
  (∀ S : List Bool, S.length = n → d < S.count true → coeff S F = false) ∧
    ∃ S : List Bool, S.length = n ∧ S.count true = d ∧ coeff S F = true

theorem count_full : ∀ S : List Bool, S.count true = S.length → S = List.replicate S.length true
  | [], _ => rfl
  | b :: S, h => by
    have hle : S.count true ≤ S.length := List.count_le_length
    cases b with
    | false =>
      simp at h
      omega
    | true =>
      simp at h
      rw [List.length_cons, List.replicate_succ, ← count_full S h]

/-- **The degree of the check** is `n` for odd `n` and `n - 1` for even `n`, for `n ≥ 1`. -/
theorem check_degree (n : Nat) (hn : 1 ≤ n) :
    IsDegree n (check n) (if n % 2 = 1 then n else n - 1) := by
  by_cases hodd : n % 2 = 1
  · rw [ite_eq_left hodd]
    refine ⟨fun S hS hlt => ?_, List.replicate n true, List.length_replicate, List.count_replicate_self,
      by rw [top_coefficient n hn, decide_eq_true hodd]⟩
    have hle : S.count true ≤ S.length := List.count_le_length
    omega
  · rw [ite_eq_right hodd]
    refine ⟨fun S hS hlt => ?_, true :: false :: List.replicate (n - 2) true, by simp; omega,
      by simp; omega, by rw [omit_coefficient n (by omega), decide_eq_true (by omega)]⟩
    have hle : S.count true ≤ S.length := List.count_le_length
    rw [count_full S (by omega), hS, top_coefficient n hn, decide_eq_false hodd]

/-! ### Parities of the counts -/

/-- The number of words of length `n ≥ 1` on which the check is black is congruent to `n`
modulo `2`. -/
theorem ones_parity (n : Nat) (hn : 1 ≤ n) : ones n % 2 = n % 2 := by
  have h := cubeSum_parity n (check n)
  have e : ones n = cubeSum n (fun l => (check n l).toNat) := rfl
  rw [e, h, top_sum n hn]
  rcases Nat.mod_two_eq_zero_or_one n with h0 | h1
  · rw [decide_eq_false (by omega), h0]
    rfl
  · rw [decide_eq_true h1, h1]
    rfl

/-- **The survivors of the first check, modulo 2.** For `n ≥ 1`, the number of rows of width at
most `2 n` that are black at column `-1` at every even tick through `2 n` is congruent to `n`
modulo `2`. -/
theorem first_check_parity (n : Nat) (hn : 1 ≤ n) : firstCheck n % 2 = n % 2 := by
  have h := first_check_count n
  have h2 := ones_parity n hn
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  rw [Nat.pow_succ] at h
  omega

/-- **The Walsh sum modulo 4.** For `n ≥ 2`, `2 ^ n - 2 * ones n` is `2` modulo `4` exactly at odd
`n`. -/
theorem walsh_mod_four (n : Nat) (hn : 2 ≤ n) :
    ((2 : Int) ^ n - 2 * (ones n : Int)) % 4 = 2 * ((n % 2 : Nat) : Int) := by
  have h := ones_parity n (by omega)
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 2 := ⟨n - 2, by omega⟩
  rw [show (2 : Int) ^ (m + 2) = 4 * 2 ^ m by rw [Int.pow_succ, Int.pow_succ]; omega]
  generalize (2 : Int) ^ m = N
  omega

/-- **The exception at `n = 1`.** There the Walsh sum is `0`, although `1` is odd. -/
theorem walsh_one : (2 : Int) ^ 1 - 2 * (ones 1 : Int) = 0 := by
  have h : ones 1 = 1 := by decide
  rw [h]
  rfl

/-! ### The other clock phase -/

/-- Column `-1` in the other phase: the free bits `g` at the even steps, black at the odd ones. -/
def altO (g : Nat → Bool) (t : Nat) : Bool := if t % 2 = 0 then g (t / 2) else true

/-- The first check past the free range in the other phase: the cell at depth `2 n` and time `0`
with the white wall, for the `n` free bits of `l`. -/
def otherCheck (n : Nat) (l : List Bool) : Bool := recon (altO (word l)) (2 * n) 0

theorem altO_snoc_ne (l : List Bool) (s : Nat) (hs : s ≠ 2 * l.length) :
    altO (word (l ++ [false])) s = altO (word (l ++ [true])) s := by
  unfold altO
  by_cases h2 : s % 2 = 0
  · rw [ite_eq_left h2, ite_eq_left h2]
    rcases Nat.lt_or_gt_of_ne (show s / 2 ≠ l.length by omega) with hlt | hgt
    · rw [word_lt l [false] hlt, word_lt l [true] hlt]
    · obtain ⟨j, hj⟩ : ∃ j, s / 2 = l.length + (j + 1) := ⟨s / 2 - l.length - 1, by omega⟩
      rw [hj, word_ge, word_ge]
      rfl
  · rw [ite_eq_right h2, ite_eq_right h2]

theorem altO_snoc_top (l : List Bool) (b : Bool) : altO (word (l ++ [b])) (2 * l.length) = b := by
  unfold altO
  rw [ite_eq_left (by omega), show 2 * l.length / 2 = l.length + 0 by omega, word_ge]
  rfl

theorem altO_snoc_low (l : List Bool) (b : Bool) (s : Nat) (hs : s < 2 * l.length) :
    altO (word (l ++ [b])) s = altO (word l) s := by
  unfold altO
  by_cases h2 : s % 2 = 0
  · rw [ite_eq_left h2, ite_eq_left h2, word_lt l [b] (by omega)]
  · rw [ite_eq_right h2, ite_eq_right h2]

theorem altO_cons (b c : Bool) (l : List Bool) (s : Nat) (hs : 1 ≤ s) :
    altO (word (b :: l)) s = altO (word (c :: l)) s := by
  unfold altO
  by_cases h2 : s % 2 = 0
  · rw [ite_eq_left h2, ite_eq_left h2]
    obtain ⟨j, hj⟩ : ∃ j, s / 2 = j + 1 := ⟨s / 2 - 1, by omega⟩
    rw [hj]
    rfl
  · rw [ite_eq_right h2, ite_eq_right h2]

/-- The part of the other-phase derivative at times `≥ 1`, which does not read `g 0`. -/
def ho (m : Nat) (l : List Bool) : Bool := zs (altO (word (l ++ [false]))) (2 * m + 1) 1

theorem ho_cons (m : Nat) (b c : Bool) (l : List Bool) : ho m (b :: l) = ho m (c :: l) :=
  zs_local (t := 1) (fun s hs => altO_cons b c (l ++ [false]) s hs) (2 * m + 1)

/-- **The other-phase derivative in the newest free bit.** Only one earlier cell survives at
time `0`, the previous check. -/
theorem other_flip (m : Nat) (p : List Bool) (hp : p.length = m) :
    xor (otherCheck (m + 1) (p ++ [false])) (otherCheck (m + 1) (p ++ [true])) =
      xor (ho m p) (!otherCheck m p) := by
  subst hp
  have hd := diag (altO (word (p ++ [false]))) (altO (word (p ++ [true]))) (2 * p.length + 1)
    (by omega) (fun s hs => altO_snoc_ne p s (by omega))
    (by rw [show 2 * p.length + 1 - 1 = 2 * p.length by omega, altO_snoc_top, altO_snoc_top]; rfl)
    (2 * p.length + 1) 0 (by omega)
  have e1 : recon (altO (word (p ++ [false]))) (2 * p.length) 0 = otherCheck p.length p :=
    recon_local _ 0 (fun j hj => altO_snoc_low p false (0 + j) (by omega))
  show xor (recon (altO (word (p ++ [false]))) (2 * (p.length + 1)) 0)
      (recon (altO (word (p ++ [true]))) (2 * (p.length + 1)) 0) = _
  rw [show 2 * (p.length + 1) = 2 * p.length + 1 + 1 by omega, hd,
    show 2 * p.length + 1 + 1 = 2 * p.length + 2 by omega, zs_two, e1]
  rfl

/-- **The other phase is always odd.** For every `n ≥ 1`, the check of the other phase is black
on an odd number of the `2 ^ n` words, so its top coefficient is `1` and its degree is `n`. -/
theorem other_phase_odd (n : Nat) (hn : 1 ≤ n) :
    coeff (List.replicate n true) (otherCheck n) = true := by
  rw [coeff_replicate]
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  induction m with
  | zero => decide
  | succ m ih =>
    have h1 : xs (m + 1 + 1) (otherCheck (m + 1 + 1)) =
        xs (m + 1) (fun l => xor (ho (m + 1) l) (!otherCheck (m + 1) l)) := by
      rw [xs_snoc]
      exact xs_congr fun l hl => other_flip (m + 1) l hl
    rw [h1, xs_xor, xs_head (F := ho (m + 1)) (fun l => ho_cons (m + 1) false true l), xs_not,
      ih (by omega)]
    rfl

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Rule30Submission.Rule30FirstChecks", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30ZeroBoundary"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"diag", "top_succ", "top_coefficient", "omit_coefficient", "anf_expansion", "check_degree", "ones_parity", "first_check_parity", "walsh_mod_four", "walsh_one", "other_phase_odd"};
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.check_degree"]["KernelCheck"]
```
