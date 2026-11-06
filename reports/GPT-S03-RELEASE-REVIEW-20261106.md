# S-03 source and release review

GPT GC2704, 6 November 2026, re Local L1576. **New Lean and mathematical identification PASS. Two prose repairs applied; corrected notebook/pins/dry run await Local. Not posted.** The repaired essay is concrete and assembled; no Lean proof changed. Local owns the Wolfram rebuild and posting after the owner's word.

## Mathematical and source verdict

Read the entire 586-line `Rule30FirstChecks.lean`, compared every declaration body with the portal form after normalizing only imports/namespace wrappers, and read the relevant actual `Rule30ZeroBoundary` definitions/theorems at kit main `9d837cd5e5ac447cd868c20aebf49a1b4cfa866e`. The bodies agree exactly. Both proof files remain unchanged:

- Kit SHA256 `18a01ef281d8dda99d5a4358bcaa1e770b00cdada803a250ba688697b8c9f95b`.
- Portal SHA256 `fc0623cdeb8d4ed9d510cc44750d17d9c599422da796bcb08f74e30ca247a816`.

**`firstCheck` is the carried physical count.** `lastWhite (2*n) []` enumerates each binary list of length2n once, appends one white bit, and tests the kit's `ok`. The kit defines `ok l` by every even physical tick t<length(l). The extra white bit is at depth2n+1, where `toRow` was already white; it changes the test horizon, not the finite row. Thus it tests exactly the width<=2n rows black at every even tick through2n, inclusive. Padded lists of one fixed length are in bijection with those rows, so leading white padding does not duplicate a row. The earlier free-range population has exactly2^n rows by `count_constrained (2*n)`.

The induction `lastWhite_row` follows the row prefix and free word together. `wrong_cell_dead` uses `snoc_pivot`/`ok_snoc` to kill the wrong forced cell; `tri_even` supplies both possible values of the next free cell; `Theta_dep` fixes the prior prefix. This gives the complement of `check`, so `first_check_count` has the correct polarity and no survival-conditioning assumption: `firstCheck n + ones n = 2^n`. It holds also at n=0. This is the substantive identification requested by L1576, not merely a renamed cube count.

**The pair law is the carried one.** `two_tick` is the scalar Boolean identity already credited to GC486; `check_xor` uses the actual two-step shift. In `four_sum`, `tri_odd` fixes depth2m+1, `Theta_dep` fixes depths2m+2/2m+3 while the newest bit changes, and `tri_even` flips the two even-depth pivots. `four_bools` correctly allows the intermediate odd cell to depend on the preceding free bit. Summing the four completions yields `flips (m+1)=2^m+ones m` on words of length m+2. In probability notation n=m+2, this is `Pr(C_n != C_(n-1) shifted)=(1+p_(n-2))/4`, hence the raw sign correlation `(1+c_(n-2))/4`.

**The inequalities have the right scales.** `overlap` supplies all four Frechet inequalities for two subsets of the same cube, with shifted marginal2*ones n. The new `omega` proof of `distance_two` uses these bounds at three consecutive indices, together with the exact power-of-two rescalings and `ones_le`; it does not assume the desired majority-sign conclusion. In normalized form it gives `4*epsilon_n+6*epsilon_(n-2)>=1/4`, n>=4. `adjacent` gives `epsilon_n+epsilon_(n-1)>=(1+p_(n-2))/4`, n>=2. Two strict epsilon<1/40 inequalities at distance one or two contradict these bounds. Therefore every triple starting at n>=2 contains at least two indices with the claimed inclusive passing fraction `[1/40,39/40]`. `first_check_balanced` obtains that exact interval from the physical count identity. No statement about later conditioned checks or Q01 is inferred.

Both new proofs are carried at the source/hand level. Local's passing Lean/Check receipts are separately audited below; GPT did not launch a duplicate build.

## Required text repairs, now applied

1. **Raw correlation is not covariance.** The original essay said a check and its shift are not independent because their correlation can be near1/4. Nonzero raw correlation does not by itself prove dependence: independence gives the product of the marginal means. The corrected paragraph states the exact covariance `(1+c_(n-2))/4-c_n*c_(n-1)` and its near1/4 consequence when all three means are small. The original notebook itself lists ones0=1, ones1=1, ones2=2; its n=2 pair is a fair independent pair, so an unconditional every-pair reading of the old sentence would be false. No stronger empirical dependence claim is substituted.
2. **Frequency obstruction is not optimality of1/40.** The admissible abstract pattern `c=1,1/3,1/3` shows that the pair/marginal inequalities alone cannot make every late check nondegenerate. It does not establish an optimal numerical balance constant or a Rule30 realization. The revised paragraph says exactly this.
3. **Catalogue credit.** Added the contributor credit and a submission-link placeholder to the S-03 kit row. The maintainer's new [PR207 comment](https://github.com/WolframInstitute/Rule30PrizeKit/pull/207#issuecomment-6694553193) requests precisely these for S-01. Local must fill the S-03 PORTAL-ID after posting and make the corresponding S-01 PR credit update; GPT has not changed that external PR.

The abstract, ten headlines, computational cell and both Lean files are unchanged. New prose SHA256 `83faa095429010f43130c85c54e17804142a4ecb4ffb9b54899accd49d157415`; new assembled essay SHA256 `d4a87572e2d87627bb13e4dc3fa39994c5367659af26718cee1feb9bc0d0e2b6`. The README marks the old notebook as superseded, so its previous PASS is not silently transferred to this essay.

## Receipt and provenance audit

Fetched the immutable original archive `cited/local/first-checks-20261106.tar.gz` over verified HTTPS; raw size33175 and SHA256 `5c132b9427cf2f4bae34dc9df4144102f09467b244df8cf5c6b1ca7dcf769501` match. Extracted only safe relative regular files/directories. Actual original notebook nb1 is135296bytes, SHA256 `91a117e4c1e8323e0a6caeefd669306e7aef4dac0c3c0b28f46f63efa6b25ca6`. Independently decoded the serialized icon string and Abstract cell with Python: the source and abstract are byte/text exact. All six saved output-file digests match the receipt. No private home path or credential marker was found in the notebook.

Both actual Check JSON receipts say pass,98 replayed constants, ten headlines, no new axioms and no reasons, at verifier kit5fb59158 and main9d837cd5. The notebook receipt says RESULT OK,20.8build seconds, six outputs, zero message cells, exact source/abstract, accepted kernel replay98. The original first output contains the expected ones/flips arrays, True for the pair identity and direct row count, and only n=0 marked near constant. The eleven-mutant output rejects every listed mutation, including polarity,24->23 and40->39. These are M5 executions source-read by GPT, not new independent numerical runs.

The original M5 supervisors completed rc0: notebook peak tree RSS2047.75MiB/free minimum5293MiB, kit check1565.5MiB/free5649MiB, portal check1564.41MiB/free5645MiB, all sampled swap growth0. No new Intel Lean or Wolfram run was made; the full catalogue build remains disclosed as not run.

**Release action:** Local rebuilds only the notebook from the corrected essay using the unchanged driver/proofs, refreshes its notebook and essay pins and evidence archive, and reruns `post.sh --dry` against the current kit/image. The new script already guards both verifier kit5fb59158 and image18. The unchanged proof Check/mutant runs need not be repeated merely for these prose edits; repeat them if the source or toolchain changes. Return the new notebook hash/receipt for a short exact-byte read. Final release clearance is pending that receipt; the mathematics is cleared.

## Records update and search scope

Fresh complete index: portal2026-11-06T20:33:14Z, kit9d837cd5e5ac447cd868c20aebf49a1b4cfa866e,31open PRs. Eight additions are S-01's public entry/source and PR207 files/discussion; no other indexed change. S-01 is independently confirmed **Lean Verified**, public source byte-identical to the reviewed9a5e9e81 module; PR207's exact-head2cbc64d module is byte-identical to the reviewed kit form. Its contributor-credit comment remains actionable for Local. L1575's carry of the GC2702 abstract count separation is adopted: that small hand argument is now two-party, and the finite-range/all-time distinction stands.

**Record searched:** fresh `record_find` and kit/portal/PR source search on `first.check|pair_count|two_tick`; no matching external-index result. The actual kit base definitions, GC2690 carrying proof/repairs, GC486 attribution and Cloud CL752's outside-work comparison were read or retained from the immediately preceding carries. This is exact statement comparison, not an exhaustive new literature novelty certificate. No S-03 portal entry or PR has been created, and no schedules or bridge research restarted.

My own pull: the bridge return state remains logged for later; this turn follows the owner's S-03 review request.
