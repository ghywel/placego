# Two of every three first checks are balanced (queue row S-03)

**POSTED, L1577.** [R30-20261106-bdd993](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-bdd993): **Lean Verified**. Submitted 20:50Z, checked 20:51:06Z. Kernel replay passed, 98 constants, ten headlines, standard axioms only, verifier image 18, kit `5fb59158`. Kit PR: [WolframInstitute/Rule30PrizeKit#209](https://github.com/WolframInstitute/Rule30PrizeKit/pull/209), branch `first-checks` at `2bd9391` on the fork, base main `9d837cd5`. The posted notebook is nb2, sha256 `41b8e52ab8cb8ce458eb9ff73114317e6ba828285862169640a55601cd87f175`, 135,928 bytes, built from GPT's corrected essay `d4a87572…`; evidence `cited/local/first-checks-nb2-20261106.tar.gz`, 32,493 bytes, sha256 `debb99129882655185607b78a66d1e05d260050a8d1ed3a613ea5281a48682d7`. **GPT's exact-byte read of nb2 was not done before posting:** the owner chose to post without it, in chat. Local's own checks are a self-check: the embedded source decodes to `fc0623cd`, the abstract matches, output cells 1, 2, 4 and 5 equal nb1's, cell 3 holds the same constants in another order, and cell 6 differs only in its temporary module name.

| Form | File | sha256 | `Check` |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) | `fc0623cdeb8d4ed9…` | pass at the verifier's kit `5fb59158`, image 18: 98 constants, 10 headlines ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30FirstChecks.lean`](Rule30FirstChecks.lean) | `18a01ef281d8dda9…` | pass at kit main `9d837cd5`, with the patch applied: 98 constants, 10 headlines ([receipt](check-kit-9d837cd5.json)) |

**Texts.** [`title.txt`](title.txt), [`abstract.txt`](abstract.txt) (196 words, `4fae6837…`), [`essay-prose.md`](essay-prose.md) (`83faa095…`), [`essay.md`](essay.md) (`d4a87572…`), [`headlines.txt`](headlines.txt), [`PR-BODY.md`](PR-BODY.md), [`kit-integration.patch`](kit-integration.patch).

**Original notebook nb1 (provenance verified GC2704; superseded by the prose correction, rebuild pending).** Sha256 `91a117e4c1e8323e0a6caeefd669306e7aef4dac0c3c0b28f46f63efa6b25ca6`, 135,296 bytes, built at the verifier's kit under `run_capped.py`: RESULT OK in 20.8 s. Six output cells, no message cells, 98 declarations accepted by the kernel; the icon payload equals `Rule30Submission.lean` byte for byte, the Abstract cell equals `abstract.txt`, and the first cell equals the plain Python replay. Notebook and receipts are in the shared store: `cited/local/first-checks-20261106.tar.gz`, 33175 bytes, sha256 `5c132b9427cf2f4bae34dc9df4144102f09467b244df8cf5c6b1ca7dcf769501`.

**Post script.** `post.sh` lives outside git and refuses unless the notebook, source, abstract, title, essay and headlines match their pins and the verifier is still kit `5fb59158`, image 18. `post.sh --dry` passes.

**Theorems.** `two_tick`, `check_xor`, `four_sum`, `pair_count`, `overlap`, `adjacent`, `distance_two`, `two_of_three`, `first_check_count`, `first_check_balanced`.

**Provenance.** CT-2's Theorems 1 and 2 and Corollaries 3 and 4, carried in GC2690; the complete new Lean and its actual kit definitions were read and carried in GC2704. The Lean differs from the hand proof in one way: it uses CT-2's own remark that the bounds follow from pair probabilities and marginals. So `distance_two` is one `omega` over the overlap bounds at three indices, not a case split on majority signs. A linear program confirmed first that the bound is exactly what those inputs give.

**GC2690's repairs.** `Theta_dep` is cited alongside `tri_odd` for fixing a cell while the newest bit changes. The two-tick identity is credited to the project's record of 8 October (GC486), with only the consequence on free words as new. There is no tightness sentence; the essay gives the exact `(1 + p_(n-2)) / 4`. Everything is stated for all even pins black. The correlation keeps `(1 + c_(n-2)) / 4`, not `1/4`. The essay says this qualifies a random-function picture and does not refute one. Survival conditioning is excluded, in the abstract and in section 6.

**Controls.** No `sorry`. [Eleven mutants](../../../../tests/probes/wolfram/first_checks_mutate.out) are rejected, including `23` for `24` and `39` for `40`. [The brute-force replay](../../../../tests/probes/swarm/sw02/block7/first_check_replay.py), written before the Lean: 0 failures to n = 14, with rows counted directly to n = 11. The Wolfram cell agrees to n = 12, rows to n = 6.

**Prior art searched.** `known_find` on two-tick, pair law, check sum, first check, composite check, free cube, consecutive check, even check, count_constrained, first_check_count, pair_count; greps of portal and PR sources for statements about `Theta f (2 n + 1)`; `rule30-open` by Block 2's table and its catalogue. No bound on these checks found. Hits on correlation (62), balanced (144) and survivor (23) were sampled by source grep, not read one by one.

**Not done.** The full catalog build. Corrected-essay notebook rebuild, new notebook/essay pins and dry run; GPT has completed the Lean read. The PR's portal id is `PORTAL-ID` until the entry exists. The Gram-matrix sharpening and the conditioned checks are not attempted.

**GC2704 text repair:** raw correlation is compared with the product of means through the exact covariance; the abstract period-three pattern limits frequency, without claiming an optimal constant or a Rule30 realization. The catalogue row now carries contributor credit and a PORTAL-ID placeholder to fill after posting. Neither Lean file, abstract, headline list nor computational cell changed.
