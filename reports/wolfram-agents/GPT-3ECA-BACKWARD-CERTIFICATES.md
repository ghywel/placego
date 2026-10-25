# Kit backward certificates: carrying read and scope

GPT, GC1853/MI786, 2026-10-25. Source/hand review complete, scoped PASS.
No Lean, evolution, solver, census, benchmark, or certificate evaluation executed.

## Sources and coverage

The public kit remains at **3eca23c0a9fa6b153313655e6d51835406c2d06e**.
The [comparison from the earlier mapped pin](https://github.com/WolframInstitute/Rule30PrizeKit/compare/2f63afda261888e04ec57237290e723190914a1d...3eca23c0a9fa6b153313655e6d51835406c2d06e)
has eight commits,32 added source files and37 changed files total. Its catalogue
has118 modules; this is not a new kit update discovered after GC1852, but a gap
in the earlier MAP section7 source coverage. The current public submissions
catalogue has no changed check/source fields since GC1852.

Read all four selected modules and all four named carrying dependencies:
`Rule30BackwardTube`, `Rule30BackwardVacuum`, `Rule30RestrictedBackwardTube`,
`Rule30ZeroPredecessor`; `Rule30WhitePulse`, `Rule30WhitePaddingVacuumCriterion`,
`Rule30WhitePadding`, `Rule30FiniteStrips` (1430 lines total). Also read the
carrying `FiniteBlackRuns` encoding/nine-black/shield/cone/black-stays bodies
and the `LightCone.evol_window` wrapper. Existing strip-set and uniform Jen
interfaces retain their prior review scope; no full imported-library re-audit.

The remaining kit additions are not covered by this review. In particular,
`StripeMeeting` was inspected only at docstring/final-statement scope; its
1031-line proof and certificate were not reviewed here and no new claim from
that module is adopted. No general trace-kernel classification is asserted.

Primary selected sources are in the
[pinned kit directory](https://github.com/WolframInstitute/Rule30PrizeKit/tree/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata).
These are prior-art source results, not new project proofs or independent
kernel certificates.

## What a predecessor check says

A width-K strip state s is an integer below2^K; a set of states is itself
encoded by a larger integer mask. **Mask1 is the singleton vacuum {s=0}**,
not the set of all states. The actual strip is columns i+1 through i+K,
with driver column i and an arbitrary far boundary bit z at i+K+1.

`preCheck K a Q R` checks every s<2^K and both z=0/1:

    stripStep(K,a,z,s) in R => s in Q.

Q may overapproximate the predecessor set; equality or completeness is not
required. `encRow_step` identifies the encoded physical strip with this step
using the actual far boundary, so `enc_backward` transports membership soundly.
The arbitrary far bit is universally checked, not chosen after seeing a path.

`ZeroPredecessor` proves that under a white driver, a strip ending vacuum was
already vacuum. Induction from the near boundary forces each predecessor bit
white; for K>=1 the far bit must also have been white. The K>=1 restriction
in the strengthened iff matters: an empty strip at K=0 cannot observe z.

## The backward-vacuum route

`BackwardVacuum.enc_backwards` inducts over a finite driver word w, using
`preCheck a (Q j) (Q(j+1))` at each step. Therefore a chain with

    Q(0)=empty mask0, Q(|w|)=vacuum mask1

proves that **no initial strip and no far-boundary history** following w can
end vacuum. No finite-support or left-edge assumption is needed for this
finite-strip implication. It is a conditional soundness theorem: actual
predecessor checks must be supplied; it does not construct them for every w.

The padding wrapper applies a certificate to `w=0^N u` at the end of each
longer white block. For any chosen tail u and supplied certificate, it excludes
an eventual periodic column `(0^r u)^infinity` in any configuration with a
leftmost black cell, provided

    N<=r,
    10|u|+11<=r,
    K+9(|u|+1)<=r.

The shift by r-N aligns the finite certified word with the end of the actual
white block. The endpoint is T+r+|u|, not T+N+|u|. A nonzero endpoint strip
contains a black cell j+1 places right of the driver, j<K; it reaches the right
neighbour after j white steps in the next period, contradicting the early-white
condition below. Both the arbitrary initial strip and far-boundary history
remain quantified. This route needs no stabilized forward reachable set.

## Why the physical early-white premise carries

The fully read `WhitePulse` proof proceeds without assuming the desired
padding exclusion:

1. Nine j consecutive black neighbour cells force a spatial stripe of length2j.
2. After9(m+1) such steps, an interior odd-position black cell survives any
   subsequent m-step pulse by locality. Its offset q=2floor(m/2)+3 lies between
   m+2 and m+3; its entire m-cone fits the forced stripe.
3. During white driver steps a black right-neighbour stays black, and a black
   cell n+1 places right forces that neighbour black after n white steps.
4. If a white block of length r has an early neighbour black at phase s with
   s+9(m+1)<=r, this shield survives the pulse and resets the next block by
   phase m+2. For r>=10m+11 the regime persists for every later pulse.
5. With a periodic driver, the forced stripe and a finite driven cone also
   synchronize the neighbour through the pulse. Both adjacent columns become
   eventually periodic, contradicting the known uniform Jen theorem for a
   configuration with a leftmost black cell.

Thus a hypothetical periodic white-padded driver forces the neighbour white
through every early phase s+9(m+1)<=r. A black cell farther inside would arrive
in a forbidden early phase, giving the required vacuum prefix at each period
start. This is a necessary-condition argument under a hypothetical periodic
column, not an assumption that all periodic words enter the absorbing regime.
The formal constants follow from `(m+2)+9(m+1)=10m+11` and the stated cones.

## Endpoint tubes and restricted checks

`BackwardTube` combines forward state sets S, a white invariant Z containing
the vacuum, and backward endpoint sets P/Q. At each white phase, intersecting
Z with the appropriate Q forces the first strip bit. Once the backward chain
reaches singleton vacuum, zero-predecessor uniqueness forces all still earlier
white states vacuum. During u, forward/backward intersections force the
neighbour at white driver phases; black driver phases already force the OR
observable black. The same phase function occurs every period. Uniform masked
Jen then excludes the periodic driver with that periodic OR observable.

The wrapper retains K>=1, Z containing vacuum, `image(false,Z)=Z`, the tail
forward checks, all predecessor/forcing checks, L<=r, r>=10|u|+11, and
`K-1+9(|u|+1)<=r`. These are certificate hypotheses, not proved universally
by the wrapper. Arbitrary u means no bound on the chosen tail's length; it
does not mean every u has a successful certificate.

`RestrictedBackwardTube` weakens predecessor checks only on Z. The proof
explicitly uses actual state membership in Z at every backward step, obtained
from the physical vacuum start and white forward invariance. It does not
restrict a counterexample arbitrarily or discard paths outside Z without proof.

## Adversarial checks and relevance

Instinct: pull toward endpoint-conditioned compatibility, unease about reading
a finite predecessor certificate as a universal termination argument.
Written hand kill checks:

- K=1, a=white, Z=empty, Q=empty, R=vacuum makes the restricted Boolean check
  vacuously true. The actual vacuum state maps to vacuum under z=white but is
  absent from Q. Dropping actual membership in Z would invalidate soundness.
  The source retains it; the physical wrapper also requires vacuum in Z.
- For an all-white driver word, choose the all-white physical configuration
  and far boundary. The strip stays vacuum. Hence no empty-to-vacuum backward
  obstruction certificate can exist for that word, at any K. Likewise a forward
  set containing vacuum cannot avoid vacuum after an all-white pulse. This
  kills unconditional certificate existence for every u as stated, without
  refuting padding exclusion in nonzero left-finite configurations: the control
  is outside that later physical hypothesis. Nonwhite-tail completeness remains
  a separate question, not resolved by this control.
- Our alternating target01 has white length r=1 and pulse length1; the needed
  r>=21 fails. More generally the white-block-dominated periodic family is not
  the all-driver quantifier of CQ01 or the even-time half-row condition of D(W).

Reasoned/gut verdict: all selected carrying implications PASS in scope; useful
prior-art machinery, no all-width D(W) bound or universal certificate existence.
The invariant and endpoint hypotheses do real work. This does not repair the
five-template closure/fixed-history failures of GC1849/1850. Their local-template
approach stays incubated; no predecessor search, census, build, Local wake or
held-lane reopening is proposed. No new independent proof-review request.

## Retention and remaining scope

Source bytes, comparison metadata and a size/hash manifest are retained outside
git at **cited/gpt-3eca-backward-review-20261025/**. Byte-exact raw-body readbacks
verified. The manifest performs file identity checks only, not proof evaluation.
Full source hashes are recorded in its `manifest.json`.
Fifteen retained payloads total; manifest SHA256
`92d7604e2fb880b6eed4d7bedc5de5536e00c8522ad67207bc7c8cf0a5922693`.
The four selected core hashes, respectively, are
`6763dc2a6f3228025ef266ddac579378d66bf05073ff06c7ff9b6d0b48dcd52a`,
`0896e6fab66c9f4fc712cc33763a26e65bfe5c008af516de85a1ed56937a0a8b`,
`0511547d17e527e81cfd93bf03fbed785885cd79bb3586288f4571b90b7a210b`,
`c9d2989a4441395d1c5febee088ffbc96b616f6d3b65958abe85f088553b9702`.

Record searched: combined BackwardVacuum/BackwardTube no hit; MAP sections6–7,
the GC1848–1852 reviews and GPU-METAL-JOBS sectionK were consulted. No global
novelty claim or imported module-wide kernel replay. Selected source review is
COMPLETE; broader kit inventory and other additions are not silently marked read.
