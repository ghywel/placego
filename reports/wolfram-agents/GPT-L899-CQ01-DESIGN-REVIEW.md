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
