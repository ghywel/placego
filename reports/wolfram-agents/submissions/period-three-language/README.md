# The column-1 language beside a period-3 center (Block 9; queue row S-14)

**Status: proof and nb1 reviewed PASS by GPT (GC2759); five text repairs accepted (L1605); notebook nb2 rebuilt from the corrected essay, re-pinned and dry-run (L1606). GPT's short final byte read is requested; posting needs the owner's word.**

[Release review](../../../GPT-S14-RELEASE-REVIEW-20261108.md): prose scope/prior-art and catalogue word count repaired. The branch catalogue row is updated (`0318b3d`) and the patch regenerated. Local rebuilds nb2 from essay `3810a902`, then the pins and dry run; GPT's final byte read remains.

| Form | File | sha256 | `Check` |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) | `4edf326d1f0ed3bb…` | pass at the verifier's kit `5fb59158`: 142 constants, 10 headlines ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30PeriodThreeLanguage.lean`](Rule30PeriodThreeLanguage.lean) | `71ac7331952cf40e…` | pass at kit main `1487f31` with the patch applied: 142 constants, 10 headlines ([receipt](check-kit-1487f31.json)) |

The kit form is byte-identical to the module in the local kit branch `b9-period3`, which has four commits ending at `0318b3d` (the catalogue row with GC2759's wording) and is not pushed. [`kit-integration.patch`](kit-integration.patch) holds its import line and catalogue row. The row's `PORTAL-ID` is filled in after posting.

**Texts.**
- Front matter: [`title.txt`](title.txt), [`abstract.txt`](abstract.txt) (216 words, `60fbdb2a…`), [`headlines.txt`](headlines.txt).
- Essay: [`essay-prose.md`](essay-prose.md) (`bacac172…`) and [`essay.md`](essay.md) (`3810a902…`), assembled by [`assemble_period_three_language_essay.py`](../../../../tests/probes/wolfram/assemble_period_three_language_essay.py).
- Kit PR and predictions: [`PR-BODY.md`](PR-BODY.md), [`prereg.txt`](prereg.txt).

**Notebook nb2 (release).** Built from the corrected essay `3810a902…`: SHA256 `b6494c364eb3585ba7f6f3182c7e0e6c4cf86ba2ca3d82a535ad21e0a83de1f1`, 189,511 bytes; RESULT OK in 41.9 s at 2.5 GB peak.
- Every gate passes: 6 output cells, no message cells; the first cell equals the Python replay ([`period_three_language_replay.py`](../../../../tests/probes/wolfram/period_three_language_replay.py)); the Abstract cell equals `abstract.txt`; the icon payload equals the portal source byte for byte; the axiom sets match `Check`; KernelChecked at 142 declarations.
- The computation, kit, theorem and axiom cells are byte-identical to nb1's. The environment and kernel-check cells name LeanLink's temporary module, so they differ, as expected. nb2 carries GC2759's corrected prose, and nb1 does not.
- Driver: [`period_three_language_notebook.wl`](../../../../tests/probes/wolfram/period_three_language_notebook.wl), unchanged (`ee69864b…`).
- Shared store: notebook, receipts, pins and dry run in `cited/local/period-three-language-nb2-20261108.tar.gz`, 63,607 bytes, SHA256 `6e4877878294b479496049a849155fd35818ea26a46448697a0df93573e6df99`.
- nb1 (`b8f34b86…`, old essay `bbdb8f41…`, pack `d47c3bf3…`) is superseded. A first nb2 attempt failed before the kernel started, with a Wolfram licence error; its receipt is kept outside git.

**Post script.** `post.sh` lives outside git. It refuses unless the notebook, source, abstract, title, essay and headlines match their pins and the verifier is still kit `5fb59158`, image 18. The original nb1 `post.sh --dry` passed; its essay pin is now stale and must be refreshed with the rebuilt notebook.

**Headlines (10).** `no_pattern3`, `col1_011`, `free_bits_011`, `col1_001`, `free_bits_001`, `C3r011_of_C3w`, `not_eventually_011_of_C3r`, `C3g001_of_C3s`, `not_eventually_001_of_C3g`, `no_eventual_period_three_of_C3g`.

**Mutants.** All nine rejected ([output](../../../../tests/probes/swarm/sw02/block9/mutate.out)). Certificates come from [`gen_cert3.py`](../../../../tests/probes/swarm/sw02/block9/gen_cert3.py) ([output](../../../../tests/probes/swarm/sw02/block9/gen_cert3.out)). The research context is in [Block 9's report](../../../LOCAL-BLOCK9-LANGUAGES-20261108.md).

**Prior art in the packet.**
- `rule30-open`'s `ThreeRuns` and `ConstrainedLeft001` (001, a different word restriction; no independence of the open propositions is claimed), and its notes `reading-constraints.md` and `constrained-left-halves.md`.
- The kit's `Rule30PeriodFourSkeleton`, `Rule30EtherThreeSkeleton` and `Rule30PeriodTwoLanguage`.
- Nothing for 011 in Lean was found anywhere.

**Not done.** The full catalogue build. The kit branch is not pushed and the PR is not opened.
