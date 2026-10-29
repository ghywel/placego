---
Template: ComputationalEssay
Name: Finite-arc rotation codes beside a Rule 30 clock
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-29
Description: A partial result excluding finite-step irrational rotation codes with arbitrarily late large continued-fraction digits as the visible neighbour of a normalized Rule 30 clock
Abstract: If a Rule 30 initial row has a leftmost black cell and column 0 alternates from time 0, its visible neighbour cannot eventually be a finite-step coding of an irrational rotation whose continued-fraction digits exceed 2^(r+1) arbitrarily late. Here r counts supplied endpoint labels. Concrete unions of k half-open intervals use 2k labels and threshold 2^(2k+1). Arbitrary endpoint values are handled through finite exceptions. This is the formal delivery of the record's Theorem E-double-prime; no all-irrational or prize result is claimed.
Keywords: [rule 30, irrational rotation, finite arcs, continued fractions, repeat windows, Lean, partial result]
Sources: ["[Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[Research record](https://github.com/ghywel/placego)", "[Jen, Global properties of cellular automata](https://doi.org/10.1007/BF01010579)"]
---

## The question and its exact scope

Assume the initial row x has its leftmost black cell at -L, with L a natural number. Its right side is
arbitrary. Assume column 0 is white at every even time and black at every odd time, starting at time 0.
The visible neighbour is c(s)=evol(x,2s,1). We ask whether c can be obtained by moving around a circle at a
fixed irrational speed and reading a finite black/white partition.

The answer proved here is no when continued-fraction digits of that speed exceed K=2^(r+1) at arbitrarily
late indices. The parameter r counts the endpoint labels supplied to the finite-step representation;
they may repeat or be redundant. The claim is deterministic and retains this digit hypothesis explicitly.
It does not settle bounded-partial-quotient speeds or every irrational rotation. The physical clock is
already normalized from time 0; an eventual match of the CODE is allowed, but an arbitrary restart of an
eventual physical clock is not an additional theorem asserted here.

A finite-step representation is a 1-periodic Bool-valued function f on the real line with r possible
endpoint locations modulo integers. If (u,v] crosses none of their integer translates, f(u)=f(v).
This convention allows consistently half-open pieces. The concrete interval theorem takes membership in
any union of [a_i+z,b_i+z), i<k and integer z. Wrapped, overlapping, empty and full-circle cases need no
extra assumptions. It uses 2k supplied endpoint labels and K=2^(2k+1), not an optimized jump count.

## Why the physical clock gives a repeat bound

The kit's finite masked window-Jen theorem, not a randomness assumption, gives the obstruction

    c(s+q)=c(s) for every a<=s<=b  implies  b<=2a+q+L, for q>0.

In the substitution, compare physical times 2a and 2(a+q) at column0. The inverse dependency reaches the
moving left edge at depth m=L+2(a+q). Column0 matches through the closing sample s=m. For s<m, its OR with
column1 matches automatically at odd phases, when the clock is black; at even phases it reduces to the
assumed visible equality. An excessively long repeat would therefore make two different left-edge
histories agree where the kit proves they cannot. `ArcRule30Bridge.repeat_bound` formalizes this directly.

## A finite number of labels cannot hide all the breaks

Suppose a binary trace has the above bound with a fixed constant C. For any fixed positive lag q, choose
its successive mismatch times d_0,d_1,... . The repeat bound supplies them and gives

    d_0 <= q+C+1,     d_(j+1) <= 2*d_j+q+C+3.

Thus d_j+(q+C+2)+1 <= 2^(j+1)*(q+C+2). Among r+1 mismatches, two have the same endpoint label, and their
positive time separation m is strictly less than B=2^(r+1)*(q+C+2).

For an approximation p/q to the rotation speed alpha put delta=q*alpha-p and epsilon=|delta|>0. A mismatch
crosses a listed endpoint. After choosing an integer lift, its position lies in the half-open interval
[e_i-max(delta,0), e_i-max(delta,0)+epsilon). The signs of delta are both covered. Two mismatches with the
same label give |m*alpha-a|<epsilon for an integer a. Strictness comes from the half-open interval.
No separation or distinctness assumption on the endpoint labels is needed.

## Continued fractions supply the contradictory spacing

For a reduced approximation p/q, a Bezout identity and the integer determinant q*a-m*p show

    |m*alpha-a|<epsilon  forces  (m+q)*epsilon>1.

The implemented lemma only needs |m*alpha-a|<epsilon; a zero error is impossible at positive m for irrational
alpha. Indeed, assuming (m+q)*epsilon<=1 makes the determinant have absolute value less than 1, hence zero.
Bezout then makes m a positive integer multiple of q, contradicting the strictly smaller error.

The kit's actual continuants give epsilon<1/q_next and q_next=a_next*q+q_previous. Put K=2^(r+1).
At sufficiently large index, q_previous>=K*(C+2). If a_next>K, then

    q_next >= K*(q+C+2)+q = B+q.

This contradicts the short return m<B above. Arbitrarily late large digits let us pay the fixed C margin
without increasing the threshold. This is why a single early large digit is not the final theorem's premise.

The following small arithmetic table illustrates only the label thresholds; it is not evidence for a
universal claim or a search over physical Rule 30 starts.

```wl
Grid[Prepend[Table[{r, 2^(r + 1)}, {r, 0, 6}], {"supplied endpoint labels r", "digit threshold K"}], Frame -> All]
```

## Finite exceptions and endpoint conventions

If traces agree from N onward, the repeat obstruction transfers from C to C+2N. For an irrational alpha,
each listed endpoint modulo integers can be visited at most once: two distinct hit times would make
(s-t)*alpha an integer. Finitely many labels therefore give a cutoff after which endpoint conventions do
not matter. This yields the endpoint-variant headline without assuming an effective numeric cutoff.

## What this adds to existing work

This formalizes Theorem E-double-prime, PROOFS entry15, from the Wolfram · Collatz · Mahler record. Its hand
proof and earlier independent G2.2 read precede this delivery. Finite endpoint changes were already handled
in G131/G132. The currently listed submission R30-20261023-8084e6 proves all Sturmian words and their finite
sliding-block codes excluded; those include important special cases whose endpoints belong to one rotation
orbit. Its `sturmian_block_excluded` does not itself represent arbitrary unrelated arc endpoints.

The ingredient methods are classical: Jen's Rule30 left-permutive obstruction, finite pigeonhole, interval
coding of rotations and continuant determinant approximation. We claim this scoped formal application,
not discovery of these methods or literature-wide novelty from negative searches. The kit at932cf8dd and
listed portal sources refreshed06:55:05Z were compared by their actual statements. The kit directs proofs
requiring Mathlib to be submitted as-is rather than inserted in its core-Lean catalogue.

## The complete formal source

This module includes every arc proof dependency we wrote. It imports only public kit/Mathlib/Lean modules.
The four physical headlines are `Rule30Submission.ArcRule30Exclusion.no_visible_rotation`,
`no_eventual_visible_rotation`, `no_visible_endpoint_variant` and `no_visible_interval_union` in that same
namespace. Reading their types exposes the clock, left edge, irrationality and digit assumptions directly.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["%%LEAN%%", "ProjectDir" -> $Rule30PrizeKit]
```

```wl
heads = {"no_visible_rotation", "no_eventual_visible_rotation", "no_visible_endpoint_variant", "no_visible_interval_union"};
fullheads = "Rule30Submission.ArcRule30Exclusion." <> # & /@ heads;
Column[rule30Submission[#]["TypeForm", "Open" -> {"Rule30Submission"}] & /@ fullheads]
```

```wl
AssociationMap[rule30Submission[#]["Axioms"] &, fullheads]
```

The replay comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission[First[fullheads]]["KernelCheck"]
```

A successful kernel replay checks every declaration of this module from its imports; reading an axiom list
alone is insufficient. Executed outputs, exact source and resource/metadata receipts must be retained with
the delivered notebook. This essay is currently a preparation draft, not a report that these cells ran.
