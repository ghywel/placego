# The period-two column-1 words from two ticks on (queue row S-21, Cloud's K-02)

**Full source/actual-nb1 read PASS GC2850; corrected-text nb2/two pins/current dry next; not posted.** [Complete review](../../../GPT-S21-RELEASE-REVIEW-20261110.md). All four L1647 questions resolved; source/proof/abstract/driver unchanged. Clarified scope/credit in prose/PR only. Local unchanged-driver nb2/original136constant gates, notebook+essay pins and fresh dry complete standing conditional posting/PR clearance without another permission round. Old nb1 below is superseded for release. Built from BR-5.2 as Cloud carried it (CL773; [triage](../../../CLOUD-SW02-CARRY-TRIAGE-20261110.md) §9.1) and as GPT carried and sharpened it to a two-tick onset at both widths ([GC2840/GC2843](../../../GPT-K02-CARRY-20261110.md)). Local wrote the module directly, with no sub-agent.

## What the module proves

`Rule30PeriodTwoOnset` is core Lean, 385 lines, and imports only `Rule30Prize` and `Rule30Jen`. It has sixteen headlines:
- `win_dstep`: two ticks from a white time of column `0` are a double step of the window of the columns `1..b`, with two free cells of column `b + 1`, for every history `H : Nat → Int → Bool` that obeys rule 30 at those columns;
- `img5_length`, `img6_length`, `img5_closed`, `img6_closed`: the first images, `20` and `38` windows, are closed under the double step;
- `no_word5`, `no_word6`, `no_short6`: an alternation on the `2 m` ticks `s..s+2m-1` excludes every word of the kit's lists of length `m`, and `101010000` at width `6`, from column `1` at `s+2..s+2m`;
- `onset5`, `onset6`, `col1_constraints5`, `col1_constraints6`: so from `T + 2`, for every history, and for the single seed the kit's statements with `T' = T + 2`;
- `free_bit5`, `free_bit6`, `free_bit_constraints5`, `free_bit_constraints6`: the complemented free bits, with the rule at column `0` and two more ticks.

The minimal-word list up to length `13` and the words excluded without the first double step are COMPUTED (Python and Wolfram), not formalised.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py) | `20c00829…` | pass at `5fb59158`: 67 declared, 136 constants, 16 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30PeriodTwoOnset.lean`](Rule30PeriodTwoOnset.lean) | `7518614f…` | pass at main `03a19bf`: 63 declared, 136 constants ([receipt](check-kit-03a19bf.json)). The portal form adds four generated `match` names. The kit branch `period-two-onset` at `e6d22df` is local; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All eight were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_period_two_onset.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (corrected `6158f9f4…`, from [`assemble_period_two_onset_essay.py`](../../../../tests/probes/wolfram/assemble_period_two_onset_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (243 words, no markdown markup);
  - [`headlines.txt`](headlines.txt) (16);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`period_two_onset_replay.py`](../../../../tests/probes/wolfram/period_two_onset_replay.py)) and Wolfram give the same result, and the prediction held:
  `{20, 38, True, True, True, True, {"11", "00000", "100101", "10010001"}, {"11", "00000", "100101", "101001", "10010001", "101010000", "1010001001", "10010000101", "1001000010001"}, {"11", "00000"}, {"11", "00000", "101001"}}`.
  The Wolfram cell uses the built-in `CellularAutomaton[30, …]`.
- **nb1** (`4114be9230e656dc569f05ea13275dc947926b81c1674425e62e582bf9f99c87`, 127,607 bytes):
  - built from [`period_two_onset_notebook.wl`](../../../../tests/probes/wolfram/period_two_onset_notebook.wl);
  - RESULT OK in 23 s;
  - every gate passes;
  - KernelChecked 136;
  - evidence `cited/local/period-two-onset-nb1-20261110.tar.gz`, 36,756 bytes, SHA256 `190ce86f462bc8f19bc843334c02a9547078fd54a5ac8aa545355e22770f2513`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The dry run passes.
