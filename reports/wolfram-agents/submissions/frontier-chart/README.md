# An immortal frontier is a finite row (queue row S-01)

**PACKAGED, REVIEWED, NOT POSTED (L1574 / GPT GC2703).** [Release review](../../../GPT-S01-RELEASE-REVIEW-20261106.md) PASS for the frozen proof, essay, notebook and receipts. Awaiting the owner's word; Local freshly checks verifier kit/image before posting. Local alone posts. Block 7 of [WARM-LEADS](../../../../WARM-LEADS.md).

| Form | File | sha256 | `Check` |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) | `9a5e9e81cb1fc276…` | pass at the verifier's kit `5fb59158`, image 18: 58 constants, 9 headlines ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30FrontierChart.lean`](Rule30FrontierChart.lean) | `4c90192e4166d7a3…` | pass at kit main `9d837cd5`, with the patch applied: 58 constants, 9 headlines ([receipt](check-kit-9d837cd5.json)) |

**Texts.** [`title.txt`](title.txt), [`abstract.txt`](abstract.txt) (191 words, `6861bec4…`), [`essay-prose.md`](essay-prose.md) (`c284b979…`), [`essay.md`](essay.md) (`803575e0…`), [`headlines.txt`](headlines.txt), [`PR-BODY.md`](PR-BODY.md), [`kit-integration.patch`](kit-integration.patch).

**Notebook.** Sha256 `6caf95da0f6c142a9522af6545a0754db944a6823d94edbf58698349752b777c`, 98,288 bytes, built at the verifier's kit under `run_capped.py`: RESULT OK in 14.5 s. Six output cells, no message cells, 58 declarations accepted by the kernel; the icon payload equals `Rule30Submission.lean` byte for byte, the Abstract cell equals `abstract.txt`, and the first cell equals the plain Python replay. The notebook and receipts are in the shared store: `cited/local/frontier-chart-20261106.tar.gz`, 28232 bytes, sha256 `ac0b19b29b4f976b2563135382698170dd42420714cae33a512a3573259b2bde`.

**Post script.** `post.sh` lives outside git and refuses unless the notebook, source, abstract, title, essay and headlines match their pins and the verifier is still `5fb59158`. `post.sh --dry` passes. The verifier can move; if it does, `Check`, the notebook and the dry run must be redone there.

**Theorems.** `mortality_of_Q01`, `mortality_iff_Q01`, `budget_iff_Q01`, with `Z_rec`, `chart_interior`, `chart_wall`, `zrow_chart`, `inX_start`, `finSupp_start`.

**Provenance.** The chart is GC2688 Appendix A and GC2690, read by GPT; the Lean was carried in GC2697. `abstract.txt` is now one paragraph, for the notebook's front matter, with GPT's wording unchanged. The Lean follows the chart with time measured from the frontier's length, so it has no parameter r. `Legal` is used only to know the first frontier is nonempty.

**Controls.** No `sorry`. [Nine mutants](../../../../tests/probes/wolfram/frontier_chart_mutate.out) are rejected. [The Python replay](../../../../tests/probes/swarm/sw02/block7/frontier_replay.py) and the Wolfram cell agree on all 10,922 legal frontiers of length at most 7: 28,560 interior and 5,208 wall cells, no mismatch.

**Prior art searched.** `known_find --new` at kit `9d837cd5`, portal 19:27Z, 30 open PRs: nothing added since the last complete check. Terms: mortality, immortal, `Q01_of_mortality`, converse with mortality, frontier with mortality. Closed PRs 75, 76, 85 read. `rule30-open` at `f877f5af` lists the converse open. The essay credits David Condrey, and G.P.J.W. Quint with Gemini.

**Not done.** The full catalog build (`bash build_all.sh`); it was not required before. GC2690's finite bound 2N = death(rho). The PR's portal id, which is `PORTAL-ID` in `PR-BODY.md` until the entry exists. The fork update before the PR. Queue row M-1 (the kit's "not known" sentences) travels with the PR.
