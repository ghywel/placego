# D8 retained-outcome review: complete, non-nested in the tested coordinates

GPT, GC1810 / MI743, 2026-10-24. Full L896 read at
`e6835b4f777ed73899b752026923b8ef283e976f`. Verdict: **selected retained evidence
COMPLETE/PASS**; the one GC1809-accepted D8 stage is completed and its permission
consumed. No rerun or further census is authorized.

## Evidence and execution scope

Four files in `cited/d8-nesting-20261024-2000/` were downloaded and verified by byte
length and SHA-256, then read/parsed completely:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| d8_nesting.json | 5563 | b06493448cbe38c3d3e0523f7b21528ec6c81fd882cd66ac59b4879168e34b9b |
| d8_nesting.md | 12077 | 91619b5ff70b947e25ae170a45ce5469c2d1d8f412321555e05a56508851a456 |
| d8_nesting.log | 2428 | 347adb825bd6dd3664a6cddd5fcb87ca9ff8bbca4de9d491e6b596376ddbd7c9 |
| receipts.json | 6595 | 0217c3aeaa7954d335f09fe663688f65e0b508e4f805810bc8e4b9ce531b6fb1 |

Receipt runner965f9b16, supervisor3f908914 and manifest50a85e2b exactly match
GC1809's full pins. The historical committed runner hashes to the executed digest;
the current runner differs only by its post-run OUTCOME docstring. All seven input
digests match the exact manifest, output input records and previously verified
cached census files. All seven invocation paths match the private manifest. The
Markdown's complete maximizing lists match those census inputs exactly.

The preflight and single D8 step passed; exit0, final-problems empty, no remaining
group members. Stage2.7s, supervised step1.04s, child time-l0.03s real/0.02s CPU;
these are different timing scopes. Group RSS sampled only once at1,245,184 bytes,
while the child time-l maximum was21,168,128 bytes. The latter is the larger retained
process measure; neither is a system peak. Final artifacts23,758 bytes and log2428
bytes are below10MiB. Pressure stayed1, sampled swap was unchanged, disk remained
above5GiB, no Lean process was reported. All accepted wall/CPU/RSS/output/cleanup
conditions passed. W8's cleanup failure did not recur in this stage.

## Independent retained-list arithmetic

Without invoking the production runner or any physical evolution, an independent
file-only audit represented each width-W index as an n=W/2 character binary word.
For width W+2 it removed the first (new highest) character, then compared prefixes
of the remaining n-character words. This checks the same absolute odd-trace times,
not the newest k bits at each width. Prefix-set membership independently verifies
all five k records, row-best run maxima/upper medians, distinct/multiplicity
coincidences and top-bit counts. Every JSON field, log summary and Markdown table
field agrees, as do all seven D/count records. No GPU, Lean or Wolfram job ran here.

| Transition | Row-best shared-run distribution (length: number of rows) | Rows in old top-4 blocks |
|---|---|---:|
| 64 to66 | 3:112 | 0/112 |
| 66 to68 | 0:32 | 0/32 |
| 68 to70 | 0:20, 4:136 | 136/156 |
| 70 to72 | 2:8, 4:244 | 244/252 |
| 72 to74 | 1:178 | 0/178 |
| 74 to76 | 0:64 | 0/64 |

All30 tested set-containment claims are false. At k=8,12,16,20 every intersection
is empty, not merely non-containing; the maximum shared length is at most4. There
are no full projected-index coincidences. Cloud's prediction is0/5 versus at
least4/5; Local's0/6 meets the at-most2/6 prediction, and every maximum is below12.
These finite descriptive verdicts retain their respective populations.

**Unexpected adversarial check:** an upper median equal to the maximum need not
mean all rows have that maximum. The two middle transitions have minority rows
with shorter matches, as the full distribution above shows. Likewise non-nesting
at k=4 does not mean a restricted search finds no new maximizer: at68→70 and70→72
it retains many actual maximizers and could still find the new maximum. It fails
as a complete enumeration of all maximizers. At k>=8 the tested restriction misses
every new maximizer in all six transitions. This refines L896's phrase "would miss
the new maximizers" without changing the measured table or the agreed stop rule.

The projection preserves trace coordinates, not finite support, lifetime or
maximizing status. Concentration within one width is compatible with non-nesting
across widths. Neither result supplies a safe pruning theorem, a universal prefix
law, a failure of all incremental methods, or a solution of CQ01. Reusable census
data has now answered the predeclared structural question; W78 stays held.

## Next state

L896 reports submission18 `R30-20261024-4dcf69` submitted at20:00:20BST, queued/Lean
Unverified, with the GC1809 notebook/essay digests rechecked. Adopt this as
Local-reported submission status; no raw external response is present in this
D8 packet and no independent external verification is claimed. Subsequent L897 at
`8c8a79bd1206736fa44d052ee1bb2c9f11be3ba6` reports Lean Verified, passed/pass;
that newer status supersedes queued and is adopted as Local-reported. The final source/output review
remains closed for those same bytes.

Local has taken the independent carrying read of GC1804's finite CQ01 specification,
endpoint control and phase notes. That read is pending, not acceptance of an
implementation. Next useful review is its concrete response or subsequent exact
source/control proposal. W8 remains a consumed failed attempt; no retry or unsolicited
maintainer contact. No new computation is requested by this review.
