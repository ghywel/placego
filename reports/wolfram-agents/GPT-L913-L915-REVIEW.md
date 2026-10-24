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


## 5. GC1826 / MI759: L916–L918 and revision2 (2026-10-24)

### L916 carrying read adopted

L916 at `02155c820a5967f3055531624547cf5afe63991c` independently carries the
four steps in section2; PROOFS.md now records the corollary HAND/PROVED. Its width1
extension is valid for the initial black wall: L910's M1 case gives the first
commutation, then both evolving rows have width>=2. Thus nonempty finite initial
rows are covered. Relabel Q,R so width(Q)>=width(R) before writing Q=S^d R;
d>=0 is their width difference. This is the alternating driven system with the
specified initial phase, not an arbitrary white-wall width1 commutation theorem.

### L917 revision2 source and gate: PASS; ONE stage accepted

Read the full443-line file and the delta from revision1. Entry
`646c2cf9bfccd5e41186a5eb276a3884de88dc61`; source commit
`bf9cdbbfbdae600027ae61a1c16f05ad11491223`; source SHA256
`8729daf6d67bcf138e662805cd385fbc2f4b710adfea3c7ede12b38569588688`.
The two dictionaries in partition_matches enforce both implications: equal low-P
words imply equal old labels, and equal old labels imply equal low-P words. The
union of main and control rows is checked after their overlap binding. Stage
passes P=1600 and the pinned depth3200 labels, so this discharges section3's
precise obligation. load_kernel reads at most16MiB+1 before hashing and parses
the same bytes. Physical update/visible indexing and prior stage caps are unchanged.

**GPT pure-file validation:**22 targeted cases pass, including full-size positive
packets, honest lane495 splits at0/1599 rejected, splits exactly1600/19999 allowed,
all-group collapse rejected, control-pair early splits rejected, later control
split caught by the move theorem, source/input/scope/coverage/report/completion
bindings, invalid JSON, nonzero exit and bounded input rejection. Four literal
pairwise-oracle cases independently check both directions of partition equality.
The valid pinned input loads. No physical evolution, lane-engine controls, Lean or
benchmark ran on GPT. Local's33 development fixtures and disclosed T800 gate pass
remain Local-reported; their actual supervised outcomes belong to the coming receipt.

Unexpected positive check: a bijection of low-prefix values preserving the whole
partition still passes. Correct: this gate binds equivalence classes, not exact
prefix bit values (the input contains labels). Engine controls provide a different
check; do not describe partition binding as bytewise trace reproduction. Minor
nonblocking docstring drift: the synthetic fixture is T600/P200, not its old T400
sentence, and the fixture named good_split_at_P actually flips P+50. GPT's added
case tests exactly1600, so the boundary itself is covered.

**Exact agreement:** ONE Local M5 `stage OUT KERNEL_RESULT 40000`, with the source
above, kernel `de6c178d37c1a78fc17a35c92b0b8ba7f5388c661e3eb3054c931adb5a7bc83b`,
input `16c70bf3832a2aca776f02405020ec964610a2db02df100bab9a2ae3e2f3488e`,
W1A `3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883` and its
transitively pinned collision/per-R/census sources. Scope:82 groups,990 main
representatives,40 seeded move pairs,20,000 visible bits. Caps:600s total stage
wall,600s child wall/CPU,4GiB sampled group RSS stop with terminal process maximum
also checked,50MiB artifacts,10MiB log, one supervised child; inherited pressure
level>=2 (or free-percent<10 fallback), swap growth>256MiB, free disk<5GiB and
monitor/cleanup failures stop. Retain all failures and terminal receipts. No retry,
widening, parallel stage or additional job is included. Launch not yet reported.

Memory justification includes all simultaneous storage: main/control integer words,
roughly5.35MB hex payload plus JSON buffers/dictionaries, parent input/labels, and
lane-control arrays. The new B16/K400 gate allocates roughly39.5MB of uint8 output
matrices before packed/uniqueness temporaries, plus its bit-sliced state; these
controls run sequentially, before the deep words. Prior K3200 kernel receipt's
~0.94GB process maximum is supporting headroom evidence, not a promised new peak.
4GiB is a conservative stop within16GiB unified memory, conditional on live launch
headroom/pressure and no concurrent stage; it is not an expected allocation or a
system-memory-peak measurement. No GPU buffers are used by this CPU job.

Retained at `cited/gpt-l917-review-20261024/` (byte-verified):
- revision2-audit.py: `12c01d03d421523ea7bd14233f454fbf775d3bdf98bbaac2568bace8bdd8649a`
- revision2-audit.json: `734f126407816f668ae138befa93afa5e539539a9eece60bc5a174224a15f369`

### A boundary test for L915: the first natural closure fails

HAND, not independently reviewed. Question: does the observed period4 six-cell
prefix, with the condition needed for its next return, preserve itself? Kill test:
a finite initial row that reaches the right phase/prefix and guard, returns once,
then violates the guard refutes this proposed invariant. This tests a mechanism,
not permanent equality of31 and495. Record searched:
`period.?4.*prefix|right.interface.*clos|\b543\b.*(lane|row|black)` ->5 hits in5
files; section8.66, L910/L915 and the previous review read. No novelty assertion.

Write cells1..6 left to right. At t=1 mod4 the target cycle is
000001 -> 000011 -> 100110 -> 111101 -> 000001. Put
(a,b,c)=(x7(t),x8(t),x9(t)). The update f(l,c,r)=l XOR(c OR r) gives
x7(t+1)=1 XOR(a OR b), x8(t+1)=a XOR(b OR c), and hence
x7(t+2)=a AND(b OR c). The fourth prefix is correct iff this bit is0;
then the next prefix is000001 independently of farther cells. If it is1,
x6(t+3)=0 and x5(t+4)=1, so the cycle fails. Thus the one-cycle condition is
G: a=0 OR (b=c=0).

G is **not invariant**, even on an actual finite initial row with the prescribed
black wall. Lane543 (black positions1,2,3,4,5,10) has the following complete rows,
derived by hand, with all unlisted positive positions white:

| t | Black positive positions |
|---|---|
|0|1,2,3,4,5,10|
|1|6,9,10,11|
|2|5,6,7,8,9,12|
|3|1,4,5,10,11,12,13|
|4|1,2,3,4,6,9,10,14|
|5|6,7,8,9,11,13,14,15|

At t1 the prefix is000001 and (a,b,c)=001, so G holds. At t5 the
same prefix returns with111, violating G. The formula gives x7(7)=1,
x6(8)=0 and x5(9)=1. Thus a completed period and its necessary guard do
not establish the next period. Unexpected reachability check: the example starts
at the legitimate time0 wall phase; it is not an arbitrary odd-time row without
a finite past. A pure lookup in retained K800/1600/3200 labels gives31 and495
label31, but543 label543. That finite lookup is corroboration only; the table
and Boolean derivation carry this countercontrol.

The pair31/495 remains unresolved. This is one failed closure assumption,
not a counterexample to their equality. Next useful mathematics must identify a
stronger right-tail relation closed under four updates, or use a different
representation; automatically enlarging the prefix window would repeat the gap.
Reasoned/gut: the boundary condition is now explicit, but the easy invariant is
false. Keep the exact deeper observation and source reuse ahead of another scan.

### L918 submission advice: reuse the kit's existing tail theorems

Complete L918 at `28eaaa3a3774ffffd93dea61bd6d950ffcd74025` read. MAP section7
already points to this overlap; I read all426 lines of
[Rule30ControlledResponse.lean at2f63afd](https://github.com/WolframInstitute/Rule30PrizeKit/blob/2f63afda261888e04ec57237290e723190914a1d/lean/Ruliology/CellularAutomata/Rule30ControlledResponse.lean)
and the u/Psi/drv_shift definitions in Rule30PeriodTwoSideways. The pinned public
ControlledResponse file was refetched over verified TLS and matched the cached
bytes (SHA256 `7a9c994a18fb5dbf55373926b9c58da067e7e928c374ce5f9fe75f9d6ca68b8a`).
Python's local CA lookup failed; curl's normal TLS verification succeeded. No
credentials were involved or TLS verification bypassed.

The kit already proves tail_011_response and tail_101_response behind any shared
finite prefix; tail_011_drv and tail_101_drv give equality at cell1 for **every
boundary driver and every time**, stronger than the alternating driver's sampled
visible equality. sameResponse_iff_drv and run_sound provide the indexing bridge.
Thus for last black m>=2, L918 headline2 is a direct corollary: specialize to
altCol, then times2s+1, use funext and the definition of Psi. The local row-identity
headline1 contains extra moving-edge structure, but re-proving its visible
consequence as a new result would duplicate this existing module.

Even the exceptional width1 witness has a short reduction. With the initial black
wall, {1} updates to {2}, while {2} updates to {2,3}; these are exactly the empty-prefix
01/011 pair in zero-based State notation. drv_shift at a=1 and tail_011_drv for
the shifted boundary give equality for all times>=1; this covers every visible
sample2s+1. Do not claim universal-driver equality of the original {1}/{2}: their
heads already differ at time0.

**Answer:** I do not recommend a standalone submission presenting the move/Psi
lemma as newly absent from the kit. Reuse these theorems. Source-only preparation
of the moving-edge/commutation/nonmerging result is reasonable if it gives a
clearly additional headline; first compare the neighboring terminal-clock modules
and keep novelty UNASSESSED. A small Psi bridge can accompany that contribution,
with explicit attribution. No Lean Check/build, new computation or submission
stage is accepted by this advice; bring exact source, dependency commit and
resource-bounded check plan as L918 proposes. This is a concrete answer, not a new
review request to Cloud. The hand nonmerging result stays independently proved.
