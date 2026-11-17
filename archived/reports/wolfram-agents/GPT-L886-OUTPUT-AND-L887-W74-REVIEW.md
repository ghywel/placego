# L886 notebook outputs and L887 width-74 stage — GPT review

GC1795 / MI728, 2026-10-24. Read L886 at
808f3112a90600bcd1b27572c76d32b922e0e6a9 and L887 at
5bb2e9c4857190ccc13b857b544483124b0c0501 in full.

## Verdicts

**L886 actual retained notebook/output review PASS.** This closes the output dependency left by GC1793/GC1794.
The exact source was already carried in GC1793; the notebook embeds those same bytes. No mathematical defect
requiring a superseding submission was found. Submission 16, R30-20261024-991a71, was already submitted under
owner authority; this read is subsequent review, not retroactive launch permission or an external verifier result.
L886 reports Lean Unverified/queued at submission. The three exact negative-edge cases have deadlines 8, 13, 14,
with arbitrary right tails, not just finite configurations. The general EdgeObservable conjecture stays open.

**L887: GPT explicitly accepts ONE width-74 census stage at the exact files, input and caps below.**
Local's explicit proposal and this acceptance constitute the two-party agreement. No launch or completion has
been observed at this checkpoint. The questions justify this single extension after the P2 comparison:
measure the new maximum, test the predeclared concentration statistic and obtain a candidate lower witness.
There is no agreement to W76, a retry, a certificate-generation run or any concurrent research job.

## L886: actual evidence read

Downloaded all 19 listed files (566449 bytes) from `cited/edge-sep-submission/`: the notebook, nine separate
cells, count/digest files, their tar archive, raw and parsed checker output, gate receipt, control output,
notebook build log and predictions. Data remain outside git. Key byte SHA-256 values:

| File | SHA-256 |
|---|---|
| essay.nb | 770639aea7695c2032112f0ff9c94012e08148e0b7ad46d53db64bb017a2d02a |
| cells.tar.gz | d0f7dcac7be544a57a9f9987598516fdbe2ff62330b73c877cd18626e273dbd2 |
| check.json | a3e95c74374721f40dd5c7649c0bedb6c3875cdbf40bd5f85ca4ba6cd019f019 |
| check.raw.txt | 7ba417662c07224db176fb2dba04f6cde2d80ca6a69451f902a48b2a575560b1 |
| gate.json | 772a20c408a748218ff491997cf55d1eeb0e58831c17d4a1fec1b74322b5fca1 |
| gate_controls.txt | a33b81b2e116966e1fc0235f4a79f8ff93e671a4ab2e05fbe22b09e1ea692e12 |
| nb_build.log | a72bb3dcd031f9c2cdf08582bc8558f85c689629ca1706fa88db8e96a8d8c52d |

The 11 archive payloads exactly match the separate nine cells/count/digest files; every cell digest matches.
Parsed JSON equals the JSON portion of the warning-prefixed raw checker output and Cloud's committed checker
receipt. Eight headlines, their types and standard-axiom reports agree; 583 constants replayed is the retained
checker's report. This was not a new GPT kernel replay.

Beyond the gate's count checks, all 279 displayed environment names and declaration kinds match the checker
(259 theorems, 20 source definitions; 18 compiler-generated match definitions excluded). All nine actual
notebook Output boxes were checked against the supplied cell exports: cells 1–7 and 9 agree after Wolfram
serialization normalization; cell 8 has exactly the same 45 graph vertices and 44 directed edges. Graph-label
serialization differs, and no pixel/layout identity is claimed. The root and four project carrying dependencies
are present; this checks the display, not an independent extraction of Lean's dependency graph.

The embedded Lean source matches SHA-256
`dd1e9b87f9f34b839461353f9c9a6ad3a256d6ed4875a1237fd8cbe3fc3f2083` exactly after notebook string decoding.
The essay source is `c8aee65530e8a387aa4b9e1145b3dae62432804ac433ff6ce1646e0b8eca4c36`; README's stale digest
has now been repaired. The gate source (6f7e613f102ad75cf0f5353f02c4643b4d885c1b80d87d90bdc3b23c3ee454c6)
and expected-output helper (9886d6a5b26c337dc0b51dce71197ebdba52da69a41b8fad01945bbc2df3740d) were read.
For the pure-file gate and mutation checks, numerical expected-value functions were replaced with the already
reviewed literal expectations: the positive packet passes and all 15 mutated packets fail. No orbit enumeration,
GPU job, Wolfram execution or Lean build was duplicated. Initial notebook comparisons exposed serialization
differences; explicit normalization resolved them without changing mathematical expressions.

Two editorial qualifications, neither a reason to resubmit: cell 5 displays the TYPE of HasLeftEdge, whose actual
definition is in the embedded module; and the reported 16 controls are one positive plus 15 negative controls.
For future gate maintenance, exact environment-name/kind and graph-structure binding would strengthen the
count/root checks; this actual packet already passed those additional checks here.

L886's first build invocation failed before compilation because lake was missing from its command environment;
retain that failure separately. Its subsequent build/checker CPU/RSS figures are Local's reports. The notebook
log reports 111.8 s internally, with 124.23 s outer wall time; the outer parent-process CPU/RSS is not a full
Wolfram-kernel resource measurement. Log-printed Wolfram hashes are not substituted for the byte hashes above.

## L887: exact accepted job

Runner source commit: **0a5963132bb538015a7f9114f08696675360f861**. Verify these bytes immediately before launch,
including the helper and previous-result input (recorded by the runner but not themselves enforced as pins):

| File / input | SHA-256 |
|---|---|
| tests/probes/wolfram/p1c_census.py | c9174d25958e6af3e6823512a47827dbdad95876c98826f3cdce5ae8673e7d60 |
| tests/probes/wolfram/p1_engine/main.swift | 6b76fe740856c3e01c5bc2baffe68de6b9022bf8dfafb1ce8241ce4c0c3bd1ec |
| tests/probes/wolfram/p1_engine/lanes.metal | 17a81e6621185098f3132ea199f41530de699f56030c9ac6c4c6392a7b1e5ec9 |
| tests/probes/wolfram/p1_lane_engine.py | ea9b7cc23d32373c270997cb8420b5ff1ce339eb5588813dd1ad1e859295738f |
| tests/probes/wolfram/d1_engine.py | e924602e39459f9180ae984babc2aedab88abbe333ac4e502286fc1061868446 |
| tests/probes/wolfram/w1a_harness.py | 3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883 |
| retained W72 p1c_result.json | 31df72e199ff1e63692bd79bffff1a1a1721a809e783a7ef0028d43c8d43293d |

Invocation: `python3 tests/probes/wolfram/p1c_census.py stage 74 OUT --prev W72_RESULT`, once on Local's M5,
with a fresh absolute output directory and the exact input above. Use the supervised `stage`, never direct `run`.
Only this job runs: one sequential engine process at a time; no concurrent notebook/Lean/GPU/census job.
The existing toolchain/device baseline and binary/source digests must remain in the receipts.

Exact scope: W=74, T=296, 37 free index bits, 32-lane words, G_max=2^19. Cover [0,2^37) once in 256 calls of
2^29 lanes, each 32 batches of 2^24. The preliminary 2^24-lane gate and carried-witness list are extra controls,
not additional coverage in the census total. No material source/input/scope/cap change inherits this agreement.

Caps: 3600 s stage wall (including preflight/build); supervised main step 3600 s wall and 3600 s sampled CPU
budget; build subprocess timeout 600 s; each engine call 120 s. Group RSS stop 6 GiB, GPU allocation budget 2 GiB,
swap growth stop 256 MiB, minimum free disk 5 GiB, artifacts 100 MiB, logs 10 MiB; existing W1A pressure/monitor
failure stops apply. These are monitored limits, not promises of zero overshoot or a measured system peak.
Any cap/pressure failure, interrupt, mismatch, truncated maxima, incomplete coverage or nonzero censoring leaves
an incomplete/failed receipt and stops without automatic retry. Persist per-call progress, job JSONs, output
JSONs, source/binary/device/toolchain evidence and final stage receipt; keep offending diagnostics.

## Why the width extension passes review

The full revision-3 runner was read, with the prior GC1780/GC1782 audits. Static syntax checks pass. Removing
only the inserted serve branch and changed mode comment from driver revision 6 gives byte-identical revision-3
source. The serve branch is not entered in census/list mode. The new concentration field does not enter a gate.

At W74,T296, the row length is 372 and the workspace has two columns of 75 lane words per group. The kernel
uses dynamically sized buffers, not a hidden width-64 array. All 37 free bits fit the 64-bit index; the largest
trace shift is 36. Death bin 148 is below the censored bin 2047, and 2^24 batch lanes fit UInt32 histogram counts.
The in-place update preserves the old left neighbour, reads the old right neighbour before overwriting it, and
computes the expanding support through W+t+1 with its zero halo. The domain extension introduces no index,
histogram or support-bound exception.

The driver's simultaneous device-buffer formula gives **1,135,617,488 bytes (about 1.058 GiB)** at the largest
batch: rows 744 MiB, workspace 300 MiB, deaths 32 MiB, bases/valid/group maxima 7 MiB, plus small trace/histogram.
The two full-call host group arrays have **256 MiB logical payload**, plus allocator capacity, runtime, receipts,
Python, retained gate/reference arrays and transient copies. Thus the 2 GiB GPU budget is justified while the
6 GiB monitored group cap and launch headroom checks cover the larger live workload. Neither figure is a
system-wide peak, and 256 MiB is not a GPU ceiling. Device max-buffer checks remain active.

Coverage checks are exact integer checks. The independent d1 gate covers every one of its 2^24 lanes; scalar
samples check 64 distinct indices per batch. All 40 W64 and 252 W72 carried starts must reconstruct identically
and die at 116/130. Every final maximizer is reconstructed and validated; every containing d1 chunk is checked
through M+1, giving its upper bound and matching complete maximum set, not just testing listed winners. Other
chunks rely on the complete GPU census with controls; this is numerical evidence, not a Lean upper certificate.

The current complete W72 receipt was reread for cost attribution: census wall 1146.38 s / 2^36 = **16.6820 ns/lane**;
GPU total 1064.91 s / 2^36 = **15.4965 ns/lane**. L887's 10%-of-W72 prediction is a WALL-time prediction. The runner
still separately scores GPU time within 20% of the older 12.9 ns value. Keep both named predictions and report
both outcomes; do not silently relabel one. Neither timing prediction nor D74>140 nor more than 8 occupied blocks
is a correctness failure. The census-wall estimate excludes gate/finalization/build overhead; the stage cap includes it.

Finally, L887's so-called negative control is a cross-engine/known-witness consistency control, not an injected
fault, and cannot promise detection of every indexing or engine fault. Retain the earlier P1 mutation controls
as historical support, with the new width's gate and carried witnesses supplying fresh domain checks. No new
mutation campaign or code revision is required for this accepted job. A failed check invalidates the run; a pass
supports the scoped numerical result without proving universal implementation correctness.

Gut and reasoned verdict: the useful new width and explicit concentration prediction justify one bounded stage;
the source and arithmetic support it. A plateau, wider concentration or slower rate must be reported just as
faithfully as a new record. Further widths or proof-generation work require a new exact proposal.
