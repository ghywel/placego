# From tick 46 on, every row beside the wall has a twin (queue row S-02)

**PACKAGED, L1584. NOT POSTED.** Awaiting GPT's packet read and the owner's word. Built at kit main `48d8fbbc`; the portal form passes `Check` at the verifier's kit `5fb59158`, image 18.

| Form | File | sha256 | `Check` |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) | `4322dc313994d98b…` | pass at the verifier's kit `5fb59158`: 143 constants, 9 headlines ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30LateTwins.lean`](Rule30LateTwins.lean) | `ed43f13da315ec68…` | pass at kit main `48d8fbbc`, with the patch applied: 143 constants, 9 headlines ([receipt](check-kit-48d8fbbc.json)) |

**Texts.** [`title.txt`](title.txt), [`abstract.txt`](abstract.txt) (183 words, `b28497ae…`), [`essay-prose.md`](essay-prose.md) (`d84f2e6c…`), [`essay.md`](essay.md) (`76a4eec3…`), [`headlines.txt`](headlines.txt).

**Notebook nb1.** SHA256 `055b6763d2c9ca64df8d5de45727a2a24cb768b4b75f2f9231d6f936af23be86`, 129,190 bytes. RESULT OK in 18.5 s: 6 output cells, no message cells. The worked numbers equal the Python replay ([`late_twins_replay.py`](../../../../tests/probes/wolfram/late_twins_replay.py)), the icon payload equals the portal source byte for byte, the axiom sets match, and KernelChecked holds at 143 declarations. Driver [`late_twins_notebook.wl`](../../../../tests/probes/wolfram/late_twins_notebook.wl), assembler [`assemble_late_twins_essay.py`](../../../../tests/probes/wolfram/assemble_late_twins_essay.py).

**Post script.** `post.sh` lives outside git and refuses unless the notebook, source, abstract, title, essay and headlines match their pins and the verifier is still kit `5fb59158`, image 18. `post.sh --dry` passes.

**Theorems.** `F_shiftRight`, `iter_F_shiftRight`, `band_settles`, `band_late`, `sync`, `twin_of_factors`, `late_twin`, `late_twin_immortal`, `late_twin_off_orbit`.

**Mutants.** All seven rejected ([receipt](../../../../tests/probes/wolfram/late_twins_mutate.out)): onset 45; 13 ticks in stage one; 11 ticks in stage two, in all four phases with the proof adjusted, rejected by the kernel; 25 ticks overall; a wrong element of `C20`; a wrong factor position; a corrupted reset word.

**Provenance.** AM-3's Result B1, carried in GC2690 with its guards: twins at every `t ≥ 46`, immortality inheritance at even `t` only. The Lean differs from the hand argument in two ways. The settling of the top twenty cells is checked in two kernel stages (4,096 and 512 cases) instead of all `2^19` starts; the bound is still exactly 26. The top band is read by the identity `F Y >>> (m + 1) = R (Y >>> m)`, with no bit reversal, so no width condition is needed for the band to evolve on its own.

**Not formalized.** The `2^3955` family past an uncomputed onset (B2), and the general reset schedule. Both are said so in the essay.

**Prior art in the packet.** Feynman's theorem on predecessors (kit `Rule30Predecessors`); Troy Lowry's open kit PR #60 (`scheduled_cascade_closes`), which assumes the resets this module proves are supplied; `Rule30PrefixMerger`; `Rule30UniversalLeftSide` and `Rule30FourLeftSides` for the settling of the top. Cloud CL752 marked the theorem CLEAR against `rule30-open` and Berzai.

**Not done.** The full catalog build. The PR is not opened. `PORTAL-ID` in the kit row is filled after posting.
