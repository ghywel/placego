# Rotation and short-tail reduction: exact carrying scope

GPT, GC1859/MI792, 2026-10-25. **Scoped source/hand PASS.** No Lean,
decomposition replay, Rule30 transition, certificate evaluation or experiment.
These are known kit arguments, not new project proofs.

## Sources read and boundary of the verdict

At pin **3eca23c0a9fa6b153313655e6d51835406c2d06e**, read all statements and
bodies in five sources,568 lines total:

| Module | Lines | SHA-256 |
|---|---|---|
| Rule30WordRotation | 81 | f5df1071ac92e1233bb0a6338834dfa1bc698fa4cad5c41989edbe8cd77e7597 |
| Rule30ShortTail | 223 | 204c381e81ed35cd4219aaa34f247cab97ddaa5f9ea0518a0946f184b9b85974 |
| Rule30FiveTailReduction | 96 | e665ba6b5802c023314bdbf58f07bb7ce5e0a0a1dd1de6131c5c298f478ea732 |
| Rule30SixTailReduction | 108 | 859aadd1ff92c8782038bf464be6f759eec63c5cb48e9871baea2930d1b7dbb5 |
| Rule30FiveTail | 60 | fabfb3713c980c1ea6084eb6f927bf18baf1bc822f6f369cf57c04b5ae4dec6c |

Sources are in the
[pinned official directory](https://github.com/WolframInstitute/Rule30PrizeKit/tree/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata).
Eight payloads fixed/readback verified at
`cited/gpt-tail-rotation-review-20261025/`: the five sources, audit script/JSON
and record search. Audit SHA256
`3616f66edfb89f75879d8335b6d070711b421588f72c18197bc02e0bf3c2b39a`.
File-only checks cover literal core lengths, black endpoints, counts and
uniqueness; they do not rerun the finite decomposition checks.

**Verdict boundary:** rotation and the length<=4 short-tail carrying chain are
read through the certificate interfaces already reviewed in GC1857. The five-
and six-tail REDUCTION arguments carry in their stated conditional/imported
scope. Reading FiveTail's60-line wrapper does not independently review its
new core certificates: FiveTailTube, VacuumExample and WhitePadding10101 are
outside this packet. No independent carrying acceptance of the complete
five/six-core certificate closure is claimed. SixTail itself was not read.

Record searched: `FiveTailReduction SixTailReduction` -> no hit including
ledgers. Current public catalogue04:59:21Z unchanged38 entries. Existing
uniform strip soundness, no-eventually-constant theorem and GC1857 certificate
premises retain their prior scope. No startup execution/pass asserted.

## Rotation preserves the word, not just its black core

If a column eventually repeats u++v, with positive total length, then it
eventually repeats v++u. `eventuallyWord_swap` chooses new starting time
T+|u| and checks the two index cases modulo |u|+|v|. Either block may be
empty; only the total word must be nonempty. No transient bound is assumed.

For a tail `0^a v 0^b`, the full word is

    0^r 0^a v 0^b  ->  0^b 0^r 0^a v  =  0^(b+r+a) v.

Thus the period length stays r+|tail|, while the padding can only increase.
It is not valid to discard white ends and keep r unchanged.

Hand endpoint control: u=01100,r=69 has a=1,b=2,v=11. The normalized period
is `0^72 11`, length74, exactly the original69+5. Keeping r69 after trimming
would instead yield length71 and would not be a rotation argument. This
cheap check distinguishes the actual reduction from the tempting deletion.

## Complete short-tail chain through the read certificates

The eight black-ended cores of length<=4 are

    1, 11, 101, 111, 1001, 1011, 1101, 1111.

They have counts1,1,2,4 at lengths1,2,3,4. The source's finite decomposition
covers all31 binary words of lengths0..4, separating the all-white case from
white ends plus one core. The checked declaration and its list-to-proposition
proof were read, not independently kernel-replayed.

`short_core_certificate` dispatches these eight cases to widths
8,6,9,14,8,6,7,10. The cheap F..I wrappers are explicit padding_strip proofs;
the other cases use the read uniform D/B/E interfaces and Heavy111's explicit
certificate. A common r>=49 dominates all the sufficient thresholds read in
GC1857. `certificate111` discharges the last initially abstract input by
Heavy111.strip_certificate; it is not left as an assumption in the final
`no_short_tail_leftFinite` theorem.

The all-white tail, including empty u, gives an eventually white column and
is ruled out separately by the known uniform no-constant-column theorem.
Otherwise rotation supplies padding b+r+a>=49 and one certified core.
Uniform strip soundness then excludes eventual repetition in EVERY column
of EVERY configuration with a leftmost black cell, allowing an infinite
right tail. The single-seed/finite-start corollaries are narrower instances.

This supplies actual formal extra uniform wrappers which GC1857 did not
claim to have read; it does not retrospectively change GC1857's read scope.

The periodic-column form also carries: for ANY positive period P after T,
a white run of length r>=49 beginning at a>=T, with r<=P and P-r<=4,
is impossible. The proof records the remaining P-r observed phases as u,
uses periodic_mul and Euclidean division to rebuild the whole eventual word,
then applies the tail theorem. P need not be a least period. “At most four
remaining phases” counts all positions, not merely black phases.

## What the five/six reduction statements add

FiveTailReduction has all eight black-ended length5 words (2^3 interior
choices); its finite decomposition covers lengths0..5. Given exclusions
for these eight cores at every r>=69, the proof handles shorter cores via
the length<=4 theorem and concludes all tails of length<=5 at r>=69.

SixTailReduction analogously lists all sixteen black-ended length6 words
(2^4 interior choices). Given their exclusions for every r>=77, it reduces
all tails of length<=6 at r>=77: the other cores use the IMPORTED FiveTail
theorem at69. In both arguments b+r+a>=r preserves the required threshold.
The bounds49/69/77 are sufficient bounds, not sharpness claims.

The imported FiveTail wrapper explicitly dispatches its eight cores to
FiveTailTube's vacuum exclusions, VacuumExample and WhitePadding10101, then
feeds the reduction. Those new core proofs were not carrying-read here;
neither the finite decomposition nor the reduction itself supplies them.
The dependency order is rotation -> short<=4 -> five reduction/closure ->
six reduction. No circular carrying step found within the read reduction
arguments; the unreviewed core certificates remain an explicit scope limit.

## Current-work consequence

These are eventual periodic-word exclusions with a bounded SHORT tail and a
long white prefix. They do not assert certificate existence for arbitrary
tail length, finite matching-trace deadlines, or CQ01/all-widthD(W) bounds.
For example the alternating01 representation has r1, below all three bounds.

Reasoned/gut: the normalization, short-tail composition and conditional
reductions carry; trimming without adding the white ends would not. Selected
review COMPLETE in this exact scope; complete new-core adoption was not the
claim under review. No new proof status, job, Local wake, held-lane reopening
or schedule change. Broader conservation remains parked/local-template
incubation unchanged.
<!-- Dated follow-up; the original review below retains its historical scope. -->
**2026-10-25, GC1860:** [the actual five-tail core review](GPT-FIVE-CORE-REVIEW.md)
now closes the five-tail source gap left here, carrying length<=5/r>=69.
The six-tail new-core closure remains unreviewed. No independent kernel replay.

