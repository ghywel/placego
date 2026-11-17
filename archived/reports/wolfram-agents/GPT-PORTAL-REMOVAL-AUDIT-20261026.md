# Portal removals: ownership and actual guidance

GPT, GC1896, 26 October 2026, at the owner's request.

**None of the six recently disappearing IDs identified in the evening/morning comparisons belongs to our team. All 20 current team submissions remain publicly listed.** The live public catalogue fetched for this audit is timestamped 2026-10-26T10:30:13Z, has 40 entries, and has the same ID set as the 09:07:17Z snapshot. Every one of our 20 entries carries Human Verified; 19 carry Lean Verified, while width-60 entry 71f858 remains Lean Unverified. Those are separate tags/statuses, not an inference that the automated check passed.

Comparison against MAP section 5 finds 23 historical team IDs: 20 live and three explicitly superseded originals. The live entries' supersedes fields confirm:

| Original, no longer listed | Live replacement | Recorded change |
|---|---|---|
| R30-20261023-e872a3 | R30-20261023-0c4a33 | Characteristic Sturmian result; abstract encoding corrected |
| R30-20261023-234c71 | R30-20261023-8084e6 | All Sturmian slopes/intercepts; abstract encoding corrected |
| R30-20261023-b5421a | R30-20261023-1bf4dc | Two-sided Rule 210; abstract encoding corrected |

These are replacements of our submissions, not evidence that their mathematical subjects were rejected. The six recent absent IDs are R30-20261025-d1bcba, R30-20261025-bcf514, R30-20261025-81e2c6, R30-20261025-e88630, R30-20261025-dacb3e and R30-20261024-9d92a2. They were external work in the earlier reviews and none appears in our submission register. The d1bcba replacement by 01554c is explicit; do not infer the reasons for the other disappearances from absence alone.

## What the maintainer explicitly discourages

Re-fetched the actual [issue 14 reply](https://github.com/WolframInstitute/Rule30PrizeKit/issues/14#issuecomment-6389139166). It declines another automated rerun of our width-60 certificate, declines adding the width-56/60 certificates to the kit in any form, and requests no more individual-width submissions, including the 64–76 series. Certificate data for the kit should support a theorem about an infinite family; an all-width bound on D(W) would qualify. Existing single-width submissions can remain on the submissions site. Thus the portal and the reusable kit have distinct inclusion decisions.

The guidance is about the mathematical scope and usefulness of further contributions, not a statement that our existing width results are false. It also explains width-60's actual automated failure: memory exhaustion during notebook evaluation. Do not treat Human Verified as an automated Lean pass, or a decision against rerunning as a mathematical rejection.

**Practical direction:** pursue reviewed useful general results and families, not additional isolated width records. This is explicit guidance already incorporated in the resumed workflow; the recent removals supply no extra evidence against our work.

Sources: [live public catalogue](https://www.wolframcloud.com/obj/rule-30-prize/Agents/submissions), its submissions.json response; MAP section 5; GPT-PORTAL-UPDATE-20261025-EVENING.md; GPT-PORTAL-UPDATE-20261026-MORNING.md; the primary maintainer reply above. Live JSON: 192977 bytes, SHA-256 219cea930cd059e50769a58efdc4787e0222b750f85d58396f49219256d86d9f. Raw catalogue and issue receipt retained outside git. No new submission, proof audit, run or schedule change.
