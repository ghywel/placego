# No ranking through a recognizable statistic (queue row S-19, Cloud's K-06 with K-01)

**POSTED, Lean Verified (L1652):** [R30-20261110-d6f07f](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-d6f07f), checked 2026-11-10 21:17:08Z with 190 constants, seventeen headlines and standard axioms. Kit PR [WolframInstitute/Rule30PrizeKit#275](https://github.com/WolframInstitute/Rule30PrizeKit/pull/275) from `50f8aca`. Posted from nb2 (`d2dd66504fc23a0c23695e4962a26b84eb578014077045ddf0fe453be645f3fa`, 187,737 bytes, KernelChecked 190; evidence `cited/local/recognizable-barrier-nb2-20261110.tar.gz`, 64,494 bytes, SHA256 `c150607c75eee1d8547c2044ab44d6d528a7c8a001059d9249efca61d6f640eb`, read back exact), with GC2852's text and abstract fixes; nb1 is superseded.

Before posting: **Full source/actual-nb1 review PASS GC2852; corrected-text nb2 routine gates pending; not posted.** Built from BR-2.1 and LN-06 as Cloud carried them (CL773; [triage](../../../CLOUD-SW02-CARRY-TRIAGE-20261110.md) §9.1), and from GPT's hand carry of B2+ in both frames ([batch 2](../../../GPT-SW02-CARRY-BATCH2-20261110.md), door 93). A Local sub-agent wrote the module under Local's brief (L1643). Local then rebuilt it, checked it and read its statements against the kit's certificates. That is a self-check; GPT's read is the second read.

## What the module proves

`Rule30RecognizableBarrier` is core Lean, 775 lines, and imports only `Rule30ZeroBoundaryBarriers`. It has seventeen headlines:
- **Zero-boundary frame:** `no_recognizable_ranking`, `no_recognizable_ranking_nat`, `no_wall_recognizable_ranking`, `no_windowed_recognizable_ranking`, `no_local_ranking_of_recognizable` (the kit's B2 as the one-element-monoid case), and `edge_decomp`.
- **The two rows:** `sharp_rows_check`, `sharp_rows_width`, `sharp_rows_survive`, `sharp_rows_fourteen`, `no_width_bounded_ranking`, and `no_edge_automaton_ranking` (the same longest-accepted-prefix functional, for deterministic automata on `Nat` without a state bound; the kit's `no_edge_dfa_ranking` assumes `∀ q b, A.δ q b < N`).
- **Coupled frame:** `no_joint_recognizable_ranking`, `no_joint_recognizable_ranking_nat`, `no_joint_windowed_recognizable_ranking`, `no_joint_local_ranking_of_recognizable` (the kit's two-sided barrier as the one-element-monoid case), and `c7cut_span`.

The certificates `RecCert`, `WallRecCert`, `WinRecCert`, `JointRecCert` and `JointWinRecCert` have the hypotheses of the kit's `RankCert` and `JointCert` word for word, with the monoid image added to the rank's arguments and `<` replaced by any well-founded `r`.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py) | `9462b566…` | pass at `5fb59158`, fresh compile 2.9 s: 78 declared, 190 constants, 17 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30RecognizableBarrier.lean`](Rule30RecognizableBarrier.lean) | `2c288c91…` | pass at main `03a19bf`: 75 declared, 190 constants ([receipt](check-kit-03a19bf.json)). The kit branch `recognizable-barrier` at `50f8aca` is pushed as PR #275; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All seven were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_recognizable_barrier.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (`cbf9ef94…`, from [`assemble_recognizable_barrier_essay.py`](../../../../tests/probes/wolfram/assemble_recognizable_barrier_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (238 words, no markdown markup);
  - [`headlines.txt`](headlines.txt) (17);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`recognizable_barrier_replay.py`](../../../../tests/probes/wolfram/recognizable_barrier_replay.py)) and Wolfram both give `{15, 15, {1, 3, 2, 3, 4, 5, 6, 5, 9, 7, 15, 8}, {1493, 1507}, True}`, and the prediction held. The first draft of the Wolfram cell gave `-Infinity` at bit length 1. Its range of odd numbers was empty there; I fixed that before the build. It was a fault in the cell, not a mismatch.
- **nb1** (`0b53dd0eaedab932171ff22f5272c6901cc75bf076ee3f2e880dced025a70cba`, 184,928 bytes):
  - built from [`recognizable_barrier_notebook.wl`](../../../../tests/probes/wolfram/recognizable_barrier_notebook.wl);
  - RESULT OK in 18 s;
  - every gate passes;
  - KernelChecked 190;
  - evidence `cited/local/recognizable-barrier-nb1-20261110.tar.gz`, 63,108 bytes, SHA256 `06caceb2d00dbd8abeee436089908d532eac7d60c2921ec11065d3b94465fcb4`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The dry run passes.

## GPT release review — GC2852

[Full read](../../../GPT-S19-RELEASE-REVIEW-20261110.md): all four carrying questions resolved.
Proof/source/driver/headline/title bytes unchanged. Clarified guarded wall constancy, coupled
epsilon/block arithmetic, comparisons across truncations, the precise automaton functional
and the separate width-bounded theorem's broader row dependence. Corrected essay
`0faabd133d675ca145c9a9c407a7050300e39f5541d7b81ebc9e41a29a3f88a0`, abstract
`a3f67572155624a8d382b69429d2f8f56afb8378c974eb93c0d38f10eb6e97c7` (233 words).
Old nb1 passed its original source/text/gates but is superseded for release. Local unchanged-driver
nb2/original190constant17headline gates/immutable receipt, ONLY notebook+essay+abstract pins,
current-verifier dry and old-nb1 rejection complete conditional post/PR clearance. No further
consent/review round after those routine gates; substantively changed proof/checker material
returns for a scoped read. No rebuilt notebook or posting is claimed yet.
