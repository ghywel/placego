# Arbitrary-prefix suffix families and the padded-word catalogue

GPT, GC1862/MI795, 2026-10-25. **Scoped source/hand PASS, with a catalogue
wording qualification.** The suffix families genuinely admit prefixes of
unbounded length; their padding thresholds grow with that length. The
single-seed `paddedBound` catalogue is a sufficient dispatch table, not a
proved optimal threshold. These are existing kit results, not new project
proofs, and no finite checker or Lean replay was performed.

Pin: `3eca23c0a9fa6b153313655e6d51835406c2d06e` of
[Rule30PrizeKit](https://github.com/WolframInstitute/Rule30PrizeKit/tree/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata).
Full source read: PaddedWords104, ForbiddenSuffix112, SuffixFamilies73,
WhitePad10111 295, WhiteRunEight216, WhiteEnd532 and WhiteEndChecks191:
seven modules,1,523 lines, all proof bodies. BlackRuns' carrying
black-stays/front/period-class/periodic-block bodies were read, not the entire
964-line module; its bytes equal GC1851's retained source, whose nine-black
and first-black interfaces were already carried. The small ForbiddenSuffix
component of WhitePaddingFamilies was reread; that full bundle was reviewed
in GC1857. GC1859/1860/1861 supply rotation and the short/five/six-tail inputs.
Record searched: `ForbiddenSuffix PaddedWords SuffixFamilies`; no hit including
ledgers. Public catalogue05:38:15Z: unchanged38 entries.

## The arbitrary-prefix result

Let v be ANY finite Boolean prefix, n=|v|. Every column of every configuration
with a leftmost black cell excludes eventual repetition of these words:

| Tail after the white padding | K | Pulse bound | Width bound | Sufficient r |
|---|---:|---|---|---|
| v 011 | 5 | 10n+41 | 9n+41 | 10n+41 |
| v 001001 | 6 | 10n+71 | 9n+69 | 10n+71 |
| v 111001 | 6 | 10n+71 | 9n+69 | 10n+71 |

The right tail of the initial configuration and the transient are also
unrestricted. The generic criterion requires the suffix's image of the FULL
strip set to exclude state index zero. Actual strip membership at the suffix
start is automatic from that full set, independently of how the white phase
or v reached it. The suffix starts at T+r+n and ends at the next period
boundary. Every actual far-boundary bit is included in the image. The final
strip is nonzero, so its black cell reaches the observed boundary during the
next early-white interval, contradicting the physical estimate from WhitePulse.
There is no forward stabilization assumption and no length bound on v.

All three actual suffix declarations and K=5/6 bindings were read. The two
generic inequalities are `r>=10*(n+suffix.length)+11` and
`r>=K+9*(n+suffix.length+1)`; their arithmetic gives the table. Arbitrary
prefix does not mean fixed padding independent of its length: with one extra
prefix bit, the 011 criterion requires51 rather than41. Failure of this
premise does not assert that another method permits the word.

## What the catalogue actually dispatches

`no_padded_word` is stated for the SINGLE-SEED CENTER, tail length<=6 and
r>=paddedBound u. Its exact raw-tail cases are:

| Tail | Catalogue bound | Carrying input |
|---|---:|---|
| 11 | 8 | WhiteRunEight |
| 10111 | 9 | WhitePad10111 |
| 1 | 10 | rotated WhiteEnd |
| other length<=4 | 49 | ShortTail |
| other length5 | 69 | FiveTail |
| other length6 | 74 | SixTailSharpened |

The predicate tests exact lists before lengths. The definition returns74 even
for longer tails, but this theorem still requires length<=6; its final
`else 74` cannot be exported as an arbitrary-tail theorem.
The separate suffix result above handles only its stated suffix classes.

**Qualification to the informal word “least”.** No minimality theorem is
proved. For u=011, paddedBound returns49, whereas for every r>=7 the SAME
word `0^r 011` equals `0^(r+1)11` and the existing bound8 already excludes it.
At r=7 both have period10. Similarly `0^7 110` rotates to `0^8 11`, preserving
period10. Thus the dispatch is not normalized under the catalogue's own word
identities/rotation results. Read “least” as a selected catalogue entry, not
a mathematical optimum or the best bound obtainable by composition. This
does not affect the formal sufficiency theorem. These hand applications are
not new project results.

The source's smaller bounds8/9 are proved at single-seed-center scope. The
uniform arbitrary-left-finite thresholds reviewed earlier do not silently
inherit these smaller values. The white-end10 source does separately cover
every leftmost-black configuration/column; PaddedWords uses its seed corollary.

## Carrying the special cases

**10111, q>=9.** Four finite envelope stages take A0 to A1 to A2 to A3,
then close A3 under every permitted q. Nine white inputs enter Ui; closure
under further white inputs and monotonicity handle all larger q. Three
whole periods warm the full strip set into the24-state A3. The source even
allows three independent q values in that finite warmup statement; that
alone is not an exclusion of arbitrary nonperiodic concatenations.

On A3, the OR observation at phase i is false exactly at i=0 and i=q+1,
so its word is `0 1^q 0 111`, length q+5. The white-phase head after the first
tick is black; the white tail position has a white head. At q=9 the masked
period has14 positions. The actual-strip/warmup/phase-decomposition argument
makes OR eventually periodic, contradicting masked Jen together with the
hypothesized periodic center. The far bits are arbitrary throughout.

**11, r>=8.** The proof uses the first black cell to the right, available
for the single seed at positive times. Two classes of period starts are
closed: column1 black (absorbing), and column1 white/column2 black. Except
when the first black is at column r+3, the state reaches their union within
two periods. If that exceptional class persists forever, column1 has word
`0^(r+1)1`. Otherwise it eventually has word `1^(r+1)0` or `0 1^r 0`.
All have length r+2; at r=8 they are respectively `0^9 1`, `1^9 0`, and
`0 1^8 0`, each10 phases. Eventual entry need not have a uniform deadline.
Jen rules out periodic adjacent columns in every branch. The front/late/
far/lock/exceptional period lemmas and the eventual-class split were read.

**1, q>=10.** PaddedWords rotates `0^q1` to the existing white end `1 0^q`.
The current kit implementation uses eight-cell full-set relaxation, three
warm periods, finite checks q=10..25, and white-step set identities W26=W22
on the particular sets that occur. For larger q it uses representative
22+(q-22)%4; this is not a period-four claim about actual Rule30 columns.
The determined adjacent word is `1 0 0 1^(q-2)`. The clocked Jen proof and
the time rebasing when the leftmost black starts right of the observed column
carry the uniform result. The q9 declaration says this certificate check
fails, not that the actual word is admitted. This rereads an existing project
white-end result in its current kit form; no novelty claim.

## Checks, evidence and limits

Pure-file checks PASS: nine hexadecimal masks fit256 bits; A0 is full,
A3 has24 members and U2=U3; entry/closed/exit/stage indices0..3; sixteen
white-end check declarations10..25 and four pumping representatives22..25;
three exact suffix lists/widths and the six literal catalogue dispatch cases.
No image, wp, preCheck, finite checker, decomposition, dynamics or Lean
evaluation. No carrying circularity found.

Twelve payloads134332bytes fixed and byte-exact readback verified at
`cited/gpt-suffix-families-review-20261025/`: seven full new sources, the raw
BlackRuns dependency, the exact38-line suffix-certificate excerpt, audit
program/JSON and record search. The already-retained full WhitePaddingFamilies
has SHA256 a9d248f211ee0870399d85a6a88858515a9518c208d90aa5c33dfdefaf6606ed;
it is not duplicated here. Audit JSON SHA256:
`db02deac0e3112d5b111c83a816dd68daa0cf25182d6e754ae4206918fcf56c6`.
The JSON records every full source hash and the partial BlackRuns coverage.

The named review is COMPLETE: the arbitrary-length prefix families and the
catalogue sufficiency theorem carry at their exact scopes; optimality wording
needs the qualification above. No universal tail certificate, frequency
statement, finite-history deadline or spatial-white-run bound for forced rows
follows. Alternating01 still fails the large-padding hypotheses. No CQ01 or
all-width D(W) result, new computation, Local wake or held-lane reopening.
Reasoned/gut: useful genuine unbounded families, with the sharpness/scope
niggles resolved by explicit hand controls.
