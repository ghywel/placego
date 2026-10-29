# Older fringe and recurrence claims: exact source comparison (GC2120)

29 October 2026, GPT. This is a delivery disposition and convention check, not a new proof, compiler run,
finite census or blanket clearing of the remaining backlog. Local's reset/exact-information work is separate.

Record searched: record_find.py GC727; PROOFS33–35 in full, GC727's actual archived hand argument,
L1080 and the prior-art audit, GC2039's PeriodicPoints comparison, MAP's rows for these candidates.
Fresh kit main932cf8dde039b89b1dcbe9636867bb1b2057fef0 and complete portal refresh08:42:19Z: only our
arc entry/source added since the preceding complete check; public source was already independently checked
GC2119. Read the actual catalogue entries and carrying statements/bodies listed below, rather than equating
keyword hits. No literature-wide novelty inference follows from these searches.

## Proposition20 / PROOFS33: the original finite stripe family is already fully covered

Actual `equivalents/Rule30Equivalents/TransformsSeeds.lean`:

- `stripeSeed n p` is black at even positions in [0,n) and at n.
- `stripePattern` equals `cell t p` whenever p<t.
- `evol_stripeSeed` proves the entire exact pattern for every n,t,p.
- `stripeSeed_center` proves literal equality of the complete center column, not merely equivalent
  eventual-periodicity status. `problem1_iff_stripeSeed` is a later consequence, not the strongest match.

These match the original S_r=1,11,101,1011,... claim, including equality on every p<=t-1 and the t=0 center.
**Disposition: known, reproved here; no additional submission for that original family.**

The GC641/L351 extension allows *any* common initial left half, with x(0)=1 and x(-1)=0, and the stripe
replacing the originally white right half. The above source fixes the single-seed left half. It is therefore
not an exact statement-level match to that extension. The old two-party diagonal argument remains valid,
but its additional formal delivery scope is still a separate candidate. Do not erase that guard or call
it delivered by the single-seed theorem. A common black at -1 is a retained counterexample to dropping it.
`Realization.seed_perturbation` instead changes an infinite left tail to prescribe a future trace; it is
not the fringe-equivalence theorem.

## Proposition21 / PROOFS34: its first-disagreement mechanism is a short kit corollary

Let x,y agree at every site strictly greater than -b and differ at -b, b a natural number. They may differ
arbitrarily farther left. For t<b, the center's entire causal interval [-t,t] lies strictly right of -b;
`AlgebraicDegree.evol_congr t 0` therefore gives equality at the center. At t=b,
`PeriodicPoints.evol_ne_of_ne_left` with k=b,i=0 gives inequality: its agreement hypotheses are precisely
-b<j<=b, and its distinguished leftmost input is -b. This is the exact arbitrary-left-tail argument;
`Mixing.evol_flip_front` alone only states the single-flipped-cell case.

Now let x have the single seed's whole center column and let y be x with its left half made white.
If x's left half is nonwhite, its shallowest black has a natural depth b. The preceding known lemmas give
that y first disagrees with the single seed at exactly b, which is Proposition21's tau(R)=b. White-left
and stripe-right corollaries follow as in the recorded hand proof. This does not solve the open converse
classification of all finite seeds sharing the column.

**Disposition: known formal mechanism with the recorded first-disagreement/tau statement as an immediate
specialization; no separate standalone portal package is needed for this corollary.** This is a source-level
hand deduction from existing exact formal lemmas, not a claim that a new tau declaration was compiled or
that the completeness conjecture is already in the kit. The original two-party hand proof remains credited.

## GC727: the sign question is settled, with an important scope boundary

Our convention in PROOFS35/GC727 is F^p(x)(i)=x(i-s), so positive s moves right.
Actual `PeriodicPoints.Recurs p d x` is F^p(x)(i)=x(i+d), so **d=-s**.
The kit guards 1-p<=d<=p translate EXACTLY, on integers, to

    -p <= s <= p-1.

Thus `recurs_add_factorial` and `ncard_recurs_le` cover GC727's complete middle interval, including the
left light-speed endpoint s=-p and stationary case s=0, but exclude the critical right endpoint s=p.
They do not cover either supercausal wing s>p or s<-p. This resolves the pending sign convention without
pretending that the kit's theorem classifies every s!=p.

The archived GC727 proof uses L=max(2p,p-s) for s<p. Its L=2p middle interval is the known kit mechanism;
L=p-s for s<-p is its longer-window case. Proposition22 handles s>p by solving the outside target, and
s<-p has its bijective length-(p+|s|) window/count. These outer claims remain two-party hand results,
not current-kit exports established by this comparison. There is no reason to regenerate their census.

### The cited Boyle–Lee remark is related, not an exact certificate for the outer count

Read [Boyle–Lee, math/0607178v1, Remark2.1](https://arxiv.org/html/math/0607178): it assumes an
*injective* cellular automaton on a prime alphabet and gives periodic-point counts in a horizontal cone.
That is a useful general precedent. Rule30 is not injective on full configurations, so this remark does
not directly prove Proposition22(b)'s exact count for shifted Rule30. The old wording says the same kind
of count and does not claim a novelty theorem; retain that modest comparison. Neither an exact prior-art
match nor a new-result priority claim is justified by this citation alone.

**Disposition:** GC727's middle interval is known, reproved here. The supercausal finite-window theorem
and exact count are carried hand results, but their additional delivery/prior-art scope is unresolved;
the middle theorem and the citation cannot silently clear them. A useful next source comparison would
be a theorem on fixed points of a one-sided permutive block map, with its exact window span and both
spatial tails accounted for. The current prefix-period carrying read takes precedence over preparing
that formalization. The critical rightward case s=p remains excluded throughout.

## GC2122: follow-up identifies the outer mechanism; packaging disposition resolved

The preceding sign check suggested the right source class: feedback shift registers. Read
[George Petrides (2022), section2, equation(1) and Cycle structure](https://link.springer.com/article/10.1007/s12095-022-00562-x).
It gives the standard nonsingular binary register

    T(w_0,...,w_(L-1))=(w_1,...,w_(L-1),w_0 XOR h(w_1,...,w_(L-1)))

and its decomposition into cycles. This matches Proposition22(b)'s window map exactly when s<-p,
L=|s|+p: the H arguments occupy a subset of the retained coordinates, with unused coordinates allowed.
The formula's inverse recovers w_0 from the appended bit and retained h; it does not require injectivity
of the original full-line cellular automaton. Every one of the2^L words gives a unique two-sided register
orbit and hence a unique LABELLED spatial row, with a fixed spatial origin. Rotations are not quotiented.
That last distinction explains the count; it counts rows, not cycles or distinct least periods.

For s>p the window map can be singular. The old stable-image proof does not need nonsingularity: on a
finite set ofN=2^(s+p) states, images T^j(X) stabilize. On the stable image T is surjective and hence a
permutation. A two-sided orbit lies in every image, hence on a cycle. Conversely a cycle defines the row
by the overlapping windows and enforces the original relation. This is the elementary finite functional-
graph fact already used in the old proof, not a further CA theorem from the Petrides paper.

**Final outer disposition:** retain the correct, independently carried Rule30 specialization as record-only
background, with explicit finite-graph/nonsingular-register attribution. No exact exported Rule30 theorem
is claimed present in the current kit, and no exact-phrase novelty or priority is asserted. A new standalone
submission is not warranted just to restate those standard mechanisms with this local rule. The original
finite census is unnecessary to these universal arguments and is not rerun. Together with the exact known
middle interval, this resolves the old recurrence *packaging* question; the critical s=p direction remains
outside the result. Reopen formal packaging if a maintainer requests this interface or a subsequent proof
needs its precise window/count lemma as a reusable dependency. This disposition does not settle the critical
periodic-profile/ring classification or finite-seed reachability.
