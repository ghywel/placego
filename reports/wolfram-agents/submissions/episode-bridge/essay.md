---
Template: ComputationalEssay
Name: Episodes and eternal tails behind Rule 30's black edge: a finite criterion
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-03
Description: A partial result proved in core Lean on the kit's edge-code objects: for any periodic phase, every depth's longest episode behind a black right edge is finite if and only if no eternal point of any period follows the phase; an episode of lcm(2^B(k+2), p) ticks lasts for ever, so finiteness is a finite question; and an eventual tail is an eternal one.
Abstract: See abstract.txt.
Keywords: [rule 30, Rule 30 Prize, edge code, frozen ruler, phase, episode, eternal point, gate clock, prefix period, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261030-7b0d12: the half-rate bound on gate clocks](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-7b0d12)"]
---

## The question

Read a row of Rule 30 from its rightmost black cell, as the kit's `Rule30FrozenRuler` does. Bit $j$ of the **edge code**
is the cell $j$ places behind the edge, and the code evolves by the edge map $T$:

$$T(c)_0 = c_0, \qquad T(c)_1 = c_1 \oplus c_0, \qquad T(c)_{j+2} = c_{j+2} \oplus (c_{j+1} \lor c_j).$$

A **phase** $E$ is a family of depth columns $E_j(t)$ that obeys the same rule at every depth $j \ge 2$ and repeats in
time with period $p > 0$. The kit's eight-tick ether is one. An **episode** of $T$ ticks at depths $k, k + 1$ is a run
$t < T$ on which those two depths of a code follow the phase. How long can an episode behind a black edge be?

The kit answers this exactly for the eight-tick ether (`Rule30EtherEpisode`: the longest episode is
$\lfloor 2k/3 \rfloor + 4 - [k \equiv 0, 2 \bmod 6]$). For other phases the record has computed tables, not proofs.
This essay relates the question to a structural one, for every phase at once.

## The objects

On the kit's `iter` (the edge map's iterates), with $x_0$ = true for a black edge:

- `IsPhase E p`: $0 < p$, the rule at every depth $j + 2$, and $E_j(t + p) = E_j(t)$ for every $j$ and $t$.
- `Episode E k x a T`: for every $t < T$, `iter t x k = E k (t + a)` and `iter t x (k + 1) = E (k + 1) (t + a)`.
- `MFinite E k`: some $L$ bounds every episode at depth $k$ of every black-edge code at every alignment.
- `EternalTail E`: some black-edge code returns to itself after some $P > 0$ ticks and follows $E$ at every depth
  $\ge d$ and every time.

## The finite criterion

Bits $0 \ldots k + 1$ of every code are purely periodic from time 0, with period dividing $2^{B(k+2)}$, where
$B(n) = \lceil n/2 \rceil + Q(0, \lfloor n/2 \rfloor)$ is the kit's half-rate bound (`Rule30GateClocks.prefixExp_le_B`;
the edge map is the gate clock with OR). The phase has period $p$. So the episode condition has period

$$H(k, p) = \operatorname{lcm}\bigl(2^{B(k+2)}, p\bigr)$$

in $t$, for every code at once (`horizon`).

**Theorems.**
- `episode_extend`: an episode of $H(k, p)$ ticks lasts for ever.
- `eternal_of_long`: such an episode gives an eternal point. Keep bits $0 \ldots k + 1$, paste the phase beyond, and
  the code returns to itself after $H(k, p)$ ticks and follows $E$ at every depth $\ge k$.
- `mfinite_iff`: the longest episode at depth $k$ is finite **if and only if** no episode reaches $H(k, p)$ ticks,
  and it is then at most $H(k, p) - 1$.

So finiteness at a fixed depth is a finite question, with an explicit horizon. No pigeonhole over prefixes is needed;
the uniform prefix period replaces it.

## The bridge

**Theorem (`episode_bridge`).** For every phase,

$$\bigl(\forall k,\ \texttt{MFinite}\ E\ k\bigr) \iff \neg\, \texttt{EternalTail}\ E .$$

An eternal point gives an infinite episode at its own depth, and conversely an episode of $H(k, p)$ ticks gives an
eternal point. **`eternal_of_eventual`**: a pair that follows $E$ from some onset on, for ever, also gives an eternal
point. Behind a black edge, "eventually follows the phase" and "eternally follows it" are the same question.

## Two controls

- **The eight-tick ether, both ways.** `g8_mfinite` takes the kit's `episode_bound_all`, and `g8_no_eternal` takes the
  kit's `no_eventual_ether_pair`. `g8_mfinite_of_grounding` derives finiteness from grounding alone through the
  bridge, with the weaker bound $H(k, 8) - 1$.
- **A phase with an eternal tail.** The kit's rain code `rainA` returns after two ticks (`period_two_iff`), so its
  orbit is a phase whose episodes are unbounded at some depth (`rain_not_mfinite`). The bridge's other side is not
  vacuous.

## A computation

The longest episode of the eight-tick ether at depths $k, k + 1$, found by brute force over every black-edge prefix
(prefix autonomy makes bits beyond $k + 1$ irrelevant) and every phase alignment, against the kit's formula:

```wl
etherBit[i_, t_] := BitGet[{43, 202, 178, 172}[[Mod[i, 4] + 1]], Mod[t, 8]];
edgeStep[c_List] := Table[Which[j == 1, c[[1]], j == 2, BitXor[c[[2]], c[[1]]], True, BitXor[c[[j]], BitOr[c[[j - 1]], c[[j - 2]]]]], {j, Length[c]}];
lw[k_] := Floor[2 k/3] + 4 - Boole[MemberQ[{0, 2}, Mod[k, 6]]];
episode[c0_, k_, i_, q_, tmax_] := Module[{c = c0, t = 0},
  While[t < tmax && c[[k + 1]] == etherBit[k + i, t + q] && c[[k + 2]] == etherBit[k + 1 + i, t + q], c = edgeStep[c]; t++]; t];
longest[k_] := Max[Table[episode[Join[{1}, IntegerDigits[m, 2, k + 1]], k, i, q, lw[k] + 5], {m, 0, 2^(k + 1) - 1}, {i, 0, 3}, {q, 0, 7}]];
Grid[Prepend[Table[{k, longest[k], lw[k]}, {k, 1, 8}], {"k", "longest episode, brute force", "the kit's formula"}], Frame -> All]
```

The two columns agree. This reproduces a known result, and is shown as an illustration of finite episodes.

## Related work and what is new

- **The bridge** was proposed in our record by Cloud (CL676; the genealogy §38.2), and carried there by hand. Here it is
  a formal theorem on the kit's objects.
- **The kit.**
  - `Rule30EtherEpisode` gives the exact longest episode for the eight-tick ether. Its ether is Troy Lowry's, from kit
    PR 69.
  - `Rule30EtherGrounding` proves that no black-edge code follows that ether eventually.
  - `Rule30FrozenRuler` supplies the edge map and prefix autonomy.
  - `Rule30GateClocks` supplies the uniform prefix period. It is our earlier submission
    [R30-20261030-7b0d12](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-7b0d12).
- **New here, as a scoped comparison:** the formal statement for every periodic phase, the finite criterion with the
  explicit horizon $\operatorname{lcm}(2^{B(k+2)}, p)$, and "eventual is eternal".
- **Scope.** No finiteness is decided for any new phase. The record's other phases (period 16, the 480-state phase,
  period 1024) have computed episode tables, and the horizon makes their finiteness a finite question, but nothing
  here computes it. Nothing here concerns the centre column of the single-cell pattern or the Prize problems
  themselves.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit modules it builds on
(`Rule30FrozenRuler`, `Rule30GateClocks`, `Rule30EtherEpisode`, `Rule30EdgeStaircases`) at the verifier's kit commit
93d98bbe: the edge map as a gate clock, the uniform prefix period, phases and episodes, the horizon and the finite
criterion, the pasted eternal point, the bridge, and the two controls.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30FrozenRuler
import Ruliology.CellularAutomata.Rule30GateClocks
import Ruliology.CellularAutomata.Rule30EtherEpisode
import Ruliology.CellularAutomata.Rule30EdgeStaircases

/-!
# Episodes and eternal tails behind a black right edge

Read a row from its rightmost black cell as in `Rule30FrozenRuler`: bit `j` of an edge code is the
cell `j` places behind the edge, and `iter t x` is the code at time `t`. A **phase** `E` is a
family of depth columns that obeys the edge map at every depth `≥ 2` and has period `p` in time.
An **episode** of `T` ticks at depths `k, k + 1` with alignment `a` is a run `t < T` with
`iter t x k = E k (t + a)` and `iter t x (k + 1) = E (k + 1) (t + a)`.

* `episode_extend`: an episode of `horizon k p = lcm (2 ^ B (k + 2), p)` ticks lasts for ever.
  Bits `0 … k + 1` of every code have period dividing `2 ^ B (k + 2)` from time `0`
  (`Rule30GateClocks.prefixExp_le_B`, the edge map being the gate clock with OR), and `E` has period
  `p`, so the episode condition has period `horizon k p` in `t`.
* `eternal_of_long`: such an episode gives an **eternal point**: paste `E` beyond depth `k + 1`;
  the code returns to itself after `horizon k p` ticks and follows `E` at every depth `≥ k`.
* `eternal_of_eventual`: a pair that follows `E` from some onset on, for ever, also gives an eternal
  point; behind a black edge, eventual and eternal tails are the same question.
* `mfinite_iff`: the longest episode at depth `k` is finite iff no episode reaches
  `horizon k p` ticks, and then it is at most `horizon k p - 1`.
* `episode_bridge`: **every depth has a finite longest episode iff no eternal point of any period
  follows `E` below some depth.**
* `g8_mfinite`, `g8_no_eternal`, `g8_mfinite_of_grounding`: for the kit's eight-tick ether the
  bridge's two sides are the kit's `episode_bound_all` and `no_eventual_ether_pair`; the last
  derives finiteness from grounding alone, through the bridge.
* `rain_not_mfinite` (control): the orbit of the kit's period-two rain code `rainA` is a phase
  with an eternal tail, so some depth has episodes of every length; the bridge's other side is not
  vacuous.

The argument needs no pigeonhole: the uniform prefix period replaces it. Scope: one-sided edge
codes; nothing here concerns a fixed wall, the centre column or densities.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

set_option autoImplicit false

open Rule30FrozenRuler Rule30RecordCharge

/-! ### The edge map is a gate clock -/

/-- The OR gate at every depth. -/
def orGate : Nat → Bool → Bool → Bool := fun _ a b => a || b

theorem T_eq_step (c : Nat → Bool) : T c = Rule30GateClocks.step orGate c := by
  funext j
  match j with
  | 0 => simp [T, Rule30GateClocks.step, orGate]
  | 1 => simp [T, Rule30GateClocks.step, orGate]
  | j + 2 => rfl

theorem iter_eq_orbit (c : Nat → Bool) : ∀ t, iter t c = Rule30GateClocks.orbit orGate c t
  | 0 => rfl
  | t + 1 => by
    show T (iter t c) = Rule30GateClocks.step orGate (Rule30GateClocks.orbit orGate c t)
    rw [iter_eq_orbit c t, T_eq_step]

/-- **Uniform prefix period**: bit `j < n` of every code repeats after every `P` divisible by
`2 ^ B n`, from time `0`. -/
theorem prefix_period (c : Nat → Bool) (n : Nat) {j : Nat} (hj : j < n) (t : Nat) {P : Nat}
    (hP : 2 ^ B n ∣ P) : iter (t + P) c j = iter t c j := by
  have hle := (Rule30GateClocks.prefixExp_le_B orGate c n).1
  have hper : Rule30GateClocks.PrefixPer orGate c n P :=
    (Rule30GateClocks.prefix_period_iff orGate c n _).mpr (Nat.dvd_trans (Nat.pow_dvd_pow 2 hle) hP)
  have h := hper (j + 1) (by omega) t
  rw [iter_eq_orbit, iter_eq_orbit]
  exact h

/-! ### Phases, episodes, eternal tails -/

/-- A phase: columns obeying the edge map at every depth `≥ 2`, with period `p` in time. -/
structure IsPhase (E : Nat → Nat → Bool) (p : Nat) : Prop where
  pos : 0 < p
  step : ∀ j t, E (j + 2) (t + 1) = xor (E (j + 2) t) (E (j + 1) t || E j t)
  period : ∀ j t, E j (t + p) = E j t

theorem IsPhase.period_mul {E : Nat → Nat → Bool} {p : Nat} (hE : IsPhase E p) (j t : Nat) :
    ∀ m, E j (t + p * m) = E j t
  | 0 => by rw [Nat.mul_zero, Nat.add_zero]
  | m + 1 => by rw [Nat.mul_succ, ← Nat.add_assoc, hE.period, hE.period_mul j t m]

theorem IsPhase.period_dvd {E : Nat → Nat → Bool} {p : Nat} (hE : IsPhase E p) (j t : Nat) {P : Nat}
    (hP : p ∣ P) : E j (t + P) = E j t := by
  obtain ⟨m, rfl⟩ := hP
  exact hE.period_mul j t m

/-- An episode of `T` ticks at depths `k, k + 1`, alignment `a`, onset `0`. -/
def Episode (E : Nat → Nat → Bool) (k : Nat) (x : Nat → Bool) (a T : Nat) : Prop :=
  ∀ t, t < T → iter t x k = E k (t + a) ∧ iter t x (k + 1) = E (k + 1) (t + a)

/-- The longest episode at depth `k` behind a black edge is finite: at most `L` ticks. -/
def MFinite (E : Nat → Nat → Bool) (k : Nat) : Prop :=
  ∃ L, ∀ (x : Nat → Bool) (a : Nat), x 0 = true → ¬ Episode E k x a (L + 1)

/-- An eternal point following `E`: a black-edge code of some period `P` whose depths `≥ d`
follow `E` at every time. -/
def EternalTail (E : Nat → Nat → Bool) : Prop :=
  ∃ (x : Nat → Bool) (P d a : Nat), x 0 = true ∧ 0 < P ∧ iter P x = x ∧
    ∀ j, d ≤ j → ∀ t, iter t x j = E j (t + a)

/-- The horizon `lcm (2 ^ B (k + 2), p)`: a common period of bits `0 … k + 1` of every code and of
the phase. -/
abbrev horizon (k p : Nat) : Nat := Nat.lcm (2 ^ B (k + 2)) p

theorem horizon_pos {p : Nat} (hp : 0 < p) (k : Nat) : 0 < horizon k p :=
  Nat.pos_iff_ne_zero.mpr (Nat.lcm_ne_zero (Nat.pos_iff_ne_zero.mp (Nat.two_pow_pos _))
    (Nat.pos_iff_ne_zero.mp hp))

/-- The horizon is at most the product `2 ^ B (k + 2) * p`; for `p = 2 ^ r` it is `2 ^ max (B (k + 2)) r`. -/
theorem horizon_dvd_prod (k p : Nat) : horizon k p ∣ 2 ^ B (k + 2) * p :=
  Nat.lcm_dvd (Nat.dvd_mul_right _ _) (Nat.dvd_mul_left _ _)

/-- **An episode of `horizon k p` ticks lasts for ever.** -/
theorem episode_extend {E : Nat → Nat → Bool} {p : Nat} (hE : IsPhase E p) {k : Nat}
    {x : Nat → Bool} {a : Nat} (h : Episode E k x a (horizon k p)) :
    ∀ t, iter t x k = E k (t + a) ∧ iter t x (k + 1) = E (k + 1) (t + a) := by
  intro t
  obtain ⟨r, m, hr, rfl⟩ : ∃ r m, r < horizon k p ∧ t = r + horizon k p * m :=
    ⟨_, _, Nat.mod_lt t (horizon_pos hE.pos k), (Nat.mod_add_div t _).symm⟩
  have hi : ∀ j, j < k + 2 → iter (r + horizon k p * m) x j = iter r x j := fun j hj =>
    prefix_period x (k + 2) hj r (Nat.dvd_trans (Nat.dvd_lcm_left _ _) (Nat.dvd_mul_right _ _))
  have he : ∀ j, E j (r + horizon k p * m + a) = E j (r + a) := by
    intro j
    rw [Nat.add_right_comm]
    exact hE.period_dvd j (r + a) (Nat.dvd_trans (Nat.dvd_lcm_right _ _) (Nat.dvd_mul_right _ _))
  rw [hi k (by omega), hi (k + 1) (by omega), he, he]
  exact h r hr

/-! ### The pasted point -/

/-- Keep bits `0 … k + 1` and paste the phase at alignment `a` beyond. -/
def paste (E : Nat → Nat → Bool) (k : Nat) (x : Nat → Bool) (a : Nat) : Nat → Bool :=
  fun j => if j < k + 2 then x j else E j a

theorem paste_agree (E : Nat → Nat → Bool) (k : Nat) (x : Nat → Bool) (a : Nat) :
    AgreeBelow (k + 2) x (paste E k x a) := by
  intro i hi
  simp [paste, hi]

/-- An infinite episode makes every depth `≥ k` of the pasted point follow `E` for ever. -/
theorem paste_tail {E : Nat → Nat → Bool} {p : Nat} (hE : IsPhase E p) {k : Nat}
    {x : Nat → Bool} {a : Nat}
    (hep : ∀ t, iter t x k = E k (t + a) ∧ iter t x (k + 1) = E (k + 1) (t + a)) :
    ∀ n t, iter t (paste E k x a) (k + n) = E (k + n) (t + a) := by
  have hag := iter_agree (paste_agree E k x a)
  have pair : ∀ n, (∀ t, iter t (paste E k x a) (k + n) = E (k + n) (t + a)) ∧
      (∀ t, iter t (paste E k x a) (k + n + 1) = E (k + n + 1) (t + a)) := by
    intro n
    induction n with
    | zero =>
      refine ⟨fun t => ?_, fun t => ?_⟩
      · rw [Nat.add_zero, ← hag t k (by omega)]
        exact (hep t).1
      · rw [Nat.add_zero, ← hag t (k + 1) (by omega)]
        exact (hep t).2
    | succ n ih =>
      refine ⟨fun t => by rw [← Nat.add_assoc]; exact ih.2 t, ?_⟩
      have e : k + (n + 1) + 1 = k + n + 2 := by omega
      rw [e]
      intro t
      induction t with
      | zero =>
        show paste E k x a (k + n + 2) = E (k + n + 2) (0 + a)
        have hlt : ¬ k + n + 2 < k + 2 := by omega
        simp [paste, hlt]
      | succ t iht =>
        show xor (iter t (paste E k x a) (k + n + 2))
            (iter t (paste E k x a) (k + n + 1) || iter t (paste E k x a) (k + n)) =
          E (k + n + 2) (t + 1 + a)
        rw [iht, ih.2 t, ih.1 t, Nat.add_right_comm t 1 a, hE.step]
  exact fun n => (pair n).1

/-- **An episode of `horizon k p` ticks gives an eternal point** of period `horizon k p`
following `E` at every depth `≥ k`. -/
theorem eternal_of_long {E : Nat → Nat → Bool} {p : Nat} (hE : IsPhase E p) {k : Nat}
    {x : Nat → Bool} {a : Nat} (hx : x 0 = true) (h : Episode E k x a (horizon k p)) :
    EternalTail E := by
  have htail := paste_tail hE (episode_extend hE h)
  refine ⟨paste E k x a, horizon k p, k, a, ?_, horizon_pos hE.pos k, ?_, ?_⟩
  · simp [paste, hx]
  · funext j
    by_cases hj : j < k + 2
    · have := prefix_period (paste E k x a) (k + 2) hj 0 (Nat.dvd_lcm_left (2 ^ B (k + 2)) p)
      rw [Nat.zero_add] at this
      exact this
    · obtain ⟨n, rfl⟩ : ∃ n, j = k + n := ⟨j - k, by omega⟩
      rw [htail n]
      show E (k + n) (horizon k p + a) = if k + n < k + 2 then x (k + n) else E (k + n) a
      simp only [hj, ↓reduceIte]
      rw [Nat.add_comm (horizon k p) a]
      exact hE.period_dvd (k + n) a (Nat.dvd_lcm_right _ _)
  · intro j hj t
    obtain ⟨n, rfl⟩ : ∃ n, j = k + n := ⟨j - k, (Nat.add_sub_of_le hj).symm⟩
    exact htail n t

/-- **Eventual is eternal**: a pair following `E` from onset `s` on gives an eternal point. -/
theorem eternal_of_eventual {E : Nat → Nat → Bool} {p : Nat} (hE : IsPhase E p) {k s a : Nat}
    {x : Nat → Bool} (hx : x 0 = true)
    (h : ∀ t, s ≤ t → iter t x k = E k (t + a) ∧ iter t x (k + 1) = E (k + 1) (t + a)) :
    EternalTail E := by
  refine eternal_of_long hE (k := k) (x := iter s x) (a := s + a) (by rw [iter_zero]; exact hx) ?_
  intro t _
  have := h (s + t) (by omega)
  have e : s + t + a = t + (s + a) := by omega
  rw [iter_add, e] at this
  exact this

/-! ### The bridge -/

/-- **The finite criterion**: the longest episode at depth `k` is finite iff no episode reaches
`horizon k p` ticks; then every episode is shorter than that. -/
theorem mfinite_iff {E : Nat → Nat → Bool} {p : Nat} (hE : IsPhase E p) (k : Nat) :
    MFinite E k ↔ ∀ (x : Nat → Bool) (a : Nat), x 0 = true → ¬ Episode E k x a (horizon k p) := by
  constructor
  · rintro ⟨L, hL⟩ x a hx h
    exact hL x a hx (fun t _ => episode_extend hE h t)
  · intro h
    refine ⟨horizon k p - 1, fun x a hx hep => h x a hx ?_⟩
    rwa [Nat.sub_add_cancel (horizon_pos hE.pos k)] at hep

/-- **The episode bridge**: every depth has a finite longest episode iff no eternal point of any
period follows `E` below some depth. -/
theorem episode_bridge {E : Nat → Nat → Bool} {p : Nat} (hE : IsPhase E p) :
    (∀ k, MFinite E k) ↔ ¬ EternalTail E := by
  constructor
  · rintro hM ⟨x, P, d, a, hx, -, -, htail⟩
    obtain ⟨L, hL⟩ := hM d
    exact hL x a hx (fun t _ => ⟨htail d (Nat.le_refl d) t, htail (d + 1) (by omega) t⟩)
  · intro hnot k
    exact (mfinite_iff hE k).mpr (fun x a hx h => hnot (eternal_of_long hE hx h))

/-! ### The eight-tick ether: both sides are the kit's -/

open Rule30EtherGrounding (ether ether_step no_eventual_ether_pair)

/-- The kit's ether as a phase: depth `j` follows `ether (j + i) (· + q)`. -/
def g8 (i q : Nat) : Nat → Nat → Bool := fun j t => ether (j + i) (t + q)

theorem ether_add_four (m t : Nat) : ether (m + 4) t = ether m t := by
  simp only [ether, Nat.add_mod_right]

theorem ether_add_eight (m t : Nat) : ether m (t + 8) = ether m t := by
  simp only [ether, Nat.add_mod_right]

theorem g8_phase (i q : Nat) : IsPhase (g8 i q) 8 where
  pos := by decide
  step j t := by
    show ether (j + 2 + i) (t + 1 + q) =
      xor (ether (j + 2 + i) (t + q)) (ether (j + 1 + i) (t + q) || ether (j + i) (t + q))
    rw [Nat.add_right_comm t 1 q, ether_step]
    have h3 : j + 2 + i + 3 = j + 1 + i + 4 := by omega
    have h2 : j + 2 + i + 2 = j + i + 4 := by omega
    rw [h3, h2, ether_add_four, ether_add_four]
  period j t := by
    show ether (j + i) (t + 8 + q) = ether (j + i) (t + q)
    rw [Nat.add_right_comm, ether_add_eight]

/-- Every depth's longest G8 episode is finite: the kit's `episode_bound_all`. -/
theorem g8_mfinite (i q : Nat) : ∀ k, MFinite (g8 i q) k := by
  intro k
  refine ⟨Rule30EtherEpisode.Lw k, fun x a hx hep => ?_⟩
  apply Rule30EtherEpisode.episode_bound_all x hx k (k + i) (a + q) 0
  intro t _ ht
  have := hep t (by omega)
  simp only [g8] at this
  rw [Nat.add_right_comm k i 1, ← Nat.add_assoc t a q]
  exact this

/-- No eternal point follows the G8 ether: the kit's `no_eventual_ether_pair`. -/
theorem g8_no_eternal (i q : Nat) : ¬ EternalTail (g8 i q) := by
  rintro ⟨x, P, d, a, hx, -, -, htail⟩
  apply no_eventual_ether_pair x hx d (d + i) (a + q)
  refine ⟨0, fun t _ => ⟨?_, ?_⟩⟩
  · rw [htail d (Nat.le_refl d) t]
    show ether (d + i) (t + a + q) = ether (d + i) (t + (a + q))
    rw [Nat.add_assoc t a q]
  · rw [htail (d + 1) (by omega) t]
    show ether (d + 1 + i) (t + a + q) = ether (d + i + 1) (t + (a + q))
    rw [Nat.add_assoc t a q, Nat.add_right_comm d 1 i]

/-- Finiteness from grounding alone, through the bridge (bound `horizon k 8 - 1`). -/
theorem g8_mfinite_of_grounding (i q : Nat) : ∀ k, MFinite (g8 i q) k :=
  (episode_bridge (g8_phase i q)).mpr (g8_no_eternal i q)

/-! ### Control: a phase with an eternal tail -/

/-- The orbit of a periodic code is a phase. -/
theorem self_phase (c : Nat → Bool) {P : Nat} (hP : 0 < P) (hc : iter P c = c) :
    IsPhase (fun j t => iter t c j) P where
  pos := hP
  step _ _ := rfl
  period j t := by
    show iter (t + P) c j = iter t c j
    rw [Nat.add_comm, iter_add, hc]

theorem self_eternal (c : Nat → Bool) {P : Nat} (hP : 0 < P) (hc : iter P c = c)
    (h0 : c 0 = true) : EternalTail (fun j t => iter t c j) :=
  ⟨c, P, 0, 0, h0, hP, hc, fun _ _ _ => rfl⟩

/-- The rain code `rainA` (`1 0 1 0 …`, the kit's `Rule30EdgeStaircases`) returns after two
ticks, so its phase has episodes of every length at some depth. -/
theorem rain_not_mfinite :
    ¬ ∀ k, MFinite (fun j t => iter t Rule30EdgeStaircases.rainA j) k := by
  have h2 : iter 2 Rule30EdgeStaircases.rainA = Rule30EdgeStaircases.rainA :=
    (Rule30EdgeStaircases.period_two_iff _ rfl).mpr (Or.inl rfl)
  exact fun h => (episode_bridge (self_phase _ (by decide) h2)).mp h
    (self_eternal _ (by decide) h2 rfl)

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30FrozenRuler"};
heads = {"episode_bridge", "mfinite_iff", "episode_extend", "eternal_of_long", "eternal_of_eventual", "rain_not_mfinite"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The horizon, as defined in the module:

```wl
show[{"horizon"}, "TermForm"]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it
resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.episode_bridge"]["KernelCheck"]
```
