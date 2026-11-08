# S-04 release review

GPT GC2727/GC2728, 8 November2026. Owner requests refreshed S02 and first-draft S04. Research continuation stays parked.

**Verdict: mathematics, both Lean sources and the existing kernel/notebook receipts PASS. One prior-art repair applied. Release awaits Local's notebook/essay-pin refresh for the corrected attribution.** No Lean, headline, abstract, title or driver change; nothing posted. S02's separate nb2 release gate is cleared in its [review](GPT-S02-RELEASE-REVIEW-20261108.md#final-refreshed-release-read--gc2728).

## Carrying mathematics and formal source

I read the complete741-line kit module, compared the portal proof body after normalizing only its imports/namespace/open/public-section wrappers, and checked the actual pinned kit definitions. The proofs match GC2690's carried statements, with the following interfaces explicit.

- **Chart:** the endpoint is the pair at depths1/2 at tick2j+1. `cone_chart` needs j+n≤S; `peel_chart` needs t+d≤S, with black depth1 at every even tick through2S. `zpair_back` has the correct depth orientation and the boundary pin uses the preceding even tick. Binary endpoint symbols require the next even check. No right-half assumption enters this chart.
- **SEP ⇔ QN:** the endpoint is2 when f is black and1 when f is white, so hard-core means no adjacent white free bits. `sep_QN` uses the kit's finite-peel-rank exclusion. In the converse, an inverse constant from N on has every positive peel zero from N on. Reading the chart at even tick2N makes the shifted Theta row white at depths≥2N+4. `two_step_shift` identifies that row with Theta of the shifted free bits, which remain in the same class. This is a valid simpler converse than the earlier rotated-stream presentation.
- **The remaining class:** `QN_eventually` moves past any initial exceptions. Failure to be eventually free of white pairs is exactly `InfWhitePairs`, classically; hence `Q01_iff_sep_and`. This does not settle whether a finite constrained row in that remaining class exists. `sep_Q01Gap` uses only the next-white consequence of GapOK for the complemented free stream, then the kit's existing CQ01Empty implication.
- **LR1 phase:** the center is black at even ticks; the word is sampled at white ticks2s+1. If its sampled value is black, the next sampled value is white. Conversely every no-adjacent-black word w is realized by x0=false, r(2s)=!w(s), r(2s+1)=false; the inductive invariant keeps both consecutive column values. Thus its complemented word lies exactly in QN's class. The forced row is Theta of that complement in the kit's black-start convention, so the historical white-start one-tick repair is unnecessary. This constructs one column with arbitrary input, not an arbitrary compatible full right half. The actual-right-half implication uses its own column2 history and is valid.
- **Finite dictionary:** the converse retains all endpoint cells through depth2(n+ℓ)+1, the light cone of the last even check. Constant c=2 gives exact width2n+2; c=3 gives exact width2n+3 with both top cells black. The ℓ=1 case needs no extra zero pair, and the proof handles it. Survival includes the final check; negating it gives death by that tick. Exact width, odd top-two guard and n≥7 are all present in `DeathBounds`.
- **At-most-width bound:** take the actual last black depth m≤W. Small m uses the kit's width16 bound32. Even large m uses the exact-width clause. For odd m, two ticks later the width is m+2 and its top two cells are black, while even-check phase is preserved. The resulting bound is2+2(m+2)−2=2m+4≤2W+4. No converse from this weaker uniform bound to BWH is asserted.

The actual theorem types in the notebook and both Check receipts match these statements. Both receipts pass164 replayed constants and17 headlines, with importsStatements true, no reasons/new axioms and only propext/Classical.choice/Quot.sound. These are Local's builds read by GPT; no new Intel compile is claimed. Both kit-integration patches apply cleanly to main48d8fbbc. Full catalogue build remains unperformed and explicitly disclosed.

## Controls and independent small replay

The kernel controls show width19 start272125 survives every even check through36 despite a white cell at depth18, and width14 start11083 survives through30. Therefore dropping the odd top-two guard or lowering the even threshold to n=6 is false. Python independently reproduces death ticks38/32, all136 peel-chart pairs at t+d≤15 for11083, and layer counts2,3,5,8,13,21. This is a cheap exact replay of the notebook's worked cell, not a new census.

All ten recorded mutants are rejected. Three fail by `decide` on false finite statements. Several other failures are proof/type failures; their rejection alone would not refute a stronger theorem. The explicit controls separately refute the two dropped guards and the wrong sampling phase. In particular the failed2W+2 proof mutation does not establish that2W+4 is optimal. The packet makes no such optimality claim. The larger n=5..9 margin table was source/output-read, not recomputed by GPT, and is prior known data independently reproduced by Local.

## Prior-art correction

I read the complete external `WedgeLadderQ01.lean`, both `WedgeLadderQ01.md` and `WedgeLadder.md`, the linked finite-dictionary simulation and its linked left-half/forced-run notes, at immutable [f877f5afd5609373e2df1639e943d04e3a56e83b](https://github.com/lhallee/rule30-open/tree/f877f5afd5609373e2df1639e943d04e3a56e83b), still that repository's head. The chart, BinaryCTS⇔Q01, Q01⇒SEP and BWH⇒Q01 are correctly credited already.

**Additional exact match found:** [WedgeLadder.md's finite-horizon section](https://github.com/lhallee/rule30-open/blob/f877f5afd5609373e2df1639e943d04e3a56e83b/Rule30Open/PeriodTwo/WedgeLadder.md) already states widths2n+2/2n+3, the top-two-black guard, and horizons2W/2W−2. It explicitly says that finite form is not in Lean and checks it through n=12. Its table also contains the same n=5..9 horizons. This is substantially more precise than an approximate width/horizon remark. The interpretation is known mathematics; S04 supplies its formal proof in both directions and its stated at-most-width consequence.

I corrected the essay, PR body, catalogue row, README, delivery tracker and PRIOR-ART to credit that source and separate formalization from a new interpretation. The original preregistration is preserved with a dated correction appended. Lean and abstract are unchanged. No contrary match for the QN class, LR1 or SEP⇒Q01Gap was found in these sources or current kit/portal/open-PR searches; this is scoped source comparison, not a universal novelty certificate.

Closed PR76's full current conversation, body and empty review-summary list were read separately: the maintainer did request the Q01 relations; the packet accurately answers that request. Its head is fa511089735aa73643560165f1cc2dceffa2420c. No message or PR comment was posted.

Exact external source hashes: WedgeLadderQ01.lean `90abfb94530f0a2d5b50e8e4457cf0191c24a477183e880885c0a520b21adcc5`; WedgeLadder.md `b4c99885b6abeed8336cbaf262eb6d8d6d28274fe60514dd863d1d711f819689`; WedgeLadderQ01.md `4b1b3238d6642ff5a71848529c2b2977250734d0996949ca2c8e44abba471b30`; computations/wedge_ladder.py `794cbb1ca6e044d4ec00352031b2e892ce394499123c4b412c9edfebc56b8f6d`.

## Artifact read and remaining release gate

Downloaded and digest-verified `cited/local/separator-q01-20261108.tar.gz`,525,975bytes, SHA256 `9ac43baa5f82ae44f651f38a7362a522309db710b2e6818382b814367a5e6319`. Nb1 is187,824bytes, SHA256 `2f09ee52487c3024c496e12f40dc4a40377b11b5f69630682c81ce7e747365aa`. Without evaluating Wolfram code, I decoded its actual iconized source and Abstract, matching the reviewed files byte for byte; its copied old essay and driver match their digests. All six actual output strings match the receipt's digests. The worked output, kit=True, LeanEnvironment, headline types/axiom sets and KernelChecked164 agree. RESULT OK14.2s, zero Message cells, no public home/scratch paths. Internal handler events are not zero and are not represented as zero.

Nb1 is now superseded for release because attribution text changed. Local owns Wolfram under AGENTS/TOOLS: rebuild from the corrected assembled essay with the unchanged driver; refresh private notebook/essay pins and run the dry check. Supply the new notebook, receipts and sanitized release-pin/dry receipt for a short final byte read. S04's old private dry run was reported by Local; that script/receipt was not supplied in the first archive, so it is not independently inspected here. No proof rebuild is needed for this text-only repair unless module/toolchain/verifier changes. The release hold is the concrete artifact refresh, not another mathematics review.

| Reviewed item | SHA256 |
|---|---|
| Portal Lean | `64b76f6da535c0476b73e6fb8ea912eea583577bd36235f88d0bff575a192037` |
| Kit Lean | `c73e6d777d96727aea99f8d2e4892086977c12d3c5142024c1974edb2a506a2a` |
| Abstract, unchanged | `5c037c1c4c937e4be10d59b708a7d397b54212cca31bf92851dcfe7f1db0a786` |
| Corrected essay | `c7916ca0bc7d1756b5b4ecb90b66e902ef7c3997c3be777cb4b315d2ac1c530c` |

Byte-audit results retained as shared store `cited/gpt/gc2728-release-audit-20261108.json`, 2117bytes, SHA256 `809e87420fc8e6f2694298eab22c379cd75f2a2ffbcfb6f74288c1399e2058b7`; uploaded with byte-exact readback. S04’s old notebook checks and its corrected-essay release hold are recorded separately.

## Fresh external index

Successful complete refresh2026-11-08T12:09:59.779778Z, kit48d8fbbc0d4a74ef5dd740cb76131704a6fc9167, portal updated12:09:55Z,12open PRs: two added index units, one entry plus its source, no changed/removed units. [R30-20261108-b1819c](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261108-b1819c) is externally Lean Verified,1628constants/16headlines. Abstract, receipt and all16 headline statements read: D401 black after2994; conditional sixteen-state transport and even-parity period16 preservation; all-period inward-column nonperiodicity retaining c≤−2985 and c≤−(T+P)+384. Source SHA256 `21414ffbc08f480f184a2803dcb20c5e8d86dc0e8b7f67f1fcf5fa590d0915b0`. No full proof carry or new local verification. These fixed-seed diagonal results do not supply a general finite-start separator/twin theorem and do not change either packet's review.

My own pull: the same shared4→7 input-history constraints, retained and parked while submission reviews finish.
