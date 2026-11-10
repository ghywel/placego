# AbsorptionT t001 is false, after lhallee/rule30-open (queue row S-05)

**RELEASE PACKET BUILT (L1623), not posted: GPT's release read requested.** At the owner's word (10 November, L1619): "S-05: yes with crediting the work at rule30-open". The theorem and the trap are Logan Hallee's ([`lhallee/rule30-open`, `Rule30Open.Columns.Traps001`](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Columns/Traps001.md), Apache-2.0, read at `1ddcd411`). It is not on the kit or the portal: `known_find` for `not_absorptionT_t001` finds nothing, and kit main `03a19bf6` calls `AbsorptionT t001` open in three places. The module is our swarm's BN-L1 replay (SW-02; agent PE-1 found the table independently), cleaned for the kit. No rule30-open code is copied.

## What the module proves

`Rule30EtherThreeNotAbsorption` (core Lean, imports only `Rule30EtherThreeTrap`, byte-identical at the verifier's kit `5fb59158`):
- `trap001fifteen_check`: `trap001fifteen` is a checked `PTrap` for `001`, with period 15, 52 cells and 153 states.
- `fifteen_apart_t001`: no state of it, cut to 47 cells, is a state of `t001` at a label of the same phase. The check covers 124,695 pairs.
- `stays`: the half given by state 0 stays in the trap for ever (`PTrap.invariant`).
- `not_absorptionT_t001`: `¬ AbsorptionT t001`.
- `rule30open_half`: rule30-open's named half is state 25 of the table, at label 3.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from the kit form by [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py), which also reproduces S-13's portal form byte for byte | `d09e01a826f91f57…` | pass at the verifier's kit `5fb59158`: 20 declared, 34 constants, 5 headlines, standard axioms; build plus Check 4.5 s, 1.8 GB ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30EtherThreeNotAbsorption.lean`](Rule30EtherThreeNotAbsorption.lean), 137 lines | see receipt | pass at kit main `03a19bf`: 20 declared, 34 constants ([receipt](check-kit-03a19bf.json)). The kit branch `not-absorption` at `eb18643` is local, with [`kit-integration.patch`](kit-integration.patch): the import, the row, and the two README status corrections |

**Mutants.** All four were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_not_absorption.out)): the witness plus one, one table bit flipped, `t001` apart from itself, and the named half at state 24.

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (`68213cf3…`), from [`assemble_not_absorption_essay.py`](../../../../tests/probes/wolfram/assemble_not_absorption_essay.py);
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (211 words);
  - [`headlines.txt`](headlines.txt) (5);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`not_absorption_replay.py`](../../../../tests/probes/wolfram/not_absorption_replay.py), prediction in its header) and Wolfram give the same list, `{-1, -1, 1270, 78, 73}`:
  - neither witness enters `t001` within 3,000 steps;
  - the empty half first enters at step 1270, the kit's `absorbed_empty`;
  - the witnesses show 78 and 73 distinct 52-cell windows.
  - The prediction held.
- **nb1.** Built by [`not_absorption_notebook.wl`](../../../../tests/probes/wolfram/not_absorption_notebook.wl) at `5fb59158`, under caps.
  - SHA256 `93867733b43d4928517be6b8ce9273832465a02d9b00b7c1eb04629ae7bcc02d`, 71,840 bytes.
  - RESULT OK in 22.7 s, 2.1 GB peak tree RSS.
  - All gates pass, KernelChecked 34.
  - Evidence: `cited/local/not-absorption-nb1-20261110.tar.gz`, 28,034 bytes, SHA256 `b5478d40cb8152fac47323eaf54dc34c77f0c11c9ab0339f569c785437933cdb`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh) is S-13's wrapper with new pins and 5 headlines. The dry run passes at `5fb59158`, image 18.
