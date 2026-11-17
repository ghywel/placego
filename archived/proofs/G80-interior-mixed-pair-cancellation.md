# interior mixed-pair cancellation

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT80. interior mixed-pair cancellation
(second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

When a Collatz number has room to spare, an odd-even pair and an even-odd pair cancel to first order.

**What it says.** Follow one number for two steps, when its count of odd steps is comfortably above the survival
boundary. Its two signed contributions to G74's sum add up to a small "second difference": the first-order parts
cancel exactly, whichever order the odd and even steps come in. Near the boundary the cancellation fails, and an
example shows why.

**Why it matters.** It is a structural reason for the cancellations seen in the data, and a first step on the route
G77 and G78 left open.

**An everyday picture.** On a gentle hill, a step up then a step down, or down then up, leaves you at almost the
same height; the little left over comes from the hill's curve. Against a wall one of the steps is blocked, and the
cancelling fails.

## The formal statement and proof

### G80. Interior mixed pairs cancel the first backward difference (2026-10-06)

G76's opposite-sign contributions sometimes cancel for a structural reason. Fix final T and two consecutive steps from t to t+2<=T. Consider one actual input still coefficient-admitted at time t, with a odd steps, and assume

    a>=ell_(t+1).

This means both choices of the first bit would pass the intermediate barrier. Since ell increases by at most1 per step, either mixed pair01 or10 also passes the endpoint barrier with a+1 ones. This statement concerns coefficient admission only, not actual survival relative to the original input.

Write F(j)=f_(t+2)(j), with the same killed-state extension as G74. Two backward fair steps give

    f_t(a)=(F(a)+2*F(a+1)+F(a+2))/4.

Indeed both intermediate states a and a+1 are admitted, so their first-step recursions apply. For either actual mixed pair, the sum of that input's two signed G74 contributions is therefore exactly

    F(a+1)-f_t(a)
      =(2*F(a+1)-F(a)-F(a+2))/4.

The first differences have cancelled, leaving a second difference. The result is independent of which mixed order the actual orbit takes. No bijection between actual01 and10 inputs, swapped orbit realization or equality of their terminal integers is asserted. It is cancellation between times along one actual input, using the coin completion potential.

**Exact block accounting.** Partition the paid tail into disjoint two-step blocks starting at m,m+2,..., leaving one final step if needed. For each alive input in a block, use the displayed curvature contribution only when it has a mixed pair and the intermediate condition holds. Every other case uses its literal potential change f_(t+2)(a_after)-f_t(a_before), with endpoint potential0 if the input dies during the block. Sum over inputs alive at the block's start. Intermediate cancellations telescope, giving C_w(T)-Q_w(T) exactly after adding the possible last step. This does not bound the number or mass of mixed blocks, the curvature, or the remaining00/11 and boundary terms. G42's Fourier resonance and G44's information guards remain intact; no generic contraction claim follows.

**Unexpected barrier guard.** At width2,m1,t1,a1,T3, the start3 has current5 and actual pair10, finishing at8 with a2. It passes both actual steps. But ell_2=2>a1, so alternative01 is killed immediately. Here f_1(1)=1/2 and f_3(2)=1, giving literal contribution1/2. The unjustified curvature formula instead gives(2*1-0-1)/4=1/4. A mixed endpoint alone does not license the two-step fair recursion at its inadmissible intermediate state.

**Recorded interior example.** Width3,T5,start7 has at t2 the actual pair10, a2 and ell_3=2. G76 records its two contributions+1/4,-1/4. Here F(2)=0,F(3)=1/2,F(4)=1, so the curvature contribution is0, explaining this exact cancellation without an independence assumption.

**Next controls, preregistered NOT RUN.** MP1: reuse widths2..10,T=m..24 and direct states, verify the curvature identity on every interior mixed block, retaining all boundary mixed blocks separately. MP2: verify disjoint block accounting against the independent final count/coin difference for all180 cases, including inputs killed inside blocks, empty ensembles and odd tail lengths. Predict exact equality; make no mixed-block frequency or curvature-size prediction. Independently evolve both guards and require interior0 and boundary1/2 versus invalid1/4. Counterfactual: the curvature formula applies to every mixed block; must fail on the boundary guard. No larger population or Local job. Independent Local reading requested. This is an elementary two-step application of G74's backward equation, not a new asymptotic cancellation theorem.


### G80 controls outcome (2026-10-06)

MP1 passes2925 interior mixed-block curvature identities in the existing width2..10,T=m..24 scope. All257 surviving boundary mixed blocks are retained separately. MP2's disjoint block accounting matches independent direct final count minus coin benchmark in all180 cases, including753 block inputs killed during their block,88 odd tail lengths and57 empty final ensembles. These repeated block counts are instrument controls, not estimates of an asymptotic mixed-block frequency. The two independently evolved guards pass: interior contribution0, boundary contribution1/2 versus unjustified curvature1/4. The unexpected unrestricted-curvature counterfactual is refuted.

Probe: `tests/probes/prizes/collatz_gpt_mixed_curvature.py`; predictions ata4645cf, GPT's Intel host, Python, under1 s. No control failed. The exact local cancellation and block identity remain pending independent reading; no bound on total curvature, boundary mass or equal-bit blocks is established. No larger actual population or Local job was run.
