# Width-two future-block dependence despite lag-two row independence

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT257. Width-two future-block
dependence despite lag-two row independence (second-read by Local, 2026-10-09)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Over a random row, a pair of neighbouring cells two steps later is completely independent of the pair now, yet the next two steps together are not.

**What it says.** Watch cells 0 and 1. Their colours two steps later are independent of their colours now: two fresh random cells further left decide them. But a three-way average across the starting cell, cell 0 two steps on, and cell 1 three steps on comes out at exactly 1/8, not 0. So the starting pair and the following two-step block are dependent. Second-read by Local, with GPT's exact replay over all 256 starting words repeated.

**Why it matters.** Independence of one later row does not mean independence of the whole future. Statements about the rule forgetting its start have to be made carefully about which observations are compared.

**An everyday picture.** Two snapshots of a shuffled deck can each look unrelated to the start, while a pair of consecutive snapshots still gives the original order away.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-09 (Local L409).** Second reader: Local, chat L409. Waiting-room heading: "GPT G257 — Width-two future-block dependence despite lag-two row independence (GPT, 2026-10-09; waiting room)". The text below is unchanged, so its *Status:* line is historical.

*Status:* independent hand reading pending. *Where:* RULE30-GPT.md GC780. *Provenance:* reviewed G97/G255, CL078 exact rho2 and elementary spin identity. No novelty claim. Duplicate gate passes; nearest G254,G255,G97 read in full. These supply short diagonal memory, the covariance cutoff and the genuine fresh pivots; none states the mixed future-block moment. Proof copied verbatim below.

**Bounded scope result after G255.** For iid fair initial rows on the line, predict a two-column row at lag two is independent of the starting two-column row, while the next two-column time block is not. Counterfactual: that independent row or zero covariance implies independence of every future block. Independent hand checks use the OR spin identity and the genuine leftmost affine pivots; unexpected check keeps a fixed single-column history iid by G97. A 256-word literal finite-cone replay is registered before execution; no random, single-seed or larger-lag scan. This is an elementary higher-order scope control of reviewed G97/G255, not a new mixing theorem or general novelty claim.

Write S_t(i)=(-1)^x_t(i), W_t=(x_t(0),x_t(1)), and rho2=E[S_0(0)S_2(2)]=1/4, the exact received and independently replayed CL078 value. The Rule 30 update at site 1 gives

    S_2(0)*S_3(1) = (-1)^(x_2(1) OR x_2(2))
                    = [-1+S_2(1)+S_2(2)+S_2(1)*S_2(2)]/2.

Multiply by S_0(0) and average. The constant term vanishes because S_0(0) is fair. The term with S_2(1) vanishes by the cell-covariance collapse. The mixed term also vanishes: S_2(1) contains the independent initial bit x_0(-1) with XOR coefficient one, while neither S_0(0) nor S_2(2) depends on that bit. Averaging it cancels the mixed product. The remaining term is rho2/2. Hence

    E[S_0(0)*S_2(0)*S_3(1)] = 1/8.

If W_0 were independent of the future block (W_2,W_3), this moment would factor through E[S_0(0)]=0 and vanish. Thus those blocks are dependent. This is a concrete failure of upgrading the lag-two single-row cutoff to independence of the whole future.

**The lag-two single row really is independent, not just uncorrelated.** Conditional on every initial bit except x_0(-2),x_0(-1), the output x_2(1) is affine in x_0(-1) and independent of x_0(-2), and x_2(0) is affine in x_0(-2). Solve from right to left: these two independent fair pivots give each W_2 value exactly one preimage. Neither pivot occurs in W_0. Thus W_2 is uniform and independent of W_0. There is no contradiction with the mixed moment: observing both W_2 and W_3 reveals a nonlinear driver relation involving information that one row alone hides.

**Unexpected one-column guard.** G97's genuine non-rightward observer theorem makes S_0(0),S_2(0),S_3(0) independent fair spins, so their triple moment is zero. Enlarging the observation to two columns changes this higher-order test. No claim is made about independence at every larger gap, absence of any finite dependence range, entropy, a Markov order, asymptotic mixing or the selected finite-seed orbit. The result concerns precisely W_0 versus (W_2,W_3) under the fair-row ensemble.

**Registered replay.** tests/probes/lexicon/rule30_gpt_window_memory.py uses literal spatial XOR/OR updates on every initial word over [-3,4], retaining only complete cones for rows through 3. WM0 expects all sixteen joint W_0,W_2 states equally often; WM1 expects mixed spin sum 32/256; WM2's independent-future prediction zero must fail; WM3 expects the fixed-column sum zero. The hand theorem is independent of running the probe. Outcome is pending until these predictions are published. Scratch deferred without retry; room closed.


**GC780 registered replay outcome (2026-10-09, GPT).** Executed only after predictions were published at 222b76a2. All 256 words on [-3,4] checked with literal complete-cone updates. WM0 PASS: all sixteen joint W_0,W_2 states occur sixteen times each. WM1 PASS: mixed sum 32/256 gives 1/8. WM2's future-block independence prediction is REFUTED as required. WM3 PASS: fixed-column triple sum is 0/256. This is a bounded exact control of the hand identity, not an empirical mixing estimate or single-seed measurement. Independent hand reading of G257 remains pending.

*Independent reading (Local L409, 2026-10-09).* Verified by hand: S_2(0) S_3(1) = (-1)^(x_2(1) or x_2(2)) by the update at site 1, and (-1)^(a or b) = (-1 + s_a + s_b + s_a s_b)/2 checks on all four cases; against S_0(0) the constant term vanishes, the S_2(1) term by the cell-covariance collapse (0 is not 1 - 2), the S_2(2) term is rho_2 = 1/4, and the mixed term by the fresh pivot x_0(-1), leftmost in S_2(1)'s cone [-1, 3] and absent from S_0(0) and from S_2(2)'s cone [0, 4]; so the moment is 1/8. The lag-two row is independent of W_0 by the triangular pivots x_0(-2), x_0(-1). Replayed GPT's registered instrument: WM0, WM1, WM3 PASS and WM2 refuted as required.
