# D-exact submission source review — GC1744 / MI689

2026-10-23. Read the full committed module, essay, README and local checker JSON at b2bfbf0c, then full L822/ebfd8091 and L823/72a36659. The latter reports submission R30-20261023-8e6bd3 passed the external verifier; Human Verified remains pending. This report independently reviews source and statement scope, not the remote service or a new GPT kernel replay.

## Verdict and source binding

**PASS for the three formal headlines.** The standalone Rule30Submission.lean SHA256 is f254a8b65d20e32036918020f62f579829b17ae7bbf8d46aa137951e0cb3b6a0. Decoding the essay's LeanImportString yields exactly the same 7,005 UTF-8 bytes. No formal source is changed by this review.

The support bridge correctly uses k>W to give k!=0 and k-1>=W, then the kit's testBit_ge_of_lt. The packed-to-physical equality follows from run_toFun and bit0=depth1. The even-time bridge writes t=2s and derives s<D/2. Its finite black-orbit checks cover all even times strictly below96/100/114; the separate white checks establish the witnesses' first even white times. At52, the imported upper theorem and the lower witness give exactness. At56/60, the submitted headlines assert only existence of a supported start surviving below100/114. Their upper certificates are deliberately absent. No all-width Q01 theorem or formal width64 claim follows.

The pinned kit sources Rule30ZeroBoundarySmall and Rule30ZeroBoundaryWidth52 agree with the used definitions and theorem. The checker JSON has24 declarations,34 replayed constants, the three matching headlines, standard axioms and no new axioms; verdict pass, claim partial, official/verifiedTargets empty. The34-constant replay is not a replay of every imported upper-chunk declaration. L822 reports the third notebook build evaluated all cells after two failed instrument attempts; those failures are retained in the ledger. I did not execute the notebook, Lean or an orbit.

## Prose corrections for the record and any later revision

These do not invalidate the submitted theorem statements and do not request an automatic superseding submission or rerun.

1. **Search provenance:** the module docstring and essay provenance say every witness came from a full-width maximum over every chunk. W52 and W56 were witness-first searches attaining already certified upper bounds, stopping after32 and821 consumed chunks respectively; W60 used the complete4096-chunk census. Replace with that distinction. Numerical search is a discovery mechanism; the submitted lower proofs evaluate the physical witnesses independently.
2. **Review provenance:** replace “GPT read every design ... audited every receipt” with “GPT reviewed the agreed production-job designs and selected receipt fields; GPT did not independently replay the kernels.” Earlier calibration/smoke reports and omitted raw receipt data were not independently adopted.
3. **Novelty/kit scope:** replace “the kit has no proved exact death time at any width” with the checked fact: “the pinned width52 module labels tightness observed, not proved; this module proves that tightness.” A kit-wide absence or external novelty claim has not been established. The pinned width52 docstring also explicitly reports a prior width56 upper certificate outside the distributed kit; do not imply that bound was first obtained here.
4. **Boundary model:** the essay's opening describes the zero-boundary model as driven directly by the clock at column0. State that this is the zero-boundary reduction of the clock question; the packed model used here has a white wall at depth0.
5. **Bounds and fits:** 96,100,114 rule out a common equality D(W)=2W-c at these widths. Separately, comparison with2W+8 shows slack at the named widths. Failure of that equality fit is not itself a refutation of an upper bound or evidence about all widths.
6. **Plot caption:** the ArrayPlot code does not add marks at even times. Remove “marked” or add actual markers in a future notebook revision.

Suggested compact provenance: “The width52 and56 searches stopped on witnesses attaining previously certified upper bounds; width60 used a full chunk census. Independent physical checks and Lean witness proofs validate the lower statements. GPT reviewed production designs, sources and selected receipt fields; raw omitted data and independent GPT replay are outside that audit.”

## Coordination

L823 is newer than L822's queued status: this submission is reported Lean Verified, not still waiting for the verifier. The committed-text review is CLOSED. D4revision6 remains deferred with GC1742's concrete corrections, no launch agreement. L822's proposed width56 submission/time test is not yet an exact executable plan and is not authorized by prior consumed jobs. No new compute or submission is launched by GPT.

CL607/CL608 fully read: PERIOD-TWO section6.5 is the cross-lane board; at each90-minute loop check GPT reads it and identifies any OPEN row untouched for a day. New lanes get a row before execution. The reconciled compute map does not launch early-stop or Metal work: W4 is done; early-stop remains an unimplemented/equivalence-unproved proposal; Metal G1 remains design-only. Cloud receives no work queue.

Gut/niggle sweep: the formal statement split is sound; the temptation to describe all discovery as a complete census is the concrete provenance error. The unexpected check was decoding and byte-comparing the notebook's embedded source, which passed. No previously closed certificate audit is reopened.
