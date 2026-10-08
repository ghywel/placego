# the first two source columns miss black0101 samples

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT216. the first two source
columns miss black0101 samples (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The two nearest nonlinear source columns cannot supply a black0101 wall sample.

**What it says.** Their allowed activation times have the wrong parity to affect odd centre times. Together with G215's left-source exclusion, a required event must begin at site2 or farther right.

**Why it matters.** It sharpens spatial necessity term by term. The sources can still activate at times when they are invisible to that observation. A finite seed gives a site2 contribution, so the same local argument cannot discard that site.

**An everyday picture.** A signal can be present but miss the observation's timing. The nearest signals miss; a farther signal can arrive.

## The formal statement and proof

**Where:** RULE30-GPT.md GC422 at83b71ef; claim, proof and finite guards copied verbatim below. Local L252 in978f1c3 checks the new parity step and every example row; L253 in401eba2 verifies the G215 dependency. The necessary finite-row event uses G214-G215. No infinite clock witness is supplied.

Combining G27,G62 and GC420 gives a sharper spatial necessary condition, without another search. In any full Rule210 orbit with centre0101 from time0, the nonlinear contribution to every odd centre sample has no terms from source sites i<=1. For a finite seed, GC420's dyadic block therefore requires a selected active source at i>=2, with t+i even and i<=T-1-t for the chosen odd T. This does not say the first two sources are inactive.

**Proof.** G27 eliminates V_t(i) for i<0. At i=0, V_t(0)=tau(t)*x_t(1) can be nonzero only at odd t, since tau is0 at even times. At i=1, G62 proves V_t(1)=0 at odd t, so its activity is confined to even t. The Pascal coefficient for an odd target T requires t+i even. It therefore selects even t at i=0 and odd t at i=1, precisely the forbidden temporal parities. These two sources vanish term by term in the odd-time Duhamel sum. No cancellation assumption is used. GC420 then restricts its required event to i>=2.

**Independent local truth-table control and retained counterfactual.** The attempted extension eliminating i=2 fails. Start from the finite seed{1,2,3}, with wall0 and empty left side, so the positive five-cell patch is11100. Literal Rule210 bits at patterns011,111,110 give respectively0,1,1 for columns1,2,3 after one update. Direct scalar truth-table evolution gives occupied sets

    time0: {1,2,3}
    time1: {0,2,3,4}
    time2: {-1,3,4,5}
    time3: {-2,0,2,4,5,6}.

Thus the centre prefix is0101. The source at time0,site2 is active and has coefficient K_2(2)=1 for target T=3. The homogeneous Rule90 centre at time3 is0: seed sites1 and3 have binomial coefficients3 and1, which cancel modulo2. Other selected source terms are absent in these three updates, so this source supplies the black time3. This is a hand evaluation of four finite rows, not a computational run or a claim that the clock continues forever. It refutes only a local extension to i>=3; infinite compatibility may impose more constraints.

**Unexpected guard: invisible does not mean absent.** The same initial seed has V_0(1)=1, yet K_2(1)=0. Its first pair really activates and is invisible to the odd time3 centre. This separates the new causal statement from G62's allowed timing and prevents replacing it with a claim that the near-wall dynamics are linear.

**Duplicate guard for G216:** nearest G215,G214,G65 read in full. G215 supplies the cone and left-source exclusion, G214 the required event, and G65 a parity-sparse infinite mirror realization. This entry removes source columns0 and1 termwise at black sample times; it does not construct a finite realization.
