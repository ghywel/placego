# The wall of rain-tailed rows: letters, three locks and a closed cloud

**Not posted.** Prepared at the owner's word (5 November 2026, L1548). Local alone posts, on the owner's word. Two things stand between this package and posting: the release notebook, which needs Wolfram Engine working again, and one read from GPT.

| Form | File | sha256 | Build (M5) | `Check` |
|---|---|---|---|---|
| Kit, base | [`Rule30RightWall.lean`](Rule30RightWall.lean) | `444b24f36cb3fde5…` | 2 s, 0.5 GB | pass at kit main 72253ae, 433 constants, 18 headlines |
| Kit, locks | [`Rule30RightWallLocks.lean`](Rule30RightWallLocks.lean) | `ead953d6a4c6d495…` | 2 s, 0.6 GB | pass, 66 constants, 12 headlines |
| Kit, cloud and entry | [`Rule30RightWallCloud.lean`](Rule30RightWallCloud.lean) | `17ef5cc3a863ce60…` | 10 s, 2.7 GB | pass, 126 constants, 6 headlines |
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) | `38fb1b2c43c6ea9b…` | 13 s, 3.0 GB | pass at the verifier's kit 722a0c51, 625 constants, 36 headlines, in 14 s at 3.3 GB |

Texts: [`title.txt`](title.txt), [`abstract.txt`](abstract.txt) (`98ee984e…`, 224 words), [`essay-prose.md`](essay-prose.md) (`9df0eded…`), [`essay.md`](essay.md) (`1dd6e798…`), [`headlines.txt`](headlines.txt), [`PR-BODY.md`](PR-BODY.md). Generators and controls: [`tests/probes/wall_floor/package/`](../../../../tests/probes/wall_floor/package/gen_base.py), [`assemble_right_wall_essay.py`](../../../../tests/probes/wolfram/assemble_right_wall_essay.py), [`right_wall_notebook.wl`](../../../../tests/probes/wolfram/right_wall_notebook.wl).

**What changed from the record's modules.**
- The row and the tick are now the kit's `Rule30FrozenRuler.T` and `iter`, so the statements are about the kit's edge codes.
- The finite checks run on numbers (`run`, `next_fast`, `closed_fast`). The cloud fell from 57 s to 9 s, and all three locks together take 2 s.
- New theorems: `predecessor_unique`, `letters_closed`, `letter_after_A`, `letter_after_B`, `held_not_periodic`, `anchor_held`, `Lock.forever`, `Lock.letters`, each lock's `letters` and `not_periodic`, `floor`, `no_floor`, `Cloud.avoids_lock`, `Cloud.not_periodic`, `Entry.entry`.
- `no_floor` and the entry were computed results before and are now in Lean.
- The two-pairs law and the 24-word window classification are not in this entry.

**Controls.** [`mutate.out`](../../../../tests/probes/wall_floor/package/mutate.out): all ten mutants rejected. [`replay_portal.out`](../../../../tests/probes/wall_floor/package/replay_portal.out): a plain Python replay from the literals, 3,392 image checks, the letters, the ranks, the reset depths and the entry row. [`check_portal.txt`](../../../../tests/probes/wall_floor/package/check_portal.txt), [`check_kit.txt`](../../../../tests/probes/wall_floor/package/check_kit.txt).

**Not done.**
- **Release notebook.** `right_wall_notebook.wl` is written but has not run. The Wolfram kernel exits at once with "not activated or is experiencing a license-related problem", so the Wolfram Language cells in `essay.md` are untested. Their logic is the Python replay's. The driver's gates are those of the forced-front notebook, with the first cell gated on `True` and the 111 letters.
- **`post.sh`.** To be written with the notebook's pins.
- **Full catalog build,** for the PR. The M5 cannot do it under its caps; Cloud ran it for earlier PRs.

**Prior art searched.** `known_find.py --new` at kit `72253aea`, portal updated 5 November 15:50Z, 13 open PRs. Terms: reset word, wall lock, right wall, backward wall, closed window, rain tail, rain row, edge code predecessor, alternating left, backward closed, closed set of windows, inverse sweep, eventually alternating, letters. Hits read: `Rule30ResetFreeCore`, `Rule30ResetFreeThree`, `Rule30ResetFreeBoundary`, PR #60's `Rule30InverseCascade`, `Rule30GateTrap`, `Rule30EdgeStaircases`, `Rule30UniversalStart`, `Rule30RightPeriods`, `Rule30FrozenRuler`. All eight reset words `F(b, u, v)` contain a word `0 1^(3m+1) 0` with a cell above it, and all are synchronizing for the inverse sweep (checked), so `Reset.above` is credited as known in kind, and the essay claims only the shape that returns. Closed PR discussions are not indexed by `known_find`.

## Questions for GPT (one read before posting)

The Lean is machine-checked, so this read is of the text against the Lean. GPT may change the texts, with reasons in the ledger, and Local rebuilds the notebook on any change.

1. **Section 1 against the Lean.** Do the words "every predecessor", "for ever" and "whatever lies below" say what `held_forever` and `Lock.letters` say? `predecessor_unique` is there so these are not empty.
2. **Section 2.** Is this inference safe: a periodic row can have no front in its orbit, so if every other rain-tailed row reached the eighteen windows, the rain pair would be the only periodic rows with a rain tail? It is offered as the shape of the open question and not as a theorem.
3. **Section 3.** Is the credit to Lowry right and is it enough? Does anything in `Rule30ResetFree*` or PR #60 already give `Reset.again`, or the shape's return three cells higher?
4. **Section 5.** "Lower states still merge before they reach the letters, but at places that move with the phase" rests on computation, not on `no_floor`. Is the sentence labelled well enough?
5. **Section 6.** Does `Entry.entry` support "a row in the cloud can step into a lock"? The row at tick 97 is held in `Q45`, and it stays in `Q45` at all lower ticks, where the third lock's top cells also lie. Tick 7 is outside the lock, tick 6 inside.
6. **Section 9.** Are the statuses right? The surrogate line is the direct run of L1547, plus earlier runs.
7. **Scope.** Title and abstract against the Lean, especially "letters forced for ever" and "No row in these sets is periodic". The first holds for the three locks, the second for the three locks and the cloud, and also for the eighteen-window front. The set of two letters alone is covered by `front_not_periodic` through `B11`.
8. **Kit PR.** Does [`PR-BODY.md`](PR-BODY.md) meet the catalog's rule on certificate data? The largest module takes 10 s at 2.7 GB.
