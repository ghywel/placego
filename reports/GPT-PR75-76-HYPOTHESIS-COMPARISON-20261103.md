# C2: what our theorems do, and do not, supply to the frontier/separator reductions

GPT, 3 November 2026 — GC2414. Status: **source-level comparison**, not a new
Lean replay of third-party modules and not a proof of an open hypothesis.
Kit main c42f6e5133f61a47e99289fd4b6e0536fd8a0453; complete index00:35:06Z.
The fresh closed discussions, review lists and exact final heads of PR75/76
were read. PR84 and PR86 were then inspected because they change the live
hypothesis table. Source hashes are in the accompanying JSON manifest.

**Pull.** Replace a vague resemblance between our capture/clock work and these
reductions with exact objects and quantifiers. Success would either discharge
an actual hypothesis or identify a smaller missing bridge. Cheap objection:
several propositions imply period-two exclusion, but need not imply one
another. Discriminating test: match their initialized objects, boundaries,
universal populations and conclusions before transporting any theorem.
No computation was launched.

## Current public sources supersede the original menu snapshot

[PR75](https://github.com/WolframInstitute/Rule30PrizeKit/pull/75), final head
f131449bf08949cbf0d815b678f6d6dc431524ad, and
[PR76](https://github.com/WolframInstitute/Rule30PrizeKit/pull/76), final head
fa511089735aa73643560165f1cc2dceffa2420c, are closed, API merged=false. Both
maintainer conversations end in an incorporation decision, and their modules
are actually on main. Do not continue describing them as open PRs. Main also
has later extensions; it is not byte-identical to every original head.

The maintainer's requested comparison is now in the actual source:

- Mortality implies Q01, through `Q01_of_mortality`. The reverse is not known;
  legal finite frontiers are not assumed to come from left-side histories.
- RW implies the orbit separator SEP. SEP is equivalent to the constant-tail
  separator. These imply period-two exclusion for finite rows.
- The original main theorem uses BWH plus SmallRW. But
  [PR84](https://github.com/WolframInstitute/Rule30PrizeKit/pull/84), exact current
  head bfea77af5dbd44ba4ece5c643cdde4ef8386d851, **already proves SmallRW** and
  `bwh_implies_rw_unconditional`, `bwh_implies_period_two` and the corresponding
  center corollary. That PR remains open; its source is public prior art even
  before merge. The maintainer explicitly accepts this finite auxiliary discharge
  while rejecting unrelated case-by-case checks of the open BWH proposition.
  Do not schedule another SmallRW census or call it an unsolved prerequisite.
- Neither the actual PR75/76 statements nor later inspected sources order SEP/RW/
  BWH against Q01 or mortality. A shared period-two consequence supplies no order.

Current main's `Rule30AlternatingTraceBridge` now identifies its duplicated
frontier definitions with `Rule30SurvivalBridge`, proves the budget equivalence
there too, identifies the history scalar as sampled column(-2), and proves its
logarithmic repeat lower bound. `Rule30SurvivalBridge` also contains exact
pure-scan conjugacies with actual left diagonals. These are available tools,
not new deductions to recreate from the old PR head.

## Objects and quantifiers

| Proposition | Object and boundary | What is required | What it gives |
|---|---|---|---|
| Q01 | Every finitely supported start of the zero-driven left half | No start keeps the required alternating-time boundary test forever | Excludes eventual period2 of the seed; no arbitrary right side is needed |
| Q01Gap | Finite starts already satisfying the constrained test | Exclude eventual gap3-or5 free-bit complements | Excludes finite reconstructed left rows for right halves entering the known gate trap; in particular CQ01Empty |
| CQ01Empty | One fixed white right half, with alternating center imposed | Its uniquely reconstructed left row Psi(empty) is not finitely supported | No finite full row with that exact right half sustains the stated alternation |
| Mortality / all-length repeat budget | Every nonempty finite word of bit pairs whose first high bit is1 | The growing scan eventually fails its terminal chronological guard | Q01 and period-two exclusion; not merely death of observed/rooted words |
| BWH | Every n>=7, c=2 or3, every four-symbol stream | Binary input prefix2n+2 cannot produce constant n-times-peeled inverse prefix n+2 | Via already-proved SmallRW in PR84, RW |
| RW | Every n>=1, r<=2 and the same tail symbols | Exclude an exact finite wedge with binary terminal symbol, junction no11 and specified12 pair | SEP; the junction and final bit cannot be dropped |
| SEP | Every finite normalized label word u and hard-core stream e | liftWord(u,const c) differs from inverse(e), c=2 or3 | Period-two exclusion; all label lengths, not just the proved length<=2 cases |

Here **hard-core** means all stream symbols are1 or2 and consecutive11 is
forbidden. It is a condition on the encoded pair stream, not on adjacent raw
Rule30 cell colors. A **peel** applies the explicit backward pair operation phi
to each pair of successive stream symbols. Its depth is not our defect-window
width or a clock's temporal period.

The actual chart is exact:
`actualEndpoint(y,o)(j) = encodePair(y(o+2j+2,-1), y(o+2j+2,-2))`.
`actual_peel_chart` reads the d-th peel at time t as the physical cell pair at
laboratory time o+t+1 and spatial position -(2d+t+2).
This explains why a leftmost black cell supplies a finite peel-rank witness.
It does not make every arbitrary hard-core endpoint a finite-origin row.

## Which of our tools discharges a hypothesis?

**None of the reviewed current theorems discharges an open all-width/all-word
hypothesis in this table.** This is a scoped matching verdict, not a claim
that no future bridge exists. The exact obstacles and routes around them are:

- **Capture clocks.** The P1024/480 results start after entry into independently
  checked windows and impose depth/initial-history guards. Mortality ranges over
  every legal growing frontier; its word length grows by1 each successful tick.
  A fixed capture graph, even with exact post-entry clocks, does not cover that
  population or prove that every scan enters the certified set. Route: prove a
  history-compatible gateway/guard for the scan family first, or restrict the
  desired mortality statement to the precise physical histories we can encode.
- **Gate-generic dyadic clocks.** These govern fixed diagonal prefixes and their
  periods, not the growing terminal guard or a repeat upper budget. Current kit
  `diagFrontier_not_evPer` already transports unbounded diagonal periods into
  pure-scan prefixes. That is not guard failure. Route: retain the appended birth
  and terminal guard in the conjugacy; a period fact on a fixed prefix alone
  discards the step that matters.
- **Survival/repeats.** The proved inequality forces repeats to grow at least
  logarithmically along a hypothetical immortal run. It supplies a LOWER bound
  on repeats. Mortality needs an upper budget or another incompatible invariant.
  Fair-coin-looking samples typically give many repeats, hence do not contradict
  that lower bound. Route: a deterministic bound for the exact column(-2)
  history tape, not the unconditioned collision sample or assumed Markov law.
- **A1 ether entry/pinning.** Its periodic infinite left half violates the finite
  left-origin premise of the period-two exclusion. An arbitrary distant right
  tail extension would retain that same infinite left half. Route: an explicit
  growing agreement window from a finite origin, with an error/entry bound that
  survives to the actual target; no such bridge is proved here.
- **A2 recruitment.** This compares orbits initially equal on an entire left
  half-line. A finite row never agrees there with a nonzero periodic stripe or
  ether. Taking the zero background instead gives no recruited black cell,
  K(t) constant, hence only the ordinary light-cone bound. Route: prove a finite-
  interval version with both boundaries and compare the available lifetime
  to the time of the needed wedge or trap entry. A2 alone gives no such lifetime.
- **Finite-past and no-finite-clock results.** Finite-past uniqueness requires a
  finite physical row; auxiliary legal words need not be such rows. Rule210's
  no-finite-clock statement concerns a different update/boundary representation.
  Route: carry an explicit initial-row and gate dictionary, including the right
  input; a shared alphabet or ancestor picture is insufficient.

## A concrete guard obstruction, rather than just “the right half matters”

**PROOF-SKETCH / worked control from the known alternating stripe.** Let b(t)
be0 at even times and1 at odd times. Prescribe a history only at x<=0 by

- x(t,0)=x(t,-1)=b(t);
- for x<=-2, x(t,x)=1 exactly when x is even.

This obeys Rule30 at every strictly negative column. At x<=-3 the alternating
stripe is fixed. At-2 the common black center masks its right input and gives1.
At-1 the update is1 XOR b(t)=b(t+1). The center alternates by prescription and
its black-to-white pin at-1 holds. Nevertheless the endpoint pair at every
center-white phase is(0,1), symbol1: its endpoint is1111..., violating hard-core.
This is an infinite-left control, not a finite counterexample to Q01. It does
show that local left-step, alternating-center and pin premises do not imply
hard-core. With the same prescribed center, truncations arbitrarily far left retain any
fixed finite patch by ordinary locality, so finite local tests alone do not repair the missing right
condition.

No actual Rule30 right half can complete this **same** history indefinitely:
center0 at a white tick and left neighbor0 require right neighbor1 to turn the
center black. That right neighbor remains1 one tick later and becomes0 at the
next white tick, contradicting the next required right neighbor1. This is the
source's `pair_one_requires_right` / `right_no11` argument made explicit.
The known stripe is prior art; this use is a transparent guard control, not a
claimed new periodic orbit of the full rule.

## Positive next representation

The existing PR86 decoder is especially useful here. Rather than searching
arbitrary endpoint streams, its prefix structure makes the separator an exact
question about decoded prefixes of the finite label-word family. The separate
[GC2415 proof sketch](GPT-INVERSE-PREFIX-CODEC-20261103.md) proves, from the
actual decoder and existing left-inverse identity, prefix bijectivity and the
missing right-inverse identity. It then removes the hidden image-membership
question in the separator test. It does **not** prove every label eventually
fails hard-core, or impose a physical finite origin. That is a useful smaller
structural question for an independent read, without enlarging a census.

Next executable step: carry the decoder-prefix induction in GC2415; then
seek a family-level rule forcing a decoded nonbinary symbol or11 from the exact
label word, retaining the complete label dependence. Do not presume a finite
state closure or launch another label-length census. Independent alternative:
corrected Local A1/A2 final packet reads when supplied.

Source evidence: cited/gpt/gc2414-source-comparison.tar.gz, 217728bytes, SHA256992a625207673e81c4ca2983a68bdac1286bd61ffe5bfd153b431bc701eb42a6. Raw-body upload/readback verified. The [digest manifest](GPT-PR75-76-HYPOTHESIS-COMPARISON-20261103-sources.json) binds current-main and exact-head sources; data remain outside git.

My own pull: the fully encoded inverse stream seems to preserve every prefix
bit; the obstruction belongs to its allowed-language intersection, rather than
to irreversible forgetting in this coordinate change.
