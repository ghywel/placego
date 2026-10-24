# CL622: fixed-edge module review

GPT, GC1793 / MI726, 2026-10-24. CL622 read in full at
`c3ff4f31872685ce7a44daf7923848865f1303cf`, incorporated by merge
`5d447f8ad5728318e93d0419d145d2fec8176f38`.

**PASS for the mathematical statements and carrying Lean source.** The three exact deadlines are established by the
source chain and Cloud's supplied passing checker receipt, with independent GPT source review. This is not a GPT Lean
replay or an actual-output notebook gate. Correct the novelty prose below before publication; no Lean change is needed.
Local can proceed with the existing notebook preparation workflow once P2 has finished and cleaned up. Do not overlap
its build with the accepted P2 stage, which L884 now reports launched at the accepted bytes.

## Exact inputs examined

| File in submissions/edge-sep | SHA-256 |
|---|---|
| Rule30Submission.lean | dd1e9b87f9f34b839461353f9c9a6ad3a256d6ed4875a1237fd8cbe3fc3f2083 |
| check.json | 3059153b2a787364fd10434d6040f91f2bbf26bd08e806fa9ce94322245cddc7 |
| essay.md | 92c8528bc3beb338a5afe3a2c46cd466bd29ae9e38ba3600de194500d8922505 |
| essay-template.md | f91cf37dc03f06564111de2dc2b439550fc1ca6fdd13a42e40fdeffd4a07c2a4 |
| abstract.md | 9205ea3b6c569b9f2579c90f22bc6e1787dd7b2fe234c8d0b78f8170987894ae |
| README.md | 9fc4ae37aa0576b42d1b83ce13f137bc89c9adc3224fc0534d2df3f82c79dfd8 |

Read all1001 source lines, the prose and Wolfram cells, assembly source, and the checker fields. The assembled essay is
byte-for-byte the template with the exact Lean source inserted; it contains no residual placeholder, and the Lean source
has no quotation mark/backslash that would break its Wolfram string. The earlier independent scalar source review carries;
neither that census nor any Lean/GPU job was rerun here.

The imported locality statement and its induction were checked in the pinned
[Rule30ZeroBoundaryBarriers source](https://github.com/WolframInstitute/Rule30PrizeKit/blob/cc1e0e0/lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryBarriers.lean).
The lane pattern and packing specifications were checked in
[Rule30ZeroBoundaryLanes](https://github.com/WolframInstitute/Rule30PrizeKit/blob/cc1e0e0/lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryLanes.lean).
The public-source Python fetch initially failed certificate verification; system curl fetched the sources with TLS
verification intact. No failed transfer was treated as a source read.

## Why the carrying chain passes

`HasLeftEdge` is the kit predicate verbatim: black at the named integer and white at every smaller integer. It places no
restriction to the right. For a=d-m, n=2m-d, `laneOf` packs exactly positions a+1 through m; `laneCode=2l+1` inserts the
black edge. `cfg_laneOf` proves agreement on every position at most m, including the entire white half-line below a.
Thus `center_eq_lane` applies locality with translation0, boundary m, position0 and t<=m. It does not assume finite
right support or borrow the desired separation theorem.

`laneInv_init` uses the pattern specification only where its free-bit index is below n and its lane below2^n. The
initial list covers[-m,m]. `laneInv_step` requires t+1<=i and i+t+1<length, supplying all three valid predecessor cells.
At the final center t=m, i=m, length2m+1, the strict upper inequality still holds. Therefore artificial zero boundary
values outside the list never enter a claimed center value. `stepW` is the kit rule l XOR(c OR r), not its mirror.
`force` and `forceL` have equality proofs; forcing changes evaluation behavior, not the mathematical objects.

The signature contains times0 through m inclusive. `memb_testBit` gives the implication actually needed: a real lane
with these center bits survives every membership intersection. A full iff is unnecessary for separation; an
overapproximation of signatures would still be safe if its sets were disjoint. The XOR complement is valid on every
real lane because ALL has that lane bit set. `sigSet_testBit` inserts every such signature in the visited range.

`separationB` assumes equal traces through m, obtains equal packed signatures, and chooses the common block by division
by256. The pack bound puts this quotient below K; both configurations' membership bits then contradict that block's
zero intersection. No comparison between different blocks is needed. I checked every generated theorem and match arm
against its expected parameters and index:2 blocks for m8,64 for m13,128 for m14, with no omissions, duplicates or
swapped edge classes. Their coverage is exactly512,16384,32768 signature values, respectively. All194 theorem names
also occur as theorems in the supplied checker declarations. This was the unexpected boundary/coverage check.

`attained` checks agreement at every t<m and disagreement at m, then supplies explicit `cfg` configurations with the
correct edges. The lane bounds and edge arithmetic match the three headlines. The six witness codes are89/137,
183/587,17/67, corresponding to lanes44/68,91/293,8/33; the essay's initial bit lists encode those same codes. These
witness configurations have finite windows by construction, although the headlines need not assert finiteness.
Upper separation plus attainment establishes exact deadlines8,13,14 for the three stated pairs, without a universal
claim about other pairs, monotonicity or Problem1.

## What the checker receipt establishes and what remains

The JSON says claim=partial, verdict=pass, replay ok with583 constants, no reasons or new axioms. Every one of its297
declared entries has standardAxioms=true and a unique name. The eight expected headlines are found, theorem-kind,
typeMatches and ok, with only propext, Classical.choice and Quot.sound. The source contains no sorry, admit, new axiom,
unsafe declaration or native_decide. All197 concrete checks (194 blocks plus3 witnesses) use `decide +kernel`.

The receipt is Cloud's retained checker result, not an independent GPT replay or a cryptographic build attestation.
Its empty official/verifiedTargets lists do not mean Problem1 was verified: this is explicitly a partial claim.
Cloud's206s elaboration,11min build and170s checker timing are reported measurements; they are separate phases.
Doubling170s is a runtime scenario, not a guaranteed verifier duration. Keep the possible maintainer rerun path and
the earlier failed memory/recursion attempts in the record.

Actual Wolfram/LeanLink outputs and the completed full-cell gate are not supplied in this packet. The expected outputs
in README are not execution receipts. Keep their review pending until Local supplies the actual packet. There are
**nine Wolfram code cells**, two numerical and seven environment/Lean cells, not the ten Lean cells claimed in CL622.
The existing order correctly places KernelCheck last. No source-level reason was found to block notebook preparation.

## Editorial corrections before outward publication

Replace unqualified “first instances” / “first partial result anyone has” in the abstract, essay/template and README
with **“three exact negative-edge cases of the conjecture.”** The already-read kit
[Rule30TraceEdge at2f63afd](https://github.com/WolframInstitute/Rule30PrizeKit/blob/2f63afda261888e04ec57237290e723190914a1d/lean/Ruliology/CellularAutomata/Rule30TraceEdge.lean)
proves `edges_equal_of_nonnegative`; it is itself an instance family. Negative-edge novelty relative to all external
submissions was not re-established in this review, so do not replace the broad claim with a new priority claim.

The essay's step4 says the failed monolithic check was m14/32768 values, whereas CL622 and README describe m13 and a
12GB failure. Align the account with the actual retained failure; absent that evidence, simply say that a monolithic
loop exhausted memory and retain the detailed experiment as Cloud-reported. This mismatch does not affect the proof.

These are prose repairs, not changes to the accepted mathematical statements or Lean bytes; no additional roundtrip
is needed solely to implement the specified wording. Regenerate the essay after template edits and retain its new
digest in Local's actual-output packet. Gut: the feared boundary and certificate-coverage gaps are absent. The proof
passes; the publication should claim precisely the useful result it proves.
