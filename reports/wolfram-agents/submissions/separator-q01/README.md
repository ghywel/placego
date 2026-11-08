# The separator is Q01 for free bits without two adjacent whites, and BWH is a death-time bound (queue row S-04)

**POSTED, Lean Verified (L1589):** [R30-20261108-752db6](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261108-752db6), submitted 14:38Z at the owner's word, checked 14:39:34Z: kernel replay of 164 constants passed, 17 headlines, standard axioms only, kit `5fb59158`. Kit PR not opened; the kit branch `s04-separator` carries the reviewed row with the id filled (`093b7dd`, local). Earlier status: **RELEASE REVIEW PASS, GPT GC2736.** The full proof/text read (GC2728) and final attribution-corrected nb2, release-pin and dry-run read pass. No further rebuild is required. [Review](../../../GPT-S04-RELEASE-REVIEW-20261108.md#final-refreshed-release-read--gc2736). The owner's posting word is next. Built at kit main `48d8fbbc`; the portal form passes `Check` at the verifier's kit `5fb59158`, image 18.

| Form | File | sha256 | `Check` |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) | `64b76f6da535c047…` | pass at the verifier's kit `5fb59158`: 164 constants, 17 headlines ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30SeparatorQ01.lean`](Rule30SeparatorQ01.lean) | `c73e6d777d96727a…` | pass at kit main `48d8fbbc`, with the patch applied: 164 constants, 17 headlines ([receipt](check-kit-48d8fbbc.json)) |

The kit form is byte-identical to the module in the local kit branch `s04-separator` (commit `684cacf`, not pushed); [`kit-integration.patch`](kit-integration.patch) holds its import line and catalogue row.

**Texts.** [`title.txt`](title.txt), [`abstract.txt`](abstract.txt) (205 words, `5c037c1c…`), [`essay-prose.md`](essay-prose.md) (`3d969140…`), [`essay.md`](essay.md) (`c7916ca0…`), [`headlines.txt`](headlines.txt), [`PR-BODY.md`](PR-BODY.md), [`prereg.txt`](prereg.txt).

**Notebook nb1: reviewed, superseded for release by GC2728 attribution repair.** SHA256 `2f09ee52487c3024c496e12f40dc4a40377b11b5f69630682c81ce7e747365aa`, 187,824 bytes. RESULT OK in 14.2 s: 6 output cells, no message cells. The worked numbers equal the Python replay ([`separator_q01_replay.py`](../../../../tests/probes/wolfram/separator_q01_replay.py)): `{38, 32, 136, True, {2, 3, 5, 8, 13, 21}}`. The icon payload equals the portal source byte for byte, the axiom sets match, KernelChecked holds at 164 declarations, and there are no home paths. Driver [`separator_q01_notebook.wl`](../../../../tests/probes/wolfram/separator_q01_notebook.wl), assembler [`assemble_separator_q01_essay.py`](../../../../tests/probes/wolfram/assemble_separator_q01_essay.py).

**Post script.** `post.sh` lives outside git and refuses unless the notebook, source, abstract, title, essay and headlines match their pins and the verifier is still kit `5fb59158`, image 18. `post.sh --dry` passes.

**Theorems (17 headlines).** `cone_chart`, `peel_chart`, `hardCore_endOf_iff`, `sep_iff_QN`, `orbitSeparator_iff_QN`, `Q01_sep`, `Q01_iff_sep_and`, `sep_Q01Gap`, `sep_CQ01Empty`, `sep_iff_LR1`, `layerWord_realizes`, `sep_CQ01`, `bwh_iff_deathBounds`, `bwh_death`, `bwh_Q01`, `odd_guard_needed`, `even_threshold_needed`.

**Mutants.** All ten rejected ([receipt](../../../../tests/probes/wolfram/separator_q01_mutate.out)):
- Three state something false and fail in `decide`: a tail symbol `1` (`phi 1 1 = 2`), the odd-guard witness to tick 38, and the threshold witness to tick 32.
- The two dropped guards (even clause from `n = 6`; the odd clause without its top two black) state what `even_threshold_needed` and `odd_guard_needed` refute.
- The layer word at the black ticks states what `black_tick_control` refutes.
- The rest break the proof: the class with no two adjacent black bits, the endpoint at the even tick, the peel chart one depth deeper, and the death bound `2W + 2`.

**Provenance.** CP-4 Claims A and B, carried in GC2690 with their repairs. The Lean differs from the hand argument in three ways:
- `QN ⇒ SEP` reads the chart at an even tick past the onset and uses `two_step_shift`, so no rotation of the stream is needed.
- `LR1` is stated in the kit's sideways phase (centre black at the even ticks), where the forced row is `Theta` of the complement, so GC2690's one-tick repair belongs only to the record's white-start convention.
- The death bound's dictionary is proved in both directions with a finite-horizon chart.

The two controls are new. The width-19 witness is the SW-02 skeptic's (SKR-CP-4-2), and the width-14 one is the record's champion `11083`.

**Cross-check.** Through the dictionary, an exhaustive search reproduces the swarm's horizon table for `n = 5` to `9` ([`separator_q01_margins.py`](../../../../tests/probes/wolfram/separator_q01_margins.py), [output](../../../../tests/probes/wolfram/separator_q01_margins.out)), as preregistered.

**Prior art in the packet.**
- `lhallee/rule30-open` at `f877f5af`, still its head (`WedgeLadderQ01`): the chart (`zcone_chart`, `zpeel_chart`), `binaryCTS_iff_Q01`, `q01_constantTailSeparator` and `bwh_Q01`. These are known, reproved here. Its `WedgeLadder.md` already states the exact-width death-time dictionary, with both horizons and the top-two-black guard, and checks it through n=12. That known interpretation is formalized here; the hard-core class, `Q01Gap` implication and layers are additional.
- The kit's Condrey/Quint separator modules (PRs 76, 84, 86, 101), whose docstrings say that no relation with `Q01` is known, and Bosdure's `Rule30GateTrap` (PR 64).
- The kit's `constant_separator_excludes_alternating`, which `sep_CQ01` restates sideways, and `q01_width_le_52_linear`, an unconditional `2W + 8` to width 52.

**Evidence.** Shared store `cited/local/separator-q01-20261108.tar.gz`, 525,975 bytes, SHA256 `9ac43baa5f82ae44f651f38a7362a522309db710b2e6818382b814367a5e6319`.

**Not done.** The full catalogue build. The kit branch is not pushed and the PR is not opened. `PORTAL-ID` in the kit row is filled in after posting.

**Local refresh, GC2728.** Rebuild from corrected `essay.md` (SHA256 `c7916ca0bc7d1756b5b4ecb90b66e902ef7c3997c3be777cb4b315d2ac1c530c`), with unchanged source/abstract/title/headlines/driver. Refresh private notebook/essay pins and publish the new notebook, receipts and sanitized pin/dry receipt for the short final byte read. No Lean rebuild is required for this prose-only change unless source/toolchain/verifier changes.

**Notebook nb2 (release), L1586.** Built from the corrected essay with the unchanged driver (`bbdc8baf…`): SHA256 `8f2305a01e65fcd5f9b8e33e9c03557e7f5ccacb9b0b2a6b3c3536a3f362f16e`, 188,972 bytes. RESULT OK in 12.4 s: 6 output cells, no message cells, essay digest `c7916ca0…`, the Abstract cell equal to `abstract.txt`, the icon payload equal to the portal source, the axiom sets matching, KernelChecked 164, no home paths. The assembler reproduces the corrected essay byte for byte. Pins refreshed to nb2 and the corrected essay; `post.sh --dry` passes (verifier `5fb59158`, image 18). Notebook, receipts and the sanitized pins and dry run: shared store `cited/local/separator-q01-nb2-20261108.tar.gz`, 512,426 bytes, SHA256 `ea8378c0c044104ea25acffa2944452e42081c9f24ee57ff34bd27033a994d4f`. The kit branch's catalogue row now carries the same `WedgeLadder.md` credit (local commit `8433a8f`).
