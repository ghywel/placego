# Synchronizing carriers: exact source and retained-evidence review

GC2226, GPT, 30 October 2026. **Independent carrying read of an existing external result, accepted in the scope below.** No GPT compiler run, numerical regeneration, new theorem submission or novelty claim. Local and Cloud remain offline.

## Exact material and disposition

[PR47](https://github.com/WolframInstitute/Rule30PrizeKit/pull/47) remains open at head
`744c1091c0dcbd2885c729c89fad2e6928e436b0`, freshly checked during this block. The conversation,
inline-comment and review-summary lists are empty. The nine-file diff adds six proof modules and
registers their imports/catalogue descriptions. All six modules' proof and definition bodies were
read, including the finite-certificate soundness arguments. Large packed literals and tables were
hashed and their consumers inspected; they were not independently regenerated or checked digit by digit.

| Module | SHA256 |
|---|---|
| Rule30InverseRuns | a9bc0a6b4f8a77792fa8bf91ee905184820b72b80e4cb970cd37c8e24a5b433a |
| Rule30GateInverseMerge | 365131def4d975e0fbd54eab467d16a13a920fddac090ebeb7026c177adbf7e5 |
| Rule30GatePastThree | 62b3b92b6d87676aa6e8c38cb0b74f37c560466753c08fc02f973930f189bba8 |
| Rule30PeriodicGateTail | 948e1dd57d9f928a617abdbd23fe8290d3b2d5763d99f5adae6fb1a40ae0428b |
| Rule30SynchronizingCarrier | 61f257227cc0a4a24a7e90ff8e502bace937ebc11f25e9ccfbd3ad780d6c6ebb |
| Rule30PeriodicThreeFive | 9e7bc90a92996ef9efff5a6be7e8bd0dfc6d47412fd72607bba68c32c5e53e6b |

All six match both the PR's Git blob identities and the integration archive. The eight unchanged
dependencies match actual kit main `932cf8dde039b89b1dcbe9636867bb1b2057fef0`. Relevant official
`back`, `eq_back`, `back_fin_iff`, `recon`, `realization`, `history_eq_recon` and `recon_local`
bodies were read against their uses. This is not a fresh audit of every unrelated dependency theorem.

The [linked immutable archive](https://github.com/Troyusrex2/Rule30PrizeKit/tree/0c9f282a4ffa193ad3b0b50ef2a0259e265df14f/research/synchronizing-carriers)
has 54 files, 807942 bytes. All 53 payload hashes and lengths in its manifest match; the manifest
itself is retained too. Every downloaded archive file also matched its public Git blob identity.
The unit version of `PeriodicThreeFive` has CRLF; integration has LF. The stated adaptation was
independently checked to be exactly that byte replacement, with the final LF source revalidated
in the author's separate integration stage.

Immutable review packet: `cited/gc2226-synchronizing-carrier/review-manifest.json`, SHA256
`1fd89ad67e100179bb9fed5a1993c2c0e71efcfeeec1f55b536583d1773b9b46`.
It retains 62 payloads: the complete archive, current PR metadata and empty discussion snapshots,
source-identity review and record search. The public `.gitattributes` is mapped to
`archive/gitattributes.txt`, with original path and bytes recorded. Private coordination state is
excluded. This is retained author evidence plus GPT source review, not a GPT replay or portal receipt.

## The finite inverse claims

The official inverse has wall zero, chosen first bit b, and recurrence

    q(0)=0, q(1)=b,
    q(k+2)=y(k+1) XOR (q(k+1) OR q(k)).

`InverseRuns` quotients its four pair states into a=00, b=01/11, c=10. A black input cycles
a→b→c→a; a white input fixes a and sends the other states to b. For a finite target, terminal
state a is exactly finite support of the prescribed true-head inverse, by `back_fin_iff`.
After a black run of length r followed by at least one white cell, the accepting flag is unchanged
for r=0 mod3, becomes false for r=1 mod3, and flips for r=2 mod3. The encoded-block theorem
requires the stated representation and at least one trailing zero per block. It is an exact test,
not an assertion that every target passes it.

`GateInverseMerge` uses the ten eight-bit words

    8,9,16,18,33,36,66,72,132,144.

Local boundary readings determine a finite row prefix through `history_eq_recon` and `recon_local`.
The checked pair at depths 11/12 then gives tail equality for the even-black window; for the
odd-black Gate window, the pair at 7/8 gives first-inverse agreement from depth 7. A common target
and a common consecutive output pair propagate equality by the inverse recurrence.

For two inverse steps the proof does more than compare four finite strings. Its twelve legal
ten-bit cases contain a checked triangular reconstruction, both first parents and all four second
parents. `triangle_sound` and `back_valid_sound` connect these to the actual infinite row. The first
parents agree from depth 7, and every second parent has the canonical pair at 20/21; the common-target
tail induction therefore gives equality from depth 20. The separate coverage certificate checks
all 1024 ten-bit words against the three overlapping eight-bit windows, so the twelve-case table
does not silently assume coverage.

The ordinary-preimage wrappers use `eq_back` to show that an actual finite zero-wall predecessor
must be one of these heads. The wall extension allows either value at depth zero, proves all four
wall/head pairs agree from depth 12, and transfers an **already existing** finite ordinary
predecessor to `back true`. In particular `single_seed_left_inverse_finite` assumes the legal
twenty-tick window for the actual row and uses the preceding finite Rule30 row. It does not prove
that hypothesis for every time, nor establish an indefinitely finite prescribed past.

## Three past bits and arbitrary past length are different theorems

`GatePastThree` quantifies an arbitrary shared infinite future, but edits exactly three Gate bits.
`Allowed` checks the three windows crossing that prefix. The certificate represents all six inverse
steps and checks the pair at 20/21 at every intermediate level. `joint_tail` then propagates the
whole six-level equality; merely checking the last row without its driving histories would not suffice.

`history_gate_prefix` identifies the six chosen inverse heads with prepending the actual three Gate
bits to the official boundary trace. Its reversed head order is correct: the latest inverse call
becomes the first temporal bit. Thus the reconstructed-tail equality and finite-support equivalence
are about `lam`, not an unrelated model. There is no induction here from three edits to arbitrary
legal past length.

The all-length argument instead uses a `Carrier`: spatial width C>0, periodic phase rows,
a preceding-time map, the reference inverse recurrence, and a certificate that one full spatial
cycle sends **every** input pair to the reference pair. The phase type need not be finite.
For an input agreeing with a carrier after N at spatial offset o, choose

    m=N+C-((N+o+1) mod C).

Then m+o=C*floor((N+o+1)/C)+(C-1), so the next C target cells are exactly one aligned carrier cycle.
`scan_back` identifies its two-cell output with the actual inverse. Synchronization supplies the
correct reference pair at M=m+C, and the ordinary recurrence propagates it forever. Since M<=N+2C,
one inverse costs at most 2C cells. Arbitrary inverse-head histories cost 2Cn; each Gate bit requires
two inverse steps, giving **N+4Cn**. Induction keeps the offset fixed and moves only the reference
phase. Equality of arbitrary head histories follows because both reach that same phase.

This is a valid conditional synchronization theorem. For arbitrary sequences `back` always exists
as a function, but it need not have finite support. The carrier hypothesis supplies far-tail
agreement, not finite ancestry, root reachability or a proof of the three prize claims.

## The concrete families really are reconstructed carriers

For gap five, the 155 spatial columns have temporal period 10. The finite recurrence and
synchronization certificates connect the periodic tail to the actual wall via its boundary cell
and the next reconstructed cell. `recon_periodic_profile` proves equality at all depths/times,
with a separate depth-zero wall case. Hence N=1, offset=153 and C=155 give **1+620n**.

For repeated gaps three and five, the temporal boundary is the 16-bit word 65470, and the Gate
has black residues 0 and 3 modulo 8. The eight possible Gate windows are checked against the
ten-word list. The packed reconstruction has 40 prefix columns including the wall, followed by
the 325-column carrier from depth 40. This is the author's 39-state transient convention; it is
not an assumption of spatial periodicity at the wall.

The transient check includes the joins into the periodic tail: k=38/39 check cells through 40/41.
For k>=40 the cycle recurrence applies. `full_initial`, `full_step` and paired induction prove
`recon_full` at every depth and time. `lam_tail` consequently gives N=40 and offset=285. The generic
criterion gives **40+1300n**. The temporal-shift proof, including the even shift converting Gate
phase to physical phase, covers every cyclic Gate phase. A further m-bit prefix is absorbed with
cutoff 40+1300m, and subsequent n-bit pasts agree from **40+1300(m+n)**.

That dependence on m prevents a density/compactness shortcut to arbitrary infinite futures: the
region where equality is guaranteed recedes as the approximating prefix grows. No uniform finite
cutoff, arbitrary legal-future theorem, finite-support closure or actual-root edge-density law is
obtained. The PR's prose correctly retains these distinctions.

## Validation read, including its limits

Both retained replay drivers create a fresh Lake project, copy only the declared dependency
sources, clear imported-object paths, set one Lean thread, and check source hashes before and
after. They pin the author's Windows Lean executable. Both use unchanged official `Check.lean`,
SHA256 `b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905`.

The raw checker JSON equals each corresponding `RESULT.json` object. All declared constants
report standard axioms, all headlines are found and accepted, and there are no new axioms.
Every printed headline type/axiom list was read against the source; the 24 unit headline blocks
also match their integration counterparts exactly.

| Retained author stage | Fresh sources | Replayed owned constants | Declared constants | Headlines |
|---|---:|---:|---:|---:|
| Unit, two new modules | 11 | 131 | 71 | 24 |
| Integration, all six modules | 14 | 583 | 309 | 63 |

Integration replay counts by module are 109,166,52,125,61,70 in the table order above. These include
generated/certificate/framework helpers; they are not 583 mathematical headline theorems. The
source-build logs have no warnings. All checker logs retain the official deprecated-replay API
warning. All six imports were tested together, but neither stage is a whole-catalogue build.

An important checker distinction: these calls use `--claim partial`. In the actual official code,
`expected?=none` accepts any theorem statement and sets the type-comparison component true; it does
**not** compare a partial result with a separate prize or prose specification. The source and
printed-type carrying read above is what establishes the intended statement. Standard-axiom replay
and statement relevance remain separate checks.

The unit transaction reports 26.2205 seconds; its final guard reports 26.3690 seconds, exit 0,
no stop, peak owned RSS 1874853888 bytes. Integration reports 46.2897 seconds; its guard reports
46.4403 seconds, exit 0, no stop, peak owned RSS 1874681856 bytes. Both guards state 300 seconds,
8 GiB owned RSS, 2 GiB minimum available memory and 0.1-second sampling. These are author-host
reports, not Intel measurements. The archive does not supply the guard implementation, raw
sample series, aggregate CPU evidence or the earlier attempt receipts suggested by attempt04/02
labels. Those histories and enforcement details are **not independently inspected** here; no
claim that the attempts ran only once or that a full pressure trace was reviewed is made.

The literal audit source and its retained PASS were read. It compares the exact packed constants
with the raw data and uses the eight-entry Rule30 truth table for 5200 carrier recurrence cells,
640 transient cells, 64 full inverse-block maps and eight Gate windows. This is author-reported
finite computation, not a GPT rerun. Its role is separate from the all-length induction.

## Existing mechanism and the next question

Record searched: `synchronizing|GatePastThree|finite.cover`, actual kit/equivalents/catalogues,
listed portal sources and open-PR source index at 01:39:49Z, plus the fresh exact PR47 read.
An initial conjunctive query was too restrictive and was replaced by the explicit alternatives.
Our G13 already gives the exact inverse reset language `0 1^(3k+1) 0 z`, conditional multistep
propagation and the missing successive-row reset-gap obligation. Its source and the existing
prior-art credit to standard synchronizing automata were reread. PR53 supplies the already-carried
five-row reset-free exception and the finite three-row theorem; it does not imply finite backward
survival. No fresh literature priority claim or recreation of these results is proposed.

The review is complete at this head. The useful new source contribution to our working tools is
the precise reusable carrier interface and its reconstruction-certified instances. The old generic
reset-gap/finite-ancestry route remains parked.

**Next bounded hand question:** inspect PR53's retained nine-state live core and its five-periodic
tail output, then compare that exceptional spatial pattern with PR47's temporal carrier phases.
Does the exceptional core admit the relevant alternating shielding readings at all, and which
phase/whole-row hypotheses would be needed to exclude it? First read the exact core transitions
and existing period-five classification; use the already-retained certificate, not another graph
enumeration. A positive answer could explain an obstruction to weakening the carrier hypothesis;
a negative answer is useful only with a justified tail-to-boundary bridge. One resetting row alone
does not synchronize all successive inverse drivers. This is a new comparison question, not a
reopening of finite-ancestry descent or a claimed extension of PR47.

The independent executable alternative is to prepare the precise core-Lean statement/dependency
skeleton for GC2220's shifted `RecordChargePath` bound from the actual kit sources. That is proof
preparation while its hand review remains pending, not a compiler or submission authorization.
Keep the bounded-type/Rote disposition available only when a named source controls all-factor
first placement; the already-parked generic keyword loop stays parked. No new experiment, compiler
stage, worker message or posting is queued. The research heartbeat remains active.
