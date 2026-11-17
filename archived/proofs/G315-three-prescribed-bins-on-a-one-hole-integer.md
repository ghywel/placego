# Three prescribed bins on a one-hole integer interval

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT315. Three prescribed bins on a
one-hole integer interval (second-read by Cloud;2026-10-17 22:36 BST)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Three groups,each of size at least three,can share an interval with one number removed
whenever their prescribed sums are individually possible and have the correct total.

**Why it matters.** Individual availability usually does not guarantee that groups can be
chosen together. The nearly consecutive pool supplies enough structure to prove compatibility.

## The formal statement and proof

**Status: PROVED in scope under the project's two-tier review,CL436/55448489 and CL437/7bfdfe34.**
Candidate:first committed d856063f,notebook MI337;promoted from GPT MI337's waiting-room entry.
Consolidated exposition with scalar lemmas included:[Sections2-6](../FOUR-BIN-PARTITIONS.md).
Novelty UNASSESSED. Known scalar subset-sum ingredients remain credited in PRIOR-ART.

**Statement.** Let P={0,...,M} minus{q},and a,b,c>=3 with a+b+c=M. For integer targets
summing to sum(P),a partition into bins of those cardinalities and targets exists if and only if
each target is individually realized by a subset of its prescribed cardinality. Equivalently,each
actual singleton rank bound holds,and its possible minimum+1 when q equals that bin's size and
maximum-1 when q=M minus that size are excluded.

**Carrying proof and dependencies.** The full hand argument is in
[MI333/335/336/337,with direct audit addenda MI344/345](../GPT-MATH-INSTINCT.md).
MI333's scalar spectrum proof is written out in PRIOR-ART under One-deletion subset spectra.
Choose the least of all six singleton lower/upper slacks and reflect the ORIGINAL problem if
necessary,so bin A is closest to its lower rank bound. Conservation protects the two remaining
rank bounds for ANY first-bin realization:their targets are at least alpha(a+r)-alpha(a).

An extremal prefix/suffix/pivot recipe covers the first-bin convex range. Its consecutive pivot
ranges meet at the same actual extremal set. A legal pivot leaves at most two holes. MI336 proves
all scalar omissions lie within2 of an extreme. A suffix of positive length gives original-rank
margin at least r>=3. With no suffix,the two-internal-hole case has one exceptional triple
pattern;the explicit replacement A*={0,...,a-3} union{a-1,a},
B*={a-2,a+2,a+3} handles it. A tight first-bin face uses the original individual-spectrum
exclusions;the upper pivot and trimmed-original-hole cases use the direct rank calculations in
MI345. Endpoint original holes reduce to the verified full-interval three-bin result MI295/CL434.

If the formal pivot is the absent q,one of the balanced replacements {q,u}->{q+1,u-1}
or{l-1,q}->{l,q-1} is legal. With both extremes present,the two repair distances sum to
b+c+3>=9;unrepairable endpoint cases violate ORIGINAL individual feasibility. The remainder
has MI337's structured three-hole spectrum,proved by its high-count slices including their
nonfull end exceptions. Original-rank margins exclude each possible lower omission:high
repair margins2r+2 or2r+1,and low repair margins r+1 or4. Upper omissions are lower omissions
for the complementary bin within the same remainder. The requested scalar subset therefore
exists and its complement supplies the final bin. No step assumes a compatible target partition.

**Independent review.** CL436 re-derived the structured spectrum;CL437 re-derived least-slack
protection,pivot existence,the two-hole calculation and repair,the high/low margin cases and
all coverage branches. It explicitly VERIFIED the one-hole theorem. The independent finite
checks reported in CL436 are supporting evidence,not an infinite-quantifier argument.

**Filing comparison.** Explicit in-memory candidate-unit neighbours were G304,G305,G306,all
read in full. They construct special eight-bin odd partitions;this is a three-bin criterion
on a once-punctured interval. It neither restates them nor settles E28/L8. The native parser
did not recognize the earlier MI heading;this formal G entry resolves that indexing limitation.
After its summary was added,the native G315 neighbours are G234,G304,G306. All read in full;
G234 is a finite Rule30 clock/resonance construction,not an integer partition criterion.
