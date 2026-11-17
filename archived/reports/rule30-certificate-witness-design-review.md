# L987 certificate-witness design: amend before launch

GPT, 26 October 2026, GC1925. The owner asked GPT to wait for Local's active
block. Waited; then fetched/merged its completed L987, including the timing
correction, before reading the new source. No compilation or execution by GPT.

Source read in full: `tests/probes/wolfram/certificate_witness.c` at
`5b1f6922650d55d955eb377463941af0a2e4c4e6`, SHA256
`988f9c41d740cff78889ca17e0a321c05e9543701f09c55619fc92db97fcd583`.

**Verdict: the exact minimum-certificate question remains useful, but the
proposed stage is not accepted as written. Its read policy always reads W
starting cells, and H3 is already false by hand.** This is a property of this
specific implementation, not an impossibility theorem for adaptive observers.

## 1. The read policy's unavoidable work

For every positive depth d and t>0, nonmutant `ev(t,d)` unconditionally evaluates
both `ev(t-1,d+1)` and `ev(t-1,d)`. Only `ev(t-1,d-1)` can be skipped. Starting
with an empty memo, the union of these compulsory dependencies contains every
leaf `ev(0,j)` for d<=j<=d+t: choose j-d deeper steps and the rest same-depth
steps. All those paths stay at positive depth. Memoization changes the number
of visits, not whether a necessary leaf has already been evaluated somewhere.

Thus the call `ev(W+1,1)` necessarily reaches every initial depth1..W. At each
such leaf the actual code sets its readmask bit regardless of the cell's colour.
No bit outside1..W is counted. Therefore **reads(F)=W for every F**, under both
the original policy and its XOR mutant. C4 is not a discriminatory negative
control for observation savings; the original has none either. Returning known
zero only at t=0 for d>W does not prune this compulsory dependency triangle.

In words: the route which is always taken has already visited every house.
Skipping part of another route cannot reduce the number of houses visited.

## 2. H3 is false throughout its declared comparison

The familiar triangular trace map supplies a universal upper bound on minimum
START certificates for these populations. For a zero-wall finite row F,

    x(t,1) = F_(t+1) XOR G_t(F_1,...,F_t).

This follows by induction using the deeper XOR input: its cone alone reaches
the new deepest cell. It is the same permutivity used in reconstruction, not a
new result. In the prescribed lane family, every even trace entry through W−2
equals1. Consequently F_1 is fixed, and each subsequent odd-depth cell
F_3,F_5,...,F_(W−1) is determined by the preceding cells. Knowing all W/2
**even-depth initial cells** determines the entire row successively.

Those W/2 cells therefore certify every lane's target in ALL, and also in its
PASS subset. Hence `START mincert(F) <= W/2`. Together with section1, for every
W>4:

    reads(F)=W > W/2+2 >= START mincert(F)+2.

So H3's fraction is exactly zero at W16,18,20, without running any of the census.
Neither a different boundary phase nor averaging over PASS repairs this policy.
This is a short hand argument awaiting Local's carrying check.

## 3. What carries in the exact group method

For each S, the counts describe precisely the population's classes under
`key & S`. The matching class is pure iff its opposite-outcome count is zero.
Gosper order enumerates all masks of a given cardinality, and cardinalities are
visited in increasing order. Assigning an unresolved lane at its first pure
class therefore gives its minimum certificate size. Once every lane is
assigned, later masks cannot improve any answer, so early exit is sound.
DIARY and START full keys distinguish all lanes; an empty population needs an
explicit EMPTY case before division/indexing, not an implicit assumption.

The nbit bounds in this exact revision keep shifts and direct indices within
range: START<=20, DIARY<=14, tables have2^21 entries. The global epoch cannot
overflow a signed32-bit integer within the frozen subset counts. Physical
evolution through the final update reaches depth<=58 at W28, below the64-bit
storage limit; memo dimensions likewise cover the target cone.

The first chosen minimum mask uses the declared Gosper tie order. PU is therefore
a statistic about that choice, not an intrinsic theorem that all smallest
witnesses live at the far edge. ALL and PASS minima are population-relative;
the cost of learning PASS membership is not included, which must stay explicit.
An offline smallest mask is not the cost of discovering it using observed bits.

## 4. Requested amendments and evidence contract

1. Keep the coordinate-wise minimum comparison if desired. Remove H3 as an
   unanswered prediction for this policy; record its hand refutation. A replacement
   policy needs a fixed, nonanticipating read rule and at least one explicit
   fixture showing its intended observation savings before a wider stage.
   Alternatively run only the minimum-certificate study first. No second policy
   or larger run is automatically authorized by this review.
2. Rename H2 as the **finite W28/W14 median-ratio prediction**. The threshold1.5
   is testable, but neither meeting it nor failing it proves or disproves
   asymptotically sublinear growth. Keep its declared thresholds unchanged if
   this finite diagnostic is retained.
3. `CHECK` currently increments `fails` and continues the remaining census.
   This contradicts the declared stop-on-control-failure rule. Fail immediately
   with nonzero exit and retained diagnostic, or explicitly stop at a small
   bounded control-phase boundary before larger work. Check allocations and
   handle EMPTY populations before using their arrays or averages.
4. Preserve per-lane certificate sizes and chosen masks (with W, population,
   lane ID and target), and enough source/population binding to replay them.
   Current stdout retains only aggregate histograms, means and positional counts.
   Those cannot support examination of which particular observations certify
   a case. State the revised byte budget; the current16MiB/file and64MiB/directory
   envelope provides room for a bounded tabular artifact, subject to calculation.
   C2 is an independent small-width oracle, not a large-width external proof
   artifact. Distinguish source-reviewed exhaustive computation from SAT/ILP
   optimality certification, which this revision no longer performs.

Three table arrays occupy24MiB; lane arrays, policy memo and histograms are small
relative to the proposed1GiB cap. That supports the allocation envelope, not
the stated seconds-to-a-minute runtime estimate. Retain the explicit wall/CPU,
pressure, disk and concurrency bounds; include build provenance and actual
source/binary hashes. The prior startup merge cap is not a reason to rerun it.
No M5 launch accepted until the revised exact source and invocation are read.

## 5. L986's boundary clarification

MAP section2(i)'s displayed algebra is correct: when the imposed wall is black,
the survival condition makes the adjacent cell black too, so its OR with the
wall equals its OR with zero; when the wall is white the updates already agree.
With phases matched, the constrained histories coincide. This is the existing
Q01 equivalence, not a newly different alternating-wall problem. It does not
turn arbitrary merging pairs into eternal survivors. The named kit formal
source was not reopened here, so this is an algebra/scope read of the cited
correspondence, not a fresh audit of the whole formal equivalence.

Reasoned/gut verdict: warm on offline certificate geometry; the proposed
short-circuit read-saving mechanism is cold for a precise, already decidable
reason. Local owns the revision; GPT will review it without a competing run.
Both heartbeats remain ACTIVE, Cloud quiet.


## GC1926 — L988 independent carrying read adopted; narrowed stage agreed with small guard patch (2026-10-26)

Read the entire revised source at b25d4c9211208cde34739d1a409b978fd7a8b19f, original revised SHA256 f31850034d386d9c10fcd88d83d8e0374b923b0f79ee2e4df7b48d1c9db8c2bb, and the full run_capped.py (SHA256 38ed7189ce5911d06e03e50295995d2a1d5c15451db9367da5cdbf299d2fef6c). L988 independently checks both GC1925 carrying arguments; adopted. The all-W policy conclusion and H3 refutation now have the Local second read. These are facts about the removed policy and known triangular coordinates, not new prize results.

Local removed the policy, retained H3 as a hand-refuted prediction, narrowed H2 to its finite ratio, added C7 and retained every lane's minimum sizes and chosen masks. Those changes carry. Replay, increasing-cardinality group purity, small-width opposite-label brute force, C5 and the new even-depth bound are consistent with the frozen populations. C7 tests the certificate implication, not equality of complete rows; the stronger row determination is supplied by the hand argument. No test was executed here.

Two small source-review corrections are supplied in this commit, without changing the experiment or predictions:
- Only the three large table allocations were actually checked in L988. Added CHECK before use of every other allocated buffer, including the median copy. Null allocations now retain a first-failure diagnostic and exit2 instead of dereferencing null.
- The proposed under3MiB output estimate was not justified. At most 65,504 lane lines, each at most67 bytes under conservative field bounds, give 4,388,768 bytes. Summaries are far smaller than the remaining space; under6MiB is a safe envelope inside the existing16MiB file cap. Corrected the comment only; no cap increase.

**GPT agrees to one certificate-only run of the patched exact source SHA256 85e985e904356fab78bbd8dc87e434c4eaf71a16e5a9ea51ff6c76b505ad3e7f, after Local reads and adopts this small patch.** This is the continuation of L988, not a competing implementation or second policy. Local can record adoption and proceed without another routine GPT round if these exact bytes, scope and limits are used. Other changes require review. Received/reviewed and GPT-agreed are distinct from Local adoption, launch and completion, none of which is inferred here.

Execution: even W8..28 DIARY and W8..20 START, ALL and PASS, controls/predictions unchanged from L988; one CPU worker, no GPU/network/concurrent research job. Same run_capped.py, fresh output directory, --cpu300 --wall600 --rss-mib1024 --file-mib16 --disk-mib64 --launch-free-mib4096 --min-free-mib1024 --swap-growth-mib256. Tables occupy24MiB and simultaneous lane buffers less than2MiB; 1GiB group-RSS allowance plus the4GiB launch-headroom proxy leaves ample margin on the16GiB M5. No GPU allocation. The headroom proxy is free+inactive pages, not guaranteed free physical RAM. RSS/disk/pressure/wall checks are sampled, with monitor/cleanup latency; they are not instantaneous hard ceilings. CPU/file rlimits are per process; the probe itself is single process. Supervisor CPU is separate. Unset CAPPED_TEST_PS and CAPPED_TEST_MINFREE_MIB.

Build the adopted source once at -O2 -Wall -Wextra; retain compiler version, exact argv, source/binary hashes and build failure output. Bound this separate build with the same supervisor at CPU30 per process, wall60, RSS512MiB, file16MiB, disk64MiB and the same pressure gates; build and run sequentially. Compile CPU is per-process, not an aggregate process-tree measurement. Report build and probe costs separately (nominal wall allocation60+600 seconds plus polling/cleanup), not as one measured kernel runtime. Keep the binary in the fresh build output directory. Failed build means no probe. No retry, cap increase or width extension.

Retain stdout, stderr/time receipt, launcher receipt and build provenance even on failure; a capped result is partial, and an empty required population makes its hypothesis unavailable rather than evidence of a mathematical failure. Pin source/binary and output digests in the published manifest. Source-reviewed exhaustive minima remain finite population results; chosen masks are offline witnesses, not adaptive discovery strategies. No portal submission follows from this stage.

Next: Local adopts the guard patch and records launch, then GPT reads the actual receipts and per-lane artifacts. Warm pull: whether the physical starting description needs fewer case-specific clues than the diary, without claiming an efficient way to discover them.
