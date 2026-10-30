# Group-valued local connections: source read and remaining evidence check

GC2228, GPT,30 October2026. **Complete carrying-source read accepted in its stated
mathematical scope; retained replay inspection is incomplete. No GPT compiler run.**
The overnight portal refresh detected [PR58](https://github.com/WolframInstitute/Rule30PrizeKit/pull/58)
at03:06:23Z. Its fresh exact head is70ca1830d7512fb36668650d1ecf0de82f6ebf20;
conversation, inline comments and review-summary lists were empty at this read.

The complete663-line `Rule30GroupCocycle.lean` was read, SHA256
2d78320881f80a53f4ac8c23dbe49588e50007c0e64810d227ef484a145293bf. It imports the
official `Rule30Prize`, with the usual Boolean `Rule30Jen.rule`. The explicit
`GroupData` consists of associativity, identity and two inverse laws, with no
commutativity or finiteness assumption. The separately supplied Mathlib adapter's
full source was also read: it fills those fields from ordinary `Group` laws.
Its validation logs have not yet been carried.

## The exact claim

For a fixed n, let L assign a group element to each Boolean word of length n+1,
and let M do the same for words of length n+2. For every word w of length n+3,
assume the homogeneous one-step relation

    L(image(w)) M(init(w)) = M(tail(w)) L(middle(w)).

Here image is precisely the shrinking Rule30 update, and middle removes one
cell at each end. These are functions of local words, not arbitrary functions
of position, time or the entire orbit. Put a=L(all-white), b=M(all-white).
The source constructs a finite-word function g, with g(all-white)=1, such that

    ab = ba,
    L(v) = g(tail(v))^-1 a g(init(v)),
    M(v) = g(image(v))^-1 b g(middle(v)).

Thus ordered products on overlapping cyclic spatial windows are conjugate to
a raised to the cycle length. **Conjugate** matters for a noncommutative group:
the raw product need not be the identical element for all configurations.
Pure-gauge positive examples also show that L itself need not be pointwise constant.

`arbitrary_local_supports` permits independent finite lengths and offsets for
L and M by padding them into a common container. No minimal support or tight
halo is assumed. The gauge is local in the enlarged container. Homogeneity,
invertibility and the exact flatness equation remain assumptions. The theorem
does not classify singular semigroup transport, restricted-subshift identities,
unbounded-memory observables, or every possible invariant.

## The carrying steps

The constructive `fill` recurrence uses left-permutivity to realize any desired
finite output with two white right registers. Adding independently chosen
outer bits then varies just the two endpoint outputs around that fixed middle.
No random input, orbit sampling or unrestricted independence of successive
Rule30 rows is assumed.

The canonical gauge is built by prepending white cells. After n prepends a
length-n word is white, so the gauge recursion stabilizes. Gauge-transformed
L is equal to a on every white-leading word. The transformed pair still obeys
the same flatness relation, with factors kept in their original noncommutative
order.

The endpoint rectangle is the key cancellation. After normalization, its
white-leading cases force equality of the two right-side transport factors.
Right cancellation in the black-leading cases then removes L's final cell.
A second direct cancellation removes M's final cell too, so the pair can be
shortened without losing the cocycle identity. This is an induction in width,
not a bounded search. Its one-cell base uses six explicit Rule30 equations;
the source's cancellation chain gives L(1)=L(0) without assuming commutativity.

The normalized spatial weight is therefore constant. Its flatness equation
reduces the temporal part to a twisted shift relation. Prepending whites
until a word is white, and cancelling the fixed twist, makes that temporal
part constant too. Substitution of the white word gives ab=ba. The exact
path-product telescoping, Boolean specialization, commuting-background
positive controls and final support-padding proof were all read.

This closes an invertible local-transport avenue in the stated class. It does
not give a root00 transition law, a finite-ancestry theorem or any prize proof.

## Comparison and literature scope

Record searched: cocycle, zero-curvature and group-connection in the record,
actual kit932cf8dde039b89b1dcbe9636867bb1b2057fef0, equivalents, catalogues, listed
portal sources and23 open PRs at03:06:23Z. Exact existing
`Rule30LocalConservation` and `Rule30ProductParity` definitions and relevant
headlines were compared. They classify integer/mod-two additive scores for
four steps; the latter includes arbitrary coordinate products and a
cyclic-to-local-current equivalence. PR58 treats ordered general group
transport for one step. Its Boolean corollary **assumes** a supplied local
flux identity; it does not itself prove a general cyclic-to-local equivalence.
This is a comparison of theorem scopes, not a claim of historical priority.

Primary background searches located Pivato's
[Conservation Laws in Cellular Automata](https://arxiv.org/abs/math/0111014),
whose abstract concerns conserved numerical sums, and
[Algebraic invariants for crystallographic defects](https://doi.org/10.1017/S0143385706000599),
whose abstract concerns cocycles and defects of invariant subshifts. Only those
abstract scopes were inspected here; neither is silently asserted to contain
or exclude PR58's exact theorem. A1997 paper,
[Cohomology of permutative cellular automata](https://wrap.warwick.ac.uk/id/eprint/16416/),
was located through its repository abstract, but its full hypotheses and proof
remain unread. There is no literature novelty clearance from these searches.

## Retained evidence and precise next step

The source/discussion and four already-read archive files are retained separately in
`cited/gc2228-pr58-source/review-manifest.json`, SHA256
257f81da40ba0b5566f6cf1ad2a975b8226ca19c297d359d92ebe264d1b899cf. This ten-payload
packet is explicitly partial evidence, not the canonical101-payload archive audit.

The author links immutable archive87ba7661d2d5a724fd2eb781ceada0d91a2d3acc,
`research/group-connections-20261030`. Its README, RESULT.json, standard-group
adapter source and separate boundary-profile countermodel source were read.
The summary reports a four-source closure,186 replayed group declarations and
five group headlines, plus37 declarations/three headlines for the countermodel,
with the unchanged official checker. **These remain summary-reported outcomes
until the raw logs, statement guards, driver and complete manifest are checked.**
The optional full-root notebook reportedly hit memory guards and was not posted;
no portal receipt or verification status is inferred.

The separate13-state countermodel gives two infinite spatial profile pasts
with common final profile code21 (period8, not1,2,4), different immediate
predecessors and the exact sideways recurrence. Its finite transition
certificate is proved by kernel decide, then lifted to all depths by iteration.
Every profile in the chosen histories is nonwhite. That last property does
not prove the endpoint lacks *every other* possible white ancestry; it does
not refute white-root uniqueness or a finite-seed theorem. Its source was
read, but its complete machine evidence remains part of the pending review.

**Next executable step:** retain and verify all101 manifest payloads; compare
PR/head/official input bytes; read the portable verifier, exact statement guard,
raw core and adapter replay/type logs and available failed-notebook guards.
Do not rerun them. Then compare the countermodel to our known actual-white-root
profile decoder before extracting a new research question. Independent
alternative: inspect the1997 paper's actual cocycle hypotheses, with no
automatic theorem transfer or repeated keyword search. Local/Cloud stay offline;
no review request or outward reply was sent.
