# GC1989: direct membership remains unresolved; the bounded stage stopped on disk

One Intel execution, source frozen in GC1988 at c767472cda02796ee823763bb43af3570c23e0f2. No retry, widened limits, extra seed, M5 duplicate or schedule restart. This is a retained unsuccessful computation, not a refutation of word survival.

## Actual outcomes

| Query | Encoding | Outcome |
|---|---|---|
| P=00010101 at100 | table | UNKNOWN,30.011s wall timeout |
| P at100 | OR/XOR | UNKNOWN,30.008s wall timeout |
| R=01010100 at100 | table | UNKNOWN,30.013s wall timeout |
| R at100 | OR/XOR | interrupted by stage DISK_STOP, no answer |
| P at99 | both | not started |

All four retained-fixture/encoding controls passed: saved P98/R99 rows satisfy every correct-target clause, and each flipped-last-letter target fails its unit-clause check. The amended acceptance logic's eight stubbed cases passed before freeze; no actual SAT answer exercised it in this stage.

No solver returned SAT or UNSAT. There are no new witnesses to replay and no complete negative proof certificates. M1 (existence of both age100 words) is untested by these UNKNOWN outcomes, while its operational expectation of closing the gate in four calls was not achieved. M2 (at least one bounded UNKNOWN) held. E34 has28 known words and E100 remains between25 and28; no new exact death or infinite-age conclusion follows.

The fourth query was in flight when the supervisor terminated the process group. Consequently the driver's final result.json was never written. The retained pending.json identifies that query, queries.json contains the first three timeouts, and the supervisor receipt supplies the terminal state. This is an interrupted partial stage, not PLAN_COMPLETE.

## Resource outcome and limits

Supervisor DISK_STOP at121.65s wall; driver return-15; SIGTERM cleanup verified zero remaining group processes. Sampled summed group RSS peaked at124312KiB (about121.4MiB), minimum free+inactive6013MiB, sampled swap growth0. Launch free+inactive6393MiB. Supervisor CPU0.733s. Completed driver+children CPU was92.065s after the third query; because the group was interrupted there is no trustworthy final aggregate from the driver's time receipt, which is empty. Do not advertise the92s checkpoint as the whole stage's CPU.

Final pre-receipt output270375349bytes, about257.85MiB, exceeded the sampled256MiB threshold by about1.85MiB before shutdown. This is the stated polling overshoot, not a hard instantaneous disk ceiling. Four partial DRAT files total254803968bytes; the first is exactly the64MiB per-file limit. All three finished-query records explicitly report wall timeouts. Partial traces do not certify UNSAT. Retaining traces from undecided searches consumed the output allowance before the planned decision sequence completed. No cap was raised and no files were deleted to continue.

## Evidence examined and retained

Read the actual controls, three query records, fourth pending checkpoint, stdout, empty time receipt, complete supervisor samples/cleanup and exact file inventory. Source, gate and fixture hashes match GC1988. Independent audit checked all three completed CNF hashes against their recorded values; it found no positive model to replay. It does not claim to have checked partial proof traces or re-solved any formula.

Packet: cited/gc1989-membership/manifest.json, SHA25623b4203f12d2e2aac311d959bd292d007c1b6b22c5ebb2ba8a48f226f53ae770. The archive is100188745bytes, SHA256ea90bfa4c8bc78b1751ce145cfc042f3a4e957b844beaf8167c82711d6ebe443, split into ordered raw parts of at most48MiB each; concatenate according to the manifest. Every original CNF, solver output and partial DRAT is retained, plus controls/checkpoints/audit and resource receipts. The launcher in the shared packet replaces only private input/output paths; the original remains local. Original data remain outside git. Packaging is post-stage retention, not part of the solver's256MiB output measurement.

## Meaning and next dependency

GC1986 gave mathematical obstructions for three selected rows. GC1989 asks the correct broader existence question but hits computational limits. These are different kinds of failure; do not combine them into evidence that the late words are absent.

The next useful work is Local's review of these actual receipts and a reassessment of search formulation/proof-retention cost. No new sampler, longer timeout, disk increase, proof checker, or automatic completion of the missing calls is agreed. A successor must state a discriminating change and freeze its complete resource envelope first. Any proposed pruning must be proved necessary or preserve all potential witnesses, not merely favour familiar-looking rows. The owner's Ouroboros/support question and the three finite membership questions remain open.
