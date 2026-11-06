# An immortal frontier is a finite row (queue row S-01)

Block 4 of [WARM-LEADS](../../../../WARM-LEADS.md). Status: **Lean, kernel-replayed at the verifier's kit; GPT carrying read PASS (GC2697); not posted.** Nothing here goes out without the owner's word.

| File | What it is |
|---|---|
| `Rule30FrontierChart.lean` | The kit-module form, for a pull request |
| `Rule30Submission.lean` | The portal form: the same proofs, no double quote and no backslash |
| `headlines.txt` | Nine headline theorems |
| `check-5fb59158.json` | `Check.lean`'s verdict, `pass`, at the verifier's kit `5fb591588cfa869bfdc47946799b5ddd70a903d1` |
| `title.txt`, `abstract.txt` | Draft |

**Theorems.** `mortality_of_Q01`, `mortality_iff_Q01`, `budget_iff_Q01`, with `Z_rec`, `chart_interior`, `chart_wall`, `zrow_chart`, `inX_start`, `finSupp_start`.

**Provenance.** The chart is GC2688 Appendix A and GC2690, read by GPT. The Lean follows it with time measured from the frontier's length, so the chart has no parameter r. `Legal` is used only to know the first frontier is nonempty.

**Not included.** GC2690's finite bound, 2N = death(rho), which needs the failed-scan extension. The essay and notebook, which Block 7 builds. A pull request; the kit's README sentence "the converse is not known" would change with it (M-1 in the queue).

**Controls.** No `sorry`. Axioms `propext`, `Classical.choice`, `Quot.sound`. Replacing the wall's `||` with `&&` in `chart_wall`'s statement makes the file fail to compile, so the wall cases carry weight.

**GPT review (GC2697).** [Carrying verdict and exact source pins](../../../GPT-BLOCK4-BRIDGE-HISTORY-20261106.md). The proof files are unchanged. The abstract’s final sentence now states the all-length logical equivalence explicitly. GPT read Local’s actual Check receipt and the complete sources; no new Intel build or public verification is claimed. Block4 is complete; Block7 still supplies essay/notebook and exact-source release checks before an owner-authorized post.
