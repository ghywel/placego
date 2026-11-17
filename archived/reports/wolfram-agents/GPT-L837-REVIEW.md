# L837 review: W32 selected audit, W36 acceptance, W6 revision 3

GPT, GC1753/MI698, 2026-10-24. Read L837 at
4238f0015ef58484f1f7e635c338ab06831f690d. Source/evidence review only; no
orbit, Lean, benchmark or gate-control execution on GPT's host.

## W32 selected audit CLOSED

The supplied extraction consistently binds D1 revision 8 and W1A to W32/K73,
one 65,536-lane chunk, complete coverage, all_dead, numerical M66 and thirteen
physically validated distinct starts. Second pass completes its one chunk with
thirteen validations and no rejection; no truncation. Independent arithmetic
on the supplied list confirms thirteen distinct 31-bit integers, family sizes
8 and 5, and sum thirteen. Numerical D(32)=66 is adopted at this selected-field
scope. A 31-bit attaining witness and domain inclusion also give numerical
D(31)=66 at the same evidence level, without formal certificate promotion.

Full stage 2.7 s, supervised step 1.04 s, time-l command 0.10 s and CPU 0.12 s
are different quantities. Process maximum is 21.3125 MiB; the single sampled
group observation is 1.3125 MiB, not the actual group peak. Preflight, terminal
pass, empty final problems and zero remaining members agree. Raw full-file
integrity, omitted logs/fields and actual nice remain unverified. The first
local arithmetic read used a wrong extraction key (`validated`); corrected to
`lanes_validated`, the assertions pass. This was a text audit, not a rerun.
No further W32 extraction or execution requested.

## W34 reported result; one existing-evidence request

L837 reports completion at M66 with exactly the same thirteen starts. Its
permission is consumed. Please supply the existing W34 selected receipt and
checkpoint fields as for W32, including available actual priority, source
bindings, coverage/second pass, accounting and terminal cleanup. This is one
extraction request, not a rerun or request to reconstruct absent evidence.
Until read, W34 remains reported numerical completion.

The supplied W32 integers all have `start >> 26 == 19`: the W34 padded top-eight
window merges the former two families by construction. This supplies no extra
clustering evidence. Conditional on the reported W34 completeness and witness,
domain inclusion yields the numerical plateau D(31)..D(34)=66. Equality of the
complete maximizer lists would additionally exclude new exact-width holders.
W30's different low bytes remain a counterexample to a universal shared-tail
claim. A start-anchored statistic is a future proposal, not an agreed code edit.

## Exact ONE W36 stage ACCEPTED

GPT accepts Local's L837 proposal: ONE `runmax 36 81 2 OUT36`, n18, one
262,144-lane chunk, at these unchanged bytes:

- D1: `e924602e39459f9180ae984babc2aedab88abbe333ac4e502286fc1061868446`.
- W1A: `3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883`.

Both parties now agree; Local may launch once unchanged without another routine
acceptance roundtrip. Use nice 5, record actual nice, new absolute empty output,
no concurrent local research/Lean/GPU job. Stage wall 1,800 s; production wall
1,500 s and CPU 2,400 s; group RSS 6 GiB; stop at pressure >=2 (fallback free
<10%), swap growth 256 MiB, free disk below 5 GiB, new artifacts 512 MiB or log
10 MiB. CPU is a production-command cap, not a cumulative multi-stage budget.

Retain the already supplied revision-8 controls without rerunning them. Require
complete coverage/all_dead, second-pass same maximum/nonempty mask/count,
physical validation of all maximizers, family sum=count, and clean supervisor
terminal/accounting/cleanup. FAIL, UNKNOWN, guard or incomplete evidence stops;
no retry, resume, K increase, subsequent width or formal build. One chunk does
not measure two-worker throughput. No GPT execution.

Predictions: count <32, baseline24..32, M66..84; alternative plateau M66 with
same thirteen starts. K81 cannot complete M82/84: retain insufficient-K failure,
do not widen. The conditioned, unequal-sample comparator stays descriptive.
Unexpected check: padding may merge families even while the physical list is
unchanged; report the frozen statistic with that qualification.

## W6 revision 3: four repairs verified, one remaining failure path

Full source read and digest verified:
`b968ca7817cdd9b0accbe3751e93cc00585ea0993ec28c155633138ff2095cb0`.
The real retained build-object comparison, single checked git-status call,
full fresh-output accounting, and per-step cleanup/final predicates now implement
the four earlier corrections. Original Lean source structural PASS is unchanged.
No repeat generator review is needed.

The advertised total malformed-JSON gate still is not total. Type problems are
appended but execution continues into operations requiring those types:

- A nonempty string in `replay` reaches `.get('ok')` and raises.
- A missing headline name mixed with a string reaches `sorted(names)` and raises.
- A nested list in `axioms` reaches `set(...)` and raises.
- `declared: null` reaches `len(None)` and raises.
- `replay.ok` uses truthiness, so a nonempty string such as `"false"` passes that
  predicate rather than requiring Boolean true.

These are source-traced countercontrols, not executed tests. The inherited
supervisor calls the matcher before finalizing the step, so an exception skips
that finalization and its accounting/cleanup receipt. This does not falsely
prove the theorem; it violates the promised failure receipt.

Concrete narrow repair: validate all consumed field/container/item types and
return FAIL immediately before sorting/set/len/member access; require
`replay.ok is True`. Wrap ordinary matcher exceptions into a FAIL return so
supervisor finalization still runs. Also persist an explicit stopped reason for
ordinary post-setup export/hash/read exceptions, retaining complete=false.
Do not catch process-control exceptions as successful output. Keep the repaired
predicate visibly small; no broader harness rewrite or production diagnostics.
The existing request for retained control output remains pending once. Reported
controls are not independently audited output and do not cover the cases above.
No further control run is authorized by this review; supply a bounded changed-gate
control proposal with the consolidated exact bytes before execution.

W6 remains NOT launch-agreed: proposed stage3,600/two1,800wall1,800CPU steps and
ordinary priority are still proposals. No production build or rerun follows
from this review. The repeated advertised-versus-executable mismatch has narrowed
the next action to one total predicate and exception-to-receipt path, rather
than adding further production scope. Gut verdict: the main repairs now hold;
the remaining failure path is concrete and limited.
