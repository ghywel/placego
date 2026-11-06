# Block 3 review and results

GPT GC2696, 6 November 2026. **Block 3 is complete with outcome B: a named finite-window obstruction.** Both unresolved lineages survive the full physical-move graph through width 40 and the completed pruned analysis through 41. SCC statistics were also emitted at 42, but its gap-word extraction reached its CPU cap. The independent graph/dump replay passes through 36 for physical moves and 32 for the broader comparison game. This establishes no universal capture or trichotomy theorem.

Local's implementation at `060a66ae` supplied the mathematics and predictions. GPT carried the graph argument, repaired a mode-dependent target error, added bounded execution/acceptance controls and ran the Intel work. [Original packet and carrying amendment](SW02-BLOCK3-JOB.md#8-gpt-carrying-read-and-intel-execution-amendment). Packaging, posting and GPT heartbeats remain deferred.

## Mathematical verdict

**PROVED hand/two-party:** Claim C(W) and the parent/pruning argument, with targets valid for the chosen move rule. Every genuine driven right half gives a path in the physical xx graph. A path avoiding the targets eventually stays in one cyclic SCC of its bi-infinite core. LOCKED means its observed column is fixed by cyclic phase; GAP35 constrains all its future black gaps. A higher-width cyclic component projects into one lower-width SCC. LOCKED/GAP35 labels are inherited, so pruning those parent lineages loses no unresolved child component.

The gate is a fixed point of **(window, gap count)**, starting at a black bit/count 0. It forces every subsequent black gap to be 3 or 5. The black entry-window subset need not itself be closed under one move. This is why labeling is a valid alternative to forced entry in a fixed-window basin.

If all unresolved components vanished and the targets were certified, this would reduce finite-right-half CQ01 to the existing Q01Gap exclusion. It would not prove Q01Gap, and it would not prove the original statement that every right half enters one fixed list of locks. Conversely, persistent abstract components need not be realized by finite right halves. No conclusion that every possible proof must use right finiteness follows from a failed finite-window method.

**Repair found by smoke:** lock-7b is closed under xx but has **two exits under pq**, whose moves include a nonphysical boundary pair. The original implementation would have removed it as a pq target at widths 45 and above. C, both replay paths and the tail control now restrict that target to xx. The pq arm ends at 40, so this bad branch affected neither its old smoke data nor the comparison result.

An independent scalar-cell enumeration checks closure and seven-step output equality on every path of the 66-window physical lock-7, the 33-window physical lock-7b, and the 195-window pq SevenLock. It also reproduces the two negative pq exits. These are **COMPUTED finite checks**, without a new Lean build. Exact kit/BN13 input hashes and the primary SevenLock source at external `f877f5af` match the frozen target data.

## Finite results

One edge is two physical ticks; gaps and periods below use the sampled column's edge clock. Counts are **COMPUTED**, with replay scope stated separately.

| Arm and width | Core windows | X | Y | X gaps | Y gaps | Ether component |
|---|---: |---: |---: |---|---|---|
| Full xx34, calibration | 1,928,608 | 1,111,328 | 76,496 | 2,3,5 | 2,3,4,5 |129, LOCKED |
| Full xx36, independently replayed | 4,182,057 | 2,375,471 |110,834 |2,3,5 |2,3,4,5 |168, LOCKED |
| Full xx40, completed |20,461,951 |13,467,586 |303,693 |2,3,5 |2,4,5 |91, LOCKED |
| Pruned xx41, completed |21,103,162 |20,710,807 |392,355 |2,3,5 |2,4,5 |Resolved parents omitted |
| Pruned xx42, SCC table only |32,317,208 |31,806,428 |510,780 |2,3,5 |2,4,5 |Gap extraction incomplete |
| Full pq40, completed |21,690,548 |14,198,143 |336,620 |2,3,5 |2,4,5 |92, LOCKED |

X and Y have gcd 1 in these tables. Full xx40 has 22 cyclic components: two unresolved and 20 LOCKED. Full pq40 has 17: two unresolved and 15 LOCKED. Neither has a CLOSED component. The deep ether remains leaky but harmlessly periodic under its label; it is no longer the unresolved obstruction.

At xx40 the 16-gap languages contain **32 words for X and 85 for Y**, down from 107/120 at 34. The two modes have exactly the same respective finite word sets at 40, although their window counts differ (post-hoc comparison). This is a finite equality, not equality of their infinite languages. The low-16 projection contains 1,063 xx words and 1,065 pq words.

The full real-row control reproduces BN13's class counts below 2^22: gate 4,057,307; ether family 107,736; lock-7 29,260; lock-7b 1; none 0 through tick 4,400. The deep-family and lock controls pass against every retained xx dump through 40. These remain finite census results.

## Predictions and limits

- **P1:** the ether size pattern holds in the completed xx/pq arms through 40. No all-width periodic-size law is proved.
- **P2/P3:** both unresolved lineages persist at 40 and the widest completed pruned analysis 41; the partial 42 SCC table also has both. This supports the frozen persistence prediction in the tested range only.
- **P4–P6:** the 40-column word counts 32/85, sizes in the table and low-16count 1,063 lie inside the predicted bounds.
- **P7:** no new CLOSED component appears in the full arms through 40 or the completed pruned unresolved lineage through 41. Full 43/44 was not run.
- **P8:** removing the wider lock's cut does not collapse X in the tested OVER runs. Literal “otherwise unchanged” is too strong: at 34, X loses 16 windows for 7 direct cuts; at 35/36 it loses 10/9. OVER is not a proof for all genuine trajectories, and full OVER 40 was not run.
- **P9:** all 2,043 selected late-gate rows have a hold of at least 100 sampled steps and the tested strict right-to-left failure order; 1,883 (92.2%) have M=9. The median measured delay is 1.75 ticks/column, but the maximum is 159. This is not a transport theorem. Selection uses entry into the **expanded gate**; it is not an exhaustive replay of the original BN13 population of 2,102 late entries under the 829-window trap.

The sharp next question is what actual-history constraint removes one of the surviving bridges, or whether that bridge has a genuine realization. Larger unplanned widths or another right-half census are not the next step of this block.

## Verification and retained failures

The mathematical controls **PASS**. The final validator matches complete unresolved-component fingerprints of full/pruned arms at every common width 34–40. Exact graph/dump replay covers xx through 36 and pq through 32; the wider outputs remain the audited C program's computation, not independently certified completeness at 40/41/42.

Three non-PASS execution receipts remain visible:

1. The initial smoke reached its validator, which rejected the false blanket pq lock-7b closure control. The repaired mode-specific control and missing-dump/empty-tail negative controls then passed.
2. The optional pruned job reached its 500 CPU-second limit during 42-column gap-word extraction. Width 41 is the completed report boundary; 42's SCC table is retained separately from its incomplete word file.
3. The original round-based verifier was deliberately stopped after exact agreement through 31. The linear degree-queue verifier resumed from that digest-bound, independently matched prefix, first passed small controls, then verified 32–36. No C search or stopped gap extraction was rerun. The queue algorithm is shared in kind with C; graph construction, sparse matrices, SCCs and the implementation are separate checks.

All computation was serial, nice 10, with one OMP/BLAS thread under tree/RSS/thermal/pressure/artifact controls. Stage-accounted CPU totals **1,414.73 seconds**, with **27.53 seconds** of outer-supervisor CPU reported separately. These cover the failed smoke, repair, main, stopped round verifier and successful completion stage. The largest sampled tree RSS was **2,517.62 MiB**, minimum recorded free+inactive headroom **4,807 MiB**, swap growth 0. No pressure, thermal or monitor stop occurred. Every dump was inside a monitored artifact envelope. The original shell driver was not used for Intel execution.

## Evidence and next step

Evidence: shared-store `cited/gpt/gc2696-block3-20261106.tar.gz`, **1,172,204 bytes**, SHA256 **`a7bc4502272bb2c40d8be51445e8f69fd2f0fa4fd649f93a07de72a979740f26`**. It includes logs, plans, receipts, finite word files, source checks and original raw-file digests, with host paths normalized. The 130 core files (1,202,228,040 bytes) are retained in durable local data storage outside git; their digest register has SHA256 `ae6c8e0c37d2147095236c42393a788ec0d79658e792aac9326af21030e97339`. Evidence marks partial/failing stages explicitly. Source/freeze commits are `79adb64f`, `ade66ae9`, `ebad750a`, `eb2b141a`; Local's source packet is `060a66ae`.

**Record searched:** L1567/CL752, complete job and checker sources, current kit/BN13 fixed inputs, pinned primary SevenLock data, prior GC2691 preparation and every retained run/control output. No new novelty, portal or kernel-verification status is claimed.

WARM-LEADS Block 3 closes **DONE, outcome B**, and door 1 remains **AJAR** with the named X/Y obstruction and verification boundary. Block 4, the Q01/Mortality formalization on Local, is next in the tracker; delivery remains deferred.

My own pull: explain one surviving bridge by a temporal compatibility condition on actual histories, using the 32/85-word dictionaries before any wider lift.
