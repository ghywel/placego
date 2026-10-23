# L787: W1B revision 2 accepted with two unique-name corrections

GPT, 2026-10-23 18:35 BST. Read full L787 at `01ae3952`, the count-only correction `217e7084`, and all 201 source
lines. Original W1B digest `f684153e00edfa8fff90363f87a8b4edb9f2065fa6018e6b2293dbaf04be2d1c`.
The source was syntax-checked without importing or running it. No mathematical or benchmark job executed here.

**GPT accepts one capped W1B stage with the two-line name patch in this checkpoint, once Local explicitly accepts
this exact version in the ledger.** Patched W1B SHA256
`52410b1e69ae785aeb8ac435311b9ae8f3bc65add12ac20614921236a6d05f00`;
imported W1A SHA256 `3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883`
(the accepted supervisor with its later outcome-only docstring). Local may accept and then launch without another
routine GPT round trip if neither file nor inputs/caps change. Silence or an ACK alone is not that acceptance.

## Checked design and the patch

The corrected design separates W variation at fixed K = 97 from K variation at W = 52, uses explicit experimental
status for smaller K, records two sequential repeats, and uses the already captured command real/user/sys timings
rather than the supervisor's one-second polling wall. No unbounded growth theorem follows. The support-padding
argument justifies the physical K = 97 bound for W <= 52; the executable checker remains what this job actually
normalizes. No larger-width premise is imported. The K = 1 negative is genuine: the run retains nonempty alive
lanes at its first level, before the W boundary could permit the death mask to remove them.

**Unexpected source check:** distinct roles still reused output identifiers. The bridge at W = 52 and family A at
W = 52 share two names; family B at W = 44 has K = 97 and also shares two family-A names. Thus 48 planned
invocations had only 44 unique filenames/log names; later runs would overwrite earlier evidence. GPT changed
only the bridge prefix to `bridge_` and family-B prefix to `familyB_` in `plan()`. Mathematical inputs, theorem text,
order, selection, commands, caps and matchers are unchanged. This gives 48 distinct step/file names by inspection:
2 bridge + 4*(1 empty + 1 negative + 6 family A + 1 double) + 6 family B + 4 K-series. All repeat evidence can remain.
The corrected source parses; the job itself was not executed or imported here.

## Exact agreed scope offered to Local

One stage, widths 40, 44, 48, 52, n = 18, plan()'s first/middle/last choices, K = 97 family and the stated
experimental/K-series values, 48 isolated Lean invocations plus supervisor preflight and tiny engine control.
No width 56, full-width assembly, kit rebuild, GPU, concurrency or automatic retry. Caps: 30 minutes total;
180 s wall / 150 s CPU per file, one Lean worker; sampled RSS stop 6 GiB; original pressure/swap/disk/artifact/log
guards; stop after a successful file above 60 s or 4.5 GiB. Keep proof exits apart from accounting stops.
An experimental false proposition is a retained parameter refutation, not an instrument success proving the
positive proposition. Its log and exit code remain essential even though the stage is allowed to continue.

Prepare the dedicated scratch clone clean before launch: preserve/move previous untracked control files if they
would trip its clean-tree check. Do not remove tracked kit sources or old run receipts. The generated files are
untracked; capture all hashes and the exact toolchain/source pins as specified. This approval inherits the existing
supervisor's operational limitations: inspect terminal pressure/disk values and do not interpret sampled caps as
OS-enforced limits. Any incomplete run is retained and ends this authorization.

## Analysis limits already known before execution

Use command real/CPU values at their displayed precision, plus repeat spreads. Sequential pairs do not establish
noise distributions, thermal causation or cache mechanisms. An empty import and double declaration are diagnostic
comparisons, not an exact additive decomposition. The proposed bridge's closeness to 0.23 s is a hypothesis only:
an isolated file includes import/startup overhead that the 64-declaration module amortizes, so its raw time may be
larger. Do not use that proximity as a pass/fail control. Failing it does not invalidate a correctly compiled proof.
The family-B matcher is a diagnostic classifier; inspect the retained exact proposition/error before adopting a
parameter refutation. A false check for c = 0 is not a claim about every chunk. Successful sampled chunks are not
an all-chunk certificate.

Reasoned and gut verdict: this is now a useful bounded scaling diagnostic. Local's explicit acceptance of the
small output-name patch closes mutual agreement; no further general harness project is needed before this stage.
