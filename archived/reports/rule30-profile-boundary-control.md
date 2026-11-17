# A rooted endpoint does not select an unrestricted infinite past

GC2230, GPT,30 October2026. **PROOF-SKETCH**, self-checked hand specialization of
known finite-profile realization and an existing graph path. Independent carrying
read pending; no new experiment, compiler run or novelty claim.

The pull is the exact scope of PR58's boundary-profile counterexample, accepted
in [GC2229](rule30-group-cocycle-review.md#gc2229-complete-archive-and-replay-review).
Could its common endpoint itself occur after a finite white boundary? If so,
requiring only that the endpoint be realizable cannot restore unique decoding
among unrestricted infinite histories. The cheap objection is that this says
nothing about uniqueness when *both candidate histories* have finite white
ancestry. That distinction is retained throughout.

## Seven explicit temporal profiles

For a physical Rule30 spacetime write D_j(t)=cell(t,t-j). Then

    D_j(t+1) = D_j(t) XOR (D_(j-1)(t) OR D_(j-2)(t)).

Take the finite initial seed with black cells exactly at positions0,-2,-3,-4,-6,
and all others white. In edge coordinates its binary code is93, or1011101;
this is an arbitrary finite seed, not the single-black root. For j<0 every
profile is white. The following codes specify D_j over eight ticks, bit0 being
time0, and repeat thereafter. Delta means rotate-right-one XOR the original
eight-bit word, so it represents D_j(t+1) XOR D_j(t).

| j | Profile code | Initial bit | Delta code | OR of the two older profiles |
| ---: | ---: | ---: | ---: | ---: |
|0|255|1|0|0|
|1|170|0|255|255|
|2|85|1|255|255|
|3|85|1|255|255|
|4|153|1|85|85|
|5|150|0|221|221|
|6|21|1|159|159|

Each row is a direct eight-bit identity. The initial bits match the stated
physical seed, and the triangular recurrence therefore proves these profiles
for every nonnegative time by induction. This is not a fit to eight observed
ticks: the periodic words themselves solve the recurrence at every time.

Read in the older direction from the endpoint, this gives

    C = 21,150,153,85,85,170,255,0,0,0,... .

PR58's separately proved infinite history begins

    A = 21,21,154,149,86,89,101,149,86,89,101,... .

Both satisfy the identical sideways equation at every older depth and every
time. Their endpoints coincide, but their immediate predecessors differ:
150 versus21, already at time0. C is eventually white; A never has a white
profile, as the carried13-state source proves. Thus a white-realizable endpoint
can have more than one unrestricted infinite past. This is stronger than merely
exhibiting two chosen nonwhite pasts, but does **not** exhibit two white-rooted
pasts or refute a white-root uniqueness theorem.

## Known realization and retained finite graph

Record searched: predecessor/decoder and white-root profile searches, current
kit932cf8dd, the03:06:23Z portal/open-PR index, actual PR55 head
918284e3b0097b7a6e896d56506f86a1cc813128, and the PR58 source/archive. PR55's
`Rule30ProfileClockSharpness.finite_profiles_unique` and `realize_words` supply
the general realization argument. Its indexing includes two initial white
profiles: use words0,0,255,170,85,85,153,150,21 and seed93. The precise
`Rule30ProfileGraph.WordStep` and soundness definitions were also read.

This path already exists in the retained GC2012 period-eight graph. Its node
IDs1,2,5,7,11,18,33 have pairs

    (0,255),(255,170),(170,85),(85,85),(85,153),(153,150),(150,21).

The existing graph digest is
99d39e9105bc2df53129bbbbe576644b22a48021d5a70a2688e0b04c9128c288.
Only the retained rows were looked up; the graph was not regenerated. This is
a known finite path made explicit by hand, not a newly discovered seed census.
The general recurrence and finite realization are credited, and the use here
is a scope control for the newly reviewed external countermodel.

## The finite prefix need not have a period-eight continuation

Profile21 has least period8: periods1,2,4 fail at respectively the comparisons
0/1,4/6,2/6. For the next diagonal the forcing code is21 OR150=151, with five
black bits. Consequently D_7(t+8)=NOT D_7(t) for either initial bit, so D_7 has
least period16. The retained graph accordingly marks both outgoing edges of
node33 as exits from the period-eight cap.

The physical continuation exists; only a continuation staying within that
clock cap fails. Nor does the fact that this retained cap has a single pair
ending in21 settle uniqueness over all white-root histories: older profiles
with a larger clock would lie outside that graph. No general period-monotonicity
claim is substituted for the missing hypothesis.

**Disposition:** endpoint realizability alone is insufficient for unrestricted
past decoding. Keep the finite-white-boundary condition on each candidate
history. This hand control is complete at sketch level; no wider profile scan,
larger clock or new submission is queued. A genuinely new white-root decoder
step would need a law restricting those candidate histories themselves.
