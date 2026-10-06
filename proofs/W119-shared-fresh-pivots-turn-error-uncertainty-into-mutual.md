# Shared fresh pivots turn error uncertainty into mutual-information increments

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G119. Shared fresh pivots turn
error uncertainty into mutual-information increments (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A common fresh bit ties new shared information to next-error uncertainty.

**What it says.** On a predetermined nonrightward path in the fair right-reading model,MI grows by1-H(next error|paired past) bits per sample.

**Why it matters.** This connects hidden-error uncertainty to unconditional information growth without assuming error closure. Two iid marginal traces alone do not suffice:cross-copy reuse gives a two-bit increment. GF0-GF2 NOT RUN;review pending. No asymptotic rate.

**An everyday picture.** A new common bit shares what an uncertain discrepancy leaves visible.

## The formal statement and proof

**Status:** general right-reading fair-ensemble identity; GF0-GF2 preregistered NOT RUN, independent review pending. Uses G107-G108's fresh-pivot property and ordinary entropy chain rule, not a new general information theorem.

Start ideal and right-reading noisy Rule30 copies from the same infinite iid fair row. The entire terminating right-reading flag field is independent of the initial row; temporal flag dependence is allowed. Observe both on a predetermined nonrightward path p_t. Put K_t=(I_t,J_t),E_t=I_t XOR J_t and M_t=MI(I0..It;J0..Jt), with empty-prefix M_-1=0. Then

    M_t-M_(t-1)=1-H(E_t | K0,...,K_(t-1)),
    M_T=(T+1)-sum_(t=0..T) H(E_t | paired past).

Each increment is between0 and1 bit;M_0=1 since the initial copies agree. No limit or entropy rate is asserted.

**Proof of the required conditional freshness.** The initial pivot index L_t=p_t-t strictly decreases. By G107-G108, both samples have form X_(L_t) XOR u_t and X_(L_t) XOR v_t, where u_t,v_t depend only on initial bits strictly to the right of L_t and the independent flag field. All prior paired samples also depend only on those higher initial bits and flags. The shared pivot remains a fresh fair bit even after conditioning on the whole paired past and E_t=u_t XOR v_t. Hence each current marginal sample is fair independent of that conditioned information, and

    H(I_t,J_t | paired past)=H(I_t,E_t | paired past)=1+H(E_t | paired past).

Each separate trace is iid fair, so extending each marginal prefix adds1 bit of entropy. Extending the joint prefix adds the displayed1+conditional-error term. Subtracting joint entropy from the sum of marginal entropies proves the increment identity;telescoping proves the total. This argument establishes unconditional information growth, unlike G108's result conditioned on the entire environment.

The relevant property is a common unused pivot relative to the paired history, not merely two iid marginal traces. Adaptive paths, reused finite-ring pivots, state-dependent flags and nonterminating right chains are outside the proof. Biased initial rows do not supply the fair-bit baseline. This gives no closure of the error history and no asymptotic information rate.

**GF0-GF2 preregistered NOT RUN.** Use two independent small finite controls, not another Rule30 production run. GF0-GF1 positive control:three fair pivots X0,X1,X2 and two fair hidden bits U,V, R=U*V;I=(X0,X1,X2),J=(X0,X1 XOR R,X2 XOR(R*X0)). All32 histories have equal weight. Predict both marginal prefixes uniform,MI prefixes1,2-h2(1/4),3-h2(1/4),and next-error conditional entropies0,h2(1/4),0. Independently compare integer joint/marginal entropy spectra with conditional-error groups, tolerance1e-12 only for logs.

GF2, unexpected cross-copy-reuse guard:all8 fair triples X,Y,Z with I=(X,Y,Z),J=(X,Z,Y). Both marginals are iid and initial samples agree, butMI prefixes are1,1,3;the last increment is2 while the last error is known from the paired past. The formula would predict1 there and must fail. This counterexample refutes extending the identity from marginal iid laws alone. Publish before execution. It is a scope control, not a Rule30 counterexample.
