# L913 outcome, L914 source and L915 mechanism review

GPT, 2026-10-24, GC1825 / MI758.

**L913's accepted kernel stage: retained-evidence PASS, permission consumed. L914 revision1:
source review complete, binding repair required before launch. L915: source and retained
aggregate read; finite observation only.** No dynamics, physical controls, GPU or Lean ran here.

## 1. Kernel result and terminal evidence

Complete L913 at61dc85da71416aaef70003ee76667d954dc2e816 read. All six original files in
`cited/cq01-kernel-20261024-2224/` were downloaded and SHA/size verified. Accepted source
`a541847fcf3b91f586d0ae0d91ef1ae8666eee3459a6cb7591e493dd11426549` matches result and
supervisor receipt. Current source `de6c178d37c1a78fc17a35c92b0b8ba7f5388c661e3eb3054c931adb5a7bc83b`
has identical executable AST; only the OUTCOME docstring changed. Frozen dependency bindings
and scope16/800/1600/3200 match GC1824.

Independently read all196,608 labels, recomputed canonical representatives, restricted counts,
nesting, move refinement and all82 merged groups. The move partition was reconstructed by
**inverse endpoint reduction**, independently of the producer's forward union-find: leading three binary digits110 has predecessor obtained by dropping its highest bit;101 has predecessor
obtained by dropping its highest bit and restoring the next bit; lane2 has predecessor1.
Other nonzero lanes have no predecessor. Descending these unique predecessors gives32,769 roots.
The whole depth800 partition equals L910's retained partition after canonicalization, digest
`35b013a093fb5f4c065a23c904bbd0291714f61f08d37d374b82c71733bb79ed`.

| Psi depth | Classes | Extra merges beyond moves |
|---:|---:|---:|
|800|31,478|1,291|
|1,600|31,820|949|
|3,200|31,861|908|

The82 groups contain **990 distinct canonical move representatives**, so comparing each with
its group's first needs908 comparisons. Largest group118; every member has cells1..4 black.
All groups and sizes match, including29 pairs and13 triples. Every representative has width>=5.
These are finite prefix partitions: depth3200 means1600 visible bits, odd times1..3199.
The decreases1291→949→908 suggest slowing, but do not establish a limiting plateau or a
second infinite-kernel mechanism. The two failed predictions remain failures.

The retained controls show the three base checks passing, all three mutants caught, and all34
file gates passing. This is an evidence review, not an independent physical replay. Receipt/log
agree: stage14.2s, supervised child12.48s, time-l real11.74s, CPU11.70s; lane pass7.57s and
assembly1.57s are components, not end-to-end costs. Sampled group RSS906,674,176 bytes and
process maximum941,834,240 bytes are different measurements, neither a system-memory peak.
Pressure stayed level1, free81→80%, swap0; terminal group members0, final problems empty,
artifacts1,291,141 bytes. Preflight and one child completed within the agreed caps. No retry.

## 2. What the delayed-move check establishes, and why it can be replaced by algebra

Read all of `eventual-move.py`, its85-byte summary and all82 detail records. The code checks
**one direct move in either direction or exact row equality**, only the first two representatives
of each group, at times1..600. It reports no certificate, with visible equality throughout.
It does not test transitive move equivalence. The reported511/511 positive control has no
invocation/output in this retained six-file packet; it remains Local-reported. No rerun is requested.

Already,36 of the82 selected pairs have width gap>1, so they cannot ever be direct neighbors:
each nonempty row's rightmost black advances exactly one cell at every step. Another23 have
width gap0: a direct move requires gap1, and unequal finite rows never become equal. Only23
pairs even have the direct-move width gap. For31 versus495 the gap is4 forever. Thus the
negative direct-move count is not additional evidence for a new mechanism.

There is a stronger **HAND corollary for Local's check**, using existing ingredients, not a
new census or a claim of novelty. Restrict to nonempty finite right halves of width>=2.
Let S be the unique forward right-end move and F_b the driven update with boundary bit b.
Then:

1. **F_b is injective on finite right halves.** At the largest differing real site j, the two
   rows agree at j+1,j+2, so their next values at j+1 differ by left permutivity. This is the
   record's standard rightmost-disagreement argument (PROOFS G121 and proposition21), valid
   for either boundary bit because j+1>=2.
2. **F_b S = S F_b.** L910's two local endpoint transitions prove exactly this identity, not
   just equality of visible words: type(a) becomes type(b), and type(b) becomes type(a).
   At width>=2 neither move consults the wall. The equal update at site M-1 also works for
   M=2 because both copies have the same clamped bit at0. The rightmost black advances by1.
3. **Move components are paths.** Each vertex has one successor of width+1 and at most one
   predecessor (the distinct110/101 inverse cases above; the width2 boundary is separate).
   Therefore two equivalent rows of widths m<=n satisfy Q=S^(n-m)R. Leaving a finite width
   cutoff cannot connect previously separate paths: there is no branching back toward them.
4. Write U_t for the composition of the t driven updates. Width difference d stays fixed,
   U_t is injective, and U_t S^d=S^d U_t. If the evolved rows become move-equivalent,
   U_t Q=S^d U_t R=U_t S^d R; injectivity gives Q=S^d R already at time0.

**Consequently initially distinct move classes in L913's domain cannot become move-equivalent
later**, even by a chain of moves. This closes the delayed-move explanation by the displayed
hand implication, subject to Local's independent read; it does not prove permanent visible
equality. For the smallest pair the four forward moves are literally
31→47→111→175→431, not495. This is an endpoint-rewrite check, not time evolution.

Unexpected boundary check: exclude the empty row and width1 from the commutation statement
as written. At width1 the move depends on the boundary phase; no such exception occurs in
these990 representatives or their forward S/evolution orbits. Negative test before adopting
the implication: could two distinct finite rows coalesce, or could equal-width vertices join
through larger widths? The rightmost-disagreement and unique-predecessor arguments exclude
both. No finite trace is used to prove an infinite assertion.

## 3. L914 executable review: exact earlier-partition binding is missing

Complete L914 and all387 lines of `cq01_deeptime.py` revision1 read, SHA256
`de67bc27b4a655c4ffee95363c6bfe133b6299fe733c9f4be653e6104a953863`.
The integer update correctly represents cell x at bit x, inserts the common wall before an
update, clears bit0 afterward, and reads cell1 after updates to odd time. No right boundary
truncates the growing row. First-difference indexing and retained-word reconstruction are
consistent. Seeded move-pair words are retained and compared; overlap with main rows is bound.
The byte-bounded matcher fails closed, and W1A retains the stage/CPU/memory/output/cleanup stops.

All28 committed file fixtures pass on handmade word packets, without `assemble`, `controls`
or `visible_word`. **But five actual-T40000 file cases expose a missing binding.** Starting
with synthetic words whose first1600-bit partition matches the input, flip lane495 at visible
index0 or1599 and recompute every report/summary honestly. Both packets pass the actual matcher,
although31 and495 must agree throughout indices0..1599 by the pinned kernel input. A packet
collapsing every old group to the same word also passes. The unchanged positive and a split
at index1600 pass; those two should continue to pass.

**Required repair:** at stage scope, recover the partition induced by the low1600 bits of every
retained main word and require exact equality with the pinned kernel partition restricted to
those rows. Within-group equality and between-group distinction are both needed. Prefer the
same check over the union of main rows and the40 move-pair control rows, whose kernel labels
are also present. This uses retained labels and words only; no extra dynamics is needed.
Keep the three rejected fixtures above, plus the positive split at1600. A mismatch is a failed
cross-engine binding, never a newly discovered early split. The smaller synthetic T400 fixture
is outside this production-prefix obligation and should be explicitly treated as such.

Also bound the **input** read before hashing: the actual pinned file is1,287,864 bytes, while
`load_groups` currently reads arbitrary-size input unboundedly before supervision. A fixed
16MiB bound is ample here; reuse one byte buffer for digest and parsing. Fix the size estimate:
20,000 bits take5,000 hex characters, not2,500. At most990+80 rows need5,350,000 hex characters,
plus keys/reports/JSON overhead. It still fits the16MiB result bound and50MiB artifact budget.
Integer row storage grows with T; the work is O(T) **big-integer operations** per row, with
roughly quadratic bit work, not O(T) bit work. The revised80s estimate is explicitly a scaling
estimate from Local's disclosed probe, not an independently verified timing.

I support this narrowed representative-only measurement after the binding/read-bound repair;
T40000 is the submitted scope (20,000 visible bits), larger than L913's informal20000-step
suggestion. **No launch acceptance for revision1.** Freeze the repaired source and keep600s
stage/step wall and CPU,4GiB sampled group RSS stop,50MiB artifacts,10MiB log,one child, pressure,
headroom,swap,disk and terminal cleanup checks; no retry or further depth widening. Account for the lane-engine controls, retained integer words, hex strings and simultaneous JSON
read/write buffers as well as the few-kilobyte current row; the single-row size is not the stage peak.

## 4. L915's trace and the next mathematical obligation

Complete L915 at a2e744ac260bd4c4d9a12cfef3942682577ad635 read, plus full pair-trace.py,
its218-byte output and RULE30-PRIZE section8.66. Source
`adff0b1ef5d362b5245c066b2ffd2af4142234eb31664130ece1a18e13387f93`, output
`730ae0ac87e70feef047f29c63fc604191794e3dac35422aee4e9a28e8cd68ef`, in L913's store directory.
The retained object is an aggregate, not all raw rows. It reports period4 on cells1..5 with
cycle00000,00001,10011,11110 from t1, cell6 black at even t>=2, and damage fronts7/9 even,
8/10 odd. The program samples t=0..3199; the last computed row at3200 is not included in its
summary. It is an outside-stage Local computation, not covered by GC1824's supervisor receipt.

The local masking identity is correct. If j>=2 is the leftmost differing site and a_(j-1)
is common, then the next difference at j-1 is (1-a_(j-1)) times the old difference at j.
A common black masks propagation left **for that step**. L915 correctly identifies the missing
recurring boundary condition at cell7; the finite period does not close its own right boundary.
Section8.66's white-diagonal lock is in k=x+t coordinates: a fixed diagonal moves left in
physical coordinates. The new proposed barrier is near a fixed physical cell. The local OR
masking is shared, but a coordinate/invariant argument is needed before identifying them as
the same permanent lock. The old probabilistic phase counts are measurements, too.

Next mathematical task: find a forward-closed relation carrying the period4 prefix together
with its necessary right-interface condition, or refute that closure. Do not merely assume
cell6's recurring blackness from the observed prefix. The hand no-delayed-move implication
above removes one dead explanation while leaving this actual boundary obligation open.

**Record searched:** `delayed.move|move.related|move.*commut|rightmost.*differ` ->53 hits in25
files; G121/proposition21, L910 and section8.66 read. No novelty claim or outside literature
claim is being made. **Niggle sweep:** transitive versus direct moves, phase/width1, finite
versus infinite evidence, diagonal versus physical coordinates, and prefix binding all checked
as above. Reasoned verdict: finite outcome sound; deeper runner needs one binding repair;
permanent equality open. Gut: the small pair is worth a boundary-invariant argument, while
another delayed-move search would spend effort on an algebraically excluded possibility.

Audit files and results are retained at `cited/gpt-l913-l915-review-20261024/`:

- audit.py: f85b6cf5d5ed9e11723cc6ea1a36aeeae694520eb102541edf5a8a851fedf31b
- audit.json: 58e3f65b7a2118dd92800904f9fd591ac85b2491cdd52a94cf7877e5622a8f5b
- deeptime-audit.py: 06243d72009458ea69ecdae3407c8179334d8325490edd493ea9142da982d603
- deeptime-audit.json: 086c9d23e2e6df4edacc0ac79ed8dcf6365f6e17c809ca778fea84f3d915d79e
