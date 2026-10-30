import Ruliology.CellularAutomata.Rule30Prize

/-!
# Nested record thresholds for every two-input gate clock

Package A (`R30-20261030-7b0d12`) proved, for every family of two-input gates `g j` and every seed, that the first
`n` bits of the edge map `x_j(t+1) = x_j(t) xor g j (x_(j-1)(t)) (x_(j-2)(t))` have period `2 ^ prefixExp g x n`
with `prefixExp g x (2 * m) ≤ m + Q 0 m`, the kit's record-charge bound. That bound allows the excess
`prefixExp g x (2 * m) - m` to reach 3 at pair-count 19. Here it is shown not to reach 3 before 2058.

* `prefixExp_le_add_two`: for every gate family and seed, `prefixExp g x (2 * m) ≤ m + 2` for all `m < 2058`.
* `first_excess_three`: a first visit to excess 3 at pair-count `N` forces `N ≥ 2058`.
* `no_three`: no three consecutive doublings once the prefix period is at least 2, for every gate.
* `after01_double_iff`: after a pair whose first bit keeps the period `P ≥ 2` and whose second doubles, the next
  bit doubles iff the gate's quadratic coefficient is 1 and the first bit has odd weight over `P`.
* `after11_order`: after two doublings from period `M = 2 ^ e ≥ 4`, the next bit has order at least `M - 2` at
  length `4 M`.

Why: excess increases only at `11` pairs, and `00` pairs lower it. The last-visit selection isolates an interval of
constant excess 2 between two bounding `11` pairs: take the stretch after the last visit to excess 1 before a first
visit to excess 3. It begins with two doublings, which `no_three` forces to be followed by a pair doubling only its
second bit. The first bit's order then starts at least `M - 2` (`after11_order`) and must count down to 0, at most
one per pair (`order_countdown_gate`, `after01_double_iff`), before a first bit can double again. After the last
such pair, the last bit's resource is half its period minus one (`order_of_antiperiod`) and must count down to 0
(`order_countdown_gate`, `order_reset_before_gate`). The two countdowns cost at least `2058` pairs in all. The
last-visit argument was found independently by Claude and GPT (OpenAI) in the shared research record.

The file contains Package A unchanged, with its copies of the kit's `Rule30RecordCharge` and
`Rule30DifferenceOrder`, which the portal verifier's kit predates; only `Rule30Prize` is imported. Nothing is claimed
about the centre column of Rule 30 or the Prize problems, about excess 3 being attained, or about thresholds beyond
the first. Package A's own statement:

The right edge of Rule 30 read in the frame moving with it is the 2-adic map
`x_j ↦ x_j xor (x_(j-1) || x_(j-2))`. The kit proves that its prefix periods grow at half rate
(`Rule30RightPeriods.per_upper_half`), by a difference identity (`Rule30DifferenceOrder`) and a
gate-free resource count (`Rule30RecordCharge.Path`). This file replaces `||` by an arbitrary gate.

For any family of gates `g j : Bool → Bool → Bool`, one for each depth, and any seed
`x : Nat → Bool`, let bit `j` evolve by `x_j(t+1) = x_j(t) xor g j (x_(j-1)(t)) (x_(j-2)(t))`, with
missing bits white. Let `prefixExp g x n` be the exponent of the least period of the first `n` bits.

* `prefix_period_iff`: `P` is a period of the first `n` bits iff `2 ^ prefixExp g x n` divides `P`.
* `prefix_window_bound`: `prefixExp (a + 2m) - prefixExp a ≤ m + Q (prefixExp a) m ≤ m + Q 0 m`,
  for every window, with the kit's thresholds and their inverse `Q`.
* `prefixExp_le_B`: the first `n` bits have period dividing `2 ^ B n`, `B n = ⌈n/2⌉ + Q 0 ⌊n/2⌋`.
* `affine_prefix_bound`: if every gate is affine, the first `n` bits have period dividing `2 ^ r`
  whenever `n + 1 ≤ 2 ^ r`.

Why it works for every gate: the derivative `g true s xor g false s` of a gate in its newer input
is constant, `s` or `!s`, so one more difference removes it (`vanish_comp`, `vanish_past_gate`).
The kit's reset and countdown laws (`order_reset_before`, `order_countdown`) only use that, and
the record-charge count never sees the gate. The proof follows the kit's `pairPath` and the
prefix-clock organization of kit PR #55 (Lowry), with the gate as a parameter; the period lifting
is the T-function cycle structure of Klimov–Shamir (`Rule30Equivalents.TFunctionCycles`),
reproved here in core Lean. The kit modules `Rule30RecordCharge` and `Rule30DifferenceOrder` are
copied below unchanged, inside this namespace, because the portal verifier's kit predates them;
only `Rule30Prize` is imported. Nothing is claimed about the centre column of Rule 30 or the Prize
problems, and no lower bound or doubling density is asserted.
-/

namespace Rule30Submission

/-! ## Kit module `Rule30RecordCharge`, copied

Copied verbatim from the kit at `a6399ef15ff409d4dc0c5feb119b289aa31588a4`,
`lean/Ruliology/CellularAutomata/Rule30RecordCharge.lean` (SHA256 `ce3fa36b5f961f39ee6fc7e6df1230be67080127165fb1ae924ea670f805c96c`), with only its namespace
moved inside `Rule30Submission`. The portal verifier's kit `19540bf` does not contain it. Its own
documentation follows. -/

namespace Rule30RecordCharge

/-!
# Record charges: the bookkeeping behind the half-rate period bound

This module is pure arithmetic on natural numbers. It is the accounting half of
`Rule30RightPeriods.per_upper_half`; the Rule 30 input is supplied there.

A *path* (`Path nu`) is a walk `i = 0, 1, 2, …` whose exponent grows by a weight `0`, `1` or `2`
at each step, together with a resource that must satisfy three laws:

* `reset_before`: the resource is `0` just before a weight-`2` step;
* `reset_after`: just after a weight-`2` step it is `2 ^ (nu + exponent - 1) - 1`;
* `countdown`: a weight-`1` step lowers it by at most `1`.

Weight-`0` steps lower the exponent's excess `exponent i - i`; weight-`2` steps raise it, but each
one needs the resource to have run down to `0`, and after a step that lands at excess `q + 1`
the resource is exponentially large. So the excess can only reach `q + 1` after a time
`threshold nu q`, with `threshold nu 0 = 1` and
`threshold nu (q + 1) = threshold nu q + 2 ^ (nu + threshold nu q + q)`
(`record_potential`, `record_time_lower_bound`). Conversely, before time `threshold nu q` the
exponent is at most `i + q` (`exponent_bound_before_threshold`).

`Q nu d` is the least `q` with `d < threshold nu q` (`Q_spec`, `threshold_le_of_lt_Q`), computed
by counting (`countBelow`), and `B j = ⌈j / 2⌉ + Q 0 ⌊j / 2⌋`. The thresholds grow like a tower of
twos (`threshold_tower_step`): `threshold 0` is `1, 3, 19, 2^21 + 19, …`, so `Q 0 d ≤ 3` for
`d ≤ 2^21 + 18` and `Q 0 d` grows like the iterated logarithm `log* d`.
-/

/-! ### Counting an initial run -/

/-- The number of `k < n` with `p k`. -/
def countBelow (p : Nat → Prop) [DecidablePred p] : Nat → Nat
  | 0 => 0
  | n + 1 => countBelow p n + if p n then 1 else 0

theorem countBelow_le (p : Nat → Prop) [DecidablePred p] : ∀ n, countBelow p n ≤ n
  | 0 => Nat.le_refl 0
  | n + 1 => by
    have := countBelow_le p n
    simp only [countBelow]
    split <;> omega

theorem countBelow_all (p : Nat → Prop) [DecidablePred p] :
    ∀ n, (∀ k, k < n → p k) → countBelow p n = n
  | 0, _ => rfl
  | n + 1, h => by
    have hn := h n (Nat.lt_succ_self n)
    simp only [countBelow, hn, ite_true, countBelow_all p n (fun k hk => h k (by omega))]

theorem down_closed {p : Nat → Prop} (hp : ∀ k, p (k + 1) → p k) :
    ∀ n, p n → ∀ k, k ≤ n → p k
  | 0, h, k, hk => by rw [Nat.le_zero.mp hk]; exact h
  | n + 1, h, k, hk => by
    rcases Nat.lt_or_eq_of_le hk with hk | hk
    · exact down_closed hp n (hp n h) k (by omega)
    · rw [hk]; exact h

/-- For a predicate closed downwards, `countBelow p n` is the length of its initial run, cut at
`n`. -/
theorem le_countBelow_iff {p : Nat → Prop} [DecidablePred p] (hp : ∀ k, p (k + 1) → p k) :
    ∀ n r, r ≤ n → (r ≤ countBelow p n ↔ ∀ k, k < r → p k)
  | 0, r, hr => by
    have hr0 : r = 0 := by omega
    subst hr0
    exact ⟨fun _ k hk => absurd hk (Nat.not_lt_zero k), fun _ => Nat.zero_le _⟩
  | n + 1, r, hr => by
    by_cases hn : p n
    · rw [countBelow_all p (n + 1) (fun k hk => down_closed hp n hn k (by omega))]
      exact ⟨fun _ k hk => down_closed hp n hn k (by omega), fun _ => hr⟩
    · have hc : countBelow p (n + 1) = countBelow p n := by
        simp only [countBelow, hn, ite_false, Nat.add_zero]
      rw [hc]
      rcases Nat.lt_or_eq_of_le hr with hr | hr
      · exact le_countBelow_iff hp n r (by omega)
      · subst hr
        have := countBelow_le p n
        exact ⟨fun h => absurd h (by omega), fun h => absurd (h n (by omega)) hn⟩

theorem lt_countBelow_iff {p : Nat → Prop} [DecidablePred p] (hp : ∀ k, p (k + 1) → p k)
    {n r : Nat} (hr : r < n) : r < countBelow p n ↔ p r := by
  rw [← Nat.succ_le_iff, le_countBelow_iff hp n (r + 1) hr]
  exact ⟨fun h => h r (Nat.lt_succ_self r),
    fun h k hk => down_closed hp r h k (by omega)⟩

/-! ### Thresholds and paths -/

/-- `threshold nu q` is the earliest time at which the excess `exponent - time` can exceed `q`. -/
def threshold (nu : Nat) : Nat → Nat
  | 0 => 1
  | q + 1 => threshold nu q + 2 ^ (nu + threshold nu q + q)

theorem threshold_step_le (nu q : Nat) : threshold nu q ≤ threshold nu (q + 1) :=
  Nat.le_add_right _ _

theorem threshold_strict (nu q : Nat) : threshold nu q < threshold nu (q + 1) := by
  have hp := Nat.two_pow_pos (nu + threshold nu q + q)
  simp only [threshold]
  omega

theorem threshold_ge (nu q : Nat) : q + 1 ≤ threshold nu q := by
  induction q with
  | zero => exact Nat.le_refl 1
  | succ q ih => have := threshold_strict nu q; omega

theorem threshold_mono (nu : Nat) {a b : Nat} (h : a ≤ b) : threshold nu a ≤ threshold nu b := by
  induction b with
  | zero => rw [Nat.le_zero.mp h]; exact Nat.le_refl _
  | succ b ih =>
    rcases Nat.lt_or_eq_of_le h with h | h
    · exact Nat.le_trans (ih (by omega)) (threshold_step_le nu b)
    · rw [h]; exact Nat.le_refl _

/-- The thresholds grow at least like a tower of twos. -/
theorem threshold_tower_step (nu q : Nat) : 2 ^ (threshold nu q) ≤ threshold nu (q + 1) := by
  have hp := Nat.pow_le_pow_right (n := 2) (by decide)
    (show threshold nu q ≤ nu + threshold nu q + q by omega)
  simp only [threshold]
  omega

/-- A walk with step weights `0`, `1`, `2` and a resource obeying the reset and countdown laws. -/
structure Path (nu : Nat) where
  weight : Nat → Nat
  exponent : Nat → Nat
  resource : Nat → Nat
  exponent_zero : exponent 0 = 0
  exponent_step : ∀ i, exponent (i + 1) = exponent i + weight i
  weight_le_two : ∀ i, weight i ≤ 2
  reset_before : ∀ i, weight i = 2 → resource i = 0
  reset_after : ∀ i, weight i = 2 → resource (i + 1) + 1 = 2 ^ (nu + exponent (i + 1) - 1)
  countdown : ∀ i, weight i = 1 → resource i ≤ resource (i + 1) + 1

/-- The invariant: an excess of `q + 1` at time `i` has paid the time `threshold nu q`, and time
plus remaining resource has paid `threshold nu (q + 1) - 1`. -/
theorem record_potential {nu : Nat} (p : Path nu) :
    ∀ i q, i + q + 1 ≤ p.exponent i →
      threshold nu q ≤ i ∧ threshold nu (q + 1) ≤ i + p.resource i + 1 := by
  intro i
  induction i with
  | zero =>
    intro q h
    have hz := p.exponent_zero
    omega
  | succ i ih =>
    intro q h
    have he := p.exponent_step i
    have hk := p.weight_le_two i
    have cases : p.weight i = 0 ∨ p.weight i = 1 ∨ p.weight i = 2 := by omega
    rcases cases with h0 | h1 | h2
    · have old := ih (q + 1) (by omega)
      have mono := threshold_step_le nu q
      constructor <;> omega
    · have old := ih q (by omega)
      have drop := p.countdown i h1
      constructor <;> omega
    · have before := p.reset_before i h2
      have after := p.reset_after i h2
      have paid : threshold nu q ≤ i + 1 := by
        cases q with
        | zero => simp only [threshold]; omega
        | succ q =>
          have old := ih q (by omega)
          omega
      refine ⟨paid, ?_⟩
      have exp_le : nu + threshold nu q + q ≤ nu + p.exponent (i + 1) - 1 := by omega
      have pow_le := Nat.pow_le_pow_right (n := 2) (by decide) exp_le
      simp only [threshold]
      omega

/-- An excess of `q + 1` is reached no earlier than `threshold nu q`. -/
theorem record_time_lower_bound {nu : Nat} (p : Path nu) (i q : Nat)
    (h : i + q + 1 ≤ p.exponent i) : threshold nu q ≤ i :=
  (record_potential p i q h).1

/-- Before time `threshold nu q` the exponent is at most `i + q`. -/
theorem exponent_bound_before_threshold {nu : Nat} (p : Path nu) (i q : Nat)
    (h : i < threshold nu q) : p.exponent i ≤ i + q := by
  have hnot : ¬ i + q + 1 ≤ p.exponent i := by
    intro hc
    have := record_time_lower_bound p i q hc
    omega
  omega

/-! ### The inverse of the thresholds -/

/-- The least `q` with `d < threshold nu q`: the number of `q < d` with `threshold nu q ≤ d`. -/
def Q (nu d : Nat) : Nat := countBelow (fun q => threshold nu q ≤ d) d

theorem threshold_down (nu d : Nat) :
    ∀ k, threshold nu (k + 1) ≤ d → threshold nu k ≤ d :=
  fun k h => Nat.le_trans (threshold_step_le nu k) h

theorem Q_le (nu d : Nat) : Q nu d ≤ d := countBelow_le _ d

theorem Q_spec (nu d : Nat) : d < threshold nu (Q nu d) := by
  rcases Nat.lt_or_eq_of_le (Q_le nu d) with h | h
  · have hiff := lt_countBelow_iff (p := fun q => threshold nu q ≤ d) (threshold_down nu d) h
    have hn : ¬ threshold nu (Q nu d) ≤ d := fun hq => Nat.lt_irrefl _ (hiff.mpr hq)
    omega
  · rw [h]; have := threshold_ge nu d; omega

theorem threshold_le_of_lt_Q {nu d q : Nat} (hq : q < Q nu d) : threshold nu q ≤ d :=
  (lt_countBelow_iff (p := fun q => threshold nu q ≤ d) (threshold_down nu d) (Nat.lt_of_lt_of_le hq (Q_le nu d))).mp hq

/-- `Q nu d` is exactly the least `q` with `d < threshold nu q`. -/
theorem Q_le_iff (nu d q : Nat) : Q nu d ≤ q ↔ d < threshold nu q := by
  constructor
  · intro h
    exact Nat.lt_of_lt_of_le (Q_spec nu d) (threshold_mono nu h)
  · intro h
    apply Nat.le_of_not_lt
    intro hq
    have := threshold_le_of_lt_Q hq
    omega

theorem Q_zero (nu : Nat) : Q nu 0 = 0 := rfl

/-- The exponent `⌈j / 2⌉ + Q 0 ⌊j / 2⌋` of `Rule30RightPeriods.per_upper_half`. -/
def B (j : Nat) : Nat := (j + 1) / 2 + Q 0 (j / 2)

theorem B_zero : B 0 = 0 := rfl
theorem B_one : B 1 = 1 := rfl

theorem threshold_zero_two : threshold 0 2 = 19 := by decide
theorem threshold_zero_three : threshold 0 3 = 2 ^ 21 + 19 := by decide

theorem pow_le_threshold (nu : Nat) : ∀ q, 2 ^ q ≤ threshold nu q
  | 0 => Nat.le_refl 1
  | q + 1 => by
    have ht := threshold_ge nu q
    have hp := Nat.pow_le_pow_right (n := 2) (by decide)
      (show q + 1 ≤ nu + threshold nu q + q by omega)
    simp only [threshold]
    omega

theorem twelve_mul_le_two_pow : ∀ n, 7 ≤ n → 12 * (n + 1) ≤ 2 ^ n
  | 0, h | 1, h | 2, h | 3, h | 4, h | 5, h | 6, h => absurd h (by decide)
  | 7, _ => by decide
  | n + 8, _ => by
    have := twelve_mul_le_two_pow (n + 7) (by omega)
    rw [Nat.pow_succ]
    omega

/-- Past the third record, `Q 0 d` is tiny compared with `d`. -/
theorem twelve_mul_Q_le {d : Nat} (hd : 2 ^ 21 ≤ d) : 12 * Q 0 d ≤ d := by
  have h21 : (2 : Nat) ^ 21 = 2097152 := by decide
  by_cases hQ : Q 0 d ≤ 8
  · omega
  · have ht := threshold_le_of_lt_Q (show Q 0 d - 1 < Q 0 d by omega)
    have hp := pow_le_threshold 0 (Q 0 d - 1)
    have hw := twelve_mul_le_two_pow (Q 0 d - 1) (by omega)
    rw [show Q 0 d - 1 + 1 = Q 0 d by omega] at hw
    omega

/-- For `j / 2 ≤ 2 ^ 21 + 18`, `B j ≤ ⌈j / 2⌉ + 3`. -/
theorem B_le_add_three {j : Nat} (hj : j / 2 ≤ 2 ^ 21 + 18) : B j ≤ (j + 1) / 2 + 3 := by
  have h : Q 0 (j / 2) ≤ 3 := (Q_le_iff 0 (j / 2) 3).mpr (by rw [threshold_zero_three]; omega)
  unfold B
  omega

/-- `B j < (2 j + 1) / 3` for every `j ≥ 18`: `B` beats the exponent of
`Rule30RightPeriods.per_upper` from there on (at `j = 17` both are `11`). -/
theorem B_lt_two_thirds {j : Nat} (hj : 18 ≤ j) : B j < (2 * j + 1) / 3 := by
  have h21 : (2 : Nat) ^ 21 = 2097152 := by decide
  unfold B
  by_cases h2 : j / 2 < 19
  · have : Q 0 (j / 2) ≤ 2 := (Q_le_iff 0 (j / 2) 2).mpr (by rw [threshold_zero_two]; omega)
    omega
  · by_cases h3 : j / 2 < 2 ^ 21 + 19
    · have : Q 0 (j / 2) ≤ 3 :=
        (Q_le_iff 0 (j / 2) 3).mpr (by rw [threshold_zero_three]; omega)
      omega
    · have := twelve_mul_Q_le (d := j / 2) (by omega)
      omega

/-- Along a path with `nu = 0`, the exponent at time `d` is at most `d + Q 0 d`. -/
theorem exponent_le_Q (p : Path 0) (d : Nat) : p.exponent d ≤ d + Q 0 d :=
  exponent_bound_before_threshold p d (Q 0 d) (Q_spec 0 d)

end Rule30RecordCharge

/-! ## Kit module `Rule30DifferenceOrder`, copied

Copied verbatim from the kit at `a6399ef15ff409d4dc0c5feb119b289aa31588a4`,
`lean/Ruliology/CellularAutomata/Rule30DifferenceOrder.lean` (SHA256 `96f50d141b6631838fe61caf0d81a56a36bb89e171e21d3fea926cdd8f271224`), with only its namespace
moved inside `Rule30Submission`. The portal verifier's kit `19540bf` does not contain it. Its own
documentation follows. -/

namespace Rule30DifferenceOrder

/-!
# The difference order of a periodic Boolean stream

For a stream `g : Nat → Bool` write `dif g t = g (t + 1) xor g t` and `difs k g` for the `k`-th
difference. This module is the algebraic half of `Rule30RightPeriods.per_upper_half`; it says
nothing about Rule 30.

**Differences at powers of two.** `difs (2 ^ v) g t = g (t + 2 ^ v) xor g t`
(`difs_two_pow`), because squaring the difference operator over `F₂` squares the shift. So a
stream of period `2 ^ v` has `difs (2 ^ v) g = 0` (`vanish_of_period`).

**The order.** `order g L` is the largest `r ≤ L - 1` with `difs (L - r) g = 0`
(`le_order_iff`). For `L = 2 ^ v` and a stream of period `L` it is the multiplicity of the
factor `1 + z` in `∑_{t < L} g t z^t` over `F₂`, capped at `L - 1`: modulo
`z^L - 1 = (1 + z)^L` the difference operator is multiplication by `z⁻¹ (1 + z)`, and `z⁻¹` is a
unit, so it does not change that multiplicity. No polynomials are used here.

**Three laws.** Let `M = 2 ^ v`, and let `h (t + 1) = h t xor (b t || s t)` where `s` has
period `M` and `b (t + M) = !b t`. Then `difs M h` is the shifted sum `h (t + M) xor h t`, and its
difference is `!s` (`dif_shift_sum`). Hence:

* `order_of_antiperiod`: if `h (t + M) = !h t` then `order h (2 * M) = M - 1`;
* `order_reset_before`: if `h (t + 2 * M) = !h t` then `order s M = 0`;
* `order_countdown`: if `h` has period `2 * M` then `order s M ≤ order h (2 * M) + 1`.

These are the reset and countdown laws of `Rule30RecordCharge.Path`.
-/

open Rule30RecordCharge

/-- The first difference of a stream over `F₂`. -/
def dif (g : Nat → Bool) (t : Nat) : Bool := xor (g (t + 1)) (g t)

/-- The `k`-th difference. -/
def difs : Nat → (Nat → Bool) → Nat → Bool
  | 0, g => g
  | k + 1, g => dif (difs k g)

theorem difs_succ' (k : Nat) (g : Nat → Bool) : difs (k + 1) g = difs k (dif g) := by
  induction k with
  | zero => rfl
  | succ k ih => simp only [difs] at ih ⊢; rw [ih]

theorem difs_add (a b : Nat) (g : Nat → Bool) : difs (a + b) g = difs a (difs b g) := by
  induction a with
  | zero => simp only [Nat.zero_add, difs]
  | succ a ih => rw [Nat.succ_add]; simp only [difs]; rw [ih]

theorem difs_xor (k : Nat) (f g : Nat → Bool) :
    difs k (fun t => xor (f t) (g t)) = fun t => xor (difs k f t) (difs k g t) := by
  induction k with
  | zero => rfl
  | succ k ih =>
    funext t
    simp only [difs, dif, ih]
    cases difs k f (t + 1) <;> cases difs k g (t + 1) <;> cases difs k f t <;>
      cases difs k g t <;> rfl

theorem difs_shift (k c : Nat) (g : Nat → Bool) :
    difs k (fun t => g (t + c)) = fun t => difs k g (t + c) := by
  induction k with
  | zero => rfl
  | succ k ih =>
    funext t
    simp only [difs, dif, ih, Nat.add_right_comm t 1 c]

theorem difs_const (k : Nat) (c : Bool) : difs (k + 1) (fun _ => c) = fun _ => false := by
  rw [difs_succ']
  have h : dif (fun _ => c) = fun _ => false := by funext t; cases c <;> rfl
  rw [h]
  induction k with
  | zero => rfl
  | succ k ih => simp only [difs, ih]; rfl

/-- Over `F₂` the `2 ^ v`-th difference is a shift by `2 ^ v` plus the identity. -/
theorem difs_two_pow (v : Nat) (g : Nat → Bool) :
    difs (2 ^ v) g = fun t => xor (g (t + 2 ^ v)) (g t) := by
  induction v generalizing g with
  | zero => rfl
  | succ v ih =>
    rw [Nat.pow_succ, Nat.mul_two, difs_add, ih, ih]
    funext t
    simp only [Nat.add_assoc]
    cases g (t + (2 ^ v + 2 ^ v)) <;> cases g (t + 2 ^ v) <;> cases g t <;> rfl

theorem two_pow_succ' (n : Nat) : 2 ^ (n + 1) = 2 * 2 ^ n := by
  rw [Nat.pow_succ, Nat.mul_comm]

/-! ### Vanishing and the order -/

/-- The `k`-th difference is identically `false`. -/
def Vanish (k : Nat) (g : Nat → Bool) : Prop := ∀ t, difs k g t = false

theorem Vanish.succ {k : Nat} {g : Nat → Bool} (h : Vanish k g) : Vanish (k + 1) g := by
  intro t
  simp only [difs, dif, h (t + 1), h t]
  rfl

theorem Vanish.mono {k m : Nat} {g : Nat → Bool} (h : Vanish k g) (hkm : k ≤ m) : Vanish m g := by
  induction m with
  | zero => rw [Nat.le_zero.mp hkm] at h; exact h
  | succ m ih =>
    rcases Nat.lt_or_eq_of_le hkm with hlt | heq
    · exact (ih (by omega)).succ
    · rw [← heq]; exact h

theorem vanish_of_period {v : Nat} {g : Nat → Bool} (h : ∀ t, g (t + 2 ^ v) = g t) :
    Vanish (2 ^ v) g := by
  intro t
  rw [difs_two_pow]
  show xor (g (t + 2 ^ v)) (g t) = false
  rw [h t]
  cases g t <;> rfl

open Classical in
/-- The largest `r ≤ L - 1` with `Vanish (L - r) g`: the number of `k < L - 1` with
`Vanish (L - 1 - k) g`. -/
noncomputable def order (g : Nat → Bool) (L : Nat) : Nat :=
  countBelow (fun k => Vanish (L - 1 - k) g) (L - 1)

open Classical in
theorem order_le (g : Nat → Bool) (L : Nat) : order g L ≤ L - 1 := countBelow_le _ _

open Classical in
theorem le_order_iff {g : Nat → Bool} {L r : Nat} (hr1 : 1 ≤ r) (hr : r ≤ L - 1) :
    r ≤ order g L ↔ Vanish (L - r) g := by
  have hp : ∀ k, Vanish (L - 1 - (k + 1)) g → Vanish (L - 1 - k) g :=
    fun k h => h.mono (by omega)
  unfold order
  rw [le_countBelow_iff hp (L - 1) r hr]
  constructor
  · intro h
    have := h (r - 1) (by omega)
    rwa [show L - 1 - (r - 1) = L - r by omega] at this
  · intro h k hk
    exact h.mono (by omega)

/-! ### The three laws -/

/-- The difference of the shifted sum `h (t + M) xor h t` is `!s`. -/
theorem dif_shift_sum {s b h : Nat → Bool} {M : Nat}
    (hs : ∀ t, s (t + M) = s t) (hb : ∀ t, b (t + M) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (b t || s t)) :
    dif (fun t => xor (h (t + M)) (h t)) = fun t => !s t := by
  funext t
  simp only [dif]
  rw [Nat.add_right_comm t 1 M, hh (t + M), hh t, hs t, hb t]
  cases h (t + M) <;> cases h t <;> cases b t <;> cases s t <;> rfl

/-- Past the `M`-th difference, `h` behaves like `!s`, hence like `s`. -/
theorem difs_past {s b h : Nat → Bool} {v : Nat}
    (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (b t || s t)) (k : Nat) :
    difs (k + 1 + 1 + 2 ^ v) h = difs (k + 1) s := by
  rw [difs_add, difs_two_pow, difs_succ' (k + 1), dif_shift_sum hs hb hh]
  have hn : (fun t => !s t) = fun t => xor ((fun _ => true) t) (s t) := by
    funext t; cases s t <;> rfl
  rw [hn, difs_xor, difs_const]
  funext t
  cases difs (k + 1) s t <;> rfl

/-- A stream that a shift by `M = 2 ^ v` complements has order `M - 1` at length `2 * M`. -/
theorem order_of_antiperiod {h : Nat → Bool} {v : Nat} (hh : ∀ t, h (t + 2 ^ v) = !h t) :
    order h (2 * 2 ^ v) = 2 ^ v - 1 := by
  have hM := Nat.one_le_two_pow (n := v)
  have hconst : difs (2 ^ v) h = fun _ => true := by
    rw [difs_two_pow]; funext t; rw [hh t]; cases h t <;> rfl
  have hnot : ¬ Vanish (2 ^ v) h := fun hv => by
    have := hv 0; rw [hconst] at this; exact Bool.noConfusion this
  have hyes : Vanish (2 ^ v + 1) h := by
    intro t
    rw [Nat.add_comm, difs_add, hconst]
    rfl
  apply Nat.le_antisymm
  · apply Nat.le_of_not_lt
    intro hlt
    have := (le_order_iff (g := h) (L := 2 * 2 ^ v) (r := 2 ^ v) hM (by omega)).mp (by omega)
    rw [show 2 * 2 ^ v - 2 ^ v = 2 ^ v by omega] at this
    exact hnot this
  · rcases Nat.lt_or_ge (2 ^ v - 1) 1 with h0 | h1
    · omega
    · apply (le_order_iff h1 (by omega)).mpr
      rw [show 2 * 2 ^ v - (2 ^ v - 1) = 2 ^ v + 1 by omega]
      exact hyes

/-- Before a step whose shifted sum is complemented by a shift of `2 * M`, the order is `0`. -/
theorem order_reset_before {s b h : Nat → Bool} {v : Nat}
    (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (b t || s t))
    (hanti : ∀ t, h (t + 2 * 2 ^ v) = !h t) :
    order s (2 ^ v) = 0 := by
  cases v with
  | zero => have := order_le s (2 ^ 0); omega
  | succ v =>
    have hM : 2 ≤ 2 ^ (v + 1) := by
      rw [Nat.pow_succ]; have := Nat.one_le_two_pow (n := v); omega
    apply Nat.eq_zero_of_not_pos
    intro hpos
    have hv := (le_order_iff (g := s) (L := 2 ^ (v + 1)) (r := 1) (by omega) (by omega)).mp hpos
    have hall : difs (2 * 2 ^ (v + 1)) h = fun _ => true := by
      rw [← two_pow_succ' (v + 1), difs_two_pow]
      funext t
      rw [two_pow_succ' (v + 1), hanti t]
      cases h t <;> rfl
    have hpast := difs_past hs hb hh (2 ^ (v + 1) - 2)
    rw [show 2 ^ (v + 1) - 2 + 1 + 1 + 2 ^ (v + 1) = 2 * 2 ^ (v + 1) by omega, hall,
      show 2 ^ (v + 1) - 2 + 1 = 2 ^ (v + 1) - 1 by omega] at hpast
    have := hv 0
    rw [← hpast] at this
    exact Bool.noConfusion this

/-- A step that returns the shifted sum after `2 * M` lowers the order by at most one. -/
theorem order_countdown {s b h : Nat → Bool} {v : Nat}
    (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (b t || s t)) :
    order s (2 ^ v) ≤ order h (2 * 2 ^ v) + 1 := by
  have hle := order_le s (2 ^ v)
  rcases Nat.lt_or_ge (order s (2 ^ v)) 2 with h2 | h2
  · omega
  · have hv := (le_order_iff (g := s) (L := 2 ^ v) (r := order s (2 ^ v)) (by omega) hle).mp
      (Nat.le_refl _)
    have hgoal : order s (2 ^ v) - 1 ≤ order h (2 * 2 ^ v) := by
      apply (le_order_iff (by omega) (by omega)).mpr
      intro t
      have hpast := difs_past hs hb hh (2 ^ v - order s (2 ^ v) - 1)
      rw [show 2 ^ v - order s (2 ^ v) - 1 + 1 + 1 + 2 ^ v =
          2 * 2 ^ v - (order s (2 ^ v) - 1) by omega,
        show 2 ^ v - order s (2 ^ v) - 1 + 1 = 2 ^ v - order s (2 ^ v) by omega] at hpast
      rw [hpast]
      exact hv t
    omega

end Rule30DifferenceOrder

open Rule30RecordCharge Rule30DifferenceOrder

/-! ### The gate laws for the difference order -/

/-- A unary Boolean function keeps a vanishing positive difference vanishing. -/
theorem vanish_comp {k : Nat} {s : Nat → Bool} (d : Bool → Bool) (hv : Vanish (k + 1) s) :
    Vanish (k + 1) (fun t => d (s t)) := by
  intro t
  cases h1 : d true <;> cases h0 : d false
  · have hc : (fun t => d (s t)) = fun _ => false := by
      funext u; cases hu : s u <;> simp [h0, h1]
    rw [hc, difs_const]
  · have hc : (fun t => d (s t)) = fun u => xor ((fun _ => true) u) (s u) := by
      funext u; cases hu : s u <;> simp [h0, h1]
    rw [hc, difs_xor, difs_const]
    simp [hv t]
  · have hc : (fun t => d (s t)) = s := by
      funext u; cases hu : s u <;> simp [h0, h1]
    rw [hc]
    exact hv t
  · have hc : (fun t => d (s t)) = fun _ => true := by
      funext u; cases hu : s u <;> simp [h0, h1]
    rw [hc, difs_const]

/-- The derivative of a gate in its first (newer) input. -/
def deriv (g : Bool → Bool → Bool) (s : Bool) : Bool := xor (g true s) (g false s)

theorem xor_shift_deriv (g : Bool → Bool → Bool) (b s x y : Bool) :
    xor (xor (xor x (g (!b) s)) (xor y (g b s))) (xor x y) = deriv g s := by
  unfold deriv
  cases b <;> simp only [Bool.not_false, Bool.not_true] <;>
    cases x <;> cases y <;> cases g true s <;> cases g false s <;> rfl

/-- For any gate, the difference of the shifted sum `h (t + M) xor h t` is the derivative. -/
theorem dif_shift_sum_gate {g : Bool → Bool → Bool} {s b h : Nat → Bool} {M : Nat}
    (hs : ∀ t, s (t + M) = s t) (hb : ∀ t, b (t + M) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (g (b t) (s t))) :
    dif (fun t => xor (h (t + M)) (h t)) = fun t => deriv g (s t) := by
  funext t
  simp only [dif]
  rw [Nat.add_right_comm t 1 M, hh (t + M), hh t, hs t, hb t]
  exact xor_shift_deriv g (b t) (s t) (h (t + M)) (h t)

/-- Past the `M`-th difference, vanishing passes from `s` to `h`, for any gate. -/
theorem vanish_past_gate {g : Bool → Bool → Bool} {s b h : Nat → Bool} {v : Nat}
    (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (g (b t) (s t))) {k : Nat} (hv : Vanish (k + 1) s) :
    Vanish (k + 1 + 1 + 2 ^ v) h := by
  intro t
  rw [difs_add, difs_two_pow, difs_succ' (k + 1), dif_shift_sum_gate hs hb hh]
  exact vanish_comp (deriv g) hv t

/-- Reset before a double step, for any gate (`Rule30DifferenceOrder.order_reset_before`). -/
theorem order_reset_before_gate {g : Bool → Bool → Bool} {s b h : Nat → Bool} {v : Nat}
    (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (g (b t) (s t)))
    (hanti : ∀ t, h (t + 2 * 2 ^ v) = !h t) :
    order s (2 ^ v) = 0 := by
  cases v with
  | zero => have := order_le s (2 ^ 0); omega
  | succ v =>
    have hM : 2 ≤ 2 ^ (v + 1) := by
      rw [Nat.pow_succ]; have := Nat.one_le_two_pow (n := v); omega
    apply Nat.eq_zero_of_not_pos
    intro hpos
    have hv := (le_order_iff (g := s) (L := 2 ^ (v + 1)) (r := 1) (by omega) (by omega)).mp hpos
    have hall : difs (2 * 2 ^ (v + 1)) h = fun _ => true := by
      rw [← two_pow_succ' (v + 1), difs_two_pow]
      funext t
      rw [two_pow_succ' (v + 1), hanti t]
      cases h t <;> rfl
    have hpast := vanish_past_gate hs hb hh (k := 2 ^ (v + 1) - 2)
      (by rw [show 2 ^ (v + 1) - 2 + 1 = 2 ^ (v + 1) - 1 by omega]; exact hv)
    rw [show 2 ^ (v + 1) - 2 + 1 + 1 + 2 ^ (v + 1) = 2 * 2 ^ (v + 1) by omega] at hpast
    have := hpast 0
    rw [hall] at this
    exact Bool.noConfusion this

/-- Countdown, for any gate (`Rule30DifferenceOrder.order_countdown`). -/
theorem order_countdown_gate {g : Bool → Bool → Bool} {s b h : Nat → Bool} {v : Nat}
    (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (g (b t) (s t))) :
    order s (2 ^ v) ≤ order h (2 * 2 ^ v) + 1 := by
  have hle := order_le s (2 ^ v)
  rcases Nat.lt_or_ge (order s (2 ^ v)) 2 with h2 | h2
  · omega
  · have hv := (le_order_iff (g := s) (L := 2 ^ v) (r := order s (2 ^ v)) (by omega) hle).mp
      (Nat.le_refl _)
    have hgoal : order s (2 ^ v) - 1 ≤ order h (2 * 2 ^ v) := by
      apply (le_order_iff (by omega) (by omega)).mpr
      have hpast := vanish_past_gate hs hb hh (k := 2 ^ v - order s (2 ^ v) - 1)
        (by rw [show 2 ^ v - order s (2 ^ v) - 1 + 1 = 2 ^ v - order s (2 ^ v) by omega]; exact hv)
      rwa [show 2 ^ v - order s (2 ^ v) - 1 + 1 + 1 + 2 ^ v =
        2 * 2 ^ v - (order s (2 ^ v) - 1) by omega] at hpast
    omega

/-! ### Gate clocks and their record-charge paths -/

/-- A prefix clock driven by gates: `profile j` has period `2 ^ exponent j`, the exponent grows
by `0` or `1`, a growth complements the next profile, and each profile is a running XOR of a gate
of the two before it. Kit PR #55's `Clock`, with `||` replaced by `gate j`. -/
structure GateClock where
  gate : Nat → Bool → Bool → Bool
  profile : Nat → Nat → Bool
  exponent : Nat → Nat
  exponent_succ_cases : ∀ j, exponent (j + 1) = exponent j ∨ exponent (j + 1) = exponent j + 1
  period : ∀ j t, profile j (t + 2 ^ exponent j) = profile j t
  antiperiod : ∀ {j}, exponent (j + 1) = exponent j + 1 →
    ∀ t, profile (j + 1) (t + 2 ^ exponent j) = !profile (j + 1) t
  recurrence : ∀ j t, profile (j + 2) (t + 1) =
    xor (profile (j + 2) t) (gate j (profile (j + 1) t) (profile j t))

namespace GateClock

variable (C : GateClock)

theorem exponent_mono (a : Nat) : ∀ n, C.exponent a ≤ C.exponent (a + n)
  | 0 => Nat.le_refl _
  | n + 1 => by
    have := exponent_mono a n
    rcases C.exponent_succ_cases (a + n) with h | h <;> rw [← Nat.add_assoc, h] <;> omega

/-- The resource at pair `i` of the window from `a`. -/
noncomputable def resource (a i : Nat) : Nat :=
  order (C.profile (a + 2 * i)) (2 ^ C.exponent (a + 2 * i))

theorem pair_index (a i : Nat) : a + 2 * (i + 1) = a + 2 * i + 1 + 1 := by omega

/-- The pairs of a window from `a` form a record-charge path with `nu = exponent a`. -/
noncomputable def windowPath (a : Nat) : Path (C.exponent a) where
  weight i := C.exponent (a + 2 * i + 1 + 1) - C.exponent (a + 2 * i)
  exponent i := C.exponent (a + 2 * i) - C.exponent a
  resource := C.resource a
  exponent_zero := by simp
  exponent_step i := by
    have h0 := C.exponent_succ_cases (a + 2 * i)
    have h1 := C.exponent_succ_cases (a + 2 * i + 1)
    have hm := C.exponent_mono a (2 * i)
    show C.exponent (a + 2 * (i + 1)) - C.exponent a = _
    rw [pair_index]
    omega
  weight_le_two i := by
    have h0 := C.exponent_succ_cases (a + 2 * i)
    have h1 := C.exponent_succ_cases (a + 2 * i + 1)
    show C.exponent (a + 2 * i + 1 + 1) - C.exponent (a + 2 * i) ≤ 2
    omega
  reset_before i hw := by
    have h0 := C.exponent_succ_cases (a + 2 * i)
    have h1 := C.exponent_succ_cases (a + 2 * i + 1)
    change C.exponent (a + 2 * i + 1 + 1) - C.exponent (a + 2 * i) = 2 at hw
    have e0 : C.exponent (a + 2 * i + 1) = C.exponent (a + 2 * i) + 1 := by omega
    have e1 : C.exponent (a + 2 * i + 1 + 1) = C.exponent (a + 2 * i + 1) + 1 := by omega
    have hanti : ∀ t, C.profile (a + 2 * i + 1 + 1) (t + 2 * 2 ^ C.exponent (a + 2 * i)) =
        !C.profile (a + 2 * i + 1 + 1) t := by
      intro t
      have := C.antiperiod e1 t
      rwa [e0, two_pow_succ'] at this
    exact order_reset_before_gate (C.period (a + 2 * i)) (C.antiperiod e0)
      (C.recurrence (a + 2 * i)) hanti
  reset_after i hw := by
    have h0 := C.exponent_succ_cases (a + 2 * i)
    have h1 := C.exponent_succ_cases (a + 2 * i + 1)
    have hm := C.exponent_mono a (2 * i)
    change C.exponent (a + 2 * i + 1 + 1) - C.exponent (a + 2 * i) = 2 at hw
    have e0 : C.exponent (a + 2 * i + 1) = C.exponent (a + 2 * i) + 1 := by omega
    have e1 : C.exponent (a + 2 * i + 1 + 1) = C.exponent (a + 2 * i + 1) + 1 := by omega
    have hanti : ∀ t, C.profile (a + 2 * i + 1 + 1) (t + 2 ^ (C.exponent (a + 2 * i) + 1)) =
        !C.profile (a + 2 * i + 1 + 1) t := by
      intro t
      have := C.antiperiod e1 t
      rwa [e0] at this
    have hord := order_of_antiperiod hanti
    show order (C.profile (a + 2 * (i + 1))) (2 ^ C.exponent (a + 2 * (i + 1))) + 1 =
      2 ^ (C.exponent a + (C.exponent (a + 2 * (i + 1)) - C.exponent a) - 1)
    rw [pair_index, e1, e0, two_pow_succ' (C.exponent (a + 2 * i) + 1), hord,
      show C.exponent a + (C.exponent (a + 2 * i) + 1 + 1 - C.exponent a) - 1 =
        C.exponent (a + 2 * i) + 1 by omega]
    have := Nat.one_le_two_pow (n := C.exponent (a + 2 * i) + 1)
    omega
  countdown i hw := by
    have h0 := C.exponent_succ_cases (a + 2 * i)
    have h1 := C.exponent_succ_cases (a + 2 * i + 1)
    change C.exponent (a + 2 * i + 1 + 1) - C.exponent (a + 2 * i) = 1 at hw
    show C.resource a i ≤ order (C.profile (a + 2 * (i + 1))) (2 ^ C.exponent (a + 2 * (i + 1))) + 1
    rw [pair_index]
    unfold resource
    rcases h0 with e0 | e0
    · -- the middle profile keeps the period: the last one is complemented by `M`
      have e1 : C.exponent (a + 2 * i + 1 + 1) = C.exponent (a + 2 * i) + 1 := by omega
      have hanti : ∀ t, C.profile (a + 2 * i + 1 + 1) (t + 2 ^ C.exponent (a + 2 * i)) =
          !C.profile (a + 2 * i + 1 + 1) t := by
        intro t
        have := C.antiperiod (j := a + 2 * i + 1) (by omega) t
        rwa [e0] at this
      rw [e1, two_pow_succ', order_of_antiperiod hanti]
      have := order_le (C.profile (a + 2 * i)) (2 ^ C.exponent (a + 2 * i))
      omega
    · -- the middle profile is complemented by `M`: countdown
      have e1 : C.exponent (a + 2 * i + 1 + 1) = C.exponent (a + 2 * i) + 1 := by omega
      rw [e1, two_pow_succ']
      exact order_countdown_gate (C.period (a + 2 * i)) (C.antiperiod e0)
        (C.recurrence (a + 2 * i))

/-- The window bound for a gate clock. -/
theorem window_bound (a m : Nat) :
    C.exponent (a + 2 * m) - C.exponent a ≤ m + Q (C.exponent a) m :=
  exponent_bound_before_threshold (C.windowPath a) m (Q (C.exponent a) m) (Q_spec _ m)

end GateClock

/-! ### The thresholds only grow with `nu` -/

theorem threshold_zero_le (nu : Nat) : ∀ q, threshold 0 q ≤ threshold nu q
  | 0 => Nat.le_refl _
  | q + 1 => by
    have ih := threshold_zero_le nu q
    have hp := Nat.pow_le_pow_right (n := 2) (by decide)
      (show 0 + threshold 0 q + q ≤ nu + threshold nu q + q by omega)
    simp only [threshold]
    omega

theorem Q_le_Q_zero (nu m : Nat) : Q nu m ≤ Q 0 m :=
  (Q_le_iff nu m (Q 0 m)).mpr (Nat.lt_of_lt_of_le (Q_spec 0 m) (threshold_zero_le nu _))

/-! ### The edge map of a gate family and its prefix exponents -/

/-- One step: bit `j` is XORed with `g j` of bits `j - 1` and `j - 2`, missing bits white. -/
def step (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) : Nat → Bool
  | 0 => xor (x 0) (g 0 false false)
  | 1 => xor (x 1) (g 1 (x 0) false)
  | j + 2 => xor (x (j + 2)) (g (j + 2) (x (j + 1)) (x j))

/-- The orbit of a seed. -/
def orbit (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) : Nat → Nat → Bool
  | 0 => x
  | t + 1 => step g (orbit g x t)

/-- Columns: `col g x 0` is a white bit below bit `0`, and `col g x (k + 1) t` is bit `k` at time `t`. -/
def col (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) : Nat → Nat → Bool
  | 0, _ => false
  | k + 1, t => orbit g x t k

/-- The input that drives column `k + 1` (bit `k`). -/
def force (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (k t : Nat) : Bool :=
  g k (col g x k t) (col g x (k - 1) t)

theorem col_step (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (k t : Nat) :
    col g x (k + 1) (t + 1) = xor (col g x (k + 1) t) (force g x k t) := by
  match k with
  | 0 => rfl
  | 1 => rfl
  | j + 2 => rfl

/-- XOR of `f t, …, f (t + n - 1)`. -/
def xsum (f : Nat → Bool) (t : Nat) : Nat → Bool
  | 0 => false
  | n + 1 => xor (xsum f t n) (f (t + n))

theorem xsum_add (f : Nat → Bool) (t a : Nat) : ∀ b, xsum f t (a + b) = xor (xsum f t a) (xsum f (t + a) b)
  | 0 => by simp [xsum]
  | b + 1 => by
    rw [← Nat.add_assoc]
    simp only [xsum]
    rw [xsum_add f t a b, Nat.add_assoc t a b]
    cases xsum f t a <;> cases xsum f (t + a) b <;> cases f (t + (a + b)) <;> rfl

theorem xsum_succ_start (f : Nat → Bool) (t : Nat) : ∀ n, xsum f (t + 1) n = xor (xsum f t n) (xor (f t) (f (t + n)))
  | 0 => by simp [xsum]
  | n + 1 => by
    simp only [xsum]
    rw [xsum_succ_start f t n, show t + 1 + n = t + (n + 1) by omega]
    cases xsum f t n <;> cases f t <;> cases f (t + n) <;> cases f (t + (n + 1)) <;> rfl

/-- Over a period of `f`, the XOR does not depend on the start. -/
theorem xsum_period {f : Nat → Bool} {L : Nat} (hf : ∀ t, f (t + L) = f t) : ∀ t, xsum f t L = xsum f 0 L
  | 0 => rfl
  | t + 1 => by
    rw [xsum_succ_start, hf t, xsum_period hf t]
    cases xsum f 0 L <;> cases f t <;> rfl

theorem xsum_mul {f : Nat → Bool} {L : Nat} (hf : ∀ t, f (t + L) = f t) (t : Nat) :
    ∀ q, xsum f t (L * q) = (xsum f 0 L && q % 2 == 1)
  | 0 => by simp [xsum]
  | q + 1 => by
    rw [Nat.mul_succ, xsum_add, xsum_mul hf t q, xsum_period hf (t + L * q)]
    rcases Nat.mod_two_eq_zero_or_one q with h | h
    · have h' : (q + 1) % 2 = 1 := by omega
      rw [h, h']
      cases xsum f 0 L <;> rfl
    · have h' : (q + 1) % 2 = 0 := by omega
      rw [h, h']
      cases xsum f 0 L <;> rfl

theorem col_add (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (k t : Nat) :
    ∀ n, col g x (k + 1) (t + n) = xor (col g x (k + 1) t) (xsum (force g x k) t n)
  | 0 => by simp [xsum]
  | n + 1 => by
    rw [← Nat.add_assoc, col_step, col_add g x k t n]
    simp only [xsum]
    cases col g x (k + 1) t <;> cases xsum (force g x k) t n <;> cases force g x k (t + n) <;> rfl

/-- The exponent of the least period of the first `n` bits, by lifting one bit at a time. -/
def prefixExp (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) : Nat → Nat
  | 0 => 0
  | n + 1 => prefixExp g x n + if xsum (force g x n) 0 (2 ^ prefixExp g x n) then 1 else 0

/-- `P` is a period of columns `0 … n`, that is of the first `n` bits. -/
def PrefixPer (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (n P : Nat) : Prop :=
  ∀ i, i ≤ n → ∀ t, col g x i (t + P) = col g x i t

theorem prefixExp_succ (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (n : Nat) :
    prefixExp g x (n + 1) =
      prefixExp g x n + if xsum (force g x n) 0 (2 ^ prefixExp g x n) then 1 else 0 := rfl

/-- **Exact prefix periods**: `P` is a period of the first `n` bits iff `2 ^ prefixExp g x n`
divides `P`. -/
theorem prefix_period_iff (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) :
    ∀ n P, PrefixPer g x n P ↔ 2 ^ prefixExp g x n ∣ P
  | 0, P => by
    constructor
    · intro _; simp [prefixExp]
    · intro _ i hi t
      rw [Nat.le_zero.mp hi]
      rfl
  | n + 1, P => by
    have ih := prefix_period_iff g x n
    have hforce : ∀ t, force g x n (t + 2 ^ prefixExp g x n) = force g x n t := by
      have hp := (ih (2 ^ prefixExp g x n)).mpr (Nat.dvd_refl _)
      intro t
      unfold force
      rw [hp n (Nat.le_refl n) t, hp (n - 1) (by omega) t]
    constructor
    · intro hP
      have hlow : PrefixPer g x n P := fun i hi t => hP i (by omega) t
      obtain ⟨q, hq⟩ := (ih P).mp hlow
      have hc := hP (n + 1) (Nat.le_refl _) 0
      rw [col_add, hq, xsum_mul hforce] at hc
      by_cases hx : xsum (force g x n) 0 (2 ^ prefixExp g x n) = true
      · rw [prefixExp_succ, ite_eq_left hx]
        have hq2 : q % 2 = 0 := by
          rcases Nat.mod_two_eq_zero_or_one q with h | h
          · exact h
          · rw [hx, h] at hc
            cases hc0 : col g x (n + 1) 0 <;> rw [hc0] at hc <;> exact absurd hc (by decide)
        obtain ⟨q', rfl⟩ : ∃ q', q = 2 * q' := ⟨q / 2, by omega⟩
        exact ⟨q', by rw [hq, Nat.pow_succ, Nat.mul_assoc]⟩
      · rw [prefixExp_succ, ite_eq_right hx, Nat.add_zero]
        exact ⟨q, hq⟩
    · intro hd i hi t
      have hle : 2 ^ prefixExp g x n ∣ 2 ^ prefixExp g x (n + 1) :=
        Nat.pow_dvd_pow 2 (by rw [prefixExp_succ]; split <;> omega)
      have hlow := (ih P).mpr (Nat.dvd_trans hle hd)
      rcases Nat.lt_or_eq_of_le hi with hi | hi
      · exact hlow i (by omega) t
      · subst hi
        obtain ⟨q, hq⟩ := Nat.dvd_trans hle hd
        rw [col_add, hq, xsum_mul hforce]
        by_cases hx : xsum (force g x n) 0 (2 ^ prefixExp g x n) = true
        · rw [prefixExp_succ, ite_eq_left hx] at hd
          obtain ⟨q2, hq2⟩ := hd
          have hqq : q = 2 * q2 := by
            apply Nat.eq_of_mul_eq_mul_left (Nat.two_pow_pos (prefixExp g x n))
            rw [← hq, hq2, Nat.pow_succ, Nat.mul_assoc]
          have h0 : q % 2 = 0 := by omega
          rw [h0]
          cases xsum (force g x n) 0 (2 ^ prefixExp g x n) <;> cases col g x (n + 1) t <;> rfl
        · have hf : xsum (force g x n) 0 (2 ^ prefixExp g x n) = false := by
            cases h : xsum (force g x n) 0 (2 ^ prefixExp g x n)
            · rfl
            · exact absurd h hx
          rw [hf]
          cases col g x (n + 1) t <;> rfl

theorem prefixExp_succ_cases (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (n : Nat) :
    prefixExp g x (n + 1) = prefixExp g x n ∨ prefixExp g x (n + 1) = prefixExp g x n + 1 := by
  rw [prefixExp_succ]
  split <;> omega

/-- When the exponent grows, a shift by the old period complements the new bit. -/
theorem col_antiperiod (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {n : Nat}
    (h : prefixExp g x (n + 1) = prefixExp g x n + 1) (t : Nat) :
    col g x (n + 1) (t + 2 ^ prefixExp g x n) = !col g x (n + 1) t := by
  have hp := (prefix_period_iff g x n (2 ^ prefixExp g x n)).mpr (Nat.dvd_refl _)
  have hforce : ∀ t, force g x n (t + 2 ^ prefixExp g x n) = force g x n t := by
    intro t
    unfold force
    rw [hp n (Nat.le_refl n) t, hp (n - 1) (by omega) t]
  have hx : xsum (force g x n) 0 (2 ^ prefixExp g x n) = true := by
    cases hc : xsum (force g x n) 0 (2 ^ prefixExp g x n)
    · rw [prefixExp_succ, hc] at h
      simp at h
    · rfl
  rw [col_add, xsum_period hforce, hx]
  cases col g x (n + 1) t <;> rfl

/-- The columns of an orbit form a gate clock. -/
def gateClock (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) : GateClock where
  gate j := g (j + 1)
  profile := col g x
  exponent := prefixExp g x
  exponent_succ_cases := prefixExp_succ_cases g x
  period j t := (prefix_period_iff g x j _).mpr (Nat.dvd_refl _) j (Nat.le_refl j) t
  antiperiod h t := col_antiperiod g x h t
  recurrence j t := by
    rw [col_step]
    rfl

/-! ### The half-rate bound -/

/-- **Window bound**: for every gate family, seed and window, the prefix exponent grows by at most
`m + Q (prefixExp a) m ≤ m + Q 0 m` over `2 m` further bits. -/
theorem prefix_window_bound (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (a m : Nat) :
    prefixExp g x (a + 2 * m) - prefixExp g x a ≤ m + Q (prefixExp g x a) m ∧
      prefixExp g x (a + 2 * m) - prefixExp g x a ≤ m + Q 0 m := by
  have h : prefixExp g x (a + 2 * m) - prefixExp g x a ≤ m + Q (prefixExp g x a) m :=
    (gateClock g x).window_bound a m
  have hQ := Q_le_Q_zero (prefixExp g x a) m
  exact ⟨h, by omega⟩

/-- Any window of `n` bits raises the prefix exponent by at most `⌈n/2⌉ + Q 0 ⌊n/2⌋`. -/
theorem prefix_window_le_B (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (a n : Nat) :
    prefixExp g x (a + n) - prefixExp g x a ≤ B n := by
  unfold B
  obtain ⟨d, rfl | rfl⟩ : ∃ d, n = 2 * d ∨ n = 2 * d + 1 := ⟨n / 2, by omega⟩
  · rw [show (2 * d + 1) / 2 = d by omega, show 2 * d / 2 = d by omega]
    exact (prefix_window_bound g x a d).2
  · rw [show (2 * d + 1 + 1) / 2 = d + 1 by omega, show (2 * d + 1) / 2 = d by omega,
      ← Nat.add_assoc]
    have := (prefix_window_bound g x a d).2
    have hm : prefixExp g x a ≤ prefixExp g x (a + 2 * d) := (gateClock g x).exponent_mono a (2 * d)
    rcases prefixExp_succ_cases g x (a + 2 * d) with h | h <;> omega

/-- **Half-rate bound**: the first `n` bits have period dividing `2 ^ B n`. -/
theorem prefixExp_le_B (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (n : Nat) :
    prefixExp g x n ≤ B n ∧ PrefixPer g x n (2 ^ B n) := by
  have h := prefix_window_le_B g x 0 n
  rw [Nat.zero_add] at h
  have hz : prefixExp g x 0 = 0 := rfl
  have h0 : prefixExp g x n ≤ B n := by omega
  exact ⟨h0, (prefix_period_iff g x n _).mpr (Nat.pow_dvd_pow 2 h0)⟩

/-! ### Affine gates: logarithmic exponents -/

/-- An affine gate: `g b s = (α && b) xor (β && s) xor γ`. -/
def Affine (g : Bool → Bool → Bool) : Prop :=
  ∃ α β γ : Bool, ∀ b s, g b s = xor (xor (α && b) (β && s)) γ

theorem vanish_xor {k : Nat} {f h : Nat → Bool} (hf : Vanish k f) (hh : Vanish k h) :
    Vanish k (fun t => xor (f t) (h t)) := by
  intro t
  rw [difs_xor]
  simp [hf t, hh t]

theorem vanish_const (k : Nat) (c : Bool) : Vanish (k + 1) (fun _ => c) := by
  intro t
  rw [difs_const]

theorem col_zero_fun (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) :
    col g x 0 = fun _ => false := by
  funext t; rfl

/-- With affine gates, column `k` (bit `k - 1`) has a vanishing `(k + 1)`-th difference. -/
theorem affine_vanish (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (hg : ∀ j, Affine (g j)) :
    ∀ k, Vanish (k + 1) (col g x k) ∧ Vanish (k + 1 + 1) (col g x (k + 1))
  | 0 => by
    refine ⟨?_, ?_⟩
    · rw [col_zero_fun]; exact vanish_const 0 false
    · have hd : dif (col g x (0 + 1)) = fun _ => g 0 false false := by
        funext t
        simp only [dif]
        rw [col_step]
        show xor (xor (col g x 1 t) (g 0 false false)) (col g x 1 t) = g 0 false false
        cases col g x 1 t <;> cases g 0 false false <;> rfl
      intro t
      rw [difs_succ', hd]
      exact vanish_const 0 _ t
  | k + 1 => by
    obtain ⟨h1, h2⟩ := affine_vanish g x hg k
    refine ⟨h2, ?_⟩
    obtain ⟨α, β, γ, hgk⟩ := hg (k + 1)
    have hd : dif (col g x (k + 1 + 1)) =
        fun t => xor (xor (α && col g x (k + 1) t) (β && col g x k t)) γ := by
      funext t
      simp only [dif]
      rw [col_step]
      unfold force
      rw [hgk, Nat.add_sub_cancel]
      cases col g x (k + 1 + 1) t <;> simp
    intro t
    rw [difs_succ', hd]
    exact vanish_xor (vanish_xor (vanish_comp (fun u => α && u) h2)
      (vanish_comp (fun u => β && u) (h1.mono (by omega)))) (vanish_const _ γ) t

theorem period_of_vanish {f : Nat → Bool} {r : Nat} (hv : Vanish (2 ^ r) f) (t : Nat) :
    f (t + 2 ^ r) = f t := by
  have h := hv t
  rw [difs_two_pow] at h
  change xor (f (t + 2 ^ r)) (f t) = false at h
  cases h1 : f (t + 2 ^ r) <;> cases h2 : f t <;> simp_all

/-- **Affine gates**: if every gate is affine, the first `n` bits have period dividing `2 ^ r`
whenever `n + 1 ≤ 2 ^ r` (unitriangular nilpotency). -/
theorem affine_prefix_bound (g : Nat → Bool → Bool → Bool) (x : Nat → Bool)
    (hg : ∀ j, Affine (g j)) {n r : Nat} (hr : n + 1 ≤ 2 ^ r) :
    PrefixPer g x n (2 ^ r) ∧ prefixExp g x n ≤ r := by
  have hper : PrefixPer g x n (2 ^ r) := fun i hi t =>
    period_of_vanish (((affine_vanish g x hg i).1).mono (by omega)) t
  refine ⟨hper, ?_⟩
  have hd := (prefix_period_iff g x n _).mp hper
  exact (Nat.pow_dvd_pow_iff_le_right (by decide)).mp hd


/-! ## Nested record thresholds (this submission's new part) -/

/-! ### Algebraic normal form of a two-input gate -/

/-- The coefficients of `g b s = λ b s ⊕ α b ⊕ β s ⊕ γ`. -/
def lamG (g : Bool → Bool → Bool) : Bool := xor (xor (g true true) (g true false)) (xor (g false true) (g false false))
def alpG (g : Bool → Bool → Bool) : Bool := xor (g true false) (g false false)
def betG (g : Bool → Bool → Bool) : Bool := xor (g false true) (g false false)
def gamG (g : Bool → Bool → Bool) : Bool := g false false

theorem gate_anf (g : Bool → Bool → Bool) (b s : Bool) :
    g b s = xor (xor (xor (lamG g && (b && s)) (alpG g && b)) (betG g && s)) (gamG g) := by
  unfold lamG alpG betG gamG
  cases b <;> cases s <;> cases h1 : g true true <;> cases h2 : g true false <;> cases h3 : g false true <;>
    cases h4 : g false false <;> simp_all

/-! ### XOR sums -/

theorem xsum_xor (f h : Nat → Bool) (t : Nat) :
    ∀ n, xsum (fun u => xor (f u) (h u)) t n = xor (xsum f t n) (xsum h t n)
  | 0 => rfl
  | n + 1 => by
    simp only [xsum]
    rw [xsum_xor f h t n]
    cases xsum f t n <;> cases xsum h t n <;> cases f (t + n) <;> cases h (t + n) <;> rfl

theorem xsum_and_const (c : Bool) (f : Nat → Bool) (t : Nat) :
    ∀ n, xsum (fun u => c && f u) t n = (c && xsum f t n)
  | 0 => by simp [xsum]
  | n + 1 => by
    simp only [xsum]
    rw [xsum_and_const c f t n]
    cases c <;> cases xsum f t n <;> cases f (t + n) <;> rfl

theorem xsum_const (c : Bool) (t : Nat) : ∀ n, xsum (fun _ => c) t n = (c && n % 2 == 1)
  | 0 => by simp [xsum]
  | n + 1 => by
    simp only [xsum]
    rw [xsum_const c t n]
    rcases Nat.mod_two_eq_zero_or_one n with h | h
    · rw [h, show (n + 1) % 2 = 1 by omega]; cases c <;> rfl
    · rw [h, show (n + 1) % 2 = 0 by omega]; cases c <;> rfl

theorem xsum_shift (f : Nat → Bool) (t c : Nat) : ∀ n, xsum f (t + c) n = xsum (fun u => f (u + c)) t n
  | 0 => rfl
  | n + 1 => by
    simp only [xsum]
    rw [xsum_shift f t c n, Nat.add_right_comm t c n]

theorem xsum_not (f : Nat → Bool) (t n : Nat) : xsum (fun u => !f u) t n = xor (xsum f t n) (n % 2 == 1) := by
  have e : (fun u => !f u) = fun u => xor ((fun _ => true) u) (f u) := by funext u; cases f u <;> rfl
  rw [e, xsum_xor, xsum_const]
  cases xsum f t n <;> cases (n % 2 == 1) <;> rfl

/-- A stream complemented by a shift of `L` has XOR sum `L mod 2` over `2 L`. -/
theorem xsum_antiperiod {f : Nat → Bool} {L : Nat} (hf : ∀ u, f (u + L) = !f u) (t : Nat) :
    xsum f t (L + L) = (L % 2 == 1) := by
  rw [xsum_add, xsum_shift]
  have e : (fun u => f (u + L)) = fun u => !f u := funext hf
  rw [e, xsum_not]
  cases xsum f t L <;> cases (L % 2 == 1) <;> rfl

/-- The overlap of an `L`-antiperiodic `b` with an `L`-periodic `s` over `2 L` is the XOR sum of `s` over `L`. -/
theorem xsum_overlap {b s : Nat → Bool} {L : Nat} (hb : ∀ u, b (u + L) = !b u) (hs : ∀ u, s (u + L) = s u)
    (t : Nat) : xsum (fun u => b u && s u) t (L + L) = xsum s t L := by
  rw [xsum_add, xsum_shift]
  have e : (fun u => b (u + L) && s (u + L)) = fun u => xor (s u) (b u && s u) := by
    funext u; rw [hb u, hs u]; cases b u <;> cases s u <;> rfl
  rw [e, xsum_xor]
  cases xsum s t L <;> cases xsum (fun u => b u && s u) t L <;> rfl

/-- The XOR sum of a gate's forcing, by its normal form. -/
theorem xsum_gate (g : Bool → Bool → Bool) (b s : Nat → Bool) (t n : Nat) :
    xsum (fun u => g (b u) (s u)) t n =
      xor (xor (xor (lamG g && xsum (fun u => b u && s u) t n) (alpG g && xsum b t n))
        (betG g && xsum s t n)) (gamG g && n % 2 == 1) := by
  have e : (fun u => g (b u) (s u)) = fun u => xor (xor (xor (lamG g && (b u && s u)) (alpG g && b u))
      (betG g && s u)) (gamG g) := funext fun u => gate_anf g (b u) (s u)
  rw [e]
  rw [show (fun u => xor (xor (xor (lamG g && (b u && s u)) (alpG g && b u)) (betG g && s u)) (gamG g)) =
      fun u => xor ((fun u => xor ((fun u => xor ((fun u => lamG g && (b u && s u)) u)
        ((fun u => alpG g && b u) u)) u) ((fun u => betG g && s u) u)) u) ((fun _ => gamG g) u) from rfl]
  rw [xsum_xor, xsum_xor, xsum_xor, xsum_and_const, xsum_and_const, xsum_and_const, xsum_const]

/-! ### Column facts -/

theorem col_period_of_le (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {n m : Nat} (h : n ≤ m) (t : Nat) :
    col g x n (t + 2 ^ prefixExp g x m) = col g x n t :=
  (prefix_period_iff g x m _).mpr (Nat.dvd_refl _) n h t

theorem prefixExp_double_iff (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (n : Nat) :
    prefixExp g x (n + 1) = prefixExp g x n + 1 ↔ xsum (force g x n) 0 (2 ^ prefixExp g x n) = true := by
  rw [prefixExp_succ]
  cases h : xsum (force g x n) 0 (2 ^ prefixExp g x n) <;> simp

theorem antiperiod_twice {f : Nat → Bool} {L : Nat} (hf : ∀ u, f (u + L) = !f u) (u : Nat) :
    f (u + (L + L)) = f u := by
  rw [← Nat.add_assoc, hf, hf, Bool.not_not]

theorem two_pow_even {e : Nat} (he : 1 ≤ e) : 2 ^ e % 2 = 0 := by
  obtain ⟨k, rfl⟩ : ∃ k, e = k + 1 := ⟨e - 1, by omega⟩
  rw [Nat.pow_succ]; simp

/-! ### No three doublings in a row -/

/-- **No three in a row**: if columns `n + 1` and `n + 2` both double and the prefix through column `n` has period at
least 2, column `n + 3` does not double. For every gate. -/
theorem no_three (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {n : Nat}
    (h1 : prefixExp g x (n + 1) = prefixExp g x n + 1)
    (h2 : prefixExp g x (n + 1 + 1) = prefixExp g x (n + 1) + 1) (hM : 1 ≤ prefixExp g x n) :
    prefixExp g x (n + 1 + 1 + 1) = prefixExp g x (n + 1 + 1) := by
  have hs : ∀ u, col g x (n + 1) (u + 2 ^ prefixExp g x n) = !col g x (n + 1) u := col_antiperiod g x h1
  have hb : ∀ u, col g x (n + 1 + 1) (u + 2 ^ prefixExp g x (n + 1)) = !col g x (n + 1 + 1) u := col_antiperiod g x h2
  have hs2 : ∀ u, col g x (n + 1) (u + 2 ^ prefixExp g x (n + 1)) = col g x (n + 1) u := by
    intro u; rw [h1, Nat.pow_succ, Nat.mul_two]; exact antiperiod_twice hs u
  have hf : force g x (n + 1 + 1) = fun u => g (n + 1 + 1) (col g x (n + 1 + 1) u) (col g x (n + 1) u) := by
    funext u; rfl
  have hL : 2 ^ prefixExp g x (n + 1 + 1) = 2 ^ prefixExp g x (n + 1) + 2 ^ prefixExp g x (n + 1) := by
    rw [h2, Nat.pow_succ, Nat.mul_two]
  have hx : xsum (force g x (n + 1 + 1)) 0 (2 ^ prefixExp g x (n + 1 + 1)) = false := by
    rw [hf, xsum_gate, hL, xsum_overlap hb hs2, xsum_antiperiod hb, xsum_add, xsum_period hs2 (0 + _)]
    rw [h1, Nat.pow_succ, Nat.mul_two, xsum_antiperiod hs]
    have e1 := two_pow_even hM
    have e2 : (2 ^ prefixExp g x n + 2 ^ prefixExp g x n) % 2 = 0 := by omega
    have e3 : (2 ^ prefixExp g x n + 2 ^ prefixExp g x n + (2 ^ prefixExp g x n + 2 ^ prefixExp g x n)) % 2 = 0 := by
      omega
    rw [e1, e2, e3]
    cases lamG (g (n + 1 + 1)) <;> cases alpG (g (n + 1 + 1)) <;> cases betG (g (n + 1 + 1)) <;>
      cases gamG (g (n + 1 + 1)) <;> cases xsum (col g x (n + 1)) 0 (2 ^ prefixExp g x n + 2 ^ prefixExp g x n) <;> rfl
  rw [prefixExp_succ, hx]
  rfl

/-! ### The doubling test after a `01` pair -/

/-- After a pair whose first column keeps the period `P ≥ 2` and whose second doubles, the next column doubles iff the
gate's quadratic coefficient is 1 and the first column has odd weight over `P`. -/
theorem after01_double_iff (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {n : Nat}
    (h0 : prefixExp g x (n + 1) = prefixExp g x n)
    (h1 : prefixExp g x (n + 1 + 1) = prefixExp g x (n + 1) + 1) (hM : 1 ≤ prefixExp g x n) :
    prefixExp g x (n + 1 + 1 + 1) = prefixExp g x (n + 1 + 1) + 1 ↔
      (lamG (g (n + 1 + 1)) && xsum (col g x (n + 1)) 0 (2 ^ prefixExp g x n)) = true := by
  have ha : ∀ u, col g x (n + 1) (u + 2 ^ prefixExp g x n) = col g x (n + 1) u := by
    intro u; rw [← h0]; exact col_period_of_le g x (Nat.le_refl _) u
  have hb : ∀ u, col g x (n + 1 + 1) (u + 2 ^ prefixExp g x n) = !col g x (n + 1 + 1) u := by
    intro u; rw [← h0]; exact col_antiperiod g x h1 u
  have hf : force g x (n + 1 + 1) = fun u => g (n + 1 + 1) (col g x (n + 1 + 1) u) (col g x (n + 1) u) := by
    funext u; rfl
  have hL : 2 ^ prefixExp g x (n + 1 + 1) = 2 ^ prefixExp g x n + 2 ^ prefixExp g x n := by
    rw [h1, h0, Nat.pow_succ, Nat.mul_two]
  rw [prefixExp_double_iff, hf, xsum_gate, hL, xsum_overlap hb ha, xsum_antiperiod hb, xsum_add,
    xsum_period ha (0 + _)]
  have e1 := two_pow_even hM
  have e2 : (2 ^ prefixExp g x n + 2 ^ prefixExp g x n) % 2 = 0 := by omega
  rw [e1, e2]
  cases lamG (g (n + 1 + 1)) <;> cases alpG (g (n + 1 + 1)) <;> cases betG (g (n + 1 + 1)) <;>
    cases gamG (g (n + 1 + 1)) <;> cases xsum (col g x (n + 1)) 0 (2 ^ prefixExp g x n) <;> simp

/-! ### Order zero is odd weight -/

theorem difs_pred_two_pow (f : Nat → Bool) : ∀ v t, difs (2 ^ v - 1) f t = xsum f t (2 ^ v)
  | 0, t => by simp [difs, xsum]
  | v + 1, t => by
    have e : 2 ^ (v + 1) - 1 = 2 ^ v + (2 ^ v - 1) := by
      have := Nat.one_le_two_pow (n := v); rw [Nat.pow_succ]; omega
    rw [e, difs_add, difs_two_pow]
    show xor (difs (2 ^ v - 1) f (t + 2 ^ v)) (difs (2 ^ v - 1) f t) = _
    rw [difs_pred_two_pow f v (t + 2 ^ v), difs_pred_two_pow f v t, Nat.pow_succ, Nat.mul_two, xsum_add]
    cases xsum f t (2 ^ v) <;> cases xsum f (t + 2 ^ v) (2 ^ v) <;> rfl

/-- For a stream of period `2 ^ v ≥ 2`, order 0 (the kit's reset condition) is odd weight over one period. -/
theorem order_zero_iff {f : Nat → Bool} {v : Nat} (hv : 1 ≤ v) (hf : ∀ t, f (t + 2 ^ v) = f t) :
    order f (2 ^ v) = 0 ↔ xsum f 0 (2 ^ v) = true := by
  have h2 : 2 ≤ 2 ^ v := by
    obtain ⟨k, rfl⟩ : ∃ k, v = k + 1 := ⟨v - 1, by omega⟩
    rw [Nat.pow_succ]; have := Nat.one_le_two_pow (n := k); omega
  have key := le_order_iff (g := f) (L := 2 ^ v) (r := 1) (Nat.le_refl 1) (by omega)
  constructor
  · intro h0
    have hnot : ¬ Vanish (2 ^ v - 1) f := fun hvan => by have := key.mpr hvan; omega
    cases hx : xsum f 0 (2 ^ v)
    · exfalso; apply hnot; intro t
      rw [difs_pred_two_pow, xsum_period hf t, hx]
    · rfl
  · intro hx
    apply Nat.eq_zero_of_not_pos
    intro hpos
    have hvan := key.mp hpos
    have := hvan 0
    rw [difs_pred_two_pow, hx] at this
    exact Bool.noConfusion this

/-! ### The first column after a `11` pair has order at least `M - 2` -/

theorem vanish_of_antiperiod {s : Nat → Bool} {e : Nat} (hs : ∀ u, s (u + 2 ^ e) = !s u) :
    Vanish (2 ^ e + 1) s := by
  have hconst : difs (2 ^ e) s = fun _ => true := by
    rw [difs_two_pow]; funext t; rw [hs t]; cases s t <;> rfl
  intro t
  rw [Nat.add_comm, difs_add, hconst]
  rfl

/-- After a pair in which both columns double, with prefix period `M = 2 ^ e ≥ 4` before it, the next column has order
at least `M - 2` at length `4 M`, for every gate. -/
theorem after11_order (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {n : Nat}
    (h1 : prefixExp g x (n + 1) = prefixExp g x n + 1)
    (h2 : prefixExp g x (n + 1 + 1) = prefixExp g x (n + 1) + 1) (hM : 2 ≤ prefixExp g x n) :
    2 ^ prefixExp g x n - 2 ≤ order (col g x (n + 1 + 1 + 1)) (2 ^ (prefixExp g x n + 2)) := by
  have hs : ∀ u, col g x (n + 1) (u + 2 ^ prefixExp g x n) = !col g x (n + 1) u := col_antiperiod g x h1
  have hb : ∀ u, col g x (n + 1 + 1) (u + 2 ^ (prefixExp g x n + 1)) = !col g x (n + 1 + 1) u := by
    intro u; rw [← h1]; exact col_antiperiod g x h2 u
  have hs2 : ∀ u, col g x (n + 1) (u + 2 ^ (prefixExp g x n + 1)) = col g x (n + 1) u := by
    intro u; rw [Nat.pow_succ, Nat.mul_two]; exact antiperiod_twice hs u
  have hh : ∀ t, col g x (n + 1 + 1 + 1) (t + 1) =
      xor (col g x (n + 1 + 1 + 1) t) (g (n + 1 + 1) (col g x (n + 1 + 1) t) (col g x (n + 1) t)) := by
    intro t; rw [col_step]; rfl
  have hv : Vanish (2 ^ prefixExp g x n + 1) (col g x (n + 1)) := vanish_of_antiperiod hs
  have hpast := vanish_past_gate (g := g (n + 1 + 1)) hs2 hb hh (k := 2 ^ prefixExp g x n) hv
  have p4 : 2 ^ (prefixExp g x n + 2) = 4 * 2 ^ prefixExp g x n := by
    rw [Nat.pow_add]; omega
  have p2 : 2 ^ (prefixExp g x n + 1) = 2 * 2 ^ prefixExp g x n := by rw [Nat.pow_succ]; omega
  have p0 : 4 ≤ 2 ^ prefixExp g x n := by
    have := Nat.pow_le_pow_right (n := 2) (by decide) hM; simpa using this
  apply (le_order_iff (by omega) (by omega)).mpr
  rw [show 2 ^ (prefixExp g x n + 2) - (2 ^ prefixExp g x n - 2) =
      2 ^ prefixExp g x n + 1 + 1 + 2 ^ (prefixExp g x n + 1) by omega]
  exact hpast

/-! ### Pairs of bits

Pair `i` is bits `2i` and `2i + 1`, that is columns `2i + 1` and `2i + 2`. -/

/-- The first bit of pair `i` doubles the prefix period. -/
def fd (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat) : Prop :=
  prefixExp g x (2 * i + 1) = prefixExp g x (2 * i) + 1

/-- The last bit of pair `i` doubles the prefix period. -/
def ld (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat) : Prop :=
  prefixExp g x (2 * i + 1 + 1) = prefixExp g x (2 * i + 1) + 1

/-- The resource before pair `i`: the order of the previous pair's last bit over the prefix period. -/
noncomputable def res (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat) : Nat :=
  order (col g x (2 * i)) (2 ^ prefixExp g x (2 * i))

/-- The order of pair `i`'s first bit over its prefix period. -/
noncomputable def ford (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat) : Nat :=
  order (col g x (2 * i + 1)) (2 ^ prefixExp g x (2 * i + 1))

theorem two_mul_succ (i : Nat) : 2 * (i + 1) = 2 * i + 1 + 1 := by omega

theorem col_rec (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (n t : Nat) :
    col g x (n + 1 + 1) (t + 1) = xor (col g x (n + 1 + 1) t) (g (n + 1) (col g x (n + 1) t) (col g x n t)) := by
  rw [col_step]; rfl

theorem col_per (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (n t : Nat) :
    col g x n (t + 2 ^ prefixExp g x n) = col g x n t :=
  col_period_of_le g x (Nat.le_refl n) t

/-- A `11` pair needs resource 0 before it. -/
theorem res_zero_of_11 (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat}
    (hf : fd g x i) (hl : ld g x i) : res g x i = 0 := by
  unfold fd at hf; unfold ld at hl; unfold res
  have hanti : ∀ t, col g x (2 * i + 1 + 1) (t + 2 * 2 ^ prefixExp g x (2 * i)) = !col g x (2 * i + 1 + 1) t := by
    intro t
    have := col_antiperiod g x hl t
    rwa [hf, two_pow_succ'] at this
  exact order_reset_before_gate (col_per g x (2 * i)) (col_antiperiod g x hf) (col_rec g x (2 * i)) hanti

/-- A doubled last bit leaves order half the new prefix period minus one. -/
theorem res_after_ld (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat} (hl : ld g x i) :
    res g x (i + 1) = 2 ^ prefixExp g x (2 * i + 1) - 1 := by
  unfold ld at hl; unfold res
  rw [two_mul_succ, hl, two_pow_succ']
  exact order_of_antiperiod (col_antiperiod g x hl)

/-- A `10` pair lowers the resource by at most one. -/
theorem res_countdown (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat}
    (hf : fd g x i) (hl : ¬ ld g x i) : res g x i ≤ res g x (i + 1) + 1 := by
  unfold fd at hf; unfold ld at hl; unfold res
  have h0 : prefixExp g x (2 * i + 1 + 1) = prefixExp g x (2 * i + 1) := by
    rcases prefixExp_succ_cases g x (2 * i + 1) with h | h
    · exact h
    · exact absurd h hl
  rw [two_mul_succ, h0, hf, two_pow_succ']
  exact order_countdown_gate (col_per g x (2 * i)) (col_antiperiod g x hf) (col_rec g x (2 * i))

theorem not_fd_eq (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat} (h : ¬ fd g x i) :
    prefixExp g x (2 * i + 1) = prefixExp g x (2 * i) := by
  rcases prefixExp_succ_cases g x (2 * i) with e | e
  · exact e
  · exact absurd e h

/-- Between consecutive `01` pairs the first-bit order drops by at most one. -/
theorem ford_countdown (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat}
    (hl : ld g x i) (hf' : ¬ fd g x (i + 1)) : ford g x i ≤ ford g x (i + 1) + 1 := by
  unfold ld at hl; unfold ford
  have e1 := not_fd_eq g x hf'
  rw [two_mul_succ] at e1
  rw [two_mul_succ, e1, hl, two_pow_succ']
  exact order_countdown_gate (col_per g x (2 * i + 1)) (col_antiperiod g x hl) (col_rec g x (2 * i + 1))

/-- After a `01` pair with prefix period at least 2, a doubling of the next first bit needs first-bit order 0. -/
theorem ford_zero (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat} (hM : 1 ≤ prefixExp g x (2 * i))
    (hf : ¬ fd g x i) (hl : ld g x i) (hf' : fd g x (i + 1)) : ford g x i = 0 := by
  have h0 := not_fd_eq g x hf
  unfold ld at hl; unfold fd at hf'; unfold ford
  rw [two_mul_succ] at hf'
  have key := (after01_double_iff g x h0 hl hM).mp hf'
  have hx : xsum (col g x (2 * i + 1)) 0 (2 ^ prefixExp g x (2 * i)) = true := by
    cases h : xsum (col g x (2 * i + 1)) 0 (2 ^ prefixExp g x (2 * i)) <;> simp_all
  rw [h0]
  have hper : ∀ t, col g x (2 * i + 1) (t + 2 ^ prefixExp g x (2 * i)) = col g x (2 * i + 1) t := by
    intro t; rw [← h0]; exact col_per g x _ t
  exact (order_zero_iff hM hper).mpr hx

/-- No-three for pairs: after a `11` pair with prefix period at least 2, the next first bit does not double. -/
theorem no_three_pair (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat} (hM : 1 ≤ prefixExp g x (2 * i))
    (hf : fd g x i) (hl : ld g x i) : ¬ fd g x (i + 1) := by
  intro h
  unfold fd at hf h; unfold ld at hl
  rw [two_mul_succ] at h
  have := no_three g x hf hl hM
  omega

/-- After a `11` pair with prefix period `M ≥ 4`, the next first bit has order at least `M - 2`. -/
theorem ford_after_11 (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat} (hM : 2 ≤ prefixExp g x (2 * i))
    (hf : fd g x i) (hl : ld g x i) : 2 ^ prefixExp g x (2 * i) - 2 ≤ ford g x (i + 1) := by
  have hnf := no_three_pair g x (by omega) hf hl
  have e1 := not_fd_eq g x hnf
  unfold fd at hf; unfold ld at hl; unfold ford
  rw [two_mul_succ] at e1 ⊢
  rw [e1, hl, hf]
  exact after11_order g x hf hl hM

/-! ### Exponent steps by pairs -/

theorem pe_step (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (n : Nat) :
    prefixExp g x n ≤ prefixExp g x (n + 1) ∧ prefixExp g x (n + 1) ≤ prefixExp g x n + 1 := by
  rcases prefixExp_succ_cases g x n with h | h <;> omega

theorem E_pair (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat) :
    prefixExp g x (2 * i) ≤ prefixExp g x (2 * (i + 1)) ∧
      prefixExp g x (2 * (i + 1)) ≤ prefixExp g x (2 * i) + 2 := by
  rw [two_mul_succ]
  have a := pe_step g x (2 * i)
  have b := pe_step g x (2 * i + 1)
  omega

theorem pair_11 (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat)
    (h : prefixExp g x (2 * (i + 1)) = prefixExp g x (2 * i) + 2) : fd g x i ∧ ld g x i := by
  unfold fd ld
  rw [two_mul_succ] at h
  have a := pe_step g x (2 * i)
  have b := pe_step g x (2 * i + 1)
  constructor <;> omega

theorem pair_w1 (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat)
    (h : prefixExp g x (2 * (i + 1)) = prefixExp g x (2 * i) + 1) :
    (fd g x i ∧ ¬ ld g x i) ∨ (¬ fd g x i ∧ ld g x i) := by
  unfold fd ld
  rw [two_mul_succ] at h
  rcases prefixExp_succ_cases g x (2 * i) with a | a <;> rcases prefixExp_succ_cases g x (2 * i + 1) with b | b
  · omega
  · right; constructor <;> omega
  · left; constructor <;> omega
  · omega

/-! ### First and last visits, and chained countdowns -/

open Classical in
theorem exists_first {p : Nat → Prop} : ∀ n k, k ≤ n → p k → ∃ m, m ≤ k ∧ p m ∧ ∀ j, j < m → ¬ p j
  | 0, k, hk, hp => by
    have : k = 0 := by omega
    subst this
    exact ⟨0, Nat.le_refl 0, hp, fun j hj => absurd hj (Nat.not_lt_zero j)⟩
  | n + 1, k, hk, hp => by
    by_cases h : ∃ j, j < k ∧ p j
    · obtain ⟨j, hj, hpj⟩ := h
      obtain ⟨m, hm, hpm, hmin⟩ := exists_first n j (by omega) hpj
      exact ⟨m, by omega, hpm, hmin⟩
    · exact ⟨k, Nat.le_refl k, hp, fun j hj hpj => h ⟨j, hj, hpj⟩⟩

open Classical in
theorem exists_last_from {q : Nat → Prop} {a : Nat} (ha : q a) :
    ∀ P, a ≤ P → ∃ K, a ≤ K ∧ K ≤ P ∧ q K ∧ ∀ m, K < m → m ≤ P → ¬ q m
  | 0, h => by
    have : a = 0 := by omega
    subst this
    exact ⟨0, Nat.le_refl 0, Nat.le_refl 0, ha, fun m h1 h2 => by omega⟩
  | P + 1, h => by
    by_cases hq : q (P + 1)
    · exact ⟨P + 1, h, Nat.le_refl _, hq, fun m h1 h2 => by omega⟩
    · rcases Nat.lt_or_eq_of_le h with h' | h'
      · obtain ⟨K, hK0, hKP, hqK, hmax⟩ := exists_last_from ha P (by omega)
        refine ⟨K, hK0, by omega, hqK, fun m h1 h2 => ?_⟩
        rcases Nat.lt_or_eq_of_le h2 with h3 | h3
        · exact hmax m h1 (by omega)
        · rw [h3]; exact hq
      · rw [h'] at ha; exact absurd ha hq

theorem chain_le {f : Nat → Nat} (a : Nat) :
    ∀ d, (∀ i, a ≤ i → i < a + d → f i ≤ f (i + 1) + 1) → f a ≤ f (a + d) + d
  | 0, _ => by simp
  | d + 1, h => by
    have ih := chain_le a d (fun i h1 h2 => h i h1 (by omega))
    have := h (a + d) (by omega) (by omega)
    rw [show a + (d + 1) = a + d + 1 by omega]
    omega

/-! ### The nested threshold: excess 3 needs 2058 pairs -/

/-- If the first `2N` bits reach excess 3 (`E(2N) ≥ N + 3`) for the first time at `N`, then `N ≥ 2058`. -/
theorem first_excess_three (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {N : Nat}
    (hN : N + 3 ≤ prefixExp g x (2 * N)) (hfirst : ∀ m, m < N → prefixExp g x (2 * m) ≤ m + 2) :
    2058 ≤ N := by
  have z : prefixExp g x (2 * 0) = 0 := rfl
  obtain ⟨P, rfl⟩ : ∃ P, N = P + 1 := by
    rcases Nat.eq_zero_or_pos N with h | h
    · subst h; omega
    · exact ⟨N - 1, by omega⟩
  have hP := hfirst P (by omega)
  have hPP := E_pair g x P
  obtain ⟨hfP, hlP⟩ := pair_11 g x P (by omega)
  have eP : prefixExp g x (2 * P) = P + 2 := by omega
  -- the last visit to excess at most 1
  obtain ⟨K, -, hKP, hEK, hKmax⟩ := exists_last_from (q := fun m => prefixExp g x (2 * m) ≤ m + 1) (a := 0)
    (by show prefixExp g x (2 * 0) ≤ 0 + 1; omega) P (Nat.zero_le P)
  have hmid : ∀ m, K < m → m ≤ P → prefixExp g x (2 * m) = m + 2 := fun m h1 h2 => by
    have h3 := hKmax m h1 h2
    have h4 := hfirst m (by omega)
    omega
  have hKP' : K < P := by
    rcases Nat.lt_or_eq_of_le hKP with h | h
    · exact h
    · subst h; omega
  have eK1 := hmid (K + 1) (by omega) (by omega)
  have hKK := E_pair g x K
  have eK : prefixExp g x (2 * K) = K + 1 := by omega
  obtain ⟨hfK, hlK⟩ := pair_11 g x K (by omega)
  -- K ≥ 2
  have hK2 : 2 ≤ K := by
    rcases (by omega : K = 0 ∨ K = 1 ∨ 2 ≤ K) with h | h | h
    · subst h
      have a := pe_step g x 0
      have b := pe_step g x 1
      have z0 : prefixExp g x 0 = 0 := rfl
      simp at eK1 a b
      omega
    · subst h
      unfold fd at hfK; unfold ld at hlK
      have e2 : prefixExp g x 2 = 2 := eK
      have e3 : prefixExp g x 3 = prefixExp g x 2 + 1 := hfK
      have e4 : prefixExp g x 4 = prefixExp g x 3 + 1 := hlK
      have b0 : prefixExp g x 1 ≤ prefixExp g x 0 + 1 := (pe_step g x 0).2
      have b1 : prefixExp g x 2 ≤ prefixExp g x 1 + 1 := (pe_step g x 1).2
      have z0 : prefixExp g x 0 = 0 := rfl
      have h1 : prefixExp g x 1 = 1 := by omega
      have h3 : prefixExp g x 4 = prefixExp g x 3 :=
        no_three g x (n := 1) (show prefixExp g x 2 = prefixExp g x 1 + 1 by omega)
          (show prefixExp g x 3 = prefixExp g x 2 + 1 from e3) (by omega)
      omega
    · exact h
  have hM8 : 8 ≤ 2 ^ prefixExp g x (2 * K) := by
    rw [eK]
    have := Nat.pow_le_pow_right (n := 2) (by decide) (show 3 ≤ K + 1 by omega)
    simpa using this
  -- pairs strictly between K and P have weight one
  have hw1 : ∀ m, K < m → m < P → (fd g x m ∧ ¬ ld g x m) ∨ (¬ fd g x m ∧ ld g x m) := fun m h1 h2 =>
    pair_w1 g x m (by have := hmid m h1 (by omega); have := hmid (m + 1) (by omega) (by omega); omega)
  have hnf1 : ¬ fd g x (K + 1) := no_three_pair g x (by omega) hfK hlK
  have hK1P : K + 1 < P := by
    rcases Nat.lt_or_eq_of_le (show K + 1 ≤ P by omega) with h | h
    · exact h
    · exact absurd (h ▸ hfP) hnf1
  have hF1 := ford_after_11 g x (by omega : 2 ≤ prefixExp g x (2 * K)) hfK hlK
  -- the first doubled first bit after pair K
  obtain ⟨j, hjP, ⟨hjK, hfj⟩, hjmin⟩ := exists_first (p := fun j => K + 2 ≤ j ∧ fd g x j) P P
    (Nat.le_refl P) ⟨by omega, hfP⟩
  have h01 : ∀ m, K + 1 ≤ m → m < j → ¬ fd g x m ∧ ld g x m := fun m h1 h2 => by
    have hnf : ¬ fd g x m := by
      rcases Nat.lt_or_eq_of_le h1 with h | h
      · exact fun hf => hjmin m h2 ⟨by omega, hf⟩
      · exact h ▸ hnf1
    rcases hw1 m (by omega) (by omega) with h | h
    · exact absurd h.1 hnf
    · exact h
  have hchain := chain_le (f := ford g x) (K + 1) (j - 1 - (K + 1)) (fun i h1 h2 =>
    ford_countdown g x (h01 i h1 (by omega)).2 (h01 (i + 1) (by omega) (by omega)).1)
  rw [show K + 1 + (j - 1 - (K + 1)) = j - 1 by omega] at hchain
  have hFz : ford g x (j - 1) = 0 := by
    have hj1 : j - 1 + 1 = j := by omega
    have hE : 1 ≤ prefixExp g x (2 * (j - 1)) := by rw [hmid (j - 1) (by omega) (by omega)]; omega
    exact ford_zero g x hE (h01 (j - 1) (by omega) (by omega)).1 (h01 (j - 1) (by omega) (by omega)).2
      (by rw [hj1]; exact hfj)
  -- the last 01 pair
  obtain ⟨ell, hell0, hellP, ⟨hnfe, hle⟩, hellmax⟩ := exists_last_from (q := fun m => ¬ fd g x m ∧ ld g x m)
    (a := j - 1) (h01 (j - 1) (by omega) (by omega)) (P - 1) (by omega)
  have h10 : ∀ m, ell < m → m ≤ P - 1 → fd g x m ∧ ¬ ld g x m := fun m h1 h2 => by
    rcases hw1 m (by omega) (by omega) with h | h
    · exact h
    · exact absurd h (hellmax m h1 h2)
  have hR := res_after_ld g x hle
  have heE : prefixExp g x (2 * ell + 1) = ell + 2 := by
    rw [not_fd_eq g x hnfe]; exact hmid ell (by omega) (by omega)
  have hRchain := chain_le (f := res g x) (ell + 1) (P - (ell + 1)) (fun i h1 h2 =>
    res_countdown g x (h10 i (by omega) (by omega)).1 (h10 i (by omega) (by omega)).2)
  have hR0 := res_zero_of_11 g x hfP hlP
  rw [show ell + 1 + (P - (ell + 1)) = P by omega, hR0, hR, heE] at hRchain
  have hpow : 2048 ≤ 2 ^ (ell + 2) := by
    have := Nat.pow_le_pow_right (n := 2) (by decide) (show 11 ≤ ell + 2 by omega)
    simpa using this
  omega

/-- **Nested threshold**: for every family of two-input gates and every seed, the first `2m` bits have period
dividing `2 ^ (m + 2)` for every `m < 2058`. -/
theorem prefixExp_le_add_two (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) :
    ∀ m, m < 2058 → prefixExp g x (2 * m) ≤ m + 2 := by
  intro m hm
  apply Nat.le_of_not_lt
  intro hlt
  obtain ⟨N, hNm, hN, hmin⟩ := exists_first (p := fun N => N + 3 ≤ prefixExp g x (2 * N)) m m (Nat.le_refl m)
    (by omega)
  have := first_excess_three g x hN (fun k hk => by have := hmin k hk; omega)
  omega

end Rule30Submission
