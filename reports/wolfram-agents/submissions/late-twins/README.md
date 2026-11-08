# From tick 46 on, every row beside the wall has a twin (queue row S-02)

**RELEASE REVIEW PASS, GPT GC2728. NOT POSTED.** Scope repairs are applied; nb2 source, Abstract, essay, output digests, sanitized release pins and dry receipt pass the final byte read. [Review](../../../GPT-S02-RELEASE-REVIEW-20261108.md). The owner's posting word remains required. Built at kit main `48d8fbbc`; the portal form passes `Check` at the verifier's kit `5fb59158`, image 18.

| Form | File | sha256 | `Check` |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) | `4322dc313994d98b…` | pass at the verifier's kit `5fb59158`: 143 constants, 9 headlines ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30LateTwins.lean`](Rule30LateTwins.lean) | `ed43f13da315ec68…` | pass at kit main `48d8fbbc`, with the patch applied: 143 constants, 9 headlines ([receipt](check-kit-48d8fbbc.json)) |

**Texts.** [`title.txt`](title.txt), [`abstract.txt`](abstract.txt) (184 words, `72fcf6cc…`), [`essay-prose.md`](essay-prose.md) (`f96db093…`), [`essay.md`](essay.md) (`0d108613…`), [`headlines.txt`](headlines.txt).

**Notebook nb1: reviewed but superseded for release after GC2726 text repairs.** SHA256 `055b6763d2c9ca64df8d5de45727a2a24cb768b4b75f2f9231d6f936af23be86`, 129,190 bytes. RESULT OK in 18.5 s: 6 output cells, no message cells. The worked numbers equal the Python replay ([`late_twins_replay.py`](../../../../tests/probes/wolfram/late_twins_replay.py)), the icon payload equals the portal source byte for byte, the axiom sets match, and KernelChecked holds at 143 declarations. Driver [`late_twins_notebook.wl`](../../../../tests/probes/wolfram/late_twins_notebook.wl), assembler [`assemble_late_twins_essay.py`](../../../../tests/probes/wolfram/assemble_late_twins_essay.py).

**Notebook nb2 (release), L1585.** Built from the corrected essay with the unchanged driver: SHA256 `83e87be1a1df4dbed7c37c1967b3b1b9e2015e6ff9ea44c4408ad872d50483ed`, 129,983 bytes. RESULT OK in 19.5 s: 6 output cells, no message cells, the Abstract cell equal to `abstract.txt` (`72fcf6cc…`), the essay digest `0d108613…`, the icon payload equal to the portal source, the axiom sets matching, KernelChecked 143, no home paths. Notebook, receipts and the sanitized pins and dry run: shared store `cited/local/late-twins-nb2-20261108.tar.gz`, 535,042 bytes, SHA256 `180ff4c753ac1258923b15c05cfeb72aa07057930abac33237e30f1ea25f4a50`.

**Post script.** `post.sh` lives outside git and refuses unless the notebook, source, abstract, title, essay and headlines match their pins and the verifier is still kit `5fb59158`, image 18. Pins refreshed to nb2, the corrected abstract and the corrected essay; `post.sh --dry` passes (L1585).

**Theorems.** `F_shiftRight`, `iter_F_shiftRight`, `band_settles`, `band_late`, `sync`, `twin_of_factors`, `late_twin`, `late_twin_immortal`, `late_twin_off_orbit`.

**Mutants.** All seven rejected ([receipt](../../../../tests/probes/wolfram/late_twins_mutate.out)): onset 45; 13 ticks in stage one; 11 ticks in stage two, in all four phases with the proof adjusted, rejected by the kernel; 25 ticks overall; a wrong element of `C20`; a wrong factor position; a corrupted reset word.

**Provenance.** AM-3's Result B1, carried in GC2690 with its guards: twins at every `t ≥ 46`, immortality inheritance at even `t` only. The Lean differs from the hand argument in two ways. The settling of the top twenty cells is checked in two kernel stages (4,096 and 512 cases) instead of all `2^19` starts; the bound is still exactly 26. The top band is read by the identity `F Y >>> (m + 1) = R (Y >>> m)`, with no bit reversal, so no width condition is needed for the band to evolve on its own.

**Not formalized.** The `2^3955` family past an uncomputed onset (B2), and the general reset schedule. Both are said so in the essay.

**Prior art in the packet.** Feynman's theorem on predecessors (kit `Rule30Predecessors`); Troy Lowry's open kit PR #60 (`scheduled_cascade_closes`), which assumes the resets this module proves are supplied; `Rule30PrefixMerger`; `Rule30UniversalLeftSide` and `Rule30FourLeftSides` for the settling of the top. Cloud CL752 marked the theorem CLEAR against `rule30-open` and Berzai.

**Not done.** The full catalog build. The PR is not opened. `PORTAL-ID` in the kit row is filled after posting.

**GC2726 refresh completed, L1585/GC2728.** The corrected essay/abstract and unchanged Lean/headline pins match nb2 and the sanitized post guards. The dry receipt confirms verifier `5fb591588cfa869bfdc47946799b5ddd70a903d1`, image18, nine headlines, nothing submitted. All six actual output strings match their receipt digests; notebook source/Abstract decode byte-exact, including the Lean source's final newline. The packet hold is cleared; no new build or posting by GPT.
