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

## CL698 synthesis: attribution audit and carrying guards — GC2565

Complete194-line essay draft,24-line plan and57-line original citation map
read. The owner's synthesis authorization and division are recorded in
CL698. GPT takes this audit; Cloud retains prose/map ownership and Local
the anchor/build after A5. No posting or new theorem clearance is given.

**All four November attribution placeholders are resolved.** Fresh public
metadata for all20 named entries says `G.P.J.W. Quint; Gemini (Google)`.
Their current status is Lean Verified. In particular, the five November
extensions of AIOvernight's left-side modules belong to Quint/Gemini, not
to the original module author. Original file-addition commits confirm
AIOvernight added LeftReset/LeftUnbounded/FrontLaw/SettledBarrier/WhiteSpacing
in37a3d844 on30 October. DefectClockBudget is different: Troyusrex added
it in a5ad97fa on31 October. Both actual addition commits were read.
The citation map has the20 exact portal ids, correct PR links and objects.
The former eight-entry PR105–108 group actually spans PR99–102 and105–108.
DefectClockBudget concerns the right-edge clock, not left settled diagonals.

The live listing at16:17:59Z has114 entries,112 Lean Verified and2 Lean
Unverified. Its fefa7e entry is now Lean Verified, not still checking.
Neither that count nor the source read makes every portal entry a checked
new theorem. Quote a dated count or omit the introductory number80.

**Integration is checked separately from PR status.** PR83/85/86/87 are
closed with merged=false, but each exact changed Lean module is byte-exact
on current kit main c42f6e51. Their portal entries carry Human Verified and
Kit Contribution. Thus they are adopted source, not pending open work;
GitHub's merged field alone would give the wrong research status. Closed
issue conversations and review-summary bodies were freshly read (empty
for those four). PR84 remains open. Its maintainer discussion and exact
current sources show the requested finite BWH checks have been removed;
SmallRW is proved, but the period-two theorem still explicitly takes hb:BWH.

Fresh exact heads and changed Lean sources were retained for PR83–87,
97–102 and105–113; discussions/review bodies were read. This is attribution
and targeted statement audit, not an independent full proof carry of all
those modules. PR101 now supplies inverse_uninverse and inverse_bijective
on all streams and word-length<=3 separators; do not attribute that new
right inverse to older PR86. PR110's current title/public abstract still
mention minus10, while the exact current head also states the stronger
minus27 onset for k>=5. Cite a specific declaration/snapshot if using the
number, rather than reading a title as its formal theorem.

### The anchor's hand read already exists, with guards

GC2550 above is the complete independent F1–F3 carry. It is PROVED
hand/two-party for positive common period and a nearer parent u containing
a black; not single-party as the new draft says. Time-labelled cycles and
cyclic wrap are required. At a black of u, e(t+1)=w(t), not0: the inclusive
running-parity formula counts that reset value. The inverse for an ACTUAL
triple remains valid when u is white; a unique forward periodic F there
does not. Coincidence/white-child equivalence uses the nonwhite guard.

The pair map is a bijection D→I with D={(a,b):b!=0} and I={(a,b):a!=0}.
It is not a permutation D→D. A fixed-u count of one predecessor among2^p
is exact counting, not a1/2^p hazard along a deterministic orbit. The
uniform-source mean bound is not a seed-path bound. Existing p8 exploration
fragments were not a cycle decomposition. These corrections from GC2550
are needed in essay sections2D,3.6,7 and the atlas; adding a family theorem
in Lean does not establish the statistical claims or novelty over the
known reset/integration literature and kit base.

### Other necessary prose repairs, with concrete alternatives

* Section0: some entries are unverified; say the portal collects submissions
  at different verification stages, not that every entry is a theorem with
  a certificate. Recent dates/counts should be pinned.
* Sections1/2E: exact rightward speed1 needs an actual rightmost discrepancy
  and agreement beyond it. A pair with arbitrary unbounded difference has
  no such edge. State that finite-edge guard explicitly.
* Sections2E/5: replace old A4 id37281a by87ba7a, preserve its alignments
  and closure-entry/arbitrary-tail guards. A1's public check still timed out;
  say locally kernel-checked, portal maintainer rerun pending, rather than
  present it with the same public status as A2/A4.
* Sections2F/4: the absence of additive conservation laws does not exclude
  monotone rank functions, non-additive potentials, clock-dependent ranks
  or proof-state refinements. DefectClockBudget itself uses such a rank.
  Describe the exact excluded conservation class and leave other potential
  methods open; do not infer that Q01 cannot have a local potential.
* Sections3.2/3.5: a shared numerical half-bit rate is not an equality of
  languages or of four information quantities. Supply the exact map and
  hypotheses for a comparison, and preserve the earlier audited capacity
  distinction. A finite14-cell upper bound is not an all-width rate.
* Sections3.6/4:0.41,2^p spacing, generic synchronization and a universal
  fair core remain observations/conjectures with specified sample regimes.
  Keep them separate from the proved periodic reset law and affine inverse.
  “Passed every generic tell” should name the finite tests and horizon.

The older generated citation table also contains truncated statements and
mixed column meanings; it is retained as a historical excerpt, not cleared
for publication. The checked November table is usable for attribution.
A whole-portal essay still needs source-level checks of each additional
statement it selects; this audit does not certify every older row.

[Attribution/source receipt](receipts/gc2565-synthesis-attribution.json)
pins the20 live portal reads,20 current PR heads and the actual addition
commits. Raw public responses/source files are retained in
`cited/gpt/gc2565-attribution-receipts.tar.gz`,836276bytes, SHA256
095647edca5f4c7770e6f15320af726ab9dcb6366b1b3c944202a3d3ff3afe3c,
with byte-exact upload/readback. The same live listing still shows A1 as
Lean Unverified/error. Last COMPLETE known_find refresh stays15:49:56Z;
this targeted audit does not advance that timestamp.
