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
rule30Submission = LeanImportString["%%LEAN%%", "ProjectDir" -> $Rule30PrizeKit]
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

## Assembly note — remove before publication

Assembled from `essay-prose.md` and `Rule30Submission.lean` by substituting the module for the marker. The
release check of both forms, the notebook build and GPT's final read come first.
