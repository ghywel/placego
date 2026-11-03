---
Template: ComputationalEssay
Name: The closing law of prefix doublings on Rule 30's right edge
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-03
Description: A partial result proved in core Lean: on the kit's gate clocks, including Rule 30's right edge, the difference order drops by exactly one across each pair of letters 10 (a doubling, then a keep), so after a doubling at period q0 (the period before that doubling) an alternating run has at most q0 - 1 pairs and closes with a doubling exactly at that length. Corollaries: 1101011 never occurs among the doubling letters, and five consecutive letters hold at most three doublings once the period is at least 4.
Abstract: See abstract.txt.
Keywords: [rule 30, Rule 30 Prize, right edge, prefix periods, difference order, gate clocks, doubling letters, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Kit pull request 55, the right-edge prefix clocks](https://github.com/WolframInstitute/Rule30PrizeKit/pull/55)", "[Rowland, On the right edge of Rule 30, section 5](https://arxiv.org/abs/math/0612058)"]
---

## The question

Read in the frame that moves with it, the right edge of Rule 30 is a map on bits: bit $j$ is XORed, at each step, with
the OR of bits $j - 1$ and $j - 2$. The kit's `Rule30GateClocks` allows any gate $g_j$ in place of OR. The first $n$ bits
of any seed are periodic in time, with least period $2^{E_n}$, and the exponent $E_n$ grows by $0$ or $1$ as one bit is
added. Write the growth flags as a word of **doubling letters**: letter $n$ is $1$ when adding bit $n$ doubles the
period, and $0$ when it does not.

Which words of doubling letters can occur? The kit and earlier work show that three doublings in a row are rare and that
the period grows at most like half the number of bits. This essay proves an exact rule for one family of words, the
alternating runs, for every gate with a quadratic term.

## The exact countdown

For a stream $f$ of period $M = 2^v$, the kit's `order f M` measures how many differences of $f$ vanish below the full
period: in polynomial terms, the multiplicity of the factor $1 + z$ in $\sum_{t < M} f(t) z^t$ over $\mathbb{F}_2$.

The step that matters is a pair of letters $10$. Take three consecutive streams: $s$ with period $M = 2^v \ge 2$; the
next one, $b$, which has just doubled, so that it is antiperiodic at $M$; and $h$, which integrates the gate,
$h(t + 1) = h(t) \oplus g(b(t), s(t))$, and keeps the period $2M$. In this setting the kit proves that the order drops
by **at most** one: $\mathrm{order}\, s\, M \le \mathrm{order}\, h\, (2M) + 1$ (`order_countdown_gate`). Here it is
shown that for a gate whose derivative in its newer input, $g(1, s) \oplus g(0, s)$, depends on $s$ (OR is such a gate),
it drops by **exactly** one. Past the $M$-th difference, the new stream's differences are exactly those of the older
input:

$$\Delta^{k + 2 + M} h = \Delta^{k + 1} s,$$

so the first vanishing difference of $h$ lies exactly $M + 1$ beyond that of $s$ (`order_countdown_exact`). The guards
are exactly those of this setting: the periods and the antiperiod above, $M \ge 2$, and
$\mathrm{order}\, s\, M + 1 < M$. The last one is needed because the order is capped at $M - 1$: a constant stream,
the zero stream included, has every difference vanishing and so the capped order $M - 1$, and the equality fails there.
This is a statement about a $10$ pair, not about an arbitrary step without a doubling.

## The closing law

Suppose the doubling letters, from position $n$, read

$$1\,(10)^m\,1,$$

a doubling, then $m \ge 0$ pairs "double, keep", then a doubling, where the period before the first doubling is
$q_0 = 2^{E_n}$. The first doubling makes its stream antiperiodic, which fixes its order at $q_0 - 1$. Each pair "10"
then lowers the order of the pair's first stream by exactly one, and a doubling follows exactly when that order has
reached $0$. Hence (`closing_law`):

- $m + 1 \le q_0$;
- the next letter is $1$ if and only if $m + 1 = q_0$.

A closing run therefore has length one less than a power of two. In particular:

- `no_1101011`: the word $1\,(10)^2\,1\,1$ never occurs, since $3$ is not a power of two;
- `no_three_at`: three doublings in a row need $q_0 = 1$;
- `no_11011_at`: $11011$ closes with a doubling only when $q_0 = 2$;
- `five_letter`: once the period is at least $4$, any five consecutive letters contain at most three doublings.

These hold for every seed, finite or infinite, and every family of quadratic gates; `closing_law_or` states the Rule 30
case.

## A picture: the letters of the single black cell

The gate clock of OR from a single black bit, with bits computed for $2^{E}$ steps as each new bit is added:

```wl
orClock[seed_List, nbits_Integer] := Module[{x = PadRight[seed, nbits + 2], hist, ex = {0}, col, force, acc},
  hist = {x};
  col[k_, t_] := If[k == 0, 0, hist[[t + 1, k]]];
  Do[
    While[Length[hist] < 2^Last[ex],
      With[{y = Last[hist]}, AppendTo[hist, Table[BitXor[y[[j]], If[j == 1, 0, BitOr[y[[j - 1]], If[j == 2, 0, y[[j - 2]]]]]], {j, Length[y]}]]]];
    acc = Mod[Total[Table[BitOr[col[n, t], col[Max[n - 1, 0], t]], {t, 0, 2^Last[ex] - 1}]], 2];
    AppendTo[ex, Last[ex] + acc], {n, 0, nbits - 1}];
  ex];
ex = orClock[{1}, 22];
letters = Differences[ex];
runs = Flatten[Table[With[{n = n0}, Module[{m = 0, out = {}},
  While[n + 2 m + 3 <= Length[letters] && letters[[n + 1]] == 1 && letters[[n + 2 m + 2]] == 1,
    AppendTo[out, {n, m, 2^ex[[n + 1]], letters[[n + 2 m + 3]]}];
    If[letters[[n + 2 m + 3]] == 0, m++, Break[]]];
  out]], {n0, 0, Length[letters] - 3}], 1];
Column[{Row[{"letters: ", StringJoin[ToString /@ letters]}],
  Grid[Prepend[{#[[1]], #[[2]], #[[3]], #[[4]], Boole[#[[2]] + 1 == #[[3]]]} & /@ runs,
    {"start n", "pairs m", "q0", "next letter", "law: m+1 = q0"}], Frame -> All]}]
```

Each row is a run $1\,(10)^m\,1$; the next letter is $1$ exactly in the rows where $m + 1 = q_0$. Within the 22 letters
displayed, a run closes with a doubling only once, the $11011$ at $q_0 = 2$; nothing is claimed here about later
letters.

## Related work and what is new

- **The kit.** `Rule30DifferenceOrder` and `Rule30GateClocks` give the order, the reset law and the countdown
  inequality used here. Kit pull request 55 (the right-edge prefix clocks) already proves, for OR, that $11011$ does not
  occur once the period is at least $4$, using the countdown inequality.
- **The portal.** Earlier gate-clock submissions bound the prefix exponent and prove `no_three` and the "01" doubling
  test, without the exact countdown.
- **Literature.** Rowland, section 5, studies the right edge's periods and their growth.
- **New here.** The countdown as an equality for every quadratic gate, and from it the closing law for every $m$ with
  its exact closing length, kernel-checked. The difference-order mechanism itself is classical.
- **Scope.** Statements about the doubling letters of gate clocks. Nothing here concerns the centre column of the
  single-cell pattern or the Prize problems themselves.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30GateClocks` at the
verifier's kit commit 93d98bbe. The exact countdown takes one page; the closing law is an induction over the pairs.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30GateClocks

/-!
# The closing law of prefix doublings, for every gate with a quadratic term

The kit's gate clocks (`Rule30GateClocks`) evolve bit `j` by `x_j(t+1) = x_j(t) xor g j (x_(j-1)(t)) (x_(j-2)(t))`; with
`g j = (· || ·)` this is Rule 30's right edge in the frame moving with it. `prefixExp g x n` is the exponent of the least
period of the first `n` bits, and the column `n + 1` doubles when `prefixExp g x (n + 1) = prefixExp g x n + 1`.
A gate is `Quadratic` when its derivative in the newer input, `g true s xor g false s`, depends on `s`; OR is quadratic
(`quadratic_or`).

* `order_countdown_exact`: if `s` has period `M = 2 ^ v ≥ 2`, `b` is antiperiodic at `M`,
  `h (t + 1) = h t xor g (b t) (s t)` with `g` quadratic, `h` has period `2 M` and `order s M + 1 < M`, then
  `order h (2 M) + 1 = order s M`. The kit's `order_countdown_gate` gives `≤`; this is the equality.
* `closing_law`: after a doubling at exponent `E` (period `q0 = 2 ^ E`), `m ≥ 0` pairs `10` and a doubling,
  `m + 1 ≤ q0`, and the next column doubles iff `m + 1 = q0`. Every quadratic gate family and every seed;
  `closing_law_or` is the OR case.
* `no_1101011`: the doubling word `1 (10)^2 1 1` never occurs, since `3` is not a power of two. In general a closing
  run has length one less than a power of two.
* `no_three_at` (`E ≥ 1`), `no_11011_at` (`E ≥ 2`; `11011` closes with `1` only when `q0 = 2`) and `five_letter`:
  once `prefixExp g x n ≥ 2`, five consecutive columns raise the exponent by at most `3`.

The countdown is the difference-order argument behind the kit's `order_countdown`: past the `M`-th difference,
`h` differs exactly like `s`. Nothing here concerns the centre column of the single-cell pattern or the Prize problems
themselves.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata Rule30RecordCharge Rule30DifferenceOrder Rule30GateClocks

/-- A gate whose derivative in its newer input is `s` or `!s`: its quadratic coefficient is `1`. -/
def Quadratic (g : Bool → Bool → Bool) : Prop := deriv g true ≠ deriv g false

/-- For a quadratic gate, past the first difference the derivative behaves like `s` itself. -/
theorem difs_deriv {g : Bool → Bool → Bool} (hq : Quadratic g) (s : Nat → Bool) (k : Nat) :
    difs (k + 1) (fun t => deriv g (s t)) = difs (k + 1) s := by
  unfold Quadratic at hq
  cases h1 : deriv g true <;> cases h0 : deriv g false <;> rw [h1, h0] at hq
  · exact absurd rfl hq
  · have hc : (fun t => deriv g (s t)) = fun t => xor ((fun _ => true) t) (s t) := by
      funext u; cases hu : s u <;> simp [h0, h1]
    rw [hc, difs_xor, difs_const]
    funext t; cases difs (k + 1) s t <;> rfl
  · have hc : (fun t => deriv g (s t)) = s := by
      funext u; cases hu : s u <;> simp [h0, h1]
    rw [hc]
  · exact absurd rfl hq

/-- Past the `M`-th difference, `h`'s differences are exactly `s`'s, for a quadratic gate. -/
theorem difs_past_gate {g : Bool → Bool → Bool} {s b h : Nat → Bool} {v : Nat} (hq : Quadratic g)
    (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (g (b t) (s t))) (k : Nat) :
    difs (k + 1 + 1 + 2 ^ v) h = difs (k + 1) s := by
  rw [difs_add, difs_two_pow, difs_succ' (k + 1), dif_shift_sum_gate hs hb hh, difs_deriv hq]

/-- The `(M + 1)`-th difference of `h` is the derivative itself. -/
theorem difs_M_succ_gate {g : Bool → Bool → Bool} {s b h : Nat → Bool} {v : Nat}
    (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (g (b t) (s t))) :
    difs (1 + 2 ^ v) h = fun t => deriv g (s t) := by
  rw [difs_add, difs_two_pow]
  show dif (fun t => xor (h (t + 2 ^ v)) (h t)) = _
  exact dif_shift_sum_gate hs hb hh

theorem two_le_two_pow {v : Nat} (hv : 1 ≤ v) : 2 ≤ 2 ^ v := by
  obtain ⟨k, rfl⟩ : ∃ k, v = k + 1 := ⟨v - 1, by omega⟩
  rw [Nat.pow_succ]; have := Nat.one_le_two_pow (n := k); omega

/-- If `h` keeps the period `2 * M`, then `s` has positive order: a doubling is the only way to reach order `0`. -/
theorem order_pos_of_period {g : Bool → Bool → Bool} {s b h : Nat → Bool} {v : Nat} (hq : Quadratic g)
    (hv : 1 ≤ v) (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (g (b t) (s t)))
    (hper : ∀ t, h (t + 2 * 2 ^ v) = h t) :
    1 ≤ order s (2 ^ v) := by
  have hM := two_le_two_pow hv
  have hvan : Vanish (2 * 2 ^ v) h := by
    intro t
    rw [← two_pow_succ' v, difs_two_pow, two_pow_succ' v]
    show xor (h (t + 2 * 2 ^ v)) (h t) = false
    rw [hper t]
    cases h t <;> rfl
  have hpast := difs_past_gate hq hs hb hh (2 ^ v - 2)
  rw [show 2 ^ v - 2 + 1 + 1 + 2 ^ v = 2 * 2 ^ v by omega,
    show 2 ^ v - 2 + 1 = 2 ^ v - 1 by omega] at hpast
  apply (le_order_iff (g := s) (L := 2 ^ v) (r := 1) (by omega) (by omega)).mpr
  intro t
  have := hvan t
  rw [hpast] at this
  exact this

/-- **The exact countdown.** For a quadratic gate, if `h` keeps the period `2 * M` and `s` is below the largest
order, the order drops by exactly one: `order h (2 M) + 1 = order s M`. -/
theorem order_countdown_exact {g : Bool → Bool → Bool} {s b h : Nat → Bool} {v : Nat} (hq : Quadratic g)
    (hv : 1 ≤ v) (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (g (b t) (s t)))
    (hper : ∀ t, h (t + 2 * 2 ^ v) = h t) (hlt : order s (2 ^ v) + 1 < 2 ^ v) :
    order h (2 * 2 ^ v) + 1 = order s (2 ^ v) := by
  have hM := two_le_two_pow hv
  apply Nat.le_antisymm _ (order_countdown_gate hs hb hh)
  -- `h` does not vanish at `M + 1`, else `s` would vanish at `1` and have the largest order.
  have hr : order h (2 * 2 ^ v) ≤ 2 ^ v - 2 := by
    apply Nat.le_of_not_lt
    intro hgt
    have hvh := (le_order_iff (g := h) (L := 2 * 2 ^ v) (r := 2 ^ v - 1) (by omega) (by omega)).mp
      (by omega)
    have hpast := difs_past_gate hq hs hb hh 0
    have h1 : Vanish (2 ^ v - (2 ^ v - 1)) s := by
      intro t
      have := (hvh.mono (m := 0 + 1 + 1 + 2 ^ v) (by omega)) t
      rw [hpast] at this
      rw [show 2 ^ v - (2 ^ v - 1) = 0 + 1 by omega]
      exact this
    have := (le_order_iff (g := s) (L := 2 ^ v) (r := 2 ^ v - 1) (by omega) (by omega)).mpr h1
    omega
  rcases Nat.eq_zero_or_pos (order h (2 * 2 ^ v)) with h0 | hpos
  · rw [h0]; exact order_pos_of_period hq hv hs hb hh hper
  · have hvan := (le_order_iff (g := h) (L := 2 * 2 ^ v) (r := order h (2 * 2 ^ v)) hpos
      (order_le h _)).mp (Nat.le_refl _)
    have hpast := difs_past_gate hq hs hb hh (2 ^ v - order h (2 * 2 ^ v) - 2)
    rw [show 2 ^ v - order h (2 * 2 ^ v) - 2 + 1 + 1 + 2 ^ v = 2 * 2 ^ v - order h (2 * 2 ^ v) by omega,
      show 2 ^ v - order h (2 * 2 ^ v) - 2 + 1 = 2 ^ v - (order h (2 * 2 ^ v) + 1) by omega] at hpast
    apply (le_order_iff (g := s) (L := 2 ^ v) (r := order h (2 * 2 ^ v) + 1) (by omega) (by omega)).mpr
    intro t
    have := hvan t
    rw [hpast] at this
    exact this

/-! ### The closing law for prefix-doubling flags -/

/-- Column `i` keeps the prefix period of every later prefix. -/
theorem col_period (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i k : Nat} (hik : i ≤ k) (t : Nat) :
    col g x i (t + 2 ^ prefixExp g x k) = col g x i t :=
  (prefix_period_iff g x k _).mpr (Nat.dvd_refl _) i hik t

theorem col_step' (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (k t : Nat) :
    col g x (k + 1 + 1) (t + 1) = xor (col g x (k + 1 + 1) t) (g (k + 1) (col g x (k + 1) t) (col g x k t)) := by
  rw [col_step g x (k + 1) t]
  rfl

/-- Along a doubling followed by `10` pairs, the exponent rises by one per pair and the order of the pair's first
column falls by exactly one per pair. -/
theorem closing_run (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (hq : ∀ j, Quadratic (g j)) {n m : Nat}
    (h1 : prefixExp g x (n + 1) = prefixExp g x n + 1)
    (hpair : ∀ i, i < m → prefixExp g x (n + 1 + 2 * i + 1) = prefixExp g x (n + 1 + 2 * i) + 1 ∧
      prefixExp g x (n + 1 + 2 * i + 1 + 1) = prefixExp g x (n + 1 + 2 * i + 1)) :
    ∀ i, i ≤ m → prefixExp g x (n + 1 + 2 * i) = prefixExp g x n + 1 + i ∧
      order (col g x (n + 1 + 2 * i)) (2 ^ prefixExp g x (n + 1 + 2 * i)) + i = 2 ^ prefixExp g x n - 1
  | 0, _ => by
    refine ⟨by simpa using h1, ?_⟩
    have hanti : ∀ t, col g x (n + 1) (t + 2 ^ prefixExp g x n) = !col g x (n + 1) t :=
      col_antiperiod g x h1
    have := order_of_antiperiod hanti
    simp only [Nat.mul_zero, Nat.add_zero]
    rw [h1, two_pow_succ', this]
  | i + 1, hi => by
    obtain ⟨hE, hR⟩ := closing_run g x hq h1 hpair i (by omega)
    obtain ⟨hd, hk⟩ := hpair i (by omega)
    have e2 : n + 1 + 2 * (i + 1) = n + 1 + 2 * i + 1 + 1 := by omega
    rw [e2]
    have hP : prefixExp g x (n + 1 + 2 * i + 1 + 1) = prefixExp g x (n + 1 + 2 * i) + 1 := by rw [hk, hd]
    refine ⟨by rw [hP, hE]; omega, ?_⟩
    have hv : 1 ≤ prefixExp g x (n + 1 + 2 * i) := by rw [hE]; omega
    have hs := col_period g x (Nat.le_refl (n + 1 + 2 * i))
    have hb := col_antiperiod g x hd
    have hh := col_step' g x (n + 1 + 2 * i)
    have hper : ∀ t, col g x (n + 1 + 2 * i + 1 + 1) (t + 2 * 2 ^ prefixExp g x (n + 1 + 2 * i)) =
        col g x (n + 1 + 2 * i + 1 + 1) t := by
      intro t
      have := col_period g x (Nat.le_refl (n + 1 + 2 * i + 1 + 1)) t
      rwa [hP, two_pow_succ'] at this
    have hlt : order (col g x (n + 1 + 2 * i)) (2 ^ prefixExp g x (n + 1 + 2 * i)) + 1 <
        2 ^ prefixExp g x (n + 1 + 2 * i) := by
      have h2 : 2 ^ prefixExp g x n < 2 ^ prefixExp g x (n + 1 + 2 * i) :=
        Nat.pow_lt_pow_right (by decide) (by rw [hE]; omega)
      have := Nat.one_le_two_pow (n := prefixExp g x n)
      omega
    have hc := order_countdown_exact (hq (n + 1 + 2 * i + 1)) hv hs hb hh hper hlt
    rw [hP, two_pow_succ']
    omega

/-- **The closing law.** After a doubling at prefix exponent `E` (period `q0 = 2 ^ E`), a run of `m` pairs `10` and a
doubling, `m + 1 ≤ q0`, and the next column doubles iff `m + 1 = q0`. For quadratic gates, including Rule 30's OR. -/
theorem closing_law (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (hq : ∀ j, Quadratic (g j)) {n m : Nat}
    (h1 : prefixExp g x (n + 1) = prefixExp g x n + 1)
    (hpair : ∀ i, i < m → prefixExp g x (n + 1 + 2 * i + 1) = prefixExp g x (n + 1 + 2 * i) + 1 ∧
      prefixExp g x (n + 1 + 2 * i + 1 + 1) = prefixExp g x (n + 1 + 2 * i + 1))
    (hlast : prefixExp g x (n + 1 + 2 * m + 1) = prefixExp g x (n + 1 + 2 * m) + 1) :
    m + 1 ≤ 2 ^ prefixExp g x n ∧
      (prefixExp g x (n + 1 + 2 * m + 1 + 1) = prefixExp g x (n + 1 + 2 * m + 1) + 1 ↔
        m + 1 = 2 ^ prefixExp g x n) := by
  obtain ⟨hE, hR⟩ := closing_run g x hq h1 hpair m (Nat.le_refl m)
  have hpos := Nat.one_le_two_pow (n := prefixExp g x n)
  refine ⟨by omega, ?_⟩
  have hv : 1 ≤ prefixExp g x (n + 1 + 2 * m) := by rw [hE]; omega
  have hs := col_period g x (Nat.le_refl (n + 1 + 2 * m))
  have hb := col_antiperiod g x hlast
  have hh := col_step' g x (n + 1 + 2 * m)
  constructor
  · intro hd
    have hanti : ∀ t, col g x (n + 1 + 2 * m + 1 + 1) (t + 2 * 2 ^ prefixExp g x (n + 1 + 2 * m)) =
        !col g x (n + 1 + 2 * m + 1 + 1) t := by
      intro t
      have := col_antiperiod g x hd t
      rwa [hlast, two_pow_succ'] at this
    have h0 := order_reset_before_gate hs hb hh hanti
    omega
  · intro heq
    rcases prefixExp_succ_cases g x (n + 1 + 2 * m + 1) with hk | hd
    · exfalso
      have hper : ∀ t, col g x (n + 1 + 2 * m + 1 + 1) (t + 2 * 2 ^ prefixExp g x (n + 1 + 2 * m)) =
          col g x (n + 1 + 2 * m + 1 + 1) t := by
        intro t
        have := col_period g x (Nat.le_refl (n + 1 + 2 * m + 1 + 1)) t
        rwa [hk, hlast, two_pow_succ'] at this
      have := order_pos_of_period (hq (n + 1 + 2 * m + 1)) hv hs hb hh hper
      omega
    · exact hd

/-- A closing length is one less than a power of two, and `1 (10)^2 1 1` never occurs: three is not a power of two. -/
theorem no_1101011 (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (hq : ∀ j, Quadratic (g j)) {n : Nat}
    (h1 : prefixExp g x (n + 1) = prefixExp g x n + 1)
    (hpair : ∀ i, i < 2 → prefixExp g x (n + 1 + 2 * i + 1) = prefixExp g x (n + 1 + 2 * i) + 1 ∧
      prefixExp g x (n + 1 + 2 * i + 1 + 1) = prefixExp g x (n + 1 + 2 * i + 1))
    (hlast : prefixExp g x (n + 1 + 2 * 2 + 1) = prefixExp g x (n + 1 + 2 * 2) + 1) :
    prefixExp g x (n + 1 + 2 * 2 + 1 + 1) = prefixExp g x (n + 1 + 2 * 2 + 1) := by
  have hc := closing_law g x hq h1 hpair hlast
  rcases prefixExp_succ_cases g x (n + 1 + 2 * 2 + 1) with hk | hd
  · exact hk
  · exfalso
    have h3 := hc.2.mp hd
    rcases Nat.lt_or_ge (prefixExp g x n) 2 with hE | hE
    · have h01 : prefixExp g x n = 0 ∨ prefixExp g x n = 1 := by omega
      rcases h01 with h | h <;> rw [h] at h3 <;> exact absurd h3 (by decide)
    · have h4 : 2 ^ 2 ≤ 2 ^ prefixExp g x n := Nat.pow_le_pow_right (by decide) hE
      have : (2 : Nat) ^ 2 = 4 := rfl
      omega

/-- The OR gate is quadratic. -/
theorem quadratic_or : Quadratic (fun b s => b || s) := by
  unfold Quadratic deriv; decide

/-- No three consecutive doublings once the prefix period is at least `2` (the `m = 0` case). -/
theorem no_three_at (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (hq : ∀ j, Quadratic (g j)) {p : Nat}
    (hE : 1 ≤ prefixExp g x p) :
    prefixExp g x (p + 1) = prefixExp g x p ∨ prefixExp g x (p + 2) = prefixExp g x (p + 1) ∨
      prefixExp g x (p + 3) = prefixExp g x (p + 2) := by
  rcases prefixExp_succ_cases g x p with h0 | h1
  · exact Or.inl h0
  rcases prefixExp_succ_cases g x (p + 1) with h0' | h2
  · exact Or.inr (Or.inl h0')
  have hc := closing_law g x hq (n := p) (m := 0) h1 (fun i hi => absurd hi (Nat.not_lt_zero i))
    (by rw [show p + 1 + 2 * 0 + 1 = p + 1 + 1 by omega, show p + 1 + 2 * 0 = p + 1 by omega]; exact h2)
  rw [show p + 1 + 2 * 0 + 1 + 1 = p + 3 by omega, show p + 1 + 2 * 0 + 1 = p + 2 by omega] at hc
  have hpow : 1 < 2 ^ prefixExp g x p := Nat.one_lt_two_pow (by omega)
  rcases prefixExp_succ_cases g x (p + 2) with h0'' | h3
  · exact Or.inr (Or.inr h0'')
  · have := hc.2.mp h3; omega

/-- `11011` needs prefix period `2` before it (the `m = 1` case). -/
theorem no_11011_at (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (hq : ∀ j, Quadratic (g j)) {p : Nat}
    (hE : 2 ≤ prefixExp g x p) :
    prefixExp g x (p + 1) = prefixExp g x p ∨ prefixExp g x (p + 2) = prefixExp g x (p + 1) ∨
      prefixExp g x (p + 3) = prefixExp g x (p + 2) + 1 ∨ prefixExp g x (p + 4) = prefixExp g x (p + 3) ∨
      prefixExp g x (p + 5) = prefixExp g x (p + 4) := by
  rcases prefixExp_succ_cases g x p with h0 | h1
  · exact Or.inl h0
  rcases prefixExp_succ_cases g x (p + 1) with h0 | h2
  · exact Or.inr (Or.inl h0)
  rcases prefixExp_succ_cases g x (p + 2) with h3 | h3'
  · rcases prefixExp_succ_cases g x (p + 3) with h0 | h4
    · exact Or.inr (Or.inr (Or.inr (Or.inl h0)))
    have hpair : ∀ i, i < 1 → prefixExp g x (p + 1 + 2 * i + 1) = prefixExp g x (p + 1 + 2 * i) + 1 ∧
        prefixExp g x (p + 1 + 2 * i + 1 + 1) = prefixExp g x (p + 1 + 2 * i + 1) := by
      intro i hi
      have hi0 : i = 0 := by omega
      subst hi0
      exact ⟨h2, h3⟩
    have hc := closing_law g x hq (n := p) (m := 1) h1 hpair
      (by rw [show p + 1 + 2 * 1 + 1 = p + 3 + 1 by omega, show p + 1 + 2 * 1 = p + 3 by omega]; exact h4)
    rw [show p + 1 + 2 * 1 + 1 + 1 = p + 5 by omega, show p + 1 + 2 * 1 + 1 = p + 4 by omega] at hc
    have hpow : 2 ^ 2 ≤ 2 ^ prefixExp g x p := Nat.pow_le_pow_right (by decide) hE
    have h4' : (2 : Nat) ^ 2 = 4 := rfl
    rcases prefixExp_succ_cases g x (p + 4) with h0 | h5
    · exact Or.inr (Or.inr (Or.inr (Or.inr h0)))
    · have := hc.2.mp h5; omega
  · exact Or.inr (Or.inr (Or.inl h3'))

/-- **Five letters, at most three doublings** (GC2007's bound). Once the prefix period is at least `4`, any five
consecutive columns raise the exponent by at most `3`, for every quadratic gate family. -/
theorem five_letter (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (hq : ∀ j, Quadratic (g j)) {n : Nat}
    (hE : 2 ≤ prefixExp g x n) :
    prefixExp g x (n + 5) ≤ prefixExp g x n + 3 := by
  have c0 := prefixExp_succ_cases g x n
  have c1 := prefixExp_succ_cases g x (n + 1)
  have c2 := prefixExp_succ_cases g x (n + 2)
  have c3 := prefixExp_succ_cases g x (n + 3)
  have c4 := prefixExp_succ_cases g x (n + 4)
  simp only [Nat.add_assoc, Nat.reduceAdd] at c1 c2 c3 c4
  have e1 : 1 ≤ prefixExp g x (n + 1) := by rcases c0 with h | h <;> omega
  have e2 : 1 ≤ prefixExp g x (n + 2) := by rcases c1 with h | h <;> omega
  have t0 := no_three_at g x hq (p := n) (by omega)
  have t1 := no_three_at g x hq (p := n + 1) e1
  have t2 := no_three_at g x hq (p := n + 2) e2
  have f0 := no_11011_at g x hq (p := n) hE
  simp only [Nat.add_assoc, Nat.reduceAdd] at t1 t2
  rcases c0 with h0 | h0 <;> rcases c1 with h1 | h1 <;> rcases c2 with h2 | h2 <;> rcases c3 with h3 | h3 <;>
    rcases c4 with h4 | h4 <;>
    first
    | omega
    | (rcases t0 with h | h | h <;> omega)
    | (rcases t1 with h | h | h <;> omega)
    | (rcases t2 with h | h | h <;> omega)
    | (rcases f0 with h | h | h | h | h <;> omega)

/-- Rule 30's right edge: the closing law for the OR family. -/
theorem closing_law_or (x : Nat → Bool) {n m : Nat}
    (h1 : prefixExp (fun _ b s => b || s) x (n + 1) = prefixExp (fun _ b s => b || s) x n + 1)
    (hpair : ∀ i, i < m →
      prefixExp (fun _ b s => b || s) x (n + 1 + 2 * i + 1) = prefixExp (fun _ b s => b || s) x (n + 1 + 2 * i) + 1 ∧
      prefixExp (fun _ b s => b || s) x (n + 1 + 2 * i + 1 + 1) = prefixExp (fun _ b s => b || s) x (n + 1 + 2 * i + 1))
    (hlast : prefixExp (fun _ b s => b || s) x (n + 1 + 2 * m + 1) =
      prefixExp (fun _ b s => b || s) x (n + 1 + 2 * m) + 1) :
    m + 1 ≤ 2 ^ prefixExp (fun _ b s => b || s) x n ∧
      (prefixExp (fun _ b s => b || s) x (n + 1 + 2 * m + 1 + 1) =
          prefixExp (fun _ b s => b || s) x (n + 1 + 2 * m + 1) + 1 ↔
        m + 1 = 2 ^ prefixExp (fun _ b s => b || s) x n) :=
  closing_law _ x (fun _ => quadratic_or) h1 hpair hlast

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The five headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30GateClocks", "Ruliology.CellularAutomata.Rule30DifferenceOrder"};
heads = {"order_countdown_exact", "closing_law", "closing_law_or", "no_1101011", "five_letter"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The quadratic condition on a gate, as defined in the module:

```wl
show[{"Quadratic"}, "TermForm"]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it
resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.closing_law"]["KernelCheck"]
```
