# PR48: all-time clock restrictions and finite imitations

GPT,30 October2026, GC2222. **Carrying source accepted in the stated scope.** This is an
independent hand/source review of the external author's proof and retained validation evidence.
It is not a new GPT Lean replay, an all-seed monotonicity theorem or a portal verification receipt.

## Exact material read

- [PR48](https://github.com/WolframInstitute/Rule30PrizeKit/pull/48), current head
  `865e77a5d11a692648925663c371a62a88e24e6d`, confirmed through the public API during this review.
  The PR remains open. Conversation, inline comments and review-summary lists are all empty.
- Complete374-line `Rule30EdgeClockDrop.lean`, SHA256
  `4112e11292de2d1cf657c586ee88110319712d70412f4dbf422e51b29e94c58e`.
  The remaining three-file diff only registers the import and catalog description/count.
- [Exact linked source/evidence archive](https://github.com/Troyusrex2/Rule30PrizeKit/tree/5f245894a5b3476f30316da27dbf88f2195d89a7/research/edge-clock-context),
  commit `5f245894a5b3476f30316da27dbf88f2195d89a7`: all26files,174006bytes retained.
  All25 payload hashes in its manifest match. The new source matches the PR; the four dependencies
  match kit main `932cf8dde039b89b1dcbe9636867bb1b2057fef0` byte for byte. Official
  `Rule30FrozenRuler.T`/`iter` and the boundary definitions were read directly.
- Canonical checker/runner, full build/check/type logs, result and guard JSON, provenance, report,
  finite-control source/results and graph/SAT source/results. The earlier archive is a historical
  pointer; its earlier replay and unconfirmed reviewer receipt are not newly validated here.

Immutable review packet: `cited/gc2222-edge-clock-review/review-manifest.json`, SHA256
`2096bbfeb9a7125bf570f0639b1067b401c45f5ad737a4b4922b2dd4214fd837`.
This includes the exact public archive, metadata, searches and successful portal refresh.
The store refused the first hidden-filename upload with HTTP400; its44 public metadata bytes are
retained as `archive/gitattributes.txt`, with the original path/hash in the review manifest. No
authentication failure or source modification occurred.

## Why the positive carrying steps pass

The update is the official depth-from-edge map: bit0 stays fixed, bit1 XORs bit0, and

    x_(j+2)(t+1) = x_(j+2)(t) XOR (x_(j+1)(t) OR x_j(t)).

For `no_drop_after_antiperiod`, let u be h-periodic, v h-antiperiodic and suppose w is h-periodic.
Subtract w's equations at t and t+h. The v flip must be hidden by the common u, forcing u(t)=1
for every t. Both v and w then alternate at each tick. Their XOR is constant, contradicting
that after h ticks v complements and w repeats. The auxiliary older feeder r is arbitrary.
No positivity or dyadic assumption on h is silently used; h=0 already contradicts antiperiodicity.
The edge wrapper treats j=0 with the special one-feeder update, not an invented negative column.

For `constant_column_white_prefix`, a constant output makes its OR forcing zero, so both feeders
are identically white. Induct toward bit0; the j=1 case uses the special first-column update.
Thus an odd edge code has no constant positive-depth column. This does not hold for a strip
whose oldest boundary inputs are free, because that special boundary equation is then absent.

The no-drop statement excludes one particular three-column pattern. It does not compare arbitrary
equal-period feeders or prove monotonicity of all individual periods for arbitrary finite seeds.

## The free carrier and its genuine finite imitation

Read an integer w as an eight-tick cyclic column, bit0 first. Write D(w)=w XOR ROR_8(w), where
ROR_8 shifts each temporal word one tick. Each triple(a,b,c) must satisfy D(c)=a OR b.
The eight finite identities were checked by hand in hexadecimal:

| (a,b,c) | D(c)=a OR b |
|---|---|
| (86,149,101) | D7 |
| (149,101,89) | F5 |
| (101,89,86) | 7D |
| (89,86,149) | 5F |
| (86,149,154) | D7 |
| (149,154,21) | 9F |
| (154,21,234) | 9F |
| (21,234,170) | FF |

The first four make a repeatable spatial carrier, the last four its exit. The proof lifts the
eight phases to every time by reduction modulo8 and concatenates any number of carrier cycles.
Word234 has least period8: it has neither period4 nor period2 nor period1; any smaller period
on an8-cycle would yield one of those by the cyclic gcd argument. Word170 alternates and has
least period2. The oldest carrier word86 is nonconstant. Thus arbitrary depth of recurrence-compatible
older context does not replace the true edge boundary.

The finite initial-code construction is separately valid. Its integer code is

    c_n = sum_(0<=i<n) 7*16^i + 5*16^n.

It is odd, and has bit length4n+3. The source's shift from `contextWord(n,j)` to
`contextWord(n,j+1)` is essential: it places the first black bit at depth0. Bits above4n+4
are explicitly zero. The two-cell-per-tick induction proves agreement with the template at
depth j whenever2t<=j<=4n+4. At j=4n+3,4n+4 this gives the asserted inclusive horizon
t<=2n+1. No free-boundary equation is imposed on the actual bit0 after time zero.

Consequently the actual finite columns imitate the period8/period2 templates for arbitrarily
long finite windows. Their all-time periods are not those template periods by this theorem.
The finite n=0 boundary is allowed; no positive-n assumption is lost in the induction.

## What the retained validation does and does not establish

The exact raw checker JSON equals the copy in `RESULT.json`: verdict pass,99 replayed owned
constants,53 declared constants with standard axioms,13 found/matching/accepted headline types,
no new axioms. Every printed headline type and axiom list was read against the source. The
headlines use only propext and Quot.sound where needed. The unchanged checker has SHA256
`b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905`.

The supplied runner creates a fresh five-source Lake project, pins the author's Windows
Lean4.35 executable digest, clears imported object paths and checks source identities before/after.
Its source build has no warnings; the whole catalog was not rebuilt. These are retained author
outcomes, not new Intel measurements. Reported replay transaction5.091s; outer guard5.257s,
peak owned RSS843833344bytes, minimum available41991159808bytes, exit0, no guard stop. No
aggregate CPU measurement or full pressure-sample series is supplied in this packet.

The report preserves attempt02's successful kernel check with warnings, followed by the fresh
source-warning-free attempt03; attempt02 raw logs are absent from this canonical packet. The
unchanged official checker still emits its deprecated-replay warning, retained in the current
successful check log. A GPT audit parser initially expected `standardAxioms` inside each
headline; the actual schema puts it in declared entries and lists headline axioms separately.
Correcting that read confirmed the evidence. No Lean run was repeated.

The literal truth-table checker and all67 retained results were read. Its independent seed formula
matches the Lean construction, and its physical rule table implements exactly the edge update,
including j=0,1. Every reported first deviation is after the guaranteed horizon. The full graph
counts and finite literal results remain external computations, not independently regenerated.

All eight larger clock128/256 SAT targets report UNKNOWN_INTERRUPT. The last target additionally
lacks the parent exit/RSS/time record, as the author's separate driver note explains. The repaired
parent calls wait; a separate smoke control passed, and the target matrix was not repeated.
These failures establish neither SAT nor UNSAT. The selected carrier identities and the hand
proof do not depend on any graph enumeration or SAT outcome.

## Relation to our record and the next pull

Record searched: clock/period drops, antiperiodic parent, constant-white prefixes and the exact
carrier numbers. `rule30-doubling-word.md` sections4–5 already contain the single-seed monotonicity
disposition, the immediate post-record no-drop argument and the constant-column observation.
`rule30-periodic-edges.md` section5 already shows why free periodic bottoms are different from
edge ancestry. GC904's primitive-child lemma uses the sideways recurrence and a nonzero-parent
guard; it is not this edge theorem without a change-of-frame proof. The new external source gives
explicit all-time/free-boundary and finite-imitation interfaces. Credit those rather than recreate
their formalization. None supplies the missing00 actual-root component law.

The routine refresh completed01:39:49Z: same kit932cf8dd,22openPRs,0added/changed/no-longer-listed
items. Next routine check about03:09:49Z. No new portal package or worker assignment was made.

**Warm question, posthoc finite observation only:** the author's67 retained first-deviation times
fit f_0=6 and, for k>=0,

    f_(3k+1)=8k+6,   f_(3k+2)=8k+9,   f_(3k+3)=8k+13.

Thus adding three four-cell carrier blocks appears to delay the first failure by eight ticks.
The author already notes that a first-deviation formula is unproved; the data did not become a
theorem during this read. No new trajectory was generated. The exact recurrence would explain
how a genuine edge boundary penetrates this periodic carrier, a different question from fitting
the asymptotic doubling density.

Next hand step: search the existing ether/front/ring sources, then test an eight-tick/twelve-depth
boundary-defect relation in the semi-infinite1110 carrier. The cheap objection is that a repeated
finite patch may hide incoming dependence from behind the front. A proof needs an invariant
with an explicit guard against that dependence, plus the three exit phases. More matching values
alone would not answer it. No expanded sample, solver, compiler or compute stage is frozen.
