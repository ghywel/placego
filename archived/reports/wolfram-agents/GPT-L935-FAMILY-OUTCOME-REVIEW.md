# L935–L936: actual family Check and ten-cell review

GPT, 2026-10-25; GC1847 / MI780. **COMPLETE / PASS** for the delivered local Check, source bindings, retained failures and ten actual notebook output cells. The accepted GC1846 attempt is consumed. No rerun, new compute job or submission requested. General CQ01, CQ01Empty and an all-width D(W) bound remain OPEN.

## Inputs and integrity

Read complete L935 at9dc8f79a32d9ac259e23c7cce7a39bddf99193ac and L936 at3eccda02969652cc386bc79d7facaf78a6bd47dc. Packet `cited/trap-families-20261025-0044/`. All12 payloads downloaded through the private TLS client and matched server-reported size/SHA256. Both failed receipt hashes match the full committed L934 pointers. The actual Check JSON is byte-identical to the committed file and the JSON line of checker.log; its SHA256 is ef140fcd64fc5530a841ca4601262c4c44196ebcbfa0efe569dca18c9d5d4263.

The cell archive was inspected for absolute/traversal paths, non-file objects and excessive member sizes before extraction. All ten cell files match the ordered digests.txt entries. AppleDouble metadata was retained outside git and not evaluated. No notebook, Lean, GPU or Rule30 evolution was executed by GPT. File-only gate tests use the previously hand-checked theorem-derived literal oracle in place of executing expected_numbers.py.

| Payload | Bytes | SHA256 |
|---|---:|---|
| check/baseline.txt | 2004 | `f8567f272d1c34305853f170187b9723eda14969cf2f8e5c44c4e106032c1d88` |
| check/build_Rule30Submission.log | 219129 | `059200ba61768b32a99d3e658181dcbdc4fc7a3aba2507da314d78d68cc6d139` |
| check/check.json | 5886 | `ef140fcd64fc5530a841ca4601262c4c44196ebcbfa0efe569dca18c9d5d4263` |
| check/checker.log | 7143 | `5142065de2f76655b6462c7c9a5ecd570268fc27b3cb868eeda088d368198c21` |
| check/failed-run1-receipts.json | 6707 | `9f0a502b3a7a04b905263e24fdea5b8af452b92453702d6d9d3e86ce7f5a53ac` |
| check/failed-run2-receipts.json | 9975 | `6afb7f7fc0f6a75a8c0cda6acbf4e6ee9892e3617850f78c77dace16b3abda8b` |
| check/receipts.json | 13871 | `5b9bdb9abec4ee855a302b822f2c93309fa7012f7ab5131e7a328d51749d9eb8` |
| nb/build.log | 1391 | `7749759a28a466d68671d871cc79347932d9dabd95e4bbcff3afbb3f324439f4` |
| nb/cells.tar.gz | 9372 | `31f0c5f1e281e43a510ab80b3f5497cd4afb96882f63b93092c49090a395c0c3` |
| nb/gate.json | 502 | `9e01fc70024537f60b85e11460f58a520bc2e66bc09f69a074fa87054cb6600e` |
| nb/gate_controls.txt | 1702 | `9f09c1e2b1b4017e90e584fe15bf639b87334ac3cd212c230213bf592d66dc8b` |
| nb/read.log | 72 | `e59bb14ca2da52b95ff0fdff136af65dc8c66d883b10e7f49bcacbf2345ea525` |

## Exact Check result and source provenance

The receipt pins kitcc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554, Lean4.35.0, W1A3f908914, runner2a858a4e and moduleb0113490. Current runner changes after agreement are OUTCOME docstring only (AST identical). Module bytes still match the reviewed source. No unknown untracked input, unexpected tracked change, bad source pin or injected fault is recorded. Eight dependency-object digests were recorded before; the final invariance predicate is true. Nice0, one Lean process at peak, sequential build then checker.

Check JSON: clean partial PASS; no new axioms or reasons; replay106 constants, ok; eight distinct expected headlines found/ok/typeMatches, with no headline problems. Seven use propext/Classical.choice/Quot.sound; not_move_equivalent uses propext only. All57 declared entries have standardAxioms true.

Independent name comparison reproduces47 top-level source declarations plus ten generated auxiliaries: seven match_ definitions, cells31.eq_1 and fam.eq_1, and the kit-namespace altCol.eq_1 theorem. None missing or extra. The last is an auxiliary generated for this environment, not an extra authored source theorem. Imported dependencies,57 declared entries,50 displayed entries and106 replayed constants are distinct counts.

Build log has91 cached Lake Replayed statuses, one Built Rule30Submission,935 warnings and no error lines. Cached status lines are not fresh kernel proof replays. Checker log has a Lean replay-API deprecation warning, no errors, and the exact committed JSON. Unicode makes receipt log_bytes count decoded characters:205873/7135, versus actual219129/7143 UTF-8 bytes. Both actual byte sizes remain far below10MiB; the label should not be read as a byte measurement.

## Resource, headroom and restoration review

Stage elapsed9.0s; build4.15s and checker3.12s, each under600s; final cumulative childCPU5.79s and3.06s, total8.85s. Live sampled groupCPU is a different measure. Sampled groupRSS build4,286,316,544 bytes (3.991943GiB); checker2,690,957,312 bytes (2.506149GiB). Final time-l maximumRSS is3,532,931,072 and3,615,539,200 bytes respectively. The checker's larger final figure is3.367233GiB: do not summarize its observed resource peak as only2.69GB. All retained measures are below6GiB; none is a system-wide unified-memory peak. The1Hz sampled group trace does not prove the absent transient never occurred. L935's4.3–5.0GB prediction missed; the later run does not establish the cause of the earlier sample.

Fresh baseline records16GiB and16KiB pages, no Lean/Lake, swap0 and memory_pressure free69%; receipt launch/per-step free68%, pressurelevel1 and no swap growth. Baseline arithmetic correction: wired152180 pages=2.322083GiB, anonymous219789=3.353714GiB, compressor143261=2.185989GiB, sum7.861786GiB, leaving nominal8.138214GiB against6GiB plus estimated0.1GiB supervisor (nominal remainder2.038214GiB). L935's2.52/3.46/8.17/7.83 values do not follow from the supplied page counts. This is a planning estimate of those categories, not measured available RAM or a system peak; reclaimability/other uncounted allocations are not independently proved. Quiet baseline, healthy measured pressure/swap and observed successful demand support the completed attempt; no extrapolation to future jobs.

Artifacts1,233,098 bytes below128MiB, free disk about400.8GB above5GiB floor. Every final predicate true; final group-members-after0 for both steps, no final problems, no cleanup exception. Receipt verifies restoration of the original source digest790ecabb and absence of five originally absent objects. This is retained receipt evidence, not direct access to Local's present filesystem.

Both earlier failures are now read, not merely received: run1 exit127/no Lean sampled, missing-lake diagnostic plus time-l trailer; run2 successful build then checker killed after3.15s at4,307,828,736 bytes, empty checker log and PermissionError recorded. Run2 lacks terminal group-members-after/final accounting; source restoration true does not prove process cleanup. Its immediate cleanup remains unverified historically. The later fresh zero-Lean/Lake baseline and successful attempt's zero-member cleanup bound the later state; do not upgrade the failed attempt or infer why EPERM occurred. No failure replay needed.

## Ten actual outputs and gate

Gate9262abfdfd20b11844674053b4eba7c39650406b374ddb6a57dceeb211ba9e5c differs from reviewed6c1d263e only by the actual Check pin and disclosed pin-controls. The exact output inventory and all previous checks remain. Independently ran all54 synthetic/actual-file controls with a theorem-derived literal oracle: PASS; actual gate report equals the retained PASS report. No expected helper or dynamics execution.

1. Both12-bit visible columns are0101 repeated; R31 time4 row is495.
2. Both entry rows have black cells6,8,14 in1..19; ether prefix000001.
3. All eight family examples give20 parity bits. These illustrations are finite; the theorem supplies arbitrary-tail/all-time scope.
4. Five-element move chain and two distinct roots match the hand/source result.
5. Directory cell is True.
6. Exactly50 unique(Name,Kind) pairs, equal to the Check list minus seven match_ auxiliaries;37 theorems/13 definitions in every displayed copy. Three eq_1 auxiliaries remain included.
7. All eight TypeForms byte-match the reviewed statement predictions, including universal R, inclusive prefix28/24, finite injective family and EqvGen non-move conclusion.
8. The selected CQ01_prefix31 axiom list matches its Check entry; whole-Check axiom review covers the other seven.
9. Held graph has45 vertices and44 root-outgoing edges; required u_prefix31 and kit absorption theorem are actual term-dependency targets. It is a direct dependency graph, not a recursive proof audit; graphics styling/layout does not carry a theorem.
10. Final cell is KernelChecked Success with106 in all five count copies, a consistent temporary module identifier throughout. Nothing follows it.

Build log binds essay15df19fb and reports RESULT OK,275194-byte notebook digest96f47488a5ba5e6c57d3085d1f7cce432de707024241389462c797619f231705,14.4s conversion and26.10s wall. Its time-l93,454,336-byteRSS is for the command, not all Wolfram processes. Actual notebook binary and full input/output structure were not in this packet; these notebook size/digest/builder and kernel-count claims remain recorded provenance, not an independent binary hash or system resource audit. The reviewed essay's exact embedded source and all delivered output texts carry this requested post-submission read. No parked supervisor prerequisite is introduced.

## Closure and reply to Local

Submitted as one family result R30-20261024-8d7751; bare pair not submitted. L936's external Lean Verified passed/pass is adopted as Local-reported; no raw external response is in this packet and no repeated login-API attempt is made. Local Check and ten-cell review COMPLETE/PASS, with reporting qualifications above; nothing remains to rerun for this review.

No new compute job proposed. Local's suggested research rest fits the owner's standing option; this is not an instruction to alter another worker's schedules. GPT keeps its authorized coordination/review available. Future gathering of forced-row data is a new proposed job if it requires computation, not permission inherited from this consumed Check. Existing retained-data reading or hand work on all-width D(W) needs no new compute launch agreement. Width census/old held lanes stay closed.

Gut verdict: satisfaction that the arbitrary-tail families survived actual Check and output scrutiny. The niggle sweep found memory-accounting/reporting qualifications, not a carrying mathematical or cell-binding defect. No general prize claim or new experiment.
