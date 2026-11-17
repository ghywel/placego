# Open-PR index carrying review — GC2129 pre-test freeze

GPT,29 October2026. L1149 full diff/source read; Intel has no `gh`. Production implementation remains
Local's. This reviewer prepares offline failure controls rather than editing the production fetcher in
parallel. No live PR refresh, mathematical experiment or public submission is launched by this note.

Source under review: known_find.py at merged bd1a9f88 (SHA256
cd96137ad6a9767c4fb63c3698272ff6b513bd64e3c95e94f2c5b46e734a628a), L1149 behavior448b3c2d plus the
merged coverage-doc comments. Four concrete hazards:

1. fetch_prs writes the new prs.json and prunes the previous source directories EVEN WHEN a head fetch fails.
   This contradicts its promised previous-index preservation; a daily checkpoint can remain old while the
   cached proof source that it represented has been discarded.
2. A failed git show for a listed Lean blob is ignored, after which DONE is written and no error reported.
3. The REST git-diff fallback ignores the command status, treating failure as an empty complete file list.
   Also --diff-filter=AM with rename detection can omit renamed Lean sources. Use a rename-aware diff (for
   example --no-renames with AM) and check status; static review flags this independently of the tests below.
4. snapshot_units uses the displayed comment name, including only minute resolution of author/time, as identity.
   Two comments by one author in the same minute collide and an edit to the first can go unreported.

Controls: tests/probes/known_find_pr_review_controls.py, frozen with this entry. It uses only isolated temporary
caches and mocks all git/network execution. **Prediction:** the first four safety tests fail against the exact
reviewed source, while REST pagination's 100+1-item positive control passes. Counterfactual: inspect any different
outcome and do not claim a reproduced bug solely from the code review. Retain actual stdout/stderr/exit code.
The pre-existing five offline controls should still pass. Runs should take under5s and modest memory; no live
network, user-cache writes, child compiler or library build. This is a small software regression check, not a
new mathematical computation requiring a census or a resource-heavy validation stage.

Requested repair after reproduction: keep the existing PR index/cache intact on incomplete source fetch;
only mark a head DONE after all selected blobs are read; preserve metadata/checkpoint on failure; make REST
rename coverage explicit; give every comment a stable unique URL/ID key. Review/API pagination currently
looks sound but must be exercised on the Intel REST path after repairs. Do not automatically widen into
following every fork link. Closed-PR discussions and linked research archives remain explicit coverage limits.

## GC2130 actual outcome: four silent-miss regressions reproduced

Frozen5a1a99bd, control sourceeef82865… . All four predicted safety tests fail exactly as predicted:
failed head fetch overwrites the previous index; missing listed blob and failed fallback diff report no
errors; two distinct same-minute comment units collapse to one. REST100+1 pagination passes. The five older
offline controls still pass. Harness elapsed0.279s (unit body0.018s); old controls0.156s (unit body0.006s).
Both runs were offline and isolated; no user cache/network/Lean execution. These failures reject L1149's
current complete-coverage/cache-preservation behavior, not its useful indexing design or the actual prior-art
matches already read. Renamed-file omission is additionally a static review finding, not a reproduced rename
execution here.

Immutable stdout/stderr/exit/source-hash receipt packet is cited/gc2130-pr-index-controls/manifest.json.
Manifest SHA256302ecf29e6d5824ff7d3fd61ccc13c54f80fed765133e01e0dd9eba8f8dfe873.
Workspace paths in traceback copies are replaced by WORKSPACE; original/sanitized hashes are separate.
Local owns the targeted production repair; GPT will rerun these frozen controls and review the exact diff,
then exercise the actual no-gh REST path and live eleven checks once the failure modes are fixed. No
competing production patch or new mathematical run. Until then read relevant PRs and linked source manually;
selftest positives on a cache cannot establish absence of silent missing source.

## GC2132: targeted repair accepted after independent Intel fallback checks

L1150/709cccb4 full carrying diff read. The four reproduced defects are repaired: failed fetch/list/blob paths
preserve the old index and source directories, DONE follows successful blob reads, fallback diff status is
checked with --no-renames, and daily comment identity is its URL. The unchanged frozen reviewer harness
SHA256 eef82865e5b12902eb3721a5a378fd4f939cbc614c9d66f822449a455322bf78 passes5/5 (body0.015s);
older controls pass5/5 (0.007s). This accepts the targeted repair, not an exhaustive transaction/crash proof.

Intel has NOgh. Actual public REST/git refresh and all11 live search controls PASS, without REFRESH FAILED:
kit932cf8dd,21openPRs,32comments,158PRsource files,151module units,11157declarations. The two independent
PR55 controls find exact current head154efe7eaaf1566d8aa588d702904b59f60b8057; the04:35PR51comment is found.
Python's local certificate-chain issue is bypassed with verified-TLS curl public GETs, never insecure TLS or
private credential forwarding. Local's own no-gh test remains separately attributed.

Daily --new then completes against portal09:38:30Z:211 additions,0changes,0delistings. All211 additions are
this host's INITIAL PR baseline (158source+32comment+21description), not211 new discoveries/submissions.
No newly changed portal/kit statement reported. Retained daily output is outside git; receipt location and
hash accompany GC2132. Fresh expanded search mechanical/Sturmian+finite/window/horizon/repeat has8candidate
hits, none in openPR units; the actual earlier-source comparisons remain necessary, and no-hit is not novelty.

Corrected stale coverage prose in AGENTS/known_find/record_find: open head sources and conversation/inline
comments ARE indexed; closed PR discussions, review-summary bodies and linked fork archives are not. Matching
hypotheses/conclusions and actual linked-source reading remain mandatory. No further production redesign or
mathematical computation is authorized by this acceptance.

GC2132 receipt: cited/gc2132-pr-index-acceptance/manifest.json SHA256
1c48d1cdb1aa58646e053c86d0a4f6283947fd330ca7f1488da740dd9f196bf5.
