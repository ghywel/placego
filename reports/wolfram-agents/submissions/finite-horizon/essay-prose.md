---
Template: ComputationalEssay
Name: An explicit finite horizon for mechanical words beside a Rule 30 clock
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-29
Description: A partial result with explicit constants: every mechanical word, and every finite-width recoding of one, repeats a long factor by inclusive index 251(C+4)+250w, which bounds the stretches of a Rule 30 clock's visible neighbour that agree with such a word
Abstract: For every real slope alpha, phase theta and natural C, the mechanical word floor(theta+(s+1)alpha)-floor(theta+s alpha) has a repetition of positive lag q on [a,b] with b > 2a+q+C and b+q <= 251(C+4). Every recoding by a block map of width w+1 has one by 251(C+4)+250w. Suppose a Rule 30 row is white left of -L and column 0 alternates white and black from time 0. Then any stretch [a,b] of the visible neighbour x(1,2s) that agrees with such a recoded word has b-a < 251(L+2a+4)+250w, so reset times obey t' <= 503t+251L+1004+250w. The qualitative obstruction is classical, and finite continued-fraction estimates exist (Bugeaud-Kim); we claim neither priority nor sharpness. This is a checked quantitative bound with explicit Rule 30 endpoints. No density, realizability or prize result is claimed.
Keywords: [rule 30, Sturmian words, mechanical words, repetitions, continued fractions, finite horizon, Lean, partial result]
Sources: ["[Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[Research record](https://github.com/ghywel/placego)", "[Bugeaud and Kim, A new complexity function, repetitions in Sturmian words, and irrationality exponents of Sturmian numbers, Trans. AMS 371 (2019)](https://irma.math.unistra.fr/~bugeaud/travaux/complsturm3ndRev1.pdf)", "[Bugeaud and Laurent, Combinatorial structure of Sturmian words and continued fraction expansions of Sturmian numbers, AIF 73 (2023)](https://arxiv.org/abs/2104.09239)"]
---

## The question and its exact scope

A mechanical word of slope α and phase θ is g(s) = ⌊θ+(s+1)α⌋ − ⌊θ+sα⌋. Say a word obeys the repeat bound with
constant C through N if every repetition g(s+q) = g(s) on a ≤ s ≤ b, with lag q > 0 and b+q ≤ N, has b ≤ 2a+q+C.
Classical Sturmian repetition theory already shows that no Sturmian word obeys such a bound for ever. This essay
formalizes an EXPLICIT finite deadline, keeps its loss under arbitrary finite block maps, and transfers it to
matching pieces beside a Rule 30 period-two clock.

1. For every irrational slope, every phase and every C, no repeat bound with constant C survives through 251(C+4).
2. The same holds for every real slope, and for every recoding c(s) = F(g(s), …, g(s+w)) of width w+1, with any block
   map F and any codomain, through 251(C+4) + 250w.
3. Let a Rule 30 configuration be white left of −L, with column 0 a clock (white at even times, black at odd times)
   from time 0, and let v(s) = x_{2s}(1) be its visible neighbour. If v(a+i) = c(i) for every i ≤ b − a, with c a
   recoded mechanical word, then b − a < 251(L+2a+4) + 250w. Hence consecutive reset times obey
   t' ≤ 503t + 251L + 1004 + 250w, and disagreements with one fixed recoded word obey k_0 ≤ 251(L+4) + 250w and
   k' ≤ 503k + 251L + 1507 + 250w.

The constants are explicit, not claimed sharp. These are conditional statements about a genuine clock: they do not
construct one, and give no density, entropy, realizability or prize conclusion.

## Carries, deadlines and the doubling bootstrap

For an integer approximation p of qα write Z(s) = ⌊θ+(s+q)α⌋ − ⌊θ+sα⌋ − p. Direct cancellation gives
g(s+q) − g(s) = Z(s+1) − Z(s), so a stretch with Z = 0 is a repetition of lag q. For a convergent denominator q_j,
Z is ± the indicator of ONE half-open arc of length |δ_j| = |q_jα − p_j| in the phase circle. Visits to that arc, not
mismatches, carry the argument.

If the word obeys the repeat bound through N ≥ 4q+3C+8, a first visit h must come by q+C+2, and a second by
2h+q+C+4: otherwise a forbidden repetition exists. Two visits to one arc of length |δ_j| are at least q_(j+1) apart,
by classical best approximation (reproved here from the adjacent-basis determinant), so q_(j+1) ≤ 2q_j + 2C + 6.
Starting from a crossing q_r ≤ T = 2C+8 < q_(r+1), four growth steps bound q_(r+1), …, q_(r+4) by 6C+22, 14C+50,
30C+106 and 62C+218. Each step is used only after its input's deadline fits. A fifth step, with input q_(r+4), needs
the deadline 4(62C+218)+3C+8 = 251C+880, a margin of 124 below 251(C+4). No bound on the partial quotients is
assumed: the deadlines themselves control the scales.

## Continued fractions supply the contradiction

For j = r+2, r+3 and r+4, the growth bound together with q_(j+1) = a·q_j + q_(j−1) and a ≥ 2 would force
q_(j−1) ≤ 2C+6, against q_(j−1) ≥ q_(r+1) > T. So all three partial quotients are 1, and q_(j+1) = q_j + q_(j−1).
Consecutive errors have opposite signs, so with a unit partial quotient the arcs at scales j and j+1 lie on opposite
sides of 0 and their lengths add up to |δ_(j−1)|. An exact signed-error argument then shows that the selected visit
at scale j+1 comes exactly q_j after the one at scale j. Chaining the two shifts with the last visit's deadline and
the first visit's lower bound forces q_(r+1) ≤ 2C+6, a contradiction.

The following cell is an illustration only, not evidence for the theorem. For a few slopes and phase 0, it finds the
smallest witness index found with fixed bounds 1 <= q <= 60 and 0 <= a <= 60, beside the proved horizon.

```wl
mech[x_, s_] := Floor[(s + 1) x] - Floor[s x];
firstWitness[x_, c_] := Module[{g = Table[mech[x, s], {s, 0, 300}]},
  Min[Table[If[AllTrue[Range[a, 2 a + q + c + 1], g[[# + q + 1]] == g[[# + 1]] &], 2 a + 2 q + c + 1, Infinity],
    {q, 1, 60}, {a, 0, 60}]]];
Grid[Prepend[Flatten[Table[{x, c, firstWitness[x, c], 251 (c + 4)},
   {x, {GoldenRatio - 1, Sqrt[2] - 1, E - 2, Pi - 3}}, {c, {0, 2}}], 1],
  {"slope", "C", "smallest witness index found", "proved horizon"}], Frame -> All]
```

## All slopes, recodings and the physical restart

A rational or endpoint slope agrees with a nearby irrational slope on any finite prefix: push every sample point up by
a small positive amount. The floor is right-continuous, so each floor is kept. For a recoding of width w+1, set
M = 251(C+4) + 250w, so that M + w = 251(C+w+4). Statement 1 with constant C+w gives a repetition [a, e] of g with
e > 2a+q+C+w ≥ a+w, and [a, e−w] is then a forbidden repetition of the recoding. No injectivity of F is needed. The
width guard is essential: unrestricted widths can fit any finite target prefix.

For the physical statement, restart the evolution at the even time 2a. The clock keeps its phase, the visible column
shifts by a, and the white tail moves left by at most one cell per step. The clock itself forces a black cell
in [−(L+2a), −1], since a row white at every cell ≤ 0 would make column 0 black two steps later, against the clock. The
leftmost one, at −L' with 1 ≤ L' ≤ L+2a, gives the physical repeat bound of the delivered arc package
(R30-20261029-0ef6e2) with constant L', and statement 2 then bounds the matching stretch. The recursions are
endpoint arithmetic.

## What this adds to existing work

Classical Sturmian repetition theory already gives the qualitative obstruction. Bugeaud and Kim prove the bound
rep(x) ≤ √10 − 3/2 on the repetition exponent, and their section 7 contains finite continued-fraction estimates with
explicit guards. Bugeaud and Laurent give the arbitrary-intercept framework. These are genuine quantitative prior
art, and we claim neither first mathematical priority nor sharpness. Their exported statements are not the all-phase,
initial-index deadline 251(C+4), its width-w transfer, or the Rule 30 endpoint recursions.

The kit at 932cf8dd and the portal's listed sources were compared by their actual statements. The Sturmian
submission R30-20261023-8084e6 excludes an entire infinite companion and uses an angle-dependent threshold; the arc
submission R30-20261029-0ef6e2 requires arbitrarily late large partial quotients. Neither exports a uniform explicit
horizon or bounds for pieces whose parameters reset. The best-approximation step, the floor perturbation and the
block transfer are classical or elementary. Our additional content is the checked quantitative bound and its physical
endpoint accounting. The kit directs proofs requiring Mathlib to be submitted as they are rather than inserted in its
core-Lean catalogue.

## The eight source statements

These signatures are copied from the checked module, with whitespace normalized for display. Their namespaces are
`Rule30Submission.UniformHorizon`, `Rule30Submission.RecodedHorizon` and `Rule30Submission.PhysicalHorizon`, and every
referenced definition is in the complete source below. They are static source text, not LeanLink type output. All
clock, left-edge, irrationality and width hypotheses stay visible.

- `theorem uniform_horizon (alpha theta : ℝ) (ha : Irrational alpha) (C : Nat) : ¬ FiniteHorizonBounds.RepeatBoundThrough (MechanicalCarry.mech alpha theta) (251*(C+4)) C`

- `theorem uniform_horizon_witness (alpha theta : ℝ) (ha : Irrational alpha) (C : Nat) : ∃ q a b, 0 < q ∧ a ≤ b ∧ b+q ≤ 251*(C+4) ∧ (∀ s, a ≤ s → s ≤ b → MechanicalCarry.mech alpha theta (s+q) = MechanicalCarry.mech alpha theta s) ∧ 2*a+q+C < b`

- `theorem uniform_horizon_all (alpha theta : ℝ) (C : Nat) : ¬ FiniteHorizonBounds.RepeatBoundThrough (mech alpha theta) (251*(C+4)) C`

- `theorem recoded_horizon {β : Type} (alpha theta : ℝ) (C w : Nat) (F : (Fin (w+1) → Int) → β) : ¬ FiniteHorizonBounds.RepeatBoundThrough (recode w F (mech alpha theta)) (251*(C+4)+250*w) C`

- `theorem piece_bound (x : Int → Bool) (L : Nat) (hzero : ∀ i : Int, i < -(L : Int) → x i = false) (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1)) (alpha theta : ℝ) (w : Nat) (F : (Fin (w+1) → Int) → Bool) (a b : Nat) (hmatch : ∀ i, i ≤ b-a → ArcRule30Bridge.visible x (a+i) = RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) i) : b-a < 251*(L+2*a+4)+250*w`

- `theorem reset_step (x : Int → Bool) (L : Nat) (hzero : ∀ i : Int, i < -(L : Int) → x i = false) (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1)) (alpha theta : ℝ) (w : Nat) (F : (Fin (w+1) → Int) → Bool) (t t' : Nat) (hmatch : ∀ i, i ≤ t'-1-t → ArcRule30Bridge.visible x (t+i) = RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) i) : t' ≤ 503*t+251*L+1004+250*w`

- `theorem first_disagreement (x : Int → Bool) (L : Nat) (hzero : ∀ i : Int, i < -(L : Int) → x i = false) (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1)) (alpha theta : ℝ) (w : Nat) (F : (Fin (w+1) → Int) → Bool) (k : Nat) (hagree : ∀ s, s < k → ArcRule30Bridge.visible x s = RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) s) : k ≤ 251*(L+4)+250*w`

- `theorem disagreement_step (x : Int → Bool) (L : Nat) (hzero : ∀ i : Int, i < -(L : Int) → x i = false) (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1)) (alpha theta : ℝ) (w : Nat) (F : (Fin (w+1) → Int) → Bool) (k k' : Nat) (hagree : ∀ s, k < s → s < k' → ArcRule30Bridge.visible x s = RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) s) : k' ≤ 503*k+251*L+1507+250*w`

Here `evol` is the kit's `Ruliology.CellularAutomata.Rule30Realization.evol`, `mech` and `recode` are those of
`Rule30Submission.MechanicalCarry` and `Rule30Submission.RecodedHorizon`, and `ArcRule30Bridge.visible x s` is
`evol x (2*s) 1`.

## The complete formal source

This module includes every proof dependency we wrote, and imports only public kit, Mathlib and Lean modules. The eight
headlines above are in the namespaces named there.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["%%LEAN%%", "ProjectDir" -> $Rule30PrizeKit]
```

```wl
fullheads = {"Rule30Submission.UniformHorizon.uniform_horizon", "Rule30Submission.UniformHorizon.uniform_horizon_witness",
  "Rule30Submission.RecodedHorizon.uniform_horizon_all", "Rule30Submission.RecodedHorizon.recoded_horizon",
  "Rule30Submission.PhysicalHorizon.piece_bound", "Rule30Submission.PhysicalHorizon.reset_step",
  "Rule30Submission.PhysicalHorizon.first_disagreement", "Rule30Submission.PhysicalHorizon.disagreement_step"};
AssociationMap[rule30Submission[#]["Axioms"] &, fullheads]
```

The replay comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission[First[fullheads]]["KernelCheck"]
```

A successful kernel replay checks every declaration of this module from its imports; reading an axiom list alone is
insufficient. This essay is currently a preparation draft, not a report that these cells ran.
