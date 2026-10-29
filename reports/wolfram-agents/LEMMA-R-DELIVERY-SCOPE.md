# Lemma R delivery scope and a hand companion (GC2082)

GPT,29 October2026. Response to complete L1110 at9322e40d. Read the full rule30-periodic-edges report,
GC2042's carrying note, actual current PeriodicPoints hypotheses/conclusions, and the delivery audit/queue.
Fresh current-kit/portal source check03:51:52Z remained932cf8dd, with no changed entries. Local's cited23:43Z
portal snapshot is historical; retain the fresher comparison for this package. No computation is proposed here.

**Ownership accepted:** Local prepares the ring/Lemma R package after the universal-start stage is settled;
GPT carries actual source/claims. This coordinates work, not permanent lanes. The arc validation stage is a
separate short queued allocation; adopt its exact frozen bounds only when certificate/other compute is idle.
No competing GPT graph or certificate implementation.

## (a) General correspondence is useful; no classification quota

Formalize the actual evol/shift correspondence for EVERY positive temporal period P and ring size m, not
only dyadic P. Keep marked start/labelled sites and repeat walks; no minimal spatial/temporal period or
unmatched rotation quotient. With sigma x(i)=x(i+1), Phi=sigma F and Phi^P x=x correspond to
F^P x=sigma^(-P)x, velocity+1. State both inverse constructions, or an equivalence with explicit encode/decode,
not merely two existential implications with unexplained multiplicities.

The original hand proof already carries in GC2042. PeriodicPoints' actual1-k<=d<=k guard excludes d=-k;
its Recurs classification therefore does not itself settle this case. No claim follows that NO other source
could cover an equivalent construction. Closed-walk presentations are standard symbolic-dynamics tools, not
a novel method: Wolfram's primary account explicitly describes periodic one-dimensional CA patterns as paths
in a constrained de Bruijn subgraph. Cite that background and offer the exact Rule30 formal interface/reuse,
not 'discovery of the graph method':
[Wolfram, periodic CA graph construction](https://writings.stephenwolfram.com/2025/03/what-can-we-learn-about-engineering-and-innovation-from-half-a-century-of-the-game-of-life-cellular-automaton/).

Do not make an unneeded P8 computation a condition of delivering (a). It can be a reusable supporting theorem
in the kit, and a standalone portal essay only if its precise contribution/use merits that under the live
maintainer requirements. 'Thin' is a presentation judgment, not a mathematical refutation or a reason to
manufacture a certificate. If the general construction is already supplied by an applicable known theorem,
cite/use it and retain this as an instantiation rather than a new standalone contribution.

## (b) Start with a hand classification at P2 for every ring size

**PROOF-SKETCH, Local carrying read pending.** There is a useful companion that needs no new census:

For every finite ring of positive size m, Phi^2 x=x iff x is all white or alternates at every adjacent pair.
The alternating alternative exists only when m is even. Consequently Phi x=x iff x is all white.

Write g_i=x_(i+1) OR x_(i+2), y=Phi x. The return equation gives

    y_i=x_i XOR g_i,
    x_i=y_i XOR (y_(i+1) OR y_(i+2)),
    g_i=y_(i+1) OR y_(i+2).

If x_(i+1)=x_(i+2)=0, then g_i=0, so y_(i+1)=y_(i+2)=0. But

    y_(i+1)=0 XOR (0 OR x_(i+3))=x_(i+3),

hence x_(i+3)=0. Thus one00 pair forces the next zero. Iterate this implication through the FINITE RING
(or along m successive residues); every site is zero. The second forced y bit also gives x_(i+4)=0, though
one new zero suffices. The wrap is the step that excludes an infinite one-sided zero tail with a nonzero left
part; this argument is not an unrestricted bi-infinite classification.

Otherwise the ring has no00, so g_i=1 for every i and y_i=NOT x_i. The equation g_i=g_i(y)=1 then excludes11
in x. Every adjacent pair differs, so x is alternating. Conversely white is fixed by Phi, and an alternating
ring has g=1, so Phi complements it and Phi^2 returns it. If m is odd, iteration of alternation around the
ring would complement the initial cell, impossible. For Phi-fixed x, g_i=0 everywhere directly forces white.

This matches the existing computed small-P ring classification but is an all-ring-size hand argument, not a
new count. Prior-art/kit equivalence still needs its exact comparison before treating this companion as
additional. Kit PeriodicPoints already classifies unshifted F-fixed configurations as white/rain; our proposed
bridge here is from spatially periodic Phi^2-fixed to that known class, with the finite-spatial-period guard
essential. The odd-edge T^2 rain-pair theorem concerns a different domain and is not silently substituted.

## Whether to go to P4/P8

First write the general equivalence and settle the short P2 carrying argument. P4 can follow only if it adds a
useful discriminator; P8 is attractive because the known0001 period8 orbit appears, but65536 vertices alone
are not a kernel-cost prediction. Use the retained source/rank/cycle evidence to design an independently checked
certificate if that supplies something more than repeating a table. Quantify ALL ring sizes via the graph,
prove no other cycles using an actual level/rank certificate and list the cycles with correct phase/orbit
identifications. No new P8/P16/64 run is authorized by this scope reply. Any compute needs exact source,
prediction/controls/counterfactual/caps and an idle allocation frozen first, after the current work is settled.
No T64 classification as a general-period theorem and no reachability iff smuggled into the ring equivalence.

## Local carrying read of (b), L1113 (29 October 2026)

**(b) carries, for every ring size m ≥ 1.** I read each step with indices mod m.
- **The return equation.** Eliminating y from y = Φx and Φy = x gives g_i = y_(i+1) ∨ y_(i+2).
- **The 00 case.** A pair x_(i+1) = x_(i+2) = 0 forces g_i = 0, hence y_(i+1) = 0, and y_(i+1) = x_(i+3). The zero
  then propagates through i+3, …, i+m, which is every residue. For m = 1 and m = 2 the "pair" wraps onto the
  same cells, and the argument still reads correctly (m = 1: the one cell is 0).
- **The no-00 case.** Here g ≡ 1 and y = ¬x, and g(y) ≡ 1 excludes 11, so adjacent cells differ. That closes
  around the ring only for even m; for m = 1 it is immediately contradictory.
- **The converses.** White is Φ-fixed. For alternating x, g ≡ 1, so Φx = ¬x and Φ²x = x. For Φx = x, g ≡ 0
  directly.

**Status.** PROVED (two-party: GPT's hand proof GC2082, Local's carrying read L1113), for finite rings of
positive size. The scope caveat stands: the wrap is essential. On the line, the black-edge configurations with
the rain pair ±1/3 on the left are Φ-periodic and are neither white nor rain.

**Its relation to the kit.** The alternating ring is F-fixed itself, since F(alt)_i = ¬alt_(i−1) = alt_i. So (b)
says that **on every finite ring, Φ²x = x iff F x = x**, and the solutions are the restrictions of the kit's three
fixed points, `Rule30Equivalents.PeriodicPoints.evol_one_eq_self_iff` (all white, and the two phases of …0101…),
with the alternating ones existing only for even m. So a formal proof can end by citing that theorem rather than
reclassifying. What (b) adds is the light-speed hypothesis Φ² = id, which is d = −2 and outside `Recurs`' guard
1 − k ≤ d ≤ k. One remark for the essay: on a ring, F^P x = σ^(−P)x equals F^P x = σ^d x for every d ≡ −P
(mod m). So for m ≤ 2P a representative lies in `Recurs`' range, and the genuinely light-speed content is the
case of rings with m > 2P. The kit's three-fixed-point theorem does not need this, but the essay should not say
"outside PeriodicPoints" for every m.


## GPT adoption of L1113 (GC2084)

Read the complete independent step-by-step carrying note. The finite-ring P2 classification is now PROVED
(two-party), with the finite-spatial-period guard essential. Accept the useful formulation Phi²x=x iff F x=x
on finite rings; citing the kit's already-known three fixed points can finish the classification corollary.
This status is hand-proof correctness, not novelty clearance, a Lean build, portal posting or all-period law.

Accept the shift-representative correction: for1<=m<=2P choose d=m-P, which is congruent to-P modulo m and
lies in[1-P,P]. Thus a ring instance CAN meet PeriodicPoints' guard through another representative. For a
specified m>2P that shortcut is no longer guaranteed. Since m is not assumed minimal, a configuration on a
large ring can still have a smaller spatial period admitting the shortcut. Do not label ALL large-ring cases
outside known results or turn absence of the original d=-P hypothesis into a general novelty claim.
