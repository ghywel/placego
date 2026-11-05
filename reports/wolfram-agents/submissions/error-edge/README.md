# The error edge of two configurations: barrier, heal criterion, six laws after a heal

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
