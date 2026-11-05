# The error edge of two configurations: barrier, heal criterion, six laws after a heal

**Reviewed with corrections, not posted (GPT GC2685, re Local L1553 and Cloud CL747).** Mathematics and corrected submission/proposed PR texts cleared. Local rebuilds on the revised pins below and posts on the owner's instruction; no further prose round if exact-source release checks pass unchanged.

**Historical release (superseded by GC2685 text/header corrections).** Notebook sha256 `65fc517295238ce6868d68d42c6df4afb32ceea95c40d1230769d025fcc6fe19`, 98,027 bytes, on verifier image 17 (kit `722a0c51`), RESULT OK in 26 s at 2.6 GB, on the first run. Every gate passed: 6 Output cells, no Message cells, the first cell equal to the plain Python replay, the Abstract cell, the icon payload, the kit cell, a LeanEnvironment, all 14 axiom sets, KernelChecked 56. No home path in it. Receipts `cited/l1553-error-edge/nb1-receipts.tar.gz` (4061 bytes, e8a9f4b51c284d60…). `post.sh --dry` passes against the live verifier. Any change to the Lean, essay or abstract moves the pins and needs a new notebook, which takes half a minute.

| Form | File | sha256 | Build (M5) | `Check` |
|---|---|---|---|---|
| Kit | [`Rule30ErrorEdge.lean`](Rule30ErrorEdge.lean) | `98a743d802cfd14d…` (header corrected) | under 1 s, closure 14 s at 2 GB | pass at kit main 5fb5915, 56 constants, 14 headlines |
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) | `e77266a078e5a3b6…` (header corrected) | under 2 s | pass at the verifier's kit 722a0c51, 56 constants, 14 headlines |

Texts: [`title.txt`](title.txt), [`abstract.txt`](abstract.txt) (228 words, `a5a02c1f…`), [`essay-prose.md`](essay-prose.md) (`e0d4c646…`), [`essay.md`](essay.md) (`9d5b5cba…`), [`headlines.txt`](headlines.txt), [`PR-BODY.md`](PR-BODY.md), [`kit-integration.patch`](kit-integration.patch). Drivers: [`assemble_error_edge_essay.py`](../../../../tests/probes/wolfram/assemble_error_edge_essay.py), [`error_edge_notebook.wl`](../../../../tests/probes/wolfram/error_edge_notebook.wl).

**What Local changed from CL747, and why.** No proof changed.
- **Header order.** The kit's rule is `module`, imports, `@[expose] public section`, then the namespace, so `Rule30ErrorEdge.lean` puts them in that order. `cloud-Rule30ErrorEdge.lean` stays as Cloud delivered it.
- **Credit.** Cloud's list did not include `Rule30HealingBound` (our own R30-20261103-e660e4). Its `healing_bound` already has the black half of `heal_iff` as its recruiting step, so the essay, the module header and the catalog row now say so, and claim the white half as the converse.
- **"Wall frame" became "from the left edge".** The word now has another meaning in R30-20261105-c15ef5, and "wall" means the zero wall in the kit.
- **"Jumps of 1 and of 8 or more".** The enumerator's window resolves jumps through 8, so the essay now says 1 and 8, and that it does not reach further.
- **The Wolfram cell.** Section 5 now runs every law on two real configurations for 3,000 ticks. A second cell three places from the seed failed as a test: its edge stops at wheel 8 for ever, above a permanently white wheel, so the cell uses 500 places, and the essay says why. Result: 1,112 heals, jumps 1 to 9, `heal_iff` at every tick, no law broken. Wolfram and [Python](../../../../tests/probes/wolfram/error_edge_replay.out) agree.
- **Bridge named.** Section 1 now names `Ld_recurrence`.
- **Internal numbers** removed from section 5. **Build time** corrected to the M5's. **Headlines** are 14: `agree_after` joins Cloud's thirteen.

**GC2685 release step.** [Review and four answers](../../../GPT-ERROR-EDGE-SUBMISSION-REVIEW-20261105.md). No theorem/proof body changed. Essay §§3/5 now retain the white-new-parent guard for jumps 6/7 and say healing by the second opportunity for 4/5. Heal and jump index guards, aligned spatial anchors, later-edge existence and the specific offset-3 control are explicit. Credit includes the exact existing `Rule30LightCone.rule_flip_right_iff` (PR98) and the white-parent step inside `child_white`; neither array in that antecedent is restricted to being a strip.

Local: regenerate the notebook on essay `9d5b5cba58cd4f5cdcc26084380473dcd25bce174bfecc24f6efae77adc0fd8b`, abstract `a5a02c1fb7b549a619579391a40df3a8ff2ea939eb99b8179177b8f666888fb2`, and portal source `e77266a078e5a3b6c625693a15ee059c1dac11658e4d3d23c6c866d784a2c97b`. Recheck the exact comment-revised sources, all established notebook gates and a fresh live-verifier dry run. The kit source is `98a743d802cfd14da8a324084f7e6c7a2088888d055ca7854438b577bc19a56e`; the revised catalog/import patch applies to `5fb59158`. Validate its import integration. The old notebook `65fc5172…` certifies the earlier essay only. The full catalog has not been built and is not represented as passed.

**Controls.** [Nine mutants](../../../../tests/probes/wolfram/error_edge_mutate.out), a flipped conclusion of each law and a dropped white-parent hypothesis, are all rejected. [Portal `Check`](../../../../tests/probes/wolfram/error_edge_check_portal.txt), [kit `Check`](../../../../tests/probes/wolfram/error_edge_check_kit.txt).

**Prior art searched.** `known_find.py --new` at kit `5fb59158`, portal 18:19Z, 12 open PRs, and the index's PR channel worked on this host. Terms: error edge, difference pattern, damage, two configurations, disagree, first differing, heal, stall, jump, two arrays, agree below, differ at. Read: `Rule30HealingBound` (credited), `Rule30UniversalLeftSide` (`child_same`, `child_white`, `same_left_side`, credited), `Rule30MaskedJen.left_of_black` (credited), `Rule30EdgeClock` and R30-20261103-e742c0 (first differences on the right-edge map `T`, another recurrence and other statements), R30-20261024-1fc962 `front_step` (the period-3 ether), R30-20261029-dc3d17 (unrelated), R30-20261027-61e435 (right-edge `iter_agree`). Nothing gives `heal_iff`'s white half for two left-diagonal arrays, or the jump laws. Closed PR discussions are not indexed.

**Not run:** the full catalog build. It is not required, and PR 156 landed without it.

---

*Cloud's original README follows.*

**Cloud, 5 November 2026 (CL747). Drafted at the owner's word; nothing posted.** Local builds of record, runs the novelty
check at the current kit, builds the notebook, and posts on the owner's word; GPT reads once before posting if the owner
asks.

**The claim (PROVED, Lean 4.35.0, the kit's `Check` on Cloud's Linux host at kit main 8cf1bd4).** For any two arrays
`a`, `b` with the kit's left-diagonal recurrence (`Rule30AgedLeftDiagonals.Recurrence`), with the error edge `Edge a b m t`
(agreement below `m`, disagreement at `m`): the edge never retreats (`agree_step`, `agree_after`, `edge_le`); the arrays
agree at the edge one tick later exactly when the wheel below the edge is black (`heal_iff`; `edge_stall`, `edge_heal`);
after a heal with the edge at `m + 2`: `white_above`, `black_two_above`, and the six laws `jump_two` … `jump_seven`
(the essay's table). Thirteen headlines, 56 constants, axioms `propext` and `Quot.sound` only, no literals, no
`decide +kernel`, no `native_decide`.

| Form | File | sha256 | Build (Cloud, Linux) | `Check` |
|---|---|---|---|---|
| Kit, `Ruliology.CellularAutomata.Rule30ErrorEdge` | [`cloud-Rule30ErrorEdge.lean`](cloud-Rule30ErrorEdge.lean) | `c35855dfe04ca89f…` | about 2 s | pass, kit main 8cf1bd4, 56 constants, 13 of 13 headlines |
| Portal, `Rule30Submission` | [`Rule30Submission.lean`](Rule30Submission.lean) | `e79cb811795318c5…` | about 2 s | pass, kit main 8cf1bd4, 56 constants, 13 of 13 headlines |

Texts: [`title.txt`](title.txt) (`9d54985223550370…`), [`abstract.txt`](abstract.txt) (250 words, `5507d1580b0865cd…`),
[`essay-prose.md`](essay-prose.md) (`30a7791b7e80a4fe…`). The essay has no Wolfram cells yet; a cell replaying one heal
and one jump on the seed would suit section 5, and Local writes it with the notebook. The six laws were found by the
exhaustive enumeration [`jump_facts.py`](../../../../tests/probes/wolfram/jump_facts.py) and measured on the seed's run
and on fair rows (CL744–CL746); none of those measurements is cited as evidence in the Lean.

`Check` recipe: with the kit module at `lean/Ruliology/CellularAutomata/Rule30ErrorEdge.lean` and its `public import`
line in `lean/Ruliology.lean`, `lake build Ruliology.CellularAutomata.Rule30ErrorEdge`, then `lake env lean --run
Check.lean Ruliology.CellularAutomata.Rule30ErrorEdge --claim partial --headline Ruliology.CellularAutomata.Rule30ErrorEdge.agree_step …`
(the thirteen names of the table in the essay); for the portal form the same with `Rule30Submission` and the
`Rule30Submission.` prefix. The portal form was checked at kit main 8cf1bd4 here, not at the verifier's 722a0c51; its
two imports are in both.

## What Local should check before posting

1. **Novelty at the current kit.** `python3 tests/probes/known_find.py --new`, then the terms "error edge", "difference",
   "damage", "two configurations", "disagree", "jump", "heal", "stall", and a read of `Rule30UniversalLeftSide`
   (`child_same`, `child_white`: the aligned-parent transport, one array a strip), `Rule30DrivenLeft`, `Rule30Coupled*`
   and the kit's catalogues. Cloud's `known_find` cache finds nothing for the first five terms; the PR index was 403 on
   Cloud's host. `heal_iff` is the two-configuration form of `child_same`/`child_white`'s step; if the kit already has
   it for two abstract arrays, say so in section 6 and keep the six laws as the entry's content.
2. **The verifier's kit.** Build and `Check` the portal form at 722a0c51; both imports exist there.
3. **The words.** Section 1's "about 0.2428 cells per step" is a cited measurement (Wolfram 1986, NKS p. 949), not a claim
   of the entry; section 5's "about 300,000 heals" is our record's count, not evidence for the theorems. Cut either if
   the portal wants only what the Lean says.

## Questions for GPT (one read before posting, if the owner asks)

1. Do the thirteen headlines say what the abstract and the essay's table say, in particular the jump indexing (edge at
   `m + 2`, new edge at `m + 2 + d`, new parent `m + 1 + d`) and the conditions "whatever it was" (`jump_four`) against
   "with a white new parent" (`jump_five` … `jump_seven`)?
2. Is "the edge never retreats" the right reading of `edge_le` (edges at `t` and `t + n`, `m ≤ m′`)?
3. Section 6's prior art: the aligned-parent transport of `Rule30UniversalLeftSide`, Wolfram 1986 and NKS p. 949 for
   the front, and our §8.66 for the heal identity in diagonal coordinates. Anything missing from the kit?
4. Scope: the statements hold for abstract arrays with the recurrence; the essay says "any two configurations with
   leftmost black cells, whatever lies to their right". Is that the right bridge (`Rule30FiniteDiagonals.Ld` satisfies
   `Recurrence`, as the four-fronts entries used)?
