# Morning kit/portal update and follow-on reviews — GC2679–GC2680

5 November 2026. Owner-requested review, starting at shared main `51404f57`. GPT owns the update and source review; Local and Cloud retain their research and posting decisions. Both GPT schedules remain paused.

## Kit and portal

The successful complete `known_find.py --new` refresh finished at **10:46:50 UTC**, with portal snapshot **10:46:45Z**, kit main **`556e8323937e3337aa14b5dd8ecd9ed5002fde79`**, **164 entries** and **12 open PRs**. The delta from the preceding complete check is four additions (the two four-fronts kit modules, the portal entry and its source) and one changed umbrella import. There is **no further new external submission** in this delta, including no additional response to the synthesis-essay invitation. The earlier external `30d8ae` remains recorded.

| Entry | Lean Verified | Human Verified | Kit Contribution |
|---|---|---|---|
| [309041, universal left side](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-309041) | Yes | Not listed | Yes |
| [458f3b, four left sides](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-458f3b) | Yes | Not listed | Yes |
| [9aa447, forced front](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-9aa447) | Yes | Not listed | Yes |
| [30d8ae, external coincidence follow-up](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-30d8ae) | Yes | Yes | Yes |

[PR156](https://github.com/WolframInstitute/Rule30PrizeKit/pull/156) closed at 00:04:08Z with null GitHub merge metadata. Its two modules nevertheless landed byte-for-byte on main; “closed” is not a rejection here. The exact PR head is `affaccedf894b92e9107053b904f0bcb396a6901`. Separate reads of the conversation, inline comments and review summaries found all three empty. The twelve still-open PRs have no new source delta in this refresh.

The [main four-fronts source](https://github.com/WolframInstitute/Rule30PrizeKit/blob/556e8323937e3337aa14b5dd8ecd9ed5002fde79/lean/Ruliology/CellularAutomata/Rule30FourFronts.lean) matches Local’s comment-cleaned package. SHA256:

- `Rule30FourFronts.lean`: `eaf14e66e18e82b5d0eb2cf4b5930d7f7584bc17d32bb2b8714fdef8ace8927a`.
- `Rule30FourFrontsBase.lean`: `50992f78bc7d14e1497f92098337b98c323038c1490bb62f8169b436b4aa2c38`.
- Public portal source: `134d62fba8e16f30912b9ca505df7e96bd80f37f73d984723c4e0e8dd8a5f911`, exactly the approved portal Lean.

L1526’s essay change is exactly deletion of the stray “so” in “Thus so the same recursion”; read and accepted. It needs no further submission. The official public replay reports 681 constants and eleven headlines. This review does not claim a new build or a fresh Wolfram notebook execution.

Refresh file SHA256 values:

| File | SHA256 |
|---|---|
| stamp.json | d6687a0059db64db4ac488d22f1fd189668a908abc6631e4fd1bd22381af104f |
| checked.json | d69fbb9cfc911acc22de3667d1b7ed34b2c1290afe3dea40a004742565202e87 |
| portal.json | 16170392808054a2505e9a53dfba774683c6da7a90f8ccdab503095af02c8970 |
| prs.json | 6a8934752ccaeaa580b042963db3153fbe7e4d40a089d9f40d3c4702db04a0a2 |

The refresh files, exact-head comparison, two kit modules and static projection check are archived in the shared store at `cited/gpt/gc2680-morning-evidence.tar.gz` (197,444 bytes), SHA256 `f16eae655b7a8005ba32baeeeabf203f5bbc5047805018f70683a62a9ae376c7`. The archive includes an individual-file manifest; raw-body upload and byte-exact download were verified. PR API responses were read directly, not retained as raw responses.

## Cloud: what stands and what changes

The generic period-32 transport, phase budget, fork separation and walk composition in [FiveFrontsBase](wolfram-agents/submissions/five-fronts/cloud-Rule30FiveFrontsBase.lean) support the reviewed headline statements. The [five-strip package](wolfram-agents/submissions/five-fronts/README.md) gives own-clock deadline **334,181** through wheel **165,749**; the [sixteen-strip package](wolfram-agents/submissions/sixteen-fronts/README.md) gives **1,798,274** through **894,235**. These include the maximum phase shift of 31. No defect was found in the reviewed proof machinery. Cloud’s kernel builds are its reported evidence; this read neither rebuilds the external strip certificates nor supplies Local’s build of record or public verification.

The sixteen-strip form is not ready under the quoted kit build limits: the root module reportedly needs about 14.2 GB. Splitting declarations across files addresses peak memory but does not by itself settle the kit’s one-data-module-per-family policy. A compact evaluator or maintainer agreement about packaging is the next release step; do not launch a 14.2 GB replay under Intel’s 8 GiB limit.

The [front probe](../tests/probes/wolfram/front_law.py) and its [output](../tests/probes/wolfram/front_law.out) support the listed finite-window slopes, with these corrections:

1. **Clock convention.** The code compares the finite prefix at upper time `t` with time `t−32`. The last unequal upper tick is 1,180,062 and the first equal one 1,180,063. The corresponding actual periodic entry is **1,180,031**. A finite prefix evolves autonomously: equality after 32 steps makes the earlier state periodic, and an earlier entry would give an earlier equality. This is a source-convention deduction from the existing output, not a new simulation. Subtracting 32 preserves the later increments, window slopes and phase modulo 32; the detector’s startup floor needs separate treatment near the edge. The absolute forced-front gap becomes **612,656**.
2. **Finite range.** The post-100,000 slopes are 1.3113–1.3272. They do not prove existence or value of an asymptotic speed, exclude a limiting 4/3, or establish universality over initial configurations. B2’s limiting question remains open. The sixteen examples are the seed and fifteen specific fork perturbations. Periodic strip rows themselves begin settled on the observed prefix.
3. **Prediction accounting.** P-C1 passed its range test and failed its declared 0.01 trend tolerance: first-to-last drift is −0.0117. Zero increments at the five tested doubling wheels reject the proposed immediate jump there; they do not exclude every asymptotic role of doubling.
4. **Exact guard.** The theorem gives `F_v(j) + s <= t`, or `max_v F_v(j) + 31 <= t` uniformly. It does not give CL739’s exact `j <= (t−31)/2` wedge. Its own maximum endpoint front, 1,798,243, exceeds twice 894,235.
5. **Counts.** The output covers 894,234 wheels and gives mean slack 0.9146. Zero-increment share and positive-slack coincidence share agree at displayed precision; white-parent wheels stop them being identical events everywhere.

**Carrying read of CL739’s local step: PROVED, hand/two-party.** Fix the final strip with its phase and define the error as actual bit XOR strip bit. Once both parents match, XORing their child updates cancels the farther parent. If the nearer parent is black, both children become the same; if white, the old child error persists. Therefore `d_k(t+1) = d_k(t) AND NOT C_(k−1)(t)`. At the parent-prefix arrival, an already matching child gives zero prefix increment; otherwise it first matches one tick after the nearer parent’s next black. If the parent is permanently white, eventual agreement with the selected branch forces the child error already to be zero. Keep this branch guard.

The full driven-error recurrence displayed by Cloud is likewise an exact Boolean identity obtained by XORing the two recurrences. The conjectural part is the proposed universal extinction speed. The next useful step is to formulate that process with the phase and arrival convention explicit, then seek an invariant for one conditional coincidence cell before another broad speed census.

## Local: the wall locks and the width-dependent cloud

The source read supports the scope of `no_AAA`, the anchored `AA`, `AB`, `BA`, `ABA` witnesses, the reset identities, the 45-cell `AB` lock, the 136-cell `AAB` lock, and the 798-window closed set. Their supplied Lean axiom receipts are local machine evidence. The row theorems retain their anchored/rain-tail and depth hypotheses; they concern already settled walls and do not prove universal capture. No new compilation was performed.

The most useful correction is also a new structural distinction: **a coarser cloud can conceal a finer lock**. The six constants in [WallLockAAB](../tests/probes/lean/TwoPairsWallLockAAB.lean), shifted right by 91, give the three top-45 codes

`27432130304288`, `27428176267484`, `27392180584198`, each twice.

All are members of `Qn` in [WallCloud](../tests/probes/lean/TwoPairsWallCloud.lean). Thus the explicit anchored `AAB` witness is already a `Q45`-cloud row. “Cloud rows cannot reach the AAB lock” is false for `Q45`; the exclusion uses the separate computed terminal clouds at widths 52, 60, 70, 76 and 92. Naming the width is essential. The static constant check has SHA256 `d9aeac24317b996040919b266688ef70042e23c0e4500f6a3fb6b5a37b1645e6`.

The [genealogy](rule30-genealogy.md#63-the-language-of-the-settled-wall-l1528l1529) now also records:

- Seeing all windows on real rows certifies those vertices, not every free-input transition or path. The width-135 escape remains a free-input path, with physical realizability unproved.
- Nine floor searches were censored. “None found within the bounded searches” is supported; exclusion of every other period through 16 is not.
- The finite departure counts are compatible with a Poisson model; they do not exclude a locked subpopulation.
- The 98.9% viability result is one-step: every next choice leaves some infinite `AAB` continuation available. It does not quantify over every future choice sequence.
- The fair-lower-state break rate is a finite-iteration surrogate. Neither its convergence nor independence/fairness of actual lower histories is proved.
- “One free letter per block” identifies the potentially branching position after `BA`; those choices need not be independent.

**Answer to L1533’s question.** Every window in this settled-wall setting already contains the top `A` or `B` reset word. The nontrivial question is whether a periodic lock needs a *distinct lower, persistent reset floor*. The two certified locks have one, and Local’s mechanism explains their shielding. Closure of a set under four input states does not by itself prove that all four states synchronize internally; the large cloud is a set-valued example of why that distinction matters. A useful next test is to quotient a candidate class by the four lower-state responses, excluding the compulsory top reset, and check for a persistent interior synchronization site. General floor necessity remains open.

## Scope and continuation

Read: current instructions, new ledger work L1526–L1533/CL736–CL739, fresh addressed flags and shared state; PR156’s separate channels and exact head; Local’s six new proof modules and relevant probe sources/outputs; Cloud’s complete generic base, probe sources/output, package descriptions, and classification/deadline interfaces. GPT subagents supplied complementary self-checks, not additional independent-worker carries. No claim is made that all external sixteen-strip data certificates were replayed.

The owner’s requested update and reviews are complete. Local has the window-width and probability-scope corrections; Cloud has the detector-time, limiting-speed and exact-guard corrections. The next research block should use these corrected statements. No posting, census, GPU job or schedule restart occurred.

My own pull: understand how a coarse cloud splits when the observation window widens, especially whether the lower reset floor is necessary for a physical periodic lock. Local’s `AAB` witness inside `Q45` makes this a concrete alternative to treating the cloud as one indivisible state.
