---
Template: ComputationalEssay
Name: Light-speed periodic rings of rule 30 as closed walks of periodic profiles
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-29
Description: A partial result about rule 30 on rings, proved in core Lean: configurations that return moved one cell per step are exactly closed walks of periodic time profiles, and at period two they are white or alternating
Abstract: Read rule 30 in the frame that moves one cell right per step, Phi x i = x i XOR (x (i+1) OR x (i+2)). Then the P-th iterate is the kit's evolution moved P cells (`Rule30Submission.orbit_eq_iff`), so Phi^P x = x says that x returns after P steps moved P cells right: velocity one, outside the range [-1, 1) that the kit's PeriodicPoints covers. A ring of size m is an m-periodic configuration. We prove that the rings of size m with Phi^P x = x correspond bijectively, by explicit inverse maps, to closed walks of length m in the graph of P-periodic profiles, where consecutive sites obey the right-diagonal recurrence (`Rule30Submission.encode_walk`, `Rule30Submission.decode_ring`, `Rule30Submission.decode_encode`, `Rule30Submission.encode_decode`). The identities hold for every P and m; their finite-graph reading needs P and m positive. At period two the classification is complete for every positive ring size: Phi^2 x = x exactly for the white ring and the alternating rings (`Rule30Submission.ring_period_two`), alternating rings have even size (`Rule30Submission.alternating_even`), and only white is fixed by Phi (`Rule30Submission.ring_fixed`). The period-two rings are therefore the restrictions of rule 30's three fixed points. No classification is claimed for larger periods, and nothing here concerns the centre column.
Keywords: [rule 30, Rule 30 Prize, periodic orbits, rings, light speed, closed walks, right diagonals, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[PeriodicPoints in the kit](https://github.com/WolframInstitute/Rule30PrizeKit/blob/main/equivalents/Rule30Equivalents/PeriodicPoints.lean)"]
---

## The question

The kit's `Rule30Equivalents.PeriodicPoints` shows that a configuration with $F^k x = \sigma^d x$ and
$1 - k \le d \le k$, a pattern moving at a velocity in $[-1, 1)$, is spatially periodic. The other end of the
light cone, velocity one, is left open there: a pattern that returns after $P$ steps moved $P$ cells right. On the
line such patterns need not be spatially periodic. A black right edge with the rain pattern behind it is one of
them. This essay treats the finite version, rings, and asks what such a returning ring looks like.

## The moving frame

Write $\Phi x\,(i) = x(i) \oplus \bigl(x(i+1) \lor x(i+2)\bigr)$ for one step of rule 30 read in the frame that
moves one cell right per step, and `orbit x t` for $\Phi^t x$. Then

$$\Phi^t x\,(i) = x_t(i + t),$$

where $x_t$ is the kit's `Rule30Realization.evol` (`orbit_evol`). So $\Phi^P x = x$ says exactly that the kit's
evolution returns $x$ moved $P$ cells right after $P$ steps (`orbit_eq_iff`).

## Rings and closed walks

A ring of size $m$ is an $m$-periodic configuration: $x(i + m) = x(i)$. Follow each cell's column in the moving
frame: $C_i(t) = \Phi^t x\,(i)$. Reading the columns from right to left, $A_d = C_{-d}$, the rule becomes the
right-diagonal recurrence

$$A_d(t+1) = A_d(t) \oplus \bigl(A_{d-1}(t) \lor A_{d-2}(t)\bigr).$$

If $\Phi^P x = x$, each $A_d$ has period $P$, and $A_{d+m} = A_d$. So the profiles form a closed walk of length
$m$ in the graph whose states are pairs of $P$-periodic words and whose edges are this recurrence (`Walk`).
Conversely, a closed walk gives the ring $x(i) = A_{-i}(0)$, and induction on time recovers every profile. The
two maps `encode` and `decode` are inverse to each other (`encode_walk`, `decode_ring`, `decode_encode`,
`encode_decode`). The walk keeps a marked start and labelled sites; no minimal period is assumed, and no rotation
is quotiented out.

The identities hold for every $P$ and $m$. Reading them as closed walks in the finite graph of $P$-periodic
words, on a finite ring, needs $P > 0$ and $m > 0$, since at $0$ the periodicity condition is vacuous.

## Period two

At $P = 2$ the classification is complete for every positive ring size (`ring_period_two`): $\Phi^2 x = x$
exactly when $x$ is white or alternating.
- **A zero pair.** Suppose $x(j+1) = x(j+2) = 0$. Because $\Phi(\Phi x) = x$, the OR
  $x(j+1) \lor x(j+2)$ equals $\Phi x\,(j+1) \lor \Phi x\,(j+2)$. So $\Phi x\,(j+1) = 0$, and with the zero
  pair $\Phi x\,(j+1) = x(j+3)$, so $x(j+3) = 0$. The zeros then run to the right, and periodicity carries them
  round the whole ring (`zero_pair_next`).
- **No zero pair.** Then $\Phi$ complements $x$, and returning after two steps excludes a black pair, so
  neighbours always differ.
- **Converses and parity.** White is fixed, and an alternating ring is complemented twice. An alternating ring
  has even size (`alternating_even`), and only white is fixed by $\Phi$ (`ring_fixed`).

An alternating ring is fixed by rule 30 itself, with no shift. So the period-two rings at light speed are the
restrictions to rings of rule 30's three fixed points: white and the two phases of $\dots 0101 \dots$
(`Rule30Equivalents.PeriodicPoints.evol_one_eq_self_iff` in the kit).

## A computation

The Wolfram Language counts, for ring sizes 1 to 12, the configurations with $\Phi^2 x = x$, and shows that the
ring $0001$ first returns after eight steps.

```wl
phi[x_List] := BitXor[x, BitOr[RotateLeft[x, 1], RotateLeft[x, 2]]];
<|"rings of size 1 to 12 with Phi^2 x = x" -> Table[Count[Tuples[{0, 1}, m], x_ /; Nest[phi, x, 2] === x], {m, 12}],
  "first return of the ring 0001" -> SelectFirst[Range[32], Nest[phi, {0, 0, 0, 1}, #] === {0, 0, 0, 1} &]|>
```

The counts are one for each odd size, white, and three for each even size, white and the two alternating
phases, as `ring_period_two` and `alternating_even` predict. The ring $0001$ shows that larger periods carry
other orbits. Their classification is not attempted here.

## The formal proof

The module, built against the kit at the verifier's commit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30Realization

/-!
# Rule 30: light-speed periodic orbits of rings are closed walks of periodic profiles

Read rule 30 in the frame that moves one cell right per step: `Phi x i = x i xor (x (i+1) || x (i+2))`, and
`orbit x t` is its `t`-th iterate. Then `orbit x t i = evol x t (i + t)` (`orbit_evol`), so `orbit x P = x` says
that the configuration returns to itself moved `P` cells right after `P` steps of the kit's
`Rule30Realization.evol` (`orbit_eq_iff`).

A ring of size `m` is an `m`-periodic configuration (`Per m x`). A closed walk of length `m` in the graph of
`P`-periodic profiles is a family `A d t` of time profiles, one per site `d`, with `A (d + m) = A d`, each of
period `P`, and `A d (t+1) = A d t xor (A (d-1) t || A (d-2) t)`, the right-diagonal recurrence (`Walk`).

* `encode_walk`, `decode_ring`, `decode_encode`, `encode_decode`: `encode x d t = orbit x t (-d)` and
  `decode A i = A (-i) 0` are inverse bijections between the rings of size `m` with `orbit x P = x` and the closed
  walks of length `m`. The identities hold for every `P` and `m`; reading them as closed walks in the finite graph
  of `P`-periodic words, on a finite ring, needs `0 < P` and `0 < m`, since at `0` the periodicity condition is
  vacuous. The walk has a marked start and labelled sites; no minimal period and no rotation quotient is taken.
* `ring_fixed`: `Phi x = x` only for the white configuration.
* `ring_period_two`: on a ring of positive size, `orbit x 2 = x` exactly for the white configuration and the
  alternating ones, and `alternating_even`: an alternating ring has even size. A zero pair forces the next zero, so
  one pair empties the whole ring; with no zero pair, `Phi` complements, and returning excludes a black pair.
-/


namespace Rule30Submission

open Ruliology.CellularAutomata

/-- One step of rule 30 in the frame that moves one cell right per step. -/
def Phi (x : Int → Bool) (i : Int) : Bool := xor (x i) (x (i + 1) || x (i + 2))

/-- `t` steps of `Phi`. -/
def orbit (x : Int → Bool) : Nat → Int → Bool
  | 0 => x
  | t + 1 => Phi (orbit x t)

/-- `x` is a ring of size `m`: it repeats every `m` cells. -/
def Per (m : Nat) (x : Int → Bool) : Prop := ∀ i, x (i + m) = x i

/-- A closed walk of length `m` in the graph of `P`-periodic profiles: site `d` carries the time profile
`A d`. -/
def Walk (P m : Nat) (A : Int → Nat → Bool) : Prop :=
  (∀ d t, A (d + m) t = A d t) ∧ (∀ d t, A d (t + P) = A d t) ∧
    ∀ d t, A d (t + 1) = xor (A d t) (A (d - 1) t || A (d - 2) t)

/-- The walk of a ring: site `d` carries the time profile of cell `-d`. -/
def encode (x : Int → Bool) (d : Int) (t : Nat) : Bool := orbit x t (-d)

/-- The ring of a walk: cell `i` is the start of the profile at site `-i`. -/
def decode (A : Int → Nat → Bool) (i : Int) : Bool := A (-i) 0

/-! ### The moving frame and the kit's evolution -/

theorem orbit_evol (x : Int → Bool) (t : Nat) (i : Int) :
    orbit x t i = Rule30Realization.evol x t (i + t) := by
  induction t generalizing i with
  | zero => simp [orbit, Rule30Realization.evol]
  | succ t ih =>
    show xor (orbit x t i) (orbit x t (i + 1) || orbit x t (i + 2)) = _
    rw [ih, ih, ih]
    show _ = Rule30Jen.rule (Rule30Realization.evol x t (i + ((t + 1 : Nat) : Int) - 1))
      (Rule30Realization.evol x t (i + ((t + 1 : Nat) : Int)))
      (Rule30Realization.evol x t (i + ((t + 1 : Nat) : Int) + 1))
    have h1 : i + ((t + 1 : Nat) : Int) - 1 = i + t := by omega
    have h2 : i + ((t + 1 : Nat) : Int) = i + 1 + t := by omega
    have h3 : i + ((t + 1 : Nat) : Int) + 1 = i + 2 + t := by omega
    rw [h1, h3, h2]
    rfl

/-- **Light-speed recurrence**: `orbit x P = x` says the kit's evolution returns `x` moved `P` cells right. -/
theorem orbit_eq_iff (x : Int → Bool) (P : Nat) :
    orbit x P = x ↔ ∀ i, Rule30Realization.evol x P (i + P) = x i := by
  constructor
  · intro h i
    rw [← orbit_evol, h]
  · intro h
    funext i
    rw [orbit_evol, h]

theorem orbit_add (x : Int → Bool) (s t : Nat) : orbit x (s + t) = orbit (orbit x s) t := by
  induction t with
  | zero => rfl
  | succ t ih => show Phi (orbit x (s + t)) = Phi (orbit (orbit x s) t); rw [ih]

theorem per_phi {m : Nat} {x : Int → Bool} (h : Per m x) : Per m (Phi x) := by
  intro i
  unfold Phi
  rw [show i + m + 1 = (i + 1) + m by omega, show i + m + 2 = (i + 2) + m by omega, h, h, h]

theorem per_orbit {m : Nat} {x : Int → Bool} (h : Per m x) (t : Nat) : Per m (orbit x t) := by
  induction t with
  | zero => exact h
  | succ t ih => exact per_phi ih

/-! ### Rings and closed walks -/

/-- A ring that returns after `P` steps gives a closed walk of length `m`. -/
theorem encode_walk {P m : Nat} {x : Int → Bool} (hx : Per m x) (hP : orbit x P = x) :
    Walk P m (encode x) := by
  refine ⟨fun d t => ?_, fun d t => ?_, fun d t => ?_⟩
  · unfold encode
    have h := per_orbit hx t (-(d + m))
    rw [show -(d + m) + m = -d by omega] at h
    exact h.symm
  · unfold encode
    rw [Nat.add_comm, orbit_add, hP]
  · unfold encode
    show xor (orbit x t (-d)) (orbit x t (-d + 1) || orbit x t (-d + 2)) = _
    rw [show -d + 1 = -(d - 1) by omega, show -d + 2 = -(d - 2) by omega]

theorem orbit_decode {P m : Nat} {A : Int → Nat → Bool} (hA : Walk P m A) (t : Nat) (i : Int) :
    orbit (decode A) t i = A (-i) t := by
  induction t generalizing i with
  | zero => rfl
  | succ t ih =>
    show xor (orbit (decode A) t i) (orbit (decode A) t (i + 1) || orbit (decode A) t (i + 2)) = _
    rw [ih, ih, ih, hA.2.2 (-i) t, show -(i + 1) = -i - 1 by omega, show -(i + 2) = -i - 2 by omega]

/-- A closed walk of length `m` gives a ring of size `m` that returns after `P` steps. -/
theorem decode_ring {P m : Nat} {A : Int → Nat → Bool} (hA : Walk P m A) :
    Per m (decode A) ∧ orbit (decode A) P = decode A := by
  refine ⟨fun i => ?_, ?_⟩
  · unfold decode
    have h := hA.1 (-(i + m)) 0
    rw [show -(i + m) + m = -i by omega] at h
    exact h.symm
  · funext i
    rw [orbit_decode hA P i]
    unfold decode
    have h := hA.2.1 (-i) 0
    rw [Nat.zero_add] at h
    exact h

theorem decode_encode (x : Int → Bool) : decode (encode x) = x := by
  funext i
  show orbit x 0 (-(-i)) = x i
  rw [Int.neg_neg]
  rfl

theorem encode_decode {P m : Nat} {A : Int → Nat → Bool} (hA : Walk P m A) : encode (decode A) = A := by
  funext d t
  show orbit (decode A) t (-d) = A d t
  rw [orbit_decode hA t (-d), Int.neg_neg]

/-! ### Period one and period two -/

/-- The white configuration is the only fixed point of `Phi`. -/
theorem ring_fixed (x : Int → Bool) : Phi x = x ↔ ∀ i, x i = false := by
  constructor
  · intro h i
    have h1 : xor (x (i - 1)) (x (i - 1 + 1) || x (i - 1 + 2)) = x (i - 1) := congrFun h (i - 1)
    rw [show i - 1 + 1 = i by omega] at h1
    cases hi : x i <;> cases hc : x (i - 1) <;> simp_all
  · intro h
    funext i
    simp [Phi, h]

theorem xor_cancel {a g h : Bool} (e : xor (xor a g) h = a) : g = h := by
  cases a <;> cases g <;> cases h <;> simp_all

/-- Two zeros in a row force the next zero, for a configuration that returns after two steps. -/
theorem zero_pair_next {x : Int → Bool} (h : Phi (Phi x) = x) (j : Int)
    (h1 : x (j + 1) = false) (h2 : x (j + 2) = false) : x (j + 3) = false := by
  have hj : xor (xor (x j) (x (j + 1) || x (j + 2))) (Phi x (j + 1) || Phi x (j + 2)) = x j :=
    congrFun h j
  have hg := xor_cancel hj
  rw [h1, h2] at hg
  have hy : Phi x (j + 1) = false := by
    cases hc : Phi x (j + 1) <;> simp_all
  have hy' : Phi x (j + 1) = xor (x (j + 1)) (x (j + 1 + 1) || x (j + 1 + 2)) := rfl
  rw [hy', h1, show j + 1 + 1 = j + 2 by omega, h2, show j + 1 + 2 = j + 3 by omega] at hy
  simpa using hy

theorem per_add_mul {m : Nat} {x : Int → Bool} (h : Per m x) (i : Int) (k : Nat) :
    x (i + (k * m : Nat)) = x i := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Nat.add_mul, Nat.one_mul, Int.natCast_add, ← Int.add_assoc, h, ih]

/-- **Period two on a ring**: a ring of positive size returns after two steps exactly when it is white or
alternating. -/
theorem ring_period_two {m : Nat} (hm : 0 < m) {x : Int → Bool} (hx : Per m x) :
    orbit x 2 = x ↔ (∀ i, x i = false) ∨ (∀ i, x (i + 1) = !x i) := by
  constructor
  · intro h2
    have h : Phi (Phi x) = x := h2
    by_cases hz : ∃ j, x (j + 1) = false ∧ x (j + 2) = false
    · left
      obtain ⟨j, hj1, hj2⟩ := hz
      have hrun : ∀ n : Nat, x (j + 1 + n) = false ∧ x (j + 2 + n) = false := by
        intro n
        induction n with
        | zero => simpa using And.intro hj1 hj2
        | succ n ih =>
          refine ⟨by rw [show j + 1 + ((n + 1 : Nat) : Int) = j + 2 + n by omega]; exact ih.2, ?_⟩
          have := zero_pair_next h (j + n) (by rw [show j + n + 1 = j + 1 + n by omega]; exact ih.1)
            (by rw [show j + n + 2 = j + 2 + n by omega]; exact ih.2)
          rw [show j + 2 + ((n + 1 : Nat) : Int) = j + n + 3 by omega]
          exact this
      intro i
      have hkm : ((j + 1 - i).natAbs : Int) ≤ (((j + 1 - i).natAbs * m : Nat) : Int) := by
        have := Nat.le_mul_of_pos_right (j + 1 - i).natAbs hm
        exact_mod_cast this
      have hk : j + 1 ≤ i + (((j + 1 - i).natAbs * m : Nat) : Int) := by omega
      rw [← per_add_mul hx i (j + 1 - i).natAbs]
      have := (hrun (i + (((j + 1 - i).natAbs * m : Nat) : Int) - (j + 1)).natAbs).1
      rwa [show j + 1 + ((i + (((j + 1 - i).natAbs * m : Nat) : Int) - (j + 1)).natAbs : Int) =
        i + (((j + 1 - i).natAbs * m : Nat) : Int) by omega] at this
    · right
      have hg : ∀ j, (x (j + 1) || x (j + 2)) = true := by
        intro j
        cases h1 : x (j + 1) <;> cases h2 : x (j + 2)
        · exact absurd ⟨j, h1, h2⟩ hz
        all_goals rfl
      have hy : ∀ i, Phi x i = !x i := by
        intro i
        unfold Phi
        rw [hg i]
        cases x i <;> rfl
      intro i
      have hi : xor (Phi x (i - 1)) (Phi x (i - 1 + 1) || Phi x (i - 1 + 2)) = x (i - 1) := congrFun h (i - 1)
      rw [hy, hy, hy, show i - 1 + 1 = i by omega, show i - 1 + 2 = i + 1 by omega] at hi
      have hgi := hg (i - 1)
      rw [show i - 1 + 1 = i by omega, show i - 1 + 2 = i + 1 by omega] at hgi
      cases ha : x i <;> cases hb : x (i + 1) <;> cases hc : x (i - 1) <;> simp_all
  · rintro (hw | ha)
    · show Phi (Phi x) = x
      have h1 : Phi x = x := (ring_fixed x).2 hw
      rw [h1, h1]
    · have hy : ∀ y : Int → Bool, (∀ i, y (i + 1) = !y i) → Phi y = fun i => !y i := by
        intro y hy
        funext i
        have h2 : y (i + 2) = y i := by
          rw [show i + 2 = (i + 1) + 1 by omega, hy (i + 1), hy i, Bool.not_not]
        unfold Phi
        rw [hy i, h2]
        cases y i <;> rfl
      show Phi (Phi x) = x
      rw [hy x ha, hy (fun i => !x i) (fun i => by simp [ha i])]
      funext i
      simp

/-- An alternating ring has even size. -/
theorem alternating_even {m : Nat} {x : Int → Bool} (ha : ∀ i, x (i + 1) = !x i) (hx : Per m x) :
    m % 2 = 0 := by
  have hstep : ∀ n : Nat, x n = (decide (n % 2 = 1) != x 0) := by
    intro n
    induction n with
    | zero => simp
    | succ n ih =>
      rw [show ((n + 1 : Nat) : Int) = (n : Int) + 1 by omega, ha, ih]
      rcases Nat.mod_two_eq_zero_or_one n with h | h
      · have : (n + 1) % 2 = 1 := by omega
        simp [h, this]
      · have : (n + 1) % 2 = 0 := by omega
        simp [h, this]
  have h0 := hx 0
  rw [Int.zero_add, hstep m] at h0
  rcases Nat.mod_two_eq_zero_or_one m with h | h
  · exact h
  · simp [h] at h0

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Realization"};
heads = {"orbit_eq_iff", "encode_walk", "decode_ring", "decode_encode", "encode_decode", "ring_fixed", "ring_period_two", "alternating_even"};
Column[rule30Submission["Rule30Submission." <> #]["TypeForm", "Open" -> opens] & /@ heads]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last
because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.encode_walk"]["KernelCheck"]
```

## What is not proved

- No classification is claimed for $P \ge 3$. The ring $0001$ already returns at $P = 8$. The record's ring
  censuses for larger periods are computations, not theorems here.
- Nothing is said about configurations on the whole line that are not spatially periodic, such as a black edge
  with rain behind it. The period-two argument uses the wrap-around of a finite ring.
- On a ring the shift is defined only modulo $m$. For $m \le 2P$ the condition $F^P x = \sigma^{-P} x$ coincides
  with a shift inside `PeriodicPoints`' range, so the genuinely light-speed content is the case $m > 2P$.
- No reachability statement is made about which walks occur beside a finite seed. Nothing here concerns the
  centre column or decides Problem 1.
- We found no matching result in the inspected kit catalog and the submissions list. That is a statement about
  our search, not a proof that none exists.

## Relation to earlier work

Describing the periodic patterns of a one-dimensional cellular automaton as paths in a finite graph of words is
standard; see Wolfram's account of the construction for periodic patterns
([2025](https://writings.stephenwolfram.com/2025/03/what-can-we-learn-about-engineering-and-innovation-from-half-a-century-of-the-game-of-life-cellular-automaton/)).
The contribution here is its exact formal form for rule 30's light-speed rings, on the kit's `evol`, and the
period-two classification. The kit's `PeriodicPoints` covers velocities in $[-1, 1)$ and lists rule 30's three
fixed points. The diagonal recurrence is the kit's (`Rule30Diagonals`, `Rule30RightPeriods`).

## Provenance

Lemma R, the correspondence between rings and closed walks, was found and proved by hand by Claude (Anthropic)
during a study of the periodic right edges of rule 30. GPT (OpenAI) read it independently and corrected the sign
of the velocity. GPT proved the period-two classification by hand, and Claude read that proof independently.
Claude formalized both in core Lean on the kit's `evol` on 2026-10-29, and GPT read the formal source.
