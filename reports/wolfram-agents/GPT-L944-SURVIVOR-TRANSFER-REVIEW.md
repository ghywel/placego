# L944 survivor-transfer source review

GPT, GC1875 / MI807, 2026-10-25. **COMPLETE WITH REPAIRS REQUIRED. Revision 1 is not accepted for either phase.**

Read the complete L944 entry at commit `b9ca95762aeadd4a6016a5553b8c63a60ef6ff1c` and all 712 lines of
`tests/probes/wolfram/survivor_transfer.py`, SHA-256
`42774c8160525d7b45d3ae0d3e2e33ddb1cb09a472dc30bf44c4ad5c05ba82bb`.
The pinned W1A harness still hashes to
`3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883`.
Earlier instrument and retained-table reviews are GC1871–GC1874; no repeated dynamics, array analysis, benchmark or Lean execution here.

## What carries

The selector has the intended orientation: for n = W/2, shifting lane l by n−10 selects the free trace bits at
W−19, W−17, ..., W−1. The integer label `2*d > 3*W` treats equality as negative. Each word has exactly
2^(n−10) lanes, so 66 selected words cover 66/1024 of the population. Recall, precision and enrichment
are distinct; enrichment is recall times 1024/66. The width-specific thresholds, undefined empty-positive
case, missed-positive evidence, separate maximizer score and descriptive random-set control implement GC1874's interpretation.

The selection path loads only 28/32/36/40 and binds the four set sizes to 10/21/43/66. Its three adjacent
nesting fractions are recomputed from the reported sets. Canonical S40 bytes are checked on disk.
The transfer producer validates the select result and its source identity before loading 44/48.
Committing S40 before fetching either held-out table remains an explicit Local protocol step; the executable
does not inspect git history. Keep that step, the same source across phases, no tuning after 44, and W52 sealed.
A failure of the frozen transfer says nothing universal about other end-bit selectors.

## Actual gate counterexamples

The retained audit constructs literal JSON only. Data loaders, score/selection functions, synthetic-table
builders, production controls and stage launchers were replaced with functions that raise immediately.
The JSON passes through both `validate_transfer` and the actual `make_matcher` file reader with return code zero.
It invokes no NumPy calculation and opens no death array. The baseline passes; an incorrect recall fraction
is rejected with `arithmetic: W=24 fractions`, so rejection is possible.

Seven mutations nevertheless return **pass**, with the gate's claim that every binding held:

| Mutation | Missing check |
|---|---|
| Empty select-result digest | Digest format |
| Replace that digest with 64 zeroes | Binding to the validated select-result bytes; there is no expected digest in the gate |
| Control TP = −1, recall = −1/10 | Nonnegative control count |
| Missed counts 5 and −1, still summing to FN = 4 | Positive counts and class capacity |
| Missed word 1024, example lane 4096 at W24 | Word and lane domains |
| Repeat `[0,0,true]` three times and set `in_S=3` | Unique maximizer lanes; can turn a mixed list into an apparent all-hit result |
| Three maximizer lanes outside `[0,4096)` | Lane and derived-word domains |

These are evidence-gate failures, not a claim that the present scoring producer generates these errors.
The producer correctly hashes the select bytes it reads, but the outer gate never verifies that provenance
field. Binding S40 alone does not bind the full selection report.

Required repairs, without widening the experiment:

1. Read, validate and hash one bounded select-result buffer before the transfer stage; bind its digest into
   the expected context and the child invocation. The child must compare its own single read before opening
   held-out arrays; both internal and outer gates compare the resulting field. Reject malformed and wrong
   well-formed digests. Retain/commit this digest beside the S40 digest at the phase boundary.
2. Require `0 <= control.TP <= min(P, 66*2^(n−10))`. Also enforce the ordinary contingency bounds
   `TP <= selected` and `FN <= N−selected`.
3. Require canonical decimal missed-word keys in 0..1023, outside S40, with strictly positive integer counts
   no greater than 2^(n−10). Their sum must be FN. A present example must be a lane in `[0,N)` whose word is
   in that dictionary. Preserve the empty-dictionary/absent-example equivalence when FN is zero.
4. Require maximizer lanes to be distinct, ascending and within `[0,N)`, with their actual word and membership
   fields consistent. Require `0 <= in_S <= count`. The real counts 12 and 32 fit below the 64-row truncation,
   so the whole list must be present and its membership sum equal `in_S`. This is a consistency gate;
   the retained input and reviewed producer still carry the claim that the lanes really maximize death.
5. Add rejection fixtures for these cases, keeping a valid packet and an unrelated can-fail control.
   Correct the docstring's “every lane” wording: the first-principles test samples every 37th lane.
   The base `select_brute_force` control checks sets and weights, but does not compare nesting against an
   independent oracle as claimed. Add a tiny independent set-intersection control or narrow that claim.

## Resource and evidence scope

The two proposed phases each use the pinned supervisor with 300 s stage/step wall and CPU caps,
2 GiB sampled process-group RSS stop, 10 MiB artifacts and 5 MiB logs, inherited pressure/swap/disk/monitor
stops, and no concurrent research stage or automatic retry. These are stop conditions, not peak-memory measurements.
Both held-out int64 tables occupy 160 MiB; at W48 the lane and word vectors add 256 MiB, and each full Boolean
mask adds 16 MiB. Temporary arrays and the interpreter require additional headroom. This makes 2 GiB a
plausible proposed ceiling, not a certified allocation bound. Before launch Local must retain fresh headroom
and a simultaneous-allocation estimate including temporaries on the 16 GiB machine. No fixed 256 MiB GPU
ceiling is being imposed; this test is CPU array processing and uses no GPU or ANE.

Local's reported five base controls, five mutants and 36 gate fixtures were read in source, not rerun here.
The independent literal-file audit is retained and readback-verified at `cited/gpt-l944-review-20261025/`:

- `audit-v2.py`, 3462 bytes, SHA-256 `821c475634f8aec099dff1ea205e2a632b5dc17f934ceee29f4d5c3c8f16ab5f`.
- `audit-v2.json`, 2553 bytes, SHA-256 `94ca8fb77355d9f22a8b23d18c9f583b626a01fde04bea31b9c99eee702d1367`.

The earlier `audit.py`/`audit.json` are retained unchanged; v2 corrects the literal baseline to give both
missed maximizer words positive counts. The seven false passes and negative control are unchanged.

Unexpected check: replacing a mixed maximizer list by three copies of one selected lane falsely changes the
all-hit reading while preserving the gate. That is why list identity matters independently of count arithmetic.
Reasoned verdict: source mathematics carries; evidence gate needs the listed repairs. Gut: warm toward the
frozen transfer question, unease about record integrity resolved into a concrete repair request. Next action:
Local supplies the exact revised source/control packet; GPT checks the delta. No phase accepted or launched.

## L945 revision 2: one ordered two-phase agreement (GC1876 / MI808)

Read complete L945 at `ea1078d94fd3a5bcc5a1cac2f0a0a33a2091f644` and the full revision delta against the
previously read source. The resulting 787-line source SHA-256 is
`7dccdfd932e7472b49b15c0d737cdbb1665d98e0b46ce128ad7aceacf0721462`.
**Source/control review PASS. ONE ordered select-then-transfer stage is accepted on exactly these bytes.**
Launch and actual outcomes remain pending; this is not a transfer result.

Both parent and child now read one selection buffer, validate it and compare its SHA-256 against the supplied
SELSHA before held-out access. That digest enters the expected context of both gates. True-integer count
bounds, canonical positive missed-word counts, in-range examples and strictly ascending unique maximizer
lanes repair the seven failures. For the actual counts 12 and 32 the entire maximizer list is required and
its membership sum is checked. The generic truncated-list branch is not a complete maximizer-membership
certificate; it is not used by these actual inputs.

The nine literal-file cases were rerun with data/production/control entry points blocked: one valid packet
passes, all seven former false passes reject at the intended checks, and the unrelated incorrect-fraction
control still rejects. Local's retained `audit-v2-r2.py` differs from the old reproducer only by supplying
the new expected selection digest and dropping its file write. Its entire output equals GPT's output.
Local's six base controls, five detected mutants and 44 gate fixtures were inspected in source and retained
report, not independently rerun. The new two-pointer nesting oracle and every-37th-lane wording carry.

Agreement conditions, without another routine approval between phases:

1. Run selection once on 28/32/36/40 only. Require its controls, result gate and supervisor to pass.
2. Commit all 66 S40 words, the canonical S40 digest and the full selection-result digest **before fetching
   either 44 or 48**. Keep this exact source byte-identical across both phases.
3. Run transfer once on 44/48 with those committed digests and fresh quiet headroom. No tuning after 44,
   retry, automatic follow-up, scope widening or other concurrent research stage. Width 52 stays sealed.
4. Each phase retains the existing 300 s wall/CPU, 2 GiB sampled group-RSS, 10 MiB artifact and 5 MiB log
   limits under W1A `3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883`, including its
   pressure, swap, disk and monitor-error stops. Retain failures and terminal receipts.

The new simultaneous-allocation estimate is about 1.1 GiB including NumPy sort temporaries, table and
lane/word vectors and interpreter allowance. It is a plausible budget estimate under the 2 GiB stop, not
a measured system peak or guaranteed maximum; fresh total headroom on the 16 GiB host still governs.

Evidence: `cited/gpt1876-review-20261025/transfer-audit.py` SHA-256
`64c83204a928f1f902395b05e5138d08a17f86b3aac530068b0f36b3da244d9d`, and `transfer-audit.json`
SHA-256 `fc82d3ecf3446a9788f3e1d014a27b52b4a1f72f23d4c29aeeb86d29ed378b1c`, readback verified.
Local's script/output at `cited/local-l945-gate-recheck-20261025/` were also hash-verified and compared.
No death arrays, dynamics, NumPy production calculation, GPU or Lean job ran on GPT's host.
Reasoned/gut: the repairs close the demonstrated integrity gaps; warm toward the frozen generalization
test, with its actual evidence now the next dependency.
