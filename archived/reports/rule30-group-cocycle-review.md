# Group-valued local connections: source and retained-evidence review

GC2228–GC2229, GPT,30 October2026. **Complete carrying-source read and retained
author replay accepted in their stated scopes. No GPT compiler run.** GC2229 below
supersedes the pending-evidence status in the historical GC2228 account.
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

## GC2228 evidence checkpoint (superseded by GC2229 below)

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

## GC2229 complete archive and replay review

All101 payloads in the author's SHA256SUMS.json match, and the manifest itself
is retained:102 archive files,540110bytes. The exact PR58 group source and the
current official Jen, Prize and unchanged Check sources match byte for byte.
Checker SHA256 is b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905.
The full retained packet, including the manifest audit and replay parsing, is
`cited/gc2229-pr58-review/review-manifest.json`, SHA256
1951fa5295282a32b9bd11f75a1f9bc2adbed11317fe4f142c7aa1525f7301ed.
All105 uploaded files were verified after raw-body upload. Archive integrity is
complete; this does not mean every exploratory script in it was carrying-read.

The portable verifier, explicit StatementGuard, raw core and boundary replay
objects, build logs, adapter outcomes, and available notebook failure summaries
were inspected. The raw outcomes agree with the author's summary:

| Closure | Replayed constants | Declared constants | Headline theorems |
| --- | ---: | ---: | ---: |
| Group connection |186|128|5|
| Boundary countermodel |37|24|3|
| Optional Mathlib group adapter |5|2|1|

No new axioms occur; the reported headline dependencies are standard. The core
and boundary heads use propext and Quot.sound, with recurrence requiring only
propext. Source builds and the explicit guard have empty warning logs. The
official checker itself emits its known deprecated-replay warning. Its partial
mode accepts arbitrary statement types: `typeMatches` does not compare a theorem
with the prose or the prize statement. The explicit guard writes out the rule,
group/Boolean connection and arbitrary-support types, and the source carrying
read separately checks their relevance. The adapter is optional and uses its
reported Mathlib pin; it is not a dependency of the core closure.

Lean4.35 on the author's Windows host is recorded with compiler-binary digest
ec7a472d1c12a09b0c0c718f7427c2be527b3f5f07810fdbe076c2507c7a91ea.
There is no separate version-command log. This is retained author provenance,
not a newly measured GPT compiler version or replay. The verifier creates a
fresh source-only output tree, builds four sources plus the guard, then runs
the unchanged checker on the two target modules. It uses one Lean thread.

The portable driver's resource claim needs care. Each direct subprocess has a
60second timeout; the120second total is checked only after each call finishes.
It is not a continuously enforced120second stage wall bound, and may overshoot
by the final call. The driver contains no aggregate CPU, RSS, pressure or
process-tree cleanup monitor. Its seven reported call times sum to16.985seconds;
that is the author's reported timing, not an Intel measurement or proof of
resource enforcement. No author code was executed here.

The older standalone essay precedes support padding and has four headlines,
178replayed/127declared constants. It is not the latest five-headline PR source.
Its successful build/check guard summaries report37.734/47.141seconds and
2064.02/2207.43MiB peak owned RSS. BUILD-ATTEMPTS preserves four earlier failures,
including two RSS stops and one low-physical-memory stop. Their original raw
logs, individual guard receipts, monitor samples and guard implementation are
absent from this archive; the summaries are retained as reported outcomes,
not independently observed enforcement. The separate GL2(F2) Wolfram control
is also reported evidence, not a GPT rerun. No portal package or live verifier
receipt is inferred from this draft.

The countermodel's mathematical source and its37-constant replay are now carried.
[GC2230's explicit finite white history](rule30-profile-boundary-control.md)
sharpens its boundary interpretation without changing the source theorem.

## A known singular example, explained by hand

The linked discovery archive already identifies its first singular-matrix
invariant as the alternating-ring recognizer. Its pilot stopped after37 of256
width-one assignments; width two was not run. The retained algorithm checks
all lengths by reachable linear spans of paired old/new products, whereas the
nonconstancy witness is just a length-two word. This is not a complete census
of the proposed matrix families, and no new run is warranted for this example.

Here is a self-checked hand explanation, **PROOF-SKETCH**, known and reproved
here. The labels2and4 are M0=E01 and M1=E10 over F2. Each square is zero,
M0M1=E00 and M1M0=E11. The trace of a cyclic product is therefore1 exactly on
strictly alternating nonempty even rings. Equal adjacent letters kill the
trace, including across the join by cyclicity; odd alternating linear words
have off-diagonal product and trace0.

An alternating Rule30 row is fixed and has no other preimage. To see the latter,
write y_i=x_(i-1) XOR (x_i OR x_(i+1)), and take a target triple y_i,y_(i+1),
y_(i+2)=0,1,0. If x_(i-1)=0, the first equation forces x_i=x_(i+1)=0, the second
forces x_(i+2)=1, and the third is impossible. Thus every input site corresponding
to a target1 is1. The equation at each such target site then forces the preceding
input, corresponding to a target0, to be0. Hence x=y. Odd rings never have this
target, so their observable is identically0. This proves trace conservation
for every positive ring size without appealing to a finite ring cutoff.

This does not evade the group theorem: both labels are singular, and a global
trace is not an additive local density. It recognizes an already-known isolated
background, giving no new root information or prize invariant. Record searches
for alternating/preimage and matrix-trace, actual current kit/portal/PR index,
and the author's precise README/discovery source were compared. No novelty
claim or further matrix search follows.

## Optional literature dependency and next question

Parry's1997 [Cohomology of permutative cellular automata](https://link.springer.com/article/10.1007/BF02760688),
Israel Journal of Mathematics99,315–333, DOI10.1007/BF02760688, is subscription-only
at the publisher; the university repository offers its abstract without full
text. The abstract discusses unitary cocycles, a mixing permutative action and
cohomology to constants as a class, not a theorem that every such cocycle is
trivial. Exact hypothesis/prior-art comparison is parked until a legitimate
copy is available. Owner access would help, but this is not blocking the programme.

The next independent hand target comes from the same archive's explicitly
conjectural dyadic periodic-background question. Its finite ring17–24 test
reports equal Phi^8/Phi^16/Phi^32 fixed counts; it says nothing about arbitrary
spatial periods or heteroclinic paths. Source and result are read, not rerun.
First compare a fixed temporal-clock graph's recurrent components and transient
connections with the existing rooted period32 certificate and PR48's carrier.
The cheap objection is a clock carried only on a connecting path, absent from
every spatial cycle. Settle that distinction before proposing any computation.
