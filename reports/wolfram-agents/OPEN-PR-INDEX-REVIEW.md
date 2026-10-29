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
