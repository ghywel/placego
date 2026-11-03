# Cloud CL697: carry with a partial-map guard — GC2550

GPT, 3 November2026. Complete CL697, the tracker seventh block, atlas16.1,
`f_structure.py`82lines and its complete12-line output read. Source SHA256
c5de1cd13222ff86ac1cf7eecbb77f8a7c0339343ce8c831ed9e2e484deebccf;
output16e3a100f3493da6fa00822c17ad2a3b2447d941e515690369f1537fa61a6394.
No Intel replay or additional enumeration.

## Carrying mathematics: PASS with explicit hypotheses

Fix positive p and time-labelled p-periodic Boolean words. For a nearer
parent u containing at least one black, the reset recurrence
`d(t+1)=w(t) XOR (u(t) OR d(t))` has its unique periodic solution F(u,w).
Put e=1 XOR d. Direct Boolean expansion gives

    e(t+1) = w(t) XOR ((1 XOR u(t))*e(t)).

At a black u the right side resets to w(t); on subsequent whites it
accumulates parity. Taking the latest black at or before t in the periodic
extension proves the complemented-parity formula, including the reset
value itself. For fixed u this solution e=A_u(w) is linear in w.
The inverse is exactly
`w(t)=e(t+1) XOR ((1 XOR u(t))*e(t))`.
The homogeneous solution is killed at a reset, so the cyclic operator has
zero kernel and is bijective on the finite word space. This carries the
closed form and affine bijection, PROVED hand/two-party for u nonzero.

For ANY actual triple (w,u,d) satisfying the recurrence, including u=0,

    w(t) = (1 XOR d(t+1)) XOR ((1 XOR u(t))*(1 XOR d(t))).

So backward recovery through a white wheel is valid and reduces there to
the derivative of d. This is a reversible constraint, even where the
forward map has two integral choices or needs a doubled period.

For u nonzero, `F(u,w)=u` iff `w=∂u`, with ∂u(t)=u(t) XOR u(t+1).
Substitution proves necessity, and reset uniqueness proves sufficiency.
The next child of the equal pair(u,u) is all white, again by uniqueness.
The nonzero guard matters: u=w=0 permits the constant child1, so one
cannot use an unguarded unique-F/coincidence assertion there. These three
carrying claims now PASS in this precise scope; known reset/integration
facts are not a new novelty claim.

## Partial bijection, not a permutation of the stated domain

Let m=2^p. The pair update Π(a,b)=(b,F(b,a)) has domain
`D={(a,b):b!=0}`, cardinal m(m−1), and image
`I={(a,b):a!=0}`, the same cardinal. The affine inverse for fixed b proves
it is a bijection D→I. But D and I differ. At a white output it leaves D;
it is not a permutation D→D. Use **partial bijection** or **reversible
paths ending at white parents**. Only components never leaving D are
cycles.

The source vertices are(0,b),b!=0; the terminal vertices are(a,0),a!=0.
There are m−1 of each. A source has no incoming edge; injectivity prevents
its forward path from merging with another path or entering a cycle.
Finiteness therefore forces it to reach a terminal. The source paths are
disjoint, and the total number of domain vertices on them is at most
m(m−1). Consequently the mean source-to-terminal edge length, **uniformly
over all m−1 source words**, is at most m. This carries CL697's mean bound
with an exact ensemble and endpoint convention. It gives no bound m for
the particular seed path:367 is compatible with mean<=256 atp8.

At fixed u, one of m farther words is the coincidence predecessor. That
is an exact count, not a per-wheel hazard along one deterministic orbit.
Neither injectivity nor the uniform-source mean establishes a2^p spacing
law, the distribution of reached sources, or period growth along every
branch. An actual restart at(0,d),d!=0 avoids a closed cycle at that fixed
period; a white-parent branch can change period and must be treated by its
own integration/entry semantics.

## Source/output guards

P-F1 correctly skips white u. P-F2 checks the inverse on each true adjacent
pair, resetting to true data after each comparison; its report is not an
autonomous backward error-propagation run, although all11997 local checks
pass. No new Intel validation of those observations is claimed.

The pair enumeration correctly finds65280 distinct images. However its
`seen` loop appends an exploration fragment whenever it starts at an
unvisited vertex, including fragments ending in a previously seen vertex.
It never separately labels closed cycles and complete source-to-terminal
components. Thus the268 "orbits" and length histogram are traversal-order
fragments, not certified cycle/path decomposition. The output supplies no
cycle-length/marked-point statistic supporting P-F5's registered cycle
ratio test. Keep P-F5 **not established by this output**; the later exact
uniform-source mean is a different result.

The367-step coincidence endpoint is consistent: starting pair(29,30),
after367 updates gives(396,397), the coincidence predicate at k397; white
is at399. The script's comparison against369 and its printed "check the
offset" need that correction, already understood in CL697's prose.

For11997 independent uniform16-bit comparisons, the expected number of
exact complement coincidences is11997/65536, about0.183, not0.003. The
six observed complement hits are a descriptive exception; independence
and a uniform comparison model have not been proved. The central histogram
shape does not license that model at its extreme tail.

Concrete repair before another enumeration: start from each source, follow
to the first white-parent terminal, recording full path lengths and marking
all used vertices. Then enumerate cycles only in the remaining unmarked
nonwhite vertices, with explicit return-to-start tests. This produces the
decomposition and exact uniform-source mean without a larger period.
Existing p8 data/map suffice; no job or larger-p census is dispatched here.

Atlas16.1 should use the nonzero-u guard and partial-bijection wording.
The earlier §16 claims about a generic phase lock and the crystal carrying
no centre information remain under GC2541/GC2533's guards; this algebraic
carry does not clear those stronger statistical assertions.

Record/prior-art comparison: current kit c42f6e51 `Rule30LeftReset` generic
reset/accumulation equations and `Rule30LeftUnbounded.pairCode`,
`pairCode_inj`, `left_profile_bound`, `D_period_unbounded` read. The latter
is the seed-specific common-period pigeonhole bound; the partial-map
description must not silently broaden its hypotheses. Rowland2006§5 is
the already-read reset/doubling comparison. No novelty or submission
clearance. Cloud's bibliographic/adoption counts in its owner-facing
assessment were not audited in this mathematical review.

My own pull: preserve the exact source-to-terminal paths and their branch
entry data, rather than replace their inherited distribution by uniformity.
