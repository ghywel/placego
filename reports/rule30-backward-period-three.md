# Period-three traces in valid root pasts

GC2023, owner question, 28 October 2026. Interpret "instead of period 2" as the moving diagonal x=t through
the root, not a spatially period-three row or a new update rule. Read bits backwards, starting at the root 1.
The proper period-three words are 100,101,110; 111 is the existing constant A control. The first two start
through B, the last through A. Keeping a branch only if its next bit matches is valid ancestry selection;
forcing a cell after reconstructing it would change the problem and is forbidden.

Record searched: GC2016–2022; root_past_tails.py; backward_diagonal_b.py; record_find period-three; G122's
spatial-tail result. No recorded conclusion for these three moving period-three traces. No novelty claim.
Hand observation: a spatial 001 background maps to all 1 then all 0, so its spatial period alone is no
reason to expect a temporal period-three diagonal. The two questions must be separated.

Prediction: at least one of the three prefixes may close through a finite compatibility obstruction;
none is presumed infinite. Counterfactual: survivors at depth 128 are only a finite prefix, and any node,
period or resource cap means inconclusive. Compare complete parent sets at every visited node using the
GC2016 constructor and Local's earlier ray generator plus literal truth-table back-solving. Reproduce
first-generation counts 1,2,5,8 and the period-two closure at 38. Sharing the Row container and least-period
normalization does not make this an independent-worker read.

Frozen source: tests/probes/wolfram/backward_period_three.py, existing two dependency sources. One worker,
128 past steps maximum per new word, 2,000 live branches, 20,000 total generated nodes over the whole stage,
right-tail period 4,096; left window -130..0 is sufficient because inverse extension propagates right to left.
Every right ray is symbolically periodic to infinity. Under run_capped.py: 60 CPU/90 wall seconds, 256 MiB
sampled group RSS, 8 MiB/file, 16 MiB output, launch free+inactive 1024 MiB, ongoing 512 MiB, swap growth
128 MiB. No automatic rerun or widening. Retain exact levels, failed parents and implementation comparisons.

## GC2024 — all three root-anchored words close within five backward steps

**COMPUTED exact, dual implementation:** the complete valid-ancestor trees first become empty at depths
5 (100), 3 (101), and 4 (110). Depth counts backward updates, excluding the root. Thus their longest
matching prefixes including the root have respectively 5, 3, and 4 cells. Rejected bits are respectively
1 instead of 0, 0 instead of 1, and 0 instead of 1. No tail, node or depth bound was reached.

| Word read backwards from root | Survivors at successive backward depths through failure |
|---|---|
| 100 | 1,1,1,1,0 |
| 101 | 1,2,0 |
| 110 | 1,1,2,0 |

The period-two control reproduces closure at 38. Total 135 generated nodes including controls; 22,233
primary update checks and 22,098 separate literal-truth checks. Every generated parent set agreed between
implementations. This excludes strict proper period three from the root on x=t for any valid full-line past,
not just the displayed branch. It does not exclude an eventual period-three trace after a transient, another
path, or a temporal period-three centre column. The all-black constant trace has period dividing three but
is not a proper period-three trace.

### Short hand explanation (PROOF-SKETCH pending Local)

Write each right-background word starting at x=1 and extending periodically in both directions. The front
bit at depth d is the complement of that background at x=-d (GC2019). All compatible parent rays are supplied
by cycles of the four-state inverse map. The elementary ray relations needed here are:

    parents(0)      = {0,1}
    parents(1)      = {001,010,100}
    parents(001)    = {101}
    parents(010)    = {011}
    parents(100)    = {110}
    parents(110)    = {010100,100010}
    parents(010100) = {010111}.

These are complete infinite-ray relations, not only some periodic candidates. For a target word w of length p,
compose G at output positions p+1 down to 2, where G_b(c,r)=(b XOR (c OR r),c). Cycles give all rays. For target
110 its pair map has cycle 01 <-> 10, with 00 and 11 transient; this gives precisely the two length-six rays.
For target 010100 all four pair states map to 01 in one composite step; its only ray is 010111. The shorter
relations follow by the same four-pair table or the existing first ancestor generations.

- **100:** required front bits select successive right backgrounds 0 (root), 1, 100, 110, 010100. The only
  next background is 010111. At x=-5 its bit is 0, so the front bit is 1; the request needs 0. This branch
  closes at depth 5.
- **101:** after background 1, depth 2 permits 001 or 010. Their only parents are 101 or 011. Both have
  background bit 1 at x=-3, so both front bits are 0 instead of the required 1.
- **110:** depth 1 selects the white-background A branch; depth 2 selects background 1. At depth 3 the request
  permits 010 or 100. Their only parents 011 or 110 both have background bit 1 at x=-4, so both front bits
  are 0 instead of 1.

The relation to the horizontal precursor is now precise: (001)^infinity evolves to all 1, then all 0.
Spatial period three therefore supplies valid ancestors but does not maintain a period-three clock along
the diagonal. Requesting a repeated diagonal word is legitimate; it is compatibility, not the request itself,
that fails. No altered Rule 30 rule was used.

### Evidence and resource receipt

Frozen source f179d368. Initial sandboxed launch refused before starting a child because the swap-usage
sysctl was denied; launcher retained. A diagnosed permission-only relaunch used identical source and caps,
with monitor access, and completed: child 0.11 real / 0.09 user / 0.01 system seconds, maximum process RSS
16,138,240 bytes; supervisor 1.04 seconds, output 24,029 bytes excluding launcher receipt. Free+inactive
at launch 5,844 MiB. The child finished before the first sampling tick, so there is no sampled group RSS or
within-run pressure measurement; zero-valued maxima are not measurements. CPU/file limits and launch gate
applied, with final output-size and process-cleanup checks. No scientific rerun or scope expansion.

Retained packet `cited/gc2023-period-three/manifest.json`, SHA-256
`ecd42d955cbae227fe26df7b12af96727caeb64918db4af61e3378e2d4647bca`:
complete level counts, all failed parents, source hashes, both launch receipts and time receipt. Upload receipts
and remote stat checks verified the file digests. No visualization change is needed: no long period-three
branch survives to replace the displayed B history.
