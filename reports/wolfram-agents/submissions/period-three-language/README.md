# The column-1 language beside a period-3 center (Block 9; queue row S-14)

**Status: release review GC2759: proof and nb1 PASS; five text repairs accepted (L1605); the corrected essay `3810a902…` needs notebook nb2, new pins and a dry run, then GPT's short final byte read. Not posted; the owner's word is needed to post.** The nb2 build is blocked for now by a Wolfram licence error (kernel slots held by other sessions' MCP kernels).

| Form | File | sha256 | `Check` |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) | `4edf326d1f0ed3bb…` | pass at the verifier's kit `5fb59158`: 142 constants, 10 headlines ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30PeriodThreeLanguage.lean`](Rule30PeriodThreeLanguage.lean) | `71ac7331952cf40e…` | pass at kit main `1487f31` with the patch applied: 142 constants, 10 headlines ([receipt](check-kit-1487f31.json)) |

The kit form is byte-identical to the module in the local kit branch `b9-period3`, which has four commits ending at `0318b3d` (the catalogue row with GC2759's wording) and is not pushed. [`kit-integration.patch`](kit-integration.patch) holds its import line and catalogue row. The row's `PORTAL-ID` is filled in after posting.

**Texts.**
- Front matter: [`title.txt`](title.txt), [`abstract.txt`](abstract.txt) (216 words, `60fbdb2a…`), [`headlines.txt`](headlines.txt).
- Essay: [`essay-prose.md`](essay-prose.md) (`69e62b8b…`) and [`essay.md`](essay.md) (`3810a902…`, after GC2759's repairs; nb1 was built from `bbdb8f41…`), assembled by [`assemble_period_three_language_essay.py`](../../../../tests/probes/wolfram/assemble_period_three_language_essay.py).
- Kit PR and predictions: [`PR-BODY.md`](PR-BODY.md), [`prereg.txt`](prereg.txt).

**Notebook nb1.** SHA256 `b8f34b86fc82e3d788a8aa351560d264608f572d6379f88f2e9836df59ca7854`, 189,195 bytes; RESULT OK in 42.1 s at 2.4 GB peak.
- Every gate passes: 6 output cells, no message cells; the first cell equals the Python replay ([`period_three_language_replay.py`](../../../../tests/probes/wolfram/period_three_language_replay.py)); the Abstract cell equals `abstract.txt`; the icon payload equals the portal source byte for byte; the axiom sets match `Check`; KernelChecked at 142 declarations.
- Driver: [`period_three_language_notebook.wl`](../../../../tests/probes/wolfram/period_three_language_notebook.wl).
- Shared store: notebook, receipts, pins and dry run in `cited/local/period-three-language-nb1-20261108.tar.gz`, 63,442 bytes, SHA256 `d47c3bf3880c69f43b62da9f8d00705e49727ed829be1641a2ace500532e81e9`.

**Post script.** `post.sh` lives outside git. It refuses unless the notebook, source, abstract, title, essay and headlines match their pins and the verifier is still kit `5fb59158`, image 18. `post.sh --dry` passes.

**Headlines (10).** `no_pattern3`, `col1_011`, `free_bits_011`, `col1_001`, `free_bits_001`, `C3r011_of_C3w`, `not_eventually_011_of_C3r`, `C3g001_of_C3s`, `not_eventually_001_of_C3g`, `no_eventual_period_three_of_C3g`.

**Mutants.** All nine rejected ([output](../../../../tests/probes/swarm/sw02/block9/mutate.out)). Certificates come from [`gen_cert3.py`](../../../../tests/probes/swarm/sw02/block9/gen_cert3.py) ([output](../../../../tests/probes/swarm/sw02/block9/gen_cert3.out)). The research context is in [Block 9's report](../../../LOCAL-BLOCK9-LANGUAGES-20261108.md).

**Prior art in the packet.**
- `rule30-open`'s `ThreeRuns` and `ConstrainedLeft001` (001, a different and incomparable language), and its notes `reading-constraints.md` and `constrained-left-halves.md`.
- The kit's `Rule30PeriodFourSkeleton`, `Rule30EtherThreeSkeleton` and `Rule30PeriodTwoLanguage`.
- Nothing for 011 in Lean was found anywhere.

**Not done.** The full catalogue build. The kit branch is not pushed and the PR is not opened.
