# Right-wall submission and proposed kit PR: review

5 November 2026, GC2684. Re Local L1548–L1549, package at `a33d3942`; subsequent shared-main changes through `c730e439` do not alter it. Owner-requested economical review. GPT read the carrying sources, checked the release receipts and replayed the finite certificates in plain Python. GPT subagent inspections are self-checks, not additional independent workers' reads.

**Verdict: the mathematics and corrected submission/PR texts are cleared.** No theorem or proof body needed repair. The corrections supply missing guards and narrow several prose claims. Local must rebuild the notebook on the revised essay and pass the exact-source release gates below. This is review of the proposed PR package, not a posted PR head or a new external verification result. Nothing was posted by GPT.

## Answers to the eight questions

1. **Every predecessor, forever, arbitrary lower completion: yes, with the stated guards.** The inverse is two-sided; `previousN` supplies an actual predecessor at every age and preserves the anchored black cell. `Closed` checks all four lower pairs, including the alternating continuation, and `held_forever` transports the window to `L + 3n`. It requires `L ≥ 2`. Nonperiodicity also requires width at least two and an equal pair at the end of every window. If a held row had positive period P, its own alternating tail would contain the equal pair transported by 3P, a contradiction. These hypotheses are satisfied by the front, letters, locks and cloud. They are now explicit in the essay and PR summary.

2. **Periodic classification: the implication is sound, the converse is not supplied.** A periodic orbit cannot meet the guarded front. Universal backward capture of every *other* anchored rain-tailed row would therefore prove that only the rain pair is periodic. It is a sufficient route, not an equivalence. `1010…` has no equal pair; `11010…` has its last equal pair at index zero. The original header's assertion that neither has a wall was false and is corrected. The open capture question now excludes this pair. The local wall rule retains `D ≥ 5`; for `deep_words` the shallowest of the four walls must have depth at least five. Infinite letter histories decompose into BA/BAA after a possible initial A or AA; finite words may end in a partial block.

3. **Reset credit: corrected and sufficient for the reviewed scope.** Lowry's `Rule30InverseCascade.run_resets` is the precise antecedent for synchronization by `0 1^(3m+1) 0` together with the following cell. `Rule30ResetFreeRuns.AvoidReset` records that family; `Rule30ResetFreeCore` supplies the graph framework. The new `Reset.again` is a finite identity on `F(b,u,v) ++ [s,!s,s]`, valid for both lower input bits, returning another F shape after dropping three cells. No matching identity was found in the sources below. That is bounded prior-art clearance, not a claim to have excluded every possible antecedent.

4. **No floor and moving merges: now separated.** `LockThird.no_floor` means: for every offset `0 ≤ d < 164`, some one of the forty 175-cell windows lacks every F(b,u,v) at d. It does not exclude all synchronizing words, a floor outside those windows, or a fixed F location along each individual orbit. The sentence about lower states merging at changing positions is explicitly COMPUTED; it is not a corollary of `no_floor`.

5. **Entry witness: yes, while staying in the coarse cloud.** `Entry.entry` certifies the forward-indexed row at k=97 in Q45, k=7 outside the third lock at the tested wall, and k=6 inside. Read backward, cloud closure gives membership at every k≤97 and lock closure gives membership at every k≤6. The two windows end at the same wall: their starting indices differ by 175−45=130. Thus entry into the third lock is not exit from Q45. The finite tail check at k=110 joins the infinite-tail bound at cell 789; no unverified gap is used. GPT's Python replay confirms the finite witness.

6. **Surrogate statuses: acceptable.** Section 9 reports no detected third-lock capture in approximately 1.2·10^11 ticks under independent fair lower inputs, with no rate or mean-wait claim. It does not transfer that artificial input law to physical rows or exclude every unknown lock. GC2683's statistical qualifications remain in force.

7. **Title and abstract: cleared after correction.** Permanent letters concern the three locks; nonperiodicity concerns held rows with the specified wall and rain conditions. The cloud rank lies between 1 and 17 and strictly decreases whenever the letter changes, ruling out seventeen successive changes; it need not equal the longest alternating run. The abstract now distinguishes the reported 13-second module compilation from the separate checker replay of 625 constants. The third lock has six certified phase classes carrying BAABAA; this repeats AAB in its letters, up to cyclic phase. No prize claim is made.

8. **Kit data policy: the package has a defensible fit.** The certificates serve infinite families: every allowed starting index, every lower completion, and every backward time. The generic `held_forever` theorem and numeric-to-word bridge establish soundness. This is more than a list of trajectories. `Rule30GateTrap` is credited for the closed-window method; its forward fixed-boundary checker does not directly implement this inverse moving-window setting. Local's largest reported module is 10 seconds and 2.7 GB. The added [integration patch](wolfram-agents/submissions/right-wall/kit-integration.patch) supplies umbrella imports, a catalog entry and the shared-namespace note, and applies cleanly to kit `c63cde84`. Actual integration validation remains a release step; the whole catalog has not been built for this package.

## Prior-art and evidence boundary

The complete `known_find.py --new` refresh succeeded at **2026-11-05 17:15:39.593891 UTC**, kit `c63cde84a0595aa5ee2a04dc14618a90eabaf2f7`, portal updated 17:15:15Z, thirteen open PRs. Current kit `lean/`, `equivalents/` and catalogs were searched. Relevant reset, boundary, stripe-cascade, GateTrap and EdgeStaircases statements were read. The refresh's unrelated new portal/kit entries are indexed, not all mathematically carried in this review.

Separately read [PR 60](https://github.com/WolframInstitute/Rule30PrizeKit/pull/60), its two issue comments, empty review/inline lists, and [the exact head source](https://github.com/Troyusrex2/Rule30PrizeKit/blob/db6e71128339d1fc45b5a7ab5f2bade997996ae3/lean/Ruliology/CellularAutomata/Rule30InverseCascade.lean). Its linked research archive at `3ebd1501497f168c04b3b0fab00595b1266f5a00` was read including review, update, provenance and proof guards; the module matches the PR head, sha256 `1d97523e4fd7d9315744852d4c34322846a422459aabd48e69b970f4512c203a`. The relevant inverse-run and carrier sources at PR 47 head `744c1091c0dcbd2885c729c89fad2e6928e436b0` were also inspected. Coven–Pivato–Yassawi's [primary paper](https://arxiv.org/pdf/math/0511030), Theorems 1 and 4, supplies general odometer context, not this precise wall-return identity. The essay's attribution is narrowed accordingly.

Local's M5 receipts report Lean 4.35.0 checks: portal at verifier kit `722a0c51`, 625 constants and 36 headlines; kit modules at `72253aea`, 433/66/126 constants and 18/12/6 headlines. Ten deliberate mutations were rejected. GPT independently reran the plain-Python literal replay: **3,392 image checks, phases, letters, ranks, reset depths and entry witness passed**. Portal generation and embedded-source byte equality were checked. No Intel Lean build or Wolfram execution was performed.

GPT read the actual archived notebook gate/output receipt, not the notebook itself: `cited/l1549-right-wall/nb2-receipts.tar.gz`, 11,681 bytes, sha256 `32fcfcb74692b1031597fd5aad8880576daa74cf5d42036ae41e1e9a8b4f7455`. It records eight Output cells, zero Message cells, correct iconized source, 111 letters, and KernelChecked 625 for the **old** essay `4d76bd72…`. Its notebook hash `f607c46d…` is historical and does not certify the revised prose. This review does not claim fresh public Lean Verified/Human Verified status.

The review archive is `cited/gpt/gc2684-right-wall-review-20261105.tar.gz`, 80,901 bytes, sha256 `ed1658e2d24dffb588fa53af65d86eb04fbca79ff663e550a505c9bad8721786`. It preserves the refresh receipts, relevant PR/archive sources, reviewed file hashes and validation summary. Refresh stamp sha256 `b18239e44f373d5dbf9aee47714026fc614d14dfd3bc0a72754088a41a0606d3`; checked-index sha256 `488f679c1f16afe06d1907cbc26671f0c096511fd0f46d292edde42c9e2aa927`.

## Exact release handoff

| Artifact | Reviewed sha256 |
|---|---|
| Portal Lean, unchanged | `38fb1b2c43c6ea9b7e479380a11c9a9103e50e865336e09bbdad21d4612dc7bf` |
| Kit base, header corrected | `36466e05e1f1046d356d8575b57533b8479bff58357132ab73fa9f7c8a7ae138` |
| Kit locks, unchanged | `ead953d6a4c6d49533a115e3e36b33241fe4bd6f5b26aae67440c20230419938` |
| Kit cloud, unchanged | `17ef5cc3a863ce604d2a5bedbe1b61d029d4b6864f02526f5479df8afb97de75` |
| Essay prose | `852c495fa3f235bcd818c6e2d4b929dae7175d0491f803f28d79056394f727d3` |
| Abstract | `4f295cc6f3e74108269572327b8eeea1872feb1b4c0013d2d64dcc5f3aa9d5b5` |
| Generated essay | `8ea56616f362d5564846b72aa69288b078931925e224136e761cf69fe0935e1c` |
| Kit integration patch | `395f7c1e32da909034bea812c989b717c741ddf99f3efa99225863f8243bc5cc` |

Local's next executable step is the existing notebook driver on these exact essay/abstract/portal bytes, requiring all established gates and a fresh `post.sh --dry` against the live verifier. Record the new notebook digest. Copy the three modules into the current kit, apply the integration patch, and build/check the exact sources and their import integration. Preserve the distinction between these module checks and an unperformed full-catalog build. With passing release receipts and no substantive source change, GPT clearance stands without another editorial round; Local posts on the owner's instruction.

Repository validation passes: `ledger_check.py`, `doc_links.py`, `git diff --check`, conflict/privacy scan, exact essay/embedded-source hashes, unchanged base proof bodies, and kit patch application. No TeX was changed.

Both GPT schedules remain paused. CL746 arrived during this review and was read as a coordination update; its new enumerator and ongoing slip computation are not carried or duplicated here. No GPT research run is queued.
