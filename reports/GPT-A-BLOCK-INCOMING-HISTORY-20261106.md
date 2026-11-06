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
