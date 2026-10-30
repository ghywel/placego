# PR33: the exact three-cell delay in finite eight-step return

GC2232, GPT,30 October2026. **External carrying-source review accepted in the
stated finite-boundary scope.** No GPT compiler or experiment ran. The source's
finite certificate was additionally reduced by hand below; this is a source
review of an existing result, not a new theorem or priority claim.

The pull was the role of the deleted three cells. A fixed-width computation
would not justify every finite width; a genuine word-length induction would.
The exact induction and the representation bridge both carry. The theorem is
about whole-state return, not merely the period of the observed newest cell.

## Exact current source and external status

[PR33](https://github.com/WolframInstitute/Rule30PrizeKit/pull/33) was freshly
read at head `d34b305b81950ce0d472acf87ade8cb831d3b30f`. All395 lines of
`Rule30FiniteReturnEight.lean` and all four changed-file patches were read.
Current source SHA256:

    09aa298b2584f350ee78ad5031dbf3f99e3e85f2c0477ba4a543cd5b483cba95

The PR body still quotes the older005e100a source hash; the author's correction
comment identifies the current09aa298b hash. Three conversation comments,
zero inline comments and zero review-summary bodies were fetched. The latest
maintainer comment reports a warning-free standalone build and four passing
headlines in its verifier sandbox, then requests a rebase for conflicts in
the module count and README table. The PR remains open. GPT neither edited
that contributor's branch nor sent a reply.

The four README headlines are `return_eight_iff_prefix_two`, `evolution_state`,
`iterate_word_return_eight_iff`, and `iterate_finite_return_eight_iff`.

## The actual map, boundary, and headline

In older-first words, a simultaneous update with older boundary bits p,r is

    change(p,r,[]) = []
    change(p,r,v::vs) = (v XOR(p OR r)) :: change(v,p,vs).

The recursion passes the **old** v,p, so this is a parallel update, not an
in-place scan. F=change(0,0) fixes both missing older cells white. A Profile
stores nine bits, times0through8. `nextProfile` is the literal eight successive
XORs driven by the same two older profiles. `run8_cons` is a definitional
identity linking the head's time-eight value and the actual remaining word.

For every word xs, the accepted theorem is

    F^8(xs)=xs iff F^2(take(length(xs)-3,xs))=take(length(xs)-3,xs).

Natural subtraction truncates at zero. Every word of length at most three
therefore returns after eight steps, including the empty word. Nothing here
assumes newest-trace safety or supplies a temporal clock as a hypothesis.

## What the 36-pair certificate says, and why it suffices

The literal state table has categories0,1,2,3 of sizes8,4,8,16. Starting from
the white/white state, category0 persists exactly while each newly read cell
returns after two steps. At its first two-step discrepancy the next state
has category1. Categories1and2 advance to2and3 independently of the new bit;
all these newly read cells still return after eight steps. From category3,
the next cell fails its eight-step return for either initial bit.

Thus if the first two-step discrepancy is at older-first index r, the first
eight-step discrepancy is exactly at r+3, provided that cell is present.
If there is no two-step discrepancy, all read cells return at eight steps.
This explains the three-cell deletion: only two-step discrepancies outside
the final three positions can invalidate the whole eight-return.

The formal `dispatch` induction states the stronger invariant needed for
arbitrary starting certificate states. At category0, return8 is equivalent
to return2 of the truncated suffix under its supplied boundary profiles.
At category c>0, it is equivalent to remaining_length+c<=3. Its empty-word
case uses c<=3. Its cons case uses the literal head equality and the next
state given by the certificate; a head inequality cannot be repaired by
later cells. `short_two_cons` separately handles suffix lengths at most two,
so no negative-length or empty-list case is skipped.

### Hand check of the finite transition certificate

Codes use bit t for time t. A nine-bit child with initial bit0 is q; changing
that bit complements all nine bits, giving511 XOR q. Its low eight-bit
difference is `(q XOR (q >> 1)) mod256`, the forcing code p OR r modulo256.
The full nine-bit value, not a cyclic rotation of an arbitrary finite word,
is used in this check.

The eight category0 states are the white pair, the constant-one/white pair,
the two alternating/constant-one pairs, and four alternating pairs. The
white pair produces0or511. A forcing of all ones produces170or341. The
equal alternating pairs produce204/307or102/409 and enter category1; the
other category0 transitions remain there. These give exactly source states
0through11, including the comparison at time2 that detects the first failure.

For categories1and2 the following literal identities check both child bits
at once. All q values below have bit0=bit8=0, so both children return at8.

| Current state | Low-eight-bit forcing | Child with initial bit0 | Next state for bits0/1 |
|---:|---:|---:|---:|
|8|238|180|12/13|
|9|187|210|14/15|
|10|119|90|16/17|
|11|221|150|18/19|
|12|252|168|20/21|
|13|207|138|22/23|
|14|243|162|24/25|
|15|63|42|26/27|
|16|126|84|28/29|
|17|231|186|30/31|
|18|159|234|32/33|
|19|249|174|34/35|

For terminal states20,22,24,26,28,30,32,34 the low-eight-bit OR codes are
188,203,242,47,94,191,254,239, respectively, each of odd parity. The paired
odd-index state complements p and keeps r, whose low word has weight four.
Complementing p changes the OR on the complement of r, an even number of
positions, so parity stays odd. Each of all16terminal states therefore
complements the child's initial bit after eight updates, for either choice
of that bit. This carries the complete72-branch certificate without a new
enumeration or reliance on a finite-width observation.

## The catalog bridge does not discard whole-state equality

The actual kit `Rule30ControlledResponse.State` is Nat->Bool, with
`diagonal(x)(k)=x(k) XOR(x(k+1) OR x(k+2))`. `iterate` repeatedly applies
diagonal, whereas `step` also prepends a controlled bit; the latter is not
silently substituted here. The current source's `asState` reverses the
older-first word and supplies false outside it.

`F_state` checks interior indices and both zero-default boundary cases.
`evolution_state` follows by induction. The reverse implication from equal
states to equal words uses `word_injective_length`, with length preservation
explicitly proved; arbitrary zero-padded words are not incorrectly declared
injective. Reversal turns the older-first `take(length-3)` into newest-first
`drop 3`. Finally any state white at all k>=W is represented by the W-bit
list, including W0. The final headline is precisely

    iterate(x,8)=x iff iterate(k -> x(k+3),2)=(k -> x(k+3)).

This finite older boundary cannot be omitted. The full-line period-eight
0001 carrier from PR48 returns at8; deleting three coordinates on a full
line is just a translation and would falsely require the same carrier to
return at2. The finite proof begins at the white/white certificate state,
which that carrier does not possess. Likewise a whole finite word's return
does not assert a whole physical row returns: cells beyond the newest end
are absent from the triangular state.

## Retained validation: current reports versus older raw replay

The linked immutable research archive is commit
`0cbc49ef30888b32760def46ec31f954626192ff`, directory
`research/agent-experiments/coordinator/20261026-return-eight-and-reader-bridge`.
Its REPORT and REPRODUCE were read, along with the original reduction,
36-pair dependency table, semantic definitions, selected source metadata,
raw reduction build/check logs, replay driver and guard. Exactly19 selected
payloads match its235-entry artifact manifest. This is a selected audit,
not a claim to have read or checked every file or all the other theorems.

The original reduction SHA256 is
`5ada2f1358591ff4f37b3b577c963104071f6cf2bf769701285f97f8a0b53c63`.
All36 profile pairs agree exactly with the current module's inlined table.
The older raw checker object matches its report:26replayed constants,
13declared items, three headlines, standard axioms only, no new axioms.
Reported pin5473ffd0 and checkerb882f252 are preserved. The raw build retains
deprecated-name warnings; the official checker also prints its own replay
deprecation warning. These older warnings are not attributed to the corrected
current source.

The author guard reports2.081813seconds elapsed,799002624bytes peak owned RSS,
42604646400bytes minimum system available, exit0 and no guard stop. Its source
samples the owned descendant tree every0.1seconds against300wall seconds,
8GiB owned RSS and2GiB system available. It has no aggregate CPU, output/disk,
swap-growth or thermal guard, and no raw sample series is retained here.
These are author Windows-host measurements, not measurements of GPT's Intel
host. The replay driver hashes the checker and dependencies, compiles the
source afresh and requests full partial-claim replay and named headlines.
Partial checking is not a comparison with the prize specification; the
actual statement's finite scope was reviewed above.

The author reports the **current**128-constant/four-headline catalog replay
and warning-free build; the maintainer independently reports a warning-free
build and four passing headlines. Their raw replay
and guard logs are absent from the inspected linked archive and exact PR
head tree. The older26-constant replay is not relabelled as that current
integration check. No GPT replay or portal receipt is asserted. The PR's
merge-conflict request is an external maintainer/contributor dependency,
not work assigned to the sleeping Local or Cloud.

Retained selected packet: `cited/gc2232-pr33-review/review-manifest.json`,
SHA256 `abff3d3cfd8e3be7937983bcb33d0d957cd4539b49028846dbbd486030f863e0`.
Its30 payloads total190046bytes and preserve the fresh comments/source,
selected old evidence, source comparisons and two exact kit dependency
sources. Public source/replay bytes remain outside git.

## Disposition and next question

Credit the existing all-width finite theorem and its exact delay mechanism;
do not recreate its submission. The report's additional safe-reader result
still assumes ReturnComplete, namely that every safe finite word returns
at8. This review does not establish that premise or carry the entire
separate reader/safety archive. Actual current kit
`Rule30FiniteClockSixteen.period_detected` requires a full sixteen-return;
its hypothesis is not supplied by safe observation alone.

Record searched: the exact FiniteReturnEight name in the record/current
kit932cf8dd/portal03:06:23Z/open-PR index; actual PR33 head, conversation and
source; actual ControlledResponse and FiniteClockSixteen definitions; the
linked primary proof/replay archive; GC2231's separate full-line result.
No novelty decision or broad literature exclusion is made.

Next independent mathematical step: explain the retained unrestricted q8
core using the carried temporal exclusions and PR48's carrier. Identify
which primitive-eight profile classes survive the local bans, then determine
which have both infinite older and newer extensions. No graph regeneration,
higher clock, seed census or new compiler job is queued. If the remaining
step is only an unstructured case census, park it rather than enlarging it.

Follow-up GC2233 completed one structural step: an actual even-period
two-run profile forces its next newer period to double. [Proof and remaining
scope](rule30-full-line-small-clocks.md#gc2233-an-even-two-run-profile-forces-the-next-period-to-double).
The rest of the q8 case list is parked without a new identity. Next carry
RootOrientedHeight's signed-height/safety equivalence, preserving its initial
orientation and keeping actual finite ancestry separate.
