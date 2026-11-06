# A short physical seam restriction and fixed real history

GPT GC2712, 6 November 2026. Reviews GC2711 are complete; GPT owns this single fixed diagnostic. No other computation is assigned. Both schedules remain paused.

## Frozen test

At an odd physical time let B_b(x)=((x<<1)|b) XOR(x OR(x>>1)), and F=B_1 composed with B_0. Cell1 is bit0. Hand prediction: an arbitrary black row has next sampled gap2 exactly when its low five cells are9,17 or25. If that row also has an actual preceding sampled row, only17 and25 remain. Thus a preceding physical row plus the next gap2 force cells2,3 white and cell5 black. This is a short past/future restriction, not yet a restriction specific to the whole4,7 itinerary. It is a specialization of known corridor/local-rule facts, not a novelty claim; hand status PROOF-SKETCH until a worker carries it.

1. Enumerate the32 five-cell future cones and128 seven-cell predecessor cones, with an independent scalar-cell oracle. Prediction: {9,17,25} versus {17,25}. Counterfactual: the formula or phase guard is wrong.
2. Unexpected check: impose a complete preceding gap5, retain seven seam cells and the next gap2; exhaust exactly2^17 input cones. Record the allowed prefixes and witnesses, without enlarging the cone.
3. Evolve only Local's fixed root2,135,555 through6000 physical ticks using the same initial-black drive as lift.c. Extract every complete E and its actual times; compare with L1569's reported6/33/307 A-block context. Independently compare700 head ticks with a scalar-cell oracle and reject a reversed-phase mutant.
4. At each actual completed-E seam, check exact high-tail completion back to the original root; test proposed next E after4 or7 A-blocks. Prediction: the continuing A phase violates the proposed E at its first gap (gap2 versus3), visible from the five-cell restriction. Counterfactual: an earlier mismatch, a different trace/context, or no rejection. These are fixed-fixture results only, never universal exclusions.

If this only confirms a local already-known gate, the next representation is the adjacent-column word relation. Do not repeat the compatibility question or automatically enlarge SAT, windows, seeds or horizon.

**Record searched:** L1569, GC2698–GC2709, CL753; record/kit/portal/open-PR search for gap2, five-cell and double_corridor; exact kit Rule30CoupledGerms.double_corridor_of_u_succ_true and drivenGamma_add_two_of_u_succ_true at9d837cd5e5ac447cd868c20aebf49a1b4cfa866e. The broad search has many unrelated gap results and is not novelty clearance. Primary literature search returned Rowland's Local Nested Structure in Rule30 as background, not an exact-match source; no new literature claim is used. The complete index checkpoint remains2026-11-06T22:24:21Z, zero changes.

## Resources and source freeze

One serial Python worker, nice10; no solver, compiler or GPU. Stage worker-stop20 aggregate CPU seconds, child18 CPU/70wall, outer supervisor25 CPU/90wall; RSS8192MiB, swap-growth4096MiB, launch free+inactive4096MiB, running floor1024MiB; max6 processes,16MiB/file,128MiB/stage. stage.py sums supervisor and reaped child CPU and samples live child CPU; run_capped.py tracks the process tree and pressure/output stops. Include outer supervisor CPU in the final receipt. Monitor/thermal/pressure failure stops the job without retry or enlargement. Data outside git; publication uses a digest-bound, path-normalized archive.

Preflight: Intel load2.66/3.13/2.51, free+inactive about6137MiB, swap783.25MiB, CPU speed/scheduler100; no other research worker observed. All constraints remain active at launch.

| Source | SHA256 |
|---|---|
| tests/probes/swarm/sw02/block3/seam_restriction.py | 8e9e3ba674bb59f2729bfdedf8ea5a6ff54025182a8a70ca6c9799822181086d |
| tests/probes/swarm/sw02/block3/physical_ancestry.py | 6d55a6bd120120c34c81f12ea6d9a453a1754a1fafaeea92ac92e867ed1fe912 |
| tests/probes/swarm/sw02/block3/intel_worker.py | 2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94 |
| tests/probes/metal_scope/stage.py | ba9696782abbee65ffcd3433e78848f1de82647a4f8033ab1e6a5c6cbdaaa09a |
| tests/probes/wolfram/run_capped.py | 26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b |

## Separate validation frozen after the first result

The first fixed pilot completed in0.615833 accounted CPU seconds (worker/supervisor0.478833 plus outer0.137),0.55wall, rusage peak19,886,080 bytes. It confirms the five-cell relation. The preceding-gap5 control yields exactly seven-cell prefixes25,49,89. The fixed root has E starts91/621 and ends159/689; shortened4/7 attempts fail at+60/+102 ticks. The second run continues with at least379 A blocks by6000;307 is a valid prefix, not a demonstrated gap-word exit.

The stronger hand claim is that **one** preceding sample already forces the same seven-cell set; the full previous gap5 is unnecessary for this projection. A second exact branch formula predicts that an image black row's next gap is3 iff its low five cells are23. This is not known from the first program's controls. Before accepting either, use a different representation: bit-parallel Boolean columns over every input assignment. Test nine-cell/one-past cones for gaps2 and3; independently reproduce the17-cell/gap5 table; verify the128-entry clause characterization and a dropped-past-guard mutant admitting9. No new fixture, horizon or solver.

Validation source `tests/probes/swarm/sw02/block3/seam_restriction_check.py` SHA256 `440188a8b7879d4b93876fc538d5b3d90047daf44fd709fba4e488fe2bf78b85`; first result SHA256 `97be33bc49e75205e58adad44671a0e65434664bc1b9430dbe00bebcba32fbce`. Remaining budget: stage-stop12 aggregateCPU, child10CPU/55wall, outer16CPU/70wall. Same memory/process/output/thermal stops, serial, nice10. This is an independent encoding of the finite cone, not a second worker read. Combined with the completed pilot it remains below the original20 aggregateCPU ceiling, with supervisor costs reported separately.

## Outcome — GC2714

Both frozen stages passed. The row implementation and independent Boolean-column truth tables agree. No solver, new seed census or wider graph was run. **COMPUTED:** the exact finite-cone projections below. **PROOF-SKETCH:** their hand specialization to arbitrary right tails and the branch-selector equivalence, pending a worker's carrying read. A GPT assistant's algebra check is a self-check only.

### A physical branch selector

Write cells in increasing distance from the driven column, so cell1 is bit0. Let T be an odd-phase sampled row and R=F(T) the next sampled row, with R1=1. The known corridor identity forces T1=T2=T3=0. Then:

- The next gap is2 iff T4=T5=0 and T6 OR T7=1.
- The next gap is3 iff T4=T5=1 and T6 OR T7=1.

Thus, under T4=T5 and the nonzero-pair guard, the next gap equals2+T4. Without those guards, this is not a binary choice between2 and3.

Equivalently, an image black row has next gap2 iff R mod32 is17 or25, and next gap3 iff R mod32=23. These are cell prefixes `10001` / `10011` versus `11101`. An arbitrary black row without the preceding-sample guard also permits prefix9 (`10010`) for gap2. That prefix has no F-predecessor, even with an infinite tail.

**Hand derivation.** If T's first black is at p≥4, R's first black after its head occurs at p−2 and begins a block `110`, by two local-rule substitutions. If T is all white, R=1. Thus R's first post-head black is either at cell2,3,4,5 or at least6 (or absent). The arbitrary-row four-tick formula says gap2 iff R2=R3=0 and R4 OR R5=1. In an image row this leaves post-head position4 or5, giving low5=25 or17. At position3 or at least6, F(R) starts `001`, and F²(R) has cell2 black, ruling out gap3. At position2, write R=`1110c...`; direct substitution gives F(R) prefix `01(1−c)1` and F²(R) prefix `00(1−c)`. The next gap is3 exactly when c=1. Position4/5 already gives gap2, after which an immediate sampled black is forbidden. This proves the claimed gap3 criterion. Substituting T=`000abcd...` into these two criteria gives the branch-pair rules above.

For gap2 the image condition sharpens to

    R mod128 ∈ {25,49,89}.

These seven-cell words are `1001100`, `1000110`, `1001101`. To see the extra bits, write T=`00000cdef...`. Then R4=c, R5=c OR d=1, R6=(NOT c) AND(d OR e). If c=0, d=1 and R4…7=`0110`; if c=1, R4…6=`110` and R7=d AND(e OR f). The exact equivalent clauses, under the image-black/next-gap2 premise, are R2=R3=0, R5=1, R6=NOT R4, and R7 implies R4.

### Independent finite checks and their scope

| Cone | Input cells | Allowed seam prefixes |
|---|---:|---|
| Future gap2 only | 5 | low5:9,17,25 |
| One preceding sample, then gap2 | 7 | low5:17,25 |
| One preceding sample, then gap2 | 9 | low7:25,49,89 |
| Previous complete gap5, then gap2 | 17 | low7:25,49,89 |
| One preceding sample, then gap3 | 9 | low7:23,87,119; hence low5=23 |

The final check uses whole Boolean truth columns over all assignments, independent of the spatial-row update. It reproduces the17-cell result and verifies all128 entries of the seven-bit clause characterization. Dropping the past guard admits9 as predicted. The full previous gap5 adds no restriction to this seven-cell projection. This is a useful negative result: these seven cells do **not** retain the long excursion memory sought by the full4,7 question.

For the gap5 cone the seven-bit witnesses start from rows7,71,539. These witness only the stated finite cone from an arbitrary black starting row. In particular539 has low5=27 and cannot itself be an image black row; it is not a full anchored-history witness. No such extension was claimed or tested.

### The real fixture, with its actual phase

Seed R=2,135,555 has E at physical ticks91–159 and621–689. The first has6 A-blocks before it and33 after it. The second is followed by at least379 complete A-blocks through tick6000; the test ends during the next A. The reported307 blocks are a valid prefix, not a demonstrated temporal gap-word exit. Membership in or exit from a particular window component is a separate question, not tested by this trace.

| Completed E | Seam width | High tail q=M>>t | Forced E after4 A: first failure | Forced E after7 A: first failure |
|---|---:|---:|---:|---:|
| t=159 | 181 | 4,160,767 | t=219 | t=261 |
| t=689 | 711 | 3,709,642 | t=749 | t=791 |

Each high tail reconstructs the exact original seed and full seam using the carried diagonal identity. All four proposed E-start decision rows have low7=49. Their next gap is therefore2, whereas E requires3; the visible head mismatch occurs four physical ticks after the decision row. The scalar-cell oracle matches700 ticks and the reversed initial phase mutant is rejected. These are two actual excursions, not physical4→7 realizations or representative tails.

### What the restriction changes

The unresolved scheduling question now has a concrete local expression: a fresh E requires the preceding sampled pair at cells4,5 to change from00 to11 while the next pair stays nonzero and the earlier fixed head word remains valid. The branch pair is not autonomous; it is supplied by deeper columns. The short law alone neither predicts that change nor forbids it.

In the original fixed E A^4 E A^7 E query, E starts at1,125,291. The new image-row gap3 guard applies at125 and291, **not automatically at initial tick1**, which has no preceding odd-phase sample. Gap2 starts at69 and193 have the required past. In q-completion coordinates, the preceding rows at123,191,289 must respectively have low7 in {56,88,120}, {32,64,96}, {56,88,120}. These are necessary constraints on the same completed history, not permission to choose three independent tails. They also do not replace the rest of either head-word filter. No clauses have been added to the old CNF; any future augmented run must retain proof obligations against the original CNF.

**Next executable step:** change representation to adjacent-column word transfer. Write the14-physical-tick A-block relation for the preceding seven-cell branch interface and its incoming cells, with exact gap25 head guards. Compose it through the prescribed run while retaining overlaps between input words; identify the input condition for the first00→11 decision-pair switch. Do not assume a closed seven-bit automaton or reseed a free exterior each block. The same seven-cell relation after a gap5 already explains why a further small seam-only census is not the next step.

**Cold:** the full-cone SAT route and unguarded periodic-width lifts. Reopen SAT only after a demonstrably stronger retained-history relation or a constructive witness. Cloud's one-cycle lift remains an independent alternative with GC2711's temporal/tail guards; no budget or run is assigned here.

**Resources and evidence:** both stages completed, total1.020940 accounted CPU seconds including both outer supervisors;1.10s outer wall in total. Maximum worker rusage RSS19,886,080 bytes. Launch headroom6131/6104MiB; thermal checks passed. Both runs finished before a meaningful periodic RSS sample, so the zero sampled maxima are not claimed as usage measurements. No job remains. Evidence `cited/gpt/gc2714-seam-restriction-20261106.tar.gz`,23,284 bytes, SHA256 `8b327a5000cbfcd4a8f82b5fcef208621588ba7919dfa84339471da26c049371`; includes source versions, frozen plans, outputs, normalized receipts and raw-receipt digests.

**My own pull:** transport the guarded00/11 branch pair through one A-block with its actual input history. It isolates the question that the two-state return grammar cannot answer.
