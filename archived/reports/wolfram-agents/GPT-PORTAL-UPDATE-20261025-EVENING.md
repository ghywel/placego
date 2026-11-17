# Evening review of new Wolfram portal material

GPT, GC1884 / MI816. Owner-requested one-off review, 2026-10-25.

**No new result presently removes our obstruction.** One replacement submission
corrects prose without changing its proof. A substantive kit update makes an
existing stripe-tail argument reusable through a general return-map theorem.
That is useful proof infrastructure, but it still assumes the successful white
witnesses that a general extinction argument would have to supply.

## Live catalogue comparison

The [public catalogue](https://www.wolframcloud.com/obj/rule-30-prize/Agents/submissions)
was fetched directly, with embedded data updated **18:59:03Z, 25 October 2026**.
It lists **41 entries: 40 Lean Verified and one Lean Unverified**, compared with
45 in the retained 12:27:47Z snapshot. The search-engine result was stale and was
not used to decide what was new.

There is one added ID, **R30-20261025-01554c**, replacing d1bcba. The other 40
retained entries have unchanged entry objects. Five former IDs are absent:
d1bcba, bcf514, 81e2c6, e88630 and dacb3e. Only d1bcba has an explicit
replacement relationship in this delta. Absence does not establish rejection,
withdrawal, supersession or a mathematical reason for the other removals.

## The replacement changes explanation rather than mathematics

[01554c](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261025-01554c),
by Emerson Villafuerte with Antigravity, retains the title about diagonal-defect
spectra, sublinear run bounds and semigroup saturation. Its external receipt
reports 735 replayed constants and 20 selected accepted headlines, checked
17:18:21Z against kit 3eca23c; no Human Verified tag or verified official prize
target is present. The abstract's 88 headlines is a different count.

The actual [Lean source](https://www.wolframcloud.com/obj/rule-30-prize/Agents/api/file?id=R30-20261025-01554c&kind=lean)
is 158547 bytes, SHA256
`d19dfbce3625a2ab7ab72c5e92cb151af8c0a32427ee5e62a96c6507eae0a181`.
Every byte outside one complete documentation comment equals the previously
reviewed d1bcba source, SHA256
`7473bbaa2a9ce9520a7ca0da45091efae79c6f1481033db20d540c56f4a4f35e`.
The changed comment correctly identifies `white_run_le_diag5` as conditional on
the spatial `preRow` hypothesis, not an unconditional centre white-run bound.

The earlier [carrying review](GPT-D1BCBA-DIAGONAL-REVIEW.md) therefore still
applies. The fixed-diagonal bounds remain linear in the starting time, despite
the title's word "sublinear". Their single-seed consecutive-run hypotheses do
not become the arbitrary-row, even-time survival hypotheses of Q01. No new proof
was added by this replacement.

## The kit now has a reusable return-map mechanism

The advertised verifier changed from image 7 at 3eca23c to image 8 at
**0090056412733accaa27643d3cbbf982104f2251**. Its three added modules are
`Rule30ZeroBoundaryStripeFrontLift`, `StripeTail13Completion` and
`Rule30ZeroBoundaryStripeFourComplete`. The GitHub comparison contains one
commit, merging PR16. This change is separate from the new submission's earlier
check receipt.

Read all 883 lines of the three added modules, including the complete generic
[lifting proof](https://github.com/WolframInstitute/Rule30PrizeKit/blob/0090056412733accaa27643d3cbbf982104f2251/lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryStripeFrontLift.lean).
The construction reuses successful tests from a smaller moving-front window,
then checks the exceptional residues in a larger window. Instead of checking
every point of the larger orbit separately, a finite return map records the
upper bits whenever the lower window completes a circuit.

In this instance the lower window has width 34, period 65536, and one missing
residue, 61005. Thirty-two upper return states give a width-46 cycle of period
2097152. The exceptional witness is checked for each of those 32 states. The
parallel lane proof explicitly transfers each packed update to the actual
front-window dynamics, including its phase. Low-window projection preserves
the previously successful observations; it does not assert fresh witnesses.

The [completed family theorem](https://github.com/WolframInstitute/Rule30PrizeKit/blob/0090056412733accaa27643d3cbbf982104f2251/lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryStripeFourComplete.lean)
handles every stripe-prefix length and every four-cell tail, including odd
prefix/tail13. Death occurs at an even time at most d-1+45, with first deviation
d at most m+6. The large certificate period is not a physical delay of two
million steps. This family, including a five-cell extension, was already in
the source-reviewed 017d83 submission; see the
[previous stripe-tail review](GPT-PERIOD4-AND-STRIPE-TAIL-REVIEW.md). The new kit
offers a general interface for that technique, rather than a new all-input
coverage theorem.

## What can and cannot be imported

`universal_front_period` proves every n-bit front window returns after 2^n
steps. It does **not** prove that the window exposes a white observation.
`return_map_cycle_lift` still requires the return-map cycle and all exceptional
white witnesses as hypotheses. Finite recurrence alone does not discharge them.

Unexpected hand control using the actual front definitions: at width 2 the
front states and phases starting at (3,0) are

    (3,0) -> (0,1) -> (1,0) -> (2,1) -> (3,0).

There is a genuine first-bit defect relative to the even-depth stripe. Yet
`Cycle 2 1 3 0 4` fails: at required residue 3, `sig 2 3 2` is false. The first
observation is at odd time; one ordinary packed step sends 2 to 7, whose first
bit is black at the next even time. Thus even an actual defect plus a return
cycle does not automatically supply the bounded witness test. This does not
refute a larger window or a longer witness budget.

**Disposition:** retain the generic lifting theorem as a way to compress a
specified certificate with a small exceptional set. There is no identified
arbitrary-tail invariant or argument that all exceptional residues eventually
obtain witnesses. No new experiment is warranted merely by its availability.
The missing general finite-tail coverage, all-width D(W) bound and amplification
construction remain missing.

## Evidence scope

This was a source/hand review and pure-file comparison, with no Lean replay or
dynamics execution. The certificate declarations are accepted-kit source, not
newly kernel-checked by GPT. Imported front definitions and `Cycle` semantics
were reread from the prior pinned source; the comparison confirms that module
is unchanged. An initial file-audit assertion used incorrect hard-coded line
indices and failed; comparison at exact comment delimiters then verified byte
identity outside the single changed comment.

Snapshot SHA256: HTML
`0d75e52d7b78ebed9155df6fd0c734bc15e786b0222b3d4bcb8dbddb972769b7`;
extracted/indented JSON
`4efd8e4cb3f09236450269ea91401ace7c00a80fe4a23891b20cc0f2bd8f6780`.
CL638 was fetched and read in full during refresh; the amplification lead stays
parked. No public write, worker wakeup, new job or schedule change. The third
halt remains after this completed owner request.
