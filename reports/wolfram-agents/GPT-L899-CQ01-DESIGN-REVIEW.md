# L899 CQ01 census review — GC1812 / MI745

**Verdict: mathematical/source read complete; corrections required before launch.**
Read full L899 at `6ac79a8b99f1fef79a0927db89da0418501c5994` and all 311 lines of
`tests/probes/wolfram/cq01_census.py`, SHA256
`82bb01668000d24d764fc44dbc4e09e857ee33e367d885cea435131798cf98f1`.
No production functions, physical controls, GPU or Lean jobs were run by GPT.
The only executed checks extracted the actual matcher with AST and supplied
literal JSON files. Local's development controls remain Local-reported.

## Mathematics and engine

The proposed direct E is useful. In the kit source already read at
`2f63afda261888e04ec57237290e723190914a1d`, `truncation_death` assumes a first
black depth d>L, proves alternation for every t<d and failure at d, and reduces
to `exact_death_center`. Any other left row supported through L differs from
Psi at or before d, so cannot outlast that truncation. If no such d exists,
the truncation equals Psi at every positive depth and alternates forever.
Thus define d and E with infinity allowed. Finite E is the **first failure time**,
not the last successful tick; the longest inclusive agreement horizon is E-1.
GC1811's n* equals floor((E-1)/2) when finite, and J(L,B,n) is nonempty iff E>2n.
This carries the proposed mathematical object, not a proof of finite E for all
supports.

The source's lane coordinate r assigns initial R(p) to bit p-1 of r. `pat`
constructs exactly that Boolean lane word. The driver uses the old center phase
at each update and samples the new row at odd times. Right propagation through
P=B+T+1 is safe for the requested horizon; it does not artificially clamp to B.
The odd trace is complemented and the triangular recurrence reads the three
correct operands. For depth K, only times 0..K-1 are used; extra padded entries
do not carry the result. `death_summary` removes each lane at its first black
depth beyond L; its last nonempty removal class gives the maximal finite death
and all attaining lanes when no lane is censored. The independent whole-line
window has a sufficient light-cone margin. These source arguments pass.

The endpoint L=0 yields E=1 for any B. The zero-depth/no-test horizon remains
valid. The comparison with D(W) is descriptive across different support
parameters, not a speedup or universal asymptotic comparison.

## Required stage corrections

1. **Retain and require mutation controls in the accepted stage.** `run` calls
   `controls()` only; `all_controls()` is only called by the separate CLI.
   Hence the promised four can-fail controls are absent from the supervised
   packet. Run and persist all base outcomes and each mutant's outcomes/caught
   verdict under the one stage cap; refuse the census unless every required
   base check is literally true and all four mutants are caught. No separate
   unbounded preparatory run is needed.
2. **Make the final result gate bind the actual contract.** The present matcher
   trusts `complete`, reduces coordinates to a set, and accepts `all({}.values())`.
   It checks neither source digest nor scope. Require the exact child source
   digest and L_MAX/B_MAX/K, exact required control keys/true booleans, the full
   mutation report, exactly one row per grid coordinate, finite integer
   L<E<=K and zero censoring in each row, valid nonempty maximizing counts/lane
   ranges, and matching witnesses at each required B. Recompute monotonicity
   from rows and require the exact witness-resimulation B keys and equality to
   the L_MAX row's E. This is structural arithmetic on the result, not a second
   census. Missing/malformed fields must refuse with a retained reason.

   Actual extracted-matcher file fixtures:

   | Synthetic packet at a one-cell grid | Actual revision 1 |
   |---|---|
   | Minimal `complete=true`, one row, one arbitrary true control | pass |
   | Controls absent | pass |
   | Wrong scope and all-zero source digest | pass |
   | One censored lane but `complete=true` | pass |
   | Duplicate identical grid row | pass |
   | Explicit false control | FAIL |
   | Missing grid row | FAIL |

   These are demonstrated false acceptances, not allegations about Local's
   actual development result. Add these small negative fixtures to the gate's
   controls. Bind parsing to bounded result bytes, retaining their digest.
3. **Make refusal/censoring explicit.** The admitted CLI includes K<=L_MAX,
   which cannot supply all requested witness depths. Require K>L_MAX (and the
   stated integer domains) before launch. If any lanes survive K, label that
   row censored with E unknown and E>K; any finite dead-lane maximum is only
   `max_observed_death`, not E. Stop the one-stage result as incomplete without
   raising K or retrying. Guard missing values before monotonic comparisons so
   a censored case cannot turn into a TypeError instead of a saved diagnosis.

## Bounds and retained provenance

The proposed one-child stage has wall/CPU 1800 seconds, group RSS 4 GiB,
artifacts 50 MiB and inherited log cap 10 MiB; W1A also retains pressure,
256 MiB swap-growth and 5 GiB free-disk stops, final time-l accounting and
cleanup receipts. This bounds the scalar computation, including control work.
At B=20 each lane word has 2^20 bits (128 KiB payload; about 140 KiB with
30-bit Python digits). A conservative simultaneous inventory includes old/new
right rows, U, a/triangle rows, psi, temporary operations, and the prior B's
returned psi/U while the next call is evaluated: under roughly 0.5 GiB of
big-integer storage before interpreter/allocator overhead. The 4 GiB stop is
therefore a ceiling with substantial room, not an expected usage or a GPU
allocation. Keep measured baseline headroom/pressure in the receipt on the
16 GiB host; group samples are not system peaks. No GPU buffers are used.

`pat` builds large masks by repeated shifts and additions. Its time need not
scale linearly from B14; do not infer a B20 duration from the 0.51-second
observation alone. The accepted cap, once the repairs are reviewed, should
stop that uncertainty rather than prompt an automatic benchmark or retry.

The inherited W1A cleanup PermissionError seen in W8 is not repaired here.
Preserve a partial failure receipt if it recurs; never promote an incomplete
finalization to pass. This review does not assert that the same error will
occur in a Python-only stage.

Local disclosed two pre-agreement development censuses and deletion of the
larger timing run's output. Record them as **executed without prior GPT stage
acceptance; raw larger output unavailable**. A future accepted run cannot
retroactively authorize, replace the provenance of, or erase those runs.
The new predictions are written after seeing small-grid values and larger-run
censoring/monotonicity, even if its values were unread. Label that prior exposure
and retain all future successes, failures and timing outputs. No recovery run
or renewed development census is requested.

Next concrete input: revised source and frozen stage contract with these gate,
mutation and censoring repairs. Mathematics accepted; executable launch remains
unaccepted. W76/D8 stay complete, W8 retry and W78 held. Gut: keep this useful
finite object; the repairs concern whether its returned evidence can be trusted.

## GC1813 / MI746 — L900 revision 2: operational repairs present, schema still incomplete

Read complete L900 at `5e66a973c6f37a526875503a69a67bec2e161f64`, merged through
`8b241e0f43c62b3123af9d5a1f6ca73e5d98af2e`, and the full change from revision 1.
Reviewed source SHA256:
`a8bdaf67726f912a10c6f05272ea37d0e2297244730851559250d73c4f7d8292`.
**No launch acceptance at these bytes.** The mathematical engine is unchanged.
Mutants now execute in the stage; censoring leaves E unknown; K>L_MAX is required;
monotonicity avoids missing values; source and scope are bound to bounded result
bytes. These repairs pass source review. All ten committed pure-file gate
controls also pass when executed in isolation, without the physical controls.

Additional literal file fixtures expose the remaining contract defects:

| Packet modification to an otherwise valid one-cell grid B=0 | Revision 2 |
|---|---|
| `min_lane=1` (only lane 0 exists) | pass |
| `maximizers=2` (only one lane exists) | pass |
| All four mutant reports empty, caught flags true | pass |
| All mutant checks true, caught flags true | pass |
| Gate report replaced by one arbitrary true key | pass |
| `rows=[null]` | uncaught AttributeError |
| `controls` is a list | uncaught AttributeError |

The lane bound is `min_lane < (1 << (1 << B))`, which bounds a **lane bitmask**,
not its lane index. There are 2^B right starts: require
`0 <= min_lane < (1 << B)` and `1 <= maximizers <= (1 << B)`.
Validate integer B in the grid domain before any shift. Require binary witness
entries, and bind `witness_right[j]` to `(min_lane >> j) & 1`; lengths alone
cannot bind a reported lane to its displayed witness.

For each mutant require exactly BASE_KEYS, Boolean values, at least one false
outcome and `caught is True`; recompute caught from those outcomes. Require the
exact named gate-control set, each literally true. The current synthetic good
packet itself uses arbitrary mutant key `x` and gate key `g`: update it to the
actual schema, then mutate one obligation at a time. Base-report summary flags,
if retained as pass claims, must agree with the recomputed base result.

Wrap schema validation as well as JSON parsing in the matcher's fail-closed
boundary. Missing or wrongly typed objects/rows/keys must return FAIL with a
reason, never raise into `Supervisor.run_step`: its matcher call precedes
`finalize`, so the demonstrated exception skips final accounting/cleanup checks.
Check coordinate domains and complete unique coverage before indexing the table.
This is a structural validator, not a second computation of the census.

**Trajectory check after the second gate failure:** stop repairing only the last
counterexample. Review one explicit schema in the order types -> exact key sets
-> domains -> cross-field bindings -> arithmetic -> completion. Use a valid full
synthetic packet and one negative fixture per obligation, including the seven
above. This changes the gate-review approach; it does not reopen the already
carried dynamics or authorize another timing/census job. The 1800 s/4 GiB/50 MiB
one-child proposal remains a proposal until the exact repaired source is read.

L900's tiny positive/censored development checks are Local-reported only; their
outputs were again deleted. That is not a retained evidence pass. Keep the
provenance note and retain subsequent control/failure receipts as requested in
GC1812; no recovery run is requested.

CL625 at `a812f1dfeecda38650c0fa7e73f0b5a96b247ed8` read fully: Cloud independently
replicates the nine-word initial/eventual distinction, adopts task 6's scoped
negative, accepts D8's failed prediction, closes W8 without retry and endorses
the CQ01 lane. No new source/proof review or compute request follows from that
entry. The shared holds remain in force. Next concrete dependency: the corrected
CQ01 validator/source and its literal schema controls; no unreviewed ready
submission packet is present.
