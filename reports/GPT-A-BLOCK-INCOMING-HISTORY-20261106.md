# Transport of the branch pair through A

GPT GC2715/GC2716, 6 November2026. Owner asks to continue the00→11 switch while preserving incoming history. GPT owns this single bounded block; no colleague work or schedule is started.

## Object and exact history interface

Take T at odd phase, two physical ticks before a black A-start R=F(T). Its first seven cells are32,64 or96: cells1–5 white, cells6–7 nonzero. A=25 lasts14 physical ticks. Retain q_t, the complete seven-cell trunk at t=0,…,14, and w_t, column8 at t=0,…,13. The exact update is

    q_(t+1) = (((q_t<<1) OR(t mod2)) XOR
               (q_t OR(q_t>>1) OR(w_t<<6))) mod128.

The head at relative ticks2,6 is black and at4,8,10,12,14 white. The endpoint must have first three cells white, which forces the next black pulse at16. Endpoint seven-cell prefixes32/64/96 select another A;56/88/120 select a gap3 and hence a candidate E-start. A single gap3 does not certify the rest of E.

The incoming word is constrained by its own adjacent column. Writing v_t for column9, the rule is

    w_(t+1) = q_t[7] XOR(w_t OR v_t).

If w_t=1, the next w bit is forced to NOT q_t[7]. If w_t=0, it fixes v_t=q_t[7] XOR w_(t+1). This includes the join between successive input words; matching q_14 alone is insufficient. A physical14-tick cone of initial width21 fixes the entire word and endpoint. Two blocks use one width35 cone, with a shared intermediate row; never two fresh exteriors.

These are hand specializations of the local rule and finite speed, PROOF-SKETCH pending carrying read. No autonomous seven-bit process or universal capture assertion.

## Prediction and counterfactual, before execution

1. Enumerate exactly3×2^14 finite trunk/input pairs, retaining the whole input word. Record the accepted A→A and A→gap3 transfer by endpoint and the first adjacent-column failure. Prediction: both endpoint types occur, but the adjacent-column condition removes many free input words. Counterfactual: one branch is absent, or every word already satisfies that condition. Both would sharpen the transfer.
2. Six bounded SAT queries use the actual21-cell cone, one per initial prefix and endpoint type. Prediction: both branches have physical witnesses for the same seven-cell start. Each SAT model is replayed against every cone cell and with a scalar-cell oracle; input words are independently extracted and replayed through the trunk. Negative/UNKNOWN solver answers have no certified exclusion status.
3. A coupled witness query changes exactly one initial cell beyond cell7, preserving the start and A heads while changing the endpoint from00 to11. Prediction: such a sensitive incoming-history witness exists. Failure stays recorded without increasing the budget.
4. Unexpected splice control: two separately physical A-blocks agree on seven seam cells, but violate column8's forced update at the join. Prediction: a witness exists with the last left input bit1; no right-tail choice can repair that particular join. This explains which history a composition must preserve.
5. One actual width35 cone supplies two successive A-blocks followed by a candidate gap3. Prediction: a joint witness exists. Keep the shared row and all column traces. This is an odd-start finite history, not an anchored E A^4 E A^7 E witness or infinite return.

Every SAT query has10000-conflict limit; nine queries total. No retry, automatic new width/horizon, larger graph, seed census or full-cone SAT revival. No symbolic Boolean minimizer is used; Wolfram remains Local's tool. The finite labelled transfer is Python exact simulation; existence queries use CaDiCaL195, the best available tool per TOOLS. Hand predicates and two encodings/oracles provide the controls. A solver answer without a checked proof remains COMPUTED.

**Record searched:** GC2714 and its source; G236 (history-bearing four-gap image obstruction, different guard/word); GC2706/GC2709; exact Rule30ControlledResponse.step/run_sound and the known corridor facts at kit9d837cd5e5ac447cd868c20aebf49a1b4cfa866e. Literal record search gives our branch notes and G236; kit/portal/open-PR index for A-block, branch pair, incoming history gives no match. Last complete index checkpoint2026-11-06T22:24:21Z. Prior primary-literature search/read of Rowland's Local Nested Structure in Rule30 is background; this block specializes the known rule, with no novelty/submission claim. Two overly broad record regex searches were stopped and replaced by this literal lookup before the research run.

## Frozen resource limits

One serial worker, nice10. stage.py worker-stop60 aggregateCPU; child55CPU/160wall; outer65CPU/180wall. RSS8192MiB; swap growth4096MiB; launch free+inactive4096MiB; running floor1024MiB; maximum6 processes,16MiB/file,128MiB/stage. run_capped.py tracks the tree and pressure/output stops; stage.py sums supervisor/reaped children and samples live CPU. Report outer supervisor cost too. Monitor/thermal/pressure failure stops the job; no enlargement/retry.

Intel preflight23:10Z: load3.14/2.08/1.92, free+inactive about6005MiB, swap783.25MiB, speed/scheduler100. No other research job. Sources:

| Source | SHA256 |
|---|---|
| tests/probes/swarm/sw02/block3/a_block_history.py | 7fea378a7ba598cedaceaae3f211871451b6b55a96656b0b4983d2e581354847 |
| tests/probes/swarm/sw02/block3/intel_worker.py | 2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94 |
| tests/probes/metal_scope/stage.py | ba9696782abbee65ffcd3433e78848f1de82647a4f8033ab1e6a5c6cbdaaa09a |
| tests/probes/wolfram/run_capped.py | 26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b |

## First result and a separately justified follow-up freeze — GC2717

COMPUTED: the free-word table has6672 accepted records, all from initial prefix64. Prefixes32 and96 cannot supply A followed by either gap2 or3, even with arbitrary column8 words. From64, raw word counts are3712 (next A) and2960 (next gap3); the column8/9 necessary consistency leaves231 and130. Physical21-cell SAT witnesses exist for both from64 (roots64 and2097088), independently checked. The prediction that all three source prefixes supply both outcomes is REFUTED. The other three planned witness questions were pinned to32, so all returned UNSAT on that premise; no certified UNSAT claim is used. The finite transfer covers all free inputs and separately explains their empty source. First stage completed,0.620971 accountedCPU seconds including outer supervisor,0.60wall; no running job.

This is new evidence for changing the *source*, with no cone/horizon/conflict increase. The live switch starts at64, not an arbitrary gap2 prefix. Before additional work, freeze this follow-up:

- Enumerate exactly the14 variable initial bits of the **same**21-cell cone with low7=64, to classify all physical incoming words. This changes representation from arbitrary temporal input to its shared initial cells; it is not a new seed/horizon census. Prediction: some of the361 adjacency-compatible words still fail deeper history compatibility; counterfactual: adjacency alone is sufficient on this particular block. All physical words must be in the frozen free table.
- Search that retained exact table for one initial-bit change exchanging endpoints00 and11. Prediction: a witness exists; absence will be recorded without enlargement.
- Two SAT witness queries, each still10000 conflicts, ask the unsafe-splice and genuinely shared-two-block questions at source64. Prediction: both have witnesses. Counterfactuals are retained; no automatic third pass. All models replay all cone cells and a separate scalar oracle.

Follow-up source SHA256 `6f267ef17db8561994a81992b07078b5924fc6bd3c48098bf26adc271d5dc50e`. Original free table SHA256 `acb9ceab098a8ecb3943e95bd470cc0b4691b44702cbde4ed0c248a9254f871d`. stage-stop20 aggregateCPU, child18CPU/65wall, outer24CPU/85wall; unchanged8192RSS/4096swap/4096launch/1024floor/6process/16file/128stage limits. Including the completed first stage, the maximum declared follow-up CPU remains within the original60-second stage allowance. No symbolic Boolean minimizer; exact finite simulation and SAT remain the tools.

Local L1579 arrived during the freeze and was safely merged. Its complete report, including both requested carrying derivations in §5, is read: GC2714 branch selector and repaired S(b) are now PROVED hand/two-party. Its new Theorem N is received as PROOF-SKETCH, with the requested later review still separate from this active block.

## Follow-up result and full-table validation freeze — GC2718

The physical21-cell cone yields17 A-continuation words and13 gap3-launch words, versus231/130 at the first adjacency filter. There are6592/6320 initial-cone assignments respectively. The one-bit switch witness is T=64 versus1088 (cell11), whose incoming words are810 versus4482 and endpoints64 versus56. Their one-tick initial-black parents are63 and991: B1(63)=64, B1(991)=1088. Thus these two witnesses can also be placed in the kit's initial-black drive at odd tick1; the single-bit comparison is at that odd row, not between the two initial roots.

The bad splice now has two separately physical witnesses: left root1825600 with input9256 and end64, right root1602496 with input3357. The join supplies column8=1 where the previous last black input and column7 force0. A genuinely shared two-A cone has root26468218944, words9258 then4482, shared seven-cell state64, final56. These are finite gap25/gap25/gap3 histories; the rest of E remains unchecked.

Before treating all30 words as the exact physical restriction, validate *every* one of the16384 retained assignments using independent Boolean truth columns, rather than integer-row evolution. Prediction: every word/output fibre agrees exactly; counterfactual stops the claimed table. No new inputs, horizons, solver or adaptive search. Validation source SHA256 `bf9a6e3dd84fba5af90ba41773271154d9c82aa6926c9a1da156d8a7df6699f2`; physical table SHA256 `9e78e74cefdc9ab88527c2bfcdb6561dc5c255dc264b9b69ef0b8afbda506b69`. stage-stop8CPU, child6CPU/30wall, outer12CPU/45wall; all prior memory/process/headroom/output/thermal caps unchanged. Combined declared follow-up/validation maxima plus completed pilot remain within the original60CPU ceiling. This is necessary full-table validation of the newly discovered exact restriction, not an enlarged search.

## Outcome — GC2719

**The switch is physically realized through one A-block, with its incoming history retained.** Odd-phase rows64 and1088 differ only at cell11, agree on the first ten cells, and both supply A=25. After14 ticks their preceding-pulse branch pairs are respectively00 and11. Their incoming column8 words differ; neither was replaced by an independently chosen word during the evolution. The exact physical input-word restriction is now small enough to state explicitly.

**Status:** COMPUTED exact finite tables, with every assignment checked by a second encoding. SAT witnesses pass all cone cells and a scalar-cell oracle. Generic trunk/word composition and locality arguments are known-rule specializations, PROOF-SKETCH pending Local's scoped carry. GC2714's branch interpretation is now PROVED hand/two-party by L1579. There is no full-E completion or4,7 return conclusion.

### The complete one-block input condition

For an odd-phase row T followed by a black pulse R=F(T), assume the first gap is2. The carried branch rule leaves T mod128 in {32,64,96}. If A=25 is followed by another gap2 or3, the exact free-input transfer forces

    T mod128 = 64.

This restriction comes from all3×2^14 trunk/input pairs, not a sampled list of physical seeds. Prefixes32 and96 have no accepted word even when column8 is free. The additional diagnostic queries at32 therefore failed their registered prediction; changing to64 was justified and separately frozen before the follow-up. No negative SAT answer is being used as a certified exclusion.

Set w=Σ_(t=0)^13 column8(t)·2^t, with T at relative time0. For a physical right half starting with low7=64, **A followed by gap3 holds exactly when**

    w ∈ {3357,4482,4498,4520,4521,4522,8797,
          9618,9640,9641,9642,14429,14941}.

These are thirteen entire14-tick words, not thirteen freely selectable bits. Their seven-cell endpoints are56,88 or120, all having branch pair11. They launch the first gap3 of a candidate E; they do not certify its remaining `3535555`.

There are seventeen physical words giving A followed by gap2. Nine return the preceding-pulse prefix to64:

    {808,809,810,1064,1065,1066,9256,9257,9258}.

The other eight end at32 or96. They are valid finite histories, but cannot continue with a further A and then another gap2/3. Consequently an indefinitely coded X history uses the nine continuing words until it selects one of the thirteen launch words, subject to all higher-column and cross-block constraints. This is a necessary input description, not an independent-choice grammar or realization theorem.

| Initial prefix64 | Next gap2 | Next gap3 |
|---|---:|---:|
| Trunk words before physical compatibility | 3712 | 2960 |
| Pass column8's immediate consistency with column7 | 231 | 130 |
| Realized by an actual21-cell initial cone | 17 | 13 |
| Initial-cone assignments in these fibres | 6592 | 6320 |

The independent Boolean-column program compares **all16384 assignments** of the14 unknown initial cells8–21 with the retained word/output fibres. It verifies all12912 accepted assignments, every exact fibre and that no accepted assignment is omitted. Cells beyond21 cannot affect the14-bit input word or seven-cell endpoint, so zero extension supplies finite witnesses for each listed word; the same finite projection applies to arbitrary farther tails. This does not supply earlier anchored ancestry or an infinite compatible extension.

### A one-bit switch with full physical histories

| Odd starting row | Changed cell | Incoming word, earliest bit first | Endpoint at14 | Next gap after A |
|---|---:|---|---:|---:|
| 64 | — | `01010100110000` (810) | 64, pair00 | 2 |
| 1088 | 11 | `01000001100010` (4482) | 56, pair11 | 3 |

The incoming words first differ at time3 and also differ at5,7,9,12. Thus an initial bit farther right changes the delivered input history before changing the branch decision. Both rows have actual one-tick initial-black parents: B1(63)=64 and B1(991)=1088. In the kit's initial-black convention they occur at odd tick1, A starts at3 and ends at17, and the next black is at21 or23. The single-bit comparison is between the odd rows, not between their initial parents. Earlier complete E excursions are not imposed in this comparison.

### An explicit bad splice and a genuinely shared composition

Two independently replayed physical blocks give this counterexample to joining on seven cells alone:

- Left odd row1825600, input word9256, ends with low7=64.
- Right odd row1602496, input word3357, starts with low7=64 and ends at120.

At the last left time13, column8 is1 and column7 is1. The rule therefore forces column8 at the join to0. The right block supplies1. No choice of column9 repairs that join. Each block is separately physical; the contradiction is in their combined incoming history. This is the concrete information lost by an endpoint-only composition.

By contrast, one width35 initial cone with odd row26468218944 gives words9258 then4482. The first block ends in the **same actual row** used by the second; the seven-cell boundary is64 and the last endpoint56. Every cone cell and an independent scalar replay agree. Its gap prefix is2,5,2,5,3. This is a positive finite composition with a genuine switch after two A-blocks, not a full excursion or periodic orbit.

The general guard is exact: across the join, and at every internal time, w_t=1 forces w_(t+1)=NOT column7(t); w_t=0 fixes column9(t)=column7(t) XOR w_(t+1). The resulting column9 word must itself obey its entire update against columns8 and10. Preserving only the immediate condition leaves361 words where the complete one-block physical history allows30. Applying the same reasoning to the whole concatenated word retains its cross-block ancestry; choosing a new right exterior for each block does not.

### Evidence, limits and next work

All three stages completed. Total **1.825472 accounted CPU seconds**, including each outer supervisor; outer wall totals2.27s. Maximum worker rusage RSS26,423,296 bytes; maximum sampled tree RSS41,000KiB and3 processes; minimum recorded launch/running headroom6038MiB, zero observed swap growth, thermal checks pass. The final short validation finished before a meaningful RSS sample; its zero sampled peak is not a usage measurement. No job remains.

Evidence: `cited/gpt/gc2719-a-block-history-20261106.tar.gz`,88,409 bytes, SHA256 `b1bf8dd88d0f315b3b8d8bd9a8e5190606e95629b8aa7bd5196baeef13635c87`. Source versions from both freezes, complete labelled/physical tables, all positive/negative solver receipts, independent validation, plans, normalized resource receipts and original raw-receipt hashes are retained. TLS/raw-body transfer and exact readback verified. No Lean build or external verification is claimed.

**Carrying request, Local:** check the14-tick trunk phase/endpoint convention, the column8 join equation and its limited scope, and the21-cell cone argument extending the exact table to arbitrary farther tails. Computed tables are separately labelled. L1579's branch/S(b) carries are adopted; its new Theorem N is received with its own pending review, not promoted by this block.

**Next executable step:** use the thirteen physical gap3-launch words as fixed input candidates and require the remaining E word on the same retained history. Determine which launch fibres survive; preserve their initial-cell witnesses and full incoming words. Freeze that separately before any run. A whole E and the earlier E A^4 past are still missing. The current block answers the requested A transport and supplies a positive two-A composition; the full4,7 query remains open.

**Cold:** prefix-only reset arguments and more blind full-cone SAT. Reopen only with a constructive candidate or stronger history relation. **Independent alternative:** the phase-guarded one-cycle lift described by Cloud, with the temporal and finite-tail distinctions in GC2711.

**My own pull:** which of the thirteen launch fibres can pay for the rest of E while retaining its actual incoming history?
