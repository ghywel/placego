# Cloud's error-edge submission and proposed kit PR: review

5 November 2026, GC2685. Owner-requested review of CL747 as packaged by Local L1553 at shared main `52bf32e7`. **Mathematics and corrected texts cleared; exact revised release checks remain with Local.** No theorem or proof body changed. There is no public error-edge PR yet; this verdict concerns the prepared source, prose and integration patch. GPT's subagent read is a self-check, not a separate worker's carry.

## Four answers

**1. The table matches the Lean; two prose summaries did not.** With old edge `m+2`, new edge `m+2+d` and new parent `m+1+d`, the six theorem statements have the advertised conclusions at t+1 or t+2. In particular `jump_four` has no white-new-parent hypothesis. `jump_five`, `jump_six` and `jump_seven` do. Essay §§3 and 5 dropped that hypothesis for jumps 6/7 and overstated how completely the jump determines the stall. Corrected: after 6/7 a white new parent forces at least two stalled updates; a black new parent gives an immediate heal. After 4/5, healing is **by** the second opportunity, not necessarily exactly then.

The existing 3,000-tick control supplies concrete counterexamples to the unguarded summaries. At t=615 its edge follows 750→756→758: jump six, black new parent, immediate further heal. At t=807 it follows 887→894→895: the same issue after jump seven. No theorem is contradicted. The Python replay reproduces all 1,112 heals and zero violations of the actual guarded laws. It tests transitions t=0,…,2998, using the final stored row for the t+2 conclusions.

**2. “Never retreats” is correct when both edges exist.** `edge_le` assumes an edge at t and another at t+n. `edge_heal` proves agreement through the old edge; it does not assert existence of a new finite edge. This distinction is now explicit. The generic heal criterion needs index at least one; the post-heal laws need old index at least two. Arbitrary recurrence arrays can differ at wheel zero. For physical black-anchored rows, wheel zero agrees always and wheel one agrees from tick one, so the latter guard holds whenever an edge exists after that tick.

**3. Prior-art credit needed one further correction.** The exact interior Boolean test is already `Rule30LightCone.rule_flip_right_iff`, introduced in [PR98](https://github.com/WolframInstitute/Rule30PrizeKit/pull/98): changing the right input flips the output iff the central input is white. At an error edge, the two earlier inputs agree and the last inputs are complements; consequently this is precisely the interior `heal_iff` test after changing coordinates and exchanging difference with equality. The boundary wheel-one OR rule is handled separately here. This mechanism is **known, reproved here**, rather than a new white-parent converse.

`Rule30UniversalLeftSide.child_white` also already contains the white-parent one-step memory identity. Its array C is abstract; being a strip is an application, not a theorem hypothesis. `child_same` and `child_white` use persistent parent alignment, whereas the error-edge package states the instantaneous criterion and derives the needed prefix agreement. `Rule30HealingBound` supplies the previously credited black-parent recruitment mechanism. The essay, Lean headers, PR body and catalog patch now say this. No matching statement of the six post-heal laws was found in the inspected sources; the novelty language is limited to that search.

The empirical speed remains background, not an assertion about arbitrary pairs or a new speed theorem. The primary source, Wolfram's [1986 paper, p.136, equation (5.2)](https://content.wolfram.com/sw-publications/2020/07/random-sequence-generation-cellular-automata.pdf), reports 0.2428±0.0003 and explicitly discusses exceptional initial configurations. The [NKS difference-pattern note, p.949](https://wolframscience.com/nks/notes-6-3--properties-of-difference-patterns/) also treats it as an observed average. The revised prose does not universalize it.

**4. The physical bridge is valid after aligning anchors.** `Ld_recurrence` requires only an initial white half-line; it imposes no finite-support restriction to the right. Translating the two leftmost black cells into alignment makes the two separately anchored arrays a comparison in the same frame. This alignment is now stated. The offset-three example is reported as that particular pinned example, not a claim that every nearby second cell fails as a control.

## A useful logical control and its failed first candidate

The distinction between healing a cell and having a later edge is substantive for the allowed arbitrary right tails. Hand control (**PROOF-SKETCH, GPT self-check; not an added Lean theorem**): initial arrays `a=(1,0,1,1,1,…)` and `b=(1,1,0,0,0,…)` both become `(1,1,0,1,0,0,…)`. At indices 0,1,2,3 direct substitution gives 1,1,0,1; at every index ≥4 the input triples are respectively 111 and 000, both giving zero. Thus their edge at one disappears. In contrast, a largest initial differing index D between finite rows forces a difference at D+2 next tick, since the higher inputs agree.

An initial proposed control, integer codes 1 and 3 both mapping to 7, was **REFUTED by the check**: they map to 7 and 11. That failed assertion is retained in the evidence. It occurred after the successful replay and does not invalidate that output; the constant-tail calculation above is the corrected control. No published finite-row coalescence claim is made.

## Source and release evidence

The complete kit/portal index refresh finished at **2026-11-05 18:45:47.314030 UTC**, kit `5fb591588cfa869bfdc47946799b5ddd70a903d1`, portal updated 18:45:32Z, thirteen open PRs. Current `lean/`, `equivalents/`, catalogs, portal sources and open PR sources were searched. The matching recurrence, physical bridge, healing, masking, light-cone and aligned-parent statements were read. Separately read the bodies and empty issue/review/inline discussions of closed PRs 98, 103 and 141, and their relevant exact-head proof sections:

| PR | Exact head |
|---|---|
| 98, light-cone flip criterion | `4ee6084b6d13c6233eb4578f3575dd03a26c26b5` |
| 103, healing bound | `3d2d609facefe45d86b02c3cd418f68a9aa28858` |
| 141, universal left side | `3b4b6ed6ef5883e366243952d0b11d87a2da1006` |

Unrelated new portal entries and Cloud/Local research blocks were received, not fully reviewed here. The refreshed portal confirms the earlier right-wall entry c15ef5 is Lean Verified, Human Verified and Kit Contribution. That is separate from the unposted error-edge package.

Local's M5 compiler/checker receipts pass the old comment headers with **56 constants, 14 headlines, no new axioms**, using only `propext` and `Quot.sound`, at kit main `5fb5915` and verifier kit `722a0c51`. Nine mutant rejections were read. GPT read both complete release proof bodies, verified their equivalence and that this review changes only comments, and replayed the existing finite Python control under a ten-CPU-second/twenty-wall-second stop. No fresh Intel Lean build, Wolfram execution, full-catalog build or public PR CI pass is claimed.

The actual archived notebook summary and output cells were read: `cited/l1553-error-edge/nb1-receipts.tar.gz`, 4,061 bytes, sha256 `e8a9f4b51c284d607953f82f15e2d50747e2600c9157fb6655dfba6427156550`. All gates pass, six Output cells, zero Message cells, KernelChecked 56; first cell agrees with the replay. Its notebook `65fc5172…` certifies old essay `850800df…`, and must be rebuilt after these corrections. GPT did not independently inspect or execute that notebook file.

Review evidence: `cited/gpt/gc2685-error-edge-review-20261105.tar.gz`, 106,190 bytes, sha256 `73de7acec5c66b5b7d2225a37324eebeef498205f8d68d3923a9ee39700ca50f`. It preserves prior PR/source receipts, the complete index receipt, replay output including the rejected first control, and reviewed hashes. Index stamp sha256 `81b87c999972161d387f0c59ee1caffab42bd9e3bd68f84379718290188daddf`; checked-index sha256 `eeffb649e8da5531f1052d939444a2c44f72f854f4f3063a043a39d20448cb50`.

## Local's exact next step

| Revised artifact | sha256 |
|---|---|
| Kit Lean, header-only change | `98a743d802cfd14da8a324084f7e6c7a2088888d055ca7854438b577bc19a56e` |
| Portal Lean, header-only change | `e77266a078e5a3b6c625693a15ee059c1dac11658e4d3d23c6c866d784a2c97b` |
| Essay prose | `e0d4c646ad9f311d6a73584175188530495719ee6ba9f3d3390cc8d1c53b64ca` |
| Abstract, 228 words | `a5a02c1fb7b549a619579391a40df3a8ff2ea939eb99b8179177b8f666888fb2` |
| Generated essay | `9d5b5cba58cd4f5cdcc26084380473dcd25bce174bfecc24f6efae77adc0fd8b` |
| Kit integration patch | `2b985125f44a880f297ffd8c4b22f850889eb4d08fa77a2c628c0bbcce793ab2` |

Repository checks pass: ledger uniqueness, relative links, whitespace, conflict/privacy scan, portal embedding and pin, unchanged proof bodies, kit/portal body equality after namespace/open adaptation, and patch application. No TeX changed.

Rebuild with the existing notebook driver on these bytes; recheck the exact commented sources, established gates and live-verifier dry run. The revised catalog/import patch applies cleanly to kit `5fb59158`; validate the added module's import integration. No whole-catalog pass is claimed. With passing exact-source release checks and no substantive change, GPT clearance stands without another prose round. Local alone posts on the owner's instruction. Both GPT schedules remain paused; no research job is queued.
